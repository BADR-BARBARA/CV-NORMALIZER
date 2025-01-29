# CV-NORMALIZER

Un outil pour normaliser et générer des CV professionnels à partir de fichiers PDF.

---

## 📝 Description

Le **CV-NORMALIZER** est une application Streamlit qui permet aux utilisateurs de télécharger un CV au format PDF, d'en extraire le texte, de le structurer en JSON, puis de générer un CV professionnel au format PDF en utilisant un modèle LaTeX prédéfini. Ce projet utilise des technologies comme **Tesseract OCR** pour l'extraction de texte, **LangChain** pour le traitement du langage naturel, et **LaTeX** pour la génération de PDF.

---

## 🚀 Fonctionnalités

- **Extraction de texte** : Extraction du texte à partir d'un fichier PDF en utilisant Tesseract OCR.
- **Nettoyage de texte** : Suppression des espaces inutiles, des lignes vides et normalisation du texte.
- **Structuration en JSON** : Conversion du texte extrait en une structure JSON standardisée.
- **Génération de LaTeX** : Utilisation d'un modèle LaTeX pour créer un CV professionnel à partir des données JSON.
- **Compilation en PDF** : Compilation du code LaTeX en un fichier PDF téléchargeable.

---

## 📦 Installation

### Prérequis

- **Python 3.8 ou supérieur**
- **Tesseract OCR** : Installé sur votre système (voir [Tesseract Installation Guide](https://github.com/tesseract-ocr/tesseract)).
- **pdflatex** : Installé sur votre système pour compiler les fichiers LaTeX.

### Étapes d'installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/BADR-BARBARA/CV-NORMALIZER.git
   cd CV-NORMALIZER

2. Installez les dépendances Python :

   ```bash

      pip install -r requirements.txt

3. Configurez Tesseract OCR :

   - Assurez-vous que Tesseract est installé sur votre système.
   - Définissez le chemin vers l'exécutable Tesseract dans le code :

     ```python

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

4. Lancez l'application Streamlit :

   ```bash

      streamlit run app.py

---

## 📧 Contact

- Pour toute question ou suggestion, contactez-moi à barbarabadr2003@gmail.com
---      