# 🛒 Sistema de Produtos e Clientes

Sistema de linha de comando (CLI) desenvolvido em **Python puro**, para gerenciamento de **clientes**, **produtos** e **vendas**. O projeto foi construído com foco em boas práticas de organização de código, separando responsabilidades entre models, services e menus (camadas de dados, regras de negócio e interface com o usuário).

## ✨ Funcionalidades

### 📦 Produtos
- Cadastrar, listar, buscar, atualizar e remover produtos
- Consultar estoque disponível por produto

### 👤 Clientes
- Cadastrar, listar, buscar, atualizar e remover clientes

### 💰 Vendas
- Iniciar uma nova venda vinculada a um cliente cadastrado
- Adicionar e remover produtos do carrinho
- Cálculo automático de subtotal e total da venda
- Baixa automática no estoque ao finalizar a venda
- Histórico de vendas realizadas

### 📊 Relatórios
- Faturamento total
- Total de produtos vendidos
- Ticket médio
- Produto mais vendido

## 🗂️ Estrutura do projeto

```
User-and-Product-Registration/
├── main.py                    # Ponto de entrada da aplicação
│
├── menus/                     # Camada de interface (CLI)
│   ├── menu_principal.py      # Menu principal do sistema
│   ├── menu_produtos.py       # Menu de produtos
│   ├── menu_clientes.py       # Menu de clientes
│   └── menu_vendas.py         # Menu do fluxo de vendas
│
├── services/                  # Camada de regras de negócio
│   ├── produto_service.py     # CRUD e consulta de estoque
│   ├── cliente_service.py     # CRUD de clientes
│   └── venda_service.py       # Fluxo de vendas e relatórios
│
├── models/                    # Camada de dados (entidades)
│   ├── produto.py
│   ├── cliente.py
│   ├── venda.py
│   └── item_venda.py
│
└── .gitignore
```

## 🏗️ Arquitetura

O projeto segue uma separação simples em três camadas:

1. **Menus** → responsáveis apenas por exibir opções e capturar a entrada do usuário
2. **Services** → concentram toda a lógica de negócio (cadastro, validações, cálculos)
3. **Models** → representam as entidades do sistema (`Produto`, `Cliente`, `Venda`, `ItemVenda`)

Essa organização facilita a manutenção e futura evolução do projeto (por exemplo, trocar o armazenamento em memória por um banco de dados sem impactar a camada de menus).

## 🚀 Como executar

```bash
git clone https://github.com/EnricoBertolacini/User-and-Product-Registration.git
cd User-and-Product-Registration
python main.py
```

> Requer apenas **Python 3.10+** (o projeto usa `match/case`), sem dependências externas.

## 🛠️ Tecnologias

- Python 3 (nativo, sem bibliotecas externas)
- Programação Orientada a Objetos
- Estrutura em camadas (menus / services / models)

## 📌 Possíveis melhorias futuras

- Persistência de dados em arquivo (JSON/CSV) ou banco de dados
- Validações de entrada mais robustas
- Testes automatizados
- Interface gráfica ou web

## 👤 Autor

**Enrico Bertolacini**
[GitHub](https://github.com/EnricoBertolacini)
