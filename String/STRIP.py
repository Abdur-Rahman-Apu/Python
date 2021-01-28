string="   Hello"

print(f"String after lstrip:{string}")
print(string.lstrip())

string="Hello   "
print(f"String after rstrip:{string}","Lets see")
print(string.rstrip(),"After apply")


string="    hello    "
print(f"String after strip,{string}:",string.strip())

print("Isspace function:")
print(f"{string} isspace()?={string.isspace()}")
empty=" "
print(f"empty has space?{empty.isspace()}")
