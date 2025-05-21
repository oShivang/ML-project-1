from transformers import T5ForConditionalGeneration
from data_injestion import data_processor
from data_transformation import data_transform
from utils import data_loader
import torch
class model_trainer:
    def __init__(self,comprehension_address:str,question_address:str,topic_address:str):
        device= ('cuda' if torch.cuda.is_available() else'cpu')
        model = T5ForConditionalGeneration.from_pretrained("t5-large").to(device)
        optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)
        data=data_processor(question_address,comprehension_address,topic_address)
        train_questions=data.questions_list()
        train_comprehensions=data.comprehension_dict()
        train_data=data_transform(train_questions,train_comprehensions)
        dataloader=data_loader(train_data.NULL_Handler())
        total_loss=0
        count=1
        for epoches in range(3):
            while(dataloader.train_stoper):
                random_que=dataloader.load_data(batch_size=1)
                input_ids = train_data.tokenize_input(random_que).to(model.device)
                labels = train_data.tokenize_output(random_que)

                outputs = model(input_ids=input_ids, labels=labels)
                loss = outputs.loss

                loss.backward()
                optimizer.step()
                optimizer.zero_grad()
                print(total_loss)
                print (count)
                count+=1
        torch.save({"model_state": model.state_dict()},)



                



