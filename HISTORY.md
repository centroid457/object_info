# RELEASE HISTORY

********************************************************************************
## TODO
1. add TIMEOUT (use start in thread!) for print! use timeout for GETATTR!!!  
2. realise PRINT_DIFFS=CHANGE_state/COMPARE_objects (one from different states like thread before and after start)!:  
	- this is about to save object STATE!  
	- add parameter show only diffs or show all  
	- add TESTS after this step!  
3. apply asyncio.run for coroutine?  
4. merge items Property/Meth? - cause it does not matter callable or not (just add type info block)  
5. add check__instance_of_user_class  

********************************************************************************
## FIXME
1. ...  

********************************************************************************
## NEWS

0.2.12 (2024/06/27 11:34:44)
------------------------------
- [OInfo] fix print  
- [TestPrimitives] move into pytest_aux  

0.2.11 (2024/06/24 12:09:19)
------------------------------
- [CICD+BADGEs] apply  
- [TESTS] separate in folder  
- [TypeChecker] fix check__nested__by_cls_or_inst  

0.2.10 (2024/06/13 15:10:03)
------------------------------
- [TypeChecker]:  
	- add check__instance_not_elementary  
	- zero finish test.parametrisation  
	- fix check__class for callables  

0.2.9 (2024/06/07 14:09:00)
------------------------------
- [TypeChecker] add check__func_or_meth  

0.2.8 (2024/06/07 09:48:08)
------------------------------
- [TypeChecker] extend test__check__class for funcs/meth ClsInst  

0.2.7 (2024/05/30 16:50:46)
------------------------------
- [TypeChecker] add check__nested__by_cls_or_inst  

0.2.6 (2024/05/30 16:17:43)
------------------------------
- [TypeChecker]:  
	- separate class  
	- separate tests  
	- finish tests  
	- add check__class  
	- fix check__exception for both INst/Cls  

0.2.5 (2024/05/22 12:41:54)
------------------------------
- [__INIT__.py] fix import  
- apply last pypi template  

0.2.4 (2024/05/03 15:10:10)
------------------------------
- [print] zero:  
	- fix WRAPPER_MAIN_LINE for convenient length in Word  
	- fix length for ellipsis in overlonged lines  

0.2.3 (2024/03/18 11:58:07)
------------------------------
- zero [NAMES__SKIP_PARTS] move all from NAMES__SKIP_FULL  

0.2.2 (2024/03/07 11:26:33)
------------------------------
- fix max_line_len/max_iter_items  

0.2.1 (2024/02/22 11:30:56)
------------------------------
- zero del double TAB in iterating lists  

0.2.0 (2024/02/19 14:57:29)
------------------------------
- big ref!:  
	- separate result item as ObjectState  
	- ...  

0.1.14 (2024/02/14 11:53:05)
------------------------------
- SKIP_FULLNAMES.extend(change collection content/count/order)  

0.1.13 (2024/02/13 17:43:37)
------------------------------
- apply new pypi template/2  
- add pretty print for one level  

0.1.12 (2024/01/15 10:26:57)
------------------------------
- apply new pypi template  
- del old _print_deep  

0.1.11 (2024-01-11)
-------------------
- show settings in print
- print always all group names

0.1.10 (2024-01-11)
-------------------
- fix tuple
- separate collections in groups

0.1.9 (2024-01-11)
-------------------
- SKIP NAMES append new
- apply last version for share (pypi template)

0.1.8 (2024-01-10)
-------------------
- SKIP_FULLNAMES.append names for common threads (wait/join)

0.1.7 (2024-01-10)
-------------------
- SKIP_FULLNAMES.append names for common threads

0.1.6 (2024-01-10)
-------------------
- fix Qthread

0.1.5 (2024-01-10)
-------------------
- SKIP_FULLNAMES.append names for PyQt5 Qthread

0.1.4 (2023-12-27)
-------------------
- add params skip_partnames/fullnames

0.1.3 (2023-12-27)
-------------------
- add _log_iter

0.1.2 (2023-12-21)
-------------------
- fix str/repr print attr-name only one time

0.1.1 (2023-12-19)
-------------------
- add str/repr print for objects

0.1.0 (2023-12-08)
-------------------
- fix str/repr print

0.0.6 (2023-12-07)
-------------------
- use big name in first print line

0.0.5 (2023-12-06)
-------------------
- add HIDE_BUILD_IN/HIDE_SKIPPED

0.0.4 (2023-12-05)
-------------------
- add parameter only_names_include in print method

0.0.3 (2023-11-30)
-------------------
- rename method to simple print! 

0.0.2 (2023-11-30)
-------------------
- add MAX_VALUE_LEN
- use params in method print_object_info
- align all separating lines into one pretty length

0.0.1 (2023-11-27)
-------------------
- first variant

********************************************************************************
