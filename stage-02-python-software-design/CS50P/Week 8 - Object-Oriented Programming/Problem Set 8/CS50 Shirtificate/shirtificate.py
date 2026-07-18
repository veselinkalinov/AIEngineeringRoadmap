from fpdf import FPDF


def main():
    name = input("Name: ")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Certificate title
    pdf.set_font("Helvetica", style="B", size=48)
    pdf.set_xy(0, 20)
    pdf.cell(
        w=pdf.w,
        h=20,
        text="CS50 Shirtificate",
        align="C",
    )

    # Center the shirt image horizontally
    image_width = 190
    image_x = (pdf.w - image_width) / 2

    pdf.image(
        "shirtificate.png",
        x=image_x,
        y=65,
        w=image_width,
    )

    # Place the user's name over the shirt
    pdf.set_font("Helvetica", style="B", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 115)
    pdf.cell(
        w=pdf.w,
        h=15,
        text=f"{name} took CS50",
        align="C",
    )

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
