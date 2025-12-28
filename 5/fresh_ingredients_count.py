
def isFresh(ingredient, ID_ranges):
    for tupple in ID_ranges:
        if(ingredient in range(tupple[0],tupple[1]+1)):
            return True
    return False

def getFreshIngredientCount(ID_ranges,ingredient_IDs):
    fresh_ingredients_count = 0
    for i in ingredient_IDs:
        if(isFresh(i, ID_ranges)):
            fresh_ingredients_count = fresh_ingredients_count + 1

    return fresh_ingredients_count

def getData(input_path):    
    try:
        with open(input_path, 'r') as file:
            flag = 1
            ID_ranges = []
            ingredient_IDs = []
            for line in file:
                if(line.strip()):
                    if(flag):
                        range = line.strip().split('-')
                        ID_ranges.append((int(range[0]),int(range[1])))
                    else:
                        ingredient_IDs.append(int(line.strip()))
                else:
                    flag = 0
                    continue

    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return (ID_ranges,ingredient_IDs)


def main():

    ID_ranges,ingredient_IDs = getData('input.txt')


    fresh_ingredients_count = getFreshIngredientCount(ID_ranges,ingredient_IDs)
    print('The # of Fresh Ingredients are : ',fresh_ingredients_count)

if __name__ == '__main__':
    main()