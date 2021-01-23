import os
import yaml

def per_section(it, is_delimiter=lambda x: x.isspace()):
    ret = []
    for line in it:
        if is_delimiter(line):
            if ret:
                yield ret  # OR  ''.join(ret)
                ret = []
        else:
            ret.append(line.rstrip())  # OR  ret.append(line)
    if ret:
        yield ret


print()

with open('multiservice.k8s-deployment.latest.yaml') as f:
    sections = list(per_section(f, lambda line: line.startswith('---'))) # comment

x=1
for y in sections:
    print(str(x) + ' ------------------------------')
    data = yaml.safe_load(str(y))
    print (yaml.dump(data))
    #print(type(str(y)))
    x=x+1

print()
