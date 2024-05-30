from typing import *

import time
import pytest
import pathlib
import shutil
from tempfile import TemporaryDirectory

from object_info import *


# =====================================================================================================================
class Test__1:
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
        class Victim:
            def run(self):
                time.sleep(0.3)

        ObjectInfo(Victim()).print()
        assert True


# =====================================================================================================================
