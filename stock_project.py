stock = []

#FUNÇÕES

#adicionar produto
def add_product(product):
    stock.append(product)
    print(f"Product {product} added succesfully!\n")

#remover produto    
def remove_product(product_name):
    for product in stock:
        if product ["name"].lower() == product_name.lower():
            stock.remove(product)
            print(f"Product {product_name} removed succesfully!\n")
            return
    print("Product not found\n")

#Listar produtos
def list_products():
    if stock:
        print("List of products:")
        for product in stock:
            print(f"-{product}\n")
    else:
        print("No products found\n")

#menu / escolhas
def menu():
    while True:
        print("----------------------------------------\nWelcome to the stock management system!\n----------------------------------------")
        print("Menu: ")
        print("\n[1]Add product\n[2]Remove product\n[3]List products\n[4]Exit")
        option = (input("Please choose an option: "))
        if option == "1":
            product_name = input("Enter the name of the product: ")
            product_brand = input("Enter the product brand: ")
            product_quantity = input("Type the amount: ")
            product = {
                "name": product_name,
                "brand": product_brand,
                "quantity":product_quantity
            }
            add_product(product)
        elif option =='2':
            product = input ("Enter the name of the product you want to remove: ")
            confirm = input(f"Are you sure you want to remove {product}? (y/n)")
            if confirm == 'y':
                remove_product(product)
            else:
                print("Operation canceled!")
        elif option =='3':
            list_products()
        elif option =='4':
            break
        else:
            print("Invalid option, try again.")
menu()
