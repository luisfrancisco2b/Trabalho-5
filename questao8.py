# 8. Segmentação e Análise de Imagens: Implementar técnicas como Watershed.

import cv2
import numpy

#carregei a imagem
img = cv2.imread('img/imagem8.jpg')
cv2.imshow("Imagem normal", img)

# converti para cinza
imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# limiarizar com o treshold
limiramizar, binarizar = cv2.threshold(imgCinza, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

#usando o kernel para operações morfológicas
kernel = numpy.ones((3, 3), numpy.uint8)

# usando a erosão para remover ruídos
ErosaoImg = cv2.erode(binarizar, kernel, iterations=1)

# Aplicando o algoritmo Watershed
dist_transform = cv2.distanceTransform(ErosaoImg, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
sure_fg = numpy.uint8(sure_fg)
unknown = cv2.subtract(ErosaoImg, sure_fg)

# Marcar os componentes conectados
ret, marcas = cv2.connectedComponents(sure_fg)

# Aumentar os marcadores para que o fundo seja 1
marcas = marcas + 1
marcas[unknown == 255] = 0

# Aplicar o Watershed
marcas = cv2.watershed(img, marcas)

# marcando as bordas com vermelho
img[marcas == -1] = [0, 0, 255]



# mostrando a imagem com a segmentação
cv2.imshow("Mostrando a imagem com a segmentacao Watershed", img)

#salvando a imagem (questao9)
cv2.imwrite('img/imagem8.jpg', img)

cv2.waitKey(0)

cv2.destroyAllWindows()

