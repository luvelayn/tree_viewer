from gi.repository import Gtk
import json
import os


class TreeViewHelper:
    def __init__(self):
        self.store = Gtk.TreeStore(str, str)

    def load_data_from_json_folder(self, folder_path):
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.json'):
                json_file_path = os.path.join(folder_path, file_name)
                with open(json_file_path, 'r') as file:
                    data = json.load(file)
                    self._fill_treeview(None, {'root': data})

    def _fill_treeview(self, parent, data):
        for key, value in data.items():
            if isinstance(value, dict):
                item = self.store.append(parent, [key, ''])
                self._fill_treeview(item, value)
            elif isinstance(value, list):
                for i, item in enumerate(value, 1):
                    data = {str(i): item}
                    self._fill_treeview(parent, data)
            else:
                self.store.append(parent, [key, str(value)])
