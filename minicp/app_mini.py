from shiny.express import ui, render, input
from shiny import reactive
from components import color_input

ui.page_opts(title="Mini color picker (Shinylive)", fillable=True)

# Load the binding once from the app's www folder (relative path; works on GitHub Pages)
ui.head_content(
    ui.tags.script(src="color_binding.js?v=3")  # bump v= to bust caches if you edit the file
)

with ui.sidebar(open="open"):
    ui.h3("Pick a color", class_="mb-2")
    color_input("accent", "Accent color", value="#1E90FF")

with ui.card():
    ui.h3("Live preview")
    @render.ui
    def swatch():
        color = input.accent() or "#1E90FF"
        return ui.div({
            "style": f"width:180px;height:100px;border:1px solid #ccc;border-radius:8px;background:{color};"
        })

with ui.card():
    @render.text
    def show_value():
        return f"Current color: {input.accent() or '(none)'}"

# Optional: demonstrate reacting to changes as an event (skip initial run)
@reactive.effect
@reactive.event(input.accent, ignore_init=True)
def _on_change():
    print("Color changed to", input.accent())