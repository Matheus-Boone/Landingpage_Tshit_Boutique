# 🚀 Antigravity Kit — Guia Completo

> O **Antigravity Kit** é um sistema modular que transforma a IA em um **time completo de especialistas** para desenvolvimento de software. Ele fica dentro da pasta `.agent/` do seu projeto.

---

## 🧠 O que é?

É um **framework de instruções** que expande as capacidades da IA. Em vez de ter uma IA genérica, você passa a ter **20 especialistas**, **37 skills** e **11 comandos rápidos** trabalhando para você.

```
Sem Antigravity:  IA genérica → Respostas genéricas
Com Antigravity:  IA + Especialistas → Respostas profissionais e contextuais
```

---

## 📁 Estrutura do Kit

```
.agent/
├── agents/       → 20 Agentes Especialistas (personas de IA)
├── skills/       → 37 Skills (módulos de conhecimento)
├── workflows/    → 11 Workflows (comandos /slash)
├── scripts/      → Scripts de validação automática
├── rules/        → Regras globais (GEMINI.md)
└── ARCHITECTURE.md → Mapa completo do sistema
```

---

## 🤖 Agentes — Seus "Funcionários Virtuais"

Cada agente é um **especialista** com regras, princípios e conhecimentos próprios. A IA **seleciona automaticamente** o melhor agente com base no que você pede.

| Agente | O que faz | Quando usar |
|--------|-----------|-------------|
| 🎨 `frontend-specialist` | UI/UX Web, React, Next.js | "Crie uma página de login" |
| ⚙️ `backend-specialist` | APIs, lógica de negócio, Node.js | "Crie uma API REST" |
| 📱 `mobile-developer` | Apps iOS/Android, React Native | "Crie um app mobile" |
| 🗄️ `database-architect` | Schema DB, SQL, Prisma | "Modele o banco de dados" |
| 🔒 `security-auditor` | Segurança, OWASP, vulnerabilidades | "Audite a segurança do projeto" |
| 🐛 `debugger` | Análise de causa raiz | "Encontre o bug nesse código" |
| 📋 `project-planner` | Planejamento, descoberta | "Planeje esse projeto" |
| 🎭 `orchestrator` | Coordena múltiplos agentes | Tarefas complexas multi-domínio |
| 🧪 `test-engineer` | Testes unitários, E2E | "Crie testes para isso" |
| 🚀 `performance-optimizer` | Core Web Vitals, otimização | "Otimize a performance" |
| 🔍 `seo-specialist` | SEO, rankeamento | "Melhore o SEO" |
| 📝 `documentation-writer` | Documentação técnica | "Documente essa API" |
| 🕹️ `game-developer` | Jogos, mecânicas | "Crie um jogo" |
| 🔴 `penetration-tester` | Segurança ofensiva | "Teste de penetração" |
| 🏗️ `devops-engineer` | CI/CD, Docker | "Configure o deploy" |
| 📦 `product-manager` | Requisitos, user stories | "Defina os requisitos" |
| 🧭 `explorer-agent` | Análise de codebase | "Analise esse projeto" |
| 🏛️ `code-archaeologist` | Código legado, refactoring | "Refatore esse código antigo" |

> **💡 Você não precisa selecionar manualmente!** A IA detecta o domínio do seu pedido e ativa o agente correto automaticamente.

---

## 🧩 Skills — Conhecimentos Especializados

Skills são **módulos de conhecimento** que os agentes usam. Pense neles como "livros de referência" que a IA consulta.

### Categorias principais:

| Categoria | Skills incluídas |
|-----------|-----------------|
| **Frontend/UI** | `react-best-practices`, `frontend-design`, `tailwind-patterns`, `web-design-guidelines` |
| **Backend/API** | `api-patterns`, `nodejs-best-practices`, `python-patterns` |
| **Banco de Dados** | `database-design` |
| **Testes** | `testing-patterns`, `webapp-testing`, `tdd-workflow` |
| **Segurança** | `vulnerability-scanner`, `red-team-tactics` |
| **Arquitetura** | `app-builder`, `architecture`, `plan-writing`, `brainstorming` |
| **Mobile** | `mobile-design` |
| **SEO** | `seo-fundamentals`, `geo-fundamentals` |
| **DevOps** | `deployment-procedures`, `server-management` |
| **Código Limpo** | `clean-code`, `code-review-checklist`, `lint-and-validate` |

