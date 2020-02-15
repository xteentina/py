#price = 100
#discount = 5
#price_with_discount = price - (price * discount / 100)
#print (price_with_discount);

#def discounted (price, discount):
#     price = abs(float(price))
#    discount = abs(float(discount))
#    if discount >= 100:
#        price_with_discount = price
#    else:
#        price_with_discount = price - (price * discount / 100)
#print (price_with_discount)
#return price_with_discount;

def get_summ(one, two, delimiter = '&'):
    one = str(one)
    two = str(two)
    res = one+delimiter+two
    return res

a = get_summ('Learn', 'Python')
print (a.upper());

def format_price(price):
    price = int(price)
    return 'Цена:' price 'руб.'

a = format_price (56)
print(a)