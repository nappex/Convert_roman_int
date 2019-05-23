import itertools
import dict_right_input


list_of_letter = ["I", "V", "X", "L", "C", "D", "M"]
WRONG_INPUT = ["IXII", "VIIII", "MMQCDAV", "MCMROIX", "MIM", "CMCMIII"]

for i in range(2, 8, 1):
    # list = list(itertools.permutations(list_of_letter, i))

    for tuple in list(itertools.permutations(list_of_letter, i)):
        WRONG_INPUT.append("".join(tuple))

for value in dict_right_input.right_input.values():
    if value in WRONG_INPUT:
        WRONG_INPUT.remove(value)

with open("list_wrong_input.py", mode="w", encoding="utf-8") as file:
    file.write("wrong_input = [\n")

    for roman in WRONG_INPUT:
        file.write("\t\t\t\t" + "\"" + roman + "\"," + "\n")

    file.write("\t\t\t]\n")
