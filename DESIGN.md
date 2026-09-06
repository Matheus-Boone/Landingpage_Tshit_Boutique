# 🏛️ Design System: T-Shirt Boutique (Urban Premium)

> **Documento Oficial de Diretrizes de Design, Tokens e Componentes**  
> **Conceito Criativo:** *"The Underground Gallery"*  
> **Público & Estilo:** Moda urbana premium, curadoria de luxo, streetwear autêntico e marcas globais importadas.

---

## 1. Visão Criativa & North Star

### "The Underground Gallery"
Este design system rejeita intencionalmente o modelo de e-commerce genérico e "seguro", adotando uma **experiência editorial imersiva**. Cada peça é tratada como uma obra de arte em exposição.

A identidade visual é fundamentada na **tensão estética** entre:
- A **crueza industrial urbana** dos tons escuros profundos (`#0e0e0e` / `#131313`).
- A **sofisticação de alta costura** representada pelo contraste do neon pink (`#FF1493` / `#ff479c`) e do brilho metálico (`#c6c6c6`).

---

## 2. Paleta de Cores & Tokens de Superfície

O sistema adota uma escala refinada de *Dark Mode* (*Surface Hierarchy*), criando profundidade física e hierarquia sem depender de linhas divisórias duras.

### 🎨 Tabela de Cores & Tokens

| Categoria | Token Tailwind | Código HEX | Aplicação & Propósito |
| :--- | :--- | :--- | :--- |
| **Acento Primário** | `primary` | `#ffb0ca` / `#FF1493` | Chamadas de ação (CTAs), destaques interativos e links ativos |
| **Container Primário**| `primary-container` | `#ff479c` | Fundo de destaque vibrante e fonte do efeito neon |
| **Texto em Primário** | `on-primary` | `#640036` | Contraste de texto sobre o fundo primário |
| **Base de Fundo** | `background` / `surface` | `#131313` | Cor padrão de fundo do corpo da página |
| **Superfície Nível 0**| `surface-container-lowest` | `#0e0e0e` | Camada mais profunda (Hero, Preloader e Rodapé) |
| **Superfície Nível 1**| `surface-container-low` | `#1b1b1b` | Cards de produtos e blocos de conteúdo |
| **Superfície Nível 2**| `surface-container` | `#1f1f1f` | Containers intermediários e seções agrupadas |
| **Superfície Nível 3**| `surface-container-high` | `#2a2a2a` | Gavetas, modais e elementos flutuantes |
| **Superfície Nível 4**| `surface-container-highest`| `#353535` | Elementos de apoio e tags neutras |
| **Tipografia Principal**| `on-surface` | `#e2e2e2` | Textos de leitura principal e títulos |
| **Tipografia Secundária**| `secondary` / `on-secondary`| `#c6c6c6` / `#b5b5b5`| Textos de suporte, legendas e metadados |
| **Bordas Fantasma** | `outline-variant` | `#5b3f48` / `rgba(91,63,72,0.2)` | Delimitação sutil sem fechamento visual pesado |
| **Sucesso / WhatsApp** | `tertiary` | `#6ae04d` / `#2fa714` | Badges de estoque, autenticidade e status ativo |

---

## 3. Tipografia: O Emparelhamento "High-Low"

Combinação da autoridade clássica editorial de uma fonte com serifa com a legibilidade moderna de uma geométrica sem serifa.

```
┌─────────────────────────────────────────────────────────────┐
│  Newsreader (Serif)   → Editorial, Expressivo, Exclusivo    │
│  Manrope (Sans-serif) → Funcional, Técnico, Legível         │
└─────────────────────────────────────────────────────────────┘
```

### Escala Tipográfica

| Função | Família | Tamanhos Usuais | Peso / Estilo | Uso |
| :--- | :--- | :--- | :--- | :--- |
| **Display Hero** | `Newsreader` (`font-headline`) | `3rem` a `4rem` (48px–64px) | `500 Medium`, `italic` em destaque | Título de abertura com sobreposição |
| **Headline / Seções**| `Newsreader` (`font-headline`) | `1.75rem` a `2.5rem` (28px–40px)| `500 Medium` / `600 Semi-bold` | Títulos das seções principais |
| **Subtítulos & Nomes**| `Manrope` (`font-body`) | `1.125rem` a `1.25rem` (18px–20px)| `600 Semi-bold` / `700 Bold` | Nomes de peças e marcas |
| **Corpo de Texto** | `Manrope` (`font-body`) | `0.875rem` a `1rem` (14px–16px) | `400 Regular`, entrelinha `relaxed` | Descrições e parágrafos |
| **Labels & Tags** | `Manrope` (`font-label`) | `0.625rem` a `0.75rem` (10px–12px)| `700 Bold`, `uppercase`, `tracking-widest` | Preços, status de estoque e categorias |

* **Ícones:** `Material Symbols Outlined` (Google Fonts), configurado com `font-variation-settings: 'FILL' 0|1, 'wght' 400, 'opsz' 24`.

---

## 4. Elevação, Iluminação & Efeitos Visuais

