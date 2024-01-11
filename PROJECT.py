from typing import *


# =====================================================================================================================
class PROJECT:
    # AUTHOR -----------------------------------------------
    AUTHOR_NAME: str = "Andrei Starichenko"
    AUTHOR_EMAIL: str = "centroid@mail.ru"
    AUTHOR_HOMEPAGE: str = "https://github.com/centroid457/"

    # PROJECT ----------------------------------------------
    NAME_INSTALL: str = "object-info"
    NAME_IMPORT: str = "object_info"
    KEYWORDS: List[str] = [
        "object info",
        "object attributes", "object properties", "object methods",
        "print attributes", "print properties", "print methods",
    ]

    # GIT --------------------------------------------------
    DESCRIPTION_SHORT: str = "print info about object (attributes+properties+methods results)"

    # README -----------------------------------------------
    DESCRIPTION_LONG: str = """
Designed to print info about object (properties+methods results)  

But why? if we can use debugger directly?  
Reason:  
1. to get and save standard text info,  
it useful to keep this info for future quick eye sight without exact condition like other OS or device/devlist/configuration 
2. in debugger we cant see result of methods!  
try to see for example information from platform module! it have only methods and no one in object tree in debugger!  
```python
import platform

obj = platform
print(platform.platform())
pass    # place debug point here
```  
3. Useful if you wish to see info from remote source if connecting directly over ssh for example  
    """
    FEATURES: List[str] = [
        # "feat1",
        # ["feat2", "block1", "block2"],

        "print all properties and methods results",
        "show exceptions on methods and properties",
        "skip names by full/part names",
        "separated collections in groups",
    ]

    # HISTORY -----------------------------------------------
    VERSION: str = "0.1.10"
    TODO: List[str] = [
        "..."
    ]
    FIXME: List[str] = [
        "..."
    ]
    NEWS: List[str] = [
        "..."
    ]


# =====================================================================================================================
if __name__ == '__main__':
    pass


# =====================================================================================================================
