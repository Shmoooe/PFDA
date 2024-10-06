# to read a CSV file and output each line as a list
# Author: Joanna Kelly

import csv

FILENAME = "data.csv"

with open (FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount:
            pass
        else:
            total += line[1]
        linecount += 1
    print(f"average is {total/(linecount-1)}")
        
