import tkinter as tk
import requests
import json

def IA(genero,idade,sintomas,doencas,temperatura,batimentos,pressao):

    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    },
    data=json.dumps({
        "model": "google/gemini-2.0-flash-thinking-exp:free",
        "messages": [
        {
            "role": "user",
            "content": [
            {
                "type": "text",
                "text": f"""A partir das informações abaixo:
                            Gênero: {genero}
                            Idade: {idade}
                            Sintomas principais: {sintomas}
                            Doenças pré-existentes: {doencas}
                            Temperatura corporal: {temperatura}
                            Batimentos cardíacos por minuto: {batimentos}
                            Pressão arterial: {pressao}


                            Gere uma resposta com as 3 possíveis doenças mais prováveis, incluindo o nome da doença e a porcentagem de acerto baseada nos sintomas e sinais vitais fornecidos.
                            Formato da resposta (sem explicações adicionais):
                            1° [doença-1] - [porcentagem]%
                            2° [doença-2] - [porcentagem]%
                            3° [doença-3] - [porcentagem]%

                            Classificação de triagem : [classificação_urgencia]
                            Em seguida, forneça apenas uma classificação de urgência com base na gravidade dos sintomas:
                            Verde: Pouco urgente


                            Amarelo: Média urgência


                            Vermelho: Emergência crítica

                            ****A resposta deve seguir rigorosamente esse formato, sem explicações adicionais ou mensagens fora do padrão.
                    """
            }
            ]
        }
        ],
        
    })
    )

    return response.json()['choices'][0]['message']['content']

def frm_result():
    nome = input_nome.get()
    idade = input_idade.get()
    genero = input_genero.get()
    sintomas = input_sintomas.get()
    doencas = input_doenças.get()
    temperatura = input_temperatura.get()
    batimentos = input_batimentos.get()
    pressao = input_pressao.get()
    resultado = (f'Nome do paciente: {nome}\n'
        f'{IA(genero,idade,sintomas,doencas,temperatura,batimentos,pressao)}'
    )

    txt_resultado.config(text=resultado)

# Criação da janela principal
frm_windows = tk.Tk()
frm_windows.title("Formulário de Triagem inteligente")
frm_windows.geometry("600x800")

# Label e entrada para nome
tk.Label(frm_windows, text="Nome completo:").pack(pady=5)
input_nome = tk.Entry(frm_windows)
input_nome.pack()

# Label e entrada para idade
tk.Label(frm_windows, text="Idade:").pack(pady=5)
input_idade = tk.Entry(frm_windows)
input_idade.pack()

# Label e entrada para sexo
tk.Label(frm_windows, text="Gênero:").pack(pady=5)
input_genero = tk.Entry(frm_windows)
input_genero.pack()

# Label e entrada para sintomas
tk.Label(frm_windows, text="Sintomas:").pack(pady=5)
input_sintomas = tk.Entry(frm_windows)
input_sintomas.pack()

# Label e entrada para doenças pré-existentes
tk.Label(frm_windows, text="Doenças pré existentes:").pack(pady=5)
input_doenças = tk.Entry(frm_windows)
input_doenças.pack()

# Label e entrada para temperatura
tk.Label(frm_windows, text="Temperatura:").pack(pady=5)
input_temperatura = tk.Entry(frm_windows)
input_temperatura.pack()

# Label e entrada para batimentos
tk.Label(frm_windows, text="Batimento:").pack(pady=5)
input_batimentos = tk.Entry(frm_windows)
input_batimentos.pack()

# Label e entrada para pressão arterial
tk.Label(frm_windows, text="Pressão arterial:").pack(pady=5)
input_pressao = tk.Entry(frm_windows)
input_pressao.pack()

# Botão para gerar resultado
btn_mostrar = tk.Button(frm_windows, text="Mostrar Resultado", command=frm_result)
btn_mostrar.pack(pady=10)

# Área onde o resultado será exibido
txt_resultado = tk.Label(frm_windows, text="", fg="black")
txt_resultado.pack(pady=20)

# Inicia o loop da janela
frm_windows.mainloop()
