roll = True
regresar = True
inventary = []
total = 0
general_total = 0
total_products = 0

def add_product():

    product_name = input("enter the product name: ").lower()
    p_price = float(input("enter the price: "))
    p_quantity = int(input("enter the quantity: "))
    
    produ = {
        "product name": product_name,
        "price": p_price,
        "quantity": p_quantity}

    inventary.append(produ)

def show_inventory():
   
    if inventary == None:
        print("the inventory is empty ")
    
    for i in inventary:
     print("product name|", i["product name"])
     print("price|", i["price"])
     print("quantity|", i["quantity"])
     


def show_total():
    for i in inventary:
        total+=i["price"]*i["quantity"]
        return print(total)
    

def show_total_products():
    for i in inventary:
        total_products+=i["product_name"]
    return print(total_products)

     

while roll: 
    print("-----MENU-----")
    print("1. add product=>  \n2. Show inventory=>   \n3. Statictis=> \n4. Exit =>")
    
    try:
        ask = int(input("please enter a option: "))
    except: (ValueError,TypeError)

    if ask == 1:

        a = input("register a new product? yes/no: ").lower()
        while a == "yes":
          add_product()
          a = input("do you want add a new product? yes/no: ").lower()

       

    elif ask == 2: 
        show_inventory()

    elif ask == 3:

        print("----STADISTICS MENU----")
        print("1. Show inventory total =>  \n2. Show total products => ")

        
        try:
            question = int(input("please, select an option =>"))
        except: (ValueError, TypeError)
        print("enter a value option. try again")

        if question == 1:
                show_total()

        elif question == 2:
            show_total_products()

        regresar = input("do you return the menu?").lower()

        if regresar == "yes":
            print("")
            regresar = True

        elif regresar == "no":
            regresar = False
            print("ok, return menu")

        else:
            print("enter a value option. try again")
            regresar = True

    elif ask == 4:
        print("exit the program, see you later! :)")
        roll = False

    else:
        print("ERROR!")
        raise (TypeError, ValueError) 
    









       
