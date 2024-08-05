menu = { 
'pizza':40,
'pasta':50,
'burger':60,
"salad":70,
'coffee':80
}

print("Welcome to Python restaurant")
print("Pizza: 40rs \nPasta: 50rs\nBurger:60rs\nSalad:60rs\ncoffee:80rs")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")

if item_1 in menu:
    order_total+= menu[item_1] #0+50
    print(f"Your item {item_1} has been ordered to your order")

else:
    print(f"ordered item {item_1} is not available yet")


another_order = input("Do you want to enter another item(y/n)")
if another_order == "y":
    item_2 = input("enter second item to add to order = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} added to the order")
    else:
        print(f"Ordered item {item_2} isnt available")

print (f"total amount for your order is  {order_total}")