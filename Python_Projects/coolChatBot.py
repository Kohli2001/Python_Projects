import openai


# Set up the OpenAI API client openai.api_key= "YOUR API KEY"

openai.api_key="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"

# Set up the model and prompt model engine="text-davinci-003" prompt = str(input())

model_engine="text-davinci-003"
prompt = str(input())

# Generate a response

completion = openai.Completion.create(

engine = model_engine,

prompt=prompt,
max_tokens= 1024,

n=1,

stop=None,

temperature= 0.5,

)
#print response as output

response=completion.choices[0].text

print (response)

