import math as m

#Here the code for the Simple brayton cycle will be made
#First the characteristics needed for the calculations:
n_iie = 0.98 #Intake isentropic efficiency
M_fcorr = 1400 #corrected Engine air mass flow rate in kg/s
FPR = 1.6 #Fan pressure ratio
BPR = 8 #Bypass ratio
PR_LPC = 1.4 #low pressure compressor pressure ratio
PR_HPC = 19 #high pressure compressor pressure ratio
T4 = 1450 #combustor exit temperature in K
n_fie = 0.92 #Fan isentropic efficiency
n_LPC = 0.90 #LPC isentropic efficiency
n_HPC = 0.9 #HPC isentropic efficiency
n_LPT = 0.92 #LPT isentropic efficiency
n_HPT = 0.92 #HPT isentropic efficiency
n_me = 0.99 #Mechanical efficiency
n_ce = 0.99 #combustion efficiency
cpr = 0.96
n_ne = 0.98
Tamb = 216
Pamb = 22632
R = 287
LHV = 43000000
Psea = 101325
Tsea = 288.15
Cpair = 1000
kair = 1.4
Cpgas = 1150
kgas = 1.33
M = 0.8
##Inlet conditions##
Tt1 = Tamb*(1+(kair-1)/2*M**2)
Pt1 = Pamb*(1+(kair-1)/2*M**2)**(kair/(kair-1))
Tt2 = Tt1
Pt2 = Pamb*(1+n_iie*(kair-1)/2*M**2)**(kair/(kair-1))
m1 = M_fcorr / (m.sqrt(Tt1/Tsea)/(Pt1/Psea))
mbp = m1/(BPR+1)*BPR
mcore = m1/(BPR+1)

## Fan Calculations ##
Pt13 = FPR*Pt2
Pt21 = Pt13
Tt13 = Tt2*(1 + 1/n_fie*((Pt13/Pt2)**((kair-1)/kair)-1))
Tt21 = Tt13
m21 = mcore
m13 = mbp

## LPC ##
Pt25 = PR_LPC*Pt21
Tt25 = Tt21*(1 + 1/n_fie*((Pt25/Pt21)**((kair-1)/kair)-1))
m25 = mcore

## HPC ##
Pt3 = PR_HPC*Pt25
Tt3 = Tt25*(1 + 1/n_fie*((Pt3/Pt25)**((kair-1)/kair)-1))
m3 = mcore

## Combustion chamber ##
Tt4 = T4
mf = m3*Cpgas*(Tt4 - Tt3)/(n_ce*LHV)
m4 = m3 + mf
Pt4 = cpr*Pt3

## High pressure Turbine ##

##Print Values##
print('-'*40)
print('Below the values for the Brayton cycle are given')
print('*'*10 + 'Inlet Conditions' + '*'*10)
print('Tt1 = %.2f K and Pt1 = %.2f Pa' %(Tt1, Pt1))
print('Tt2 = %.2f K and Pt2 = %.2f Pa' %(Tt2, Pt2))
print('Real mass flow rate = %.2f kg/s'% m1)
print('core mass flow = %.2f kg/s and bypass mass flow = %.2f kg/s' %(mcore,mbp))
print('*'*10 + 'Fan calculations' + '*'*10)
print('Pt13 = Pt21 = %.2f Pa' % Pt13)
print('Tt13 = Tt21 = %.2f K' % Tt13)
print('m21 = %.2f kg/s and m13 = %.2f kg/s'%(m21,m13))
print('*'*10 + 'LPC calculations' + '*'*10)
print('Pt25 %.2f Pa' % Pt25)
print('Tt25 %.2f K' % Tt25)
print('m25 = %.2f kg/s' % m25)
print('*'*10 + 'HPC calculations' + '*'*10)
print('Pt3 %.2f Pa' % Pt3)
print('Tt3 %.2f K' % Tt3)
print('m3 = %.2f kg/s' % m3)
print('*'*10 + 'Combustion chamber calculations' + '*'*10)
print('Pt4 = %.2f Pa' % Pt4)
print('Tt4 = %.2f K' % Tt4)
print('mf = %.2f kg/s and m4 = %.2f kg/s' %(mf,m4))
print('*'*10 + 'HPT calculations' + '*'*10)

### exit the program
input('Press ENTER to exit')


