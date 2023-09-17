# Определение простое число или составное


import argparse
import logging
from functools import wraps

FORMAT = \
    '{levelname:<8} - {asctime}. В модуле "{name}" ' \
    'в строке {lineno:03d} функция "{funcName}()" ' \
    'в {created} секунд записала сообщение: {msg}'

logging.basicConfig(format=FORMAT,
                    style='{',
                    filename="log_for_task2.log",
                    encoding='utf-8',
                    level=logging.ERROR,
                    filemode='a')

logger = logging.getLogger(__name__)


def deco(func: callable):

    @wraps(func)
    def wrapper(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except Exception as message_errors:
            logger.error(f'Функция {func.__name__} '
            f'с аргументами {args = }, '
            f'{kwargs =} выдвала ошибку: '
            f'{message_errors = }')
            return None

    return wrapper

MAX_VALE =100_000

@deco
def num_check(num):
    num = int(num)
    if num <= 0 or num > MAX_VALE:
        result = "введено не корретное число"
        return result
    elif num > 0 and num < MAX_VALE:
        if num > 2:
            count = 0
            for i in range(1,num):
                if num % i == 0:
                    count += 1 
            if count > 1:
                result = "число составное"
            else:
                result = "число простое"
            return result



def pars():
    parser = argparse.ArgumentParser(description='My second argument parser')
    parser.add_argument('-n', '--num', type=str)
    args = parser.parse_args()
    return num_check(f'{args.num}')


if __name__ == '__main__':
    print(pars())