import csv
import pandas as pd
import nltk
import gensim
import sys
from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
import string
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


nltk.download('stopwords')
data= pd.DataFrame()
data = pd.read_csv(r'/Users/engrbundle/Documents/ECEN 404/Skynet_Pizza/recipe_output_correct.csv', encoding='utf-8')

#create empty list
review_data_list = list()

indv_lines = data['Removed amounts and measurements'].values.tolist()

for line in indv_lines:

	#create word tokens as well as remove punctuation in one go
	rem_tok_punc = RegexpTokenizer(r'\w+')
	#rem_spc = line.replace("","_")
	tokens = rem_tok_punc.tokenize(line)

    
	#convert the words to lower case
	words = [w.lower() for w in tokens]

	#Invoke all the english stopwords
	stop_word_list = set(stopwords.words('english'))

	#Remove stop words
	words = [w for w in words if not w in stop_word_list]

	#Append words in the review_data_list list.
	review_data_list.append(words)

#Amount of recipes in the list
print('Amount of recipes: %d' % len(review_data_list)) 

Embedding_Dim = 100
#train word2vec model
model = gensim.models.Word2Vec(sentences = review_data_list, size = Embedding_Dim, workers = 4, min_count = 1)
#Vocabulary size
words = list(model.wv.vocab)
print('Amount of ingredients: %d' % len(words))



#------------------------------
#RECOMMENDATION SYSTEM CODE:


ingredient1 = sys.argv[1]
print(f"Ingredients similar too {ingredient1}")
print(str(model.wv.most_similar(ingredient1)))
exit()

ingredient2= input("Which ingredient would you like to add to the pizza?")
decision1= input(f"Your current pizza consists of {ingredient1} and {ingredient2} , would you like us to search for another similar ingredient that would go well with this current pizza? Type yes or no" )
print('-------------------------------------------------------------------------------')
if decision1 == "no" :
    print('Your finalized pizza has %s and %s' % (ingredient1,ingredient2))
elif decision1 == "yes" :
    print(f"Here are the results of similar ingredients recommended for your pizza:     {model.wv.most_similar(ingredient2)}")
    ingredient3= input("Which ingredient would you like to add to the pizza?")
    print("--------------------------------------------------------------------------------------------------")
    decision2= input(f"Your current pizza consists of {ingredient1},{ingredient2}, and {ingredient3}. Would you like us to search for another similar ingredient that would go well with this current pizza? Type yes or no " )
else:
    print("Thank you for choosing Skynet Pizzeria, have a great day")

if decision2 == "no" :
    print('Your finalized pizza has %s , %s , and %s' % (ingredient1,ingredient2,ingredient3))
elif decision2 == "yes" :
    print(f"Here are the results of similar ingredients recommended for your pizza:     {model.wv.most_similar(ingredient3)}")
    ingredient4= input("Which ingredient would you like to add to the pizza?")
    print("--------------------------------------------------------------------------------------------------")
    decision3= input(f"Your current pizza consists of {ingredient1},{ingredient2},{ingredient3}, and {ingredient4}. Would you like us to search for another similar ingredient that would go well with this current pizza? Type yes or no (NOTE: You are limited to ONE more topping) " )
else:
    print("Thank you for choosing Skynet Pizzeria, have a great day")

if decision3 == "no" :
    print('Your finalized pizza has %s , %s , and %s' % (ingredient1,ingredient2,ingredient3))
elif decision3 == "yes" :
    print(f"Here are the results of similar ingredients recommended for your pizza:     {model.wv.most_similar(ingredient4)}")
    ingredient5= input("Which ingredient would you like to add to the pizza?")
    print("--------------------------------------------------------------------------------------------------")
    print(f"Your final pizza consists of {ingredient1},{ingredient2},{ingredient3},{ingredient4}, and {ingredient5}. Thank you for choosing Skynet Pizzeria, we hope you enjoy your custom pizza!")
else:
    print("Thank you for choosing Skynet Pizzeria, have a great day")


