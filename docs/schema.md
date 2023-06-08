# [◀](./index.html) [schema](/jsonpack/__init__.py)

Creates a jsonschema from a class or function.

## Example Code
```py
jsonpack.schema(node, cls_or_func, traits, child=False, skiparg=-1)
```

## Arguments

| Argument | Description |
|--|--|
|node|The jsonpack._node.|
|cls_or_func|A class or function to create a jsonschema from.|
|traits|A list of traits for this schema. components, events, images.|
|child|Whether or not this is a child event.|
|skiparg|Argument index to skip. (used to skip the first CONTEXT arg for nodes and events)|
