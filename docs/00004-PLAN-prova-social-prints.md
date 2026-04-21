# 00004 - PLAN - Prova Social com Prints Reais

🤖 **Aplicando conhecimento de `@[frontend-specialist]` + `@[frontend-design]`...**

## 1. Problema Atual

A seção "Experiência e Prova Social" (linhas 432-499 do `index.html`) está usando:
- 3 cards estáticos com imagens geradas por IA (genéricas, não reais).
- Textos de depoimentos fictícios embutidos diretamente no HTML.
- Grid fixo de 3 colunas que não escala para mais conteúdo.

**Objetivo**: Transformar esta seção em uma vitrine de **prints reais de conversas/feedbacks** de clientes (screenshots do WhatsApp, Instagram DMs, etc.), preparada para receber **volume variável** de imagens sem precisar editar o HTML toda vez.

---

## 2. Nova Arquitetura da Seção

### 2.1 Estrutura Proposta

```
┌─────────────────────────────────────────────────┐
│  HEADER (centralizado)                          │
│  Headline + Subtítulo + Contador de avaliações  │
├─────────────────────────────────────────────────┤
│  CARROSSEL INFINITO DE PRINTS (Marquee Duplo)   │
│                                                 │
│  Linha 1: ← scroll automático (esq → dir)       │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐  │
│  │print1│ │print2│ │print3│ │print4│ │print5│  │
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘  │
│                                                 │
│  Linha 2: → scroll automático (dir → esq)       │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐  │
│  │print6│ │print7│ │print8│ │print9│ │printN│  │
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘  │
│                                                 │
├─────────────────────────────────────────────────┤
│  CTA (centralizado)                             │
│  "Fazer Parte Desta Comunidade"                 │
└─────────────────────────────────────────────────┘
```

### 2.2 Por que Marquee/Carrossel Infinito?

- **Escalabilidade**: Funciona com 6 ou 60 prints sem quebrar o layout.
- **Confiança visual**: O movimento constante e a **quantidade visível** de prints passam credibilidade massiva — o olho humano lê "muitas pessoas satisfeitas" antes mesmo de ler qualquer texto (Lei de Miller + efeito de bandwagon).
- **Consistência**: Já usamos exatamente este padrão na seção "Panteão das Marcas" com as logos, então a linguagem visual se mantém coesa.
- **Pausa no hover**: Permite que o usuário pause e examine um print específico com atenção.

---

## 3. Design Detalhado

### 3.1 Header da Seção

- **Headline**: *"Quem Veste, Aprova."* (Newsreader, serif, grande)
- **Subtítulo**: *"Feedbacks reais de clientes reais. Sem filtro, sem edição."* (Manrope, `text-secondary`)
- **Badge de contagem** (opcional): `"150+ avaliações 5★"` — chip pequeno com ícone de estrela em `text-primary`. Atualizar manualmente conforme cresce.

### 3.2 Cards de Print

Cada print é um card minimalista que funciona como uma "moldura de celular":

```css
/* Conceito do card */
.print-card {
    width: 280px;         /* largura fixa para uniformidade no carrossel */
    flex-shrink: 0;
    aspect-ratio: 9/16;   /* proporção de tela de celular (retrato) */
    border-radius: Level 2 (moderado);
    overflow: hidden;
    background: surface-container-high;
    border: ghost-border (1px sutil);
}
```

- **Imagem**: `object-cover` preenchendo o card inteiro. A imagem **é** o card — sem texto abaixo, sem nome, sem estrelas. O print fala por si.
- **Hover**: Leve `scale(1.03)` + sombra mais intensa + `grayscale(0)` caso esteja com filtro.
- **Click/Tap (opcional futuro)**: Expandir o print em um lightbox/modal para leitura completa.

### 3.3 Organização dos Arquivos de Imagem

Criar uma pasta dedicada para os prints:

```
assets/
└── prints/
    ├── print-01.webp
    ├── print-02.webp
    ├── print-03.webp
    ├── ...
    └── print-N.webp
```

**Regras dos arquivos**:
- Formato: `.webp` (compressão superior, suportado em todos os browsers modernos).
- Resolução recomendada: **560px de largura** (2x do card de 280px, para telas retina).
- Nomenclatura sequencial: `print-01.webp`, `print-02.webp`, etc.
- **Privacidade**: Borrar/censurar dados sensíveis (número de telefone, foto de perfil) antes de salvar.

### 3.4 Animação do Marquee

Reutilizar as `@keyframes marquee` e `marquee-reverse` que já existem na seção de marcas (linhas 310-311), ajustando a velocidade:

