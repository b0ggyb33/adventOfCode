import unittest

class Elf(object):
    def __init__(self,number):
        self.number=number
    def deliversToHouse(self,number):
        if 0==number%self.number:
            return True
        else:
            return False


class houseDeliveryManager(object):
    def __init__(self):
        self.elves={1:Elf(1)}
        self.house=0

    def addExtraElves(self,newMaximum):
        #elfNumbers= [elf.number for elf in self.elves]
        for elfNumber in range(len(self.elves),newMaximum+1):
            if elfNumber not in self.elves.keys():
                self.elves[elfNumber]=Elf(elfNumber)

    def deliver(self,house):
        if house>len(self.elves):
            self.addExtraElves(house)
        presents=0
        for elf in self.elves.values():
            if elf.deliversToHouse(house):
                presents += 10 * elf.number
        return presents

    def deliverToNextHouse(self):
        self.house+=1
        return self.deliver(self.house)

    def solve(self,puzzleInput):
        presents=0
        while presents<puzzleInput:
            presents=self.deliverToNextHouse()
            if self.house==puzzleInput:
                return self.house
        return self.house

class test_day20(unittest.TestCase):

    def setUp(self):
        self.puzzleInput = 36000000
        self.hdm = houseDeliveryManager()

    def houseDeliverer(self,number,elves):
        hdm=houseDeliveryManager()
        hdm.elves=elves
        return hdm.deliver(number)

    def test_elfOneDeliversToFirstHouse(self):
        elf = {1:Elf(1)}
        self.assertEqual(10,self.houseDeliverer(1,elf))

    def test_elfTwoDeliversToHouse4(self):
        elf={2:Elf(2)}
        self.assertEqual(10+20+40,self.houseDeliverer(4,elf))

    def test_elfOneDeliversToHouse3(self):
        elf={1:Elf(1)}
        self.assertEqual(40,self.houseDeliverer(3,elf))

    def test_OneElfDeliversToHouse1(self):
        elf={1:Elf(1)}
        self.assertEqual(10,self.houseDeliverer(1,elf))

    def test_ElfTwoDoesntDeliverToHouse1(self):
        elf={2:Elf(2)}
        self.assertEqual(0,self.houseDeliverer(1,elf))

    def test_firstTwoElvesDeliverToHouse2(self):
        elves={1:Elf(1),2:Elf(2)}
        self.assertEqual(30,self.houseDeliverer(2,elves))

    def hdmDoesNotMakeAZeroElf(self):
        hdm = houseDeliveryManager()
        hdm.addExtraElves(1)
        self.assertEqual(1,len(hdm.elves))
        self.assertEqual(1,hdm.elves[0].number)

    def test_houseDeliverManagerReturns30OnHouse2(self):
        hdm=houseDeliveryManager()
        self.assertEqual(30,hdm.deliver(2))

    def test_hdmHouse8Returns150(self):
        self.assertEqual(150,self.hdm.deliver(8))

    def test_successiveDelivers(self):
        self.assertEqual(10,self.hdm.deliverToNextHouse())
        self.assertEqual(30,self.hdm.deliverToNextHouse())
        self.assertEqual(2,self.hdm.house)

    def test_hdm_deliverer_returns_3_with_puzzleInputOf40(self):
        self.assertEqual(self.hdm.solve(40),3)

    def test_hdm_returns_8_with_input_of_150(self):
        self.assertEqual(self.hdm.solve(150),8)

    def hdm_part1(self):
        print self.hdm.solve(self.puzzleInput)


