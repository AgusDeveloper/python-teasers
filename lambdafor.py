funcs = []
for i in range(3):
    print(i)
    funcs.append(lambda: i)
    
print([f()for f in funcs])