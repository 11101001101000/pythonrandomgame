import random
ToBeOrNotToBe = 0
clicks = 0
cleared = False
exit = 0
print ("Press ENTER key. The probability is 0.0066666666666666666666666666666666666666666666666666666666666666...%.")
var1 = input ()
if var1 == 'hack':
    while cleared == False:
        clicks = clicks + 1
        ToBeOrNotToBe = random.randrange (1,15000)
        if ToBeOrNotToBe == 1:
            cleared = True
        else:
            cleared = False
            print ("Your computer is not lucky this time :(\ntried " + str(clicks) + ' times')
while cleared == False:
    input ()
    clicks = clicks + 1
    ToBeOrNotToBe = random.randrange (1,15000)
    if ToBeOrNotToBe == 1:
        cleared = True
    else:
        cleared = False
        print ("You're not lucky this  time :(\nYou've pressed " + str(clicks) + ' times')
if cleared == True:
    print ('This is a trash game.' + ' You pressed Enter key ' + str(clicks) + ' times')
    while exit == 0:
        var = input ("type 'exit' and press ENTER to exit: ")
        if var == "exit":
            exit = 1
print ('This is a trash game.' + ' You pressed Enter key ' + str(clicks) + ' times')
