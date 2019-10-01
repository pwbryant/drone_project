# stuck on pending jobs
# run the following in /var/lib/drone/drone.sqlite
`update builds set build_status = 'error' where build_status = 'pending';`
