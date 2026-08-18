# completar_bib.py — añade entradas faltantes al .bib maestro (anti-duplicados)
import pathlib
BIB = pathlib.Path.home()/'Zotero/Tesis_profesor_leal.bib'
txt = BIB.read_text(encoding='utf-8')
entradas = {
'noaa2024ch4': """@misc{noaa2024ch4,
  author = {{NOAA Global Monitoring Laboratory}},
  title = {Trends in Atmospheric Methane},
  year = {2024},
  url = {https://gml.noaa.gov/ccgg/trends_ch4/}
}""",
'jcgmEvaluationMeasurementData2008': """@techreport{jcgmEvaluationMeasurementData2008,
  author = {{Joint Committee for Guides in Metrology (JCGM)}},
  title = {Evaluation of Measurement Data --- Guide to the Expression of Uncertainty in Measurement (GUM)},
  number = {JCGM 100:2008},
  institution = {BIPM},
  year = {2008},
  url = {https://www.bipm.org/en/publications/guides/gum.html}
}""",
'ipccGuidelinesNationalGreenhouse2006': """@techreport{ipccGuidelinesNationalGreenhouse2006,
  author = {{IPCC}},
  title = {2006 IPCC Guidelines for National Greenhouse Gas Inventories},
  institution = {Institute for Global Environmental Strategies (IGES)},
  year = {2006},
  url = {https://www.ipcc-nggip.iges.or.jp/public/2006gl/}
}""",
'ideam2021inventario': """@techreport{ideam2021inventario,
  author = {{IDEAM}},
  title = {Inventario Nacional de Emisiones y Absorciones Atmosféricas de Colombia},
  institution = {Instituto de Hidrología, Meteorología y Estudios Ambientales, MinAmbiente},
  address = {Bogotá, Colombia},
  year = {2024}
}""",
'atkinsPhysicalChemistry2014': """@book{atkinsPhysicalChemistry2014,
  author = {Atkins, Peter and de Paula, Julio},
  title = {Physical Chemistry},
  edition = {10},
  publisher = {Oxford University Press},
  year = {2014}
}""",
'roels1980': """@article{roels1980,
  author = {Roels, J. A.},
  title = {Application of Macroscopic Principles to Microbial Metabolism},
  journal = {Biotechnology and Bioengineering},
  volume = {22}, number = {12}, pages = {2457--2514},
  year = {1980}, doi = {10.1002/bit.260221202}
}""",
'jucker2017': """@article{jucker2017,
  author = {Jucker, C. and Erba, D. and Leonardi, M. G. and Lupi, D. and Savoldelli, S.},
  title = {Assessment of Vegetable and Fruit Substrates as Potential Rearing Media for {Hermetia} illucens},
  journal = {Environmental Entomology},
  year = {2017}, doi = {10.1093/ee/nvx154},
  note = {VERIFICAR contra fuente original}
}""",
'hutchinsonMethodsSoilAnalysis1992': """@article{hutchinsonMethodsSoilAnalysis1992,
  author = {Hutchinson, G. L. and Mosier, A. R.},
  title = {Improved Soil Cover Method for Field Measurement of Nitrous Oxide Fluxes},
  journal = {Soil Science Society of America Journal},
  volume = {45}, number = {2}, pages = {311--316},
  year = {1981}, doi = {10.2136/sssaj1981.03615995004500020017x},
  note = {VERIFICAR contra fuente original}
}""",
'allanSummaryPolicymakers2023': """@report{allanSummaryPolicymakers2023,
  author = {{IPCC}},
  editor = {Allan, R. P. and Arias, P. and Berger, S. and Canadell, J. G. and others},
  title = {Climate Change 2023: Synthesis Report. Summary for Policymakers},
  institution = {Intergovernmental Panel on Climate Change},
  year = {2023}, doi = {10.1017/9781009325844.001}
}""",
'shulerbioprocess2017': """@book{shulerbioprocess2017,
  author = {Shuler, Michael L. and Kargi, Fikret and DeLisa, Matthew P.},
  title = {Bioprocess Engineering: Basic Concepts},
  edition = {3},
  publisher = {Pearson},
  year = {2017},
  isbn = {9780137062706}
}"""}
n=0
for k, e in entradas.items():
    if '{'+k+',' not in txt:
        txt += '\n\n' + e + '\n'; n+=1; print('  añadida:', k)
BIB.write_text(txt, encoding='utf-8')
print(f'Listo: {n} entradas añadidas a {BIB}')
