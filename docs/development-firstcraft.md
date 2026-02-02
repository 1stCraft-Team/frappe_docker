# Getting Started

## Prerequisites

refer to Prerequisites sections in https://github.com/1stCraft-Team/frappe_docker/blob/firstcraft/docs/development.md#prerequisites

## Bootstrap Containers for development

Clone frappe_docker

```shell
mkdir frappe_docker
cd frappe_docker
git clone https://github.com/1stCraft-Team/frappe_docker.git .
```

Copy example devcontainer config from `devcontainer-example` to `.devcontainer`

```shell
cp -R devcontainer-example .devcontainer
```

Copy example vscode config for devcontainer from `development/vscode-example` to `development/.vscode`. This will setup basic configuration for debugging.

```shell
cp -R development/vscode-example development/.vscode
```

Open In VSCode or Cursor By
```shell
code .
#OR
cursor .
```

Allow Full Permissions
```shell
chmod -R 777 ./development
```

## Use VSCode Remote Containers extension

Make sure to install Dev Container or Remote Container Extension.
https://github.com/1stCraft-Team/frappe_docker/blob/firstcraft/docs/development.md#use-vscode-remote-containers-extension

- Launch the command, from Command Palette (Ctrl + Shift + P) `Dev Containers: Reopen in Container`. You can also click in the bottom left corner to access the remote container menu.

## Get App Json

**Get {project_name}-apps.json from your team and place it alongside apps-example.json**


## Setup bench / new site using script

Init bench, install site, etc. from script.

**Change {frappe version} to your project**
```shell
python install.py {project_name} -t {frappe version}
# example:
python install.py mis -t v15.45.1
```

A new bench and / or site is created for the client with following defaults.

- MariaDB root password: `123`
- Admin password: `123`


## Set Config

Go into Bench folder
```shell
cd frappe-bench-{project_name}
# example:
cd frappe-bench-mis
```

Enable Server script
```shell
bench set-config -g server_script_enabled 1
```

# Install Others Apps

Install Other Apps as required in your project.


## Etc.

Further customization command can be found in https://github.com/1stCraft-Team/frappe_docker/blob/firstcraft/docs/development.md