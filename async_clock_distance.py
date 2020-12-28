import random

# MHz

# Fout     = Fref  /refdiv*fbdiv/posdiv1/posdiv2
# 200Mhz   = 100Mhz/4     *32   /4      /1
# 433.3Mhz = 100Mhz/4     *52   /3      /1

#freq1 = 400 + 1.0/3.0*100
freq2 = 240/4 *25  # 1500
freq1 = 160/4 *25  # 1200

print(freq1, freq2)

# period
t1 = 1 / freq1 * 1000
t2 = 1 / freq2 * 1000

loop = 1000

# randomnize clock offset
start_distance = random.random() * t1

print("T1=", t1)
print("T2=", t2)
print("start_dis=", start_distance)

iter = 0
rise1 = 0
rise2 = start_distance

distances = []
while iter < loop:
    if rise1+t1 > rise2:
        if rise1 < rise2:
            delta = rise2 - rise1
        else:
            delta = rise2 + t2 - rise1
        # print("at time", rise1, rise2, "delta", delta)
        distances.append(delta)
        iter += 1
    # else:
    #     print("at time", rise1, rise2)


    next_rise1 = rise1 + t1
    next_rise2 = rise2 + t2

    if next_rise1 < rise2:
        rise1 = next_rise1
    else:
        rise2 = next_rise2
        if next_rise2 > next_rise1:
            rise1 = next_rise1

import matplotlib.pyplot as plt
plt.hist(distances, bins=100)
plt.show()
