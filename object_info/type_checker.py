from typing import *


# =====================================================================================================================
@final
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
    def check__bool_none(source: Any) -> bool:
        """
        GOAL
        ----
        help in case of
            assert 0 == False
            assert 1 == True
            assert 2 == False   # unclear!!!

        CREATED SPECIALLY FOR
        ---------------------
        funcs_aux.Valid.compare_doublesided
        """
        return isinstance(source, (bool, type(None)))

    @staticmethod
    def check__elementary(source: Any) -> bool:
        if callable(source):
            return False
        return isinstance(source, TypeChecker.TYPES__ELEMENTARY)

    @staticmethod
    def check__elementary_single(source: Any) -> bool:
        return isinstance(source, TypeChecker.TYPES__ELEMENTARY_SINGLE)

    @staticmethod
    def check__elementary_single_not_none(source: Any) -> bool:
        """
        its just an Idea!!!

        GOAL
        ----
        prepare to work with ensure_collection
        None assumed as not Passed value! so we can ensure to return None -> ()

        SPECIALLY CREATED FOR
        ---------------------
        ensure_collection somewhere!
        """
        return TypeChecker.check__elementary_single(source) and source is not None

    @staticmethod
    def check__elementary_collection(source: Any) -> bool:
        return isinstance(source, TypeChecker.TYPES__ELEMENTARY_COLLECTION)

    @staticmethod
    def check__elementary_collection_not_dict(source: Any) -> bool:
        return isinstance(source, TypeChecker.TYPES__ELEMENTARY_COLLECTION) and not isinstance(source, dict)

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
    def check__iterable_not_str(source: Any) -> bool:
        """
        GOAL
        ----
        checks if SOURCE is iterable, but not exactly str!!!

        NOTE
        ----
        DONT USE FOR ensure_collection! instead prefer check__elementary_single
        """
        return TypeChecker.check__iterable(source, str_and_bytes_as_iterable=False)

    # CLASSES ---------------------------------------------------------------------------------------------------------
    @staticmethod
    def check__class(source: Any) -> bool:
        """
        works both for funcs/meths for any Сды/Штые1 see tests test__check__class
        """
        # return hasattr(source, "__class__")     # this is incorrect!!! tests get fail!
        try:
            return issubclass(source, object)
        except:
            return False

    @staticmethod
    def check__func_or_meth(source: Any) -> bool:
        """
        creates specially for detect all funcs like func/meth/or even DescriptedClasses (it is class but actually used like func!)
        recommended using instead of just Callable! cause Callable keeps additionally every class instead of just simple func/method!
        """
        if TypeChecker.check__class(source):
            result = issubclass(source, TypeChecker.TYPES__ELEMENTARY)
        else:
            result = callable(source)
        return result

    @staticmethod
    def check__instance(source: Any) -> bool:
        return not TypeChecker.check__class(source) and not TypeChecker.check__func_or_meth(source)

    @staticmethod
    def check__instance_not_elementary(source: Any) -> bool:
        return TypeChecker.check__instance(source) and not TypeChecker.check__elementary(source)

    @staticmethod
    def check__exception(source: Any) -> bool:
        """
        any of both variant (Instance/Class) of any Exception!
        """
        if isinstance(source, Exception):
            return True
        try:
            return issubclass(source, Exception)
        except:
            pass
        return False

    @staticmethod
    def check__nested__by_cls_or_inst(source: Any, parent: Any) -> bool | None:
        """
        any of both variant (Instance/Class) comparing with TARGET of both variant (Instance/Class)

        specially created for pytest_aux for comparing with Exception!
        """
        if TypeChecker.check__instance(source):
            source = source.__class__
        if TypeChecker.check__instance(parent):
            parent = parent.__class__

        if not TypeChecker.check__class(source) or not TypeChecker.check__class(parent):
            return None

        return issubclass(source, parent)


# =====================================================================================================================
