def discount():
    import sys
    
    prohibited = set(",.")
    total = input("Enter the total of your grocery: ")
    
    if any(char in prohibited for char in total):
        print(f"Please don't use these symbols: {prohibited}")
        sys.exit()
    
    try:
        total = int(total)
    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")
        sys.exit()
    
    discount = 0
    
    
    if total >= 1000000:
        discount = 10 / 100 * total
    elif total >= 500000:
        discount = 5 / 100 * total
    elif total >= 100000:
        discount = 2 / 100 * total
    
    final_total = total - discount
    
    print(f'''
    Before discount total\t: {total}
    Discount\t\t\t: {discount}
    After discount total\t: {final_total}
    ''') 

discount()