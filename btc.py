import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

from plotly import tools
import plotly.plotly as py
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
import plotly.graph_objs as go
import gc

import matplotlib.pyplot as plt
import seaborn as sns

#import os
#print(os.listdir("../input"))

from subprocess import check_output
print(check_output(["ls", "./data/Data.csv"]).decode("utf8"))