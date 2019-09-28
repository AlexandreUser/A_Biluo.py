def full_names(x,y):
    names = []
    tags = []
    compost = []
    for i in range(0,len(y)):
        if(x[i] != "O-PER"):
            if(x[i] not in names):
                names.append(y[i])
                if(x[i] == "L-PER" or x[i] == "U-PER"):
                    names.append(",")
    names = " ".join(names)
    names = names.split(",")
    for name in names:
        if (len(name) > 1):
            compost.append(name)
    return sorted(set(compost))

def startBiluo(dicts):
    import json
    from_txt = open("nomes_minusculo.txt").read()
    from_txt = from_txt[1:-2]
    from_txt = from_txt.replace("'","")
    from_txt = from_txt.split(",")
    nomes = json.loads(open('cap_names.json').read())
    nomes["cap_names"] = nomes["cap_names"] + from_txt;
    print(nomes)
    #savename = nomes
    exceptions = json.loads(open('exception.json').read())
    tupla = []
    nomes["cap_names"] += [nome.upper() for nome in nomes['cap_names']]
        
    i = 0
    stack = 0
    dicts.append('None')
    dicts.append('None')
    Desc = []
    tags = []
    nomesreais = []
    #position = []
    Unit = 0
    #BegginingPosition = []
    acrescentar = ["e","E","ou","OU"]
    for i in range(0,len(dicts)):
        if dicts[i] in exceptions["exp"]:
            tags.append("O-PER")
            if tags[i-1] == "I-PER":
                tags[i-1] = "L-PER"
            stack = 0
            """
            Essa parte do codigo remove os são paulos, são caetanos dos nomes reais.
            """
        elif dicts[i] in nomes["cap_names"]:
            """
            Aqui começamos a checar se a lista de tokens possui nomes. Desculpe a quantidade de if's
            são ocasiões bem complicadas
            """
            if stack == 0:
                if dicts[i + 1] not in nomes["cap_names"] and dicts[i + 2] not in nomes["cap_names"]:
                    tags.append("U-PER")
                    #nomesreais.append(dicts[i])
                    #tupla.append([dicts[i],"U"])
                    """
                    Aqui é para caso o nome seja unitario
                    """
                elif dicts[i+1] in acrescentar:
                    tags.append("U-PER")
                    #nomesreais.append(dicts[i])
                    #tupla.append([dicts[i],"U"])
                elif dicts[i] not in nomes["cap_names"]:
                    tags.append("O-PER")

                elif dicts[i + 1] in nomes["cap_names"] or dicts[i + 2] in nomes["cap_names"]:
                    stack += 1
                    Unit += 1
                    #BegginingPosition.append(i)
                    tags.append("B-PER")
                    #tupla.append([dicts[i],"B"])
                    #nomesreais.append(dicts[i])
                    """
                    A variavel stack define se ja estamos dentro de um nome ou acabamos de descobrir um,
                    pois se a stack for maior que zero significa que estamos no meio de um nome ja encontrado
                    """





            else:
                if dicts[i] in nomes["cap_names"] and dicts[i + 1] not in nomes["cap_names"]:
                    tupla.append([dicts[i],"L"])
                    #position.append(i)
                    Unit = 0
                    stack = 0
                    #BegginingPosition.append(i)
                    tags.append('L-PER')
                    if tags[i-1] == "O-PER":
                        tags[i-1] = "I-PER"
                    #nomesreais.append(dicts[i])
                    """
                    nessa parte eu defino o final de um nome
                    """

                else:
                    if dicts[i] in nomes["cap_names"]:
                        tags.append('I-PER')
                        #tupla.append([dicts[i],"I"])
                        #nomesreais.append(dicts[i])
                        Unit += 1
                        stack += 1



        elif dicts[i] == "None":
            pass
        else:
            if dicts[i] in nomes["cap_names"]:
                if stack > 0:
                    if dicts[i] == "do" and dicts[i + 1] in nomes["cap_names"]:
                        tags.append("I-PER")
                        #tupla.append([dicts[i],"I"]) 
                        if tags[i-1] == "O-PER":
                            tags[i-1] = "I-PER"
                        #nomesreais.append(dicts[i])

                    elif dicts[i] == "da" and dicts[i + 1] in nomes["cap_names"]:
                        tags.append("I-PER")
                        #tupla.append([dicts[i],"I"])
                        if tags[i-1] == "O-PER":
                            tags[i-1] = "I-PER"
                        #nomesreais.append(dicts[i])

                    elif dicts[i] == "de" and dicts[i + 1] in nomes["cap_names"]:
                        tags.append("I-PER")
                        #tupla.append([dicts[i],"I"])
                        if tags[i-1] == "O-PER":
                            tags[i-1] = "I-PER"
                        #nomesreais.append(dicts[i])

                    elif dicts[i] in nomes["cap_names"] and dict[i + 1] in nomes["cap_names"]:
                        tags.append('I-PER')
                        #tupla.append([dicts[i],"I"])
                        if tags[i-1] == "O-PER":
                            tags[i-1] = "I-PER"

                        #nomesreais.append(dicts[i])
                    else:
                        tags.append('O-PER')
                        if stack > 0:
                            if tags[i - 1] == "I-PER":
                                tags[i - 1] = "L-PER"  
                            stack = 0
        
            else:
                tags.append("O-PER")
                if stack > 0:
                    if tags[i - 1] == "I-PER":
                        tags[i - 1] = "L-PER"  
                    stack = 0
    

        i += 1
    
    dicts.remove("None")
    dicts.remove("None")
    #textos = ""

    #print(tags)
    #for palavra in dicts:
    #    textos += palavra+" "
   
    #print(len(tags) == len(dicts))
    #if len(tags) != len(dicts):
    #    print(dicts)
    #    print(tags)
    return tags, dicts


