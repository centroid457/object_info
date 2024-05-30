from typing import *


# =====================================================================================================================
class TypeChecker:
    TYPES__ELEMENTARY_SINGLE: tuple = (
        type(None), bool,
        str, bytes,
        int, float,
    )
    TYPES__ELEMENTARY_COLLECTION: tuple = (
        tuple, list,
        set, dict,
    )
    TYPES__ELEMENTARY: tuple = (*TYPES__ELEMENTARY_SINGLE, *TYPES__ELEMENTARY_COLLECTION,)

    # -----------------------------------------------------------------------------------------------------------------
    @staticmethod
    def check__name_is_build_in(name: str) -> bool:
        return name.startswith("__") and name.endswith("__") and len(name) > 4

    # -----------------------------------------------------------------------------------------------------------------
    @staticmethod
    def check__iterable(
            # self,
            source: Any,
            dict_as_iterable: bool = True,
            str_and_bytes_as_iterable: bool = True,
    ) -> bool:
        """checks if SOURCE is iterable.

        :param source: SOURCE data
        :param dict_as_iterable: if you dont want to use dict in your selecting,
            becouse maybe you need flatten all elements in list/set/tuple into one sequence
            and dict (as extended list) will be irrelevant!
        :param str_and_bytes_as_iterable: usually in data processing you need to work with str-type elements as OneSolid element
            but not iterating through chars!
        """
        if isinstance(source, dict):
            return dict_as_iterable
        elif isinstance(source, (str, bytes)):
            return str_and_bytes_as_iterable
        elif isinstance(source, (tuple, list, set,)):  # need to get it explicitly!!!
            return True
        elif hasattr(source, '__iter__') or hasattr(source, '__getitem__'):
            return True

        # FINAL ---------------------
        return False

    @staticmethod
    def check__iterable_but_not_str(source):
        """checks if SOURCE is iterable, but not exactly str!!!"""
        return TypeChecker.check__iterable(source, str_and_bytes_as_iterable=False)

    # -----------------------------------------------------------------------------------------------------------------
    @staticmethod
    def check__elementary(source) -> bool:
        return isinstance(source, TypeChecker.TYPES__ELEMENTARY)

    @staticmethod
    def check__elementary_single(source) -> bool:
        return isinstance(source, TypeChecker.TYPES__ELEMENTARY_SINGLE)

    @staticmethod
    def check__elementary_collection(source) -> bool:
        return isinstance(source, TypeChecker.TYPES__ELEMENTARY_COLLECTION)

    @staticmethod
    def check__elementary_collection_not_dict(source) -> bool:
        return isinstance(source, TypeChecker.TYPES__ELEMENTARY_COLLECTION) and not isinstance(source, dict)

    # CLASSES ---------------------------------------------------------------------------------------------------------
    @staticmethod
    def check__class(source: Any) -> bool:
        # return hasattr(source, "__class__")     # this is incorrect!!! tests get fail!
        try:
            return issubclass(source, object)
        except:
            return False

    @staticmethod
    def check__instance(source: Any) -> bool:
        return not TypeChecker.check__class(source)

    @staticmethod
    def check__exception(source) -> bool:
        """
        any of both variant (Instyance/Class) of any Exception!
        """
        if isinstance(source, Exception):
            return True
        try:
            return issubclass(source, Exception)
        except:
            pass
        return False

    @staticmethod
    def check__nested__by_cls_or_inst(source: Any, parent: Any) -> bool:
        """
        any of both variant (Instyance/Class) comparing with TARGET of both variant (Instyance/Class)
        """
        if TypeChecker.check__instance(source):
            source = source.__class__
        if TypeChecker.check__instance(parent):
            parent = parent.__class__
        return issubclass(source, parent)


# =====================================================================================================================