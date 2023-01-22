if __name__ == '__main__':
    n, n_roll, b, b_roll = int(input()), set(map(int, input().split())), int(input()), set(map(int, input().split()))
    print(len(n_roll.symmetric_difference(b_roll)))

