from mol2vec.features import generate_corpus, insert_unk

input="D://thesis//HDAC2//mol2vec//databaseChemBL.smi"
output="D://thesis//HDAC2//mol2vec//ligandscorpus.cp"
radius=1                                                     # ECFP radius
n_jobs=4                                                     # Số core CPU
uncommon_token="UNK"                                         # Token thay cho identifier hiếm
threshold=3                                                  # Ngưỡng xuất hiện tối thiểu

generate_corpus(input, output, radius, sentence_type='alt', n_jobs=n_jobs)
print(f"Corpus saved to: {output}")

print(f"Inserting uncommon tokens (threshold ≤ {threshold})...")
insert_unk(output, output + ".unk", threshold=threshold, uncommon=uncommon_token)
print(f"Final corpus with UNK saved to: {output}.unk")
