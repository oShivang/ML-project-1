import pandas as pd
from transformers import LEDTokenizer
class data_loader_cum_summerizer:
    def __init__(self,questions_dataframe:pd.DataFrame,comprehension_dict:dict):
        self.questions_dataframe=questions_dataframe
        self.comprehension_dict=comprehension_dict
    def NULL_Handler(self):
        dataframe=self.questions_dataframe
        dataframe.dropna(subset=dataframe.columns[0:3])
        return dataframe
    def tokenize(self,question:pd.DataFrame):
        pair=question.iloc[1].lower()+self.comprehension_dict[question[0].lower()]
        tokenizer=LEDTokenizer.from_pretrained("allenai/led-base-16384")
        return tokenizer(pair,return_tensors="pt",padding="max_length",truncation=True,max_length=16384)

        
    
