def get_element(category_name: str):
    """Print less selled elemement in iven category 

    Args:
        category_name (str): name of your category
    """    
    # Parse data from file
    with open("./products.csv", "r") as f:
        data = [i.replace("\n", "").split(";") for i in f.readlines()]
    #Getting all elements of given category
    category = [_ for _ in data if _[0] == category_name]
    #Checking if given category exists
    if len(category) == 0:
        print("Такой категории не существует в нашей БД")
        return
    #Getting data of min Count element in given category
    min_item = min([el[4] for el in category])
    el = [_[1] for _ in category if _[4] == min_item]
    print(
        f"В категории: {category_name} товар: {el[0]} был куплен {min_item} раз"
    )
    return


if __name__ == "__main__":
    category_name = input()
    #Getting data while input is not equal to "Молоко"
    while category_name  != "Молоко":
        get_element(category_name=category_name)
        category_name = input()