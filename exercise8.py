import pypdf as p
reader=p.PdfReader('CSI members.pdf')
print(len(reader.pages))