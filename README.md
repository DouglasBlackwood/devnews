# DEVNEWS



## Quickstart

Installer l'application

	pip install devnews

L'appel via la ligne de commande se fait simplement

	# Pour avoir toutes les dernières news
	devnews
	# ou pour avoir les dernières news Python
	devnews python



## Développer sur l'application

Installer poetry et télécharger le dépôt de l'application. Exécuter la commande suivante à la racine du projet.

	poetry install

### Exécuter les tests

	poetry run pytest



## TODO

- mise en cache des news (fichier? sqlite?)
- publier webapp
- outil de filtre sur la webapp
- pagination cli (click.echo_via_pager bug avec printtable)
