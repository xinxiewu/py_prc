SIGN = 'H'

def logo(thickness):
    # Top Cone
    for i in range(thickness):
        print((SIGN*i).rjust(thickness-1)+SIGN+(SIGN*i).ljust(thickness-1))
    #Top Pillars    
    for i in range(thickness+1):
        print((SIGN*thickness).center(thickness*2)+(SIGN*thickness).center(thickness*6))
    #Middle Belt
    for i in range((thickness+1)//2):
        print((SIGN*thickness*5).center(thickness*6))
    #Bottom Pillars
    for i in range(thickness+1):
        print((SIGN*thickness).center(thickness*2)+(SIGN*thickness).center(thickness*6))
    #Bottom Cone
    for i in range(thickness):
        print(((SIGN*(thickness-i-1)).rjust(thickness)+SIGN+(SIGN*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

if __name__ == '__main__':
    thickness = int(input())
    logo(thickness)