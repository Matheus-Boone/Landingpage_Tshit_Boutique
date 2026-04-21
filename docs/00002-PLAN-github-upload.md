# 00002 - PLAN - Upload para o GitHub

Este plano descreve as etapas para inicializar o controle de versão e subir o projeto para um novo repositório no GitHub do usuário `Matheus-Boone`.

## 1. Visão Geral
Atualmente o projeto não possui controle de versão (Git). Vamos inicializar um repositório local, configurar o que deve ser ignorado e usar o GitHub CLI para criar o repositório remoto e subir os arquivos.

## 2. Divisão de Tarefas

### Fase 1: Configuração Local
- [ ] Criar arquivo `.gitignore`.
- [ ] Rodar `git init`.
- [ ] Adicionar arquivos: `git add .`.
- [ ] Primeiro commit: `git commit -m "feat: initial landing page setup"`.

### Fase 2: Criar Repositório no GitHub
- [ ] Rodar `gh repo create Landingpage_Tshit_Boutique --public --source=. --remote=origin --push`.
- [ ] Verificar se o push foi concluído.

## 3. Portão Socrático (Decisões Requeridas)
1. **Privacidade**: Deseja que o repositório seja **Público** ou **Privado**? (O padrão será público).
2. **Nome**: O nome `Landingpage_Tshit_Boutique` está bom para o repositório?

## 4. Verificação
- [ ] O comando `git remote -v` exibe a URL correta.
- [ ] O repositório está acessível via web.
