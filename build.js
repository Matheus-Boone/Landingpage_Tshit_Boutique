const fs = require('fs');
const path = require('path');

const distDir = path.join(__dirname, 'dist');

// Limpa e recria a pasta dist
if (fs.existsSync(distDir)) {
  fs.rmSync(distDir, { recursive: true, force: true });
}
fs.mkdirSync(distDir, { recursive: true });

// Arquivos e pastas que devem ser publicados no site
const publishList = [
  'index.html',
  '404.html',
  '_headers',
  '_redirects',
  'assets',
  'logovetorizada.webp',
  'Web-Prototype-Catalogo_Tshirt'
];

for (const item of publishList) {
  const src = path.join(__dirname, item);
  const dest = path.join(distDir, item);

  if (fs.existsSync(src)) {
    fs.cpSync(src, dest, { recursive: true });
    console.log(`[OK] Copiado: ${item}`);
  } else {
    console.warn(`[AVISO] Item não encontrado: ${item}`);
  }
}

console.log('\n[SUCESSO] Build concluído com sucesso na pasta dist/');
