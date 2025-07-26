from mol2vec.features import featurize

input = "D:\\thesis\\HDAC2\\mol2vec\\smiles.smi"
output = "D:\\thesis\\HDAC2\\mol2vec\\vectors.csv"
model = "D:\\thesis\\HDAC2\\mol2vec\\model.pkl"

featurize(
    in_file=input,
    out_file=output,
    model_path=model,
    r=1,
    uncommon="UNK"
)

print(f"Featurized output saved to: {output}")
