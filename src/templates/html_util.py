from templates.css_util import generate_css


def construct_html(value):
    style = generate_css()
    html_template = """
  <!DOCTYPE html>
  <html>
  <head>
   {}
  </head>

  <body>
    <section class="main">
        <h2 class="header">{}</h2>
        <div class="info">
          <p class="row-info">{}</p>
          <p class="row-info">{}</p>
          <p class="row-info">{}</p>
        </div>
      <div class="table">
       <div class="row">
         {}
       </div>
       <div class="row">
        {}
       </div>
      <div class="row">
        {}
       </div>
        {}
      </div>
    </section>
  </body>
  </html>
  """.format(
        style,
        value['header'],
        value['groupname'],
        value['pcp'],
        value['as_of_date'],
        display_main_head_rows(value['main_heads']),
        display_slim_rows(value['slim_rows']),
        display_sub_head_rows(value['sub_heads']),
        display_rest_rows(value['rest_rows'])
    ).replace("+++", "}").replace("++", "{").encode()
    return html_template


def display_main_head_rows(rows):
    main_string = ""
    for row in rows:
        converted = "\t<div class=\"col main-head\">{}</div>\n".format(row)
        main_string += converted
    return main_string


def display_sub_head_rows(rows):
    main_string = ""
    for row in rows:
        converted = "\t<div class=\"col sub-head\">{}</div>\n".format(row)
        main_string += converted
    return main_string


def display_slim_rows(rows):
    main_string = ""
    for row in rows:
        converted_slim = "\t<div class=\"col slim-row\">{}</div>\n".format(row)
        main_string += converted_slim
    return main_string


def display_rest_rows(rows_complex):
    main_str = ""
    for row in rows_complex:
        main_str += "<div class=\"row\">\n"
        for sub_row in row:
            if sub_row == 'Very High Priority':
                converted_slim = "\t<div class=\"col rest-row very-high-pri\">{}</div>\n".format(
                    sub_row)
            elif sub_row == 'High Priority':
                converted_slim = "\t<div class=\"col rest-row high-pri\">{}</div>\n".format(
                    sub_row)
            elif sub_row == 'Low':
                converted_slim = "\t<div class=\"col rest-row low-pri\">{}</div>\n".format(
                    sub_row)
            elif sub_row == 'Medium':
                converted_slim = "\t<div class=\"col rest-row medium-pri\">{}</div>\n".format(
                    sub_row)
            else:
                converted_slim = "\t<div class=\"col rest-row\">{}</div>\n".format(
                    sub_row)
            main_str += converted_slim
        main_str += "</div>\n"
    return main_str
