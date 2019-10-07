stu = [
    {'num':'201801','name':'Wangwu','score':89},
    {'num':'201802','name':'Liujun','score':95},
    {'num':'201803','name':'Limeng','score':85}]		#定义学生信息
stu.sort(key = lambda x:x['score'])						#按成绩排序
for s in stu:
    print('学号:',s['num'],'姓名:',s['name'],'成绩:',s['score'])	#输出列表