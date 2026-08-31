# Plano de Captação — 20 Clientes para Vulk. • 30% Comissão

## Modelo Confirmado
- Agente (você): negocia, passa orçamento e data → 30% comissão
- Prestador (Vulk.): executa o serviço
- Você NÃO executa — você vende, agenda e repassa orçamento

## Sistema Automático (cron 1h — job 52f3eab33b96)
- Arquivo: leads_prospeccao.csv (20 empresas reais)
- Script: prospeccao-20clientes.py (atualiza status)
- Mensagem: MENSAGEM-DIVULGACAO.txt (disparo WhatsApp)
- Ciclo: a cada 1h — 0 confirmações — autonomia total

## Como você opera (manual + automatizado):
1. Receber lead do CSV (nome, segmento, WhatsApp)
2. Enviar mensagem via WhatsApp (modelo salvo)
3. Receber resposta → solicitar detalhes do serviço
4. Passar ao prestador → receber orçamento
5. Repassar orçamento + data ao cliente
6. Agendar → confirmar → receber comissão (30%) após conclusão

## Meta
20 clientes = 20 orçamentos enviados = fechamento esperado com comissão de 30% sobre cada serviço executado.
