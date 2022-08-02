import tkinter.ttk as ttk
# from ttkbootstrap.constants import *
# from ttkbootstrap import utility
from tkinter import Toplevel


class ToolTip:
    """A semi-transparent tooltip popup window that shows text when the
    mouse is hovering over the widget and closes when the mouse is no
    longer hovering over the widget. Clicking a mouse button will also
    close the tooltip.

    ![](../assets/tooltip/tooltip.gif)

    Examples:

        ```python
        import ttkbootstrap as ttk
        from ttkbootstrap.constants import *
        from ttkbootstrap.tooltip import ToolTip

        app = ttk.Window()
        b1 = ttk.Button(app, text="default tooltip")
        b1.pack()
        b2 = ttk.Button(app, text="styled tooltip")
        b2.pack()

        # default tooltip
        ToolTip(b1, text="This is the default style")

        # styled tooltip
        ToolTip(b2, text="This is dangerous", bootstyle=(DANGER, INVERSE))

        app.mainloop()
        ```
    """

    def __init__(
        self,
        widget,
        text:str="widget info",
        image=None,
        compound:str='left',
        wraplength:int=None,
        delay:int=250,    # milliseconds
        **kwargs,
    ):
        """
        Parameters:

            widget (Widget):
                The tooltip window will position over this widget when
                hovering.

            text (str):
                The text to display in the tooltip window.

            wraplength (int):
                The width of the tooltip window in screenunits before the
                text is wrapped to the next line. By default, this will be
                a scaled factor of 300.

            **kwargs (Dict):
                Other keyword arguments passed to the `Toplevel` window.
        """
        self.widget = widget
        self.text = text
        self.image = image
        self.compound = compound
        self.wraplength = wraplength #or utility.scale_size(self.widget, 300)
        self.toplevel = None
        self.delay = delay
        self.id = None

        # set keyword arguments
        kwargs["master"] = self.widget
        self.toplevel_kwargs = kwargs

        # event binding
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<Motion>", self.move_tip)
        self.widget.bind("<ButtonPress>", self.leave)

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hide_tip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.delay, self.show_tip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def show_tip(self, *_):
        """Create a show the tooltip window"""
        if self.toplevel:
            return

        self.toplevel = Toplevel(**self.toplevel_kwargs, background='#000000')

        self.toplevel.overrideredirect(True)
        self.toplevel.attributes('-alpha', 0.95)
        x = self.widget.winfo_pointerx() - (100 + (self.image.width() if self.image else 0))
        y = self.widget.winfo_pointery() - (50 + (self.image.height() if self.image else 0))
        self.toplevel.geometry('+%s+%s' % (x, y))

        lbl = ttk.Label(
            master=self.toplevel,
            text=self.text,
            foreground='#000000',
            background='#ffffff', # Pycharm grey = #4b4c4c
            # justify=LEFT,
            image=self.image,
            compound=self.compound,
            cursor=None,
            takefocus=False,
            wraplength=self.wraplength,
            padding=10
        )
        lbl.pack(fill='both', expand=True, padx=1, pady=1)

    def move_tip(self, *_):
        """Move the tooltip window to the current mouse position within the
        widget.
        """
        if self.toplevel:
            x = self.widget.winfo_pointerx() - (100 + (self.image.width() if self.image else 0))
            y = self.widget.winfo_pointery() - (50 + (self.image.height() if self.image else 0))
            self.toplevel.geometry(f"+{x}+{y}")

    def hide_tip(self, *_):
        """Destroy the tooltip window."""
        if self.toplevel:
            self.toplevel.destroy()
            self.toplevel = None