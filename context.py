'''manage context for env-switcher
'''

import config
import utils
import os


def init_context(context_name):
    base_dict = config.BASE_DICT
    utils.set_base_field(base_dict, config.BASE_CONTEXT_NAME, context_name)

    json_name = utils.context_to_json(context_name)
    if os.path.exists(json_name):
        print("Warning: this context already exists")
        return
    utils.dict_to_json(base_dict, json_name)


if __name__ == '__main__':
    init_context("sample")
