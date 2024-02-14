
def main():
    # Parse data from file
    with open("./products.csv", "r") as f:
        data = [i.replace("\n", "").split(";") for i in f.readlines()]

    hash_table = {}

    #Creating hash table
    for row in data[1:]:
        hash_table[row[0]] = 0.0
    for row in data[1:]:
        hash_table[row[0]] += float(row[4])
    
    #Sort and print less selled items
    less_selled = sorted(hash_table.items(), key=lambda x: x[1])
    for i in range(10):
        print(",".join(map(str,less_selled[i])))
   
if __name__ == "__main__":
    main()