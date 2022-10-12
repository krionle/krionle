import random
name=['汤子凡', '沈欢', '张龙', '蔡锦江', '黄运宇', '李鹤', '杜亮', '徐历', '胡文杰', '王相博',
           '赵国冬', '阮佳怡', '李蒋科', '刘天帅', '高博武', '付代鑫', '周文齐', '赵俊杰', '江宏宝', '蔡光达', '郭志豪']
while True:
    con = str(input("是否添加姓名y/n:"))
    if con == 'y':
        add_name = str(input("请输入姓名:"))
        name.append(add_name)
        # continue
    else:
        break
max_name = len(name) - 1
cs = int(input('请输入要选几个：'))
k = random.sample(name, cs)
# while True :
#     a = random.randint(0,max_name)
#     b = random.randint(0,max_name)
#     if a !=b :
#         break
#     else:
#         continue
# for i in k :
#     print(name[i])
for i in k:
    print(i)