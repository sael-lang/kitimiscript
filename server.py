import json
import re
from fastapi import FastAPI, Request
import requests
from typing import List, Dict
import emoji
from datetime import date, datetime
from pydantic import BaseModel
from fastapi_utilities import repeat_at
from unidecode import unidecode
app = FastAPI()
prename=""
checklang=""
productslist= {
"Products":[
 {
  "Brand": 1,
  "Type": "01",
  "Number": "001",
  "SKU": "101001",
  "FR": "Planche de Couverture",
  "Weight (g)": 90,
  "EN": "Cover board",
  "DE": "Abdeckungstafel"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "001",
  "SKU": "102001",
  "FR": "Gestes du quotidien",
  "Weight (g)": 150,
  "EN": "Daily life 1",
  "DE": "Alltag"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "002",
  "SKU": "102002",
  "FR": "Gestes du quotidien 2",
  "Weight (g)": 150,
  "EN": "Daily life 2",
  "DE": "Alltag 2"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "003",
  "SKU": "102003",
  "FR": "Gestes du quotidien 3",
  "Weight (g)": 150,
  "EN": "Daily life 3",
  "DE": "Alltag 3"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "004",
  "SKU": "102004",
  "FR": "Formes - couleurs et tailles",
  "Weight (g)": 150,
  "EN": "Shapes - Colors & Sizes",
  "DE": "FORMEN - FARBEN& GROBEN"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "005",
  "SKU": "102005",
  "FR": "Denombrement",
  "Weight (g)": 150,
  "EN": "Count",
  "DE": "Aufzahlung"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "006",
  "SKU": "102006",
  "FR": "Cadre temporel - Jour et Nuit",
  "Weight (g)": 150,
  "EN": "Time Frame - Day & Night",
  "DE": "Zeitrahmen - Tag & Nacht"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "007",
  "SKU": "102007",
  "FR": "Logique et Puzzle",
  "Weight (g)": 150,
  "EN": "Logic & Puzzle",
  "DE": "Logik & Ratsel"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "008",
  "SKU": "102008",
  "FR": "Pizza et Horloge",
  "Weight (g)": 150,
  "EN": "Pizza & Clock",
  "DE": "Pizza & Uhr"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "009",
  "SKU": "102009",
  "FR": "Schema corporel fille",
  "Weight (g)": 150,
  "EN": "Girl Body Map",
  "DE": "Der Madchenkoper"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "010",
  "SKU": "102010",
  "FR": "Schema corporel garcon",
  "Weight (g)": 150,
  "EN": "Boy Body Map",
  "DE": "Der Jungenkorper"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "011",
  "SKU": "102011",
  "FR": "Fruits et Legumes",
  "Weight (g)": 150,
  "EN": "Fruits & Veggies",
  "DE": "Obst & Gemuse"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "012",
  "SKU": "102012",
  "FR": "Saisons",
  "Weight (g)": 150,
  "EN": "Seasons",
  "DE": "Jahreszeiten"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "013",
  "SKU": "102013",
  "FR": "Cadre spatial et Transport",
  "Weight (g)": 150,
  "EN": "Space Frame & Transport",
  "DE": "Raumliches Denken &  Verkehr"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "014",
  "SKU": "102014",
  "FR": "Toucher et Memorisation",
  "Weight (g)": 150,
  "EN": "Touch & Memorization",
  "DE": "Beruhren & speichern"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "015",
  "SKU": "102015",
  "FR": "Animaux - Jungle et Ferme",
  "Weight (g)": 150,
  "EN": "Animals - Jungle & Farm",
  "DE": "Tiere - Dschungel & Bauernhof"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "016",
  "SKU": "102016",
  "FR": "Table",
  "Weight (g)": 150,
  "EN": "Table",
  "DE": "Am Tisch"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "017",
  "SKU": "102017",
  "FR": "Animaux - mer et Dexterite",
  "Weight (g)": 150,
  "EN": "Sea Animals & Dexterity",
  "DE": "Meereslebewesen & Geschicklichkeit"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "018",
  "SKU": "102018",
  "FR": "Animaux - Desert et Banquise",
  "Weight (g)": 150,
  "EN": "Animals - Desert & Pack Ice",
  "DE": "Tiere - Wuste & Eis"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "019",
  "SKU": "102019",
  "FR": "Emotions",
  "Weight (g)": 150,
  "EN": "Emotions",
  "DE": "Emotionen"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "020",
  "SKU": "102020",
  "FR": "Cycle - Eau et Fleur",
  "Weight (g)": 150,
  "EN": "Cycle - Water & Flower",
  "DE": "Zyklus - Wasser & Blume"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "021",
  "SKU": "102021",
  "FR": "Dessin et Ecriture",
  "Weight (g)": 150,
  "EN": "Drawing & Writing",
  "DE": "Zeichnen & Schreiben"
 },
 {
  "Brand": 1,
  "Type": "02",
  "Number": "022",
  "SKU": "102022",
  "FR": "Vetements",
  "Weight (g)": 150,
  "EN": "Clothes",
  "DE": "Kleidung"
 },
 {
  "Brand": 1,
  "Type": "03",
  "Number": "001",
  "SKU": "103001",
  "FR": "Lacets rouges",
  "Weight (g)": 10,
  "EN": "Red Laces",
  "DE": "Rot"
 },
 {
  "Brand": 1,
  "Type": "03",
  "Number": "002",
  "SKU": "103002",
  "FR": "Lacets verts",
  "Weight (g)": 10,
  "EN": "Green Laces",
  "DE": "Grun"
 },
 {
  "Brand": 1,
  "Type": "03",
  "Number": "003",
  "SKU": "103003",
  "FR": "Lacets bleus",
  "Weight (g)": 10,
  "EN": "Blue Laces",
  "DE": "Blau"
 },
 {
  "Brand": 1,
  "Type": "03",
  "Number": "004",
  "SKU": "103004",
  "FR": "Lacets jaunes",
  "Weight (g)": 10,
  "EN": "Yellow Laces",
  "DE": "Gelb"
 },
 {
  "Brand": 1,
  "Type": "03",
  "Number": "005",
  "SKU": "103005",
  "FR": "Lacets oranges",
  "Weight (g)": 10,
  "EN": "Orange Laces",
  "DE": "Orangefarben"
 },
 {
  "Brand": 1,
  "Type": "03",
  "Number": "006",
  "SKU": "103006",
  "FR": "Lacets roses",
  "Weight (g)": 10,
  "EN": "Pink Laces",
  "DE": "Rosa"
 },
 {
  "Brand": 1,
  "Type": "04",
  "Number": "001",
  "SKU": "104001",
  "FR": "Coffret",
  "Weight (g)": 500,
  "EN": "Color box",
  "DE": "Farbkasten"
 },
 {
  "Brand": 1,
  "Type": "04",
  "Number": "002",
  "SKU": "104002",
  "FR": "Boite",
  "Weight (g)": 250,
  "EN": "Box",
  "DE": "Kasten"
 },
 {
  "Brand": 1,
  "Type": "05",
  "Number": "001",
  "SKU": "105001",
  "FR": "Cube de rangement",
  "Weight (g)": 600,
  "EN": "Storage cube",
  "DE": "Kitibook Aufbewahrungsbox"
 },
 {
  "Brand": 1,
  "Type": "06",
  "Number": "001",
  "SKU": "106001",
  "FR": "Kit Alphabet - Vert",
  "Weight (g)": 95,
  "EN": "Green purse",
  "DE": "Grune Handtasche"
 },
 {
  "Brand": 1,
  "Type": "06",
  "Number": "002",
  "SKU": "106002",
  "FR": "Kit Alphabet - Bleu",
  "Weight (g)": 95,
  "EN": "Blue purse",
  "DE": "Blaue Handtasche"
 },
 {
  "Brand": 1,
  "Type": "06",
  "Number": "003",
  "SKU": "106003",
  "FR": "Kit Alphabet - Orange",
  "Weight (g)": 95,
  "EN": "Orange purse",
  "DE": "Orange Handtasche"
 },
 {
  "Brand": 1,
  "Type": "06",
  "Number": "004",
  "SKU": "106004",
  "FR": "Kit Alphabet - Rose",
  "Weight (g)": 95,
  "EN": "Pink purse",
  "DE": "Pink Handtasche"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "001",
  "SKU": "107001",
  "FR": "A",
  "Weight (g)": 4,
  "EN": "A",
  "DE": "A"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "002",
  "SKU": "107002",
  "FR": "B",
  "Weight (g)": 4,
  "EN": "B",
  "DE": "B"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "003",
  "SKU": "107003",
  "FR": "C",
  "Weight (g)": 4,
  "EN": "C",
  "DE": "C"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "004",
  "SKU": "107004",
  "FR": "D",
  "Weight (g)": 4,
  "EN": "D",
  "DE": "D"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "005",
  "SKU": "107005",
  "FR": "E",
  "Weight (g)": 4,
  "EN": "E",
  "DE": "E"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "006",
  "SKU": "107006",
  "FR": "F",
  "Weight (g)": 4,
  "EN": "F",
  "DE": "F"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "007",
  "SKU": "107007",
  "FR": "G",
  "Weight (g)": 4,
  "EN": "G",
  "DE": "G"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "008",
  "SKU": "107008",
  "FR": "H",
  "Weight (g)": 4,
  "EN": "H",
  "DE": "H"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "009",
  "SKU": "107009",
  "FR": "I",
  "Weight (g)": 4,
  "EN": "I",
  "DE": "I"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "010",
  "SKU": "107010",
  "FR": "J",
  "Weight (g)": 4,
  "EN": "J",
  "DE": "J"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "011",
  "SKU": "107011",
  "FR": "K",
  "Weight (g)": 4,
  "EN": "K",
  "DE": "K"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "012",
  "SKU": "107012",
  "FR": "L",
  "Weight (g)": 4,
  "EN": "L",
  "DE": "L"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "013",
  "SKU": "107013",
  "FR": "M",
  "Weight (g)": 4,
  "EN": "M",
  "DE": "M"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "014",
  "SKU": "107014",
  "FR": "N",
  "Weight (g)": 4,
  "EN": "N",
  "DE": "N"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "015",
  "SKU": "107015",
  "FR": "O",
  "Weight (g)": 4,
  "EN": "O",
  "DE": "O"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "016",
  "SKU": "107016",
  "FR": "P",
  "Weight (g)": 4,
  "EN": "P",
  "DE": "P"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "017",
  "SKU": "107017",
  "FR": "Q",
  "Weight (g)": 4,
  "EN": "Q",
  "DE": "Q"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "018",
  "SKU": "107018",
  "FR": "R",
  "Weight (g)": 4,
  "EN": "R",
  "DE": "R"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "019",
  "SKU": "107019",
  "FR": "S",
  "Weight (g)": 4,
  "EN": "S",
  "DE": "S"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "020",
  "SKU": "107020",
  "FR": "T",
  "Weight (g)": 4,
  "EN": "T",
  "DE": "T"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "021",
  "SKU": "107021",
  "FR": "U",
  "Weight (g)": 4,
  "EN": "U",
  "DE": "U"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "022",
  "SKU": "107022",
  "FR": "V",
  "Weight (g)": 4,
  "EN": "V",
  "DE": "V"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "023",
  "SKU": "107023",
  "FR": "W",
  "Weight (g)": 4,
  "EN": "W",
  "DE": "W"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "024",
  "SKU": "107024",
  "FR": "X",
  "Weight (g)": 4,
  "EN": "X",
  "DE": "X"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "025",
  "SKU": "107025",
  "FR": "Y",
  "Weight (g)": 4,
  "EN": "Y",
  "DE": "Y"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "026",
  "SKU": "107026",
  "FR": "Z",
  "Weight (g)": 4,
  "EN": "Z",
  "DE": "Z"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "027",
  "SKU": "107027",
  "FR": "Å",
  "Weight (g)": 4,
  "EN": "Å",
  "DE": "Å"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "028",
  "SKU": "107028",
  "FR": "Ä",
  "Weight (g)": 4,
  "EN": "Ä",
  "DE": "Ä"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "029",
  "SKU": "107029",
  "FR": "Ö",
  "Weight (g)": 4,
  "EN": "Ö",
  "DE": "Ö"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "030",
  "SKU": "107030",
  "FR": "Ø",
  "Weight (g)": 4,
  "EN": "Ø",
  "DE": "Ø"
 },
 {
  "Brand": 1,
  "Type": "07",
  "Number": "031",
  "SKU": "107031",
  "FR": "Æ",
  "Weight (g)": 4,
  "EN": "Æ",
  "DE": "Æ"
 }
],
"Aftersale":[
 {
  "SKU": "102020/1",
  "FR": "Cycle - Eau et Fleur / Nuage",
  "EN": "Cycle - Water & Flower / White cloud",
  "SKU Planche": "102020",
  "Nom Planche": "Cycle - Eau et Fleur",
  "Idpièce": 1,
  "Nom FR without special letters": "Nuage",
  "Nom FR": "Nuage",
  "Nom sheet EN": "Cycle - Water & Flower",
  "Nom EN": "White cloud"
 },
 {
  "SKU": "102020/2",
  "FR": "Cycle - Eau et Fleur / Nuage pluie",
  "EN": "Cycle - Water & Flower / Rain cloud",
  "SKU Planche": "102020",
  "Nom Planche": "Cycle - Eau et Fleur",
  "Idpièce": 2,
  "Nom FR without special letters": "Nuage pluie",
  "Nom FR": "Nuage pluie",
  "Nom sheet EN": "Cycle - Water & Flower",
  "Nom EN": "Rain cloud"
 },
 {
  "SKU": "102020/3",
  "FR": "Cycle - Eau et Fleur / Neige",
  "EN": "Cycle - Water & Flower / Snow",
  "SKU Planche": "102020",
  "Nom Planche": "Cycle - Eau et Fleur",
  "Idpièce": 3,
  "Nom FR without special letters": "Neige",
  "Nom FR": "Neige",
  "Nom sheet EN": "Cycle - Water & Flower",
  "Nom EN": "Snow"
 },
 {
  "SKU": "102020/4",
  "FR": "Cycle - Eau et Fleur / Riviere",
  "EN": "Cycle - Water & Flower / River",
  "SKU Planche": "102020",
  "Nom Planche": "Cycle - Eau et Fleur",
  "Idpièce": 4,
  "Nom FR without special letters": "Riviere",
  "Nom FR": "Rivière",
  "Nom sheet EN": "Cycle - Water & Flower",
  "Nom EN": "River"
 },
 {
  "SKU": "102020/5",
  "FR": "Cycle - Eau et Fleur / Mer",
  "EN": "Cycle - Water & Flower / Blue sea",
  "SKU Planche": "102020",
  "Nom Planche": "Cycle - Eau et Fleur",
  "Idpièce": 5,
  "Nom FR without special letters": "Mer",
  "Nom FR": "Mer",
  "Nom sheet EN": "Cycle - Water & Flower",
  "Nom EN": "Blue sea"
 },
 {
  "SKU": "102020/6",
  "FR": "Cycle - Eau et Fleur / Fleur",
  "EN": "Cycle - Water & Flower / Pink flower",
  "SKU Planche": "102020",
  "Nom Planche": "Cycle - Eau et Fleur",
  "Idpièce": 6,
  "Nom FR without special letters": "Fleur",
  "Nom FR": "Fleur",
  "Nom sheet EN": "Cycle - Water & Flower",
  "Nom EN": "Pink flower"
 },
 {
  "SKU": "102020/7",
  "FR": "Cycle - Eau et Fleur / Ruche",
  "EN": "Cycle - Water & Flower / Hive",
  "SKU Planche": "102020",
  "Nom Planche": "Cycle - Eau et Fleur",
  "Idpièce": 7,
  "Nom FR without special letters": "Ruche",
  "Nom FR": "Ruche",
  "Nom sheet EN": "Cycle - Water & Flower",
  "Nom EN": "Hive"
 },
 {
  "SKU": "102020/8",
  "FR": "Cycle - Eau et Fleur / Rose",
  "EN": "Cycle - Water & Flower / Red flower",
  "SKU Planche": "102020",
  "Nom Planche": "Cycle - Eau et Fleur",
  "Idpièce": 8,
  "Nom FR without special letters": "Rose",
  "Nom FR": "Rose",
  "Nom sheet EN": "Cycle - Water & Flower",
  "Nom EN": "Red flower"
 },
 {
  "SKU": "102020/9",
  "FR": "Cycle - Eau et Fleur / Pistil",
  "EN": "Cycle - Water & Flower / Pistil",
  "SKU Planche": "102020",
  "Nom Planche": "Cycle - Eau et Fleur",
  "Idpièce": 9,
  "Nom FR without special letters": "Pistil",
  "Nom FR": "Pistil",
  "Nom sheet EN": "Cycle - Water & Flower",
  "Nom EN": "Pistil"
 },
 {
  "SKU": "102020/10",
  "FR": "Cycle - Eau et Fleur / Abeille",
  "EN": "Cycle - Water & Flower / Bee",
  "SKU Planche": "102020",
  "Nom Planche": "Cycle - Eau et Fleur",
  "Idpièce": 10,
  "Nom FR without special letters": "Abeille",
  "Nom FR": "Abeille",
  "Nom sheet EN": "Cycle - Water & Flower",
  "Nom EN": "Bee"
 },
 {
  "SKU": "102012/1",
  "FR": "Saisons / Soleil",
  "EN": "Seasons / Sun",
  "SKU Planche": "102012",
  "Nom Planche": "Saisons",
  "Idpièce": 1,
  "Nom FR without special letters": "Soleil",
  "Nom FR": "Soleil",
  "Nom sheet EN": "Seasons",
  "Nom EN": "Sun"
 },
 {
  "SKU": "102012/2",
  "FR": "Saisons / Arbre",
  "EN": "Seasons / Green Tree",
  "SKU Planche": "102012",
  "Nom Planche": "Saisons",
  "Idpièce": 2,
  "Nom FR without special letters": "Arbre",
  "Nom FR": "Arbre",
  "Nom sheet EN": "Seasons",
  "Nom EN": "Green Tree"
 },
 {
  "SKU": "102012/3",
  "FR": "Saisons / Sol vert",
  "EN": "Seasons / Grass",
  "SKU Planche": "102012",
  "Nom Planche": "Saisons",
  "Idpièce": 3,
  "Nom FR without special letters": "Sol vert",
  "Nom FR": "Sol vert",
  "Nom sheet EN": "Seasons",
  "Nom EN": "Grass"
 },
 {
  "SKU": "102012/4",
  "FR": "Saisons / Sol orange",
  "EN": "Seasons / Dry grass",
  "SKU Planche": "102012",
  "Nom Planche": "Saisons",
  "Idpièce": 4,
  "Nom FR without special letters": "Sol orange",
  "Nom FR": "Sol orange",
  "Nom sheet EN": "Seasons",
  "Nom EN": "Dry grass"
 },
 {
  "SKU": "102012/5",
  "FR": "Saisons / Soleil",
  "EN": "Seasons / Sun",
  "SKU Planche": "102012",
  "Nom Planche": "Saisons",
  "Idpièce": 5,
  "Nom FR without special letters": "Soleil",
  "Nom FR": "Soleil",
  "Nom sheet EN": "Seasons",
  "Nom EN": "Sun"
 },
 {
  "SKU": "102012/6",
  "FR": "Saisons / Fleur sans tige",
  "EN": "Seasons / Flower",
  "SKU Planche": "102012",
  "Nom Planche": "Saisons",
  "Idpièce": 6,
  "Nom FR without special letters": "Fleur sans tige",
  "Nom FR": "Fleur sans tige",
  "Nom sheet EN": "Seasons",
  "Nom EN": "Flower"
 },
 {
  "SKU": "102012/7",
  "FR": "Saisons / Fleur avec tige",
  "EN": "Seasons / Flower with stem",
  "SKU Planche": "102012",
  "Nom Planche": "Saisons",
  "Idpièce": 7,
  "Nom FR without special letters": "Fleur avec tige",
  "Nom FR": "Fleur avec tige",
  "Nom sheet EN": "Seasons",
  "Nom EN": "Flower with stem"
 },
 {
  "SKU": "102012/8",
  "FR": "Saisons / Feuille d arbre verte",
  "EN": "Seasons / Green leaf",
  "SKU Planche": "102012",
  "Nom Planche": "Saisons",
  "Idpièce": 8,
  "Nom FR without special letters": "Feuille d arbre verte",
  "Nom FR": "Feuille d'arbre verte",
  "Nom sheet EN": "Seasons",
  "Nom EN": "Green leaf"
 },
 {
  "SKU": "102012/9",
  "FR": "Saisons / Feuille d arbre rouge",
  "EN": "Seasons / Red leaf",
  "SKU Planche": "102012",
  "Nom Planche": "Saisons",
  "Idpièce": 9,
  "Nom FR without special letters": "Feuille d arbre rouge",
  "Nom FR": "Feuille d'arbre rouge",
  "Nom sheet EN": "Seasons",
  "Nom EN": "Red leaf"
 },
 {
  "SKU": "102012/10",
  "FR": "Saisons / Pomme",
  "EN": "Seasons / Apple",
  "SKU Planche": "102012",
  "Nom Planche": "Saisons",
  "Idpièce": 10,
  "Nom FR without special letters": "Pomme",
  "Nom FR": "Pomme",
  "Nom sheet EN": "Seasons",
  "Nom EN": "Apple"
 },
 {
  "SKU": "102012/11",
  "FR": "Saisons / Flocon de neige",
  "EN": "Seasons / Snowflake",
  "SKU Planche": "102012",
  "Nom Planche": "Saisons",
  "Idpièce": 11,
  "Nom FR without special letters": "Flocon de neige",
  "Nom FR": "Flocon de neige",
  "Nom sheet EN": "Seasons",
  "Nom EN": "Snowflake"
 },
 {
  "SKU": "102017/1",
  "FR": "Animaux - mer et Dexterite / Stylo a eau",
  "EN": "Sea Animals & Dexterity / Water pen",
  "SKU Planche": "102017",
  "Nom Planche": "Animaux - mer et Dexterite",
  "Idpièce": 1,
  "Nom FR without special letters": "Stylo a eau",
  "Nom FR": "Stylo à eau",
  "Nom sheet EN": "Sea Animals & Dexterity",
  "Nom EN": "Water pen"
 },
 {
  "SKU": "102022/1",
  "FR": "Vetements / Tete homme",
  "EN": "Clothes / Boy head",
  "SKU Planche": "102022",
  "Nom Planche": "Vetements",
  "Idpièce": 1,
  "Nom FR without special letters": "Tete homme",
  "Nom FR": "Tête homme",
  "Nom sheet EN": "Clothes",
  "Nom EN": "Boy head"
 },
 {
  "SKU": "102022/2",
  "FR": "Vetements / Tete femme",
  "EN": "Clothes / Girl head",
  "SKU Planche": "102022",
  "Nom Planche": "Vetements",
  "Idpièce": 2,
  "Nom FR without special letters": "Tete femme",
  "Nom FR": "Tête femme",
  "Nom sheet EN": "Clothes",
  "Nom EN": "Girl head"
 },
 {
  "SKU": "102022/3",
  "FR": "Vetements / Pantalon",
  "EN": "Clothes / Pants",
  "SKU Planche": "102022",
  "Nom Planche": "Vetements",
  "Idpièce": 3,
  "Nom FR without special letters": "Pantalon",
  "Nom FR": "Pantalon",
  "Nom sheet EN": "Clothes",
  "Nom EN": "Pants"
 },
 {
  "SKU": "102022/4",
  "FR": "Vetements / Short",
  "EN": "Clothes / Shorts",
  "SKU Planche": "102022",
  "Nom Planche": "Vetements",
  "Idpièce": 4,
  "Nom FR without special letters": "Short",
  "Nom FR": "Short",
  "Nom sheet EN": "Clothes",
  "Nom EN": "Shorts"
 },
 {
  "SKU": "102022/5",
  "FR": "Vetements / Jupe",
  "EN": "Clothes / Skirt",
  "SKU Planche": "102022",
  "Nom Planche": "Vetements",
  "Idpièce": 5,
  "Nom FR without special letters": "Jupe",
  "Nom FR": "Jupe",
  "Nom sheet EN": "Clothes",
  "Nom EN": "Skirt"
 },
 {
  "SKU": "102022/6",
  "FR": "Vetements / Tee-shirt",
  "EN": "Clothes / T-shirt",
  "SKU Planche": "102022",
  "Nom Planche": "Vetements",
  "Idpièce": 6,
  "Nom FR without special letters": "Tee-shirt",
  "Nom FR": "Tee-shirt",
  "Nom sheet EN": "Clothes",
  "Nom EN": "T-shirt"
 },
 {
  "SKU": "102022/7",
  "FR": "Vetements / Pull",
  "EN": "Clothes / Sweater",
  "SKU Planche": "102022",
  "Nom Planche": "Vetements",
  "Idpièce": 7,
  "Nom FR without special letters": "Pull",
  "Nom FR": "Pull",
  "Nom sheet EN": "Clothes",
  "Nom EN": "Sweater"
 },
 {
  "SKU": "102022/8",
  "FR": "Vetements / Chemise",
  "EN": "Clothes / Shirt",
  "SKU Planche": "102022",
  "Nom Planche": "Vetements",
  "Idpièce": 8,
  "Nom FR without special letters": "Chemise",
  "Nom FR": "Chemise",
  "Nom sheet EN": "Clothes",
  "Nom EN": "Shirt"
 },
 {
  "SKU": "102022/9",
  "FR": "Vetements / Robe",
  "EN": "Clothes / Dress",
  "SKU Planche": "102022",
  "Nom Planche": "Vetements",
  "Idpièce": 9,
  "Nom FR without special letters": "Robe",
  "Nom FR": "Robe",
  "Nom sheet EN": "Clothes",
  "Nom EN": "Dress"
 },
 {
  "SKU": "102022/10",
  "FR": "Vetements / Chaussures",
  "EN": "Clothes / Shoes",
  "SKU Planche": "102022",
  "Nom Planche": "Vetements",
  "Idpièce": 10,
  "Nom FR without special letters": "Chaussures",
  "Nom FR": "Chaussures",
  "Nom sheet EN": "Clothes",
  "Nom EN": "Shoes"
 },
 {
  "SKU": "102004/1",
  "FR": "Formes - couleurs et tailles / Rectangle",
  "EN": "Shapes - Colors & Sizes / Rectangle",
  "SKU Planche": "102004",
  "Nom Planche": "Formes - couleurs et tailles",
  "Idpièce": 1,
  "Nom FR without special letters": "Rectangle",
  "Nom FR": "Rectangle",
  "Nom sheet EN": "Shapes - Colors & Sizes",
  "Nom EN": "Rectangle"
 },
 {
  "SKU": "102004/2",
  "FR": "Formes - couleurs et tailles / Carre",
  "EN": "Shapes - Colors & Sizes / Square",
  "SKU Planche": "102004",
  "Nom Planche": "Formes - couleurs et tailles",
  "Idpièce": 2,
  "Nom FR without special letters": "Carre",
  "Nom FR": "Carré",
  "Nom sheet EN": "Shapes - Colors & Sizes",
  "Nom EN": "Square"
 },
 {
  "SKU": "102004/3",
  "FR": "Formes - couleurs et tailles / Coeur",
  "EN": "Shapes - Colors & Sizes / Heart",
  "SKU Planche": "102004",
  "Nom Planche": "Formes - couleurs et tailles",
  "Idpièce": 3,
  "Nom FR without special letters": "Coeur",
  "Nom FR": "Coeur",
  "Nom sheet EN": "Shapes - Colors & Sizes",
  "Nom EN": "Heart"
 },
 {
  "SKU": "102004/4",
  "FR": "Formes - couleurs et tailles / Losange",
  "EN": "Shapes - Colors & Sizes / Diamond",
  "SKU Planche": "102004",
  "Nom Planche": "Formes - couleurs et tailles",
  "Idpièce": 4,
  "Nom FR without special letters": "Losange",
  "Nom FR": "Losange",
  "Nom sheet EN": "Shapes - Colors & Sizes",
  "Nom EN": "Diamond"
 },
 {
  "SKU": "102004/5",
  "FR": "Formes - couleurs et tailles / Cercle",
  "EN": "Shapes - Colors & Sizes / Circle",
  "SKU Planche": "102004",
  "Nom Planche": "Formes - couleurs et tailles",
  "Idpièce": 5,
  "Nom FR without special letters": "Cercle",
  "Nom FR": "Cercle",
  "Nom sheet EN": "Shapes - Colors & Sizes",
  "Nom EN": "Circle"
 },
 {
  "SKU": "102004/6",
  "FR": "Formes - couleurs et tailles / Triangle",
  "EN": "Shapes - Colors & Sizes / Triangle",
  "SKU Planche": "102004",
  "Nom Planche": "Formes - couleurs et tailles",
  "Idpièce": 6,
  "Nom FR without special letters": "Triangle",
  "Nom FR": "Triangle",
  "Nom sheet EN": "Shapes - Colors & Sizes",
  "Nom EN": "Triangle"
 },
 {
  "SKU": "102004/7",
  "FR": "Formes - couleurs et tailles / Taille 1",
  "EN": "Shapes - Colors & Sizes / Top",
  "SKU Planche": "102004",
  "Nom Planche": "Formes - couleurs et tailles",
  "Idpièce": 7,
  "Nom FR without special letters": "Taille 1",
  "Nom FR": "Taille 1",
  "Nom sheet EN": "Shapes - Colors & Sizes",
  "Nom EN": "Top"
 },
 {
  "SKU": "102004/8",
  "FR": "Formes - couleurs et tailles / Taille 2",
  "EN": "Shapes - Colors & Sizes / Mid-top",
  "SKU Planche": "102004",
  "Nom Planche": "Formes - couleurs et tailles",
  "Idpièce": 8,
  "Nom FR without special letters": "Taille 2",
  "Nom FR": "Taille 2",
  "Nom sheet EN": "Shapes - Colors & Sizes",
  "Nom EN": "Mid-top"
 },
 {
  "SKU": "102004/9",
  "FR": "Formes - couleurs et tailles / Taille 3",
  "EN": "Shapes - Colors & Sizes / Middle",
  "SKU Planche": "102004",
  "Nom Planche": "Formes - couleurs et tailles",
  "Idpièce": 9,
  "Nom FR without special letters": "Taille 3",
  "Nom FR": "Taille 3",
  "Nom sheet EN": "Shapes - Colors & Sizes",
  "Nom EN": "Middle"
 },
 {
  "SKU": "102004/10",
  "FR": "Formes - couleurs et tailles / Taille 4",
  "EN": "Shapes - Colors & Sizes / Mid-bottom",
  "SKU Planche": "102004",
  "Nom Planche": "Formes - couleurs et tailles",
  "Idpièce": 10,
  "Nom FR without special letters": "Taille 4",
  "Nom FR": "Taille 4",
  "Nom sheet EN": "Shapes - Colors & Sizes",
  "Nom EN": "Mid-bottom"
 },
 {
  "SKU": "102004/11",
  "FR": "Formes - couleurs et tailles / Taille 5",
  "EN": "Shapes - Colors & Sizes / Bottom",
  "SKU Planche": "102004",
  "Nom Planche": "Formes - couleurs et tailles",
  "Idpièce": 11,
  "Nom FR without special letters": "Taille 5",
  "Nom FR": "Taille 5",
  "Nom sheet EN": "Shapes - Colors & Sizes",
  "Nom EN": "Bottom"
 },
 {
  "SKU": "102006/1",
  "FR": "Cadre temporel - Jour et Nuit / Porte",
  "EN": "Time Frame - Day & Night / Door",
  "SKU Planche": "102006",
  "Nom Planche": "Cadre temporel - Jour et Nuit",
  "Idpièce": 1,
  "Nom FR without special letters": "Porte",
  "Nom FR": "Porte",
  "Nom sheet EN": "Time Frame - Day & Night",
  "Nom EN": "Door"
 },
 {
  "SKU": "102006/2",
  "FR": "Cadre temporel - Jour et Nuit / Fenetre jaune",
  "EN": "Time Frame - Day & Night / Yellow window",
  "SKU Planche": "102006",
  "Nom Planche": "Cadre temporel - Jour et Nuit",
  "Idpièce": 2,
  "Nom FR without special letters": "Fenetre jaune",
  "Nom FR": "Fenêtre jaune",
  "Nom sheet EN": "Time Frame - Day & Night",
  "Nom EN": "Yellow window"
 },
 {
  "SKU": "102006/3",
  "FR": "Cadre temporel - Jour et Nuit / Nuage gris",
  "EN": "Time Frame - Day & Night / Dark cloud",
  "SKU Planche": "102006",
  "Nom Planche": "Cadre temporel - Jour et Nuit",
  "Idpièce": 3,
  "Nom FR without special letters": "Nuage gris",
  "Nom FR": "Nuage gris",
  "Nom sheet EN": "Time Frame - Day & Night",
  "Nom EN": "Dark cloud"
 },
 {
  "SKU": "102006/4",
  "FR": "Cadre temporel - Jour et Nuit / Nuage blanc",
  "EN": "Time Frame - Day & Night / White cloud",
  "SKU Planche": "102006",
  "Nom Planche": "Cadre temporel - Jour et Nuit",
  "Idpièce": 4,
  "Nom FR without special letters": "Nuage blanc",
  "Nom FR": "Nuage blanc",
  "Nom sheet EN": "Time Frame - Day & Night",
  "Nom EN": "White cloud"
 },
 {
  "SKU": "102006/5",
  "FR": "Cadre temporel - Jour et Nuit / Soleil",
  "EN": "Time Frame - Day & Night / Sun",
  "SKU Planche": "102006",
  "Nom Planche": "Cadre temporel - Jour et Nuit",
  "Idpièce": 5,
  "Nom FR without special letters": "Soleil",
  "Nom FR": "Soleil",
  "Nom sheet EN": "Time Frame - Day & Night",
  "Nom EN": "Sun"
 },
 {
  "SKU": "102006/6",
  "FR": "Cadre temporel - Jour et Nuit / Fenetre blanche",
  "EN": "Time Frame - Day & Night / White window",
  "SKU Planche": "102006",
  "Nom Planche": "Cadre temporel - Jour et Nuit",
  "Idpièce": 6,
  "Nom FR without special letters": "Fenetre blanche",
  "Nom FR": "Fenêtre blanche",
  "Nom sheet EN": "Time Frame - Day & Night",
  "Nom EN": "White window"
 },
 {
  "SKU": "102006/7",
  "FR": "Cadre temporel - Jour et Nuit / Nuage eclair",
  "EN": "Time Frame - Day & Night / Flash cloud",
  "SKU Planche": "102006",
  "Nom Planche": "Cadre temporel - Jour et Nuit",
  "Idpièce": 7,
  "Nom FR without special letters": "Nuage eclair",
  "Nom FR": "Nuage éclair",
  "Nom sheet EN": "Time Frame - Day & Night",
  "Nom EN": "Flash cloud"
 },
 {
  "SKU": "102006/8",
  "FR": "Cadre temporel - Jour et Nuit / Nuage pluie",
  "EN": "Time Frame - Day & Night / Rain cloud",
  "SKU Planche": "102006",
  "Nom Planche": "Cadre temporel - Jour et Nuit",
  "Idpièce": 8,
  "Nom FR without special letters": "Nuage pluie",
  "Nom FR": "Nuage pluie",
  "Nom sheet EN": "Time Frame - Day & Night",
  "Nom EN": "Rain cloud"
 },
 {
  "SKU": "102006/9",
  "FR": "Cadre temporel - Jour et Nuit / Lune",
  "EN": "Time Frame - Day & Night / Moon",
  "SKU Planche": "102006",
  "Nom Planche": "Cadre temporel - Jour et Nuit",
  "Idpièce": 9,
  "Nom FR without special letters": "Lune",
  "Nom FR": "Lune",
  "Nom sheet EN": "Time Frame - Day & Night",
  "Nom EN": "Moon"
 },
 {
  "SKU": "102007/1",
  "FR": "Logique et Puzzle / Puzzle - haut droite",
  "EN": "Logic & Puzzle / Top-right",
  "SKU Planche": "102007",
  "Nom Planche": "Logique et Puzzle",
  "Idpièce": 1,
  "Nom FR without special letters": "Puzzle - haut droite",
  "Nom FR": "Puzzle - haut droite",
  "Nom sheet EN": "Logic & Puzzle",
  "Nom EN": "Top-right"
 },
 {
  "SKU": "102007/2",
  "FR": "Logique et Puzzle / Puzzle - haut gauche",
  "EN": "Logic & Puzzle / Top-left",
  "SKU Planche": "102007",
  "Nom Planche": "Logique et Puzzle",
  "Idpièce": 2,
  "Nom FR without special letters": "Puzzle - haut gauche",
  "Nom FR": "Puzzle - haut gauche",
  "Nom sheet EN": "Logic & Puzzle",
  "Nom EN": "Top-left"
 },
 {
  "SKU": "102007/3",
  "FR": "Logique et Puzzle / Puzzle - bas droite",
  "EN": "Logic & Puzzle / Bottom-right",
  "SKU Planche": "102007",
  "Nom Planche": "Logique et Puzzle",
  "Idpièce": 3,
  "Nom FR without special letters": "Puzzle - bas droite",
  "Nom FR": "Puzzle - bas droite",
  "Nom sheet EN": "Logic & Puzzle",
  "Nom EN": "Bottom-right"
 },
 {
  "SKU": "102007/4",
  "FR": "Logique et Puzzle / Puzzle - bas gauche",
  "EN": "Logic & Puzzle / Bottom-left",
  "SKU Planche": "102007",
  "Nom Planche": "Logique et Puzzle",
  "Idpièce": 4,
  "Nom FR without special letters": "Puzzle - bas gauche",
  "Nom FR": "Puzzle - bas gauche",
  "Nom sheet EN": "Logic & Puzzle",
  "Nom EN": "Bottom-left"
 },
 {
  "SKU": "102007/5",
  "FR": "Logique et Puzzle / Piece 1",
  "EN": "Logic & Puzzle / Piece 1",
  "SKU Planche": "102007",
  "Nom Planche": "Logique et Puzzle",
  "Idpièce": 5,
  "Nom FR without special letters": "Piece 1",
  "Nom FR": "Pièce 1",
  "Nom sheet EN": "Logic & Puzzle",
  "Nom EN": "Piece 1"
 },
 {
  "SKU": "102007/6",
  "FR": "Logique et Puzzle / Piece 2",
  "EN": "Logic & Puzzle / Piece 2",
  "SKU Planche": "102007",
  "Nom Planche": "Logique et Puzzle",
  "Idpièce": 6,
  "Nom FR without special letters": "Piece 2",
  "Nom FR": "Pièce 2",
  "Nom sheet EN": "Logic & Puzzle",
  "Nom EN": "Piece 2"
 },
 {
  "SKU": "102007/7",
  "FR": "Logique et Puzzle / Piece 3",
  "EN": "Logic & Puzzle / Piece 3",
  "SKU Planche": "102007",
  "Nom Planche": "Logique et Puzzle",
  "Idpièce": 7,
  "Nom FR without special letters": "Piece 3",
  "Nom FR": "Pièce 3",
  "Nom sheet EN": "Logic & Puzzle",
  "Nom EN": "Piece 3"
 },
 {
  "SKU": "102007/8",
  "FR": "Logique et Puzzle / Piece 4",
  "EN": "Logic & Puzzle / Piece 4",
  "SKU Planche": "102007",
  "Nom Planche": "Logique et Puzzle",
  "Idpièce": 8,
  "Nom FR without special letters": "Piece 4",
  "Nom FR": "Pièce 4",
  "Nom sheet EN": "Logic & Puzzle",
  "Nom EN": "Piece 4"
 },
 {
  "SKU": "102007/9",
  "FR": "Logique et Puzzle / Piece 5",
  "EN": "Logic & Puzzle / Piece 5",
  "SKU Planche": "102007",
  "Nom Planche": "Logique et Puzzle",
  "Idpièce": 9,
  "Nom FR without special letters": "Piece 5",
  "Nom FR": "Pièce 5",
  "Nom sheet EN": "Logic & Puzzle",
  "Nom EN": "Piece 5"
 },
 {
  "SKU": "102007/10",
  "FR": "Logique et Puzzle / Piece 6",
  "EN": "Logic & Puzzle / Piece 6",
  "SKU Planche": "102007",
  "Nom Planche": "Logique et Puzzle",
  "Idpièce": 10,
  "Nom FR without special letters": "Piece 6",
  "Nom FR": "Pièce 6",
  "Nom sheet EN": "Logic & Puzzle",
  "Nom EN": "Piece 6"
 },
 {
  "SKU": "102008/1",
  "FR": "Pizza et Horloge / Pizza part 1",
  "EN": "Pizza & Clock / Pizza 1",
  "SKU Planche": "102008",
  "Nom Planche": "Pizza et Horloge",
  "Idpièce": 1,
  "Nom FR without special letters": "Pizza part 1",
  "Nom FR": "Pizza part 1",
  "Nom sheet EN": "Pizza & Clock",
  "Nom EN": "Pizza 1"
 },
 {
  "SKU": "102008/2",
  "FR": "Pizza et Horloge / Pizza part 2",
  "EN": "Pizza & Clock / Pizza 2",
  "SKU Planche": "102008",
  "Nom Planche": "Pizza et Horloge",
  "Idpièce": 2,
  "Nom FR without special letters": "Pizza part 2",
  "Nom FR": "Pizza part 2",
  "Nom sheet EN": "Pizza & Clock",
  "Nom EN": "Pizza 2"
 },
 {
  "SKU": "102008/3",
  "FR": "Pizza et Horloge / Pizza part 3",
  "EN": "Pizza & Clock / Pizza 3",
  "SKU Planche": "102008",
  "Nom Planche": "Pizza et Horloge",
  "Idpièce": 3,
  "Nom FR without special letters": "Pizza part 3",
  "Nom FR": "Pizza part 3",
  "Nom sheet EN": "Pizza & Clock",
  "Nom EN": "Pizza 3"
 },
 {
  "SKU": "102008/4",
  "FR": "Pizza et Horloge / Pizza part 4",
  "EN": "Pizza & Clock / Pizza 4",
  "SKU Planche": "102008",
  "Nom Planche": "Pizza et Horloge",
  "Idpièce": 4,
  "Nom FR without special letters": "Pizza part 4",
  "Nom FR": "Pizza part 4",
  "Nom sheet EN": "Pizza & Clock",
  "Nom EN": "Pizza 4"
 },
 {
  "SKU": "102008/5",
  "FR": "Pizza et Horloge / Pizza part 5",
  "EN": "Pizza & Clock / Pizza 5",
  "SKU Planche": "102008",
  "Nom Planche": "Pizza et Horloge",
  "Idpièce": 5,
  "Nom FR without special letters": "Pizza part 5",
  "Nom FR": "Pizza part 5",
  "Nom sheet EN": "Pizza & Clock",
  "Nom EN": "Pizza 5"
 },
 {
  "SKU": "102008/6",
  "FR": "Pizza et Horloge / Pizza part 6",
  "EN": "Pizza & Clock / Pizza 6",
  "SKU Planche": "102008",
  "Nom Planche": "Pizza et Horloge",
  "Idpièce": 6,
  "Nom FR without special letters": "Pizza part 6",
  "Nom FR": "Pizza part 6",
  "Nom sheet EN": "Pizza & Clock",
  "Nom EN": "Pizza 6"
 },
 {
  "SKU": "102019/1",
  "FR": "Emotions / Face 1",
  "EN": "Emotions / Face 1",
  "SKU Planche": "102019",
  "Nom Planche": "Emotions",
  "Idpièce": 1,
  "Nom FR without special letters": "Face 1",
  "Nom FR": "Face 1",
  "Nom sheet EN": "Emotions",
  "Nom EN": "Face 1"
 },
 {
  "SKU": "102019/2",
  "FR": "Emotions / Face 2",
  "EN": "Emotions / Face 2",
  "SKU Planche": "102019",
  "Nom Planche": "Emotions",
  "Idpièce": 2,
  "Nom FR without special letters": "Face 2",
  "Nom FR": "Face 2",
  "Nom sheet EN": "Emotions",
  "Nom EN": "Face 2"
 },
 {
  "SKU": "102019/3",
  "FR": "Emotions / Face 3",
  "EN": "Emotions / Face 3",
  "SKU Planche": "102019",
  "Nom Planche": "Emotions",
  "Idpièce": 3,
  "Nom FR without special letters": "Face 3",
  "Nom FR": "Face 3",
  "Nom sheet EN": "Emotions",
  "Nom EN": "Face 3"
 },
 {
  "SKU": "102019/4",
  "FR": "Emotions / Face 4",
  "EN": "Emotions / Face 4",
  "SKU Planche": "102019",
  "Nom Planche": "Emotions",
  "Idpièce": 4,
  "Nom FR without special letters": "Face 4",
  "Nom FR": "Face 4",
  "Nom sheet EN": "Emotions",
  "Nom EN": "Face 4"
 },
 {
  "SKU": "102019/5",
  "FR": "Emotions / Face 5",
  "EN": "Emotions / Face 5",
  "SKU Planche": "102019",
  "Nom Planche": "Emotions",
  "Idpièce": 5,
  "Nom FR without special letters": "Face 5",
  "Nom FR": "Face 5",
  "Nom sheet EN": "Emotions",
  "Nom EN": "Face 5"
 },
 {
  "SKU": "102019/6",
  "FR": "Emotions / Face 6",
  "EN": "Emotions / Face 6",
  "SKU Planche": "102019",
  "Nom Planche": "Emotions",
  "Idpièce": 6,
  "Nom FR without special letters": "Face 6",
  "Nom FR": "Face 6",
  "Nom sheet EN": "Emotions",
  "Nom EN": "Face 6"
 },
 {
  "SKU": "102019/7",
  "FR": "Emotions / Face 7",
  "EN": "Emotions / Face 7",
  "SKU Planche": "102019",
  "Nom Planche": "Emotions",
  "Idpièce": 7,
  "Nom FR without special letters": "Face 7",
  "Nom FR": "Face 7",
  "Nom sheet EN": "Emotions",
  "Nom EN": "Face 7"
 },
 {
  "SKU": "102019/8",
  "FR": "Emotions / Face 8",
  "EN": "Emotions / Face 8",
  "SKU Planche": "102019",
  "Nom Planche": "Emotions",
  "Idpièce": 8,
  "Nom FR without special letters": "Face 8",
  "Nom FR": "Face 8",
  "Nom sheet EN": "Emotions",
  "Nom EN": "Face 8"
 },
 {
  "SKU": "102019/9",
  "FR": "Emotions / Face 9",
  "EN": "Emotions / Face 9",
  "SKU Planche": "102019",
  "Nom Planche": "Emotions",
  "Idpièce": 9,
  "Nom FR without special letters": "Face 9",
  "Nom FR": "Face 9",
  "Nom sheet EN": "Emotions",
  "Nom EN": "Face 9"
 },
 {
  "SKU": "102019/10",
  "FR": "Emotions / Face 10",
  "EN": "Emotions / Face 10",
  "SKU Planche": "102019",
  "Nom Planche": "Emotions",
  "Idpièce": 10,
  "Nom FR without special letters": "Face 10",
  "Nom FR": "Face 10",
  "Nom sheet EN": "Emotions",
  "Nom EN": "Face 10"
 },
 {
  "SKU": "102019/11",
  "FR": "Emotions / Face 11",
  "EN": "Emotions / Face 11",
  "SKU Planche": "102019",
  "Nom Planche": "Emotions",
  "Idpièce": 11,
  "Nom FR without special letters": "Face 11",
  "Nom FR": "Face 11",
  "Nom sheet EN": "Emotions",
  "Nom EN": "Face 11"
 },
 {
  "SKU": "102019/12",
  "FR": "Emotions / Face 12",
  "EN": "Emotions / Face 12",
  "SKU Planche": "102019",
  "Nom Planche": "Emotions",
  "Idpièce": 12,
  "Nom FR without special letters": "Face 12",
  "Nom FR": "Face 12",
  "Nom sheet EN": "Emotions",
  "Nom EN": "Face 12"
 },
 {
  "SKU": "102019/13",
  "FR": "Emotions / Peau de banane",
  "EN": "Emotions / Banana skin",
  "SKU Planche": "102019",
  "Nom Planche": "Emotions",
  "Idpièce": 13,
  "Nom FR without special letters": "Peau de banane",
  "Nom FR": "Peau de banane",
  "Nom sheet EN": "Emotions",
  "Nom EN": "Banana skin"
 },
 {
  "SKU": "102010/1",
  "FR": "Schema corporel garcon / Cheveux",
  "EN": "Boy Body Map / Hair",
  "SKU Planche": "102010",
  "Nom Planche": "Schema corporel garcon",
  "Idpièce": 1,
  "Nom FR without special letters": "Cheveux",
  "Nom FR": "Cheveux",
  "Nom sheet EN": "Boy Body Map",
  "Nom EN": "Hair"
 },
 {
  "SKU": "102010/2",
  "FR": "Schema corporel garcon / Oeil",
  "EN": "Boy Body Map / Eye",
  "SKU Planche": "102010",
  "Nom Planche": "Schema corporel garcon",
  "Idpièce": 2,
  "Nom FR without special letters": "Oeil",
  "Nom FR": "Oeil",
  "Nom sheet EN": "Boy Body Map",
  "Nom EN": "Eye"
 },
 {
  "SKU": "102010/3",
  "FR": "Schema corporel garcon / Nez",
  "EN": "Boy Body Map / Nose",
  "SKU Planche": "102010",
  "Nom Planche": "Schema corporel garcon",
  "Idpièce": 3,
  "Nom FR without special letters": "Nez",
  "Nom FR": "Nez",
  "Nom sheet EN": "Boy Body Map",
  "Nom EN": "Nose"
 },
 {
  "SKU": "102010/4",
  "FR": "Schema corporel garcon / Oreille gauche",
  "EN": "Boy Body Map / Right ear",
  "SKU Planche": "102010",
  "Nom Planche": "Schema corporel garcon",
  "Idpièce": 4,
  "Nom FR without special letters": "Oreille gauche",
  "Nom FR": "Oreille gauche",
  "Nom sheet EN": "Boy Body Map",
  "Nom EN": "Right ear"
 },
 {
  "SKU": "102010/5",
  "FR": "Schema corporel garcon / Oreille droite",
  "EN": "Boy Body Map / Left ear",
  "SKU Planche": "102010",
  "Nom Planche": "Schema corporel garcon",
  "Idpièce": 5,
  "Nom FR without special letters": "Oreille droite",
  "Nom FR": "Oreille droite",
  "Nom sheet EN": "Boy Body Map",
  "Nom EN": "Left ear"
 },
 {
  "SKU": "102010/6",
  "FR": "Schema corporel garcon / Bouche",
  "EN": "Boy Body Map / Mouth",
  "SKU Planche": "102010",
  "Nom Planche": "Schema corporel garcon",
  "Idpièce": 6,
  "Nom FR without special letters": "Bouche",
  "Nom FR": "Bouche",
  "Nom sheet EN": "Boy Body Map",
  "Nom EN": "Mouth"
 },
 {
  "SKU": "102010/7",
  "FR": "Schema corporel garcon / Tete",
  "EN": "Boy Body Map / Head",
  "SKU Planche": "102010",
  "Nom Planche": "Schema corporel garcon",
  "Idpièce": 7,
  "Nom FR without special letters": "Tete",
  "Nom FR": "Tête",
  "Nom sheet EN": "Boy Body Map",
  "Nom EN": "Head"
 },
 {
  "SKU": "102010/8",
  "FR": "Schema corporel garcon / Ventre",
  "EN": "Boy Body Map / Torso",
  "SKU Planche": "102010",
  "Nom Planche": "Schema corporel garcon",
  "Idpièce": 8,
  "Nom FR without special letters": "Ventre",
  "Nom FR": "Ventre",
  "Nom sheet EN": "Boy Body Map",
  "Nom EN": "Torso"
 },
 {
  "SKU": "102010/9",
  "FR": "Schema corporel garcon / Bras droit",
  "EN": "Boy Body Map / Right arm",
  "SKU Planche": "102010",
  "Nom Planche": "Schema corporel garcon",
  "Idpièce": 9,
  "Nom FR without special letters": "Bras droit",
  "Nom FR": "Bras droit",
  "Nom sheet EN": "Boy Body Map",
  "Nom EN": "Right arm"
 },
 {
  "SKU": "102010/10",
  "FR": "Schema corporel garcon / Bras gauche",
  "EN": "Boy Body Map / Left arm",
  "SKU Planche": "102010",
  "Nom Planche": "Schema corporel garcon",
  "Idpièce": 10,
  "Nom FR without special letters": "Bras gauche",
  "Nom FR": "Bras gauche",
  "Nom sheet EN": "Boy Body Map",
  "Nom EN": "Left arm"
 },
 {
  "SKU": "102010/11",
  "FR": "Schema corporel garcon / Jambe droite",
  "EN": "Boy Body Map / Right leg",
  "SKU Planche": "102010",
  "Nom Planche": "Schema corporel garcon",
  "Idpièce": 11,
  "Nom FR without special letters": "Jambe droite",
  "Nom FR": "Jambe droite",
  "Nom sheet EN": "Boy Body Map",
  "Nom EN": "Right leg"
 },
 {
  "SKU": "102010/12",
  "FR": "Schema corporel garcon / Jambe gauche",
  "EN": "Boy Body Map / Left leg",
  "SKU Planche": "102010",
  "Nom Planche": "Schema corporel garcon",
  "Idpièce": 12,
  "Nom FR without special letters": "Jambe gauche",
  "Nom FR": "Jambe gauche",
  "Nom sheet EN": "Boy Body Map",
  "Nom EN": "Left leg"
 },
 {
  "SKU": "102009/1",
  "FR": "Schema corporel fille / Cheveux",
  "EN": "Girl Body Map / Hair",
  "SKU Planche": "102009",
  "Nom Planche": "Schema corporel fille",
  "Idpièce": 1,
  "Nom FR without special letters": "Cheveux",
  "Nom FR": "Cheveux",
  "Nom sheet EN": "Girl Body Map",
  "Nom EN": "Hair"
 },
 {
  "SKU": "102009/2",
  "FR": "Schema corporel fille / Oeil",
  "EN": "Girl Body Map / Eye",
  "SKU Planche": "102009",
  "Nom Planche": "Schema corporel fille",
  "Idpièce": 2,
  "Nom FR without special letters": "Oeil",
  "Nom FR": "Oeil",
  "Nom sheet EN": "Girl Body Map",
  "Nom EN": "Eye"
 },
 {
  "SKU": "102009/3",
  "FR": "Schema corporel fille / Nez",
  "EN": "Girl Body Map / Nose",
  "SKU Planche": "102009",
  "Nom Planche": "Schema corporel fille",
  "Idpièce": 3,
  "Nom FR without special letters": "Nez",
  "Nom FR": "Nez",
  "Nom sheet EN": "Girl Body Map",
  "Nom EN": "Nose"
 },
 {
  "SKU": "102009/4",
  "FR": "Schema corporel fille / Oreille droite",
  "EN": "Girl Body Map / Right ear",
  "SKU Planche": "102009",
  "Nom Planche": "Schema corporel fille",
  "Idpièce": 4,
  "Nom FR without special letters": "Oreille droite",
  "Nom FR": "Oreille droite",
  "Nom sheet EN": "Girl Body Map",
  "Nom EN": "Right ear"
 },
 {
  "SKU": "102009/5",
  "FR": "Schema corporel fille / Oreille gauche",
  "EN": "Girl Body Map / Left ear",
  "SKU Planche": "102009",
  "Nom Planche": "Schema corporel fille",
  "Idpièce": 5,
  "Nom FR without special letters": "Oreille gauche",
  "Nom FR": "Oreille gauche",
  "Nom sheet EN": "Girl Body Map",
  "Nom EN": "Left ear"
 },
 {
  "SKU": "102009/6",
  "FR": "Schema corporel fille / Bouche",
  "EN": "Girl Body Map / Mouth",
  "SKU Planche": "102009",
  "Nom Planche": "Schema corporel fille",
  "Idpièce": 6,
  "Nom FR without special letters": "Bouche",
  "Nom FR": "Bouche",
  "Nom sheet EN": "Girl Body Map",
  "Nom EN": "Mouth"
 },
 {
  "SKU": "102009/7",
  "FR": "Schema corporel fille / Tete",
  "EN": "Girl Body Map / Head",
  "SKU Planche": "102009",
  "Nom Planche": "Schema corporel fille",
  "Idpièce": 7,
  "Nom FR without special letters": "Tete",
  "Nom FR": "Tête",
  "Nom sheet EN": "Girl Body Map",
  "Nom EN": "Head"
 },
 {
  "SKU": "102009/8",
  "FR": "Schema corporel fille / Ventre",
  "EN": "Girl Body Map / Torso",
  "SKU Planche": "102009",
  "Nom Planche": "Schema corporel fille",
  "Idpièce": 8,
  "Nom FR without special letters": "Ventre",
  "Nom FR": "Ventre",
  "Nom sheet EN": "Girl Body Map",
  "Nom EN": "Torso"
 },
 {
  "SKU": "102009/9",
  "FR": "Schema corporel fille / Bras droit",
  "EN": "Girl Body Map / Right arm",
  "SKU Planche": "102009",
  "Nom Planche": "Schema corporel fille",
  "Idpièce": 9,
  "Nom FR without special letters": "Bras droit",
  "Nom FR": "Bras droit",
  "Nom sheet EN": "Girl Body Map",
  "Nom EN": "Right arm"
 },
 {
  "SKU": "102009/10",
  "FR": "Schema corporel fille / Bras gauche",
  "EN": "Girl Body Map / Left arm",
  "SKU Planche": "102009",
  "Nom Planche": "Schema corporel fille",
  "Idpièce": 10,
  "Nom FR without special letters": "Bras gauche",
  "Nom FR": "Bras gauche",
  "Nom sheet EN": "Girl Body Map",
  "Nom EN": "Left arm"
 },
 {
  "SKU": "102009/11",
  "FR": "Schema corporel fille / Jambe droite",
  "EN": "Girl Body Map / Right leg",
  "SKU Planche": "102009",
  "Nom Planche": "Schema corporel fille",
  "Idpièce": 11,
  "Nom FR without special letters": "Jambe droite",
  "Nom FR": "Jambe droite",
  "Nom sheet EN": "Girl Body Map",
  "Nom EN": "Right leg"
 },
 {
  "SKU": "102009/12",
  "FR": "Schema corporel fille / Jambe gauche",
  "EN": "Girl Body Map / Left leg",
  "SKU Planche": "102009",
  "Nom Planche": "Schema corporel fille",
  "Idpièce": 12,
  "Nom FR without special letters": "Jambe gauche",
  "Nom FR": "Jambe gauche",
  "Nom sheet EN": "Girl Body Map",
  "Nom EN": "Left leg"
 },
 {
  "SKU": "102011/1",
  "FR": "Fruits et Legumes / Pomme de terre",
  "EN": "Fruits & Veggies / Potato",
  "SKU Planche": "102011",
  "Nom Planche": "Fruits et Legumes",
  "Idpièce": 1,
  "Nom FR without special letters": "Pomme de terre",
  "Nom FR": "Pomme de terre",
  "Nom sheet EN": "Fruits & Veggies",
  "Nom EN": "Potato"
 },
 {
  "SKU": "102011/2",
  "FR": "Fruits et Legumes / Oignon",
  "EN": "Fruits & Veggies / Onion",
  "SKU Planche": "102011",
  "Nom Planche": "Fruits et Legumes",
  "Idpièce": 2,
  "Nom FR without special letters": "Oignon",
  "Nom FR": "Oignon",
  "Nom sheet EN": "Fruits & Veggies",
  "Nom EN": "Onion"
 },
 {
  "SKU": "102011/3",
  "FR": "Fruits et Legumes / Carotte",
  "EN": "Fruits & Veggies / Carrot",
  "SKU Planche": "102011",
  "Nom Planche": "Fruits et Legumes",
  "Idpièce": 3,
  "Nom FR without special letters": "Carotte",
  "Nom FR": "Carotte",
  "Nom sheet EN": "Fruits & Veggies",
  "Nom EN": "Carrot"
 },
 {
  "SKU": "102011/4",
  "FR": "Fruits et Legumes / Tomate",
  "EN": "Fruits & Veggies / Tomato",
  "SKU Planche": "102011",
  "Nom Planche": "Fruits et Legumes",
  "Idpièce": 4,
  "Nom FR without special letters": "Tomate",
  "Nom FR": "Tomate",
  "Nom sheet EN": "Fruits & Veggies",
  "Nom EN": "Tomato"
 },
 {
  "SKU": "102011/5",
  "FR": "Fruits et Legumes / Aubergine",
  "EN": "Fruits & Veggies / Eggplant",
  "SKU Planche": "102011",
  "Nom Planche": "Fruits et Legumes",
  "Idpièce": 5,
  "Nom FR without special letters": "Aubergine",
  "Nom FR": "Aubergine",
  "Nom sheet EN": "Fruits & Veggies",
  "Nom EN": "Eggplant"
 },
 {
  "SKU": "102011/6",
  "FR": "Fruits et Legumes / Orange",
  "EN": "Fruits & Veggies / Orange",
  "SKU Planche": "102011",
  "Nom Planche": "Fruits et Legumes",
  "Idpièce": 6,
  "Nom FR without special letters": "Orange",
  "Nom FR": "Orange",
  "Nom sheet EN": "Fruits & Veggies",
  "Nom EN": "Orange"
 },
 {
  "SKU": "102011/7",
  "FR": "Fruits et Legumes / Ananas",
  "EN": "Fruits & Veggies / Pineapple",
  "SKU Planche": "102011",
  "Nom Planche": "Fruits et Legumes",
  "Idpièce": 7,
  "Nom FR without special letters": "Ananas",
  "Nom FR": "Ananas",
  "Nom sheet EN": "Fruits & Veggies",
  "Nom EN": "Pineapple"
 },
 {
  "SKU": "102011/8",
  "FR": "Fruits et Legumes / Banane",
  "EN": "Fruits & Veggies / Banana",
  "SKU Planche": "102011",
  "Nom Planche": "Fruits et Legumes",
  "Idpièce": 8,
  "Nom FR without special letters": "Banane",
  "Nom FR": "Banane",
  "Nom sheet EN": "Fruits & Veggies",
  "Nom EN": "Banana"
 },
 {
  "SKU": "102011/9",
  "FR": "Fruits et Legumes / Fraise",
  "EN": "Fruits & Veggies / Strawberry",
  "SKU Planche": "102011",
  "Nom Planche": "Fruits et Legumes",
  "Idpièce": 9,
  "Nom FR without special letters": "Fraise",
  "Nom FR": "Fraise",
  "Nom sheet EN": "Fruits & Veggies",
  "Nom EN": "Strawberry"
 },
 {
  "SKU": "102018/1",
  "FR": "Animaux - Desert et Banquise / Chameau",
  "EN": "Animals - Desert & Pack Ice / Camel",
  "SKU Planche": "102018",
  "Nom Planche": "Animaux - Desert et Banquise",
  "Idpièce": 1,
  "Nom FR without special letters": "Chameau",
  "Nom FR": "Chameau",
  "Nom sheet EN": "Animals - Desert & Pack Ice",
  "Nom EN": "Camel"
 },
 {
  "SKU": "102018/2",
  "FR": "Animaux - Desert et Banquise / Vautour",
  "EN": "Animals - Desert & Pack Ice / Vulture",
  "SKU Planche": "102018",
  "Nom Planche": "Animaux - Desert et Banquise",
  "Idpièce": 2,
  "Nom FR without special letters": "Vautour",
  "Nom FR": "Vautour",
  "Nom sheet EN": "Animals - Desert & Pack Ice",
  "Nom EN": "Vulture"
 },
 {
  "SKU": "102018/3",
  "FR": "Animaux - Desert et Banquise / Lezard",
  "EN": "Animals - Desert & Pack Ice / Lizzard",
  "SKU Planche": "102018",
  "Nom Planche": "Animaux - Desert et Banquise",
  "Idpièce": 3,
  "Nom FR without special letters": "Lezard",
  "Nom FR": "Lézard",
  "Nom sheet EN": "Animals - Desert & Pack Ice",
  "Nom EN": "Lizzard"
 },
 {
  "SKU": "102018/4",
  "FR": "Animaux - Desert et Banquise / Serpent",
  "EN": "Animals - Desert & Pack Ice / Snake",
  "SKU Planche": "102018",
  "Nom Planche": "Animaux - Desert et Banquise",
  "Idpièce": 4,
  "Nom FR without special letters": "Serpent",
  "Nom FR": "Serpent",
  "Nom sheet EN": "Animals - Desert & Pack Ice",
  "Nom EN": "Snake"
 },
 {
  "SKU": "102018/5",
  "FR": "Animaux - Desert et Banquise / Scorpion",
  "EN": "Animals - Desert & Pack Ice / Scorpion",
  "SKU Planche": "102018",
  "Nom Planche": "Animaux - Desert et Banquise",
  "Idpièce": 5,
  "Nom FR without special letters": "Scorpion",
  "Nom FR": "Scorpion",
  "Nom sheet EN": "Animals - Desert & Pack Ice",
  "Nom EN": "Scorpion"
 },
 {
  "SKU": "102018/6",
  "FR": "Animaux - Desert et Banquise / Penguin",
  "EN": "Animals - Desert & Pack Ice / Pinguin",
  "SKU Planche": "102018",
  "Nom Planche": "Animaux - Desert et Banquise",
  "Idpièce": 6,
  "Nom FR without special letters": "Penguin",
  "Nom FR": "Penguin",
  "Nom sheet EN": "Animals - Desert & Pack Ice",
  "Nom EN": "Pinguin"
 },
 {
  "SKU": "102018/7",
  "FR": "Animaux - Desert et Banquise / Ours polaire",
  "EN": "Animals - Desert & Pack Ice / Polar bear",
  "SKU Planche": "102018",
  "Nom Planche": "Animaux - Desert et Banquise",
  "Idpièce": 7,
  "Nom FR without special letters": "Ours polaire",
  "Nom FR": "Ours polaire",
  "Nom sheet EN": "Animals - Desert & Pack Ice",
  "Nom EN": "Polar bear"
 },
 {
  "SKU": "102018/8",
  "FR": "Animaux - Desert et Banquise / Loup blanc",
  "EN": "Animals - Desert & Pack Ice / White wolf",
  "SKU Planche": "102018",
  "Nom Planche": "Animaux - Desert et Banquise",
  "Idpièce": 8,
  "Nom FR without special letters": "Loup blanc",
  "Nom FR": "Loup blanc",
  "Nom sheet EN": "Animals - Desert & Pack Ice",
  "Nom EN": "White wolf"
 },
 {
  "SKU": "102018/9",
  "FR": "Animaux - Desert et Banquise / Phoque",
  "EN": "Animals - Desert & Pack Ice / Sea lion",
  "SKU Planche": "102018",
  "Nom Planche": "Animaux - Desert et Banquise",
  "Idpièce": 9,
  "Nom FR without special letters": "Phoque",
  "Nom FR": "Phoque",
  "Nom sheet EN": "Animals - Desert & Pack Ice",
  "Nom EN": "Sea lion"
 },
 {
  "SKU": "102018/10",
  "FR": "Animaux - Desert et Banquise / Baleine",
  "EN": "Animals - Desert & Pack Ice / Whale",
  "SKU Planche": "102018",
  "Nom Planche": "Animaux - Desert et Banquise",
  "Idpièce": 10,
  "Nom FR without special letters": "Baleine",
  "Nom FR": "Baleine",
  "Nom sheet EN": "Animals - Desert & Pack Ice",
  "Nom EN": "Whale"
 },
 {
  "SKU": "102016/1",
  "FR": "Table / Verre",
  "EN": "Table / Cup",
  "SKU Planche": "102016",
  "Nom Planche": "Table",
  "Idpièce": 1,
  "Nom FR without special letters": "Verre",
  "Nom FR": "Verre",
  "Nom sheet EN": "Table",
  "Nom EN": "Cup"
 },
 {
  "SKU": "102016/2",
  "FR": "Table / Tasse",
  "EN": "Table / Mug",
  "SKU Planche": "102016",
  "Nom Planche": "Table",
  "Idpièce": 2,
  "Nom FR without special letters": "Tasse",
  "Nom FR": "Tasse",
  "Nom sheet EN": "Table",
  "Nom EN": "Mug"
 },
 {
  "SKU": "102016/3",
  "FR": "Table / Assiette",
  "EN": "Table / Plate",
  "SKU Planche": "102016",
  "Nom Planche": "Table",
  "Idpièce": 3,
  "Nom FR without special letters": "Assiette",
  "Nom FR": "Assiette",
  "Nom sheet EN": "Table",
  "Nom EN": "Plate"
 },
 {
  "SKU": "102016/4",
  "FR": "Table / Fourchette",
  "EN": "Table / Fork",
  "SKU Planche": "102016",
  "Nom Planche": "Table",
  "Idpièce": 4,
  "Nom FR without special letters": "Fourchette",
  "Nom FR": "Fourchette",
  "Nom sheet EN": "Table",
  "Nom EN": "Fork"
 },
 {
  "SKU": "102016/5",
  "FR": "Table / Cuillere",
  "EN": "Table / Spoon",
  "SKU Planche": "102016",
  "Nom Planche": "Table",
  "Idpièce": 5,
  "Nom FR without special letters": "Cuillere",
  "Nom FR": "Cuillère",
  "Nom sheet EN": "Table",
  "Nom EN": "Spoon"
 },
 {
  "SKU": "102016/6",
  "FR": "Table / Couteau",
  "EN": "Table / Knife",
  "SKU Planche": "102016",
  "Nom Planche": "Table",
  "Idpièce": 6,
  "Nom FR without special letters": "Couteau",
  "Nom FR": "Couteau",
  "Nom sheet EN": "Table",
  "Nom EN": "Knife"
 },
 {
  "SKU": "102016/7",
  "FR": "Table / Lampe",
  "EN": "Table / Lamp",
  "SKU Planche": "102016",
  "Nom Planche": "Table",
  "Idpièce": 7,
  "Nom FR without special letters": "Lampe",
  "Nom FR": "Lampe",
  "Nom sheet EN": "Table",
  "Nom EN": "Lamp"
 },
 {
  "SKU": "102016/8",
  "FR": "Table / Vase",
  "EN": "Table / Vase",
  "SKU Planche": "102016",
  "Nom Planche": "Table",
  "Idpièce": 8,
  "Nom FR without special letters": "Vase",
  "Nom FR": "Vase",
  "Nom sheet EN": "Table",
  "Nom EN": "Vase"
 },
 {
  "SKU": "102016/9",
  "FR": "Table / Petite assiette",
  "EN": "Table / Platter",
  "SKU Planche": "102016",
  "Nom Planche": "Table",
  "Idpièce": 9,
  "Nom FR without special letters": "Petite assiette",
  "Nom FR": "Petite assiette",
  "Nom sheet EN": "Table",
  "Nom EN": "Platter"
 },
 {
  "SKU": "102016/10",
  "FR": "Table / Table",
  "EN": "Table / Table",
  "SKU Planche": "102016",
  "Nom Planche": "Table",
  "Idpièce": 10,
  "Nom FR without special letters": "Table",
  "Nom FR": "Table",
  "Nom sheet EN": "Table",
  "Nom EN": "Table"
 },
 {
  "SKU": "102016/11",
  "FR": "Table / Chaise",
  "EN": "Table / Chair",
  "SKU Planche": "102016",
  "Nom Planche": "Table",
  "Idpièce": 11,
  "Nom FR without special letters": "Chaise",
  "Nom FR": "Chaise",
  "Nom sheet EN": "Table",
  "Nom EN": "Chair"
 },
 {
  "SKU": "102013/1",
  "FR": "Cadre spatial et Transport / Avion",
  "EN": "Space Frame & Transport / Plane",
  "SKU Planche": "102013",
  "Nom Planche": "Cadre spatial et Transport",
  "Idpièce": 1,
  "Nom FR without special letters": "Avion",
  "Nom FR": "Avion",
  "Nom sheet EN": "Space Frame & Transport",
  "Nom EN": "Plane"
 },
 {
  "SKU": "102013/2",
  "FR": "Cadre spatial et Transport / Bateau",
  "EN": "Space Frame & Transport / Boat",
  "SKU Planche": "102013",
  "Nom Planche": "Cadre spatial et Transport",
  "Idpièce": 2,
  "Nom FR without special letters": "Bateau",
  "Nom FR": "Bateau",
  "Nom sheet EN": "Space Frame & Transport",
  "Nom EN": "Boat"
 },
 {
  "SKU": "102013/3",
  "FR": "Cadre spatial et Transport / Voiture",
  "EN": "Space Frame & Transport / Car",
  "SKU Planche": "102013",
  "Nom Planche": "Cadre spatial et Transport",
  "Idpièce": 3,
  "Nom FR without special letters": "Voiture",
  "Nom FR": "Voiture",
  "Nom sheet EN": "Space Frame & Transport",
  "Nom EN": "Car"
 },
 {
  "SKU": "102013/4",
  "FR": "Cadre spatial et Transport / Papillon",
  "EN": "Space Frame & Transport / Butterfly",
  "SKU Planche": "102013",
  "Nom Planche": "Cadre spatial et Transport",
  "Idpièce": 4,
  "Nom FR without special letters": "Papillon",
  "Nom FR": "Papillon",
  "Nom sheet EN": "Space Frame & Transport",
  "Nom EN": "Butterfly"
 },
 {
  "SKU": "102013/5",
  "FR": "Cadre spatial et Transport / Tortue",
  "EN": "Space Frame & Transport / Turtle",
  "SKU Planche": "102013",
  "Nom Planche": "Cadre spatial et Transport",
  "Idpièce": 5,
  "Nom FR without special letters": "Tortue",
  "Nom FR": "Tortue",
  "Nom sheet EN": "Space Frame & Transport",
  "Nom EN": "Turtle"
 },
 {
  "SKU": "102013/6",
  "FR": "Cadre spatial et Transport / Lapin",
  "EN": "Space Frame & Transport / Rabbit",
  "SKU Planche": "102013",
  "Nom Planche": "Cadre spatial et Transport",
  "Idpièce": 6,
  "Nom FR without special letters": "Lapin",
  "Nom FR": "Lapin",
  "Nom sheet EN": "Space Frame & Transport",
  "Nom EN": "Rabbit"
 },
 {
  "SKU": "102013/7",
  "FR": "Cadre spatial et Transport / Poisson mauve",
  "EN": "Space Frame & Transport / Fish 1",
  "SKU Planche": "102013",
  "Nom Planche": "Cadre spatial et Transport",
  "Idpièce": 7,
  "Nom FR without special letters": "Poisson mauve",
  "Nom FR": "Poisson mauve",
  "Nom sheet EN": "Space Frame & Transport",
  "Nom EN": "Fish 1"
 },
 {
  "SKU": "102013/8",
  "FR": "Cadre spatial et Transport / Poisson orange",
  "EN": "Space Frame & Transport / Fish 2",
  "SKU Planche": "102013",
  "Nom Planche": "Cadre spatial et Transport",
  "Idpièce": 8,
  "Nom FR without special letters": "Poisson orange",
  "Nom FR": "Poisson orange",
  "Nom sheet EN": "Space Frame & Transport",
  "Nom EN": "Fish 2"
 },
 {
  "SKU": "102015/1",
  "FR": "Animaux - Jungle et Ferme / Cheval",
  "EN": "Animals - Jungle & Farm / Horse",
  "SKU Planche": "102015",
  "Nom Planche": "Animaux - Jungle et Ferme",
  "Idpièce": 1,
  "Nom FR without special letters": "Cheval",
  "Nom FR": "Cheval",
  "Nom sheet EN": "Animals - Jungle & Farm",
  "Nom EN": "Horse"
 },
 {
  "SKU": "102015/2",
  "FR": "Animaux - Jungle et Ferme / Vache",
  "EN": "Animals - Jungle & Farm / Cow",
  "SKU Planche": "102015",
  "Nom Planche": "Animaux - Jungle et Ferme",
  "Idpièce": 2,
  "Nom FR without special letters": "Vache",
  "Nom FR": "Vache",
  "Nom sheet EN": "Animals - Jungle & Farm",
  "Nom EN": "Cow"
 },
 {
  "SKU": "102015/3",
  "FR": "Animaux - Jungle et Ferme / Poule",
  "EN": "Animals - Jungle & Farm / Chicken",
  "SKU Planche": "102015",
  "Nom Planche": "Animaux - Jungle et Ferme",
  "Idpièce": 3,
  "Nom FR without special letters": "Poule",
  "Nom FR": "Poule",
  "Nom sheet EN": "Animals - Jungle & Farm",
  "Nom EN": "Chicken"
 },
 {
  "SKU": "102015/4",
  "FR": "Animaux - Jungle et Ferme / Chevre",
  "EN": "Animals - Jungle & Farm / Goat",
  "SKU Planche": "102015",
  "Nom Planche": "Animaux - Jungle et Ferme",
  "Idpièce": 4,
  "Nom FR without special letters": "Chevre",
  "Nom FR": "Chèvre",
  "Nom sheet EN": "Animals - Jungle & Farm",
  "Nom EN": "Goat"
 },
 {
  "SKU": "102015/5",
  "FR": "Animaux - Jungle et Ferme / Mouton",
  "EN": "Animals - Jungle & Farm / Sheep",
  "SKU Planche": "102015",
  "Nom Planche": "Animaux - Jungle et Ferme",
  "Idpièce": 5,
  "Nom FR without special letters": "Mouton",
  "Nom FR": "Mouton",
  "Nom sheet EN": "Animals - Jungle & Farm",
  "Nom EN": "Sheep"
 },
 {
  "SKU": "102015/6",
  "FR": "Animaux - Jungle et Ferme / Cochon",
  "EN": "Animals - Jungle & Farm / Pig",
  "SKU Planche": "102015",
  "Nom Planche": "Animaux - Jungle et Ferme",
  "Idpièce": 6,
  "Nom FR without special letters": "Cochon",
  "Nom FR": "Cochon",
  "Nom sheet EN": "Animals - Jungle & Farm",
  "Nom EN": "Pig"
 },
 {
  "SKU": "102015/7",
  "FR": "Animaux - Jungle et Ferme / Lion",
  "EN": "Animals - Jungle & Farm / Lion",
  "SKU Planche": "102015",
  "Nom Planche": "Animaux - Jungle et Ferme",
  "Idpièce": 7,
  "Nom FR without special letters": "Lion",
  "Nom FR": "Lion",
  "Nom sheet EN": "Animals - Jungle & Farm",
  "Nom EN": "Lion"
 },
 {
  "SKU": "102015/8",
  "FR": "Animaux - Jungle et Ferme / Elephant",
  "EN": "Animals - Jungle & Farm / Elephant",
  "SKU Planche": "102015",
  "Nom Planche": "Animaux - Jungle et Ferme",
  "Idpièce": 8,
  "Nom FR without special letters": "Elephant",
  "Nom FR": "Eléphant",
  "Nom sheet EN": "Animals - Jungle & Farm",
  "Nom EN": "Elephant"
 },
 {
  "SKU": "102015/9",
  "FR": "Animaux - Jungle et Ferme / Singe",
  "EN": "Animals - Jungle & Farm / Monkey",
  "SKU Planche": "102015",
  "Nom Planche": "Animaux - Jungle et Ferme",
  "Idpièce": 9,
  "Nom FR without special letters": "Singe",
  "Nom FR": "Singe",
  "Nom sheet EN": "Animals - Jungle & Farm",
  "Nom EN": "Monkey"
 },
 {
  "SKU": "102015/10",
  "FR": "Animaux - Jungle et Ferme / Giraffe",
  "EN": "Animals - Jungle & Farm / Giraffe",
  "SKU Planche": "102015",
  "Nom Planche": "Animaux - Jungle et Ferme",
  "Idpièce": 10,
  "Nom FR without special letters": "Giraffe",
  "Nom FR": "Giraffe",
  "Nom sheet EN": "Animals - Jungle & Farm",
  "Nom EN": "Giraffe"
 },
 {
  "SKU": "102015/11",
  "FR": "Animaux - Jungle et Ferme / Hippopotame",
  "EN": "Animals - Jungle & Farm / Hippo",
  "SKU Planche": "102015",
  "Nom Planche": "Animaux - Jungle et Ferme",
  "Idpièce": 11,
  "Nom FR without special letters": "Hippopotame",
  "Nom FR": "Hippopotame",
  "Nom sheet EN": "Animals - Jungle & Farm",
  "Nom EN": "Hippo"
 },
 {
  "SKU": "102015/12",
  "FR": "Animaux - Jungle et Ferme / Zebre",
  "EN": "Animals - Jungle & Farm / Zebra",
  "SKU Planche": "102015",
  "Nom Planche": "Animaux - Jungle et Ferme",
  "Idpièce": 12,
  "Nom FR without special letters": "Zebre",
  "Nom FR": "Zèbre",
  "Nom sheet EN": "Animals - Jungle & Farm",
  "Nom EN": "Zebra"
 },
 {
  "SKU": "102014/1",
  "FR": "Toucher et Memorisation / Poisson colore",
  "EN": "Touch & Memorization / Colorful fish",
  "SKU Planche": "102014",
  "Nom Planche": "Toucher et Memorisation",
  "Idpièce": 1,
  "Nom FR without special letters": "Poisson colore",
  "Nom FR": "colorful fish",
  "Nom sheet EN": "Touch & Memorization",
  "Nom EN": "Colorful fish"
 },
 {
  "SKU": "102014/2",
  "FR": "Toucher et Memorisation / Triangle vert",
  "EN": "Touch & Memorization / Green triangle",
  "SKU Planche": "102014",
  "Nom Planche": "Toucher et Memorisation",
  "Idpièce": 2,
  "Nom FR without special letters": "Triangle vert",
  "Nom FR": "Triangle vert",
  "Nom sheet EN": "Touch & Memorization",
  "Nom EN": "Green triangle"
 },
 {
  "SKU": "102014/3",
  "FR": "Toucher et Memorisation / Hexagone jaune",
  "EN": "Touch & Memorization / Yellow hexagone",
  "SKU Planche": "102014",
  "Nom Planche": "Toucher et Memorisation",
  "Idpièce": 3,
  "Nom FR without special letters": "Hexagone jaune",
  "Nom FR": "Hexagone jaune",
  "Nom sheet EN": "Touch & Memorization",
  "Nom EN": "Yellow hexagone"
 },
 {
  "SKU": "102014/4",
  "FR": "Toucher et Memorisation / Trapeze",
  "EN": "Touch & Memorization / Red trapezoid",
  "SKU Planche": "102014",
  "Nom Planche": "Toucher et Memorisation",
  "Idpièce": 4,
  "Nom FR without special letters": "Trapeze",
  "Nom FR": "Trapèze",
  "Nom sheet EN": "Touch & Memorization",
  "Nom EN": "Red trapezoid"
 },
 {
  "SKU": "102014/5",
  "FR": "Toucher et Memorisation / Parallelogramme bleu",
  "EN": "Touch & Memorization / Blue parallelogram",
  "SKU Planche": "102014",
  "Nom Planche": "Toucher et Memorisation",
  "Idpièce": 5,
  "Nom FR without special letters": "Parallelogramme bleu",
  "Nom FR": "Parallélogramme bleu",
  "Nom sheet EN": "Touch & Memorization",
  "Nom EN": "Blue parallelogram"
 },
 {
  "SKU": "102014/6",
  "FR": "Toucher et Memorisation / Losange blanc",
  "EN": "Touch & Memorization / White diamond",
  "SKU Planche": "102014",
  "Nom Planche": "Toucher et Memorisation",
  "Idpièce": 6,
  "Nom FR without special letters": "Losange blanc",
  "Nom FR": "Losange blanc",
  "Nom sheet EN": "Touch & Memorization",
  "Nom EN": "White diamond"
 },
 {
  "SKU": "101001/1",
  "FR": "Planche de Couverture / Miroir",
  "EN": "Cover board / Mirror",
  "SKU Planche": "101001",
  "Nom Planche": "Planche de Couverture",
  "Idpièce": 1,
  "Nom FR without special letters": "Miroir",
  "Nom FR": "Miroir",
  "Nom sheet EN": "Cover board",
  "Nom EN": "Mirror"
 },
 {
  "SKU": "101001/0",
  "FR": "Planche de Couverture / Vierge",
  "EN": "Cover board / Cover board",
  "SKU Planche": "101001",
  "Nom Planche": "Planche de Couverture",
  "Idpièce": 0,
  "Nom FR without special letters": "Planche de Couverture",
  "Nom sheet EN": "Cover board",
  "Nom EN": "Cover board"
 },
 {
  "SKU": "102001/0",
  "FR": "Gestes du quotidien / Vierge",
  "EN": "Daily life 1 / Daily life 1",
  "SKU Planche": "102001",
  "Nom Planche": "Gestes du quotidien",
  "Idpièce": 0,
  "Nom FR without special letters": "Gestes du quotidien",
  "Nom sheet EN": "Daily life 1",
  "Nom EN": "Daily life 1"
 },
 {
  "SKU": "102002/0",
  "FR": "Gestes du quotidien 2 / Vierge",
  "EN": "Daily life 2 / Daily life 2",
  "SKU Planche": "102002",
  "Nom Planche": "Gestes du quotidien 2",
  "Idpièce": 0,
  "Nom FR without special letters": "Gestes du quotidien 2",
  "Nom sheet EN": "Daily life 2",
  "Nom EN": "Daily life 2"
 },
 {
  "SKU": "102003/0",
  "FR": "Gestes du quotidien 3 / Vierge",
  "EN": "Daily life 3 / Daily life 3",
  "SKU Planche": "102003",
  "Nom Planche": "Gestes du quotidien 3",
  "Idpièce": 0,
  "Nom FR without special letters": "Gestes du quotidien 3",
  "Nom sheet EN": "Daily life 3",
  "Nom EN": "Daily life 3"
 },
 {
  "SKU": "102004/0",
  "FR": "Formes - couleurs et tailles / Vierge",
  "EN": "Shapes - Colors & Sizes / Shapes - Colors & Sizes",
  "SKU Planche": "102004",
  "Nom Planche": "Formes - couleurs et tailles",
  "Idpièce": 0,
  "Nom FR without special letters": "Formes - couleurs et tailles",
  "Nom sheet EN": "Shapes - Colors & Sizes",
  "Nom EN": "Shapes - Colors & Sizes"
 },
 {
  "SKU": "102005/0",
  "FR": "Denombrement / Vierge",
  "EN": "Count / Count",
  "SKU Planche": "102005",
  "Nom Planche": "Denombrement",
  "Idpièce": 0,
  "Nom FR without special letters": "Denombrement",
  "Nom sheet EN": "Count",
  "Nom EN": "Count"
 },
 {
  "SKU": "102006/0",
  "FR": "Cadre temporel - Jour et Nuit / Vierge",
  "EN": "Time Frame - Day & Night / Time Frame - Day & Night",
  "SKU Planche": "102006",
  "Nom Planche": "Cadre temporel - Jour et Nuit",
  "Idpièce": 0,
  "Nom FR without special letters": "Cadre temporel - Jour et Nuit",
  "Nom sheet EN": "Time Frame - Day & Night",
  "Nom EN": "Time Frame - Day & Night"
 },
 {
  "SKU": "102007/0",
  "FR": "Logique et Puzzle / Vierge",
  "EN": "Logic & Puzzle / Logic & Puzzle",
  "SKU Planche": "102007",
  "Nom Planche": "Logique et Puzzle",
  "Idpièce": 0,
  "Nom FR without special letters": "Logique et Puzzle",
  "Nom sheet EN": "Logic & Puzzle",
  "Nom EN": "Logic & Puzzle"
 },
 {
  "SKU": "102008/0",
  "FR": "Pizza et Horloge / Vierge",
  "EN": "Pizza & Clock / Pizza & Clock",
  "SKU Planche": "102008",
  "Nom Planche": "Pizza et Horloge",
  "Idpièce": 0,
  "Nom FR without special letters": "Pizza et Horloge",
  "Nom sheet EN": "Pizza & Clock",
  "Nom EN": "Pizza & Clock"
 },
 {
  "SKU": "102009/0",
  "FR": "Schema corporel fille / Vierge",
  "EN": "Girl Body Map / Girl Body Map",
  "SKU Planche": "102009",
  "Nom Planche": "Schema corporel fille",
  "Idpièce": 0,
  "Nom FR without special letters": "Schema corporel fille",
  "Nom sheet EN": "Girl Body Map",
  "Nom EN": "Girl Body Map"
 },
 {
  "SKU": "102010/0",
  "FR": "Schema corporel garcon / Vierge",
  "EN": "Boy Body Map / Boy Body Map",
  "SKU Planche": "102010",
  "Nom Planche": "Schema corporel garcon",
  "Idpièce": 0,
  "Nom FR without special letters": "Schema corporel garcon",
  "Nom sheet EN": "Boy Body Map",
  "Nom EN": "Boy Body Map"
 },
 {
  "SKU": "102011/0",
  "FR": "Fruits et Legumes / Vierge",
  "EN": "Fruits & Veggies / Fruits & VEGGIES",
  "SKU Planche": "102011",
  "Nom Planche": "Fruits et Legumes",
  "Idpièce": 0,
  "Nom FR without special letters": "Fruits et Legumes",
  "Nom sheet EN": "Fruits & Veggies",
  "Nom EN": "Fruits & VEGGIES"
 },
 {
  "SKU": "102012/0",
  "FR": "Saisons / Vierge",
  "EN": "Seasons / Seasons",
  "SKU Planche": "102012",
  "Nom Planche": "Saisons",
  "Idpièce": 0,
  "Nom FR without special letters": "Saisons",
  "Nom sheet EN": "Seasons",
  "Nom EN": "Seasons"
 },
 {
  "SKU": "102013/0",
  "FR": "Cadre spatial et Transport / Vierge",
  "EN": "Space Frame & Transport / Space Frame & Transport",
  "SKU Planche": "102013",
  "Nom Planche": "Cadre spatial et Transport",
  "Idpièce": 0,
  "Nom FR without special letters": "Cadre spatial et Transport",
  "Nom sheet EN": "Space Frame & Transport",
  "Nom EN": "Space Frame & Transport"
 },
 {
  "SKU": "102014/0",
  "FR": "Toucher et Memorisation / Vierge",
  "EN": "Touch & Memorization / Touch & Memorization",
  "SKU Planche": "102014",
  "Nom Planche": "Toucher et Memorisation",
  "Idpièce": 0,
  "Nom FR without special letters": "Toucher et Memorisation",
  "Nom sheet EN": "Touch & Memorization",
  "Nom EN": "Touch & Memorization"
 },
 {
  "SKU": "102015/0",
  "FR": "Animaux - Jungle et Ferme / Vierge",
  "EN": "Animals - Jungle & Farm / Animals - Jungle & Farm",
  "SKU Planche": "102015",
  "Nom Planche": "Animaux - Jungle et Ferme",
  "Idpièce": 0,
  "Nom FR without special letters": "Animaux - Jungle et Ferme",
  "Nom sheet EN": "Animals - Jungle & Farm",
  "Nom EN": "Animals - Jungle & Farm"
 },
 {
  "SKU": "102016/0",
  "FR": "Table / Vierge",
  "EN": "Table / Table",
  "SKU Planche": "102016",
  "Nom Planche": "Table",
  "Idpièce": 0,
  "Nom FR without special letters": "Table",
  "Nom sheet EN": "Table",
  "Nom EN": "Table"
 },
 {
  "SKU": "102017/0",
  "FR": "Animaux - mer et Dexterite / Vierge",
  "EN": "Sea Animals & Dexterity / Sea Animals & Dexterity",
  "SKU Planche": "102017",
  "Nom Planche": "Animaux - mer et Dexterite",
  "Idpièce": 0,
  "Nom FR without special letters": "Animaux - mer et Dexterite",
  "Nom sheet EN": "Sea Animals & Dexterity",
  "Nom EN": "Sea Animals & Dexterity"
 },
 {
  "SKU": "102018/0",
  "FR": "Animaux - Desert et Banquise / Vierge",
  "EN": "Animals - Desert & Pack Ice / Animals - Desert & Pack Ice",
  "SKU Planche": "102018",
  "Nom Planche": "Animaux - Desert et Banquise",
  "Idpièce": 0,
  "Nom FR without special letters": "Animaux - Desert et Banquise",
  "Nom sheet EN": "Animals - Desert & Pack Ice",
  "Nom EN": "Animals - Desert & Pack Ice"
 },
 {
  "SKU": "102019/0",
  "FR": "Emotions / Vierge",
  "EN": "Emotions / Emotions",
  "SKU Planche": "102019",
  "Nom Planche": "Emotions",
  "Idpièce": 0,
  "Nom FR without special letters": "Emotions",
  "Nom sheet EN": "Emotions",
  "Nom EN": "Emotions"
 },
 {
  "SKU": "102020/0",
  "FR": "Cycle - Eau et Fleur / Vierge",
  "EN": "Cycle - Water & Flower / Cycle - Water & Flower",
  "SKU Planche": "102020",
  "Nom Planche": "Cycle - Eau et Fleur",
  "Idpièce": 0,
  "Nom FR without special letters": "Cycle - Eau et Fleur",
  "Nom sheet EN": "Cycle - Water & Flower",
  "Nom EN": "Cycle - Water & Flower"
 },
 {
  "SKU": "102021/0",
  "FR": "Dessin et Ecriture / Vierge",
  "EN": "Drawing & Writing / Drawing & Writing",
  "SKU Planche": "102021",
  "Nom Planche": "Dessin et Ecriture",
  "Idpièce": 0,
  "Nom FR without special letters": "Dessin et Ecriture",
  "Nom sheet EN": "Drawing & Writing",
  "Nom EN": "Drawing & Writing"
 },
 {
  "SKU": "102022/0",
  "FR": "Vetements / Vierge",
  "EN": "Clothes / Clothes",
  "SKU Planche": "102022",
  "Nom Planche": "Vetements",
  "Idpièce": 0,
  "Nom FR without special letters": "Vetements",
  "Nom sheet EN": "Clothes",
  "Nom EN": "Clothes"
 }
],
"sheets":[
 {
  "EN": "Cycle - water & flower",
  "Part": "White cloud",
  "FR": "Cycle - eau et fleur",
  "Piece": "Nuage",
  "SKU": "102020 01",
  "Piece Atomicseller": "Nuage"
 },
 {
  "EN": "Cycle - water & flower",
  "Part": "Rain cloud",
  "FR": "Cycle - eau et fleur",
  "Piece": "Nuage pluie",
  "SKU": "102020 02",
  "Piece Atomicseller": "Nuage pluie"
 },
 {
  "EN": "Cycle - water & flower",
  "Part": "Snow",
  "FR": "Cycle - eau et fleur",
  "Piece": "Neige",
  "SKU": "102020 03",
  "Piece Atomicseller": "Neige"
 },
 {
  "EN": "Cycle - water & flower",
  "Part": "River",
  "FR": "Cycle - eau et fleur",
  "Piece": "Rivière",
  "SKU": "102020 04",
  "Piece Atomicseller": "Riviere"
 },
 {
  "EN": "Cycle - water & flower",
  "Part": "Blue sea",
  "FR": "Cycle - eau et fleur",
  "Piece": "Mer",
  "SKU": "102020 05",
  "Piece Atomicseller": "Mer"
 },
 {
  "EN": "Cycle - water & flower",
  "Part": "Pink flower",
  "FR": "Cycle - eau et fleur",
  "Piece": "Fleur",
  "SKU": "102020 06",
  "Piece Atomicseller": "Fleur"
 },
 {
  "EN": "Cycle - water & flower",
  "Part": "Hive",
  "FR": "Cycle - eau et fleur",
  "Piece": "Ruche",
  "SKU": "102020 07",
  "Piece Atomicseller": "Ruche"
 },
 {
  "EN": "Cycle - water & flower",
  "Part": "Red flower",
  "FR": "Cycle - eau et fleur",
  "Piece": "Rose",
  "SKU": "102020 08",
  "Piece Atomicseller": "Rose"
 },
 {
  "EN": "Cycle - water & flower",
  "Part": "Pistil",
  "FR": "Cycle - eau et fleur",
  "Piece": "Pistil",
  "SKU": "102020 09",
  "Piece Atomicseller": "Pistil"
 },
 {
  "EN": "Cycle - water & flower",
  "Part": "Bee",
  "FR": "Cycle - eau et fleur",
  "Piece": "Abeille",
  "SKU": "102020 10",
  "Piece Atomicseller": "Abeille"
 },
 {
  "EN": "Seasons",
  "Part": "Sun",
  "FR": "Saisons",
  "Piece": "Soleil",
  "SKU": "102012 01",
  "Piece Atomicseller": "Soleil"
 },
 {
  "EN": "Seasons",
  "Part": "Green tree",
  "FR": "Saisons",
  "Piece": "Arbre",
  "SKU": "102012 02",
  "Piece Atomicseller": "Arbre"
 },
 {
  "EN": "Seasons",
  "Part": "Grass",
  "FR": "Saisons",
  "Piece": "Sol vert",
  "SKU": "102012 03",
  "Piece Atomicseller": "Sol vert"
 },
 {
  "EN": "Seasons",
  "Part": "Dry grass",
  "FR": "Saisons",
  "Piece": "Sol orange",
  "SKU": "102012 04",
  "Piece Atomicseller": "Sol orange"
 },
 {
  "EN": "Seasons",
  "Part": "Sun",
  "FR": "Saisons",
  "Piece": "Soleil",
  "SKU": "102012 05",
  "Piece Atomicseller": "Soleil"
 },
 {
  "EN": "Seasons",
  "Part": "Flower",
  "FR": "Saisons",
  "Piece": "Fleur sans tige",
  "SKU": "102012 06",
  "Piece Atomicseller": "Fleur sans tige"
 },
 {
  "EN": "Seasons",
  "Part": "Flower with stem",
  "FR": "Saisons",
  "Piece": "Fleur avec tige",
  "SKU": "102012 07",
  "Piece Atomicseller": "Fleur avec tige"
 },
 {
  "EN": "Seasons",
  "Part": "Green leaf",
  "FR": "Saisons",
  "Piece": "Feuille d'arbre verte",
  "SKU": "102012 08",
  "Piece Atomicseller": "Feuille d arbre verte"
 },
 {
  "EN": "Seasons",
  "Part": "Red leaf",
  "FR": "Saisons",
  "Piece": "Feuille d'arbre rouge",
  "SKU": "102012 09",
  "Piece Atomicseller": "Feuille d arbre rouge"
 },
 {
  "EN": "Seasons",
  "Part": "Apple",
  "FR": "Saisons",
  "Piece": "Pomme",
  "SKU": "102012 10",
  "Piece Atomicseller": "Pomme"
 },
 {
  "EN": "Seasons",
  "Part": "Snowflake",
  "FR": "Saisons",
  "Piece": "Flocon de neige",
  "SKU": "102012 11",
  "Piece Atomicseller": "Flocon de neige"
 },
 {
  "EN": "Sea animals & dexterity",
  "Part": "Water pen",
  "FR": "Animaux - mer et dexterite",
  "Piece": "Stylo à eau",
  "SKU": "102017 01",
  "Piece Atomicseller": "Stylo a eau"
 },
 {
  "EN": "Clothes",
  "Part": "Boy head",
  "FR": "Vetements",
  "Piece": "Tête homme",
  "SKU": "102022 01",
  "Piece Atomicseller": "Tete homme"
 },
 {
  "EN": "Clothes",
  "Part": "Girl head",
  "FR": "Vetements",
  "Piece": "Tête femme",
  "SKU": "102022 02",
  "Piece Atomicseller": "Tete femme"
 },
 {
  "EN": "Clothes",
  "Part": "Pants",
  "FR": "Vetements",
  "Piece": "Pantalon",
  "SKU": "102022 03",
  "Piece Atomicseller": "Pantalon"
 },
 {
  "EN": "Clothes",
  "Part": "Shorts",
  "FR": "Vetements",
  "Piece": "Short",
  "SKU": "102022 04",
  "Piece Atomicseller": "Short"
 },
 {
  "EN": "Clothes",
  "Part": "Skirt",
  "FR": "Vetements",
  "Piece": "Jupe",
  "SKU": "102022 05",
  "Piece Atomicseller": "Jupe"
 },
 {
  "EN": "Clothes",
  "Part": "T-shirt",
  "FR": "Vetements",
  "Piece": "Tee-shirt",
  "SKU": "102022 06",
  "Piece Atomicseller": "Tee-shirt"
 },
 {
  "EN": "Clothes",
  "Part": "Sweater",
  "FR": "Vetements",
  "Piece": "Pull",
  "SKU": "102022 07",
  "Piece Atomicseller": "Pull"
 },
 {
  "EN": "Clothes",
  "Part": "Shirt",
  "FR": "Vetements",
  "Piece": "Chemise",
  "SKU": "102022 08",
  "Piece Atomicseller": "Chemise"
 },
 {
  "EN": "Clothes",
  "Part": "Dress",
  "FR": "Vetements",
  "Piece": "Robe",
  "SKU": "102022 09",
  "Piece Atomicseller": "Robe"
 },
 {
  "EN": "Clothes",
  "Part": "Shoes",
  "FR": "Vetements",
  "Piece": "Chaussures",
  "SKU": "102022 10",
  "Piece Atomicseller": "Chaussures"
 },
 {
  "EN": "Shapes - colors & sizes",
  "Part": "Rectangle",
  "FR": "Formes - couleurs et tailles",
  "Piece": "Rectangle",
  "SKU": "102004 01",
  "Piece Atomicseller": "Rectangle"
 },
 {
  "EN": "Shapes - colors & sizes",
  "Part": "Square",
  "FR": "Formes - couleurs et tailles",
  "Piece": "Carré",
  "SKU": "102004 02",
  "Piece Atomicseller": "Carre"
 },
 {
  "EN": "Shapes - colors & sizes",
  "Part": "Heart",
  "FR": "Formes - couleurs et tailles",
  "Piece": "Coeur",
  "SKU": "102004 03",
  "Piece Atomicseller": "Coeur"
 },
 {
  "EN": "Shapes - colors & sizes",
  "Part": "Diamond",
  "FR": "Formes - couleurs et tailles",
  "Piece": "Losange",
  "SKU": "102004 04",
  "Piece Atomicseller": "Losange"
 },
 {
  "EN": "Shapes - colors & sizes",
  "Part": "Circle",
  "FR": "Formes - couleurs et tailles",
  "Piece": "Cercle",
  "SKU": "102004 05",
  "Piece Atomicseller": "Cercle"
 },
 {
  "EN": "Shapes - colors & sizes",
  "Part": "Triangle",
  "FR": "Formes - couleurs et tailles",
  "Piece": "Triangle",
  "SKU": "102004 06",
  "Piece Atomicseller": "Triangle"
 },
 {
  "EN": "Shapes - colors & sizes",
  "Part": "Top",
  "FR": "Formes - couleurs et tailles",
  "Piece": "Taille 1",
  "SKU": "102004 07",
  "Piece Atomicseller": "Taille 1"
 },
 {
  "EN": "Shapes - colors & sizes",
  "Part": "Mid-top",
  "FR": "Formes - couleurs et tailles",
  "Piece": "Taille 2",
  "SKU": "102004 08",
  "Piece Atomicseller": "Taille 2"
 },
 {
  "EN": "Shapes - colors & sizes",
  "Part": "Middle",
  "FR": "Formes - couleurs et tailles",
  "Piece": "Taille 3",
  "SKU": "102004 09",
  "Piece Atomicseller": "Taille 3"
 },
 {
  "EN": "Shapes - colors & sizes",
  "Part": "Mid-bottom",
  "FR": "Formes - couleurs et tailles",
  "Piece": "Taille 4",
  "SKU": "102004 10",
  "Piece Atomicseller": "Taille 4"
 },
 {
  "EN": "Shapes - colors & sizes",
  "Part": "Bottom",
  "FR": "Formes - couleurs et tailles",
  "Piece": "Taille 5",
  "SKU": "102004 11",
  "Piece Atomicseller": "Taille 5"
 },
 {
  "EN": "Time frame - day & night",
  "Part": "Door",
  "FR": "Cadre temporel - jour et nuit",
  "Piece": "Porte",
  "SKU": "102006 01",
  "Piece Atomicseller": "Porte"
 },
 {
  "EN": "Time frame - day & night",
  "Part": "Yellow window",
  "FR": "Cadre temporel - jour et nuit",
  "Piece": "Fenêtre jaune",
  "SKU": "102006 02",
  "Piece Atomicseller": "Fenetre jaune"
 },
 {
  "EN": "Time frame - day & night",
  "Part": "Dark cloud",
  "FR": "Cadre temporel - jour et nuit",
  "Piece": "Nuage gris",
  "SKU": "102006 03",
  "Piece Atomicseller": "Nuage gris"
 },
 {
  "EN": "Time frame - day & night",
  "Part": "White cloud",
  "FR": "Cadre temporel - jour et nuit",
  "Piece": "Nuage blanc",
  "SKU": "102006 04",
  "Piece Atomicseller": "Nuage blanc"
 },
 {
  "EN": "Time frame - day & night",
  "Part": "Sun",
  "FR": "Cadre temporel - jour et nuit",
  "Piece": "Soleil",
  "SKU": "102006 05",
  "Piece Atomicseller": "Soleil"
 },
 {
  "EN": "Time frame - day & night",
  "Part": "White window",
  "FR": "Cadre temporel - jour et nuit",
  "Piece": "Fenêtre blanche",
  "SKU": "102006 06",
  "Piece Atomicseller": "Fenetre blanche"
 },
 {
  "EN": "Time frame - day & night",
  "Part": "Flash cloud",
  "FR": "Cadre temporel - jour et nuit",
  "Piece": "Nuage éclair",
  "SKU": "102006 07",
  "Piece Atomicseller": "Nuage eclair"
 },
 {
  "EN": "Time frame - day & night",
  "Part": "Rain cloud",
  "FR": "Cadre temporel - jour et nuit",
  "Piece": "Nuage pluie",
  "SKU": "102006 08",
  "Piece Atomicseller": "Nuage pluie"
 },
 {
  "EN": "Time frame - day & night",
  "Part": "Moon",
  "FR": "Cadre temporel - jour et nuit",
  "Piece": "Lune",
  "SKU": "102006 09",
  "Piece Atomicseller": "Lune"
 },
 {
  "EN": "Logic & puzzle",
  "Part": "Top-right",
  "FR": "Logique et puzzle",
  "Piece": "Puzzle - haut droite",
  "SKU": "102007 01",
  "Piece Atomicseller": "Puzzle - haut droite"
 },
 {
  "EN": "Logic & puzzle",
  "Part": "Top-left",
  "FR": "Logique et puzzle",
  "Piece": "Puzzle - haut gauche",
  "SKU": "102007 02",
  "Piece Atomicseller": "Puzzle - haut gauche"
 },
 {
  "EN": "Logic & puzzle",
  "Part": "Bottom-right",
  "FR": "Logique et puzzle",
  "Piece": "Puzzle - bas droite",
  "SKU": "102007 03",
  "Piece Atomicseller": "Puzzle - bas droite"
 },
 {
  "EN": "Logic & puzzle",
  "Part": "Bottom-left",
  "FR": "Logique et puzzle",
  "Piece": "Puzzle - bas gauche",
  "SKU": "102007 04",
  "Piece Atomicseller": "Puzzle - bas gauche"
 },
 {
  "EN": "Logic & puzzle",
  "Part": "Piece 1",
  "FR": "Logique et puzzle",
  "Piece": "Pièce 1",
  "SKU": "102007 05",
  "Piece Atomicseller": "Piece 1"
 },
 {
  "EN": "Logic & puzzle",
  "Part": "Piece 2",
  "FR": "Logique et puzzle",
  "Piece": "Pièce 2",
  "SKU": "102007 06",
  "Piece Atomicseller": "Piece 2"
 },
 {
  "EN": "Logic & puzzle",
  "Part": "Piece 3",
  "FR": "Logique et puzzle",
  "Piece": "Pièce 3",
  "SKU": "102007 07",
  "Piece Atomicseller": "Piece 3"
 },
 {
  "EN": "Logic & puzzle",
  "Part": "Piece 4",
  "FR": "Logique et puzzle",
  "Piece": "Pièce 4",
  "SKU": "102007 08",
  "Piece Atomicseller": "Piece 4"
 },
 {
  "EN": "Logic & puzzle",
  "Part": "Piece 5",
  "FR": "Logique et puzzle",
  "Piece": "Pièce 5",
  "SKU": "102007 09",
  "Piece Atomicseller": "Piece 5"
 },
 {
  "EN": "Logic & puzzle",
  "Part": "Piece 6",
  "FR": "Logique et puzzle",
  "Piece": "Pièce 6",
  "SKU": "102007 10",
  "Piece Atomicseller": "Piece 6"
 },
 {
  "EN": "Pizza & clock",
  "Part": "Pizza 1",
  "FR": "Pizza et horloge",
  "Piece": "Pizza part 1",
  "SKU": "102008 01",
  "Piece Atomicseller": "Pizza part 1"
 },
 {
  "EN": "Pizza & clock",
  "Part": "Pizza 2",
  "FR": "Pizza et horloge",
  "Piece": "Pizza part 2",
  "SKU": "102008 02",
  "Piece Atomicseller": "Pizza part 2"
 },
 {
  "EN": "Pizza & clock",
  "Part": "Pizza 3",
  "FR": "Pizza et horloge",
  "Piece": "Pizza part 3",
  "SKU": "102008 03",
  "Piece Atomicseller": "Pizza part 3"
 },
 {
  "EN": "Pizza & clock",
  "Part": "Pizza 4",
  "FR": "Pizza et horloge",
  "Piece": "Pizza part 4",
  "SKU": "102008 04",
  "Piece Atomicseller": "Pizza part 4"
 },
 {
  "EN": "Pizza & clock",
  "Part": "Pizza 5",
  "FR": "Pizza et horloge",
  "Piece": "Pizza part 5",
  "SKU": "102008 05",
  "Piece Atomicseller": "Pizza part 5"
 },
 {
  "EN": "Pizza & clock",
  "Part": "Pizza 6",
  "FR": "Pizza et horloge",
  "Piece": "Pizza part 6",
  "SKU": "102008 06",
  "Piece Atomicseller": "Pizza part 6"
 },
 {
  "EN": "Emotions",
  "Part": "Face 1",
  "FR": "Emotions",
  "Piece": "Face 1",
  "SKU": "102019 01",
  "Piece Atomicseller": "Face 1"
 },
 {
  "EN": "Emotions",
  "Part": "Face 2",
  "FR": "Emotions",
  "Piece": "Face 2",
  "SKU": "102019 02",
  "Piece Atomicseller": "Face 2"
 },
 {
  "EN": "Emotions",
  "Part": "Face 3",
  "FR": "Emotions",
  "Piece": "Face 3",
  "SKU": "102019 03",
  "Piece Atomicseller": "Face 3"
 },
 {
  "EN": "Emotions",
  "Part": "Face 4",
  "FR": "Emotions",
  "Piece": "Face 4",
  "SKU": "102019 04",
  "Piece Atomicseller": "Face 4"
 },
 {
  "EN": "Emotions",
  "Part": "Face 5",
  "FR": "Emotions",
  "Piece": "Face 5",
  "SKU": "102019 05",
  "Piece Atomicseller": "Face 5"
 },
 {
  "EN": "Emotions",
  "Part": "Face 6",
  "FR": "Emotions",
  "Piece": "Face 6",
  "SKU": "102019 06",
  "Piece Atomicseller": "Face 6"
 },
 {
  "EN": "Emotions",
  "Part": "Face 7",
  "FR": "Emotions",
  "Piece": "Face 7",
  "SKU": "102019 07",
  "Piece Atomicseller": "Face 7"
 },
 {
  "EN": "Emotions",
  "Part": "Face 8",
  "FR": "Emotions",
  "Piece": "Face 8",
  "SKU": "102019 08",
  "Piece Atomicseller": "Face 8"
 },
 {
  "EN": "Emotions",
  "Part": "Face 9",
  "FR": "Emotions",
  "Piece": "Face 9",
  "SKU": "102019 09",
  "Piece Atomicseller": "Face 9"
 },
 {
  "EN": "Emotions",
  "Part": "Face 10",
  "FR": "Emotions",
  "Piece": "Face 10",
  "SKU": "102019 10",
  "Piece Atomicseller": "Face 10"
 },
 {
  "EN": "Emotions",
  "Part": "Face 11",
  "FR": "Emotions",
  "Piece": "Face 11",
  "SKU": "102019 11",
  "Piece Atomicseller": "Face 11"
 },
 {
  "EN": "Emotions",
  "Part": "Face 12",
  "FR": "Emotions",
  "Piece": "Face 12",
  "SKU": "102019 12",
  "Piece Atomicseller": "Face 12"
 },
 {
  "EN": "Emotions",
  "Part": "Banana skin",
  "FR": "Emotions",
  "Piece": "Peau de banane",
  "SKU": "102019 13",
  "Piece Atomicseller": "Peau de banane"
 },
 {
  "EN": "Boy body map",
  "Part": "Hair",
  "FR": "Schema corporel garcon",
  "Piece": "Cheveux",
  "SKU": "102010 01",
  "Piece Atomicseller": "Cheveux"
 },
 {
  "EN": "Boy body map",
  "Part": "Eye",
  "FR": "Schema corporel garcon",
  "Piece": "Oeil",
  "SKU": "102010 02",
  "Piece Atomicseller": "Oeil"
 },
 {
  "EN": "Boy body map",
  "Part": "Nose",
  "FR": "Schema corporel garcon",
  "Piece": "Nez",
  "SKU": "102010 03",
  "Piece Atomicseller": "Nez"
 },
 {
  "EN": "Boy body map",
  "Part": "Right ear",
  "FR": "Schema corporel garcon",
  "Piece": "Oreille gauche",
  "SKU": "102010 04",
  "Piece Atomicseller": "Oreille gauche"
 },
 {
  "EN": "Boy body map",
  "Part": "Left ear",
  "FR": "Schema corporel garcon",
  "Piece": "Oreille droite",
  "SKU": "102010 05",
  "Piece Atomicseller": "Oreille droite"
 },
 {
  "EN": "Boy body map",
  "Part": "Mouth",
  "FR": "Schema corporel garcon",
  "Piece": "Bouche",
  "SKU": "102010 06",
  "Piece Atomicseller": "Bouche"
 },
 {
  "EN": "Boy body map",
  "Part": "Head",
  "FR": "Schema corporel garcon",
  "Piece": "Tête",
  "SKU": "102010 07",
  "Piece Atomicseller": "Tete"
 },
 {
  "EN": "Boy body map",
  "Part": "Torso",
  "FR": "Schema corporel garcon",
  "Piece": "Ventre",
  "SKU": "102010 08",
  "Piece Atomicseller": "Ventre"
 },
 {
  "EN": "Boy body map",
  "Part": "Right arm",
  "FR": "Schema corporel garcon",
  "Piece": "Bras droit",
  "SKU": "102010 09",
  "Piece Atomicseller": "Bras droit"
 },
 {
  "EN": "Boy body map",
  "Part": "Left arm",
  "FR": "Schema corporel garcon",
  "Piece": "Bras gauche",
  "SKU": "102010 10",
  "Piece Atomicseller": "Bras gauche"
 },
 {
  "EN": "Boy body map",
  "Part": "Right leg",
  "FR": "Schema corporel garcon",
  "Piece": "Jambe droite",
  "SKU": "102010 11",
  "Piece Atomicseller": "Jambe droite"
 },
 {
  "EN": "Boy body map",
  "Part": "Left leg",
  "FR": "Schema corporel garcon",
  "Piece": "Jambe gauche",
  "SKU": "102010 12",
  "Piece Atomicseller": "Jambe gauche"
 },
 {
  "EN": "Girl body map",
  "Part": "Hair",
  "FR": "Schema corporel fille",
  "Piece": "Cheveux",
  "SKU": "102009 01",
  "Piece Atomicseller": "Cheveux"
 },
 {
  "EN": "Girl body map",
  "Part": "Eye",
  "FR": "Schema corporel fille",
  "Piece": "Oeil",
  "SKU": "102009 02",
  "Piece Atomicseller": "Oeil"
 },
 {
  "EN": "Girl body map",
  "Part": "Nose",
  "FR": "Schema corporel fille",
  "Piece": "Nez",
  "SKU": "102009 03",
  "Piece Atomicseller": "Nez"
 },
 {
  "EN": "Girl body map",
  "Part": "Right ear",
  "FR": "Schema corporel fille",
  "Piece": "Oreille droite",
  "SKU": "102009 04",
  "Piece Atomicseller": "Oreille droite"
 },
 {
  "EN": "Girl body map",
  "Part": "Left ear",
  "FR": "Schema corporel fille",
  "Piece": "Oreille gauche",
  "SKU": "102009 05",
  "Piece Atomicseller": "Oreille gauche"
 },
 {
  "EN": "Girl body map",
  "Part": "Mouth",
  "FR": "Schema corporel fille",
  "Piece": "Bouche",
  "SKU": "102009 06",
  "Piece Atomicseller": "Bouche"
 },
 {
  "EN": "Girl body map",
  "Part": "Head",
  "FR": "Schema corporel fille",
  "Piece": "Tête",
  "SKU": "102009 07",
  "Piece Atomicseller": "Tete"
 },
 {
  "EN": "Girl body map",
  "Part": "Torso",
  "FR": "Schema corporel fille",
  "Piece": "Ventre",
  "SKU": "102009 08",
  "Piece Atomicseller": "Ventre"
 },
 {
  "EN": "Girl body map",
  "Part": "Right arm",
  "FR": "Schema corporel fille",
  "Piece": "Bras droit",
  "SKU": "102009 09",
  "Piece Atomicseller": "Bras droit"
 },
 {
  "EN": "Girl body map",
  "Part": "Left arm",
  "FR": "Schema corporel fille",
  "Piece": "Bras gauche",
  "SKU": "102009 10",
  "Piece Atomicseller": "Bras gauche"
 },
 {
  "EN": "Girl body map",
  "Part": "Right leg",
  "FR": "Schema corporel fille",
  "Piece": "Jambe droite",
  "SKU": "102009 11",
  "Piece Atomicseller": "Jambe droite"
 },
 {
  "EN": "Girl body map",
  "Part": "Left leg",
  "FR": "Schema corporel fille",
  "Piece": "Jambe gauche",
  "SKU": "102009 12",
  "Piece Atomicseller": "Jambe gauche"
 },
 {
  "EN": "Fruits & veggies",
  "Part": "Potato",
  "FR": "Fruits et legumes",
  "Piece": "Pomme de terre",
  "SKU": "102011 01",
  "Piece Atomicseller": "Pomme de terre"
 },
 {
  "EN": "Fruits & veggies",
  "Part": "Onion",
  "FR": "Fruits et legumes",
  "Piece": "Oignon",
  "SKU": "102011 02",
  "Piece Atomicseller": "Oignon"
 },
 {
  "EN": "Fruits & veggies",
  "Part": "Carrot",
  "FR": "Fruits et legumes",
  "Piece": "Carotte",
  "SKU": "102011 03",
  "Piece Atomicseller": "Carotte"
 },
 {
  "EN": "Fruits & veggies",
  "Part": "Tomato",
  "FR": "Fruits et legumes",
  "Piece": "Tomate",
  "SKU": "102011 04",
  "Piece Atomicseller": "Tomate"
 },
 {
  "EN": "Fruits & veggies",
  "Part": "Eggplant",
  "FR": "Fruits et legumes",
  "Piece": "Aubergine",
  "SKU": "102011 05",
  "Piece Atomicseller": "Aubergine"
 },
 {
  "EN": "Fruits & veggies",
  "Part": "Orange",
  "FR": "Fruits et legumes",
  "Piece": "Orange",
  "SKU": "102011 06",
  "Piece Atomicseller": "Orange"
 },
 {
  "EN": "Fruits & veggies",
  "Part": "Pineapple",
  "FR": "Fruits et legumes",
  "Piece": "Ananas",
  "SKU": "102011 07",
  "Piece Atomicseller": "Ananas"
 },
 {
  "EN": "Fruits & veggies",
  "Part": "Banana",
  "FR": "Fruits et legumes",
  "Piece": "Banane",
  "SKU": "102011 08",
  "Piece Atomicseller": "Banane"
 },
 {
  "EN": "Fruits & veggies",
  "Part": "Strawberry",
  "FR": "Fruits et legumes",
  "Piece": "Fraise",
  "SKU": "102011 09",
  "Piece Atomicseller": "Fraise"
 },
 {
  "EN": "Animals - desert & pack ice",
  "Part": "Camel",
  "FR": "Animaux - desert et banquise",
  "Piece": "Chameau",
  "SKU": "102018 01",
  "Piece Atomicseller": "Chameau"
 },
 {
  "EN": "Animals - desert & pack ice",
  "Part": "Vulture",
  "FR": "Animaux - desert et banquise",
  "Piece": "Vautour",
  "SKU": "102018 02",
  "Piece Atomicseller": "Vautour"
 },
 {
  "EN": "Animals - desert & pack ice",
  "Part": "Lizzard",
  "FR": "Animaux - desert et banquise",
  "Piece": "Lézard",
  "SKU": "102018 03",
  "Piece Atomicseller": "Lezard"
 },
 {
  "EN": "Animals - desert & pack ice",
  "Part": "Snake",
  "FR": "Animaux - desert et banquise",
  "Piece": "Serpent",
  "SKU": "102018 04",
  "Piece Atomicseller": "Serpent"
 },
 {
  "EN": "Animals - desert & pack ice",
  "Part": "Scorpion",
  "FR": "Animaux - desert et banquise",
  "Piece": "Scorpion",
  "SKU": "102018 05",
  "Piece Atomicseller": "Scorpion"
 },
 {
  "EN": "Animals - desert & pack ice",
  "Part": "Pinguin",
  "FR": "Animaux - desert et banquise",
  "Piece": "Penguin",
  "SKU": "102018 06",
  "Piece Atomicseller": "Penguin"
 },
 {
  "EN": "Animals - desert & pack ice",
  "Part": "Polar bear",
  "FR": "Animaux - desert et banquise",
  "Piece": "Ours polaire",
  "SKU": "102018 07",
  "Piece Atomicseller": "Ours polaire"
 },
 {
  "EN": "Animals - desert & pack ice",
  "Part": "White wolf",
  "FR": "Animaux - desert et banquise",
  "Piece": "Loup blanc",
  "SKU": "102018 08",
  "Piece Atomicseller": "Loup blanc"
 },
 {
  "EN": "Animals - desert & pack ice",
  "Part": "Sea lion",
  "FR": "Animaux - desert et banquise",
  "Piece": "Phoque",
  "SKU": "102018 09",
  "Piece Atomicseller": "Phoque"
 },
 {
  "EN": "Animals - desert & pack ice",
  "Part": "Whale",
  "FR": "Animaux - desert et banquise",
  "Piece": "Baleine",
  "SKU": "102018 10",
  "Piece Atomicseller": "Baleine"
 },
 {
  "EN": "Table",
  "Part": "Cup",
  "FR": "Table",
  "Piece": "Verre",
  "SKU": "102016 01",
  "Piece Atomicseller": "Verre"
 },
 {
  "EN": "Table",
  "Part": "Mug",
  "FR": "Table",
  "Piece": "Tasse",
  "SKU": "102016 02",
  "Piece Atomicseller": "Tasse"
 },
 {
  "EN": "Table",
  "Part": "Plate",
  "FR": "Table",
  "Piece": "Assiette",
  "SKU": "102016 03",
  "Piece Atomicseller": "Assiette"
 },
 {
  "EN": "Table",
  "Part": "Fork",
  "FR": "Table",
  "Piece": "Fourchette",
  "SKU": "102016 04",
  "Piece Atomicseller": "Fourchette"
 },
 {
  "EN": "Table",
  "Part": "Spoon",
  "FR": "Table",
  "Piece": "Cuillère",
  "SKU": "102016 05",
  "Piece Atomicseller": "Cuillere"
 },
 {
  "EN": "Table",
  "Part": "Knife",
  "FR": "Table",
  "Piece": "Couteau",
  "SKU": "102016 06",
  "Piece Atomicseller": "Couteau"
 },
 {
  "EN": "Table",
  "Part": "Lamp",
  "FR": "Table",
  "Piece": "Lampe",
  "SKU": "102016 07",
  "Piece Atomicseller": "Lampe"
 },
 {
  "EN": "Table",
  "Part": "Vase",
  "FR": "Table",
  "Piece": "Vase",
  "SKU": "102016 08",
  "Piece Atomicseller": "Vase"
 },
 {
  "EN": "Table",
  "Part": "Platter",
  "FR": "Table",
  "Piece": "Petite assiette",
  "SKU": "102016 09",
  "Piece Atomicseller": "Petite assiette"
 },
 {
  "EN": "Table",
  "Part": "Table",
  "FR": "Table",
  "Piece": "Table",
  "SKU": "102016 10",
  "Piece Atomicseller": "Table"
 },
 {
  "EN": "Table",
  "Part": "Chair",
  "FR": "Table",
  "Piece": "Chaise",
  "SKU": "102016 11",
  "Piece Atomicseller": "Chaise"
 },
 {
  "EN": "Space frame & transport",
  "Part": "Plane",
  "FR": "Cadre spatial et transport",
  "Piece": "Avion",
  "SKU": "102013 01",
  "Piece Atomicseller": "Avion"
 },
 {
  "EN": "Space frame & transport",
  "Part": "Boat",
  "FR": "Cadre spatial et transport",
  "Piece": "Bateau",
  "SKU": "102013 02",
  "Piece Atomicseller": "Bateau"
 },
 {
  "EN": "Space frame & transport",
  "Part": "Car",
  "FR": "Cadre spatial et transport",
  "Piece": "Voiture",
  "SKU": "102013 03",
  "Piece Atomicseller": "Voiture"
 },
 {
  "EN": "Space frame & transport",
  "Part": "Butterfly",
  "FR": "Cadre spatial et transport",
  "Piece": "Papillon",
  "SKU": "102013 04",
  "Piece Atomicseller": "Papillon"
 },
 {
  "EN": "Space frame & transport",
  "Part": "Turtle",
  "FR": "Cadre spatial et transport",
  "Piece": "Tortue",
  "SKU": "102013 05",
  "Piece Atomicseller": "Tortue"
 },
 {
  "EN": "Space frame & transport",
  "Part": "Rabbit",
  "FR": "Cadre spatial et transport",
  "Piece": "Lapin",
  "SKU": "102013 06",
  "Piece Atomicseller": "Lapin"
 },
 {
  "EN": "Space frame & transport",
  "Part": "Fish 1",
  "FR": "Cadre spatial et transport",
  "Piece": "Poisson mauve",
  "SKU": "102013 07",
  "Piece Atomicseller": "Poisson mauve"
 },
 {
  "EN": "Space frame & transport",
  "Part": "Fish 2",
  "FR": "Cadre spatial et transport",
  "Piece": "Poisson orange",
  "SKU": "102013 08",
  "Piece Atomicseller": "Poisson orange"
 },
 {
  "EN": "Animals - jungle & farm",
  "Part": "Horse",
  "FR": "Animaux - jungle et ferme",
  "Piece": "Cheval",
  "SKU": "102015 01",
  "Piece Atomicseller": "Cheval"
 },
 {
  "EN": "Animals - jungle & farm",
  "Part": "Cow",
  "FR": "Animaux - jungle et ferme",
  "Piece": "Vache",
  "SKU": "102015 02",
  "Piece Atomicseller": "Vache"
 },
 {
  "EN": "Animals - jungle & farm",
  "Part": "Chicken",
  "FR": "Animaux - jungle et ferme",
  "Piece": "Poule",
  "SKU": "102015 03",
  "Piece Atomicseller": "Poule"
 },
 {
  "EN": "Animals - jungle & farm",
  "Part": "Goat",
  "FR": "Animaux - jungle et ferme",
  "Piece": "Chèvre",
  "SKU": "102015 04",
  "Piece Atomicseller": "Chevre"
 },
 {
  "EN": "Animals - jungle & farm",
  "Part": "Sheep",
  "FR": "Animaux - jungle et ferme",
  "Piece": "Mouton",
  "SKU": "102015 05",
  "Piece Atomicseller": "Mouton"
 },
 {
  "EN": "Animals - jungle & farm",
  "Part": "Pig",
  "FR": "Animaux - jungle et ferme",
  "Piece": "Cochon",
  "SKU": "102015 06",
  "Piece Atomicseller": "Cochon"
 },
 {
  "EN": "Animals - jungle & farm",
  "Part": "Lion",
  "FR": "Animaux - jungle et ferme",
  "Piece": "Lion",
  "SKU": "102015 07",
  "Piece Atomicseller": "Lion"
 },
 {
  "EN": "Animals - jungle & farm",
  "Part": "Elephant",
  "FR": "Animaux - jungle et ferme",
  "Piece": "Eléphant",
  "SKU": "102015 08",
  "Piece Atomicseller": "Elephant"
 },
 {
  "EN": "Animals - jungle & farm",
  "Part": "Monkey",
  "FR": "Animaux - jungle et ferme",
  "Piece": "Singe",
  "SKU": "102015 09",
  "Piece Atomicseller": "Singe"
 },
 {
  "EN": "Animals - jungle & farm",
  "Part": "Giraffe",
  "FR": "Animaux - jungle et ferme",
  "Piece": "Giraffe",
  "SKU": "102015 10",
  "Piece Atomicseller": "Giraffe"
 },
 {
  "EN": "Animals - jungle & farm",
  "Part": "Hippo",
  "FR": "Animaux - jungle et ferme",
  "Piece": "Hippopotame",
  "SKU": "102015 11",
  "Piece Atomicseller": "Hippopotame"
 },
 {
  "EN": "Animals - jungle & farm",
  "Part": "Zebra",
  "FR": "Animaux - jungle et ferme",
  "Piece": "Zèbre",
  "SKU": "102015 12",
  "Piece Atomicseller": "Zebre"
 },
 {
  "EN": "Touch & memorization",
  "Part": "Colorful fish",
  "FR": "Toucher et memorisation",
  "Piece": "Colorful fish",
  "SKU": "102014 01",
  "Piece Atomicseller": "Poisson colore"
 },
 {
  "EN": "Touch & memorization",
  "Part": "Green triangle",
  "FR": "Toucher et memorisation",
  "Piece": "Triangle vert",
  "SKU": "102014 02",
  "Piece Atomicseller": "Triangle vert"
 },
 {
  "EN": "Touch & memorization",
  "Part": "Yellow hexagone",
  "FR": "Toucher et memorisation",
  "Piece": "Hexagone jaune",
  "SKU": "102014 03",
  "Piece Atomicseller": "Hexagone jaune"
 },
 {
  "EN": "Touch & memorization",
  "Part": "Red trapezoid",
  "FR": "Toucher et memorisation",
  "Piece": "Trapèze",
  "SKU": "102014 04",
  "Piece Atomicseller": "Trapeze"
 },
 {
  "EN": "Touch & memorization",
  "Part": "Blue parallelogram",
  "FR": "Toucher et memorisation",
  "Piece": "Parallélogramme bleu",
  "SKU": "102014 05",
  "Piece Atomicseller": "Parallelogramme bleu"
 },
 {
  "EN": "Touch & memorization",
  "Part": "White diamond",
  "FR": "Toucher et memorisation",
  "Piece": "Losange blanc",
  "SKU": "102014 06",
  "Piece Atomicseller": "Losange blanc"
 },
 {
    "EN": "Cover board",
    "Part": "Mirror",
    "FR": "Planche de couverture",
    "Piece": "Miroir",
    "SKU": "101001 01",
    "Piece Atomicseller": "Miroir"
   },
   {
    "EN": "Cover board",
    "Part": "Cover board blank",
    "FR": "Planche de couverture",
    "Piece": "Planche de couverture vierge",
    "SKU": "101001 00",
    "Piece Atomicseller": "Planche de couverture vierge"
   },
 {
  "EN": "Shapes - colors & sizes",
  "Part": "Shapes - colors & sizes blank",
  "FR": "Formes - couleurs et tailles",
  "Piece": "Formes - couleurs et tailles vierge",
  "SKU": "102004 00",
  "Piece Atomicseller": "Formes - couleurs et tailles vierge"
 },
 {
  "EN": "Time frame - day & night",
  "Part": "Time frame - day & night blank",
  "FR": "Cadre temporel - jour et nuit",
  "Piece": "Cadre temporel - jour et nuit vierge",
  "SKU": "102006 00",
  "Piece Atomicseller": "Cadre temporel - jour et nuit vierge"
 },
 {
  "EN": "Logic & puzzle",
  "Part": "Logic & puzzle blank",
  "FR": "Logique et puzzle",
  "Piece": "Logique et puzzle vierge",
  "SKU": "102007 00",
  "Piece Atomicseller": "Logique et puzzle vierge"
 },
 {
  "EN": "Pizza & clock",
  "Part": "Pizza & clock blank",
  "FR": "Pizza et horloge",
  "Piece": "Pizza et horloge vierge",
  "SKU": "102008 00",
  "Piece Atomicseller": "Pizza et horloge vierge"
 },
 {
  "EN": "Girl body map",
  "Part": "Girl body map blank",
  "FR": "Schema corporel fille",
  "Piece": "Schéma corporel fille vierge",
  "SKU": "102009 00",
  "Piece Atomicseller": "Schema corporel fille vierge"
 },
 {
  "EN": "Boy body map",
  "Part": "Boy body map blank",
  "FR": "Schema corporel garcon",
  "Piece": "Schéma corporel garcon vierge",
  "SKU": "102010 00",
  "Piece Atomicseller": "Schema corporel garcon vierge"
 },
 {
  "EN": "Fruits & veggies",
  "Part": "Fruits & veggies blank",
  "FR": "Fruits et legumes",
  "Piece": "Fruits et légumes vierge",
  "SKU": "102011 00",
  "Piece Atomicseller": "Fruits et legumes vierge"
 },
 {
  "EN": "Seasons",
  "Part": "Seasons blank",
  "FR": "Saisons",
  "Piece": "Saisons vierge",
  "SKU": "102012 00",
  "Piece Atomicseller": "Saisons vierge"
 },
 {
  "EN": "Space frame & transport",
  "Part": "Space frame & transport blank",
  "FR": "Cadre spatial et transport",
  "Piece": "Cadre spatial et transport vierge",
  "SKU": "102013 00",
  "Piece Atomicseller": "Cadre spatial et transport vierge"
 },
 {
  "EN": "Touch & memorization",
  "Part": "Touch & memorization blank",
  "FR": "Toucher et memorisation",
  "Piece": "Toucher et mémorisation vierge",
  "SKU": "102014 00",
  "Piece Atomicseller": "Toucher et memorisation vierge"
 },
 {
  "EN": "Animals - jungle & farm",
  "Part": "Animals - jungle & farm blank",
  "FR": "Animaux - jungle et ferme",
  "Piece": "Animaux - jungle et ferme vierge",
  "SKU": "102015 00",
  "Piece Atomicseller": "Animaux - jungle et ferme vierge"
 },
 {
  "EN": "Table",
  "Part": "Table blank",
  "FR": "Table",
  "Piece": "Table vierge",
  "SKU": "102016 00",
  "Piece Atomicseller": "Table vierge"
 },
 {
  "EN": "Animals - desert & ice",
  "Part": "Animals - desert & ice blank",
  "FR": "Animaux - desert et banquise",
  "Piece": "Animaux - desert et banquise vierge",
  "SKU": "102018 00",
  "Piece Atomicseller": "Animaux - desert et banquise vierge"
 },
 {
  "EN": "Emotions",
  "Part": "Emotions blank",
  "FR": "Emotions",
  "Piece": "Emotions vierge",
  "SKU": "102019 00",
  "Piece Atomicseller": "Emotions vierge"
 },
 {
  "EN": "Cycle - water & flower",
  "Part": "Cycle - water & flower blank",
  "FR": "Cycle - eau et fleur",
  "Piece": "Cycle - eau et fleur vierge",
  "SKU": "102020 00",
  "Piece Atomicseller": "Cycle - eau et fleur vierge"
 },
 {
  "EN": "Clothes",
  "Part": "Clothes blank",
  "FR": "Vetements",
  "Piece": "Vêtements vierge",
  "SKU": "102022 00",
  "Piece Atomicseller": "Vetements vierge"
 }
]
}
processed_data = []
def removeDigits(s):
    answer = []
    for char in s:
        if not char.isdigit():
            answer.append(char)
    return ''.join(answer)
