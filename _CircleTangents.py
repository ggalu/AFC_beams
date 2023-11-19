import math

def getTangents(x1, y1, r1, x2, y2, r2):
    """
    

    Parameters
    ----------
    x1 : TYPE
        DESCRIPTION.
    y1 : TYPE
        DESCRIPTION.
    r1 : TYPE
        DESCRIPTION.
    x2 : TYPE
        DESCRIPTION.
    y2 : TYPE
        DESCRIPTION.
    r2 : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    
    d_sq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    if (d_sq <= (r1-r2)*(r1-r2)):
        return None

    d = math.sqrt(d_sq)
    vx = (x2 - x1) / d
    vy = (y2 - y1) / d

    #double[][] res = new double[4][4];
    res = []
    i = 0
    # // Let A, B be the centers, and C, D be points at which the tangent
    # // touches first and second circle, and n be the normal vector to it.
    # //
    # // We have the system:
    # //   n * n = 1          (n is a unit vector)          
    # //   C = A + r1 * n
    # //   D = B +/- r2 * n
    # //   n * CD = 0         (common orthogonality)
    # //
    # // n * CD = n * (AB +/- r2*n - r1*n) = AB*n - (r1 -/+ r2) = 0,  <=>
    # // AB * n = (r1 -/+ r2), <=>
    # // v * n = (r1 -/+ r2) / d,  where v = AB/|AB| = AB/d
    # // This is a linear equation in unknown vector n.
    
    
    for sign1 in [1, -1]:
    #for (int sign1 = +1; sign1 >= -1; sign1 -= 2) {
        c = (r1 - sign1 * r2) / d

        #Now we're just intersecting a line with a circle: v*n=c, n*n=1

        if (c*c > 1.0):
            pass
        else:
            h = math.sqrt(max(0.0, 1.0 - c*c))
    
            for sign2 in [1, -1]:
                nx = vx * c - sign2 * h * vy;
                ny = vy * c + sign2 * h * vx;
    
                #double[] a = res[i++];
                a0 = x1 + r1 * nx
                a1 = y1 + r1 * ny
                a2 = x2 + sign1 * r2 * nx
                a3 = y2 + sign1 * r2 * ny
                res.append((a0,a1,a2,a3))
    
    return res
    