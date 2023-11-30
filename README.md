# object_info
Designed to print info about object (properties+methods results)

But why? if we can use debugger directly?
Reason:
1. to get and save standard text info,  
it useful to keep this info for future quick eye sight without exact condition like other OS or device/devlist/configuration 
2. in debugger we cant see result of methods!
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


ObjectInfo(Cls1()).print_object_info()
ObjectInfo().print_object_info(Cls1())
"""
==========PRINT_OBJECT_INFO=========================================================================
str=<__main__.Cls1 object at 0x000002103087D130>
repr=<__main__.Cls1 object at 0x000002103087D130>
----------properties_ok-----------------------------------------------------------------------------
__dict__                 	dict      :{}
__doc__                  	NoneType  :None
__module__               	str       :__main__
__weakref__              	NoneType  :None
attrDict                 	dict      :{1: 1}
attrFloat                	int       :2
attrInt                  	int       :1
attrList                 	list      :[1, 2, 3]
attrListObj              	list      :[<__main__.Cls0 object at 0x000002103087C8F0>, <__main__.Cls0 object at 0x000002103087C950>, 1]
attrNone                 	NoneType  :None
attrSet                  	set       :{1, 2, 3}
propertyInt              	int       :1
----------properties_exx----------------------------------------------------------------------------
propertyExx              	Exception :exxMsg
----------objects-----------------------------------------------------------------------------------
attrObj                  	Cls0      :<__main__.Cls0 object at 0x0000021030873440>
----------methods_ok--------------------------------------------------------------------------------
__class__                	Cls1      :<__main__.Cls1 object at 0x000002103087DF70>
__dir__                  	str       :['__module__', 'attrMissFullName', 'attrMissPartName', 'attrNone', 'attrInt', 'attrFloat', 'attrC...
__getstate__             	NoneType  :None
__hash__                 	int       :141784808723
__repr__                 	str       :<__main__.Cls1 object at 0x000002103087D130>
__sizeof__               	int       :16
__str__                  	str       :<__main__.Cls1 object at 0x000002103087D130>
__subclasshook__         	NotImplementedType:NotImplemented
attrClass                	Cls0      :<__main__.Cls0 object at 0x000002103087E120>
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
```
