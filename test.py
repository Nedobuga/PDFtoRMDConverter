from predicts import construct_df
from PDF2RMDConverter import pdf2rmdconverter

#df = construct_df.get_text_detection("C:/Users/kiril/Pictures/tmp/Zadacznik4_page-0218_jpg.rf.f8b66422e32f2508a725ad261edfebd1.jpg")
#print(df[df['label'] == 'Text'])
pdf2rmdconverter.convert(["C:/Users/kiril/Pictures/tmp/Снимокэкрана2025-02-28193057.png", "C:/Users/kiril/Pictures/tmp/test3.jpg", "C:/Users/kiril/Pictures/tmp/test2.jpg"])