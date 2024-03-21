# nginx-load-balancer
Repositório de teste para lidar com migrations e um load balancer do nginx usando o docker compose. Teste feito com FastAPI e com Flask.

### Lógica Base
- Criar uma imagem da API com o ENTRYPOINT chamando apenas o start da aplicação (python3 app.py runserver).
- Criar os serviços da API no compose file e sobrescrever o ENTRYPOINT com o arquivo `entrypoint.sh` dentro de cada imagem de um desses serviços para realizar as migrations e popular o banco com os dados mockados
- Todos os outros serviços da API devem depender da finalização das migrations desse serviço

### Observações
- O protocolo de balancing do nginx é o `ip_hash` pois esse projeto surgiu da necessidade de balancear a carga de um chat usando socketio e é especificado que o load balancer precisa estar usando hashing de ip para funcionar, pode-se usar qualquer outro protocolo.

### Dependências
- O load balancer do nginx depende da existência de processos já rodando nas portas em que se pretende balancear a carga, logo o container do NGINX **vai depender de todas as instâncias da API**
- A instância da api que irá fazer as migrations vai depender do setup do container do banco, logo irá haver um healthcheck para garantir a integridade do banco de dados postgres
- Todas as instâncias da API que não fazem migrations vão depender da instância que faz, pois ela que vai deixar o banco no estado pronto de uso