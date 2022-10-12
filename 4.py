import random
import matplotlib.pyplot as plt
f1 = open('t1.txt',mode='w',encoding='utf-8')
name = ['汤子凡', '沈欢', '张龙', '蔡锦江', '黄运宇', '李鹤', '杜亮', '徐历', '胡文杰', '王相博','赵国冬', '阮佳怡', '李蒋科', '刘天帅', '高博武', '付代鑫', '周文齐', '赵俊杰', '江宏宝', '蔡光达', '郭志豪']
soc = []
eng_c =[]
math_c = []
chinese_c = []
for i in name:
    chinese = random.randint(0,100)
    math_s = random.randint(0,100)
    english = random.randint(0,100)
    zf = chinese+math_s+english
    #所有数据
    a = [i,math_s,chinese,english,zf]
    #每个科目分数
    chinese_c.append(chinese)
    math_c.append(math_s)
    eng_c.append(english)
    soc.append(a)

mm = str(max(math_c))
me = str(max(eng_c))
mc = str(max(chinese_c))
f1.write("数学最大分：%s  语文最大分:%s  英语最大分:%s"%(mm,mc,me))
f1.write("\n")
f1.write("数学  语文  英语  总分")
f1.write("\n")

soc.sort(key=lambda ele:ele[4],reverse = True )

for i in soc:
    for j in i :
        dty = str(j)
        f1.write("%s  "%dty)
    f1.write("\n")
f1.close()

soc.clear()
math_c.clear()
eng_c.clear()
chinese_c.clear()

