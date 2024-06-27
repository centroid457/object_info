![Ver/TestedPython](https://img.shields.io/pypi/pyversions/object_info)
![Ver/Os](https://img.shields.io/badge/os_development-Windows-blue)  
![repo/Created](https://img.shields.io/github/created-at/centroid457/object_info)
![Commit/Last](https://img.shields.io/github/last-commit/centroid457/object_info)
![Tests/GitHubWorkflowStatus](https://github.com/centroid457/object_info/actions/workflows/test_linux.yml/badge.svg)
![Tests/GitHubWorkflowStatus](https://github.com/centroid457/object_info/actions/workflows/test_windows.yml/badge.svg)  
![repo/Size](https://img.shields.io/github/repo-size/centroid457/object_info)
![Commit/Count/t](https://img.shields.io/github/commit-activity/t/centroid457/object_info)
![Commit/Count/y](https://img.shields.io/github/commit-activity/y/centroid457/object_info)
![Commit/Count/m](https://img.shields.io/github/commit-activity/m/centroid457/object_info)

# object_info (current v0.2.12/![Ver/Pypi Latest](https://img.shields.io/pypi/v/object_info?label=pypi%20latest))

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
from pytest_aux import *


# =====================================================================================================================
class ClsMain(ClsFullTypes):
    attrUpper = "ATTRUPPER"
    attrLower = "attrlower"
    attrSkipFullName = "attrSkipFullName"
    attrSkipPartName = "SkipPartName"


ObjectInfo(
    ClsMain(),
    log_iter=True,
    names__use_only_parts=[],
    names__skip_full=["attrSkipFullName", ],
    names__skip_parts=["SkipPartName", ],
    hide_build_in=None,
).print()
"""
==========================================================================================
----------OBJECTINFO.PRINT--------------------------------------------------------------------------
str(SOURCE)=<__main__.ClsMain object at 0x000001AD37B06C90>
repr(SOURCE)=<__main__.ClsMain object at 0x000001AD37B06C90>
----------SETTINGS----------------------------------------------------------------------------------
self.NAMES__USE_ONLY_PARTS=[]
self.NAMES__SKIP_FULL=['attrSkipFullName']
self.NAMES__SKIP_PARTS=['init', 'new', 'create', 'enter', 'install', 'set', 'clone', 'copy', 'move', 'next', 'clear', 'reduce', 'close', 'del', 'exit', 'kill', 'exec', 'exec_', 'pyqtConfigure', 'checkout', 'detach', 'run', 'start', 'wait', 'join', 'terminate', 'quit', 'disconnect', 'pop', 'popleft', 'append', 'appendleft', 'extend', 'extendleft', 'add', 'insert', 'reverse', 'rotate', 'sort', 'SkipPartName']
self.HIDE_BUILD_IN=None
self.LOG_ITER=True
self.MAX_LINE_LEN=100
self.MAX_ITER_ITEMS=5
----------log_iter(wait last touched)---------------------------------------------------------------
1:	__class__
2:	__delattr__
3:	__dict__
4:	__dir__
5:	__doc__
6:	__eq__
7:	__format__
8:	__ge__
9:	__getattribute__
10:	__getstate__
11:	__gt__
12:	__hash__
13:	__init__
14:	__init_subclass__
15:	__le__
16:	__lt__
17:	__module__
18:	__ne__
19:	__new__
20:	__reduce__
21:	__reduce_ex__
22:	__repr__
23:	__setattr__
24:	__sizeof__
25:	__str__
26:	__subclasshook__
27:	__weakref__
28:	attrBytes
29:	attrCls
30:	attrDict
31:	attrFalse
32:	attrFloat
33:	attrFunc
34:	attrFuncTrue
35:	attrInst
36:	attrInstCallable
37:	attrInstMeth
38:	attrInt
39:	attrList
40:	attrListInst
41:	attrLower
42:	attrNone
43:	attrSet
44:	attrSkipFullName
45:	attrSkipPartName
46:	attrStr
47:	attrTrue
48:	attrTuple
49:	attrUpper
50:	attrZero
51:	methExx
52:	methFunc
53:	methInt
54:	propertyExx
55:	propertyFunc
56:	propertyInt
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
__doc__             	NoneType    :None
__module__          	str         :__main__
__weakref__         	NoneType    :None
attrBytes           	bytes       :b'bytes'
attrFalse           	bool        :False
attrFloat           	float       :1.1
attrInt             	int         :1
attrLower           	str         :attrlower
attrNone            	NoneType    :None
attrStr             	str         :str
attrTrue            	bool        :True
attrUpper           	str         :ATTRUPPER
attrZero            	int         :0
propertyInt         	int         :1
----------PROPERTIES__ELEMENTARY_COLLECTION---------------------------------------------------------
__dict__            	dict        :{}
attrDict            	dict        :{1: 1}
attrList            	list        :[1, 2, 3]
attrListInst        	list        :[<pytest_aux.primitives.ClsEmpty object at 0x000001AD487673D...
                    	ClsEmpty    :	<pytest_aux.primitives.ClsEmpty object at 0x000001AD487673D0>
                    	ClsEmpty    :	<pytest_aux.primitives.ClsEmpty object at 0x000001AD487673D0>
                    	ClsEmpty    :	<pytest_aux.primitives.ClsEmpty object at 0x000001AD487673D0>
                    	int         :	1
attrSet             	set         :{1, 2, 3}
attrTuple           	tuple       :(1, 2, 3)
----------PROPERTIES__OBJECTS-----------------------------------------------------------------------
attrInst            	ClsEmpty    :<pytest_aux.primitives.ClsEmpty object at 0x000001AD487672D0>
                    	__repr()    :<pytest_aux.primitives.ClsEmpty object at 0x000001AD487672D0>
----------PROPERTIES__EXX---------------------------------------------------------------------------
propertyExx         	Exception   :Exception('exxMsg')
----------METHODS__ELEMENTARY_SINGLE----------------------------------------------------------------
__getstate__        	NoneType    :None
__hash__            	int         :115217204937
__repr__            	str         :<__main__.ClsMain object at 0x000001AD37B06C90>
__sizeof__          	int         :24
__str__             	str         :<__main__.ClsMain object at 0x000001AD37B06C90>
attrFunc            	NoneType    :None
attrFuncTrue        	bool        :True
attrInstCallable    	NoneType    :None
attrInstMeth        	NoneType    :None
methInt             	int         :1
propertyFunc        	NoneType    :None
----------METHODS__ELEMENTARY_COLLECTION------------------------------------------------------------
__dir__             	list        :['__module__', 'attrUpper', 'attrLower', 'attrSkipFullName',...
                    	str         :	__module__
                    	str         :	attrUpper
                    	str         :	attrLower
                    	str         :	attrSkipFullName
                    	str         :	attrSkipPartName
                    	            :	...
----------METHODS__OBJECTS--------------------------------------------------------------------------
__class__           	ClsMain     :<__main__.ClsMain object at 0x000001AD37B06ED0>
                    	__repr()    :<__main__.ClsMain object at 0x000001AD37B06ED0>
__subclasshook__    	NotImplementedType:NotImplemented
                    	__repr()    :NotImplemented
attrCls             	ClsEmpty    :<pytest_aux.primitives.ClsEmpty object at 0x000001AD48767B50>
                    	__repr()    :<pytest_aux.primitives.ClsEmpty object at 0x000001AD48767B50>
methFunc            	function    :<function FUNC at 0x000001AD48768540>
----------METHODS__EXX------------------------------------------------------------------------------
__eq__              	TypeError   :TypeError('expected 1 argument, got 0')
__format__          	TypeError   :TypeError('ClsMain.__format__() takes exactly one argument (...
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
    ClsMain(),
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
str(SOURCE)=<__main__.ClsMain object at 0x000001AD38A0FDD0>
repr(SOURCE)=<__main__.ClsMain object at 0x000001AD38A0FDD0>
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
attrBytes           	bytes       :b'bytes'
attrFalse           	bool        :False
attrFloat           	float       :1.1
attrInt             	int         :1
attrLower           	str         :attrlower
attrNone            	NoneType    :None
attrStr             	str         :str
attrTrue            	bool        :True
attrUpper           	str         :ATTRUPPER
attrZero            	int         :0
----------PROPERTIES__ELEMENTARY_COLLECTION---------------------------------------------------------
attrDict            	dict        :{1: 1}
attrList            	list        :[1, 2, 3]
attrListInst        	list        :[<pytest_aux.primitives.ClsEmpty object at 0x000001AD487673D...
                    	ClsEmpty    :	<pytest_aux.primitives.ClsEmpty object at 0x000001AD487673D0>
                    	ClsEmpty    :	<pytest_aux.primitives.ClsEmpty object at 0x000001AD487673D0>
                    	ClsEmpty    :	<pytest_aux.primitives.ClsEmpty object at 0x000001AD487673D0>
                    	int         :	1
attrSet             	set         :{1, 2, 3}
attrTuple           	tuple       :(1, 2, 3)
----------PROPERTIES__OBJECTS-----------------------------------------------------------------------
attrInst            	ClsEmpty    :<pytest_aux.primitives.ClsEmpty object at 0x000001AD487672D0>
                    	__repr()    :<pytest_aux.primitives.ClsEmpty object at 0x000001AD487672D0>
----------PROPERTIES__EXX---------------------------------------------------------------------------
----------METHODS__ELEMENTARY_SINGLE----------------------------------------------------------------
attrFunc            	NoneType    :None
attrFuncTrue        	bool        :True
attrInstCallable    	NoneType    :None
attrInstMeth        	NoneType    :None
----------METHODS__ELEMENTARY_COLLECTION------------------------------------------------------------
----------METHODS__OBJECTS--------------------------------------------------------------------------
attrCls             	ClsEmpty    :<pytest_aux.primitives.ClsEmpty object at 0x000001AD48774190>
                    	__repr()    :<pytest_aux.primitives.ClsEmpty object at 0x000001AD48774190>
----------METHODS__EXX------------------------------------------------------------------------------
__getattribute__    	TypeError   :TypeError('expected 1 argument, got 0')
==========================================================================================
"""
```

********************************************************************************
