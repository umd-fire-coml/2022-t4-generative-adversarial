""" Semantically picks most similar tags in training space of
    generative model """

# IMPORTS
import json
import torch
from typing import List
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity


# FUNCTIONS
# create embeddings
def get_embeddings(text, token_length, tokenizer, model):
    tokens = tokenizer(text, max_length=token_length,
                       padding='max_length', truncation=True)
    output = model(torch.tensor(tokens.input_ids).unsqueeze(0),
                   attention_mask=torch.tensor(
                       tokens.attention_mask
                    ).unsqueeze(0)).hidden_states[-1]
    return torch.mean(output, axis=1).detach().numpy()


# get doc with highest similarity to query
def nearest_doc(doc_list: List[str],
                query: str,
                tokenizer,
                model,
                token_length: int = 50):
    # get embeddings for each document
    outs = [
        get_embeddings(doc, token_length, tokenizer, model) for doc in doc_list
    ]
    # get embeddings for query
    query_embeddings = get_embeddings(query, token_length=token_length)
    # get similarity of each document embedding to query embedding
    sims = [cosine_similarity(out, query_embeddings)[0][0] for out in outs]
    return max(zip(sims, doc_list))[1]


# MAIN 
def get_nearest_tags(user_tags: List[str]):
    # download pretrained model
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased",)
    model = AutoModel.from_pretrained("bert-base-uncased",
                                      output_hidden_states=True)

    # get tag lists from local json file
    with open("./tags.json", "r") as jf:
        tags = json.load(jf)

    # separate tags by type
    user_genre, user_mood, user_instr = user_tags
    genres, moods, instrs = tags["genre"], tags["mood"], tags["instrument"]

    return (
        nearest_doc(genres, user_genre, tokenizer, model),
        nearest_doc(moods, user_mood, tokenizer, model),
        nearest_doc(instrs, user_instr, tokenizer, model)
    )
