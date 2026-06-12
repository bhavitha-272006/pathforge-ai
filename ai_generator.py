# ai_generator.py
# PDF export using ReportLab — called from app.py /download_pdf/<id>

from flask import make_response
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import io
from datetime import datetime


# ── Colour palette ──────────────────────────
PURPLE      = colors.HexColor("#7F77DD")
PURPLE_DARK = colors.HexColor("#3C3489")
TEAL        = colors.HexColor("#1D9E75")
AMBER       = colors.HexColor("#BA7517")
LIGHT_GRAY  = colors.HexColor("#F3F4F6")
MID_GRAY    = colors.HexColor("#6B7280")
DARK        = colors.HexColor("#111827")
WHITE       = colors.white


def generate_pdf(roadmap: dict):
    """
    Generate a PDF for the given roadmap dict and return a Flask Response.
    """
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title=f"{roadmap['goal']} Roadmap",
    )

    styles = getSampleStyleSheet()

    # ── Custom styles ──
    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        fontSize=24,
        textColor=PURPLE_DARK,
        spaceAfter=6,
        fontName="Helvetica-Bold",
    )
    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        fontSize=11,
        textColor=MID_GRAY,
        spaceAfter=4,
    )
    section_style = ParagraphStyle(
        "Section",
        parent=styles["Heading2"],
        fontSize=13,
        textColor=PURPLE_DARK,
        spaceBefore=14,
        spaceAfter=6,
        fontName="Helvetica-Bold",
    )
    skill_name_style = ParagraphStyle(
        "SkillName",
        parent=styles["Heading3"],
        fontSize=11,
        textColor=DARK,
        spaceBefore=10,
        spaceAfter=2,
        fontName="Helvetica-Bold",
    )
    body_style = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontSize=9,
        textColor=DARK,
        spaceAfter=3,
        leading=14,
    )
    bullet_style = ParagraphStyle(
        "Bullet",
        parent=styles["Normal"],
        fontSize=9,
        textColor=DARK,
        leftIndent=12,
        spaceAfter=2,
        leading=13,
        bulletIndent=4,
    )
    label_style = ParagraphStyle(
        "Label",
        parent=styles["Normal"],
        fontSize=8,
        textColor=MID_GRAY,
        spaceAfter=1,
    )

    story = []

    # ── Header ──
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph("✦ PathForge AI", ParagraphStyle(
        "Brand", parent=styles["Normal"], fontSize=9,
        textColor=PURPLE, spaceAfter=8, fontName="Helvetica-Bold"
    )))
    story.append(Paragraph(roadmap["goal"], title_style))
    story.append(Paragraph(
        f"{roadmap['level']} · {roadmap['duration']} · {roadmap['hours_per_day']} hrs/day",
        subtitle_style
    ))

    source_label = "AI Generated" if roadmap.get("source") == "ai" else "Curated Roadmap"
    story.append(Paragraph(
        f"Source: {source_label}  |  Generated: {datetime.now().strftime('%d %b %Y')}",
        label_style
    ))
    story.append(Spacer(1, 0.3 * cm))
    story.append(HRFlowable(width="100%", thickness=2, color=PURPLE, spaceAfter=10))

    # ── Summary table ──
    summary_data = [
        ["Goal", "Level", "Duration", "Daily Hours", "Total Skills"],
        [
            roadmap["goal"],
            roadmap["level"],
            roadmap["duration"],
            f"{roadmap['hours_per_day']} hrs",
            str(len(roadmap.get("skills", []))),
        ],
    ]
    summary_table = Table(summary_data, colWidths=[3.8 * cm, 2.8 * cm, 2.8 * cm, 2.8 * cm, 2.8 * cm])
    summary_table.setStyle(TableStyle([
        ("BACKGROUND",  (0, 0), (-1, 0),  PURPLE),
        ("TEXTCOLOR",   (0, 0), (-1, 0),  WHITE),
        ("FONTNAME",    (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",    (0, 0), (-1, 0),  8),
        ("FONTSIZE",    (0, 1), (-1, 1),  9),
        ("BACKGROUND",  (0, 1), (-1, 1),  LIGHT_GRAY),
        ("GRID",        (0, 0), (-1, -1), 0.5, colors.HexColor("#D1D5DB")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [LIGHT_GRAY]),
        ("ALIGN",       (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",      (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",  (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("ROUNDEDCORNERS", [4]),
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 0.5 * cm))

    # ── Skills ──
    story.append(Paragraph("Learning Roadmap", section_style))

    for i, skill in enumerate(roadmap.get("skills", []), 1):
        # Skill header row
        skill_header_data = [[
            Paragraph(f"{i}. {skill['name']}", skill_name_style),
            Paragraph(skill.get("duration", ""), ParagraphStyle(
                "Dur", parent=styles["Normal"], fontSize=8,
                textColor=PURPLE, alignment=2
            )),
        ]]
        skill_header = Table(skill_header_data, colWidths=[13 * cm, 4 * cm])
        skill_header.setStyle(TableStyle([
            ("VALIGN",  (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING",  (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ("LINEBELOW", (0, 0), (-1, -1), 0.5, colors.HexColor("#E5E7EB")),
        ]))
        story.append(skill_header)

        # Topics
        if skill.get("topics"):
            story.append(Paragraph("Topics:", label_style))
            topics_str = "  •  ".join(skill["topics"])
            story.append(Paragraph(topics_str, body_style))

        # Tasks
        if skill.get("tasks"):
            story.append(Paragraph("Hands-on Tasks:", label_style))
            for task in skill["tasks"]:
                story.append(Paragraph(f"▸  {task}", bullet_style))

        # Resources
        if skill.get("resources"):
            story.append(Paragraph("Resources:", label_style))
            for res in skill["resources"]:
                story.append(Paragraph(
                    f'<link href="{res["url"]}" color="#7F77DD">{res["title"]}</link>',
                    bullet_style
                ))

        story.append(Spacer(1, 0.2 * cm))

    # ── Footer ──
    story.append(Spacer(1, 0.5 * cm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=MID_GRAY))
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph(
        "Generated by PathForge AI  |  Your personalized career roadmap generator",
        ParagraphStyle("Footer", parent=styles["Normal"], fontSize=8,
                       textColor=MID_GRAY, alignment=1)
    ))

    doc.build(story)
    buffer.seek(0)

    filename = f"{roadmap['goal'].replace(' ', '_')}_Roadmap.pdf"
    response = make_response(buffer.read())
    response.headers["Content-Type"]        = "application/pdf"
    response.headers["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response


def generate_pdf_bytes(roadmap: dict) -> bytes:
    """
    Same as generate_pdf() but returns raw bytes instead of a Flask response.
    Used for attaching the PDF to an email.
    """
    buffer = io.BytesIO()
    _build_pdf(roadmap, buffer)
    buffer.seek(0)
    return buffer.read()


def _build_pdf(roadmap: dict, buffer):
    """Internal builder — shared by generate_pdf and generate_pdf_bytes."""
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.lib import colors
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    )
    from reportlab.lib.enums import TA_LEFT, TA_CENTER
    from datetime import datetime

    PURPLE      = colors.HexColor("#7F77DD")
    PURPLE_DARK = colors.HexColor("#3C3489")
    TEAL        = colors.HexColor("#1D9E75")
    LIGHT_GRAY  = colors.HexColor("#F3F4F6")
    MID_GRAY    = colors.HexColor("#6B7280")
    DARK        = colors.HexColor("#111827")
    WHITE       = colors.white

    doc = SimpleDocTemplate(buffer, pagesize=A4,
        rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm,
        title=f"{roadmap['goal']} Roadmap")
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle("CT", parent=styles["Title"], fontSize=24,
        textColor=PURPLE_DARK, spaceAfter=6, fontName="Helvetica-Bold")
    subtitle_style = ParagraphStyle("Sub", parent=styles["Normal"],
        fontSize=11, textColor=MID_GRAY, spaceAfter=4)
    section_style = ParagraphStyle("Sec", parent=styles["Heading2"],
        fontSize=13, textColor=PURPLE_DARK, spaceBefore=14, spaceAfter=6, fontName="Helvetica-Bold")
    skill_name_style = ParagraphStyle("SN", parent=styles["Heading3"],
        fontSize=11, textColor=DARK, spaceBefore=10, spaceAfter=2, fontName="Helvetica-Bold")
    body_style = ParagraphStyle("Body", parent=styles["Normal"],
        fontSize=9, textColor=DARK, spaceAfter=3, leading=14)
    bullet_style = ParagraphStyle("Bullet", parent=styles["Normal"],
        fontSize=9, textColor=DARK, leftIndent=12, spaceAfter=2, leading=13, bulletIndent=4)
    label_style = ParagraphStyle("Label", parent=styles["Normal"],
        fontSize=8, textColor=MID_GRAY, spaceAfter=1)

    story = []
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("✦ PathForge AI", ParagraphStyle("Brand",
        parent=styles["Normal"], fontSize=9, textColor=PURPLE, spaceAfter=8, fontName="Helvetica-Bold")))
    story.append(Paragraph(roadmap["goal"], title_style))
    story.append(Paragraph(
        f"{roadmap['level']} · {roadmap['duration']} · {roadmap['hours_per_day']} hrs/day", subtitle_style))
    source_label = "AI Generated" if roadmap.get("source") in ("ai","ai_cached") else "Curated Roadmap"
    story.append(Paragraph(
        f"Source: {source_label}  |  Generated: {datetime.now().strftime('%d %b %Y')}",
        label_style))
    story.append(Spacer(1, 0.3*cm))
    story.append(HRFlowable(width="100%", thickness=2, color=PURPLE, spaceAfter=10))

    summary_data = [
        ["Goal","Level","Duration","Daily Hours","Total Skills"],
        [roadmap["goal"], roadmap["level"], roadmap["duration"],
         f"{roadmap['hours_per_day']} hrs", str(len(roadmap.get("skills",[])))],
    ]
    t = Table(summary_data, colWidths=[3.8*cm,2.8*cm,2.8*cm,2.8*cm,2.8*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),PURPLE), ("TEXTCOLOR",(0,0),(-1,0),WHITE),
        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"), ("FONTSIZE",(0,0),(-1,0),8),
        ("FONTSIZE",(0,1),(-1,1),9), ("BACKGROUND",(0,1),(-1,1),LIGHT_GRAY),
        ("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#D1D5DB")),
        ("ALIGN",(0,0),(-1,-1),"CENTER"), ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("TOPPADDING",(0,0),(-1,-1),5), ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("Learning Roadmap", section_style))

    for i, skill in enumerate(roadmap.get("skills",[]), 1):
        sh = Table([[
            Paragraph(f"{i}. {skill['name']}", skill_name_style),
            Paragraph(skill.get("duration",""), ParagraphStyle("Dur",
                parent=styles["Normal"], fontSize=8, textColor=PURPLE, alignment=2)),
        ]], colWidths=[13*cm, 4*cm])
        sh.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),
            ("TOPPADDING",(0,0),(-1,-1),6), ("BOTTOMPADDING",(0,0),(-1,-1),2),
            ("LINEBELOW",(0,0),(-1,-1),0.5,colors.HexColor("#E5E7EB"))]))
        story.append(sh)
        if skill.get("topics"):
            story.append(Paragraph("Topics:", label_style))
            story.append(Paragraph("  •  ".join(skill["topics"]), body_style))
        if skill.get("tasks"):
            story.append(Paragraph("Hands-on Tasks:", label_style))
            for task in skill["tasks"]:
                story.append(Paragraph(f"▸  {task}", bullet_style))
        if skill.get("resources"):
            story.append(Paragraph("Resources:", label_style))
            for res in skill["resources"]:
                story.append(Paragraph(
                    f'<link href="{res["url"]}" color="#7F77DD">{res["title"]}</link>',
                    bullet_style))
        story.append(Spacer(1, 0.2*cm))

    story.append(Spacer(1, 0.5*cm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=MID_GRAY))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Generated by PathForge AI  |  Your personalized career roadmap generator",
        ParagraphStyle("Footer", parent=styles["Normal"], fontSize=8, textColor=MID_GRAY, alignment=1)))
    doc.build(story)