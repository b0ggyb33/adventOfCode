import unittest
import numpy as np
from algorithms import lightSwitcher,NordicLightSwitcher
class test_day6(unittest.TestCase):
    def setUp(self):
        self.lights = lightSwitcher()
        self.lights2 = NordicLightSwitcher()

    def test_noLightsOn(self):
        self.assertEqual(0,self.lights.sum())

    def test_nineLightsOn(self):
        self.lights.turnOn((0,0),(2,2))
        self.assertEqual(9,self.lights.sum())

    def test_nineLightsOff(self):
        self.lights.turnOn((0,0),(2,2))
        self.lights.turnOff((0,0),(2,2))
        self.assertEqual(0,self.lights.sum())

    def test_toggleLight(self):
        self.lights.lights = np.array(((0,1,0),
                                      (0,0,0),
                                      (1,1,1)))
        self.lights.toggle((0,0),(1,1))
        self.assertEqual(True,np.all(np.array(((1,0,0),
                                  (1,1,0),
                                  (1,1,1)))==self.lights.lights))

    def test_allOn(self):
        self.lights.turnOn((0,0),(999,999))
        self.assertEqual(1000000,self.lights.sum())

    def test_middleFourOff(self):
        self.lights.turnOn((0,0),(999,999))
        self.lights.turnOff((499,499),(500,500))
        self.assertEqual(0,self.lights.lights[499:501,499:501].sum())
        self.assertEqual(999996,self.lights.sum())

    def test_toggleFirstRow(self):
        self.lights.turnOn((0,0),(999,999))
        self.lights.toggle((0,0),(999,0))
        self.assertEqual(1000000-1000,self.lights.sum())
        self.assertEqual(0,self.lights.lights[:,0].sum())

    def getparseLineFun(self,line):
        self.lights.parseLine(line)

    def test_turnOnLightsCommand(self):
        line="turn on 0,0 through 999,999"
        self.getparseLineFun(line)
        self.assertEqual(1000000,self.lights.sum())

    def test_toggleCommand(self):
        line="toggle 0,0 through 999,0"
        self.getparseLineFun(line)
        self.assertEqual(1000,self.lights.sum())
        self.assertEqual(1000,self.lights.lights[:,0].sum())

    def test_turnOffCommand(self):
        line="turn off 499,499 through 500,500"
        self.getparseLineFun(line)
        self.assertEqual(0,self.lights.lights[499:501,499:501].sum())
        self.assertEqual(0,self.lights.sum())

    def test_lightCOmmands(self):
        for line in open("testData/lightCommands"):
            self.lights.parseLine(line)

        self.assertEqual(400410,self.lights.sum())

    def test_nordic_with0(self):
        self.assertEqual(0,self.lights2.sum())

    def test_nordicWithToggle(self):
        self.lights2.toggle((0,0),(999,999))
        self.assertEqual(2000000,self.lights2.sum())

    def test_nordicWithToggleAndoff(self):
        self.lights2.toggle((0,0),(999,999))
        self.lights2.turnOff((0,0),(999,999))
        self.assertEqual(1000000,self.lights2.sum())

    def test_nordicWithToggleAndoffAndOn(self):
        self.lights2.toggle((0,0),(999,999))
        self.lights2.turnOff((0,0),(999,999))
        self.lights2.turnOn((0,0),(999,999))
        self.assertEqual(2000000,self.lights2.sum())

    def test_datacannotgonegative(self):
        self.lights2.turnOn((500,500),(999,999))
        self.lights2.turnOff((0,0),(999,999))
        self.assertEqual(0,self.lights2.sum())

    def test_nordicWithtestData(self):
        for line in open("testData/lightCommands"):
            self.lights2.parseLine(line)

        self.assertEqual(15343601,self.lights2.sum())

