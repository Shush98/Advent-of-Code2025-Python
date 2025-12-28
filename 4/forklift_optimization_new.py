def get_adjacent_sum(paper_grid,adjacent):
    sum = 0
    for x in adjacent:
        if(x[0]>=0 and x[0]<len(paper_grid) and x[1]>=0 and x[1]<len(paper_grid[0])):
            sum+=paper_grid[x[0]][x[1]]
    return sum

def findPaperRolls(paper_grid):
    paper_roll_indices = []
    for i in range(len(paper_grid)):
        for j in range(len(paper_grid[i])):
            if(paper_grid[i][j]==1):
                adjacent_sum = get_adjacent_sum(paper_grid,[(i-1,j),(i+1,j),(i,j-1),(i,j+1),(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)])
                if(adjacent_sum<4):
                    paper_roll_indices.append((i,j))
    return paper_roll_indices

def forkliftIterations(paper_grid):
    paper_roll_indices_master = []
    while True:
        paper_roll_indices = findPaperRolls(paper_grid)
        if(len(paper_roll_indices)==0):
            break
        paper_roll_indices_master = paper_roll_indices_master + paper_roll_indices
        for roll in paper_roll_indices:
            paper_grid[roll[0]][roll[1]] = 0
        
    return len(paper_roll_indices_master)
    
def getCountOfPaperRolls(input_path):

    cnt_paper_rolls = 0
    try:
        with open(input_path, 'r') as file:
            paper_grid = []
            for line in file:
                paper_grid.append([1 if x == '@' else 0 for x in line.strip()])

            cnt_paper_rolls = forkliftIterations(paper_grid)
                

    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return cnt_paper_rolls


def main():

    cnt_paper_rolls = getCountOfPaperRolls('input.txt')
    print('The # of paper rolls that can be removed are : ',cnt_paper_rolls)

if __name__ == '__main__':
    main()