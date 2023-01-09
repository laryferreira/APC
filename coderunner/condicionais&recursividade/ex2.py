print("O programa funciona?")
resp0 = input()
if resp0 == "SIM":
    print("Você entende o que fez?")
    resp1 = input()
    if resp1 == "SIM":
        print("Ótimo. Então não mexe!")
    elif resp1 == "NAO":
        print("Já foi na tutoria?")
        resp5 = input()
        if resp5 == "SIM":
            print("Choremos!")
        elif resp5 == "NAO":
            print("Temos um time a disposição!")
elif resp0 == "NAO":
    print("Você sabe onde está o erro?")
    resp2 = input()
    if resp2 == "NAO":
        print("Já foi na tutoria?")
        resp5 = input()
        if resp5 == "SIM":
            print("Choremos!")
        elif resp5 == "NAO":
            print("Temos um time a disposição!")
    elif resp2 == "SIM":
        print("Acha que pode solucionar sozinho?")
        resp3 = input()
        if resp3 == "SIM":
            print("Então mão na massa!")
        elif resp3 == "NAO":
            print("Já pesquisou no google?")
            resp4 = input()
            if resp4 == "NAO":
                print("Corre lá então!")
            elif resp4 == "SIM":
                print("Já foi na tutoria?")
                resp5 = input()
                if resp5 == "SIM":
                    print("Choremos!")
                elif resp5 == "NAO":
                    print("Temos um time a disposição!")
