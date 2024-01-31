import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



# redefining plot save parameters
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Charter"],
    "font.size": 12
})

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

# defining the isosbestic point
isosbestic_point = 3390

# reading the prepared data
temp_data_raw = pd.read_csv('water-temperature_data-raw.csv', sep=';')
temp_data_norm = pd.read_csv('water-temperature_data-norm.csv', sep=';')
temp_time = pd.read_csv('water-temperature_data-time.csv', sep=';')

temp_data_norm.set_index('Wellenlange', inplace=True)
temp_data_raw.set_index('Wellenlange', inplace=True)
temp_time.set_index('time', inplace=True)

temp_data_raw[1:] = temp_data_raw[1:]/1000000


# Plot of raw data
# temp_data_raw['0'].plot(label='lowest temperature')
# temp_data_raw['70'].plot(label='highest temperature')
# plt.axvline(x = isosbestic_point, color='purple', linestyle='--', label='isosbestic point')
# plt.xlabel('Raman shift $\Delta \tilde{v}$ in $\mathrm{cm^{-1}$')
# plt.ylabel('Signal intensity')
# plt.grid()
# plt.legend()
# plt.savefig('temp_data_raw.pgf')



# Plot of normalized data
# temp_data_norm['0'].plot(label='lowest temperature')
# temp_data_norm['70'].plot(label='highest temperature')
# plt.axvline(x = isosbestic_point, color='purple', linestyle='--', label='isosbestic point')
# plt.xlabel('Raman shift')# ' in $cm$')
# plt.ylabel('Normalized signal intensity')
# plt.grid()
# plt.legend()
# plt.savefig('temp_data_norm.pgf')

# Plot of temperatures from thermocouple and raman
# temp_time['T_thermocouple'].plot(label='T by thermocouple')
# temp_time['T_raman'].plot(label='T by Raman')
# plt.xlabel('Time in $\mathrm{s}$')
# plt.ylabel('Temperature in $\mathrm{K}$')
# plt.grid()
# plt.legend()
# plt.savefig('temp_time.pgf')