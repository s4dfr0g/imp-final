def main():
    #Parse data from file
    with open('./products.csv', 'r') as f:
        data = [i.replace('\n', '').split(';') for i in f.readlines()]

    header = data[0]+['total']
    new_data = []

    #Adding new column "total" to data
    for row in data[1:]:
        total = float(row[3])* float(row[4])
        new_data.append(row+[total])

    #Writing new data to file
    with open('./products_new.csv', 'w') as f:
        f.write(";".join(header)+"\n")
        f.writelines([";".join(map(str,row))+"\n" for row in new_data])

    #Counting total sum where Category is "Закуски"
    result = sum([_[-1] for _ in new_data if _[0] == "Закуски"])

    print(result)

if __name__ == "__main__":
    main()