# JvRAD Proteomics Analysis

This repository contains scripts and data for the JvRAD project, focused on proteomics analysis. The analysis workflow is implemented in R using various packages including DEP, dplyr, and SummarizedExperiment.

## Files and Descriptions

### JvRAD.Rmd
- **Description**: R Markdown file containing the entire workflow for the JvRAD proteomics analysis.

### enrichMKEGG.png
- **Description**: [PNG image](enrichMKEGG.png) displaying KEGG pathway enrichment analysis results using the `enrichMKEGG` function. This plot shows the enriched KEGG pathways and their associated statistics, helping to identify pathways that are significantly enriched among differentially expressed proteins.

### jvrad_cnetplot.png
- **Description**: [PNG image](jvrad_cnetplot.png) displaying network plots for enriched KEGG pathways using the `cnetplot` function. These plots provide a visual representation of the relationships between proteins within enriched pathways, aiding in the interpretation of pathway-level effects.

### jvrad_heatmap.png
- **Description**: [PNG image](jvrad_heatmap.png) displaying a heatmap with hierarchical clustering to visualize protein expression patterns across samples and replicates. This heatmap allows for the identification of clusters of proteins with similar expression patterns, highlighting potential biological trends or sample groupings.

### jvrad_keggEnrichPathways.png
- **Description**: [PNG image](jvrad_keggEnrichPathways.png) displaying KEGG pathway enrichment analysis results using the `enrichKEGG` function. This plot presents the enriched KEGG pathways and their associated statistics, helping to identify pathways that are significantly enriched among differentially expressed proteins.

### jvrad_key_protsSinglePlots.png
- **Description**: [PNG image](jvrad_key_protsSinglePlots.png) displaying single plots for selected proteins of interest. These plots provide detailed visualizations of the expression profiles of specific proteins across conditions and replicates, allowing for the examination of individual protein behavior.

### jvrad_volcanoPlot.png
- **Description**: [PNG image](jvrad_volcanoPlot.png) displaying a volcano plot to visualize differentially expressed proteins for a specific contrast. This plot highlights proteins that exhibit significant changes in expression between experimental conditions based on fold change and statistical significance.

### jvrad.png
- **Description**: Placeholder image.

### mmu05014.pathview.png
- **Description**: [PNG image](mmu05014.pathview.png) displaying pathway visualization for the mmu05014 pathway using the `pathview` function. This plot provides a graphical representation of the mmu05014 pathway, with differentially expressed proteins highlighted to illustrate their roles within the pathway.

### mmu05014.png
- **Description**: Placeholder image.

### mmu05014.xml
- **Description**: Placeholder XML file.

## Usage
To reproduce the analysis, follow the instructions in the `JvRAD.Rmd` file.