### 1. A Regra do "No-Line"
É proibido o uso de linhas sólidas horizontais (`<hr>` ou `border-b`) para separar seções. A transição deve ser orgânica, feita puramente pela variação tonal do fundo (`#0e0e0e` → `#131313` → `#1b1b1b`).

### 2. Efeito Neon Glow (`.neon-glow`)
Simula a iluminação tátil de letreiros neon urbanos em ambientes escuros:
```css
.neon-glow {
    box-shadow: 0 0 15px rgba(255, 71, 156, 0.3);
}
.neon-glow:hover {
    box-shadow: 0 0 25px rgba(255, 71, 156, 0.5);
}
```

### 3. Ghost Border (`.ghost-border`)
Borda de baixa opacidade para campos de entrada ou botões secundários, evitando fechar rigidamente os elementos:
```css
.ghost-border {
    border: 1px solid rgba(91, 63, 72, 0.2);
}
```

### 4. Glassmorphism na Navegação
Barra de topo flutuante com desfoque e transparência:
```html
<nav class="fixed top-0 w-full z-50 bg-neutral-950/80 backdrop-blur-xl shadow-[0_4px_30px_rgba(0,0,0,0.5)]">
```

### 5. Textura de Ruído Analógico (`.noise-texture`)
Camada SVG imperceptível (`opacity: 0.03`) que elimina a sensação de "plástico digital" e confere textura de papel fotográfico editorial.

### 6. Scroll-Driven Color Revival
Técnica onde as fotografias das peças iniciam em preto-e-branco granulado (`grayscale(1) brightness(0.6)`) e revelam sua cor e nitidez reais à medida que entram na visão do usuário através do scroll.

---

## 5. Biblioteca de Componentes

### 🔘 Botões
- **Primário (CTA Master):** Fundo `#FF1493`, texto de alto contraste, bordas sutis (`rounded-sm`), acompanhado de `.neon-glow`.
- **Secundário (Consultor / Outline):** Fundo transparente, borda `border-pink-500/50`, texto rosa e transição suave para preenchimento no hover.
- **Terciário (Texto Editorial):** Texto `Newsreader` ou `Manrope` com sublinhado expansivo e micro-interação.

### 🖼️ Vitrine & Cards de Produtos (Frameless Style)
- Sem bordas pesadas de contorno;
- Imagens em proporção vertical editorial (`aspect-[3/4]` ou `aspect-[4/5]`);
- Tipografia de preço em destaque limpo;
- Selo de autenticidade integrado.

### 🏷️ Badges & Chips de Escassez
- Pílula translúcida com indicador pulsante (`bg-pink-500 animate-ping` / `animate-pulse`) sinalizando estoque ultralimitado e exclusividade de importação.

### ⏳ Preloader de Experiência
- Animação circular rosa neon com contador percentual e efeito de transição `opacity` ao término do carregamento.

---

## 6. Diretrizes de Espaçamento e Formas

- **Bordas e Cantos:** Moderados (`0.25rem` / `rounded-sm` / `rounded`). Proibido o uso de cantos 100% pontiagudos ou formato de pílula excessivo em cartões estruturais.
- **Espaço em Branco:** Generoso (escala de 4px, 8px, 16px, 24px, 32px, 48px, 64px, 96px) para garantir respiro e atmosfera de luxo.

---

## 7. Regras de Ouro (Do's & Don'ts)

| Fazer (Do) ✅ | Não Fazer (Don't) ❌ |
| :--- | :--- |
| **Utilizar contraste tonal** para criar hierarquia entre seções | **Não usar réguas sólidas (`<hr>`)** ou linhas de 1px como divisores de tela |
| **Harmonizar serifa e sem serifa** (Newsreader nos títulos e Manrope no corpo) | **Não misturar mais de 2 famílias tipográficas** para manter a elegância |
| **Aplicar brilho neon com moderação** em botões principais e estados de foco | **Não usar cores aleatórias** fora da paleta (manter a trinca Preto/Prata/Rosa) |
| **Manter fotos com proporção vertical** e efeito suave de hover | **Não usar cantos excessivamente redondos** em cards de produtos |
| **Dar destaque aos diferenciais de originalidade** com metadados claros | **Não poluir o layout** com excesso de elementos concorrentes |

---

## 8. Código de Configuração (Tailwind CSS)

```javascript
tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        "surface": "#131313",
        "surface-container-lowest": "#0e0e0e",
        "surface-container-low": "#1b1b1b",
        "surface-container": "#1f1f1f",
        "surface-container-high": "#2a2a2a",
        "primary": "#ffb0ca",
        "primary-container": "#ff479c",
        "secondary": "#c6c6c6",
        "on-surface": "#e2e2e2",
        "outline-variant": "#5b3f48",
        "tertiary": "#6ae04d"
      },
      borderRadius: {
        DEFAULT: "0.25rem",
        lg: "0.25rem",
        xl: "0.25rem"
      },
      fontFamily: {
        headline: ["Newsreader", "serif"],
        body: ["Manrope", "sans-serif"],
        label: ["Manrope", "sans-serif"]
      }
    }
  }
}
```