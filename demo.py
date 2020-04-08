

a = "test"
nr = 1

print("  {str(nr+1)} {a}")
print( f"  {str(nr+1)} {a}" )
print( "  " + str(nr+1) + " " + a )

eine_liste = input("list:").split(",")

i = int(input(":"))
length = len(eine_liste)
print(length)
if i >= 0 and i <= length:
    print(eine_liste [i])