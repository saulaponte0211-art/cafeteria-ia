# 🏆 01 · La misión: Bug Bounty en CafeterIA

> **Lunes, 7:00 a. m.** CafeterIA sale a producción en unas horas. El decano te mira y dice:
> *«Encuéntrenme todo lo que esté mal. Y arréglenlo. Ah, y no rompan nada, que la gente quiere su tinto.»*

## ⏱️ Las fases (1 hora)

| Tiempo | Fase | Qué hacen |
|---|---|---|
| 0:00 | 🎬 Historia y reglas | Escuchar (y prepararse para competir) |
| 0:05 | 🤖 Quiz: «¿La IA tiene razón?» | Calentar el pensamiento crítico |
| 0:10 | 👥 Equipos y roles | App corriendo, Copilot abierto, roles asignados |
| 0:15 | 🔎 **Fase 1: Cacería** (20 min) | Encontrar y **demostrar** vulnerabilidades. Reportar al juez |
| 0:35 | 🛠️ **Fase 2: Parches** (13 min) | Corregir lo más grave. `pytest` debe seguir en verde |
| 0:48 | ⚖️ **Fase 3: ¡Que entre el Árbitro!** | El instructor dice la clave y el Árbitro ataca su app |
| 0:53 | 🏅 Premiación y cierre | Lecciones aprendidas y reto para la casa |

## 🎯 Puntos

| Severidad | Encontrar (con evidencia) | Corregir (según el Árbitro) |
|---|---|---|
| 🔴 Crítica | 200 | 200 |
| 🟠 Alta | 150 | 150 |
| 🟡 Media | 100 | 100 |
| 🟢 Baja | 50 | 50 |

El juez decide la severidad final según el impacto real.

| Bonus y penalizaciones | Puntos |
|---|---|
| 🩸 **Primera sangre**: primer equipo en reportar una vulnerabilidad | +50 |
| 🤖 **La IA se equivocó**: demuestren con evidencia un error de la IA (máx. 2 por equipo) | +100 |
| ⛓️ **Cadena de ataque**: combinen 2 o más vulnerabilidades para lograr algo peor | +100 |
| ⭐ **Bonus del Árbitro** | lo que diga el Árbitro |
| 🙈 **Reporte falso**: reportar algo que no es vulnerable (¡cuidado con los señuelos 🪤!) | −50 |

**¿Qué cuenta como «la IA se equivocó»?**

- 🪤 **Falso positivo:** dijo que algo era vulnerable y no lo es.
- 🙈 **Falso negativo:** dijo que algo era seguro y no lo es.
- 🩹 **Parche incompleto:** su corrección se puede saltar (y lo demostraron).
- 👻 **Alucinación:** inventó un paquete, una función, una CVE o una opción que no existe.
- 🎭 **Manipulación:** el código la convenció de ignorar algo.

## 🔎 Fase 1: Cacería (20 min)

1. **Exploren la app** como usuarios normales: pidan algo, escriban una reseña, usen la calculadora…
2. **Revisen el código con la IA.** Sean específicos (lean la [guía de IA](02-guia-ia-para-seguridad.md)):
   > *«Actúa como auditor de seguridad. Revisa la función `login` de `app.py`. Para cada problema dime
   > la línea, el tipo de vulnerabilidad (OWASP Top 10) y cómo lo demostraría en la app.»*
3. **Demuestren cada hallazgo en la app.** Sin evidencia no hay puntos. La evidencia puede ser una
   captura, un comando `curl` o una petición que hace algo que no debería.
4. **Revisen también lo que no es código:** dependencias (`pip-audit -r requirements.txt`, alertas de
   Dependabot), configuración, plantillas HTML y el **historial de git** del repositorio original del taller.
5. **Reporten** cada hallazgo con una tarjeta (abajo) y muéstrenle la evidencia al juez.

### 🧭 Pistas para empezar (por si se bloquean)

- ¿Qué pasa si escribes una comilla `'` en los formularios?
- ¿Qué tal si cambias un número en la URL?
- ¿Qué tanto confía el servidor en lo que le manda el navegador? (Herramientas del desarrollador → `F12`)
- ¿Qué archivos puede descargar la sección de descargas?
- ¿Qué pasa si visitas una página que no existe… con un nombre *muy* raro?
- El decano tiene una contraseña que nadie sabe. ¿Hay otras formas de ser el decano?
- Un desarrollador borró una clave secreta en un commit. ¿La borró de verdad?

## 🛠️ Fase 2: Parches (13 min)

1. Elijan las vulnerabilidades **más graves**: el tiempo no alcanza para todo, así que prioricen como
   en la vida real.
2. Pídanle a la IA una corrección **y cuestiónenla**:
   > *«¿Esta corrección se puede saltar? Dame 3 formas en que un atacante intentaría evadirla.»*
3. Después de cada cambio:
   - Vuelvan a intentar el ataque: ¿ya no funciona?
   - Corran `pytest`: ¿la app sigue funcionando?
4. ⚠️ **Una corrección que rompe la app no cuenta.** El Árbitro la marca como 🚫.
5. Hagan *commit* de sus cambios (`git add . && git commit -m "Corrige ..."`).

> 📌 **No cambien** los nombres de las rutas, el nombre de la función `create_app()`, los campos de
> los formularios ni las cuentas de ejemplo. El Árbitro y las pruebas los necesitan.

## ⚖️ Fase 3: ¡Que entre el Árbitro!

Cuando el instructor diga la clave, el Parchador corre en el repositorio oficial del equipo:

```bash
python desbloquear_arbitro.py --equipo "Nombre del equipo"
```

El Árbitro ataca su versión de CafeterIA y muestra qué corrigieron ✅, qué sigue vulnerable ❌ y qué
rompieron 🚫. Tómenle una captura de pantalla y muéstrensela al juez.

## 📝 Tarjeta de hallazgo

Llénenla en papel o como *issue* en su repositorio (**Issues → New issue → 🐛 Reporte de hallazgo**).

```text
Equipo: ______________________        Hallazgo #: ____
¿Qué encontramos? (archivo y línea): ______________________________
Tipo (OWASP Top 10:2025): __________   Severidad propuesta: 🔴 🟠 🟡 🟢
¿Cómo lo demostramos? (pasos o evidencia): ______________________
Impacto (¿qué podría hacer un atacante?): ______________________
¿Cómo lo corregiríamos?: ______________________________________
¿Qué dijo la IA?  ✅ acertó   ❌ se equivocó   🤔 a medias
Prompt que usamos: ____________________________________________
```

## 📚 Referencia rápida: OWASP Top 10:2025

| ID | Categoría |
|---|---|
| A01 | Control de acceso roto (*Broken Access Control*) |
| A02 | Configuración de seguridad incorrecta (*Security Misconfiguration*) |
| A03 | Fallas en la cadena de suministro de software (*Software Supply Chain Failures*) |
| A04 | Fallas criptográficas (*Cryptographic Failures*) |
| A05 | Inyección (*Injection*) |
| A06 | Diseño inseguro (*Insecure Design*) |
| A07 | Fallas de autenticación (*Authentication Failures*) |
| A08 | Fallas de integridad de software o datos (*Software or Data Integrity Failures*) |
| A09 | Fallas de registro y alertas de seguridad (*Security Logging & Alerting Failures*) |
| A10 | Mal manejo de condiciones excepcionales (*Mishandling of Exceptional Conditions*) |

Además, para IA: [OWASP Top 10 para aplicaciones con LLM](https://genai.owasp.org/llm-top-10/)
(por ejemplo, **LLM01: Prompt Injection**).
