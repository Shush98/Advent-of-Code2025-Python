
def get_invalidIdSUM_from_range(range_item):
    

    LL,UL = range_item.split('-')[0].strip(),range_item.split('-')[1].strip()
    
    sumIDs = 0
    # print(LL,UL)
    for i in range(int(LL),int(UL)+1):
        if(str(i) in (str(i)*2)[1:-1]):
            sumIDs = sumIDs + i

    return sumIDs

def getInvalidIdSUM(input_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read().split(',')

            invalid_id_sum = 0
            for rangeItem in content:
                invalid_id_sum = invalid_id_sum + get_invalidIdSUM_from_range(rangeItem)

            return invalid_id_sum

    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():

    invalidID_sum = getInvalidIdSUM('input.txt')

    print('The Invalid ID SUM is : ',invalidID_sum)

if __name__ == '__main__':
    main()