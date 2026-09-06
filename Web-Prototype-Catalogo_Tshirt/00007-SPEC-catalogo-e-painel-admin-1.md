# 📐 Especificação Completa de Telas & UI/UX: Catálogo & Painel Admin
> **Projeto:** T-Shirt Boutique (Urban Premium)  
> **Destinatário:** Time de Design UI/UX & Engenharia Front-end  
> **Conceito Visual:** *"The Underground Gallery"* (Dark Luxury, Neon Glow, Tipografia High-Low Serif/Sans)

---

## 🗺️ Mapa Geral da Aplicação

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. ÁREA PÚBLICA (CLIENTE)                                              │
│   ├── [Tela 01] Landing Page Principal (index.html) → [Já Existente]   │
│   ├── [Tela 02] Catálogo de Peças (catalogo.html)                      │
│   │     ├── [Modal 02.A] Gaveta/Drawer de Filtros Avançados (Mobile)   │
│   │     ├── [Modal 02.B] Visualização Rápida da Peça (Quick Lookbook)  │
│   │     └── [Modal 02.C] Drawer da Sacola de Interesse (WhatsApp)      │
│   └── [Tela 03] Página Individual da Peça / Detalhes (Opcional/SEO)    │
└────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────┐
│ 2. ÁREA ADMINISTRATIVA (LOJISTA)                                       │
│   ├── [Tela 04] Login / Autenticação do Lojista (/admin/login)         │
│   ├── [Tela 05] Dashboard & Listagem de Produtos (/admin/produtos)     │
│   ├── [Tela 06] Cadastro / Edição de Peça (/admin/produtos/novo)       │
│   └── [Tela 07] Gestão de Marcas & Categorias (/admin/marcas)          │
└────────────────────────────────────────────────────────────────────────┘
```

---

# 📱 PARTE 1: Telas da Área do Cliente (Frontend Público)

---

### [Tela 02] Página do Catálogo Principal (`catalogo.html`)
* **Objetivo:** Vitrine editorial imersiva onde o cliente navega pelas camisetas importadas, filtra com agilidade e escolhe as peças desejadas para fechar a compra no WhatsApp.

#### Componentes & Estrutura Visual:
1. **Header Fixo (Glassmorphism):**
   - Logo T-Shirt Boutique à esquerda.
   - Link de retorno: *"← Voltar à Home"*.
   - Ícone/Botão flutuante da **"Sacola de Interesse"** com badge contador (ex: `🛍️ 2`).
2. **Hero Editorial Compacto:**
   - Título estilizado em `Newsreader` (ex: *"Coleções Exclusivas & Importadas"*).
   - Subtítulo em `Manrope` reforçando: *"Peças 100% originais com estoque ultralimitado"*.
3. **Barra de Controle & Filtros Rápidos (Sticky Bar):**
   - **Campo de Busca:** Input com ícone de lupa e texto placeholder: *"Buscar por modelo, marca ou cor..."*.
   - **Filtros em Pílula (Carrossel Horizontal no Mobile):**
     - `[Todas]` | `[Lacoste]` | `[Tommy Hilfiger]` | `[Tripps]` | `[Aero For Men]` | `[Lançamentos 🔥]`.
   - **Filtro de Tamanho:** Chips rápidos: `[P]` `[M]` `[G]` `[GG]`.
   - **Ordenação:** Dropdown (*Mais Recentes*, *Menor Preço*, *Maior Preço*).
   - **Botão "Filtros Avançados":** Abre o Drawer lateral no mobile.
4. **Grid de Produtos (Frameless Layout):**
   - Layout de 2 colunas no Mobile e 4 colunas no Desktop.
   - **Card de Produto (Cada item):**
     - Imagem principal em proporção vertical `3:4` com efeito *Scroll-Driven Color Revival* e hover de zoom sutil.
     - Badge flutuante de status: `[Últimas Unidades]` ou `[100% Original]`.
     - Nome da Marca em caixa-alta `font-label` metálico (`#c6c6c6`).
     - Nome da Peça em `Manrope Semi-bold`.
     - Grade de tamanhos disponíveis (ex: `P • M • G`).
     - Preço formatado (ex: `R$ 289,00` ou `Consulte Condição Especial`).
     - **Ação Principal 1:** Botão *"Pedir no WhatsApp"* (Abre conversa direta com texto pronto).
     - **Ação Principal 2:** Ícone `+` ou *"Adicionar à Sacola"* (para quem quer levar mais de uma peça).
