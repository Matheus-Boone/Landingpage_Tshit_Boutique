# 00003-PLAN — Otimização de Performance Mobile-First

> **Objetivo:** Reduzir drasticamente o tempo de carregamento, otimizar o consumo de dados e garantir uma experiência fluida em dispositivos móveis (4G/LTE).

---

## 📊 Diagnóstico Atual — O Problema

### Inventário de Assets (Peso Total Estimado: ~45 MB)

| Categoria | Qtd | Peso Total | Problema |
|---|---|---|---|
| **Imagens de Produtos (PNG)** | 4 | **~21 MB** | 🔴 CRÍTICO. PNGs gigantes (~5 MB cada). Sem compressão. |
| **Vídeo Frames (WebP)** | 240 | **~11.5 MB** | 🟡 ALTO. Todos carregados de uma vez no JS (`preloadImages`). |
| **Vídeos de Feedback (MP4)** | 10 | **~7.2 MB** | 🟡 ALTO. 20 tags `<video>` (10 originais + 10 duplicados). Autoplay em TODOS. |
| **Prints de Feedback (JPG/WebP)** | 10 | **~2.2 MB** | 🟢 MODERADO. `loading="lazy"` presente, mas sem `srcset`. |
| **Fotos Seção Fem/Masc (JPEG)** | 7 | **~576 KB** | 🟢 OK. Tamanhos razoáveis. Falta `loading="lazy"`. |
| **Logo (WebP)** | 1 | **~460 KB** | 🟡 ALTO. Para uma logo vetorial, é excessivo. |
| **Vídeos originais (MP4)** | 2 | **~21 MB** | 🔴 CRÍTICO. Não são usados na página, mas estão no repositório. |

### Dependências Externas (Bloqueadoras de Renderização)

| Recurso | Tipo | Impacto |
|---|---|---|
| `cdn.tailwindcss.com` (com plugins) | JS render-blocking | 🔴 **~300 KB+ parse time** em runtime |
| Google Fonts (Newsreader + Manrope) | CSS render-blocking | 🟡 **2 requests de roundtrip** |
| Google Material Symbols | CSS render-blocking | 🟡 **Duplicado** (2x a mesma tag `<link>`) |

### Problemas de Código

| Problema | Onde | Impacto |
|---|---|---|
| `preloadImages()` carrega **240 frames de uma vez** | Script final | 🔴 **11.5 MB de download imediato** |
| `requestAnimationFrame` roda **continuamente** (sem throttle) | Script final | 🟡 Consome CPU/bateria constantemente |
| Vídeos do carrossel com `autoplay` **sem IntersectionObserver** | Seção Feedback | 🔴 **CPU/GPU pesada**: 20 vídeos decodificando simultâneamente |
| Nenhuma imagem usa `srcset` ou `<picture>` | Global | 🟡 Mobile carrega resolução de desktop |
| Nenhum `<meta>` de SEO (description, OG tags) | `<head>` | 🟡 SEO fraco em compartilhamentos |
| `animação_video.mp4` e `video_scroll_final.mp4` no repo | Root | 🟡 **~21 MB** desnecessários no deploy |

---

## 🛡️ Decisões que Requerem Aprovação do Usuário

> [!IMPORTANT]
> **Compressão de Imagens de Produto:** As 4 imagens PNG dos produtos (Aero, Lacoste, Tommy, Tripps) totalizam **21 MB**. A conversão para WebP com qualidade 85% pode reduzir para ~500 KB total (redução de **97%**). Isso altera os arquivos originais — deseja manter os PNGs originais como backup?

> [!WARNING]
> **Tailwind CDN vs Build:** O CDN do Tailwind em runtime é ideal para prototipagem, mas em produção gera ~300 KB de JS que o navegador precisa parsear. A alternativa é gerar um CSS final estático com apenas as classes utilizadas. Isso requer instalar Node.js e rodar um build. Deseja seguir com essa abordagem?

> [!CAUTION]
> **Remoção de Vídeos Brutos:** Os arquivos `animação_video.mp4` (14.7 MB) e `video_scroll_final.mp4` (6.8 MB) estão na raiz e não são referenciados no HTML. Removê-los do repositório economiza ~21 MB no clone/deploy. Confirma a remoção?

