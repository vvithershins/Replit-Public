message = """"""#add message here

capitalize_next = True

for char in message:
    if char == ' ':
        print(char, end='')
    elif capitalize_next:
        print(char.upper(), end='')
        capitalize_next = False
    else:
        print(char.lower(), end='')
        capitalize_next = True
