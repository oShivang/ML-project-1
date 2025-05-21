from sentence_transformers import SentenceTransformer, util
import nltk
from nltk.tokenize import sent_tokenize
import torch

nltk.download('punkt')

def chunk_creater(query: str, comprehension: str, top_k: int, token_per_chunk: int):
    model = SentenceTransformer('all-mpnet-base-v2')

    # Step 1: Chunk comprehension text
    chunks = []
    current_chunk = ""
    current_len = 0

    sentences = sent_tokenize(comprehension)

    for sentence in sentences:
        sentence_len = len(sentence.split())

        if current_len + sentence_len > token_per_chunk:
            if current_chunk.strip():
                chunks.append(current_chunk.strip())
            current_chunk = sentence
            current_len = sentence_len
        else:
            current_chunk += " " + sentence
            current_len += sentence_len

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    # Step 2: Encode chunks and query
    chunk_embeddings = model.encode(chunks, convert_to_tensor=True)
    query_embedding = model.encode(query, convert_to_tensor=True)

    # Step 3: Compute cosine similarity
    cosine_similarity = util.pytorch_cos_sim(query_embedding, chunk_embeddings)[0]

    # Step 4: Get top-k most relevant chunks
    top_k_scores, top_k_indices = torch.topk(cosine_similarity, k=top_k)

    top_chunks = [chunks[i] for i in top_k_indices.tolist()]

    return " ".join(top_chunks)
