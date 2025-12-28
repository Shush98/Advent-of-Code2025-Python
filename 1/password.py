def rotateDial(initPOS, instruction):

    rotation = 1 if(instruction[0]=='R') else -1
    value = int(instruction[1:]) % 100
    
    finalPOS = (initPOS + rotation*value)%100

    return finalPOS

def getPassword(input_path):

    password = 0
    initial_position = 50
    try:
        with open(input_path, 'r') as file:
            for line in file:
                final_position = rotateDial(initial_position, line.strip())
                if(final_position == 0):
                    password = password + 1
                initial_position = final_position

    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return password


def main():

    password = getPassword('input.txt')
    print('The Password is : ',password)

if __name__ == '__main__':
    main()