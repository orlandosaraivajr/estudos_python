program PilhaExemplo;

type
  // Definição do nó da pilha
  PNoh = ^TNoh;
  TNoh = record
    Dado: integer;
    Proximo: PNoh;
  end;

// Tipo de dados para representar a pilha
Pilha = record
  Topo: PNoh;
end;

// Procedimento para inicializar a pilha
procedure Inicializar(var p: Pilha);
begin
  p.Topo := nil;
end;

// Função para verificar se a pilha está vazia
function PilhaVazia(p: Pilha): boolean;
begin
  PilhaVazia := (p.Topo = nil);
end;

// Procedimento para empilhar um elemento na pilha
procedure Empilhar(var p: Pilha; valor: integer);
var
  novoNo: PNoh;
begin
  New(novoNo);
  novoNo^.Dado := valor;
  novoNo^.Proximo := p.Topo;
  p.Topo := novoNo;
end;

// Procedimento para desempilhar um elemento da pilha
procedure Desempilhar(var p: Pilha);
var
  temp: PNoh;
begin
  if PilhaVazia(p) then
  begin
    WriteLn('Erro: Pilha vazia');
    Halt;
  end;
  
  temp := p.Topo;
  WriteLn('Desempilhou: ', temp^.Dado);
  p.Topo := temp^.Proximo;
  Dispose(temp);
end;

// Procedimento para imprimir os elementos da pilha
procedure ImprimirPilha(p: Pilha);
var
  atual: PNoh;
begin
  atual := p.Topo;
  Write('Pilha: ');
  while atual <> nil do
  begin
    Write(atual^.Dado, ' ');
    atual := atual^.Proximo;
  end;
  WriteLn;
end;

// Procedimento principal
var
  minhaPilha: Pilha;
begin
  Inicializar(minhaPilha);

  // Empilhando elementos na pilha
  Empilhar(minhaPilha, 1);
  Empilhar(minhaPilha, 2);
  Empilhar(minhaPilha, 3);
  Empilhar(minhaPilha, 4);
  Empilhar(minhaPilha, 5);

  // Imprimindo a pilha
  ImprimirPilha(minhaPilha);

  // Desempilhando elementos
  WriteLn('Desempilhando elementos:');
  while not PilhaVazia(minhaPilha) do
  begin
    Desempilhar(minhaPilha);
  end;
end.
