import os
import time

import pytest
import pathlib
import shutil
from tempfile import TemporaryDirectory
from typing import *
from configparser import ConfigParser

from PyQt5.QtCore import QThread

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
    def test__QThread(self):
        class Victim(QThread):
            def run(self):
                time.sleep(0.3)

        ObjectInfo(Victim()).print()
        assert True


# =====================================================================================================================
