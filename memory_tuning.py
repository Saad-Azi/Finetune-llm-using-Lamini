from lamini import Lamini
import lamini


try:
    lamini.api_key="add your key here (get it from lamini's official site)"
except Exception as e:
    print("api error ::")
    raise e

def get_data():
    data=[
        # add your data here
        {"input":"question","output":"response"},
    ]
    return data

# For training
# llm = Lamini(model_name='meta-llama/Meta-Llama-3.1-8B-Instruct')
# data = get_data()
# llm.train(data_or_dataset_id=data*20, finetune_args={"max_steps": 100, "learning_rate": 0.0003}, gpu_config={"gpus": 8, "nodes": 1})


# For testing
llm=Lamini(model_name="trained_model_id (get it form your lamini's account once the model is trained)")
print(llm.generate("""<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n Your input here <|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"""))
