variable "cloudflare_api_token" {
  description = "Token de cuenta gratuita (sin tarjeta). Nunca commitear."
  type        = string
  sensitive   = true
  default     = ""
}

variable "account_id" {
  description = "ID de la cuenta gratuita."
  type        = string
  default     = ""
}

variable "project_name" {
  description = "Nombre de la pieza (concreta y nombrada)."
  type        = string
  default     = "sitio-portafolio"
}
