## projeto python com Flask
Praticando python com flask criando API.

### dependências utilizadas:

**Flask:**

**Descrição:** Framework web leve para Python. Ele é projetado para ser simples e fácil de usar, permitindo que os desenvolvedores construam aplicativos web rapidamente e com poucas linhas de código. Flask fornece funcionalidades essenciais para criar rotas, manipular solicitações HTTP, gerenciar sessões e muito mais.
**Para que serve:** É usado para desenvolver aplicativos web, desde simples APIs até aplicativos web mais complexos.

**make_response:**

**Descrição:** Uma função do Flask que cria uma resposta HTTP personalizada. Ela permite que você construa uma resposta HTTP completa com controle sobre os cabeçalhos, status e conteúdo da resposta.
**Para que serve:** Essa função é útil quando você precisa personalizar a resposta HTTP além do que uma função de rota típica do Flask pode fazer, permitindo mais controle sobre a resposta enviada de volta ao cliente.

**jsonify:**

**Descrição:** Função do Flask que converte um objeto Python em uma resposta JSON válida. Ele garante que o cabeçalho Content-Type seja configurado corretamente para indicar que o conteúdo é JSON.
**Para que serve:** Usado comumente em rotas que precisam enviar dados JSON como resposta. Ele facilita a conversão de objetos Python em JSON e configura automaticamente o cabeçalho Content-Type.
request:

**Descrição:** Objeto global no Flask que fornece acesso aos dados da solicitação HTTP. Ele contém informações sobre os parâmetros da URL, os dados do corpo da solicitação, cabeçalhos e muito mais.
**Para que serve:** request é usado para acessar informações sobre a solicitação HTTP atual dentro de uma rota do Flask. Ele permite que você recupere dados enviados pelo cliente, como parâmetros de consulta ou dados do corpo da solicitação.


