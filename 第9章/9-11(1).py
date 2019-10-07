import jieba							#导入jieba库
with open("三国演义.txt", "r")as file:
    txt =file.read()						#打开文件并读取文件内容
words = jieba.lcut(txt)					#进行分词，将结果放入words列表中
counts = {}							#定义字典用于存储词语和计数器
for word in words:
    if len(word) == 1:					#排除单个字符的分词结果
        continue
    else:
        counts[word] = counts.get(word,0) + 1		#计数器累加
items = list(counts.items())						#将字典元素转换为列表
items.sort(key=lambda x:x[1], reverse=True)		#排序
for i in range(15):								#输出前15项
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
