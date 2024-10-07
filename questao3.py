# 3. Implementação de Pré-processamento de Imagens: Adicionar a funcionalidade de 
# converter e redimensionar imagens.

# importando a biblioteca
import cv2

# carregando a imagem
img = cv2.imread('img/imagem2.webp')

#mostrando a imagem normal
cv2.imshow("Imagem Normal", img)

#convertendo a imagem para cinza
imgConvertidaCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#mostarndo a imagem em cinza
cv2.imshow("Imagem em Cinza", imgConvertidaCinza)

#redimensionando a imagem / largura e altura
imgCortada = cv2.resize(img, (600, 300))

#salvando a imagem (questao9)
cv2.imwrite('img/imagem2.webp', imgCortada)

#mostrando a imagem redimensionada
cv2.imshow("Imagem Cortada", imgCortada)

cv2.waitKey(0)

cv2.destroyAllWindows