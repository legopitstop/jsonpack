# [◀](./README) [Node](/jsonpack/node.py)

Helper class used for creating nodes.

## Example Code
```py
module = jsonpack.Module('default', 'data')

@module.node()
class Item(jsonpack.Node):
    ...
```

## Default Arguments

| Argument | Description |
|--|--|
|`__file__`|File path to the file that was loaded.|


## Methods

- .to_dict()<br>Converts a :class:`Node` to a :class:`dict`
- .from_dict(data)<br>Converts a :class:`dict` to a :class:`Node`
- .on_load()<br>Should be overridden. Triggers when this node is loaded.
- .on_unload()<br>Should be overridden. Triggers when this node is unloaded.

## [Componentable](/jsonpack/node.py)

Helper class used for creating nodes with dynamic components.

### Example Code
```py
module = jsonpack.Module('default', 'data')

@module.node()
class Item(jsonpack.Node, jsonpack.Componentable):
    traits = ['components']

@Item.component()
def on_click(ctx:jsonpack.Context):
    pass
```

### Arguments

| Argument | Description |
|--|--|
|components|All components for this node.|

### Methods

- .get_component(name)<br>Returns the component.
- .trigger_component(name, **extra)<br>Returns the result of the component function when called.

## [Eventable](/jsonpack/node.py)

Helper class used for creating nodes with dynamic events.

### Example Code
```py
module = jsonpack.Module('default', 'data')

@module.node()
class Item(jsonpack.Node, jsonpack.Eventable):
    traits = ['events']
```

### Arguments

| Argument | Description |
|--|--|
|events|All events for this node.|

### Methods

- .add_event(name, **kw)<br>Adds an event to the node.
- .remove_event(name)<br>Removes an event at a specified name.
- .clear_events()<br>Removes all events from this node.
- .get_event(name)<br>Get the event from the name.
- .trigger_event(name)<br>Runs this event from the name.

## Imageable
### Example Code
```py
module = jsonpack.Module('default', 'resources')

@module.node()
class Texture(jsonpack.Node):
    traits = ['images']
```

### Arguments

| Argument | Description |
|--|--|
|image|The PIL.ImageFile from the loaded image|
