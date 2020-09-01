from rdflib import Graph

lines = []
code_blocks = []
with open('docs/source/contents/4_draft_mapping.rst', 'r') as draft:
    for line in draft:
        lines.append(line)

i = 0
for line in lines:
    i += 1
    if line.startswith('.. code-block:: turtle'):
        new_block = ""
        #print(f'New block on line {i}')
        code_block_i = i + 1
        try:
            while lines[code_block_i].startswith("\n") or lines[code_block_i].startswith("\t") or lines[code_block_i].startswith(" "):
                # print(f'{code_block_i}: {lines[code_block_i]}')
                new_block += lines[code_block_i]
                code_block_i += 1
        except IndexError:
            pass
        code_blocks.append(new_block)
for block in code_blocks:
    Graph().parse(data=block, format="ttl")