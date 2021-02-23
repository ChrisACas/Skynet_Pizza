##Formats allrecipe.com recipe data

class Format:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    #testing: prints raw list 
    def printList(self):
        print(self.ingredients)

    #puts parsed words into ingredient array. 
    def individualIngredients(self):
        wordArray = []
        for ingredient in self.ingredients:
            wordArray.append(self.parsedIngredient(ingredient))
        return wordArray

    #parses individual word out of ingredient string       
    def parsedIngredient(self, ingredient):
        if ',' in ingredient:
            commasplit = ingredient.split(',')
            lastword = commasplit[0].split(' ')
            return lastword[-1]
        else:
            return ingredient.split(' ')[-1]

