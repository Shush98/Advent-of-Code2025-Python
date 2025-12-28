
def get_invalidIdSUM_from_range(range_item):
    

    LL,UL = range_item.split('-')[0].strip(),range_item.split('-')[1].strip()
    # print(LL,UL)
    # print(len(LL),len(UL))

    LL = str(10**len(LL)) if(len(LL)%2) else LL
    UL = str((10**len(UL))-1) if(len(UL)%2) else UL
    
    LL_len2 = int(len(LL)/2)
    UL_len2 = int(len(UL)/2)

    if(int(LL[:LL_len2])>=int(LL[LL_len2:])):
        LL = LL[:LL_len2]
    else:
        LL = str(int(LL[:LL_len2])+1)
    

    if(int(UL[:UL_len2])>int(UL[UL_len2:])):
        UL = str(int(UL[:UL_len2])-1)
    else:    
        UL = UL[:UL_len2]


    if(int(LL)>int(UL)):
        return 0
    else:
        sumIDs = 0
        # print(LL,UL)
        for i in range(int(LL),int(UL)+1):
            sumIDs = sumIDs + int(str(i)*2)
            # print(int(str(i)*2))
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