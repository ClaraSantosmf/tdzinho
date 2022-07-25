# tdzinho
Project to practice django

Criando ambiente virtual

```console
python -m venv .venv --upgrade-deps
```

Ativando o ambiente virtual

```console
source .venv/bin/activate
```

Instalando o pip-tools

```console
pip install pip-tools
```

Gerando o arquivo requirements com hashes

```console
pip-compile --generate-hashes requirements.in
```

Instalando com pip

```console
pip install -r requirements.txt
```
