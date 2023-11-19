""" Nothing 
"""
import os, shutil
import numpy as np

def run_ls_prepost(folder_name):
    
    cmd_file = "force.cmd"

    target_path = os.path.join(os.getcwd(), folder_name)
    source_path = os.path.join(os.getcwd(), "LS-Prepost")
    source_path = os.path.join(source_path, cmd_file)
    shutil.copy(source_path, target_path)
    
    import subprocess
    print(" --- Running LS-PrePost ---")
    comm = [r'/home/gcg/APPLICATIONS/lsprepost4.10_common_gtk3/lspp410',
            'c=force.cmd', '-nographics']
    outfile = open('subprocess_lsprepost.txt', "w")
    status = subprocess.run(comm, cwd=target_path, stdout=outfile)
    outfile.close()

    filename = os.path.join(target_path, "force.csv")
    data = np.genfromtxt(filename, delimiter=",", skip_header=2)
    x, y = data[:,0], data[:,1]
    integral = np.trapz(y, x=x)
    print("value of integral: ", integral)
    return integral
    
if __name__ == "__main__":
  run_ls_prepost("test")

