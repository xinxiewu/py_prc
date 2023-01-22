def sym_dif(m_int, n_int):
    res = sorted(m_int.difference(n_int).union(n_int.difference(m_int)))
    for i in res:
        print(i)

if __name__ == '__main__':
    m = int(input())
    m_int = set(map(int, input().split()))
    n = int(input())
    n_int = set(map(int, input().split()))
    sym_dif(m_int, n_int)