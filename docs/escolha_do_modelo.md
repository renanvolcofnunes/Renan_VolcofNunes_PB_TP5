# Escolha do Modelo LLM

## Modelo escolhido

O modelo utilizado no projeto foi o `Qwen/Qwen2.5-1.5B-Instruct`, executado localmente com PyTorch e Transformers.

## Critérios utilizados

A escolha considerou três critérios principais: desempenho para a tarefa de resumo, custo computacional local e possibilidade de execução sem depender de uma API externa.

## Desempenho

O modelo foi testado com um texto relacionado à empregabilidade jovem e produziu um resumo coerente com as informações apresentadas.

No computador utilizado no desenvolvimento, uma inferência medida levou aproximadamente 19,19 segundos.

Para o projeto, esse tempo foi considerado aceitável porque o processamento ocorre localmente e a tarefa principal é resumir textos enviados pelo usuário.

## Comparação com uma alternativa

Como alternativa foi considerado o `Qwen/Qwen2.5-0.5B-Instruct`, modelo menor da mesma família.

O Qwen2.5-0.5B-Instruct possui aproximadamente 0,5 bilhão de parâmetros, contra aproximadamente 1,5 bilhão do modelo escolhido. Por possuir menos parâmetros, tende a exigir menos recursos computacionais, sendo uma alternativa interessante para máquinas com menor quantidade de memória.

Por outro lado, o modelo de 1.5B possui maior capacidade de processamento de instruções e geração de texto. Como o computador utilizado possui memória suficiente para executá-lo, foi possível priorizar a capacidade do modelo em vez de escolher apenas a opção de menor tamanho.

Não foi realizado no projeto um benchmark completo entre os dois modelos utilizando exatamente o mesmo conjunto de textos. Por isso, não são apresentados números de desempenho da alternativa como se fossem medições realizadas neste computador.

## Parâmetros e custo computacional

O modelo escolhido pertence à classe de aproximadamente 1,5 bilhão de parâmetros.

O projeto utiliza o modelo em `float32`, com execução em CPU.

O ambiente utilizado possui aproximadamente 15,91 GB de memória RAM.

O download local realizado ocupou aproximadamente 3,10 GB.

O uso de `float32` aumenta o consumo de memória em relação a formatos de menor precisão, porém apresentou compatibilidade com a CPU utilizada no projeto.

Modelos maiores poderiam aumentar ainda mais o consumo de memória e o tempo de processamento. Já um modelo menor, como o Qwen 0.5B, seria um plano alternativo caso o hardware não suportasse o modelo escolhido.

## Acessibilidade local

O modelo pode ser baixado previamente e executado localmente com PyTorch e Transformers.

O download é realizado pelo script:

`python -m src.baixar_modelo`

Os arquivos são armazenados em:

`modelos/qwen2.5-1.5b-instruct`

Após o download, o carregamento utiliza `local_files_only=True`, permitindo o processamento local sem depender de uma API externa durante a execução.

A pasta `modelos/` está incluída no `.gitignore` e não é enviada ao GitHub devido ao seu tamanho.

## Licença e disponibilidade

O modelo escolhido utiliza licença Apache 2.0 e pode ser obtido pelo Hugging Face para execução local.

Essa disponibilidade foi importante porque o projeto utiliza execução local do modelo no próprio ambiente de desenvolvimento.

## Integração com FastAPI

O modelo é carregado uma única vez durante a inicialização da API utilizando o `lifespan` do FastAPI.

A rota `POST /processar_texto` recebe o texto validado por Pydantic, executa o modelo local e retorna uma resposta estruturada pelo `ResultadoAnalise`.

Quando o modelo não está disponível, a rota retorna HTTP 503. Entradas abaixo do tamanho mínimo são rejeitadas com HTTP 422 e falhas durante o processamento retornam HTTP 500.

## Decisão final

O critério que mais pesou na escolha foi o equilíbrio entre capacidade de geração de texto e compatibilidade com o hardware disponível.

O Qwen2.5-1.5B-Instruct apresentou resultado satisfatório na tarefa de resumo e conseguiu ser executado localmente com os 15,91 GB de RAM disponíveis.

Embora um modelo menor pudesse reduzir o consumo de recursos, o computador suportou o modelo de 1.5B. Por isso, foi escolhida a opção com maior capacidade, mantendo a execução totalmente local.


