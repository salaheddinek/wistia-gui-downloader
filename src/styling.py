import colorsys
import logging


COLORS = {
    "entry_bg": "#fafafa",
    # "entry_bg": "#fafa00",
    "borders": "#b4b4b4",
    "borders_focus": "#9c9cc9",
}

LOGS_COLORS = {
    logging.INFO: "#206040",
    logging.WARNING: "#996633",
    logging.ERROR: "#ad1f1f"
}


def change_lightness(in_hex_color, in_added_lightness):
    c_hex = in_hex_color.lstrip('#')
    lv = len(c_hex)
    r, g, b = tuple(int(c_hex[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    h, l, s = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
    n_l = l + in_added_lightness
    n_l = max(0, min(1, n_l))
    r, g, b = colorsys.hls_to_rgb(h, n_l, s)
    return '#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255))


def generate_button_stylesheet(hex_color):
    light_c = change_lightness(hex_color, 0.05)
    c = hex_color
    dark_c = change_lightness(hex_color, -0.05)
    darker_c = change_lightness(hex_color, -0.1)
    darkest_c = change_lightness(hex_color, -0.2)

    ss = ""
    ss += "QPushButton {"
    ss += f"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 {c}, stop:1 {dark_c});"
    ss += f"border-radius:3px; border: solid {darkest_c}; "
    ss += "border-width: 1px 2px 2px 1px;"
    ss += "padding: 10px 15px 10px 15px;"
    ss += "}"
    ss += "QPushButton:hover {"
    ss += f"background-color: qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 {light_c}, stop:1 {c});"
    ss += "}"
    ss += "QPushButton:disabled {"
    ss += f"background-color: qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 {dark_c}, stop:1 {darker_c});"
    ss += "}"
    ss += f"QPushButton:pressed {{background-color: {darker_c};}}"
    ss_tb = ss.replace("QPushButton", "QToolButton")
    ss_tb = ss_tb.replace("padding: 10px 15px 10px 15px;", "padding: 7px 7px 7px 7px;")
    # print(ss_tb)
    return ss + ss_tb


def generate_tool_button_stylesheet(hex_color):
    ss_btn = generate_button_stylesheet(hex_color)
    ss = ss_btn.replace("QPushButton", "QToolButton")
    ss = ss.replace("padding: 10px 15px 10px 15px;", "padding: 7px 7px 7px 7px;")
    return ss


def generate_frame_stylesheet(bg_color="", exclusive_id=""):
    ss = "QFrame"

    ss += f"{{border-width: 1; border-radius: 3; border-style: solid; border-color: {COLORS['borders']};}}"
    if bg_color != "":
        ss += f"QFrame{{background-color: {bg_color};}}"
        ss += f"QFrame::disabled{{background-color: {change_lightness(bg_color, -0.1)};}}"
        ss += f"QFrame::focus{{border-color: {COLORS['borders_focus']};border-width: 1.55;}}"

    if exclusive_id != "":
        ss = ss.replace("QFrame", f"QFrame#{exclusive_id}")
    return ss


def generate_line_edit_stylesheet(bg_color=""):
    frame_ss = generate_frame_stylesheet(bg_color=bg_color)
    frame_ss = frame_ss.replace("QFrame", "QLineEdit")
    frame_ss += "QLineEdit{padding: 3px;}"
    return frame_ss
