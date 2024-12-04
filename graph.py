import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def sigmoid(x, a, b, c, d, e):
    return a/(b+np.exp(c*x+e))+d


def inverseSigmoid(y, params):
    a = params[0]
    b = params[1]
    c = params[2]
    d = params[3]
    e = params[4]
    return (np.log((a/(y-d))-b)-e)/c

def getCodingGain(BER, NoCodeParams, CodeParams):
    return inverseSigmoid(BER, NoCodeParams)-inverseSigmoid(BER, CodeParams)
    

SNR = np.array([-20, -10, -5, -3.5, -3, -2.5, -2, -1.5, -1, 1, 1.5, 2, 2.5, 3, 3.5, 5, 10, 20])
BERNoCode = np.array([0.4597, 0.3737, 0.28592, 0.25248, 0.23918, 0.22846, 0.21191, 0.20134, 0.18747, 0.13061, 0.11798, 0.10448, 0.09121, 0.07858, 0.06610, 0.03676, 0.00089, 0.00000])
#plt.plot(SNR, BERNoCode)
BERBCH = np.array([0.45869, 0.37562, 0.27076, 0.22649, 0.20743, 0.18966, 0.17333, 0.15233, 0.13533, 0.05986, 0.04580, 0.03245, 0.02280, 0.01498, 0.00797, 0.00159, 0.00000, 0.00000])
#plt.plot(SNR, BERBCH)
BERTurbo = np.array([0.46482, 0.38035, 0.23582, 0.15015, 0.11985, 0.08864, 0.06435, 0.04169, 0.02697, 0.00124, 0.00043, 0.00014, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000])
myX = np.arange(-20,20,0.00001)

BERNoCodeParams, param_cov = curve_fit(sigmoid, SNR, BERNoCode, method='trf')
a = BERNoCodeParams[0]
b = BERNoCodeParams[1]
c = BERNoCodeParams[2]
d = BERNoCodeParams[3]
e = BERNoCodeParams[4]
BERNoCodeEstimate = []
for i in range(0, len(SNR)):
    BERNoCodeEstimate.append(sigmoid(SNR[i], a, b, c, d, e))

myY = np.array([sigmoid(i,a,b,c,d,e) for i in myX])
plt.plot(myX, myY, color=(1,0,0), label="No Code")

BERBCHParams, param_cov = curve_fit(sigmoid, SNR, BERBCH, method='trf')
a = BERBCHParams[0]
b = BERBCHParams[1]
c = BERBCHParams[2]
d = BERBCHParams[3]
e = BERBCHParams[4]
BERBCHEstimate = []
for i in range(0, len(SNR)):
    BERBCHEstimate.append(sigmoid(SNR[i], a, b, c, d, e))

myY = np.array([sigmoid(i,a,b,c,d,e) for i in myX])
plt.plot(myX, myY, color=(0,1,0), label="BCH")

BERTurboParams, param_cov = curve_fit(sigmoid, SNR, BERTurbo, method='trf')
a = BERTurboParams[0]
b = BERTurboParams[1]
c = BERTurboParams[2]
d = BERTurboParams[3]
e = BERTurboParams[4]
BERTurboEstimate = []
for i in range(0, len(SNR)):
    BERTurboEstimate.append(sigmoid(SNR[i], a, b, c, d, e))

#plt.plot(SNR, BERTurbo)
#plt.plot(SNR, np.array(BERNoCodeEstimate))
#plt.plot(SNR, np.array(BERBCHEstimate))
#plt.plot(SNR, np.array(BERTurboEstimate))

myY = np.array([sigmoid(i,a,b,c,d,e) for i in myX])
plt.plot(myX, myY, color=(0,0,1), label="Turbo")

plt.scatter(SNR, BERNoCode, color=(1,0,0))
plt.scatter(SNR, BERBCH, color=(0,1,0))
plt.scatter(SNR, BERTurbo, color=(0,0,1))

if __name__=='__main__':
    print(f"We have made observations on {len(SNR)} simulations")
    print("SNR:No Code BER")
    for i in range(0, len(SNR)):
        print(f"{SNR[i]}:{BERNoCode[i]}")
    print()
    input()
    print("SNR:BCH BER")
    for i in range(0, len(SNR)):
        print(f"{SNR[i]}:{BERBCH[i]}")
    print()
    input()
    print("SNR:Turbo BER")
    for i in range(0, len(SNR)):
        print(f"{SNR[i]}:{BERTurbo[i]}")
    print()
    input()
    plt.show()
    YourBER = float(input("What is your BER for Coding Gain: "))
    print()
    print(f"Your coding gain for BCH is: {getCodingGain(YourBER, BERNoCodeParams, BERBCHParams)}")
    print(f"Your coding gain for Turbo is: {getCodingGain(YourBER, BERNoCodeParams, BERTurboParams)}")
