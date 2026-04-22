# Scroll-Driven Color Revival — Landing Page T-Shirt Boutique

As imagens da landing page ficam em modo `grayscale` por padrão, mas o usuário mobile raramente para para fazer hover. O objetivo é fazer cada imagem **ganhar cor, brilho e vida automaticamente conforme o usuário scrolla**, sem exigir nenhuma interação — efeito "foto revelando-se em quarto escuro".

## Estratégia: Híbrida (B + A)

| Camada | Tecnologia | Browsers | Mecanismo |
|--------|-----------|---------|----------|
| **Principal** | CSS Scroll-Driven Animations API | Chrome/Edge 115+ | `animation-timeline: view()` — zero JS, off-main-thread |
| **Fallback** | IntersectionObserver | Safari + Firefox + todos | Anima ao entrar na viewport via CSS class toggle |
| **Legado** | `group-hover` (já existente) | Qualquer | Permanece para interação desktop |

---

## Proposed Changes

### Seção 1 — CSS Global (dentro de `<style>` no `index.html`)

#### [MODIFY] [index.html](file:///c:/Users/mateu/OneDrive/Documentos/Projects/Landingpage_Tshit_Boutique/index.html)

Adicionar ao bloco `<style>` já existente:

**1. Classe-base para todas as imagens animadas:**
```css
.scroll-colorize {
  filter: grayscale(1) brightness(0.6) saturate(0);
  transform: scale(1.03);
  transition: filter 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94),
              transform 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  will-change: filter, transform;
}
```

**2. Estado "revelado" (aplicado pelo IntersectionObserver — fallback):**
```css
.scroll-colorize.is-revealed {
  filter: grayscale(0) brightness(1) saturate(1.1);
  transform: scale(1);
}
```

**3. CSS Scroll-Driven Animation (browsers modernos — override do fallback):**
```css
@supports (animation-timeline: view()) {
  @keyframes colorReveal {
    from { filter: grayscale(1) brightness(0.6) saturate(0); transform: scale(1.04); }
    to   { filter: grayscale(0) brightness(1) saturate(1.1); transform: scale(1);    }
  }

  .scroll-colorize {
    animation: colorReveal linear both;
    animation-timeline: view();
    animation-range: entry 5% cover 55%;
    /* Override transition pois a API cuida do timing */
    transition: none;
  }

  /* Garante que hover ainda funciona em desktop sobre o estado base */
  .scroll-colorize:hover {
    filter: grayscale(0) brightness(1.05) saturate(1.2);
    transform: scale(1) !important;
  }
}
```

**4. Respeito a `prefers-reduced-motion`:**
```css
@media (prefers-reduced-motion: reduce) {
  .scroll-colorize {
    filter: grayscale(0) brightness(1) saturate(1);
    transform: scale(1);
    animation: none;
    transition: none;
  }
}
```

---

### Seção 2 — HTML: Substituição de classes nas imagens

Substituir `grayscale group-hover:grayscale-0 transition-all duration-700` pela classe `scroll-colorize` em **todas as imagens afetadas**:

#### Curadoria (linha ~272–283) — 4 imagens de produto
```html
<!-- ANTES -->
<img class="... grayscale group-hover:grayscale-0 transition-all duration-700" ...>

<!-- DEPOIS -->
<img class="... scroll-colorize" ...>
```
> Remover também `group` dos containers quando não for mais necessário para outros efeitos.

#### Masculino — Bloco 1 (linha ~400) — 1 imagem
```html
<!-- ANTES -->
<img ... class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700 ease-in-out scale-105 group-hover:scale-100">

<!-- DEPOIS -->
<img ... class="w-full h-full object-cover scroll-colorize">
```
> A classe `scroll-colorize` já cuida de `scale` — remover as classes Tailwind de escala.

#### Masculino — Bloco 2 (linha ~410) — 1 imagem
Mesma substituição.

#### Feminino — Galeria Assimétrica (linhas ~463, ~470, ~474) — 3 imagens
```html
<!-- ANTES -->
<img ... class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700 ease-in-out">

<!-- DEPOIS -->
<img ... class="w-full h-full object-cover scroll-colorize">
```

---

### Seção 3 — JavaScript: IntersectionObserver (Fallback Universal)

Adicionar ao final do `<body>`, após o script do Scrollytelling existente:

```js
(function() {
  // Executa apenas se a Scroll-Driven API NÃO estiver disponível
  if (CSS.supports('animation-timeline', 'view()')) return;

  const images = document.querySelectorAll('.scroll-colorize');
  if (!images.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-revealed');
          // Após revelar, para de observar (performance)
          observer.unobserve(entry.target);
        }
      });
    },
    {
      threshold: [0.15, 0.35],
      rootMargin: '0px 0px -5% 0px'
    }
  );

  images.forEach(img => observer.observe(img));
})();
```

---

## Efeito Visual Final

```
Estado Inicial (fora da viewport):
  filter: grayscale(1) brightness(0.6) saturate(0)
  transform: scale(1.04)
  → Imagem escura, sem cor, levemente ampliada

Durante o scroll (entry 5% → cover 55%):
  grayscale(1→0) brightness(0.6→1) saturate(0→1.1)
  scale(1.04→1)
  → Cor "derramando" na imagem, brilho aumentando, leve zoom-out

Estado Final (dentro da viewport):
  filter: grayscale(0) brightness(1) saturate(1.1)
  transform: scale(1)
  → Imagem totalmente viva, com leve boost de saturação (premium feel)
```

---

## Arquivos Afetados

| Arquivo | Tipo de mudança |
|---------|----------------|
| `index.html` / `<style>` | [MODIFY] Adicionar 4 blocos CSS |
| `index.html` / `<body>` (Curadoria) | [MODIFY] 4 imgs — trocar classes Tailwind |
| `index.html` / `<body>` (Masculino) | [MODIFY] 2 imgs — trocar classes Tailwind |
| `index.html` / `<body>` (Feminino) | [MODIFY] 3 imgs — trocar classes Tailwind |
| `index.html` / `<script>` (final) | [MODIFY] Adicionar IntersectionObserver |

**Total: 1 arquivo, ~50 linhas adicionadas/modificadas.**

---

## Open Questions

> [!IMPORTANT]
> **Manter ou remover o `group-hover` nas seções?**
> Proposta: remover das imagens que passam a usar `scroll-colorize`, pois o efeito de hover ainda funciona via `.scroll-colorize:hover` no bloco `@supports`. Mas se quiser manter o `group-hover` como camada extra em desktop, posso preservar.

> [!NOTE]
> **Saturate boost (`saturate(1.1)`)**: O estado final aplica uma leve supersaturação para dar o "pop" visual de peça de moda premium. Pode ser ajustado para `1.0` se preferir fidelidade de cor real.

---

## Verification Plan

### Testes Automatizados
- Nenhum script de teste necessário para esta mudança (pura CSS/DOM)

### Verificação Manual
1. **Chrome/Edge (moderno):** Scrollar cada seção e verificar que a cor revela-se progressivamente com o scroll — frame a frame
2. **Firefox/Safari (fallback):** Verificar que ao entrar na viewport a imagem anima suavemente de cinza para cor via `transition`
3. **Mobile (scroll real):** Testar em dispositivo Android/iPhone — validar que o efeito não causa jank
4. **`prefers-reduced-motion`:** Ativar nas configurações do SO e verificar que as imagens aparecem sempre coloridas (sem animação)
5. **Hover desktop:** Verificar que o hover ainda dá um boost sutil de saturação sobre o estado já revelado
