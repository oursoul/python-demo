def demo(newitem,old_list = []):
    old_list.append(newitem)
    return old_list
print(demo('5',[1,2,3,4]))
print(demo('a'))
print(demo('b'))