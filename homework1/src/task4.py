
def calculate_discount(price, discount):

    #testing if price/discount is an int or float. Type error if not numberic, value error if not within limits
    if not (isinstance(price, (int, float)) and isinstance(discount, (int, float))):
        raise TypeError("Price and discount must be numeric types")
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - discount / 100)


