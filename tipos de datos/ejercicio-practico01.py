otros_cursos_min = 2.5

otros_cursos_max = 7

otros_cursos_promedio = 4

dalto_cursos = 1.5

diferencia_min = 100 - ( dalto_cursos / otros_cursos_min * 100 )
diferencia_max = 100 - dalto_cursos * 1000 // otros_cursos_max / 10
diferencia_promedio = 100 - ( dalto_cursos / otros_cursos_promedio * 100 )

print(f'El curso de Dalto dura un {diferencia_min}% menos que el mas rapido')
print(f'El curso de Dalto dura un {diferencia_max}% menos que el mas lento')
print(f'El curso de Dalto dura un {diferencia_promedio}% menos que el promedio')

