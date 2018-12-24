class Calculator:                    #a=int(input("Enter First number:"))
                                    #b=int(input("Enter another number:"))
    def add(self):
        a=int(input("Enter First number:"))
        b=int(input("Enter another number:"))
        addition=a+b
        print(addition)
    def sub(self):
        a=int(input("Enter First number:"))
        b=int(input("Enter another number:"))
        substraction=a-b

        print(substraction)
    def mul(self):
        a=int(input("Enter First number:"))
        b=int(input("Enter another number:"))
        multiplication=a*b
        print(multiplication)


def main():
    obj=Calculator()
    obj.add()
    obj.sub()
    obj.mul()
    
   
if __name__=="__main__":main()