#*************************************************************************
# author: Lakshmi Narasimha vedantam (Dundi)
#
#************************************************************************

# import the necessary packages
import radius,sys
fullCmdArguments = sys.argv
argumentList = fullCmdArguments[1:]

# construct the arguments
# first_arg : username 
# second_arg : password 
# thrid_arg : secret
# fourth_arg : host

r = radius.Radius('+argumentList[2]+', host='+argumentList[3]+', port=1812)

if r.authenticate('+argumentList[0]+','+argumentList[1]+'):
        print("ok");
else:
        print("wrong user name and password");
