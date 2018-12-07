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


def context_to_json(context):
    '''map context name to json file
    '''
    return "c_{}.json".format(context)


def json_to_context(json_name):
    '''map json file to context name
    '''
    if not json_name[0:2] == "c_":
        print("Warning: this file is not for env-switcher")
        return ""
    if not json_name.split(".")[-1] == "json":
        print("Warning: this file not json file")
        return ""
    return json_name.split(".")[0][2:]


if __name__ == '__main__':
    base_dict = config.BASE_DICT
    set_base_field(base_dict, "context-name", "sample")
    base_dict["fields"]["f_sample"] = config.FIELD_DICT
    set_field(base_dict, "f_sample", "description", "sample")
    dict_to_json(base_dict, 'out.json')

    print(context_to_json("sample"))
    print(json_to_context("c_sample.json"))
    print(json_to_context("hello.json"))
    print(json_to_context("c_hello.jon"))
