variable "docker_host" {
  description = "Socket del Docker Engine del laboratorio."
  type        = string
  default     = "npipe:////./pipe/docker_engine"
}

variable "project_name" {
  description = "Nombre de la pieza (concreta y nombrada)."
  type        = string
  default     = "sitio-portafolio"
}

variable "host_port" {
  description = "Puerto del host."
  type        = number
  default     = 8080
}
