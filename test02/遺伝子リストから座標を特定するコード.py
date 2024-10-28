import pandas as pd

# Load the gene list and coordinates files
gene_list_path = r"遺伝子リストのCSVファイルのパスをここに記入"
gene_coordinates_path = r"遺伝子アノテーションファイルのパスをここに記入"

# Read the files
gene_list_df = pd.read_csv(gene_list_path)

# Display the first few rows to check the data
print("Gene list data:\n", gene_list_df.head())

# Clean up the gene list DataFrame
gene_list_df_cleaned = gene_list_df.rename(columns={gene_list_df.columns[0]: 'gene_name'})  # First column as 'gene_name'
gene_list_df_cleaned = gene_list_df_cleaned[['gene_name']].dropna()

# Check cleaned DataFrame
print("Cleaned gene list data:\n", gene_list_df_cleaned.head())

# Read gene coordinates
gene_coordinates_df = pd.read_csv(gene_coordinates_path)

# Clean up the coordinates DataFrame
gene_coordinates_df_cleaned = gene_coordinates_df[['name2', 'chrom', 'txStart', 'txEnd']].rename(columns={'name2': 'gene_name'})

# Merge the gene list with the gene coordinates based on the gene_name
merged_df = pd.merge(gene_list_df_cleaned, gene_coordinates_df_cleaned, on='gene_name', how='left')

# Save the merged result to a new CSV file
output_path = r"出力先のファイルのパスを記入CSV"
merged_df.to_csv(output_path, index=False)

print("Output saved to:", output_path)