---

## ⚡ Workflows — Comandos Rápidos `/slash`

Esta é a parte mais prática para o seu dia a dia. **Digite um comando e a IA executa um fluxo completo.**

| Comando | O que faz | Exemplo de uso |
|---------|-----------|----------------|
| `/create` | Cria uma aplicação do zero | "Quero criar um SaaS de gestão" |
| `/plan` | Gera plano de projeto detalhado | "Planeje um sistema de e-commerce" |
| `/brainstorm` | Sessão de brainstorming guiada | "Preciso de ideias para resolver X" |
| `/enhance` | Adiciona/melhora features existentes | "Adicione autenticação ao app" |
| `/debug` | Investigação sistemática de bugs | "Esse endpoint retorna erro 500" |
| `/test` | Gera e executa testes | "Crie testes para o módulo de auth" |
| `/deploy` | Executa deploy com checks pré-voo | "Deploy para produção" |
| `/preview` | Inicia servidor de desenvolvimento | "Quero visualizar as mudanças" |
| `/orchestrate` | Coordena múltiplos especialistas | "Análise completa do projeto" |
| `/status` | Mostra progresso do projeto | "Como está o projeto?" |
| `/ui-ux-pro-max` | Design de UI com 50 estilos e 21 paletas | "Crie uma interface premium" |

---

## 🎯 Como Usar no Dia a Dia

### 1. **Para começar um projeto novo**
```
Você: /create
→ A IA faz perguntas sobre seu projeto
→ Define stack, arquitetura, estrutura
→ Gera todo o código base
```

### 2. **Para planejar antes de codar**
```
Você: /plan Quero criar um sistema de agendamento
→ A IA gera um plano detalhado em 4 fases
→ Análise → Planejamento → Solução → Implementação
```

### 3. **Para debugar um problema**
```
Você: /debug O login não está funcionando
→ Ativa o agente debugger com metodologia de 4 fases
→ Investiga sistematicamente até encontrar a causa raiz
```

### 4. **Para criar interfaces bonitas**
```
Você: /ui-ux-pro-max Crie uma dashboard administrativa
→ 50 estilos de design disponíveis
→ 21 paletas de cores pré-definidas
→ 50 fontes curadas
```

### 5. **Para pedidos simples (sem comando)**
```
Você: "Corrija esse bug" ou "Adicione um botão"
→ A IA auto-detecta o agente correto
→ Aplica as skills relevantes
→ Entrega código profissional
```

### 6. **Para validar antes do deploy**
```
Você: "final checks" ou "son kontrolleri yap"
→ Executa checklist.py automaticamente
→ Verifica: Segurança → Lint → Schema → Testes → UX → SEO
```

---

## 🔑 Dicas Importantes

1. **Gate Socrático**: Para pedidos complexos, a IA vai **perguntar antes de codar**. Isso é intencional — garante que o resultado seja exatamente o que você precisa.

2. **Roteamento Automático**: Você não precisa dizer "use o agente X". Basta descrever o que quer e o sistema escolhe o especialista correto.

3. **Regras Globais**: O `clean-code` é aplicado a **todo** código gerado, garantindo qualidade consistente.

4. **Prioridade de Regras**: [GEMINI.md](file:///c:/Users/mateu/OneDrive/Documentos/Configs/Antigravity/.agent/rules/GEMINI.md) (P0) > `Agent .md` (P1) > `SKILL.md` (P2).

---

## 📊 Resumo em Números

| Métrica | Valor |
|---------|-------|
| Agentes especialistas | 20 |
| Skills de conhecimento | 37 |
| Comandos /slash | 11 |
| Scripts de validação | 2 master + 18 skill-level |
| Cobertura | ~90% dev web/mobile |
