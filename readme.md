# Furry Detector

## Sumário

O sistema web criado tem como propósito criar uma forma de pessoas descobrirem se seus desenhos são "furries" ou não.
Para a criação do sistema foram utilizadas as bibliotecas de python: Keras para o reconhecimento das imagens, Numpy para calculos e Flask para criação da API. 

A seguir serão descritos o funcionamento do sistema, a metodologia empregada e os resultados obtidos.

## Casos de Uso

O sistema recebe como entrada um arquivo comprimido .zip contendo todas as imagens que o usuário quer que sejam avaliadas por ele. Em seguida o usuário deve clicar no botão confirmar para que os dados sejam enviados para o nosso servidor backend que será feito o processamento. Após um tempo de espera será disponibilizado na mesma pagina os resultados de cada imagem do arquivo zip que mostrarão o quão Furry o desenho enviado é.

## Metodologia

![Fluxograma](./fsi.png)

- Inicialmente a pagina web recebe um conjunto de imagens a serem processadas
- Em seguida as imagens são enviadas ao servidor
- As imagens são lidas e redimensionadas para 512 pixels por 512 pixels
- Os dados são enviados a uma rede neural convolucional
- O resultado da rede neural é uma porcentagem relacionada ao quão furry sua imagem é
- Esse resultado é enviado de volta a página web onde é mostrada para o usuário.

## 