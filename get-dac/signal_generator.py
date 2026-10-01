import numpy as np
import time


def get_sin_wave_amplitude(freq, time):
    return (np.sin(2 * np.pi * freq * time) + 1) / 2

def get_trig_wave_amplitude(freq, time):

    return abs(2 * np.mod(time * freq, 1) - 1)
    # return 2* abs(2 *(freq*time - np.floor(freq*time +0.5)))
def wait_for_sampling_period(sampling_frequency):
    time.sleep(1 / sampling_frequency)

