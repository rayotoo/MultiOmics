
# Running lefse

# 1. Run  this in qiime2 environment
``
dokdo prepare-lefse \
    -t ./table-no-ecmu-hits-abund.qza \
    -x ./taxonomy.qza \
    -m ./JvSFN_diet-Metadata.tsv \
    -c TreatmentGroup \
    -o ./input_table.tsv \
``
