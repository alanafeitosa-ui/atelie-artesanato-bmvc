# *Sistema de gestão para ateliê de artesanato*

## *Sobre*
Sistema web desenvolvido para a disciplina de programação orientada a objetos utilizando a arquitetura BMVC.
O sistema é destinado exclusivamente ao proprietário de um ateliê de artesanato, permitindo gerenciar produtos, clientes, pedidos, matérias-primas e estoque de forma organizada.

---

## *Objetivo*
Desenvolver um sistema seguindo os princípios da Programação Orientada a Objetos e da arquitetura MVC, contemplando os requisitos dos quatro níveis da disciplina.

---

## *Funcionalidades*
- Cadastro de produtos;
- Cadastro de clientes;
- Cadastro de pedidos;
- Controle de estoque;
- Controle de matéria-prima;
- Sistema de login;
- Área administrativa;
- Atualização de estoque em tempo real via WebSocket, sem necessidade de recarregar a página.

---

## *Tecnologias* 
- Python;
- Flask;
- Flask-SocketIO;
- Socket.IO (cliente);
- SQLite;
- HTML5;
- CSS3;
- JavaScript.

---

## *Arquitetura*
O projeto segue o padrão **BMVC**
```
Boundary
↓
Controller
↓
Model
↓
SQLite
↓
View (Templates HTML)
```
---

## *Estrutura do projeto*
```
src/
|
|--app.py
|--websocket.py
|--controllers/
|--models/
|--boundary/
|--database/
|--templates/
|--static/
|   |--css/
|   |--js/

---

## *Como executar*
```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Criar o banco de dados
cd src/database
python database.py
cd ../..

# 3. Rodar o servidor
cd src
python app.py
```
Acesse `http://127.0.0.1:5000` no navegador.

**Login padrão:** `admin` / `123456`

---

## *Modelagem*
O sistema utiliza conceitos de Orientação a Objetos como:
- Abstração;
- Herança;
- Encapsulamento;
- Polimorfismo;
- Enum;
- Associação;
- Composição.

---

## *Principais Classes*
- Produto(abstrata)
- ProdutoProntaEntrega
- ProdutoEncomenda
- Cliente
- Pedido
- ItemPedido
- MateriaPrima
- Usuario

---

## *Integrantes*
- Alana Cristyna
- Yasmim Ayres

---

## *Status*
✅ Concluído — Níveis Ⅰ, Ⅱ, Ⅲ e Ⅳ entregues
