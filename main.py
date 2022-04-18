from queen import NQueens


def main():
    print('N-Queens Problem :')
    size = int(input('Please enter the size of board: '))
    print_solutions = input(
        'Do you want the solutions to be printed (Y/N): ').lower() == 'y'
    # s = []
    # t = []

    # for i in range(1, 12):
    #     n_queens = NQueens(i)
    #     dfs_solutions, times_result = n_queens.solve_dfs()
    #     s.append(i)
    #     t.append(sum(times_result))

    n_queens = NQueens(size)
    dfs_solutions, times_result = n_queens.solve_dfs()

    print_solutions = False
    if print_solutions:
        for i, (solution, time_taken) in enumerate(zip(dfs_solutions, times_result)):
            print('DFS Solution %d:' % (i + 1))
            n_queens.print(solution)
            print('Time taken: ', time_taken)

    print(
        f"\nTotal DFS solutions: {len(dfs_solutions)} total time taken {sum(times_result)} seconds")
    # print(
    #     s, t
    # )


if __name__ == '__main__':
    main()
