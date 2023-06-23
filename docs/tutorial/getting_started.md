# [◀](../README) Getting Started

First you must use [App](../App) to configure your app to use jsonpack
```py
import jsonpack
import os

PATH = os.path.dirname(os.path.realpath(__file__))

# Main class for loading all packs
app = jsonpack.App('app')

# Add folders that it should check for packs.
app.add_path(os.path.join(PATH, 'packs'), permission_level=2)

# Load all packs
app.run()
```

When you run your app for the first time it will create all the folders that you defined using `App.add_path()`. These folders are where you place your packs.

Now that you've setup your app see [Creating Modules](./creating_modules) to learn how to customize your packs.