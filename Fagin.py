import ScorerFileManager

class Fagin:
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

    def fagin_algorithm(self, query_id, k):
        values_text = self.dictionary_text.get(query_id)
        values_title = self.dictionary_title.get(query_id)
        dictionary_text_final = self.list_to_dictionary(values_text)
        print(values_text)
        dictionary_title_final = self.list_to_dictionary(values_title)
        memory = {}
        print(dictionary_text_final)
        dictionary_final = {}
        i = 0
        counter = k
        while (counter != 0 and i<200):

            item_title = values_title[i][0]
            item_text = values_text[i][0]

            #    memory[item_title] += 1
            #    if memory[item_title]==2:
            #        counter = counter -1



            if item_title not in memory:
                memory[item_title] = 1
            else:
                memory[item_title] += 1

            if item_text not in memory:
                memory[item_text] = 1
            else:
                memory[item_text] += 1

            if memory[item_text] == 2:
                #if item_text not in tops:
                counter = counter - 1

            if memory[item_title] == 2:
                if item_text != item_title :
                    counter = counter -1

            i = i + 1
            #print("Iteration")
            #print(i)
        for value in list(memory.keys()):
            if dictionary_title_final.get(value) is None:
                dictionary_final[value] = 0.0 + float(dictionary_text_final[value])
            else:
                if dictionary_text_final.get(value) is None:
                    dictionary_final[value] = float(dictionary_title_final[value]) + 0.0
                else:
                    dictionary_final[value] = float(dictionary_title_final[value]) + float(dictionary_text_final[value])
        return dictionary_final

    def sort_dictionary(self, dictionary):
        list = []
        for key in dictionary.items():
            temp = dictionary.get(key)
            list.append(key)
        return sorted(list, key=lambda x: x[1],reverse=True)

