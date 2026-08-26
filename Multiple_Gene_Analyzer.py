import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


print("." * 30)

print("MULTIPLE GENE SEQUENCE ANALYZER")

print("." * 30)


dna_sequence = [

    "ATGCGATCG",
    "GGCCATAT",
    "ATATATGC",
    "GCGCGCAA",
    "ATGCCGTA"

]

print("\n", "." * 10, "SEQUENCE INFORMATION", "." * 10)

for sequence in dna_sequence:

    print(
        "Sequence:", sequence,
        "|",
        "Length:", len(sequence)
    )

print("\n", "." * 10, "SEQUENCE ANALYSIS", "." * 10)


def seq_length(sequence):

    return len(sequence)


def seq_count(sequence):

    gc_content = (
        sequence.count("G")
        +
        sequence.count("C")
    )

    gc_percentage = (
        gc_content / len(sequence)
    ) * 100

    return gc_percentage


for sequence in dna_sequence:

    length = seq_length(sequence)

    gc = seq_count(sequence)

    print(
        "Sequence:", sequence,
        "| Length:", length,
        "| GC_CONTENT:", round(gc, 2), "%"
    )

print(
    "\n",
    "." * 10,
    "STORE LENGTH AND GC_CONTENT IN NUMPY ARRAYS",
    "." * 10
)


length_array = np.array([

    seq_length(sequence)

    for sequence in dna_sequence

])


print(
    "Length Of DNA Sequences as NumPy Array is:\n",
    length_array
)


count_values = np.array([

    seq_count(sequence)

    for sequence in dna_sequence

])


print(
    "\nGC_CONTENT VALUES ARE:\n",
    count_values
)

dataframe = pd.DataFrame({

    "Sequence": dna_sequence,

    "Length": length_array,

    "GC_CONTENT": count_values

})


print(
    "\n",
    "." * 10,
    "SEQUENCE DATA FRAME",
    "." * 10
)

print(dataframe)

dataframe["GC_GROUP"] = np.where(

    dataframe["GC_CONTENT"] >= 50,

    "HIGH GC",

    "LOW GC"

)


print(
    "\n",
    "." * 10,
    "GROUPING DATA FRAME",
    "." * 10
)

print(dataframe)

print(
    "\n",
    "." * 10,
    "SORTED SEQUENCE BY GC_CONTENT",
    "." * 10
)


sorted_dataframe = dataframe.sort_values(

    by="GC_CONTENT",

    ascending=False

)


print(sorted_dataframe)

print(
    "\n",
    "." * 10,
    "ANALYSIS COMPARISON",
    "." * 10
)


# Highest Length

high_length = dataframe.loc[

    dataframe["Length"].idxmax()

]


# Lowest Length

low_length = dataframe.loc[

    dataframe["Length"].idxmin()

]


# Highest GC Content

high_gc = dataframe.loc[

    dataframe["GC_CONTENT"].idxmax()

]


# Lowest GC Content

low_gc = dataframe.loc[

    dataframe["GC_CONTENT"].idxmin()

]


print(
    "HIGHEST LENGTH IS:\n",
    high_length
)


print(
    "\nLOWEST LENGTH IS:\n",
    low_length
)


print(
    "\nHIGHEST GC_CONTENT IS:\n",
    high_gc
)


print(
    "\nLOWEST GC_CONTENT IS:\n",
    low_gc
)


# ==================================================
# VISUALIZATION
# ==================================================

print(
    "\n",
    "." * 10,
    "DATA VISUALIZATION",
    "." * 10
)


sns.set_theme(style="whitegrid")


# ==================================================
# 1. GC CONTENT COMPARISON
# ==================================================

plt.figure(figsize=(10, 6))


sns.barplot(

    data=dataframe,

    x="Sequence",

    y="GC_CONTENT",

    hue="GC_GROUP",

    palette={
        "HIGH GC": "seagreen",
        "LOW GC": "tomato"
    },

    legend=True

)


plt.title(

    "GC Content Comparison of DNA Sequences",

    fontsize=16,

    fontweight="bold"

)


plt.xlabel(

    "DNA Sequence",

    fontsize=12

)


plt.ylabel(

    "GC Content (%)",

    fontsize=12

)


plt.xticks(rotation=20)


plt.legend(

    title="GC Group"

)


plt.tight_layout()


plt.show()


# ==================================================
# 2. DNA SEQUENCE LENGTH COMPARISON
# ==================================================

plt.figure(figsize=(10, 6))


sns.barplot(

    data=dataframe,

    x="Sequence",

    y="Length",

    color="skyblue"

)


plt.title(

    "DNA Sequence Length Comparison",

    fontsize=16,

    fontweight="bold"

)


plt.xlabel(

    "DNA Sequence",

    fontsize=12

)


plt.ylabel(

    "Sequence Length (bp)",

    fontsize=12

)


plt.xticks(rotation=20)


plt.tight_layout()


plt.show()


# ==================================================
# 3. GC CONTENT VS SEQUENCE LENGTH
# ==================================================

plt.figure(figsize=(9, 6))


sns.scatterplot(

    data=dataframe,

    x="Length",

    y="GC_CONTENT",

    hue="GC_GROUP",

    palette={
        "HIGH GC": "green",
        "LOW GC": "red"
    },

    s=180,

    edgecolor="black"

)


plt.title(

    "GC Content vs DNA Sequence Length",

    fontsize=16,

    fontweight="bold"

)


plt.xlabel(

    "Sequence Length (bp)",

    fontsize=12

)


plt.ylabel(

    "GC Content (%)",

    fontsize=12

)


plt.legend(

    title="GC Group"

)


plt.tight_layout()


plt.show()


# ==================================================
# END OF PROJECT
# ==================================================

print(
    "\n",
    "." * 30
)

print("MULTIPLE GENE SEQUENCE ANALYSIS COMPLETED")

print("." * 30)
