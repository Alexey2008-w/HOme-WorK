cook_book = {
    'индейка в сливочном соусе': [
        {'ingridient_name': 'Филе бедра индейки', 'quantity': 700, 'measure': 'гр'},
        {'ingridient_name': 'Репчатый лук', 'quantity': 150, 'measure': 'гр'},
        {'ingridient_name': 'Сливки', 'quantity': 200, 'measure': 'мл'},
        {'ingridient_name': 'Соевый соус', "quantity": 60, "measure": 'мл'},
        {'ingridient_name': 'Прованские травы', 'quantity': 1, 'measure': 'ст.ложка'},
        {'ingridient_name': 'Мед', 'quantity': 50, 'measure': 'гр'}],
    'рис по-тайски': [
        {'ingridient_name': 'рис', 'quantity': 200, 'measure': 'гр'},
        {'ingridient_name': 'Чеснок', 'quantity': 2, 'measure': 'зубчика'},
        {'ingridient_name': 'Болгарский перец', 'quantity': 100, 'measure': 'гр'},
        {'ingridient_name': 'Репчатый лук', 'quantity': 100, 'measure': 'гр'},
        {'ingridient_name': 'Карри', 'quantity': 1, 'measure': 'ч.ложка'},
        {'ingridient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'},
        {'ingridient_name': 'Зеленый горошек', 'quantity': 50, 'measure': 'гр'}],
    'запеченные яблоки': [
        {'ingridient_name': 'Яблоки (крупные)', 'quantity': 2, 'measure': 'шт'},
        {'ingridient_name': 'Тесто слоенное', 'quantity': 150, "measure": 'гр'},
        {'ingridient_name': 'Орехи грецкие рубленые', 'quantity': 2, 'measure': 'ст.ложки'},
        {'ingridient_name': 'Мед', 'quantity': 30, 'measure': 'гр'},
        {'ingridient_name': 'Яйцо', "quantity": 1, 'measure': 'шт'}
        ]
    }

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']


    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print(
            '{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)
    print()


create_shop_list()