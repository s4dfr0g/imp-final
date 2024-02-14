def main():
    # Parse data from file
    with open("./products.csv", "r") as f:
        data = [i.replace("\n", "").split(";") for i in f.readlines()]

    header = data[0] + ["total"]

    #Sort
    for i in range(1, len(data)):
        while (data[i][0] if data[i][0] != None else 0) < (
            data[i - 1][0] if data[i - 1][0] != None else 0
        ) and i != 0:
            data[i], data[i - 1] = data[i - 1], data[i]
            i -= 1

    first_category = [data[1]]

    #Getting items of first category
    for i in range(2, len(data)):
        if data[i][0] == data[i - 1][0]:
            first_category.append(data[i])
        else:
            break
    
    #Getting data of max item in that category
    max_item = max([el[3] for el in first_category])
    el = [_[1] for _ in first_category if _[3] == max_item]
    print(
        f"В категории: {first_category[0][0]} самый дорогой товар: {el[0]} его цена за единицу товара составляет {max_item}"
    )


if __name__ == "__main__":
    main()
