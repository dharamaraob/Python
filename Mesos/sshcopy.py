#!/usr/bin/python3
import yaml
with open('users.yaml') as users:
    usersdata = yaml.safe_load(users)
print (usersdata)

with open('publickeys.yaml') as pks:
    publickeys = yaml.safe_load(pks)
print (publickeys)

def getKeysforHost(host):
    #print (host)
    for usergroups,hosts in usersdata["host_groups"].items():
        #print (usergroups,hosts)
        if host in hosts:
            #print (usergroups)
            for user, usergroups in usersdata["users"].items():
                print (user)




getKeysforHost("host2.example.com")