def remove_accents(text):
    return unidecode(text)
def remove_emoji(string):
    return emoji.replace_emoji(string, replace='')
def process_prénom(value):
    if value and value.strip():  
        return ','.join(char for char in value if char != ' ')
    return ''
def transform_date_string(date_string):
    try:
        parts = date_string.split('/')
        first_part = parts[0]
        second_part = parts[1].zfill(2)  # Pad with a leading zero if necessary
        transformed_string = first_part + second_part
        return transformed_string
    except:
        return date_string
def checklangauge(value):
    global checklang
    products=value.upper()
    products_list = products.split(',')
    products_list = [product.replace("&AMP;", "&").replace("Ö", "O").replace("Ä", "A").replace("Ü", "U") for product in products_list]
    for i in range(len(products_list)):
        products_list[i] = re.sub(r'd{2,}', '', products_list[i])
    products_list=[s.strip() for s in products_list]
    type_1 = []
    type_2 = []
    type_3 = []

    # Regular expressions for matching
    regex_type_2 = re.compile(r'^\d{6} /[0-9]+ .+')
    regex_type_3 = re.compile(r'^\d{6} .+')

    # Categorize each string into one of the three types
    for string in products_list:
        if string.isalpha() or ' ' in string and all(word.isalpha() for word in string.split()):
            type_1.append(string)
        elif regex_type_2.match(string):
            type_2.append(string)
        elif regex_type_3.match(string):
            type_3.append(string)
    if type_1:
        first_product = type_1[0]
        try:
            if first_product=='TABLE':
                first_product = type_1[1]
            if first_product=='EMOTIONS':
                first_product = type_1[1]
            for row in  productslist["Products"]:
                product = row['FR']
                product_upper = product.upper()
                if product_upper==first_product:
                    checklang='fr'
                product = row['EN']
                product_upper = product.upper()
                if product_upper==first_product:
                    checklang='en'
                product = row['DE']
                product_upper = product.upper()
                if product_upper==first_product:
                    checklang='de'
        except:
            checklang='de'
    else:
        checklang='de'
