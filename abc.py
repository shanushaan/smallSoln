'''def smallestTrailSum(matrix):
    # assmuming the tests for differnt tests done.
    # find min_sum till [path]

    if not matrix: 
        return None
    if len(matrix) == 0 :
        return None
    
    for row in range(len(matrix)): 
        for col in range(len(matrix[row])): 
            if row ==0 and col ==0: 
                pass
            elif row==0:
                matrix[row][col] += matrix[row][col-1] 
            elif col==0:
                matrix[row][col] += matrix[row-1][col]
            else: 
                matrix[row][col] += min(matrix[row][col-1],matrix[row-1][col])
    print matrix
    return matrix[-1][-1]

myArray = [[1, 2, 3, 4],
             [1, -2, 7, 11],
            [9, 5,7,12]]

print zip(*myArray)[::-1]

#print smallestTrailSum(myArray)


myArray = None
#print smallestTrailSum(myArray)
'''

#
# [1, 2, 3, 4]
# [5, 6, 7, 8]
# [9, 10,11,12]
# [13,14,15,16]
#  
# Mat(i,j) = Mat(i,j) + min(Mat (i,j-1), Mat (i-1,j))
#
# [1, 3, 6, 10]
# [6, 9, 13, 18]
#
#
# Smallest SUM of trail starting from LT to RB.
# 1 - 2 - 3 -4 - 8 - 12 - 16
# 1 - 2 - 3 - 7 - 8 - 12 - 16
# 1 - 2 - 3 - 7 - 11 - 12 - 16
# 
#
#
# 1 - 5 - 9- 13 - 14 - 15 - 16

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
inp = raw_input()
remove = ["NS", "SN", "EW", "WE"]
removeDict = {"NES":"E","NWS":"W","SWN":"W","SEN":"E", "ENW":"N","ESW":"S","WSE":"S","WNE":"N"}
strReplaced = True
while(strReplaced):
    changed = False
    for item in remove:
        while inp.find(item) != -1:
            inp= inp.replace(item, "")
            changed =True
    for item in removeDict:
        if inp.find(item)!= -1:           
            changed = True
            inp = inp.replace(item,removeDict[item])
    if (changed):
        strReplaced =True
    else:
        strReplaced =False

print "".join(sorted(inp))
'''

env_codes={
        "environment":{
            "PUT":{
                        ("Please provide valid variable",901),
                        ("Success: Environment",700),
                        ("Error: Environment'",902),
                        ("user does not exist",903)},
            "DELETE":{
                        ("Please provide valid variable",901),
                        ("environment was DELETEd successfully",701),
                        ("environment does not exist in the system Please provide valid environment",904),
                        ("user does not exist",903)},
            "GET":{
                        ("Please provide valid variable",901),
                        ("Item found",703),
                        ("Item could not be found",906),
                        ("user does not exist",903)},
            "POST":{
                        ("Please provide valid variable",901),
                        ("already exist in the table Please update",907),
                        ("was successfully added",704),
                        ("user does not exist",903)}
        },
        "user":{	
            "POST":{
			("Error: Provide manadatory input parameter eagle",908),
			("was successfully updated",705),
			("does not exist in the system",909),
			("already exist in the ServiceNow",910)},
	
            "DELETE":{  ("was deleted",706),
			("does not exist in the system",903)},
			
            "PUT":{     ("Error: Provide manadatory input parameter _name",911),
			("does not exist in the ServiceNow",903),
			("Success: ' + _name + '  successfully updated",707)}
			
	},
        "case":{	
            "POST":{    ("valid user_name",912),
                        ("valid master_client_code",913),
                        ("not found in ServiceNow",903),
                        ("inserted successfully",707)},
            "PUT":{
                        ("not found in ServiceNow",903),
                        ("Mandatory parameter user_name does not exist",914),
                        ("The record has been updated  successfully",708)},						
            "GET":{     ("success",709),
                        ("not found in ServiceNow",915)}
        },
        "request":{	
            "POST":{    ("Please provide valid variable",901),
			("Item was requested successfully",710),
			("Item was not successfully",917),
			("user does not exist",903)},
            "GET":	{("master client code",918),
			("Success",711)},
            "PUT":{	("updated related task",712),
			("User not found",903),
			("not found Requested item",919),
			("did not found in ServiceNow",920)}
	},
        "notification":{
            "POST":{	("valid email address",921),
			("Notificaiton Group was inserted",713),
			("Notification Group already exists in the system",922),
			("provide a valid user name",903)},
            "DELETE":{	("invalid email address",921),
			("Group record was deleted successfully",714)},
            "PUT":{	("Please provide valid variable",901),
			("provide a valid email address",921),
			("updated successfully",715),
			("provide a valid user name",903)},
            "GET":{	("Failed to get the groups details",923),
			("Got the result successfully",716)}
        },
        "attachment":{
            "POST":{    ("Request completed successfully",717),
                        ("Request did not completed successfully",924),
                        ("File format is not allowed to upload",925)
                    },
            "DELETE":{  ("Resource executed successfully",718),
                        ("Resource did not executed successfully",926)
                    }
        }
        
}




def getCode(msg, action, uri,basecall):
    setCodes =None
    if uri.find("environments")!=-1:
        setCodes=env_codes["environment"][action.upper()]
    elif uri.find("users")!=-1:
        setCodes=env_codes["user"][action.upper()]
    elif uri.find("attachment")!=-1:
        setCodes=env_codes["attachment"][action.upper()]
    elif uri.find("cases")!=-1:
        setCodes=env_codes["case"][action.upper()]
    elif uri.find("requests")!=-1:
        setCodes=env_codes["request"][action.upper()]
    elif uri.find("groups")!=-1:
        setCodes=env_codes["notification"][action.upper()]
    
    if not setCodes:
        return 899

    for item in setCodes:
        if msg.find(item[0])!=-1:
            return item[1] 

    return 899

print getCode("File format is not allowed to upload", "post", "456/attachments/1231" )
