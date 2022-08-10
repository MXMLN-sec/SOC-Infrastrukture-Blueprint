# DISCLAIMER: THIS IS STILL FOR TESTING PURPOSES - PLEASE DO NOT USE

# [The SOC Infrastructure Blueprint Repository](#thesocblueprintinfrastructurerepository)

## [Introduction](#introduction)
This is Maternas Ansible Blueprint repository which surfes two purposes:

1. Manage and collect all configurations cross client developed that are necessary for the SIEM in abstraction. In this way the abstract configuration can be used as a blueprint for various customers and use cases.

2. A Customer Preparation Tool that simplifies the deployment of a new customer Elastic Environemnt. It creates a clean configuration in a seperte customer repository within the *SOC Infrastruktur* Project. This way it is not necessary to build the config manualy from scratch - only customer specific changes are required.

If a customer needs a configuration for a Logsoruce that has not been implemented by us yet, the new configuration should be added to the Blueprint Repositiory so it can be reused for other custoemrs as well.
# [Ansible-Playbook Guide](#ansible-playbook-guire)
## [Preparation to run Ansible-Playbooks with encrypted properties](@preparation-encrypted-playbook)
1. Clone the Repository to the local machine 
2. Create a file in the repository name `.vault_password` 
3. Copy the Password *SOC Infrastruktur Ansible Vault Passwort* from the DVTools Password Manager, Group: *root-SOC-Betrieb.ECE* and store it in the `.vault_password` file
4. Run a Ansible Playbook like so:
   ``` Shell
   ansible-playbook [playbook-role-name].yaml --vault-password-file=.vault_password
   ```

## [Verifying Anyible-Playbooks](#verify-ansible-playbook)
You may want to verify your playbooks to catch syntax errors and other problems before you run them. The `ansible-playbook` command offers several options for verification, including

  - `--check` -
  - `--diff` -  
  - `--list-hosts` - 
  - `--list-tasks` - 
  - `--syntax-check` - 

## [Run Playbooks](#run-playbooks=)
```shell
ansible-playbook -i [/path/to/my_inventory_file] -u  [my_connection_user] -k [/path/to/my_ssh_key] -T [30] -t [my_tag] -m [/path/to/my_modules] -b -K [playbook-role-name].yaml
```

Loads `[playbook-role-name].yaml` from the current working directory and:
  * `-i` - uses `my_inventory_file` in the path provided for inventory to match the pattern
  * `-u` - connects `over SSH <connections>` as `my_connection_user`
  * `-k` - uses `my_ssh_key` in the path provided for SSH authentication
  * `-T` - sets a 30-second timeout
  * `-t` or `--tags`- runs only tasks marked with the tag `my_tag`
  * `-m` - loads `local modules <developing_locally>` from `/path/to/my/modules`
  * `-b` - executes with elevated privileges (uses `become <become>`)
  * `-K` - prompts the user for the become password

other parameters:
- `--verbose` - creates detailed output from successful modules as well as unsuccessful ones.


## [Limit to hosts](@limit-to-hosts)
You can limit the hosts you target on a particular run with the --limit flag.

* Limit to one host
``` Shell
ansible-playbook [playbook-role-name].yaml --limit "host1" 
```

* Limit to multiple hosts
``` Shell
ansible-playbook [playbook-role-name].yaml --limit "host1:host2" 
```

* Exclude host (Note that single quotes MUST be used to prevent bash interpolation)
``` Shell
ansible-playbook [playbook-role-name].yaml --limit 'all:!host1' 
```

* Limit to one host group
``` Shell
ansible-playbook [playbook-role-name].yaml --limit "group1"
```

* Limit to multiple host groups
``` Shell
ansible-playbook [playbook-role-name].yaml --limit "group1:group2"
```

* Limit to intersection of groups (any hosts in group1 that are also in staging)
``` Shell
ansible-playbook [playbook-role-name].yaml --limit 'group1:&staging'
```

* Exclude groups (any hosts in group1 that are not in staging)
``` Shell
ansible-playbook [playbook-role-name].yaml --limit 'group1:!stagingt' 
```

### Aniyble-Playbook failed to run 
* If the `ansible-playbook` run failed, a `~/.ansible-retry/[playbook-role-name].retry` will be created containing a list of the failed hosts. This file is overwritten each time `ansible-playbook` finishes running.

* You can use --limit to read the list of hosts from the `~/.ansible-retry/[playbook-role-name].retry` file by prefixing the file name with @:
``` Shell
ansible-playbook [playbook-role-name].yaml --limit "@~/.ansible-retry/[playbook-role-name].retry"
```

## [Controll the tasks which should be executed](@controll-playbooks-with-tasks)
* `--tags all` - run all tasks, ignore tags (default behavior)
* `--tags [tag1, tag2]` - run only tasks with either the tag `tag1` or the tag `tag2`
* `--skip-tags [tag3, tag4]` - run all tasks except those with either the tag `tag3` or the tag `tag4`
* `--tags tagged` - run only tasks with at least one tag
* `--tags untagged` - run only tasks with no tags


* Run only tasks and blocks tagged `install` and `configure`:
``` Shell
ansible-playbook [playbook-role-name].yaml --tags "install,configure"
```

* To run all tasks except those tagged `configure`:
``` Shell
ansible-playbook [playbook-role-name].yaml --skip-tags "configure"
```

* if you do not know whether the tag for configure tasks is `configure` or `conf` in a playbook, you can display all available tags without running any tasks:
``` Shell
ansible-playbook [playbook-role-name].yaml --list-tags
```


# Additional knowledge
Encrypt string:
``` Shell
ansible-vault encrypt_string --vault-password-file .vault_password
```