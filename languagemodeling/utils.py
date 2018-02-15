patterns = {
  'basic' : r'''(?x)    # set flag to allow verbose regexps
                (?:[A-Z]\.)+        # abbreviations, e.g. U.S.A.
              | \w+(?:-\w+)*        # words with optional internal hyphens
              | \$?\d+(?:\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
              | \.\.\.            # ellipsis
              | [][.,;"'?():-_`]  # these are separate tokens; includes ], [
            ''',
  'sofisticated' : r'''(?x)    # set flag to allow verbose regexps
                    (?:\d{1,3}(?:\.\d{3})+)  # numbers with '.' in the middle
                    | (?:[Ss]r\.|[Ss]ra\.|art\.)  # common spanish abbreviations
                    | (?:[A-Z]\.)+        # abbreviations, e.g. U.S.A.
                    | \w+(?:-\w+)*        # words with optional internal hyphens
                    | \$?\d+(?:\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
                    | \.\.\.            # ellipsis
                    | [][.,;"'?():-_`]  # these are separate tokens; includes ], [
                  '''
}