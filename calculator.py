import re

pElement = re.compile(r'\([^()]+\)|\d+|[\-+/*^]')
OPERATORS = '^*/+-'

def getResult(operation):
    # Do the simple calculation : number operator number
    n1, operator, n2 = operation
    n1, n2 = float(n1), float(n2)
    if operator == '+':
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2
    elif operator == '*':
        result = n1 * n2
    elif operator == '^':
        result = n1 ** n2
    elif operator == '/':
        result = n1 / n2
    return result

def calculation(elements):
    # Do the whole operation (take account of the operator precedance)
    backup = elements[:]
    for i in range(5):
        if OPERATORS[i] in elements:
            for j in range(len(elements)):
                bloc = elements[j:j+3]
                if len(bloc) < 3:
                    break
                if bloc[1] == OPERATORS[i]:
                    result = getResult(bloc)
                    backup[j:j+3] = [str(result)]
            elements = backup[:]
    return float(elements.pop())

def remove_parenthesis(elements):
    # Replace parenthesis by its result
    backup = elements[:]
    for index, item in enumerate(elements):
        if item.startswith('(') and item.endswith(')'):
            bloc = pElement.findall(item.strip('( )'))
            result = calculation(bloc)
            backup[index] = result
    return backup

def main():
    while True:
        userInput = input('Input : ')
        if not userInput:
            break
        elements = pElement.findall(userInput)
        try :
            result = calculation(remove_parenthesis(elements))
        except :
            continue
        print('Output :', result)

if __name__ == '__main__':
    main()
