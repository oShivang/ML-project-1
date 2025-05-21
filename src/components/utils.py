import pandas as pd
import random
class data_loader:
    def __init__(self,dataframe:pd.DataFrame):
        self.dataframe=dataframe
    def load_data(self,batch_size:int):
        batch:pd.DataFrame
        for i in range(batch_size):
            if(self.dataframe.__len__()>0):
                random_index=random.choice(self.dataframe.index.tolist())
                ##pd.concat([batch,self.dataframe[random_index]])
                self.dataframe.drop(random_index).reset_index(drop=True)
                return self.dataframe.iloc[random_index]##delete it later
            else:
                break
        return batch
    def train_stoper(self):
        if self.dataframe.__len__()>0:
            return True
        return False
            