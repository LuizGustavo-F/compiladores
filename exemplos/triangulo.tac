READ a
READ b
READ c
_t0 = a > 0
_t1 = b > 0
_t2 = _t0 && _t1
IF_FALSE _t2 GOTO L0
_t3 = a + b
_t4 = _t3 > c
_t5 = a + c
_t6 = _t5 > b
_t7 = _t4 && _t6
IF_FALSE _t7 GOTO L2
_t8 = a == b
_t9 = b == c
_t10 = _t8 && _t9
IF_FALSE _t10 GOTO L4
WRITE "Triângulo equilátero válido"
GOTO L5
L4:
_t11 = a == b
_t12 = a == c
_t13 = _t11 || _t12
IF_FALSE _t13 GOTO L6
WRITE "Triângulo isósceles válido"
GOTO L7
L6:
WRITE "Triângulo escaleno válido"
L7:
L5:
GOTO L3
L2:
WRITE "Medidas inválidas"
L3:
GOTO L1
L0:
WRITE "Erro: valores negativos ou zero não são permitidos"
L1:
