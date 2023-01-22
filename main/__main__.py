from collections import deque

if __name__ == '__main__':
    n = int(input())
    op_list = [input().lower() for i in range(n)]
    deq = deque()
    for op in op_list:
        getattr(deq, op.split()[0])(*map(int, op.split()[1:]))
    
    print(' '.join(list(str(i) for i in deq)))