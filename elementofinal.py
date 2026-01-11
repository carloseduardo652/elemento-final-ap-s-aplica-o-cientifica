import tkinter as tk
from tkinter import messagebox
import random

# [cite: 1] Nome do programa: elemento final após aplicação científica
def rodar_programa():
    def processar_escolha():
        selecao = lista_opcoes.curselection()
        
        #  O programa deve permitir apenas uma escolha e informar se nada for selecionado
        if not selecao:
            messagebox.showwarning("Aviso", "Você deve selecionar exatamente uma opção.")
            return
        
        item_escolhido = lista_opcoes.get(selecao[0])
        
        # Dicionário contendo os dados dos Casos 01, 02 e 03 baseados no documento
        dados_casos = {
            "Força = 2 N": {
                "Caso 01 (Bola Normal)": "Pequena deformação, Bola quase não muda de forma, Resposta elástica, Não quebra", # [cite: 7]
                "Caso 02 (Bola de Papel)": "Deformação visível, Pode amassar levemente, Parte da deformação já pode ser permanente", # [cite: 12]
                "Caso 03 (Bola de Vidro)": "Quase nenhuma deformação, Material rígido, Pode resistir se não houver impacto" # [cite: 17]
            },
            "Força = 50 N": {
                "Caso 01 (Bola Normal)": "Grande deformação elástica, A bola achata e volta à forma original, Armazena energia elástica, Pode ganhar velocidade", # [cite: 8]
                "Caso 02 (Bola de Papel)": "Amassamento forte, Deformação plástica, Não retorna à forma original, Energia dissipada", # [cite: 13]
                "Caso 03 (Bola de Vidro)": "Tensão interna muito alta, Fratura / quebra, Liberação súbita de energia" # [cite: 18]
            },
            "Energia cinética = 80 J": {
                "Caso 01 (Bola Normal)": "A bola deforma bastante (alta elasticidade), Absorve parte da energia, Quica e continua em movimento, Não se quebra", # [cite: 9]
                "Caso 02 (Bola de Papel)": "Grande deformação, Parte da energia vira deformação permanente, Pode amassar ou rasgar, Pouco ou nenhum quique", # [cite: 14]
                "Caso 03 (Bola de Vidro)": "Não deforma, Energia não é absorvida, Quebra ou estilhaça, Colisão frágil e destrutiva" # [cite: 19]
            },
            "Energia cinética = 1 J": {
                "Caso 01 (Bola Normal)": "Pequena deformação, Movimento fraco, Quique baixo ou quase nenhum, Estrutura permanece intacta", # [cite: 10]
                "Caso 02 (Bola de Papel)": "Leve deformação, Movimento pequeno, Estrutura quase não muda", # [cite: 15]
                "Caso 03 (Bola de Vidro)": "Impacto fraco, Não quebra, Pode apenas rolar ou bater levemente" # [cite: 20]
            }
        }

        # Montagem da mensagem final de detecção
        info = dados_casos[item_escolhido]
        resultado_texto = f"Resultado para {item_escolhido}:\n\n"
        for caso, situacao in info.items():
            resultado_texto += f"{caso}:\n- {situacao}\n\n"
        
        messagebox.showinfo("Elemento Final", resultado_texto)

    # Configuração da Janela
    janela = tk.Tk()
    janela.title("Elemento final após aplicação científica")
    janela.geometry("500x450")

    # [cite: 5] Texto obrigatório na tela
    label_instrucao = tk.Label(
        janela, 
        text="Você deve escolher uma aplicação científica para obter informação\ndo elemento final que no momento é bola normal, bola de papel e bola de vidro",
        wraplength=450,
        justify="center",
        font=("Arial", 10, "bold")
    )
    label_instrucao.pack(pady=20)

    #  Informar limite de uma escolha
    label_limite = tk.Label(janela, text="(Limite: Escolha apenas 1 item abaixo)", fg="red")
    label_limite.pack()

    # [cite: 2, 3] Conceitos físicos e medidas sem repetição e misturados
    opcoes = ["Força = 2 N", "Força = 50 N", "Energia cinética = 80 J", "Energia cinética = 1 J"]
    random.shuffle(opcoes)

    lista_opcoes = tk.Listbox(janela, width=40, height=5, selectmode=tk.SINGLE)
    for opt in opcoes:
        lista_opcoes.insert(tk.END, opt)
    lista_opcoes.pack(pady=10)

    # Botão para detectar a situação
    botao = tk.Button(janela, text="Detectar Situação", command=processar_escolha)
    botao.pack(pady=10)

    janela.mainloop()

if __name__ == "__main__":
    rodar_programa()