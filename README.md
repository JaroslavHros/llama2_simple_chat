# Simple commandline/notebook chat application using LLAMA 2 7B model
model imported from https://huggingface.co/

## Usage
model initialization:
```python
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
model.cuda()  # for using GPU
```

1. initialize model
2. take input from cli and encode it to the tensors using autotokenizer
3. when using GPU memory we need to convert tensors to CUDA (nvidia)
4. generate output from inputed prompt
5. finally decode output and return in to the user :)
