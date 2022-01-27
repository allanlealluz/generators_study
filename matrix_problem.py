def solution(matrix):
    position = soma = uj = 0
    for l in range(0, len(matrix)):
        # print(f'linhas {l}')
        print(f'matrix original {matrix}')
        for c in matrix[l]:
            if c == 0:
                for num in range(0,len(matrix)):
                    print(matrix[l][position])
                    matrix[num][position] = 0
            position += 1
        for n in matrix[l]:
            soma += n
        print(f'soma {soma}')
        print(f'matrix alterada {matrix}')
        position = 0
solution([[0,1,1,2],
 [0,5,0,0],
 [2,0,3,3]])