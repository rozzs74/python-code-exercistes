#https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?h_r=next-challenge&h_v=zen
# x + n = z
# n + y = z
# if both n is equal in both equation the mouse escape
# if eq 1 is higher than eq 2 ans  is eq1 otherwise eq2
# Where n is must be an absolute value
def catAndMouse(x, y, z):
    catA = abs(z - x)
    catB = abs(z - y)
    print(f"Cat A = {abs(catA)}")
    print(f"Cat b = {abs(catB)}")
    if catA == catB:
        return "Mouse C"
    elif catA > catB:
        return "Cat B"
    else: 
        return "Cat A"
        
a = catAndMouse(2, 5, 4)    
# a =catAndMouse(1, 2, 3)
# a = catAndMouse(1, 3, 2)
print(f"final answer {a}")