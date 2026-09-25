# Genera Entrega-Taller-Despliegue.pdf (documento formal del taller).
# Uso: python generar-pdf.py
from fpdf import FPDF

AZUL = (13, 71, 161)
GRIS = (245, 245, 245)
BORDE = (200, 200, 200)

class Doc(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Arial", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, "Taller de despliegue con Terraform — pieza sitio-portafolio", align="R")
        self.ln(12)

    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-15)
        self.set_font("Arial", "", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f"Página {self.page_no() - 1}", align="C")

    def titulo(self, txt):
        self.set_font("Arial", "B", 15)
        self.set_text_color(*AZUL)
        self.multi_cell(0, 9, txt)
        self.set_draw_color(*AZUL)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(4)

    def cuerpo(self, txt):
        self.set_font("Arial", "", 11)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 6.5, txt)
        self.ln(2)

    def bullets(self, items):
        self.set_font("Arial", "", 11)
        self.set_text_color(30, 30, 30)
        for it in items:
            x = self.get_x()
            self.cell(6, 6.5, chr(8226))
            self.multi_cell(0, 6.5, it)
            self.set_x(x)
        self.ln(2)

    def tabla(self, head, rows):
        self.set_font("Arial", "B", 10)
        self.set_fill_color(*AZUL)
        self.set_text_color(255, 255, 255)
        w = (self.w - self.l_margin - self.r_margin) / len(head)
        for h in head:
            self.cell(w, 8, h, border=1, fill=True)
        self.ln()
        self.set_font("Arial", "", 10)
        self.set_text_color(30, 30, 30)
        fill = False
        for r in rows:
            if fill:
                self.set_fill_color(*GRIS)
            maxlines = 1
            celdas = []
            for c in r:
                n = max(1, int(len(c) / 34) + 1)
                maxlines = max(maxlines, n)
                celdas.append(c)
            h = 7 * maxlines
            y0 = self.get_y()
            if y0 + h > self.h - 20:
                self.add_page()
                y0 = self.get_y()
            x0 = self.get_x()
            for i, c in enumerate(celdas):
                self.set_xy(x0 + i * w, y0)
                self.rect(x0 + i * w, y0, w, h)
                self.set_xy(x0 + i * w + 1, y0 + 1)
                self.multi_cell(w - 2, 7, c)
            self.set_xy(x0, y0 + h)
            fill = not fill
        self.ln(3)

    def codigo(self, txt):
        self.set_fill_color(30, 30, 30)
        self.set_text_color(240, 240, 240)
        self.set_font("Courier", "", 9.5)
        self.multi_cell(0, 6, txt, fill=True)
        self.ln(3)


pdf = Doc()
pdf.set_auto_page_break(True, 20)
pdf.add_font("Arial", "", r"C:\Windows\Fonts\arial.ttf")
pdf.add_font("Arial", "B", r"C:\Windows\Fonts\arialbd.ttf")
pdf.add_font("Arial", "I", r"C:\Windows\Fonts\ariali.ttf")

# Portada
pdf.add_page()
pdf.ln(45)
pdf.set_font("Arial", "B", 26)
pdf.set_text_color(*AZUL)
pdf.multi_cell(0, 12, "Taller de despliegue\ncon Terraform", align="C")
pdf.ln(4)
pdf.set_font("Arial", "", 14)
pdf.set_text_color(60, 60, 60)
pdf.multi_cell(0, 8, "Pieza sitio-portafolio: laboratorio (Docker)\nfrente a hosting estático gratuito", align="C")
pdf.ln(10)
pdf.set_font("Arial", "I", 11)
pdf.set_text_color(120, 120, 120)
pdf.multi_cell(0, 7, "Entrega calificada — supuestos, prototipo reproducible,\ncostos con punto de ruptura, reversión y ADR", align="C")

