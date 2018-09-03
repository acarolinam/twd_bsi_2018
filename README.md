Passo a passo para desenvolvimento da aplicação Rango.
Veja no ar em: http://brunotissi.pythonanywhere.com/

Github
  Criar repositório com .gitignore 
  Clonar repositório na máquina

Virtualenv
	Criar virtualenv na máquina e ativá-la
	Criar arquivo requirements.txt
	Instalar requirements (pip install -r requirements)

Django
	Criar projeto django (django-admin.py startproject tango_with_django_project)
	Entrar na pasta do projeto e criar o app Rango (python manage.py startapp rango)
	
GitHub
	Adicionar arquivos no repositório (git add .)
	Commit (git commit -m “Criação requirements, projeto e app”)
	Adicionar ao git (git push origin master)
	
Django
	Adicionar app ‘rango’ em INSTALLED_APPS no settings.py
	Criar view httpresponse
	Mapear urls em urls.py do projeto
	Criar arquivo urls.py dentro do app rango

Pythonanywhere
	Clonar repositório com git clone
	Criar virtualenv com mkvirtualenv
	Fazer instalação do django com pip install 
	Alterar diretório do path na interface
	Alterar WSGI configuration file
