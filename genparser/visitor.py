
from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

class ProductVisitor(NodeVisitor):
    def visit_sentence(self, node, visited_children):
        """ Returns the overall output. """
        output = {}
        output.update(visited_children[0][0])     #name
        if(isinstance(visited_children[0][1], list)):
            output.update(visited_children[0][1][0])  #class
        output.update({'attrs': []})
        for child in visited_children[0][2]:
            output['attrs'].append(child)  #value unit attr
        return output

    def visit_name(self, node, visited_children):
        name = node.text
        return {'name' : name }
    
    def visit_class(self, node, visited_children):
        name =  node.text
        return {'class' : name }
    
    def visit_value_unit_attr(self, node, visited_children):
        output = {'value_unit_attr':{}}
        output['value_unit_attr'].update(visited_children[0][0])     #value unit
        output['value_unit_attr'].update(visited_children[0][1])  #attr
        return output
    
    def visit_value_unit(self, node, visited_children):
        output = {'value_unit':{}}
        output['value_unit'].update(visited_children[0][0])  #value
        output['value_unit'].update(visited_children[0][1])  #unit
        return output
        
    def visit_value(self, node, visited_children):
        val = node.text
        return {'value': val}


    def visit_unit(self, node, visited_children):
        unit = node.text
        return {'unit': unit}


    def visit_attr(self, node, visited_children):
        attr = node.text
        return {'attr': attr}

    def generic_visit(self, node, visited_children):
        """ The generic visit method. """
        return visited_children or node