def process_value(key, value, prénom_encountered):
    global prename
    if key == "Prénom":
        if prénom_encountered:
            prename=value
            return '' + process_prénom(value)
        else:
            return process_prénom(value)
    if key == "Child Name":
        if prénom_encountered:
            prename=value
            return '' + process_prénom(value)
        else:
            return process_prénom(value) 
    if key == "Vorname":
        if prénom_encountered:
            prename=value
            return '' + process_prénom(value)
        else:
            return process_prénom(value)  
    else:
        return value
def transform_number_in_string(input_string):
    parts = input_string.split()
    if len(parts) >= 2:
        modified_number = parts[1].replace('0', '/')
        modified_string = f"{parts[0]} {modified_number} {' '.join(parts[2:])}"
        return modified_string
    return input_string
def compare_products( products):
    products_list = products.split(',')
    products_upper = [product.upper() for product in products_list]
    products_upper = [product.replace("&AMP;", "&").replace("Ö", "O").replace("Ä", "A").replace("Ü", "U") for product in products_upper]
    products_upper=[s.strip() for s in products_upper]
  
    matched_values = []
    type_1 = []
    type_2 = []
    type_3 = []
    type_4 = []
    type_sku = []
    # Regular expressions for matching
    regex_type_2 = re.compile(r'^\d{6} /[0-9]+ .+')
    regex_type_3 = re.compile(r'^\d{6} .+')
    regex_type_4 = re.compile(r'^\d{6} \d{2} .+')
    regex_sku = re.compile(r'^\d{6} \d{2}$')

    # Categorize each string into one of the three types
    for string in products_upper:
        if string.isalpha() or ' ' in string and all(word.isalpha() for word in string.split()):
            type_1.append(string)
        elif regex_sku.match(string):
            type_sku.append(string)
        elif regex_type_2.match(string):
            type_2.append(string)
        elif regex_type_4.match(string):  # Check for the new type first
            string=transform_number_in_string(string)
            type_2.append(string)
        elif regex_type_3.match(string):
            type_3.append(string)
    number_parts = [item.split()[0] for item in type_3]
    
    number_and_identifiers_no_space = [item.split()[0] + item.split()[1] for item in type_2]
    for row in productslist['Products']:
        product = row['SKU']
        product_upper = product.upper()
        for pro in number_parts:
            if pro==product_upper:
                matched_values.append(row)
    for row in productslist['sheets']:
        product = row['SKU']
        product_upper = product.upper()
        for pro in type_sku:
            if pro==product_upper:
                matched_values.append(row)
    for row in productslist['Aftersale']:
        product = row['SKU']
        product_upper = product.upper()
        for pro in number_and_identifiers_no_space:
            if pro==product_upper:
                matched_values.append(row)
    for row in productslist['Products']:
        if checklang == "fr":
            product = row['FR']
        elif checklang == "de":
            product = row['DE']
        elif checklang == "en":
            product = row['EN']
        else:
            product = row['FR']
        product_upper = product.upper()
        for pro in type_1:
            if pro==product_upper:
                matched_values.append(row)
    return matched_values
