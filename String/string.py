string="I was a good person"

print("Replace function:")
old='was'
new='am'
Replace=string.replace(old,new)
print(f"After replace:{Replace}")

print("\nFind function:")
Find=string.find('person')
print(f"After find index no is:{Find}")

print("\nCenter method:")
string1="Hello"
print(string1.center(len(string1)+8,'*'))

print("\nUpper function,isupper() function:")
Upper=string.upper()
print("After upper method:",Upper," and isupper()=",Upper.isupper())

print("\nLower function and islower() function:")
Lower=string.lower()
print("After lower function:",Lower," and islower()=",Lower.islower())

print("\nTitle function and istitle() function:")
Title=string.title()
print("After Title function:",Title," and istitle():",Title.istitle())

print("\nstartswith function:")
Startswith="I"
print(f"Startswith {Startswith}?:{string.startswith(Startswith)}")

print("\nendswith():")
Endswith="person"
print(f"Endswith {Endswith}?:{string.endswith(Endswith)}")

print("\nisalpha()")
name="Hello i am a writer"
print(f"{name} isalpha()?={name.isalpha()}")

print("\nisnumeric()")
string2="Abc1"
print(f"{string2} is numeric?={string2.isnumeric()}")

print("\nisalnumeric()")
print(f"{string2} is alnumeric?={string2.isalnum()} and {string} is alnum?{string.isalnum()}")

