'''
config file for env-switcher
'''

import codecs
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = "{}/config.json".format(BASE_DIR)


def get_json_dir():
    '''get directory of saving json file
    '''
    c_dict = {}
    with codecs.open(CONFIG_FILE, 'r', 'utf-8') as reader:
        c_dict = json.load(reader)
    return c_dict["JSON_DIR"]


def get_log_dir():
    '''get directory of saving logs
    '''
    c_dict = {}
    with codecs.open(CONFIG_FILE, 'r', 'utf-8') as reader:
        c_dict = json.load(reader)
    return c_dict["LOG_DIR"]


# constants
BASE_CONTEXT_NAME = "context-name"
BASE_DESCRIPTION = "description"
BASE_FIELDS = "fields"

FIELD_ENCRYPTION = "encryption"
FIELD_VALUE = "value"


# base dict
BASE_DICT = {
    BASE_CONTEXT_NAME: "",
    BASE_DESCRIPTION: "",
    BASE_FIELDS: {},
}

# field dict
FIELD_DICT = {
    FIELD_ENCRYPTION: "",
    FIELD_VALUE: "",
}
