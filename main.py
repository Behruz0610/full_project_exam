from models import create_tables
import shop

def main():
    create_tables()
    current_user = None

    while True:
        print(""")
Options:
1. Register
2. Login
3. Add Product (Admin)
4. List Products
5. Add to Cart
6. View Cart
7. Exit
""")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            shop.register(username, password)
        elif choice == '2':
            username = input("Username: ")
            password = input("Password: ")
            user = shop.login(username, password)
            if user:
                current_user = user
        elif choice == '3':
            if current_user and current_user['is_admin']:
                name = input("Product Name: ")
                price = float(input("Price: "))
                shop.add_product(name, price)
            else:
                print("\nAdmin access required.")
        elif choice == '4':
            shop.list_products()
        elif choice == '5':
            if current_user:
                product_id = int(input("Enter product ID to add to cart: "))
                shop.add_to_cart(current_user['user_id'], product_id)
            else:
                print("\nLogin required.")
        elif choice == '6':
            if current_user:
                shop.view_cart(current_user['user_id'])
            else:
                print("\nLogin required.")
        elif choice == '7':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option.")

if __name__ == "__main__":
    main()
