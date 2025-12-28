def solveEquation(eq1,eq2,eq3,eq4,operator):
    if(operator=='+'):
        answer = int(eq1) + int(eq2) + int(eq3) + int(eq4)
        # print(f'{eq1} {operator} {eq2} {operator} {eq3} {operator} {eq4} = ',answer)
        return answer
    else:
        answer = int(eq1) * int(eq2) * int(eq3) * int(eq4)
        # print(f'{eq1} {operator} {eq2} {operator} {eq3} {operator} {eq4} = ',answer)
        return answer


def solveHomework(equations):
    sum_of_equations = 0
    for i in range(len(equations[0])):
        sum_of_equations = sum_of_equations + solveEquation(equations[0][i],equations[1][i],equations[2][i],equations[3][i],equations[4][i])
        # print(sum_of_equations)

    return sum_of_equations

def getHomeworkData(input_path):

    equations = []
    try:
        with open(input_path, 'r') as file:
            for line in file:
                equations.append([x for x in line.strip().split()])            

    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return equations


def main():

    equations = getHomeworkData('input.txt')
    # print("Initial Equations: ",equations)
    homework_result = solveHomework(equations)
    print('The solution of the Homework is : ',homework_result)

if __name__ == '__main__':
    main()