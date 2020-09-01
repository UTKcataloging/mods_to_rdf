from rdflib import Graph
import os


class TurtleTester:
    def __init__(self, filepath: str):
        self.lines = self.__walk_file(filepath)
        self.code_blocks = self.__get_code_blocks()

    @staticmethod
    def __walk_file(filepath):
        with open(filepath, "r") as current_file:
            return [lines for lines in current_file]

    def __get_code_blocks(self):
        code_blocks = []
        i = 0
        for line in self.lines:
            i += 1
            if line.startswith(".. code-block:: turtle"):
                new_block = ""
                code_block_i = i + 1
                try:
                    while (
                        self.lines[code_block_i].startswith("\n")
                        or self.lines[code_block_i].startswith("\t")
                        or self.lines[code_block_i].startswith(" ")
                    ):
                        new_block += self.lines[code_block_i]
                        code_block_i += 1
                except IndexError:
                    pass
                code_blocks.append(new_block)
        return code_blocks

    def test_turtle_blocks(self):
        for block in self.code_blocks:
            Graph().parse(data=block, format="ttl")
        return


if __name__ == "__main__":
    directories_in_doc_source = ("contents", "top_level_elements", "working_docs")
    for directory in directories_in_doc_source:
        for root, dirs, files in os.walk(f'docs/source/{directory}'):
            for name in files:
                if name.endswith('.rst'):
                    x = TurtleTester(f'{root}/{name}')
                    x.test_turtle_blocks()
