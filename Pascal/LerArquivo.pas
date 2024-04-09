program LerArquivo;

var
  arquivo: text;
  linha: string;

begin
  // Abrindo o arquivo para leitura
  Assign(arquivo, 'dados.txt');
  Reset(arquivo);

  // Exibindo o conteúdo do arquivo na tela
  WriteLn('Conteudo do arquivo:');
  while not Eof(arquivo) do
  begin
    ReadLn(arquivo, linha);
    WriteLn(linha);
  end;

  // Fechando o arquivo de leitura
  Close(arquivo);
end.
