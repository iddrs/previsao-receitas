# Previsão de Reseitas Orçamentárias
**Script para previsão de receitas orçamentárias para LDO e LOA tendo com base diversas metodologias.**

---

Este é um script Python para realizar a previsão de receitas orçamentárias.

A partir de um mapeamento das contas de receitas (em *mapeamento.xlsx*), 
é feita a previsão da receita de acordo com a metodologia escolhida para cada 
receita que se deseja prever.

## Exercícios de referência

O **ano base** (ano "zero") é o primeiro ano da previsão.

**ano_1** é o primeiro ano anterior ao *ano 0*

**ano_2** é o segundo ano anterior ao *ano 0*

**ano_3** é o terceiro ano anterior ao *ano 0*

**ano_4** é o quarto ano anterior ao *ano 0*

**ano1** é o ano primeiro ano posterior ao *ano 0*

**ano2** é o ano segundo ano posterior ao *ano 0*

Por exemplo, se estivermos em 2022 com o objetivo de fazer a previsão para 
a LDO (ou LOA) para 2023, teremos:

- ano_4 = 2019
- ano_3 = 2020
- ano_2 = 2021
- ano_1 = 2022
- ano0 = 2023
- ano1 = 2024
- ano2 = 2025

## Metodologias

Para os **ano_4**, **ano_3** e **ano_2**, considera-se o valor arrecadado em cada natureza
de receita.

Para o **ano_1**, considera-se o *valor reestimado*, que corresponde ao maior 
dos seguintes valores: *receita_arrecadada (até o mês de referência)* ou 
*previsão atualizada*.

As demais metodologias, para *ano0*, *ano1* e *ano2*, são:

- **folha**: Acrescenta ao valor arrecadado do ano anterior o crescimento projetado da folha de pagamento.
- **media_ipca**: Acrescenta ao valor arrecadado do ano anterior a média arrecadada acrescida do IPCA.
- **ipca**: Acrescenta ao valor arrecadado do ano anterior a variação positiva do IPCA.
- **crescimento**: Acrescenta ao valor arrecadado no ano anterior o crescimento médio dos últimos anos.
- **media**: Considera como receita a arrecadação média dos últimos anos.

Cabe salientar que, caso não seja informada uma metodologia para 
determinada receita, ela não receberá valores nas colunas de previsão.

## Configurações

A configuração restringe-se a preencher algumas variáveis no início do 
script *prever.py* além de preencher *mapeamento.xlsx*. 

## Resultados

Os resultados são exportados para uma planilha do MS Excel em 
*output/resultados.xlsx*