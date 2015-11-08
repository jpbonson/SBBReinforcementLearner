#!/usr/bin/env python
# encoding: utf-8
## vim:ts=4:et:nowrap

# http://www.danielsoper.com/statcalc3/calc.aspx?id=96
# https://www.mccallum-layton.co.uk/tools/statistic-calculators/confidence-interval-for-mean-calculator/#confidence-interval-for-mean-calculator

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import matplotlib.mlab as mlab
import math

patches = []

use_chart1 = True

if use_chart1:

    d = [
[0.52488, 0.55502, 0.56436, 0.56215, 0.558, 0.56223, 0.5625],
[0.52213, 0.55698, 0.55706, 0.55633, 0.55865, 0.55852, 0.56178],
[0.51783, 0.54462, 0.55485, 0.55533, 0.55693, 0.55725, 0.55791],
    ]

    data = d[0]
    color = 'r'
    plt.plot(data,color)
    patches.append(mpatches.Patch(color=color, label='default'))

    data = d[1]
    color = 'b'
    plt.plot(data,color)
    patches.append(mpatches.Patch(color=color, label='loose'))

    data = d[2]
    color = 'g'
    plt.plot(data,color)
    patches.append(mpatches.Patch(color=color, label='loose+HF'))

    # data = d[3]
    # color = 'm'
    # plt.plot(data,color)
    # patches.append(mpatches.Patch(color=color, label='4'))

    # data = d[4]
    # color = 'c'
    # plt.plot(data,color)
    # patches.append(mpatches.Patch(color=color, label='5'))

#     # data = d[5]
#     # color = 'y'
#     # plt.plot(data,color)
#     # patches.append(mpatches.Patch(color=color, label='NCD (C4, 3g)'))

#     # data = d[6]
#     # color = 'k'
#     # plt.plot(data,color)
#     # patches.append(mpatches.Patch(color=color, label='NCD (C4, 5g)'))

    plt.title("Champion (seed 5)")
    plt.legend(handles=patches, loc=1)
    # plt.axis([0, 6, 0, 1.0]) # per validation
    plt.axis([0, 6, 0.4, 0.8]) # per validation
    # plt.axis([0, 149, 0.4, 0.8]) # per training
    # plt.axis([0, 149, 0.0, 1.0]) # per training
    # plt.axis([0, 124, 0.4, 0.8]) # per training, diversity
    # plt.axis([0, 99, 0.4, 0.8]) # per training, opponent
    plt.show()

    #######################################

#     d = [
# [197.23958, 195.58333, 194.97916, 194.06249, 193.64583, 193.5, 192.79166, 192.68749, 192.36458, 192.35416, 192.0, 191.99999, 191.89583, 191.74999, 191.36458, 190.35416, 189.57291, 186.88541, 182.43749, 182.14583, 176.67708, 176.47916, 175.63541, 175.29166, 173.8125, 170.92708, 170.80208, 168.42708, 168.09375, 167.92708, 166.70833, 166.67708, 165.375, 165.17708, 164.03124, 163.53124, 161.07291, 159.9375, 157.61458, 157.20833, 155.13541, 154.92708, 150.23958, 149.64583, 149.22916, 147.98958, 147.29166, 140.56249, 118.90624, 104.95833],
# [197.23958, 201.95833, 205.60416, 206.47916, 208.48958, 209.39583, 210.08333, 210.29166, 210.42708, 210.42708, 210.98958, 211.05208, 211.09374, 211.09374, 211.18749, 211.72916, 211.87499, 212.21875, 214.40624, 215.88541, 222.27083, 224.375, 228.04166, 228.72916, 229.57291, 229.90625, 230.03125, 230.05208, 230.57291, 230.6875, 230.72916, 230.97916, 230.97916, 231.0, 231.0625, 231.09375, 232.21875, 232.21875, 232.26041, 233.27083, 233.27083, 233.45833, 233.45833, 233.52083, 233.79166, 234.07291, 234.21875, 234.28125, 234.28125, 234.28125]
#     ]

#     data = d[0]
#     color = '#B00000'
#     plt.plot(data, color)
#     patches.append(mpatches.Patch(color=color, label='1: indiv.'))
#     data = d[1]
#     color = 'r'
#     plt.plot(data, color)
#     patches.append(mpatches.Patch(color=color, label='1: accum.'))

