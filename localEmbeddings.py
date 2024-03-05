from transformers import AutoModel, AutoTokenizer


tokenizer = AutoTokenizer.from_pretrained("./fineTuning/Tokeniser")

# Load the model
model = AutoModel.from_pretrained("./fineTuning/Model")


def generate_embeddings(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    outputs = model(**inputs)
    # return outputs.last_hidden_state.detach().numpy()
    embeddings = outputs.last_hidden_state[:, 0, :].cpu().detach().numpy()
    embeddings = embeddings.flatten().tolist()
    final_embeddings = []
    for i in range(0, 768):
        if i < len(embeddings):
            final_embeddings.append(embeddings[i])
        else:
            final_embeddings.append(0.0)
    return final_embeddings
