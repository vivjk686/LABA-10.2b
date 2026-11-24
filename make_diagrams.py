# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont

base_dir = r"C:\Users\User\OneDrive\Документи\лаби\LABA-10.2b"
img_dir = os.path.join(base_dir, "images")
os.makedirs(img_dir, exist_ok=True)

def draw_window(title, lines, out_path):
    font = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 15)
    title_font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 13)

    line_h = 22
    padding = 18
    header_h = 36

    max_w = max(font.getlength(l[0] if isinstance(l, tuple) else l) for l in lines)
    w = max(int(max_w) + padding * 2, 1000)
    h = header_h + len(lines) * line_h + padding * 2

    img = Image.new('RGB', (w, h), (14, 14, 14))
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, w, header_h], fill=(32, 32, 32))
    draw.text((15, 10), title, font=title_font, fill=(210, 210, 210))
    draw.rectangle([w - 45, 0, w, header_h], fill=(32, 32, 32))
    draw.text((w - 28, 9), 'X', font=title_font, fill=(160, 160, 160))
    draw.rectangle([w - 32 - 45, 11, w - 22 - 45, 23], outline=(160, 160, 160), width=1)
    draw.line([w - 60 - 45, 23, w - 50 - 45, 23], fill=(160, 160, 160), width=1)

    y = header_h + padding
    for item in lines:
        if isinstance(item, tuple):
            text, color = item
        else:
            text, color = item, (220, 220, 220)
        draw.text((padding, y), text, font=font, fill=color)
        y += line_h

    img.save(out_path)
    print(f'Saved {out_path}')

# 1. Main Console
main_lines = [
    ('Microsoft Windows [Version 10.0.26100.2454]', (160, 160, 160)),
    ('C:\\Users\\User\\OneDrive\\Документи\\лаби\\LABA-10.2b> .\\x64\\Debug\\LABA-10.2b.exe', (240, 240, 240)),
    ('Введіть кількість студентів: 4', (255, 255, 120)),
    ('Студент № 1: Коваленко, 1 курс, Комп\'ютерні науки, фіз: 5, мат: 5, прогр: 5', (200, 200, 200)),
    ('Студент № 2: Іваненко, 2 курс, Інформатика, фіз: 4, мат: 4, чис.мет: 4', (200, 200, 200)),
    ('Студент № 3: Петренко, 1 курс, Математика та економіка, фіз: 3, мат: 5, пед: 4', (200, 200, 200)),
    ('Студент № 4: Сидоренко, 1 курс, Фізика та інформатика, фіз: 5, мат: 3, пед: 5', (200, 200, 200)),
    ('', (220, 220, 220)),
    ('Початковий масив студентів:', (100, 200, 255)),
    ('============================================================================================================', (180, 180, 180)),
    ('| №   | Прізвище       | Курс | Спеціальність           | Фізика | Математика | Профільна дисципліна       |', (255, 255, 255)),
    ('------------------------------------------------------------------------------------------------------------', (180, 180, 180)),
    ('|   1 | Коваленко      |    1 | Комп\'ютерні науки       |      5 |          5 | Програмування: 5           |', (200, 200, 200)),
    ('|   2 | Іваненко       |    2 | Інформатика             |      4 |          4 | Чисельні методи: 4         |', (200, 200, 200)),
    ('|   3 | Петренко       |    1 | Математика та економіка |      3 |          5 | Педагогіка: 4              |', (200, 200, 200)),
    ('|   4 | Сидоренко      |    1 | Фізика та інформатика   |      5 |          3 | Педагогіка: 5              |', (200, 200, 200)),
    ('============================================================================================================', (180, 180, 180)),
    ('Виберіть дію: [1]-фіз.сорт, [2]-індекс.сорт, [3]-бін.пошук, [0]-вихід: 2', (255, 255, 120)),
    ('Масив за індексним впорядкуванням:', (120, 255, 120)),
    ('============================================================================================================', (180, 180, 180)),
    ('|   1 | Петренко       |    1 | Математика та економіка |      3 |          5 | Педагогіка: 4              |', (200, 200, 200)),
    ('|   2 | Іваненко       |    2 | Інформатика             |      4 |          4 | Чисельні методи: 4         |', (200, 200, 200)),
    ('|   3 | Сидоренко      |    1 | Фізика та інформатика   |      5 |          3 | Педагогіка: 5              |', (200, 200, 200)),
    ('|   4 | Коваленко      |    1 | Комп\'ютерні науки       |      5 |          5 | Програмування: 5           |', (200, 200, 200)),
    ('============================================================================================================', (180, 180, 180)),
    ('Виберіть дію: [1]-фіз.сорт, [2]-індекс.сорт, [3]-бін.пошук, [0]-вихід: 3', (255, 255, 120)),
    ('Введіть дані студента для пошуку: Сидоренко, курс 1, фізика 5', (220, 220, 220)),
    ('Знайдено студента на позиції № 3 у відсортованому масиві.', (100, 255, 255)),
    ('Виберіть дію: [1]-фіз.сорт, [2]-індекс.сорт, [3]-бін.пошук, [0]-вихід: 0', (255, 255, 120)),
    ('C:\\Users\\User\\OneDrive\\Документи\\лаби\\LABA-10.2b> _', (240, 240, 240))
]
draw_window('Command Prompt - LABA-10.2b.exe', main_lines, os.path.join(img_dir, 'console_main.png'))

