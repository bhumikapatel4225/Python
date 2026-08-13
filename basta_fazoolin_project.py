class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return f"{self.name} menu available from {self.start_time} am to {self.end_time} pm"
  
  def calculate_bill(self, purchased_items):
    bill_amount = 0
    for item in purchased_items:
      bill_amount += self.items[item]
    return bill_amount

# Brunch Menu
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch = Menu("Brunch", brunch_items, 11, 16)
print(brunch)
brunch_total_amount = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
print("Brunch Total Amount:",brunch_total_amount)

# Early-birld Menu
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu("Early-bird", early_bird_items, 15, 18)
early_bird_total_amount = early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])
print("Early-bird Total Amount:",early_bird_total_amount)

# Dinner Menu
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner = Menu("Dinner", dinner_items, 17, 23)

# Kids Menu
kids_item = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu("Kids'", kids_item, 11, 21)

# Take a' Arepa Menu
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take a' Arepa", arepas_items, 10, 20)


class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available_menu = []
    for menu in self.menus:
      if menu.start_time <= time < menu.end_time:
        available_menu += [menu.items]
    return available_menu

menus = [brunch, early_bird, dinner, kids]
flagship_store = Franchise("1232 West End Road", menus)
print("At 12 noon:", flagship_store.available_menus(12))
print("At 5 pm:", flagship_store.available_menus(17))
new_installment = Franchise("12 East Mulberry Street", menus)
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])


class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
Business("Take a' Arepa", [arepas_place])