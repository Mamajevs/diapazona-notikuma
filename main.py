def noteiktDiapazonu(d1,d2,sk):
    rezultats = "Skaitlis nav diapozoni"
    if d1>sk<=d2:
        rezultats = "Skaitlis ir diapozoni"
    return rezultats
    
d1 = int(input("Ievadi diapazona sākumu: "))
d2 = int(input("Ievadi diapazona beigas: "))
sk = int(input("Ievadi skaitli: "))
rez = noteiktDiapazonu(d1,d2,sk)
print(rez)