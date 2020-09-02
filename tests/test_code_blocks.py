from rdflib import Graph
import os
import sys


class TurtleTester:
    def __init__(self, filepath: str):
        self.filename = filepath
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
                        if ":caption:" not in self.lines[code_block_i] and ":name:" not in self.lines[code_block_i]:
                            new_block += self.lines[code_block_i]
                        if self.lines[code_block_i].strip().lower().startswith("prefix"):
                            raise Exception(f'SPARQL syntax prefix detected in {self.filename} on line {code_block_i + 1}.')
                        code_block_i += 1
                except IndexError:
                    pass
                code_blocks.append(new_block)
        return code_blocks

    def test_turtle_blocks(self):
        for block in self.code_blocks:
            try:
                Graph().parse(data=block, format="ttl")
            except:
                print(f"Problem in {self.filename} with this block: {block}.\nThe problem is: {sys.exc_info()[0]}\n\n\n")
                raise
        return


if __name__ == "__main__":
    directories_in_doc_source = ("contents", "top_level_elements")
    for directory in directories_in_doc_source:
        for root, dirs, files in os.walk(f'docs/source/{directory}'):
            for name in files:
                if name.endswith('.rst'):
                    x = TurtleTester(f'{root}/{name}')
                    x.test_turtle_blocks()
