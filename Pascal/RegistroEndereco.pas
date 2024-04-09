program RegistrosEndereco;

type
  // Definição do registro Endereco
  Endereco = record
    Rua: string[25];
    Bairro: string[25];
    Numero: integer;
  end;

  // Definição do registro Pessoa
  Pessoa = record
    ID: integer;
    Nome: string;
    Endereco: Endereco;
  end;


// Função para preencher os dados da pessoa
function PreencherDadosPessoa: Pessoa;
  // Declaração de uma variável do tipo Pessoa
  var 
    p: Pessoa;
begin
  // Preenchendo os dados da pessoa
  p.ID := 1;
  p.Nome := 'João';
  p.Endereco.Rua := 'Rua A';
  p.Endereco.Bairro := 'Centro';
  p.Endereco.Numero := 123;

  // Retornando a pessoa com os dados preenchidos
  PreencherDadosPessoa := p;
end;

procedure ExibirDadosPessoa(p: Pessoa);
begin
  WriteLn('Dados da Pessoa:');
  WriteLn('ID: ', p.ID);
  WriteLn('Nome: ', p.Nome);
  WriteLn('Endereco:');
  WriteLn('  Rua: ', p.Endereco.Rua);
  WriteLn('  Bairro: ', p.Endereco.Bairro);
  WriteLn('  Numero: ', p.Endereco.Numero);
end;

var
  // Declaração de uma variável do tipo Pessoa
  pessoa1: Pessoa;
  pessoa2: Pessoa;

begin
  pessoa1 := PreencherDadosPessoa;

  pessoa2.ID := 2;
  pessoa2.Nome := 'Maria';
  pessoa2.Endereco.Rua := 'Rua B';
  pessoa2.Endereco.Bairro := 'Centro';
  pessoa2.Endereco.Numero := 123;


    ExibirDadosPessoa(pessoa1);
    ExibirDadosPessoa(pessoa2);
end.

