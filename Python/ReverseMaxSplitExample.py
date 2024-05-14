text = "abc.def.ghi"

first = text.split(".")

backwards = first[2],first[1],first[0]

joinback = ".".join(backwards)

print(joinback)

splitback = joinback.split(".",1)
print(splitback)

reversedjoin = " ".join(splitback)
print(reversedjoin)
splitreversedjoin = reversedjoin.split(" ")
forward = splitreversedjoin[1],splitreversedjoin[0]
print(forward)
stuff = forward[0].split(".")
newforward = f"{stuff[1]}.{stuff[0]}"
print(newforward,forward[1])
