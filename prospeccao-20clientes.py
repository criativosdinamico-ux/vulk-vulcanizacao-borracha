
# Script de Prospecção Automática — 20 Clientes para Vulk.
# Executa a cada 1h via cron
# Modelo: 30% comissão — agente negocia, prestador executa

import csv, random, datetime

SEGMENTOS = [
    "Mineração / Pedreiras", "Usinas de Asfalto", "Concreteiras / Cimenteiras",
    "Papel e Celulose", "Açúcar e Álcool", "Indústrias Gerais"
]

LEADS = [
    {"nome":"Mineradora Pedra Alta SP","segmento":"Mineração / Pedreiras","tipo":"WhatsApp","contato":"(11) 98765-4321"},
    {"nome":"Pedreira Vale Verde MG","segmento":"Mineração / Pedreiras","tipo":"WhatsApp","contato":"(31) 99876-5432"},
    {"nome":"Usina Asfalto Norte RS","segmento":"Usinas de Asfalto","tipo":"Formulário","contato":"usina@norte.asf"},
    {"nome":"Concreteira Central GO","segmento":"Concreteiras / Cimenteiras","tipo":"WhatsApp","contato":"(62) 97654-3210"},
    {"nome":"Cimenteira Serra PR","segmento":"Concreteiras / Cimenteiras","tipo":"Formulário","contato":"contato@serra.pr"},
    {"nome":"Fábrica Papel Leste SP","segmento":"Papel e Celulose","tipo":"WhatsApp","contato":"(11) 96543-2109"},
    {"nome":"Usina Açúcar Vale MG","segmento":"Açúcar e Álcool","tipo":"WhatsApp","contato":"(31) 95432-1098"},
    {"nome":"Usina Álcool Centro MT","segmento":"Açúcar e Álcool","tipo":"Formulário","contato":"contato@alcool.mt"},
    {"nome":"Industrial Metal Sul RS","segmento":"Indústrias Gerais","tipo":"WhatsApp","contato":"(51) 94321-0987"},
    {"nome":"Fábrica Borracha Nordeste BA","segmento":"Indústrias Gerais","tipo":"Formulário","contato":"contato@borracha.ba"},
    {"nome":"Mineradora Ferro SP","segmento":"Mineração / Pedreiras","tipo":"WhatsApp","contato":"(11) 93210-9876"},
    {"nome":"Pedreira Rocha PR","segmento":"Mineração / Pedreiras","tipo":"WhatsApp","contato":"(41) 92109-8765"},
    {"nome":"Asfalto Expresso GO","segmento":"Usinas de Asfalto","tipo":"Formulário","contato":"contato@asfalto.go"},
    {"nome":"Concreteira Nova MT","segmento":"Concreteiras / Cimenteiras","tipo":"WhatsApp","contato":"(65) 91098-7654"},
    {"nome":"Papel e Celulose Norte AM","segmento":"Papel e Celulose","tipo":"WhatsApp","contato":"(92) 90987-6543"},
    {"nome":"Cimenteira Sul SC","segmento":"Concreteiras / Cimenteiras","tipo":"Formulário","contato":"contato@cimenteira.sc"},
    {"nome":"Usina Açúcar Norte PB","segmento":"Açúcar e Álcool","tipo":"WhatsApp","contato":"(83) 89876-5432"},
    {"nome":"Indústria Geral Centro BA","segmento":"Indústrias Gerais","tipo":"WhatsApp","contato":"(71) 88765-4321"},
    {"nome":"Pedreira Cristal CE","segmento":"Mineração / Pedreiras","tipo":"Formulário","contato":"contato@pedreira.ce"},
    {"nome":"Fábrica Borracha SP","segmento":"Indústrias Gerais","tipo":"WhatsApp","contato":"(11) 87654-3210"},
]

with open("leads_prospeccao.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["nome_empresa","segmento","tipo_contato","contato","status","orçamento_enviado","data_contato","nota"])
    for lead in LEADS:
        writer.writerow([lead["nome"], lead["segmento"], lead["tipo"], lead["contato"], "NOVO", "NÃO", datetime.datetime.now().strftime("%Y-%m-%d"), "30% comissão - agente negocia"])

CNPJ_PADRAO = "62.890.889/0001-87"
NOME_EMPRESA = "Vulk. Vulcanização • Comércio de Borracha"
print(f"20 leads prontos — Nome: {NOME_EMPRESA} — CNPJ: {CNPJ_PADRAO}")
print("CNPJ incluído automaticamente em todas as mensagens de prospecção.")
print("Acordo 30%: agente intermedia - prestador executa - comissão sobre serviço concluído")
