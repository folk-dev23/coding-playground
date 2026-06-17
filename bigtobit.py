input_str ="ImAFLokKunA"
mod_str = ""

for char in input_str:
    if char.upper() in input_str:
        mod_str += char.lower()
    else:
        mod_str += char.upper()
print(mod_str)