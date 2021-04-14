import copy


def dict_without_key(dict, text):
    keys = text.split('.')
    new_dict = copy.deepcopy(dict)
    next = new_dict
    if keys[0] in next:
        for key in keys[:-1]:
            next = next[key]
        if keys[-1] in next:
            del next[keys[-1]]
        else:
            return None
        return new_dict
    else:
        return None


def change_value_by_key(dict, text, value):
    keys = text.split('.')
    new_dict = copy.deepcopy(dict)
    next = new_dict
    if keys[0] in next:
        for key in keys[:-1]:
            next = next[key]
        if keys[-1] in next:
            next[keys[-1]] = value
        else:
            return None
        return new_dict
    else:
        return None


def add_key_to_dict(dict, text, value):
    keys = text.split('.')
    new_dict = copy.deepcopy(dict)
    next = new_dict

    if len(keys) == 1 and keys[0] not in next:
        next[keys[0]] = value
        return new_dict
    elif len(keys) == 1 and keys[0] in next:
        return None

    for key in keys[:-1]:
        if key in next:
            next = next[key]
        else:
            return None

    if keys[-1] in next:
        return None
    else:
        next[keys[-1]] = value
        return new_dict