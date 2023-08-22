import os

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from dotenv import load_dotenv

load_dotenv()

def translate_from_english(input_en_text, dest_lang):
    tokenizer = AutoTokenizer.from_pretrained(
        "facebook/nllb-200-distilled-600M", src_lang="english")

    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")

    # tokenize input English text
    inputs = tokenizer(input_en_text, return_tensors="pt")

    translated_tokens = model.generate(
        **inputs, forced_bos_token_id=tokenizer.lang_code_to_id["deu_Latn"], max_length=30
    )
    
    return tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]

if __name__ == "__main__":
    print("hello?")
    print(translate_from_english(input("Enter: "), "chinese"))