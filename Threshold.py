import ScorerFileManager

class Threshold:
    def __init__(self):
        self.sfm = ScorerFileManager.ScorerFileManager()
        self.dictionary_text = self.sfm.get_out_cran_eng_stop_text_bm25()
        self.dictionary_title = self.sfm.get_out_cran_eng_stop_title_bm25()

    def list_to_dictionary(self, list):
        dictionary = {}
        if list is not None:
            for value in list:
                dictionary[value[0]] = value[1]
        return dictionary

    def threshold_algorithm(self, query_id, k):

        #[(doc_id,score)...(x,y)]
        values_text = self.dictionary_text.get(query_id)
        values_title = self.dictionary_title.get(query_id)

        #{doc_id: score, ..., x:y}
        dictionary_text = self.list_to_dictionary(values_text)
        dictionary_title = self.list_to_dictionary(values_title)

        memory = []

        dictionary_final = {}
        i = 0
        threshold = float(values_text[i][1]) + float(values_title[i][1])
        min_threshold = 0

        while (min_threshold < threshold):

            item_title = values_title[i][0]
            item_text = values_text[i][0]

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


            #I have the same item in the same row
            if item_title == item_text:
                if [(item_text, item_text_score)] not in memory:
                    memory.append([item_text,item_text_score])

            #I have two different Items
            else:
                #item1 not in memory -> append
                if [(item_title, item_title_score)] not in memory:
                    memory.append([item_title, item_title_score])

                #the same for item2
                if [(item_text, item_text_score)] not in memory:
                    memory.append([item_text, item_text_score])


            memory = sorted(memory, key=lambda x: x[1],reverse=True)
            threshold = float(values_text[i+1][1]) + float(values_title[i+1][1])


            min_threshold = self.getKth(memory, k)
            i = i + 1
        return self.firstKlist(memory, k)

    def getKth(self, list, k):
        if len(list) < k :
            return 0
        else:
            return list[k-1][1]

    def firstKlist(self, list, k):
        output= []
        i = 0
        while (i<k):
            output.append(list[i])
            i = i+1
        return output

    def sort_dictionary(self, dictionary):
        list = []
        for key in dictionary.items():
            temp = dictionary.get(key)
            list.append(key)
        return sorted(list, key=lambda x: x[1],reverse=True)

