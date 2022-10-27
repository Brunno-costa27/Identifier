from Identifier import Identifier

if __name__ == '__main__':
    id = input("id: ")
    if(len(id) == 0):
        print("Error: Digite um valor")
    else:
        if(Identifier.validateIdentifier(id)):
            print("Valido")
        else:
            print("Invalido")
