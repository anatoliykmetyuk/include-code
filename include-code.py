#!/usr/bin/env python

"""
Pandoc filter to import code from some directory.
"""

import os
import sys
from subprocess import Popen, PIPE, call

from pandocfilters import *


def log(txt):
  out = open("./include-code.log","a")
  out.write(txt + '\n')
  out.flush()
  out.close()

def read_snippet(file, snippet_name, dedent = 3):
  f = open(file, 'r')
  lines = []
  start_from = None
  for l in f:
    if 'end snippet ' + snippet_name in l: start_from = None
    
    if start_from: lines.append(l[start_from-dedent:])
    
    idx = l.find('start snippet ' + snippet_name)
    if idx >= 0: start_from = idx

  f.close()
  return ''.join(lines)

def to_dict(keyvals):
  res = {}
  for [k, v] in keyvals: res[k] = v
  return res

def include_code(key, value, fmt, meta):
  if key == 'CodeBlock':
    [[ident, classes, keyvals], code] = value
    kvs = to_dict(keyvals)
    include = kvs.get("include")
    snippet = kvs.get("snippet")

    if include and snippet:
      src = read_snippet(include, snippet)
      return CodeBlock([ident, classes, keyvals], src)

if __name__ == "__main__":
  toJSONFilter(include_code)