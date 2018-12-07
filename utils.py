'''utils for env-switcher
'''

import json
import config


def dict_to_json(d_dict, json_name):
    '''write dict to json
    '''
    with open(json_name, 'w') as writer:
        json.dump(d_dict, writer, indent=4)


def set_base_field(b_dict, f_name, f_value):
    '''set dict value for base dict
    '''
    b_dict[f_name] = f_value


def set_field(b_dict, f_name, fd_name, f_value):
    '''set dict value for field
    '''
    if f_name not in b_dict["fields"].keys():
        print("Warning: no fields for {}".format(f_name))
        return
    b_dict["fields"][f_name][fd_name] = f_value


if __name__ == '__main__':
    base_dict = config.BASE_DICT
    set_base_field(base_dict, "context-name", "sample")
    base_dict["fields"]["f_sample"] = config.FIELD_DICT
    set_field(base_dict, "f_sample", "description", "sample")
    dict_to_json(base_dict, 'out.json')
