dict1 = {'user':'runoob','num':[1,2,3]}
dict2 = dict1				#引用对象
dict3 = dict1.copy()			#浅复制，深复制父对象，子对象不复制，还是引用
import copy
dict4 = copy.deepcopy(dict1)	#深复制，完全复制父对象及其子对象
dict1['user'] = 'root'			#将dict1中键为'user'的值改为'root'
dict1['num'].remove(1)		#移除dict1中键为'num'的列表值中的1
#输出结果
print('dict1=',dict1)
print('dict2=',dict2)
print('dict3=',dict3)
print('dict4=',dict4)