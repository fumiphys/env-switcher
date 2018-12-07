'''utils for env-switcher
'''

import json
import config


def dict_to_json(d_dict, json_name):
    '''write dict to json
    '''
    with open(json_name, 'w') as writer:
        json.dump(d_dict, writer, indent=4)


if __name__ == '__main__':
    base_dict = config.BASE_DICT
    base_dict["fields"].append(config.FIELD_DICT)
    dict_to_json(base_dict, 'out.json')
