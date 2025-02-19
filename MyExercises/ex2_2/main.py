import csv
from collections import Counter

class Row:
    __slot__ = ["route", "date", "daytype", "rides"]
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

if __name__ == "__main__":
    records = []
    my_set = set()
    my_dict = dict()
    my_counter2 = Counter()
    my_counter3 = Counter()
    
    with open("./ctabus.csv") as file:
        rows = csv.reader(file)
        _ = next(rows)
        for line in rows:
            records.append(Row(line[0], line[1], line[2], int(line[3])))
        for record in records:
            my_set.add(record.route)
            my_dict[record.route, record.date] = record.rides
            my_counter2[record.route] += record.rides
            if "2011" in record.date:
                my_counter3[record.route] += record.rides
            elif "2001" in record.date:
                my_counter3[record.route] -= record.rides
    
    print("Question 1:", len(my_set))
    print("Question 2:", my_dict["22", "02/02/2011"])
    print("Question 3:", my_counter2.most_common(3))
    print("Question 4:", my_counter3.most_common(5))
    
    
    
        