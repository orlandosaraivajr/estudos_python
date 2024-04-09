program ArquivoExemplo;

var
  arquivo: text;
  linha: string;

begin
  // Abrindo o arquivo para gravação
  Assign(arquivo, 'dados.txt');
  Rewrite(arquivo);

  // Solicitando ao usuário para inserir algumas linhas de texto
  WriteLn('Digite algumas linhas de texto (digite "." para encerrar):');
  repeat
    ReadLn(linha);
    if linha <> '.' then
      WriteLn(arquivo, linha); // Gravando a linha no arquivo
  until linha = '.';

  // Fechando o arquivo de gravação
  Close(arquivo);

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
