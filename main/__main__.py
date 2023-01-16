import string

def print_rangoli(size):
    all_alpha = string.ascii_lowercase
    res = []

    for i in range(size):
        s = '-'.join(all_alpha[i: size])
        res.append((s[::-1] + s[1:]).center(4*size - 3, '-'))

    print('\n'.join(res[::-1] + res[1:]))

    return

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)