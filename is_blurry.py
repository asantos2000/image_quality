from asyncio import as_completed
import cv2
from skimage import filters, io
import os

from PIL import Image
import numpy as np

def sharpness(image_file, threshold=3.0):
    im = Image.open(image_file).convert('L') # to grayscale
    array = np.asarray(im, dtype=np.int32)
    gy, gx = np.gradient(array)
    gnorm = np.sqrt(gx**2 + gy**2)
    sharpness = np.average(gnorm)

    # less sharpness means more blurry
    if sharpness > threshold:
        return True, sharpness
    else:
        return False, sharpness

# Ref: https://learnopencv.com/image-quality-assessment-brisque/
def image_quality(image_file):
    img = cv2.imread(image_file)
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurScore = cv2.Laplacian(grey, cv2.CV_64F).var()
    score = cv2.quality.QualityBRISQUE_compute(img, "brisque_model_live.yml", "brisque_range_live.yml")
    return blurScore, score

def is_blurry(image_path, threshold=80):
    # Carregar a imagem
    image = cv2.imread(image_path)

    # Converter a imagem em escala de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calcular a variância Laplaciana da imagem
    variance = cv2.Laplacian(gray, cv2.CV_64F).var()

    #print(f'is_blurry: Variance is {variance}')

    # Verificar se a imagem é embaçada com base na variação da Laplaciana
    if variance > threshold:
        return True, variance
    else:
        return False, variance

def is_blurry2(image_path, threshold=0.5):
    # Carregar a imagem
    image = io.imread(image_path, as_gray=True)

    # Calcular o contraste da imagem
    contrast = filters.threshold_otsu(image)

    #print(f'is_blurry2: Contraste is {contrast}')

    # Verificar se a imagem é desfocada com base no contraste
    if contrast < threshold:
        return True, contrast
    else:
        return False, contrast

if __name__ == '__main__':

    diretorio = "images"

    # Listar todos os arquivos no diretório
    arquivos = os.listdir(diretorio)

    # Percorrer a lista de arquivos
    for arquivo in arquivos:
        # Verificar se o arquivo é um arquivo comum (não um diretório)
        image_file = os.path.join(diretorio, arquivo)
        if os.path.isfile(image_file):
            # blurry_state, grade = is_blurry(image_file)
            # if blurry_state:
            #     print(f'A imagem {image_file} é embaçada ({grade})')
            # else:
            #     print(f'A imagem {image_file} não é embaçada ({grade})')
            
            # sharp_state, grade = sharpness(image_file)
            # if sharp_state:
            #     print(f'A imagem {image_file} não é embaçada ({grade})')
            # else:
            #     print(f'A imagem {image_file} é embaçada ({grade})')

            blur_score, brisque_score = image_quality(image_file)
            print(f'Image quality: {image_file} has blur score: {blur_score} and brisque score: {brisque_score}')

