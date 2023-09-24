def távol_keleti(év):
    ciklus_k = 1984
    ciklus_v = 2043

    if év < ciklus_k or év > ciklus_v:
        return "Nincs ilyen a japán naptárban"

    színek = ["zöld", "piros", "sárga", "fehér", "fekete"]
    evszam = év - ciklus_k + 1
    színkód = (evszam - 1) % 60
    szín = színek[színkód // 12]
    return szín
év = int(input("Adjon meg egy évet (1984-2043): "))
szín = távol_keleti(év)
print(f"{év} az {szín} színű év a naptár szerint.")
