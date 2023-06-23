# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.2] 6/23/2023
### General
- If decorator like functions are not coroutine functions it will raise TypeError.

### Breaking Changes
- `@mimetype` function will now only pass 1 argument "Context" which then has the old file, node, and subtype arguments.
- `@mimetype` Now has an error method for handling errors.
- Now requires [schemaser](https://pypi.org/project/schemaser/) for converting methods and classes to JSON schema
- removed "script" parameter from .set_path() and replaced it with "permission_level". permission_level is an integer that decribes the level of permission needed for this path.
    - 0 - No scripts. (default)
    - 1 - Will ask user for permission to load the script.
    - 2 - Highest level, can load scripts without asking the user.
- All decorator functions need to be asynchronous.

### New
- You can now get all registered nodes using App.get_item(path, name) or using App[path][name]. "path" being `<module_type>.<node_type>` for example if I wanted all "item" nodes from the "data" module I would use. `App.get_item('data.item')` or `App['data.item']`
- event, component, and node methods now except "description".

### Fixes
- Fixed AttributeError: 'Item' object has no attribute 'event' when triggering an event.

## [0.0.1] 6/14/2023
- Initial release