@app.post("/process_data")
async def process_data(request: Request):
    data= await request.json()
    modified_data = []
    totalwieght=0
    for d in data:
     if not d["shipping_country"]=="CH":
        d["StoreKey"] = "KITIMIMI"
        d["OrderType"] = "Sell" 
        full_name = d["shipping_full_name"]  
        first_name, last_name = full_name.split(maxsplit=1) 
        
        static_fields_to_remove = [key for key in d.keys() if key.startswith("static_field")]
        for key in list(d.keys()):
            if key.startswith("order_number"):
                new_key = "OrderKey" + key[len("order_number"):]
                d[new_key] = d.pop(key)
        for key in list(d.keys()):
            if key.startswith("order_date"):
                new_key = "OrderDate" + key[len("order_date"):]
                d[new_key] = d.pop(key)
        for key in static_fields_to_remove:
            del d[key]
        prénom_encountered = False
        products = d.get('products', [])
        result = []
        target_keys = ["Prénom", "Child Name", "Vorname"]
        formatted_data = {}
        for product in products:
            final_result=''
            processed_values = []
            for key, value in product.items():
                value = remove_accents(value)
                if key not in target_keys and value is not None and value != '':
                    checklangauge(value)
                    break
            for key, value in product.items():
                value = remove_accents(value)
                if value is not None and value != '' and key!="Ref":
                    value_without_emojis = remove_emoji(value)
                    if key == "Prénom":
                        prénom_encountered = True
                        if "CheckoutMessage" not in d:
                            d["CheckoutMessage"] =remove_accents(value) 
                        else:
                            d["CheckoutMessage"] =d["CheckoutMessage"] +" ,"+ remove_accents(value)    
                    if key == "Child Name":
                        prénom_encountered = True
                        if "CheckoutMessage" not in d:
                            d["CheckoutMessage"] =remove_accents(value) 
                        else:
                            d["CheckoutMessage"] =d["CheckoutMessage"] +" ,"+ remove_accents(value)
                    if key == "Vorname":
                        prénom_encountered = True
                        if "CheckoutMessage" not in d:
                            d["CheckoutMessage"] =remove_accents(value) 
                        else:
                            d["CheckoutMessage"] =d["CheckoutMessage"] +" ,"+ remove_accents(value)  
                    processed_value = process_value(key, value_without_emojis, prénom_encountered)
                    if r"u00é" in processed_value:
                        processed_value = processed_value.replace(r'u00é', 'e')
                    if r"é" in processed_value:
                        processed_value = processed_value.replace(r'é', 'e')
                    if r"ç" in processed_value:
                        processed_value = processed_value.replace(r'ç', 'c')
                    processed_values.append(processed_value)
            result.append(','.join(processed_values))
            final_result = ','.join(result)
            checking=compare_products(final_result)
            result=[]
            for item in checking:
                sku =item['SKU'] 
                sku=transform_date_string(sku)
                quantity = 1  # Quantity is the sixth element
                try:
                    weight = int(item['Weight (g)'])
                except (KeyError, ValueError):
                    weight = 0 
                ProductName=item['FR']  
                totalwieght=weight+totalwieght
                if sku not in formatted_data:
                    formatted_data[sku] = {
                        "SKU": sku,
                        "Quantity": quantity,
                        "ProductName": ProductName,  # Empty for now, will be filled later
                        "CN23Category": "",
                        "PriceExclTax": "",
                        "Weight": weight,
                        "EANCode": "",
                        "VariationID": "",
                        "VAT": ""
                    }
                else:
                    formatted_data[sku]["Quantity"] += quantity
        # Convert the dictionary to a list of formatted dictionaries
        formatted_list = list(formatted_data.values())
        del d['products']
        d["products"] = formatted_list
        d["Delivery"] = {
        "Recipient":{
                    "RecipLanguageCode":"FR",
                    "RecipCompanyName":"",
                    "RecipFirstName":remove_accents(first_name),
                    "RecipLastName":remove_accents(last_name),
                    "RecipAdr2":"",
                    "RecipAdr1":remove_accents(d["shipping_address_2"]),
                    "RecipAdr0":remove_accents(d["shipping_address_1"]),
                    "RecipZipCode":remove_accents(d["shipping_postcode"]),
                    "RecipCity":remove_accents(d["shipping_city"]),
                    "RecipCountryCode":remove_accents(d["shipping_country"]),
                    "RecipCountryLib":remove_accents(d["shipping_country_full"]),
                    "Recipemail":remove_accents(d["billing_email"]),
                    "RecipMobileNumber":"",
                    "RecipPhoneNumber":d["shipping_phone"],
                    "DeliveryRelayCountry":"",
                    "DeliveryRelayNumber":""
                },
                "Parcel":{
                    "ShippingServiceKey":"DPDKITIMIMI",
                    "ShippingProductCode":"PREDICT",
                    "InsurranceYN":"",
                    "InsurranceCurrency":"",
                    "ParcelValueCurrency":"",
                    "ParcelWeight":totalwieght,
                    "WeightUnit":"g",
                    "DeliveryInstructions1":prename
                },
                "Sender":{
                    "SenderLanguageCode":"FR",
                    "SenderAdr2":"51 Rue de Toufflers",
                    "SenderAdr3":"POUR KITIMIMI",
                    "Sendercity":" Lys-lez-Lannoy",
                    "SenderzipCode":"59390",
                    "SendercompanyName":" Stock logistic",
                    "SendercountryCode":"FR",
                    "SendercountryLib":"FRANCE",
                    "SenderphoneNumber":"0033320200909",
                    "Senderemail":"hello@kitimimi.com"
                }

    }   
        totalwieght=0
        if 'billing_email' in d:
            del d['billing_email']
        if 'order_number' in d:
            del d['order_number']
        if 'shipping_address_1' in d:
            del d['shipping_address_1']
        if 'shipping_address_2' in d:
            del d['shipping_address_2']
        if 'shipping_city' in d:
            del d['shipping_city']
        if 'shipping_country' in d:
            del d['shipping_country']
        if 'shipping_full_name' in d:
            del d['shipping_full_name']
        if 'shipping_phone' in d:
            del d['shipping_phone']
        if 'shipping_postcode' in d:
            del d['shipping_postcode']
        if 'shipping_country_full' in d:
            del d['shipping_country_full']
        if 'order_total_inc_refund' in d:
            del d['order_total_inc_refund']
        if 'order_total_tax_minus_refund' in d:
            del d['order_total_tax_minus_refund']
        if 'payment_method' in d:
            del d['payment_method']
        modified_data.append(d)
    # Construct response data
    response_data ={
        "Request": 
    {
        "Orders": modified_data,
    }}
    # file_name = "response_data.json"
    # with open(file_name, "w") as json_file:
    #     json.dump(response_data, json_file)
    
    # headers = {
    #     "Token": "KEy5YrFM3EieHYc+CSoFTZlFBtVonvat" 
    # } 
    # api_url = "https://sl.atomicseller.com/Api/Order/CreateOrders"
    # response = requests.post(
    #     url=api_url,
    #     json=response_data,
    #     headers=headers,
    # )
    print(response_data)

    # if response.status_code == 200:
    #     print("Response sent successfully.")
    # else:
    #    print("Failed to send response. Status code:", response.status_code)

