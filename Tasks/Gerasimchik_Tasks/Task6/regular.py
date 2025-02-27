import re
import arith


def calc(string):
    number = re.compile(r'-?(\d+(\.\d*)?|\.\d+)')
    math_operand = re.compile(r'\d[-+*/]')
    first = number.search(string).group()
    if math_operand.search(string):
        symbol = math_operand.search(string).group()[1:]
        symbol_pos = math_operand.search(string).end()
        second = number.search(string[symbol_pos:]).group()
        if symbol == '*' or symbol == '/':
            string = string.replace(first + symbol + second, simple_math(first, symbol, second))
            return calc(string)
        else:
            second_end_position = number.search(string[symbol_pos:]).end() + symbol_pos
            if math_operand.search(string[second_end_position - 1:]):
                next_symbol = math_operand.search(string[second_end_position - 1:]).group()[1:]
                if next_symbol == '/' or next_symbol == '*':
                    third = number.search(string[second_end_position+1:]).group()
                    string = string.replace(second + next_symbol + third, simple_math(second, next_symbol, third))
                    return calc(string)
                else:
                    string = string.replace(first + symbol + second, simple_math(first, symbol, second))
                    return calc(string)
            else:
                second = number.search(string[symbol_pos:]).group()
                string = string.replace(first + symbol + second, simple_math(first, symbol, second))
                return string

    else:
        return string


def simple_math(a, b, c):
    if b == '+':
        return str(arith.add(a, c))
    elif b == '-':
        return str(arith.sub(a, c))
    elif b == '*':
        return str(arith.mult(a, c))
    else:
        if c == '0':
            print('В процессе вычислений возникло деление на 0')
            exit(0)
        else:
            return str(arith.div(a, c))


def curculator(string):
    if re.search(r'\(([^()]+)\)', string):
        a = calc(re.search(r'\(([^()]+)\)', string).group(1))
        string = string.replace(re.search(r'\(([^()]+)\)', string).group(), a)
        return curculator(string)
    elif re.search(r'\d[-+*/]', string):
        return calc(string)
    else:
        return string


s = '((((12.5*2+(-4-3)*2)*(12+(2-1))+1)+1-1)/(9-9))'
print(curculator(s))
