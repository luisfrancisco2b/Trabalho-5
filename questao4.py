# 4. Aplicação de Filtros: Implementar filtros como GaussianBlur, Canny, Sobel

# importando a biblioteca
import cv2

# carregando a imagem
img = cv2.imread('img/imagem3.webp')

#mostrando a imagem
cv2.imshow('Imagem Sem Filtro', img)

#colocando o filtro gaaussiniano na imagem
imagemFiltro =  cv2.GaussianBlur(img, (3, 3), 0)

#mostrando a imagem com o filtro gaaussiniano
cv2.imshow("Imagem Com Filtro Gaussiniano", imagemFiltro)

#salvando a imagem (questao9)
cv2.imwrite('img/imagem3.webp', imagemFiltro)

cv2.waitKey(0)

cv2.destroyAllWindows