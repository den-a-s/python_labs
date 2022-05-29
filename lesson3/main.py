from os import system
import os
from menu import getting_task, show_menu

def main():
    show_menu()
    task = getting_task()
    task()

if __name__ == "__main__":
    main()
    exit()
