# Policychecking in Kubernetes

This repository contains Ansible Playbooks for provisioning Kubernetes clusters, and manifests that supports different multi-tenant configurations.

# How to run?

1. Configure the [inventory](https://github.com/henricson/masters-cluster/blob/main/inventory) file with the IP-address of control-plane nodes and worker nodes. Passwordless SSH access to these servers are assumed. This playbook is tested with Ubuntu 22.04 LTS, and is not guaranteed to work with other versions (although it might).
2. Install Ansible roles:

```bash
ansible-galaxy install -r requirements.yml
```

3. Run the playbook:

```bash
ansible-playbook -i inventory main.yml
```
