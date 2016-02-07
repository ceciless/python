# -*- coding: utf-8 -*-



a=param[0]
b=param[1]
c=param[2]
d=param[3]

x=U[0]
y=U[1]
U_dot =[x*(a-b*y), y*(-c+d*x)]
return no.array(U_dot)

def Resolution_Euler(t,U_0):
    X=np.zeros((len(U_0),len(t)),'float')
    X[:,0]=U_0
    for k in range(len(t)-1):
        X[:,K+1]=X[:,K]+h*f(X[:,k],t)
    return X


if __name__=="__main__":
    print("Test du modele")
    a=3.
    b=1.
    c=2.
    d=1.
    param=[a,b,c,d]
    U_0=[1.0,2.0]
    print('parametre de modele: ',param)