---

## 🏗️ Plano de Execução

### Fase 1: Compressão de Assets (Impacto Máximo, Risco Mínimo)

#### 1.1 — Converter Imagens de Produto PNG → WebP

| Arquivo | Atual | Estimado pós-WebP |
|---|---|---|
| `aero for man.png` | 5.9 MB | ~120 KB |
| `lacoste.png` | 5.4 MB | ~110 KB |
| `tommy hilfiger.png` | 4.5 MB | ~100 KB |
| `tripps.png` | 5.3 MB | ~110 KB |
| **Total** | **21.1 MB** | **~440 KB** |

**Ação:** Usar script Python com Pillow ou `cwebp` do Google para converter com qualidade 85%.  
**Atualizar:** `index.html` — trocar extensões `.png` → `.webp`.

#### 1.2 — Otimizar Logo

| Arquivo | Atual | Estimado |
|---|---|---|
| `logovetorizada.webp` | 460 KB | ~50 KB |

**Ação:** Recomprimir com qualidade 80% e redimensionar para max 400px de largura (suficiente para o uso no site).

#### 1.3 — Otimizar Prints de Feedback

**Ação:** Redimensionar JPGs grandes (>200 KB) para max 600px de largura.  
**Resultado esperado:** De ~2.2 MB → ~800 KB total.

---

### Fase 2: Lazy Loading Inteligente de Vídeos

#### 2.1 — IntersectionObserver para Vídeos do Carrossel

**Problema atual:** 20 `<video>` com `autoplay` carregando e decodificando simultaneamente.

**Solução:**

```javascript
// Apenas dar play nos vídeos que estão na viewport
const videoObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    const video = entry.target;
    if (entry.isIntersecting) {
      video.play();
    } else {
      video.pause();
      video.currentTime = 0;
    }
  });
}, { rootMargin: '200px' });

document.querySelectorAll('#experiencia video').forEach(v => {
  v.removeAttribute('autoplay');
  videoObserver.observe(v);
});
```

#### 2.2 — Lazy Source Loading nos Vídeos

**Solução:** Trocar `src` por `data-src` e carregar o `src` real apenas quando o `IntersectionObserver` detectar proximidade.

---

### Fase 3: Carregamento Progressivo dos Video Frames

#### 3.1 — Carregar Frames sob Demanda (Chunked Loading)

**Problema atual:** `preloadImages()` dispara 240 requests HTTP simultaneamente.

**Solução:**

```javascript
// Carregar apenas os frames próximos ao progresso atual
const loadChunk = (centerFrame, range = 20) => {
  const start = Math.max(1, centerFrame - range);
  const end = Math.min(frameCount, centerFrame + range);
  for (let i = start; i <= end; i++) {
    if (!images[i - 1]) {
      const img = new Image();
      img.src = currentFrame(i);
      images[i - 1] = img;
    }
  }
};

// No scroll handler, carregar chunk antes de renderizar
const updateScrolly = () => {
  // ... calcular frameIndex ...
  loadChunk(frameIndex, 30); // Carrega 30 frames em cada direção
  render();
};
```

**Resultado:** Carrega ~60 frames por vez em vez de 240. Reduz download inicial de **11.5 MB → ~2.8 MB**.

#### 3.2 — Throttle no requestAnimationFrame

**Solução:** Limitar a 30 FPS no mobile para economizar bateria.

```javascript
let lastTime = 0;
const targetFPS = 30;
const frameInterval = 1000 / targetFPS;

const updateScrolly = (timestamp) => {
  if (timestamp - lastTime < frameInterval) {
    requestAnimationFrame(updateScrolly);
    return;
  }
  lastTime = timestamp;
  // ... lógica atual ...
};
```

---

### Fase 4: Otimização do `<head>` (Render-Blocking)

#### 4.1 — Remover `<link>` Duplicado do Material Symbols

**Problema:** A mesma folha de estilo `Material+Symbols+Outlined` está carregada **2 vezes** (linhas 10 e 11).

**Ação:** Remover a linha 11 (duplicata).

#### 4.2 — Preconnect para Google Fonts

