import sys
name = sys.argv[1]
file = open(name,"r")
lista1=[]
for line in file:
	if "Unclassified" not in line:		
		aux= line[0:-1].split("\t")
		aux2= aux[3].split(";")
		if "miRNA" in aux2 and "sRNA" in aux2 and "transcript" in aux2:
			define="miRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "miRNA" in aux2 and "rRNA" in aux2: 
			define=""
			if"tRNA" in aux2: 
				define= "Unclassified"
			else:
				define="rRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)	
		elif "miRNA" in aux2 and "tRNA" in aux2: 
			define="tRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "CD-box" in aux2 and "snoRNA" in aux2:
			define="CD-box"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "HACA-box" in aux2 and "snoRNA" in aux2:
			define="HACA-box"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "piRNA" in aux2 and "sRNA" in aux2:
			define = ""
			if "miRNA"in aux2:
				define = "miRNA"
			else:
				define="piRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "sRNA" in aux2 and "transcript" in aux2: 
			define="sRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "miRNA"in aux2 and "siRNA/RNAi" in aux2:
			define="miRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "miRNA" in aux2 and "transcript" in aux2: 
			define="miRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "piRNA" in aux2 and "transcript" in aux2: 
			define="piRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "rRNA,sRNA" in aux2 and "sRNA" in aux2:
			define="rRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "sRNA" in aux2 and "siRNA/RNAi" in aux2:
			define="sRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "miRNA" in aux2 and "piRNA" in aux2: 
			define="miRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "rRNA" in aux2 and "sRNA" in aux2: 
			define="rRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "transcript" in aux2:
			define=""
			if "sRNA" in aux2:
				define="sRNA"
			else:
				define="Unclassified"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "rRNA,sRNA" in aux2 and "rRNA" in aux2:
			define="rRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "piRNA" in aux2 and "tRNA" in aux2: 
			define="tRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "piRNA" in aux2 and "rRNA" in aux2: 
			define="rRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "piRNA" in aux2 and "siRNA/RNAi" in aux2: 
			define="piRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "miRNA" in aux2 and "sRNA" in aux2: 
			define= "miRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "rRNA" in aux2 and "tRNA" in aux2: 
			define= "Unclassified"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "snRNA" in aux2 and "splicing" in aux2:
			define= "snRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "rRNA,sRNA" in aux2 and "siRNA/RNAi" in aux2:
			define= "rRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "rRNA,sRNA" in aux2:
			define= "rRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "siRNA/RNAi" in aux2: 
			define="siRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "rRNA" in aux2 and "siRNA/RNAi" in aux2:
			define="rRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "sRNA" in aux2 and "snoRNA" in aux2:	
			define="snoRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "sRNA" in aux2 and "tRNA" in aux2:
			define="tRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "miRNA" in aux2 and "rRNA" in aux2:
			define="rRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "sRNA" in aux2 and "snoRNA" in aux2:
			define="snoRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "miRNA,rRNA" in aux2:
			define="rRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "piRNA" in aux2 and "snoRNA" in aux2:
			define="snoRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "Cis-reg" in aux2 and "miRNA" in aux2: 
			define="Cis-reg"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "Cis-reg" in aux2 and "piRNA" in aux2: 
			define="Cis-reg"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "Cis-reg" in aux2 and "rRNA" in aux2:
			define="rRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "IRES" in aux2 and "miRNA" in aux2: 
			define="IRES"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "miRNA" in aux2 and "snoRNA" in aux2: 
			define="snoRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "lncRNA" in aux2 and "tRNA" in aux2:
			define="lncRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "rRNA"  in aux2 and "snoRNA" in aux2: 
			define="rRNA" 
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "rRNA" in aux2 and "siRNA" in aux2: 
			define="rRNA" 
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "piRNA,miRNA" in aux2: 
			define="miRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "sRNA"in aux2 and "siRNA" in aux2: 
			define="sRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "lncRNA" in aux2 and "sRNA" in aux2: 
			define="lncRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "Cis-reg" in aux2 and "sRNA" in aux2:
			define="Cis-reg"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "tRNA,miRNA" in aux2:
			define="tRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "Gene" in aux2: 
			define="Unclassified" 
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
		elif "miRNA" in aux2 and "miRNA,piRNA" in aux2: 
			define="miRNA"
			print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+define)
			
	
			
			
			
			
			
			
			
			
		else:
			print(line[:-1])
		
