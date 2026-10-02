# Task 6: Apply a 20% discount for purchases >= Rs. 5000, 10% for
# Rs. 3000-4999, and 5% below Rs. 3000. Return discount and final amount.

def calculate_discount(purchase_amount):
    if purchase_amount < 0:
        raise ValueError("Purchase amount cannot be negative.")

    if purchase_amount >= 5000:
        discount_rate = 0.20
    elif purchase_amount >= 3000:
        discount_rate = 0.10
    else:
        discount_rate = 0.05

    discount_amount = round(purchase_amount * discount_rate, 2)
    final_amount = round(purchase_amount - discount_amount, 2)
    return discount_amount, final_amount


def main():
    try:
        purchase_amount = float(input("Enter the purchase amount in rupees: "))
        discount_amount, final_amount = calculate_discount(purchase_amount)
    except ValueError as error:
        print(error)
        return

    print(f"Discount amount: Rs. {discount_amount:.2f}")
    print(f"Final payable amount: Rs. {final_amount:.2f}")


if __name__ == "__main__":
    main()