
from parsimonious.grammar import Grammar
from visitor import ProductVisitor



#~r"^.+?(?=\d+)"

grammar = Grammar(
    r"""
    sentence         = (name class? value_unit_attr+)*
    name             = ~r"^.+?(?=\d+)"
    class            = ~r"\d+#\s+"
    value_unit_attr  = (value_unit attr) / value_unit
    value_unit       = (value unit) / value
    value            = fraction / number
    attr             = ~r"[a-zA-Z\s,]+"
    unit             = (symbol / word)
    word             = ~r"[^\s]+"
    symbol           = ~r"['\"]"
    number           = ~r"\d+\s*"
    fraction         = ~r"[0-9]*[-]*[0-9]+\/[0-9]+\s*"
    """
)


data1 = """PIPE FLANGE FORGED STEEL SLIP-ON WELD 150# 1/2" DIAM
"""
data2 = """PIPE FLANGE FS SLIP ON WELD 300LB 1-1/4" PIPE DIAM
"""
data3 = """PIPE FLANGE WELD NECK 150LB 1" PIPE DIAM
"""
data4 = """VALVES BRONZE BALL 125 LB SOLDER, 3/8" DIAM
"""

datarr = [data1, data2, data3, data4]

for data in datarr:
    tree = grammar.parse(data)

    pv = ProductVisitor()
    output = pv.visit(tree)
    print(data)
    print(output)
    print("\n")
