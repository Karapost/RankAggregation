
class ScorerFileManager:
    def __init__(self):

        #fagin
        self.out_cran_eng_stop_text_bm25 = "/home/xu/Documents/wir/HW12017/fagin/out_cran_eng_stop_text_bm25.tsv"
        self.out_cran_eng_stop_title_bm25 = "/home/xu/Documents/wir/HW12017/fagin/out_cran_eng_stop_title_bm25.tsv"


    #pick doc_id and score
    def from_file_to_dictionary_aggregation(self, file_path):

        file = open(file_path, "r")
        lines = file.readlines()
        dictionary = {}

        for i in range(1,len(lines)):
            parsed_line = lines[i].split()
            query_id = parsed_line[0]	
            doc_id = parsed_line[1]
            score = parsed_line[3]
            if query_id in dictionary:
                dictionary[query_id].update({doc_id: score})
            else:
                dictionary[query_id] = {doc_id: score}
        file.close()
        return dictionary
    
    def get_out_cran_eng_stop_text_bm25(self):
        return self.from_file_to_dictionary_aggregation(self.out_cran_eng_stop_text_bm25)


    def get_out_cran_eng_stop_title_bm25(self):
        return self.from_file_to_dictionary_aggregation(self.out_cran_eng_stop_title_bm25)

