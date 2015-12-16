import unittest
import mock
import numpy as np
from day15 import Recipe,Ingredient
class test_recipe_optimiser(unittest.TestCase):

    """
    def test_fakeIngredientsCanProduceDataPoint(self):


        Recipe.get=mock.MagicMock(return_value=62842880)

        recipeCurve=[(Recipe.get(44,56),44,56),(60000000,44,47)]

        self.assertEqual((Recipe.get(44,56),44,56),max(recipeCurve))

    def getAnIngredient(self):
        ingredient = Ingredient()
        ingredient.properties = mock.MagicMock(return_value={'capacity':1,'durability':1, 'flavor':1, 'texture':1, 'calories':1})
        ingredient.name = mock.MagicMock(return_value="cinnamon")
        return ingredient

    def test_recipe_produces_something_with_one_ingredient(self):
        ingredient = self.getAnIngredient()
        recipe = Recipe([ingredient])
        self.assertEqual((100*100*100*100,{'cinnamon':100}),recipe.get())

    def test_recipe_produces_something_with_one_ingredient_with_new_values(self):
        ingredient = self.getAnIngredient()
        recipe = Recipe([ingredient])
        self.assertEqual((200*100*100*100,{'cinnamon':100}),recipe.get())



    def test_recipe_produces_something_with_two_ingredients(self):
        ingredient = self.getAnIngredient()
        recipe=Recipe([ingredient,ingredient])
        self.assertEqual((100*100*100*100,{'cinnamon':100,'cardamom':0}),recipe.get())

    """
    def setUp(self):
        self.butterscotch={'capacity':-1,'durability':-2, 'flavor':6, 'texture':3, 'calories':8}
        self.cinnamon={'capacity':2,'durability':3, 'flavor':-2, 'texture':-1, 'calories':3}
        self.fakeIngredient = {'capacity':2,'durability':3, 'flavor':2, 'texture':1, 'calories':3}

        self.sugar = {'capacity': 3, 'durability': 0, 'flavor': 0, 'texture': -3, 'calories': 2}
        self.sprinkles = {'capacity': -3, 'durability': 3, 'flavor': 0, 'texture': 0, 'calories': 9}
        self.candy = {'capacity': -1, 'durability': 0, 'flavor': 4, 'texture': 0, 'calories': 1}
        self.chocolate = {'capacity': 0, 'durability': 0, 'flavor': -2, 'texture': 2, 'calories': 8}

        self.testData = [self.sugar,self.sprinkles,self.candy,self.chocolate]

    def recipeScorer(self,ingredients):
        ingredient_scores = {'capacity':0,'durability':0, 'flavor':0, 'texture':0, 'calories':0}
        for ingredient,quantity in ingredients:
            for score in ingredient_scores.keys():
                ingredient_scores[score] += ingredient[score]*quantity
        product=1
        for score,value in ingredient_scores.items():
            if score == 'calories':
                if value != 500:
                    value=0
                else:
                    value=1
            else:
                if value<0:
                    value = 0
            product*=value
        return product

    def test_score_of_100tsps_butterscotch(self):
        self.assertEqual(0,self.recipeScorer([(self.butterscotch,100)]))

    def test_score_of_99tsps_butterscotch_one_cinnamon(self):
        self.assertEqual(0,self.recipeScorer([(self.butterscotch,99),(self.cinnamon,1)]))

    def test_score_of_100tsps_fake_ingredient(self):
        self.assertEqual(2*100*3*100*2*100*100,self.recipeScorer([(self.fakeIngredient,100)]))

    def test_score_of_99tsps_fake_and_one_fake_with_no_flavor(self):
        fakeIngredient = {'capacity':2,'durability':3, 'flavor':0, 'texture':1, 'calories':3}
        self.assertEqual(200*300*100*(99*2+0),self.recipeScorer([(self.fakeIngredient,99),(fakeIngredient,1)]))

    def test_score_of51tsps_fake_49tsps_cinnamon_isPositive(self):
        self.assertGreater(self.recipeScorer([(self.fakeIngredient,51),(self.cinnamon,49)]),0)

    def test_score_of49tsps_fake_51tsps_cinnamon_isZero(self):
        self.assertEqual(self.recipeScorer([(self.fakeIngredient,49),(self.cinnamon,51)]),0)

    def test_44_butterscotch_56_cinnamon(self):
        self.assertEqual(62842880,self.recipeScorer([(self.butterscotch,44),(self.cinnamon,56)]))

    def test_brute_force(self):
        score=0
        for x in range(100,0,-1):
            y=100-x
            localScore = self.recipeScorer([(self.butterscotch,x),(self.cinnamon,y)])
            if localScore>score:
                score=localScore
        self.assertEqual(62842880,score)

    def test_answer_part1(self):
        score=0
        for x in range(100):
            for y in range(100-x):
                for z in range(100-x-y):
                    a=100-x-y-z
                    localScore = self.recipeScorer([(self.testData[0],x),(self.testData[1],y),(self.testData[2],z),(self.testData[3],a)])
                    if localScore>score:
                        score=localScore

        self.assertEqual(score,222870)