def filter_SSID(ssid_str):
    #add exceotion for no content in string here
    #split to list
    ssid_buf_ls = ssid_str.split("\n")
    #strip white space and remove empty ssid and add index
    index = 0
    ssid_buf_noWS_ls = []
    for str in ssid_buf_ls:
        if '""' not in str:
            ssid_buf_noWS_ls.append( f"(id : {index})" +str.strip())
        index = index +1

    return ssid_buf_noWS_ls

def print_ssid(ssid_ls):
    print("Available Networks : ")
    index = 1
    for str in ssid_ls:
        if not (index % 3):
            print(str, "\n")
        else:
            print(str)
        index = index +1 
def getList_usingID(id, ls):
    return ls[id]
    
