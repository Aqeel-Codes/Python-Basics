import os
import re

lst = {}
crop_list = []
livestock = []
hs = []
hs_sales = []


def menu():
    print("1 : create user ")
    print("2 : log in  user ")


def check_password(password):
    if len(password) <= 9:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not re.search("[!@#$%^&*]", password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True


def create_user(username, password):
    if username in lst:
        print("Username already exists. Please choose another username.")
        return False
    if not check_password(password):
        print("Password must be 10 characters long and contain at least one uppercase letter, one special character, and one digit.")
        return False
    lst[username] = password
    os.system('cls')
    print("User created successfully!")
    return True


def crop(crop_list):
    print("1 : Add new crops to the farm inventory ")
    print("2 : Remove crops from the inventory ")
    print("3 : Update crop details such as name, quantity, price, etc ")
    print("4 : Display the current crop inventory list ")
    print("5 : Exit")
    c = int(input("Enter your choice : "))
    if c == 1:
        return crop_inventory(crop_list)
    elif c == 2:
        return crop_inventory_remove(crop_list)
    elif c == 3:
        return update_crops_inventory(crop_list)
    elif c == 4:
        return current_crops_inventory(crop_list)
    elif c == 5:
        os.system('cls')
        return managements()
    else:
        print("Incorrect input")

def crop_inventory(crop_list):
    crop_type = input("Enter the type of livestock: ")
    crop_quantity = int(input("Enter the quantity: "))
    crop_price = float(input("Enter the price per unit: "))
    crop_list.append({"Type": crop_type, "Quantity": crop_quantity, "Price": crop_price})
    print("Crops added to inventory.")
    os.system('cls')
    return


def crop_inventory_remove(crop_list):
    i = int(input("Enter the index of the livestock to remove: "))
    if 0 <= i < len(crop_list):
        crop_list.pop(i)
        os.system('cls')
        print("removed")
    else:
        os.system('cls')
        print("Invalid index.Enter the correct index ")
        crop_inventory_remove(crop_list)

def update_crops_inventory(crop_list):
    if not crop_list:
        print("Inventory is empty ")
        return
    print("Current Livestock Inventory:")
    print(crop_list)
    i = int(input("Enter the index of the crops_stock to update: "))
    if 0 <= i < len(crop_list):
        crop_type = input("Enter the updated type of crops_stock: ")
        crop_quantity = int(input("Enter the updated quantity: "))
        crop_price = float(input("Enter the updated price per unit: "))
        crop_list[i] = {"type": crop_type, "quantity": crop_quantity, "price": crop_price}
        os.system('cls')
        print("Livestock details updated.")
    else:
        os.system('cls')
        print("Invalid index.Enter the correct index ")
        update_crops_inventory(crop_list)


def current_crops_inventory(crop_list):
    if not crop_list:
        print("Inventory is empty ")
        return
        os.system('cls')
    for i, item in enumerate(crop_list):
        crop_list= print(f"{i}. Type: {item['type']}, Quantity: {item['quantity']}, Price per unit: {item['price']}")


def livestock_inventory(livestock):
    livestock_type = input("Enter the type of livestock: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price per unit: "))
    livestock.append({"Type": livestock_type, "Quantity": quantity, "Price": price})
    os.system('cls')
    print("Livestock added to inventory.")
    

def remove_livestock_inventory(livestock):
    i = int(input("Enter the index of the livestock to remove: "))
    if 0 <= i < len(livestock):
        livestock.pop(i)
        os.system('cls')
        print("removed")
    else:
        os.system('cls')
        print("Invalid index.Enter the correct index")
        remove_livestock_inventory(livestock)

def update_livestock_inventory(livestock):
    if not livestock:
        print("Inventory is empty ")
        return
    print("Current Livestock Inventory:")
    print(livestock)
    i = int(input("Enter the index of the livestock to update: "))
    if 0 <= i < len(livestock):
        livestock_type = input("Enter the updated type of livestock: ")
        quantity = int(input("Enter the updated quantity: "))
        price = float(input("Enter the updated price per unit: "))
        livestock[i] = {"type": livestock_type, "quantity": quantity, "price": price}
        os.system('cls')
        print("Livestock details updated.")
    else:
        os.system('cls')
        print("Invalid index.")
        update_livestock_inventory(livestock)

def current_livestock_inventory(livestock):
    if not livestock:
        print("Inventory is empty ")
        return
    for i, item in enumerate(livestock):
        livestock = print(f"{i}. Type: {item['type']}, Quantity: {item['quantity']}, Price per unit: {item['price']}")


def livestock_management(livestock):
    print("1 : Add new livestock to the farm inventory ")
    print("2 : Remove livestock from the inventory ")
    print("3 : Update livestock details such as type, quantity, price, etc ")
    print("4 : Display the current livestock inventory list ")
    print("5 : Exit")
    c = int(input("Enter your choice : "))
    if c == 1:
        return livestock_inventory(livestock)
    elif c == 2:
        return remove_livestock_inventory(livestock)
    elif c == 3:
        return update_livestock_inventory(livestock)
    elif c == 4:
        return current_livestock_inventory(livestock)

    elif c == 5:
        os.system('cls')
        return managements()
    else:
        print("Incorrect input")

def harvested_record(hs):
    crop_name = input("Enter the crop name : ")
    quantity = int(input("Enter quantity : "))
    hs.append({"type": "harvested", "name": crop_name, "quantity": quantity})
    os.system('cls')
    print("Recorded")

def sales_transaction(hs_sales):
    crop_name = input("Enter the crop name : ")
    quantity = int(input("Enter quantity : "))
    price = float(input("Enter the price per unit : "))
    hs_sales.append({"type": "Sold", "name": crop_name, "quantity": quantity, "price": price})
    os.system('cls')


def display_record(hs,hs_sales):
    os.system('cls')
    print("*****Record of harvested crop ***** ")
    print(hs)
    print("***** Record of sales transaction *****")
    print(hs_sales)


def hs_management(hs,hs_sales):
    while True:
        print("\nHarvest and Sales Management Menu:")
        print("1. Record harvest")
        print("2. Record sales transaction")
        print("3. Calculate total sales and profits")
        print("4. Display harvest and sales history")
        print("5. Exit")
        c = int(input("Enter your choice : "))
        if c == 1:
            return harvested_record(hs)
        elif c == 2:
            return sales_transaction(hs_sales)
        elif c == 3:
            print("Total Sales and profits")

        elif c == 4:
            return display_record(hs,hs_sales)
        elif c == 5:
            os.system('cls')
            return managements()
        else:
            return False


def managements():
    print("1. Crop Managemnet")
    print("2. Livestock Management")
    print("3. Harvest and Sales Management")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        print("Crop inventory")
        while True:
            crop(crop_list)
    elif ch == 2:
        print("Livestock Management")
        while True:
            livestock_management(livestock)
    elif ch == 3:
        print("Harvest and Sales Management ")
        while True:
            hs_management(hs, hs_sales)


while True:
    menu()
    choice = int(input("Enter your choice : "))
    if choice == 1:
        username = input("Enter username: ")
        password = input("Enter password: ")
        create_user(username, password)
        print(lst)
    elif choice == 2:
        print("Enter username and password for log in :")
        username = input(" Username : ")
        password = input(" Password : ")
        if username in lst:
            if lst[username] == password:
                os.system('cls')
                print("Logged In")
                managements()
            else:
                print("Incorrect password")
        else:
            os.system('cls')
            print("incorrect username data")
