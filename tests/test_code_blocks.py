from rdflib import Graph
import os
import sys


class TurtleTester:
    def __init__(self, filepath: str):
        self.filename = filepath
        self.exceptions = []
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
                        if (
                            ":caption:" not in self.lines[code_block_i]
                            and ":name:" not in self.lines[code_block_i]
                        ):
                            new_block += self.lines[code_block_i]
                        if (
                            self.lines[code_block_i]
                            .strip()
                            .lower()
                            .startswith("prefix")
                        ):
                            self.exceptions.append(
                                f"SPARQL syntax prefix detected in {self.filename} on line {code_block_i + 1}."
                            )
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
                self.exceptions.append(
                    f"Problem in {self.filename} with this block:\n\n {block}\n"
                    f"\tThe problem as reported by rdflib is: {sys.exc_info()[0]}\n\n\n"
                )
        return


if __name__ == "__main__":
    all_exceptions = []
    bad_files = 0
    print("Testing turtle code blocks.\n")
    directories_in_doc_source = ("contents", "top_level_elements")
    for directory in directories_in_doc_source:
        for root, dirs, files in os.walk(f"docs/source/{directory}"):
            for name in files:
                if name.endswith(".rst"):
                    x = TurtleTester(f"{root}/{name}")
                    x.test_turtle_blocks()
                    if len(x.exceptions) == 0:
                        print(f"\tAll turtle code blocks in {x.filename} pass.")
                    else:
                        print(f"\tFAILURES: {len(x.exceptions)} in {x.filename}:")
                        bad_files += 1
                        for exception in x.exceptions:
                            print(f"\n\t{exception}")
                            all_exceptions.append(exception)
    if len(all_exceptions) == 0:
        print("\nTurtle code blocks in all directories have passed.")
    else:
        raise Exception(f"\n\n{len(all_exceptions)} FAILURES in {bad_files} files.")
