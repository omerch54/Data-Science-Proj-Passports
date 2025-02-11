# websites to scrape:
# https://en.wikipedia.org/wiki/Henley_Passport_Index -> passport index
# https://www.datapandas.org/ranking/education-rankings-by-country#full-data -> education rankings
# https://en.wikipedia.org/wiki/List_of_countries_by_exports -> exports
# https://en.wikipedia.org/wiki/List_of_countries_by_imports -> imports
# csv available
# https://worldpopulationreview.com/country-rankings/average-iq-by-country -> average IQ
# https://worldpopulationreview.com/country-rankings/literacy-rate-by-country -> literacy rate
# https://data.worldbank.org/indicator/NY.GDP.PCAP.CD -> GDP per capita

import os
import time
import requests
import re

import numpy as np
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# global urls
PASSPORT_INDEX_URL = "https://en.wikipedia.org/wiki/Henley_Passport_Index"
EDUCATION_RANKINGS_URL = "https://www.datapandas.org/ranking/education-rankings-by-country"
EXPORTS_URL = "https://en.wikipedia.org/wiki/List_of_countries_by_exports"
IMPORTS_URL = "https://en.wikipedia.org/wiki/List_of_countries_by_imports"


# class to scrape data from the web
class ScraperABC:

    def __init__(self, url, save_path):
        self.url = url
        self.data = None
        self.save_path = save_path

    def scrape(self):
        # scrape data
        response = requests.get(self.url)
        assert response.status_code == 200
        soup = BeautifulSoup(response.content, 'html.parser')
        self._scrape_logic(soup)

    def _scrape_logic(self, content):
        # scrape data abstract method
        pass

    def save(self):
        # save data
        assert self.save_path is not None
        os.makedirs(os.path.dirname(self.save_path), exist_ok=True)
        self.data.to_csv(self.save_path, index=False)

    def load(self):
        # load data
        self.data = pd.read_csv(self.save_path)


# class to scrape data from wikipedia passport index
class PassportIndexScraper(ScraperABC):
    def __init__(self, url, save_path):
        super().__init__(url, save_path)

    def _scrape_logic(self, content):
        # tables for years 2022, 2023, 2024
        tables = content.find_all('table', class_='wikitable')
        rows = [t.find_all('tr') for t in tables[:3]]

        # get data from tables
        data = []
        # hard coded due to inconsistent table structure and edge cases
        col_names = ["Rank", "Passport Issuing Country", "Number of Visa-Free Destinations"]
        for i, table in enumerate(rows):
            prev_rank = None
            curr_year_data = []
            curr_year = 2022 + i
            for j, row in enumerate(table[1:]):
                cols = row.find_all('td')
                if len(cols) < 3:
                    cols = [prev_rank] + cols
                else:
                    prev_rank = cols[0]
                cols = [ele.text.strip() for ele in cols]
                curr_year_data.append({col_names[k]: cols[k] for k in range(len(cols))})
                curr_year_data[-1]["Year"] = curr_year
            data.extend(curr_year_data)

        self.data = pd.DataFrame(data)


# class to scrape data from datapandas education rankings 2022
class EducationRankingsScraper(ScraperABC):
    def __init__(self, url, save_path):
        super().__init__(url, save_path)
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = None

    def _scrape_logic(self, content):
        # content not loaded initially
        table = content.find('table', id='full_data_table')
        rows = table.find_all('tr')
        assert len(rows) < 1
        # dynamic table
        try:
            self.driver = webdriver.Chrome(options=self.options)
            self.driver.get(self.url)
            wait = WebDriverWait(self.driver, 5)
            _ = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "table_body")))
            table = self.driver.find_element(By.ID, "full_data_table")
            rows = table.find_elements(By.TAG_NAME, "tr")

            data = []
            col_names = [row.text for row in rows[0].find_elements(By.TAG_NAME, "th")]
            for row in rows[1:]:
                cols = row.find_elements(By.TAG_NAME, "td")
                cols = [ele.text.strip() for ele in cols]
                data.append({col_names[k]: cols[k] for k in range(len(cols))})

            self.data = pd.DataFrame(data)
        finally:
            if self.driver is not None:
                self.driver.quit()


# class to scrape data from wikipedia exports
class ExportsScraper(ScraperABC):
    def __init__(self, url, save_path):
        super().__init__(url, save_path)

    def _scrape_logic(self, content):
        table = content.find('table', class_='wikitable')
        rows = table.find_all('tr')

        data = []
        col_names = [row.text.strip().split('[')[0].split('\n')[0] for row in rows[0].find_all('th')]
        for row in rows[1:]:
            cols = row.find_all('td')
            cols = [ele.text.strip().split('[')[0] for ele in cols]
            data.append({col_names[k]: cols[k] for k in range(len(cols))})

        self.data = pd.DataFrame(data)


# class to scrape data from wikipedia imports
class ImportsScraper(ExportsScraper):
    def __init__(self, url, save_path):
        super().__init__(url, save_path)

    def _scrape_logic(self, content):
        super()._scrape_logic(content)


# class to scrape data from world bank GDP per capita
class GDPPerCapitaScraper(ScraperABC):
    def __init__(self, save_path):
        super().__init__(url=None, save_path=save_path)

    def _scrape_logic(self, content):
        raise Exception("Load downloaded csv instead of scraping")


# class to scrape data from world population review average IQ
class AverageIQScraper(ScraperABC):
    def __init__(self, save_path):
        super().__init__(url=None, save_path=save_path)

    def _scrape_logic(self, content):
        raise Exception("Load downloaded csv instead of scraping")


# class to scrape data from wikipedia literacy rate
class LiteracyRateScraper(ScraperABC):
    def __init__(self, save_path):
        super().__init__(url=None, save_path=save_path)

    def _scrape_logic(self, content):
        raise Exception("Load downloaded csv instead of scraping")
