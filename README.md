# object_info (v0.2.5)

## DESCRIPTION_SHORT
print info about object (attributes+properties+methods results)

## DESCRIPTION_LONG
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
3. Useful if you wish to see info from remote SOURCE if connecting directly over ssh for example


## Features
1. print all properties/methods results  
2. show exceptions on methods/properties  
3. skip names by full/part names and use only by partnames  
4. separated collections by groups  


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
    attr1 = 1

class Cls1:
    ATTR_UPPERCASE = "UPPERCASE"
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
    attrListObj = [*[Cls0(), ] * 5, 1]
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


ObjectInfo(
    Cls1(),
    log_iter=True,
    names__use_only_parts=[],
    names__skip_full=["attrSkipFullName", ],
    names__skip_parts=["SkipPartName", ],
    hide_build_in=None,
).print()
"""
==========================================================================================
----------OBJECTINFO.PRINT--------------------------------------------------------------------------
str(SOURCE)=<__main__.Cls1 object at 0x000001A014B97950>
repr(SOURCE)=<__main__.Cls1 object at 0x000001A014B97950>
----------SETTINGS----------------------------------------------------------------------------------
self.NAMES__USE_ONLY_PARTS=[]
self.NAMES__SKIP_FULL=['attrSkipFullName']
self.NAMES__SKIP_PARTS=['init', 'new', 'create', 'enter', 'install', 'set', 'clone', 'copy', 'move', 'next', 'clear', 'reduce', 'close', 'del', 'exit', 'kill', 'exec', 'exec_', 'pyqtConfigure', 'checkout', 'detach', 'run', 'start', 'wait', 'join', 'terminate', 'quit', 'disconnect', 'pop', 'popleft', 'append', 'appendleft', 'extend', 'extendleft', 'add', 'insert', 'reverse', 'rotate', 'sort', 'SkipPartName']
self.HIDE_BUILD_IN=None
self.LOG_ITER=True
self.MAX_LINE_LEN=100
self.MAX_ITER_ITEMS=5
----------log_iter(wait last touched)---------------------------------------------------------------
1:	ATTR_UPPERCASE
2:	__class__
3:	__delattr__
4:	__dict__
5:	__dir__
6:	__doc__
7:	__eq__
8:	__format__
9:	__ge__
10:	__getattribute__
11:	__getstate__
12:	__gt__
13:	__hash__
14:	__init__
15:	__init_subclass__
16:	__le__
17:	__lt__
18:	__module__
19:	__ne__
20:	__new__
21:	__reduce__
22:	__reduce_ex__
23:	__repr__
24:	__setattr__
25:	__sizeof__
26:	__str__
27:	__subclasshook__
28:	__weakref__
29:	attrClass
30:	attrDict
31:	attrFloat
32:	attrInt
33:	attrList
34:	attrListObj
35:	attrNone
36:	attrObj
37:	attrSet
38:	attrSkipFullName
39:	attrSkipPartName
40:	attrTuple
41:	methExx
42:	methInt
43:	propertyExx
44:	propertyInt
----------SKIPPED_FULLNAMES-------------------------------------------------------------------------
1:	attrSkipFullName
----------SKIPPED_PARTNAMES-------------------------------------------------------------------------
1:	__delattr__
2:	__init__
3:	__init_subclass__
4:	__new__
5:	__reduce__
6:	__reduce_ex__
7:	__setattr__
8:	attrSkipPartName
----------PROPERTIES__ELEMENTARY_SINGLE-------------------------------------------------------------
ATTR_UPPERCASE      	str         :UPPERCASE
__doc__             	NoneType    :None
__module__          	str         :__main__
__weakref__         	NoneType    :None
attrFloat           	float       :2.2
attrInt             	int         :1
attrNone            	NoneType    :None
propertyInt         	int         :1
----------PROPERTIES__ELEMENTARY_COLLECTION---------------------------------------------------------
__dict__            	dict        :{}
attrDict            	dict        :{1: 1}
attrList            	list        :[1, 2, 3]
attrListObj         	list        :[<__main__.Cls0 object at 0x000001A014B96E10>, <__main__.Cls0 o...
                    	Cls0        :	<__main__.Cls0 object at 0x000001A014B96E10>
                    	Cls0        :	<__main__.Cls0 object at 0x000001A014B96E10>
                    	Cls0        :	<__main__.Cls0 object at 0x000001A014B96E10>
                    	Cls0        :	<__main__.Cls0 object at 0x000001A014B96E10>
                    	Cls0        :	<__main__.Cls0 object at 0x000001A014B96E10>
                    	            :	...
attrSet             	set         :{1, 2, 3}
attrTuple           	tuple       :(1, 2, 3)
----------PROPERTIES__OBJECTS-----------------------------------------------------------------------
attrObj             	Cls0        :<__main__.Cls0 object at 0x000001A014B978D0>
                    	__repr()    :<__main__.Cls0 object at 0x000001A014B978D0>
----------PROPERTIES__EXX---------------------------------------------------------------------------
propertyExx         	Exception   :Exception('exxMsg')
----------METHODS__ELEMENTARY_SINGLE----------------------------------------------------------------
__getstate__        	NoneType    :None
__hash__            	int         :111690880917
__repr__            	str         :<__main__.Cls1 object at 0x000001A014B97950>
__sizeof__          	int         :24
__str__             	str         :<__main__.Cls1 object at 0x000001A014B97950>
methInt             	int         :1
----------METHODS__ELEMENTARY_COLLECTION------------------------------------------------------------
__dir__             	list        :['__module__', 'ATTR_UPPERCASE', 'attrSkipFullName', 'attrSkipP...
                    	str         :	__module__
                    	str         :	ATTR_UPPERCASE
                    	str         :	attrSkipFullName
                    	str         :	attrSkipPartName
                    	str         :	attrNone
                    	            :	...
----------METHODS__OBJECTS--------------------------------------------------------------------------
__class__           	Cls1        :<__main__.Cls1 object at 0x000001A014B97C10>
                    	__repr()    :<__main__.Cls1 object at 0x000001A014B97C10>
__subclasshook__    	NotImplementedType:NotImplemented
                    	__repr()    :NotImplemented
attrClass           	Cls0        :<__main__.Cls0 object at 0x000001A0151A9150>
                    	__repr()    :<__main__.Cls0 object at 0x000001A0151A9150>
----------METHODS__EXX------------------------------------------------------------------------------
__eq__              	TypeError   :TypeError('expected 1 argument, got 0')
__format__          	TypeError   :TypeError('Cls1.__format__() takes exactly one argument (0 give...
__ge__              	TypeError   :TypeError('expected 1 argument, got 0')
__getattribute__    	TypeError   :TypeError('expected 1 argument, got 0')
__gt__              	TypeError   :TypeError('expected 1 argument, got 0')
__le__              	TypeError   :TypeError('expected 1 argument, got 0')
__lt__              	TypeError   :TypeError('expected 1 argument, got 0')
__ne__              	TypeError   :TypeError('expected 1 argument, got 0')
methExx             	Exception   :Exception('exxMsg')
==========================================================================================
"""

