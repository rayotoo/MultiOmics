# JvRAD mRNA and Proteomics Data Integration with MixOmics

- This repository contains scripts and data for the JvRAD project, focused on Data Integration analysis. The analysis workflow is implemented in R using the Diablo toolkit from the MixOmics package.

## Files and Descriptions

### JvRAD.Rmd
- **Description**: R Markdown file containing the entire workflow for the JvRAD proteomics analysis.


## CircosPlot 

![CircosPlot](circos_plot.png)

- Circular plot visualizing the relationships between mRNA and protein data, aiding in the exploration of potential co-regulations or correlations.

### jvrad_cnetplot.png
## CNet Plot
![CNet Plot](jvrad_cnetplot.png)

- Displaying network plots for enriched KEGG pathways using the `cnetplot` function. These plots provide a visual representation of the relationships between proteins within enriched pathways, aiding in the interpretation of pathway-level effects.

### jvrad_heatmap.png

## Heatmap
![Heatmap](jvrad_heatmap.png)

- Displaying a heatmap with hierarchical clustering to visualize protein expression patterns across samples and replicates. This heatmap allows for the identification of clusters of proteins with similar expression patterns, highlighting potential biological trends or sample groupings.


## KEGG Enrichment Pathways
![KEGG Enrichment Pathways](jvrad_keggEnrichPathways.png)

- Displaying KEGG pathway enrichment analysis results using the `enrichKEGG` function. This plot presents the enriched KEGG pathways and their associated statistics, helping to identify pathways that are significantly enriched among differentially expressed proteins.


## Key Proteins Single Plots
![Key Proteins Single Plots](jvrad_key_protsSinglePlots.png)

- Displaying single plots for selected proteins of interest. These plots provide detailed visualizations of the expression profiles of specific proteins across conditions and replicates, allowing for the examination of individual protein behavior.


## Volcano Plot
![Volcano Plot](jvrad_volcanoPlot.png)

- Displaying a volcano plot to visualize differentially expressed proteins for a specific contrast. This plot highlights proteins that exhibit significant changes in expression between experimental conditions based on fold change and statistical significance.


## JvRAD Plot
![JvRAD Plot](jvrad.png)

## JvRAD R Markdown File
[JvRAD.Rmd](JvRAD.Rmd)

## Pathview Plot
![Pathview Plot](mmu05014.pathview.png)

- Displaying pathway visualization for the mmu05014 pathway using the `pathview` function. This plot provides a graphical representation of the mmu05014 pathway, with differentially expressed proteins highlighted to illustrate their roles within the pathway.


## Pathview Image
![Pathview Image](mmu05014.png)

-  **Description**: Placeholder image.

## Pathview XML File
[Pathview XML File](mmu05014.xml)

- **Description**: Placeholder XML file.
