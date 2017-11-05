import json
import sys
import os

def convert_to_json(data):
    parsed_json = json.loads(data)
    return parsed_json

def build_label(element, item):
    element += "<span style=\"font-size:" + str(item["font-size"]) + ";\">"
    element += item["text"]
    element += "</span>"
    return element

def build_textfield(element, item):
    element += "<input type=\"text\" "
    element += "value=\"" + item["text"] + "\" "
    element += "placeholder=\"" + item["placeholder"] + "\" "
    element += "style=\"width:" + str(item["width"]) + "; "
    element += "height:" + str(item["height"]) + "; "
    element += "font-size:" + str(item["font-size"]) + ";\">"
    return element

def build_button(element, item):
    element += "<button type=\"button\" "
    element += "style=\"width:" + str(item["width"]) + "; "
    element += "height:" + str(item["height"]) + "; "
    element += "font-size:" + str(item["font-size"]) + ";\">"
    element += item["text"]
    element += "</button>"
    return element

def convert_to_html(data):
    elements = []
    for key in data:
        item = data[key]

        # Build html elements
        element = "<div style=\"position:absolute; top:"
        element += str(item["y-coordinate"]) + "; left:"
        element += str(item["x-coordinate"]) + ";\""
        element += " id=\"" + item["id"] + "\">"

        # Build for specific ui element
        if item["type"] == "label":
            element = build_label(element, item)
        elif item["type"] == "textfield":
            element = build_textfield(element, item)
        elif item["type"] == "button":
            element = build_button(element, item) 

        element = element + "</div>"


        elements.append(element)

    return elements

def build_html(elements):
    html = "<html><body>"

    for item in elements:
        html += item

    html += "</body></html>"

    return html


def write_to_file(string_to_write, filename="output.html"):
    with open(filename, "w") as f:
        f.write(string_to_write)

def parse(file):
    data = file.read()
    parsed_json = convert_to_json(data)
    html_elements = convert_to_html(parsed_json)
    html_string = build_html(html_elements)
    write_to_file(html_string, "./ui_parser/templates/output/output.html")
    

# arg_list = sys.argv[1:]
# for arg in arg_list:
#     print("Reading file: " + arg)
#     with open(arg, "r") as f:
#         data = f.read()
#         parsed_json = parse(data)
#         html_elements = convert_to_html(parsed_json)
#         html_string = build_html(html_elements)
#         write_to_file(html_string, (arg.split(".")[0])+".html")
        

