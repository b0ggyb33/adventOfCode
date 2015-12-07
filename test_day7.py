import unittest
from algorithms import Wire,wireParse
class test_day7(unittest.TestCase):
    def test_wireholdsvalue(self):
        wire=Wire()
        self.assertEqual(0,wire)

    def test_canSetValue(self):
        wire=Wire(10)
        self.assertEqual(10,wire)

    def test_ANDwithtwowires(self):
        a=Wire(1)
        b=Wire(0)
        self.assertEqual(0,a & b)

    def test_ORwithTwowires(self):
        a=Wire(5)
        b=Wire(2)
        self.assertEqual(7,a | b)

    def test_NOT(self):
        a=Wire(5)
        self.assertEqual(65531, ~a)

    def test_Lshift(self):
        a=Wire(1)
        self.assertEqual(2,a<<1)

    def test_rshift(self):
        self.assertEqual(1,Wire(2)>>1)

    def test_naming(self):
        self.assertEqual("bob",str(Wire(0,"bob")))

    def test_123(self):
        self.assertEqual(Wire(123),wireParse("123 -> x",[]))

    def test_AND_instruction(self):
        x = Wire(2,"x")
        y = Wire(3,"y")
        wires=[x,y]
        self.assertEqual(2, wireParse("x AND y -> z",wires))