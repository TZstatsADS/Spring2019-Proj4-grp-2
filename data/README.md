# Project: OCR (Optical Character Recognition) 

### Data folder

The data directory contains data used in the analysis. This is treated as read only; in paricular the R/python files are never allowed to write to the files in here. Depending on the project, these might be csv files, a database, and the directory itself may have subdirectories.

In this project, there are three subfolders -- ground_truth, tesseract, and ground_truth_trimmed. Each folder contains 100 text files with same file names correspondingly.


### Note
Please note that we figured there are exactly 13 text files whose total number of lines do not match between their corresponding ground_truth and tesseract files. Therefore, we manually trimmed the lines of those files and saved all those files in the folder called "ground_truth_trimmed".
