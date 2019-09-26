import sys
name = sys.argv[1]
file = open(name,"r")
lista1=[]
diccionario = {}
f = open("/home/lalo/Desktop/ncRNAs_Leishmania_spp/struct_search/all_families_rfam.list","r")
for line in f:
	aux = line[:-1].split("\t")
	diccionario[aux[0]] = aux[1]
f.close()

for line in file:
		aux= line[0:-1].split("\t")
		rf= aux[3].split("_")[-1]
		define="" 
		print (aux[0]+"\t"+aux[1]+"\t"+aux[2]+"\t"+diccionario[rf]+"\t"+aux[4]+"\t"+aux[5])
		
