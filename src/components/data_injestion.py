import pandas as pd
import os
class data_processor:
    def __init__(self,ques_path:str,comprehensions_path:str,topics_path:str):
        self.ques_path=ques_path
        self.comprehensions_path=comprehensions_path
        self.topics_path=topics_path
    def comprehension_dict(self):
        data_comprehension={}
        for filename in os.listdir(self.comprehensions_path):
            if filename.endswith('.txt.clean'):
                file_path=os.path.join(self.comprehensions_path,filename)
                with open(file_path,encoding='latin1') as f:
                    key=f.readline().strip().lower()
                    comprehension=[line.strip().lower() for line in f.readlines() if line != "\n"]
                    data_comprehension[key]=" ".join(comprehension)
        return data_comprehension
    def topic_list(self):
        data_topics=[]
        for filename in os.listdir(self.topics_path):
            if filename.endswith('.txt'):
                file_path =os.path.join(self.topics_path,filename)
                with open(file_path) as f:
                    [data_topics.append(line.strip().lower()) for line in f.readlines()]
        return data_topics
    def questions_list(self):
        list_questions=[]
        for filename in os.listdir(self.ques_path):
            if filename.endswith('.txt'):
                file_path=os.path.join(self.ques_path,filename)
                try:
                    df=pd.read_csv(filepath_or_buffer=file_path,sep='\t')
                    list_questions.append(df)
                except UnicodeDecodeError:
                    df=pd.read_csv(filepath_or_buffer=file_path,sep='\t',encoding='latin1')
                    list_questions.append(df)
        data_frame=pd.concat(list_questions,ignore_index=True)
        return data_frame


