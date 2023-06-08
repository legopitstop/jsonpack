# [◀](./README) [mimetype](/jsonpack/__init__.py)

Adds a mimetype to the app.

## Example Code
```py
@jsonpack.mimetype(type, subtype=None)
def mimetype_function(file, node, subtype):
    return node.cls.from_dict(data)
```

## Arguments

| Argument | Description |
|--|--|
|type|The type of mimetype. **type**/subtype|
|subtype|The subtype of mimetype. type/**subtype**|
