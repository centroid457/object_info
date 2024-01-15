# object_info (v0.1.12)

## DESCRIPTION_SHORT
Print info about object (attributes+properties+methods results)

## DESCRIPTION_LONG
designed to print info about object (properties+methods results)  

but why? if we can use debugger directly?  
reason:  
1. to get and save standard text info,  
it useful to keep this info for future quick eye sight without exact condition like other os or device/devlist/configuration 
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
3. skip names by full/part names  
4. separated collections in groups  


********************************************************************************
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


********************************************************************************
## USAGE EXAMPLES
See tests and sourcecode for other examples.

------------------------------
### 1. example1.py
```python
from object_info import *

class Cls0:
    attr1=1

class Cls1:
    attrSkipFullName = "attrSkipFullName"
    attrSkipPartName = "SkipPartName"
    attrNone = None
    attrInt = 1
    attrFloat = 2.2
    attrClass = Cls0
    attrObj = Cls0()
    attrSet = {1,2,3}
    attrList = [1,2,3]
    attrTuple = (1,2,3)
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


# ObjectInfo(Cls1()).print()
# ObjectInfo().print(Cls1())
ObjectInfo(Cls1()).print(
    _log_iter=True,
    only_names_include=[],
    skip_fullnames=["attrSkipFullName", ],
    skip_partnames=["SkipPartName", ],
    hide_build_in=None,
    hide_skipped=None,
)

"""
==========OBJECTINFO.PRINT==========================================================================
str(source)=<__main__.Cls1 object at 0x0000014AFAC606E0>
repr(source)=<__main__.Cls1 object at 0x0000014AFAC606E0>
----------SETTINGS----------------------------------------------------------------------------------
skip_fullnames=['attrSkipFullName']
skip_partnames=['SkipPartName']
only_names_include=[]
hide_build_in=None
hide_skipped=None
_log_iter=True
----------_log_iter(wait last touched)--------------------------------------------------------------
1		__class__
2		__delattr__
3		__dict__
4		__dir__
5		__doc__
6		__eq__
7		__format__
8		__ge__
9		__getattribute__
10		__getstate__
11		__gt__
12		__hash__
13		__init__
14		__init_subclass__
15		__le__
16		__lt__
17		__module__
18		__ne__
19		__new__
20		__reduce__
21		__reduce_ex__
22		__repr__
23		__setattr__
24		__sizeof__
25		__str__
26		__subclasshook__
27		__weakref__
28		attrClass
29		attrDict
30		attrFloat
31		attrInt
32		attrList
33		attrListObj
34		attrNone
35		attrObj
36		attrSet
37		attrSkipFullName
38		attrSkipPartName
39		attrTuple
40		methExx
41		methInt
42		propertyExx
43		propertyInt
----------properties_ok-----------------------------------------------------------------------------
__dict__                 	dict      :{}
__doc__                  	NoneType  :None
__module__               	str       :__main__
__weakref__              	NoneType  :None
attrFloat                	float     :2.2
attrInt                  	int       :1
attrNone                 	NoneType  :None
propertyInt              	int       :1

attrDict                 	dict      :{1: 1}
attrList                 	list      :[1, 2, 3]
attrListObj              	list      :[<__main__.Cls0 object at 0x0000014AFAC60320>, <__main__.Cls0 object at 0x0000014AFAC60830>, 1]
attrSet                  	set       :{1, 2, 3}
attrTuple                	tuple     :(1, 2, 3)
----------properties_exx----------------------------------------------------------------------------
propertyExx              	Exception :Exception('exxMsg')
----------methods_ok--------------------------------------------------------------------------------
__class__                	Cls1      :str(<__main__.Cls1 object at 0x0000014AFAC61220>)
                         	Cls1      :repr(<__main__.Cls1 object at 0x0000014AFAC61220>)
__dir__                  	str       :['__module__', 'attrSkipFullName', 'attrSkipPartName', 'attrNone', 'attrInt', 'attrFloat', 'attrC...
__getstate__             	NoneType  :None
__hash__                 	int       :88846655598
__repr__                 	str       :<__main__.Cls1 object at 0x0000014AFAC606E0>
__sizeof__               	int       :16
__str__                  	str       :<__main__.Cls1 object at 0x0000014AFAC606E0>
__subclasshook__         	NotImplementedType:str(NotImplemented)
                         	NotImplementedType:repr(NotImplemented)
attrClass                	Cls0      :str(<__main__.Cls0 object at 0x0000014AFAC63E60>)
                         	Cls0      :repr(<__main__.Cls0 object at 0x0000014AFAC63E60>)
methInt                  	int       :1
----------methods_exx-------------------------------------------------------------------------------
__eq__                   	TypeError :TypeError('expected 1 argument, got 0')
__format__               	TypeError :TypeError('Cls1.__format__() takes exactly one argument (0 given)')
__ge__                   	TypeError :TypeError('expected 1 argument, got 0')
__getattribute__         	TypeError :TypeError('expected 1 argument, got 0')
__gt__                   	TypeError :TypeError('expected 1 argument, got 0')
__le__                   	TypeError :TypeError('expected 1 argument, got 0')
__lt__                   	TypeError :TypeError('expected 1 argument, got 0')
__ne__                   	TypeError :TypeError('expected 1 argument, got 0')
methExx                  	Exception :Exception('exxMsg')
----------objects-----------------------------------------------------------------------------------
attrObj                  	Cls0      :str(<__main__.Cls0 object at 0x0000014AFAC60410>)
                         	Cls0      :repr(<__main__.Cls0 object at 0x0000014AFAC60410>)
----------skipped_fullnames-------------------------------------------------------------------------
attrSkipFullName
----------skipped_partnames-------------------------------------------------------------------------
__delattr__
__init__
__init_subclass__
__new__
__reduce__
__reduce_ex__
__setattr__
attrSkipPartName
====================================================================================================
"""

ObjectInfo(Cls1()).print(only_names_include="attr")
"""
==========OBJECTINFO.PRINT==========================================================================
str(source)=<__main__.Cls1 object at 0x0000014AFAC60650>
repr(source)=<__main__.Cls1 object at 0x0000014AFAC60650>
----------SETTINGS----------------------------------------------------------------------------------
skip_fullnames=None
skip_partnames=None
only_names_include='attr'
hide_build_in=None
hide_skipped=None
_log_iter=None
----------_log_iter(wait last touched)--------------------------------------------------------------
----------properties_ok-----------------------------------------------------------------------------
attrFloat                	float     :2.2
attrInt                  	int       :1
attrNone                 	NoneType  :None
attrSkipFullName         	str       :attrSkipFullName
attrSkipPartName         	str       :SkipPartName

attrDict                 	dict      :{1: 1}
attrList                 	list      :[1, 2, 3]
attrListObj              	list      :[<__main__.Cls0 object at 0x0000014AFAC60320>, <__main__.Cls0 object at 0x0000014AFAC60830>, 1]
attrSet                  	set       :{1, 2, 3}
attrTuple                	tuple     :(1, 2, 3)
----------properties_exx----------------------------------------------------------------------------
----------methods_ok--------------------------------------------------------------------------------
attrClass                	Cls0      :str(<__main__.Cls0 object at 0x0000014AFAC701A0>)
                         	Cls0      :repr(<__main__.Cls0 object at 0x0000014AFAC701A0>)
----------methods_exx-------------------------------------------------------------------------------
__getattribute__         	TypeError :TypeError('expected 1 argument, got 0')
----------objects-----------------------------------------------------------------------------------
attrObj                  	Cls0      :str(<__main__.Cls0 object at 0x0000014AFAC60410>)
                         	Cls0      :repr(<__main__.Cls0 object at 0x0000014AFAC60410>)
----------skipped_fullnames-------------------------------------------------------------------------
----------skipped_partnames-------------------------------------------------------------------------
__delattr__
__setattr__
====================================================================================================
"""
```

********************************************************************************
