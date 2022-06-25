from pip import main


a =7
def printjoke(str):
    print(f"this function is a joke {str}")

if __name__ == "__main__":
 print(a)

'''if __name__ == "__main__": means when someone calls this file as a module then The module exclude all things under if __name__ == "__main__":

If we dont use if __name__ == "__main__": then when we call this then it will also print print(a).
'''