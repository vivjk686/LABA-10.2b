# -*- coding: utf-8 -*-
import os
import docx
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex="F4F6F8"):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._element.get_or_add_tcPr().append(shading_elm)

def set_table_borders(table, color="D3D3D3", sz="4", val="single"):
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>\n'
            f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
            f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
            f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
            f'  <w:insideV w:val="none"/>\n'
            f'  <w:left w:val="none"/>\n'
            f'  <w:right w:val="none"/>\n'
            f'</w:tblBorders>'
        )
        tblPr[0].append(borders)

def add_p(doc, text="", bold=False, italic=False, size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, space_before=0, line_spacing=1.15):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.line_spacing = line_spacing
    if text:
        r = p.add_run(text)
        r.bold = bold
        r.italic = italic
        r.font.name = 'Times New Roman'
        r.font.size = Pt(size)
        r.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_h(doc, text, level=1):
    p = doc.add_paragraph()
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.color.rgb = RGBColor(0, 51, 102)
    if level == 1:
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        r.font.size = Pt(14)
    elif level == 2:
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        r.font.size = Pt(12.5)
    return p

def add_code_block(doc, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_shading(cell, "F8F9FA")
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    tcPr = cell._element.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'  <w:left w:val="single" w:sz="18" w:space="0" w:color="003366"/>\n'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>\n'
        f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>\n'
        f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>\n'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    r = p.add_run(code_text)
    r.font.name = 'Consolas'
    r.font.size = Pt(9.5)
    r.font.color.rgb = RGBColor(30, 30, 30)
    add_p(doc, "", space_after=4)

def add_image_box(doc, img_path, caption, width_inches=6.0):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(width_inches))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(10)
        r_cap = p_cap.add_run(caption)
        r_cap.font.name = 'Times New Roman'
        r_cap.font.size = Pt(10)
        r_cap.italic = True
        r_cap.font.color.rgb = RGBColor(80, 80, 80)

def read_txt(base_dir, rel_path):
    with open(os.path.join(base_dir, rel_path), "r", encoding="utf-8") as f:
        return f.read().rstrip()

BASE_DIR = r"C:\Users\User\OneDrive\Документи\лаби\LABA-10.2b"
IMG_DIR = os.path.join(BASE_DIR, "images")
OUT_DOCX = os.path.join(BASE_DIR, "АП_РІ-13_Шах_ЛР-10.2б.docx")

