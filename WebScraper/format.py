class Format:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def printList(self):
        print(self.ingredients)

    def individualIngredients(self):
        wordArray = []
        for ingredient in self.ingredients:
            wordArray.append(self.parsedIngredient(ingredient))
        return wordArray
            
    def parsedIngredient(self, ingredient):
        if ',' in ingredient:
            commasplit = ingredient.split(',')
            lastword = commasplit[0].split(' ')
            return lastword[-1]
        else:
            return ingredient.split(' ')[-1]

