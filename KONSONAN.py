r1=open("C:/Users/NOVO/Downloads/Hitung Huruf Vokal.txt","r")
r2=r1.read()
r1.close()
def jumlah(huruf):
	output=0
	Konsonan =['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
	for a in huruf:
		if a in konsonan:
			output +=1
	return output
	
def get_huruf_konsonan(huruf):
	output = 0
	for a in huruf.lower().split(" "):
		output += jumlah(a)
	return output
	
a1= get_huruf_konsonan(r2)
print(f"jumlah huruf Konsonan : {a1}")
