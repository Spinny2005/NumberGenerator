import math
while True:
    result = float(input("Starting value: "))
    step = float(input("Step size: "))
    count = int(input("Steps: "))
    decimal = int(input("Decimal places: "))
    array = []
    for x in range(count):
        result = step + result
        result = round(result, decimal)
        array.append(result)
    print(array)
    
