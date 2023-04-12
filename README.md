# nlp-analysis-imdb
## Descrição 

O objetivo do projeto foi realizar a extração de uma lista 
de reviews sobre o filme O Poderoso Chefão (1972) no site 
IMDB utilizando a técnica de raspagem de dados (biblioteca 
selenium e scrapy). Então, a lista de reviews foi processada 
e tratada, a fim de obtermos uma nuvem de palavras para evidenciar
a frequência dos termos utilizados pelos usuários.

## Web Scraping

Para a **extração de dados**, utilizaremos o site de reviews de filmes do IMDB (http://www.imdb.com/), que apresenta os comentários dos usuários e algumas descrições sobre os filmes.

Neste caso, olharemos apenas para as reviews de usuários do filme "O Poderoso Chefão".

Para a criação da nossa base de estudos, utilizaremos um DataFrame para explorar fazer o processamento e tratamento das reviews.

Nesta parte, utilizaremos as bibliotecas **Selenium** (driver), **Scrapy** (raspador) e **TQDM** (iterador dinâmico).

## Preparação de Dados

Como queremos criar uma nuvem de palavras traduzidas para o português, foi utilizada a biblioteca **deep_translator**, que se comunica com a API do Google Tradutor para realizar uma tradução automática.

Após criar uma coluna com as reviews traduzidas, foram removidas as reviews vazias e duplicadas do DataFrame.

## Processamento de Linguagem Natural

Inicialmente, cada palavra das reviews foi transformada em elementos mínimos através da técnica de tokenização,
sendo que, destes tokens, foram removidas as pontuações e os números de cada token.

Depois, para não impactar o resultado final da nossa núvem de palavras, foram removidas todas as stop words, ou seja, palavras 
que não trazem muita relevância para as nossas análises de texto, gerando inclusive ruídos que podem afetar os resultados finais.
Exemplo: conectivos, como "o", "a", "que", "de", etc... 

A partir disso foi gerado a núvem de palavras, sendo salva uma imagem para ser renderizada com as palavras mais frequêntes nas reviews.

## Núvem de Palavras

![Nuvem de Palavras](../../wbscp/analysis/../../GitHub/nlp-analysis-imdb/wbscp/analysis/nlp/N.png)