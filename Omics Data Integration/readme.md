## Multi-Omics Data Integration Analysis

This repository contains data and scripts for integrating multiple omics datasets from the JvRad project. The goal is to gain a deeper understanding of biological processes by analyzing various data types simultaneously.

### Subdirectories

This repository is organized into subdirectories, each focusing on a specific data integration approach:

1. **01_Transcriptomics_Proteomics**: This directory contains the data integration pipeline and files for integrating mRNA (RNA-Seq) and proteomics data. The analysis leverages the MixOmics package to perform Data Integration Analysis for Biomarker discovery with Latent variabel Optimization (DIABLO).

2. **02_Transcriptomics_Proteomics_Epigenomics** (**In Development**): This directory will contain the data integration pipeline and files for integrating mRNA, proteomics, and DNA methylation data. The specific approach for this analysis is still under development.


### File Descriptions

The contents of each subdirectory may vary depending on the specific data integration approach. However, common file types you might encounter include:

* **R Markdown Script ( `.Rmd` )**: This file contains the code for data preprocessing, integration analysis, and visualization.
* **Data Files ( `.csv` or `.txt` )**: These files store the raw omics data, such as RNA-Seq counts, proteomics measurements, and DNA methylation levels.
* **Plots ( `.png` )**: These image files depict the results of the integration analysis, including heatmaps, network plots, and circos plots.

### Getting Started

To explore the data integration analysis for a specific subdirectory, follow these steps:

1. **Navigate to the subdirectory**: Use your terminal or file explorer to navigate to the directory of interest (e.g., `01_Transcriptomics_Proteomics`).
2. **Open the R Markdown script**: The R Markdown script (e.g., `JvRad_RNAseqProteomics_Integration.Rmd`) provides an overview of the analysis workflow and the code used. You can open this file in a text editor or an RStudio environment.
3. **Run the analysis (optional)**: If you have R and the required packages installed, you can run the code in the R Markdown script to reproduce the analysis and generate the plots.

### Additional Notes

* This repository is a work in progress, and the contents may be updated as the analysis evolves.
* Refer to the R Markdown script in each subdirectory for more details about the specific data integration approach used.
* If you have any questions or require further assistance, please refer to the relevant documentation for MixOmics or contact the repository owner.
