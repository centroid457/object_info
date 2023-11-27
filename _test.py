import os
import pytest
import pathlib
import shutil
from tempfile import TemporaryDirectory
from typing import *
from configparser import ConfigParser

from object_info import *


# =====================================================================================================================
class Test__888888888888:
    VICTIM: Type[print_object_info] = type("VICTIM", (print_object_info,), {})

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        self.VICTIM = type("VICTIM", (print_object_info,), {})

    # -----------------------------------------------------------------------------------------------------------------
    def test__ClassMethod_and_obj(self):
        assert True


# =====================================================================================================================
