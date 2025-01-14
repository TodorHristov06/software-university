KID = 14
TEEN = 18
YOUNG_ADULT = 21
ADULT = 21


age = int(input())

if ( age <= KID ):
    print("drink toddy")
elif ( age <= TEEN ):
    print("drink coke")
elif ( age <= YOUNG_ADULT ):
    print("drink beer")
else:
    print("drink whisky")