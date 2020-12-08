import os
from Folder import Folder
from pathlib import Path
import ntpath

"""djikstra algo"""
class Search(object):
    def dfs_method(self, start_path, parent_folder, indents, root_contents):
        path = start_path
        parent_f = path.parent
        if os.path.isdir(path):
            if indents <= 1:
                for ind in range(0, indents):
                    print("    ", end = '')
                print("(dir) "+ntpath.basename(path))
            indents += 1
            """print(os.listdir(path))"""
            fold = Folder(path)
            try:
                content_list = os.listdir(path)
            except:
                content_list = []
                pass
            for file in content_list:
                self.dfs_method(Path(os.path.join(path, file)), fold, indents, root_contents)

            parent_folder.size += fold.size
            if ntpath.basename(path) in root_contents:
                for ind in range(0, indents):
                    print("    ", end = '')
                print("FOLDER SIZE - "+str(fold.size)+"MB")
            indents -= 1
        else:
            try:
                parent_folder.size += os.path.getsize(path)/1000000.0
            except:
                pass
            """
            for ind in range(0, indents):
                print("    ", end = '')
            print(ntpath.basename(path)+" - "+str(os.path.getsize(path)/1000000.0)+"MB")
            """
        
        return
