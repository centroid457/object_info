from typing import *
import re


# =====================================================================================================================
pass


# =====================================================================================================================
TYPE_ELEMENTARY_SINGLE: tuple = (type(None), bool, str, bytes, int, float, )
TYPE_ELEMENTARY_COLLECTION: tuple = (set, list, dict, )
TYPE_ELEMENTARY: tuple = (*TYPE_ELEMENTARY_SINGLE, *TYPE_ELEMENTARY_COLLECTION, )


def _value_search_by_list(source=None, search_list=[]):
    match_item = None

    for search_item in search_list:
        try:
            result = search_item in source
        except:
            result = source == search_item

        if result:
            match_item = search_item
            break
    return match_item


def type_is_iterable(source, dict_as_iterable=True, str_and_bytes_as_iterable=True):
    """checks if source is iterable.

    :param source: source data
    :param dict_as_iterable: if you dont want to use dict in your selecting,
        becouse maybe you need flatten all elements in list/set/tuple into one sequence
        and dict (as extended list) will be irrelevant!
    :param str_as_iterable: usually in data processing you need to work with str-type elements as OneSolid element
        but not iterating through chars!
    """
    if isinstance(source, dict):
        return dict_as_iterable
    elif isinstance(source, (str, bytes)):
        return str_and_bytes_as_iterable
    elif isinstance(source, (tuple, list, set, )):    # need to get it explicitly!!!
        return True
    elif hasattr(source, '__iter__') or hasattr(source, '__getitem__'):
        return True
    else:
        return False


def type_is_iterable_but_not_str(source):
    """checks if source is iterable, but not exactly str!!!"""
    return type_is_iterable(source, str_and_bytes_as_iterable=False)


def type_is_elementary_single(source):
    """ check object for Elementary type, Not collection, only separate single element
    not iterable except str!

    str/int/float/NoneType/bool - True
    not any objects/otherIterabled - False
    """
    return isinstance(source, TYPE_ELEMENTARY_SINGLE)


names_miss_fullnames = [
    # TEST
    "attrMissFullName",
    # GIT
    "checkout", "detach",
]


names_danger_entries = [
    # TEST
    "MissPartName",

    # MAIN
    "init", "new", "create", "enter",
    "set",
    "clone", "copy", "move",
    "next",
    "close", "del", "exit", "clear", "reduce"
]


