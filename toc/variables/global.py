#defining a global inside the fuction
def glob():
    global gb
    gb = 3.146
glob()
r = input('enter radius:')
# initialized the function and using global value of pi
print(gb*r*r)
