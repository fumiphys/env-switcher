'''test for utils.py
'''

import utils
import config
import os


OUT_JSON = "out.json"


class TestUtil(object):
    def test_dict_to_json(self):
        if os.path.exists(OUT_JSON):
            os.remove(OUT_JSON)
        base_dict = config.BASE_DICT
        utils.dict_to_json(base_dict, OUT_JSON)

        assert os.path.exists(OUT_JSON)

    def test_json_to_dict(self):
        base_dict = config.BASE_DICT
        if not os.path.exists(OUT_JSON):
            utils.dict_to_json(base_dict, OUT_JSON)
        b_dict = utils.json_to_dict(OUT_JSON)

        assert b_dict == base_dict

    def test_set_base_field(self):
        base_dict = config.BASE_DICT
        utils.set_base_field(base_dict, config.BASE_DESCRIPTION, "sample")

        assert base_dict[config.BASE_DESCRIPTION] == "sample"

        utils.set_base_field(base_dict, config.BASE_CONTEXT_NAME, "sample")

        assert base_dict[config.BASE_CONTEXT_NAME] == ""

    def test_set_field(self):
        base_dict = config.BASE_DICT
        utils.set_field(base_dict, "f_sample", "f_value")

        assert base_dict[config.BASE_FIELDS]["f_sample"][config.FIELD_VALUE] == "f_value"
        assert base_dict[config.BASE_FIELDS]["f_sample"][config.FIELD_ENCRYPTION] == ""

        utils.set_field(base_dict, "b_sample", "b_value", encryption="base64")

        assert base_dict[config.BASE_FIELDS]["b_sample"][config.FIELD_VALUE] == "Yl92YWx1ZQ=="
        assert base_dict[config.BASE_FIELDS]["b_sample"][config.FIELD_ENCRYPTION] == "base64"

    def test_context_to_json(self):
        assert utils.context_to_json("sample") == "./c_sample.json"

    def test_json_to_context(self):
        assert utils.json_to_context("./c_sample.json") == "sample"
        assert utils.json_to_context("./c_sample.jon") == ""
        assert utils.json_to_context("./d_sample.json") == ""
