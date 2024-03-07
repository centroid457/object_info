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
====================================================================================================
----------OBJECTINFO.PRINT--------------------------------------------------------------------------
str(SOURCE)=<__main__.Cls1 object at 0x0000011EFDE34A90>
repr(SOURCE)=<__main__.Cls1 object at 0x0000011EFDE34A90>
----------SETTINGS----------------------------------------------------------------------------------
self.NAMES__USE_ONLY_PARTS=[]
self.NAMES__SKIP_FULL=['checkout', 'detach', 'run', 'start', 'wait', 'join', 'terminate', 'quit', 'disconnect', 'exec', 'exec_', 'pyqtConfigure', 'pop', 'popleft', 'append', 'appendleft', 'extend', 'extendleft', 'add', 'insert', 'reverse', 'rotate', 'sort', 'attrSkipFullName', 'attrSkipFullName']
self.NAMES__SKIP_PARTS=['init', 'new', 'create', 'enter', 'install', 'set', 'clone', 'copy', 'move', 'next', 'clear', 'reduce', 'close', 'del', 'exit', 'kill', 'SkipPartName', 'SkipPartName']
self.HIDE_BUILD_IN=None
self.LOG_ITER=True
self.MAX_LINE_LEN=100
self.MAX_ITER_ITEMS=5
----------log_iter(wait last touched)---------------------------------------------------------------
1:		ATTR_UPPERCASE
2:		__class__
3:		__delattr__
4:		__dict__
5:		__dir__
6:		__doc__
7:		__eq__
8:		__format__
9:		__ge__
10:		__getattribute__
11:		__getstate__
12:		__gt__
13:		__hash__
14:		__init__
15:		__init_subclass__
16:		__le__
17:		__lt__
18:		__module__
19:		__ne__
20:		__new__
21:		__reduce__
22:		__reduce_ex__
23:		__repr__
24:		__setattr__
25:		__sizeof__
26:		__slotnames__
27:		__str__
28:		__subclasshook__
29:		__weakref__
30:		attrClass
31:		attrDict
32:		attrFloat
33:		attrInt
34:		attrList
35:		attrListObj
36:		attrNone
37:		attrObj
38:		attrSet
39:		attrSkipFullName
40:		attrSkipPartName
41:		attrTuple
42:		methExx
43:		methInt
44:		propertyExx
45:		propertyInt
----------SKIPPED_FULLNAMES-------------------------------------------------------------------------
1:		attrSkipFullName
----------SKIPPED_PARTNAMES-------------------------------------------------------------------------
1:		__delattr__
2:		__init__
3:		__init_subclass__
4:		__new__
5:		__reduce__
6:		__reduce_ex__
7:		__setattr__
8:		attrSkipPartName
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
__slotnames__       	list        :[]
attrDict            	dict        :{1: 1}
attrList            	list        :[1, 2, 3]
attrListObj         	list        :[<__main__.Cls0 object at 0x0000011EFDFB70D0>, <__main__.Cls0 o...
                    	Cls0        :	<__main__.Cls0 object at 0x0000011EFDFB70D0>
                    	Cls0        :	<__main__.Cls0 object at 0x0000011EFDFB70D0>
                    	Cls0        :	<__main__.Cls0 object at 0x0000011EFDFB70D0>
                    	Cls0        :	<__main__.Cls0 object at 0x0000011EFDFB70D0>
                    	Cls0        :	<__main__.Cls0 object at 0x0000011EFDFB70D0>
                    	            :	...
attrSet             	set         :{1, 2, 3}
attrTuple           	tuple       :(1, 2, 3)
----------PROPERTIES__OBJECTS-----------------------------------------------------------------------
attrObj             	Cls0        :<__main__.Cls0 object at 0x0000011EFDFB7050>
                    	__repr()    :<__main__.Cls0 object at 0x0000011EFDFB7050>
----------PROPERTIES__EXX---------------------------------------------------------------------------
propertyExx         	Exception   :Exception('exxMsg')
----------METHODS__ELEMENTARY_SINGLE----------------------------------------------------------------
__getstate__        	NoneType    :None
__hash__            	int         :77038761129
__repr__            	str         :<__main__.Cls1 object at 0x0000011EFDE34A90>
__sizeof__          	int         :24
__str__             	str         :<__main__.Cls1 object at 0x0000011EFDE34A90>
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
__class__           	Cls1        :<__main__.Cls1 object at 0x0000011EFE5CD490>
                    	__repr()    :<__main__.Cls1 object at 0x0000011EFE5CD490>
__subclasshook__    	NotImplementedType:NotImplemented
                    	__repr()    :NotImplemented
attrClass           	Cls0        :<__main__.Cls0 object at 0x0000011EFE5CD790>
                    	__repr()    :<__main__.Cls0 object at 0x0000011EFE5CD790>
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
====================================================================================================
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
====================================================================================================
----------OBJECTINFO.PRINT--------------------------------------------------------------------------
str(SOURCE)=<__main__.Cls1 object at 0x0000011EFE5CD910>
repr(SOURCE)=<__main__.Cls1 object at 0x0000011EFE5CD910>
----------SETTINGS----------------------------------------------------------------------------------
self.NAMES__USE_ONLY_PARTS=['attr']
self.NAMES__SKIP_FULL=['checkout', 'detach', 'run', 'start', 'wait', 'join', 'terminate', 'quit', 'disconnect', 'exec', 'exec_', 'pyqtConfigure', 'pop', 'popleft', 'append', 'appendleft', 'extend', 'extendleft', 'add', 'insert', 'reverse', 'rotate', 'sort', 'attrSkipFullName', 'attrSkipFullName']
self.NAMES__SKIP_PARTS=['init', 'new', 'create', 'enter', 'install', 'set', 'clone', 'copy', 'move', 'next', 'clear', 'reduce', 'close', 'del', 'exit', 'kill', 'SkipPartName', 'SkipPartName']
self.HIDE_BUILD_IN=None
self.LOG_ITER=False
self.MAX_LINE_LEN=100
self.MAX_ITER_ITEMS=5
----------log_iter(wait last touched)---------------------------------------------------------------
----------SKIPPED_FULLNAMES-------------------------------------------------------------------------
1:		attrSkipFullName
----------SKIPPED_PARTNAMES-------------------------------------------------------------------------
1:		__delattr__
2:		__setattr__
3:		attrSkipPartName
----------PROPERTIES__ELEMENTARY_SINGLE-------------------------------------------------------------
ATTR_UPPERCASE      	str         :UPPERCASE
attrFloat           	float       :2.2
attrInt             	int         :1
attrNone            	NoneType    :None
----------PROPERTIES__ELEMENTARY_COLLECTION---------------------------------------------------------
attrDict            	dict        :{1: 1}
attrList            	list        :[1, 2, 3]
attrListObj         	list        :[<__main__.Cls0 object at 0x0000011EFDFB70D0>, <__main__.Cls0 o...
                    	Cls0        :	<__main__.Cls0 object at 0x0000011EFDFB70D0>
                    	Cls0        :	<__main__.Cls0 object at 0x0000011EFDFB70D0>
                    	Cls0        :	<__main__.Cls0 object at 0x0000011EFDFB70D0>
                    	Cls0        :	<__main__.Cls0 object at 0x0000011EFDFB70D0>
                    	Cls0        :	<__main__.Cls0 object at 0x0000011EFDFB70D0>
                    	            :	...
attrSet             	set         :{1, 2, 3}
attrTuple           	tuple       :(1, 2, 3)
----------PROPERTIES__OBJECTS-----------------------------------------------------------------------
attrObj             	Cls0        :<__main__.Cls0 object at 0x0000011EFDFB7050>
                    	__repr()    :<__main__.Cls0 object at 0x0000011EFDFB7050>
----------PROPERTIES__EXX---------------------------------------------------------------------------
----------METHODS__ELEMENTARY_SINGLE----------------------------------------------------------------
----------METHODS__ELEMENTARY_COLLECTION------------------------------------------------------------
----------METHODS__OBJECTS--------------------------------------------------------------------------
attrClass           	Cls0        :<__main__.Cls0 object at 0x0000011EFE5CDE50>
                    	__repr()    :<__main__.Cls0 object at 0x0000011EFE5CDE50>
----------METHODS__EXX------------------------------------------------------------------------------
__getattribute__    	TypeError   :TypeError('expected 1 argument, got 0')
====================================================================================================
"""
