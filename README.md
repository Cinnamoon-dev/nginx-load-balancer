# nginx-load-balancer
Repositório de teste para lidar com migrations e um load balancer do nginx usando o docker compose. Teste feito com FastAPI e com Flask.

## Problema em Questão
Em uma API REST Flask já existente foi necesário implementar um chat com socketio. A aplicação Flask usava o gunicorn como WSGI com 10 workers, porém para interagir com o socketio se fazia necessário definir apenas 1 worker para o gunicorn limitando assim o throughput da aplicação e aumentando muito o seu tempo de resposta.

Diante dessa situação problema, uma solução encontrada foi criar várias instâncias da aplicação com 1 worker e usar um load balancer para distribuir a carga entre essas várias instâncias.

Ao criar a aplicação depara-se com outro problema, nem todas as instâncias da API podem fazer as migrations pois haveriam conflitos de várias migrations iguais no banco (inclusive as iniciais que populam o banco com os dados base). A solução encontrada foi fazer com que apenas uma instância faça as migrations iniciais e as outras dependam dela para iniciar.

### Lógica Base
- Criar uma imagem da API com o ENTRYPOINT chamando apenas o start da aplicação (python3 app.py runserver).
- Criar os serviços da API no compose file e sobrescrever o ENTRYPOINT com o arquivo `entrypoint.sh` dentro de cada imagem de um desses serviços para realizar as migrations e popular o banco com os dados mockados
- Todos os outros serviços da API devem depender da finalização das migrations desse serviço

### Observações
- O protocolo de balancing do nginx é o `ip_hash` pois esse projeto surgiu da necessidade de balancear a carga de um chat usando socketio e é especificado que o load balancer precisa estar usando hashing de ip para funcionar, pode-se usar qualquer outro protocolo.

### Dependências Docker
- O load balancer do nginx depende da existência de processos já rodando nas portas em que se pretende balancear a carga, logo o container do NGINX **vai depender de todas as instâncias da API**
- A instância da api que irá fazer as migrations vai depender do setup do container do banco, logo irá haver um healthcheck para garantir a integridade do banco de dados postgres
- Todas as instâncias da API que não fazem migrations vão depender da instância que faz, pois ela que vai deixar o banco no estado pronto de uso