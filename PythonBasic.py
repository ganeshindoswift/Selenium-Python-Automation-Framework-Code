str="y8u9r2lly30lov123thisi34llljhlalfd90"
for i in str:

    if i.isalpha():

        print(i, end="")
print("\n")

# fin only digit then

str1= "y8u9r2lly30lov123thisi34llljhlalfd90"

for i in str1:
    if i.isdigit():
        print(i, end="")

# string lower Letters
Cstr="HI THIS IS PYTHON STRING OR CHARACTER CONVERSTION"
Small_letters=Cstr.lower()
print("\n")
print(Small_letters)

# string Upper Letters
print("########## Upper letters Conversions###########")
Cap_letters=Cstr.upper()
print("\n ", Cap_letters)

###########################
f" this is very example"
mix_letters="Hi This is yours Book How do u find This one"
Lower=mix_letters.islower()
print(Lower)

################String break up less than 3 caracters...############
def stringsep(strparam, size=3):
    for ch in mix_letters.split():
        if (ch<size):
