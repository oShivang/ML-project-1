import pandas as pd
from transformers import LEDTokenizer
from chunker import chunk_creater
class data_loader_cum_summerizer:
    def __init__(self,questions_dataframe:pd.DataFrame,comprehension_dict:dict):
        self.questions_dataframe=questions_dataframe
        self.comprehension_dict=comprehension_dict
    def NULL_Handler(self):
        dataframe=self.questions_dataframe
        dataframe.dropna(subset=dataframe.columns[0:3])
        return dataframe
    def tokenize_input(self,question:pd.DataFrame):
        pair=question.iloc[1].lower()+chunk_creater(question.iloc[1].lower(),self.comprehension_dict[question[0].lower()],3,512)
        tokenizer=LEDTokenizer.from_pretrained("allenai/led-base-16384")
        return tokenizer(pair,return_tensors="pt",padding="max_length",truncation=True,max_length=16384)
    def tokenize_output(self,question:pd.DataFrame):
        tokenizer=LEDTokenizer.from_pretrained("allenai/led-base-16384")
        return tokenizer(question.iloc[2].lower(),return_tensors="pt",padding="max_length",truncation=True,max_length=16384)


        
    
