Objetivo da atividade
Nesta atividade, você deverá aplicar, de forma prática, três padrões de projeto amplamente
utilizados em sistemas orientados a objetos (Factory Method, Strategy, e Observer). O foco
será:
● Compreender quando e como aplicar padrões para resolver problemas recorrentes de
projeto;
● Melhorar a flexibilidade e a manutenibilidade do código por meio de boas abstrações
e desacoplamento entre componentes;
● Praticar a modelagem e implementação orientada a objetos em Python, respeitando
princípios como SRP e OCP (Princípios SOLID).
Contexto do problema
Você foi contratado para desenvolver um sistema de pedidos online para uma cafeteria
artesanal, que está modernizando seu atendimento. A cafeteria oferece diversos produtos
(cafés, chás, doces) com possibilidade de personalização (adicionais, tamanhos, embalagens
ecológicas).
O gerente deseja um sistema modular, que permita:
● Cadastrar e preparar diferentes tipos de bebidas;
● Oferecer diferentes estratégias de desconto (ex: fidelidade, horário promocional);
● Enviar notificações automatizadas (para cozinha, cliente, e histórico do pedido).
Como o cardápio muda com frequência, e novas promoções são lançadas a cada semana, o
sistema deve ser flexível e fácil de manter.
Atividade
Implemente, em Python, um sistema simplificado de pedidos para a cafeteria. O sistema deve
conter:
Factory Method

Para a criação de diferentes tipos de bebidas e comidas (ex: CafeLatte, CháVerde,
Brownie, etc.).
● Cada produto deve herdar de uma interface comum Produto, com atributos como
nome, preço base e preparo.
● Um método fabrica_produto(tipo: str) deve instanciar o produto correto
com base na string de entrada.
Strategy
Para aplicação de diferentes estratégias de desconto, como:
● Cliente frequente (desconto fixo),
● Promoção do dia (por tipo de produto),
● Cupom personalizado (por porcentagem).

Essas estratégias devem implementar uma interface comum EstrategiaDesconto, e
serem aplicadas ao total do pedido.
Observer
Para permitir que diferentes partes do sistema sejam notificadas quando um pedido for
finalizado:
● NotificadorCliente envia confirmação (simulada via print);
● NotificadorCozinha informa os itens a preparar;
● LoggerSistema registra o pedido em um histórico.
Dica: O pedido deve funcionar como objeto observado, e os notificadores como observadores
registrados.