import numpy as np
from aircraft import aircraft, aspect_ratio, g
from atmosphere import isa_atmosphere

# محاسبه سرعت واماندگی
def stall_speed(rho):

    # وزن هواپیما
    W = aircraft["mass"] * g

    # مساحت بال
    S = aircraft["S"]

    # ضریب برا بیشینه
    CLmax = aircraft["CLmax"]

    # رابطه سرعت واماندگی
    return np.sqrt((2*W)/(rho*S*CLmax))


# محاسبه مسافت برخاست
def takeoff_distance():

    # دریافت چگالی در سطح دریا
    _,_,rho,_ = isa_atmosphere(0)

    # سرعت واماندگی
    Vs = stall_speed(rho)

    # سرعت برخاست 
    V_to = 1.2 * Vs

    # وزن
    W = aircraft["mass"] * g

    # تراست
    T = aircraft["thrust"]

    # مساحت بال
    S = aircraft["S"]

    # ضریب پسا پایه
    CD0 = aircraft["CD0"]

    # نسبت منظری
    AR = aspect_ratio()

    # فاکتور اسوالد
    e = aircraft["e"]

    # ضریب اصطکاک باند
    mu = 0.03

    # مقدار اولیه سرعت و مسافت
    V = 0
    s = 0

    # گام زمانی
    dt = 0.1

    # شبیه سازی حرکت روی باند
    while V < V_to:

        # ضریب برا
        CL = aircraft["CLmax"] * (V/V_to)**2

        # ضریب پسا
        CD = CD0 + CL**2/(np.pi*AR*e)

        # نیروی برا
        L = 0.5*rho*V**2*S*CL

        # نیروی پسا
        D = 0.5*rho*V**2*S*CD

        # نیروی خالص
        F = T - D - mu*(W-L)

        # شتاب
        a = F/aircraft["mass"]

        # بروزرسانی سرعت
        V += a*dt

        # بروزرسانی مسافت
        s += V*dt

    return s, Vs
