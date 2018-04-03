# coding=utf-8
"""用类实现斐波那契数列"""

class Fib():
    def __call__(self, *args, **kwargs):
        ret = [1,1]
        num = int(args[0])
        if num == 1:
            return [1,]
        else:
            while len(ret)< num:
                ret.append(ret[-1]+ret[-2])
            return ret

fib = Fib()
print(fib(5))