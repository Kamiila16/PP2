import json

with open('sample-data.json') as file:
    data=json.load(file)

print('Interface Status')
print('================================================================================')
print("{:<50} {:<20} {:<10} {:<6}".format("DN", "Description", "Speed", "MTU"))
print('-------------------------------------------------- --------------------  ------  ------')

for i, entry in enumerate(data["imdata"]):
    if i == 3:
        break
    dn = entry["l1PhysIf"]["attributes"]["dn"]
    description = entry["l1PhysIf"]["attributes"].get("description", "inherit")
    speed = entry["l1PhysIf"]["attributes"]["speed"]
    mtu = entry["l1PhysIf"]["attributes"].get("mtu", "inherit")

    print("{:<71} {:<10} {:<6}".format(dn, speed, mtu))
