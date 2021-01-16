diffrenter = ["aller"]
a = input(str("Entrez un verbe de permier groupe : "))
#definition to do the verbe
def verb():
    size = len(a)
    print(str("Je ")+ str(a[:size -2])+"e")
    print(str("Tu ")+ str(a[:size -2])+"es")
    print(str("Il/Elle ")+ str(a[:size -2])+"e")
    print(str("Nous ")+ str(a[:size -2])+"ons")
    print(str("Vous ")+ str(a[:size -2])+"ez")
    print(str("Ils/Elles ")+ str(a[:size -2])+"ent")

def valler():
    print("Je vais")
    print("Tu vas")
    print("Il/Elle va")
    print("Nous allons")
    print("Vous allez")
    print("Ils/Elles vont")

#check the user input 
while True:
    if a == "aller":
        valler()
        break
    elif a[-2:] == "er":
        print("Correct")
        verb()
        break   
    else:
        a = input(str("Entrez un verbe de permier groupe : "))

