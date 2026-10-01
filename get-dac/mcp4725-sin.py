import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    dac = None
    try:
        dac = mcp.MCP4725(5.11, 0x61, False)

        while True:
            u = amplitude * sg.get_sin_wave_amplitude(signal_frequency, time.time())
            dac.set_voltage(u)
            sg.wait_for_sampling_period(sampling_frequency)

    finally:
        if dac is not None:
            dac.deinit()