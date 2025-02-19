if __name__ == "__main__":
    sum = 0.0
    with open("./portfolio.dat", "r") as file:     
        for line in file:
            words = line.split()
            sum += int(words[1]) * float(words[2])
    print("Total cost: ", sum)