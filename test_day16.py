import unittest

class Sue(object):
    def __init__(self,string=None,**kwargs):

        self.properties=dict()

        if string is not None:
            #parse string to create Sue
            nameString = string.split(":")[0]
            string = string.lstrip(nameString+":")
            self.properties['index'] = int(nameString.split(" ")[1])

            properties = string.split(",")
            for property in properties:
                key,val = property.split(":")
                self.properties[key.strip(" ")] = int(val)

            #overwrite with kwargs
            for key,val in kwargs.items():
                self.properties[key]=val

        else:
            #just construct with whatever data was passed through kwargs
            self.properties=kwargs

    def getAttribute(self,name):
        if name not in self.properties:
            return None
        else:
            return self.properties[name]

    def compare(self,otherSue):
        returnValue=True
        for attribute,value in self.properties.items():
            if otherSue.getAttribute(attribute) != value:
                if otherSue.getAttribute(attribute) is not None:
                    return False
        return True


class test_day16(unittest.TestCase):

    def setUp(self):
        self.testData = [line.strip("\n") for line in open("testData/sue")]

        self.realSue = Sue(children=3,
                           cats=7,
                           samoyeds=2,
                           pomeranians=3,
                           akitas=0,
                           vizslas=0,
                           goldfish=5,
                           trees=3,
                           cars=2,
                           perfumes=1)

    def getAttribute(self,sue,name):
        return sue.getAttribute(name)

    def sueWithNChildren(self,n):
        return Sue(children=n)

    def test_sue_has_a_child(self):
        sue=self.sueWithNChildren(1)
        self.assertEqual(1,self.getAttribute(sue,'children'))

    def test_sue_has_two_children(self):
        sue=self.sueWithNChildren(2)
        self.assertEqual(2,self.getAttribute(sue,'children'))

    def test_cannot_remember_if_sue_has_children(self):
        sue=Sue()
        self.assertEqual(None,self.getAttribute(sue,'children'))

    def test_can_create_sue_from_string_with_index(self):
        sueString=self.testData[0]
        self.assertEqual(1,self.getAttribute(Sue(sueString),'index'))

    def test_can_create_sue_from_string_with_goldfish(self):
        sueString=self.testData[0]
        self.assertEqual(9,self.getAttribute(Sue(sueString),'goldfish'))

    def test_can_create_sue_from_string_with_cars(self):
        sueString=self.testData[0]
        self.assertEqual(0,self.getAttribute(Sue(sueString),'cars'))

    def test_can_create_sue_from_string_with_trees(self):
        sueString=self.testData[0]
        self.assertEqual(None,self.getAttribute(Sue(sueString),'trees'))

    def test_compare_different_sues_returns_false(self):
        self.assertEqual(False,self.realSue.compare(Sue(self.testData[0])))

    def test_compare_same_sue_returns_true(self):
        self.assertEqual(True,self.realSue.compare(self.realSue))

    def test_can_overwrite_properties(self):
        self.assertEqual(None,Sue(self.testData[0],goldfish=None).getAttribute('goldfish'))

    def test_compare_same_sue_with_one_none(self):
        sue = self.realSue
        sue.properties['goldfish']=None
        self.assertEqual(True,self.realSue.compare(sue))

    def test_part1(self):
        matching=[]
        for test in self.testData:
            fakeSue=Sue(test)
            if self.realSue.compare(fakeSue):
                matching.append(fakeSue)

        self.assertEqual(len(matching),1)
        self.assertEqual(matching[0].getAttribute('index'),40)
