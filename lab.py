import numpy as np
import matplotlib.pyplot as plt
#import statistics as stat
from scipy.optimize import curve_fit
from scipy.special import factorial
from scipy.stats import poisson
from scipy.stats import norm
from scipy.stats import geom
from scipy.interpolate import make_interp_spline
import math


import csv 


def read_csv(filename):
    data=[]
    with open(filename,mode='r') as csv_file:
        csvReader = csv.reader(csv_file)
        i=0
        for row in csvReader:
            if i<15:
                print(row)
                i+=1
            elif i==15:
                # data.append(row)
                i+=1
            else:
                if len(row)==5:
                    # print(type(row[0]))
                    new_row=np.array(list(map(float, row)))
                    newer_row=[]
                    for j in new_row:
                        newer_row.append(abs(j))
                    data.append(newer_row)
                    
                else:
                    print(row)
                    print(i)
                i+=1
      
    data=np.stack(data,1)


    
    return data

def plot_set(x,y,name):
    
    
    
    
    
    
    plt.plot(
    x,
    y,
    
)
    
    # plt.legend(['Poisson Fit','Data'])
    plt.title(name.replace(".CSV",""))
    plt.xlabel("Applied Voltage (volts)")
    plt.ylabel("Collector Current (Amps)")
    plt.savefig(name.replace(".CSV",".png"))
    
    plt.show()
    return None 
def plot_smooth(x,y):
    print(x.ndim)
    print(np.any(x[1:] <= x[:-1]))
    
    
    xnew = np.linspace(x.min(), x.max(), 300)
  
    gfg = make_interp_spline(x, y, k=3)
    
    y_new = gfg(xnew)
    
    plt.plot(xnew, y_new)
    
    plt.show()
   
    
    
    
    return None
def find_peak(x,data,plot):
       

    
    #     ___ detection of local minimums and maximums ___
    
    a = np.diff(np.sign(np.diff(data))).nonzero()[0] + 1               # local min & max
    b = (np.diff(np.sign(np.diff(data))) > 0).nonzero()[0] + 1         # local min
    c = (np.diff(np.sign(np.diff(data))) < 0).nonzero()[0] + 1         # local max
    # +1 due to the fact that diff reduces the original index number
    #this function has been modified to only return the highest peaks. 
    # plot
    peak_ind=np.argmax(data[c])
    booL=x[c]>-17&x[c]<-15

    B=c[booL]
    

    print(x[B])
    peak_x=x[c][peak_ind]
    peak_y=data[c][peak_ind]
    if plot:
        plt.figure(figsize=(12, 5))
        plt.plot(x, data, color='grey')
        plt.plot(x[b], data[b], "o", label="min", color='r')
        plt.plot(peak_x, peak_y, "o", label="max", color='b')
        plt.show()
    return [peak_x,peak_y] 


def split(data,junk_range):
    size=data.shape[1]
    split1=(int(size/2)-1)-junk_range
    split2=(int(size/2)-1)+junk_range
    return data[:,0:split1],data[:,split2:size-50]
def see_voltage(data):
    plot_set(range(len(data[3,:])),data[3,:],"voltage")
def prune_data(data,thresh):
    
    bad_vals=[]
    for i in range(1,data.shape[1]):
        
        diff=data[3,i-1]-data[3,i]
        if abs(diff)>thresh:
            bad_vals.append(i)
    bad_vals=np.asarray(bad_vals)
    new_data=np.delete(data,bad_vals,axis=1)
    return new_data








"Frank Hertz Set"
# filename="2batteries_temp150C.CSV"
# split0=50
# split1=29200
# split2=31700
# split3=91350
# split4=94400

# split5=122700



# data=read_csv(filename)[:,1:]

# see_voltage(data)


# # plot_set(temp[3,:],temp[1,:],"splitt")
# plot_set(data[3,:split1],data[1,:split1],filename)
# plot_set(data[3,split2:split3],data[1,split2:split3],filename)

# plot_set(data[3,split4:split5],data[1,split4:split5],filename)


# "Frank Hertz Set"

# filename="1battery_temp150C (1).CSV"
# split0=50
# split1=31200
# split2=30600
# split3=91400
# split4=93000
# split5=122700



# data=read_csv(filename)[:,1:]
# see_voltage(data)


# # plot_set(temp[3,:],temp[1,:],"splitt")
# plot_set(data[3,:split1],data[1,:split1],filename)
# plot_set(data[3,split2:split3],data[1,split2:split3],filename)
# # plot_set(data[3,split4:split5],data[1,split4:split5],filename)













# filename="3volt2ndpeaks.CSV"
# split0=50
# split1=2480
# split2=2650
# split3=5100



# data=read_csv(filename)[:,1:]
# see_voltage(data)


# # plot_set(temp[3,:],temp[1,:],"splitt")
# plot_set(data[3,:split1],data[1,:split1],filename)
# # plot_set(data[3,split2:split3],data[1,split2:split3],filename)


# filename="3volt1stpeaks.CSV"
# split0=50
# split1=2480
# split2=2650
# split3=5100



# data=read_csv(filename)[:,1:]
# see_voltage(data)


# # plot_set(temp[3,:],temp[1,:],"splitt")
# plot_set(data[3,split0:split1],data[1,split0:split1],filename)
# plot_set(data[3,split2:],data[1,split2:],filename)





filename="1.5volt2ndpeaks.CSV"
split1=2480
split2=2650
split3=5100



data=read_csv(filename)[:,1:]
see_voltage(data)


# plot_set(temp[3,:],temp[1,:],"splitt")
plot_set(data[3,0:split1],data[1,0:split1],filename)
plot_set(data[3,split2:split3],data[1,split2:split3],filename)





# filename="1.5Volt1stpeaks (1).CSV"
# split1=2480
# split2=2650
# split3=5100



# data=read_csv(filename)[:,1:]
# see_voltage(data)


# # plot_set(temp[3,:],temp[1,:],"splitt")
# plot_set(data[3,0:split1],data[1,0:split1],filename)
# plot_set(data[3,split2:split3],data[1,split2:split3],filename)



"Frank Hertz Set"

# filename="temperature135C (1).CSV"
# split1=20500
# split2=25000
# split3=85500
# split4=90000
# split5=123200


# data=read_csv(filename)[:,1:]
# see_voltage(data)

# # find_peak(data[3,split2:split3],data[1,split2:split3],True)



# # plot_set(data[3,0:split1],data[1,0:split1],filename)
# plot_set(data[3,split2:split3],data[1,split2:split3],filename)
# # plot_set(data[3,split4:split5],data[1,split4:split5],filename+"Three")

"Frank Hertz Set"

# filename="temperature180C.CSV"
# split1=41100
# split2=43000
# split3=103000
# split4=106000

# data=read_csv(filename)[:,1:]
# see_voltage(data)



# plot_set(data[3,0:split1],data[1,0:split1],filename)
# plot_set(data[3,split2:split3],data[1,split2:split3],filename)
# # plot_set(data[3,split4:],data[1,split4:],filename)



