import streamlit as st
from streamlit_ace import st_ace
import pandas as pd
# from streamlit_metrics import metric, metric_row
# import numpy as np
# import altair as alt
# import cufflinks as cf

st.set_page_config(page_title='StreamlitPython.com Livecode 1 Column', page_icon=':memo:', layout='wide', initial_sidebar_state='collapsed')
st.sidebar.title(":memo: Editor Settings")

THEMES = [
  "ambiance", "chaos", "chrome", "clouds", "clouds_midnight", "cobalt", "crimson_editor", "dawn",
  "dracula", "dreamweaver", "eclipse", "github", "gob", "gruvbox", "idle_fingers", "iplastic",
  "katzenmilch", "kr_theme", "kuroir", "merbivore", "merbivore_soft", "mono_industrial", "monokai",
  "nord_dark", "pastel_on_dark", "solarized_dark", "solarized_light", "sqlserver", "terminal",
  "textmate", "tomorrow", "tomorrow_night", "tomorrow_night_blue", "tomorrow_night_bright",
  "tomorrow_night_eighties", "twilight", "vibrant_ink", "xcode"
]
KEYBINDINGS = ["emacs", "sublime", "vim", "vscode"]

# editor, display = st.columns((3, 2))

# with editor:
code = st_ace(
  value="""st.write('Hello')""",
  language="python",
  placeholder="st.write('Hello world')",
  theme=st.sidebar.selectbox("Theme", options=THEMES, index=6),
  keybinding=st.sidebar.selectbox("Keybinding mode", options=KEYBINDINGS, index=3),
  font_size=st.sidebar.slider("Font size", 5, 24, 14),
  tab_size=st.sidebar.slider("Tab size", 1, 8, 2),
  wrap=st.sidebar.checkbox("Wrap lines", value=False),
  show_gutter=False,
  show_print_margin=False,
  auto_update=False,
  readonly=False,
  key="ace-editor"
)

# with display:
exec(code)

with st.sidebar:
  pass
