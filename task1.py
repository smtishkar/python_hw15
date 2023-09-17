# Проверка года на высокосность


import argparse
import logging
from functools import wraps

FORMAT = \
    '{levelname:<8} - {asctime}. В модуле "{name}" ' \
    'в строке {lineno:03d} функция "{funcName}()" ' \
    'в {created} секунд записала сообщение: {msg}'

logging.basicConfig(format=FORMAT,
                    style='{',
                    filename="log.log",
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

year = 2000
year2 = 2001
year3 = 'RIDK'
MAIN_LEAP_CRYTERIA = 4
ADDITIONAL_LEAP_CRYTERIA = 400
LEAP_EXCLUDINGG_CRYTERIA = 100

@deco
def year_type(year):
    year = int(year)
    if year % MAIN_LEAP_CRYTERIA == 0 and year%LEAP_EXCLUDINGG_CRYTERIA !=0 or year %ADDITIONAL_LEAP_CRYTERIA == 0:
        result = "Год высокосный"
    else: 
        result = "Год обычный"
    return result


def pars():
    parser = argparse.ArgumentParser(description='My first argument parser')
    parser.add_argument('-y', '--year', type=str)
    args = parser.parse_args()
    return year_type(f'{args.year}')


if __name__ == '__main__':
    print(pars())