#     d = [
# [199.35416, 199.20833, 197.78125, 195.36458, 194.72916, 192.10416, 191.66666, 190.74999, 190.29166, 189.91666, 187.4375, 187.36458, 187.36458, 184.34375, 184.10416, 183.62499, 183.04166, 183.0, 181.67708, 181.25, 180.84375, 180.08333, 179.54166, 179.37499, 178.83333, 177.77083, 176.77083, 176.74999, 176.22916, 176.17708, 174.66666, 174.63541, 174.57291, 172.11458, 171.27083, 169.14583, 166.35416, 159.18749, 155.30208, 154.16666, 152.47916, 152.45833, 144.97916, 142.375, 141.79166, 140.93749, 139.88541, 139.08333, 132.9375, 130.79166],
# [199.35416, 200.36458, 201.32291, 204.04166, 206.1875, 211.97916, 214.625, 215.77083, 218.04166, 219.02083, 219.0625, 219.3125, 219.3125, 220.29166, 220.41666, 222.04166, 226.83333, 226.83333, 228.22916, 228.64583, 229.33333, 230.35416, 230.58333, 230.72916, 230.8125, 231.04166, 231.04166, 231.08333, 232.33333, 232.5, 232.5, 232.85416, 233.02083, 233.89583, 234.10416, 234.3125, 234.45833, 234.70833, 234.72916, 234.90625, 234.90625, 234.90625, 234.92708, 235.01041, 235.01041, 235.23958, 235.23958, 235.23958, 235.23958, 235.96875]
#     ]

#     data = d[0]
#     color = '#000066'
#     plt.plot(data, color)
#     patches.append(mpatches.Patch(color=color, label='2: indiv.'))
#     data = d[1]
#     color = 'b'
#     plt.plot(data, color)
#     patches.append(mpatches.Patch(color=color, label='2: accum.'))

# #     d = [
# # [194.23958, 193.90625, 193.78125, 193.17708, 193.09374, 192.90624, 192.59374, 192.59374, 191.57291, 191.48958, 190.82291, 190.15624, 189.94791, 189.55208, 188.70833, 188.57291, 188.48958, 188.44791, 188.28125, 188.26041, 187.46875, 187.40625, 187.23958, 186.77083, 185.82291, 185.77083, 185.52083, 185.41666, 183.84375, 182.42708, 181.81249, 181.73958, 181.07291, 179.51041, 178.93749, 178.23958, 177.71874, 177.1875, 176.17708, 173.20833, 172.29166, 170.80208, 170.28124, 168.92708, 166.28125, 156.44791, 155.13541, 134.11458, 127.45833, 126.69791],
# # [194.23958, 199.09374, 203.65624, 203.96874, 206.86458, 206.90624, 207.96874, 208.34374, 208.80208, 208.90624, 209.38541, 213.44791, 215.21874, 215.26041, 219.05208, 219.53124, 219.53124, 219.80208, 219.84374, 220.07291, 220.32291, 220.81249, 220.87499, 221.66666, 222.89583, 222.89583, 225.49999, 225.49999, 225.49999, 227.39583, 227.74999, 227.84374, 229.26041, 229.78124, 229.86458, 231.42708, 231.46875, 232.76041, 232.76041, 232.76041, 232.80208, 232.92708, 232.92708, 232.92708, 233.21875, 233.90625, 233.90625, 236.07291, 236.07291, 236.07291]
# #     ]
# #     data = d[0]
# #     color = '#006600'
# #     plt.plot(data, color)
# #     patches.append(mpatches.Patch(color=color, label='3: indiv.'))
# #     data = d[1]
# #     color = 'g'
# #     plt.plot(data, color)
# #     patches.append(mpatches.Patch(color=color, label='3: accum.'))

