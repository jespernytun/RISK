from simulate-throw import Kast
import matplotlib.pyplot as pyplot

N = 1000
Win = 0
Loss = 0
Total = 0

while Total <= N:
    result = Kast(100,100)
    if result == True:
        Win += 1
        Total += 1
    elif result == False:
        Loss += 1
        Total += 1

xplot = ["wins","losses"]
yplot = [100*Win/(Win+Loss), 100*Loss/(Win+Loss)]

plt.bar(xplot,yplot)
plt.title("risk defender/attacker simulation N = 10000")
plt.xlabel("result")
plt.ylabel("percentage chance of given result")
plt.show()
