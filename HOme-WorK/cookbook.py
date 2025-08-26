cook_book = {}
with open('recipes.txt', 'r', encoding='utf-8') as file:
    while True:
        # Читаем название блюда
        dish_name = file.readline().strip()
        if not dish_name:  
            break

        
        ing_count = file.readline().strip()
        if not ing_count:  
            break
        ing_count = int(ing_count)

        
        ingredients = []
        for _ in range(ing_count):
            ing_line = file.readline().strip()
            if not ing_line:  
                break
            
            ing_data = ing_line.split('|')
            if len(ing_data) < 3:  
                continue
            ingredient_name = ing_data[0].strip()
            quantity = int(ing_data[1].strip())
            measure = ing_data[2].strip()
            
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        cook_book[dish_name] = ingredients

        empty_line = file.readline()
        if not empty_line:  
            break

for dish, ingredients in cook_book.items():
    print(f"{dish}:")
    for ing in ingredients:
        print(f"  {ing}")






def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count
                
                if name not in shop_list:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
                else:
                    shop_list[name]['quantity'] += quantity
        else:
            print(f"Блюдо '{dish}' не найдено в кулинарной книге")
    return shop_list

