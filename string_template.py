__author__ = 'jszheng'

from string import Template

t1 = """
digraph G {
  ranksep=.25;
  edge [arrowsize=.5]
  node [shape=circle, fontname="ArialNarrow",
        fontsize=12, fixedsize=true, height=.45];

  $func_list
  $edge_list
}
"""

funcs = "main; fact; a; b; c; d; e;"
edges = """
  a -> b;
  c -> d;
"""

s = Template(t1)
# 也可以用
#output = s.substitute(vars())
print(vars())
output = s.substitute(func_list=funcs, edge_list=edges)
print(output)