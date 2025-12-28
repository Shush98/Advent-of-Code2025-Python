def rotateDial(initPOS, instruction):
    extraZero = 0

    rotation = 1 if(instruction[0]=='R') else -1
    value = int(instruction[1:]) % 100

    extraZero = extraZero + int(int(instruction[1:])/100)
    
    rotatedDial = initPOS + rotation*value

    if(initPOS and (rotatedDial<0 or rotatedDial>100)):
        extraZero = extraZero + 1

    finalPOS = (rotatedDial)%100

    return (finalPOS, extraZero)

def getPassword(input_path):

    password = 0
    initial_position = 50
    try:
        with open(input_path, 'r') as file:
            for line in file:
                final_position, extra_zero = rotateDial(initial_position, line.strip())
                if(final_position == 0):
                    password = password + 1
                password = password + extra_zero

                initial_position = final_position

    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return password


def main():

    password = getPassword('input.txt')
    print('The method 0x434C49434B Password is : ',password)

if __name__ == '__main__':
    main()