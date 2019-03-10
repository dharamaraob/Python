#!/Users/baladh/python3/bin/python
import yaml
with open('users.yaml') as users:
    usersdata = yaml.safe_load(users)
print (usersdata)

# transoform usersdata to host to group mapping
# output = list(map(lambda kv: (kv[1], kv[0]), usersdata['host_groups'].items()))
# print(str(output))

hosttogrp = dict()
for kv in usersdata['host_groups'].items():
    for hostname in kv[1]:
        if hostname in hosttogrp:
            hosttogrp[hostname].add(kv[0])
        else:
            hosttogrp[hostname] = set()
            hosttogrp[hostname].add(kv[0])
print(str(hosttogrp))

grptouser = dict()
for kv in usersdata['users'].items():
    for username in kv[1]:
        if username in hosttogrp:
            grptouser[username].add(kv[0])
        else:
            grptouser[username] = set()
            grptouser[username].add(kv[0])

print(str(grptouser))

def finduserinhost(hostname_input):
    users = set()
    for grp in hosttogrp[hostname_input]:
        users.update(grptouser[grp])
    return users
    # with open('publickeys.yaml') as pks:
#     publickeys = yaml.safe_load(pks)
# print (publickeys)
#
#
# def getKeysforHost(host):
#     #print (host)
#     for usergroups,hosts in usersdata["host_groups"].items():
#         #print (usergroups,hosts)
#         if host in hosts:
#             #print (usergroups)
#             for user, groups in usersdata["users"].items():
#                 if usergroups in groups:
#                     print (user, groups)
#
#


print(finduserinhost("host1.example.com"))
