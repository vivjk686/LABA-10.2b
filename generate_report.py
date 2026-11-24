# -*- coding: utf-8 -*-
import os
from docx import Document
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = r"C:\Users\User\OneDrive\Документи\лаби\LABA-10.2b"
IMG_DIR = os.path.join(BASE_DIR, "images")
OUT_DOCX = os.path.join(BASE_DIR, "АП_РІ-13_Шах_ЛР-10.2б.docx")

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex="F8F9FA"):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._element.get_or_add_tcPr().append(shading_elm)

def add_p(doc, text="", bold=False, italic=False, size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, space_before=0):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.line_spacing = 1.15
    if text:
        r = p.add_run(text)
        r.bold = bold
        r.italic = italic
        r.font.name = 'Times New Roman'
        r.font.size = Pt(size)
        r.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_h(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(text)
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_code_block(doc, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_shading(cell, "F8F9FA")
    set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
    tcPr = cell._element.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'  <w:left w:val="single" w:sz="12" w:space="0" w:color="333333"/>\n'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    r = p.add_run(code_text)
    r.font.name = 'Courier New'
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(0, 0, 0)
    add_p(doc, "", space_after=4)

def add_img(doc, path, caption):
    if os.path.exists(path):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        p.add_run().add_picture(path, width=Inches(5.5))
        add_p(doc, caption, italic=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)

def read_txt(rel_path):
    with open(os.path.join(BASE_DIR, rel_path), "r", encoding="utf-8") as f:
        return f.read().rstrip()

def generate_report():
    doc = Document()
    for section in doc.sections:
        section.top_margin = Cm(2)
        section.bottom_margin = Cm(2)
        section.left_margin = Cm(2)
        section.right_margin = Cm(2)

    add_p(doc, "", space_after=60)
    title_text = (
        "ЗВІТ\n"
        "про виконання лабораторної роботи № 10.2b\n"
        "«Масиви структур та об'єднань»\n"
        "з дисципліни\n"
        "«Алгоритмізація та програмування»\n\n"
        "студента групи РІ-13\n"
        "Шаха Владислава Ігоровича"
    )
    add_p(doc, title_text, bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    add_p(doc, "", space_after=60)
    add_p(doc, "Варіант № 32", bold=True, size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    doc.add_page_break()

    add_h(doc, "1. Мета роботи")
    add_p(doc, "Метою лабораторної роботи є набуття практичних навичок визначення і використання структур даних (struct), переліків (enum) та об'єднань (union) у мові програмування С++. Вивчення способів оголошення масивів структур, звернення до полів структур, а також реалізації підпрограм обробки масивів структур.")

    add_h(doc, "2. Завдання")
    add_img(doc, os.path.join(IMG_DIR, "task.png"), "Рис. 1. Умова лабораторної роботи № 10.2b (Варіант 32)")

    add_h(doc, "3. Алгоритм розв'язання")
    add_p(doc, "1. Описано структуру Student рівня В з переліком Specialnist та анонімним об'єднанням union { int programming; int numericalMethods; int pedagogy; } для зберігання третьої профільної оцінки.")
    add_p(doc, "2. Підпрограми Create(), Print() та PrintWithIndex() працюють з активним полем об'єднання залежно від поля spec кожного студента.")
    add_p(doc, "3. Реалізовано фізичне сортування PhysicalSort(p, N) та індексне сортування BuildIndexArray(p, N, idx) за спільним компаратором compareStudents: оцінка з фізики (за зростанням), номер курсу (за зростанням), прізвище (за спаданням).")
    add_p(doc, "4. Підпрограма BinarySearch(p, N, prizv, kurs, physics) виконує двійковий пошук у фізично відсортованому масиві структур з урахуванням того ж багатоключового порядку.")
    add_p(doc, "5. У головній програмі реалізовано інтерактивне меню з валідацією введення та коректним звільненням динамічних масивів p та idx.")

    add_h(doc, "4. Лістинг програми")
    add_p(doc, "Головний файл програми LABA-10.2b.cpp:", bold=True, space_after=4)
    add_code_block(doc, read_txt(r"LABA-10.2b\LABA-10.2b.cpp"))
    add_p(doc, "Заголовний файл student2b.h:", bold=True, space_after=4)
    add_code_block(doc, read_txt(r"LABA-10.2b\student2b.h"))
    add_p(doc, "Файл реалізації student2b.cpp:", bold=True, space_after=4)
    add_code_block(doc, read_txt(r"LABA-10.2b\student2b.cpp"))

    add_h(doc, "5. Схема програми")
    add_img(doc, os.path.join(IMG_DIR, "struct.png"), "Рис. 2. Структурна схема програми LABA-10.2b")

    add_h(doc, "6. Результати виконання програми")
    add_img(doc, os.path.join(IMG_DIR, "console_main.png"), "Рис. 3. Результат роботи основної програми у консолі")
    add_img(doc, os.path.join(IMG_DIR, "console_test.png"), "Рис. 4. Результат виконання модульних тестів (vstest.console.exe)")

    add_h(doc, "7. Контрольні запитання")
    qa = [
        ("1. Як об'єднання (union) взаємодіє з операціями фізичного сортування структур?",
         "При копіюванні або обміні структур std::swap(p[j], p[j+1]) у C++ копіюються всі поля, включно з об'єднанням; оскільки всі поля об'єднання в цій задачі мають тип int, поточне активне поле коректно переноситься разом зі структурою."),
        ("2. Чому індексне сортування не змінює порядок елементів у вихідному масиві?",
         "Алгоритм формує окремий масив індексів idx[] і переставляє значення в ньому, порівнюючи елементи вихідного масиву через p[idx[j]], завдяки чому сам масив p лишається недоторканим."),
        ("3. Що потрібно зробити перед викликом функції бінарного пошуку?",
         "Обов'язково потрібно фізично відсортувати масив структур за тим самим критерієм, за яким працює компаратор бінарного пошуку, тому перед BinarySearch викликається PhysicalSort(p, N)."),
        ("4. Як впливає використання enum Specialnist на роботу з union?",
         "Значення enum Specialnist виступає дискримінантом (тегом), який однозначно вказує, яке з полів union (programming, numericalMethods або pedagogy) слід зчитувати чи виводити."),
        ("5. Навіщо у програмі передбачається контроль помилок введення користувача?",
         "Перевірка стану потоку cin (cin.clear(), cin.ignore()) запобігає нескінченним циклам та некоректній роботі меню у випадку введення нечислових або недопустимих значень.")
    ]
    for q, a in qa:
        add_p(doc, q, bold=True, size=12, space_before=4, space_after=2)
        add_p(doc, a, bold=False, size=12, space_before=0, space_after=6)

    add_h(doc, "8. Висновки")
    add_p(doc, "Під час виконання лабораторної роботи № 10.2b об'єднано роботу зі структурами даних, що містять анонімне об'єднання union, з алгоритмами фізичного та індексного сортування і бінарного пошуку за кількома ключами. Усі три модульні тести в UnitTest10.2b успішно пройшли перевірку, підтвердивши правильність реалізованих алгоритмів.")

    doc.save(OUT_DOCX)
    print("Saved:", OUT_DOCX)

if __name__ == "__main__":
    generate_report()
