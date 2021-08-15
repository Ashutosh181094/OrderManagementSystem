import CartOperation
import MyOrders
import ShowProducts
import WishListOperation


class mainMenu:
    def mainMenuOptions(self):
        print("Select the Operation that you want to perform")
        print("1-Show Products")
        print("2-Go to Cart")
        print("3-Go to Wishlist")
        print("4-Display my Orders")
        print("5-Exit Shopping")
        choice = input()
        if choice == '1':
            ShowProducts.showProducts().showAvailableProducts()
        elif choice == '2':
            CartOperation.Cart().displayCart()
        elif choice == '3':
            WishListOperation.wishList().displayWishList()
        elif choice == '4':
            MyOrders.myOrders().orders()
        elif choice == '5':
            print("Thanks for shopping with Us")
            exit(1)
        else:
            print("Invalid Option Entered")
            exit(1)
