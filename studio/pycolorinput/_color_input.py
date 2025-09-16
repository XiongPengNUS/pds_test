from htmltools import Tag, TagList, tags


def color_input(id: str, label: str, value: str = "#1E90FF") -> Tag:
    """
    A reusable color picker that integrates with Shiny inputs as input.<id>().
    - id: input id (string)
    - label: label text
    - value: initial hex color (e.g., "#RRGGBB")
    """
    # Input element with our binding class and data-input-id
    el = tags.input(
        {
            "type": "color",
            "class": "py-color-input form-control",
            "id": id,                 # normal id is fine; binding uses it as inputId
            "data-input-id": id,      # explicit for clarity
            "value": value,
            "aria-label": label,
            "style": "width: 90%; height: 30px; padding: 4px; margin-top: 5px; margin-left: 10%",
        }
    )

    if label != "":
        elements = (tags.label({"for": id}, label), el)
    else:
        elements = (el,) 

    return TagList(*elements)

