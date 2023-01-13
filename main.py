import json
import autoit

# Lê o arquivo json e armazena as credenciais em uma variável
with open('credentials.json') as json_file:
    credentials = json.load(json_file)

# Pergunta ao usuário qual conta ele deseja usar
print("Selecione uma conta para fazer login:")
for i in range(len(credentials)):
    print(f"{i+1}) {credentials[i]['user']}")

selected_account = int(input()) - 1

# Aguarda o programa 
autoit.win_wait_active("Riot Client Main")

# Preenche o formulário 
autoit.send(credentials[selected_account]['user'])
autoit.send("{TAB}")
autoit.send(credentials[selected_account]['password'])
autoit.send("{ENTER}")

exit()