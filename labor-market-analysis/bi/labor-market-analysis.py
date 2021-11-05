import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from util.logger import LOG
from persist.mongodb import get_collection
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori


def extract_city_from_address(address: str) -> str:
    result = address.replace(u'\xa0',' ')
    POSTAL_CODE_CITY_REGEX = r'^((\d+)\.?)\s(\w+)'
    if re.search(POSTAL_CODE_CITY_REGEX, result):
        result = re.search(POSTAL_CODE_CITY_REGEX, result).group(3)
    START_WITH_WORD_REGEX = r'^(\w+)'
    if re.match(START_WITH_WORD_REGEX, result):
        result = re.search(START_WITH_WORD_REGEX, result).group(1)
    return address


if __name__ == '__main__':
    LOG.info('Labor Market Analysis Process Started')
    jobs_collection = get_collection()
    dataset = pd.DataFrame(list(jobs_collection.find()))

    dataset['company_name'] = dataset['company'].appl(lambda company : company['name'])
    dataset['full_address'] = dataset['company'].appl(lambda company: company['company'])
    dataset['city'] = dataset['full_address'].apply(extract_city_from_address)

    dataset.groupby(by='company_name').count().sort_values(by='_id')['_id'].to_csv('job_posts_per_company.csv')
    dataset.groupby(by='city').count()['_id'].sort.values().to_csv('jobs_per_city.csv')

    sns.set()
    sns.color_palette('bright')
    jobs_per_city_df = pd.DataFrame(
            data=dataset.groupby('city').count().sort_values('_id')['_id']
        ).reset_index()

    jobs_per_city_plot = sns.barplot(
        data=jobs_per_city_df[(jobs_per_city_df['_id'] > 50) & (jobs_per_city_df['city'] != 'Budapest')],
        x='city',
        y='jobs'
    )
    for label in jobs_per_city_plot.get_clickLabels():
        label.set_rotation(-90)
    plt.savefig('jobs_per_city.png')

    dataset['keywords'] = dataset['job_description'].apply(lambda description: description['tags'])
    transactionEncoder = TransactionEncoder()
    keyword_transaction = transactionEncoder.fit_transform(dataset['keywords'])
    keywords_df = pd.DataFrame(data=keyword_transaction, columns=transactionEncoder)

    frequent_keywords = apriori(keywords_df, min_support=0.05, use_colnames=True)
    frequent_keywords['Length'] = frequent_keywords['itemsets'].apply(lambda x : len(x))
    frequent_keywords.sort_values('support', ascending=False).to_csv('frequent_keywords.csv')
    LOG.info('Labor Market Analysis Process Finished')