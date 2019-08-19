#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)
library(pheatmap)
library(RColorBrewer)
library(ggplot2)


# geneExp <- read.table("z_final_data_FC_heatmap.tab", header=T, sep="\t")

#geneExp <- as.matrix(read.table("~/Desktop/ncRNAs_Leishmania_spp/clustering_nc/Leishmania_nc.clstr.strain_binary_matrix", header=TRUE,
#                                sep = "\t",
#                              row.names = 1,
#                              as.is=TRUE))




geneExp <- as.matrix(read.table(args[1], header=TRUE,
                                sep = "\t",
                                row.names = 1,
                                as.is=TRUE))



  #geneExp_log <- log2(geneExp)
  #APLICA LOG10 a toda la matriz (solamente los numeros deben estar en la matriz)
  #geneExp_log[geneExp_log==-Inf] <- 0 
  
# write.table(geneExp_log, "z_geneExp_log2_v3.tab", sep="\t") 
# pheatmap(geneExp_log2, show_rownames = F, cluster_cols = F, 
#         cellwidth = 7, cellheight = 1.5, fontsize = 8, filename = "test.pdf")
  

my_sample_col2 <- data.frame(c(subgenera = rep(c("Leishmania", "Viannia", "Unknown", "LenrComplex", "Sauroleishmania"), c(16,6,2,1,1))),
                             c(disease_type=c("CL","CL","ND","VL","VL","VL","VL","ND","VL","VL","CL","CL","CL","CL","CL","CL","MCL","MCL",
                                              "CL","CL","CL","CL","ND","ND","ND","ND")))
rownames(my_sample_col2)<- c("LaetL147", "LamaM2269", "LaraLEM1108", "LdonAG83", "LdonBHU1220", "LdonBPK282A1", 
                             "LdonPasteur", "LgerLEM452","LinfJPCM5","LinfTR01","LmajFriedlin","LmajLV39c5","LmajSD75","LmexU1103","LtroL590","LturLEM423",
                             "LbraM2903","LbraM2904","LpanL13","LpanPSC1","LperLEM1537",
                             "LperPAB4377","LspLD974","LspLEM2494","LenrLEM3045","LtarParTarII")
colnames(my_sample_col2) <- c("subgenera","disease_type")
my_colour = list(subgenera=c(Leishmania="#1a5276",Viannia="#ff7f00", Unknown ="#d4ac0d", LenrComplex="#641e16",
                             Sauroleishmania= "#16a085"),
                disease_type= c(CL ="#e41a1c",VL="#377eb8",MCL="#4daf4a",ND="#984ea3"))

breaks=c(0,1)
pheatmap(geneExp,
        annotation_colors = my_colour,
        annotation_col = my_sample_col2,
        show_rownames = F,
        cluster_cols = T,
        cluster_rows = T, 
        legend = T,
        treeheight_row = 0,
        scale = "column",
        color = colorRampPalette(c("#8c510a", "#35978f"),space= "Lab")(2),
        legend_breaks = breaks,
        legend_labels = c("absence","presence"),
        cellwidth = 10, cellheight = 0.1, fontsize = 8, 
        border_color = "black",
        filename = "binary_heatmap.pdf")

# cellheight : Altura de cada cuadrado
# cellwidth : Ancho de cada cuadrado

#pheatmap(geneExp, cellwidth = 30, cellheight = 24, fontsize = 8, filename = "test.pdf")
