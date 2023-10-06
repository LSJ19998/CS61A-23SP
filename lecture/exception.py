def invert(x):
    result = 1/x
    print('Never printed if x is 0')
    return result


def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        print('Error raising')
        return str(e)


class IterImproveError(Exception):
    def __init__(self, last_guess):
        self.last_guess = last_guess


def improve(update, done, guess=1, max_updates=1000):
    k = 0
    try:
        while not done(guess) and k < max_updates:
            guess = update(guess)
            k += 1
    except ValueError:
        raise IterImproveError(guess)
