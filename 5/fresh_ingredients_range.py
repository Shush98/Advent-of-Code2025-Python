
def getID_count(range_list):
    count = 0
    for tupple in range_list:
        
        count = count + (tupple[1]-tupple[0] + 1)
    return count

def getFreshIngredientCount(ID_ranges):

    ID_ranges = sorted(ID_ranges)
    current_tuple = ID_ranges[0]
    range_list = []
    for tupple in ID_ranges[1:]:
        if(tupple[0]<=current_tuple[1]+1):
           
            listy = list(current_tuple)
            listy[1] = max(current_tuple[1],tupple[1])
            current_tuple = listy
        else:
          
            range_list.append(current_tuple)
            current_tuple = tupple

    range_list.append(current_tuple)

    return getID_count(range_list)

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


    fresh_ingredients_count = getFreshIngredientCount(ID_ranges)
    print('The # of Fresh Ingredient IDs are : ',fresh_ingredients_count)

if __name__ == '__main__':
    main()