from typing import *
import pathlib
import time

import pytest
from pytest import mark
from pytest_aux import *

from object_info import *

from PyQt5.QtCore import QThread


# =====================================================================================================================
class Test_FREEZE:
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
