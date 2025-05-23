from trainer import model_trainer
try:
    model_trainer('..data/comprehensions','..data/questions','../data/topics')
except Exception as e:
    print(f"[ERROR] {e}")
    import traceback
    traceback.print_exc()
