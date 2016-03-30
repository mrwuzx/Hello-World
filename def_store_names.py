def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data, label, name):
    return data[label].get(name)

def store(data, *full_names):
    for full_name in full_names:
        ##将输入的名字拆开
        names = full_name.split()
        ##如果没有中间名,添加空格
        if len(names) == 2: names.insert(1, '')
        labels = 'first', 'middle', 'last'
        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]

#d = {}
#init(d)
#store(d, 'Han Solo', 'Xia ab Tian')
