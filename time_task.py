import time


def kbrdinpt(hms):
    k = 1
    intrvl = 0
    while k == 1:
        try:
            intrvl = int(input(f"Please type how many {hms} - 0 for None - "))
            k = 0
        except:
            print("Please type digits. Please")
    return intrvl


p = 1
print("Time Module Imported")
print("Please, set the period of time")
hrs = kbrdinpt("hours")
mnts = kbrdinpt("minutes")
scnds = kbrdinpt("seconds")

print("Start of the Timer")

while True:
    print(f"Time left: {hrs}:{mnts}:{scnds}")
    time.sleep(1)
    if scnds>0:
        scnds-=1
    else:
        if mnts>0:
            mnts-=1
            scnds=59
        else:
            if hrs>0:
                hrs-=1
                mnts=59
                scnds=59
            else:
                print("End of the Timer")
                break


