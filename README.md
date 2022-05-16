# sIPM-LFR: Learning fair representation with a parametric integral probability metric

Official pytorch implementation of [Learning fair representation with a parametric integral probability metric](https://arxiv.org/abs/2202.02943) published in ICML 2022 by Dongha Kim, Kunwoong Kim, Insung Kong, Ilsang Ohn, and Yongdai Kim.


## Dependencies

- python 3.6+
- torch 1.11.0+
- CUDA 10.2+
- numpy 1.22.2+
- sklearn 1.1.0+
- argparse 1.1+

## Example commands

### with a single fair hyperparameter
- For unsupervised LFR:
```python
python main.py --dataset adult --lmda 0.0 --lmdaR 1.0 --lmdaF 5.0 --head_net 1smooth
```
- For supervised LFR:
```python
python main.py --dataset adult --lmda 1.0 --lmdaR 0.0 --lmdaF 5.0 --head_net 1smooth
```

### sweeping with many hyperparameters
- run ```./execute.bash```
dataset:
svm: 
unsup:
pcg_id:
head_net:


## Citation

## Datasets
- Adult Income dataset: 
- COMPAS dataset: 
- Heritage Health dataset: 

### TODO


