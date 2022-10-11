import zhinst.core
import zhinst.utils
import numpy as np
from scipy.signal import chirp

device = 'dev8416'  # device ID for G14.
daq = zhinst.core.ziDAQServer('localhost', 8004, 6) # Connect to the dataserver
daq.connectDevice(device, '1GbE') # Connect to device

# Generate waveform and marker

LENGTH = 1024
wave_a = np.sin(np.linspace(0, 10*np.pi, LENGTH))*np.exp(np.linspace(0,-5,LENGTH))
wave_b = np.sin(np.linspace(0, 20*np.pi, LENGTH))*np.exp(np.linspace(0,-5,LENGTH))
wave_c = np.sin(np.linspace(0, 30*np.pi, LENGTH))*np.exp(np.linspace(0,-5,LENGTH))

marker_a = np.concatenate([ 0b11*np.ones(32), np.zeros(LENGTH-32)]).astype(int)
marker_bc = np.concatenate([0b1111*np.ones(32), np.zeros(LENGTH-32)]).astype(int)

# Convert and send them to the instrument

wave_raw_a = zhinst.utils.convert_awg_waveform(wave_a, markers=marker_a)
wave_raw_bc = zhinst.utils.convert_awg_waveform(wave_b, wave_c, markers=marker_bc)

set_cmd = [(f'/{device:s}/awgs/0/waveform/waves/10', wave_raw_a),
           (f'/{device:s}/awgs/0/waveform/waves/11', wave_raw_bc) ]

daq.set(set_cmd)