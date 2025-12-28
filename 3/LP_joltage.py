def findMaxJoltage(battery_bank):
    max,min = int(battery_bank[0]),int(battery_bank[1])
    min_index = 1 
    for i in range(1,len(battery_bank)-1):
        j = i+1
        if(int(battery_bank[i])>max):
            max = int(battery_bank[i])
            # if(min_index==i):
            #     min = 0
            min = 0
        if(int(battery_bank[j])>min):
            min = int(battery_bank[j])
            # min_index = j
    return 10*max+min

def getMaxJoltageSum(input_path):

    sum_maxJoltage = 0
    try:
        with open(input_path, 'r') as file:
            for line in file:
                maxJoltage = findMaxJoltage(line.strip())
                sum_maxJoltage = sum_maxJoltage + maxJoltage

    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return sum_maxJoltage


def main():

    joltage_sum = getMaxJoltageSum('input.txt')
    print('The Joltage SUM is : ',joltage_sum)

if __name__ == '__main__':
    main()