5. **Estado Vazio (Empty State):**
   - Mensagem estilizada caso a busca não retorne peças: *"Nenhuma peça encontrada com esses filtros. Fale com um consultor para buscar sob encomenda."* + Botão WhatsApp.

---

### [Modal 02.B] Visualização Rápida da Peça (*Quick Lookbook Modal*)
* **Objetivo:** Exibir detalhes e fotos em alta resolução sem tirar o cliente da página do catálogo.

#### Componentes & Estrutura Visual:
1. **Galeria de Imagens:** Carrossel/Slides com fotos da frente, costas e detalhes do tecido/bordado.
2. **Painel de Informações:**
   - Selo de Autenticidade (`Garantia de Peça Importada Original`).
   - Título em serifa `Newsreader`.
   - Seletor de Tamanho interativo (o cliente clica no tamanho que deseja).
   - Guia de Medidas rápido em link discreto (*"Ver tabela de medidas"*).
   - Destaques de tecido: `Algodão Pima / Jersey Premium`.
3. **CTAs de Alta Conversão:**
   - Botão Primário Neon (`#FF1493`): **"Garantir Esta Peça no WhatsApp"**.
   - Botão Secundário Ghost: **"Adicionar à Minha Sacola de Atendimento"**.

---

### [Modal 02.C] Drawer da "Sacola de Interesse" (*WhatsApp Batching*)
* **Objetivo:** Permitir que o cliente junte 2 ou 3 camisetas de marcas diferentes e envie uma mensagem única para o consultor, aumentando o ticket médio.

#### Componentes & Estrutura Visual:
1. **Gaveta Lateral Deslizante:** Abre suavemente pela direita.
2. **Lista de Peças Selecionadas:**
   - Miniatura da foto, Marca, Nome, Tamanho escolhido, Preço e botão de remover.
3. **Resumo & Valor Total:** Somatório das peças selecionadas.
4. **Botão Mestre Neon Glow:**
   - **"Enviar Pedido Completo ao Consultor via WhatsApp (X peças)"**.
   - Ao clicar, abre o WhatsApp com a mensagem pré-formatada:
     > *"Olá! Gostei dessas peças do catálogo e quero fechar o pedido:*\n*1. Camiseta Lacoste Classic (Tam M) - R$ 290*\n*2. Camiseta Tommy Hilfiger Essential (Tam M) - R$ 280*\n*Qual a forma de pagamento e envio para o meu CEP?"*

---

# 💻 PARTE 2: Telas do Painel Administrativo (Lojista)

---

### [Tela 04] Login do Lojista (`/admin/login`)
* **Objetivo:** Acesso restrito e seguro para o administrador da boutique.

#### Componentes & Estrutura Visual:
1. **Card Centralizado:** Fundo `surface-container-low` (`#1b1b1b`) com textura sutil e logo da boutique.
2. **Campos:**
   - E-mail / Usuário.
   - Senha (com botão de mostrar/ocultar senha).
3. **Ação:** Botão *"Entrar no Painel"* em Rosa Neon.
4. **Segurança:** Bloqueio contra tentativas excessivas.

---

### [Tela 05] Dashboard & Gestão de Produtos (`/admin/produtos`)
* **Objetivo:** Tela principal onde o lojista vê todo o seu estoque, pesquisa peças e altera disponibilidade em 1 segundo.

#### Componentes & Estrutura Visual:
1. **Header do Admin:**
   - Boas-vindas, botão *"Ver Catálogo Público"* e botão *"Sair"*.
2. **Cards de Métricas Rápidas (Topo):**
   - Total de Peças Ativas no Catálogo.
   - Peças com Estoque Baixo / Últimas Unidades.
   - Total de Cliques no WhatsApp nos últimos 7 dias.
3. **Barra de Ações:**
   - Campo de busca rápida por produto/marca.
   - Filtro por status (`Todos`, `Ativos`, `Esgotados`, `Em Destaque`).
   - Botão de Destaque: `[ + Nova Peça ]`.
