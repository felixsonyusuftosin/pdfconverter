import xlrd
import os
import pdfkit
from templates.html_util import construct_html

options = {
    'page-size': 'Letter',
    'orientation':'Portrait',
    'margin-top': '0.35in',
    'margin-right': '0.35in',
    'margin-bottom': '0.35in',
    'margin-left': '0.35in',
    'encoding': "UTF-8",
    'footer-right': '[page] of [topage]',
    'footer-center': 'Confidential',
    'custom-header' : [
        ('Accept-Encoding', 'gzip')
    ]
}

def compile_pdf(filename):
    html_file = os.path.join(os.path.dirname(
        __file__), "output_files/{}.html".format(filename))
    out_pdf = os.path.join(os.path.dirname(__file__),
                           "output_files/{}.pdf".format(filename))
    pdfkit.from_file(html_file, out_pdf, options)


def transform(items_to_transform,  filename):
    output_file = os.path.join(os.path.dirname(
        __file__), "output_files/{}.html".format(filename))
    print(output_file)
    f = open(output_file, "wb")
    f.write(construct_html(items_to_transform))
    f.close()
    compile_pdf(filename)


def generate_pdf():
    for root, dirs, files in os.walk(os.path.join(os.path.dirname(__file__), "input_files")):
        for filename in files:
            xls_path = os.path.join(root, filename)
            wb = xlrd.open_workbook(xls_path)
            sheet = wb.sheet_by_index(0)

            # properties
            xls_row_len = sheet.nrows
            xls_col_len = sheet.ncols

            ''' First line which contains the title'''
            header = ""
            for i in range(xls_col_len):
                first_line = (sheet.cell_value(0, i))
                if str(first_line).strip():
                  header += first_line
            header = header.strip()

            ''' Second line through 4th line contains info'''
            groupname = (sheet.cell_value(1, 0)).strip()
            pcp = (sheet.cell_value(2, 0)).strip()
            as_of_date = (sheet.cell_value(3, 0)).strip()

            ''' Fifth line contains some header info '''
            main_sheet_heads = []
            for i in range(xls_col_len):
                line = sheet.cell_value(5, i)
                if str(line).strip():
                  main_sheet_heads.append(line.strip())

            ''' sixth line contains slim row '''
            slim_rows = []
            for i in range(xls_col_len):
                line = sheet.cell_value(6, i)
                if str(line).strip().replace('.0', ''):
                  slim_rows.append(str(line).strip())

            ''' seventh line contains subhead'''
            sub_heads = []
            for i in range(xls_col_len):
                line = sheet.cell_value(7, i)
                if str(line).strip():
                  sub_heads.append(str(line).strip())

            ''' all the other lines'''
            rest_rows = []
            for i in range(8, xls_row_len):
                row = []
                for x in range(xls_col_len):
                    line = sheet.cell_value(i, x)
                    row.append(str(line).strip())
                rest_rows.append(row)

            data = dict()
            data['header'] = header
            data['groupname'] = groupname
            data['pcp'] = pcp
            data['as_of_date'] = as_of_date
            data['main_heads'] = main_sheet_heads
            data['slim_rows'] = slim_rows
            data['sub_heads'] = sub_heads
            data['rest_rows'] = rest_rows

            transform(data, filename)


generate_pdf()
