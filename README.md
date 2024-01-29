# Policychecking in Kubernetes

This repository contains Ansible Playbooks for provisioning Kubernetes clusters, and manifests that supports different multi-tenant configurations.

# How to run?

1. Configure the inventory file with control-plane and nodes. Passwordless SSH access is assumed.
2. Install Ansible roles:

`ansible-galaxy install -r requirements.yml`

3. Run the playbook:

`ansible-playbook -i inventory main.yml`
