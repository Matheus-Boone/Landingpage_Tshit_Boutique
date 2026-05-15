# Projeto: Otimização de SEO para WhatsApp

## Visão Geral
Melhorar a renderização dos links da página "T-Shirt Boutique" ao serem compartilhados via WhatsApp, focando no Open Graph (OG), imagem de preview com dimensões adequadas (<300KB, JPG/PNG, Webp não é ideal para clientes antigos), e inclusão de tags essenciais.

## 🛑 Socratic Gate (Esperando Respostas do Usuário)
**Antes de iniciar a implementação**, por favor, responda a estas 3 perguntas estratégicas para garantirmos o sucesso:

1. **URL Base:** Qual será o domínio ou link final de produção do site? (ex: `https://tshirtboutique.com.br`). O WhatsApp e o Facebook exigem caminhos absolutos na tag `og:url` e `og:image` para funcionarem sem falhas.
2. **Imagem de Compartilhamento:** A tag atual aponta para `screen.webp`. O WhatsApp é muito rigoroso com o tamanho da imagem de preview (deve ser menor que 300KB) e o formato ideal para compatibilidade máxima é **JPG** ou **PNG** (1200x630px). Você gostaria que eu gerasse/otimizasse uma imagem nova ou já possui o arquivo final?
3. **Mensagem / Descrição:** A descrição que aparece hoje é *"Peças exclusivas de moda urbana. 100% originais e importadas."* Deseja manter isso, ou adicionar alguma *Call to Action* (chamada) específica para quem vê o link no WhatsApp?

## Tipo de Projeto
WEB

## Critérios de Sucesso
- Links compartilhados no WhatsApp exibem título, descrição e imagem de pré-visualização corretamente em todas as plataformas (iOS, Android, Web).
- Imagem estática (<300KB, JPG/PNG) com tags `og:image:width`, `og:image:height` e `og:image:type` definidas.
- Adição da tag `og:url` para evitar problemas de rastreamento e cache do WhatsApp.

## Tech Stack
- HTML5 Meta Tags (Open Graph / Twitter Cards)
- Ferramenta de Otimização de Imagens (Conversão para JPG)

## Estrutura de Arquivos
- `index.html` (Modificação do `<head>`)
- `assets/seo-image.jpg` (Criação de imagem nova ou conversão de existente)

## Divisão de Tarefas

### Tarefa 1: Otimização de Assets para o WhatsApp
- **Agente:** `frontend-specialist`
- **Skill:** `seo-fundamentals`
- **Prioridade:** P1
- **Descrição:** Converter o asset atual (ou o que for definido no Socratic Gate) para JPG, garantir proporção ~1.91:1 e tamanho inferior a 300KB.
- **INPUT:** Imagem base ou nova imagem.
- **OUTPUT:** Novo arquivo em `assets/` (ex: `whatsapp-preview.jpg`).
- **VERIFY:** O tamanho do arquivo gerado deve ser garantidamente menor que 300KB e em formato amplamente suportado (JPG/PNG).

### Tarefa 2: Implementação de Meta Tags Avançadas
- **Agente:** `frontend-specialist`
- **Skill:** `seo-fundamentals`
- **Prioridade:** P2
- **Descrição:** Atualizar o cabeçalho do `index.html` com o bloco completo do Open Graph, removendo o apontamento falho para .webp e substituindo por URLs absolutos ou corretos baseados nas respostas do Socratic Gate.
- **INPUT:** `index.html`, URL base e título fornecidos.
- **OUTPUT:** `index.html` atualizado com todas as tags do protocolo Open Graph e Twitter Card.
- **VERIFY:** Tags `<meta property="og:image:width">`, `<meta property="og:image:height">`, `<meta property="og:url">` foram incluídas e o arquivo foi validado sem quebra de sintaxe.

## ✅ PHASE X: Verificação Final
- [ ] O arquivo da imagem possui extensão `.jpg` ou `.png` e pesa menos de 300KB.
- [ ] O `index.html` contém tags Open Graph completas.
- [ ] O `index.html` contém tags para Twitter Cards (`twitter:card` etc).
- [ ] Não há erro no path da imagem e as dimensões (width/height) declaradas correspondem à realidade.
