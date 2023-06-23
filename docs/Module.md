# [◀](./index.html) [Module](/jsonpack/__init__.py)

Defines a modules nodes when defined in the packs manifest.json.

## Example Code
```py
module = jsonpack.Module(module_type, namespace)
```

## Arguments

| Argument | Description |
|--|--|
|module_type|The type of module this is. example; "data" for server side modules, "resources" is for client side modules.|
|namespace|The namespace used for components. `<namespace>:<component_name>`|

## Methods

- .add_node(cls, pathname, mimetype=None, resourcepath_command=None)<br>Creates a node from a regular class.
- .remove_node(name)<br>Removes a node with the specified name.
- .clear_nodes()<br>Removes all nodes from this module.
- .node(pathname, mimetype=None, resourcepath_command=None)<br>Creates a node from a regular class.
- .add_event(func, name=None)<br>Creates an event from a regular function.
- .remove_event(name)<br>Removes an event with the specified name.
- .clear_events()<br>Removes all events from this module.
- .event(name=None)<br>Creates an event from a regular function.