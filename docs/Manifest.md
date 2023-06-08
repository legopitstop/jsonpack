# [◀](./README) [Manifest](/jsonpack/__init__.py)

A class used to describe a manifest.json file.

## Example Code
```py
jsonpack.Manifest(name, description, uuid)
```

## Arguments

| Argument | Description |
|--|--|
|name| Name of the pack.|
|description| Description of the pack.|
|uuid| UUID of this pack.|
|scripts|A list of scripts.|
|version|The packs version.|
|path|This packs path.|
|modules|This of modules this pack uses.|
|dependencies|List of pack dependencies.|
|`__file__`|File path to the loaded manifest.json|

## Methods

- .enable_scripts(value)<br>Whether or not this pack can load scripts.
- .set_version(version)<br>Sets the version for the pack.
- .set_path(path)<br>Sets the path for the pack.
- .set_icon(fp)<br>Sets the icon for the pack.
- .add_module(version, type, uuid, path=None)<br>Adds a module to the manifest.
- .remove_module(index)<br>Removes a module at a specified index.
- .clear_modules()<br>Removes all modules from this manifest.
- .add_dependency(uuid, version=None, min_version=None, description=None)<br>Adds a dependency to the manifest.
- .remove_dependency(index)<br>Removes a dependency at a specified index.
- .clear_dependencies()<br>Removes all dependencies from this manifest.
- .from_dict()<br>Converts a :class:`dict` to a :class:`Manifest`
- .to_dict()<br>Converts a :class:`Manifest` to a :class:`dict`
- .schema()<br>This classes JSON schema used for validation when loading the file.
- .join()<br>Joins all paths realitive to this packs path.
