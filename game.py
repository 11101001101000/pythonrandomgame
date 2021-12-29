import random
ToBeOrNotToBe = 0
clicks = 0
cleared = False
exit = 0
print ("엔터 키를 눌러 봐. 확률은 0.0066666666666666666666666666666666666666666666666666666666666666...%야.")
var1 = input ()
if var1 == 'hack':
    while cleared == False:
        clicks = clicks + 1
        ToBeOrNotToBe = random.randrange (1,15000)
        if ToBeOrNotToBe == 1:
            cleared = True
        else:
            cleared = False
            print ("운 수준\n클릭 " + str(clicks) + '번')
while cleared == False:
    input ()
    clicks = clicks + 1
    ToBeOrNotToBe = random.randrange (1,15000)
    if ToBeOrNotToBe == 1:
        cleared = True
    else:
        cleared = False
        print ("운 수준\n클릭 " + str(clicks) + '번')
if cleared == True:
    print ('운빨 망겜' + ' 클릭 ' + str(clicks) + '번')
    while exit == 0:
        var = input ("type exit and press enter to exit: ")
        if var == "exit":
            exit = 1
print ('운빨 망겜' + ' 클릭 ' + str(clicks) + '번')
