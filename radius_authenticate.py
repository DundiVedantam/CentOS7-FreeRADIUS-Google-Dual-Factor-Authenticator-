import radius,sys
fullCmdArguments = sys.argv
argumentList = fullCmdArguments[1:]

r = radius.Radius('+argumentList[2]+', host='+argumentList[3]+', port=1812)

if r.authenticate('+argumentList[0]+','+argumentList[1]+'):
        print("ok");
else:
        print("wrong user name and password");
