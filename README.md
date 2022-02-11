Code for paper "Detecting Cash-out Users via Dense Subgraphs" 

ANTICO is developped for spotting cash-out users based on bipartite graph and subgraph detection. It is designed for credit card services and real-world banking data.

Main Contact: 

- Yingsheng Ji (jiyingsheng@gmail.com)
- Zheng Zhang (zhang.zh0707@gmail.com)


============ RUNNING ANTICO ON A TEST EXAMPLE ============

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