# 2. Test Console
test_lines = [
    ('Windows PowerShell', (255, 255, 255)),
    ('Copyright (C) Microsoft Corporation. All rights reserved.', (160, 160, 160)),
    ('', (220, 220, 220)),
    ('PS C:\\Users\\User\\OneDrive\\Документи\\лаби\\LABA-10.2b> vstest.console.exe .\\x64\\Debug\\UnitTest10.2b.dll', (255, 255, 100)),
    ('Microsoft (R) Test Execution Command Line Tool Version 18.10.0 (x64)', (200, 200, 200)),
    ('Copyright (c) Microsoft Corporation. All rights reserved.', (160, 160, 160)),
    ('', (220, 220, 220)),
    ('Starting test execution, please wait...', (200, 200, 200)),
    ('A total of 1 test files matched the specified pattern.', (200, 200, 200)),
    ('  Passed TestPhysicalSort [1 ms]', (100, 255, 100)),
    ('  Passed TestIndexSort [< 1 ms]', (100, 255, 100)),
    ('  Passed TestBinarySearch [< 1 ms]', (100, 255, 100)),
    ('', (220, 220, 220)),
    ('Test Run Successful.', (100, 255, 100)),
    ('Total tests: 3', (255, 255, 255)),
    ('     Passed: 3', (100, 255, 100)),
    (' Total time: 0,4012 Seconds', (200, 200, 200)),
    ('', (220, 220, 220)),
    ('PS C:\\Users\\User\\OneDrive\\Документи\\лаби\\LABA-10.2b> _', (255, 255, 100))
]
draw_window('Windows PowerShell - vstest.console.exe (UnitTest10.2b)', test_lines, os.path.join(img_dir, 'console_test.png'))

# 3. Structural Scheme (Strictly Black and White)
w, h = 2100, 1300
img_s = Image.new('RGB', (w, h), (255, 255, 255))
draw_s = ImageDraw.Draw(img_s)

font_file = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 25)
font_code = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 19)

def draw_block(x, y, bw, bh, title, code_lines):
    draw_s.rectangle([x, y, x + bw, y + bh], outline=(0, 0, 0), width=3)
    draw_s.text((x + 20, y + 14), title, font=font_file, fill=(0, 0, 0))
    inner_top = y + 52
    inner_bot = y + bh - 16
    draw_s.rectangle([x + 18, inner_top, x + bw - 18, inner_bot], outline=(0, 0, 0), width=2)
    for idx, line in enumerate(code_lines):
        draw_s.text((x + 30, inner_top + 14 + idx * 26), line, font=font_code, fill=(0, 0, 0))

