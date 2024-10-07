# 1. Configuração do Ambiente: Instalar Python e a biblioteca OpenCV.
# 2. Leitura e Exibição de Imagens: Criar um script para carregar e exibir imagens.

# importando a biblioteca
import cv2

# carregando a imagem
img = cv2.imread('img/imagem1.jpeg')

#mostrando a imagem
cv2.imshow("Imagem", img)

#salvando a imagem (questao9)
cv2.imwrite('img/imagem1.jpeg', img)

#esperando digitar qualquer tecla para fechar as janelas
cv2.waitKey(0)

#fecha todos as janelas
cv2.destroyAllWindows