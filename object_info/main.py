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
    # SETTINGS --------------------------------------------
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

    # VALUES --------------------------------------------
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


# =====================================================================================================================
