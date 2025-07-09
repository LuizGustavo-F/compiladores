WRITE "Insira um valor para o triangulo de pascal"
READ n
linha = 0
L0:
_t0 = linha < n
IF_FALSE _t0 GOTO L1
j = 0
L2:
_t1 = n - linha
_t2 = _t1 - 1
_t3 = j < _t2
IF_FALSE _t3 GOTO L3
WRITE " "
_t4 = j + 1
j = _t4
GOTO L2
L3:
C = 1
i = 0
L4:
_t5 = i <= linha
IF_FALSE _t5 GOTO L5
WRITE C
_t6 = linha - i
_t7 = C * _t6
_t8 = i + 1
_t9 = _t7 / _t8
C = _t9
_t10 = i + 1
i = _t10
GOTO L4
L5:
WRITE "\n"
_t11 = linha + 1
linha = _t11
GOTO L0
L1:
