# 5. Detecção de Características: Usar detectores de cantos e contornos.
# importando a biblioteca
import cv2

# carregando a imagem
img = cv2.imread('img/imagem4.webp')

# aqui tive que recortar a imagem que escolhi porque ela é muito grande*
imgRecortada = cv2.resize(img, (500, 300))

#mostrando a imagem sem contorno
cv2.imshow("Imagem Sem Contorno", imgRecortada)

#tem transformar em cinza para colocar as bordas/contornos
imgCinza = cv2.cvtColor(imgRecortada, cv2.COLOR_RGB2GRAY)

#marcando as bordas/contornos da imagem
imgBorda = cv2.Canny(imgCinza, threshold1=100, threshold2=200)

#mostrando a imagem com as bordas/contornos
cv2.imshow("Imagem Com Contorno", imgBorda)

#salvando a imagem (questao9)
cv2.imwrite('img/imagem4.webp', imgBorda)

cv2.waitKey(0)

cv2.destroyAllWindows