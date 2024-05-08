# Simple commandline/notebook chat application using LLAMA 2 7B model
model imported from https://huggingface.co/


## Prerequisities
1. access to the llama2 model on https://huggingface.co/meta-llama/Llama-2-7b-chat-hf (you can gain it simply , having account on HF and fill the formular on the model site)
2. available IDE e.g. visual studio
3. installed python kernel or pykernel and pip for package management
4. install hugginface_hub, transfomers, torch, accelerate from pip e.g.:
   ```shell
   pip install torch
   ```
5. ensure your HW is capable to run the pretrained model, you can use GPU or CPU to run the model. Memory Calculator for model can be found here:
   https://huggingface.co/spaces/hf-accelerate/model-memory-usage
   
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
