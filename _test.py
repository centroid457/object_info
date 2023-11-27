import os
import pytest
import pathlib
import shutil
from tempfile import TemporaryDirectory
from typing import *
from configparser import ConfigParser

from object_info import *


# =====================================================================================================================
class Test_1:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    # -----------------------------------------------------------------------------------------------------------------
    def test__obj_show_attr_all(self):
        obj_show_attr_all(list)


# =====================================================================================================================
class Cls1:
    attr1=1
    attr2=2


if __name__ == "__main__":
    obj_show_attr_all(Cls1())
    ObjectInfo(Cls1()).print_object_info()