4. **Tabela / Grid de Gerenciamento:**
   - **Miniatura da Foto.**
   - **Nome & Marca.**
   - **Tamanhos Cadastrados:** Chips coloridos (`P`, `M`, `G`, `GG`).
   - **Preço (R$).**
   - **Interruptor (Toggle Switch):** Ativar / Desativar visibilidade no site instantaneamente.
   - **Ações Rápidas:** Botão `Editar (Lápis)` e `Excluir (Lixeira)`.

---

### [Tela 06] Cadastro / Edição de Peça (`/admin/produtos/novo` ou `/editar/:id`)
* **Objetivo:** Formulário intuitivo e ultra-rápido, otimizado para preenchimento tanto no computador quanto direto pelo celular do lojista.

#### Campos & Componentes do Formulário:
1. **Upload de Fotos (Drag & Drop + Câmera do Celular):**
   - Foto Principal (Capa) + até 4 fotos secundárias.
   - Pré-visualização instantânea e botão de reordenar fotos.
2. **Informações Básicas:**
   - **Marca:** Dropdown com busca (*Lacoste, Tommy Hilfiger, Tripps, Aero For Men, etc.*) + botão rápido *"Cadastrar nova marca"*.
   - **Nome do Modelo:** Input de texto (ex: *"Camiseta Piquet Crocodilo Classic Verde Militar"*).
   - **Preço:** Input monetário formatado (R$).
3. **Grade de Tamanhos & Estoque:**
   - Checkboxes interativos com badge: `[x] P` `[x] M` `[x] G` `[ ] GG`.
4. **Etiquetas Promocionais / Destaques:**
   - `[ ] Marcar como Lançamento`
   - `[ ] Marcar como Últimas Unidades`
   - `[ ] Peça 100% Original Importada (Selo)`
5. **Descrição Editorial (Opcional):**
   - Caixa de texto com composição (ex: *"100% Algodão Pima, caimento slim fit, toque macio..."*).
6. **Ações:**
   - Botão Secundário: *"Cancelar"*.
   - Botão Primário: **"Salvar e Publicar no Catálogo"**.

---

### [Tela 07] Gestão de Marcas & Categorias (`/admin/marcas`)
* **Objetivo:** Permitir ao lojista adicionar novas marcas ou coleções sem precisar de suporte técnico.

#### Componentes:
1. Listagem das marcas cadastradas com logo da marca.
2. Modal simples para cadastrar nova marca (`Nome`, `Logo / Imagem`, `Descrição Curta`).

---

---

# 📱 PARTE 3: Diretrizes de Responsividade, Ergonomia Tátil & Mobile-First

> **Atenção Designer:** Mais de **85% a 90% do tráfego** da T-Shirt Boutique virá de dispositivos móveis (Instagram Ads, Stories, Links em Bio e Grupos VIP). O catálogo e o painel admin devem ser projetados **Mobile-First**, priorizando o uso com uma única mão (*Thumb Zone*).

---

### 1. Grid Responsivo & Breakpoints

| Dispositivo / Tela | Breakpoint | Estrutura do Grid do Catálogo | Comportamento de Filtros & Navegação |
| :--- | :--- | :--- | :--- |
| **Mobile Pequeno / Médio** | `< 640px` (ex: iPhone, Galaxy) | **2 colunas compactas** (aspect ratio 3:4 das fotos) | Carrossel horizontal de marcas + Botão flutuante inferior para WhatsApp/Sacola |
| **Mobile Grande / Phablet**| `640px – 767px` | **2 colunas confortáveis** com espaçamento lateral de 16px | Barra de filtros sticky no topo com scroll horizontal |
| **Tablet / iPad** | `768px – 1023px` | **3 colunas** | Filtros em barra superior expandida |
| **Desktop / Monitores** | `≥ 1024px` | **4 colunas** | Grid amplo com sidebar ou barra de topo refinada e hover states ricos |

---

### 2. Ergonomia & Zona do Polegar (*Thumb Zone Navigation*)

```
┌─────────────────────────┐
│     Área Difícil        │ ◄── Header & Logo (Apenas visualização)
│       (Topo)            │
├─────────────────────────┤
│                         │
│     Área Natural        │ ◄── Scroll de Produtos & Imagens
│       (Centro)          │
│                         │
├─────────────────────────┤
│     Área Fácil          │ ◄── BOTÕES PRINCIPAIS:
│   (Zona do Polegar)     │     • "Pedir no WhatsApp"
│                         │     • "Filtros Rápidos" / "Sacola"
└─────────────────────────┘
```

