import marimo

__generated_with = "0.8.18"
app = marimo.App(width="medium")


@app.cell
def __(ui):
    ui.slider()
    return


if __name__ == "__main__":
    app.run()
