from typing import *

import time
import pytest
import pathlib
import shutil
from tempfile import TemporaryDirectory

from object_info import *
from pytest_aux import *


# =====================================================================================================================
func_lambda = lambda: None


def func():
    pass


class Cls:
    attr = None

    def meth(self):
        pass


class Exx(Exception):
    pass


# ---------------------------------------------------------------------------------------------------------------------
# class ClsBool(bool):  # cant use it!
#     pass


class ClsInt(int):
    pass


class ClsStr(str):
    pass


class ClsList(list):
    pass


class ClsSet(set):
    pass


class ClsDict(dict):
    pass


CLASSES__AS_FUNC: list = [ClsInt, ClsStr, ClsList, ClsSet, ClsDict, ]


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
    @pytest.mark.parametrize(
        argnames="args, _EXPECTED",
        argvalues=[
            ("_", False),
            ("__", False),
            ("____", False),

            ("___abc___", True),
            ("__abc__", True),
            ("__abc_", False),
            ("__abc", False),

            ("_abc__", False),
            ("_abc_", False),
            ("_abc", False),

            ("abc__", False),
            ("abc_", False),
            ("abc", False),
        ]
    )
    def test__name_is_build_in(self, args, _EXPECTED):
        victim = self.Victim.check__name_is_build_in
        pytest_func_tester__no_kwargs(victim, args, _EXPECTED)

    # -----------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        argnames="args, _EXPECTED",
        argvalues=[
            (("str", True, True), True),
            (("str", True, False), False),

            ((b"bytes", True, True), True),
            ((b"bytes", True, False), False),

            ((111, ), False),
            (((111, ),), True),
            (([111, ],), True),
            (({111, },), True),
            (({111: 222, },), True),
            (({111: 222, }, True, True), True),
            (({111: 222, }, False, True), False),

            (int, False),
            (int(1), False),
            (str, True),        # not clear!!!
            (str(1), True),

            (Exception, False),
            (Exception(), False),

            (Cls, False),
            (Cls(), False),
            (ClsInt, False),
            (ClsInt(), False),

        ]
    )
    def test__iterable(self, args, _EXPECTED):
        victim = self.Victim.check__iterable
        pytest_func_tester__no_kwargs(victim, args, _EXPECTED)











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
    def test__check__func_or_meth(self):
        victim = self.Victim.check__func_or_meth

        assert victim("str") is False
        assert victim(b"str") is False
        assert victim(111) is False
        assert victim((111,)) is False
        assert victim([111, ]) is False
        assert victim({111, }) is False
        assert victim({111: 222}) is False

        assert victim(int) is True
        assert victim(int(1)) is False
        assert victim(str) is True
        assert victim(str(1)) is False
        assert victim(Exception) is False
        assert victim(Exception()) is False
        assert victim(Exx) is False
        assert victim(Exx()) is False
        assert victim(Cls) is False
        assert victim(Cls()) is False
        assert victim(ClsInt) is True
        assert victim(ClsInt()) is False

        assert victim(func) is True
        assert victim(func_lambda) is True
        assert victim(Cls.meth) is True
        assert victim(Cls().meth) is True
        assert victim(Cls.attr) is False
        assert victim(Cls().attr) is False

        for class_i in CLASSES__AS_FUNC:
            assert victim(class_i) is True

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
        assert victim(func_lambda) is False
        assert victim(Cls.meth) is False
        assert victim(Cls().meth) is False
        assert victim(Cls.attr) is False
        assert victim(Cls().attr) is False

        for class_i in CLASSES__AS_FUNC:
            assert victim(class_i) is True

    # TODO: add check__instance_of_user_class

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

        assert victim(func) is False
        assert victim(func_lambda) is False
        assert victim(Cls.meth) is False
        assert victim(Cls().meth) is False
        assert victim(Cls.attr) is True
        assert victim(Cls().attr) is True

        for class_i in CLASSES__AS_FUNC:
            assert victim(class_i) is False

    # -----------------------------------------------------------------------------------------------------------------
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
