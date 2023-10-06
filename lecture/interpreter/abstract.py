def scheme_eval(expr, env):
    if scheme_symbolp(expr):
        return env[expr]
    elif scheme_atomp(expr):
        return expr
    first, rest = expr.first, expr.second
    if first == 'lambda':
        return do_lambda_form(rest, env)
    elif first == 'define':
        do_define_form(first, env)
        return None
    else:
        procedure = scheme_eval(first, env)
        args = scheme_eval(first, env)
        return scheme_apply(procedure, args, env)
