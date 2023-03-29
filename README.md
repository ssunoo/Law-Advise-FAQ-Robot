# Law-Advise-FAQ-Robot
[dataset/](https://github.com/ssunoo/Law-Advise-FAQ-Robot/tree/main/dataset): Put in the dataset which you want to search.

[src/preprocessing.py](https://github.com/ssunoo/Law-Advise-FAQ-Robot/blob/main/src/preprocessing.py): Run once to generate embedding of dataset. You need to change three path variable datasetPath, chineseDict, outPath if you use your own dataset and dict.

[src/faq.py](https://github.com/ssunoo/Law-Advise-FAQ-Robot/blob/main/src/faq.py): FAQ example. You need to change three path variable dictPath, datasetPath, embeddingPath if you use your own dataset and dict. embeddingPath is the path to the file which preprocessing.py generate. 
