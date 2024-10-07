# 7. Operações Morfológicas: Usar erosão e dilatação.
#importando as bibliotecas
import cv2
import numpy

#Aqui é a parte da erosão / remove ruídos

#carregando a imagem
img = cv2.imread('img/imagem7.jpg')

#mostrando a imagem original
cv2.imshow("Imagem Normal", img)

#kernel é usada para operação de erosão, aqui é
# matrix 3x5
kernel = numpy.ones((3, 5), numpy.uint8)

#aplica a erosão, iterations é quantidade de vezes
# que a erosão é aplicada
imgErosao = cv2.erode(img, kernel, iterations=1)

#mostra a imagem com a erosão
cv2.imshow("Imagem com Erosao", imgErosao)


#Aqui é a parte da dilatação / restaura o tamanho original após a erosão

#aplicando a dilatação na imagem
imgDilatada = cv2.dilate(img, kernel, iterations=1)

#mostrando a imagem dilatada
cv2.imshow("Imagem com Dilatacao", imgDilatada)

#salvando a imagem (questao9)
cv2.imwrite('img/imagem7.jpg', img)

cv2.waitKey(0)

cv2.destroyAllWindows