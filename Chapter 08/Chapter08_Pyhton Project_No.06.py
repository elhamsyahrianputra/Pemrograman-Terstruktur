def sortStringByChar(myData):
    endData = []
    
    for data in myData: 
        newData = (len(data), data)
        endData.append(newData)
    
    endData.sort(reverse=True) 
    
    sortData = []
    for bil in endData:
        sortData.append(bil[1])
        
    return sortData


myData = ["semangka", "rambutan", "anggur", "ubi", "lidah buaya"]
print(sortStringByChar(myData))