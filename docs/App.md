#  [◀](./index.html) [App](/jsonpack/__init__.py)

The root app.

## Example Code
```py
app = jsonpack.App(default_namespace='default')
```

## Arguments

| Argument | Description |
|--|--|
|default_namespace|The default namespace for components. if default namespace is "foo" then a component can be defined "foo:bar" or "bar"|
|ui|When true it will use UI's when needed. For example when ui=False a pack contains a script it will ask via console. When ui=True it will use a Tkinter window.|

## Methods

- .add_bind(event, func)<br>Run a function when a certain event triggers.
- .bind(event)<br>Run a function when a certain event triggers.
- .unbind(event)<br>Removes a bind event.
- .call_bind_event(event)<br>Runs the bind event callbacks.
- .get_node(name)<br>Returns with the Node.
- .add_module(module_type, namespace, cls)<br>Adds a module to the app.
- .remove_module(name)<br>Removes a module at a specified name.
- .clear_modules()<br>Removes all modules from this app.
- .add_mimetype(func, type, subtype=None)<br>Adds a mimetype to the app.
- .remove_mimetype(index)<br>Removes a mimetype at a specified index.
- .clear_mimetypes()<br>Removes all scripts from this app.
- .add_script(name, fp)<br>Adds a script to the app.
- .remove_script(name)<br>Removes a script at a specified name.
- .clear_scripts()<br>Removes all scripts from this app.
- .add_path(path, scripts=False)<br>Adds a path to the app.
- .remove_path(index)<br>Removes a path at a specified index.
- .clear_paths()<br>Removes all paths from this app.
- .reload(threaded=True)<br>Reload all packs
- .unload()<br>Unloads all packs.
- .load()<br>Load all packs from the configured paths.<br>WARNING: If you need to reload all packs use App.reload instead!
- .dump_registries(path='')<br>Generates a folder of files that list all loaded registries.
- .run()<br>Runs the app.