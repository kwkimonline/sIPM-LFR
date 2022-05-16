# sIPM-LFR: Learning fair representation with a parametric integral probability metric

Official pytorch implementation of [Learning fair representation with a parametric integral probability metric](https://arxiv.org/abs/2202.02943) published in ICML 2022.


## Dependencies

## Example commands

### with a single $`\lambda`$
For unsupervised LFR:
```python
python main.py --dataset adult --lmda 0.0 --lmdaR 1.0 --lmdaF 5.0 --head_net 1smooth
```
For supervised LFR:
```python
python main.py --dataset adult --lmda 1.0 --lmdaR 0.0 --lmdaF 5.0 --head_net 1smooth
```

### sweeping with many ```\lambda```s

## Citation

### TODO