ObjectInfo(
    Cls1(),
    log_iter=False,
    names__use_only_parts="attr",
    # names__skip_full=["attrSkipFullName", ],
    # names__skip_parts=["SkipPartName", ],
    # hide_build_in=None,
    # max_line_len=0,
    # max_iter_items=0,
).print()
"""
==========================================================================================
----------OBJECTINFO.PRINT--------------------------------------------------------------------------
str(SOURCE)=<__main__.Cls1 object at 0x000001A014BE28D0>
repr(SOURCE)=<__main__.Cls1 object at 0x000001A014BE28D0>
----------SETTINGS----------------------------------------------------------------------------------
self.NAMES__USE_ONLY_PARTS=['attr']
self.NAMES__SKIP_FULL=['attrSkipFullName']
self.NAMES__SKIP_PARTS=['init', 'new', 'create', 'enter', 'install', 'set', 'clone', 'copy', 'move', 'next', 'clear', 'reduce', 'close', 'del', 'exit', 'kill', 'exec', 'exec_', 'pyqtConfigure', 'checkout', 'detach', 'run', 'start', 'wait', 'join', 'terminate', 'quit', 'disconnect', 'pop', 'popleft', 'append', 'appendleft', 'extend', 'extendleft', 'add', 'insert', 'reverse', 'rotate', 'sort', 'SkipPartName']
self.HIDE_BUILD_IN=None
self.LOG_ITER=False
self.MAX_LINE_LEN=100
self.MAX_ITER_ITEMS=5
----------log_iter(wait last touched)---------------------------------------------------------------
----------SKIPPED_FULLNAMES-------------------------------------------------------------------------
1:	attrSkipFullName
----------SKIPPED_PARTNAMES-------------------------------------------------------------------------
1:	__delattr__
2:	__setattr__
3:	attrSkipPartName
----------PROPERTIES__ELEMENTARY_SINGLE-------------------------------------------------------------
ATTR_UPPERCASE      	str         :UPPERCASE
attrFloat           	float       :2.2
attrInt             	int         :1
attrNone            	NoneType    :None
----------PROPERTIES__ELEMENTARY_COLLECTION---------------------------------------------------------
attrDict            	dict        :{1: 1}
attrList            	list        :[1, 2, 3]
attrListObj         	list        :[<__main__.Cls0 object at 0x000001A014B96E10>, <__main__.Cls0 o...
                    	Cls0        :	<__main__.Cls0 object at 0x000001A014B96E10>
                    	Cls0        :	<__main__.Cls0 object at 0x000001A014B96E10>
                    	Cls0        :	<__main__.Cls0 object at 0x000001A014B96E10>
                    	Cls0        :	<__main__.Cls0 object at 0x000001A014B96E10>
                    	Cls0        :	<__main__.Cls0 object at 0x000001A014B96E10>
                    	            :	...
attrSet             	set         :{1, 2, 3}
attrTuple           	tuple       :(1, 2, 3)
----------PROPERTIES__OBJECTS-----------------------------------------------------------------------
attrObj             	Cls0        :<__main__.Cls0 object at 0x000001A014B978D0>
                    	__repr()    :<__main__.Cls0 object at 0x000001A014B978D0>
----------PROPERTIES__EXX---------------------------------------------------------------------------
----------METHODS__ELEMENTARY_SINGLE----------------------------------------------------------------
----------METHODS__ELEMENTARY_COLLECTION------------------------------------------------------------
----------METHODS__OBJECTS--------------------------------------------------------------------------
attrClass           	Cls0        :<__main__.Cls0 object at 0x000001A0151A9C90>
                    	__repr()    :<__main__.Cls0 object at 0x000001A0151A9C90>
----------METHODS__EXX------------------------------------------------------------------------------
__getattribute__    	TypeError   :TypeError('expected 1 argument, got 0')
==========================================================================================
"""
```

********************************************************************************
