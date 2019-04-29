import biluo
dicts = open("texto.txt","r");
dicts = dicts.read();
dicts = dicts.split(" ");
x,y = biluo.startBiluo(dicts)
names = biluo.full_names(x,y)
print(names)

                
            

