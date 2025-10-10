def sudy_nebo_lichy(cislo):
    if cislo % 2==0: # % pro zbytek po dělění a zbytek je 0
        print (f"Číslo {cislo} je sudé!") #f pro vypisování proměnné
    else:
        print (f"Číslo {cislo} je liché!") #podmínka není naplněna


sudy_nebo_lichy (5) #volání funkce
sudy_nebo_lichy(1000000)
    
