def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary_all = line.split(',')
                try:
                    salary = int(salary_all)
                    total += salary
                    count += 1
                except ValueError:
                    print('Value Error')
        average = total // count
        return total, average
    except FileNotFoundError:
        print('File not found')

path = 'Temp/salary.txt'
total, average = total_salary(path)
print(f'Загальна сума зарплати: {total}, Середня зарплата: {average}')

