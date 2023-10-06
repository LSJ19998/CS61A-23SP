from functools import reduce, map
from math import add, mul, truediv, sub


def clac_eval(exp):
    # 1. 如果是原始数据, 直接返回
    if type(exp) in (int, float):
        return simplify(exp)
    # 2. 如果是复合表达式
    elif isinstance(exp, Pair):
        # 计算子表达式
        arguments = exp.second.map(clac_eval)
        # 将子表达式的结果应用到操作符上, 计算出该表达式的值
        return simplify(calc_apply(exp.first, arguments))
    # 3. 如果不是原始数据 或者 调用表达式 引发错误
    else:
        raise TypeError(exp + ' is not a number or call expression')


def calc_apply(operator, args):
    # Checking type
    if not isinstance(operator, str):
        raise TypeError(str(operator) + ' is not a symbol!')
    if operator == '+':
        return reduce(add, args, 0)
    elif operator == '-':
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        elif len(args) == 1:
            return -args.first
        else:
            return reduce(sub, args, args.first)
    elif operator == '*':
        return reduce(mul, args, 1)
    elif operator == '/':
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        elif len(args) == 1:
            return 1/args.first
        else:
            return reduce(truediv, args.second, args.first)
    else:
        raise TypeError(operator + ' is an unknown operator')


def read_eval_print_loop_demo():
    while True:
        src = buffer_input()
        while src.more_on_line:
            expression = scheme_read(src)
            print(calc_eval(expression))


def read_eval_print_loop():
    while True:
        try:
            src = buffer_input()
            while src.more_on_line:
                expression = scheme_read(src)
            print(clac_eval(expression))
        except (SyntaxError, TypeError, ValueError, ZeroDivisionError) as err:
            print(type(err).__name__ + ": ", err)
        except (KeyboardInterrupt, EOFError):
            print('Calculation completed.')
            return
