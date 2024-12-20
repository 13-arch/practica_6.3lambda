#logvinov
#enter two numbers to get their 
# greatest common divisor
#==============================


#function
def gcd(a:int, b:int) -> int:
    if a == 0 or b == 0: 
         return max(a, b)
    else:
        if a > b:
            return gcd(a - b, b)
        else:
            return gcd(a, b - a)

# Main function
def main():
    inp = input('Введите два числа через пробел ') # ввод с клавы
    inp_is = inp.split()
    inp_1 = int(inp_is[0]) # преобразование в int
    inp_2 = int(inp_is[1])
    Nod=gcd(inp_1,inp_2)
    print(f'Нод чисел {inp_1} и {inp_2}: {gcd(inp_1, inp_2)}')

if __name__=='__main__':
    main()