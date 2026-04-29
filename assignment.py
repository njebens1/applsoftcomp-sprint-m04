# Imports

import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import matplotlib.pyplot as plt

# Load model
model = SentenceTransformer("all-mpnet-base-v2")

# =========================
# Functions
# =========================
def make_axis(positive_words, negative_words, embedding_model):
    """Return a unit-length semantic axis from two word sets."""

    pos_emb = embedding_model.encode(positive_words, normalize_embeddings=True)
    neg_emb = embedding_model.encode(negative_words, normalize_embeddings=True)

    pole_pos = pos_emb.mean(axis=0)
    pole_neg = neg_emb.mean(axis=0)

    v = pole_pos - pole_neg
    v = v / (np.linalg.norm(v) + 1e-10)

    return v


def score_words(words, axis, embedding_model):
    """Project each word onto the axis. Returns one score per word."""

    emb = embedding_model.encode(list(words), normalize_embeddings=True)
    proj = emb @ axis

    return proj

# Load dataset
df = pd.read_csv("data/sp500.csv")

# Axis 1 (Growth vs Stability)
axis1_pos = ["growth", "innovation", "technology", "expansion", "future"]
axis1_neg = ["stability", "tradition", "legacy", "mature", "established"]

axis_growth = make_axis(axis1_pos, axis1_neg, model)

# Axis 2 (Consumer vs Industrial)
axis2_pos = ["consumer", "retail", "customer", "brand", "household"]
axis2_neg = ["industrial", "infrastructure", "manufacturing", "materials", "machinery"]

axis_industry = make_axis(axis2_pos, axis2_neg, model)

# Score companies
x = score_words(df["name"].tolist(), axis_growth, model)
y = score_words(df["name"].tolist(), axis_industry, model)

df_scored = df.assign(x=x, y=y)

# Plot
plt.figure(figsize=(8, 6))

for sector in df_scored["sector"].unique():
    subset = df_scored[df_scored["sector"] == sector]
    plt.scatter(subset["x"], subset["y"], label=sector, alpha=0.7)

plt.xlabel("Growth / Innovation  ↔  Stability / Tradition")
plt.ylabel("Consumer  ↔  Industrial")
plt.title("S&P 500 Semantic Map")

plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=8)
plt.tight_layout()

# make sure folder exists OR comment this out if needed
import os
os.makedirs("figs", exist_ok=True)

plt.savefig("figs/semantic_map.png", dpi=300)
plt.show()
