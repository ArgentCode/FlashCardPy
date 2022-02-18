import random
import sys


def main():
    print("Welcome to the flashcard game!")
    print("Enter 0 fro flashcard game, or 1 for the conjugation game")
    userOption = input("Enter option: ")
    if userOption == "0":
        flash_card_game()


def flash_card_game():
    flash_card_list = load_flash_card_game()
    print("Complete!")
    list_length = len(flash_card_list)-1
    print(list_length)
    userinput = ""
    while(userinput != "Quit"):
        rand = random.randint(0, list_length)
        question = flash_card_list[rand].getEnglish()
        userinput = input("What is " + question + " in spanish?")
        if userinput == "Quit":
            print("Thanks for playing!")
            sys.exit()
        elif userinput == flash_card_list[rand].getSpanish():
            print("Correct! Next question!")
        else:
            print("Nope! It is actually " + flash_card_list[rand].getSpanish())
        print()

def load_flash_card_game():
    print("Loading Flash Cards!")
    flash_card_list = []
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
    flash_card_list.append(Flash_Card("twenty", "veinte"))
    flash_card_list.append(Flash_Card("thirty", "treinta"))
    return flash_card_list


class Flash_Card:
    
    def __init__(self, english, spanish):
        self.english = english
        self.spanish = spanish
    

    def getEnglish(self):
        return self.english


    def getSpanish(self):
        return self.spanish


if __name__ == "__main__":
    main()
