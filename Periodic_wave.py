import matplotlib.pyplot as plt
import numpy as np
import mplcyberpunk

plt.style.use("cyberpunk")


def f_periodic_wave(ksi, c0, a, lyambda):
    """
    Periodic wave

    :param ksi:
    :param c0: CONST
    :param a:
    :param lyambda:
    :return: y


    """
    return c0 + a * np.sin(2 * np.pi * ksi / lyambda)


ksi, c0 = np.linspace(0, 12, 100), float(input("Input CONST c0:"))
y = f_periodic_wave(ksi=ksi, c0=c0, a=float(input("Input param a:")), lyambda=float(input("Input param lyambda:")))
y1 = -ksi
fig, ax = plt.subplots(figsize=(10, 6))
plt.grid(which='both', linewidth=1.5, linestyle='-', color='gray')
ax.tick_params(which='major', length=8, width=2)
ax.tick_params(which='minor', length=8, width=2)
ax.minorticks_on()
ax.grid(which='major',
        linewidth=2)
ax.grid(which='minor',
        linestyle=':')
plt.title('$c = F(\epsilon) = c_0 + asin(2\pi\epsilon/\lambda)$')
plt.xlabel('$\epsilon$')
plt.ylabel('F')
ax.set_xlim(0, 12)
ax.set_ylim(-12, 12)
plt.axhline(c0, c='yellow', linewidth=4)
plt.plot(ksi, y, c='blue', linewidth=4)
plt.fill_between(ksi, y, y1+6, where=(ksi >= 1.0) & (ksi <= 11.0), hatch='\\\\\\\\', interpolate=False, facecolor='red')
# where=(ksi >= 1.0) & (ksi <= 11.0)
plt.plot(ksi, y1+6, marker='D', linewidth=4)
legend = plt.legend(['$y=c_0$', 'Ударна конструкція для періодичної хвилі'], title='Legend',
                    loc='upper right', shadow=True, fontsize='x-large',
                    frameon=True, title_fontsize=15, framealpha=1)
frame = legend.get_frame()
frame.set_facecolor('black')
frame.set_edgecolor('red')
mplcyberpunk.add_glow_effects()
mplcyberpunk.add_gradient_fill(alpha_gradientglow=0.5)
plt.show()
fig.savefig('P_Wave.png', dpi=300, bbox_inches='tight')
