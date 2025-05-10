print("welcome to the tip calculator")
bill = float(input("what was the total bill? $"))

tip = int(input("what percentage tip would you like to give?  10 15 20 30 40 50\n  "))

people = int(input("how many people to split the bill \n"))

bill_with_tip = bill * (1 + tip / 100)

print(f"total bill with tip is {bill_with_tip} ")

print("thank you")



# hotel menu system



menu = {
    "Pizza":  250,
    "Tea" :  100,
    "Coffee": 200,
    "Momos": 150,
    "Burger" :  120,
    "chauwmin" : 60,
    "sandwich" : 40
    
    
}

def display_menu():
    print("\n *****Hotel Menu*****")
    for items, price in menu.items():
        print(f"{items} : ${price}")

def take_order():
    order={}
    while True:
        item = input("\n Enter the item you want to order(or type 'done' to finish)").capitalize()
        if item == 'Done':
            break
        if item in menu:
            quantity = int(input("how much {items} would you like"))
            order[item]= order.get(item,0) + quantity
        else:
            print("sorry this item is not available. please choose from the menu")
    return order

def calculate_bill(order):
    total_bill=0
    print("\n ****Order Summary****") 
    for item,quantity in order.items():
        item_total=menu[item] * quantity   
        print(f"{item} X {quantity} :  {item_total}")
        total_bill= total_bill + item_total

    print(f"\n Total Bill : ${total_bill}") 


if __name__=="__main__":
    display_menu()
    order = take_order()
    calculate_bill(order)           



     