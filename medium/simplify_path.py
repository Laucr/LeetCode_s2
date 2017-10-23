def simplifyPath(path):
    """
    emmmm I thought this qus should be classified in Easy
    :type path: str
    :rtype: str
    """
    paths = [p for p in path[1:].split('/') if p != '']
    res = []
    for p in paths:
        if p == '.':
            continue
        if p == '..':
            if len(res) > 0:
                res.pop()
        else:
            res.append(p)
    return '/' + '/'.join(res)

print simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///")



