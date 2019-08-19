#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)
gc_cont<- read.table(args[1], header=TRUE,
                                sep = "\t",
                                row.names = 1,
                               as.is=TRUE)



A<-rownames(gc_cont)
gsub("\\|",">", A[1])->a
b<-strsplit(a,">")[[1]]

cat(c(c(b[2],mean(gc_cont$X..GCContent),"\n")))


