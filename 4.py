def get_promo(name: str, date: str):
    """Generating promocode

    Args:
        name (str): name of element
        date (str): date of element

    Returns:
        str: promocode
    """
    day, month, _ = date.split(".")

    return name[:2].upper() + day + (name[-2:].upper())[::-1] + month[::-1]


def main():
    # Parse data from file
    with open("./products.csv", "r") as f:
        data = [i.replace("\n", "").split(";") for i in f.readlines()]

    header = data[0] + ["promocode"]
    new_data = []

    # Adding new column "promocode" to data
    for row in data[1:]:
        new_data.append(row + [get_promo(name=row[1], date=row[2])])

    # Writing new data to file
    with open("./products_promo.csv", "w") as f:
        f.write(";".join(header) + "\n")
        f.writelines([";".join(map(str, row)) + "\n" for row in new_data])


if __name__ == "__main__":
    main()
