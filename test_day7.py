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
        self.assertEqual(65530, ~a)

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
        wires={"x":x,"y":y}
        z = wireParse("x AND y -> z",wires)
        self.assertEqual(2,z)
        self.assertEqual("z",str(z))

    def test_NOT_instruction(self):
        e = Wire(3,"e")
        wires={"e":e}
        f=wireParse("NOT e -> f",wires)
        self.assertEqual(65532, f)
        self.assertEqual("f",str(f))

    def test_RSHIFT(self):
        y = Wire(8,"y")
        wires={"y":y}
        g=wireParse("y RSHIFT 2 -> g",wires)
        self.assertEqual(2,g)
        self.assertEqual("g",str(g))

    def test_LSHIFT(self):
        y = Wire(2,"y")
        wires={"y":y}
        g=wireParse("y LSHIFT 2 -> g",wires)
        self.assertEqual(8,g)
        self.assertEqual("g",str(g))

    def test_Assignment(self):
        lx = Wire(10,"lx")
        newWire=wireParse("lx -> a",{"lx":lx})
        self.assertEqual(str(newWire),"a")
        self.assertEqual(newWire,10)

    def test_sample(self):
        samples=["123 -> x\n",
                 "456 -> y\n",
                 "x AND y -> d\n",
                 "x OR y -> e\n",
                 "x LSHIFT 2 -> f\n",
                 "y RSHIFT 2 -> g\n",
                 "NOT x -> h\n",
                 "NOT y -> i"]

        wireList={}
        for sample in samples:
            newWire=wireParse(sample.strip("\n"),wireList)
            if newWire not in wireList:
                wireList[newWire.name]=newWire

        self.assertEqual(72,wireList["d"])
        self.assertEqual(507,wireList["e"])
        self.assertEqual(492,wireList["f"])
        self.assertEqual(114,wireList["g"])
        self.assertEqual(65412,wireList["h"])
        self.assertEqual(65079,wireList["i"])
        self.assertEqual(123,wireList["x"])
        self.assertEqual(456,wireList["y"])
