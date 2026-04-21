# 00003 - PLAN - Segmentação de Público (Expansão do Layout)

🤖 **Aplicando conhecimento de `@[frontend-specialist]` + `@[frontend-design]`...**

## 1. Visão Geral

Adicionar duas novas seções segmentadas por gênero à landing page, posicionadas **após a seção "Panteão das Marcas" (Section 3)** e **antes da seção "Experiência e Prova Social" (Section 4)**. A narrativa flui naturalmente: o visitante conhece as marcas → se identifica no universo masculino ou feminino → vê a prova social.

A transição entre as duas seções deve ser **sutil e orgânica**, utilizando apenas mudanças tonais de fundo (sem bordas, conforme a regra "No-Line" do DESIGN.md), criando a sensação de dois universos dentro da mesma boutique.

---

## 2. Arquitetura de Seções (Posicionamento Final)

```
┌─────────────────────────────────────┐
│  1. HERO                            │
│  2. Video Scrollytelling            │
│  3. Curadoria                       │
│  4. Panteão das Marcas              │
│  ──────────────────────────────────  │  ← Inserção aqui
│  5. 🆕 O PADRÃO MASCULINO          │
│  6. 🆕 A EXCLUSIVIDADE FEMININA    │
│  ──────────────────────────────────  │
│  7. Experiência e Prova Social      │
│  8. Footer                          │
└─────────────────────────────────────┘
```

---

## 3. Design Detalhado por Seção

### 3.1 — Seção "O Padrão Masculino" (`#masculino`)

