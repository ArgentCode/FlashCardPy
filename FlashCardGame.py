import random
import sys


def main():
    print("Welcome to the flashcard game!")
    print("Enter 0 fro flashcard game, or the number of the chapter you would like to study.")
    userOption = input("Enter option: ")
    flash_card_game(userOption)
        
    


def flash_card_game(userOption):
    flash_card_list = load_flash_card_game(userOption)
    print("Loading Complete!")
    print(len(flash_card_list)-1)
    userinput = ""
    rand=0
    while(userinput != "Quit"):
        # rand = random.randint(0, list_length)

        question = flash_card_list[rand].getEnglish()
        print("(á, é, í, ó, ú, ü, ñ, ¿, ¡)")
        userinput = input("What is: " + question + " ")
        if userinput == "Quit":
            print("Thanks for playing!")
            sys.exit()
        elif userinput == flash_card_list[rand].getSpanish():
            print("Correct! Next question!")
        else:
            print("Nope! It is actually " + flash_card_list[rand].getSpanish())
            flash_card_list.append(flash_card_list[rand])
        print()
        rand = rand + 1

        if (len(flash_card_list) < 1):
            flash_card_list = load_flash_card_game(userOption)

def load_flash_card_game(userOption):
    print("Loading Flash Cards!")
    flash_card_list = []
    if userOption == "2":
        return Chapter_2(flash_card_list)
    elif userOption == "3":
        return Chapter_3(flash_card_list)
    else:
        flash_card_game = Chapter_2(flash_card_list)
        flash_card_game = Chapter_3(flash_card_list)
    
    return flash_card_list

