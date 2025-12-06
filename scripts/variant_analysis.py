 # Extract chromosome, position, reference allele, alternative allele, quality, filter, and info fields
bcftools query -f '%CHROM\t%POS\t%REF\t%ALT\t%QUAL\t%FILTER\t%INFO\n' VCF.vcf > variants.tsv
# Extract only SNPs
vcftools --vcf VCF.vcf --remove-indels --recode --out snps_only

# Extract only INDELs
vcftools --vcf VCF.vcf --keep-only-indels --recode --out indels_only
# Extract genotype (GT) information
vcftools --vcf VCF.vcf --extract-FORMAT-info GT --out genotypes

# Python Script For Variant Analysis
import pandas as pd

# Load the tab-separated file
df = pd.read_csv("variants.tsv", sep="\t", header=None)

# Display the first few rows
print(df.head())

# Identify SNPs (where REF and ALT are of the same length and single nucleotide)
snps = df[(df[2].str.len() == 1) & (df[3].str.len() == 1)]

# Identify INDELs (where REF or ALT is more than one nucleotide long)
indels = df[(df[2].str.len() > 1) | (df[3].str.len() > 1)]

# Save results
snps.to_csv("SNPs.tsv", sep="\t", index=False, header=False)
indels.to_csv("INDELs.tsv", sep="\t", index=False, header=False)

print(f"Total SNPs: {len(snps)}")
print(f"Total INDELs: {len(indels)}")

# Summary statistics
total_variants = len(df)
total_snps = len(snps)
total_indels = len(indels)

# Chromosome-wise distribution
chromosome_counts = df[0].value_counts()

print("=== Summary of Variant Calling ===")
print(f"Total Variants Identified: {total_variants}")
print(f"Total SNPs: {total_snps} ({(total_snps/total_variants)*100:.2f}%)")
print(f"Total INDELs: {total_indels} ({(total_indels/total_variants)*100:.2f}%)")
print("\nChromosome-wise Variant Distribution:")
print(chromosome_counts)

