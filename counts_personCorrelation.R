#!/usr/bin/env Rscript

#usage of this script 

# Rscript --vanilla Script.R input.file outfile.pdf

args = commandArgs(trailingOnly=TRUE)

# make a dataframe of normalized counts 
rlog.norm.counts<- read.csv(args[1],sep = "\t", header = T, row.names = 1)

#cor() calculates the correlation between columns of a matrix
distance.m_rlog <- as.dist(1 - cor(rlog.norm.counts, method = "pearson"))

#open a pdf file
pdf(args[2]) 

#plot() can directly interpret the output of hclust()
plot( hclust(distance.m_rlog),
      labels = colnames(rlog.norm.counts),
      main  ="rlog transformed read counts\ndistance: Pearson correlation")


# Close the pdf file
dev.off() 
