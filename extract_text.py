from docling.document_converter import DocumentConverter

def convert_to_dict(source):
    converter = DocumentConverter()
    result = converter.convert(source)

# dictioanry is the same as json object
# exports the file as a dictionary, easy for nlp tasks
# Docling can parse tables within a document and provide content of every cell
# the content of the document metadata might be useful in developing  RAG Model, you might look into it later
    return result.document.export_to_dict()

docx = "https://calibre-ebook.com/downloads/demos/demo.docx"
pptx = "https://file-examples-com.github.io/uploads/2017/08/file_example_PPTX_500kB.pptx"
pdf = "https://arxiv.org/pdf/1708.08021.pdf"

result = convert_to_dict(docx)

print(result)

for i in result['texts']:
    print(i["orig"])  # print first 100 characters of each page

