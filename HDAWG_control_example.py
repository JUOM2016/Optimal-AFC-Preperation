import zhinst.core
import zhinst.utils
import numpy as np

device = 'dev8416'  # device ID for G14.
daq = zhinst.core.ziDAQServer('localhost', 8004, 6) # Connect to the dataserver
daq.connectDevice(device, '1GbE') # Connect to device

# Generate waveform and marker

LENGTH = 1024
wave_a = np.sin(np.linspace(0, 10*np.pi, LENGTH))*np.exp(np.linspace(0,-5,LENGTH))
wave_b = np.sin(np.linspace(0, 20*np.pi, LENGTH))*np.exp(np.linspace(0,-5,LENGTH))
wave_c = np.sin(np.linspace(0, 30*np.pi, LENGTH))*np.exp(np.linspace(0,-5,LENGTH))
wave_d = np.sin(np.linspace(0, 40*np.pi, LENGTH))*np.exp(np.linspace(0,-5,LENGTH))

marker_a = np.concatenate([ 0b11*np.ones(32), np.zeros(LENGTH-32)]).astype(int)
marker_bc = np.concatenate([0b1111*np.ones(32), np.zeros(LENGTH-32)]).astype(int)

# Convert and send them to the instrument

marker_ab = np.concatenate([0b1111*np.ones(32), np.zeros(LENGTH-32)]).astype(int)
marker_cd = np.concatenate([0b1111*np.ones(32), np.zeros(LENGTH-32)]).astype(int)

wave_raw_ab = zhinst.utils.convert_awg_waveform(wave_a, wave_b, markers=marker_ab)
wave_raw_cd = zhinst.utils.convert_awg_waveform(wave_c, wave_d, markers=marker_cd)

set_cmd = [(f'/{device:s}/awgs/0/waveform/waves/10', wave_raw_ab),
           (f'/{device:s}/awgs/1/waveform/waves/10', wave_raw_cd)]

daq.set(set_cmd)