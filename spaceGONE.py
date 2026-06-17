input_str = "sdf      sdfs sdfs" 
mod_str = ""
space = " "

for char in input_str :
    char_upper = char.upper()
    if char_upper in space:
         mod_str += "" 
    else:
         mod_str += char_upper
print(mod_str)