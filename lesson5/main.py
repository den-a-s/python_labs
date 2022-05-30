from menu import complete_the_task, show_menu
from people import DataPeople

def main():
    show_menu()
    dataPeople = DataPeople()
    dataPeople.load("peoples.txt")
    complete_the_task(dataPeople)

if __name__ == "__main__":
    main()