import logging

import pandas as pd


def start_verify_scraped_data(df: pd.DataFrame, budget: float):
    # Call the necessary functions to verify scraped data
    logging.basicConfig(level=logging.INFO)
    if not all(list(map(classify_search_category, list(df['Category'])))):
        logging.info(f'search category is not valid')
    if not all(list(map(validation_acc, list(df['Year'])))):
        logging.info(f'There is invalid year data.')
    if not all(list(map(cost_compare, list(df['Cost']), [budget] * df.shape[0])))):
        logging.info(f'There is cost data higher than our budget.')

    if __name__ == '__main__':
        logging.basicConfig(level=logging.DEBUG, filename='debug.log', filemode='w')
    budget = 2000.00
    scraped_data = pd.read_csv('scraped_data.csv', index_col=False, header=0)
    start_verify_scraped_data(scraped_data, budget=budget)


def start_verify_scraped_data(df: pd.DataFrame, budget: float):
    # Call the necessary functions to verify scraped data
    logging.basicConfig(level=logging.INFO)
    if not all(list(map(classify_search_category, list(df['Category'])))):
        logging.info(f'search category is not valid')
    if not all(list(map(validation_acc, list(df['Year'])))):
        logging.info(f'There is invalid year data.')
    if not all(list(map(cost_compare, list(df['Cost']), [budget] * df.shape[0])))):
        logging.info(f'There is cost data higher than our budget.')

    if __name__ == '__main__':
        logging.basicConfig(level=logging.DEBUG, filename='debug.log', filemode='w')
    budget = 2000.00
    scraped_data = pd.read_csv('scraped_data.csv', index_col=False, header=0)
    start_verify_scraped_data(scraped_data, budget=budget)
