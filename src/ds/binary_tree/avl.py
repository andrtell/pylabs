import ds.binary_tree.bst as bst


def insert(path, data):
    path, count = bst.insert(path, data)

    if not count:
        return path, count

    pass


def delete(path, data):
    path, count = bst.delete(path, data)

    if not count:
        return path, count

    pass
