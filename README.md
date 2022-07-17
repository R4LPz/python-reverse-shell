# Python Reverse Shell

Estudo sobre uma shell reversa com transferência de arquivos utilizando sockets em python.

**Disclaimer :** Não me responsabilizo ​​por qualquer uso indevido do código fonte aqui presente. Use-o por sua própria responsabilidade.

## Como funciona um shell reverso

O Reverse Shell nada mais é que o ato de executar comandos locais e fazer com que eles sejam executados em uma máquina remota, desta forma todos os comando executados na máquina de um atacante, serão exe

O reverse shell é um programa que tem como finalidade enviar comandos de uma máquina local (atacante) para obter os resultados destes em uma máquina remota (vítima). 

Para obter a conexão, o sistema consiste de dois lados, o servidor que roda na máquina local e espera por conexões das máquinas remotas. E o cliente que se conecta ao servidor e aguarda pelo recebimento de novas instruções para que sejam executadas e respondidas.

Dessa forma, uma vez que estas máquinas estejam conectadas, o lado do servidor permite que o usuário entre com um comando, interpreta e envia esse comando para o cliente. O cliente, uma vez que recebe esta instrução, irá executa-la no shell local (cmd.exe ou bash, por exemplo) e retornar para o servidor os resultados. 

Essa estrutura permite que o usuário execute comandos remotamente e comande a máquina remota silenciosamente.

## Execução

Como exposto no tópico anterior, será necessário executar os dois lados da aplicação. Portanto, primeiramente execute o *server.py* na máquina local com:

```
 $ python server.py <host> <port>
```
Substitua *<host>* e *<port>*, pelo endereço IP e porta, respectivamente. Caso queira mais informações dos comandos, é possível passar o parâmentro *--help*.

Com o servidor em execução, vamos conectar o cliente a ele. Para fazer isso, precisamos executar o *client.py* com o seguinte comando:

```
 $ python client.py <host> <port>
```

Substitua *<host>* e *<port>*, pelo endereço IP e porta, respectivamente.

Existem vários vetores que podem ser explorados e permitirem a execução de um código arbitrário, porém, para testar o código e verificar seu funcionamento, você pode executar o cliente especificando o host local como 127.0.0.1.

A partir do momento em que o cliente se conectar ao servidor, você deverá receber uma mensagem no servidor confirmando que uma máquina foi capturada. Agora basta executar seus comandos e ve-los retornar os valores do cliente ;)

Para realizar alguma transferência de arquivo, basta utilizar o comando **give** seguido do nome do arquivo.

## Fonte

Este código foi baseado nos seguintes artigos:

- https://www.thepythoncode.com/article/create-reverse-shell-python
- https://www.rootinstall.com/tutorial/how-to-setup-a-reverse-shell-in-linux/
