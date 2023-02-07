import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt



# N - całkowita populacja
N = 1000
# Początkowa liczba zarażonych I0 i Ozdrowiałych R0
I0, R0 = 1, 0

# S0 - potencjalni zarażeni
S0 = N - I0 - R0

# Wzkaźnik kontaktu - beta, współczynnik ozdrowień - gamma w przeciągu dnia.
beta, gamma = 0.2, 1./10 

# Zakres czasu w dniach
t = np.linspace(0, 160, 160)

#Równanie.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# vektor kondycji
y0 = S0, I0, R0
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

# Tworzenie wykresu
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)

#kolory do danych
ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Podejrzany')
ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Zainfekowany')
ax.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Odporny ozdrowieniec')

ax.set_xlabel('Czas/ dni')
ax.set_ylabel('Numer (1000s)')
ax.set_ylim(0,1.4)

#ax.yaxis.set_tick_params(length=0)
#ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')

#konfigurtacja legendy
legend = ax.legend()
legend.get_frame().set_alpha(0.5)

for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)

plt.show()