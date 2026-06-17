input_str = input("input: ")
mod_str = ""
number = "1234567890"

for char in input_str:
    char_lower = char.lower()
    if char_lower in number:
        mod_str += "#"
    else:
        mod_str += char_lower 
print(mod_str)
