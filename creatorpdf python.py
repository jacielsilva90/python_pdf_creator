from reportlab.pdfgen import canvas

# nome do arquivo PDF
pdf = canvas.Canvas("meu_primeiro_pdf.pdf")

# Adiciona um texto definindo a posição X, Y
pdf.drawString(100, 750, "Olá! Este PDF foi gerado usando Python e ReportLab.")
#pdf.showPage() = avançar para uma nova página no mesmo documento
# Salva o pdf
pdf.save()
