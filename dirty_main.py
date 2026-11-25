from datetime import date

from application.db.people import *
from application.salary import *


if __name__ == '__main__':
    print(f'Текущая дата: {date.today():%d.%m.%Y}')
    calculate_salary()
    get_employees()