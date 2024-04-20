from gi.repository import Gtk
from .treeViewHelper import TreeViewHelper


class Confirmation(Gtk.MessageDialog):
    def __init__(self):
        Gtk.MessageDialog.__init__(self)
        self.set_markup('<b>Вы уверены, что хотите выйти?</b>')
        self.add_button('Да', 1)
        self.add_button('Нет', 0)


class TreeTab(Gtk.Box):
    def __init__(self, app):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)

        treeview_helper = TreeViewHelper()
        treeview_helper.load_data_from_json_folder('./tree_viewer/dataset')
        treeview = Gtk.TreeView(model=treeview_helper.store)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Переменная", renderer, text=0)
        treeview.append_column(column)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Значение", renderer, text=1)
        treeview.append_column(column)

        sw = Gtk.ScrolledWindow()
        sw.set_child(treeview)

        sw.set_size_request(1300, 800)

        self.append(sw)


class Window(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        Gtk.ApplicationWindow.__init__(self, *args, **kwargs)

        self.app = kwargs['application']
        self.connect('close-request', self.handle_exit)

        tree_tab = TreeTab(self.app)
        self.set_child(tree_tab)

    def handle_exit(self, _):
        dialog = Confirmation()
        dialog.set_transient_for(self)
        dialog.show()
        dialog.connect('response', self.exit)
        return True

    def exit(self, widget, response):
        if response == 1:
            self.app.quit()
        widget.destroy()
