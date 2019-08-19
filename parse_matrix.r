#!/usr/bin/env Rscript

#usage Rscript	--vanilla parse_matrix.r input_matrix.file  
# input file count matrix 


args = commandArgs(trailingOnly=TRUE)


df <- read.delim(args[1],header = T,row.names ="Cluster")

df$X.conserved<- NULL
df$Classes<-NULL
df2<-data.matrix(df)
df2[df2 > 0] = 1
write.table(df2,file="~/Desktop/ncRNAs_Leishmania_spp/clustering_nc/Leishmania_nc.clstr.strain_binary_matrix",sep = "\t")
