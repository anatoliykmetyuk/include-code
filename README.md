A Pandoc plugin to include code snippets from source files.

# Usage
In markdown code block:
```
{include="./target_file" snippet="snippet_name"}
```

In the target file:

```
...

// snippet start snippet_name
...
// snippet end snippet_name
```
