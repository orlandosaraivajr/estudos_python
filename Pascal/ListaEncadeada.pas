program ListaEncadeada;

type
  // Definição do nó da lista encadeada
  PNo = ^TNo;
  TNo = record
    Dado: integer;
    Proximo: PNo;
  end;

// Função para adicionar um novo elemento no final da lista
procedure AdicionarElemento(var inicio: PNo; valor: integer);
var
  novoNo, atual: PNo;
begin
  New(novoNo);
  novoNo^.Dado := valor;
  novoNo^.Proximo := nil;

  if inicio = nil then
    inicio := novoNo
  else
  begin
    atual := inicio;
    while atual^.Proximo <> nil do
      atual := atual^.Proximo;
    atual^.Proximo := novoNo;
  end;
end;

// Procedimento para imprimir a lista encadeada
procedure ImprimirLista(inicio: PNo);
var
  atual: PNo;
begin
  atual := inicio;
  while atual <> nil do
  begin
    Write(atual^.Dado, ' ');
    atual := atual^.Proximo;
  end;
  WriteLn;
end;

// Procedimento principal
var
  inicio: PNo;  
begin
  inicio := nil;

  // Adicionando elementos na lista encadeada
  AdicionarElemento(inicio, 1);
  AdicionarElemento(inicio, 2);
  AdicionarElemento(inicio, 3);
  AdicionarElemento(inicio, 4);
  AdicionarElemento(inicio, 5);

  // Imprimindo a lista encadeada
  Write('Lista Encadeada: ');
  ImprimirLista(inicio);
end.

