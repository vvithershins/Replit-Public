def replinebreak(word):
    count = -1
    max_spacelength = 1
    current_spacelength = 1
    space = " "  # Define space variable here
    max_space_start_index = 0

    for index, letter in enumerate(word):
        count += 1
        if letter == " ":
            if word[count + 1] == " ":
                current_spacelength += 1
            else:
                if current_spacelength > max_spacelength:
                    max_spacelength = current_spacelength
                    max_space_start_index = index - max_spacelength + 1
                current_spacelength = 1

    space *= max_spacelength  # Create the string of spaces here

    word = word[:max_space_start_index] + word[max_space_start_index:].replace(space, "\n", 1)
    print(word)

replinebreak("""abc                                                                       def                                                                                    ghi""")


def newversion(thresh,word):
    start = -1
    lastcharisspace = False

    while True:
        replaced = False  # Flag to track if any replacements were made in this iteration
        pos = -1
        end = -1
        for index, char in enumerate(word):
            if not lastcharisspace:
                if char == " ":
                    lastcharisspace = True
                    pos = index
                    end = index
                else:
                    lastcharisspace = False
            else:
                if char == " ":
                    end = index
                else:
                    if ((end - pos) +1) > int(thresh):  # Check if the difference between pos and end is greater than 1
                        replaced_text = "\n" + word[end:].lstrip()  # Remove leading spaces after newline insertion
                        word = word[:pos] + replaced_text
                        replaced = True
                        break  # Exit the loop once a replacement is made
                    else:
                        lastcharisspace = False

        if not replaced:  # If no replacements were made in this iteration, exit the loop
            break

    print(word)
print("newversion()example1")
newversion(1,"abc                                                                                        def  geh")
print()
print("newversion()example 2")
newversion(2,"abc                                                                                        def  geh"))

"""Outputs:
newversion()example1
abc
def
geh

newversion()example 2
abc
def  geh"""
