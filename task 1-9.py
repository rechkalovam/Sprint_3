import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    #1 задание
    @property
    def name_items(self):
        return self.__name_items
    
    @property
    def number_items(self):
        return self.__number_items
    
    #2 задание
    def add_item_to_cheque(self, name):
        try:
            if len(name) == 0 or len(name) > 40:
                raise ValueError(f'Нельзя добавить товар, если в его названии нет символов или их больше 40')
            elif name not in self.__item_price:
                raise NameError(f'Позиция отсутствует в товарном справочнике')
            self.__name_items.append(name)
            self.__number_items += 1
        except ValueError as e:
            print(e)
        except NameError as e:
            print(e)