#### Identidade Visual
- **Fundo**: `bg-surface-container-lowest` (#0e0e0e) — o nível mais profundo e pesado da paleta. Aplicar uma textura CSS sutil via `background-image` com noise grain ultra-leve (opacidade ~3%) para transmitir uma sensação tátil e brutalista.
- **Acento**: Branco/cinza prata (`on-surface` #e2e2e2 e `secondary` #c6c6c6) como cores dominantes de texto, com `#FF1493` aparecendo **apenas** nos CTAs e em micro-detalhes (linhas decorativas, badges).

#### Layout: Zigue-Zague Editorial (2 blocos)
Cada bloco ocupa largura total (`max-w-7xl`) e é um grid de 2 colunas (`lg:grid-cols-2`). A ordem se inverte a cada bloco usando `lg:order-1` / `lg:order-2`:

```
┌──────────────────────────────────────────┐
│  BLOCO 1:                                │
│  [COPY esquerda]  |  [MÍDIA direita]     │
│                                          │
│  BLOCO 2:                                │
│  [MÍDIA esquerda] |  [COPY direita]      │
└──────────────────────────────────────────┘
```

- **Copy do Bloco 1**: Headline serif (Newsreader) grande. Subtítulo curto e direto. Foco em **status e autoridade**.
  - Headline: *"Presença Que Dispensa Apresentações."*
  - Subtítulo: *"Cortes precisos e marcas que definem autoridade. Para quem não precisa provar nada — só vestir."*
- **Copy do Bloco 2**: Foco em **durabilidade e caimento**.
  - Headline: *"Caimento Sob Medida. Tecido Que Resiste."*
  - Subtítulo: *"Algodão pesado, costuras reforçadas e silhuetas que valorizam. Cada peça foi feita para durar e impressionar."*

#### Mídia
- **Vídeos curtos em loop** (`.mp4`, `autoplay`, `muted`, `loop`, `playsinline`), mostrando o caimento das peças no corpo masculino.
- Formato `aspect-[3/4]` (retrato), com bordas arredondadas moderadas (Level 2) e efeito `grayscale` que revela cores no hover.
- **Fallback**: Caso os vídeos não estejam prontos, usar `<img>` com `data-alt` descritivo para gerar imagens via IA posteriormente.

#### CTA
- Botão `#FF1493` com glow neon e link para WhatsApp, copy: *"Montar Meu Look Masculino"*

#### Transição de Saída (para a seção feminina)
- Um `div` com gradiente vertical: `bg-gradient-to-b from-surface-container-lowest via-[#1a1a1a] to-[#1c1a1b]` (movendo sutilmente do preto puro para um preto com microtonalidade rosada/quente). Altura de `h-24 md:h-32`. **Zero bordas**.

---

### 3.2 — Seção "A Exclusividade Feminina" (`#feminino`)

#### Identidade Visual — A "Quebra Sutil"
- **Fundo**: `bg-[#1c1a1b]` — Um chumbo muito escuro com uma micro-camada quente, diferenciando-se sutilmente do preto bruto da seção masculina. A sensação é de **seda escura**.
- **Acento `#FF1493`**: Aqui ele aparece de forma mais **refinada e delicada**: em tipografia italic, em linhas finas horizontais decorativas (`w-16 h-[1px] bg-primary-container/40`), e em micro-detalhes como o foco de cor em hover de imagens.
- **Tipografia**: Maior uso de `italic` no Newsreader para trazer elegância e suavidade editorial.

#### Layout: Galeria Editorial de Detalhes (Assimétrico)
Diferente do zigue-zague da seção masculina, aqui usamos um layout que **respira mais** — refletindo a sofisticação do público feminino:

```
┌──────────────────────────────────────────┐
│  BLOCO INTRO (Full-Width, Centralizado): │
│      Headline + Subtítulo + Linha Rosa   │
│                                          │
│  GALERIA ASSIMÉTRICA (3 colunas):        │
│  [IMG tall]  |  [IMG sq] + [IMG sq]     │
│              |           (stacked)       │
│                                          │
│  BLOCO COPY FINAL (Full-Width, Centro):  │
│      Frase de impacto + CTA             │
└──────────────────────────────────────────┘
```

- No mobile, a galeria colapsa para uma coluna única com espaçamento generoso.

#### Copy
- **Headline Intro**: *"A União Perfeita Entre Conforto Absoluto e Design Global."*
- **Subtítulo**: *"Peças selecionadas para mulheres que ditam seu próprio estilo. Do toque do tecido à exclusividade do design — cada detalhe foi pensado para você."*
- **Frase de impacto final**: *"Exclusividade não se compra em qualquer lugar."* (italic, primary color)

#### Mídia
- **Fotos editoriais** focadas em **detalhes**: textura do tecido, composições com blazer + t-shirt, looks casuais premium.
- Formato misto: 1 imagem em `aspect-[3/5]` (tall) + 2 imagens em `aspect-square` empilhadas.
- Efeito: `grayscale hover:grayscale-0` com `transition-all duration-700`, mantendo o padrão editorial da seção Curadoria.

#### CTA
- Botão com estilo ligeiramente diferente: `bg-transparent border border-pink-500/50 text-pink-400` com hover que revela o `bg-[#FF1493]`. Copy: *"Explorar Coleção Feminina"*. Essa diferença sutil no estilo do CTA reforça a personalidade distinta da seção.

---

## 4. Detalhes Técnicos de Implementação

### 4.1 Arquivo Modificado
- **`index.html`**: Inserir as duas novas `<section>` + o bloco de transição entre elas, após a `</section>` do Panteão das Marcas (linha ~313) e antes da Section 4 "Experiência e Prova Social" (linha ~314).

### 4.2 Navegação (Navbar)
- Adicionar links `#masculino` e `#feminino` à navbar (opcional, pode ser um submenu de "CURADORIA").
- Ou substituir o link "AUTENTICIDADE" por dois links segmentados.

### 4.3 Considerações de Performance
- Vídeos em loop devem ser curtos (5-8 segundos), comprimidos via H.264 com bitrate baixo (~1-2mbps).
- Usar `loading="lazy"` em todas as `<img>` das novas seções.
- Usar `preload="none"` nos `<video>` para que não disputem banda com o vídeo scrollytelling.

### 4.4 CSS Adicional
- Classe utilitária `.noise-texture` para o background grain da seção masculina (usando `background-image` com um SVG inline ou data-URI de ruído).

---

## 5. Portão Socrático — Decisões Requeridas

> [!IMPORTANT]
> Antes de começarmos a codar, preciso das suas respostas:

1. **Mídia Real vs. Placeholder**: Você já possui os vídeos curtos masculinos e as fotos femininas? Ou devo usar imagens geradas por IA como placeholder para montar a estrutura visual?

2. **Navegação**: Deseja adicionar links na navbar para `#masculino` e `#feminino`? Ou prefere que o usuário descubra as seções naturalmente pelo scroll?

3. **Copy Final**: Os textos que propus acima estão alinhados com o tom da boutique? Gostaria de ajustar alguma headline ou subtítulo?

---

## 6. Checklist de Verificação

- [ ] Transição entre seção masculina e feminina é imperceptível (sem bordas, só tonal).
- [ ] Layout zigue-zague responsivo funciona no mobile (empilha corretamente).
- [ ] Galeria assimétrica feminina colapsa elegantemente em tela pequena.
- [ ] Vídeos em loop não prejudicam performance (preload=none, muted, playsinline).
- [ ] CTAs de ambas as seções direcionam para WhatsApp com mensagens contextuais.
- [ ] Consistência com o Design System: sem bordas 1px, espaçamento Level 2, arredondamento moderado.
- [ ] Efeitos hover dos cards seguem o padrão grayscale→color da seção Curadoria.
