import draw

# essa desgraça não funciona

def main():
    # the master object, you may subclass it in order to
    # organize your gui
    master = draw.Master()
    
    # the DrawAreaInterface-subclass object that will
    # do the drawing-operations
    area = draw.C4dDrawArea(master)
    area.minSize = 200, 130
    
    # the c4d-dialog that shows the drawarea
    dlg = draw.C4dDrawArea('A simple gray field.', area)
    dlg.open()

main()
    
# versão 5.3 do lua