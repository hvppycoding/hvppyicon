# hvppyicon

Hvppyicon is an alphabet icon generator for Notion.

You can generate single-letter icons with rounded corners, background colors, and optional RGBA customization.

---

## 🎨 Available Preset Colors

You can use one of the following named colors via `-c` or `--color`:

* `gray`
* `brown`
* `orange`
* `yellow`
* `green`
* `blue`
* `purple`
* `pink`
* `red`

These map to predefined RGBA values for convenience.

---

## ⚙️ New: Custom RGBA Colors

You can now pass RGBA values directly to override background and font colors.

### ✅ Example

```bash
hvppyicon -bg "rgba(255, 255, 255, 255)" -fc "rgba(0, 0, 0, 255)" A
```

* `--bg-color` (`-bg`): background color in `"rgba(R,G,B,A)"` format
* `--font-color` (`-fc`): font color in `"rgba(R,G,B,A)"` format
* `--yoffset`: vertical text adjustment in pixels (e.g. `--yoffset -10`)

---

## 🛠️ Installation

```bash
git clone https://github.com/hvppycoding/hvppyicon.git
cd hvppyicon
pip install .
```

---

## ✏️ Usage Examples

### Using a preset color

```bash
hvppyicon -c red -o red_A.png A
```

### Using RGBA colors

```bash
hvppyicon -bg "rgba(240, 240, 240, 255)" -fc "rgba(50, 50, 50, 255)" -o custom_A.png A
```

### Adjusting vertical alignment

```bash
hvppyicon -c blue --yoffset -16 -o adjusted_A.png A
```

---

## 📷 Output Preview

![Example](doc/example_red_A.png)

---

## 📘 Application in Notion

These icons can be uploaded as image blocks or page icons in Notion.

![Application Example](doc/application_example.png)

---

## 📦 Prebuilt Images

Use these images by 'Copy Image Link'.

