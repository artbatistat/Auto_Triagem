# IA_Triagem
Application to screening people and classification your urgency.

Objetivo da aplicação

O sistema vai coletar os dados do paciente na entrada e com base nas informações (sintomas, sinais vitais, idade), vamos utilizar a inteligência artificial para sugerir uma possível situação/doença e classificar a gravidade com base no risco.

Não é objetivo desta aplicação definir com 100% de certeza qual a doença que paciente contraiu, ela somente adiantará o processo de triagem para um atendimento direto com o médico para assim ser tratada da melhor forma.

A aplicação irá classificar a gravidade com base no risco entre três categorias.


Verde : pouco urgente;
Amarelo : média urgência;
Vermelho : emergência crítica



Ideia final

O totem deverá ter somente uma tela onde aparecerá as informações coletadas do paciente.
Como será coletado estes dados?
Para facilidade de todas as idades e tipos de pessoas a usar o totem, terá um microfone e um auto-falante embutido no totem. Onde pelo auto-falante a IA realizará as perguntas do formulário e o paciente responderá cada pergunta na qual o sistema montará o formulário e irá resultar na classificação.

Um exemplo de equipamento já utilizado na sociedade é a Alexa. Ela nos faz uma pergunta e espera uma resposta para montar sua outra pergunta ou sua resposta definitiva.

Entre estes dados coletados será:
Nome;
Idade;
Sexo;
Sintomas principais;
Doenças pré-existentes;
Temperatura, batimentos e pressão;

Como será coletado estes dados:

Informações como nome, idade, sexto, sintomas e doenças pré-existentes, serão captadas de forma oral na qual será interpretada pela IA.

Agora sinais vitais como temperatura, batimento e pressão, será utilizado tecnologias como sensor infravermelho (termômetro IR), fotopletismografia (PPG).

Protótipo

1° Fase - Teremos uma aplicação na qual todos os dados são inseridos de forma manual na aplicação e a inteligência artificial nos resultará um breve resultado com possiveis doenças, e a classificação da triagem.

A aplicação terá uma tela simples de formulário, como um totem de atendimento onde o usuário não terá muita navegação devido a aplicação ser orientada apenas para um segmento.

2° Fase - Teremos a mesma aplicação porém com captação de voz dos dados que não necessitam de equipamentos para serem aferidas, como nome, idade, sexo, sintomas, e doenças pré-existentes. Os demais dados de sinais vitais será inserido de forma manual , devido não termos o hardware adequado para aferir.

A aplicação irá manter a tela simples, todos os dados informados em tela e terá a confirmação da IA sempre que uma resposta for dada pelo usuário para confirmar se a informação será inserida corretamente.


Prompt: O prompt criado para ser utilizado no protótipo será o criado abaixo:

A partir das informações abaixo:
Gênero: [genero]
Idade: [idade]
Sintomas principais: [listar sintomas]
Doenças pré-existentes: [listar doenças ou "nenhuma"]
Temperatura corporal: [em °C]
Batimentos cardíacos por minuto: [número]
Pressão arterial: [ex: 120/80]


Gere uma resposta com as 3 possíveis doenças mais prováveis, incluindo o nome da doença e a porcentagem de acerto baseada nos sintomas e sinais vitais fornecidos.
Formato da resposta (sem explicações adicionais):
1° {doença-1} - {porcentagem}%
 2° {doença-2} - {porcentagem}%
 3° {doença-3} - {porcentagem}%

Classificação de triagem : {classificação_urgencia}
Em seguida, forneça apenas uma classificação de urgência com base na gravidade dos sintomas:
Verde: Pouco urgente


Amarelo: Média urgência


Vermelho: Emergência crítica


⚠️ A resposta deve seguir rigorosamente esse formato, sem explicações adicionais ou mensagens fora do padrão.

A modelo de inteligência utilizado foi o “google/gemini-2.0-flash-thinking-exp:free”
Modelo Gemini API grátis


