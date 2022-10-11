import zhinst.core
import zhinst.utils
import numpy as np
from scipy.signal import chirp

##  Initiliase HDAWG system  ##
device = 'dev8416'  # device ID for G14.
awgMod = HDAWG_PLser(device)
command_table=1

## Common Parameter Definition
#Clock Parameters
sampling_rate=2.4E9 # Hz; Sampling rate, should be the same as what you set on the right panel!

Number_of_burning_pulses = 299 # Number of burning pulse repetitions  
Number_of_burning_back_pulses = 200 # Number of burn-back pulse repetitions 
Number_of_cleaning_pulses = 260 # Number of clean pulse repetitions 
Number_of_AFC_pulses = 50 # Number of repetitions of AFC preperation pulse train

# Burning Pulse Parameters
centre_freq_burning=250E6; #Hz; Central frequency set to drive the AOM for burning 
#chirpAmplitude_burning = 0; # V; amplitude of burning pulse 
chirpAmplitude_burning = 0.10; # V; amplitude of burning pulse 
freq_sweeping_burning=3.5E6 # Hz; set the scanning frequency range of burning pulse (the actual scanning range should be 4*freq_detuning)
burning_duration=0.6e-3; # s; burning time 
t_burning = np.linspace(0,burning_duration,burning_duration*sampling_rate)

# Burning back Pulse Parameters
centre_freq_burning_back=263.75E6; # Hz; Central frequency set to drive the AOM for burn-back
#chirpAmplitude_burning_back = 0; # V; amplitude of burn-back
chirpAmplitude_burning_back = 0.047; # V; amplitude of burn-back
freq_sweeping_burning_back=0.8e6; # Hz; set the scanning frequency range of burn-back (the actual scanning range should be 4*freq_detuning)
burning_back_duration=0.1e-3; # s; burning time burn-back
t_burning_back = np.linspace(0,burning_back_duration,burning_back_duration*sampling_rate)

# Cleaning Pulse Parameters
centre_freq_cleaning=252.7E6 # Hz; Central frequency set to drive the AOM for cleaning
#chirpAmplitude_cleaning = 0.0
chirpAmplitude_cleaning = 0.05 #  V; amplitude of cleaning
freq_sweeping_cleaning=1E6 # Hz; set the scanning frequency range of cleaning (the actual scanning range should be 4*freq_detuning)
cleaning_duration=0.5e-3 # s; burning time cleaning
t_cleaning = np.linspace(0,cleaning_duration,cleaning_duration*sampling_rate)

# Reading Pulse Parameters
centre_freq_reading=250E6; # Hz; Central frequency set to read out the burned spectral hole
chirpAmplitude_reading = 0.03; # V; amplitude of reading-out pulse
freq_sweeping_reading=5E6; # Hz; set the scanning frequency range of reading-out pulse (the actual scanning range should be 4*freq_detuning) 1.32877326E6
reading_duration=4e-3; # s; reading-out time
t_reading = np.linspace(0,reading_duration,reading_duration*sampling_rate)

# Shuffle Pulse Parameters
centre_freq_shuffle=250E6; # Hz; Central frequency of the shuffle pulse
chirpAmplitude_shuffle = 0.21; # V; amplitude of shuffling pulse
freq_sweeping_shuffle=20E6; # Hz; set the scanning frequency range of shuffling pulse
shuffle_duration=10e-3; # s; shuffling time
t_shuffle = np.linspace(0,shuffle_duration,shuffle_duration*sampling_rate)

## Waveform Definitions

chirpedSine_burning = chirpAmplitude_burning*chirp(t_burning,centre_freq_burning-freq_sweeping_burning/2,burning_duration,centre_freq_burning+freq_sweeping_burning/2)
chirpedSine_burning_back = chirpAmplitude_burning_back*chirp(t_burning_back,centre_freq_burning_back-freq_sweeping_burning_back/2,burning_back_duration,centre_freq_burning_back+freq_sweeping_burning_back/2)
chirpedSine_cleaning = chirpAmplitude_cleaning*chirp(t_cleaning,centre_freq_cleaning-freq_sweeping_cleaning/2,cleaning_duration,centre_freq_cleaning+freq_sweeping_cleaning/2)
chirpedSine_reading = chirpAmplitude_reading*chirp(t_reading,centre_freq_reading-freq_sweeping_reading/2,reading_duration,centre_freq_reading+freq_sweeping_reading/2)
chirpedSine_shuffle = chirpAmplitude_shuffle*chirp(t_shuffle,centre_freq_shuffle-freq_sweeping_shuffle/2,shuffle_duration,centre_freq_shuffle+freq_sweeping_shuffle/2)

