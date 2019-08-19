library(UpSetR)

data <- read.table("Leishmania_nc.clstr.strain_binary_matrix", header=T,sep="\t",row.names = 1)


upset(data, sets = c("LaetL147","LamaM2269","LaraLEM1108","LbraM2903","LbraM2904","LdonAG83","LdonBHU1220","LdonBPK282A1","LdonPasteur","LenrLEM3045","LgerLEM452","LinfJPCM5","LinfTR01","LmajFriedlin","LmajLV39c5","LmajSD75","LmexU1103","LpanL13","LpanPSC1","LperLEM1537","LperPAB4377","LspLD974","LspLEM2494","LtarParTarII","LtroL590","LturLEM423"),
      mb.ratio = c(0.55, 0.45), order.by = "freq")
