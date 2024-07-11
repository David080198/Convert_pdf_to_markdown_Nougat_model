#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install -q pymupdf python-Levenshtein nltk')
get_ipython().system('pip install -q git+https://github.com/huggingface/transformers.git')


# In[2]:


get_ipython().system('pip install transformers')


# In[3]:


from transformers import AutoProcessor, VisionEncoderDecoderModel
import torch

from huggingface_hub import hf_hub_download
from typing import Optional, List
import io
import fitz
from pathlib import Path
from PIL import Image

# Load the Nougat model and processor from the hub
processor = AutoProcessor.from_pretrained("facebook/nougat-small")
model = VisionEncoderDecoderModel.from_pretrained("facebook/nougat-small")


# In[4]:


get_ipython().run_cell_magic('capture', '', 'device = "cuda" if torch.cuda.is_available() else "cpu"\nmodel.to(device)\n')


# In[5]:


from typing import Optional, List
import io
import fitz
from pathlib import Path

def rasterize_paper(
    pdf: Path,
    outpath: Optional[Path] = None,
    dpi: int = 96,
    return_pil=False,
    pages=None,
) -> Optional[List[io.BytesIO]]:
    """
    Rasterize a PDF file to PNG images.

    Args:
        pdf (Path): The path to the PDF file.
        outpath (Optional[Path], optional): The output directory. If None, the PIL images will be returned instead. Defaults to None.
        dpi (int, optional): The output DPI. Defaults to 96.
        return_pil (bool, optional): Whether to return the PIL images instead of writing them to disk. Defaults to False.
        pages (Optional[List[int]], optional): The pages to rasterize. If None, all pages will be rasterized. Defaults to None.

    Returns:
        Optional[List[io.BytesIO]]: The PIL images if `return_pil` is True, otherwise None.
    """

    pillow_images = []
    if outpath is None:
        return_pil = True
    try:
        if isinstance(pdf, (str, Path)):
            pdf = fitz.open(pdf)
        if pages is None:
            pages = range(len(pdf))
        for i in pages:
            page_bytes: bytes = pdf[i].get_pixmap(dpi=dpi).pil_tobytes(format="PNG")
            if return_pil:
                pillow_images.append(io.BytesIO(page_bytes))
            else:
                with (outpath / ("%02d.png" % (i + 1))).open("wb") as f:
                    f.write(page_bytes)
    except Exception:
        pass
    if return_pil:
        return pillow_images


# In[6]:


from transformers import StoppingCriteria, StoppingCriteriaList
from collections import defaultdict

class RunningVarTorch:
    def __init__(self, L=15, norm=False):
        self.values = None
        self.L = L
        self.norm = norm

    def push(self, x: torch.Tensor):
        assert x.dim() == 1
        if self.values is None:
            self.values = x[:, None]
        elif self.values.shape[1] < self.L:
            self.values = torch.cat((self.values, x[:, None]), 1)
        else:
            self.values = torch.cat((self.values[:, 1:], x[:, None]), 1)

    def variance(self):
        if self.values is None:
            return
        if self.norm:
            return torch.var(self.values, 1) / self.values.shape[1]
        else:
            return torch.var(self.values, 1)
            
class StoppingCriteriaScores(StoppingCriteria):
    def __init__(self, threshold: float = 0.015, window_size: int = 200):
        super().__init__()
        self.threshold = threshold
        self.vars = RunningVarTorch(norm=True)
        self.varvars = RunningVarTorch(L=window_size)
        self.stop_inds = defaultdict(int)
        self.stopped = defaultdict(bool)
        self.size = 0
        self.window_size = window_size

    @torch.no_grad()
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor):
        last_scores = scores[-1]
        self.vars.push(last_scores.max(1)[0].float().cpu())
        self.varvars.push(self.vars.variance())
        self.size += 1
        if self.size < self.window_size:
            return False

        varvar = self.varvars.variance()
        for b in range(len(last_scores)):
            if varvar[b] < self.threshold:
                if self.stop_inds[b] > 0 and not self.stopped[b]:
                    self.stopped[b] = self.stop_inds[b] >= self.size
                else:
                    self.stop_inds[b] = int(
                        min(max(self.size, 1) * 1.15 + 150 + self.window_size, 4095)
                    )
            else:
                self.stop_inds[b] = 0
                self.stopped[b] = False
        return all(self.stopped.values()) and len(self.stopped) > 0
     


# In[7]:


from PyPDF2 import PdfReader

