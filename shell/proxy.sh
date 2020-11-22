#!/bin/bash

# My first and most useful shell script
function unsetproxy() {
	unset {http,https,ftp}_proxy
	unset {HTTP,HTTPS,FTP}_proxy
	# erase docker conf and restart service
	echo "" >| ~/.docker/config.json
	systemctl restart docker
	systemctl status docker | head -n 3
}

function dockerconf() {
	cat <<- _EOF_ >| ~/.docker/config.json
	{
	    "proxies":
	    {
	        "default":
	        {
	            "httpProxy": $http_proxy,
	            "httpsProxy": $http_proxy,
	            "ftpProxy": $http_proxy,
	            "noProxy": $no_proxy
	        }
	    }
	}
	_EOF_
}

function setproxy() {
	export {http,https,ftp}_proxy="http://proxy-server:port"
	export {HTTP,HTTPS,FTP}_proxy="http://proxy-server:port"
	export no_proxy="localhost,127.0.0.1,"
	dockerconf
	systemctl restart docker
	systemctl status docker | head -n 3
}