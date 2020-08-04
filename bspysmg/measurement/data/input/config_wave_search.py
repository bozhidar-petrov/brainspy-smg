import numpy as np
from scipy import signal
from SkyNEt.config.config_class import config_class
import os


class experiment_config(config_class):
    '''
    This is the config for the wave search experiment. The input waves are generated by generateSineWave
    which can be configured with the parameters below. The input data is not saved in the experiment file
    (and also not in the RAM) since this takes up too much space. 
    '''

    def __init__(self):
        super().__init__()

        self.waveElectrodes = 7
        self.factor = 0.05
        self.freq2 = np.array([2, np.pi, 5, 7, 13, 17, 19])
        self.freq = np.sqrt(self.freq2[:self.waveElectrodes]) * self.factor
        self.phase = np.zeros(self.waveElectrodes)

        self.fs = 50
        self.amplitude = np.array([0.9, 0.9, 0.9, 0.9, 0.9, 0.5, 0.5])  # Maximum amount of voltage for the inputs
        self.offset = np.array([-0.3, -0.3, -0.3, -0.3, -0.3, -0.2, -0.2])  # Optional offset for the sine waves

        self.sampleTime = 500  # Sample time of the sine waves for one grid point (in seconds)

        self.transientTest = False
        self.n = 500  # Amount of test points for the transient test
        self.samplePoints = int(50 * self.fs)  # Amount of sample points per batch measurement (sampleTime*fs/samplePoints batches)
        self.amplification = 100
        self.gain_info = '10MV/A'
        self.postgain = 1

        #                               Summing module S2d      Matrix module           device
        self.electrodeSetup = [['ao5', 'ao3', 'ao1', 'ao0', 'a02', 'ao4', 'ao6', 'out'], [1, 3, 5, 6, 11, 13, 15, 17], [5, 6, 7, 8, 1, 2, 3, 4]]

        # Save settings
        self.filepath = r'filepath'
        self.name = 'name'
        self.configSrc = os.path.dirname(os.path.abspath(__file__))
        self.inputData = self.generateTriangle