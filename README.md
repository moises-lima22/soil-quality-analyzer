# Soil Quality Analyzer 🌱

Sistema desenvolvido para a atividade avaliativa da disciplina **Gestão do Agronegócio com Python (Capítulos 3 a 6)**, com foco em tecnologias aplicadas ao setor agro. A aplicação analisa amostras de solo com base em parâmetros físico-químicos e classifica o solo como **Apto** ou **Inapto** para plantio, com base em regras de negócio definidas.

---

## 🧪 Parâmetros Avaliados

| Parâmetro    | Faixa Ideal              |
|--------------|--------------------------|
| pH           | 5.5 – 7.0                |
| Nitrogênio   | > 20 ppm                 |
| Fósforo      | > 15 ppm                 |
| Potássio     | > 100 ppm                |
| Compactação  | < 1.4 g/cm³              |

- Se **4 ou mais critérios** forem atendidos, o solo é considerado **Apto**.

---

## 🎯 Propósito no Agronegócio

O sistema atua na **análise da qualidade do solo**, uma etapa crítica no planejamento agrícola. A proposta se alinha com o setor de **serviços de apoio do agronegócio**, facilitando a tomada de decisões sobre cultivo e uso da terra.

---

## 🧠 Conteúdo Técnico Aplicado (Cap. 3 a 6)

- ✅ Funções e procedimentos (subalgoritmos)
- ✅ Listas, tuplas, dicionários
- ✅ Manipulação de arquivos (JSON e texto)
- ✅ Conexão com banco de dados Oracle (modo completo)

---

## 📁 Estrutura do Projeto

```
soil-quality-analyzer/
├── backend/
│   ├── config/                 # Configurações do projeto (ex.: banco de dados)
│   ├── controllers/            # Controladores para rotas e lógica de API
│   ├── services/               # Serviços para lógica de negócios
│   ├── utils/                  # Funções utilitárias (ex.: validações)
│   ├── app.py                  # API principal (Flask)
│   ├── docker-compose.yml      # Configuração Docker para backend e banco
│   ├── Dockerfile              # Dockerfile do backend
│   ├── requirements.txt        # Dependências do backend
│   ├── samples.json            # Base simulada de amostras
│   └── setup_oracle.py         # Script para configurar o banco Oracle
├── frontend/
│   ├── public/                 # Arquivos públicos (ex.: index.html)
│   ├── src/                    # Código-fonte do frontend (Vue 3)
│   │   ├── components/         # Componentes Vue reutilizáveis
│   │   ├── views/              # Páginas principais da aplicação
│   │   ├── App.vue             # Componente raiz
│   │   └── main.js             # Arquivo principal do Vue
│   ├── Dockerfile              # Dockerfile do frontend
│   ├── package.json            # Dependências do frontend
│   ├── vite.config.mjs         # Configuração do Vite
│   └── tsconfig.json           # Configuração TypeScript
├── atividade.txt               # Enunciado original da atividade
├── docker-compose.yml          # Configuração Docker para todo o projeto
└── README.md                   # Documentação do projeto
```

---

## 🚀 Como Executar

O projeto é executado com docker e docker compose

### 🐳 Executar com Docker (Banco de Dados Oracle)

1. Clone o repositório:
   ```bash
   git clone https://github.com/moises-lima22/soil-quality-analyzer.git
   cd soil-quality-analyzer
   ```

2. Suba os containers Docker (backend, frontend e banco de dados Oracle):
   ```bash
   docker-compose up --build
   ```

3. Acesse o sistema no navegador:
   - Frontend: [http://localhost:8080](http://localhost:8080)
   - Backend (API): [http://localhost:5000](http://localhost:5000)

4. O banco de dados Oracle será configurado automaticamente com a tabela necessária para armazenar as amostras de solo.

---

## ✅ Requisitos

 - Docker e Docker Compose instalados

---

## 📊 Relatório e Resultados

As análises podem ser visualizadas via interface gráfica (frontend), contendo:

- 📋 Formulário de entrada
- 🧪 Tabela de amostras
- 📈 Gráfico de distribuição Apto/Inapto

Além disso, os dados podem ser exportados para um arquivo `report.txt` no modo texto, contendo um resumo das análises realizadas.

---

## 👨‍💻 Desenvolvedor

**Moisés da Silva de Lima**  
RM563625 — FIAP 2025

---
