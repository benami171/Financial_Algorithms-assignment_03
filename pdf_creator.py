from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    textobject = c.beginText(50, height - 50)
    text_lines = [
        "",
        "Question 5:",
        "",
        "Author: Gal Ben Ami",
        "",
        "a): Does the LLM's answer describe the same algorithm as my code?",
        "",
        "Yes, the LLM's answer accurately describes the same algorithm as",
        "the one implemented in my code.",
        "Both the LLM's answer and my code describe the same algorithm:",
        "- The llm outlines a Fisher market approach where each agent's utility is a",
        "  weighted sum of allocated goods, with emphasis on 'bang-per-buck' optimality,",
        "  market clearing, and duality via the Eisenberg–Gale convex program.",
        "- my code implements this by defining allocation variables, computing",
        "  utilities, maximizing a sum of budgets multiplied by log(utilities), and",
        "  enforcing supply constraints. The dual variables of these constraints provide",
        "  the equilibrium prices.",
        "",
        "b): Did the LLM's answer provide a correct solution to the examples?",
        "",
        "Yes, the LLM's answer provides a correct solution to the examples and its solution is",
        "Described in the Linked Conversation below:",
        "https://chatgpt.com/share/67ec0ace-42b8-8004-a939-10ff1721c27a"
    ]
    
    for line in text_lines:
        textobject.textLine(line)
    
    c.drawText(textobject)
    
    # Define the rectangle for clickable link.
    # Adjust the coordinates based on where your link text is drawn.
    # In this example, we assume the link is at (50, height-200) with a width of 300 and height 15.
    c.linkURL("https://chatgpt.com/share/67ec0ace-42b8-8004-a939-10ff1721c27a",
              (50, height-200, 350, height-185), relative=0)
    
    c.showPage()
    c.save()
    print("PDF created:", filename)

if __name__ == "__main__":
    create_pdf("Question5_Explenation.pdf")