**Ação:** Adicionar antes dos `<link>` de fontes:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

#### 4.3 — Meta Tags de SEO e Open Graph

```html
<meta name="description" content="T-Shirt Boutique: moda urbana premium com peças 100% originais e importadas. Marcas como Lacoste, Tommy Hilfiger, Tripps e Aero For Men com estoque limitado.">
<meta property="og:title" content="T-Shirt Boutique - Urban Premium">
<meta property="og:description" content="Peças exclusivas de moda urbana. 100% originais e importadas.">
<meta property="og:image" content="screen.png">
<meta property="og:type" content="website">
```

---

### Fase 5: Responsive Images com `srcset`

#### 5.1 — Implementar `srcset` nas Imagens Principais

Para imagens de produtos e seções masculina/feminina, servir tamanhos diferentes conforme a tela:

```html
<img 
  srcset="assets/imagens-produtos/aero-for-man-400w.webp 400w,
          assets/imagens-produtos/aero-for-man-800w.webp 800w"
  sizes="(max-width: 768px) 400px, 800px"
  src="assets/imagens-produtos/aero-for-man-800w.webp"
  alt="Camiseta Aero For Men"
  loading="lazy"
/>
```

**Ação:** Gerar 2 variantes de cada imagem (400px e 800px de largura).

#### 5.2 — `loading="lazy"` em Todas as Imagens Abaixo da Dobra

**Ação:** Adicionar `loading="lazy"` em TODAS as `<img>` exceto a hero (primeira visível).

---

### Fase 6: Limpeza do Repositório

#### 6.1 — Remover Arquivos Não Utilizados

| Arquivo | Tamanho | Status |
|---|---|---|
| `animação_video.mp4` | 14.7 MB | ❌ Não referenciado no HTML |
| `video_scroll_final.mp4` | 6.9 MB | ❌ Não referenciado no HTML |
| `screen.png` | 433 KB | ⚠️ Pode ser usado para OG image |
| `get_video_info.py` | 555 B | ❌ Script utilitário, não é deploy |

**Ação:** Remover via `git rm` ou mover para `.gitignore`.

---

## 📈 Impacto Estimado

| Métrica | Antes | Depois | Melhoria |
|---|---|---|---|
| **Peso Total da Página** | ~45 MB | ~6 MB | **-87%** |
| **Requests Iniciais** | ~260+ | ~30 | **-88%** |
| **First Contentful Paint** | ~4-6s (4G) | ~1.5-2s (4G) | **-66%** |
| **Largest Contentful Paint** | ~8-12s (4G) | ~3-4s (4G) | **-66%** |
| **Consumo de Bateria** | Alto (rAF + 20 vídeos) | Baixo (throttle + IO) | **Significativo** |

---

## ✅ Checklist de Verificação

- [ ] Todas as imagens PNG convertidas para WebP
- [ ] Logo recomprimida
- [ ] `<link>` duplicado do Material Symbols removido
- [ ] `preconnect` adicionado para Google Fonts
- [ ] Meta tags SEO/OG inseridas
- [ ] Vídeos do carrossel com IntersectionObserver (play/pause automático)
- [ ] Carregamento progressivo dos 240 frames (chunks)
- [ ] Throttle de 30 FPS no scroll listener (mobile)
- [ ] `loading="lazy"` em todas as imagens below-the-fold
- [ ] Arquivos não utilizados removidos do repositório
- [ ] Teste no Chrome DevTools (Lighthouse mobile)
- [ ] Teste em dispositivo real (4G throttle)

---

## 🔢 Prioridade de Execução

| # | Fase | Esforço | Impacto |
|---|---|---|---|
| 1 | **Compressão de Imagens PNG → WebP** | Baixo | 🔴 MÁXIMO |
| 2 | **IntersectionObserver nos Vídeos** | Baixo | 🔴 ALTO |
| 3 | **Carregamento Progressivo dos Frames** | Médio | 🔴 ALTO |
| 4 | **Otimização do `<head>`** | Baixo | 🟡 MÉDIO |
| 5 | **Responsive Images (`srcset`)** | Médio | 🟡 MÉDIO |
| 6 | **Limpeza do Repositório** | Baixo | 🟢 BAIXO |
