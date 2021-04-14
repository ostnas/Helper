import copy
import pyt

dict = {
    "one": 1,
    "two": "smth",
    "three": True,
    "five": {
        "one": {
            "two": 2,
            "test": 3
        }
    }
}


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



print(dict_without_key(dict, "text"))
print(dict_without_key(dict, "five"))
print(dict_without_key(dict, "five.one"))
print(dict_without_key(dict, "five.two"))
print(dict_without_key(dict, "five.one.two"))
print(dict_without_key(dict, ""))
print(dict_without_key({}, "text"))
print(dict_without_key({}, "five"))
print(dict_without_key({}, "five.one"))
print(dict_without_key({}, "five.two"))
print(dict_without_key({}, "five.one.two"))
print(dict_without_key({}, ""))

print(change_value_by_key(dict, "text", "new"))
print(change_value_by_key(dict, "five", "new"))
print(change_value_by_key(dict, "five.one", "new"))
print(change_value_by_key(dict, "five.two", "new"))
print(change_value_by_key(dict, "five.one.two", "new"))
print(change_value_by_key(dict, "", "new"))
print(change_value_by_key({}, "text", "new"))
print(change_value_by_key({}, "five", "new"))
print(change_value_by_key({}, "five.one", "new"))
print(change_value_by_key({}, "five.two", "new"))
print(change_value_by_key({}, "five.one.two", "new"))
print(change_value_by_key({}, "", "new"))

print(add_key_to_dict(dict, "text", "new"))
print(add_key_to_dict(dict, "five", "new"))
print(add_key_to_dict(dict, "five.1", "new"))
print(add_key_to_dict(dict, "five.one", "new"))
print(add_key_to_dict(dict, "five.two", "new"))
print(add_key_to_dict(dict, "five.one.two", "new"))
print(add_key_to_dict(dict, "", "new"))
print(add_key_to_dict({}, "text", "new"))
print(add_key_to_dict({}, "five", "new"))
print(add_key_to_dict({}, "five.1", "new"))
print(add_key_to_dict({}, "five.one", "new"))
print(add_key_to_dict({}, "five.two", "new"))
print(add_key_to_dict({}, "five.one.two", "new"))
print(add_key_to_dict({}, "", "new"))