def generate_report():
    doc = docx.Document()
    for section in doc.sections:
        section.top_margin = Cm(2)
        section.bottom_margin = Cm(2)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(1.5)

    # --- ТИТУЛЬНА СТОРІНКА ---
    add_p(doc, "МІНІСТЕРСТВО ОСВІТИ І НАУКИ УКРАЇНИ", bold=True, size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ «ЛЬВІВСЬКА ПОЛІТЕХНІКА»", bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "Кафедра інформаційних систем та мереж", bold=False, italic=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=36)

    add_p(doc, "ЗВІТ", bold=True, size=20, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_p(doc, 'про виконання лабораторної роботи № 10.2б', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, '«Впорядкування та бінарний пошук в масиві структур з об’єднанням (Рівень В)»', bold=True, size=15, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "з дисципліни", bold=False, italic=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "«Алгоритмізація та програмування»", bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=50)

    info_tbl = doc.add_table(rows=2, cols=2)
    info_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_tbl.columns[0].width = Inches(3.2)
    info_tbl.columns[1].width = Inches(3.2)

    c0 = info_tbl.cell(0, 1)
    p0 = c0.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r0 = p0.add_run("Виконав:\nстудент групи РІ-13\nШах Владислав Ігорьович\nВаріант № 32")
    r0.font.name = 'Times New Roman'
    r0.font.size = Pt(12)

    c1 = info_tbl.cell(1, 1)
    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r1 = p1.add_run("Прийняв:\nГригорович В.Г.")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(12)

    add_p(doc, "", space_after=80)
    add_p(doc, "Львів – 2026", bold=False, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)
    doc.add_page_break()

    # --- 1. МЕТА ТА ТЕОРЕТИЧНІ ВІДОМОСТІ ---
    add_h(doc, "1. Мета роботи та теоретичні відомості", level=1)
    add_p(doc, 'Мета роботи: об’єднати роботу зі структурами з анонімним об’єднанням (рівень В) з алгоритмами фізичного та індексного багатоключового впорядкування і бінарного пошуку, організувавши керування через текстове меню з контролем помилок.')
    add_h(doc, "Теоретичні положення:", level=2)

    add_p(doc, '1. Структури з об’єднанням при сортуванні: під час фізичного впорядкування структури Student копіюються в пам’яті разом зі своїм активним полем об’єднання union та дискримінатором spec, що повністю зберігає цілісність третьої оцінки.')
    add_p(doc, '2. Перевага індексного сортування для структур з union: масив індексів idx оперує лише 4-байтовими цілими числами замість переміщення великих структур із рядками std::string та об’єднанням.')
    add_p(doc, '3. Бінарний пошук у впорядкованому масиві: використовує ті самі критерії впорядкування (фізика за зростанням, курс за зростанням, прізвище за спаданням) і гарантує знаходження запису або повернення -1 за O(log N) порівнянь.')

    # --- 2. УМОВА ЗАВДАННЯ ---
    add_h(doc, "2. Умова завдання (Варіант № 32)", level=1)
    add_p(doc, "Спільна частина завдання для всіх варіантів:")
    add_p(doc, 'Сформувати динамічний масив структур з анонімним об’єднанням рівня В. Програма має містити текстове меню з контролем помилок, функції фізичного та індексного впорядкування і бінарного пошуку.')
    add_image_box(doc, os.path.join(IMG_DIR, "task_common.png"), "Рис. 1. Загальна умова лабораторної роботи № 10.2б з методичних вказівок", width_inches=6.0)
    add_p(doc, "Індивідуальне завдання для Варіанта № 32 (стор. 64–65, 77):")
    add_p(doc, '1) Фізично впорядкувати масив: 1-й ключ — оцінка з фізики (за зростанням), 2-й ключ — номер курсу (за зростанням), 3-й ключ — прізвище (за спаданням — у зворотному до алфавітного порядку).\n2) Побудувати індексний масив за тими самими ключами (фізика, курс, прізвище).\n3) За допомогою бінарного пошуку визначити, чи навчається студент із вказаним прізвищем на вказаному курсі та з вказаною оцінкою з фізики.')
    add_image_box(doc, os.path.join(IMG_DIR, "task_var32.png"), "Рис. 2. Умова Варіанта № 32 з методичних вказівок", width_inches=6.0)

    # --- 3. СТРУКТУРНА СХЕМА ПРОГРАМИ ---
    add_h(doc, "3. Структурна схема програми", level=1)
    add_p(doc, "Програма побудована за модульним принципом згідно з вимогами методичних вказівок викладача Григоровича В.Г. Інтерфейсна частина (.h), реалізація функцій (.cpp) та головна програма розділені:")
    add_image_box(doc, os.path.join(IMG_DIR, "struct.png"), "Рис. 3. Структурна схема програми LABA-10.2b", width_inches=6.2)
    add_p(doc, "Опис архітектури та підпрограм:")

    add_p(doc, '• Головний блок main(): зчитує N, виділяє масив Student* p = new Student[N] та організовує циклічне меню [1]–[5], [0].')
    add_p(doc, '• Create(p, N), Print(p, N) та PrintIndexSorted(p, I, N): введення з валідацією та вивід 9-колонкової таблиці з підтримкою анонімного об’єднання union.')
    add_p(doc, '• Sort(p, N) та IndexSort(p, N): фізичне та індексне впорядкування за ключами (фізика↑, курс↑, прізвище↓).')
    add_p(doc, '• BinSearch(p, N, prizv, kurs, fizyka): двійковий пошук у фізично відсортованому масиві.')

    # --- 4. ТЕКСТ ПРОГРАМИ ---
    add_h(doc, "4. Текст програми", level=1)

    add_h(doc, '4.1. Текст програми LABA-10.2b.cpp', level=2)
    add_code_block(doc, read_txt(BASE_DIR, 'LABA-10.2b\\LABA-10.2b.cpp'))

    # --- 5. МОДУЛЬНЕ ТЕСТУВАННЯ ---
    add_h(doc, "5. Модульне тестування (UnitTest10.2b)", level=1)
    add_p(doc, 'У проекті UnitTest10.2b протестовано фізичне сортування, індексне сортування та бінарний пошук на масиві структур рівня В із заповненими полями union для різних спеціальностей.')
    add_code_block(doc, read_txt(BASE_DIR, 'UnitTest10.2b\\UnitTest10.2b.cpp'))
    add_p(doc, "Результати автоматизованого тестування (консольна утиліта vstest.console.exe):")
    add_image_box(doc, os.path.join(IMG_DIR, "console_test.png"), "Рис. 4. Успішне проходження всіх модульних тестів проекту", width_inches=6.0)

    # --- 6. РЕЗУЛЬТАТИ ВИКОНАННЯ ПРОГРАМИ ---
    add_h(doc, "6. Результати виконання програми", level=1)
    add_p(doc, 'Програму скомпільовано у Debug x64 (0 помилок, 0 попереджень). Тестування в консолі підтвердило збереження оцінок в об’єднанні після фізичного переміщення структур, правильну роботу індексного масиву та точний бінарний пошук.')
    add_image_box(doc, os.path.join(IMG_DIR, "console_main.png"), "Рис. 5. Консольне вікно виконання програми", width_inches=6.0)

    # --- 7. ПОСИЛАННЯ НА GITHUB ---
    add_h(doc, "7. Посилання на GitHub-репозиторій", level=1)
    add_p(doc, "Вихідний програмний код, заголовочні файли, файли реалізації, проект Visual Studio, юніт-тести та звіт розміщені у віддаленому репозиторії GitHub:")
    add_p(doc, 'https://github.com/vivjk686/LABA-10.2b', bold=True, size=12, align=WD_ALIGN_PARAGRAPH.LEFT)

    # --- 8. ВІДПОВІДІ НА КОНТРОЛЬНІ ПИТАННЯ ---
    add_h(doc, "8. Відповіді на контрольні питання", level=1)
    qa = [('1. Загальний синтаксис оголошення масивів та переліків, структур і об’єднань.', 'Масив: тип ім’я[розмір]; (динамічний: тип* ім’я = new тип[N];). Перелік: enum [Ім’я] { елем1, елем2, ... };. Структура: struct [Ім’я] { тип1 поле1; тип2 поле2; ... };. Об’єднання: union [Ім’я] { тип1 поле1; тип2 поле2; ... }; (або анонімне об’єднання без імені типу всередині структури).'), ('2. Доступ до елементів масивів та переліків, структур і об’єднань.', 'До елемента масиву звертаються за індексом a[i]. Переліку присвоюються та порівнюються його нумератори (p[i].spec = KOMP_NAUKY). До полів структури чи об’єднання за іменем змінної звертаються через оператор крапка (s.prizv), а через вказівник — оператором стрілка (ps->prizv або (*ps).prizv). Для анонімного об’єднання в структурі доступ до полів прямий: p[i].programming.'), ('3. Дії з масивами та переліками, структурами і об’єднаннями.', 'З елементами масиву виконують перебір, пошук, сортування, обчислення агрегатів. Переліки можна порівнювати (==, !=, <, >) та використовувати у switch. Структури одного типу можна присвоювати (s1 = s2), передавати у функції за значенням, вказівником або посиланням. У об’єднанні в кожний момент часу актуальним є лише одне поле, що займає спільну область пам’яті.'), ('4. Ініціалізація масивів та переліків, структур і об’єднань.', 'Ініціалізація виконується списком у фігурних дужках у порядку оголошення полів: Student s = {"Коваленко", 1, KOMP_NAUKY, 5, 5, 5};. Для об’єднання при статичній ініціалізації можна задати значення лише першому полю. Незаповнені поля ініціалізуються нулями.'), ('5. Внутрішня реалізація масивів та переліків, структур і об’єднань.', 'Масив зберігається у неперервній ділянці пам’яті. Елементи переліку компілятор замінює на цілі константи (0, 1, 2, ...). Поля структури розміщуються послідовно в пам’яті з урахуванням вирівнювання (padding) по границі, кратній розміру типу. Поля об’єднання накладаються одне на одне з однієї адреси, а розмір об’єднання дорівнює розміру його найбільшого поля.'), ('6. Передавання та опрацювання масивів та структур у функціях.', 'Динамічний масив структур передається у функцію через вказівник на перший елемент та кількість елементів: void Print(const Student* p, const int N). Якщо функція не змінює дані, використовується модифікатор const. Для повернення кількох значень застосовуються параметри-посилання (int& count5, int& count4, int& count3).'), ('7. Загальний синтаксис оголошення та формування динамічних масивів.', 'Виділення пам’яті: Student* p = new Student[N];, де N вводиться під час виконання програми. Заповнення здійснюється у циклі for (int i = 0; i < N; i++). Після завершення роботи пам’ять обов’язково звільняється оператором delete[] p;.'), ('8. Загальна схема фізичного впорядкування масиву.', 'Фізичне впорядкування змінює фактичне розташування структур у пам’яті. Використовується алгоритм обміну (бульбашкове сортування) з багатоключовим порівнянням: спочатку за первинним ключем (оцінка з фізики за зростанням), при рівності — за вторинним (курс за зростанням), при рівності обох — за третинним (прізвище за спаданням).'), ('9. Загальна схема індексного впорядкування масиву.', 'Індексне впорядкування не змінює вихідний масив структур p. Створюється цілочисельний масив індексів idx[0..N-1], ініціалізується значеннями 0, 1, ..., N-1, після чого методом вставки сортуються самі індекси з порівнянням структур p[idx[j]] та p[key]. Доступ до відсортованих записів здійснюється як p[idx[i]].'), ('10. Загальна схема бінарного пошуку в масиві.', 'Бінарний пошук працює лише на попередньо відсортованому масиві за тими самими ключами. На кожному кроці область пошуку [L; R] ділиться навпіл: m = (L + R) / 2. Якщо p[m] відповідає шуканим (prizv, kurs, physics) — повертається m; інакше звужується ліва або права половина залежно від порядку сортування (фізика↑, курс↑, прізвище↓). Складність — O(log N).')]
    for q, a in qa:
        add_p(doc, q, bold=True, size=11, space_before=4, space_after=2)
        add_p(doc, a, bold=False, size=11, space_before=0, space_after=6)

    # --- 9. ВИСНОВКИ ---
    add_h(doc, "9. Висновки", level=1)

    add_p(doc, '1. Успішно поєднано структуру рівня В з анонімним об’єднанням union та алгоритми багатоключового фізичного й індексного впорядкування.')
    add_p(doc, '2. Реалізовано бінарний пошук за прізвищем, курсом та оцінкою з фізики відповідно до порядку сортування Варіанта № 32.')
    add_p(doc, '3. Усі 3 модульні тести UnitTest10.2b пройшли успішно (3/3 Passed), що підтверджує коректність реалізації.')

    doc.save(OUT_DOCX)
    print("Report saved successfully:", OUT_DOCX)

if __name__ == "__main__":
    generate_report()
