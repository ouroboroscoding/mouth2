# mouth2_oc releases

## 2.2.1
- Fixed bug in `POST email` where errors were not returned correctly, potentially causing issues in clients.

## 2.2.0
- Updated [body_oc](https://pypi.org/project/body_oc/) to 2.2.0, a breaking change.
- Updated [brain2_oc](https://pypi.org/project/brain2_oc/) to 2.4.0, a breaking change.

## 2.1.3
- Updated [rest_mysql](https://pypi.org/project/rest_mysql/) to latest.
- Updated [brain2_oc](https://pypi.org/project/brain2_oc/) to latest.
- Stopped hardcoding DB host to **mouth** and now the user can set if via `config.mouth.mysql`.

## 2.1.2
- Fixed a bug in the install process where the wrong module was imported.

## 2.1.1
- Updated LICENSE.
- Updated [body_oc](https://pypi.org/project/body_oc/) to latest.
- Updated [brain2_oc](https://pypi.org/project/brain2_oc/) to latest.

## 2.1.0
- Removed local "definition" files and replaced them with submodule "define" files.
- Updated all `_id` fields to be trimmed UUIDs `tuuid` instead of full, `uuid`. This includes all fields that point to an `_id`.
- Refactored install.py and added upgrade.py to allow them to work when loaded by another project, allowing us to call the install and upgrade process form inside our own install/upgrade scripts without forcing the user to also install/upgrade mouth manually.