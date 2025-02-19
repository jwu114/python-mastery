def portfolio_cost(filename):
    sum = 0.0
    with open(filename, "r") as file:     
        try:
            for line in file:
                words = line.split()
                sum += int(words[1]) * float(words[2])
        except ValueError:
            print("ValueError: Could not convert data to an integer or float.")
    return sum
    
print(portfolio_cost('./portfolio3.dat'))