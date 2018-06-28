#from plotter import *
import os
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from plotter import *
from matplotlib import rc
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
font = {'size': 15}
rc('font', **font)



if __name__ == '__main__':

    if len(sys.argv) == 1:
        file = None
    else:
        file = os.path.splitext(sys.argv[1])[0]

    

    #file = "test_param_0067"
    #file = "train_param_0069"
    #file = None

    if file is None:
        all_files = [f for f in os.listdir("logs") if os.path.isfile(os.path.join("logs", f))]
        #print(all_files)
        #print("\n")
        csv_list = [os.path.splitext(f)[0] for f in all_files if os.path.splitext(f)[1]=='.csv']
        #print(csv_list)
        #print("\n")
        png_list = [os.path.splitext(f)[0] for f in all_files if os.path.splitext(f)[1]=='.png']
        #print(png_list)
        #print("\n")
        fname_list = [f for f in csv_list if f not in png_list]
        #print(fname_list)
        #print("\n")

    else: 
        fname_list = [file]

    for fname in fname_list:

        plot_log(fname)
    
