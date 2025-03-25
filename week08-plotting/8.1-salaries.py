import numpy as np
import matplotlib.pyplot as plt

minsalary = 20000
maxsalary = 80000
values = 10

minage = 21
maxage = 65

np.random.seed(1984)

salaries = np.random.randint(minsalary,maxsalary,values)
ages = np.random.randint(minage,maxage,values)
print(salaries)

salariesplus = salaries + 5000
print(salariesplus)

salariesmult = salaries * 1.05
salariesmult = salariesmult.astype(int)
print(salariesmult)

# plt.hist(salaries)
# plt.show()

plt.scatter(ages, salaries, label="Salaries")

xpoints = np.arange(1, 101)
ypoints = xpoints**2

plt.plot(xpoints, ypoints, color='r',label='$x^2$')

plt.title("Random Plot")
plt.xlabel("Salaries")
plt.ylabel("Ages")
plt.legend()

plt.savefig("prettier-plot.png")

plt.show()