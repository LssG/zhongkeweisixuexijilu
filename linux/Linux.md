# Linux

## 登录方式
命令行登录  
ssh登录  
> 默认ssh服务端口号为 22  
> > 常见默认服务端口号  
> > > SSH 服务器  
> > > 22  
> > > Web 服务器  
> > > 80  
> > > HTTPS  
> > > 443  
> > > FTP 服务器  
> > > 21  
> 
> ```
> ssh [-p port] user@remote  
> ```
> > user 是在远程机器上的用户名，如果不指定的话默认为当前用户  
> > remote 是远程机器的地址，可以是 IP／域名，或者是 后面会提到的别名  
> > port 是 SSH Server 监听的端口，如果不指定，就为默认值 22  
>
> 启动ssh服务  
> > 安装ufw防火墙工具 开启22端口号  
> > 进入etc/ssh   ssh_config解除端口号的注释  
> > 安装openssh-server service ssh start(/etc/init.d/ssh start)    

图形界面登录