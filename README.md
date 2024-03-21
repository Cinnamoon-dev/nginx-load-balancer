# nginx-load-balancer
Repositório de teste para lidar com migrations e um load balancer do nginx usando o docker compose. Teste feito com FastAPI e com Flask.

### Lógica Base
- Criar uma imagem da API com o ENTRYPOINT chamando apenas o start da aplicação (python3 app.py runserver).
- Criar os serviços da API no compose file e sobrescrever o ENTRYPOINT com o arquivo `entrypoint.sh` dentro de cada imagem de um desses serviços para realizar as migrations e popular o banco com os dados mockados
- Todos os outros serviços da API devem depender da finalização das migrations desse serviço

### Observações
- O protocolo de balancing do nginx é o `ip_hash` pois esse projeto surgiu da necessidade de balancear a carga de um chat usando socketio e é especificado que o load balancer precisa estar usando hashing de ip para funcionar, pode-se usar qualquer outro protocolo.