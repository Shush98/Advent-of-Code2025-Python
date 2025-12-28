import math
def solveEquation(eq_list,operator):
    # print(eq_list,operator)
    if(operator=='+'):
        answer = sum(eq_list)
        # print(f'{eq1} {operator} {eq2} {operator} {eq3} {operator} {eq4} = ',answer)
        # print(answer)
        return answer
    else:
        answer = math.prod(eq_list)
        # print(f'{eq1} {operator} {eq2} {operator} {eq3} {operator} {eq4} = ',answer)
        # print(answer)
        return answer


def solveHomework(equations):
    sum_of_equations = 0
    op = 0
    eq = []
    for i in range(len(equations[0])-1):
        operator = equations[len(equations)-1][op]
        space_counter = 0
        term = 0
        for j in range(len(equations)-1):
            if(equations[j][i]==' '):
                space_counter = space_counter + 1
            else:
                term = 10*term + int(equations[j][i])
        if(space_counter == len(equations)-1):
            op = op + 1
            sum_of_equations = sum_of_equations + solveEquation(eq,operator)
            eq = []

        else:
            eq.append(term)
    sum_of_equations = sum_of_equations + solveEquation(eq,operator)

        # print(sum_of_equations)

    return sum_of_equations

def getHomeworkData(input_path):

    equations = []
    try:
        with open(input_path, 'r') as file:
            for line in file:
                equations.append([x for x in line])  
        equations[len(equations)-1] = (''.join(equations[len(equations)-1])).strip().split()          

    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return equations


def main():

    equations = getHomeworkData('input.txt')
    # print(f"Initial Equations length:")
    # for i in equations:
    #     print(len(i))
        # print(i)
    homework_result = solveHomework(equations)
    print('The solution of the Homework is : ',homework_result)

if __name__ == '__main__':
    main()