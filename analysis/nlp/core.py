import nltk
from nltk.tokenize import word_tokenize
from processing import processar_dados
import string
import re
from nltk import corpus
from matplotlib import pyplot
from wordcloud import WordCloud

nltk.download('punkt')
nltk.download('stopwords')
stop_words = corpus.stopwords.words("portuguese")

df = processar_dados()

tds_as_plvrs = []

for index in df.index:

    tokens = word_tokenize(df["review_pt_processado"][index])

    tds_as_plvrs.extend(tokens)

tds_as_plvrs_s_pont = [''.join(c for c in s if c not in string.punctuation) for s in tds_as_plvrs]
tds_as_plvrs_s_num = []

for palavra in tds_as_plvrs_s_pont:

    if not re.search("[0-9]", palavra):

        tds_as_plvrs_s_num.append(palavra)

tds_as_plvrs_s_stopwords = []

for palavra in tds_as_plvrs_s_num:

    if palavra in stop_words:

        pass

    else:

        tds_as_plvrs_s_stopwords.append(palavra)

tds_as_palavras_processadas = [x for x in tds_as_plvrs_s_stopwords if x != '']

tds_as_palavras_final = ' '.join(map(str, tds_as_palavras_processadas))

nuvem_de_palavras = WordCloud(width = 800, height = 500, max_font_size = 110, collocations = False).generate(tds_as_palavras_final)
nuvem_de_palavras.to_file('N.png')