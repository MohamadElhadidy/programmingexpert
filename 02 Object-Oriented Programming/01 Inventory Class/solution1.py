
class Inventory:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.items = []

    def add_item(self, name, price, quantity):
        sums = quantity
        for item in self.items:
            sums += item[2]
            if item[0] == name:
                return False
        if self.max_capacity < sums:
            return False
        self.items.append([name, price, quantity])
        return True

    def delete_item(self, name):
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)
                return True

        return False

    def get_items_in_price_range(self, min_price, max_price):
        new_list = []
        for item in self.items:
            if item[1] >= min_price and item[1] <= max_price:
                new_list.append(item[0])
        return new_list

    def get_most_stocked_item(self):
        if len(self.items) == 0:
            return None
        else:
            new_dict = {}
            for item in self.items:
                new_dict[item[0]] = item[2]
            return sorted(new_dict, reverse=True, key=new_dict.get)[:1][0]
