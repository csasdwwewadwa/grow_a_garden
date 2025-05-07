with open('milestone.txt') as f:
    lines = f.read().split('\n')

freq:dict[str, list] = {}
for line in lines:
    name = line.split()[0]
    weight, *attr = line.split()[1:]

    if name in freq:
        freq[name].append('[' + ','.join(attr) + weight + ']')
    else:
        freq[name] = ['[' + ','.join(attr) + weight + ']']

for k, v in freq.items():
    line = f'{k}:  {", ".join(v)}'
    print(line)