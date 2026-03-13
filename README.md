# Projeto
Uso de IA local para leitura de arquivo com o propósito de gerar respota com base no documento de texto enviado.

# Funcionamento
O projeto faz a leitura de um arquivo e gera o mapa de vetores usando mxbai-embed-large que será servido como contexto a geração da respota
do modelo llama, caso não haja arquivo ou a pergunda escape a especificação dada ele responderá com um mensagem emgraçada do tema instruído, no prompt atual ele tentará auxiliar na leitura de um limbro de clean code mas pode ser alterado a vontade.

# Modelo
- Embedding: mxbai-embed-large  
- LLM: llama3.2


<img src=.github/page.png />
