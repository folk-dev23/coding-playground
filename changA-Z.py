input_str = "abc123!"
mod_str = ""
Consonants = "abcdefghijklmnopqrstuvwxyz"

for char in input_str:
    if char in Consonants:
        mod_str += "_"
    else:
        mod_str += char
print(mod_str)