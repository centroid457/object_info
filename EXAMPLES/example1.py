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


# ObjectInfo(Cls1()).print()
# ObjectInfo().print(Cls1())
ObjectInfo(Cls1()).print(
    _log_iter=True,
    only_names_include=[],
    skip_fullnames=["attrSkipFullName", ],
    skip_partnames=["SkipPartName", ],
    hide_build_in=None,
)
"""
==========OBJECTINFO.PRINT==========================================================================
str(SOURCE)=<__main__.Cls1 object at 0x00000160168F6F10>
repr(SOURCE)=<__main__.Cls1 object at 0x00000160168F6F10>
----------SETTINGS----------------------------------------------------------------------------------
skip_fullnames=['attrSkipFullName']
skip_partnames=['SkipPartName']
only_names_include=[]
hide_build_in=None
log_iter=True
----------log_iter(wait last touched)--------------------------------------------------------------
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
attrListObj              	list      :
                         	Cls0      :<__main__.Cls0 object at 0x00000160168F6E10>
                         	Cls0      :<__main__.Cls0 object at 0x00000160168F6E10>
                         	Cls0      :<__main__.Cls0 object at 0x00000160168F6E10>
                         	Cls0      :<__main__.Cls0 object at 0x00000160168F6E10>
                         	Cls0      :<__main__.Cls0 object at 0x00000160168F6E10>
                         	          :...
attrSet                  	set       :{1, 2, 3}
attrTuple                	tuple     :(1, 2, 3)
----------properties_exx----------------------------------------------------------------------------
propertyExx              	Exception :Exception('exxMsg')
----------methods_ok--------------------------------------------------------------------------------
__class__                	Cls1      :str(<__main__.Cls1 object at 0x0000016016C0AC90>)
                         	Cls1      :repr(<__main__.Cls1 object at 0x0000016016C0AC90>)
__dir__                  	list      :
                         	str       :__module__
                         	str       :attrSkipFullName
                         	str       :attrSkipPartName
                         	str       :attrNone
                         	str       :attrInt
                         	          :...
__getstate__             	NoneType  :None
__hash__                 	int       :94512936689
__repr__                 	str       :<__main__.Cls1 object at 0x00000160168F6F10>
__sizeof__               	int       :24
__str__                  	str       :<__main__.Cls1 object at 0x00000160168F6F10>
__subclasshook__         	NotImplementedType:str(NotImplemented)
                         	NotImplementedType:repr(NotImplemented)
attrClass                	Cls0      :str(<__main__.Cls0 object at 0x0000016016C0AED0>)
                         	Cls0      :repr(<__main__.Cls0 object at 0x0000016016C0AED0>)
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
attrObj                  	Cls0      :str(<__main__.Cls0 object at 0x00000160168F6DD0>)
                         	Cls0      :repr(<__main__.Cls0 object at 0x00000160168F6DD0>)
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
str(SOURCE)=<__main__.Cls1 object at 0x0000016016C0B0D0>
repr(SOURCE)=<__main__.Cls1 object at 0x0000016016C0B0D0>
----------SETTINGS----------------------------------------------------------------------------------
skip_fullnames=None
skip_partnames=None
only_names_include='attr'
hide_build_in=None
log_iter=None
----------log_iter(wait last touched)--------------------------------------------------------------
----------properties_ok-----------------------------------------------------------------------------
attrFloat                	float     :2.2
attrInt                  	int       :1
attrNone                 	NoneType  :None
attrSkipFullName         	str       :attrSkipFullName
attrSkipPartName         	str       :SkipPartName

attrDict                 	dict      :{1: 1}
attrList                 	list      :[1, 2, 3]
attrListObj              	list      :
                         	Cls0      :<__main__.Cls0 object at 0x00000160168F6E10>
                         	Cls0      :<__main__.Cls0 object at 0x00000160168F6E10>
                         	Cls0      :<__main__.Cls0 object at 0x00000160168F6E10>
                         	Cls0      :<__main__.Cls0 object at 0x00000160168F6E10>
                         	Cls0      :<__main__.Cls0 object at 0x00000160168F6E10>
                         	          :...
attrSet                  	set       :{1, 2, 3}
attrTuple                	tuple     :(1, 2, 3)
----------properties_exx----------------------------------------------------------------------------
----------methods_ok--------------------------------------------------------------------------------
attrClass                	Cls0      :str(<__main__.Cls0 object at 0x0000016016C0B490>)
                         	Cls0      :repr(<__main__.Cls0 object at 0x0000016016C0B490>)
----------methods_exx-------------------------------------------------------------------------------
__getattribute__         	TypeError :TypeError('expected 1 argument, got 0')
----------objects-----------------------------------------------------------------------------------
attrObj                  	Cls0      :str(<__main__.Cls0 object at 0x00000160168F6DD0>)
                         	Cls0      :repr(<__main__.Cls0 object at 0x00000160168F6DD0>)
----------skipped_fullnames-------------------------------------------------------------------------
----------skipped_partnames-------------------------------------------------------------------------
__delattr__
__setattr__
====================================================================================================
"""