# @app.post("/get_data")
# async def get_data(dates:Request):
#     request_data = await dates.json()
#     # Extract start_date and end_date from the request body
#     start_date = request_data.get("start_date")
#     end_date = request_data.get("end_date")
#     response_data ={
#    "Header":   {
#         "Token": "KEy5YrFM3EieHYc+CSoFTZlFBtVonvat" 
#     },   "Request": 
#     {
#         "StoreKey": "KITIMIMI",
#         "CreatedFromTime":start_date,
#         "UpdatedFromTime":end_date
#     }}
#     api_url = "https://sl.atomicseller.com/Api/Delivery/GetDeliveries"
#     response = requests.get(
#         url=api_url,
#         json=response_data,
#     )

#     data = response.json()
#     # with open('data.json', 'w') as json_file:
#     #     json.dump(data, json_file, indent=4)
#     # print(data)
#     for key in data['Response']['Deliveries']:
#         print(key['Delivery']['TrackingNumber'])
#         print(key['Order']['OrderKey'])
#         if key['Delivery']['TrackingNumber']!='':
#             order={key['Order']['OrderKey']}
#             string = order.pop()
#             last_five_chars = string[-5:]
#             url = f"https://kitimimi.com/wp-json/wc-shipment-tracking/v3/orders/{last_five_chars}/shipment-trackings"
#             print(last_five_chars)
#             payload ={
#             "tracking_provider": "DPD France",
#             "tracking_number": key['Delivery']['TrackingNumber'],
#             "status_shipped": 1,
#             "replace_tracking": 1
#         }
#             headers = {
#             'Authorization': 'Basic Y2tfNDVjNTRiMmFkZjNjNjNlNTIwNjBkM2ZmY2E1NDFkZTg4YjcxYjc5Yjpjc18yZjQ4NDZiNTBhYzVmNmZlNjk3OGNjMzllMTcyNDRjODRhYTVkZmFi',
#             'Cookie': 'aelia_cs_selected_currency=EUR; aelia_customer_country=PK; wfwaf-authcookie-6f4abdd7a72b5bd7453008536b22a4ea=1%7Cadministrator%7Cmanage_options%2Cunfiltered_html%2Cedit_others_posts%2Cupload_files%2Cpublish_posts%2Cedit_posts%2Cread%2Cmanage_network%7Cd2272d76759d97df144fcb2810f0342fa6a6c498ae165e61484e709b25407963; wp-wpml_current_admin_language_d41d8cd98f00b204e9800998ecf8427e=en'
#             }
#             response = requests.request("POST", url, headers=headers, data=payload)