- **Linha 1**: `animation: marquee 60s linear infinite` (esquerda para direita, mais lento que as logos pois os prints precisam de mais tempo de leitura).
- **Linha 2**: `animation: marquee-reverse 65s linear infinite` (velocidade ligeiramente diferente para evitar sincronia artificial).
- **Hover no container pai**: `[animation-play-state: paused]` — para o scroll e mostra que os cards são interagíveis.

### 3.5 Responsividade

| Breakpoint | Largura do card | Cards visíveis |
|------------|----------------|----------------|
| Mobile (<640px) | 220px | ~1.5 (revela parcialmente o próximo) |
| Tablet (640-1024px) | 250px | ~3 |
| Desktop (>1024px) | 280px | ~4-5 |

---

## 4. Implementação Técnica

### 4.1 Arquivos Modificados

| Arquivo | Ação |
|---------|------|
| `index.html` | Substituir o conteúdo da Section "Experiência e Prova Social" (linhas 432-499) |

### 4.2 Novo Arquivo/Pasta

| Caminho | Ação |
|---------|------|
| `assets/prints/` | **[NEW]** Pasta para armazenar os prints `.webp` do usuário |

### 4.3 Estrutura HTML Simplificada

```html
<section id="experiencia" class="py-16 md:py-24 bg-surface overflow-hidden">
  <!-- Header -->
  <div class="text-center max-w-3xl mx-auto px-4 space-y-4 mb-12">
    <h2>Quem Veste, Aprova.</h2>
    <p>Feedbacks reais de clientes reais. Sem filtro, sem edição.</p>
  </div>

  <!-- Marquee Container -->
  <div class="space-y-4 md:space-y-6 group">
    <!-- Linha 1: Esquerda → Direita -->
    <div class="flex items-center min-w-max animate-[marquee_60s_linear_infinite] group-hover:[animation-play-state:paused]">
      <!-- Duplicar o set inteiro para loop seamless -->
      <div class="flex gap-4">
        <!-- print cards aqui (metade 1) -->
      </div>
      <div class="flex gap-4">
        <!-- print cards aqui (metade 2 = cópia da 1) -->
      </div>
    </div>

    <!-- Linha 2: Direita → Esquerda -->
    <div class="flex items-center min-w-max animate-[marquee-reverse_65s_linear_infinite] group-hover:[animation-play-state:paused]">
      <!-- Mesma estrutura duplicada -->
    </div>
  </div>

  <!-- CTA -->
  <div class="text-center pt-12 px-4">
    <a href="https://wa.me/...">Fazer Parte Desta Comunidade</a>
  </div>
</section>
```

### 4.4 Adicionando Novos Prints (Fluxo Futuro)

Para adicionar um novo print, o usuário só precisa:
1. Salvar a imagem em `assets/prints/print-XX.webp`.
2. Adicionar uma `<img>` no HTML dentro de ambas as metades do marquee (para manter o loop contínuo).

> **Melhoria futura possível**: Um script JS que lê a pasta e gera os cards automaticamente (requer server-side ou build tool).

---

## 5. Portão Socrático — Decisões Requeridas

> [!IMPORTANT]
> Preciso de respostas antes de implementar:

1. **Quantidade inicial**: Quantos prints reais você tem prontos agora? (O mínimo recomendado para o marquee ficar visualmente cheio são **8-10 prints**.)

2. **Formato dos prints**: São prints de conversas do **WhatsApp**? **Instagram DMs**? **Avaliações do Google**? (Isso afeta o aspect-ratio ideal dos cards.)

3. **Privacidade**: Os prints já estão com dados sensíveis borrados (número de telefone, foto de perfil)? Ou precisa que eu considere um overlay de blur automático?

4. **Lightbox**: Deseja que ao clicar num print ele abra em tela maior (modal/lightbox)? Ou apenas o carrossel visual é suficiente por enquanto?

---

## 6. Checklist de Verificação

- [ ] Marquee roda suavemente sem "pulo" no loop (duplicação correta dos cards).
- [ ] Hover pausa a animação e permite leitura.
- [ ] Cards mantêm proporção correta em todas as telas.
- [ ] Imagens em `.webp` com `loading="lazy"` para performance.
- [ ] CTA direciona para WhatsApp com mensagem contextual.
- [ ] Sem bordas 1px — apenas `ghost-border` sutil (conforme DESIGN.md).
- [ ] Pasta `assets/prints/` criada e documentada para fácil manutenção.
