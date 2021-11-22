from Tests.TestAll import runalltests
from UI.Console import run_menu
from UI.Console2 import run_menu_2


def main():
    runalltests()
    optiune = input("Old menu or New menu? (old/new): ")
    while optiune != "old" and optiune != "new":
        print("Optiune invalida! Reincercati cu old/new.")
        optiune = input("Old menu or New menu? (old/new): ")
    if optiune == "old":
        run_menu([])
    else:
        run_menu_2([])
    run_menu([])


main()
