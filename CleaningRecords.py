#Create function for updating data
def update(currmem,exmem):
    
    with open(currmem,'r+') as memList: #Open file
        with open(exmem,'a+') as exList: #open second file
            memList.seek(0) #go to the starting location of the file
            members = memList.readlines() #get all data in the form of lines.
            header = members[0] #define first line of the data as the header
            members.pop(0) #pop remove the first line of data.
            inactive =[] #create inactive list in memory
            for member in members: #Note to self - members refers to the data read, not the file itself
                if 'no' in member:
                    inactive.append(member) #append ex member to the inactive list.
            
            memList.seek(0) #go back to the starting location
            memList.write(header) #write the defined header again
            for member in members: #check if member in inactive and write them accordingly.
                if (member in inactive):
                    exList.write(member)
                else:
                    memList.write(member)
            memList.truncate() # remove the additional/duplicate data

currmem = 'members_copy.txt'
exmem = 'inactive_copy.txt'            
update(currmem,exmem)
