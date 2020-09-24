#!/usr/bin/env python3


def generate(rule):
    sizes = {
        'default': {
            'vert': 0.9375,
            'hor': 0.9375,
        },
        'sm': {
            'vert': 0.625,
            'hor': 0.625,
        },
        'xs': {
            'vert': 0.3125,
            'hor': 0.3125,
        }
    }

    orientations = ['top', 'right', 'bottom', 'left']
    output = f''
    # iterate over sizes
    for key, value in sizes.items():
        output += f'@mixin {rule}-{key}'
        output += ' {\n'
        output += f"  {rule}: {value['vert']}rem {value['hor']}rem {value['vert']}rem {value['hor']}rem;\n"
        output += '}\n\n'
        for index, orientation in enumerate(orientations):
            if orientation == 'top':
                # vertical
                output += f'@mixin {rule}-vertical-{key}'
                output += ' {\n'
                output += f"  {rule}-top: {value['vert']}rem;"
                output += '\n'
                output += f"  {rule}-bottom: {value['vert']}rem;"
                output += '}\n\n'
            if orientation == 'left':
                # vertical
                output += f'@mixin {rule}-horizontal-{key}'
                output += ' {\n'
                output += f"  {rule}-left: {value['hor']}rem;"
                output += '\n'
                output += f"  {rule}-right: {value['hor']}rem;"
                output += '}\n\n'
            output += f'@mixin {rule}-{orientation}-{key}'
            output += ' {\n'
            output += f"  {rule}-{orientation}: "
            output += (str(value['vert']) if index %
                       2 == 0 else str(value['hor'])) + 'rem;\n'
            output += '}\n\n'

    return output


print(generate('margin'))
print(generate('padding'))
