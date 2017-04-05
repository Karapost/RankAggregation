import ScorerFileManager
import Fagin
import Threshold

threshold = Threshold.Threshold()
fagin = Fagin.Fagin()
sc = ScorerFileManager.ScorerFileManager()

#print(fagin.sort_dictionary(fagin.fagin_algorithm("1", 20)))
#print(sc.get_out_cran_eng_stop_text_bm25().get(list(sc.get_out_cran_eng_stop_text_bm25().keys())[0]))
#print(sc.get_out_cran_eng_stop_text_bm25())
print(threshold.threshold_algorithm("1", 5))