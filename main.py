from takeoff import takeoff_distance
from vn_diagram import plot_vn

# تابع اصلی اجرای برنامه
def main():

    # محاسبه مسافت برخاست و سرعت واماندگی
    s, Vs = takeoff_distance()

    # چاپ خروجی
    print("Takeoff Distance:", s, "meters")
    print("Stall Speed:", Vs, "m/s")

    # رسم دیاگرام V-n
    plot_vn()


if __name__ == "__main__":
    main()
