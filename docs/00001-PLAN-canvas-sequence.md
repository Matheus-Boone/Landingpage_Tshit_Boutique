# PLAN - Otimização Scrollytelling via Canvas (Opção A)

## 1. Visão Geral
Substituir a atual reprodução nativa de vídeo (`<video>`) pela renderização indexada de imagens em alta velocidade através de um elemento `<canvas>`. Essa abordagem contornará as limitações de hardware do *hardware decoding* (mobile e iOS), promovendo um scrollytelling fluido (60 frames por segundo) independente da direção da rolagem e livrando o processador.

## 2. Divisão de Tarefas

### Fase 1: Pré-Processamento dos Assets (No Terminal)
- Extrair todos os quadros (frames) do arquivo `video_scroll_final.mp4` para uma nova pasta como `assets/video-frames/`.
- Converter e comprimir via FFmpeg para o formato `.webp` de modo a reduzir dramaticamente a carga de rede sem sacrificar os visuais premium.
- Estimar e reduzir a taxa de fps extraído (ex: 24 ou 30fps) visando um peso total saudável para download.

### Fase 2: Ajustes de Interface (HTML/CSS)
- Trocar o `<video id="unboxing-video" class="... object-cover">` por um `<canvas id="unboxing-canvas" class="absolute inset-0 w-full h-full object-cover">`.
- Certificar-se de manter intactos os "Dark Overlays" e cópias para o CSS funcionar como antes, além de redimensionar o canvas responsivamente.

### Fase 3: Engenharia JavaScript e Lógica
- Construir e isolar o mecanismo assíncrono de **Preloading** das imagens para evitar as chamadas piscadas no scroll.
- Acoplar o progresso atual `(0 a 1)` gerado pela bounding box num cálculo baseado na quantidade em array de Imagens, definindo `index = Math.floor(progress * totalDeImagens)`.
- Atualizar dinamicamente a pintura `ctx.drawImage` para cada mínimo evento de roda no scroll/dedo de forma otimizada com `requestAnimationFrame`.

### Fase 4: Otimização Mobile vs Desktop (Bônus Paridade)
- Assegurar que os fade-ins das fontes continuam disparando perfeitamente nos percentis estabelecidos nas linhas de ação (0%–15%, 30%–45% e 70%–90%).

---

## 3. Portão Socrático (Decisões Requeridas)
🤖 **Aplicando conhecimento de `@[project-planner]` e do fluxo Socrático...**  
Antes de gerarmos os códigos para implementarmos esta solução, por favor confirme:

1. **Peso da Carga Inicial**: Ao transformarmos em Canvas, centenas de imagens WebP serão baixadas na entrada do site (podem englobar de 5 a 10 Megabytes no total dependendo da compressão). Estamos de acordo com isso se priorizarmos uma fluidez visual "Apple-like"?
2. **Setup do FFmpeg**: Farei uso dos seus terminais no Windows usando FFmpeg para extrair esses quadros imediatamente do MP4 direto pra pasta. Ele já se encontra instalado no seu sistema ou nós instalaremos?
3. **Responsividade Proporcional**: Originalmente o vídeo corta laterais em modo celular (`object-fit: cover`). Podemos instruir o sistema do Canvas a calcular o mesmo enquadramento sem nos preocupar ativamente na exportação?

---

## 4. Lista de Verificação Pós-Construção (Checklist Final)
- [ ] O `canvas` não perde resolução ou estica agressivamente na troca mobile/desktop.
- [ ] O scrollytelling roda imaculadamente para cima e para baixo em todos browsers modernos.
- [ ] As instâncias antigas de `<video>` e de metadados não sujam o código.
- [ ] Nenhuma tag de texto (`<h2>`, `<p>`) quebra a subida pela ausência do `video.duration`.
