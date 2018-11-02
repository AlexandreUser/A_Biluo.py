import biluo
dicts = open("texto.txt","r");
dicts = dicts.read();
dicts = dicts.split(" ");
#dicts = ["Eu","sou","Alexandre","Vieira","e","Carlos","e","meu","amigo","João","são","legais"]
x,y = biluo.startBiluo(dicts)
names = biluo.full_names(x,y)
print(names)

                
            

