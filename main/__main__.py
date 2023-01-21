def mutate_string(string, position, character):
    return ''.join([list(string)[i] if i != position else character for i in range(len(string))])
    
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)