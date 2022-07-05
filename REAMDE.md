# DISCLAIMER: THIS IS STILL FOR TESTING PURPOSES - PLEASE DO NOT USE

# [The SOC Infrastructure Blueprint Repository](#thesocblueprintinfrastructurerepository)

## [Introduction](#introduction)
This is Maternas Ansible Blueprint repository which surfes two purposes:

1. Manage and collect all configurations cross client developed that are necessary for the SIEM in abstraction. In this way the abstract configuration can be used as a blueprint for various customers and use cases.

2. A Shovel Tool that simplifies the deployment of a new customer Elastic Environemnt. It creates a clean configuration in a seperte customer repository within the _SOC Infrastructure_ Project. This way it is not necessary to build the config manualy from scratch - only customer specific changes are required.

If a customer needs a configuration for a Logsoruce that has not been implemented by us yet, the new configuration should be added to the Blueprint Repositiory so it can be reused for other custoemrs as well.

## [Management](#management)

- Roles
- ...
- ...


## [Deployment - The Shovel](#deployment)
This tool automatically generates Ansible configuration for new customers, based on information in the `rules` directory


**Important:** Update this Repository every time before using it! This prevents you from using an old configuration.
```shell
git pull
```

Or if you need to download the Repository:
```shell
git clone https://bitbucket.materna.de/scm/socinfra/abstract.git
```
``shovel.py``

Arguments:
- `--customer` or`-c`
- `--repo` or`-r`

### [Vaults](#vaults)

Password are stored in vault var files. The password is the 'XXXXXXXX' password in the DVTools password manager.
To use the ansible vault automatically, set a password in the file `.vault_password`.
