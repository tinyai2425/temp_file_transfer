model_name = 'Qwen2_5_7B_Instruct'
TOKENIZER_CONFIG_PATH = "../Model_file/Qwen2.5-7B-Instruct" # tokenizer配置文件，主要用于确定token length

# Related to model sampling
TEMPERATURE = 0.7
TOPP = 0.8
TOPK = 20
REPETITIONPENALTY = 1.05

#OMC model parameters
INFER_TYPE = 0
TOKENIZER_TYPE = 4
TOKENIZER_PATH = "tokenizer.json"
MODEL_TYPE = 0
MODEL_PATH = "qwen25_7b_ceval_g128_fp32.omc"
WEIGHT_DIR = "./"
PREFIX_PROMPT = ""
PMT_CACHE_OP = ""
PFX_INIT_TOKEN_LEN = 6
LORA_CFG_PATH = ""
CALLBACK_FREQ = 2
SAMPLE_FLAG = True
SEED = 99
INIT_TOKEN_LEN = 1024
IS_ASYNC = True
STOP_SEQ = ["<|im_end|>", "<|endoftext|>"]