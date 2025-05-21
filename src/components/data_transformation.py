import pandas as pd
from transformers import T5Tokenizer
from chunker import chunk_creater
class data_transform:
    def __init__(self,questions_dataframe:pd.DataFrame,comprehension_dict:dict):
        self.questions_dataframe=questions_dataframe
        self.comprehension_dict=comprehension_dict
        self.tokenizer=T5Tokenizer.from_pretrained("google/flan-t5-large")
    def NULL_Handler(self):
        dataframe=self.questions_dataframe
        dataframe.dropna(subset=dataframe.columns[0:3])
        return dataframe
    def tokenize_input(self,question:pd.DataFrame):
        pair=question.iloc[1].lower()+chunk_creater(question.iloc[1].lower(),self.comprehension_dict[question.iloc[0].lower()],3,512)
        return self.tokenizer(pair,return_tensors="pt",padding="max_length",truncation=True,max_length=2048)["input_ids"]
    def tokenize_output(self,question:pd.DataFrame):
        return self.tokenizer(question.iloc[2].lower(),return_tensors="pt",padding="max_length",truncation=True,max_length=2048)["input_ids"]


        
    
