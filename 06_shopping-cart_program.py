def cart():
    dictionary={}
    total_price=0
    while True:
        choice=int(input("Enter 1 for adding an element to cart\n Enter 2 for removing element from cart\n Enter 3 for viewing your list of items in the cart\nEnter 4 for exiting this program:- \t"))
        if choice==1:
            item=input("Enter name of item that you want to add to the list of items of the cart:-\t")
            price=int(input("Enter the price of the item that you added:-\t"))
            dictionary[item]=price
            total_price=total_price+price
            print(f"the total price of all your items that you added in the cart is{total_price}\n meanwhile the items along with the price is {dictionary}\t")
        elif choice==2:
            item=input("Enter the name of the item that you wanted to remove from the cart of the list:-\t")
            if item in dictionary:
                remove_value=dictionary.pop(item)
                print(f"the item that you removed from the list is {remove_value}\n therefore the cart is {dictionary}")
                cost=dictionary.values(item)
                break
            
                total_price= total_price-cost
            else:
                print(f"please enter the item that is in your list \n as the item that you entered is not in the list\n the elements in  your cart are as follows \n {dictionary}")
        elif choice==3:
            print(f"the items in your list are as follows\n{dictionary}\n the total_price of all the goods that you placed in the cart is equal to {total_price}")
        elif choice==4:
            print("thanks for choosing our services \n ______________________________________________________________________________________________________________________________________________________________________________________________")
        else:
            print("please enter a valid choice as the choice tht you entered is not on the meny=iun list")
cart()




