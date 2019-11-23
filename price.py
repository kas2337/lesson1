def format_price(price):
    price = int(price)
    return f"Price: {price} rub."

pr = format_price(56.24)
print(pr)