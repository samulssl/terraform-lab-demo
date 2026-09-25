# ADR — Despliegue de `sitio-portafolio`: laboratorio frente a hosting gratuito

- **Estado:** aceptado — 2026-09-25
- **Pieza:** `sitio-portafolio` (sitio estático, un `index.html`). Una sola pieza, no el sistema.
- **Condición:** uso normal ~1 000 visitas/mes, sin tarjeta, $0.

## Alternativas

- **A. Laboratorio (Docker + nginx):** contenedor siempre vivo con `pieza/` montada. Sin tarjeta, $0.
- **B. Hosting estático gratuito:** proyecto Pages con `pieza/`. Sin tarjeta, $0 hasta 500 builds/mes.

## Decisión: A

1. $0 sin ruptura de precio ni cuentas externas; el lab siempre está disponible.
2. Reversión en segundos (restaurar `pieza/` + `apply`).
3. B cabe en el gratuito (30 vs 500 builds) pero depende de internet y de un tercero; queda como plan B y su ruptura está calculada en `scripts/estimar-costos.mjs`.

## Consecuencias

- Desplegar A con Terraform; evidencia: `validate` + `curl` + salida del script (no capturas de tutorial).
- Si el lab cae, aplicar B con el token gratuito.
