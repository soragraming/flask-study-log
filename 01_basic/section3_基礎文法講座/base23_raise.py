# raise, 例外作成

class Myexception(Exception):
    pass

class CustomError(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(self.message)

def devide(a, b):
    if b == 0:
        raise Myexception('0で割るな！')
        raise ZeroDivisionError('0では割り切れません')
    return a / b

try:
    c = devide(8, 0)
    print(c)
except ZeroDivisionError as e:
    print(e)
except Myexception as e:
    print(e)
except CustomError as e:
    print(e.message, e.code)