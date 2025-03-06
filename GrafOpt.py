import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def f(x,a,b):
    y=a*x+b;
    return y

def RL(T,n):
    N=np.size(T);
    sT=0; sn=0; sT2=0; sTn=0; serr=0;
    for i in range(0,N):
        sT+=T[i];
        sn+=n[i];
        sT2+=T[i]**2;
        sTn+=T[i]*n[i];

    a=(N*sTn-sT*sn)/(N*sT2-sT**2);    
    b=(sn-a*sT)/N;    

    for i in range(0,N):
        serr+=(n[i]-f(T[i],a,b))**2;

    sig=np.sqrt(serr/(N-2));
    da=(np.sqrt(N)*sig)/(np.sqrt(N*sT2-sT**2));
    db=da*np.sqrt(sT2/N);
    #Err=np.sqrt((da*20)**2+(0.1*a)**2+(db)**2);
    V=[a,b,da,db];
    
    return V
