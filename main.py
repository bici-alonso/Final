from menu import Menu



def main():
    """
    Función principal del programa.

    Crea una instancia de la clase `Menu` y ejecuta el método `menu()`,
    que lanza la interfaz de interacción del usuario con el sistema INCUCAI.

    Este método actúa como punto de entrada del programa.
    """
    menu = Menu()
    menu.menu()

if __name__ == "__main__":
    main()
    
