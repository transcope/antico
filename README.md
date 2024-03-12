Introduction
------
Implementation of our KDD paper "[Detecting Cash-out Users via Dense Subgraphs](https://dl.acm.org/doi/abs/10.1145/3534678.3539252)".

[[Code]](https://github.com/transcope/antico)
[[Video]](https://dl.acm.org/doi/abs/10.1145/3534678.3539252#)

  
ANTICO is developped for spotting cash-out users based on bipartite graph and subgraph detection. It is designed for credit card services and real-world banking data.

Main Contact: 

- Yingsheng Ji (jiyingsheng@gmail.com)
- Zheng Zhang (zhang.zh0707@gmail.com)


Running ANTICO on a test example
------
Support python 3.6

    pip install -r requirements.txt


The direct way to use ANTICO is to run in command line:

    python toy.py

where default demo is running on a synthetic dataset. 

Input Data Fromat:

- cards: account id, personal credit limit, label  
- merchants: account id, prior, label
- transactions: card account id, merchant account id, amount, timestamp, label

The main configuration items involve start\_date and ending\_date, and time\_spans in config.py. 

Cite
------
```latex
@inproceedings{ji2022detecting,
  title={Detecting cash-out users via dense subgraphs},
  author={Ji, Yingsheng and Zhang, Zheng and Tang, Xinlei and Shen, Jiachen and Zhang, Xi and Yang, Guangwen},
  booktitle={Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining},
  pages={687--697},
  year={2022}
}
```
