.. test1 documentation master file, created by
   sphinx-quickstart on Fri Jan 24 22:43:40 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. Bienvenue dans la documentation du CV Normalizer !

===================
CV Normalizer
===================

Introduction
============
Le **CV Normalizer** est une application Streamlit qui permet aux utilisateurs de télécharger un CV au format PDF, d'en extraire le texte, de le structurer en JSON, puis de générer un CV professionnel au format PDF en utilisant un modèle LaTeX prédéfini. Ce projet utilise des technologies comme **Tesseract OCR** pour l'extraction de texte, **LangChain** pour le traitement du langage naturel, et **LaTeX** pour la génération de PDF.

Fonctionnalités
===============
1. **Extraction de texte** : Extraction du texte à partir d'un fichier PDF en utilisant Tesseract OCR.
2. **Nettoyage de texte** : Suppression des espaces inutiles, des lignes vides et normalisation du texte.
3. **Structuration en JSON** : Conversion du texte extrait en une structure JSON standardisée.
4. **Génération de LaTeX** : Utilisation d'un modèle LaTeX pour créer un CV professionnel à partir des données JSON.
5. **Compilation en PDF** : Compilation du code LaTeX en un fichier PDF téléchargeable.

Prérequis
=========
Avant d'utiliser l'application, assurez-vous d'avoir installé les dépendances suivantes :

- **Python 3.8 ou supérieur**
- **Streamlit** : `pip install streamlit`
- **Tesseract OCR** : Installé sur votre système (voir `Tesseract Installation Guide <https://github.com/tesseract-ocr/tesseract>`_).
- **pdf2image** : `pip install pdf2image`
- **pytesseract** : `pip install pytesseract`
- **LangChain** : `pip install langchain`
- **pdflatex** : Installé sur votre système pour compiler les fichiers LaTeX.

Installation
============
1. Clonez le dépôt du projet :

   .. code-block:: bash

      git clone https://github.com/BADR-BARBARA/CV-NORMALIZER.git
      cd CV-NORMALIZER

2. Installez les dépendances Python :

   .. code-block:: bash

      pip install -r requirements.txt

3. Configurez Tesseract OCR :

   - Assurez-vous que Tesseract est installé sur votre système.
   - Définissez le chemin vers l'exécutable Tesseract dans le code :

     .. code-block:: python

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

4. Lancez l'application Streamlit :

   .. code-block:: bash

      streamlit run app.py

Utilisation
===========

Étape 1 : Téléchargement du CV
------------------------------
- Cliquez sur le bouton "Upload your PDF CV" pour télécharger un fichier PDF contenant votre CV.

Étape 2 : Extraction et nettoyage du texte
------------------------------------------
- L'application extrait le texte du PDF et le nettoie automatiquement.

Étape 3 : Génération du JSON structuré
--------------------------------------
- Le texte extrait est converti en une structure JSON standardisée.

Étape 4 : Génération du code LaTeX
----------------------------------
- Le JSON est utilisé pour remplir un modèle LaTeX prédéfini.

Étape 5 : Compilation en PDF
----------------------------
- Le code LaTeX est compilé en un fichier PDF, que vous pouvez télécharger.

Structure du Projet
===================
::

   cv-normalizer/
   ├── app.py                  # Script principal de l'application Streamlit
   ├── TEMPLATE.tex            # Modèle LaTeX pour le CV
   ├── EXAMPLE.tex             # Exemple de code LaTeX généré
   ├── J_exa.json              # Exemple de JSON structuré
   ├── requirements.txt        # Fichier des dépendances
   └── generated_files/        # Dossier contenant les fichiers générés (PDF, LaTeX, logs)


Personnalisation
===============

Modifier le modèle LaTeX
------------------------
- Vous pouvez personnaliser le modèle LaTeX en éditant le fichier `TEMPLATE.tex`.

Ajouter des sections supplémentaires
------------------------------------
- Pour ajouter des sections supplémentaires au JSON ou au modèle LaTeX, modifiez les fichiers `app.py`, `TEMPLATE.tex`, et les prompts correspondants.

Déploiement sur Read the Docs
=============================
1. Créez un compte sur `Read the Docs <https://readthedocs.org/>`_.
2. Importez votre dépôt GitHub.
3. Configurez les paramètres de build pour utiliser un fichier `docs/conf.py` et `docs/index.rst`.
4. Assurez-vous que votre documentation est au format reStructuredText (`.rst`) ou Markdown (`.md`).

Conclusion
==========
Le **CV Normalizer** est un outil puissant pour automatiser la création de CV professionnels. Grâce à cette documentation, vous pouvez facilement installer, utiliser et personnaliser l'application pour répondre à vos besoins spécifiques.

Pour toute question ou contribution, n'hésitez pas à ouvrir une issue sur le dépôt GitHub.




.. toctree::
   :maxdepth: 2
   :caption: Contents:

