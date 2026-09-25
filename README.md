# Taller: despliegue comparado — pieza `sitio-portafolio`

> Pieza concreta y nombrada: **`sitio-portafolio`** = sitio estático (un `index.html` en `pieza/`). No es el sistema entero, es una sola pieza (categoría "el sitio").
> Ninguna alternativa es una función → la cláusula de arranque en frío no aplica.
> Ninguna alternativa pide tarjeta. El servidor del laboratorio siempre cumple (alternativa A).

## 1. Supuestos

- **S-01 Uso:** ~1 000 visitas/mes, página de ~5 KB. Tráfico normal, sin picos.
- **S-02 Sin tarjeta** en ambas alternativas. Presupuesto $0.
- **S-03 SLO:** el sitio responde 200 en < 1 s el 99 % de las veces.
- **S-04 Despliegues:** ~30 actualizaciones/mes (1 al día).

## 2. Alternativas comparadas

| Criterio | **A. Laboratorio (Docker + nginx)** — elegida | **B. Hosting estático plan gratuito** — descartada |
|---|---|---|
| Terraform | `terraform-lab/` (provider `kreuzwerker/docker`) | `terraform-cloud/` (provider `cloudflare`, recurso `cloudflare_pages_project`) |
| Tarjeta | No | No (plan gratuito sin tarjeta) |
| Cómo sirve la pieza | Contenedor nginx con `pieza/` montada, `restart: unless-stopped` | Proyecto Pages conectado a la carpeta `pieza/` |
| Costo | $0 fijos | $0 hasta ruptura (§5) |
| Reversión | Re-apply de imagen/versión previa (§6) | Redeploy del deployment anterior (§6) |

## 3. Plan reproducible

```bash
# A — laboratorio (aplica real, sin tarjeta)
cd terraform-lab
terraform init; terraform validate; terraform plan -out=tfplan; terraform apply tfplan
curl http://localhost:8080   # debe mostrar "sitio-portafolio OK"

# B — hosting gratuito (plan reproducible; apply con token gratuito)
cd ../terraform-cloud
terraform init; terraform validate; terraform plan
# terraform apply  # exige CLOUDFLARE_API_TOKEN + CLOUDFLARE_ACCOUNT_ID (cuenta gratuita)

# Costos
node ../scripts/estimar-costos.mjs --despliegues-mes 30
```

Evidencia (no valen capturas de tutorial): `terraform validate` de ambos módulos, `curl` al sitio y salida del script de costos.

## 4. Costo + punto de ruptura del gratuito

- **A. Lab:** $0/mes. Ruptura física (RAM/CPU del servidor), no de precio.
- **B. Gratuito:** $0 con ~500 builds (despliegues)/mes incluidos. Con S-04 (30/mes) sobra.
- **Ruptura:** si `despliegues-mes > 500` se acaban los builds incluidos y toca plan pago o espaciar despliegues. El script lo calcula: con 30/mes hay margen de **x16,7 (~500 despliegues/mes)**.

## 5. Reversión (< 5 min)

- **A:** `terraform destroy -auto-approve` y re-`apply` con la versión anterior de `pieza/` (la carpeta se versiona; downtime de segundos).
- **B:** en el dashboard, redeploy del deployment anterior (inmutables, un clic).

## 6. Decisión (resumen del ADR)

Se adopta **A**: $0 sin ruptura de precio, funciona sin internet ni cuentas externas, reversión en segundos y el lab siempre está disponible. **B** queda como plan B si el lab cae. Detalle en `ADR.md`.

## 7. Evidencia de ejecución (salidas reales, 2026-09-25)

Terraform instalado: `Terraform v1.9.8 on windows_amd64` (`terraform version`).

```text
# terraform-lab: init + validate + fmt
Terraform has been successfully initialized!
Success! The configuration is valid.
(fmt -check: limpio, sin diferencias)

# terraform-cloud: init + validate + fmt
Terraform has been successfully initialized!
Success! The configuration is valid.
(fmt -check: limpio, sin diferencias)

# Costos (node scripts/estimar-costos.mjs --despliegues-mes 30)
A Lab (Docker+nginx): $0/mes. Sin ruptura de precio.
B gratuito: despliegues=30/mes builds_incluidos=500 cabe=SI
RUPTURA_FREE: a x16.7 (~500 despliegues/mes). Luego plan pago o espaciar despliegues.
```

> `terraform plan` / `apply` de la alternativa A y el `curl` se ejecutan en el laboratorio (esta máquina no tiene Docker Engine: el `plan` devuelve `Error pinging Docker server`, resultado esperado y documentado). El `plan` de la alternativa B requiere el token de cuenta gratuita.

> Ejecución real en máquina Ubuntu con Docker (provider actualizado a 3.9, socket Linux):
>
> ```text
> Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
> Outputs:
> pieza = "sitio-portafolio"
> reversion = "Restaurar la versión anterior de pieza/ y: terraform apply -auto-approve"
> url = "http://localhost:8080/"
> <!doctype html><html lang="es"><head><meta charset="utf-8">
> <title>sitio-portafolio</title></head>
> <body><h1>sitio-portafolio OK</h1>
> <p>Pieza de ejemplo para el taller de despliegue.</p></body></html>
> ```
