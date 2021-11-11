class Dish:
    def __init__(self, name):
        self.name = name
        self.ingredient = []
        self.quatity = []
        self.unit = []

    def add_ingredient(self, new_ingredient):
        self.ingredient.append(new_ingredient)

    def how_ingredient(self, how_quatity):
        self.quatity.append(how_quatity)

    def unit_n(self, unit_name):
        self.unit.append(unit_name)

cook_book = []

question = 'y'
while question == 'y':
    question = input('Добавляем новое блюдо? y/n')
    if question == 'y':
        new_d = Dish(input('Введи название'))
        cook_book.append(new_d.__dict__)
        new_d.add_ingredient(input('введи ингредиент'))
        new_d.how_ingredient(int(input('введи количество')))
        new_d.unit_n(input('Введи еденицу измерения'))

        ques = 'y'
        while ques == 'y':
            ques = input('есть еще ?')
            if ques == 'y':
                new_d.add_ingredient(input('введи ингредиент'))
                new_d.how_ingredient(int(input('введи количество')))
                new_d.unit_n(input('Введи еденицу измерения'))
            elif ques == 'n':
                break

    elif question == 'n':
        question = False
        print('Вышли из программы')

print(cook_book)

## Условно добавили два блюда, как теперь привести это к нормальному виду ????
co = [{'name': 'pizza', 'ingredient': ['becon', 'sausage'], 'quatity': [500, 300], 'unit': ['gr', 'gr']}, {'name': 'salat', 'ingredient': ['zelen', 'tomat'], 'quatity': [500, 3], 'unit': ['gr', 'sht']}]

for i in co:
    print(i['ingredient'][len(i['ingredient'])-1])