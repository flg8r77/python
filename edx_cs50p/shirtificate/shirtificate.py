from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("courier", "B", 34)
        width = self.get_string_width(self.title)
        self.set_x((210 - width) / 2)
        self.cell(
            width,
            40,
            self.title,
            align="C"
        )


def main():
    name = input("Name: ")
    logo = f"{name} took CS50"

    pdf = PDF()
    pdf.set_title("CS50 Shirtificate")
    pdf.add_page()
    pdf.image("./shirtificate.png", 27, 70, 156.9, 156.6)
    pdf.set_font("helvetica", "B", 21)
    logo_width = pdf.get_string_width(logo)
    pdf.set_xy(60,110)
    pdf.set_text_color(233, 230, 223)
    pdf.cell(
        90,
        21,
        logo,
        align='C'
    )
    pdf.output("./shirtificate.pdf")

if __name__ == "__main__":
    main()