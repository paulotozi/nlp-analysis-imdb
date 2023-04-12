import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm
from scrapy.selector import Selector
import pandas as pd
import numpy as np
from deep_translator import GoogleTranslator


url = "https://www.imdb.com/title/tt0068646/reviews?ref_=tt_urv"

res = requests.get(url)

soup = BeautifulSoup(res.content, "html.parser")

reviews = soup.find_all("div", {"class" : ["lister-item mode-detail imdb-user-review collapsable"]})

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get(url)

num_reviews = 1000

qtd_vezes_botao = int(num_reviews / 25) - 1

for i in tqdm(range(qtd_vezes_botao)):

    try:
        seletor_css = "load-more-trigger"
        driver.find_element(By.ID, seletor_css).click()

    except:
        pass

review_list = []
error_url_list = []
error_msg_list = []
reviews = driver.find_elements(By.CSS_SELECTOR, 'div.review-container')

for text_review in tqdm(reviews):
    try:
        selector_scrapy = Selector(text = text_review.get_attribute('innerHTML'))
        try:
            review = selector_scrapy.css('.text.show-more__control::text').extract_first()
        except:
            review = np.NaN

        review_list.append(review)
    except Exception as e:
        error_url_list.append(url)
        error_msg_list.append(e)
review_df = pd.DataFrame({
    'review_en':review_list
    })           

review_df["review_pt"] = np.NaN

for index,row in review_df.iterrows():

    if len(row["review_en"]) <= 5000:

        review_df["review_pt"].loc[index] = GoogleTranslator(source = "auto", target = 'pt').translate(row["review_en"])

review_df.to_csv('test.csv')