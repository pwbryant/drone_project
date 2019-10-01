# stuck on pending jobs
# run the following in /var/lib/drone/drone.sqlite
`update builds set build_status = 'error' where build_status = 'pending';`

# compose server and agent with ansible and docker-compose
https://0-8-0.docs.drone.io/installation/
https://docs.ansible.com/ansible/latest/modules/docker_compose_module.html
