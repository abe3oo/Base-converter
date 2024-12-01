import sys
#Color and text style
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#List converter
def convert_list_to_string(lst1):
    str1 = ""
    for i in lst1:
        str1 = str1 + str(i)
    return str1

#==== 1-16 to 10
def number_to_10(a, number):
    list1 = []
    result = []
    for i in range(len(number)):
        n1 = a ** i
        list1.append(n1)
    list1.reverse()
    #====== 16 to 10
    if a > 10:
        for i in range(len(number)-1, -1,-1):
            if number[i] == "A":
                xx = 10 * list1[i]
            elif number[i] == "B":
                xx = 11 * list1[i]
            elif number[i] == "C":
                xx = 12 * list1[i]
            elif number[i] == "D":
                xx = 13 * list1[i]
            elif number[i] == "E":
                xx = 14 * list1[i]
            elif number[i] == "F":
                xx = 15 * list1[i]
            else:
                xx = int(number[i]) * list1[i]
            result.append(xx)
        return str(sum(result))
    else:
        #=============1-9 to 10
        for i in range(len(number)-1, -1,-1):
            xx = int(number[i]) * list1[i]
            result.append(xx)
        return str(sum(result))

#==== 10 to 1-16
def ten_to_enything(a,number):
    result = []
    while True:
        if a > 10:
            x1 = number % a
            x2 = number // a
            if x2 < a:
                if x1 == 10:
                    result.append("A")
                elif x1 == 11:
                    result.append("B")
                elif x1 == 12:
                    result.append("C")
                elif x1 == 13:
                    result.append("D")
                elif x1 == 14:
                    result.append("E")
                elif x1 == 15:
                    result.append("F")
                else:
                    result.append(x1)
                result.append(x2)
                result.reverse()
                r = convert_list_to_string(result)
                return r
            else:
                if x1 == 10:
                    result.append("A")
                elif x1 == 11:
                    result.append("B")
                elif x1 == 12:
                    result.append("C")
                elif x1 == 13:
                    result.append("D")
                elif x1 == 14:
                    result.append("E")
                elif x1 == 15:
                    result.append("F")
                else:
                    result.append(x1)
                number = x2
        else:
            x1 = number % a
            x2 = number // a
            if x2 < a:
                result.append(x1)
                result.append(x2)
                result.reverse()
                r = convert_list_to_string(result)
                return r
            else:
                result.append(x1)
                number = x2

#==== main
while True:
    print(f"_-_-_{color.BOLD + 'Base converter' + color.END}_-_-_( to close the app please type {color.BOLD + 'exit' + color.END} )")
    number = input("enter your number: ")
    if number == "exit":
        sys.exit()
    try:
        fm = int(input("From base: "))
        sm = int(input("to base: "))
    except:
        print(color.BOLD+ "!!! Please enter the base correctly !!!"+ color.END)
    try:
        x = number_to_10(fm,number)
        y = ten_to_enything(sm, int(x))
        print(f"Result ==> {color.BOLD + y + color.END}")
    except:
        print("!!! The input is invalid !!!")