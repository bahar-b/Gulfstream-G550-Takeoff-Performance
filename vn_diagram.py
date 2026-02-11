import numpy as np
import matplotlib.pyplot as plt
from aircraft import aircraft, g
from atmosphere import isa_atmosphere

# رسم دیاگرام V-n
def plot_vn():

    # چگالی هوا
    _,_,rho,_ = isa_atmosphere(0)

    # وزن
    W = aircraft["mass"]*g

    # مساحت بال
    S = aircraft["S"]

    # ضریب برا بیشینه
    CLmax = aircraft["CLmax"]

    # بازه سرعت
    V = np.linspace(0, aircraft["VD"], 500)

    # رابطه واماندگی
    n_stall = (0.5*rho*V**2*S*CLmax)/W

    plt.figure(figsize=(8,6))

    # رسم خطوط واماندگی
    plt.plot(V, n_stall)
    plt.plot(V, -n_stall)

    # محدودیت بار
    plt.axhline(aircraft["n_limit_pos"], linestyle="--")
    plt.axhline(aircraft["n_limit_neg"], linestyle="--")

    # سرعت شیرجه
    plt.axvline(aircraft["VD"], linestyle="--")

    plt.xlabel("Velocity (m/s)")
    plt.ylabel("Load Factor n")
    plt.title("V-n Diagram G550")
    plt.grid()

    plt.show()
