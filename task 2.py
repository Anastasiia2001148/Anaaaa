def get_cats_info(path):
    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cats_info = line.strip().split(',')
                cat_d= ({'id': cats_info[0],'name': cats_info[1],'age': cats_info[2]})
                cats.append(cat_d)
            return cats
    except FileNotFoundError:
        print('File not found')


path = 'Temp/cats.txt'
cats = get_cats_info(path)
print(f'{cats}')