from typing import *


# =====================================================================================================================
class TypeChecker:
    TYPES_ELEMENTARY_SINGLE: tuple = (
        type(None), bool,
        str, bytes,
        int, float,
    )
    TYPES_ELEMENTARY_COLLECTION: tuple = (
        tuple, list,
        set, dict,
    )
    TYPES_ELEMENTARY: tuple = (*TYPES_ELEMENTARY_SINGLE, *TYPES_ELEMENTARY_COLLECTION,)

    @staticmethod
    def check__name_is_build_in(name: str) -> bool:
        return name.startswith("__") and name.endswith("__")

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

    @staticmethod
    def check__elementary(source) -> bool:
        return isinstance(source, TypeChecker.TYPES_ELEMENTARY)

    @staticmethod
    def check__elementary_single(source) -> bool:
        return isinstance(source, TypeChecker.TYPES_ELEMENTARY_SINGLE)

    @staticmethod
    def check__elementary_collection(source) -> bool:
        return isinstance(source, TypeChecker.TYPES_ELEMENTARY_COLLECTION)

    @staticmethod
    def check__elementary_collection_not_dict(source) -> bool:
        return isinstance(source, TypeChecker.TYPES_ELEMENTARY_COLLECTION) and not isinstance(source, dict)

    @staticmethod
    def check__Exception(source) -> bool:
        return isinstance(source, Exception)

    @staticmethod
    def check__instance(source) -> bool:
        return not TypeChecker.check__elementary(source) and not TypeChecker.check__Exception(source)

    @staticmethod
    def check__class(source) -> bool:
        try:
            return issubclass(source, type)
        except:
            return False


# =====================================================================================================================
