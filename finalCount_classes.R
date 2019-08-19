#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

count_clases<-(read.table(args[1], header=TRUE,
                                sep = "\t",
#                              row.names = 1,
                              as.is=TRUE))

specie<-colnames(count_clases)[1]

suma<-sum(count_clases$count)
cat(c(c(specie,suma),"\n"))