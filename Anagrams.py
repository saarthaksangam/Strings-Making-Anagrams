def number_needed(a, b):
    s = 0
    
    maxm=""
    minn=""
    
    if max(len(a),len(b)) == len(b):
        
        for k in b:
            maxm = maxm + k
        for n in a:
            minn = minn + n
        
    else:
        
        for k in a:
            maxm = maxm + k
        for n in b:
            minn = minn + n
    
    
    
    for i in range(len(maxm)):
        for j in range(len(minn)):
            
            if maxm[i] == minn[j] and minn[j] != "X":
                s += 1
                c = list(minn)
                c[j] = "X"
                minn="".join(c)
                break
    print maxm
    print minn
    return len(a)+len(b)-(s*2)
    
    
    
a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
