# object_info
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
3. useful if you wish to see info from remote source if connecting directly over ssh for example

## Features
1. print all properties and methods results
2. show exceptions on methods and properties
3. skip names by full/part name

## License
See the [LICENSE](LICENSE) file for license rights and limitations (MIT).


## Release history
See the [HISTORY.md](HISTORY.md) file for release history.


## Installation
```commandline
pip install object-info
```

## Import

```python
from object_info import *
```


## GUIDE

### USAGE

```python
from object_info import *

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


ObjectInfo(Cls1()).print()
ObjectInfo().print(Cls1())
"""
==========OBJECTINFO.PRINT==========================================================================
str=<__main__.Cls1 object at 0x000001D1B0468650>
repr=<__main__.Cls1 object at 0x000001D1B0468650>
----------properties_ok-----------------------------------------------------------------------------
__dict__                 	dict      :{}
__doc__                  	NoneType  :None
__module__               	str       :__main__
__weakref__              	NoneType  :None
attrDict                 	dict      :{1: 1}
attrFloat                	int       :2
attrInt                  	int       :1
attrList                 	list      :[1, 2, 3]
attrListObj              	list      :[<__main__.Cls0 object at 0x000001D1B0468380>, <__main__.Cls0 object at 0x000001D1B0468590>, 1]
attrNone                 	NoneType  :None
attrSet                  	set       :{1, 2, 3}
propertyInt              	int       :1
----------properties_exx----------------------------------------------------------------------------
propertyExx              	Exception :exxMsg
----------methods_ok--------------------------------------------------------------------------------
__class__                	Cls1      :<__main__.Cls1 object at 0x000001D1B0468A70>
__dir__                  	str       :['__module__', 'attrMissFullName', 'attrMissPartName', 'attrNone', 'attrInt', 'attrFloat', 'attrC...
__getstate__             	NoneType  :None
__hash__                 	int       :125007325285
__repr__                 	str       :<__main__.Cls1 object at 0x000001D1B0468650>
__sizeof__               	int       :16
__str__                  	str       :<__main__.Cls1 object at 0x000001D1B0468650>
__subclasshook__         	NotImplementedType:NotImplemented
attrClass                	Cls0      :<__main__.Cls0 object at 0x000001D1B0468CB0>
methInt                  	int       :1
----------methods_exx-------------------------------------------------------------------------------
__eq__                   	TypeError :expected 1 argument, got 0
__format__               	TypeError :Cls1.__format__() takes exactly one argument (0 given)
__ge__                   	TypeError :expected 1 argument, got 0
__getattribute__         	TypeError :expected 1 argument, got 0
__gt__                   	TypeError :expected 1 argument, got 0
__le__                   	TypeError :expected 1 argument, got 0
__lt__                   	TypeError :expected 1 argument, got 0
__ne__                   	TypeError :expected 1 argument, got 0
methExx                  	Exception :exxMsg
----------objects-----------------------------------------------------------------------------------
attrObj                  	Cls0      :str(<__main__.Cls0 object at 0x000001D1B03F5B20>)
                         	Cls0      :repr(<__main__.Cls0 object at 0x000001D1B03F5B20>)
----------skipped-----------------------------------------------------------------------------------
attrMissFullName
----------skipped_danger----------------------------------------------------------------------------
__delattr__
__init__
__init_subclass__
__new__
__reduce__
__reduce_ex__
__setattr__
attrMissPartName
====================================================================================================
"""

ObjectInfo(Cls1()).print(only_names_include="attr", hide_build_in=True, hide_skipped=True)
"""
==========OBJECTINFO.PRINT==========================================================================
INCLUDE names [attr]
str=<__main__.Cls1 object at 0x000001831C08C770>
repr=<__main__.Cls1 object at 0x000001831C08C770>
----------properties_ok-----------------------------------------------------------------------------
attrDict                 	dict      :{1: 1}
attrFloat                	int       :2
attrInt                  	int       :1
attrList                 	list      :[1, 2, 3]
attrListObj              	list      :[<__main__.Cls0 object at 0x000001831C08C4A0>, <__main__.Cls0 object at 0x000001831C08C6B0>, 1]
attrNone                 	NoneType  :None
attrSet                  	set       :{1, 2, 3}
----------properties_exx----------------------------------------------------------------------------
----------methods_ok--------------------------------------------------------------------------------
attrClass                	Cls0      :<__main__.Cls0 object at 0x000001831C08CB90>
----------methods_exx-------------------------------------------------------------------------------
----------objects-----------------------------------------------------------------------------------
attrObj                  	Cls0      :str(<__main__.Cls0 object at 0x000001831C0CEED0>)
                         	Cls0      :repr(<__main__.Cls0 object at 0x000001831C0CEED0>)
====================================================================================================
"""
```
