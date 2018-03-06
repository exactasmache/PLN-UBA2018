import os 
 
root_path = os.path.dirname( __file__ ) 
corpus_root = os.path.join(root_path, '../corpus')
 
corpus_folder_name = 'InterTASS_2017'
tweets_path = os.path.join(corpus_root, corpus_folder_name)

InterTASS_train_path = os.path.join(tweets_path, 'intertass-train-tagged.xml')
GeneralTASS_train_path = os.path.join(tweets_path, 'general-train-tagged.xml')
