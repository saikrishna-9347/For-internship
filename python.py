pin = "4536"
is_digit = pin.isdigit()
is_4_digit = (len(pin)) == 4 
is_valid = is_digit and is_4_digit 
print(is_valid)

pin = "456a"
is_digit = pin.isdigit()
is_4_digit = (len(pin)) == 4 
is_valid = is_digit and is_4_digit 
print(is_valid)

pin = "979790"
is_digit = pin.isdigit()
is_6_digit = (len(pin)) == 6 
is_valid = is_digit and is_6_digit
print(is_valid)

mobile = " 9876543210 "
mobile = mobile.strip()
print(mobile)

name = "...ravi...."
name = name.strip(".")
print(name)

name = " , ... ,. ravi  ,. ,, ... ,,"
name = name.strip(" ,. ")
print(name)

sentence = "monht is a part of the year and monht is mainly part"
sentence = sentence.replace("monht","month")
print(sentence)

sentence = "teh cat and teh dog"
sentence = sentence.replace("teh","the")
print(sentence)

gmail_id = "saikrishnaelc999@gmail.com"
is_gmail = gmail_id.endswith("@gmail.com")
print(is_gmail)

url = "https://onthegomodel.com"
is_secure_url = url.startswith("https://")
print(is_secure_url)

name = "sikrishna"
print(name.upper())

name = "SAIKRISHNA"
print(name.lower())