pandoc \
  --filter ../include-code.py \
  -o out.html input.md

open out.html
