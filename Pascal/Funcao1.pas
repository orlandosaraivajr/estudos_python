program ResolverEquacao;

uses
  Math;

// Função para resolver a equação
function ResolverEquacao(X, A, B, C: real): real;
begin
  ResolverEquacao := X + Sin(A + B + C);
end;

var
  X, A, B, C, resultado: real;
begin
  Write('Digite o valor de X: ');
  ReadLn(X);
  Write('Digite o valor de A: ');
  ReadLn(A);
  Write('Digite o valor de B: ');
  ReadLn(B);
  Write('Digite o valor de C: ');
  ReadLn(C);

  resultado := ResolverEquacao(X, A, B, C);

  WriteLn('O resultado da equacao é: ', resultado:0:2);
end.
