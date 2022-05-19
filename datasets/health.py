import os

import pandas as pd
import requests

from datasets.standard_dataset import StandardDataset


class HealthDataset(StandardDataset):
    def __init__(self):
        super(HealthDataset, self).__init__()
        self.name = "health"
        self.protected_attribute_name = "age"
        self.privileged_classes = ["None"]
        filedir = "datasets/health/"
        
        if not os.path.exists("datasets/health/health_train.csv"):
        
            df = pd.read_csv("datasets/health/health_Y2.csv")

            df["age"] = df["age_05"] + df["age_15"] + df["age_25"] + df["age_35"] + df["age_45"] + df["age_55"] + df["age_65"]
#             + df["age_75"] + df["age_85"]
            
            df = df.sample(frac=1, random_state=0)
            self.test = df.tail(int(df.shape[0] * 0.4))
            self.train = df.head(df.shape[0] - self.test.shape[0])
            self.test.sample(frac=1, random_state=0)
            n_test_val = self.test.shape[0]
            self.val = self.test.tail(int(n_test_val * 0.5))
            self.test = self.test.head(n_test_val - self.val.shape[0])
            
            self.train.to_csv(os.path.join(filedir, "health_train.csv"), index=None)
            self.val.to_csv(os.path.join(filedir, "health_val.csv"), index=None)
            self.test.to_csv(os.path.join(filedir, "health_test.csv"), index=None)
            
        else:
            self.train = pd.read_csv(
                os.path.join(filedir, "health_train.csv"), index_col=False
            )
            self.val = pd.read_csv(
                os.path.join(filedir, "health_val.csv"), index_col=False
            )
            self.test = pd.read_csv(
                os.path.join(filedir, "health_test.csv"), index_col=False
            )


def main():
    HealthDataset()


if __name__ == "__main__":
    main()
