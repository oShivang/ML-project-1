from src.components.trainer import model_trainer
try:
    model_trainer('/Users/shivangkarthikey/Desktop/project1/data/comprehensions','/Users/shivangkarthikey/Desktop/project1/data/questions','/Users/shivangkarthikey/Desktop/project1/data/topics')
except Exception as e:
    print(f"[ERROR] {e}")
    import traceback
    traceback.print_exc()
