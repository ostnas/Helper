import copy


def find_element(original_dict, keys_list):
    next_dict = original_dict
    for key in keys_list[:-1]:
        if key not in next_dict:
            return None
        next_dict = next_dict[key]
    return next_dict


def dict_without_key(original_dict, text):
    keys = text.split('.')
    new_dict = copy.deepcopy(original_dict)
    next_dict = find_element(new_dict, keys)
    assert(next_dict is not None and keys[-1] in next_dict), f'Key "{text}" not found.'
    del next_dict[keys[-1]]
    return new_dict


def dict_with_edited_value(original_dict, text, value):
    keys = text.split('.')
    new_dict = copy.deepcopy(original_dict)
    next_dict = find_element(new_dict, keys)
    assert(next_dict is not None and keys[-1] in next_dict), f'Key "{text}" not found.'
    next_dict[keys[-1]] = value
    return new_dict


def dict_with_new_key(original_dict, text, value):
    keys = text.split('.')
    new_dict = copy.deepcopy(original_dict)
    next_dict = find_element(new_dict, keys)
    assert(next_dict is not None and keys[-1] not in next_dict), f'Key "{text}" already exists or path to key is incorrect'
    next_dict[keys[-1]] = value
    return new_dict