import random

slovo = ""
veta = ""
text = ""
pocitadlo_vet = 0

pocet_vet_radek = 3
pocet_radku_odstavec = 4


pocet_odstavcu = 5
pocet_slov_veta = 5

pozice_1 = 0 # přednastavené - možnost 1
pozice_2 = 3

while True:
    print("Vítej, toto je můj Lorem ipsum generátor")
    volba = int(input("Chceš si formát textu nastavit sám [1], nebo použiješ přednastavený? [2]: "))
    if volba == 1:
        print("Dobře můžeš ovlivnit tyto věci: počet odstavců, počet slov ve větě, počet vět na řádku, délku slov, počet řádků v odstavci")
        pocet_odstavcu = int(input("Zadej počet odstavců: "))
        pocet_slov_veta = int(input("Zadej počet slov ve větě: "))
        pocet_vet_radek = int(input("Zadej počet vět na řádku: "))
        pocet_radku_odstavec = int(input("Zadej počet řádků v odstavci: "))
        print("Počet znaků ve slově: ")
        print("Možnost [1] 2-5 znaků")
        print("Možnost [2]  5-9 znaků")
        print("Možnost [3]  9-12 znaků")
        vyber = int(input("Zadej možnost (1/2/3): "))
        if vyber == 1:
            pozice_1 = 0
            pozice_2 = 3
        if vyber == 2:
            pozice_1 = 3
            pozice_2 = 7
        if vyber == 3:
            pozice_1 = 7
            pozice_2 = 10
        break



    if volba == 2:
        print("zvolil jsi přednastavené generování, pro spuštění zmáčkni enter")
        input()
        break

celkovy_pocet_vet = pocet_vet_radek * pocet_radku_odstavec

varianty = [1,2]
varianty_pravdepodobnosti = [4,1]

samohlasky = ["a","á", "e","é", "i","í", "o","ó", "u","ů",]
samohlasky_pravdepodobnosti = [2.5,0.4,0.5,0.3,0.75,0.04,1,0.03,0.5,0.01]

souhlasky = ["b", "c", "č", "d", "ď", "f", "g", "h", "j", "k", "l", "m", "n", "ň", "p", "r","ř", "s", "š", "t", "ť", "v", "w", "x", "y","ý", "z", "ž"]
souhlasky_pravdepodobnosti = [1,0.75,0.5,0.8,0.2,0.5,0.3,1,1,1,1,1,1,0.2,1,0.5,0.2,1,0.2,0.8,0.2,0.8,0.1,0.1,0,0,0.8,0.5]
# generace slova 

varianta_prvni_pismeno = random.choices(varianty, weights= varianty_pravdepodobnosti )
varianta_prvni_pismeno = int(varianta_prvni_pismeno[0])


for z in range(0,pocet_odstavcu):

    varianta_prvni_pismeno = random.choices(varianty, weights= varianty_pravdepodobnosti )
    varianta_prvni_pismeno = int(varianta_prvni_pismeno[0])

    for i in range(0,celkovy_pocet_vet):
        pocitadlo_vet += 1
        for ix in range(0,pocet_slov_veta):
            if varianta_prvni_pismeno == 1:
                prvni_pismeno = random.choices(souhlasky, weights = souhlasky_pravdepodobnosti)
                druhe_pismeno = random.choices(samohlasky, weights = samohlasky_pravdepodobnosti)

                prvni_pismeno = str(prvni_pismeno[0])
                druhe_pismeno = str(druhe_pismeno[0])
            
                if ix == 0:
                    prvni_pismeno = prvni_pismeno.upper()

                slovo += (prvni_pismeno + druhe_pismeno)

                

            else:
                prvni_pismeno = random.choices(samohlasky, weights = samohlasky_pravdepodobnosti)
                druhe_pismeno = random.choices(souhlasky, weights = souhlasky_pravdepodobnosti)

                prvni_pismeno = str(prvni_pismeno[0])
                druhe_pismeno = str(druhe_pismeno[0])

                if ix == 0:
                    prvni_pismeno = prvni_pismeno.upper()

                slovo += (prvni_pismeno + druhe_pismeno)

            pocet_znaku_random = random.randint(pozice_1,pozice_2)


            for iy in range(pocet_znaku_random): # počet znaků ve slově
                if slovo[len(slovo) - 1] in samohlasky:
                    pismeno = random.choices(souhlasky, weights = souhlasky_pravdepodobnosti)
                    pismeno = str(pismeno[0])

                    slovo += pismeno
                else:
                    pismeno = random.choices(samohlasky, weights = samohlasky_pravdepodobnosti)
                    pismeno = str(pismeno[0])

                    slovo += pismeno

            if ix == (pocet_slov_veta - 1):
                veta += (slovo + ". ")
                text += veta
                veta = ""
                slovo = ""
            else:
                veta += (slovo + " ")
                slovo = ""
        if pocitadlo_vet == pocet_vet_radek:
            text += "\n"
            pocitadlo_vet = 0
        
    text += "\n"
    

print(text)



    