def Chapter_2(flash_card_list):
    # Numbers
    flash_card_list.append(Flash_Card("one", "uno"))
    flash_card_list.append(Flash_Card("two", "dos"))
    flash_card_list.append(Flash_Card("three", "tres"))
    flash_card_list.append(Flash_Card("four", "cuatro"))
    flash_card_list.append(Flash_Card("five", "cinco"))
    flash_card_list.append(Flash_Card("six", "seis"))
    flash_card_list.append(Flash_Card("seven", "siete"))
    flash_card_list.append(Flash_Card("eight", "ocho"))
    flash_card_list.append(Flash_Card("nine", "nueve"))
    flash_card_list.append(Flash_Card("ten", "diez"))
    flash_card_list.append(Flash_Card("eleven", "once"))
    flash_card_list.append(Flash_Card("tweleve", "doce"))
    flash_card_list.append(Flash_Card("thirteen", "trece"))
    flash_card_list.append(Flash_Card("fourteen", "catorce"))
    flash_card_list.append(Flash_Card("fifteen", "quince"))
    flash_card_list.append(Flash_Card("sixteen", "dieciséis"))
    flash_card_list.append(Flash_Card("seventeen", "diecisiete"))
    flash_card_list.append(Flash_Card("eighteen", "dieciocho"))
    flash_card_list.append(Flash_Card("nineteen", "diecinueve"))
    flash_card_list.append(Flash_Card("twenty", "veinte"))
    flash_card_list.append(Flash_Card("twenty four", "veintecuatro"))
    flash_card_list.append(Flash_Card("twenty five", "veinticinco"))
    flash_card_list.append(Flash_Card("thirty", "treinta"))

    # Nouns
    flash_card_list.append(Flash_Card("bathroom", "el baño"))
    flash_card_list.append(Flash_Card("chair", "la silla"))
    flash_card_list.append(Flash_Card("table", "la mesa"))
    flash_card_list.append(Flash_Card("backpack", "la mochila"))
    flash_card_list.append(Flash_Card("notebook", "el cuaderno"))
    flash_card_list.append(Flash_Card("textbook", "libro de texto"))
    flash_card_list.append(Flash_Card("pencil", "el lápiz"))
    flash_card_list.append(Flash_Card("dog", "el perro"))
    flash_card_list.append(Flash_Card("cat", "el gato"))
    flash_card_list.append(Flash_Card("brother", "el hermano"))
    flash_card_list.append(Flash_Card("sister", "la hermana"))
    flash_card_list.append(Flash_Card("father", "el padre"))
    flash_card_list.append(Flash_Card("mother", "la madre"))
    flash_card_list.append(Flash_Card("check", "la cuenta"))
    flash_card_list.append(Flash_Card("clothes", "la ropa"))
    flash_card_list.append(Flash_Card("dress", "el vestido"))
    flash_card_list.append(Flash_Card("shirt", "la camisa"))
    flash_card_list.append(Flash_Card("watch", "el reloj"))
    flash_card_list.append(Flash_Card("store", "la tienda"))

    # Verbs
    flash_card_list.append(Flash_Card("to like", "gustar"))
    flash_card_list.append(Flash_Card("to dance", "bailar"))
    flash_card_list.append(Flash_Card("to read", "leer"))
    flash_card_list.append(Flash_Card("to ride", "andar"))
    flash_card_list.append(Flash_Card("to look for", "buscar"))
    flash_card_list.append(Flash_Card("to walk", "caminar"))
    flash_card_list.append(Flash_Card("to chat", "charlar"))
    flash_card_list.append(Flash_Card("to buy", "comprar"))
    flash_card_list.append(Flash_Card("to listen to", "escuchar"))
    flash_card_list.append(Flash_Card("to study", "estudiar"))
    flash_card_list.append(Flash_Card("to speak", "hablar"))
    flash_card_list.append(Flash_Card("to play (sport)", "jugar"))
    flash_card_list.append(Flash_Card("to take", "tomar"))
    flash_card_list.append(Flash_Card("to work", "trabajar"))
    flash_card_list.append(Flash_Card("to swim", "nadar"))
    flash_card_list.append(Flash_Card("to eat dinner", "cenar"))
    flash_card_list.append(Flash_Card("to eat breakfast", "descansar"))
    flash_card_list.append(Flash_Card("to arrive", "llegar"))
    flash_card_list.append(Flash_Card("to learn", "aprender"))
    flash_card_list.append(Flash_Card("to drink", "beber"))
    flash_card_list.append(Flash_Card("to eat", "comer"))
    flash_card_list.append(Flash_Card("to run", "correr"))
    flash_card_list.append(Flash_Card("to believe", "creer"))
    flash_card_list.append(Flash_Card("to sell", "vender"))
    flash_card_list.append(Flash_Card("to write", "escribir"))
    flash_card_list.append(Flash_Card("to receive", "recibir"))
    flash_card_list.append(Flash_Card("to live", "vivir"))

    #Seasons, dates, and such
    flash_card_list.append(Flash_Card("Summer", "el verano"))
    flash_card_list.append(Flash_Card("Spring", "la primavera"))
    flash_card_list.append(Flash_Card("Winter", "el invierno"))
    flash_card_list.append(Flash_Card("January", "enero"))
    flash_card_list.append(Flash_Card("February", "febrero"))
    flash_card_list.append(Flash_Card("March", "marzo"))
    flash_card_list.append(Flash_Card("April", "abril"))
    flash_card_list.append(Flash_Card("May", "mayo"))
    flash_card_list.append(Flash_Card("June", "junio"))
    flash_card_list.append(Flash_Card("July", "julio"))
    flash_card_list.append(Flash_Card("August", "agosto"))
    flash_card_list.append(Flash_Card("September", "septiembre"))
    flash_card_list.append(Flash_Card("October", "octubre"))
    flash_card_list.append(Flash_Card("November", "noviembre"))
    flash_card_list.append(Flash_Card("December", "diciembre"))
    flash_card_list.append(Flash_Card("Monday", "lunes"))
    flash_card_list.append(Flash_Card("Tuesday", "martes"))
    flash_card_list.append(Flash_Card("Thursday", "jueves"))
    flash_card_list.append(Flash_Card("Friday", "viernes"))
    flash_card_list.append(Flash_Card("Sunday", "domingo"))

    # Colors
    flash_card_list.append(Flash_Card("Green", "verde"))
    flash_card_list.append(Flash_Card("Red", "rojo"))
    flash_card_list.append(Flash_Card("Black", "negro"))
    flash_card_list.append(Flash_Card("White", "blanco"))
    flash_card_list.append(Flash_Card("Yellow", "amarillo"))
    flash_card_list.append(Flash_Card("Orange", "anaranjado"))
    flash_card_list.append(Flash_Card("Purple", "morado"))
    flash_card_list.append(Flash_Card("Blue", "azul"))
    flash_card_list.append(Flash_Card("Grey", "gris"))
    flash_card_list.append(Flash_Card("Pink", "rosado"))
    
    return flash_card_list

