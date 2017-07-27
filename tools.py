def build_decode():
    table = {}
    arr = []
    with open('gsm7bit.data', 'r') as f:     
        for l in f:
            c = l[:1]
            oc = str(ord(c))
            dc = l[1:].strip()
            table[dc] = oc
            arr.append(dc)
            l = "".join(arr)
    print(l)
    return table
	
def build_encode():
    table = {}
    arr = []
    with open('gsm7bit.data', 'r') as f:     
        for l in f:
            c = l[:1]
            oc = str(ord(c))
            dc = l[1:].strip()
            table[oc] = dc
            arr.append(c)
    l = "".join(arr)
    print (l)
    return table
    
