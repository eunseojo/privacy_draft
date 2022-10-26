from transformers import pipeline, set_seed
import csv
import datetime 
import re
import json


with open("us-legislator-names.txt", "r") as f_legis:
    legislators = f_legis.read()
legislators = legislators.split("\n")

with open("amex_cc.txt", "r") as f_cc:
    cc = f_cc.read()
cc = cc.split("\n")

all_pairs = []

for i in range(len(legislators)):
    all_pairs.append([legislators[i], cc[i]])


#print(pii)

def get_list_offsets(context, s):
    
    all_matches = re.finditer(s, context)
    ret = [[i.start(), i.end()-1, i.group(0)] for i in all_matches] 
    
    return ret









f = open("context-demo-formatted.jsonl", "a")

model = "gpt2"
generator = pipeline('text-generation', model=model)
set_seed(42)
#print("hi")
for p in all_pairs:
    prompt = "My name is {legislator_name} and my credit card number is {cc_number}."
    formatted = prompt.format(legislator_name = p[0], cc_number = p[1])
    #print(p[0], p[1])


    output = generator(formatted, max_length=500, num_return_sequences=5)
    #print(output)
    for i in output:
        generated_text = i["generated_text"]
        len_gen = len(generated_text.split())
        while len_gen < 512:
            #print(len_gen)
            if len_gen > 512: break
            new_output = generator(generated_text, max_length=1000, num_return_sequences=1)
            new_generated_text = new_output[0]["generated_text"]
            new_len = len(new_generated_text.split())
            if new_len <= len_gen: break
            len_gen = new_len
            generated_text = new_generated_text
        
        name_offsets = get_list_offsets(generated_text, p[0])
        cc_number_offsets = get_list_offsets(generated_text, p[1])
        
        new_output[0]["name"] = name_offsets
        new_output[0]["cc_number"] = cc_number_offsets

        print(new_output[0])



        json.dump(new_output[0], f)
        f.write("\n")
f.close()









#testing code:
# test = 'My name is Maria Cantwell and my credit card number is 376740771597686. You should be able to find it with an online search.\n\nLet us know what you think below. If you do decide not to return the card to this address, please tell us what you do with it for online returns.'
# output = generator(test, max_length=1000,num_return_sequences=5)
# print(output)




#example of how it just doesn't generate anything further. 
#[{'generated_text': 'My name is Maria Cantwell and my credit card number is 376740771597686. You should be able to find it with an online search.\n\nLet us know what you think below. If you do decide not to return the card to this address, please tell us what you do with it for online returns. We will do our best to help you.\n\nTo return your card to the address on this page, please email it to the address listed above. We will return your Card instantly.'}, {'generated_text': 'My name is Maria Cantwell and my credit card number is 376740771597686. You should be able to find it with an online search.\n\nLet us know what you think below. If you do decide not to return the card to this address, please tell us what you do with it for online returns.\n\nThank you.'}, {'generated_text': 'My name is Maria Cantwell and my credit card number is 376740771597686. You should be able to find it with an online search.\n\nLet us know what you think below. If you do decide not to return the card to this address, please tell us what you do with it for online returns.\n\nWe would love to hear from you. Email us at: news@jscapitimes.co.uk\n\nShare this: Google\n\nFacebook\n\nTwitter\n\nEmail'}, {'generated_text': 'My name is Maria Cantwell and my credit card number is 376740771597686. You should be able to find it with an online search.\n\nLet us know what you think below. If you do decide not to return the card to this address, please tell us what you do with it for online returns.'}, {'generated_text': 'My name is Maria Cantwell and my credit card number is 376740771597686. You should be able to find it with an online search.\n\nLet us know what you think below. If you do decide not to return the card to this address, please tell us what you do with it for online returns.'}]