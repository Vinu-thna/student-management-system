from transformers import GPT2LMHeadModel, GPT2Tokenizer

class LLMAgent:
    def __init__(self, model_name='gpt2'):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)

    def query_llm(self, prompt, max_tokens=150):
        inputs = self.tokenizer(prompt, return_tensors='pt')

        outputs = self.model.generate(
            inputs.input_ids, 
            max_length=len(inputs.input_ids[0]) + max_tokens, 
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            pad_token_id=self.tokenizer.eos_token_id
        )

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
