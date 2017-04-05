import Fagin
import ScorerFileManager

sfm = ScorerFileManager.ScorerFileManager()
fagin = Fagin.Fagin()

file = open("/home/xu/Documents/wir/HW12017/fagin/output_fagin.txt", "w")

file.write("Query_ID" + "\t" + "Doc_ID" + "\t" + "Rank" + "\t" + "Score" + "\n")

for query in range(1, 226):

    list_doc_score = fagin.fagin_algorithm(query, 2)

    if( list_doc_score is None):
        continue
    i = 1
    for element in list_doc_score:
        doc_id = element[0]
        doc_score = element[1]
        file.write(str(query) + "\t" + doc_id + "\t" + str(i + 1) + "\t" + str(doc_score))
        i = i + 1
        file.write("\n")
file.close()
