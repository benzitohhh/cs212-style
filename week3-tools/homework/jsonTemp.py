object => {} | { members }
members => pair | pair , members
pair => string : value
array => [] | [ elements ]
elements => value  | value , elements
value => string | number | object | array | true | false | null
string => "" | " chars "
chars => char | char chars
char => [^\"\\\/\b\f\n\r\t\u]
number => int | int frac | int exp | int frac exp
int => digit | digit1-9 digits | - digit | - digit1-9 digits
frac => . digits
exp => e digits
digits => digit | digit digits
e => e | e+ | e- | E | E+ | E-
digit => [0-9]
digit1-9 => [1-9]