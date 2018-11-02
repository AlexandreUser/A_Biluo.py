import biluo
dicts = ["Eu","sou","Alexandre","Vieira","e","Carlos","e","meu","amigo","João","são","legais"]
x,y = biluo.startBiluo(dicts)
def fix(x,y):
    names = []
    tags = []
    compost = []
    for i in range(0,len(y)):
        if(x[i] != "O-PER"):
            names.append(y[i])
            if(x[i] == "L-PER" or x[i] == "U-PER"):
                names.append(",")
    names = " ".join(names)
    names = names.split(",")
    for name in names:
        if (len(name) > 1):
            compost.append(name)
    return compost

names = fix(x,y)
print(names)

                
            

