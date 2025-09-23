
def calculate_discount(price, discount):
    if not (isinstance(price, (int, float)) and isinstance(discount, (int, float))):
        raise TypeError("Price and discount must be numeric types")
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - discount / 100)