# =====================================================================================================================
class ObjectInfo:
    source: Any = None

    def __init__(self, source: Any):
        self.source = source

    # =================================================================================================================
    def print_object_info(self) -> None:
        """print all params from object
        if method - try to start it!
        """
        self.skipped = []
        self.skipped_danger = []

        self.properties_ok = {}
        self.properties_exx = {}
        self.objects = {}
        self.methods_ok = {}
        self.methods_exx = {}

        print("="*50 + "print_object_info")
        print(f"str={str(self.source)}")
        print(f"repr={repr(self.source)}")
        # print("-"*50)

        for name in dir(self.source):
            # SKIP
            if name in names_miss_fullnames:
                self.skipped.append(name)
                continue
            if _value_search_by_list(source=name, search_list=names_danger_entries):
                self.skipped_danger.append(name)
                continue

            try:
                attr_obj = getattr(self.source, name)
            except Exception as exx:
                value = exx
                self.properties_exx.update({name: value})
                continue

            if callable(attr_obj):
                try:
                    value = attr_obj()
                    self.methods_ok.update({name: value})
                except Exception as exx:
                    value = exx
                    self.methods_exx.update({name: value})
                continue

            # print(f"{name=}/{attr_obj=}/type={type(attr_obj)}/elementary={isinstance(attr_obj, TYPE_ELEMENTARY)}")

            if isinstance(attr_obj, TYPE_ELEMENTARY):
                value = attr_obj
                self.properties_ok.update({name: value})
            else:
                value = attr_obj
                self.objects.update({name: value})

        for batch_name in ["properties_ok", "properties_exx", "objects", "methods_ok", "methods_exx"]:
            print("-" * 10 + f"[{batch_name}]" + "-" * 50)
            for name, value in getattr(self, batch_name).items():
                print(f"{name:25}\t{value.__class__.__name__:10}:{value}")

        for batch_name in ["skipped", "skipped_danger"]:
            print("-" * 10 + f"[{batch_name}]" + "-" * 50)
            for name in getattr(self, batch_name):
                print(name)

        print("="*50)

    # =================================================================================================================
    def _print_object_info__deep(
            self,
            show_hidden=True,
            go_nested_max=0,
            go_iterables_max=1,
            nested_skip_names=[],
            miss_names=[],
            _parents_list=[],
            _print_step_element=False,
        ):
        """
        DONT USE IT! TOO COMPLICATED!

        Show structure of object with all names of attributes and string values.
        useful if you want to find out exact info in object or get know if it have not!!!

        But in some situations standart debugger will not help!
            Try to find methods and attributes for pyQt QApplication!!! - will not show! otherwice this method will work correct!

        you can instead use STANDARD PYCHARM DEBUGGER to inspect OBJECT in convenient tree-stile!
            1. create concrete object or its part (give a name to object)
            2. PLACE A STOP POINT on it code
            3. explore elements in the Tree!!!

        BUT sometimes it cant show you exact nested elements!

        :param show_hidden: only show/hide in log!!! in any case not recommended go inside!
        :param go_nested_max:
        :param go_iterables_max: if source is as iterable type - iterate items!
        :param _print_step_element: recommended in first starts! so to find elements wich will cause stops or errors!

        HOW TO USE (steps):
            1=EXPLORER EXACT TREE ELEMENTS
                1. use it ones to see items/values
                    print(f"request=[{request}]")
                    UFU.print_object_info_pro(request, go_nested_max=0)

                2. add showing some another variants
                    print(f"request=[{request}]")
                    UFU.print_object_info_pro(request, go_nested_max=0)

                    print()
                    print(f"request.node=[{request.node}]")
                    UFU.print_object_info_pro(request.node, go_nested_max=0)

            2=AVOID STOP ATTRIBUTS
                from PyQt5.QtWidgets import QApplication
                TESTING_OBJ = QApplication
                UFU.print_object_info_pro(TESTING_OBJ)  #1=HERE WE WILL SEE UNEXPECTED STOP!
                UFU.print_object_info_pro(TESTING_OBJ,_print_step_element=True)  #2=HERE WE WILL SEE UNEXPECTED STOP! with last used element NAME!
                UFU.print_object_info_pro(TESTING_OBJ, miss_names=["aboutQt", ],_print_step_element=True)   #3=place STOP element in miss_names parameter and go to find next STOP elements!
                UFU.print_object_info_pro(TESTING_OBJ, miss_names=["aboutQt", "beep", "fontMetrics", "pyqtConfigure", "exec", "exec_"])     #4=final usage


        EXAMPLE:
            UFU.print_object_info_pro(QApplication,miss_names=["aboutQt", "beep", "fontMetrics", "pyqtConfigure", "exec", "exec_"])
        """
        source = self.source

        nested_level = len(_parents_list)

        # START line
        if nested_level == 0:
            msg = f"{'/' * 50} print_object_info_pro {'/' * 50}"
            print(msg)
        msg = f"{'/' * 10} _parents_list={_parents_list} nested_level=[{nested_level}] source={source} {'/' * 10}"
        print(msg)

        # 1=ELEMENTARY types -------------------------------------------------------------------------------------
        if type_is_elementary_single(source):
            msg = f"ELEMTARY SINGLE TYPE source=[{source}]"
            print(msg)
            return

        # 2=ITERABLE types ---------------------------------------------------------------------------------------
        if type_is_iterable_but_not_str(source):
            source_len = len(source)
            msg = f"ITERABLE TYPE len=[{source_len}] source=[{source}]!"
            print(msg)
            if source_len > 0 and go_iterables_max:
                i = 0
                for item in source:
                    if i >= go_iterables_max:
                        break
                    i += 1
                    if type_is_elementary_single(item):
                        msg = f"ELEMTARY SINGLE TYPE item=[{item}]"
                        print(msg)
                    else:
                        self.__class__(item)._print_object_info__deep(
                            show_hidden=show_hidden,
                            go_nested_max=go_nested_max,
                            go_iterables_max=go_iterables_max,
                            _parents_list=_parents_list + [str(nested_level)])
            return

        # 3=exact WORKING! attributes and methods ----------------------------------------------------------------
        # print(f"[{dir(source)=}]")
        for attr_str in dir(source):
            if _print_step_element:
                print(f"\t{attr_str=}")

            if not show_hidden and attr_str.startswith("__"):
                continue

            if nested_level != 0 and attr_str == _parents_list[-1]:
                continue

            if miss_names:
                names_miss_fullnames.extend(miss_names)

            # get VALUE
            if attr_str in names_miss_fullnames:
                value = "***MISSED SPECIAL***"

            elif _value_search_by_list(source=attr_str, search_list=names_danger_entries):
                value = "***MISSED DANGER***"

            else:
                try:
                    value = getattr(source, attr_str)
                except:
                    value = "***EXCEPTION***"

            # determine TYPE!
            if type_is_elementary_single(value):
                attr_or_meth = "attr"

            elif callable(value):
                attr_or_meth = "meth"
                if attr_or_meth.startswith("__"):
                    value = "***MISSED HIDDEN CALLABLE DANGER***"
                else:
                    try:
                        value = value()
                    except:
                        pass

            else:
                attr_or_meth = "obj "
                if nested_level < go_nested_max and not attr_str.startswith("__") and attr_str not in nested_skip_names:
                    self.__class__(value)._print_object_info__deep(
                        show_hidden=show_hidden,
                        go_nested_max=go_nested_max,
                        go_iterables_max=go_iterables_max,
                        _parents_list=_parents_list + [attr_str, ]
                    )

                # if type_is_instance_of_any_user_class(source):
                #     self.print_object_info_pro(value)
            if nested_level == 0:
                parents_str = ""
            else:
                parents_str = "." + '.'.join(_parents_list)
            msg = f"{attr_or_meth}=[{parents_str}.{attr_str}]".ljust(
                30 + (10 * (nested_level + 1))) + f"value=[{value}]"
            print(msg)

        # FINAL LINE!
        if nested_level == 0:
            msg = f"{'/' * 100}"
            print(msg)
        return


