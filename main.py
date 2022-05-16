shopping_cart = {}

def shopping():
    while True:
        to_do = input('What would you like to do? Add/Remove/Review/Checkout: ')
        if to_do == 'Add':
            item = input('What item would you like?: ')
            quantity = input('How many would you like?: ')
            shopping_cart.update({item: quantity})
        if to_do == 'Remove':
                remove = input('Which item would you like to remove?: ')
                del shopping_cart[remove]
        if to_do == 'Review':
                print(shopping_cart)
        if to_do == 'Checkout':
                print(shopping_cart)
                print('Have a nice day.')
                break

shopping()