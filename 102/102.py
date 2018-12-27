#we know ,centroid is always inside the triangle,if origin is inside,they must give same signs with all the line inequalities
with open('p102_triangles.txt','r') as file:
    lines=file.readlines()
    points=[];n=0
    for line in lines:
        line_point=line.split(",")
        a,b,c,d,e,f=[int(x) for x in line_point]
        g,h=(a+c+e)/3,(b+d+f)/3#centroid
        def line_value(x1,y1,x2,y2):
            if x1-x2!=0:
                slope=(y2-y1)/(x2-x1)
                return lambda x,y:(slope*x-y-slope*x1+y1)>=0
            else:
                return lambda x,y:(x-x1)>=0
        line1=line_value(a,b,c,d)
        line2=line_value(c,d,e,f)
        line3=line_value(e,f,a,b)
        if line1(g,h)==line1(0,0) and line2(g,h)==line2(0,0) and line3(g,h)==line3(0,0):n+=1
    print(n)
