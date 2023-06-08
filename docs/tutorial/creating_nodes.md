# [◀](./creating_modules) Creating Nodes

Nodes are the files in your pack that adds the configureation to your app.

See [Node](../Node) class for more info.

## Example
```py
import jsonpack
# See Creating Modules for more info
client = jsonpack.Module(namespace='default', module_type='resources')

# Define your node
# This node will load all PNG images as the class Image
@client.node(pathname='/assets/images/**/*.png', mimetype='image/png')
class Image(jsonpack.Node):
    traits = ['images'] # more info below

```

## Traits
Node traits are a way to implement dynamic features to your class like, loading an image and placing it in the `image` attrubute. Adding expandable components and events to your JSON file to make your files customizable!

|Name|Description|
|--|--|
|`components`| Adds [components](./components) to this JSON to create expandable behavior to this node|
|`events`| Adds [events](./events) to this JSON to run any global event|
|`images`| Loads this file as a PIL.ImageFile. Stored in the `image` attrubute|

## Images Trait
Python code:

This code will load any image file in the folder `/packs/*/assets/images/` with the extention 'PNG'.
```py
import jsonpack
module = jsonpack.Module(namespace='app', module_type='resources')

# Define node
@module.node(pathname='/assets/images/**/*.png', mimetype='image/png')
class Images(jsonpack.Node):
    traits = ['images']

    def on_load(self, ctx):
        print(self.image) # Prints the PIL.ImageFile of the loaded image.
```

## Components and Events Trait
Component and Event traits will most likely be used together.

Python code:
```py
import jsonpack
module = jsonpack.Module( namespace='app',module_type='data')

# Define node
@module.node(pathname='/data/items/**/*.json', mimetype='application/json')
class Item(jsonpack.Node, jsonpack.Componentable, jsonpack.Eventable):
    traits = ['components','events'] # Define Traits

    def on_load(self, ctx):
        print(self.events)
        print(self.components)

# Define a component for the node.
@Item.component('on_load')
def on_load(ctx:Context, event:str):
    ctx.item.trigger_event(event) # Runs the event

# Define an event
@module.event('print')
def _print(ctx:Context, text:str):
    print(text)
    
```
The above node will load a JSON file located `/packs/MyPack/data/items/test.json`.
```json
{
    // Any component defined by Item.component()
    "components": {
        "app:on_load": {
            "event": "MyEvent"
        }
    },

    // Define your events
    "events": {
        // Name of the event that will trigger
        "MyEvent": {
            // Any event defined by module.event()
            "print": {
                "text": "Hello World!"
            }
        }
    }
}
```

Now that you've learn how to create nodes you can test everything out by creating your pack. see [Creating Packs](./creating_packs)