# Project: OCR (Optical Character Recognition) 

![image](figs/ocrexample.jpg)

### [Full Project Description](doc/project4_desc.md)

Term: Spring 2019

+ Team #2
+ Team members
	+ Zongbo Cai
	+ Charlie Chen
	+ Shiwei Hua
	+ Xin Xia
	+ Chao Yin

+ Project summary: In this project, we created an OCR post-processing procedure to enhance Tesseract OCR output. We convert scanned images into machine readable character streams and process raw scanned images relying on the Tessearct OCR machine

![image](figs/example 3.jpg)

+ Methods:
	1. Rule-based techniques
	2. Supervised model – correction regressor

+ Feature extracted: Levenshtein edit distance, String similarity, Language popularity, Lexicon existance,  Exact-context popularity, and Relaxed-context popularity.

+ Model: AdaBoost with Parameters: learning_rate = 0.01, loss = 'exponential', n_estimators = 50, random_state = None

+ Evaluation on:
	1.  Precision: is the percentage of correctly found words with respect to the total word count of the OCR output
	2.  Recall: the percentage of words in the original text correctly found by the OCR engine

![image](figs/example 2.jpg)

**Contribution statement**: ([default](doc/a_note_on_contributions.md)) All team members contributed equally in all stages of this project. All team members approve our work presented in this GitHub repository including this contributions statement. 

Chao Yin: Completed Candidate Search, Feature Scoring and Model Evaluation according to paper C2. Worked on Measurement with Xin Xia.

Xin Xia: Completed error detection part from paper D1 and worked on measurement with Chao Yin.

Zongbo Cai: Completed parameters tunning and training for AdaBoost. Provided data for measurement.

Following [suggestions](http://nicercode.github.io/blog/2013-04-05-projects/) by [RICH FITZJOHN](http://nicercode.github.io/about/#Team) (@richfitz). This folder is orgarnized as follows.

```
proj/
├── lib/
├── data/
├── doc/
├── figs/
└── output/
```

Please see each subfolder for a README file.
