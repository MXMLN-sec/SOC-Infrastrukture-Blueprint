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


# [Ansible](#ansible)

## [Verifying Playbooks](#verify-playbook)

You may want to verify your playbooks to catch syntax errors and other problems before you run them. The `ansible-playbook` command offers several options for verification, including

  - ``--check`` -
  - ``--diff`` -  
  - ``--list-hosts`` - 
  - ``--list-tasks`` - 
  - ``--syntax-check`` - 

### ansible-lint
You can use `ansible-lint` for detailed, Ansible-specific feedback on your playbooks before you execute them. For example, if you run `ansible-lint` on the playbook called `verify-apache.yaml` you should get the following results:

```shell
$ ansible-lint verify-apache.yml
[403] Package installs should not use latest
verify-apache.yml:8
Task/Handler: ensure apache is at the latest version
```

## [Run Playbooks](#run-playbooks=)

```shell
ansible-playbook -i /path/to/my_inventory_file -u my_connection_user -k /path/to/my_ssh_key -f 3 -T 30 -t my_tag -m /path/to/my_modules -b -K my_playbook.yml
```

Loads ``my_playbook.yml`` from the current working directory and:
  - ``-i`` - uses ``my_inventory_file`` in the path provided for inventory to match the pattern.
  - ``-u`` - connects :ref:`over SSH <connections>` as ``my_connection_user``.
  - ``-k`` - uses ``my_ssh_key`` in the path provided for SSH authentication.
  - ``-f`` - allocates 3 :ref:`forks <playbooks_strategies>`.
  - ``-T`` - sets a 30-second timeout.
  - ``-t`` - runs only tasks marked with the :ref:`tag <tags>` ``my_tag``.
  - ``-m`` - loads :ref:`local modules <developing_locally>` from ``/path/to/my/modules``.
  - ``-b`` - executes with elevated privileges (uses :ref:`become <become>`).
  - ``-K`` - prompts the user for the become password.

other parameters:
- ``--verbose`` - creates detailed output from successful modules as well as unsuccessful ones.