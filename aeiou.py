# รับสตริงจากผู้ใช้
input_string = input("ใส่ข้อความ: ")
# กำหนดให้ตัวแปรผลลัพธ์เป็นสตริงว่าง
modified_string = ""
# กำหนดชุดตัวอักษรสระ (a, e, i, o, u ทั้งพิมพ์เล็กและพิมพ์ใหญ่)
vowels = "aeiouAEIOU"
# ใช้ลูป for วนผ่านทุกตัวอักษรใน input_string
for char in input_string:
    # แปลงตัวอักษรเป็นตัวพิมพ์ใหญ่
    upper_char = char.upper()
    if upper_char in vowels:
        modified_string += "*"
    else:
        modified_string += upper_char

# แสดงผลลัพธ์ของสตริงที่ถูกปรับแต่ง
print("สตริงที่ถูกปรับแต่ง:", modified_string)
