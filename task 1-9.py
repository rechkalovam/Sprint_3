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

    #3 задание 
    def delete_item_from_check(self, name):
        try:
            if name not in self.__name_items:
                raise NameError(f'Позиция отсутствует в чеке')
            
            self.__name_items.remove(name)
            self.__number_items -= 1

        except NameError as e:
            print(e)
    
    #4 задание
    def check_amount(self):
        total = []

        for i in self.__name_items:
            total.append(self.__item_price[i])

        total_sum = sum(total)

        if len(self.__name_items) > 10:
            return total_sum * 0.9
        return total_sum
    
    #5 задание
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []

        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item])

        total_sum = sum(total)
        
        if len(self.__name_items) > 10:
            return (total_sum * 0.9) * 0.2
        return total_sum * 0.2
    
    #6 задание
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []

        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item])

        total_sum = sum(total)
        
        if len(self.__name_items) > 10:
            return (total_sum * 0.9) * 0.1
        return total_sum * 0.1
    
    #7 задание
    def total_tax(self):
        total_tax = self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
        return total_tax
    