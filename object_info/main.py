from typing import *
import re
# from enum import Enum


# =====================================================================================================================
pass


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
        else:
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


# =====================================================================================================================
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


# =====================================================================================================================
class InternalItem(NamedTuple):
    KEY: str
    VALUE: str


# =====================================================================================================================
class ObjectState(NamedTuple):
    SKIPPED_FULLNAMES: List[str] = []
    SKIPPED_PARTNAMES: List[str] = []

    PROPERTIES_OK: Dict[str, Any] = {}
    PROPERTIES_OBJECTS: Dict[str, Any] = {}
    PROPERTIES_EXX: Dict[str, Exception] = {}

    METHODS_OK: Dict[str, Any] = {}
    METHODS_OBJECTS: Dict[str, Any] = {}
    METHODS_EXX: Dict[str, Exception] = {}


# =====================================================================================================================
class ObjectInfo:
    # SETTINGS --------------------------------------------

    # LOAD ------------------------------------------------
    MAX_VALUE_LEN: int = 100
    MAX_ITER_ITEMS: int = 5
    HIDE_BUILD_IN: bool = None
    LOG_ITER: bool = None

    NAMES__USE_ONLY_PARTS: List[str] = []
    NAMES__SKIP_FULL: List[str] = [
        # GIT
        "checkout", "detach",
        # threads
        "run", "start", "wait", "join", "terminate", "quit", "disconnect",
        # PyQt5 Qthread
        "exec", "exec_", "pyqtConfigure",
        # change collection content/count/order
        "pop", "popleft",
        "append", "appendleft",
        "extend", "extendleft",
        "add", "insert",
        "reverse", "rotate", "sort",
    ]
    NAMES__SKIP_PARTS: List[str] = [
        # DANGER
        "init", "new", "create", "enter", "install",
        "set",
        "clone", "copy", "move",
        "next",
        "clear", "reduce",
        "close", "del", "exit", "kill",
    ]

    # VALUES --------------------------------------------------
    ITEM_CLS: type[ObjectState] = ObjectState
    ITEM: ObjectState = ITEM_CLS()
    SOURCE: Any = None

    def __init__(
            self,
            source: Optional[Any] = None,

            # max_value_len: Optional[int] = None,
            # only_names_include: Union[None, str, List[str]] = None,
            # hide_build_in: Optional[bool] = None,
            # skip_fullnames: Optional[List[str]] = None,
            # skip_partnames: Optional[List[str]] = None,
            # log_iter: Optional[bool] = None
    ):
        self._groups__clear()

        if source is not None:
            self.SOURCE = source

    # =================================================================================================================
    def _groups__clear(self) -> None:
        self.ITEM = self.ITEM_CLS()

    def _groups__reload(self) -> None:
        self._groups__clear()

        # WORK --------------------------------------
        name = "log_iter(wait last touched)"
        self._print_line__group_separator(name)

        for pos, name in enumerate(dir(self.SOURCE), start=1):
            if self.LOG_ITER:
                print(f"{pos}:\t\t{name}")

            # filter names -------------------------
            if self.HIDE_BUILD_IN and TypeChecker.check__name_is_build_in(name):
                continue

            if self.NAMES__USE_ONLY_PARTS:
                use_name = False
                for name_include_item in self.NAMES__USE_ONLY_PARTS:
                    if name_include_item.lower() in name.lower():
                        use_name = True
                        break
                if not use_name:
                    continue

            # SKIP ----------------------------------
            SKIP_FULLNAMES = []
            if self.NAMES__SKIP_FULL:
                SKIP_FULLNAMES.extend(self.NAMES__SKIP_FULL)
            if SKIP_FULLNAMES:
                SKIP_FULLNAMES.extend(SKIP_FULLNAMES)
            if name in SKIP_FULLNAMES:
                self.ITEM.SKIPPED_FULLNAMES.append(name)
                continue

            SKIP_PARTNAMES = []
            if self.NAMES__SKIP_PARTS:
                SKIP_PARTNAMES.extend(self.NAMES__SKIP_PARTS)
            if SKIP_PARTNAMES:
                SKIP_PARTNAMES.extend(SKIP_PARTNAMES)
            if _value_search_by_list(source=name, search_list=SKIP_PARTNAMES):
                self.ITEM.SKIPPED_PARTNAMES.append(name)
                continue

            try:
                attr_obj = getattr(self.SOURCE, name)
            except Exception as exx:
                value = exx
                self.ITEM.PROPERTIES_EXX.update({name: value})
                continue

            if callable(attr_obj):
                try:
                    value = attr_obj()
                    self.ITEM.METHODS_OK.update({name: value})
                except Exception as exx:
                    value = exx
                    self.ITEM.METHODS_EXX.update({name: value})
                continue

            # print(f"{name=}/{attr_obj=}/type={type(attr_obj)}/elementary={isinstance(attr_obj, TYPES_ELEMENTARY)}")

            if TypeChecker.check__elementary(attr_obj):
                value = attr_obj
                self.ITEM.PROPERTIES_OK.update({name: value})
            else:
                value = attr_obj
                self.ITEM.PROPERTIES_OBJECTS.update({name: value})

    # =================================================================================================================
    def _print_line__group_separator(self, name: str) -> str:
        """
        GOAL MAIN - print!
        GOAL SECONDARY - return str - just for tests!!!
        """
        result = "-" * 10 + f"{name:-<90}"
        print(result)
        return result

    def _print_line__name_type_value(self, name: Optional[str] = None, value: Union[None, Any, InternalItem] = None, intend: Optional[int] = None) -> str:
        # -------------------------------
        name = name or ""
        block_name = f"{name:25}"

        # -------------------------------
        if isinstance(value, InternalItem):
            block_type = f"{value.KEY.__class__.__name__}:{value.VALUE.__class__.__name__}"
        elif value is None:
            block_type = f"None"
        else:
            block_type = f"{value.__class__.__name__}"

        # -------------------------------
        intend = intend or 0
        _block_intend = " " * intend

        # -------------------------------
        block_value = f"{value}"

        # -------------------------------
        result = f"{block_name}\t{block_type}:{_block_intend}{block_value}"
        # FIXME: FINISH!!!
        # FIXME: FINISH!!!
        # FIXME: FINISH!!!
        # FIXME: FINISH!!!
        # FIXME: FINISH!!!
        # FIXME: FINISH!!!
        # FIXME: FINISH!!!
        # FIXME: FINISH!!!
        # FIXME: FINISH!!!
        # FIXME: FINISH!!!







        if isinstance(value, InternalItem):
            name = ""
            result = f"{'':25}\t{value.KEY.__class__.__name__}:{value.VALUE.__class__.__name__}:{_block_intend}{value.KEY}:{value.VALUE}"

        if len(str(value)) > self.MAX_VALUE_LEN:
            value = str(value)[:self.MAX_VALUE_LEN - 3] + "..."

        result = f"{name:25}\t{value.__class__.__name__:10}:{_block_intend}{value}"
        print(result)
        return result

    # =================================================================================================================
    def _print_block__head(self) -> None:
        # apply settings ----------------------------------
        if self.MAX_VALUE_LEN is None:
            max_value_len = self.MAX_VALUE_LEN

        # start printing ----------------------------------
        name = f"{self.__class__.__name__}.print"
        self._print_line__group_separator(name.upper())

        print(f"str(SOURCE)={str(self.SOURCE)}")
        print(f"repr(SOURCE)={repr(self.SOURCE)}")

        # SETTINGS ----------------------------------------
        name = "SETTINGS"
        self._print_line__group_separator(name)

        print(f"{self.NAMES__SKIP_FULL=}")
        print(f"{self.NAMES__SKIP_PARTS=}")
        print(f"{self.NAMES__USE_ONLY_PARTS=}")

        print(f"{self.HIDE_BUILD_IN=}")
        print(f"{self.LOG_ITER=}")

    def _print_block__name_value(self, name, value) -> None:
        # WORK ---------------------------------------------------------------------------------
        self._print_line__name_type_value(name=name, value=value)
        if len(str(value)) <= self.MAX_VALUE_LEN:
            return

        if TypeChecker.check__elementary_single(value):
            return

        elif TypeChecker.check__elementary_collection(value):
            # start some pretty style -------------------------------------
            if not isinstance(value, dict):
                _index = 0
                for item in value:
                    _index += 1
                    if _index > self.MAX_ITER_ITEMS:
                        print(f"{' ':25}\t{' ':10}:...")
                        break

                    self._print_line__name_type_value(name=None, value=item, intend=4)

            elif isinstance(value, dict):
                _index = 0
                for item_key, item_value in value.items():
                    _index += 1
                    if _index > self.MAX_ITER_ITEMS:
                        print(f"{' ':25}\t{' ':10}:...")
                        break
                    self._print_line__name_type_value(name=None, value=item, intend=4)

                    print(f"{' ':25}\t{item_key.__class__.__name__}:{item_value.__class__.__name__:10}:{item_key}: {item_value}")

        elif isinstance(value, (Exception, )):
            print(f"{name:25}\t{value.__class__.__name__:10}:{value!r}")

        else:
            for value_var in [f"str({str(value)})", f"repr({repr(value)})"]:
                if len(value_var) > self.MAX_VALUE_LEN:
                    value = str(value_var)[:self.MAX_VALUE_LEN - 3] + "..."
                if value_var.startswith("str"):
                    print(f"{name:25}\t{value.__class__.__name__:10}:{value_var}")
                else:
                    print(f"{' ':25}\t{value.__class__.__name__:10}:{value_var}")


            for value_var in [f"str({str(value)})", f"repr({repr(value)})"]:
                if len(value_var) > self.MAX_VALUE_LEN:
                    value = str(value_var)[:self.MAX_VALUE_LEN - 3] + "..."
                if value_var.startswith("str"):
                    self._print_line__name_type_value(name=name, value=value_var)
                else:
                    self._print_line__name_type_value(name=None, value=value_var)

    # =================================================================================================================
    def print(self) -> None:
        """print all params from object
        if method - try to start it!
        """
        # GROUPS ----------------------------------------
        self._groups__reload()

        self._print_block__head()

        # RESULTS ----------------------------------
        for batch_name in [
            "properties_ok", "properties_exx",
            "methods_ok", "methods_exx",
            "objects",
            "skipped_fullnames", "skipped_partnames",
        ]:
            self._print_line__group_separator(batch_name)

            if batch_name.startswith("skip"):
                for name in getattr(self, batch_name):
                    print(name)
            else:
                postpone_collections: Dict = {}
                for name, value in getattr(self, batch_name).items():
                    if not name.startswith("__") and TypeChecker.check__elementary_collection(value):
                        postpone_collections.update({name: value})
                        continue
                    self._print_block__name_value(name, value)
                if postpone_collections:
                    print()
                for name, value in postpone_collections.items():
                    self._print_block__name_value(name, value)

        print("="*100)

    # =================================================================================================================
    def print_diffs(self) -> None:
        pass
        # TODO: FINISH!


# =====================================================================================================================
