# sIPM-LFR: Learning fair representation with a parametric integral probability metric

Official pytorch implementation of ["Learning fair representation with a parametric integral probability metric"](https://arxiv.org/abs/2202.02943) published in [ICML 2022](https://icml.cc/Conferences/2022/) by Dongha Kim, Kunwoong Kim, Insung Kong, Ilsang Ohn, and Yongdai Kim.

<p align="center"><img src="https://user-images.githubusercontent.com/83457230/169192250-014ff243-4a4a-4231-8689-5c533c9610ca.png" width="400" height="40"></p>

## 1. Dependencies

### Environments

- python 3.6+
- torch 1.11.0+
- CUDA 10.2+
- numpy 1.22.2+
- sklearn 1.1.0+
- argparse 1.1+
- yaml 6.0+

Automatically, those environmental dependencies are installed by running the following command:
```pip install -r requirements.txt```

### Datasets
- [Adult Income dataset](https://archive.ics.uci.edu/ml/datasets/adult)
- [COMPAS dataset](https://github.com/propublica/compas-analysis)
- [Heritage Health dataset](https://foreverdata.org/1015/index.html)

Practitioners can freely use other custom datasets.

## 2. Training

### Example commands

#### with a single fair hyperparameter
- For unsupervised LFR:
```python main.py --dataset adult --lmda 0.0 --lmdaR 1.0 --lmdaF 5.0 --head_net 1smooth```
- For supervised LFR:
```python main.py --dataset compas --lmda 1.0 --lmdaR 0.0 --lmdaF 0.1 --head_net 1smooth```

#### sweeping with many hyperparameters
- run ```./execute.bash``` for Adult dataset.

### Saved models and results
- The selected models and corresponding results are saved in folders ```/models``` and ```/results```.

<!-- ## 3. Results (paper)
Experimental results on Adult dataset:
<p align="center"><img src="https://user-images.githubusercontent.com/83457230/169193245-c0d7e06d-642f-443f-9e85-b91933e09b3f.png" width="850" height="250"></p>


### Citation

```
@inproceedings{kim2022sipmlfr,
  title={Learning fair representation with a parametric integral probability metric},
  author={Dongha Kim and Kunwoong Kim and Insung Kong and Ilsang Ohn and Yongdai Kim},
  booktitle={International Conference on Machine Learning},
  year={2022}
}
``` -->
