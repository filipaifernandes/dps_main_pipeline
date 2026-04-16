import sys
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Bio import AlignIO

plt.switch_backend("Agg")

# inputs
alignment_file = sys.argv[1]
output_csv = sys.argv[2]
output_png = sys.argv[3]

# ensure output folder exists
os.makedirs(os.path.dirname(output_csv), exist_ok=True)

# load alignment (FASTA)
alignment = AlignIO.read(alignment_file, "fasta")

names = [record.id for record in alignment]
n = len(alignment)

# sanity check: all same length (true alignment)
lengths = [len(record.seq) for record in alignment]
if len(set(lengths)) != 1:
    raise ValueError("ERROR: sequences are not properly aligned (different lengths)")

# identity function
def identity(seq1, seq2):
    matches = 0
    valid = 0

    for a, b in zip(str(seq1), str(seq2)):
        if a == "-" or b == "-":
            continue
        valid += 1
        if a == b:
            matches += 1

    return matches / valid if valid > 0 else 0

# build matrix
matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        matrix[i, j] = identity(alignment[i].seq, alignment[j].seq)

df = pd.DataFrame(matrix, index=names, columns=names)

# save CSV
df.to_csv(output_csv)

# plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df, cmap="viridis", vmin=0, vmax=1, square=True)

plt.title("Sequence Identity Heatmap (Final Alignment)")
plt.tight_layout()
plt.savefig(output_png, dpi=300)
