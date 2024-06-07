from typing import *

import time
import pytest
import pathlib
import shutil
from tempfile import TemporaryDirectory

from object_info import *


# =====================================================================================================================
def func():
    pass


class Cls:
    def meth(self):
        pass


class ClsInt(int):
    pass


class Exx(Exception):
    pass


# =====================================================================================================================
class Test__1:
    @classmethod
    def setup_class(cls):
        pass
        cls.Victim = TypeChecker

    # @classmethod
    # def teardown_class(cls):
    #     pass
    #
    # def setup_method(self, method):
    #     pass
    #
    # def teardown_method(self, method):
    #     pass

    # -----------------------------------------------------------------------------------------------------------------
    def test__name_is_build_in(self):
        victim = self.Victim.check__name_is_build_in
        assert victim("_") is False
        assert victim("__") is False
        assert victim("____") is False
        assert victim("__abc__") is True

        assert victim("__abc_") is False
        assert victim("__abc") is False
        assert victim("_abc") is False
        assert victim("_abc_") is False
        assert victim("_abc__") is False
        assert victim("abc__") is False

        assert victim("___abc___") is True

    # -----------------------------------------------------------------------------------------------------------------
    def test__iterable(self):
        victim = self.Victim.check__iterable

        assert victim("str", True, True) is True
        assert victim("str", True, False) is False

        assert victim(b"str", True, True) is True
        assert victim(b"str", True, False) is False

        assert victim(111) is False

        assert victim((111, )) is True
        assert victim([111, ]) is True
        assert victim({111, }) is True

        assert victim({111: 222 }) is True
        assert victim({111: 222 }, True, True) is True
        assert victim({111: 222 }, False, True) is False

        assert victim(int) is False
        assert victim(int(1)) is False
        assert victim(str) is True      # not clear!!!
        assert victim(str(1)) is True
        assert victim(Exception) is False
        assert victim(Exception()) is False
        assert victim(Cls) is False
        assert victim(Cls()) is False
        assert victim(ClsInt) is False
        assert victim(ClsInt()) is False

    def test__iterable_but_not_str(self):
        victim = self.Victim.check__iterable_but_not_str

        assert victim("str") is False
        assert victim(b"str") is False

        assert victim(111) is False

        assert victim((111, )) is True
        assert victim([111, ]) is True
        assert victim({111, }) is True

        assert victim({111: 222 }) is True

        assert victim(int) is False
        assert victim(int(1)) is False
        assert victim(str) is True        # not clear!!!
        assert victim(str(1)) is False
        assert victim(Exception) is False
        assert victim(Exception()) is False
        assert victim(Cls) is False
        assert victim(Cls()) is False
        assert victim(ClsInt) is False
        assert victim(ClsInt()) is False

    # -----------------------------------------------------------------------------------------------------------------
    def test__check__elementary(self):
        victim = self.Victim.check__elementary

        assert victim("str") is True
        assert victim(b"str") is True
        assert victim(111) is True
        assert victim((111, )) is True
        assert victim([111, ]) is True
        assert victim({111, }) is True
        assert victim({111: 222 }) is True

        assert victim(int) is False
        assert victim(int(1)) is True
        assert victim(str) is False
        assert victim(str(1)) is True
        assert victim(Exception) is False
        assert victim(Exception()) is False
        assert victim(Exx) is False
        assert victim(Exx()) is False
        assert victim(Cls) is False
        assert victim(Cls()) is False
        assert victim(ClsInt) is False
        assert victim(ClsInt()) is True     # not clear!!!

    def test__check__elementary_single(self):
        victim = self.Victim.check__elementary_single

        assert victim("str") is True
        assert victim(b"str") is True
        assert victim(111) is True
        assert victim((111, )) is False
        assert victim([111, ]) is False
        assert victim({111, }) is False
        assert victim({111: 222 }) is False

        assert victim(int) is False
        assert victim(int(1)) is True
        assert victim(str) is False
        assert victim(str(1)) is True
        assert victim(Exception) is False
        assert victim(Exception()) is False
        assert victim(Exx) is False
        assert victim(Exx()) is False
        assert victim(Cls) is False
        assert victim(Cls()) is False
        assert victim(ClsInt) is False
        assert victim(ClsInt()) is True     # not clear!!!

    def test__check__elementary_collection(self):
        victim = self.Victim.check__elementary_collection

        assert victim("str") is False
        assert victim(b"str") is False
        assert victim(111) is False
        assert victim((111, )) is True
        assert victim([111, ]) is True
        assert victim({111, }) is True
        assert victim({111: 222 }) is True

        assert victim(int) is False
        assert victim(int(1)) is False
        assert victim(str) is False
        assert victim(str(1)) is False
        assert victim(Exception) is False
        assert victim(Exception()) is False
        assert victim(Exx) is False
        assert victim(Exx()) is False
        assert victim(Cls) is False
        assert victim(Cls()) is False
        assert victim(ClsInt) is False
        assert victim(ClsInt()) is False

    def test__check__elementary_collection_not_dict(self):
        victim = self.Victim.check__elementary_collection_not_dict

        assert victim("str") is False
        assert victim(b"str") is False
        assert victim(111) is False
        assert victim((111, )) is True
        assert victim([111, ]) is True
        assert victim({111, }) is True
        assert victim({111: 222 }) is False

        assert victim(int) is False
        assert victim(int(1)) is False
        assert victim(str) is False
        assert victim(str(1)) is False
        assert victim(Exception) is False
        assert victim(Exception()) is False
        assert victim(Exx) is False
        assert victim(Exx()) is False
        assert victim(Cls) is False
        assert victim(Cls()) is False
        assert victim(ClsInt) is False
        assert victim(ClsInt()) is False

    # -----------------------------------------------------------------------------------------------------------------
    def test__check__class(self):
        victim = self.Victim.check__class

        assert victim("str") is False
        assert victim(b"str") is False
        assert victim(111) is False
        assert victim((111, )) is False
        assert victim([111, ]) is False
        assert victim({111, }) is False
        assert victim({111: 222 }) is False

        assert victim(int) is True
        assert victim(int(1)) is False
        assert victim(str) is True
        assert victim(str(1)) is False
        assert victim(Exception) is True
        assert victim(Exception()) is False
        assert victim(Exx) is True
        assert victim(Exx()) is False
        assert victim(Cls) is True
        assert victim(Cls()) is False
        assert victim(ClsInt) is True
        assert victim(ClsInt()) is False

        assert victim(func) is False
        assert victim(Cls.meth) is False
        assert victim(Cls().meth) is False


    def test__check__instance(self):
        victim = self.Victim.check__instance

        assert victim("str") is True
        assert victim(b"str") is True
        assert victim(111) is True
        assert victim((111, )) is True
        assert victim([111, ]) is True
        assert victim({111, }) is True
        assert victim({111: 222 }) is True

        assert victim(int) is False
        assert victim(int(1)) is True
        assert victim(str) is False
        assert victim(str(1)) is True
        assert victim(Exception) is False
        assert victim(Exception()) is True
        assert victim(Exx) is False
        assert victim(Exx()) is True
        assert victim(Cls) is False
        assert victim(Cls()) is True
        assert victim(ClsInt) is False
        assert victim(ClsInt()) is True

    def test__check__exception(self):
        victim = self.Victim.check__exception

        assert victim("str") is False
        assert victim(b"str") is False
        assert victim(111) is False
        assert victim((111, )) is False
        assert victim([111, ]) is False
        assert victim({111, }) is False
        assert victim({111: 222 }) is False

        assert victim(int) is False
        assert victim(int(1)) is False
        assert victim(str) is False
        assert victim(str(1)) is False
        assert victim(Exception) is True
        assert victim(Exception()) is True
        assert victim(Exx) is True
        assert victim(Exx()) is True
        assert victim(Cls) is False
        assert victim(Cls()) is False
        assert victim(ClsInt) is False
        assert victim(ClsInt()) is False

    def test__check__nested__by_cls_or_inst(self):
        victim = self.Victim.check__nested__by_cls_or_inst

        assert victim("str", "str") is True
        assert victim("str", str) is True
        assert victim(str, str) is True
        assert victim(str, "str") is True
        assert victim(int, str) is False
        assert victim(int, "str") is False

        assert victim(int, 111) is True
        assert victim(111, int) is True

        assert victim(Exception, Exception) is True
        assert victim(Exception(), Exception) is True
        assert victim(Exception(), Exception()) is True
        assert victim(Exception, Exception()) is True

        assert victim(Exx, Exception) is True
        assert victim(Exx(), Exception) is True
        assert victim(Exx(), Exception()) is True
        assert victim(Exx, Exception()) is True

        assert victim(Exception, Exx) is False
        assert victim(Exception(), Exx) is False
        assert victim(Exception(), Exx()) is False
        assert victim(Exception, Exx()) is False


# =====================================================================================================================
