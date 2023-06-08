# [◀](../index.html) Creating Pack
First, you will need to create a folder in your packs folder that was generated when you ran your app for the first time. See [Getting Started](./getting_started) for more. This folder will contain all files for your pack. The name of the folder doesn't matter however it's useful to make it match the name of your pack.

## Manifest
Now in the folder that you created, create a new file called `manifest.json`. Syntax should match what is defined in [manifest.json](../manifest_json) This file is used to configure and validate your pack.
```json
{
    "name": "Example",
    "description": "An example pack",
    "uuid": "554a79db-2e7a-43bf-95be-d9f0b5209360",
    "version": [1, 0, 0],
    "modules": [
        // Built-in module for loading scripts
        {
            "version": [1, 0, 0],
            "type": "script",
            "uuid": "7db3a4d8-00e0-4362-9e83-331f8627a962",

            // This file is where you should place all your code from Creating Modules and Creating Nodes
            "path": "./scripts/main.py"
        },

        // `data` module defined in Creating Modules
        {
            "version": [1, 0, 0],
            "type": "data",
            "uuid": "dc72d95d-72ee-4148-9825-a50a7d889c65"
        },

        // `resources` module defined in Creating Modules
        {
            "version": [1, 0, 0],
            "type": "resources",
            "uuid": "dc72d95d-72ee-4148-9825-a50a7d889c65"
        }
    ]
}
```

## Icon
You can add your own pack icon by placing it in the same folder as the manifest.json file that you created and rename the image to `pack_icon.png`.

## Nodes
Now that you've created a manifest file you can add nodes to your pack to configure your app. Below you can find an example of the nodes created in [Creating Nodes](./creating_nodes)

### Images
1. Create a folder in your pack called `assets`. This directory will contain all client-side nodes
2. Now create a folder called `images`. This folder is where you can place any PNG image to load it in your app.


### Item
1. Create a folder in your pack called `data`. This directory will contain all server-side nodes.
2. Now create a folder called `items`. This folder will contain JSON files containing configureation for items to use in your app.
3. Create a JSON file named `test.json` which contains the following JSON:
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

