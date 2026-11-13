# ✅ 00 · Antes de la clase (10 minutos)

La clase dura **una hora** y queremos usarla para hackear, no para instalar cosas.
Haz esto **antes** de llegar. Si algo falla, no te preocupes: avísale al instructor al empezar.

## 1. Cuenta de GitHub y Copilot

- [ ] Tener una cuenta en <https://github.com> (gratis).
- [ ] **Recomendado:** verificar tu cuenta como estudiante en
      [GitHub Education](https://github.com/settings/education/benefits). Así tienes **GitHub Copilot gratis**.
      ⏰ La verificación puede tardar varios días: hazlo con tiempo.
- [ ] Si todavía no estás verificado, puedes usar **Copilot Free** (tiene un límite mensual)
      o cualquier otra IA que conozcas (ChatGPT, Gemini, Claude, etc.).

## 2. Tu copia de CafeterIA

- [ ] Entra al repositorio del taller (el instructor te comparte el enlace).
- [ ] Clic en **Use this template → Create a new repository**. Nómbralo, por ejemplo, `cafeteria-ia`.
      Déjalo **público**.
- [ ] En tu nuevo repositorio: **Code → Codespaces → Create codespace on main**.
- [ ] Cuando termine de cargar, en la terminal escribe `python app.py` y abre el puerto **5000**.
      Deberías ver el menú de la cafetería 🍔.
- [ ] Detén la app con `Ctrl + C` y escribe `pytest`. Deben pasar todas las pruebas ✅.
- [ ] Abre el chat de Copilot (ícono de Copilot o `Ctrl + Alt + I`) y pregúntale:
      *«¿Qué hace este proyecto? Resúmelo en 5 líneas.»*

> 💡 **Tip:** el Codespace se apaga solo si no lo usas. El día de la clase vuelve a abrirlo desde
> <https://github.com/codespaces>; tus archivos siguen ahí.

## 3. Activa las herramientas de seguridad de GitHub (2 minutos)

En tu repositorio: **Settings → Advanced Security** (o **Code security**):

- [ ] **Dependabot alerts → Enable**
- [ ] **CodeQL analysis → Set up → Default**

Tardan unos minutos en analizar el código. En la clase vamos a comparar lo que encuentran estas
herramientas con lo que encuentra la IA… y con lo que encuentras **tú**.

## 4. Arma tu equipo

Equipos de **3 o 4 personas**. Piensen en un nombre épico (ej.: *Los Parches*, *Inyección de Tinto*,
*404 Hambre Not Found*). En la clase se reparten estos roles:

| Rol | Qué hace |
|---|---|
| 🔍 **Cazador/a** | Revisa el código con la IA y propone posibles vulnerabilidades |
| 🧪 **Verificador/a** | Demuestra cada hallazgo en la app (sin prueba no hay puntos) |
| 🛠️ **Parchador/a** | Corrige el código en el repositorio oficial del equipo y corre `pytest` |
| 📝 **Reportero/a** | Llena las tarjetas de hallazgo y negocia con el juez 😎 |

En equipos de 3, el Reportero también verifica.

## ¿No puedes usar Codespaces?

Mira la **Opción B** del [README](../README.md) para correrlo en tu computador con Python 3.11, 3.12 o 3.13.
