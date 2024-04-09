program CalculadoraRaizQuadrada;

var
  numero, raiz: real;

begin
  // Solicita ao usuário que insira o número
  writeln('Digite um numero para calcular sua raiz quadrada: ');
  readln(numero);

  // Calcula a raiz quadrada
  if numero >= 0 then
  begin
    raiz := sqrt(numero);
    writeln('A raiz quadrada de ', numero:0:2, ' eh ', raiz:0:2);
  end
  else
  begin
    writeln('Erro: Nao e possivel calcular a raiz quadrada de um numero negativo.');
  end;
end.
