from typing import *
import re


# =====================================================================================================================
pass


# =====================================================================================================================
TYPE_ELEMENTARY_SINGLE: tuple = (
    type(None), bool,
    str, bytes,
    int, float,
)
TYPE_ELEMENTARY_COLLECTION: tuple = (
    tuple, list,
    set, dict,
)
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


# =====================================================================================================================
class ObjectInfo:
    MAX_VALUE_LEN: int = 100
    HIDE_BUILD_IN: bool = None
    HIDE_SKIPPED: bool = None

    SKIP_FULLNAMES = [
        # GIT
        "checkout", "detach",
        # threads
        "run", "start", "wait", "join", "terminate", "quit", "disconnect",
        # PyQt5 Qthread
        "exec", "exec_", "pyqtConfigure",
    ]
    SKIP_PARTNAMES = [
        # DANGER
        "init", "new", "create", "enter", "install",
        "set",
        "clone", "copy", "move",
        "next",
        "clear", "reduce",
        "close", "del", "exit", "kill",
    ]

    source: Any = None

    def __init__(self, source: Optional[Any] = None):
        self._groups_clear()
        self.source = source

    def _groups_clear(self) -> None:
        self.skipped_fullnames = []
        self.skipped_partnames = []

        self.properties_ok = {}
        self.properties_exx = {}
        self.objects = {}
        self.methods_ok = {}
        self.methods_exx = {}

    def _groups_reload(
            self,
            source: Optional[Any] = None,
            only_names_include: Union[None, str, List[str]] = None,
            hide_build_in: Optional[bool] = None,
            hide_skipped: Optional[bool] = None,
            skip_fullnames: Optional[List[str]] = None,
            skip_partnames: Optional[List[str]] = None,
            _log_iter: Optional[bool] = None
    ) -> None:
        self._groups_clear()

        # apply settings ----------------------------------
        if source is None:
            source = self.source
        if hide_build_in is None:
            hide_build_in = self.HIDE_BUILD_IN
        if hide_skipped is None:
            hide_skipped = self.HIDE_SKIPPED

        # WORK ----------------------------------
        name = "_log_iter(wait last touched)"
        print("-" * 10 + f"{name:-<90}")

        for pos, name in enumerate(dir(source), start=1):
            if _log_iter:
                print(f"{pos}\t\t{name}")

            # filter names -------------------------
            if hide_build_in and name.startswith("__"):
                continue

            if only_names_include:
                use_name = False
                if isinstance(only_names_include, str):
                    only_names_include = [only_names_include, ]
                for name_include_item in only_names_include:
                    if name_include_item.lower() in name.lower():
                        use_name = True
                        break
                if not use_name:
                    continue

            # SKIP -------------------------
            SKIP_FULLNAMES = []
            if self.SKIP_FULLNAMES:
                SKIP_FULLNAMES.extend(self.SKIP_FULLNAMES)
            if skip_fullnames:
                SKIP_FULLNAMES.extend(skip_fullnames)
            if name in SKIP_FULLNAMES:
                self.skipped_fullnames.append(name)
                continue

            SKIP_PARTNAMES = []
            if self.SKIP_PARTNAMES:
                SKIP_PARTNAMES.extend(self.SKIP_PARTNAMES)
            if skip_partnames:
                SKIP_PARTNAMES.extend(skip_partnames)
            if _value_search_by_list(source=name, search_list=SKIP_PARTNAMES):
                self.skipped_partnames.append(name)
                continue

            try:
                attr_obj = getattr(source, name)
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

            if self._check_type_is_elementary(attr_obj):
                value = attr_obj
                self.properties_ok.update({name: value})
            else:
                value = attr_obj
                self.objects.update({name: value})

    def _check_type_is_elementary(self, obj) -> bool:
        return isinstance(obj, TYPE_ELEMENTARY)

    # =================================================================================================================
    def print(
            self,
            source: Optional[Any] = None,
            max_value_len: Optional[int] = None,
            only_names_include: Union[None, str, List[str]] = None,
            hide_build_in: Optional[bool] = None,
            hide_skipped: Optional[bool] = None,
            skip_fullnames: Optional[List[str]] = None,
            skip_partnames: Optional[List[str]] = None,
            _log_iter: Optional[bool] = None
    ) -> None:
        """print all params from object
        if method - try to start it!

        :param _log_iter: useful when we have hidden exx! (pyqt5 for example!) you will get last name before sys.exit!
        """
        # apply settings ----------------------------------
        if source is None:
            source = self.source
        if max_value_len is None:
            max_value_len = self.MAX_VALUE_LEN

        # start printing ----------------------------------
        name = f"{self.__class__.__name__}.print"
        print("="*10 + f"{name.upper():=<90}")

        print(f"str(source)={str(source)}")
        print(f"repr(source)={repr(source)}")

        # SETTINGS ----------------------------------------
        name = "settings"
        print("-"*10 + f"{name.upper():-<90}")

        print(f"{skip_fullnames=}")
        print(f"{skip_partnames=}")
        print(f"{only_names_include=}")

        print(f"{hide_build_in=}")
        print(f"{hide_skipped=}")
        print(f"{_log_iter=}")

        # GROUPS ----------------------------------------
        self._groups_reload(
            source=source,
            only_names_include=only_names_include,
            hide_build_in=hide_build_in,
            hide_skipped=hide_skipped,
            skip_fullnames=skip_fullnames,
            skip_partnames=skip_partnames,
            _log_iter=_log_iter
        )

        # RESULTS ----------------------------------
        for batch_name in [
            "properties_ok", "properties_exx",
            "methods_ok", "methods_exx",
            "objects",
            "skipped_fullnames", "skipped_partnames",
        ]:
            print("-" * 10 + f"{batch_name:-<90}")
            if batch_name.startswith("skip"):
                if hide_skipped:
                    continue
                for name in getattr(self, batch_name):
                    print(name)
            else:
                postpone_collections: Dict = {}
                for name, value in getattr(self, batch_name).items():
                    if not name.startswith("__") and isinstance(value, TYPE_ELEMENTARY_COLLECTION):
                        postpone_collections.update({name: value})
                        continue
                    self._print_name_value(name, value, max_value_len)
                if postpone_collections:
                    print()
                for name, value in postpone_collections.items():
                    self._print_name_value(name, value, max_value_len)

        print("="*100)

    def _print_name_value(self, name, value, max_value_len: Optional[int] = None) -> None:
        if max_value_len is None:
            max_value_len = self.MAX_VALUE_LEN

        if self._check_type_is_elementary(value):
            if len(str(value)) > max_value_len:
                value = str(value)[:max_value_len - 3] + "..."
            print(f"{name:25}\t{value.__class__.__name__:10}:{value}")
        elif isinstance(value, (Exception, )):
            print(f"{name:25}\t{value.__class__.__name__:10}:{value!r}")
        else:
            for value_var in [f"str({str(value)})", f"repr({repr(value)})"]:
                if len(value_var) > max_value_len:
                    value = str(value_var)[:max_value_len - 3] + "..."
                if value_var.startswith("str"):
                    print(f"{name:25}\t{value.__class__.__name__:10}:{value_var}")
                else:
                    print(f"{' ':25}\t{value.__class__.__name__:10}:{value_var}")

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
        DONT USE IT! TOO COMPLICATED! this is only for history as first result from t8! -NEED DELETE!

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
                self.SKIP_FULLNAMES.extend(miss_names)

            # get VALUE
            if attr_str in self.SKIP_FULLNAMES:
                value = "***MISSED SPECIAL***"

            elif _value_search_by_list(source=attr_str, search_list=self.SKIP_PARTNAMES):
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


# =====================================================================================================================
