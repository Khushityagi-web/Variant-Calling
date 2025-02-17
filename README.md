# Variant Calling Analysis - SNPs & INDELs Identification

## Introduction 
This repository contains the variant calling analysis performed on a VCF file (VCF.vcf). The analysis includes filtering variants, extracting SNPs & INDELs, and summarizing the key findings. The results provide insights into genetic variations such as Single Nucleotide Polymorphisms (SNPs) and Insertions/Deletions (INDELs).


## Commands Used for Variant Processing 

### 1. View and Filter Variants  
# View the VCF file in a readable format
bcftools view VCF.vcf | less -S

# Extract only SNPs and INDELs from the VCF file
bcftools view -v snps,indels -O v -o filtered_variants.vcf VCF.vcf

# Key Findings
1. Total Variants Identified
Total Variants: 1,964,791
2. Classification of Variants
SNPs Identified: 1,964,063 (99.96% of total variants)
INDELs Identified: 728 (0.04% of total variants)
3. Chromosome-Wise Variant Distribution
All 1,964,791 variants were found on AE005672.3, indicating a single reference sequence.
Conclusion
The variant calling analysis successfully identified a high proportion of SNPs compared to INDELs.
The chromosome-wide distribution suggests that all variations belong to a single reference sequence (AE005672.3).
Further downstream analysis, such as functional annotation, could provide insights into the biological significance of these variants.

# File Contents
VCF.vcf: Original VCF file with raw variant data
filtered_variants.vcf:	Processed VCF file with only SNPs & INDELs
variants.tsv:	Tab-separated file with variant information
SNPs.tsv:	SNPs extracted from the VCF file
INDELs.tsv:	INDELs extracted from the VCF file
genotypes.FORMAT:	Extracted genotype information

