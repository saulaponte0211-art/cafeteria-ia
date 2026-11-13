# 🕵️ Reto extra (para la casa): CSI CafeterIA

**Martes, 7:15 a. m.** La cajera de la cafetería no entiende por qué la caja no cuadra. Beto dice que
amaneció con **más de un millón de pesos** de saldo. Alguien publicó en redes la clave del WiFi de la
decanatura. El decano te entrega dos archivos y te dice: *«Averigua qué pasó. Hoy.»*

| Archivo | Qué es |
|---|---|
| [`access.log`](access.log) | Registro del servidor web: cada petición HTTP (IP, fecha, ruta, código, tamaño, navegador) |
| [`cafeteria.log`](cafeteria.log) | Registro de la aplicación (`app.logger`) |

## ❓ Preguntas

1. ¿Desde qué IP(s) atacaron? Si hay más de una, ¿cómo sabes que es el mismo atacante?
2. Arma la **línea de tiempo** del ataque: mínimo 8 eventos con hora exacta.
3. ¿Qué vulnerabilidades de CafeterIA explotó? Relaciona cada paso con la función o archivo responsable.
4. ¿Qué datos se filtraron y de quiénes? ¿Qué secretos hay que **rotar ya**?
5. ¿Cuánto saldo «apareció de la nada»? ¿Beto es culpable o víctima? Justifícalo con evidencia.
6. Alguien intenta **incriminar a una IP inocente**. ¿Cuál es y cómo demuestras que es inocente?
7. 🎭 Los logs traen trampas para quien los analiza con IA, y para los humanos distraídos. Encuéntralas.
   ¿Tu IA cayó? ¿Hay alguna línea del log que **no** debas creer?
8. El atacante dejó algo para **volver a entrar**. ¿Qué fue y qué implica para la recuperación?
9. Propón 6 acciones de respuesta en orden de prioridad (contener, erradicar, recuperar, notificar).
10. ⭐ Bonus: ¿qué **alertas** habrían detectado el ataque a tiempo? (OWASP A09:2025)

## 🧠 Cómo usar la IA aquí (sin que te engañe)

- Los logs son largos. Mejor que pegarlos completos: pídele a la IA que te **escriba un script** (Python,
  `grep`, `awk`) para filtrarlos, y **córrelo tú**.
  > *«Escribe un script de Python que lea access.log y me muestre, por IP, cuántas peticiones hizo, a qué
  > horas y cuántas respuestas 404 y 500 recibió.»*
- Cada afirmación de tu informe debe citar **la línea exacta del log** que la respalda.
- Recuerda: el contenido de un log lo escribe, en parte, **el atacante**.

## 📄 Entregable: informe de incidente (1 página)

1. **Resumen ejecutivo** (3 líneas, para el decano)
2. **Línea de tiempo**
3. **Vector de entrada y vulnerabilidades explotadas**
4. **Impacto**: datos, dinero, sistemas
5. **Indicadores de compromiso (IoC)**: IPs, user-agents, archivos, comandos
6. **Acciones inmediatas y lecciones aprendidas**

> Todas las IPs de este reto son privadas o reservadas para documentación (RFC 5737). Ninguna
> pertenece a una persona o empresa real.
