
def calculate(self, s : str) -> int:
    i = 0
    integer = []
    operators = []
    num = 0
    has_num = False
    priority = {"+" : 1, "-" : 1, "/" : 2, "*" : 2}

    def calc(op):
        last = integer.pop()
        first = integer.pop()
        if op == "*":
            return first * last
        if op == "/":
            return first / last
        if op == "+":
            return first + last
        if op == "-":
            return first - last

    while i < len(s):
        if s[i] == ' ':
            i += 1
            continue
        
        if s[i].isdigit():
            has_num = True
            num = int(s[i]) + num*10
            i+=1
            continue
        if not s[i].isdigit() and has_num:
            integer.append(num)
            num = 0 
            has_num = False
            
        if s[i] == "(":
            operators.append(s[i])
            i += 1
            continue
            
        if s[i] == ")":
            while operators[-1] != "(":
                op = operators.pop()
                integer.append(calc(op))

            operators.pop()
            i+=1
            continue
            

        if not operators:
            operators.append(s[i])
            i += 1
        else:
            while operators and operators[-1] != "(" and priority[operators[-1]] >= priority[s[i]]:

                op = operators.pop()
                integer.append(calc(op))

            operators.append(s[i])
            i+=1
        
    if has_num:
        integer.append(num)
    while operators:
        op = operators.pop()
        integer.append(calc(op))
    return integer[-1]


   

    