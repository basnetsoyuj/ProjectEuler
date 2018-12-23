with open("p067_triangle.txt",'r') as file:
    str_=file.read()
    rowlist_=[[int(x) for x in a.split(' ') ]for a in str_.split("\n")]
    lenrow=len(rowlist_)
    def modifier(n):
        global rowlist_
        for i in range(0,len(rowlist_[n])-1):
            rowlist_[n-1][i]=max(rowlist_[n][i],rowlist_[n][i+1])+rowlist_[n-1][i]
    [modifier(x) for x in range(lenrow-1,0,-1)]
    print(rowlist_[0][0])
