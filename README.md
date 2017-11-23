# NPK Backup
Um pequeno utilitário para automatizar a cópia de segurança de uma determinada pasta (por exemplo, cópias de segurança locais de bases de dados Filemaker, coleções de scripts e aplicações do Pythonista, etc.), criando arquivos zip individuais a partir de cada pasta principal na localização especificada e fazendo upload dos mesmos para a Dropbox. 

O programa mantém um registo simples, por forma a nao repetir as tarefas de compressão e upload já realizadas. Em cada execução, são efetuadas cópias individuais de cada pasta nova, que ainda não conste nas cópias anteriores. Convém notar que ___não são___ copiadas pastas nem ficheiros previamente processados, mesmo que possam ter sido alterados entretanto.

## Dependências
Esta aplicação é desenvolvida em Python 3.5 e requer, na versão atual, o(s) seguinte(s) módulo(s) externo(s):

- dropbox

O desenvolvimento e testes têm sido realizados em Mac e iOS (Pythonista 3), no entanto deverá ser bastante simples a adaptação para funcionar sem problemas em Windows ou Linux.


## Como usar
Inicialmente, deverão ser especificadas no ficheiro `app_settings.py` as constantes relativas ao caminho dos ficheiros ou pastas de origem. Para a realização de cópias de segurança de bases de dados, é recomendável consultar a respetiva documentação, no sentido de verificar quais as pastas e ficheiros a copiar.

É também necessário registar a aplicação no site da Dropbox e configurar no ficheiro `app_settings.py` a *token* lá indicada.

Para iniciar a cópia, basta executar o ficheiro `npk-backup.py` com o interpretador Python 3.5 ou superior. Em sistemas operativos que suportem algum mecanismo de agendamento (cron, launchd, etc.), este script pode ser utilizado para a realização de cópias automatizadas, requerendo para tal a sua chamada a partir do serviço correspondente do sistema.
