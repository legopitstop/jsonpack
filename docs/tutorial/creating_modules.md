# [◀](./getting_started) Creating Modules

Modules are a way to enable server-side and client-side features. Its best to define your modules in a built-in pack this way you can easly reload your modules at runtime.

See [Module](../Module) class for more info.

## Example
```py
import jsonpack

# Define your modules.
# This module will be used to load client-side data (textures, models, etc)
client = jsonpack.Module(namespace='default', module_type='resources')

# This module will be used to load server-side data (items, events, etc)
server = jsonpack.Module(namespace='default', module_type='data')
```

To use your module features in a pack make sure to include your module type in the [manifest.json](../manifest_json) like below.
```json
{
    ...
    "modules": [
        {
            // The module_type that you defined in Module.module_type
            "type": "resources",
            "uuid": "41ece309-0b6a-466c-92c3-ebd830a7af7f",
            "version": [1,0,0]
        }
    ]
}
```

Now that you've setup your modules see [Creating Nodes](./creating_nodes) to learn how to add nodes to your modules.