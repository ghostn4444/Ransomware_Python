
# 🛡️ Educational Ransomware Simulator (Python)

### ⚠️ Disclaimer

Este projeto é um **simulador educacional de ransomware**.

Ele foi criado exclusivamente para:

* estudo de cibersegurança
* demonstração de criptografia de arquivos
* aprendizado sobre comportamento de malware em ambiente controlado

❌ Não utilize fora de ambientes de teste
❌ Não execute em arquivos pessoais ou sistemas reais
✔ Use apenas dentro da pasta `files/`

<br/>

## 📁 Estrutura do Projeto

```bash
project/
│
├── malware.py              # Criptografa arquivos e inicia interface
├── decript-window.py       # Interface + descriptografia
├── build.py                # Gera executáveis (Windows/Linux)
├── thekey.key              # chave gerada automaticamente
│
├── files/                  # pasta segura de testes
│   ├── file1.txt
│   ├── file2.txt
│
└── build/                  # executáveis gerados
    ├── windows/
    ├── linux/
```

<br/>

## ⚙️ Funcionalidades

### 🔐 Malware Simulator

* Criptografa arquivos dentro da pasta `files/`
* Gera chave AES (Fernet)
* Executa em thread para não travar o sistema
* Abre automaticamente a interface de resgate

<br/>

### 💀 Interface de Resgate

* Janela centralizada
* Mensagem estilo ransomware (educacional)
* Timer regressivo
* Endereço de carteira Bitcoin com botão COPY
* Campo de senha para descriptografia
* Bloqueio do botão de fechar (X)

<br/>

### 🔓 Recuperação de Arquivos

* Validação de senha via **hash SHA-256**
* Descriptografia usando chave salva em `thekey.key`
* Execução em thread (UI não trava)

<br/>

### 📦 Build Automático

* Geração de executáveis via PyInstaller
* Suporte para:

  * 🪟 Windows (`.exe`)
  * 🐧 Linux (binário)
* Separação automática por sistema operacional

<br/>

## 🧪 Como Executar (Modo Python)

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 2. Criar arquivos de teste

Coloque arquivos dentro da pasta:

```bash
files/
```

---

### 3. Rodar o simulador

```bash
python malware.py
```

<br/>

## 🔐 Senha de teste

```text
GTH3kf7
```

<br/>

## 📦 Gerar executáveis (Windows/Linux)

### Rodar build automático:

```bash
python build.py
```

---

<br/>

## Resultado:

#### 🪟 Windows

```bash
build/windows/
├── malware.exe
├── decript-window.exe
```

#### 🐧 Linux

```bash
build/linux/
├── malware
├── decript-window
```

### 🚀 Como usar

#### 📦 instalar dependências
```make install```

#### 🧪 rodar projeto
```make run```

#### 📦 gerar executáveis
```make build```

#### 🧹 limpar projeto
```make clean```

<br/>

## 🧠 Conceitos abordados

Este projeto demonstra:

* Criptografia simétrica (Fernet)
* Hash de senha (SHA-256)
* Threads em Python
* GUI com Tkinter
* Simulação de comportamento de ransomware
* Controle de arquivos em diretórios isolados
* Build de executáveis multiplataforma

<br/>

## 🧱 Tecnologias

* Python 3.x
* cryptography
* tkinter
* threading
* hashlib
* os / subprocess
* PyInstaller

<br/>

## 🛑 Aviso Legal

> Este projeto não tem intenção maliciosa.

Ele é apenas uma simulação educacional de técnicas utilizadas em malware para fins de aprendizado em segurança ofensiva e defensiva.

<br/>

## 📌 Licença

MIT License
