#CMPT 120 - Lab #6
#Sydnee Ramirez
#25-10-2018

def showIntro():
    print("Welocme to the Arithmetic Engline!")
    print("==================================\n")
    print("Valid commands are 'add", 'mult', 'sub', and 'quit'.\n")

def showOutro():
    print("\nThank you for using the Arithmetic Engline...")
    print('\nPlease come back again soon!")

def doLoop():
    while True:
          cmd = input("What computation do you want to perform? ")
        num1 = int(input("Enter the first  number: "))
        num2 = int(input("Enter the second number: "))

        if cmd == "add":
            result = num1 + num2
        elif cmd == "sub":
            result = num1 – num2
        elif cmd == "mult":
            result = num1 * num2
        elif cmd == "div":
            result = num1 // num2
        elif cmd == "quit":
            break
        print("The result is " + str(result) + ".\n")


def main():
    showIntro()
    doLoop()
    showOutro()
main()
