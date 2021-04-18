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
# manages dictionaries
from operator import itemgetter


nltk.download('stopwords')
data= pd.DataFrame()
data = pd.read_csv(r'/Users/engrbundle/Documents/ECEN 404/Skynet_Pizza/recipe_output_latest.csv', encoding='utf-8')

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
#  print('Recipes: %d' % len(review_data_list))


Embedding_Dim = 100
#train word2vec model
model = gensim.models.Word2Vec(sentences = review_data_list, size = Embedding_Dim, workers = 4, min_count = 1)
#Vocabulary size
words = list(model.wv.vocab)
#  print('Ingredients: %d' % len(words))


#------------------------------
#RECOMMENDATION SYSTEM CODE:


# Gather 3 core ingredients inputs and num of outputs
ingredient_list = list(sys.argv[1].split(" "))
crust_type = ingredient_list[0]
cheese_type = ingredient_list[1]
sauce_type = ingredient_list[2]
topping_num = int(sys.argv[2])

# Type cast to dictionary before only getting desired number of toppings 
ingredients = dict(model.wv.most_similar(crust_type))
n_ingredients = dict(sorted(ingredients.items(), key = itemgetter(1), reverse = True)[:topping_num])

# print n num of dict items sorted from high to low
for key, value in n_ingredients.items():
    print(key, value)
    
# Print entire dictionary
# for key, value in ingredients.items():
#     print(key, value)
    

exit()

