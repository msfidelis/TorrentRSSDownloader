# TorrentRSSDownloader
Script/Daemon que eu fiz em Python para baixar todos os novos episódios de Game of Thrones por Torrent. Mas na verdade você pode utilizar em qualquer série ;) #NãoSouResponsávelPeloUsoDessaParada

Mais RSS: https://showrss.info/?cs=feeds

# Dependências 

* python-libtorrent 0.16.18.0

```
  # sudo apt-get build-dep python-libtorrent
``` 

Ou compile a source: https://coderwall.com/p/muvnow/installing-libtorrent-on-linux

* feedparser s

```
  # sudo pip install feedparser
```

# Instalando o projeto 

```
  # git clone https://github.com/msfidelis/TorrentRSSDownloader.git
```

# Observações:
Criei o projeto inicialmente para ser uma especie de Daemon no sistema, para que ele ficasse rodando em background em um servidor caseiro que eu tenho aqui em casa, lendo o feed de hora em hora para ver se existem novos itens.
Existem muitas formas de fazer isso, lá vai:

# Modo 1 :: Colocando o script na inicialização do sistema

Meu servidor caseiro é um Debian 8 Jessie, então é só adicionar a chamada para o script dentro do rc.local do sistema, como: 

```
  # echo 'python /home/matheus/TorrentRSSDownloader/Torrent-Downloader.py & ' >> /etc/rc.local
```

Customize o caminho para o arquivo e já era. Muita atenção aqui...

# Modo 2 :: Criar uma Screen no Servidor 

Há alguns dias antes desse script, postei lá o meu blog um manual de uso do comando Screen do Linux. Fiquem a vontade para ler e entender melhor:

Link: http://www.nanoshots.com.br/2016/05/screen-dicas-de-administracao-de-varios.html


Mais uma vez:

# Não me responsabilizo pelo mau uso da ferramenta. 
