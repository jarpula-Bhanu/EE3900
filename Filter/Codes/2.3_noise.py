import soundfile as sf
from scipy import signal

#read .wav file
input_signal,fs = sf.read("../sound files/Sound_Noise.wav")

#sampling frequency of input signal
sampl_freq = fs

#order of the filter
order = 4

#cutoff frquency 4KHz
cutoff_freq = 4000.0

#digital frequency
Wn = 2*cutoff_freq/sampl_freq

# b and a are numerator and denominator polynomial respectively
b,a = signal.butter(order,Wn,'low')

#filter the input signal with butterworth filter
output_signal = signal.filtfilt(b,a,input_signal)

#write the output signal into .wav file 
sf.write("../sound files/Sound_With_ReducedNoise.wav",output_signal,fs)