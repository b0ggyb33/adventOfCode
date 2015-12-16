__author__ = 'b0ggyb33'

class Recipe:
    def __init__(self,listOfIngredients):
        self.ingredients = listOfIngredients
        self.teaspoonsLeft=100
    def produceMixture(self):
        mixture=[]
        for ingredient in self.ingredients:
            mixture.append((ingredient.name(),self.teaspoonsLeft))
            if self.teaspoonsLeft>0:
                self.teaspoonsLeft=0


        return mixture
    def get(self):
        return 100*100*100*100,self.produceMixture()

class Ingredient:
    pass
