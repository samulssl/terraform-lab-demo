# Cómo funciona el taller (guía completa en palabras simples)

Este documento explica tres cosas: **qué pidió el profesor**, **qué se hizo para cumplirlo** y **cómo funciona Terraform** en este proyecto.

---

## 1. Qué pidió el profesor vs qué se hizo

| Lo que pidió el profesor | Qué se hizo | Dónde está |
|---|---|---|
| Elegir **una pieza concreta y nombrada**, no el sistema entero | Pieza `sitio-portafolio`: un sitio estático de un solo `index.html` | `pieza/index.html` |
| Comparar **dos alternativas** de despliegue para esa pieza | A: laboratorio con Docker + nginx. B: hosting estático en plan gratuito | `terraform-lab/` y `terraform-cloud/` |
| Al menos una alternativa **sin tarjeta** (el lab siempre cumple) | Las dos son sin tarjeta | `README.md` §1–§2 |
| Si una alternativa es **función**, medir su arranque en frío vs el p95 | Ninguna es función: se declara que no aplica | `README.md` §2 |
| Incluir los **supuestos** | S-01 a S-04 (visitas, $0, SLO, despliegues/mes) | `README.md` §1 |
| **Prototipo o plan reproducible** con Terraform | Dos módulos Terraform que pasan `init` + `validate` | `terraform-lab/`, `terraform-cloud/` |
| **Costo** con el punto donde se rompe el plan gratuito | Script que calcula la ruptura: x16,7 (~500 despliegues/mes) | `scripts/estimar-costos.mjs`, `README.md` §4 |
| Procedimiento de **reversión** | Pasos de vuelta atrás para A y B (< 5 min) | `README.md` §5 |
| Un **ADR** que justifique la elección | Decisión a favor del laboratorio, con 3 razones y consecuencias | `ADR.md` |
| **Evidencia real**, no capturas de tutoriales | Salidas de `validate`, `plan`, `curl` y el script (se generan en el lab) | Se pegan en el `README.md` §3 |

---

## 2. Cómo funciona Terraform (la idea en 5 líneas)

Terraform es una herramienta que **crea cosas siguiendo un archivo de instrucciones** (los `.tf`). Tú describes lo que quieres ("un contenedor nginx con esta carpeta") y Terraform lo hace realidad. El ciclo siempre es:

1. `terraform init` → **prepara**: descarga el *provider* (el plugin que sabe hablar con Docker, con la nube, etc.). Solo la primera vez.
2. `terraform validate` → **revisa**: verifica que el código esté bien escrito. No toca nada.
3. `terraform plan` → **simula**: muestra lo que VA a crear/cambiar/borrar. No toca nada. Es la cotización.
4. `terraform apply` → **ejecuta**: hace los cambios de verdad. Pide confirmar con `yes`.
5. `terraform destroy` → **deshace**: borra todo lo que creó. La limpieza.

Tres ideas clave para entenderlo:

- **Provider**: el conector con cada plataforma. Aquí usamos `kreuzwerker/docker` (habla con Docker) y `cloudflare` (habla con el hosting). Cada módulo declara el suyo en `versions.tf`.
- **Resource**: cada cosa que Terraform crea y controla. Ejemplo: `docker_container.web` (el contenedor del sitio). Están en `main.tf`.
- **State**: el archivo `terraform.tfstate` donde Terraform anota lo que creó. Por eso `terraform state list` te dice qué está "a cargo" de Terraform y `terraform plan` sin cambios dice `No changes`: el código y la realidad coinciden.

---

## 3. Cómo funciona cada parte del proyecto

```
Taller-Despliegue/
├── pieza/index.html          → LA PIEZA: lo que se despliega (el sitio).
├── terraform-lab/            → ALTERNATIVA A: docker_image + docker_container
│                               con nginx sirviendo pieza/ (solo lectura).
├── terraform-cloud/          → ALTERNATIVA B: recurso cloudflare_pages_project
│                               (proyecto de hosting gratuito para pieza/).
├── scripts/estimar-costos.mjs→ Calcula con tus números cuándo se acaba lo
│                               gratuito (despliegues/mes vs 500 incluidos).
├── README.md                 → El documento del taller (supuestos, tabla
│                               comparativa, costos, reversión, decisión).
└── ADR.md                    → La justificación formal de por qué ganó A.
```

El flujo completo, en orden: lees el `README.md` (qué y por qué) → corres `init/validate/plan/apply` en `terraform-lab` (el cómo, en el laboratorio con Docker) → compruebas con `curl http://localhost:8080` → corres el script de costos → pegas esas salidas como evidencia → si algo sale mal, aplicas la reversión del `README.md` §5.

---

## 4. Qué falta por hacer (checklist final)

- [ ] Correr `init`, `validate`, `plan`, `apply` en `terraform-lab` (en el laboratorio, con Docker).
- [ ] Correr `curl http://localhost:8080` y guardar la salida.
- [ ] Correr `node scripts/estimar-costos.mjs --despliegues-mes 30` y guardar la salida.
- [ ] Pegar esas tres salidas en el `README.md` como sección "Evidencia".
- [ ] Subir todo al repo (`git add .`, `commit`, `push`).
- [ ] Ensayar la frase de sustentación: pieza, alternativas, costos con ruptura, elección y reversión.
