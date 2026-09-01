
#!/usr/bin/env python3
# Loop contínuo — envia e-mails automaticamente a cada 60 min
# Autonomia total — nenhuma confirmação

import time, subprocess, os
from datetime import datetime

while True:
    # Executar script de envio
    try:
        # Verifica se o script existe
        script_path = "/root/ecosystem/projects/vulk-vulcanizacao/repo/envio_email_20clientes.py"
        if os.path.exists(script_path):
            # Executa o envio apenas se houver NOVO
            result = subprocess.run(["python3", script_path], capture_output=True, timeout=300)
            # Salvar log silencioso (apenas arquivo)
            with open("/root/ecosystem/projects/vulk-vulcanizacao/repo/logs/envio-silencioso.log", "a") as f:
                f.write(f"{datetime.now().isoformat()} - envio executado (exit={result.returncode})\n")
        # Atualiza CSV (marcar o que foi enviado) — já feito no script
    except Exception as e:
        with open("/root/ecosystem/projects/vulk-vulcanizacao/repo/logs/envio-silencioso.log", "a") as f:
            f.write(f"{datetime.now().isoformat()} - erro no loop: {str(e)[:200]}\n")
    
    # Aguardar 60 minutos (1h) — sem parar, sem confirmar
    time.sleep(3600)
