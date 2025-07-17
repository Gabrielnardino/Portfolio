# Desafio de Análise de Dados: E-commerce

## Introdução

Bem-vindo ao desafio de Análise de Dados para E-commerce! Este projeto foi desenvolvido para simular um cenário real de trabalho, onde você, como Analista de Dados Júnior, terá a oportunidade de aplicar suas habilidades para extrair insights valiosos de um conjunto de dados de vendas de uma empresa de comércio eletrônico. O objetivo é não apenas responder a perguntas de negócio, mas também demonstrar sua capacidade de transformar dados brutos em informações acionáveis, que podem ser utilizadas para otimizar estratégias de vendas, marketing e operações.

Este desafio é ideal para ser adicionado ao seu portfólio, pois abrange diversas etapas do ciclo de vida da análise de dados, desde a compreensão do problema até a apresentação dos resultados. Ele foi projetado para destacar suas competências em manipulação, limpeza, análise exploratória e visualização de dados, além de sua habilidade em comunicar descobertas de forma clara e concisa.

## Cenário de Negócio

Você foi contratado como Analista de Dados Júnior em uma empresa de e-commerce em crescimento. A empresa coletou dados de clientes, produtos e transações ao longo do último ano e precisa de sua ajuda para entender melhor o desempenho das vendas, o comportamento dos clientes e a performance dos produtos. A gerência busca insights que possam embasar decisões estratégicas para impulsionar o crescimento e a lucratividade.

## Objetivos do Desafio

Seu principal objetivo é analisar os dados fornecidos e responder às questões de negócio propostas, apresentando suas descobertas de forma clara e visualmente atraente. Além disso, espera-se que você forneça recomendações acionáveis baseadas em suas análises.

## Dataset

O dataset é composto por três arquivos CSV, localizados na pasta `data/`:

1.  **`customers.csv`**: Contém informações sobre os clientes.
    *   `customer_id`: Identificador único do cliente.
    *   `age`: Idade do cliente.
    *   `gender`: Gênero do cliente.
    *   `city`: Cidade de residência do cliente.
    *   `membership_level`: Nível de associação do cliente (Bronze, Silver, Gold, Platinum).

2.  **`products.csv`**: Contém informações sobre os produtos.
    *   `product_id`: Identificador único do produto.
    *   `category`: Categoria do produto (e.g., Electronics, Clothing, Books).
    *   `price`: Preço unitário do produto.
    *   `stock_quantity`: Quantidade em estoque do produto.

3.  **`transactions.csv`**: Contém detalhes de cada transação de compra.
    *   `transaction_id`: Identificador único da transação.
    *   `customer_id`: Identificador do cliente que realizou a compra.
    *   `product_id`: Identificador do produto comprado.
    *   `quantity`: Quantidade do produto comprada na transação.
    *   `transaction_date`: Data da transação.
    *   `payment_method`: Método de pagamento utilizado (e.g., Credit Card, Debit Card, Bank Transfer, Boleto).
    *   `total_price`: Preço total da transação (calculado como `quantity * price`).

## Questões de Negócio e Tarefas Analíticas

Para responder às questões de negócio, você deverá realizar as seguintes tarefas e responder às perguntas específicas:

### 1. Performance de Vendas

*   **Tarefa:** Analise as tendências de vendas ao longo do tempo. Identifique picos, quedas e padrões sazonais.
*   **Perguntas:**
    *   Qual foi a receita total gerada no período?
    *   Como a receita e a quantidade de vendas se comportaram mensalmente/trimestralmente?
    *   Qual o produto mais vendido em termos de quantidade e o mais lucrativo em termos de receita?
    *   Qual a categoria de produto mais lucrativa?

### 2. Comportamento do Cliente

*   **Tarefa:** Explore o perfil dos clientes e seu comportamento de compra.
*   **Perguntas:**
    *   Qual a distribuição demográfica dos clientes (idade, gênero, cidade)?
    *   Existe alguma correlação entre o nível de associação do cliente e o valor total gasto?
    *   Identifique os 10 clientes que mais gastaram (clientes de alto valor).
    *   Qual a média de idade dos clientes por nível de associação?

### 3. Análise de Produtos

*   **Tarefa:** Avalie o desempenho dos produtos e categorias.
*   **Perguntas:**
    *   Quais são os 5 produtos mais vendidos e os 5 produtos que geraram mais receita?
    *   Existem produtos populares com baixo estoque que podem levar a perdas de vendas?
    *   Qual a categoria de produto com maior número de vendas e maior receita?

### 4. Métodos de Pagamento

*   **Tarefa:** Analise a preferência dos clientes por métodos de pagamento.
*   **Perguntas:**
    *   Qual o método de pagamento mais utilizado pelos clientes?
    *   Existe diferença no ticket médio por método de pagamento?

### 5. Insights e Recomendações

*   **Tarefa:** Com base em todas as suas análises, sintetize os principais insights e forneça recomendações acionáveis para a empresa de e-commerce.
*   **Perguntas:**
    *   Quais são as principais descobertas que a empresa deve saber?
    *   Que ações a empresa pode tomar para otimizar as vendas, melhorar a experiência do cliente ou gerenciar o estoque de forma mais eficiente?

## Requisitos Técnicos

Você pode utilizar as ferramentas e linguagens de sua preferência para realizar a análise, mas as mais comuns e recomendadas para um Analista de Dados Júnior incluem:

*   **Linguagens de Programação:** Python (com bibliotecas como Pandas, NumPy, Matplotlib, Seaborn) ou R.
*   **SQL:** Para manipulação e consulta de dados, caso opte por carregar os dados em um banco de dados.
*   **Ferramentas de Visualização:** Matplotlib, Seaborn, Plotly (Python/R) ou ferramentas como Power BI, Tableau, Looker Studio (para dashboards interativos).

## Entrega

Sua entrega deve incluir:

1.  **Código-fonte:** Um notebook (Jupyter Notebook, Google Colab) ou script(s) Python/R com todo o código utilizado para a análise, incluindo limpeza, pré-processamento, análise exploratória, cálculos e visualizações. O código deve ser bem comentado e organizado.
2.  **Relatório/Apresentação:** Um documento (PDF, Markdown, HTML) ou slides (PPTX) que apresente suas descobertas, insights e recomendações. Este relatório deve ser claro, conciso e visualmente atraente, como se fosse apresentado à gerência da empresa. Inclua os gráficos e tabelas mais relevantes.
3.  **Explicação:** Uma breve explicação sobre as decisões tomadas durante a análise, os desafios encontrados e como foram superados.

## Critérios de Avaliação

Seu trabalho será avaliado com base nos seguintes critérios:

*   **Compreensão do Problema:** Capacidade de entender as questões de negócio e traduzi-las em análises de dados.
*   **Qualidade do Código:** Clareza, organização, eficiência e comentários no código.
*   **Corretude da Análise:** Precisão dos cálculos e das análises realizadas.
*   **Qualidade das Visualizações:** Clareza, relevância e estética dos gráficos e dashboards.
*   **Profundidade dos Insights:** Capacidade de extrair insights significativos e não apenas descrever os dados.
*   **Recomendações Acionáveis:** Recomendações práticas e baseadas em dados que a empresa possa implementar.
*   **Comunicação:** Clareza e concisão na apresentação dos resultados e na explicação das suas decisões.

Boa sorte com o desafio! Estamos ansiosos para ver suas análises e descobertas.