# #     d = [
# # [194.78124, 194.38541, 193.76041, 193.26041, 193.26041, 192.44791, 191.67708, 190.90624, 190.73958, 190.36458, 190.30208, 190.26041, 189.69791, 189.44791, 189.32291, 189.11458, 189.05208, 188.94791, 188.94791, 188.44791, 188.36458, 187.84375, 187.82291, 187.76041, 187.42708, 187.36458, 186.86458, 186.78124, 186.69791, 186.17708, 186.05208, 185.92708, 185.82291, 185.55208, 184.63541, 180.82291, 180.01041, 178.67708, 178.57291, 177.42708, 177.42708, 175.80208, 175.34374, 172.15624, 171.65624, 166.40624, 146.48958, 144.17708, 141.09374, 140.94791],
# # [194.78124, 199.46874, 200.15624, 202.05208, 202.05208, 202.07291, 205.34374, 208.37499, 208.99999, 210.47916, 212.54166, 212.58333, 213.16666, 213.16666, 214.68749, 215.62499, 216.14583, 216.14583, 220.10416, 220.33333, 220.33333, 220.33333, 220.33333, 221.71874, 222.71874, 223.80208, 224.01041, 224.01041, 224.36458, 224.36458, 224.36458, 224.71874, 224.96874, 224.96874, 224.96874, 225.46874, 226.76041, 226.76041, 227.63541, 227.63541, 228.32291, 228.90624, 228.90624, 229.36458, 229.40624, 229.73958, 232.15624, 236.34374, 236.44791, 236.46874]
# #     ]
# #     data = d[0]
# #     color = '#CC0066'
# #     plt.plot(data, color)
# #     patches.append(mpatches.Patch(color=color, label='4: indiv.'))
# #     data = d[1]
# #     color = 'm'
# #     plt.plot(data, color)
# #     patches.append(mpatches.Patch(color=color, label='4: accum.'))

