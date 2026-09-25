# Plan B: demo en vivo sin instalar nada (Play with Docker)

Play with Docker (`labs.play-with-docker.com`) es un Docker real en el navegador: gratis, sin instalar nada. Solo pide entrar con una cuenta gratuita de Docker Hub. La sesión dura unas 4 horas: alcanza para el demo.

## Secuencia exacta (copiar y pegar en orden)

**1. Entra y crea la máquina:** abre `labs.play-with-docker.com` → Start → **Add New Instance**. Te da una terminal Linux con Docker.

**2. Clona tu repo:**
```bash
git clone https://github.com/samulssl/terraform-lab-demo.git
cd terraform-lab-demo/terraform-lab
```

**3. Instala Terraform ahí dentro (la máquina viene vacía):**
```bash
curl -sSL -o tf.zip https://releases.hashicorp.com/terraform/1.9.8/terraform_1.9.8_linux_amd64.zip
unzip -o tf.zip && chmod +x terraform && export PATH=$PWD:$PATH
terraform version
```

**4. Aplica la alternativa A (OJO: allá es Linux, se cambia el docker_host):**
```bash
terraform init
terraform validate
terraform plan -var='docker_host=unix:///var/run/docker.sock'
terraform apply -var='docker_host=unix:///var/run/docker.sock'
```
Escribe `yes` cuando pregunte. Debe terminar en `Apply complete!`.

**5. Comprueba el sitio:**
```bash
curl http://localhost:8080
docker ps
```
El `curl` debe traer el HTML con `sitio-portafolio OK`. Para verlo en el navegador: botón **OPEN PORT** (arriba de la terminal) → escribe `8080` → abre la URL pública que genera.

## Alternativa sin Terraform (misma página, un comando)

Si solo quieres mostrar la página corriendo, sin Terraform:
```bash
cd ..
docker compose up -d --build
curl http://localhost:8080
```
Usa el `Dockerfile` + `docker-compose.yml` del repo. Para tumbarlo: `docker compose down`.

## Notas para la sustentación

- Esto demuestra la alternativa A funcionando de verdad, sin instalar nada en tu PC.
- La sesión se borra sola a las ~4 horas: es solo para el demo, no para guardar nada.
- La evidencia del taller sigue siendo la del laboratorio; esto es el plan B en vivo.
