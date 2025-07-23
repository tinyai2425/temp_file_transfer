model_name = 'DeepSeek_R1_Distill_Qwen_7B'
TOKENIZER_CONFIG_PATH = "../Model_file/DeepSeek-R1-Distill-Qwen-7B" # tokenizer配置文件，主要用于确定token length

# Related to model sampling
TEMPERATURE = 0.6
TOPP = 0.95
TOPK = 10
REPETITIONPENALTY = 1.1

#OMC model parameters
INFER_TYPE = 0
TOKENIZER_TYPE = 4
TOKENIZER_PATH = "tokenizer.json"
MODEL_TYPE = 0
MODEL_PATH = "7b_seq_dynamic.omc"
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
STOP_SEQ = ["<endofsentence>", "<｜end▁of▁sentence｜>"]