def contar_paginas(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        num_paginas = len(reader.pages)
    return num_paginas
    
filepath = r"F:\nuevo_conocimiento\Alex Project\Aceptados\Texto (1).pdf"
num_paginas = contar_paginas(filepath)
print("El número de páginas del PDF es:", num_paginas)

texto_final = ""
for i in range(0, num_paginas):
    filepath = r"F:\nuevo_conocimiento\Alex Project\Aceptados\Texto (1).pdf"
    images = rasterize_paper(pdf=filepath, return_pil=True)
    image = Image.open(images[i])
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    outputs = model.generate(
        pixel_values.to(device),
        min_length=1,
        max_length=3584,
        bad_words_ids=[[processor.tokenizer.unk_token_id]],
        return_dict_in_generate=True,
        output_scores=True,
        stopping_criteria=StoppingCriteriaList([StoppingCriteriaScores()]),
    )
    generated = processor.batch_decode(outputs[0], skip_special_tokens=True)[0]
    generated = processor.post_process_generation(generated, fix_markdown=False)
    #print(generated)
    texto_final = texto_final + generated
print(texto_final)


# In[13]:


def contar_paginas(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        num_paginas = len(reader.pages)
    return num_paginas

def read_and_convert_pdf(title):
    print(f"Procesando texto: {title}")
    text = "F:\\nuevo_conocimiento\\Alex Project\\Aceptados\\"
    ruta = text + title
    num_paginas = contar_paginas(ruta)
    print(f"El número de páginas del PDF {title} es: {num_paginas}")
    texto_final = ""
    for i in range(0, num_paginas):
        images = rasterize_paper(pdf=ruta, return_pil=True)
        image = Image.open(images[i])
        pixel_values = processor(images=image, return_tensors="pt").pixel_values
        outputs = model.generate(
            pixel_values.to(device),
            min_length=1,
            max_length=3584,
            bad_words_ids=[[processor.tokenizer.unk_token_id]],
            return_dict_in_generate=True,
            output_scores=True,
            stopping_criteria=StoppingCriteriaList([StoppingCriteriaScores()]),
        )
        generated = processor.batch_decode(outputs[0], skip_special_tokens=True)[0]
        generated = processor.post_process_generation(generated, fix_markdown=False)
        #print(generated)
        texto_final = texto_final + generated

    return texto_final


# In[6]:


import os
from PyPDF2 import PdfReader
from tqdm import tqdm
import pandas as pd

# Ruta del directorio que deseas listar
directorio = "F:\\nuevo_conocimiento\\Alex Project\\Aceptados"

# Lista los archivos en el directorio
archivos = os.listdir(directorio)
print("Lista_de_archivos")
print(archivos)


# In[5]:


# Imprime el nombre de cada archivo
titulos_pdf = [archivo for archivo in archivos if archivo.lower().endswith('.pdf')]
print(titulos_pdf)


# In[16]:


print(titulos_pdf[42])


# In[17]:


lista_de_textos = []
i = 1
nuevo_directorio = "F:\\nuevo_conocimiento\\Alex Project\\markdown_text\\"

for archivo in tqdm(titulos_pdf[43:], desc="Procesando pdf"):
        result = read_and_convert_pdf(archivo)

        nombre_sin_extension = os.path.splitext(archivo)[0]
        nombre_archivo = nombre_sin_extension + ".md"
        ruta_archivo = nuevo_directorio + nombre_archivo
        # Escribir el texto en el archivo
        with open(ruta_archivo, "w",encoding='utf-8') as archivo:
            archivo.write(result)

        print(result)
        lista_de_textos.append(result)


# In[18]:


print(len(lista_de_textos))


# In[19]:


import re
 
#print(lista_de_textos[0])
patron = r'#+\s+(.*)'

resultados_finales = []
for i in range(len(lista_de_textos)):
    resultados_finales.append(re.findall(patron, lista_de_textos[i]))
    
print(resultados_finales[0])
    
for texto in resultados_finales:
    print(texto)


# In[28]:


def eliminar_contenido_entre_tablas(texto):
    # Definir la expresión regular para encontrar el contenido entre \begin{table} y \end{table}
    patron = re.compile(r'\\begin\{table\}.*?\\end\{table\}', re.DOTALL)
    
    # Sustituir el contenido encontrado por una cadena vacía
    texto_limpio = re.sub(patron, '', texto)
    
    return texto_limpio

def texto_separar_informacion(texto,inicio,fin):
    inicio_abstract = texto.find(inicio)
    fin_abstract = texto.find(fin)
    if inicio_abstract != -1 and fin_abstract != -1:
        # Extraer el texto entre el abstract y el contenido
        texto_entre_secciones = texto[inicio_abstract + len(inicio):fin_abstract]
        #print(texto_entre_secciones.strip())
        return texto_entre_secciones
    else:
        x = 0

def ultima_seccion(texto,inicio):
    inicio_abstract = texto.find(inicio)
    if inicio_abstract != -1:
        # Extraer el texto entre el abstract y el contenido
        texto_entre_secciones = texto[inicio_abstract + len(inicio):]
        #print(texto_entre_secciones.strip())
        return texto_entre_secciones
    else:
        x = 0

texto_entre_secciones = {}
#print(len(resultados_finales[0]))

#texto_sin_tablas = eliminar_contenido_entre_tablas(lista_de_textos[0])
lista_de_elementos = {}
conteo = 0

for texto in tqdm(lista_de_textos, desc="Separando texto"):
    print(f"Procesando texto numero {conteo}")
    texto_sin_tablas = eliminar_contenido_entre_tablas(texto)
    for i in range(len(resultados_finales[conteo])):
        if i != len(resultados_finales[conteo])-1:
            #print("***************************************")
            #print(f"Procesando: {resultados_finales[conteo][i]}")
            #print(f"Procesando: {resultados_finales[conteo][i+1]}")
            texto_entre_secciones[resultados_finales[conteo][i]] = texto_separar_informacion(texto_sin_tablas,resultados_finales[conteo][i],resultados_finales[conteo][i+1])
        elif i == len(resultados_finales[conteo])-1:
            #print("***************************************")
            #print(f"Procesando final: {resultados_finales[conteo][i]}")
            texto_entre_secciones[resultados_finales[conteo][i]] = ultima_seccion(texto_sin_tablas,resultados_finales[conteo][i])
    conteo += 1
    dic_name = titulos_pdf[conteo]
    lista_de_elementos[dic_name] = texto_entre_secciones
    texto_entre_secciones = {}


# In[29]:


for clave in lista_de_elementos.keys():
    print("Clave:", clave)
#    print("Texto:", texto_entre_secciones[clave])


# In[ ]:


print(lista_de_elementos["Texto_12"])


# In[23]:


import json
# Guardar el diccionario en un archivo JSON
with open("diccionario_textos.json", "w") as archivo:
    json.dump(lista_de_elementos, archivo)


# In[ ]:




