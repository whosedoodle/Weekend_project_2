shopping_cart = {}

def shopping():
    yes_or_no = input('What would you like to do? Add/Remove/Review/Checkout: ')
    if yes_or_no == 'Add':
        item = input('What item would you like?: ')
        quantity = input('How many would you like?: ')
        shopping_cart.update({'item': quantity})
    if yes_or_no == 'Remove':
            remove = input('Which item would you like to remove?: ')
            del shopping_cart['remove']
    if yes_or_no == 'Review':
            print(shopping_cart)
    if yes_or_no == 'Checkout':
            print('Have a nice day.')

shopping()