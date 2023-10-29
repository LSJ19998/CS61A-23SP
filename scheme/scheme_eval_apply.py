import sys

from pair import *
from scheme_utils import *
from ucb import main, trace

import scheme_forms

##############
# Eval/Apply #
##############


def scheme_eval(expr, env, _=None):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    #  atomic  expression
    if scheme_symbolp(expr):
        return env.lookup(expr)
    elif self_evaluating(expr):
        return expr

    # All non-atomic expressions are lists (combinations)
    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))
    first, rest = expr.first, expr.rest
    # 特殊形式的操作
    if scheme_symbolp(first) and first in scheme_forms.SPECIAL_FORMS:
        return scheme_forms.SPECIAL_FORMS[first](rest, env)
    # 正常形式的操作
    else:
        # BEGIN PROBLEM 3
        "*** YOUR CODE HERE ***"
        # 1. 解析函数
        procedure = scheme_eval(first, env)
        # 2, 解析参数
        args = rest.map(lambda expr: scheme_eval(expr, env))
        return scheme_apply(procedure, args, env)
        # END PROBLEM 3


def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    # 检查传入数据的合法化
    validate_procedure(procedure)
    if not isinstance(env, Frame):
        assert False, "Not a Frame: {}".format(env)
    # 应用不同的操作符

    # 内置的函数, 直接使用该函数, 然后传入参数
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2
        # 收集参数
        pyargs = []
        while args is not nil:
            pyargs += [args.first]
            args = args.rest
        # END PROBLEM 2
        try:
            # BEGIN PROBLEM 2
            # 将参数应用到该环境中
            if procedure.need_env:
                return procedure.py_func(*pyargs, env)
            return procedure.py_func(*pyargs)
            # END PROBLEM 2
        except TypeError as err:
            raise SchemeError(
                'incorrect number of arguments: {0}'.format(procedure))

    # 问题:  词法作用域 和 动态作用域的不清晰
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9
        "*** YOUR CODE HERE ***"
        # 词法作用域 -> 使用的是过程函数
        child_env = procedure.env.make_child_frame(procedure.formals, args)
        return eval_all(procedure.body, child_env)
        # END PROBLEM 9

    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        "*** YOUR CODE HERE ***"
        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)


def eval_all(expressions, env):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    Frame ENV (the current environment) and return the value of the last.

    >>> eval_all(read_line("(1)"), create_global_frame())
    1
    >>> eval_all(read_line("(1 2)"), create_global_frame())
    2
    >>> x = eval_all(read_line("((print 1) 2)"), create_global_frame())
    1
    >>> x
    2
    >>> eval_all(read_line("((define x 2) x)"), create_global_frame())
    2
    """
    # BEGIN PROBLEM 6
    result = None
    while expressions is not nil:
        result = scheme_eval(expressions.first, env)
        expressions = expressions.rest
    return result
    # END PROBLEM 6


class Unevaluated:
    """An expression and an environment in which it is to be evaluated."""

    def __init__(self, expr, env):
        """Expression EXPR to be evaluated in Frame ENV."""
        self.expr = expr
        self.env = env


def complete_apply(procedure, args, env):
    """Apply procedure to args in env; ensure the result is not an Unevaluated."""
    validate_procedure(procedure)
    val = scheme_apply(procedure, args, env)
    if isinstance(val, Unevaluated):
        return scheme_eval(val.expr, val.env)
    else:
        return val
