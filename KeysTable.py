from tkinter.ttk import Treeview, Frame, Scrollbar, Entry, Button, Label, Combobox, LabelFrame
from tkinter import StringVar
from Keys import KD
from tooltip import ToolTip


def Key_table(**kwargs):
    results = []
    up_position = 0
    down_position = -1

    main_frame = LabelFrame(**kwargs, text='Keyboard keys')
    # main_frame.pack(fill='both', expand=True)

    search_frame = Frame(main_frame)
    search_frame.pack(side='top', fill='both')

    found_lbl = Label(search_frame)
    found_lbl.pack(side='right', fill='x')

    def Down():
        global down_position
        if results:
            try:
                keys_table.see(results[down_position])
                keys_table.focus(results[down_position])
                down_position -= 1
            except IndexError:
                pass
    search_down = Button(search_frame, text='down', takefocus=False, cursor='hand2', command=lambda :Down())
    search_down.pack(side='right', fill='x')
    def Up():
        global up_position
        if results:
            try:
                keys_table.see(results[up_position])
                keys_table.focus(results[up_position])
                up_position += 1
            except IndexError:
                pass
    search_up = Button(search_frame, text='up', takefocus=False, cursor='hand2', command=lambda :Up())
    search_up.pack(side='right', fill='x')

    search_entry = Entry(search_frame, takefocus=False)
    search_entry.pack(side='left', fill='x', expand=True, padx=5, pady=5)
    def Search():
        global up_position
        global down_position
        if search_entry.get():
            up_position = 0
            down_position = -1
            results.clear()
            for id in keys_table.get_children():
                # print(keys_table.item(id)['values'][0])
                if str(search_entry.get()) in str(keys_table.item(id)['values'][0]):
                    keys_table.item(id, tags='found')
                    results.append(id)
            if results:
                found_lbl.config(text=len(results))
                keys_table.see(results[0])
                keys_table.focus(results[0])
                # keys_table.tag_bind('found')
                keys_table.tag_configure('found', background='green')
            else:
                found_lbl.config(text='')
                for id in keys_table.get_children():
                    keys_table.item(id, tags=())
        else:
            found_lbl.config(text='')
            for id in keys_table.get_children():
                keys_table.item(id, tags=())

    search_entry.bind('<KeyPress>', lambda a:Search())
    search_entry.bind('<KeyRelease>', lambda a:Search())

    # Table_side = Combobox(main_frame, values=('top','bottom', 'right', 'left'), textvariable=sideVar, state='readonly')
    # ToolTip(Table_side, "Side of the keys table")
    # Table_side.bind('<<ComboboxSelected>>', lambda a:onChange_execute())
    # Table_side.pack(side='bottom', anchor='w', )

    selection_information_lbl = Label(main_frame, text='No selection set.')
    selection_information_lbl.pack(side='bottom', fill='x')

    V = Scrollbar(main_frame, orient='vertical')
    V.pack(side='right', fill='y')
    H = Scrollbar(main_frame, orient='horizontal')
    H.pack(side='bottom', fill='x')

    keys_table = Treeview(main_frame, show='tree', selectmode='browse', columns=('keyboard',), xscrollcommand=H.set, yscrollcommand=V.set, padding=0, takefocus=True)
    def selection_information():
        if keys_table.selection():
            selection_information_lbl.config(text=f"{keys_table.item(keys_table.selection()[0])['values'][0]}")
    keys_table.bind('<<TreeviewSelect>>', lambda a:selection_information())
    H.config(command=keys_table.xview)
    V.config(command=keys_table.yview)
    keys_table.pack(side='bottom', fill='both', expand=True)

    for key in KD.keyboard_keys:
        if KD.isKey(key):
            key = str(key.encode())[2:-1]
            key_cell = keys_table.insert('', 'end', values=(key,))
            button = KD.button(key)
            button_cell = keys_table.insert(key_cell, 'end', values=('Button',))
            keys_table.insert(button_cell, 'end', values=(button,))
            description = KD.description(key)
            description_cell = keys_table.insert(key_cell, 'end', values=('Description',))
            keys_table.insert(description_cell, 'end', values=(description,))
            type = KD.type(key)
            type_cell = keys_table.insert(key_cell, 'end', values=('Type',))
            keys_table.insert(type_cell, 'end', values=(type,))

    return main_frame