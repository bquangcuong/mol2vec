from mol2vec.features import train_word2vec_model

input = "D:\\thesis\\HDAC2\\mol2vec\\ligandscorpus.cp.unk"
output = "D:\\thesis\\HDAC2\\mol2vec\\model.pkl"

model=train_word2vec_model(
    infile_name=input,
    outfile_name=output,
    vector_size=300,
    window=10,
    min_count=3,
    n_jobs=4,
    method="skip-gram"
)

print(f"Model saved to: {output}")