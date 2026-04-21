from PIL import Image
import os

images = ["aero for man.png", "lacoste.png", "tommy hilfiger.png", "tripps.png"]
source_dir = "assets/backup_originals"
dest_dir = "assets/imagens-produtos"

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

for img_name in images:
    try:
        source_path = os.path.join(source_dir, img_name)
        dest_path = os.path.join(dest_dir, img_name.replace(".png", ".webp"))
        
        with Image.open(source_path) as img:
            img.save(dest_path, "WEBP", quality=85)
            print(f"Convertida: {img_name} -> {dest_path}")
    except Exception as e:
        print(f"Erro ao converter {img_name}: {e}")
