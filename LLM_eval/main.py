"""
Script to give a rough assessment of the HWs using LLM. Requires langchain and OpenAI API.
- Paolo Frazzetto <paolo.frazzetto@phd.unipd.it>
"""
import time

import pandas as pd
from decouple import config
from langchain import LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (AIMessagePromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate,
									SystemMessagePromptTemplate)

if __name__ == '__main__':

	# Load dataframe with questions from ./subs/
	df = pd.read_excel("subs/HW4_1sub.xlsx", sheet_name="Questions")
	df = df[df['TA'] == 'Paolo']

	# Store OpenAI API KEY in an .env file
	OPENAI_API_KEY = config('OPENAI_API_KEY')
	# Pick LLM
	llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model='gpt-3.5-turbo', temperature=0)

	# Prompt Engineering
	template = """
	You are instructed to correct Deep Learning Homeworks form a Computer Science University course.
	The students have to find a configuration of a Transformer that can beat a given RNN, by experimenting with different hyperparameters. 
	The hyperparamters to try and discuss are:
	– the number of expected features in the encoder/decoder inputs;
	- number of heads;
	- number of layers in the encoder/decoder.
	The dataset is always IMDB and the evaluation metric is the accuracy. The correct answer should be extensive, coherent, appropriate and covering all those aspects.
	The scores you have to assign are:
	- A if the answer is correct;
	- B if the answer is incomplete or wrong.
	- C if you are unsure.
    Reply with the score and give a concise feedback only for B and C.
    ---
	"""

	system_message_prompt = SystemMessagePromptTemplate.from_template(template)
	human_template = "{answer}"
	human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

	chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

	# Build chain
	llm_chain = LLMChain(prompt=chat_prompt, llm=llm)

	# Loop over answers and save the score
	for index, row in df.iterrows():
		df.at[index, 'Penalty Q4'] = llm_chain.run(row['Q4 - Discusison Transformers'])
		print(index, row['Name'], df.at[index, 'Penalty Q4'])
		time.sleep(1)  # to avoid too fast API requests

	# Save results
	df.to_excel("subs/outputQ4.xlsx")
	print("Done!")