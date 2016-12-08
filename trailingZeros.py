def find_trailing_zeros(n):
    div_by = 5
    results = []
    while div_by <= n:
        _trailing_zeros = int((n -(n%5))/div_by)
        results.append(_trailing_zeros)
        div_by *= 5
    return sum(results)


if __name__ == '__main__':
    _n = input('enter the number :')
    _n = int(_n)
    zeros = find_trailing_zeros(n=_n)
    print('Number of trailing 0s in '+str(_n)+'! is :'+str(zeros))
