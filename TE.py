#try and except
UserAge = input ('Enter your age:')
try :
    val = int(UserAge)
except:
    val = -1
    print ('Please Enter a whole number')
if val > 0:
    print ('Loading')
else:
    print ('Please Enter a whole number')
    UserAge1 = input ('Enter your age:')
    try :
    val = int(UserAge)
    except:
    val = -1

    if val > 0:
        print ('Thank You')
    else:
        print ('Please Be Serious')
