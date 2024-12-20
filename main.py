# Logvinov
#
#======================


# import all nessesary libs and modules
import Euclid as E
import Pascal as P
import notations as n


# main function
def main():
    user_chiose = (input("Choose E if you want to use Euclid: "))
    if user_chiose.lower() =='e':
        ecl= (input("Введите два числа через пробел: "))
        inp_is =ecl.split()
        inp_1 = int(inp_is[0]) # преобразование в int
        inp_2 = int(inp_is[1])
        print('nod chisel raven:', E.gcd(inp_1,inp_2))
    if user_chiose.lower()=='p':
        pass
    

if __name__=='__main__':
    main()