# sIPM-LFR: Learning fair representation with a parametric integral probability metric

Official pytorch implementation of ["Learning fair representation with a parametric integral probability metric"](https://arxiv.org/abs/2202.02943) published in [ICML 2022](https://icml.cc/Conferences/2022/) by Dongha Kim, Kunwoong Kim, Insung Kong, Ilsang Ohn, and Yongdai Kim.

## 1. Dependencies

### Environments

- python 3.6+
- torch 1.11.0+
- CUDA 10.2+
- numpy 1.22.2+
- sklearn 1.1.0+
- argparse 1.1+

Automatically, those environmental dependencies are installed by the following command:
```pip install -r requirement.txt```

### Datasets
- Adult Income dataset: 
- COMPAS dataset: 
- Heritage Health dataset: 

For other datasets, you can freely perform experiments by adding those data in folder ```./datasets```.

## 2. Training

### Example commands

#### with a single fair hyperparameter
- For unsupervised LFR:
```python main.py --dataset adult --lmda 0.0 --lmdaR 1.0 --lmdaF 5.0 --head_net 1smooth```
- For supervised LFR:
```python main.py --dataset adult --lmda 1.0 --lmdaR 0.0 --lmdaF 5.0 --head_net 1smooth```

#### sweeping with many hyperparameters
- run ```./execute.bash```

Then, you see five components to be typed.
* dataset:
* svm: 
* unsup:
* pcg_id:
* head_net:

## 3. Results (paper)

![mean_dp_acc_scatter_laftr_Adadelta_2 0](https://user-images.githubusercontent.com/83457230/168527608-ad483f89-07eb-4bb1-87e6-8202045203d0.png)
![mean_dp_acc_scatter_pipm_Adadelta_2 0](https://user-images.githubusercontent.com/83457230/168527611-c8944011-0bc5-459f-a748-6938e6e0e7b7.png)
![adult_mean_dp_acc](https://user-images.githubusercontent.com/83457230/168527612-fd49301f-48a8-40ec-b908-b06b6e685cd9.png)
![compas_mean_dp_acc](https://user-images.githubusercontent.com/83457230/168527613-d921617d-a536-4854-9c98-132147826f5f.png)
![health_mean_dp_acc](https://user-images.githubusercontent.com/83457230/168527615-7764ef5b-cfaa-49d1-aa12-ad33d2fc3614.png)

### Citation

```
@inproceedings{kim2022sipmlfr,
  title={Learning fair representation with a parametric integral probability metric},
  author={Dongha Kim and Kunwoong Kim and Insung Kong and Ilsang Ohn and Yongdai Kim},
  booktitle={International Conference on Machine Learning},
  year={2022}
}
```

### TODO