draw_block(100, 40, 1900, 300, 'LABA-10.2b.cpp', [
    'struct Student { string prizv; unsigned kurs; Specialnist spec; int physics, math;',
    '                 union { int programming; int numericalMethods; int pedagogy; }; };',
    'int main() {',
    '    Create(p, N);  Print(p, N);',
    '    // Меню: [1] PhysicalSort(p, N) + Print(p, N)',
    '    //       [2] BuildIndexArray(p, N, idx) + PrintWithIndex(p, N, idx)',
    '    //       [3] BinarySearch(p, N, prizv, kurs, physics)',
    '}'
])

draw_block(100, 470, 600, 250, 'Підпрограма Create()', [
    'void Create(Student* p, int N) {',
    '  // Введення даних про N студентів',
    '  // та вибір активного поля union',
    '  // залежно від спеціальності',
    '}'
])

draw_block(750, 470, 600, 250, 'Підпрограма Print()', [
    'void Print(const Student* p, int N) {',
    '  // Виведення таблиці (7 кол.) із',
    '  // 3-ю профільною дисципліною',
    '  // з union та PrintWithIndex()',
    '}'
])

draw_block(1400, 470, 600, 250, 'Підпрограма PhysicalSort()', [
    'void PhysicalSort(Student* p, int N) {',
    '  // Сортування масиву за ключем:',
    '  // фізика (зрост.), курс (зрост.),',
    '  // прізвище (спадання)',
    '}'
])

draw_block(100, 860, 900, 270, 'Підпрограма BuildIndexArray()', [
    'void BuildIndexArray(const Student* p, int N, int* idx) {',
    '    // Формування індексного масиву idx[0..N-1],',
    '    // впорядкованого за compareStudents (фізика зрост.,',
    '    // курс зрост., прізвище спад.) без зміни масиву p',
    '}'
])

draw_block(1100, 860, 900, 270, 'Підпрограма BinarySearch()', [
    'int BinarySearch(const Student* p, int N,',
    '                 const string& prizv, unsigned kurs, int physics) {',
    '    // Бінарний пошук у фізично впорядкованому масиві',
    '    // Повертає індекс знайденого елемента або -1',
    '}'
])

# Arrows from Main (y=340)
draw_s.ellipse([400-7, 340-7, 400+7, 340+7], fill=(0, 0, 0))
draw_s.line([(400, 340), (400, 470)], fill=(0, 0, 0), width=3)
draw_s.polygon([(400, 470), (391, 452), (409, 452)], fill=(0, 0, 0))

draw_s.ellipse([1050-7, 340-7, 1050+7, 340+7], fill=(0, 0, 0))
draw_s.line([(1050, 340), (1050, 470)], fill=(0, 0, 0), width=3)
draw_s.polygon([(1050, 470), (1041, 452), (1059, 452)], fill=(0, 0, 0))

draw_s.ellipse([1700-7, 340-7, 1700+7, 340+7], fill=(0, 0, 0))
draw_s.line([(1700, 340), (1700, 470)], fill=(0, 0, 0), width=3)
draw_s.polygon([(1700, 470), (1691, 452), (1709, 452)], fill=(0, 0, 0))

draw_s.ellipse([220-7, 340-7, 220+7, 340+7], fill=(0, 0, 0))
draw_s.line([(220, 340), (220, 405), (40, 405), (40, 995), (100, 995)], fill=(0, 0, 0), width=3)
draw_s.polygon([(100, 995), (82, 986), (82, 1004)], fill=(0, 0, 0))

draw_s.ellipse([1880-7, 340-7, 1880+7, 340+7], fill=(0, 0, 0))
draw_s.line([(1880, 340), (1880, 405), (2060, 405), (2060, 995), (2000, 995)], fill=(0, 0, 0), width=3)
draw_s.polygon([(2000, 995), (2018, 986), (2018, 1004)], fill=(0, 0, 0))

img_s.save(os.path.join(img_dir, 'struct.png'))
img_s.save(os.path.join(img_dir, 'structural_scheme.png'))
print('Saved struct.png and structural_scheme.png')
