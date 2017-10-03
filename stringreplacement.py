
def findSubstr(textToSearch,subText):


    retList = []
    # Validation of strings only
    if (type(textToSearch) != str or type(subText) != str):
        print "Please provide strings input only"
        # can do a custom exception here
        raise Exception
    

    lenText = len(textToSearch)
    lenSub = len(subText)

    # Validations
    if lenText<lenSub  or lenText ==0 or lenSub == 0:
        return retList

    # loop through searchText and match the strings with subtexts 
    # for subtexts we will use the differnt counter a little smartly 
    # i.e. in co-relation with first index so that we can do this in single
    # loop

    
    subIndex =0
    match = False
    for textIndex in range(lenText):
        # we will increase the subIndex each time we match the subs char with
        # respective text char.
        if match == False:
            if textToSearch[textIndex].lower() == subText[subIndex].lower():
                # Matched the first char of sub in the text -> put match to true and increase subindex
                subIndex +=1
                match =True
                 
        else:
            if textToSearch[textIndex].lower() == subText[subIndex].lower():
                # matched second and more keep increasing the subIndex till we match the complete SubText
                subIndex +=1
            else:
                # OOPS the matching failed in between # escape out #reset match and subindex.
                match = False
                subIndex = 0
                continue
        
        # the match will be done when we have completed the complete length of sub in the text 
        if subIndex == lenSub:
            # add the starting index to return list
            # Adding +2 as
            # 1. Python uses index from 0 expected result is from 1, so + 1
            # 2. The lenSub is already at increased length with respect to index 0 , so +1
            # total +2 to counter 
            retList.append(textIndex-lenSub+2)

            # reset subindex and match
            subIndex =0
            match = False

    return retList
        


str1 = "Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!"

### Test Cases ####
print findSubstr(str1, "Peter")
print findSubstr(str1, "Pi")
print findSubstr(str1, "P")
print findSubstr(str1, "Peterz")
print findSubstr(str1, "")
print findSubstr("", "P")
print findSubstr(12, "123w12P")
print findSubstr(None, "PW")
### End ####



