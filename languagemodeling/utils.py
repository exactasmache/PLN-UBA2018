from collections import Counter

patterns = {
    'basic': r'''(?x)    # set flag to allow verbose regexps
                (?:[A-Z]\.)+        # abbreviations, e.g. U.S.A.
              | \w+(?:-\w+)*        # words with optional internal hyphens
              | \$?\d+(?:\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
              | \.\.\.            # ellipsis
              | [][.,;"'?():-_`]  # these are separate tokens; includes ], [
            ''',
    'sofisticated': r'''(?x)    # set flag to allow verbose regexps
                    (?:\d{1,3}(?:\.\d{3})+)  # numbers with '.' in the middle
                    | (?:[Ss]r\.|[Ss]ra\.|art\.)  # common spanish abbreviations
                    | (?:[A-Z]\.)+        # abbreviations, e.g. U.S.A.
                    | \w+(?:-\w+)*        # words with optional internal hyphens
                    | \$?\d+(?:\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
                    | \.\.\.            # ellipsis
                    | [][.,;"'?():-_`]  # these are separate tokens; includes ], [
                  '''
}


def show_basic_statistics(sents):
    """
        Prints in order to manually find tokenizations differences
        sents -- list of sentences, each one being a list of tokens.
    """
    count = Counter()
    for sent in sents:
        count.update(sent)

    # print the 20's firsts sentences in order to check the tokenization
    for s in sents[:20]:
        print(s)

    print('10 palabras mas frecuentes:')
    for w, a in count.most_common()[:10]:
        print(w, '\t:\t', a)
    print('Vocabulario:', len(count))
    print('Tokens:', sum(count.values()))
    print('Porcentaje de diversidad: {0:.2f}'.format(
        100*len(count)/sum(count.values())))
    return
