import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer

# login to access hugging faces
from huggingface_hub import login
login()

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
model.cuda()  # for using GPU


# simple function to chat wit model
def chat_with_llama(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    input_ids = input_ids.to('cuda')
    output = model.generate(input_ids, max_length=256, num_beams=4, no_repeat_ngram_size=2)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# while loop for taking input and returing response for model
while True:
    prompt = input("You: ")
    response = chat_with_llama(prompt)
    print("Llama:", response)
