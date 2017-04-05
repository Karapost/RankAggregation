import Fagin
import ScorerFileManager

sc = ScorerFileManager.ScorerFileManager()
fagin = Fagin.Fagin()


file = open("/home/xu/Documents/wir/HW12017/fagin/output_fagin.txt", "w")
queries = list(sc.get_out_cran_eng_stop_text_bm25().keys())
#print(queries)
file.write("Query_ID" + "\t" + "Doc_ID" + "\t" + "Rank" + "\t" + "Score")
file.write("\n")
for query in queries:
    temp = fagin.fagin_algorithm(query,3)
    lista = fagin.sort_dictionary(temp)
    #print("Query ID")
    #print(query)
    i=0
    for value in lista:
        doc_id = value[0]
        #print("doc_id")
        #print(doc_id)
        doc_score = value[1]
        #print("doc_score")
        #print(doc_score)
        file.write(query + "\t" + doc_id + "\t" + str(i+1) + "\t" + str(doc_score))
        i=i+1
        file.write("\n")
file.close()
