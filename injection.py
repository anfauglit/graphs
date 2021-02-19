import matplotlib.pyplot as plt
import numpy as np
import math

def myfunc(x):
	return 2 * x + 1

# plt.rc('text', usetex=True)
# plt.rc('font', family='serif')

domain = np.linspace(-5, 5, 100)

fig, axes = plt.subplots(3, 2, sharex='col', figsize=(10,10))

ax = axes.flatten()
for axis in fig.axes:
	axis.spines['left'].set_position('zero')
	axis.spines['bottom'].set_position('zero')
	axis.spines['right'].set_visible(False)
	axis.spines['top'].set_visible(False)
	axis.grid(True)

# ax[5].axis('off')
ax[0].set_title('Injection (inclusion)', loc='left')
ax[1].set_title(r'Injection $f(x) = 2x + 1$', loc='left')
ax[2].set_title(r'Non-injective function $f(x) = x^2$', loc='left')
ax[3].set_title(r'Injection $f(x) = e^x$', loc='left')
ax[4].set_title(r'Injection $f(x) = \ln(x)$', loc='left')
ax[5].set_title(r'Inverse relation of $f(x) = x^2$', loc='left')

#xticks = list(range(-5, 6))
#ax.set_xticks(xticks)
#yticks = xticks
#yticks.remove(0)
#ax.set_yticks(yticks)

ax[0].plot(domain, domain)
ax[1].plot(domain, list(map(myfunc, domain)))
domain_plus = list(filter(lambda x: x >= 0, domain))
ax[2].plot(domain, list(map(lambda x: x ** 2, domain)))
ax[3].plot(domain, list(map(lambda x: math.e ** x, domain)))
ax[4].plot(domain_plus, list(map(lambda x: math.log(x), domain_plus)))
ax[5].plot(list(map(lambda x: x ** 2, domain)), domain)

plt.show()
