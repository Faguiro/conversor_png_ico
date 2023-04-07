Conversor de imagens PNG para ICO
Este é um aplicativo de desktop simples que converte imagens PNG para o formato ICO usando a biblioteca Tkinter do Python.

Instalação
Antes de usar o aplicativo, é necessário instalar as dependências do Python. Para isso, é recomendável criar um ambiente virtual e instalar as dependências usando o arquivo requirements.txt. Para criar o ambiente virtual e instalar as dependências, siga os seguintes passos:

Clone o repositório do aplicativo:
git clone https://github.com/Faguiro/conversor_png_ico.git

Navegue até o diretório do projeto:
cd nome-do-repositorio

Crie um ambiente virtual para o projeto:
python -m venv qt_venv

Ative o ambiente virtual:
source qt_venv/bin/activate (para Linux ou macOS)
qt_venv\Scripts\activate (para Windows)

Instale as dependências:
pip install -r requirements.txt

Uso
Para iniciar o aplicativo, execute o arquivo main.py:
python main.py

Compilação
Para compilar este aplicativo para um executável (windows only), execute:
pyinstaller --noconfirm --onefile --windowed  ""


Na janela do aplicativo, clique no botão "Selecionar arquivo" para escolher um arquivo PNG para converter. Em seguida, clique no botão "Converter" e escolha a pasta de destino para gerar um arquivo ICO com base na imagem selecionada.

Quando a conversão estiver concluída, uma mensagem de notificação será exibida informando o caminho do arquivo ICO gerado. Você pode clicar no botão "Reset" para limpar a seleção de arquivo e começar uma nova conversão.

Contribuindo
Contribuições são sempre bem-vindas! Se você quiser melhorar o aplicativo, sinta-se à vontade para enviar um pull request. Certifique-se de seguir as diretrizes de contribuição do projeto.

Licença
Este aplicativo é distribuído sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.