![A_red.png](doc/images/A_red.png)
![A_orange.png](doc/images/A_orange.png)
![A_yellow.png](doc/images/A_yellow.png)
![A_green.png](doc/images/A_green.png)
![A_blue.png](doc/images/A_blue.png)
![A_purple.png](doc/images/A_purple.png)
![A_pink.png](doc/images/A_pink.png)
![A_brown.png](doc/images/A_brown.png)
![A_gray.png](doc/images/A_gray.png)
![B_red.png](doc/images/B_red.png)
![B_orange.png](doc/images/B_orange.png)
![B_yellow.png](doc/images/B_yellow.png)
![B_green.png](doc/images/B_green.png)
![B_blue.png](doc/images/B_blue.png)
![B_purple.png](doc/images/B_purple.png)
![B_pink.png](doc/images/B_pink.png)
![B_brown.png](doc/images/B_brown.png)
![B_gray.png](doc/images/B_gray.png)
![C_red.png](doc/images/C_red.png)
![C_orange.png](doc/images/C_orange.png)
![C_yellow.png](doc/images/C_yellow.png)
![C_green.png](doc/images/C_green.png)
![C_blue.png](doc/images/C_blue.png)
![C_purple.png](doc/images/C_purple.png)
![C_pink.png](doc/images/C_pink.png)
![C_brown.png](doc/images/C_brown.png)
![C_gray.png](doc/images/C_gray.png)
![D_red.png](doc/images/D_red.png)
![D_orange.png](doc/images/D_orange.png)
![D_yellow.png](doc/images/D_yellow.png)
![D_green.png](doc/images/D_green.png)
![D_blue.png](doc/images/D_blue.png)
![D_purple.png](doc/images/D_purple.png)
![D_pink.png](doc/images/D_pink.png)
![D_brown.png](doc/images/D_brown.png)
![D_gray.png](doc/images/D_gray.png)
![E_red.png](doc/images/E_red.png)
![E_orange.png](doc/images/E_orange.png)
![E_yellow.png](doc/images/E_yellow.png)
![E_green.png](doc/images/E_green.png)
![E_blue.png](doc/images/E_blue.png)
![E_purple.png](doc/images/E_purple.png)
![E_pink.png](doc/images/E_pink.png)
![E_brown.png](doc/images/E_brown.png)
![E_gray.png](doc/images/E_gray.png)
![F_red.png](doc/images/F_red.png)
![F_orange.png](doc/images/F_orange.png)
![F_yellow.png](doc/images/F_yellow.png)
![F_green.png](doc/images/F_green.png)
![F_blue.png](doc/images/F_blue.png)
![F_purple.png](doc/images/F_purple.png)
![F_pink.png](doc/images/F_pink.png)
![F_brown.png](doc/images/F_brown.png)
![F_gray.png](doc/images/F_gray.png)
![G_red.png](doc/images/G_red.png)
![G_orange.png](doc/images/G_orange.png)
![G_yellow.png](doc/images/G_yellow.png)
![G_green.png](doc/images/G_green.png)
![G_blue.png](doc/images/G_blue.png)
![G_purple.png](doc/images/G_purple.png)
![G_pink.png](doc/images/G_pink.png)
![G_brown.png](doc/images/G_brown.png)
![G_gray.png](doc/images/G_gray.png)
![H_red.png](doc/images/H_red.png)
![H_orange.png](doc/images/H_orange.png)
![H_yellow.png](doc/images/H_yellow.png)
![H_green.png](doc/images/H_green.png)
![H_blue.png](doc/images/H_blue.png)
![H_purple.png](doc/images/H_purple.png)
![H_pink.png](doc/images/H_pink.png)
![H_brown.png](doc/images/H_brown.png)
![H_gray.png](doc/images/H_gray.png)
![I_red.png](doc/images/I_red.png)
![I_orange.png](doc/images/I_orange.png)
![I_yellow.png](doc/images/I_yellow.png)
![I_green.png](doc/images/I_green.png)
![I_blue.png](doc/images/I_blue.png)
![I_purple.png](doc/images/I_purple.png)
![I_pink.png](doc/images/I_pink.png)
![I_brown.png](doc/images/I_brown.png)
![I_gray.png](doc/images/I_gray.png)
![J_red.png](doc/images/J_red.png)
![J_orange.png](doc/images/J_orange.png)
![J_yellow.png](doc/images/J_yellow.png)
![J_green.png](doc/images/J_green.png)
![J_blue.png](doc/images/J_blue.png)
![J_purple.png](doc/images/J_purple.png)
![J_pink.png](doc/images/J_pink.png)
![J_brown.png](doc/images/J_brown.png)
![J_gray.png](doc/images/J_gray.png)
![K_red.png](doc/images/K_red.png)
![K_orange.png](doc/images/K_orange.png)
![K_yellow.png](doc/images/K_yellow.png)
![K_green.png](doc/images/K_green.png)
![K_blue.png](doc/images/K_blue.png)
![K_purple.png](doc/images/K_purple.png)
![K_pink.png](doc/images/K_pink.png)
![K_brown.png](doc/images/K_brown.png)
![K_gray.png](doc/images/K_gray.png)
![L_red.png](doc/images/L_red.png)
![L_orange.png](doc/images/L_orange.png)
![L_yellow.png](doc/images/L_yellow.png)
![L_green.png](doc/images/L_green.png)
![L_blue.png](doc/images/L_blue.png)
![L_purple.png](doc/images/L_purple.png)
![L_pink.png](doc/images/L_pink.png)
![L_brown.png](doc/images/L_brown.png)
![L_gray.png](doc/images/L_gray.png)
![M_red.png](doc/images/M_red.png)
![M_orange.png](doc/images/M_orange.png)
![M_yellow.png](doc/images/M_yellow.png)
![M_green.png](doc/images/M_green.png)
![M_blue.png](doc/images/M_blue.png)
![M_purple.png](doc/images/M_purple.png)
![M_pink.png](doc/images/M_pink.png)
![M_brown.png](doc/images/M_brown.png)
![M_gray.png](doc/images/M_gray.png)
![N_red.png](doc/images/N_red.png)
![N_orange.png](doc/images/N_orange.png)
![N_yellow.png](doc/images/N_yellow.png)
![N_green.png](doc/images/N_green.png)
![N_blue.png](doc/images/N_blue.png)
![N_purple.png](doc/images/N_purple.png)
![N_pink.png](doc/images/N_pink.png)
![N_brown.png](doc/images/N_brown.png)
![N_gray.png](doc/images/N_gray.png)
![O_red.png](doc/images/O_red.png)
![O_orange.png](doc/images/O_orange.png)
![O_yellow.png](doc/images/O_yellow.png)
![O_green.png](doc/images/O_green.png)
![O_blue.png](doc/images/O_blue.png)
![O_purple.png](doc/images/O_purple.png)
![O_pink.png](doc/images/O_pink.png)
![O_brown.png](doc/images/O_brown.png)
![O_gray.png](doc/images/O_gray.png)
![P_red.png](doc/images/P_red.png)
![P_orange.png](doc/images/P_orange.png)
![P_yellow.png](doc/images/P_yellow.png)
![P_green.png](doc/images/P_green.png)
![P_blue.png](doc/images/P_blue.png)
![P_purple.png](doc/images/P_purple.png)
![P_pink.png](doc/images/P_pink.png)
![P_brown.png](doc/images/P_brown.png)
![P_gray.png](doc/images/P_gray.png)
![Q_red.png](doc/images/Q_red.png)
![Q_orange.png](doc/images/Q_orange.png)
![Q_yellow.png](doc/images/Q_yellow.png)
![Q_green.png](doc/images/Q_green.png)
![Q_blue.png](doc/images/Q_blue.png)
![Q_purple.png](doc/images/Q_purple.png)
![Q_pink.png](doc/images/Q_pink.png)
![Q_brown.png](doc/images/Q_brown.png)
![Q_gray.png](doc/images/Q_gray.png)
![R_red.png](doc/images/R_red.png)
![R_orange.png](doc/images/R_orange.png)
![R_yellow.png](doc/images/R_yellow.png)
![R_green.png](doc/images/R_green.png)
![R_blue.png](doc/images/R_blue.png)
![R_purple.png](doc/images/R_purple.png)
![R_pink.png](doc/images/R_pink.png)
![R_brown.png](doc/images/R_brown.png)
![R_gray.png](doc/images/R_gray.png)
![S_red.png](doc/images/S_red.png)
![S_orange.png](doc/images/S_orange.png)
![S_yellow.png](doc/images/S_yellow.png)
![S_green.png](doc/images/S_green.png)
![S_blue.png](doc/images/S_blue.png)
![S_purple.png](doc/images/S_purple.png)
![S_pink.png](doc/images/S_pink.png)
![S_brown.png](doc/images/S_brown.png)
![S_gray.png](doc/images/S_gray.png)
![T_red.png](doc/images/T_red.png)
![T_orange.png](doc/images/T_orange.png)
![T_yellow.png](doc/images/T_yellow.png)
![T_green.png](doc/images/T_green.png)
![T_blue.png](doc/images/T_blue.png)
![T_purple.png](doc/images/T_purple.png)
![T_pink.png](doc/images/T_pink.png)
![T_brown.png](doc/images/T_brown.png)
![T_gray.png](doc/images/T_gray.png)
![U_red.png](doc/images/U_red.png)
![U_orange.png](doc/images/U_orange.png)
![U_yellow.png](doc/images/U_yellow.png)
![U_green.png](doc/images/U_green.png)
![U_blue.png](doc/images/U_blue.png)
![U_purple.png](doc/images/U_purple.png)
![U_pink.png](doc/images/U_pink.png)
![U_brown.png](doc/images/U_brown.png)
![U_gray.png](doc/images/U_gray.png)
![V_red.png](doc/images/V_red.png)
![V_orange.png](doc/images/V_orange.png)
![V_yellow.png](doc/images/V_yellow.png)
![V_green.png](doc/images/V_green.png)
![V_blue.png](doc/images/V_blue.png)
![V_purple.png](doc/images/V_purple.png)
![V_pink.png](doc/images/V_pink.png)
![V_brown.png](doc/images/V_brown.png)
![V_gray.png](doc/images/V_gray.png)
![W_red.png](doc/images/W_red.png)
![W_orange.png](doc/images/W_orange.png)
![W_yellow.png](doc/images/W_yellow.png)
![W_green.png](doc/images/W_green.png)
![W_blue.png](doc/images/W_blue.png)
![W_purple.png](doc/images/W_purple.png)
![W_pink.png](doc/images/W_pink.png)
![W_brown.png](doc/images/W_brown.png)
![W_gray.png](doc/images/W_gray.png)
![X_red.png](doc/images/X_red.png)
![X_orange.png](doc/images/X_orange.png)
![X_yellow.png](doc/images/X_yellow.png)
![X_green.png](doc/images/X_green.png)
![X_blue.png](doc/images/X_blue.png)
![X_purple.png](doc/images/X_purple.png)
![X_pink.png](doc/images/X_pink.png)
![X_brown.png](doc/images/X_brown.png)
![X_gray.png](doc/images/X_gray.png)
![Y_red.png](doc/images/Y_red.png)
![Y_orange.png](doc/images/Y_orange.png)
![Y_yellow.png](doc/images/Y_yellow.png)
![Y_green.png](doc/images/Y_green.png)
![Y_blue.png](doc/images/Y_blue.png)
![Y_purple.png](doc/images/Y_purple.png)
![Y_pink.png](doc/images/Y_pink.png)
![Y_brown.png](doc/images/Y_brown.png)
![Y_gray.png](doc/images/Y_gray.png)
![Z_red.png](doc/images/Z_red.png)
![Z_orange.png](doc/images/Z_orange.png)
![Z_yellow.png](doc/images/Z_yellow.png)
![Z_green.png](doc/images/Z_green.png)
![Z_blue.png](doc/images/Z_blue.png)
![Z_purple.png](doc/images/Z_purple.png)
![Z_pink.png](doc/images/Z_pink.png)
![Z_brown.png](doc/images/Z_brown.png)
![Z_gray.png](doc/images/Z_gray.png)
![A_white.png](doc/images/A_white.png)
![B_white.png](doc/images/B_white.png)
![C_white.png](doc/images/C_white.png)
![D_white.png](doc/images/D_white.png)
![E_white.png](doc/images/E_white.png)
![F_white.png](doc/images/F_white.png)
![G_white.png](doc/images/G_white.png)
![H_white.png](doc/images/H_white.png)
![I_white.png](doc/images/I_white.png)
![J_white.png](doc/images/J_white.png)
![K_white.png](doc/images/K_white.png)
![L_white.png](doc/images/L_white.png)
![M_white.png](doc/images/M_white.png)
![N_white.png](doc/images/N_white.png)
![O_white.png](doc/images/O_white.png)
![P_white.png](doc/images/P_white.png)
![Q_white.png](doc/images/Q_white.png)
![R_white.png](doc/images/R_white.png)
![S_white.png](doc/images/S_white.png)
![T_white.png](doc/images/T_white.png)
![U_white.png](doc/images/U_white.png)
![V_white.png](doc/images/V_white.png)
![W_white.png](doc/images/W_white.png)
![X_white.png](doc/images/X_white.png)
![Y_white.png](doc/images/Y_white.png)
![Z_white.png](doc/images/Z_white.png)