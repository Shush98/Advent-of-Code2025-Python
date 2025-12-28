def findMaxJoltage(battery_bank):
    # max,min = int(battery_bank[0]),int(battery_bank[1])
    battery_combination = [int(x) for x in battery_bank[:12]]
    # print(battery_combination)
    for i in range(1,len(battery_bank)-11):
        new_battery_options = [int(x) for x in battery_bank[i:i+12]]
        # print(new_battery_options)
        for j in range(12):
            if(new_battery_options[j]>battery_combination[j]):
                battery_combination[j] = new_battery_options[j]
                if(j==11):
                    continue
                else:
                    battery_combination[j+1] = 0

    return int(''.join(map(str, battery_combination)))

def getMaxJoltageSum(input_path):

    sum_maxJoltage = 0
    try:
        with open(input_path, 'r') as file:
            for line in file:
                # print(line)
                maxJoltage = findMaxJoltage(line.strip())
                sum_maxJoltage = sum_maxJoltage + maxJoltage
                # print(maxJoltage)

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