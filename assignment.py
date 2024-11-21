def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if the discount is 20% or higher.
    
    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to be applied.
    
    Returns:
        float: The final price after applying the discount or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    
    final_price = calculate_discount(original_price, discount_percentage)

    if discount_percentage >= 20:
        print(f"The discount was applied. The final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price remains: ${original_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for the price and discount percentage.")
