hotel_menu={
    'veg manchurian':250,
    'fried rice':150,
    'veg momos':100,
    'chicken manchurian':350,
    'non veg momo':150
}
##remove 
remove_item=hotel_menu.pop('non veg momo')
print(remove_item)
print(hotel_menu)
#randomly remove item
rmv=hotel_menu.popitem()
print(rmv)
print(hotel_menu)

hotel_menu.clear()
print(hotel_menu)