# 1
pdf.add_page()
pdf.titulo("1. Pieza elegida y condición operativa")
pdf.cuerpo("La pieza concreta y nombrada es sitio-portafolio, de la categoría «el sitio»: un sitio estático compuesto por un único index.html. Se analiza una sola pieza y no el sistema entero. Ninguna de las dos alternativas es una función serverless, por lo que la cláusula de contraste entre arranque en frío y p95 no resulta aplicable, hecho que queda declarado expresamente.")
pdf.bullets([
    "S-01 Uso: unas 1 000 visitas al mes sobre una página de ~5 KB, tráfico normal sin picos.",
    "S-02 Economía: sin tarjeta en ambas alternativas y presupuesto de cero.",
    "S-03 SLO de la pieza: respuesta 200 en menos de 1 segundo el 99 % de las veces.",
    "S-04 Cambios: unas 30 actualizaciones al mes (una diaria).",
])

# 2
pdf.titulo("2. Alternativas comparadas")
pdf.tabla(["Criterio", "A. Laboratorio (elegida)", "B. Hosting gratuito (descartada)"],
    [["Recurso Terraform", "terraform-lab (provider Docker)", "terraform-cloud (provider Cloudflare)"],
     ["Tarjeta", "No, siempre cumple", "No, plan gratuito"],
     ["Despliegue", "Contenedor nginx con pieza/ montada", "Proyecto Pages con pieza/"],
     ["Costo", "$0 fijos", "$0 hasta ruptura"],
     ["Reversión", "Re-apply (< 5 min)", "Redeploy anterior"]])

# 3
pdf.titulo("3. Plan reproducible")
pdf.cuerpo("Ningún paso pide tarjeta. La alternativa A se aplica en el laboratorio (con Docker); la B requiere un token de cuenta gratuita solo para el apply; ambos módulos pasan terraform init y terraform validate en cualquier máquina.")
pdf.codigo("cd terraform-lab\nterraform init\nterraform validate\nterraform plan -out=tfplan\nterraform apply tfplan\ncurl http://localhost:8080\nnode ../scripts/estimar-costos.mjs --despliegues-mes 30")

# 4
pdf.titulo("4. Costos y punto de ruptura")
pdf.cuerpo("La alternativa A cuesta $0 al mes y no tiene ruptura tarifaria: su único límite es físico (memoria y CPU del servidor del laboratorio). La alternativa B cuesta $0 mientras los despliegues mensuales no superen los 500 builds incluidos en el plan gratuito. Con el supuesto de 30 despliegues al mes, el margen medido por el script es de 16,7 veces, es decir, la ruptura llega a unos 500 despliegues mensuales; desde ahí tocaría pagar un plan o espaciar los despliegues.")
pdf.codigo("A Lab (Docker+nginx): $0/mes. Sin ruptura de precio.\nB gratuito: despliegues=30/mes builds_incluidos=500 cabe=SI\nRUPTURA_FREE: a x16.7 (~500 despliegues/mes).")

# 5
pdf.titulo("5. Reversión")
pdf.bullets([
    "A (laboratorio): restaurar la versión anterior de pieza/ y ejecutar terraform apply; downtime de segundos.",
    "B (gratuito): redeploy del deployment anterior inmutable desde el dashboard, en un clic.",
])

# 6
pdf.titulo("6. Decisión (ADR)")
pdf.cuerpo("Se adopta la alternativa A. Primero, cuesta $0 sin ruptura de precio ni cuentas externas y el laboratorio siempre está disponible. Segundo, su reversión tarda segundos y no depende de internet ni de terceros. Tercero, la alternativa B cabe en el plan gratuito pero introduce una dependencia externa y una ruptura calculada, por lo que queda como plan B si el laboratorio cae. La pieza es stateless, de modo que la reversión no arriesga datos.")

# 7
pdf.titulo("7. Evidencia")
pdf.cuerpo("Conforme a lo exigido, la evidencia está formada por salidas reales de ejecución y no por capturas de tutoriales: terraform validate exitoso en ambos módulos, terraform plan de la alternativa A, respuesta del curl al sitio en funcionamiento y salida del script de costos. Estas salidas se generan en el laboratorio y se anexan al README como sección de evidencia.")

pdf.output("Entrega-Taller-Despliegue.pdf")
print("PDF generado")
