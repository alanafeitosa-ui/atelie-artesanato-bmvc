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
- Área administrativa
- Atualização em tempo real (WebSocket).

---

## *Tecnologias* 
- Python;
- Flask;
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
|--controllers/
|--models/
|--boundary/
|--database/
|--templates/
|--static/
```
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
🚧 Em desenvolvimento