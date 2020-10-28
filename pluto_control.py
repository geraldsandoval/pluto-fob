import adi
import matplotlib.pyplot as plt
import numpy as np
import time


class PlutoSDR:

    def __init__(self, bandwidth, center_freq, sample_rate, buffer_size):
        self.bandwidth = int(bandwidth)
        self.buffer_size = buffer_size
        self.center_freq = int(center_freq) 
        self.sample_rate = int(sample_rate)
        self.sdr = adi.Pluto("ip:192.168.2.1")
        self.pluto_config()

    def pluto_config(self):
        self.sdr.sample_rate = self.sample_rate
        self.sdr.rx_rf_bandwidth = self.bandwidth
        self.sdr.rx_lo = self.center_freq
        self.sdr.rx_buffer_size = self.buffer_size

    def capture_signals(self):
        capture = []
        for i in range(0, 10):
            #capture.append(self.sdr.rx())
            #plt.plot(capture)
            samples = self.sdr.rx()    
            plt.plot(samples)
            plt.show()


def main():

    pluto = PlutoSDR(bandwidth=1e6, 
                     center_freq=315e6, 
                     sample_rate=61.44e6, 
                     buffer_size=10240)

    pluto.capture_signals()


if __name__ == '__main__':
    main()

