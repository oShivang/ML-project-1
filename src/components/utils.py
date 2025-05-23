import pandas as pd
import random
class data_loader:
    def __init__(self,dataframe:pd.DataFrame):
        self.dataframe=dataframe
    def load_data(self,batch_size:int):
        for i in range(batch_size):
            if(self.dataframe.__len__()>0):
                random_index=random.randint(0,len(self.dataframe))
                temp=self.dataframe.iloc[random_index]
                self.dataframe=self.dataframe.drop(random_index).reset_index(drop=True)
                print(temp)
                return temp
    def train_stoper(self):
        if self.dataframe.__len__()>0:
            return True
        return False