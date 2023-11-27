from typing import *


# =====================================================================================================================
pass


# =====================================================================================================================
class ObjectInfo:
    obj: Any = None

    def __init__(self, obj: Any):
        self.obj = obj

    def print_object_info(self) -> None:
        print("="*50)
        print(f"str={str(self.obj)}")
        print("-"*50)
        print(f"repr={repr(self.obj)}")
        print("-"*50)

        for name in dir(self.obj):
            value = getattr(self.obj, name)
            if callable(value):
                try:
                    type_ = "M"
                    value = value()
                except:
                    type_ = "A"
                    value = "*ERROR*"
            print(f"{type_} {name:<20} {value!r}")
            if not isinstance(value, (str, int, float, set, tuple, list, dict, type(None))):
                print(f"{'':<22} {value}")

        print("*"*50)


# =====================================================================================================================
# FROM utilities
def obj_show_attr_all(source,
                      show_hidden=True,
                      go_nested_max=0,
                      go_iterables_max=1,
                      nested_skip_names=[],
                      miss_names=[],
                      _debug_mod=None,
                      _parents_list=[],
                      _print_step_element=False
                      ):    # starichenko
    """
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
                UFU.obj_show_attr_all(request, go_nested_max=0)

            2. add showing some another variants
                print(f"request=[{request}]")
                UFU.obj_show_attr_all(request, go_nested_max=0)

                print()
                print(f"request.node=[{request.node}]")
                UFU.obj_show_attr_all(request.node, go_nested_max=0)

        2=AVOID STOP ATTRIBUTS
            from PyQt5.QtWidgets import QApplication
            TESTING_OBJ = QApplication
            UFU.obj_show_attr_all(TESTING_OBJ)  #1=HERE WE WILL SEE UNEXPECTED STOP!
            UFU.obj_show_attr_all(TESTING_OBJ,_print_step_element=True)  #2=HERE WE WILL SEE UNEXPECTED STOP! with last used element NAME!
            UFU.obj_show_attr_all(TESTING_OBJ, miss_names=["aboutQt", ],_print_step_element=True)   #3=place STOP element in miss_names parameter and go to find next STOP elements!
            UFU.obj_show_attr_all(TESTING_OBJ, miss_names=["aboutQt", "beep", "fontMetrics", "pyqtConfigure", "exec", "exec_"])     #4=final usage


    EXAMPLE:
        UFU.obj_show_attr_all(QApplication,miss_names=["aboutQt", "beep", "fontMetrics", "pyqtConfigure", "exec", "exec_"])
    """
    if not _debug_mod:
        return

    nested_level = len(_parents_list)

    # START line
    if nested_level == 0:
        msg = f"{'/'*50} obj_show_attr_all {'/'*50}"
        print(msg)
    msg = f"{'/'*10} _parents_list={_parents_list} nested_level=[{nested_level}] source={source} {'/'*10}"
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
                    obj_show_attr_all(
                        source=item, show_hidden=show_hidden,
                        go_nested_max=go_nested_max, go_iterables_max=go_iterables_max,
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

        miss_danger_entries_list = [
            "init", "new", "create", "enter",
            "set",
            "clone", "copy", "move",
            "next",
            "close", "del", "exit", "clear", "reduce"
        ]

        miss_names_special = [
            # GIT
            "checkout",  "detach",
        ]
        if miss_names:
            miss_names_special.extend(miss_names)

        # get VALUE
        if attr_str in miss_names_special:
            value = "***MISSED SPECIAL***"

        elif value_search_by_list(source=attr_str, search_list=miss_danger_entries_list, search_type_1starts_2full_3ends_4any_5fullmatch=4):
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
            attr_or_meth = "obj"
            if nested_level < go_nested_max and not attr_str.startswith("__") and attr_str not in nested_skip_names:
                obj_show_attr_all(source=value, show_hidden=show_hidden, go_nested_max=go_nested_max,
                                        go_iterables_max=go_iterables_max, _parents_list=_parents_list + [attr_str, ])

            # if type_is_instance_of_any_user_class(source):
            #     obj_show_attr_all(value)
        if nested_level == 0:
            parents_str = ""
        else:
            parents_str = "." + '.'.join(_parents_list)
        msg = f"{attr_or_meth}=[{parents_str}.{attr_str}]".ljust(30+(10*(nested_level+1))) + f"value=[{value}]"
        print(msg)

    # FINAL LINE!
    if nested_level == 0:
        msg = f"{'/' * 100}"
        print(msg)
    return


# =====================================================================================================================
