from math import pi
import cadquery as cq
from cadquery import *
from cqkit import *

from _CircleTangents import getTangents



def write_lsdyna_beam_elements(nodes, beams):
    """
    beams is a list containing tuples(startpoint, endpoints)
    """
    
    def beamcard(node1, node2, pid, eid):
        line = "%8d%8d%8d%8d%8d%8d%8d%8d%8d%8d\n" % (eid, pid, node1, node2, 0, 0, 0, 0, 0, 0)
        line += "%10g%10g%10g\n" % (0.0, 0.0, 1.0)
        return line
    
    def nodecard(node):
        nid, pos = node[0], node[1]
        #return "%8d,%g,%g%g" % (nid, pos[0], pos[1], pos[2])
        return "%8d%16g%16g%16g%8d%8d" % (nid, pos[0], pos[1], pos[2], 0, 0)
    
    f = open("beams.k", "w")
    f.write("*KEYWORD\n")
    f.write("*PART\n")
    f.write("Beams\n")
    f.write("$#     pid     secid       mid     eosid      hgid      grav    adpopt      tmid\n")
    f.write("         1         1         1         0         0         0         0         0\n")
    
    pid = 1
    eid = 1
    f.write("*ELEMENT_BEAM_ORIENTATION\n")
    f.write("$#   eid     pid      n1      n2      n3     rt1     rr1     rt2     rr2   local\n")
    for beam in beams:
        start, end = beam[0], beam[1]
        lines = beamcard(start, end, pid, eid)
        f.writelines(lines)
        eid += 1

    f.write("*NODE\n")
    f.write("$#   nid               x               y               z      tc      rc\n")
    for node in nodes:
        line = nodecard(node)
        f.writelines(line + "\n")

    f.write("*END\n")
    f.close()

    print("wrote beams.k with %d nodes and %d elements" % (len(nodes), len(beams)))
        
    

def generate_hourglass(parameters):

    # parameters which work
    H = 6 # 1/2 vertical height
    W = 6 # 1/2 horizontal distance
    R = 1.0 # radius of corner [0.5 ..2]
    r = 1.0 # radius of center half-circle [0.5 ..2]
    gap = 0.05 # 1/2 gap between stems and center arc
    T = 0.375# thickness
    T_stem = T 

    # overwrite with parameters passed into function
    r = parameters[0]
    R = parameters[1]

    # compute location of corner circle
    x1 = -(W - R)
    y1 = -H + R

    # compute location of center circle
    x2 = -r - T - 1.5*T_stem - 2*gap
    y2 = 0

    # outer tangent lines
    tgsOut = getTangents(x1, y1, R, x2, y2, r)
    tgOut = tgsOut[2] # there are 4 possible tangents, index=2 is the one we need

    # inner tangent lines
    tgsIn = getTangents(x1, y1, R-T, x2, y2, r+T)
    tgIn = tgsIn[2] # there are 4 possible tangents, index=2 is the one we need

    # create a work plane
    wp = cq.Workplane("XY")

    #
    # create outer boundary first.
    # We only model the bottom left quadrant and use symmetry to get the entire structure
    #

    # draw straight line from center to corner circle
    wp.add(wp.moveTo(0, -H).lineTo(x1, -H))

    # draw corner arc from current point over a midpoint (defining the radius) until tangent point
    midpoint = [x1-R,y1]
    endpoint = [tgOut[0], tgOut[1]] # 
    wp.add(wp.threePointArc(midpoint, endpoint))

    # draw outer tangent to center arc
    wp.add(wp.lineTo(tgOut[2], tgOut[3]))

    # draw central tangent arc
    endpoint = [x2+r, 0]
    wp.add(wp.radiusArc(endpoint, -r))

    # finish by mirroring quarter geometry to full plane
    wp.add(wp.mirrorX())
    wp.add(wp.mirrorY())
    

    # -------------------------------------------------------------------------
    # add stems
    # -------------------------------------------------------------------------

    # add top stem
    wp.add(wp.moveTo(0, H).lineTo(0, 0))

    # add lower stems
    wp.add(wp.moveTo(-T_stem - gap, -H).lineTo(-T_stem - gap, 0))
    # add lower stems
    wp.add(wp.moveTo(T_stem + gap, -H).lineTo(T_stem + gap, 0))
    
    # -------------------------------------------------------------------------
    # add bumps
    # -------------------------------------------------------------------------
    
    h_bump =0.25
    wp.add(wp.moveTo(-0.3*W, H).lineTo(-0.3*W, (1-h_bump)*H)) # add left bump
    wp.add(wp.moveTo( 0.3*W, H).lineTo( 0.3*W, (1-h_bump)*H)) # add right bump
     
    nid = 1
    nodes = []
    beams = []
    edges = wp.edges().vals() # vals()
    for edge in edges:
        length = edge.Length()
        
        num_pts = int(length/0.2)
        #print(length, num_pts)
        pts = discretize_edge(edge, resolution=num_pts)
        for pt in pts:
            wp.add( wp.moveTo(pt[0], pt[1]).circle(T) )            
            
        N = len(pts)
        for i in range(N):
            nodes.append((nid, pts[i]))
            if i < N - 1:
                beams.append((nid, nid+1))
            nid += 1
            
    write_lsdyna_beam_elements(nodes, beams)

    
    
    #display(wp2)
    #display(wp)
    
    
   

if __name__ == "__main__":
    generate_hourglass([2.5, 1.5])