#     plt.title("Accumulative Curve (validation score)")
#     plt.legend(handles=patches, loc=3)
#     plt.axis([0, 49, 0, 300])
#     plt.show()
else:
    # m = [[0.0, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.0, 0.153, 0.0, 0.0, 1.0, 0.0, 1.0], [0.0, 0.153, 0.0, 0.0, 1.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.423, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.423, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.423, 0.0, 1.0, 0.0], [0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.475, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.475, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.475, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.475, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.386, 0.538, 0.435, 0.0, 0.736, 0.0, 0.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.589, 1.0, 0.333, 0.0, 0.0, 0.0, 0.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.589, 1.0, 0.333, 0.0, 0.0, 0.0, 0.0], [0.555, 1.0, 0.538, 0.0, 0.0, 0.0, 0.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.555, 1.0, 0.538, 0.0, 0.0, 0.0, 0.0], [0.555, 1.0, 0.538, 0.0, 0.0, 0.0, 0.0], [0.738, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.738, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.508, 1.0, 0.589, 0.0, 0.0, 0.0, 0.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.738, 0.0, 0.461, 0.884, 0.0, 0.0, 0.0], [0.555, 1.0, 0.538, 0.0, 0.0, 0.0, 0.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.555, 1.0, 0.538, 0.0, 0.0, 0.0, 0.0], [0.738, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.738, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.538, 1.0, 0.0, 0.0, 0.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.0, 0.0, 0.538, 1.0, 0.0, 0.0, 0.0], [0.738, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.538, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.538, 1.0, 0.0, 0.0, 0.0], [0.508, 1.0, 0.589, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.538, 1.0, 0.0, 0.0, 0.0], [0.738, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.897, 0.0, 0.641, 0.884, 0.0, 0.0, 0.0]]
    # OLD
    # m = [[0.035, 0.0, 0.0, 0.0, 0.992, 0.0, 1.0], [0.035, 0.0, 0.0, 0.0, 0.992, 0.0, 1.0], [0.452, 0.615, 0.0, 0.0, 0.0, 0.0, 1.0], [0.452, 0.615, 0.0, 0.0, 0.0, 0.0, 1.0], [0.452, 0.615, 0.0, 0.0, 0.0, 0.0, 1.0], [0.452, 0.615, 0.0, 0.0, 0.0, 0.0, 1.0], [0.452, 0.615, 0.0, 0.0, 0.0, 0.0, 1.0], [0.452, 0.615, 0.0, 0.0, 0.0, 0.0, 1.0], [0.452, 0.615, 0.0, 0.0, 0.0, 0.0, 1.0], [0.452, 0.615, 0.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]]

    # m = [[0.856, 0.846, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.846, 0.0, 0.447, 0.271, 0.0, 0.0], [0.625, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.856, 0.846, 0.0, 0.0, 0.0, 0.0, 0.0], [0.856, 0.846, 0.0, 0.0, 0.0, 0.0, 0.0], [0.625, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.198, 0.0, 0.0, 0.821, 0.0, 0.0, 0.0], [0.468, 0.0, 0.0, 0.931, 0.0, 0.0, 0.0], [0.0, 0.0, 0.564, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.564, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.538, 0.0, 0.756, 1.0, 0.0], [0.795, 0.769, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.564, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.564, 0.0, 1.0, 0.0, 0.0], [0.795, 0.769, 0.0, 0.0, 0.0, 0.0, 1.0], [0.795, 0.769, 0.0, 0.0, 0.0, 0.0, 1.0], [0.795, 0.769, 0.0, 0.0, 0.0, 0.0, 1.0], [0.795, 0.769, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.564, 0.0, 1.0, 0.0, 0.0], [0.795, 0.769, 0.0, 0.0, 0.0, 0.0, 1.0]]
    # m = [[0.64, 0.0, 0.41, 0.714, 0.0, 0.0, 0.0], [0.64, 0.0, 0.41, 0.714, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.64, 0.0, 0.41, 0.714, 0.0, 0.0, 0.0], [0.997, 0.923, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.672, 0.0, 1.0, 0.0, 0.802, 0.0, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.756, 0.846, 0.0, 0.0, 0.0, 0.0, 1.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.12, 0.0, 0.384, 0.0, 0.362, 0.75, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0]]

    # m = [[0.0, 0.0, 0.0, 0.439, 0.0, 0.75, 1.0], [0.756, 0.846, 0.358, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.439, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0]]
    # m = [[0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.635, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.635, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.635, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.681, 0.846, 0.0, 0.0, 0.0, 0.0, 1.0], [0.493, 0.0, 0.615, 0.0, 0.0, 1.0, 0.0], [0.642, 0.0, 0.846, 0.0, 0.436, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.593, 0.0, 0.0], [0.635, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0]]

    m = [[0.494, 0.692, 0.0, 0.0, 0.0, 1.0, 0.0], [0.494, 0.692, 0.0, 0.0, 0.0, 1.0, 0.0], [0.494, 0.692, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.692, 0.0, 0.0, 0.0, 1.0, 0.5], [0.0, 0.461, 0.179, 0.466, 0.0, 0.75, 0.0], [0.0, 0.461, 0.179, 0.466, 0.0, 0.75, 0.0], [0.0, 0.461, 0.179, 0.466, 0.0, 0.75, 0.0], [0.0, 0.461, 0.179, 0.466, 0.0, 0.75, 0.0], [0.0, 0.461, 0.179, 0.466, 0.0, 0.75, 0.0], [0.0, 0.692, 0.076, 0.0, 0.0, 1.0, 0.5], [0.0, 0.692, 0.076, 0.0, 0.0, 1.0, 0.5], [0.117, 0.461, 0.179, 0.466, 0.0, 0.75, 0.0], [0.0, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.0, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.0, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.152, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.152, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.0, 0.692, 0.256, 0.508, 0.0, 0.75, 0.5], [0.0, 0.692, 0.256, 0.508, 0.0, 0.75, 0.5], [0.0, 0.692, 0.256, 0.508, 0.0, 0.75, 0.5], [0.0, 0.692, 0.256, 0.508, 0.0, 0.75, 0.5], [0.117, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.553, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.553, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.553, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.553, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.4, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.46, 0.692, 0.205, 0.448, 0.0, 0.75, 0.5], [0.521, 0.692, 0.205, 0.448, 0.0, 0.75, 0.5], [0.521, 0.692, 0.205, 0.448, 0.0, 0.75, 0.5], [0.521, 0.692, 0.205, 0.448, 0.0, 0.75, 0.5], [0.553, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.546, 0.692, 0.0, 0.574, 0.0, 0.75, 0.5], [0.713, 0.692, 0.0, 0.334, 0.0, 0.75, 0.5], [0.713, 0.692, 0.0, 0.334, 0.0, 0.75, 0.5], [0.577, 0.692, 0.0, 0.448, 0.954, 0.0, 0.5], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 0.5], [0.404, 0.692, 0.205, 0.448, 0.954, 0.0, 0.5], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 0.5], [0.404, 0.692, 0.205, 0.448, 0.954, 0.0, 0.5], [0.499, 0.692, 0.0, 0.448, 0.954, 0.0, 0.5], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 0.5], [0.561, 0.692, 0.0, 0.479, 0.951, 0.0, 0.5], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 0.5], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 0.5], [0.577, 0.692, 0.0, 0.508, 0.954, 0.0, 0.5], [0.3, 0.923, 0.205, 0.447, 0.954, 0.0, 0.5], [0.3, 0.923, 0.205, 0.447, 0.954, 0.0, 0.5], [0.3, 0.923, 0.205, 0.447, 0.954, 0.0, 0.5], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 1.0], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 1.0], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 1.0], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 1.0], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 1.0], [0.478, 0.692, 0.205, 0.479, 0.951, 0.0, 0.5], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 1.0], [0.478, 0.692, 0.205, 0.479, 0.951, 0.0, 0.5], [0.481, 0.692, 0.205, 0.26, 0.951, 0.0, 1.0], [0.481, 0.692, 0.205, 0.26, 0.951, 0.0, 1.0], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 1.0], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 1.0], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 0.5], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 1.0], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.545, 0.769, 0.205, 0.495, 0.954, 0.0, 0.5], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.545, 0.769, 0.205, 0.494, 0.954, 0.0, 0.5], [0.478, 0.769, 0.205, 0.495, 0.954, 0.0, 0.5], [0.38, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.478, 0.692, 0.205, 0.479, 0.951, 0.0, 0.5], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.605, 0.692, 0.205, 0.374, 0.985, 0.0, 1.0], [0.605, 0.692, 0.205, 0.374, 0.985, 0.0, 0.5], [0.605, 0.692, 0.205, 0.374, 0.985, 0.0, 0.5], [0.545, 0.769, 0.205, 0.494, 0.953, 0.0, 0.5], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.605, 0.692, 0.205, 0.374, 0.985, 0.0, 1.0], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.479, 0.692, 0.205, 0.531, 0.95, 0.0, 1.0], [0.509, 0.692, 0.205, 0.551, 0.954, 0.0, 0.5], [0.545, 0.769, 0.0, 0.561, 0.953, 0.0, 0.5], [0.525, 0.769, 0.0, 0.428, 0.985, 0.0, 1.0], [0.642, 0.769, 0.0, 0.494, 0.953, 0.0, 1.0], [0.642, 0.769, 0.0, 0.494, 0.953, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.953, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.954, 0.0, 1.0], [0.625, 0.769, 0.0, 0.532, 0.95, 0.0, 1.0], [0.625, 0.769, 0.0, 0.532, 0.95, 0.0, 1.0], [0.689, 0.461, 0.205, 0.494, 0.953, 0.0, 0.5], [0.54, 0.615, 0.0, 0.606, 0.953, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.953, 0.0, 1.0], [0.518, 0.615, 0.0, 0.606, 0.953, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.953, 0.0, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.6, 0.307, 0.0, 0.792, 0.954, 0.0, 1.0], [0.545, 0.769, 0.205, 0.495, 0.953, 0.0, 0.5], [0.662, 0.769, 0.205, 0.247, 0.983, 0.0, 0.5], [0.538, 0.769, 0.205, 0.578, 0.953, 0.0, 1.0], [0.538, 0.769, 0.205, 0.578, 0.953, 0.0, 1.0], [0.726, 0.769, 0.0, 0.522, 0.981, 0.25, 1.0], [0.726, 0.769, 0.0, 0.522, 0.981, 0.25, 1.0], [0.642, 0.769, 0.0, 0.561, 0.953, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.953, 0.0, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.625, 0.769, 0.0, 0.602, 0.978, 0.25, 1.0], [0.642, 0.769, 0.0, 0.561, 0.953, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.953, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.953, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.953, 0.0, 1.0], [0.725, 0.769, 0.0, 0.522, 0.981, 0.25, 1.0], [0.625, 0.769, 0.0, 0.602, 0.978, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.642, 0.769, 0.0, 0.561, 0.954, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.954, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.954, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.954, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.954, 0.0, 1.0], [0.625, 0.769, 0.0, 0.602, 0.977, 0.25, 1.0], [0.625, 0.769, 0.0, 0.602, 0.977, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.635, 0.769, 0.0, 0.628, 0.954, 0.0, 1.0], [0.818, 0.769, 0.0, 0.521, 0.985, 0.25, 1.0], [0.818, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.642, 0.923, 0.0, 0.433, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.982, 0.75, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.982, 0.75, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.982, 0.75, 1.0], [0.818, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.75, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.818, 0.769, 0.0, 0.521, 0.985, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.982, 0.75, 1.0], [0.818, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.818, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.708, 0.692, 0.0, 0.577, 0.983, 0.75, 1.0], [0.706, 0.692, 0.0, 0.577, 0.983, 0.75, 1.0], [0.708, 0.692, 0.0, 0.577, 0.983, 0.75, 1.0], [0.708, 0.692, 0.0, 0.577, 0.983, 0.75, 1.0], [0.708, 0.692, 0.0, 0.577, 0.983, 0.75, 1.0], [0.622, 0.692, 0.0, 0.574, 0.982, 0.75, 1.0], [0.688, 0.692, 0.0, 0.596, 0.982, 0.75, 1.0], [0.677, 0.692, 0.0, 0.601, 0.983, 0.75, 1.0], [0.694, 0.538, 0.0, 0.686, 0.982, 0.75, 1.0], [0.694, 0.538, 0.0, 0.686, 0.982, 0.75, 1.0], [0.764, 0.846, 0.0, 0.401, 0.983, 0.75, 1.0], [0.764, 0.846, 0.0, 0.401, 0.983, 0.75, 1.0], [0.646, 0.923, 0.0, 0.433, 0.983, 0.75, 1.0], [0.685, 0.846, 0.0, 0.433, 0.983, 0.75, 1.0], [0.587, 0.923, 0.0, 0.599, 0.983, 0.75, 1.0], [0.573, 0.692, 0.0, 1.0, 0.983, 0.75, 1.0], [0.609, 0.692, 0.0, 1.0, 0.987, 0.75, 1.0], [0.609, 0.692, 0.0, 1.0, 0.987, 0.75, 1.0], [0.737, 0.769, 0.0, 0.882, 0.983, 0.75, 1.0], [0.609, 0.692, 0.0, 1.0, 0.987, 0.75, 1.0], [0.587, 0.846, 0.0, 0.882, 0.983, 0.75, 1.0], [0.573, 0.692, 0.0, 1.0, 0.983, 0.75, 1.0], [0.776, 0.769, 0.0, 0.51, 0.998, 0.75, 1.0], [0.573, 0.692, 0.0, 1.0, 0.983, 0.75, 1.0], [0.609, 0.692, 0.0, 1.0, 0.987, 0.75, 1.0], [0.737, 0.769, 0.0, 0.882, 0.983, 0.75, 1.0], [0.588, 0.846, 0.0, 0.882, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.736, 0.769, 0.0, 0.882, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.882, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.882, 0.985, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.985, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.882, 0.983, 0.75, 1.0], [0.736, 0.769, 0.0, 0.882, 0.982, 0.75, 1.0], [0.736, 0.769, 0.0, 0.882, 0.982, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.882, 0.985, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.985, 0.75, 1.0], [0.573, 0.692, 0.0, 1.0, 0.985, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.985, 0.75, 1.0], [0.69, 0.692, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.985, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.985, 0.75, 1.0], [0.69, 0.692, 0.0, 1.0, 0.983, 0.75, 0.5], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.736, 0.769, 0.0, 0.882, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.882, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.982, 1.0, 1.0], [0.73, 0.538, 0.0, 1.0, 0.985, 0.75, 1.0], [0.69, 0.692, 0.0, 1.0, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.73, 0.538, 0.0, 1.0, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.882, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.707, 0.846, 0.0, 0.882, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.586, 0.846, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.771, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.771, 0.769, 0.0, 0.967, 0.985, 0.75, 0.5], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.771, 0.769, 0.0, 0.967, 0.985, 0.75, 0.5], [0.771, 0.769, 0.0, 0.967, 0.985, 0.75, 0.5], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.771, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.771, 0.769, 0.0, 0.967, 0.985, 0.75, 0.5], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.763, 0.769, 0.0, 0.967, 0.985, 0.75, 0.5], [0.763, 0.769, 0.0, 0.967, 0.985, 0.75, 0.5], [0.763, 0.769, 0.0, 0.967, 0.985, 0.75, 0.5], [0.763, 0.769, 0.0, 0.967, 0.985, 0.75, 0.5], [0.771, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.771, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.706, 0.846, 0.0, 0.967, 0.985, 0.75, 1.0], [0.706, 0.846, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.706, 0.846, 0.0, 0.967, 0.982, 0.75, 1.0], [0.706, 0.846, 0.0, 0.967, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.983, 0.75, 0.5], [0.666, 0.846, 0.256, 0.821, 0.983, 0.75, 0.5], [0.707, 0.846, 0.0, 0.967, 0.983, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.605, 0.846, 0.282, 0.967, 0.983, 0.75, 0.5], [0.666, 0.769, 0.282, 0.967, 0.983, 0.75, 0.5], [0.704, 0.769, 0.153, 0.967, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.769, 0.282, 0.967, 0.983, 0.75, 0.5], [0.677, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.677, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.677, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.588, 0.846, 0.256, 0.796, 0.985, 0.75, 1.0], [0.727, 0.846, 0.256, 0.796, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.737, 0.846, 0.41, 0.818, 0.983, 0.75, 1.0], [0.737, 0.846, 0.41, 0.818, 0.983, 0.75, 1.0], [0.737, 0.846, 0.41, 0.818, 0.983, 0.75, 1.0], [0.737, 0.846, 0.41, 0.818, 0.983, 0.75, 1.0], [0.737, 0.846, 0.41, 0.818, 0.983, 0.75, 1.0], [0.737, 0.846, 0.384, 0.812, 0.985, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.737, 0.846, 0.41, 0.818, 0.983, 0.75, 1.0], [0.812, 0.769, 0.256, 0.821, 0.985, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.737, 0.846, 0.41, 0.818, 0.983, 0.75, 1.0], [0.8, 0.846, 0.41, 0.818, 0.985, 0.75, 1.0], [0.8, 0.846, 0.41, 0.818, 0.985, 0.75, 1.0], [0.737, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.807, 0.769, 0.256, 0.821, 0.983, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.634, 0.846, 0.358, 0.821, 0.985, 0.75, 1.0], [0.634, 0.846, 0.358, 0.821, 0.985, 0.75, 1.0], [0.682, 0.769, 0.256, 0.821, 0.985, 0.75, 1.0], [0.737, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.682, 0.769, 0.256, 0.821, 0.983, 0.75, 1.0], [0.737, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.682, 0.769, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.682, 0.769, 0.256, 0.821, 0.985, 0.75, 1.0], [0.812, 0.769, 0.256, 0.821, 0.985, 0.75, 1.0], [0.812, 0.769, 0.256, 0.821, 0.983, 0.75, 1.0], [0.774, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.774, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.634, 0.846, 0.358, 0.821, 0.985, 0.75, 1.0], [0.634, 0.846, 0.358, 0.821, 0.985, 0.75, 1.0], [0.634, 0.846, 0.358, 0.821, 0.985, 0.75, 1.0], [0.634, 0.846, 0.358, 0.821, 0.983, 0.75, 1.0], [0.896, 0.769, 0.051, 0.967, 0.983, 0.75, 1.0], [0.896, 0.769, 0.051, 0.967, 0.983, 0.75, 1.0], [0.896, 0.769, 0.051, 0.967, 0.983, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.737, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.634, 0.846, 0.358, 0.821, 0.983, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.982, 0.75, 1.0], [0.634, 0.846, 0.358, 0.821, 0.983, 0.75, 1.0], [0.825, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.74, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.742, 0.846, 0.282, 0.821, 0.983, 0.75, 1.0], [0.742, 0.846, 0.282, 0.821, 0.983, 0.75, 1.0], [0.667, 0.923, 0.282, 0.814, 0.985, 0.75, 0.5], [0.841, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.85, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.71, 0.923, 0.256, 0.821, 0.983, 0.75, 1.0], [0.822, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.982, 0.75, 1.0], [0.831, 0.846, 0.256, 0.821, 0.982, 0.75, 1.0], [0.71, 0.923, 0.256, 0.821, 0.983, 0.75, 1.0], [0.85, 0.846, 0.256, 0.821, 0.982, 0.75, 1.0], [0.776, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.79, 0.846, 0.256, 0.821, 0.982, 0.75, 1.0], [0.723, 0.923, 0.256, 0.821, 0.983, 0.75, 1.0], [0.841, 0.615, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.615, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.836, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.982, 0.75, 1.0], [0.831, 0.615, 0.256, 0.821, 0.983, 0.75, 1.0], [0.79, 0.846, 0.256, 0.821, 0.982, 0.75, 1.0], [0.79, 0.846, 0.256, 0.821, 0.982, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.982, 0.75, 1.0], [0.836, 0.615, 0.256, 0.821, 0.985, 0.75, 1.0], [0.836, 0.615, 0.256, 0.821, 0.985, 0.75, 1.0], [0.831, 0.615, 0.256, 0.821, 0.983, 0.75, 1.0], [0.822, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.836, 0.615, 0.256, 0.821, 0.985, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.538, 0.282, 0.967, 0.983, 0.75, 1.0], [0.853, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.843, 0.538, 0.282, 0.967, 0.985, 0.75, 1.0], [0.843, 0.538, 0.282, 0.967, 0.985, 0.75, 1.0], [0.823, 0.538, 0.282, 0.967, 0.985, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.843, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.703, 0.538, 0.282, 0.967, 0.985, 0.75, 1.0], [0.843, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.843, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.843, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.853, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.538, 0.282, 0.967, 0.985, 0.75, 1.0], [0.703, 0.538, 0.282, 0.967, 0.983, 0.75, 1.0], [0.703, 0.538, 0.282, 0.967, 0.983, 0.75, 1.0], [0.703, 0.538, 0.282, 0.967, 0.983, 0.75, 1.0], [0.703, 0.538, 0.282, 0.967, 0.983, 0.75, 1.0], [0.824, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.824, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.824, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.843, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.666, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.831, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.831, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.843, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.853, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.713, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.802, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.713, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.843, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.864, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.843, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.634, 0.769, 0.384, 0.967, 0.985, 0.75, 1.0], [0.634, 0.769, 0.384, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.737, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.615, 0.282, 0.967, 0.983, 0.75, 0.5], [0.634, 0.769, 0.384, 0.967, 0.985, 0.75, 1.0], [0.834, 0.615, 0.282, 0.967, 0.985, 0.75, 1.0], [0.834, 0.615, 0.282, 0.967, 0.985, 0.75, 1.0], [0.824, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.824, 0.615, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.615, 0.282, 0.967, 0.985, 0.75, 1.0], [0.834, 0.615, 0.282, 0.967, 0.982, 0.75, 1.0], [0.802, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.823, 0.615, 0.282, 0.967, 0.985, 0.75, 1.0], [0.834, 0.615, 0.282, 0.967, 0.982, 0.75, 1.0], [0.958, 0.615, 0.0, 0.967, 0.983, 0.75, 1.0], [0.951, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.953, 0.538, 0.0, 0.967, 0.983, 0.75, 1.0], [0.958, 0.538, 0.0, 0.967, 0.982, 0.75, 1.0], [0.958, 0.538, 0.0, 0.967, 0.985, 0.75, 1.0], [0.93, 0.769, 0.051, 0.967, 0.985, 0.75, 1.0], [0.831, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.93, 0.769, 0.051, 0.967, 0.985, 0.75, 1.0], [0.831, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.831, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.957, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.951, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.802, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.802, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.802, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.958, 0.769, 0.0, 0.967, 0.982, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.802, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.634, 0.769, 0.384, 0.967, 0.983, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.824, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.824, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.615, 0.282, 0.967, 0.985, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.824, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.615, 0.282, 0.967, 0.985, 0.75, 1.0], [0.823, 0.615, 0.282, 0.967, 0.985, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.824, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.816, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.615, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.819, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.831, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.819, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.861, 0.769, 0.282, 0.883, 0.985, 0.75, 1.0], [0.653, 0.769, 0.384, 0.967, 0.985, 0.75, 1.0], [0.831, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.7, 0.769, 0.307, 0.967, 0.983, 0.75, 1.0], [0.7, 0.769, 0.307, 0.967, 0.983, 0.75, 1.0], [0.653, 0.769, 0.384, 0.967, 0.983, 0.75, 1.0], [0.818, 0.769, 0.076, 0.967, 0.983, 0.75, 1.0], [0.634, 0.769, 0.384, 0.967, 0.985, 0.75, 1.0]]

    a = np.array(m)
    np.set_printoptions(precision=3)
    d = [a[:,0], a[:,1], a[:,2], a[:,3], a[:,4], a[:,5], a[:,6]]

    for item in d:
        data = item
        plt.plot(data)

    plt.title("DR per class over generations")
    plt.axis([0, 499, -0.1, 1.1])
    plt.show()
