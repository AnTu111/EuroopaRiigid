from random import*


valimine = input("Valige allolevatest tehingutest:\n1. - Näita pealinn riigi järgi\n2. - Näita riiki pealinna järgi\n3. - Lisage uus sõna\n4. - Parandus kui viga on tuvastatud\n5. - Mäng (5 küsimust)\n6. - Lõpp\n")



def failist_to_dict(f:str):
    riik_pealinn={}
    pealinn_riik={}
    riigid=[]
    file=open(f,'r',encoding="utf-8-sig")
    for line in file:
        k,v=line.strip().split('-')
        riik_pealinn[k]=v
        pealinn_riik[v]=k
        riigid.append(k)
    file.close()
    return riik_pealinn,pealinn_riik,riigid

riik_pealinn,pealinn_riik,riigid=failist_to_dict("riigid_pealinnad.txt")

def lisamine(country:list,capitals:list,file:str):
    f=open(file,'w',encoding="utf-8-sig")
    for country, capital in riik_pealinn.items():
        f.write(f"{country} - {capital}\n")
    f.close()


def el_lisamine(riik_pealinn: dict, v_riik: str, v_pealinn: str) -> any:
    if v_riik not in riik_pealinn:
        riik_pealinn[v_riik] = v_pealinn
        print(f"riik {v_riik} pealinnaga {v_pealinn} lisatud.")
    else:
        print(f"Riik {v_riik} juba olemas")
    return v_riik,v_pealinn



def mang(riik_pealinn: dict, pealinn_riik: dict, riigid: list):
       import random
       
       for i in riigid[5]: 
             n = random.choice(riigid)
             vastus = input(f"Pealinn riigis {n}: ")
             õige_pealinn = riik_pealinn[n]
             if vastus.title() == õige_pealinn.title():
                oige += 1
                print("Õige!")
             else:
               print(f"Vale! Õige vastus: {õige_pealinn}")
       prots = (oige / 5)*100
       print(f"Teie võit protsentide on{prots}")

            


while True:
    try:
        if valimine == "1":
            riik = input("Siseta riik: ").title()
            print(riik_pealinn[riik])
            break
        elif valimine  =="2":
             pealinn = input("Siseta pealinn: ").title()
             print(pealinn_riik[pealinn])
             break
        elif valimine == "3":
             new_key = input("Sistage uus riik: ")
             new_value = input("Sistage uus pealinn: ")
             el_lisamine(riik_pealinn,new_key,new_value)
             lisamine(new_key,new_value,"riigid_pealinnad.txt")    
             break
        elif valimine == "4":
             uus = str(input("Sisestage riigi nimi: "))
             if uus in riigid:
                vana_pealinn = riik_pealinn[uus]
                uus_pealinn = input(f"Sisestatud riik {uus} ja tema pealinn on {vana_pealinn}. Sisestage uus pealinn: ")
                riik_pealinn[uus] = uus_pealinn
                print(f"Riigi {uus} pealinn on: {uus_pealinn}.")
                lisamine(uus,uus_pealinn,"riigid_pealinnad.txt")
             break
        elif valimine == "5":
              mang(riik_pealinn, pealinn_riik, riigid)
              break
    except KeyError:
     vigade_vastus = print("Sisestatud nimi ei ole korreknte või ei ole leitav./nSoovi korral valige 3(Uue lisamine) või 4(parandamine) programmi käivitamisel")
