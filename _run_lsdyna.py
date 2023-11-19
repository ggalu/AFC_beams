import os
import shutil

""" Nothing 
"""
def run_ls_dyna(folder_name):
    
    # make directory for this simulation and copy required files there
    path = os.path.join(os.getcwd(), folder_name)

    if os.path.exists(path):
       print("Warning, folder %s exists" % (path))
       print(" ... deleting this folder and carrying on")
       shutil.rmtree(path)

    os.mkdir(path)
    shutil.copy("main.k", path)
    shutil.copy("beams.k", path)


    import subprocess
    print(" --- Running LS-Dyna ---")
    comm = [r'/home/gcg/APPLICATIONS/LS-Dyna/lsdyna',
            'i=main.k', 'ncpu=2', 'memory=512M']
    outfile = open('subprocess_lsdyna.txt', "w")
    status = subprocess.run(comm, cwd=path, stdout=outfile)
    outfile.close()
    
    return status.returncode

if __name__ == "__main__":
  run_ls_dyna(("test"))

