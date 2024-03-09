## md 1
print('modulo 1 ')

seguimiento1_modulo1 = float(input('1 nota se seguimiento: '))
seguimiento2_modulo1 = float(input('2 nota se seguimiento: '))
seguimiento3_modulo1 = float(input('3 nota se seguimiento: '))
seguimiento4_modulo1 = float(input('4 nota se seguimiento: '))

seguimiento_def_modulo1 = (seguimiento1_modulo1 + seguimiento2_modulo1 +
                           seguimiento3_modulo1 + seguimiento4_modulo1) / 4

parcial1_modulo1 = float(input('1 nota de parcial: '))
parcial2_modulo1 = float(input('2 nota de parcial: '))
parcial3_modulo1 = float(input('3 nota de parcial: '))

parcial_def_modulo1 = (parcial3_modulo1 + parcial2_modulo1 + parcial3_modulo1) / 3

auto_ev_modulo1 = float(input('nota de auto: '))
coe_ev_modulo1 = float(input('nota de coevaluación: '))

auto_coe_def_modulo1 = (auto_ev_modulo1 + coe_ev_modulo1) / 2

nota_modulo1 = (seguimiento_def_modulo1 * 0.35) + (parcial_def_modulo1 * 0.6) + (auto_coe_def_modulo1 * 0.05)

## md 2
print('modulo 2 ')

seguimiento1_modulo2 = float(input('1 nota se seguimiento: '))
seguimiento2_modulo2 = float(input('2 nota se seguimiento: '))
seguimiento3_modulo2 = float(input('3 nota se seguimiento: '))
seguimiento4_modulo2 = float(input('4 nota se seguimiento: '))

seguimiento_def_modulo2 = (seguimiento1_modulo2 + seguimiento2_modulo2 +
                           seguimiento3_modulo2 + seguimiento4_modulo2) / 4

parcial1_modulo2 = float(input('1 nota de parcial: '))
parcial2_modulo2 = float(input('2 nota de parcial: '))
parcial3_modulo2 = float(input('3 nota de parcial: '))

parcial_def_modulo2 = (parcial3_modulo2 + parcial2_modulo2 + parcial3_modulo2) / 3

auto_ev_modulo2 = float(input('nota de auto: '))
coe_ev_modulo2 = float(input('nota de coevaluación: '))

auto_coe_def_modulo2 = (auto_ev_modulo2 + coe_ev_modulo2) / 2

nota_modulo2 = (seguimiento_def_modulo2 * 0.35) + (parcial_def_modulo2 * 0.6) + (auto_coe_def_modulo2 * 0.05)

## md 3
print('modulo 3 ')

seguimiento1_modulo3 = float(input('1 nota se seguimiento: '))
seguimiento2_modulo3 = float(input('2 nota se seguimiento: '))
seguimiento3_modulo3 = float(input('3 nota se seguimiento: '))
seguimiento4_modulo3 = float(input('4 nota se seguimiento: '))

seguimiento_def_modulo3 = (seguimiento1_modulo3 + seguimiento2_modulo3 +
                           seguimiento3_modulo3 + seguimiento4_modulo3) / 4

parcial1_modulo3 = float(input('1 nota de parcial: '))
parcial2_modulo3 = float(input('2 nota de parcial: '))
parcial3_modulo3 = float(input('3 nota de parcial: '))

parcial_def_modulo3 = (parcial3_modulo3 + parcial2_modulo3 + parcial3_modulo3) / 3

auto_ev_modulo3 = float(input('nota de auto: '))
coe_ev_modulo3 = float(input('nota de coevaluación: '))

auto_coe_def_modulo3 = (auto_ev_modulo3 + coe_ev_modulo3) / 2

nota_modulo3 = (seguimiento_def_modulo3 * 0.35) + (parcial_def_modulo3 * 0.6) + (auto_coe_def_modulo3 * 0.05)

nota_de_la_materia = (nota_modulo1 + nota_modulo3 + nota_modulo3) / 3
rounded = round(nota_de_la_materia)

if rounded < 3:
    print(f'perdió con {rounded}')
else:
    print(f'ganó con {rounded}')
