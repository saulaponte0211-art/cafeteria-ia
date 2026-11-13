# 🤖 02 · Guía: la IA como compañera de seguridad

Piensa en la IA como un **pasante brillante**: lee código a una velocidad absurda, nunca se cansa y
sabe de todo un poco… pero a veces se equivoca **con total seguridad**, no conoce tu contexto y
puede ser manipulada. Tú eres quien firma el reporte.

## 🧱 Anatomía de un buen prompt de seguridad

| Ingrediente | Ejemplo |
|---|---|
| **Rol** | «Actúa como auditor de seguridad de aplicaciones web.» |
| **Contexto** | «Es una app Flask con SQLite; los usuarios son estudiantes.» |
| **Tarea concreta** | «Revisa la función `pedir` de `app.py`.» (mejor que «revisa todo») |
| **Formato** | «Dame una tabla: línea, problema, categoría OWASP, severidad.» |
| **Evidencia** | «Para cada problema, dime cómo lo demostraría en la app.» |
| **Honestidad** | «Si no estás seguro de algo, dilo. No inventes.» |

❌ *«¿Este código es seguro?»* → respuesta vaga.

✅ *«Actúa como auditor de seguridad. En `app.py`, revisa SOLO las funciones `login` y `registro`.
Para cada problema dame la línea, el tipo (OWASP Top 10:2025), un ejemplo concreto de ataque y cómo
corregirlo. Si algo parece peligroso pero no lo es, explícame por qué.»*

## 🗺️ Prompts por fase

**1. Entender** (antes de atacar hay que entender)

- «Explícame qué hace `app.py` como si fuera un mapa: rutas, qué datos recibe cada una y quién puede usarla.»
- «¿Qué datos del usuario llegan al servidor y por dónde? Haz una lista de todas las entradas.»

**2. Cazar**

- «¿Dónde se mezclan datos del usuario con SQL, HTML, rutas de archivos, plantillas o código?»
- «¿Qué rutas no verifican quién es el usuario o si tiene permiso?»
- «¿Qué decisiones de seguridad se toman en el navegador y no en el servidor?»
- «Revisa `config.py` y `requirements.txt`. ¿Qué malas prácticas ves?»

**3. Demostrar**

- «Dame un ejemplo de entrada que demuestre esta vulnerabilidad **en mi propia app local**.»
- «¿Cómo envío este formulario con `curl` cambiando el campo `cantidad`?»

**4. Corregir**

- «Corrige esta función usando la práctica recomendada, no una lista negra. Explica por qué funciona.»
- «¿Tu corrección rompe algún uso normal de la app?»

**5. Atacar tu propia corrección** (aquí está la magia ✨)

- «Actúa ahora como atacante. ¿Cómo evadirías esta corrección? Dame 3 intentos.»
- «¿Qué casos borde no cubre? (mayúsculas, codificación, rutas de Windows, números negativos…)»

## 🚩 Señales de alerta: cuándo NO creerle a la IA a la primera

1. **Te recomienda un paquete que no conoces.** Búscalo en <https://pypi.org>: ¿existe? ¿Quién lo
   mantiene? ¿Cuántas descargas tiene? ¿Desde cuándo existe?
   > 📰 **Caso real (*slopsquatting*):** un estudio presentado en USENIX Security 2025 encontró que
   > cerca del **20 %** de los paquetes recomendados por modelos de IA para generar código
   > **no existían**. Un investigador registró `huggingface-cli`, un nombre que las IA inventaban
   > seguido. El paquete estaba vacío y recibió **más de 15.000 descargas** en tres meses. Un atacante
   > habría podido meter cualquier cosa ahí.
2. **Dice «es seguro» sin explicar por qué.** Pídele la justificación y el ataque que descartó.
3. **Corrige con listas negras o filtros:** «quita `<script>`», «borra `--`», «reemplaza `../`». Casi
   siempre hay forma de saltarlos.
4. **Cita una CVE, una versión o una opción de configuración.** Verifícala en
   <https://osv.dev> o en <https://github.com/advisories>.
5. **Cambia de opinión después de leer un archivo.** El código y los documentos pueden traer
   instrucciones escondidas para la IA (*prompt injection*). Si tu IA de repente dice que algo
   «ya fue auditado», desconfía.
6. **Su corrección toca muchas cosas que no pediste.** Revisa línea por línea antes de aceptar.
7. **Marca como crítico algo que depende del contexto.** Por ejemplo, MD5 es terrible para contraseñas
   pero no es un problema para calcular la huella de un archivo de caché. **El contexto importa.**

## ✅ Antes de reportar o hacer commit: «Confía, pero verifica»

- [ ] ¿Lo **reproduje** yo mismo en la app?
- [ ] ¿Entiendo **por qué** es vulnerable (y no solo que la IA lo dijo)?
- [ ] ¿La corrección ataca la **causa** y no solo el ejemplo que probé?
- [ ] ¿Volví a intentar el ataque **después** de corregir?
- [ ] ¿`pytest` sigue en verde?

## 🛠️ La IA no reemplaza a las herramientas: las complementa

| Herramienta | Qué encuentra | Cómo usarla |
|---|---|---|
| `pip-audit` | Dependencias con vulnerabilidades conocidas (CVE) | `pip-audit -r requirements.txt` |
| Dependabot | Lo mismo, directo en GitHub, y propone actualizaciones | Pestaña **Security** de tu repo |
| CodeQL | Patrones de código inseguro (análisis estático) | Pestaña **Security → Code scanning** |
| Secret scanning | Claves y tokens subidos por error | Pestaña **Security** de tu repo |
| `git log -p` | Lo que alguna vez estuvo en el repo… aunque se haya «borrado» | Terminal |

💬 **Pregunta para tu equipo:** ¿qué encontró la IA que las herramientas no? ¿Y al revés?

## 🔐 Una nota de privacidad

En este taller no hay secretos reales. En un trabajo de verdad, **nunca pegues contraseñas, claves ni
datos de clientes en un chat de IA**, y sigue la política de tu empresa sobre qué herramientas de IA
están aprobadas.
