# 🍔🤖 CafeterIA — Taller «Hackea con IA»

> [!WARNING]
> **Esta aplicación es INTENCIONALMENTE VULNERABLE.** Fue creada para un taller universitario
> de seguridad. Úsala solo en tu equipo o en tu GitHub Codespace. **Nunca** la publiques en
> internet, no cambies el puerto a «Public» y no reutilices este código en proyectos reales.

## 📖 La historia

La cafetería de la universidad lanzó **CafeterIA**, una app para pedir empanadas, tintos y
bandejas paisas sin hacer fila. Un estudiante la construyó **100 % con IA en un fin de semana**
(*vibe coding*), sin revisar una sola línea. Funciona, se ve bonita... y sale a producción el lunes.

El decano escuchó rumores de que «algo huele raro en la cocina» 🧐 y los contrató a ustedes como
**equipo de seguridad**. Su misión:

1. 🔎 **Encontrar** las vulnerabilidades, con la IA como compañera de equipo.
2. 🧪 **Demostrarlas**: sin evidencia no hay puntos.
3. 🛠️ **Corregirlas** sin romper la app.
4. ⚖️ Sobrevivir al **Árbitro**, un programa que atacará su versión al final.

Hay **más de 20 vulnerabilidades** escondidas: errores de código, paquetes inseguros y malas
prácticas. También hay **señuelos** 🪤: código que *parece* peligroso pero no lo es. La IA va a
caer en algunos. ¿Ustedes también?

> **Regla de oro del taller: «Confía, pero verifica.»** La IA es una compañera brillante pero a veces
> se equivoca con total seguridad. Ustedes son los responsables de lo que reportan y de lo que corrigen.

## 🚀 Cómo empezar

### Opción A: GitHub Codespaces (recomendada, no instalas nada)

1. Arriba a la derecha, haz clic en **Use this template → Create a new repository**. Déjalo **público**
   (así tendrás las herramientas de seguridad de GitHub gratis).
2. En tu nuevo repositorio: **Code → Codespaces → Create codespace on main**.
3. Espera a que termine de instalar (1–3 minutos) y en la terminal escribe:

   ```bash
   python app.py
   ```

4. VS Code te ofrecerá abrir el puerto **5000** en el navegador. ¡Listo! 🎉

### Opción B: en tu computador

Necesitas **Python 3.11, 3.12 o 3.13** y Git.

```bash
git clone https://github.com/<tu-usuario>/<tu-repo>.git
cd <tu-repo>
python -m venv .venv
# Windows: .venv\Scripts\activate      macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
python app.py
```

Abre <http://127.0.0.1:5000>.

### Cuentas de prueba

| Usuario | Correo | Contraseña |
|---|---|---|
| Estudiante | `ana@cafeteria.edu` | `ana12345` |
| Decano (admin) | `decano@cafeteria.edu` | 🤫 Nadie la sabe. ¿Puedes entrar como él? |

También puedes crear tu propia cuenta (¡te regalan $20.000!).

### Comandos útiles

| Comando | Para qué sirve |
|---|---|
| `python app.py` | Inicia la app en <http://127.0.0.1:5000> |
| `python app.py --reiniciar` | Borra la base de datos y vuelve a los datos de ejemplo |
| `pytest` | Pruebas funcionales: verifican que tus correcciones **no rompan** la app |
| `pip-audit -r requirements.txt` | Busca vulnerabilidades conocidas en las dependencias (ya viene en Codespaces; en tu PC usa `pipx run pip-audit -r requirements.txt`) |
| `python desbloquear_arbitro.py` | ⚖️ Solo cuando el instructor diga la clave |

## 🏆 El juego

Lee la misión completa en **[ejercicios/01-mision-bug-bounty.md](ejercicios/01-mision-bug-bounty.md)**.

| Severidad | Encontrar (con evidencia) | Corregir (según el Árbitro) |
|---|---|---|
| 🔴 Crítica | 200 | 200 |
| 🟠 Alta | 150 | 150 |
| 🟡 Media | 100 | 100 |
| 🟢 Baja | 50 | 50 |

Hay bonus por **primera sangre** 🩸, por **cazar errores de la IA** 🤖 y por **encadenar ataques** ⛓️, y
penalización por reportar cosas falsas sin verificar 🙈.

## 📚 Material del taller

| Archivo | Contenido |
|---|---|
| [INSTRUCCIONES-ESTUDIANTES.pdf](ejercicios/INSTRUCCIONES-ESTUDIANTES.pdf) | 📄 Instrucciones de la clase en PDF (pasos, roles, puntos, IA gratis y tarjetas de hallazgo) |
| [00-antes-de-clase.md](ejercicios/00-antes-de-clase.md) | Preparación (10 min, **hazla antes de la clase**) |
| [01-mision-bug-bounty.md](ejercicios/01-mision-bug-bounty.md) | La misión, los roles, las fases y los puntos |
| [02-guia-ia-para-seguridad.md](ejercicios/02-guia-ia-para-seguridad.md) | Cómo usar la IA como profesional de seguridad (y cómo no) |
| [reto-extra-csi/](ejercicios/reto-extra-csi/) | 🕵️ Reto para la casa: investigar un ataque real a CafeterIA |

## ⚖️ Ética (léelo, en serio)

- Solo ataca **tu propia copia** de CafeterIA. Atacar sistemas sin autorización es un **delito**
  en la mayoría de países, aunque «solo estés probando».
- Lo que aprendes aquí es para **defender**. Los profesionales de seguridad trabajan con permiso
  explícito y alcance definido. Si encuentras una vulnerabilidad en un sistema real, repórtala de
  forma responsable al dueño (muchas empresas tienen programas de *bug bounty*).

## 📄 Licencia

[MIT](LICENSE). Hecho con ☕ para que más ingenieros aprendan a construir software seguro, con IA y con criterio.
