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
