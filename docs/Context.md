# [◀](./index.html) [Context](/jsonpack/util.py)

## Example Code
```py
ctx = jsonpack.Context(node, module, **extras)
```

## Arguments

| Argument | Description |
|--|--|
|node|The node that this context came from.|
|module|The module that this context came from.|
|extras|Extra arguments to pass.|

## Methods

- .add_extras(**kw)<br>Extra arguments to pass.
- .copy()<br>Creates a copy of this class.
- .from_dict(data)<br>Converts a :class:`dict` to a :class:`Context`.
- .to_dict()<br>Converts a :class:`Context` to a :class:`dict.`