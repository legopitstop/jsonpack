# [◀](./index.html) [Manifest.json](/jsonpack/__init__.py)

## Example
```json
{
    "name": "Example",
    "description": "An example pack",
    "uuid": "554a79db-2e7a-43bf-95be-d9f0b5209360",
    "version": [1, 0, 0],
    "modules": [
        {
            "version": [1,0,0],
            "type": "script",
            "uuid": "7db3a4d8-00e0-4362-9e83-331f8627a962",
            "path": "./scripts/main.py"
        }
    ],
    "dependencies": [
        {
            "uuid": "0a132a92-6bc3-4190-8a99-a492083d4c8e",
            "min_version": [1, 0, 0]
        }
    ]
}
```

## Syntax
| Name | Type | Required | Description |
|--|--|--|--|
| `name` | string | Yes | Name of your pack. |
| `description` | string | Yes | A short description of what your pack does. |
| `uuid` | string | Yes | The unique ID of your pack. |
| `version` | array | Yes | The version of your pack in [major, minor, patch] format.|
| `module`| [Module](#module) | Yes | A list of modules that your pack uses.|
|`dependencies`| [Dependency](#dependency) | Yes | A list of required packs |


## Module
| Name | Type | Required | Description |
|--|--|--|--|
| `version` | array | Yes | The version of this module |
| `type` | [Module Types](#module-types) | Yes | The type of module |
| `uuid` | string | Yes  | The unique ID for this module.  |
| `path` | string | No | If type=script this is the path to the Python file or Python package to load. |

## Module Types

|Name|Description|
|--|--|
|`script`| Built-in module type used to load and run Python files. Scripts are always loaded first before any other Node. |

## Dependency
| Name | Type | Required | Description |
|--|--|--|--|
| `version` | array | Yes | The exact version of this pack that you need. |
| `min_version` | array | No | The minimum version that this you need.  |
| `uuid` | string | Yes  | The unique ID of the required pack.  |
