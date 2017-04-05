import Threshold
import ScorerFileManager

sc = ScorerFileManager.ScorerFileManager()
threshold = Threshold.Threshold()


file = open("/home/xu/Documents/wir/HW12017/fagin/output_threshold.txt", "w")
queries = list(sc.get_out_cran_eng_stop_text_bm25().keys())
file.write("Query_ID" + "\t" + "Doc_ID" + "\t" + "Rank" + "\t" + "Score")
file.write("\n")
for query in queries:
    temp = threshold.threshold_algorithm(query, 10)
    print(temp)
    i=0
    for value in temp:
        doc_id = value[0]
        doc_score = value[1]
        file.write(query + "\t" + doc_id + "\t" + str(i+1) + "\t" + str(doc_score))
        i=i+1
        file.write("\n")
file.close()
