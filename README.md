# Trabalho-5
Trabalho sobre OpenCV com imagens

Esse trabalho visa mostrar algums exemplos da utilização da visão computacional utilizando 
a linguagem Python juntamente com a biblioteca OpenCV.

Exemplos de algumas instruções:

imagem = cv2.imread('caminho da sua imagem') / carrega a imagem desejada

cv2.imshow("Imagem", imgagem) / mostra a sua imagem

imagemRedimensionada = cv2.resize(imagem, (tamanho da largura, tamanho da altura)) / redimensiona o tamanho desejado da imagem

imagemCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) / transforma a imagem em cinza

cv2.imwrite('caminho da imagem', imagem) / salva a imagem processada

imagemFiltro = cv2.GaussianBlur(img, (3, 3), 0) / aplica o filtro Gaussiniano

imagemBordas = cv2.Canny(imagem, threshold1=100, threshold2=200) / marca as bordas,contornos na sua imagem. Obs: sua imagem tem que estar em cinza

