'''
config file for env-switcher
'''

import codecs
import json
import os
import sys

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


def set_json_dir(json_dir):
    '''set directory of saving jsons
    '''
    c_dict = {}
    with codecs.open(CONFIG_FILE, 'r', 'utf-8') as reader:
        c_dict = json.load(reader)
    c_dict["JSON_DIR"] = json_dir
    with codecs.open(CONFIG_FILE, 'w', 'utf-8') as writer:
        json.dump(c_dict, writer)


def set_log_dir(log_dir):
    '''set directory of saving jsons
    '''
    c_dict = {}
    with codecs.open(CONFIG_FILE, 'r', 'utf-8') as reader:
        c_dict = json.load(reader)
    c_dict["LOG_DIR"] = log_dir
    with codecs.open(CONFIG_FILE, 'w', 'utf-8') as writer:
        json.dump(c_dict, writer)


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


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("At least one argument is required")
        sys.exit(1)
    if sys.argv[1] == "get":
        if len(sys.argv) == 2:
            print("JSON_DIR : {}".format(get_json_dir()))
            print("LOG_DIR  : {}".format(get_log_dir()))
        elif len(sys.argv) == 3:
            if sys.argv[2].lower() == "log_dir":
                print("LOG_DIR  : {}".format(get_log_dir()))
            elif sys.argv[2].lower() == "json_dir":
                print("JSON_DIR : {}".format(get_json_dir()))
    elif sys.argv[1] == "set":
        if not len(sys.argv) == 4:
            print("exactly three arguments are required.")
            sys.exit(1)
        if sys.argv[2].lower() == "log_dir":
            set_log_dir(sys.argv[3])
        elif sys.argv[2].lower() == "json_dir":
            set_json_dir(sys.argv[3])
