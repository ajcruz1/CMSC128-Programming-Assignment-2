def getHammingDistance(str1, str2):
    hammingDistance = 0

    if len(str1) == len(str2):
        for index in range(len(str1)):
            if ord(str1[index]) != ord(str2[index]):
                hammingDistance += 1
        return hammingDistance
    else:
        return None

def countSubstrPattern(str1, str2):
    count = 0
    index = 0

    if len(str2) < len(str1):
        while index < len(str1):
            if str1.find(str2, index, index + len(str2)) != -1:
                count += 1
            index += 1
        return count
    else :
        return None

def isValidString(str1, str2):
    check = 0

    for index in range(len(str1)):
        ch = str1[index]
        for index1 in range(len(str2)):
            if ord(str1[index]) == ord(str2[index1]):
                check += 1
    if check == len(str1):
        return True
    else :
        return False

def getSkew(str1,n):
    index = 0
    g = 0
    c = 0

    while index < n:
        if ord(str1[index]) == ord('G'):
            g += 1
        if ord(str1[index]) == ord('C'):
            c += 1
        index += 1

    return g-c

def getMaxSkew(str1,n):
    max = getSkew(str1,n)

    if n > 0:
        for index in range(n):
            if max < getSkew(str1,n-index):
                max = getSkew(str1,n-index)
    return max

def getMinSkew(str1,n):
    min = getSkew(str1,n)

    if n > 0:
        for index in range(n):
            if min > getSkew(str1,n-index):
                min = getSkew(str1,n-index)
    return min

def printMenu():
    print "==========================="
    print "[3] Check String"
    print "[1] Get Hamming Distance"
    print "[2] Count Substring Pattern"
    print "[4] Get Skew"
    print "[5] Get Maximum Skew"
    print "[6] Get Minimum Skew"
    print "[7] Exit"
    print "==========================="

    return input("CHOICE: ")


#MAIN FUNCTION
choice = 0
n = 0
while choice != 7:
    choice = printMenu()
    if choice == 1:
        str1 = raw_input("First string: ")
        str2 = raw_input("Second string: ")
        ans = getHammingDistance(str1,str2)
        if ans != None:
            print "\n\nHamming Distance: %d\n\n" % ans
        else :
            print "\n\nString lengths do not MATCH!!\n\n"
    elif choice == 2:
        str1 = raw_input("String: ")
        str2 = raw_input("Substring: ")
        ans = countSubstrPattern(str1,str2)
        if ans != None:
            print "\n\nSubstrings: %d\n\n" % ans
        else :
            print "\n\nSubstring's length is larger than original String!\n\n"
    elif choice == 3:
        str1 = raw_input("String: ")
        str2 = raw_input("Library: ")
        ans = isValidString(str1, str2)
        if ans == True:
            print "VALID"
        else:
            print "INVALID"
    elif choice == 4:
        str1 = raw_input("String: ")
        while n <= 0 or n > len(str1):
            n = int(raw_input("Starting index: "))
            if n <= 0:
                print "Index starts at 1!"
            if n > len(str1):
                print "Index is greater than the length of the string!"
        ans = getSkew(str1,n)
        n = 0
        print "\n\nSkew: %d\n\n" % ans
    elif choice == 5:
        str1 = raw_input("String: ")
        while n <= 0 or n > len(str1):
            n = int(raw_input("Starting index: "))
            if n <= 0:
                print "Index starts at 1!"
            if n > len(str1):
                print "Index is greater than the length of the string!"
        ans = getMaxSkew(str1,n)
        n = 0
        print "\n\nSkew: %d\n\n" % ans
    elif choice == 6:
        str1 = raw_input("String: ")
        while n <= 0 or n > len(str1):
            n = int(raw_input("Starting index: "))
            if n <= 0:
                print "Index starts at 1!"
            if n > len(str1):
                print "Index is greater than the length of the string!"
        ans = getMinSkew(str1,n)
        n = 0
        print "\n\nSkew: %d\n\n" % ans
