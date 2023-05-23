class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class CartItem:
    def __init__(self, product, quantity, gift_wrap):
        self.product = product
        self.quantity = quantity
        self.gift_wrap = gift_wrap


class DiscountRule:
    def __init__(self, name, condition, discount):
        self.name = name
        self.condition = condition
        self.discount = discount


def calculate_discount(cart_items):
    discounts = []
    total_quantity = sum(item.quantity for item in cart_items)

    for item in cart_items:
        if item.quantity > 10:
            discounts.append(DiscountRule("bulk_5_discount", item.product.name, item.product.price * 0.05))

    if total_quantity > 20:
        discounts.append(DiscountRule("bulk_10_discount", "Cart Total", calculate_cart_total(cart_items) * 0.1))

    if total_quantity > 30 and any(item.quantity > 15 for item in cart_items):
        discount_amount = sum((item.quantity - 15) * (item.product.price * 0.5) for item in cart_items if item.quantity > 15)
        discounts.append(DiscountRule("tiered_50_discount", "Above 15 Quantity Products", discount_amount))

    return max(discounts, key=lambda discount: discount.discount, default=None)


def calculate_cart_total(cart_items):
    return sum(item.product.price * item.quantity for item in cart_items)


def calculate_gift_wrap_fee(cart_items):
    return sum(item.quantity for item in cart_items)


def calculate_shipping_fee(cart_items):
    total_quantity = sum(item.quantity for item in cart_items)
    return (total_quantity // 10) * 5


def main():
    products = [
        Product("Product A", 20),
        Product("Product B", 40),
        Product("Product C", 50)
    ]

    cart_items = []
    for product in products:
        quantity = int(input(f"Enter the quantity of {product.name}: "))
        gift_wrap = input(f"Is {product.name} wrapped as a gift? (yes/no): ").lower() == "yes"
        cart_items.append(CartItem(product, quantity, gift_wrap))

    print("\nProduct Details:")
    for item in cart_items:
        total_amount = item.product.price * item.quantity
        print(f"Product: {item.product.name}, Quantity: {item.quantity}, Total Amount: ${total_amount}")

    subtotal = calculate_cart_total(cart_items)
    print("\nSubtotal:", subtotal)

    discount = calculate_discount(cart_items)
    if discount:
        print(f"\nDiscount Applied: {discount.name}, Discount Amount: ${discount.discount}")

    gift_wrap_fee = calculate_gift_wrap_fee(cart_items)
    print("\nGift Wrap Fee:", gift_wrap_fee)

    shipping_fee = calculate_shipping_fee(cart_items)
    print("Shipping Fee:", shipping_fee)

    total_amount = subtotal - (discount.discount if discount else 0) + gift_wrap_fee + shipping_fee
    print("\nTotal Amount:", total_amount)


if __name__ == '__main__':
    main()

