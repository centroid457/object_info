from typing import *
import pathlib

import pytest
from pytest import mark
from pytest_aux import *

from object_info import *


# =====================================================================================================================
values_elementary_single = [None, True, False, 0, 11, 11.22]


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
            (None, True),
            (True, True),
            (False, True),
            (0, True),
            (111, True),
            (111.222, True),
            ("str", True),
            (b"bytes", True),

            (((111, ),), True),
            (([111, ],), True),
            (({111, },), True),
            (({111: 222, },), True),

            (int, False),
            (int(1), True),
            (str, False),
            (str(1), True),

            (Exception, False),
            (Exception(), False),
            (Exx, False),
            (Exx(), False),

            (Cls, False),
            (Cls(), False),
            (ClsInt, False),
            (ClsInt(), True),    # int() == 0!!!

            (func, False),
            (func_lambda, False),
            (Cls.meth, False),
            (Cls().meth, False),
            (Cls.attr, True),
            (Cls().attr, True),

            *[(class_i, False) for class_i in CLASSES__AS_FUNC]
        ]
    )
    def test__check__elementary(self, args, _EXPECTED):
        victim = self.Victim.check__elementary
        pytest_func_tester__no_kwargs(victim, args, _EXPECTED)

    @pytest.mark.parametrize(
        argnames="args, _EXPECTED",
        argvalues=[
            (None, True),
            (True, True),
            (False, True),
            (0, True),
            (111, True),
            (111.222, True),
            ("str", True),
            (b"bytes", True),

            (((111, ),), False),
            (([111, ],), False),
            (({111, },), False),
            (({111: 222, },), False),

            (int, False),
            (int(1), True),
            (str, False),
            (str(1), True),

            (Exception, False),
            (Exception(), False),
            (Exx, False),
            (Exx(), False),

            (Cls, False),
            (Cls(), False),
            (ClsInt, False),
            (ClsInt(), True),    # int() == 0!!!

            (func, False),
            (func_lambda, False),
            (Cls.meth, False),
            (Cls().meth, False),
            (Cls.attr, True),
            (Cls().attr, True),

            *[(class_i, False) for class_i in CLASSES__AS_FUNC]
        ]
    )
    def test__check__elementary_single(self, args, _EXPECTED):
        victim = self.Victim.check__elementary_single
        pytest_func_tester__no_kwargs(victim, args, _EXPECTED)

    @pytest.mark.parametrize(
        argnames="args, _EXPECTED",
        argvalues=[
            (None, False),
            (True, False),
            (False, False),
            (0, False),
            (111, False),
            (111.222, False),
            ("str", False),
            (b"bytes", False),

            (((111, ),), True),
            (([111, ],), True),
            (({111, },), True),
            (({111: 222, },), True),

            (int, False),
            (int(1), False),
            (str, False),
            (str(1), False),

            (Exception, False),
            (Exception(), False),
            (Exx, False),
            (Exx(), False),

            (Cls, False),
            (Cls(), False),
            (ClsInt, False),
            (ClsInt(), False),    # int() == 0!!!

            (func, False),
            (func_lambda, False),
            (Cls.meth, False),
            (Cls().meth, False),
            (Cls.attr, False),
            (Cls().attr, False),

            *[(class_i, False) for class_i in CLASSES__AS_FUNC]
        ]
    )
    def test__check__elementary_collection(self, args, _EXPECTED):
        victim = self.Victim.check__elementary_collection
        pytest_func_tester__no_kwargs(victim, args, _EXPECTED)

    @pytest.mark.parametrize(
        argnames="args, _EXPECTED",
        argvalues=[
            (None, False),
            (True, False),
            (False, False),
            (0, False),
            (111, False),
            (111.222, False),
            ("str", False),
            (b"bytes", False),

            (((111, ),), True),
            (([111, ],), True),
            (({111, },), True),
            (({111: 222, },), False),

            (int, False),
            (int(1), False),
            (str, False),
            (str(1), False),

            (Exception, False),
            (Exception(), False),
            (Exx, False),
            (Exx(), False),

            (Cls, False),
            (Cls(), False),
            (ClsInt, False),
            (ClsInt(), False),    # int() == 0!!!

            (func, False),
            (func_lambda, False),
            (Cls.meth, False),
            (Cls().meth, False),
            (Cls.attr, False),
            (Cls().attr, False),

            *[(class_i, False) for class_i in CLASSES__AS_FUNC]
        ]
    )
    def test__check__elementary_collection_not_dict(self, args, _EXPECTED):
        victim = self.Victim.check__elementary_collection_not_dict
        pytest_func_tester__no_kwargs(victim, args, _EXPECTED)

    # -----------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        argnames="args, _EXPECTED",
        argvalues=[
            (("str", True, True), True),
            (("str", True, False), False),

            ((b"bytes", True, True), True),
            ((b"bytes", True, False), False),

            # -----------------------
            (None, False),
            (True, False),
            (False, False),
            (0, False),
            (111, False),
            (111.222, False),
            ("str", True),
            (b"bytes", True),

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
            (Exx, False),
            (Exx(), False),

            (Cls, False),
            (Cls(), False),
            (ClsInt, False),
            (ClsInt(), False),

            (func, False),
            (func_lambda, False),
            (Cls.meth, False),
            (Cls().meth, False),
            (Cls.attr, False),
            (Cls().attr, False),

            # *[(class_i, False) for class_i in CLASSES__AS_FUNC]
        ]
    )
    def test__iterable(self, args, _EXPECTED):
        victim = self.Victim.check__iterable
        pytest_func_tester__no_kwargs(victim, args, _EXPECTED)

    @pytest.mark.parametrize(
        argnames="args, _EXPECTED",
        argvalues=[
            (None, False),
            (True, False),
            (False, False),
            (0, False),
            (111, False),
            (111.222, False),
            ("str", False),
            (b"bytes", False),

            (((111, ),), True),
            (([111, ],), True),
            (({111, },), True),
            (({111: 222, },), True),

            (int, False),
            (int(1), False),
            (str, True),        # not clear!!!
            (str(1), False),

            (Exception, False),
            (Exception(), False),
            (Exx, False),
            (Exx(), False),

            (Cls, False),
            (Cls(), False),
            (ClsInt, False),
            (ClsInt(), False),

            (func, False),
            (func_lambda, False),
            (Cls.meth, False),
            (Cls().meth, False),
            (Cls.attr, False),
            (Cls().attr, False),

            # *[(class_i, False) for class_i in CLASSES__AS_FUNC]
        ]
    )
    def test__iterable_but_not_str(self, args, _EXPECTED):
        victim = self.Victim.check__iterable_not_str
        pytest_func_tester__no_kwargs(victim, args, _EXPECTED)

    # -----------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        argnames="args, _EXPECTED",
        argvalues=[
            (None, False),
            (True, False),
            (False, False),
            (0, False),
            (111, False),
            (111.222, False),
            ("str", False),
            (b"bytes", False),

            (((111, ),), False),
            (([111, ],), False),
            (({111, },), False),
            (({111: 222, },), False),

            (int, True),
            (int(1), False),
            (str, True),
            (str(1), False),

            (Exception, False),
            (Exception(), False),
            (Exx, False),
            (Exx(), False),

            (Cls, False),
            (Cls(), False),
            (ClsInt, True),
            (ClsInt(), False),    # int() == 0!!!

            (func, True),
            (func_lambda, True),
            (Cls.meth, True),
            (Cls().meth, True),
            (Cls.attr, False),
            (Cls().attr, False),

            *[(class_i, True) for class_i in CLASSES__AS_FUNC]
        ]
    )
    def test__check__func_or_meth(self, args, _EXPECTED):
        victim = self.Victim.check__func_or_meth
        pytest_func_tester__no_kwargs(victim, args, _EXPECTED)

    # -----------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        argnames="args, _EXPECTED",
        argvalues=[
            (None, False),
            (True, False),
            (False, False),
            (0, False),
            (111, False),
            (111.222, False),
            ("str", False),
            (b"bytes", False),

            (((111, ),), False),
            (([111, ],), False),
            (({111, },), False),
            (({111: 222, },), False),

            (int, True),
            (int(1), False),
            (str, True),
            (str(1), False),

            (Exception, True),
            (Exception(), False),
            (Exx, True),
            (Exx(), False),

            (Cls, True),
            (Cls(), False),
            (ClsInt, True),
            (ClsInt(), False),    # int() == 0!!!

            (func, False),
            (func_lambda, False),
            (Cls.meth, False),
            (Cls().meth, False),
            (Cls.attr, False),
            (Cls().attr, False),

            *[(class_i, True) for class_i in CLASSES__AS_FUNC]
        ]
    )
    def test__check__class(self, args, _EXPECTED):
        victim = self.Victim.check__class
        pytest_func_tester__no_kwargs(victim, args, _EXPECTED)

    @pytest.mark.parametrize(
        argnames="args, _EXPECTED",
        argvalues=[
            (None, True),
            (True, True),
            (False, True),
            (0, True),
            (111, True),
            (111.222, True),
            ("str", True),
            (b"bytes", True),

            (((111, ),), True),
            (([111, ],), True),
            (({111, },), True),
            (({111: 222, },), True),

            (int, False),
            (int(1), True),
            (str, False),
            (str(1), True),

            (Exception, False),
            (Exception(), True),
            (Exx, False),
            (Exx(), True),

            (Cls, False),
            (Cls(), True),
            (ClsInt, False),
            (ClsInt(), True),    # int() == 0!!!

            (func, False),
            (func_lambda, False),
            (Cls.meth, False),
            (Cls().meth, False),
            (Cls.attr, True),
            (Cls().attr, True),

            *[(class_i, False) for class_i in CLASSES__AS_FUNC]
        ]
    )
    def test__check__instance(self, args, _EXPECTED):
        victim = self.Victim.check__instance
        pytest_func_tester__no_kwargs(victim, args, _EXPECTED)

    @pytest.mark.parametrize(
        argnames="args, _EXPECTED",
        argvalues=[
            (None, False),
            (True, False),
            (False, False),
            (0, False),
            (111, False),
            (111.222, False),
            ("str", False),
            (b"bytes", False),

            (((111, ),), False),
            (([111, ],), False),
            (({111, },), False),
            (({111: 222, },), False),

            (int, False),
            (int(1), False),
            (str, False),
            (str(1), False),

            (Exception, False),
            (Exception(), True),
            (Exx, False),
            (Exx(), True),

            (Cls, False),
            (Cls(), True),
            (ClsInt, False),
            (ClsInt(), False),    # int() == 0!!!

            (func, False),
            (func_lambda, False),
            (Cls.meth, False),
            (Cls().meth, False),
            (Cls.attr, False),
            (Cls().attr, False),

            *[(class_i, False) for class_i in CLASSES__AS_FUNC]
        ]
    )
    def test__check__instance_not_elementary(self, args, _EXPECTED):
        victim = self.Victim.check__instance_not_elementary
        pytest_func_tester__no_kwargs(victim, args, _EXPECTED)

    # -----------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        argnames="args, _EXPECTED",
        argvalues=[
            (None, False),
            (True, False),
            (False, False),
            (0, False),
            (111, False),
            (111.222, False),
            ("str", False),
            (b"bytes", False),

            (((111, ),), False),
            (([111, ],), False),
            (({111, },), False),
            (({111: 222, },), False),

            (int, False),
            (int(1), False),
            (str, False),
            (str(1), False),

            (Exception, True),
            (Exception(), True),
            (Exx, True),
            (Exx(), True),

            (Cls, False),
            (Cls(), False),
            (ClsInt, False),
            (ClsInt(), False),    # int() == 0!!!

            (func, False),
            (func_lambda, False),
            (Cls.meth, False),
            (Cls().meth, False),
            (Cls.attr, False),
            (Cls().attr, False),

            *[(class_i, False) for class_i in CLASSES__AS_FUNC]
        ]
    )
    def test__check__exception(self, args, _EXPECTED):
        victim = self.Victim.check__exception
        pytest_func_tester__no_kwargs(victim, args, _EXPECTED)

    # -----------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        argnames="args, _EXPECTED",
        argvalues=[
            (("str", "str"), True),
            (("str", str), True),
            ((str, "str"), True),
            ((str, str), True),

            ((int, str), False),
            ((int, "str"), False),

            ((111, 111), True),
            ((int, 111), True),
            ((111, int), True),
            ((int, int), True),

            ((Exception, Exception), True),
            ((Exception(), Exception), True),
            ((Exception, Exception()), True),
            ((Exception(), Exception()), True),

            ((Exx, Exception), True),
            ((Exx(), Exception), True),
            ((Exx, Exception()), True),
            ((Exx(), Exception()), True),

            ((Exception, Exx), False),      # REMEMBER! not clear!
            ((Exception(), Exx), False),    # REMEMBER! not clear!
            ((Exception, Exx()), False),    # REMEMBER! not clear!
            ((Exception(), Exx()), False),  # REMEMBER! not clear!

            ((Cls, Cls), True),
            ((Cls, Cls()), True),
            ((Cls(), Cls), True),
            ((Cls(), Cls()), True),

            ((func, Cls), None),
            ((func, Cls()), None),
        ]
    )
    def test__check__nested__by_cls_or_inst(self, args, _EXPECTED):
        victim = self.Victim.check__nested__by_cls_or_inst
        pytest_func_tester__no_kwargs(victim, args, _EXPECTED)


# =====================================================================================================================
