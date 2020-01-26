"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

QTY_PLANTS = (input('Please insert plants names via space: ')).split(' ')
QTY = len(QTY_PLANTS)
BASE = {}
for i in range(len(QTY_PLANTS)):
    list1 = input(f'Please input EBIT for each quater via space. Plant {QTY_PLANTS[i]}:').split(' ')
    list1 = [int(item) for item in list1]
    BASE[QTY_PLANTS[i]] = list1

AVG_VALUE = sum(map(sum, BASE.values())) / QTY
LIST_LESS = []
LIST_BIG = []
for i in range(QTY):
    if sum(BASE.get(QTY_PLANTS[i])) < AVG_VALUE:
        LIST_LESS.append(QTY_PLANTS[i])
    else:
        LIST_BIG.append(QTY_PLANTS[i])

print(f'Меньше среднего: {LIST_LESS}')
print(f'Больше среднего: {LIST_BIG}')

# Решение через namedtuple

from collections import namedtuple

AVG_EBIT = 0

COMPANY_QTY = 4
Company_info = namedtuple('company', 'name ebit')
company_list = []
for i in range(COMPANY_QTY):
    name_c = input('company name: ')
    total_year = [int(i) for i in input(f'please put an ebit for each quter via space for company {name_c}').split(' ')]
    company = Company_info(name=name_c, ebit=sum(total_year))
    company_list.append(company)

for i in company_list:
    AVG_EBIT += i.ebit
AVG_EBIT = AVG_EBIT / COMPANY_QTY
print(f'Avarage EBIT of all companies: {AVG_EBIT}')
print(f'Companies above avarage EBIT {[i for i in company_list if i.ebit > AVG_EBIT]}')
print(f'Companies less avarage EBIT {[i for i in company_list if i.ebit < AVG_EBIT]}')
