import os
import sys
from pathlib import Path


class Directoy_Tree():
    filename_prefix_middle = '├──'
    filename_prefix_last = '└──'
    parent_prefix_middle = '    '
    parent_prefix_last = '│   '

    def __init__(self, path, parent, is_last):
        self.path = Path(str(path))
        self.parent = parent
        self.is_last = is_last
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0
    @classmethod
    def set_root(self, hint="Input Path:"):
        """ input path."""
        """Vaild path"""

        while True:
            path = Path(input(hint))
            #path = Path(filedialog.askdirectory())
            if path.exists():
                return path
            print("The Path is not exist.")
            
    @property
    def display_name(self):
        """ display the dir or file name"""
        
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    @classmethod
    def make_tree(self, root, parent=None, is_last=False):
        """ Make a new Tree."""
        
        root = Path(str(root))
        displayable_root = self(root, parent, is_last)
        yield displayable_root

        children = sorted(list(path for path in root.iterdir()),
                          key=lambda s: str(s).lower())
        count = 1
        for path in children:
            is_last = count == len(children)
            if path.is_dir():
                yield from self.make_tree(path,
                                          parent=displayable_root,
                                          is_last=is_last)
            else:
                yield self(path, displayable_root, is_last)
            count += 1

    def display(self):
        """ display tree"""
        if self.parent is None:
            return self.display_name

        prefix = (self.filename_prefix_last
                  if self.is_last
                  else self.filename_prefix_middle)

        parts = ["{!s} {!s}".format(prefix,
                                    self.display_name)]
        parent = self.parent
        while parent and parent.parent is not None:
            parts.append(self.parent_prefix_middle
                         if parent.is_last
                         else self.parent_prefix_last)
            parent = parent.parent

        return ''.join(reversed(parts))

if __name__ == "__main__":
    paths = Directoy_Tree.make_tree(Directoy_Tree.set_root())
    for path in paths:
        print(path.display())
