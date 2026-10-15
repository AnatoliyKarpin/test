import RPi.GPIO as GPIO
import time


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def __del__(self):
        try:
            GPIO.output(self.bits_gpio, 0)
        except Exception:
            pass
        finally:
            GPIO.cleanup()

    def number_to_dac(self, number):
        bits_count = len(self.bits_gpio)
        for i, pin in enumerate(self.bits_gpio):
            bit = (number >> (bits_count - 1 - i)) & 1
            GPIO.output(pin, bit)

        if self.verbose:
            print(f"number_to_dac({number}) -> {number:08b}")

    def sequential_counting_adc(self):
        
        max_number = (1 << len(self.bits_gpio)) - 1

        for number in range(max_number + 1):
            self.number_to_dac(number)
            time.sleep(self.compare_time)

            comp_state = GPIO.input(self.comp_gpio)

            if self.verbose:
                print(f"number={number}, comparator={comp_state}")

            if comp_state:
                return number

        return max_number

    def get_sc_voltage(self):
      
        number = self.sequential_counting_adc()
        max_number = (1 << len(self.bits_gpio)) - 1
        return self.dynamic_range * number / max_number


if __name__ == "__main__":
    adc = None
    try:
        
        adc = R2R_ADC(dynamic_range=3.3, verbose=False)

        while True:
            voltage = adc.get_sc_voltage()
            print(f"Измеренное напряжение: {voltage:.3f} В")

    finally:
        if adc is not None:
            del adc