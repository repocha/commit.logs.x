with open("openstack.p.all") as f:
    lines = f.readlines()
    new_lines = []
    for line in lines:
        if line in new_lines:
            continue
        new_lines.append(line)


with open("output", "w") as f2:
    for line in new_lines:
        f2.write(line)