#             print(response.text)

    # consumer_key = 'ck_e52f312ff798091b0fb498ddb12aea1dfb7f5bc0'
    # consumer_secret = 'cs_7ac5a12e9100834003914596970ba994556afe59'
    # order_id = '57592'
    # url = f'https://kitimimi.com/wp-json/wc-shipment-tracking/v3/orders/{order_id}/shipment-tracking'
    # tracking_data = {
    #     "tracking_provider": "DPD France",
    #     "tracking_number": "10593007600016",
    #     "date_shipped": "2019-04-29",
    #     "status_shipped": 1,
    #     "replace_tracking": 1
    # }

    # # Send the request
    # response = requests.post(url, json=tracking_data, auth=(consumer_key, consumer_secret), headers={'Content-Type': 'application/json'})

    # # Check the response
    # if response.status_code == 200:
    #     print("Tracking information updated successfully.",response)
    # else:
    #     print("Failed to update tracking information. Status code:", response.status_code)
    #     print("Response:", response.text)


@app.post("/dummypath")
async def get_body(request: Request):
    data= await request.json()
    for d in data:
        print(d)

@app.on_event('startup')
@repeat_at(cron="26 15 * * *")
async def print_hello():
    today = datetime.today().strftime('%Y-%m-%d')
    response_data ={
   "Header":   {
        "Token": "KEy5YrFM3EieHYc+CSoFTZlFBtVonvat" 
    },   "Request": 
    {
        "StoreKey": "KITIMIMI",
        "CreatedFromTime":today,
    }}
    api_url = "https://sl.atomicseller.com/Api/Delivery/GetDeliveries"
    response = requests.get(
        url=api_url,
        json=response_data,
    )

    data = response.json()
    print(data)
    for key in data['Response']['Deliveries']:
        print(key['Delivery']['TrackingNumber'])
        print(key['Order']['OrderKey'])
        if key['Delivery']['TrackingNumber']!='':
            order={key['Order']['OrderKey']}
            string = order.pop()
            last_five_chars = string[-5:]
            url = f"https://kitimimi.com/wp-json/wc-shipment-tracking/v3/orders/{last_five_chars}/shipment-trackings"
            print(last_five_chars)
            payload ={
            "tracking_provider": "DPD France",
            "tracking_number": key['Delivery']['TrackingNumber'],
            "status_shipped": 1,
            "replace_tracking": 1
        }
            headers = {
            'Authorization': 'Basic Y2tfNDVjNTRiMmFkZjNjNjNlNTIwNjBkM2ZmY2E1NDFkZTg4YjcxYjc5Yjpjc18yZjQ4NDZiNTBhYzVmNmZlNjk3OGNjMzllMTcyNDRjODRhYTVkZmFi',
            'Cookie': 'aelia_cs_selected_currency=EUR; aelia_customer_country=PK; wfwaf-authcookie-6f4abdd7a72b5bd7453008536b22a4ea=1%7Cadministrator%7Cmanage_options%2Cunfiltered_html%2Cedit_others_posts%2Cupload_files%2Cpublish_posts%2Cedit_posts%2Cread%2Cmanage_network%7Cd2272d76759d97df144fcb2810f0342fa6a6c498ae165e61484e709b25407963; wp-wpml_current_admin_language_d41d8cd98f00b204e9800998ecf8427e=en'
            }
            response = requests.request("POST", url, headers=headers, data=payload)

            print(response.text)











