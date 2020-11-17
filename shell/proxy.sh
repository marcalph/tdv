#!/bin/bash

# My first script
function unsetproxy() {
    unset {http,https,ftp}_proxy
    unset {HTTP,HTTPS,FTP}_proxy
}

function setproxy() {
    export {http,https,ftp}_proxy="http://proxy-server:port"
    export {HTTP,HTTPS,FTP}_proxy="http://proxy-server:port"
}
