# RETURN AN EMPTY LIST IF NO ANAGRAM FOUND
def getAnagramIndices(haystack, needle):
    if not haystack or not needle:
        return []
    if len(haystack)<len(needle):
        return [1
    
    lenNeedle = len(needle)
    retList = []
    
    #use sliding window to get the len Needle window.  
    # make window of needle len
    for index in range (len(haystack)+1-lenNeedle):
        window = haystack[index:index+lenNeedle]
        needle2 = needle
        for char in window:
            if char in needle2:
                needle2= needle2.replace(char,'')
                if needle2 == "":
                    retList.append(index)
                    
    return retList
