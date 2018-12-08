'''manage context for env-switcher
'''

import config
import utils
import glob
import os
import sys


def init_context(context_name):
    '''initialize context for name {context_name}
    '''
    base_dict = config.BASE_DICT
    utils.set_base_field(base_dict, config.BASE_CONTEXT_NAME, context_name)

    json_name = utils.context_to_json(context_name)
    if os.path.exists(json_name):
        print("Warning: this context already exists")
        return
    utils.dict_to_json(base_dict, json_name)


def update_context(context_name, f_name, f_value):
    '''update context for {context_name}
    '''
    json_name = utils.context_to_json(context_name)
    c_dict = utils.json_to_dict(json_name)
    utils.set_base_field(c_dict, f_name, f_value)

    utils.dict_to_json(c_dict, json_name)


def update_field_context(context_name, f_name, f_value, encryption=""):
    '''update context for fields
    '''
    json_name = utils.context_to_json(context_name)
    c_dict = utils.json_to_dict(json_name)
    utils.set_field(c_dict, f_name, f_value, encryption=encryption)

    utils.dict_to_json(c_dict, json_name)


def copy_context(from_c, to_c):
    '''copy context from_c -> to_c
    '''
    from_j = utils.context_to_json(from_c)
    to_j = utils.context_to_json(to_c)
    if os.path.exists(to_j):
        print("Warning: to context already exists")
        return
    if not os.path.exists(from_j):
        print("Warning: from context does not exists")
        return
    from_dict = utils.json_to_dict(from_j)
    utils.set_base_field(from_dict, config.BASE_CONTEXT_NAME, to_c)
    utils.dict_to_json(from_dict, to_j)


def get_context_list():
    '''get all context available
    '''
    json_list = glob.glob("{}/c_*.json".format(config.JSON_DIR))
    return list(map(utils.json_to_context, json_list))


if __name__ == '__main__':
    # init_context("sample")
    # copy_context("sample", "sample2")
    # update_context("sample", "description", "sample update")
    if len(sys.argv) < 3:
        print("At least two arguments are required!")
        sys.exit(1)
    if sys.argv[1] == "context":
        if sys.argv[2] == "list":
            print(" ".join(get_context_list()))
