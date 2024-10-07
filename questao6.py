# 6. Transformações Geométricas e Operações Aritméticas: Implementar rotacionamento
# , translação e operações como soma e subtração de imagens.
#importando as bibliotecas
import cv2
import numpy

#carregando as imagens
img = cv2.imread('img/imagem5.jpg')
img2 = cv2.imread('img/imagem6.jpg')

cv2.imshow("Imagem 1 Normal", img)
cv2.imshow("Imagem 2 Normal", img2)


# Aqui começa a rotação
#altura (height) e largura (width) da imagem / dois valores da imagem
(h, w) = img.shape[:2]

#calcula o centro da imagem para a rotação com a divisão
# da altura e largura da imagem por 2
centro = (w // 2, h // 2)

#gira/rotaciona a imagem em 90 graus
anguloRotacao = 90.0
#mantém o tamanho da imagem normal
escala = 1.0

#rotacao da matrix
rotacaoMatrix = cv2.getRotationMatrix2D(centro, anguloRotacao, escala)

#aplica a rotação
imgRotacao = cv2.warpAffine(img, rotacaoMatrix, (w, h))



# Aqui começa a translação

# a imagem será movida 100 pixels para direita(tx) e 100 pixels
# para baixo(ty)
tx, ty = 100, 100

#define a matrix de translação de como a imagem será deslocada (x e y)
matrixTranslação = numpy.float32([[1, 0, tx], [0, 1, ty]])

# aplica a translação a imagem
imgTranslação = cv2.warpAffine(img, matrixTranslação, (w, h))

#mostra a imagem com rotação
cv2.imshow("Imagem 1 com Rotacao de 90 Graus", imgRotacao)

#mostra a imagem com translação
cv2.imshow("Imagem 1 com Translacao", imgTranslação)



# Aqui começa a soma das imagens

#somando as duas imagens
somaImgs = cv2.add(img, img2)

# mostrando a soma das duas imagens
cv2.imshow("Soma das duas imagens", somaImgs)

#sobre a questao 9, nao da para salvar dessa forma pois
# a imagem foi gerada aqui
# cv2.imwrite()

cv2.waitKey(0)

cv2.destroyAllWindows