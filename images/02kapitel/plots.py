import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp

# redefining plot save parameters
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Charter"],
    "font.size": 12
})

matplotlib.use("pgf")

# defining the isosbestic point
isosbestic_point = 3390

# reading the prepared data
temp_data_raw = pd.read_csv('water-temperature_data-raw.csv', sep=';')
temp_data_norm = pd.read_csv('water-temperature_data-norm.csv', sep=';')
temp_time = pd.read_csv('water-temperature_data-time.csv', sep=';')
data_spectrum = pd.read_csv('plot-data-spectrum.csv', sep=';')
data_molar = pd.read_csv('plot-data-molar.csv', sep=';')
data_intersec = pd.read_csv('plot-intersec.csv', sep=';')

temp_data_norm.set_index('Wellenlange', inplace=True)
temp_data_raw.set_index('Wellenlange', inplace=True)
temp_time.set_index('time', inplace=True)
data_spectrum.set_index('raman_shift', inplace=True)
data_molar.set_index('xETOH', inplace=True)
data_intersec.set_index('raman_shift', inplace=True)

temp_data_raw[1:] = temp_data_raw[1:]/1000000
data_spectrum[1:] = data_spectrum[1:]/1000000
data_intersec[1:] = data_intersec[1:]/10000

# # Plot of raw data
# temp_data_raw['0'].plot(label='$T_\mathrm{K}=293,35~\mathrm{K}$')
# temp_data_raw['70'].plot(label='$T_\mathrm{K}=346,65~\mathrm{K}$')
# plt.axvline(x = isosbestic_point, color='purple', linestyle='--', label='isosbestic point')
# plt.xlabel('Raman shift $\Delta v$ in $\mathrm{cm}^\mathrm{-1}$')
# plt.ylabel('Signal intensity in $10^6$')
# plt.grid()
# plt.legend()
# plt.savefig('temp_data_raw.pgf')
# plt.close()

# # Plot of normalized data
# temp_data_norm['0'].plot(label='$T_\mathrm{K}=293,35~\mathrm{K}')
# temp_data_norm['70'].plot(label='$T_\mathrm{K}=346,65~\mathrm{K}')
# plt.axvline(x = isosbestic_point, color='purple', linestyle='--', label='isosbestic point')
# plt.xlabel('Raman shift $\Delta v$ in $\mathrm{cm}^\mathrm{-1}$')
# plt.ylabel('Normalized signal intensity')
# plt.grid()
# plt.legend()
# plt.savefig('temp_data_norm.pgf')
# plt.close()

# # Plot of temperatures from thermocouple and raman
# temp_time['T_thermocouple'].plot(label='T by thermocouple')
# temp_time['T_raman'].plot(label='T by Raman')
# plt.xlabel('Time in $\mathrm{s}$')
# plt.ylabel('Temperature in $\mathrm{K}$')
# plt.grid()
# plt.legend()
# plt.savefig('temp_time.pgf')
# plt.close()

# # Plot of spectrum e00, e10 and unknown
# data_spectrum['e00'].plot(label='spectrum $x=0,0$')
# data_spectrum['e10'].plot(label='spectrum $x=1,0$')
# data_spectrum['e_unknown'].plot(label='spectrum $x=\mathrm{unknown}$')
# plt.legend()
# plt.grid()
# plt.xlabel('Raman shift $\Delta v$ in $\mathrm{cm}^\mathrm{-1}$')
# plt.ylabel('Siganl intensity in $10^6$')
# plt.savefig('spectra.pgf')
# plt.close()

# Plot of the determination integration limits
# intersec = data_intersec['stw'].to_list()
# plt.plot(data_intersec.index, intersec, '*', color='orange', label='standard deviation of all spectra')
# plt.legend()
# plt.xlabel('Raman shift $\Delta v$ in $\mathrm{cm}^\mathrm{-1}$')
# plt.ylabel('standard deviation in $10^4$')
# plt.ylim(bottom=0)
# plt.grid()
# plt.savefig('stw.pgf')
# plt.close()

# # Plot of calibration curve (linear fit)
# calib_data = data_molar.drop('unknown', axis=0)
# calib_lst = calib_data['signal_ratio'].tolist()
# calib_x = [0,0.1,0.2,0.4,0.6,0.8,1]

# def fit_func(x, m):
#     y = m*x
#     return y

# m, z = sp.optimize.curve_fit(fit_func, calib_x, calib_lst)

# plt.plot(calib_x, calib_lst, '.', label='signal ratio calibration')
# plt.plot(calib_x, fit_func(calib_x, m), '--', label='fit function')
# plt.text(0.7, 0.25, 'fit function:\ny(x)= '+str(np.round(m[0], 3))+' $\cdot$ x')
# plt.legend()
# plt.grid()
# plt.xlabel('Molar ethanol content')
# plt.ylabel('Signal ratio')
# plt.ylim(bottom=0, top=1.1)
# # plt.savefig('calibration.pgf')
# plt.show()
# # plt.close()

# Plot of calibration curve (inverted, polynomial fit)
calib_data = data_molar.drop('unknown', axis=0)
calib_x = calib_data['signal_ratio'].tolist()
calib_lst = [0,0.1,0.2,0.4,0.6,0.8,1]

m = np.polyfit(calib_x, calib_lst, 2)

fit_func = np.poly1d(m)
fit_x = [0,0.1,0.2,0.4,0.6,0.8,1]

plt.plot(calib_x, calib_lst, '.', label='signal ratio calibration')
plt.plot(fit_x, fit_func(fit_x), '--', label='fit function')
plt.text(0.05, 0.7, 'fit function:\ny(x)= '+str(np.round(m[0], 3))+' $\cdot~x^2-$'+str(abs(np.round(m[1], 3)))+' $\cdot~x+$'+str(np.round(m[2], 3)))
plt.legend()
plt.grid()
plt.ylabel('Molar ethanol content')
plt.xlabel('Signal ratio')
# plt.ylim(bottom=0, top=1.1)
plt.xlim(left=0, right=1.0)
plt.savefig('calibration.pgf')
plt.show()
plt.close()