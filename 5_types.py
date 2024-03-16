# 对字符串求长度
s = "Hello world!"
print(len(s))

# 通过索引获取单个字符
print(s[0])
print(s[11])
print(s[len(s) - 2])
print('''s[0] 
s[1]
s[2]
s[3]''') #虽然完成了换行功能的实现，但是因为被字符串包裹，所以导致整体变为字符串而无法取值

# 布尔类型
b1 = True
b2 = False

# 空置类型
n = None

# type函数
print(type(s))
print(type(b1))
print(type(n))
print(type(1.5))

# len(b1) 使用错误的类型就会报错，所以要清楚了解各个操作对象的所属类型