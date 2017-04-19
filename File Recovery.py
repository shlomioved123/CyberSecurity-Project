input_file = open("cyber_security_file_recovery","rb").read()
searching = True
header=""
trailer=""
file=""
PDFs = []
PNGs = []
for byte in input_file:
    #Searches for header
    if searching:
        header+=chr(byte)
        #print(header)
        if len(header) > 3:
            header = header[1:len(header)]

    if searching and (header == "PNG" or header == "PDF"):
        searching = False
        #print("Searching: ",searching)

    #Saves binary data while searches for trailer
    if not searching:
        trailer += chr(byte)
        if header == "PNG" and len(trailer) > 4:
            trailer = trailer[1:len(trailer)]
        elif header == "PDF" and len(trailer) > 3:
            trailer = trailer[1:len(trailer)]
        file += chr(byte)

        #If trailer is found, stops saving data file and adds it to appropriate list
        if (header == "PNG" and trailer == "IEND"):
            PNGs.append("‰PN"+file+"®B`,")
            print(len(PNGs) , "PNG files found")
            #Resets file, header, trailer, and continues searching
            file = ""
            header = ""
            trailer = ""
            searching = True
            
        elif (header == "PDF" and trailer == "EOF"):
            PDFs.append("%PD"+file)
            print(len(PDFs) , "PDF files found")
            file = ""
            header = ""
            trailer = ""
            searching = True
            
#Writes data to text file
output_file = open("Recovered Files", "wb")

for file in PDFs:
    output_file.write(str.encode(file))

for file in PNGs:
    output_file.write(str.encode(file))

output_file.close()

print("PNGs and PDFs recovered and saved to 'Recovered Files'")
