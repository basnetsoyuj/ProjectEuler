n=286
while True:
    t_num=n*(n+1)*0.5
    p_index=(1+(1+24*t_num)**0.5)/6
    h_index=(1+(1+8*t_num)**0.5)/4
    if p_index==int(p_index) and h_index==int(h_index):
        print(int(t_num))
        break
    n+=1
