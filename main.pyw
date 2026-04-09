import tkinter as tk
from tkinter import messagebox, scrolledtext

def analisar_risco():
    # Coleta o texto inserido
    projeto = entrada.get("1.0", tk.END).lower().strip()
    
    if not projeto or "escreva" in projeto:
        messagebox.showwarning("Aviso / Warning", "Por favor, descreva a obra.\nPlease describe the project.")
        return

    # Log Bilíngue
    log_box.insert(tk.END, f"\n[ANALYZING / ANALISANDO]: {projeto[:30]}...\n")
    root.update_idletasks()
    
    # Lista de termos críticos (PT e EN)
    riscos = ["poste", "alta tensão", "rede", "fiação", "cavar", "escavação", "valeta", "grid", 
              "power", "electricity", "excavation", "wire", "high voltage", "pole"]
    
    achados = [word for word in riscos if word in projeto]
    
    if achados:
        # Mensagem de Erro Bilíngue
        messagebox.showerror("🚨 ALERTA DE SEGURANÇA / SAFETY ALERT", 
            "STATUS: BLOQUEADO PELO AGENTE POSE / BLOCKED BY POSE AGENT\n\n"
            "RISCO DETECTADO / RISK DETECTED: Proximidade com Rede Elétrica.\n\n"
            "Ação / Action: Paralisar atividades e acionar concessionária.\n"
            "Stop activities and contact utility providers.")
        log_box.insert(tk.END, f">>> [ERROR]: OPERATION BLOCKED / OPERAÇÃO BLOQUEADA\n", "erro")
    else:
        # Mensagem de Sucesso Bilíngue
        messagebox.showinfo("✅ CONFORMIDADE / COMPLIANCE APPROVED", 
            "STATUS: APROVADO / APPROVED\n\n"
            "Nenhum risco detectado. O Protocolo POSE autoriza a continuidade.\n"
            "No risks detected. The POSE Protocol authorizes the project.")
        log_box.insert(tk.END, ">>> [SUCCESS]: PROJECT APPROVED / PROJETO APROVADO\n", "sucesso")
    
    log_box.see(tk.END)

# --- Interface Gráfica ---
root = tk.Tk()
root.title("POSE AI Agent V2 - Governance & Safety System")
root.geometry("750x600")
root.configure(bg="#f4f4f4")

# Cabeçalho Bilíngue
header_text = "🛡️ PROTOCOLO POSE - IA DE SEGURANÇA\nPOSE PROTOCOL - SAFETY AI"
header = tk.Label(root, text=header_text, font=("Arial", 14, "bold"), bg="#004a99", fg="white", pady=15)
header.pack(fill=tk.X)

# Instruções Bilíngues
tk.Label(root, text="Describe the project below / Descreva a obra abaixo:", 
         bg="#f4f4f4", font=("Arial", 10, "italic")).pack(pady=15)

# Campo de Texto
entrada = tk.Text(root, height=6, width=80, font=("Arial", 11), bd=2, relief="groove")
entrada.pack(pady=5, padx=20)
entrada.insert(tk.END, "Escreva a descrição aqui... / Write description here...")

# Botão Bilíngue
btn_analisar = tk.Button(root, text="ANALISAR COM IA / RUN AI ANALYSIS", 
                        command=analisar_risco, 
                        bg="#28a745", fg="white", 
                        font=("Arial", 12, "bold"), 
                        cursor="hand2", padx=25, pady=12)
btn_analisar.pack(pady=20)

# Painel de Log Bilíngue
tk.Label(root, text="Operational Log / Log de Operações:", bg="#f4f4f4", font=("Arial", 9, "bold")).pack(anchor="w", padx=25)
log_box = scrolledtext.ScrolledText(root, height=12, width=90, font=("Consolas", 9), bg="#1e1e1e", fg="#dcdcdc")
log_box.pack(pady=5, padx=20)

# Tags de cores
log_box.tag_config("erro", foreground="#ff6b6b")
log_box.tag_config("sucesso", foreground="#51cf66")
log_box.insert(tk.END, "System Online... Monitorando conformidade / Monitoring compliance.\n")

# Rodapé
footer = tk.Label(root, text="GitLab AI Hackathon 2026 - POSE Agent Platform V2", 
                 font=("Arial", 8), bg="#f4f4f4", fg="#888")
footer.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