def Chapter_3(flash_card_list): 
    #Nouns
    flash_card_list.append(Flash_Card("vacuum cleaner", "la aspiradora"))
    flash_card_list.append(Flash_Card("stove", "la estufa"))
    flash_card_list.append(Flash_Card("oven", "el horno"))
    flash_card_list.append(Flash_Card("microwave", "el microondas"))
    flash_card_list.append(Flash_Card("washing machine", "la lavadora"))
    flash_card_list.append(Flash_Card("dryer", "la secadora"))
    flash_card_list.append(Flash_Card("the floor", "el piso"))
    flash_card_list.append(Flash_Card("the bed", "la cama"))
    flash_card_list.append(Flash_Card("clothes", "la ropa"))
    flash_card_list.append(Flash_Card("always", "siempre"))
    flash_card_list.append(Flash_Card("never", "nunca"))
    flash_card_list.append(Flash_Card("church", "la iglesia"))

    #verbs
    flash_card_list.append(Flash_Card("to tidy/clean", "arreglar"))
    flash_card_list.append(Flash_Card("to wash", "lavar"))
    flash_card_list.append(Flash_Card("to clean", "limpiar"))
    flash_card_list.append(Flash_Card("to mop", "trapear"))
    flash_card_list.append(Flash_Card("to sweep", "barrer"))
    flash_card_list.append(Flash_Card("to fold", "doblar"))
    flash_card_list.append(Flash_Card("to cook", "cocinar"))
    flash_card_list.append(Flash_Card("should/ ought to", "deber"))
    #e-ie verbs
    flash_card_list.append(Flash_Card("to think", "pensar"))
    flash_card_list.append(Flash_Card("to lose", "perder"))
    flash_card_list.append(Flash_Card("to close", "cerrar"))
    flash_card_list.append(Flash_Card("to begin", "empezar"))
    flash_card_list.append(Flash_Card("to understand", "entender"))
    flash_card_list.append(Flash_Card("to hang", "tender"))
    #o-ue verbs
    flash_card_list.append(Flash_Card("to have lunch", "almorzar"))
    flash_card_list.append(Flash_Card("to return", "volver"))
    flash_card_list.append(Flash_Card("to sleep", "dormir"))
    flash_card_list.append(Flash_Card("to show", "mostrar"))
    flash_card_list.append(Flash_Card("to find", "encontrar"))
    flash_card_list.append(Flash_Card("to play", "jugar"))
    flash_card_list.append(Flash_Card("to be able", "poder"))
    flash_card_list.append(Flash_Card("to usually (do something)", "soler"))
    #e-i verbs
    flash_card_list.append(Flash_Card("to ask for/to order", "pedir"))
    flash_card_list.append(Flash_Card("to serve", "servir"))
    flash_card_list.append(Flash_Card("to get/obtain", "conseguir"))
    flash_card_list.append(Flash_Card("to continue/folow", "seguir"))
    #irregular verbs
    flash_card_list.append(Flash_Card("to do/make", "hacer"))
    flash_card_list.append(Flash_Card("to put/place", "poner"))
    flash_card_list.append(Flash_Card("to leave/go out", "salir"))
    flash_card_list.append(Flash_Card("to bring", "traer"))
    flash_card_list.append(Flash_Card("to see/watch", "ver"))

    #Phrases
    flash_card_list.append(Flash_Card("to take out the trash", "sacar la basura"))
    flash_card_list.append(Flash_Card("to iron the clothes", "planchar la ropa"))
    flash_card_list.append(Flash_Card("to make the bed", "hacer la cama"))
    flash_card_list.append(Flash_Card("to sweep the floor", "barrer el piso"))
    flash_card_list.append(Flash_Card("to vaccuum the floor", "pasar la aspiradora"))
    flash_card_list.append(Flash_Card("to fold the clothes", "doblar la ropa"))
    flash_card_list.append(Flash_Card("to hang the clothes", "tender la ropa"))
    flash_card_list.append(Flash_Card("to wash the dishes", "lavar los platos"))
    flash_card_list.append(Flash_Card("to mow the lawn", "cortar el césped"))

    #Expressions
    flash_card_list.append(Flash_Card("to be hot", "tener calor"))
    flash_card_list.append(Flash_Card("to be careful", "tener cuidado"))
    flash_card_list.append(Flash_Card("to be successfull", "tener éxito"))
    flash_card_list.append(Flash_Card("to be cold", "tener frío"))
    flash_card_list.append(Flash_Card("to feel like", "tener ganas de"))
    flash_card_list.append(Flash_Card("to be hungry", "tener hambre"))
    flash_card_list.append(Flash_Card("to be scared", "tener miedo"))
    flash_card_list.append(Flash_Card("to be in a hurry", "tener prisa"))
    flash_card_list.append(Flash_Card("to be right", "tener razón"))
    flash_card_list.append(Flash_Card("to be sleepy", "tener sueño"))
    flash_card_list.append(Flash_Card("once a week", "una vez a la semana"))
    flash_card_list.append(Flash_Card("once a month", "una vez al mes"))


    return flash_card_list


def conjugation(flash_card_list):

    return flash_card_list


class Flash_Card:
    
    def __init__(self, english, spanish):
        self.english = english
        self.spanish = spanish
    

    def getEnglish(self):
        return self.english


    def getSpanish(self):
        return self.spanish


class conjugation_card:

    def __init__(self, regular):
        self.regular = regular
        
    def __init__(self, regular, I, you, he, we, yall, they):
        self.regular = regular
        self.I = I
        self.you = you
        self.he = he
        self.we = we
        self.yall = yall
        self.they = they

    def getRegular(self):
        return self.regular
    
    def getI(self):
        return self.I

    def getyou(self):
        return self.you    

    def gethe(self):
        return self.he

    def getwe(self):
        return self.we 

    def getyall(self):
        return self.yall

    def getthey(self):
        return self.they
        
if __name__ == "__main__":
    main()
