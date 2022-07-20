# Awesome Transaction Fraud Detection Research Works.

A list of works on fraud detection in transaction data. 

## 2022
- **MonLAD: Money Laundering Agents Detection in Transaction Streams (WSDM 2022)**
  - Xiaobing Sun, Wenjie Feng, Shenghua Liu, Yuyang Xie, Siddharth Bhatia, Bryan Hooi, Wenhan Wang, Xueqi Cheng
  - [[Paper]](https://shenghua-liu.github.io/papers/wsdm2022-monlad.pdf), [[Code]](https://github.com/BGT-M/MonLAD)

- **Detecting Cash-out Users via Dense Subgraphs (KDD 2022)**
  - Yingsheng Ji, Zheng Zhang, Xinlei Tang, 
Jiachen Shen, Xi Zhang, Guangwen Yang
  - [[Code]](https://github.com/transcope/antico)

## 2021
- **xFraud: Explainable Fraud Transaction Detection**
  - Susie Xi Rao, Shuai Zhang, Zhichao Han, Zitao Zhang, Wei Min, Zhiyao Chen, Yinan Shan, Yang Zhao, Ce Zhang
  - [[Paper]](https://drive.google.com/file/d/1OS-iB82tRSM6jbnBiEKbQ87hTeRDfX9K/view), [[Code]](https://github.com/eBay/xFraud/)

- **CubeFlow: Money Laundering Detection with Coupled Tensors (PAKDD 2021)**
  - Xiaobing Sun, Jiabao Zhang, Qiming Zhao, Shenghua Liu, Jinglei Chen, Ruoyu Zhuang, Huawei Shen, Xueqi Cheng  
  - [[Paper]](https://shenghua-liu.github.io/papers/cubeflow-pakdd2021.pdf), [[Code]](https://github.com/BGT-M/spartan2-tutorials/blob/master/CubeFlow.ipynb)

## 2020

- **FlowScope: Spotting Money Laundering Based on Graphs (AAAI 2020)**
  - Xiangfeng Li, Shenghua Liu, Zifeng Li, Xiaotian Han, Chuan Shi, Bryan Hooi, He Huang, Xueqi Cheng
  - [[Paper]](https://shenghua-liu.github.io/papers/aaai2020cr-flowscope.pdf), [[Code]](https://github.com/aplaceof/FlowScope)

- **Modeling Users’ Behavior Sequences with Hierarchical Explainable Network for Cross-domain Fraud Detection (WWW 2020)**
  - Yongchun Zhu, Dongbo Xi, Bowen Song, Fuzhen Zhuang, Shuai Chen, Xi Gu, Qing He
  - [[Paper]](https://www.researchgate.net/profile/Bowen-Song-13/publication/341123092_Modeling_Users'_Behavior_Sequences_with_Hierarchical_Explainable_Network_for_Cross-domain_Fraud_Detection/links/60004b76299bf1408893f900/Modeling-Users-Behavior-Sequences-with-Hierarchical-Explainable-Network-for-Cross-domain-Fraud-Detection.pdf), [[Slider]](https://easezyc.github.io/data/WWW20_HEN_slides.pdf)
  
## 2019

- **Cash-Out User Detection Based on Attributed Heterogeneous Information Network with a Hierarchical Attention Mechanism (AAAI 2019)**
  - Binbin Hu, Zhiqiang Zhang, Chuan Shi, Jun Zhou, Xiaolong Li, Yuan Qi
  - [[Paper]](http://www.shichuan.org/doc/64.pdf), [[Code]](https://github.com/safe-graph/DGFraud)

- **TitAnt: Online Real-time Transaction Fraud Detection in Ant Financial (VLDB 2019)**
  - Shaosheng Cao, XinXing Yang, Cen Chen, Jun Zhou, Xiaolong Li, Yuan Qi  
  - [[Paper]](http://www.vldb.org/pvldb/vol12/p2082-cao.pdf)

  InfDetect: a Large Scale Graph-based Fraud Detection System for E-Commerce Insurance

- **Deeptrax: Embedding Graphs of Financial Transactions (ICMLA 2019)**
  - C. Bayan Bruss, Anish Khazane, Jonathan Rider, Richard Serpe, Antonia Gogoglou, Keegan E. Hines
  - [[Paper]](https://arxiv.org/pdf/1907.07225.pdf)

## 2017
- **Graph Mining Assisted Semi-supervised Learning for Fraudulent Cash-out Detection (ASONMA 2017)**
  - Yuan Li, Yiheng Sun, Noshir Contractor
  - [[Paper]](https://nosh.northwestern.edu/wp-content/uploads/2020/10/Graph-mining-assisted-semi-supervised-learning-for-fraudulent-cash-out-detection.pdf), [[Slider]](https://nosh.northwestern.edu/wp-content/uploads/2017/08/asonam2017-graph-mining.pdf)

## 2015
- **APATE: A Novel Approach for Automated Credit Card Transaction Fraud Detection using Network-Based Extensions (ASONMA 2017)**
  - Véronique Van Vlasselaer, Cristián Bravo, Olivier Caelen, Tina EliassRad, Leman Akoglu, Monique Snoeck, Bart Baesen
  - [[Paper]](http://www.eliassi.org/papers/vanvlasselaer_dss2015.pdf)


## Summary

| Model | Business problem | Scenario | Method |
| :---- | :---- | :---- | :---- | 
| MonLAD | Anti-money laundering | Bank | DSD |
| CubeFlow | Anti-money laundering | Bank | DSD |
| FlowScope | Anti-money laundering | Bank | DSD |
| ANTICO | Cash-out detection | Credit card | DSD |
| HACUD  | Cash-out detection | Credit payment | HIN |
| JD-Finance | Cash-out detection | Credit payment | Markov Random Field |
| xFraud | Fraudulent transactions | E-commerce | Heterogeneous GNN |
| HEN | Fraudulent transactions | E-commerce | Transfer Learning |
| TitAnt | Fraudulent transactions | E-payment | Graph Embedding |
| DeepTrax | Fraudulent transactions | Credit card | Graph Embedding |
| APATE | Fraudulent transactions | Credit card | Social network analysis |


