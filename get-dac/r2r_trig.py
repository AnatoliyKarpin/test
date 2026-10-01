import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.18
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    dac = None
    try:
        dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, False)

        while True:
            u = (sg.get_trig_wave_amplitude(signal_frequency, time.time())) * amplitude
            dac.set_voltage(u)
            sg.wait_for_sampling_period(sampling_frequency)

    finally:
        if dac is not None:
            dac.deinit()