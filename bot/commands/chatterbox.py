from transformers import AutoTokenizer, AutoModelForCausalLM
from aiogram import types

tokenizer = AutoTokenizer.from_pretrained('/home/anton/tg_bot/models/tokenizer_for_dialogue')
model = AutoModelForCausalLM.from_pretrained("/home/anton/tg_bot/models/model_for_dialogue")

async def q_chatterbox(message: types.message):
    await message.reply('О чем поговорим?')


async def chatterbox(message: types.message):

    def respond_to_dialog(texts):
        prefix = '\nx:'
        for i, t in enumerate(texts):
            prefix += t
            prefix += '\nx:' if i % 2 == 1 else '\ny:'
        tokens = tokenizer(prefix, return_tensors='pt')
        tokens = {k: v.to(model.device) for k, v in tokens.items()}
        end_token_id = tokenizer.encode('\n')[0]
        size = tokens['input_ids'].shape[1]
        output = model.generate(
            **tokens,
            eos_token_id=end_token_id,
            do_sample=True,
            max_length=size+128,
            repetition_penalty=3.2,
            temperature=1,
            num_beams=3,
            length_penalty=0.01,
            pad_token_id=tokenizer.eos_token_id
        )
        decoded = tokenizer.decode(output[0])
        result = decoded[len(prefix):]
        return result.strip()



    seed = input('Начните диалог с ботом любой фразой\n')
    history = [seed]
    while True:
        result = respond_to_dialog(history[-10:])
        next_sentence = input(result + '\n')
        history.append(result)
        history.append(next_sentence)

    await message.reply(f'lalala{history}')
