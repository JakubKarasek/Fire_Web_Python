
days = int(input("number of days: "))

def rental_car_cost(days):
    total = 40 * days
    if days >= 7:
        total -= 50
    elif days >= 3:
        total -= 25
    return total

print (rental_car_cost(days))