1. **Sticky Bottom Action Bar (Barra Fixa Inferior no Mobile):**
   - No celular, o botão de **"Ver Sacola de Interesse (X)"** ou **"Falar com Consultor"** deve ficar fixado na parte inferior da tela, com suporte obrigatório a `safe-area-inset-bottom` (para não sobrepor a barra de navegação do iPhone/Android).
2. **Tamanho Mínimo de Alvos de Toque (Touch Targets):**
   - Todos os botões, ícones de fechar, seletores de tamanho (`P`, `M`, `G`, `GG`) e chips devem ter no mínimo **44x44px** (ideal **48x48px**) de área clicável.
   - Espaçamento de no mínimo **8px** entre botões adjacentes para evitar toques acidentais.

---

### 3. Padrões de Interação Mobile (App-Like Experience)

* **Bottom Sheets (Gavetas Inferiores) em vez de Modais no Mobile:**
  - Ao clicar em *"Filtros Avançados"* ou *"Detalhes da Peça"*, a tela deve abrir uma **gaveta deslizando de baixo para cima** (*Bottom Sheet*) cobrindo 80% a 90% da tela, com alça de arrasto (*drag handle*) para fechar puxando para baixo.
* **Carrossel Horizontal de Filtros (*Snap-to-Point*):**
  - As pílulas de marcas no mobile devem deslizar suavemente para os lados (`overflow-x-auto snap-x no-scrollbar`) com feedback visual claro da marca ativa (borda rosa neon iluminada).
* **Gestos de Swipe nas Fotos:**
  - Na visualização do produto, permitir deslizar com o dedo para a esquerda/direita para ver a foto das costas ou detalhes do tecido.
* **Teclados Otimizados (Inputs):**
  - Campo de busca com `type="search"` e botão instantâneo de limpar (`x`);
  - No painel administrativo, campo de preço abre teclado numérico (`inputmode="decimal"`).

---

### 4. Responsividade do Painel Administrativo (Uso na Loja Física)

O lojista precisa conseguir **cadastrar uma camiseta direto do balcão ou estoque usando o próprio celular**:
- **Upload via Câmera:** O botão de adicionar foto no celular permite abrir direto a câmera do smartphone para fotografar a peça recém-chegada.
- **Visualização em Cards no Mobile:** A tabela de produtos do desktop converte-se em cards empilhados no mobile, com botões grandes de *Editar*, *Excluir* e o interruptor de *Ativo/Pausado*.

---

# 📦 Resumo para o Designer UI/UX

| Tela | Tipo | Prioridade | Principais Desafios de Design |
| :--- | :--- | :--- | :--- |
| **02. Catálogo Geral** | Desktop & Mobile | 🔥 Alta | Filtros fluidos sem poluir a tela, fotos com proporção vertical elegante e botão WhatsApp muito visível. |
| **02.B Lookbook Modal / Bottom Sheet** | Modal / Drawer | 🔥 Alta | Sensação de boutique de luxo, boa navegação entre fotos no mobile com swipe. |
| **02.C Sacola de Atendimento** | Bottom Sheet (Mobile) / Drawer (Desktop) | 🔥 Alta | Visual de carrinho de alta-costura, facilidade de remover/adicionar itens e CTA verde/rosa para WhatsApp. |
| **05. Lista de Produtos (Admin)** | Dashboard Responsivo | Média | Tabela no desktop e cards fáceis no mobile com toggle de ativar/desativar muito acessível. |
| **06. Formulário de Cadastro** | Form Mobile-Friendly | Média | Upload de fotos simples direto da câmera do celular e seleção de tamanhos rápida. |

---

# 🛠️ Como será a Engenharia (Back-end & Front-end)

1. **Front-end do Catálogo (`catalogo.html`):** Desenvolvido em HTML5 + Tailwind CSS + Vanilla JS, consumindo os produtos com performance extrema (carregamento instantâneo) e respeitando 100% o Design System.
2. **Back-end & Banco de Dados:** Banco serverless (Supabase / Firebase / Postgres) para armazenar os produtos e o storage de fotos, com autenticação nativa e segura para o lojista.
3. **Disparador WhatsApp:** Gerador de links dinâmicos `https://wa.me/556992762900?text=...` codificados via URL Encode, já enviando o resumo do pedido limpo e profissional.

