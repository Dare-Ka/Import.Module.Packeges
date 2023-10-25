from package.salary import calculate_salary
from package.people import get_employees
import datetime


def main():
    print(datetime.date.today())
    calculate_salary()
    get_employees()


if __name__ == '__main__':
    main()
