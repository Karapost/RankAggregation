import ScorerFileManager
import operator

class Threshold:
    def __init__(self):
        self.sfm = ScorerFileManager.ScorerFileManager()
        self.dictionary_text_query = self.sfm.get_out_cran_eng_stop_text_bm25()
        self.dictionary_title_query = self.sfm.get_out_cran_eng_stop_title_bm25()

    def threshold_algorithm(self, query_id, k):

        dictionary_title = self.dictionary_title_query.get(str(query_id))  # Dictionary
        dictionary_text = self.dictionary_text_query.get(str(query_id))  # Dictionary

        iterator_title = iter(dictionary_title.keys())  # Iterator on keys
        iterator_text = iter(dictionary_text.keys())  # Iterator on keys

        iterator_title_threshold =  iter(dictionary_title.keys())
        iterator_text_threshold = iter(dictionary_text.keys())

        memory = {}

        threshold = float(dictionary_title.get(next(iterator_title_threshold))) + float(dictionary_text.get(next(iterator_text_threshold)))
        i = 0
        min_threshold = 0

        while (min_threshold < threshold and i<199 ):

            item_title = next(iterator_title)
            item_text = next(iterator_text)

            #Case if the item is only in dictionary for item_title
            if dictionary_title.get(item_title) is None:
                item_title_score = 0.0 + float(dictionary_text.get(item_title))

            elif dictionary_text.get(item_title) is None:
                    item_title_score = float(dictionary_title.get(item_title)) + 0.0
            else:
                item_title_score = float(dictionary_title.get(item_title)) + float(dictionary_text.get(item_title))

            # Case if the item is only in dictionary for item_text
            if dictionary_title.get(item_text) is None:
                item_text_score = 0.0 + float(dictionary_text.get(item_text))

            elif dictionary_text.get(item_text) is None:
                item_text_score = float(dictionary_title.get(item_text)) + 0.0
            else:
                item_text_score = float(dictionary_text.get(item_text)) + float(dictionary_title.get(item_text))

            #If the items are the same, the second if will find that it is in memory
            if item_title not in memory:
                memory[item_title] = item_title_score

            if item_text not in memory:
                memory[item_text] = item_text_score

            list_temp = sorted(memory.items(), key=operator.itemgetter(1), reverse=True)
            threshold = float(dictionary_title.get(next(iterator_title_threshold))) + float(dictionary_text.get(next(iterator_text_threshold)))
            min_threshold = self.getKth(list_temp, k)
            i = i + 1

        return self.firstKlist(list_temp, k)

    def getKth(self, list, k):
        if len(list) < k :
            return 0
        else:
            return list[k-1][1]

    def firstKlist(self, list, k):
        output = []
        i = 0
        while (i < k):
            output.append(list[i])
            i = i + 1
        return output


