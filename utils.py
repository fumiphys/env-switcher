'''utils for env-switcher
'''

import json
import config
import base64
import codecs


def dict_to_json(d_dict, json_name):
    '''write dict to json
    '''
    with codecs.open(json_name, 'w') as writer:
        json.dump(d_dict, writer, indent=4)


def json_to_dict(json_name):
    '''fetch dict from json
    '''
    d_dict = {}
    with codecs.open(json_name, 'r') as writer:
        d_dict = json.load(writer)
    return d_dict


def set_base_field(b_dict, f_name, f_value):
    '''set dict value for base dict
    '''
    if f_name == config.BASE_CONTEXT_NAME:
        return
    b_dict[f_name] = f_value


def set_field(b_dict, f_name, f_value, encryption=""):
    '''set dict value for field
    '''

    if f_name not in b_dict[config.BASE_FIELDS].keys():
        print("Warning: no fields for {}".format(f_name))
        b_dict[config.BASE_FIELDS][f_name] = {}
    b_dict[config.BASE_FIELDS][f_name][config.FIELD_ENCRYPTION] = encryption
    if encryption == "base64":
        f_value = base64.b64encode(f_value.encode('utf-8')).decode('utf-8')
    b_dict[config.BASE_FIELDS][f_name][config.FIELD_VALUE] = f_value


def context_to_json(context):
    '''map context name to json file
    '''
    return "{}/c_{}.json".format(config.JSON_DIR, context)


def json_to_context(json_name):
    '''map json file to context name
    '''
    d_sp = json_name.split(".")
    s_sp = json_name.split("/")
    if not s_sp[-1][0:2] == "c_":
        print("Warning: this file is not for env-switcher")
        return ""
    if not d_sp[-1] == "json":
        print("Warning: this file not json file")
        return ""
    return d_sp[-2].split("/")[-1][2:]


if __name__ == '__main__':
    base_dict = config.BASE_DICT
    set_base_field(base_dict, "context-name", "sample")
    base_dict["fields"]["f_sample"] = config.FIELD_DICT
    set_field(base_dict, "f_sample", "sample", encryption="base64")
    dict_to_json(base_dict, 'out.json')

    print(context_to_json("sample"))
    print(json_to_context("c_sample.json"))
    print(json_to_context("hello.json"))
    print(json_to_context("c_hello.jon"))
