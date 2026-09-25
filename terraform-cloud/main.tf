# Alternativa B — hosting estático en plan gratuito (sin tarjeta).
# El contenido a publicar es la carpeta pieza/. El apply exige token gratuito.
resource "cloudflare_pages_project" "sitio" {
  account_id        = var.account_id
  name              = var.project_name
  production_branch = "main"
}
