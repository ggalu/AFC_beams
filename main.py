# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 14:18:58 2021

@author: Georg

This is the main routine which drives optimization of a geometry towards an
FEA-criteria

also see:
    https://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html

"""

import numpy as np
from scipy.optimize import minimize
from scipy.optimize import Bounds
import os
import _generate_hourglass
import _run_lsdyna
import _run_lsprepost


iteration = 0
import os
logfile = "opt_course.txt"
if os.path.exists(logfile):
  os.remove(logfile)
else:
  print("The file does not exist") 

def cost_function(p):
    """ main driver routine """
    
    print("current px:", p)

    folder_name = "run_r%4.2f_R%4.2f" % (p[0], p[1])
    print("this run:", folder_name)
    
    # generate geometry
    _generate_hourglass.generate_hourglass(p)
    status = _run_lsdyna.run_ls_dyna(folder_name)
    print("return code of LS-Dyna: ", status)
    metric = _run_lsprepost.run_ls_prepost(folder_name)
    
    with open(logfile, "a") as myfile:
        myfile.write("%g %g %g\n" % (p[0], p[1], metric))
        
    return metric

if __name__ == "__main__":

  case = "scan"

  if case == "opt": # do optimization
    bounds = Bounds([0.5, 0.5], [2.0, 2.0])
    p0 = np.array([1.5, 1.5])
    res = minimize(cost_function, p0, method='Nelder-Mead', bounds=bounds,
                options={'disp':True, 'xatol':0.1, 'fatol':0.0001})       
    #res = minimize(cost_function, p0, method='L-BFGS-B', bounds=bounds,
    #            options={'disp':99, 'ftol':0.0001, 'eps':0.2})              
    print(res.x) 

  elif case =="scan":
     R0 = 1.0
     r0 = 1.5
     #r_range = r0 + np.linspace(-0.5, 0.5, 10)
     R_range = R0 + np.linspace(-0.5, 0.0, 10)
     for R in R_range:
        p = [r0, R]
        cost_function(p)


  else: # run once
    #p0 = np.array([2.5, 1.5])
    p0 = np.array([1.5, 5/3])
    cost_function(p0)





    

