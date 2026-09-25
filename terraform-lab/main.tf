# Alternativa A — laboratorio: nginx sirve la carpeta pieza/ (solo lectura).
resource "docker_image" "web" {
  name         = "nginx:alpine"
  keep_locally = true
}

resource "docker_container" "web" {
  name  = var.project_name
  image = docker_image.web.image_id

  ports {
    internal = 80
    external = var.host_port
  }

  volumes {
    host_path      = abspath("${path.module}/../pieza")
    container_path = "/usr/share/nginx/html"
    read_only      = true
  }

  memory  = 256
  restart = "unless-stopped"
}
