def evaluatePoly(poly,x):
    Sum=0.0
    for i in range(len(poly)):
        Sum=Sum+(poly[i]*((x)**i))
    return Sum


        
