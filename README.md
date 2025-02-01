# Intro

This repository serves as a collection of Ansible playbooks to install and manage software and mods on a Steam Deck, or really any machine running Steam OS.

## Installation

Users need to do a few things in order to run playbooks in this repository.

### On your Steam device
1. Know the `sudo` password of your Steam device, which is needed to install software. If you have already set this you should know what it is, otherwise open up `konsole` and enter `passwd` and set your password.
1. Enable SSH on the Steam device by running `sudo systemctl enable sshd --now` (you will need your sudo password from your Steam device)

### On this computer
1. Install [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/index.html)
1. Add the IP address of your Steam Deck or Steam OS device to the [`inventory/hosts.yml`](inventory/hosts.yml) file. An easy way to find this is to go to desktop mode on your Steam device, open up the `konsole` app and enter `ip addr`. If on wifi, you will see your device's IP under the `wlan0` entry next to `inet`.
1. Create an ssh key pair on this computer. [GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) has a nice guide
1. Copy the ssh key you just created to the Steam device with `ssh-copy-id -f -i ~/.ssh/id_ed25519 deck@ip_of_your_steam_device` (you will need your sudo password from your Steam device)

### Testing the connection
1. Once all the above steps are completed, you should be able to run `ansible-playbook -i inventory/hosts.yml hello_world.yml -l my_deck`. You will see something like the following output:
```
PLAY [Hello World Playbook] ******************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************
[WARNING]: Platform linux on host my_deck is using the discovered Python interpreter at /usr/bin/python3.11, but future installation of another Python interpreter could change
the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [my_deck]

TASK [Print Hello World] *********************************************************************************************************************************************************
ok: [my_deck] => {
    "msg": "Hello World, connected to my_deck!"
}

PLAY RECAP ***********************************************************************************************************************************************************************
my_deck                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

After the above steps, you will be able to run any of the playbooks contained in this repository for easy setup of software, or mods for a given game that is supported.
