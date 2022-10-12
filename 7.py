class MyClass:
    def __init__(self,i):
        self.a = i

    def f(self):
        c=self.a
        print('调用完成')
        return c


# 实例化类
x = MyClass('5asda')
# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.a)
print("MyClass 类的属性 i 为：", x.a)
print("MyClass 类的方法 f 为：", x.f())