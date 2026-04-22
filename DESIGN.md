# Design System Strategy: Curadoria Premium & Marcas Globais

## 1. Overview & Creative North Star
**Creative North Star: "The Underground Gallery"**
This design system rejects the "standard e-commerce template" in favor of a high-end, editorial experience. It treats streetwear as fine art. The aesthetic is built on the tension between the raw, industrial nature of urban life (#000000) and the high-fashion sophistication of luxury retail (#FF1493). 

By utilizing intentional asymmetry—such as staggered image grids and large-scale serif typography overlapping sleek sans-serif UI—we move away from "safe" layouts. This system creates a digital flagship store that feels exclusive, serious, and deeply intentional.

---

## 2. Colors & Tonal Depth
The color palette is a study in "Dark Mode" sophistication. We do not use pure black for everything; we use layers of darkness to create a sense of physical space.

### The Palette
- **Core Surface:** `surface` (#000000) – The foundation for all screens, reflecting the neutral base.
- **Accent High-Contrast:** `primary` (#FF1493) – The brand's most distinctive chromatic color, used for key interactive elements.
- **Metallic Neutral:** `secondary` (#D3D3D3) – Provides a silver, industrial sheen for supporting UI elements.

### The Rules of Engagement
- **The "No-Line" Rule:** Explicitly prohibit 1px solid borders for sectioning. Boundaries must be defined solely through background shifts.
- **Surface Hierarchy & Nesting:** Use surface tiers to create depth. A "Cart" drawer should feel physically closer to the user than the product gallery.
- **The "Glass & Gradient" Rule:** To avoid a flat, "matte" feel, floating navigation elements must use semi-transparent surface colors with a backdrop-blur. Main CTAs should utilize a subtle linear gradient to add "soul" and dimension.

---

### 3. Typography: The High-Low Mix
We pair the traditional authority of a serif with the modern utility of a geometric sans-serif.

*   **Display & Headlines (Newsreader):** These are our "Editorial" voices. 
    *   **Display-LG:** Reserved for hero messaging. Use tight letter-spacing and overlap images to break the grid.
    *   **Headline-MD:** Used for collection titles.
*   **UI & Body (Manrope):** These are our "Functional" voices.
    *   **Title-SM:** Bold weight for product names and button text.
    *   **Body-MD:** For descriptions. Set with generous line-height to ensure readability against the dark background.
    *   **Label-SM:** All-caps for metadata, price points, and tags.

---

## 4. Elevation & Depth
In this system, depth is felt, not seen. We move away from heavy drop shadows toward "Tonal Layering."

- **The Layering Principle:** Stack darker cards on slightly lighter sections to create a "recessed" look, making the product photography pop forward.
- **Ambient Shadows:** For floating modals, use custom soft shadows. Never use harsh, high-opacity shadows.
- **The "Ghost Border" Fallback:** If a border is required for input fields, use a low-opacity variant. 100% opaque borders are forbidden as they "trap" the design.
- **Subtle Glow:** Primary buttons should emit a soft glow using the primary color to mimic a neon sign in a dark alley.

---

## 5. Components

### Buttons (The "Neon Tactile" Style)
- **Primary:** Background: `primary` (#FF1493). Shape: Moderate Roundedness (Level 2). Add a subtle glow on hover.
- **Secondary:** Background: Transparent. Border: Ghost Border. Text: `on_surface`.
- **Tertiary:** Text only, bold label style, using `secondary` (#D3D3D3) with an underline that expands on hover.

### Cards & Lists (The "Frameless" Style)
- **Product Cards:** Forbid the use of divider lines. Separate product info from the image using consistent vertical white space (Spacing Level 2). 
- **Input Fields:** Use "Underline" style rather than boxed. A 1px line that turns into the primary color on focus.

### Boutique-Specific Components
- **The "Drop" Countdown:** Large headline numbers in a secondary tone with a faint primary outer glow.
- **Exclusive Access Chip:** A container-based chip with a primary dot indicator to signal limited stock.

---

## 6. Do's and Don'ts

### Do:
- **Use "Extreme" White Space:** Follow the Normal (Level 2) spacing scale to allow elements to breathe.
- **Layer Text Over Images:** Use high-contrast text over darkened image overlays to create an editorial feel.
- **Stick to Moderate Curves:** Every corner (cards, buttons, inputs) must use Moderate (Level 2) roundedness. This maintains a sophisticated, balanced brand persona.

### Don't:
- **Don't Use Dividers:** Never use a horizontal rule to separate content. Use background color shifts.
- **Don't Use Sharp or Pill Edges:** The brand is "Urban/High-End." Avoid Level 0 (sharp) or Level 3 (pill) shapes; keep to the defined Moderate roundedness.
- **Don't Overcrowd:** Avoid Level 0 or 1 spacing; the editorial feel requires the breathing room of Level 2.