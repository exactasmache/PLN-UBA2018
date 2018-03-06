import os
from sentiment.tass import InterTASSReader, GeneralTASSReader

root_path = os.path.dirname(__file__)
corpus_root = os.path.join(root_path, '../corpus')

corpus_folder_name = 'InterTASS_2017'
tweets_path = os.path.join(corpus_root, corpus_folder_name)
graphs_path = os.path.join(root_path, 'graphs')

tweets = {
    'InterTASS': {
        'train': {
            'name': 'InterTASS Train Tweets',
            'path': os.path.join(tweets_path, 'intertass-train-tagged.xml')
        },
        'development': {
            'name': 'InterTASS Development Tweets',
            'path': os.path.join(tweets_path, 'intertass-development-tagged.xml')
        },
        'test': {
            'name': 'InterTASS Test Tweets',
            'path': os.path.join(tweets_path, 'intertass-test.xml'),
            'res_path': os.path.join(tweets_path, 'intertass-sentiment.qrel')
        },
        'reader': InterTASSReader
    },
    'GeneralTASS': {
        'train': {
            'name': 'GeneralTASS Train Tweets',
            'path': os.path.join(tweets_path, 'general-train-tagged.xml')
        },
        'reader': GeneralTASSReader
    }
}