# VISUAL TESTS ========================================================================================================
class Cls0:
    attr1=1


class Cls1:
    attrMissFullName = "attrMissFullName"
    attrMissPartName = "MissPartName"
    attrNone = None
    attrInt = 1
    attrFloat = 2
    attrClass = Cls0
    attrObj = Cls0()
    attrSet = {1,2,3}
    attrList = [1,2,3]
    attrDict = {1:1}
    attrListObj = [Cls0(), Cls0(), 1]
    @property
    def propertyInt(self):
        return 1
    @property
    def propertyExx(self):
        raise Exception("exxMsg")
    def methInt(self):
        return 1
    def methExx(self):
        raise Exception("exxMsg")


if __name__ == "__main__":
    ObjectInfo(Cls1()).print_object_info()
"""
==================================================print_object_info
str=<__main__.Cls1 object at 0x000001F6BFE13FE0>
repr=<__main__.Cls1 object at 0x000001F6BFE13FE0>
----------[properties_ok]--------------------------------------------------
__dict__                 	dict      :{}
__doc__                  	NoneType  :None
__module__               	str       :__main__
__weakref__              	NoneType  :None
attrDict                 	dict      :{1: 1}
attrFloat                	int       :2
attrInt                  	int       :1
attrList                 	list      :[1, 2, 3]
attrListObj              	list      :[<__main__.Cls0 object at 0x000001F6BFE126C0>, <__main__.Cls0 object at 0x000001F6BFE13F20>, 1]
attrNone                 	NoneType  :None
attrSet                  	set       :{1, 2, 3}
propertyInt              	int       :1
----------[properties_exx]--------------------------------------------------
propertyExx              	Exception :exxMsg
----------[objects]--------------------------------------------------
attrObj                  	Cls0      :<__main__.Cls0 object at 0x000001F6BFE12B70>
----------[methods_ok]--------------------------------------------------
__class__                	Cls1      :<__main__.Cls1 object at 0x000001F6BFE09070>
__dir__                  	list      :['__module__', 'attrMissFullName', 'attrMissPartName', 'attrNone', 'attrInt', 'attrFloat', 'attrClass', 'attrObj', 'attrSet', 'attrList', 'attrDict', 'attrListObj', 'propertyInt', 'propertyExx', 'methInt', 'methExx', '__dict__', '__weakref__', '__doc__', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__reduce_ex__', '__reduce__', '__getstate__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
__getstate__             	NoneType  :None
__hash__                 	int       :134955799550
__repr__                 	str       :<__main__.Cls1 object at 0x000001F6BFE13FE0>
__sizeof__               	int       :16
__str__                  	str       :<__main__.Cls1 object at 0x000001F6BFE13FE0>
__subclasshook__         	NotImplementedType:NotImplemented
attrClass                	Cls0      :<__main__.Cls0 object at 0x000001F6BFE09760>
methInt                  	int       :1
----------[methods_exx]--------------------------------------------------
__eq__                   	TypeError :expected 1 argument, got 0
__format__               	TypeError :Cls1.__format__() takes exactly one argument (0 given)
__ge__                   	TypeError :expected 1 argument, got 0
__getattribute__         	TypeError :expected 1 argument, got 0
__gt__                   	TypeError :expected 1 argument, got 0
__le__                   	TypeError :expected 1 argument, got 0
__lt__                   	TypeError :expected 1 argument, got 0
__ne__                   	TypeError :expected 1 argument, got 0
methExx                  	Exception :exxMsg
----------[skipped]--------------------------------------------------
attrMissFullName
----------[skipped_danger]--------------------------------------------------
__delattr__
__init__
__init_subclass__
__new__
__reduce__
__reduce_ex__
__setattr__
attrMissPartName
==================================================
"""