# Task
You are a biomedical named entity recognition system for the BioRED annotation scheme.
Identify every mention of the following entity types in the sentence:
- CellLine: A specific cell line used in biomedical research (e.g., HeLa, A549).
- ChemicalEntity: A chemical compound, drug, or small molecule (e.g., doxorubicin, ethanol).
- DiseaseOrPhenotypicFeature: A disease or observable trait (e.g., Parkinson's disease, fever).
- GeneOrGeneProduct: A gene or its expressed product (e.g., TP53, insulin).
- OrganismTaxon: A species or strain (e.g., Homo sapiens, E. coli).
- SequenceVariant: A specific variation in a DNA/RNA/protein sequence (e.g., BRCA1 c.68_69delAG).

Rules:
- Copy each entity text exactly as it appears in the sentence (same characters and spacing).
- Do not annotate text of any other type.
- If the same entity text occurs several times, listing it once is enough.
- For each entity give "confidence": your probability between 0.0 and 1.0 that the text and type are correct.
- Optionally give "normalized_form": the canonical name of the entity when you know it.
- Answer only with JSON of the form {"entities": [{"text": "...", "type": "...", "confidence": 0.0}]}; use {"entities": []} if there are none.
- Example answers shown in the conversation are reference annotations and therefore carry no confidence.

# Items
Each item below is independent. Answer every item.

## Item biored:test:152
Example input:
Sentence: Clinicians should be aware of potential hepatotoxicity with simvastatin-ezetimibe especially in elderly patients and should carefully monitor serum aminotransferase levels when starting therapy and titrating the dosage .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "simvastatin-ezetimibe", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "serum aminotransferase", "type": "ChemicalEntity"}]}

Example input:
Sentence: Prolonged CsA exposure aggravated renal damage , without clear changes on the traditional markers , but with changes in serums TGF- b and IL-7 , TBARs clearance , and kidney TGF-b and mTOR .

Example answer:
{"entities": [{"text": "CsA", "type": "ChemicalEntity"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TGF- b", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "TBARs", "type": "ChemicalEntity"}, {"text": "TGF-b", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In patients requiring the concurrent use of statins and CYP3A4 inhibitors , pravastatin , fluvastatin , and rosuvastatin carry the lowest risk of drug interactions ; atorvastatin carries moderate risk , whereas simvastatin and lovastatin have the highest risk and should be avoided in patients taking concomitant CYP3A4 inhibitors .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "statins", "type": "ChemicalEntity"}, {"text": "CYP3A4", "type": "GeneOrGeneProduct"}, {"text": "pravastatin", "type": "ChemicalEntity"}, {"text": "fluvastatin", "type": "ChemicalEntity"}, {"text": "rosuvastatin", "type": "ChemicalEntity"}, {"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}, {"text": "lovastatin", "type": "ChemicalEntity"}, {"text": "CYP3A4 inhibitors", "type": "ChemicalEntity"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Treatment-related adverse events ( AEs ) occurred in 44 % and 52 % , 57 % , and 41 % of the asenapine at 5 and 10 mg BID , haloperidol , and placebo groups , respectively .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: From the present study it is concluded that mangiferin exerts a beneficial effect against ISPH-induced MI due to its antioxidant potential , which regulated the tissues defense system against cardiac damage .

Example answer:
{"entities": [{"text": "mangiferin", "type": "ChemicalEntity"}, {"text": "ISPH-induced", "type": "ChemicalEntity"}, {"text": "MI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac damage", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Simvastatinezetimibe and escitalopram ( which she was taking for depression ) were discontinued , and other potential causes of hepatotoxicity were excluded .

Example answer:
{"entities": [{"text": "Simvastatinezetimibe", "type": "ChemicalEntity"}, {"text": "escitalopram", "type": "ChemicalEntity"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}]}

Example input:
Sentence: Severe rhabdomyolysis and acute renal failure secondary to concomitant use of simvastatin , amiodarone , and atazanavir .

Example answer:
{"entities": [{"text": "rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acute renal failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "atazanavir", "type": "ChemicalEntity"}]}

Example input:
Sentence: OBJECTIVE : To report a case of a severe interaction between simvastatin , amiodarone , and atazanavir resulting in rhabdomyolysis and acute renal failure .

Example answer:
{"entities": [{"text": "simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "atazanavir", "type": "ChemicalEntity"}, {"text": "rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acute renal failure", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Physicians and other healthcare professionals should be aware of this potential adverse effect of tiapride and amisulpride .

## Item biored:test:123
Example input:
Sentence: A CASP8 promoter region six-nucleotide deletion/insertion ( -652 6N ins/del ) variant and a coding region D302H polymorphism are reportedly important in cancer development , but no reported study has assessed the associations of these genetic variations with risk of head and neck cancer .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N ins/del", "type": "SequenceVariant"}, {"text": "D302H", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "head and neck cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Founder mutations in the BRCA1 gene in Polish families with breast-ovarian cancer .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "breast-ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We hypothesised that a common substitution in the basal promoter of MLH1 ( position -93 , rs1800734 ) modifies the risk of cancer after methylating chemotherapy .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "rs1800734", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the haplotype analysis , 1 haplotype carrying the variant allele from both +3100 T/G and +8365 C/T , with a population frequency of 3 % , was also significantly associated with decreased risk of prostate cancer ( p=0.036 , global simulated p-value=0.046 ) .

Example answer:
{"entities": [{"text": "+3100 T/G", "type": "SequenceVariant"}, {"text": "+8365 C/T", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We detected a novel , single , heterozygous nucleotide ( G -- > C ) substitution at position 1201 ( exon 2 ) of the hGR gene , which resulted in aspartic acid to histidine substitution at amino acid position 401 in the amino-terminal domain of the hGRalpha .

Example answer:
{"entities": [{"text": "( G -- > C ) substitution at position 1201", "type": "SequenceVariant"}, {"text": "hGR", "type": "GeneOrGeneProduct"}, {"text": "aspartic acid to histidine substitution at amino acid position 401", "type": "SequenceVariant"}, {"text": "hGRalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : These data support the hypothesis that the common polymorphism at position -93 in the core promoter of MLH1 defines a risk allele for the development of cancer after methylating chemotherapy for Hodgkin lymphoma .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BRCA1 abnormalities were identified in all four families with ovarian cancer only , in 67 % of 27 families with both breast and ovarian cancer , and in 34 % of 35 families with breast cancer only .

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast and ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Gene polymorphism resulting in the substitution of glutamine with lysine at residue 223 in the carbohydrate recognition domain of SP-A2 increases susceptibility to meningococcal disease , as well as the risk of death .

Example answer:
{"entities": [{"text": "glutamine with lysine at residue 223", "type": "SequenceVariant"}, {"text": "carbohydrate", "type": "ChemicalEntity"}, {"text": "SP-A2", "type": "GeneOrGeneProduct"}, {"text": "meningococcal disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "death", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The single family with a BRCA2 mutation had the breast-ovarian cancer syndrome .

Example answer:
{"entities": [{"text": "BRCA2", "type": "GeneOrGeneProduct"}, {"text": "breast-ovarian cancer syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The HH genotype of the nonconservative amino acid substitution polymorphism N372H in the BRCA2 gene was reported to be associated with a 1.3- to 1.5-fold increase in risk of both breast and ovarian cancer .

## Item biored:test:105
Example input:
Sentence: DESIGN AND METHODS : Nine patients clinically diagnosed with hemochromatosis were included in the study .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "hemochromatosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We performed 2 sets of case-control comparisons using Japanese subjects ( first set : 830 patients with RA and 658 controls ; second set : 1112 patients with RA and 940 controls ) , and then performed a stratified analysis using human leukocyte antigen ( HLA ) -DRB1 shared epitope ( SE ) status .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "leukocyte antigen ( HLA ) -DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Thirty-five lamivudine-na ve HBV infected patients with or without HIV co-infection were studied : 15 chronic HBV mono-infected patients and 20 HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "lamivudine-na", "type": "ChemicalEntity"}, {"text": "HBV infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HIV co-infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HBV mono-infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Serum samples were collected from cirrhotic potential liver transplant patients ( LTx ) with ( n=61 ) and without HCC ( n=78 ) as well as from healthy controls ( HCs ; n=39 ) .

Example answer:
{"entities": [{"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Patients with HCC had higher serum TPO and chemokines ( P < 0.001 for TPO , CCL4 , CCL5 and CXCL5 ) and lower CCL2 ( P=0.008 ) levels than cirrhotic patients without HCC .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: One-hundred and fifty HCM ( 90 sporadic hypertrophic cardiomyopathy [ SHCM ] and 60 familial hypertrophic cardiomyopathy [ FHCM ] ) patients and 165 age- and sex-matched normal healthy controls without known hypertension and left ventricular hypertrophy were included in the study .

Example answer:
{"entities": [{"text": "HCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sporadic hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "familial hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular hypertrophy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 46-year old man with a chronic hepatitis C virus infection received triple therapy with ribavirin , pegylated interferon and telaprevir .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "hepatitis C virus infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ribavirin", "type": "ChemicalEntity"}, {"text": "pegylated interferon", "type": "ChemicalEntity"}, {"text": "telaprevir", "type": "ChemicalEntity"}]}

Example input:
Sentence: Included were 5,128 CL/P cases , 1,745 CPO cases , and 3,712 controls ( like-sexed , non-malformed liveborn infant , born immediately after a malformed one , in the same hospital ) , over 4,199,630 consecutive births .

Example answer:
{"entities": [{"text": "CL/P", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CPO", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : This study included 133 patients with AVSD and 200 healthy controls .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "AVSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS AND METHODS : We examined 102 patients ( men/women , 40/62 ; median age , 42 ) diagnosed with chronic ITP and 188 healthy controls ( men/women , 78/110 ; median age , 38 ) .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "men/women", "type": "OrganismTaxon"}, {"text": "chronic ITP", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: METHODS : We analyzed 186 individuals with spontaneous HCV clearance , 501 chronically HCV infected patients , and 217 healthy controls .

## Item biored:test:103
Example input:
Sentence: Immune escape variants of the hepatitis B virus ( HBV ) represent an emerging clinical challenge , because they can be associated with vaccine escape , HBV reactivation , and failure of diagnostic tests .

Example answer:
{"entities": [{"text": "hepatitis B virus", "type": "OrganismTaxon"}, {"text": "HBV", "type": "OrganismTaxon"}]}

Example input:
Sentence: The results in this study significantly improve our understanding of the durability of IL-10-producing CD4 ( + ) T cells postinfection and provide information on how IL-10 may contribute to optimized parasite control and prevention of immune-mediated pathology during repeated malaria infections .

Example answer:
{"entities": [{"text": "IL-10-producing", "type": "GeneOrGeneProduct"}, {"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "malaria infections", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Most hepatocellular carcinomas ( HCC ) develop as a result of chronic liver inflammation .

Example answer:
{"entities": [{"text": "hepatocellular carcinomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chronic liver inflammation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Serum levels of TPO and chemokines were lower , whereas M30 was significantly higher in cirrhotic patients than in HCs .

Example answer:
{"entities": [{"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In response to IL-2 , these CD25 ( + ) Tfh cells increased expression of costimulatory molecules ICOS or OX40 , upregulated transcription factor cMaf , produced cytokines IL-21 , IL-17 , and IL-10 , and raised the levels of antiapoptotic protein Bcl2 .

Example answer:
{"entities": [{"text": "IL-2", "type": "GeneOrGeneProduct"}, {"text": "CD25", "type": "GeneOrGeneProduct"}, {"text": "ICOS", "type": "GeneOrGeneProduct"}, {"text": "OX40", "type": "GeneOrGeneProduct"}, {"text": "cMaf", "type": "GeneOrGeneProduct"}, {"text": "IL-21", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "Bcl2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The aim of our study is to evaluate the diagnostic value of serum growth factors , apoptotic and inflammatory mediators of cirrhotic patients with and without HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : High serum levels of inflammatory chemokines such as CCL4 and CCL5 in the serum of cirrhotic patients indicate the presence of HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 46-year old man with a chronic hepatitis C virus infection received triple therapy with ribavirin , pegylated interferon and telaprevir .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "hepatitis C virus infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ribavirin", "type": "ChemicalEntity"}, {"text": "pegylated interferon", "type": "ChemicalEntity"}, {"text": "telaprevir", "type": "ChemicalEntity"}]}

Example input:
Sentence: Rhabdomyolysis in a hepatitis C virus infected patient treated with telaprevir and simvastatin .

Example answer:
{"entities": [{"text": "Rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatitis C virus infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "telaprevir", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Patients with HCC had higher serum TPO and chemokines ( P < 0.001 for TPO , CCL4 , CCL5 and CXCL5 ) and lower CCL2 ( P=0.008 ) levels than cirrhotic patients without HCC .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: BACKGROUND/AIMS : Interleukin-12 ( IL-12 ) governs the Th1-type immune response , affecting the spontaneous and treatment-induced recovery from HCV-infection .

## Item biored:test:113
Example input:
Sentence: RESULTS : There were more incidents of bradycardia in subjects treated with clonidine compared with those not treated with clonidine ( 17.5 % versus 3.4 % ; p =.02 ) , but no other significant group differences regarding electrocardiogram and other cardiovascular outcomes .

Example answer:
{"entities": [{"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clonidine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Included were 5,128 CL/P cases , 1,745 CPO cases , and 3,712 controls ( like-sexed , non-malformed liveborn infant , born immediately after a malformed one , in the same hospital ) , over 4,199,630 consecutive births .

Example answer:
{"entities": [{"text": "CL/P", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CPO", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Field potential duration ( FPD ) in human-induced pluripotent stem cell-derived cardiomyocytes ( hiPS-CMs ) , which can express QT interval in an electrocardiogram , is reported to be a useful tool to predict K ( + ) channel and Ca ( 2+ ) channel blocker effects on QT interval .

Example answer:
{"entities": [{"text": "human-induced", "type": "OrganismTaxon"}, {"text": "K ( + ) channel and Ca ( 2+ ) channel blocker", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS AND FINDINGS : Cord blood mononuclear cells ( CBMCs ) of 200 neonates were genotyped for two TBX21 and three HLX1 SNPs .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Takotsubo syndrome ( TS ) , also known as broken heart syndrome , is characterized by left ventricle apical ballooning with elevated cardiac biomarkers and electrocardiographic changes suggestive of an acute coronary syndrome ( ie , ST-segment elevation , T wave inversions , and pathologic Q waves ) .

Example answer:
{"entities": [{"text": "Takotsubo syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "broken heart syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acute coronary syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "myocardial stunning", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Physicians prescribing clonidine should monitor for bradycardia and advise patients about the high likelihood of initial drowsiness .

Example answer:
{"entities": [{"text": "clonidine", "type": "ChemicalEntity"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "drowsiness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the classical form it presents as neonatal apnea , intractable seizures , and hypotonia , followed by significant psychomotor retardation .

Example answer:
{"entities": [{"text": "apnea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypotonia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "psychomotor retardation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report a case of 54-year-old woman with medical history of mitral valve prolapse and migraines , who was admitted to the hospital for substernal chest pain and electrocardiogram demonstrated 1/2 mm ST-segment elevation in leads II , III , aVF , V5 , and V6 and positive troponin I. Emergent coronary angiogram revealed normal coronary arteries with moderately reduced left ventricular ejection fraction with wall motion abnormalities consistent with TS .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "mitral valve prolapse", "type": "DiseaseOrPhenotypicFeature"}, {"text": "migraines", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chest pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "motion abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: In this study we investigated a newborn patient with fetal bradycardia , 2:1 atrioventricular block and ventricular tachycardia soon after birth .

## Item biored:test:158
Example input:
Sentence: To determine the pathogenic importance of CB depletions in AD models , we crossed 5 familial AD mutations ( 5XFAD ; Tg ) mice with CB knock-out ( CBKO ) mice and generated a novel line CBKO.5XFAD ( CBKOTg ) mice .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "CBKO", "type": "GeneOrGeneProduct"}, {"text": "CBKO.5XFAD", "type": "GeneOrGeneProduct"}, {"text": "CBKOTg", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We hypothesized that Thra1 ( PV/+ ) mice could be used to predict the skeletal outcome of human THRA mutations and determine whether prolonged treatment with a supraphysiological dose of T4 ameliorates the skeletal abnormalities .

Example answer:
{"entities": [{"text": "Thra1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "THRA", "type": "GeneOrGeneProduct"}, {"text": "T4", "type": "ChemicalEntity"}, {"text": "skeletal abnormalities", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DOCK8 was expressed in a variety of human organs , including the lungs , and was also expressed in type II alveolar , bronchiolar epithelial and bronchial epithelial cells , which are considered as being progenitors for lung cancer cells .

Example answer:
{"entities": [{"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Remarkably , transfection of Langerin cDNA into fibroblasts created a compact network of membrane structures with typical features of BG .

Example answer:
{"entities": [{"text": "Langerin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These genes were assessed and ranked by cartilage selectivity with whole-genome microarray data , revealing only two genes , encoding aggrecan and chondroitin sulfate proteoglycan 4 , that were selectively expressed in cartilage .

Example answer:
{"entities": [{"text": "aggrecan", "type": "GeneOrGeneProduct"}, {"text": "chondroitin sulfate proteoglycan 4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BMPR signalling was markedly impaired in TAK1-deficient chondrocytes as evidenced by reduced expression of known BMP target genes as well as reduced phosphorylation of Smad1/5/8 and p38/Jnk/Erk MAP kinases .

Example answer:
{"entities": [{"text": "BMPR", "type": "GeneOrGeneProduct"}, {"text": "TAK1-deficient", "type": "GeneOrGeneProduct"}, {"text": "BMP", "type": "GeneOrGeneProduct"}, {"text": "Smad1/5/8", "type": "GeneOrGeneProduct"}, {"text": "p38/Jnk/Erk", "type": "GeneOrGeneProduct"}, {"text": "MAP kinases", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Object of the present study was to study the influence of SLCO1B1 * 5 , * 15 and * 15+C1007G , a novel haplotype found in a patient with pravastatin-induced myopathy , on the functional properties of OATP1B1 by transient expression systems of HEK293 and HeLa cells using endogenous conjugates and statins as substrates .

Example answer:
{"entities": [{"text": "SLCO1B1", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "pravastatin-induced", "type": "ChemicalEntity"}, {"text": "myopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OATP1B1", "type": "GeneOrGeneProduct"}, {"text": "HEK293", "type": "CellLine"}, {"text": "HeLa", "type": "CellLine"}]}

Input:
Sentence: The function of these variants was studied in transfected human immortalized CH-8 articular chondrocytes .

## Item biored:test:108
Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Serum levels of TPO and chemokines were lower , whereas M30 was significantly higher in cirrhotic patients than in HCs .

Example answer:
{"entities": [{"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: However , the concomitant occurrence of HBeAg negativity ( PC/BCP ) , sP120T , and LAM resistance resulted in the restoration of replication to levels of wild-type HBV .

Example answer:
{"entities": [{"text": "HBeAg", "type": "ChemicalEntity"}, {"text": "PC/BCP", "type": "GeneOrGeneProduct"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}]}

Example input:
Sentence: Haplotype reconstruction via the expectation-maximization algorithm showed in both populations that only the haplotype containing the minor ( W ) allele at codon 620 was associated with T1D ( OR=2.26 , 95 % CI 1.68-3.02 in Czechs , OR=14.8 , 95 % CI 2.0-651 in Azeri ) or JIA ( OR=2.43 , 95 % CI 1.66-3.56 in Czechs ) .

Example answer:
{"entities": [{"text": "( W ) allele at codon 620", "type": "SequenceVariant"}, {"text": "T1D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "JIA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Patients with HCC had higher serum TPO and chemokines ( P < 0.001 for TPO , CCL4 , CCL5 and CXCL5 ) and lower CCL2 ( P=0.008 ) levels than cirrhotic patients without HCC .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Replication-competent HBV strains with sG145R or sP120T and LAM resistance ( rtM204I or rtL180M/rtM204V ) were generated on an HBeAg-positive and an HBeAg-negative background with precore ( PC ) and basal core promoter ( BCP ) mutants .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBeAg-positive", "type": "ChemicalEntity"}, {"text": "HBeAg-negative", "type": "ChemicalEntity"}, {"text": "precore", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We therefore systematically analyzed the functional impact of the most prevalent immune escape variants , the sG145R and sP120T mutants , on the viral replication efficacy and antiviral drug susceptibility of common treatment-associated mutants with resistance to lamivudine ( LAM ) and/or HBeAg negativity .

Example answer:
{"entities": [{"text": "lamivudine", "type": "ChemicalEntity"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBeAg", "type": "ChemicalEntity"}]}

Example input:
Sentence: In particular , subjects with stage IV had a two times higher probability of having either IL1B-31TT ( or IL1B-511CC ) genotype compared with stage I subjects .

Example answer:
{"entities": [{"text": "IL1B-31TT", "type": "GeneOrGeneProduct"}, {"text": "IL1B-511CC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Differential impact of immune escape mutations G145R and P120T on the replication of lamivudine-resistant hepatitis B virus e antigen-positive and -negative strains .

Example answer:
{"entities": [{"text": "G145R", "type": "SequenceVariant"}, {"text": "P120T", "type": "SequenceVariant"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B virus e", "type": "ChemicalEntity"}]}

Example input:
Sentence: The sG145R mutation strongly reduced HBsAg levels and was able to fully restore the impaired replication of LAM-resistant HBV mutants to the levels of wild-type HBV , and PC or BCP mutations further enhanced viral replication .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "LAM-resistant", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: However , HCV genotype 1-infected patients with high baseline viremia carrying the IL12B 3'-UTR 1188-C-allele showed significantly higher sustained virologic response ( SVR ) rates ( 25.3 % vs. 46 % vs. 54.5 % for A/A , A/C and C/C ) due to reduced relapse rates ( 24.2 % vs. 12 % vs. zero % for A/A , A/C and C/C ) .

## Item biored:test:181
Example input:
Sentence: CONCLUSIONS : In two different Caucasian populations , the Czechs and the Azeri , no independent contribution can be detected either of the -1123 promoter SNP or the +2740 3'-UTR SNP , and only the minor allele at PTPN22 codon 620 contributes to the risk of autoimmunity .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We hypothesised that a common substitution in the basal promoter of MLH1 ( position -93 , rs1800734 ) modifies the risk of cancer after methylating chemotherapy .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "rs1800734", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SNP 10510452_139 in the promoter region was shown to have a high posterior probability ( P = 0.77-0.86 ) of influencing BMI , fat mass , and waist circumference in Hispanic children .

Example answer:
{"entities": [{"text": "SNP 10510452_139", "type": "SequenceVariant"}]}

Example input:
Sentence: PAI-1 4G/5G promoter genotypes frequencies were similar in patients with or without liver fibrosis associated to NASH ( p = 0.6 ) .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These data support the hypothesis that the common polymorphism at position -93 in the core promoter of MLH1 defines a risk allele for the development of cancer after methylating chemotherapy for Hodgkin lymphoma .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The promoter indel and rs2070197 had independent genetic effects , which accounted for the association of rs2004640 and rs10954213 .

Example answer:
{"entities": [{"text": "rs2070197", "type": "SequenceVariant"}, {"text": "rs2004640", "type": "SequenceVariant"}, {"text": "rs10954213", "type": "SequenceVariant"}]}

Example input:
Sentence: Our data indicate that the 5-HTTLPR polymorphic element within the SLC6A4 promoter may govern the genetic risk of PD in Italians .

Example answer:
{"entities": [{"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}, {"text": "SLC6A4", "type": "GeneOrGeneProduct"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : We demonstrated that individuals with the presence of D allele for the -1607 promoter polymorphism of MMP1 are about 1.5 times more susceptible to develop DDD when compared with those having G allele only .

Example answer:
{"entities": [{"text": "D allele for the -1607", "type": "SequenceVariant"}, {"text": "MMP1", "type": "GeneOrGeneProduct"}, {"text": "DDD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A CASP8 promoter region six-nucleotide deletion/insertion ( -652 6N ins/del ) variant and a coding region D302H polymorphism are reportedly important in cancer development , but no reported study has assessed the associations of these genetic variations with risk of head and neck cancer .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N ins/del", "type": "SequenceVariant"}, {"text": "D302H", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "head and neck cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The six-nucleotide deletion/insertion variant in the CASP8 promoter region is inversely associated with risk of squamous cell carcinoma of the head and neck .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We hypothesized that promoter variants would be the most likely candidates for determinants of risk .

## Item biored:test:131
Example input:
Sentence: We investigated the mechanisms responsible for the functional disparity on B cells between a wild-type p17 ( refp17 ) and a vp17 named S75X .

Example answer:
{"entities": [{"text": "p17", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}]}

Example input:
Sentence: Our results thus indicates that PON1 192RR homozygosity is associated with increased mortality in women in the second half of life and that this increased mortality is possibly related to CHD severity and survival after CHD rather than susceptibility to development of CHD .

Example answer:
{"entities": [{"text": "PON1", "type": "GeneOrGeneProduct"}, {"text": "192RR", "type": "SequenceVariant"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conducted a screening of the MHC region for 1,536 single nucleotide polymorphisms ( SNPs ) and the deletion of the C4A gene in a SLE case-control study ( 380 cases , 765 age-matched controls ) nested within the prospective Black Women 's Health Study .

Example answer:
{"entities": [{"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "C4A", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Women", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS AND FINDINGS : Cord blood mononuclear cells ( CBMCs ) of 200 neonates were genotyped for two TBX21 and three HLX1 SNPs .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Three BRCA1 abnormalities - 5382insC , C61G , and 4153delA - accounted for 51 % , 20 % , and 11 % of the identified mutations , respectively ..

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5382insC", "type": "SequenceVariant"}, {"text": "C61G", "type": "SequenceVariant"}, {"text": "4153delA", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Carrier frequency of the MLH1 -93 variant was higher in patients who developed therapy related acute myeloid leukaemia ( t-AML ) ( 75.0 % , n = 12 ) or breast cancer ( 53.3 % .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "acute myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We observed strong linkage disequilibrium between the T allele at -511 and the C allele at -31 and between the C allele at -511 and the T allele at -31 in IL1B in both the cases and controls ( R ( 2 ) =0.94 ) .

Example answer:
{"entities": [{"text": "T allele at -511", "type": "SequenceVariant"}, {"text": "C allele at -31", "type": "SequenceVariant"}, {"text": "C allele at -511", "type": "SequenceVariant"}, {"text": "T allele at -31", "type": "SequenceVariant"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BRCA1 abnormalities were identified in all four families with ovarian cancer only , in 67 % of 27 families with both breast and ovarian cancer , and in 34 % of 35 families with breast cancer only .

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast and ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A multiple logistic regression analysis indicated that the odds ratio for EH in the -395A allele carriers as compared with the control group was 0.593 ( P=0.024 ) after adjusting for current traditional risk factors .

Example answer:
{"entities": [{"text": "EH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "-395A", "type": "SequenceVariant"}]}

Example input:
Sentence: No Hardy Weinberg disequilibrium and no significant difference in allele frequencies between patients and controls were observed for any variation .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: on newborn females and adult female controls , we found no departure from Hardy-Weinberg equilibrium in the distribution of N372H alleles for our female BRCA1 carriers .

## Item biored:test:149
Example input:
Sentence: Although only limited subjects were investigated , our results suggested that a genetic polymorphism in ABCG2 might alter the transport activity for the drug and elevate the systemic circulation level of irinotecan , leading to severe myelosuppression .

Example answer:
{"entities": [{"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "irinotecan", "type": "ChemicalEntity"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These findings suggest that glutamate-mediated mechanisms in the neural circuits at the IC level influence haloperidol-induced catalepsy and participate in the regulation of motor activity .

Example answer:
{"entities": [{"text": "glutamate-mediated", "type": "ChemicalEntity"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: High-dose tranexamic Acid is associated with nonischemic clinical seizures in cardiac surgical patients .

Example answer:
{"entities": [{"text": "tranexamic Acid", "type": "ChemicalEntity"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Cyclooxygenase inhibitors cause complex changes in renal , vascular and cardiac prostanoid profiles thereby increasing vascular resistance and fluid retention .

Example answer:
{"entities": [{"text": "Cyclooxygenase inhibitors", "type": "ChemicalEntity"}, {"text": "prostanoid", "type": "ChemicalEntity"}]}

Example input:
Sentence: This patient presented with symptoms of neuroleptic malignant syndrome ( NMS ) , thus demonstrating that NMS-like symptoms can occur after combined paroxetine and alprazolam treatment .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "neuroleptic malignant syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NMS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NMS-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}]}

Example input:
Sentence: The antiepileptic drugs , phenobarbitone and carbamazepine are well known to cause cognitive impairment on chronic use .

Example answer:
{"entities": [{"text": "antiepileptic drugs", "type": "ChemicalEntity"}, {"text": "phenobarbitone", "type": "ChemicalEntity"}, {"text": "carbamazepine", "type": "ChemicalEntity"}, {"text": "cognitive impairment", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cocaine-induced anxiety was also attenuated in Dbh +/- mice following administration of disulfiram , a dopamine beta-hydroxylase ( DBH ) inhibitor .

Example answer:
{"entities": [{"text": "Cocaine-induced", "type": "ChemicalEntity"}, {"text": "anxiety", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "disulfiram", "type": "ChemicalEntity"}, {"text": "dopamine beta-hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "DBH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Desipramine-induced sensitization of lidocaine seizures may have a mechanism distinct from kindling resulting from repeated administration of cocaine .

Example answer:
{"entities": [{"text": "Desipramine-induced", "type": "ChemicalEntity"}, {"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Catecholamine-induced cardiomyopathy due to chronic excess of endogenous catecholamines has been recognized for decades as a clinical phenomenon .

Example answer:
{"entities": [{"text": "Catecholamine-induced", "type": "ChemicalEntity"}, {"text": "cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "catecholamines", "type": "ChemicalEntity"}]}

Example input:
Sentence: Down-regulation of norepinephrine transporter function induced by chronic administration of desipramine linking to the alteration of sensitivity of local-anesthetics-induced convulsions and the counteraction by co-administration with local anesthetics .

Example answer:
{"entities": [{"text": "norepinephrine transporter", "type": "GeneOrGeneProduct"}, {"text": "desipramine", "type": "ChemicalEntity"}, {"text": "convulsions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "anesthetics", "type": "ChemicalEntity"}]}

Input:
Sentence: DISCUSSION : Drug-induced symptoms of pheochromocytoma are often associated with the use of substituted benzamide drugs , but the underlying mechanism is unknown .

## Item biored:test:2
Example input:
Sentence: On the Positive and Negative Syndrome Scale positive subscale , all treatments were superior to placebo with LOCF and MMRM ; asenapine at 5 mg BID was superior to placebo on the negative subscale with MMRM and on the general psychopathology subscale with LOCF and MMRM .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}]}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "a reduced locomotor activity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Compared with those carrying at least one variant 326Ile allele , carriers with the Met326Met genotype had higher serum 17-hydroxyprogesterone ( 17-OHP ) { 1.1 [ 95 % confidence interval ( CI ) 1.1-1.3 ] ng/ml in those with the Met326Met genotype versus 0.8 ( 95 % CI 0.7-1.0 ) ng/ml in those with Ile326Ile and Met326Ile genotypes , P = 0.0073 } and free testosterone levels [ 1.2 ( 95 % CI 1.1-1.4 ) pg/ml for Met326Met genotype versus 0.9 ( 95 % CI 0.6-1.3 ) pg/ml for Ile326Ile and Met326Ile genotypes , P = 0.038 ] .

Example answer:
{"entities": [{"text": "326Ile", "type": "SequenceVariant"}, {"text": "Met326Met", "type": "SequenceVariant"}, {"text": "17-hydroxyprogesterone", "type": "ChemicalEntity"}, {"text": "17-OHP", "type": "ChemicalEntity"}, {"text": "Ile326Ile", "type": "SequenceVariant"}, {"text": "Met326Ile", "type": "SequenceVariant"}, {"text": "testosterone", "type": "ChemicalEntity"}]}

Example input:
Sentence: The metabolic responses to isoprenaline in dogs ( an increase in circulating glucose , lactate and free fatty acids ) were all blocked by ( - ) -propranolol .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}, {"text": "dogs", "type": "OrganismTaxon"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "fatty acids", "type": "ChemicalEntity"}]}

Example input:
Sentence: Several studies have reported that , compared with wild-type individuals , CYP2C19 variant allele carriers exhibit a significantly lower capacity to metabolize clopidogrel into its active metabolite and inhibit platelet activation , and are therefore at significantly higher risk of adverse cardiovascular events .

Example answer:
{"entities": [{"text": "CYP2C19", "type": "GeneOrGeneProduct"}, {"text": "clopidogrel", "type": "ChemicalEntity"}]}

Example input:
Sentence: Methadone , an agonist of OPRM1 , enhances the sensitivity of parental leukemic cells , but not OPRM1-depleted cells , to L-asparaginase treatment , indicating that OPRM1 is required for the synergistic action of L-asparaginase and methadone , and that OPRM1 loss promotes leukemic cell survival likely through downregulation of the OPRM1-mediated apoptotic pathway .

Example answer:
{"entities": [{"text": "Methadone", "type": "ChemicalEntity"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "leukemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1-depleted", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "methadone", "type": "ChemicalEntity"}, {"text": "OPRM1-mediated", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Changes evoked by a single intraperitoneal injection of rilmenidine ( 600 microg/kg ) or alpha-methyldopa ( 100 mg/kg ) , selective I1- and alpha2-receptor agonists , respectively , in blood pressure , hemodynamic variability , and locomotor activity were assessed in radiotelemetered sham-operated and ovariectomized ( Ovx ) Sprague-Dawley female rats with or without 12-wk estrogen replacement .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "I1- and alpha2-receptor", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "estrogen", "type": "ChemicalEntity"}]}

Example input:
Sentence: In blocking the positive inotropic and chronotropic responses to isoprenaline , ( + ) -propranolol had less than one hundredth the potency of ( - ) -propranolol .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , mitochondrial respiratory dysfunction characterized by decreased respiratory control ratio and ADP/O was observed in isoproterenol-treated rats .

Example answer:
{"entities": [{"text": "mitochondrial respiratory dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ADP/O", "type": "ChemicalEntity"}, {"text": "isoproterenol-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Metfromin markedly lowered isoproterenol-induced elevation in the levels of TLR4 mRNA , myeloid differentiation protein 88 ( MyD88 ) , tumor necrosis factor-alpha ( TNF-a ) , and interleukin 6 ( IL-6 ) in the heart tissues .

Example answer:
{"entities": [{"text": "Metfromin", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "myeloid differentiation protein 88", "type": "GeneOrGeneProduct"}, {"text": "MyD88", "type": "GeneOrGeneProduct"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}, {"text": "interleukin 6", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The two metabolic phenotypes , extensive ( EM ) and poor metabolizers ( PM ) , show different stereoselective metabolism , resulting in apparently higher beta-1 adrenoceptor antagonistic potency of racemic metoprolol in EMs .

## Item biored:test:129
Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , the number of the CASP8 -652 6N del ( but not 302H ) variant allele tended to correlate with increased levels of camptothecin-induced p53-mediated apoptosis in T lymphocytes from 170 cancer-free controls .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "302H", "type": "SequenceVariant"}, {"text": "camptothecin-induced", "type": "ChemicalEntity"}, {"text": "p53-mediated", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the haplotype analysis , 1 haplotype carrying the variant allele from both +3100 T/G and +8365 C/T , with a population frequency of 3 % , was also significantly associated with decreased risk of prostate cancer ( p=0.036 , global simulated p-value=0.046 ) .

Example answer:
{"entities": [{"text": "+3100 T/G", "type": "SequenceVariant"}, {"text": "+8365 C/T", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The p.A1369S variant was associated with a significantly lower risk of type 2 diabetes ( odds ratio [ OR ] 0.93 ; 95 % CI 0.91 , 0.95 ; P = 1.2 x 10 ( -11 ) ) .

Example answer:
{"entities": [{"text": "p.A1369S", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A CASP8 promoter region six-nucleotide deletion/insertion ( -652 6N ins/del ) variant and a coding region D302H polymorphism are reportedly important in cancer development , but no reported study has assessed the associations of these genetic variations with risk of head and neck cancer .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N ins/del", "type": "SequenceVariant"}, {"text": "D302H", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "head and neck cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The estimated relative risk was significantly high for individuals with w1/m1 genotype at 3'UTR of CYP1A1 gene ( OR-4.64 ; 95 % CI = 1.51-14.86 ; P < 0.01 ) whereas the CYP1A1 Ile/Val genotype ( w2/m2 ) on exon 7 was found to be associated with a decreased risk for prostate cancer ( OR-0.17 ; 95 % CI = 0.02-0.89 ; P=0.03 ) .

Example answer:
{"entities": [{"text": "CYP1A1", "type": "GeneOrGeneProduct"}, {"text": "Ile/Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: An intronic SNP , rs2622604 , in ABCG2 showed P ( Fisher ) =0.0419 in the second stage and indicated a significant association with severe myelosuppression in the combined study ( P ( Fisher ) =0.000237 ; P ( Corrected ) =0.036 ) .

Example answer:
{"entities": [{"text": "rs2622604", "type": "SequenceVariant"}, {"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A multiple logistic regression analysis indicated that the odds ratio for EH in the -395A allele carriers as compared with the control group was 0.593 ( P=0.024 ) after adjusting for current traditional risk factors .

Example answer:
{"entities": [{"text": "EH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "-395A", "type": "SequenceVariant"}]}

Input:
Sentence: In respect of ovarian cancer risk , we also saw no effect with the N372H variant but we did observe a borderline association with the 5'-untranslated region 203A allele ( hazard ratio , 1.43 ; CI , 1.01-2.00 ) .

## Item biored:test:148
Example input:
Sentence: Multivariate logistic regression revealed the common haplotypes H1 ( AGACT ) , H2 ( AGAWT ) , and H3 ( AGAWC ) were associated with the persistent postoperative hypertension ( P = .01 , 0.03 , 0.005 after Bonferroni correction ) .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , an increase of serum creatinine at various times postoperatively is more predictive of the development of CRF or ESRD .

Example answer:
{"entities": [{"text": "creatinine", "type": "ChemicalEntity"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The diagnosis of 17alpha-hydroxylase deficiency was initially established through HPLC serum adrenal profiles in Qilu Hospital , China , from 1983-1993 .

Example answer:
{"entities": [{"text": "17alpha-hydroxylase deficiency", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Association of DNA polymorphisms within the CYP11B2/CYP11B1 locus and postoperative hypertension risk in the patients with aldosterone-producing adenomas .

Example answer:
{"entities": [{"text": "CYP11B2/CYP11B1", "type": "GeneOrGeneProduct"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "aldosterone-producing adenomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Echocardiography was performed at 3 and 28 days post-MI , whereas the haemodynamics test was performed 28 days post-MI .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSION : The results confirmed the diagnostic value of the HPLC serum adrenal profile for 17alpha-hydroxylase deficiency .

Example answer:
{"entities": [{"text": "17alpha-hydroxylase deficiency", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVES : Hypertension often persists after adrenalectomy for primary aldosteronism .

Example answer:
{"entities": [{"text": "Hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The rs4539 ( AA ) , H1 , H2 , and H3 are genetic predictors for postoperative persistence of hypertension for Chinese patients treated by adrenalectomy with APA .

Example answer:
{"entities": [{"text": "rs4539", "type": "SequenceVariant"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "APA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : CYP11B2-CYP11B1 haplotype was associated with persistent postoperative hypertension in Chinese patients undergoing adrenalectomy with APA ( P = .006 ) .

Example answer:
{"entities": [{"text": "CYP11B2-CYP11B1", "type": "GeneOrGeneProduct"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "APA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of this study was to investigate the association of DNA polymorphisms within steroid synthesis genes ( CYP11B2 , CYP11B1 ) and the postoperative resolution of hypertension in Chinese patients undergoing adrenalectomy for aldosterone-producing adenomas ( APA ) .

Example answer:
{"entities": [{"text": "steroid synthesis genes", "type": "GeneOrGeneProduct"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "aldosterone-producing adenomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "APA", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Abdominal ultrasound showed an adrenal mass , and postoperative histologic examination confirmed the diagnosis of pheochromocytoma .

## Item biored:test:111
Example input:
Sentence: The severe phenotype with seriously impaired intellectual development , hyperkinetic behaviour , tachycardia , hearing and visual impairment is probably due to the dominant negative effect of the I280S mutant protein and the absence of any functional TR-beta .

Example answer:
{"entities": [{"text": "impaired intellectual development", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperkinetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tachycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hearing and visual impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "I280S", "type": "SequenceVariant"}, {"text": "TR-beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The patient was a compound heterozygote for SRD5A2 mutations , carrying 2 mutations in exon 4 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Four patients harbor yet non-described SRD5A2 gene mutations : a single nucleotide deletion ( del642T ) , a G158R amino acid substitution , a splice junction mutation ( IVS3+1G > A ) , and the insertion of a cytosine ( 217_218insC ) occurring at a CCCC motif .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "del642T", "type": "SequenceVariant"}, {"text": "G158R", "type": "SequenceVariant"}, {"text": "IVS3+1G > A", "type": "SequenceVariant"}, {"text": "217_218insC", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : The mother and daughter were each heterozygous for PPARG nonsense mutation Y355X , whose protein product in vitro was transcriptionally inactive with no dominant-negative activity against the wild-type receptor .

Example answer:
{"entities": [{"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "Y355X", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : A single heterozygous missense mutation , substitution of a cytosine residue with thymidine in exon 2 of MSH5 , was found in two Caucasian women in whom POF developed at 18 and 36 years of age .

Example answer:
{"entities": [{"text": "cytosine residue with thymidine", "type": "SequenceVariant"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: In conclusion , our study suggests that p.R246Q mutation is common amongst patients with SRD5A2 gene defect from the Northern states of India .

Example answer:
{"entities": [{"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Recently , a lethal phenotype characterized by sudden infant death with dysgenesis of the testes syndrome ( SIDDT ) was identified to be caused by loss of function mutations in the TSPYL1 gene .

Example answer:
{"entities": [{"text": "sudden infant death with dysgenesis of the testes syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SIDDT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSPYL1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Identification of this new de novo nonsense mutation confirms the diagnosis of FDH in this child and highlights the clinical importance of PORCN and Wnt signalling pathways in embryogenesis .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PORCN", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: A novel SCN5A mutation manifests as a malignant form of long QT syndrome with perinatal onset of tachycardia/bradycardia .

## Item biored:test:132
Example input:
Sentence: In overall analysis , the homozygous Cys/Cys genotype showed a significant association with lung cancer compared to Ser allele carrier status ( odds ratio ( OR ) =1.31 , 95 % confidence interval ( CI ) =1.02-1.69 ) .

Example answer:
{"entities": [{"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The estimated CAD risk for BMI -- 25 and the -930G allele interaction was about 160 % greater than that predicted by assuming additivity of the effects , and about 40 % greater for interaction of cigarette smoking and the -930G allele .

Example answer:
{"entities": [{"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "-930G", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : These data support the hypothesis that the common polymorphism at position -93 in the core promoter of MLH1 defines a risk allele for the development of cancer after methylating chemotherapy for Hodgkin lymphoma .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Three BRCA1 abnormalities - 5382insC , C61G , and 4153delA - accounted for 51 % , 20 % , and 11 % of the identified mutations , respectively ..

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5382insC", "type": "SequenceVariant"}, {"text": "C61G", "type": "SequenceVariant"}, {"text": "4153delA", "type": "SequenceVariant"}]}

Example input:
Sentence: In the haplotype analysis , 1 haplotype carrying the variant allele from both +3100 T/G and +8365 C/T , with a population frequency of 3 % , was also significantly associated with decreased risk of prostate cancer ( p=0.036 , global simulated p-value=0.046 ) .

Example answer:
{"entities": [{"text": "+3100 T/G", "type": "SequenceVariant"}, {"text": "+8365 C/T", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The estimated relative risk was significantly high for individuals with w1/m1 genotype at 3'UTR of CYP1A1 gene ( OR-4.64 ; 95 % CI = 1.51-14.86 ; P < 0.01 ) whereas the CYP1A1 Ile/Val genotype ( w2/m2 ) on exon 7 was found to be associated with a decreased risk for prostate cancer ( OR-0.17 ; 95 % CI = 0.02-0.89 ; P=0.03 ) .

Example answer:
{"entities": [{"text": "CYP1A1", "type": "GeneOrGeneProduct"}, {"text": "Ile/Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BRCA1 abnormalities were identified in all four families with ovarian cancer only , in 67 % of 27 families with both breast and ovarian cancer , and in 34 % of 35 families with breast cancer only .

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast and ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The single family with a BRCA2 mutation had the breast-ovarian cancer syndrome .

Example answer:
{"entities": [{"text": "BRCA2", "type": "GeneOrGeneProduct"}, {"text": "breast-ovarian cancer syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To evaluate this phenomenon , the association between two single nucleotide polymorphisms ( A to G transition in exon7 leading to amino acid substitution Ile462Val and T3801C at 3'UTR ) of CYP1A1 gene in prostate cancer were analyzed in a case-control study of 100 individuals in South Indian population .

Example answer:
{"entities": [{"text": "A to G", "type": "SequenceVariant"}, {"text": "Ile462Val", "type": "SequenceVariant"}, {"text": "T3801C", "type": "SequenceVariant"}, {"text": "CYP1A1", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This single nucleotide polymorphism ( SNP ) seemed to be functional as it was associated with decreased lung cancer risk .

Example answer:
{"entities": [{"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We conclude that if these single-nucleotide polymorphisms do modify the risk of cancer in BRCA1 mutation carriers , their effects are not significantly larger than that of N372H previously observed in the general population .

## Item biored:test:155
Example input:
Sentence: A heterozygous caveolin-1 c.474delA mutation has been identified in a family with heritable pulmonary arterial hypertension ( PAH ) .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "pulmonary arterial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Additionally , mutation analysis for MKS3/TMEM67 in 120 patients with JBTS yielded seven different ( four novel ) mutations in five patients , four of whom also presented with congenital liver fibrosis .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "JBTS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : To identify mutations in the carbohydrate sulfotransferase gene ( CHST6 ) for a Chinese family with macular corneal dystrophy ( MCD ) and to investigate the histopathological changes in the affected cornea .

Example answer:
{"entities": [{"text": "carbohydrate sulfotransferase gene", "type": "GeneOrGeneProduct"}, {"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "macular corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Hypomorphic mutations in meckelin ( MKS3/TMEM67 ) cause nephronophthisis with liver fibrosis ( NPHP11 ) .

Example answer:
{"entities": [{"text": "meckelin", "type": "GeneOrGeneProduct"}, {"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "nephronophthisis with liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NPHP11", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Aryl hydrocarbon receptor interacting protein ( AIP ) gene mutation analysis in children and adolescents with sporadic pituitary adenomas .

Example answer:
{"entities": [{"text": "Aryl hydrocarbon receptor interacting protein", "type": "GeneOrGeneProduct"}, {"text": "AIP", "type": "GeneOrGeneProduct"}, {"text": "pituitary adenomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Both sporadic and inherited BCCs are associated with mutations in the tumor suppressor gene PTCH1 , but there is still uncertainty on the role of its homolog PTCH2 .

Example answer:
{"entities": [{"text": "BCCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "PTCH2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We next sequenced PTPN11 in DNA samples from 54 patients with the multiple enchondromatosis disorders Ollier disease or Maffucci syndrome , but found no coding sequence PTPN11 mutations .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "enchondromatosis disorders Ollier disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Maffucci syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Those novel compound heterozygous mutations were thought to contribute to the loss of CHST6 function , which induced the abnormal metabolism of keratan sulfate ( KS ) that deposited in the corneal stroma .

Example answer:
{"entities": [{"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "keratan sulfate", "type": "ChemicalEntity"}, {"text": "KS", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSION : Mutations found in the PTCH1 gene and neighboring repetitive sequences may have contributed to the development of the studied BCCs .

Example answer:
{"entities": [{"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "BCCs", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: This study investigated the potential for ANKH sequence variants to promote sporadic chondrocalcinosis .

## Item biored:test:138
Example input:
Sentence: Haloperidol-induced catalepsy was challenged with prior intracollicular microinjections of glutamate NMDA receptor antagonists , MK-801 ( 15 or 30 mmol/0.5 microl ) and AP7 ( 10 or 20 nmol/0.5 microl ) , or of the NMDA receptor agonist N-methyl-d-aspartate ( NMDA , 20 or 30 nmol/0.5 microl ) .

Example answer:
{"entities": [{"text": "Haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glutamate NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "N-methyl-d-aspartate", "type": "ChemicalEntity"}, {"text": "NMDA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Here , we investigated the effects of CCK-8 on long-term potentiation ( LTP ) in the lateral perforant path ( LPP ) -granule cell synapse of rat dentate gyrus ( DG ) in acute saline or morphine-treated rats .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "morphine-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The present results demonstrate that CCK-8 attenuates the effect of morphine on hippocampal LTP through CCK2 receptors and suggest an ameliorative function of CCK-8 on morphine-induced memory impairment .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "morphine", "type": "ChemicalEntity"}, {"text": "CCK2 receptors", "type": "GeneOrGeneProduct"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "memory impairment", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVE : This study determined the antihyperalgesic effect of CNSB002 , a sodium channel blocker with antioxidant properties given alone and in combinations with morphine in rat models of inflammatory and neuropathic pain .

Example answer:
{"entities": [{"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "sodium channel blocker", "type": "ChemicalEntity"}, {"text": "morphine", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathic pain", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DESIGN : Dose response curves for nonsedating doses of morphine and CNSB002 given intraperitoneally alone and together in combinations were constructed for antihyperalgesic effect using paw withdrawal from noxious heat in two rat pain models : carrageenan-induced paw inflammation and streptozotocin ( STZ ) -induced diabetic neuropathy .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "carrageenan-induced", "type": "ChemicalEntity"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "streptozotocin", "type": "ChemicalEntity"}, {"text": "STZ", "type": "ChemicalEntity"}, {"text": "diabetic neuropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cholecystokinin-octapeptide restored morphine-induced hippocampal long-term potentiation impairment in rats .

Example answer:
{"entities": [{"text": "Cholecystokinin-octapeptide", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The antinociception after morphine ( 3.2 mg/kg ) was increased by co-administration with CNSB002 from 28.0 and 31.7 % to 114.6 and 56.9 % reversal of hyperalgesia in the inflammatory and neuropathic models , respectively ( P < 0.01 ; one-way analysis of variance-significantly greater than either drug given alone ) .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "hyperalgesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Acute morphine ( 30mg/kg , s.c. ) treatment significantly attenuated hippocampal LTP and CCK-8 ( 1ug , i.c.v . )

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CCK-8", "type": "ChemicalEntity"}]}

Example input:
Sentence: The results showed that intracollicular microinjection of MK-801 and AP7 previous to systemic injections of haloperidol significantly attenuated the catalepsy , as indicated by a reduced latency to step down from a horizontal bar .

Example answer:
{"entities": [{"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We have previously reported that CCK-8 significantly alleviated morphine-induced amnesia and reversed spine density decreases in the CA1 region of the hippocampus in morphine-treated animals .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "morphine-treated", "type": "ChemicalEntity"}]}

Input:
Sentence: Second , we investigated the effect of IT MK-801 ( 30 mug ) on the histopathologic changes in the spinal cord after morphine-induced spastic paraparesis .

## Item biored:test:172
Example input:
Sentence: Polymorphisms in the promoter region of DRD4 ( -120 bp duplication , -616C/G , and -521C/T ) were genotyped using allele-specific polymerase chain reaction analysis .

Example answer:
{"entities": [{"text": "DRD4", "type": "GeneOrGeneProduct"}, {"text": "-120 bp duplication", "type": "SequenceVariant"}, {"text": "-616C/G", "type": "SequenceVariant"}, {"text": "-521C/T", "type": "SequenceVariant"}]}

Example input:
Sentence: Polymerase chain reaction was carried out and single nucleotide polymorphisms of FGFR4 were identified by restriction enzyme digestion .

Example answer:
{"entities": [{"text": "FGFR4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Using PCR-RFLP , we confirmed the heterozygous mutation in six affected family members and excluded it in three healthy members .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : Blood samples of 107 patients with biopsy-proven NASH and of 150 healthy volunteers were analyzed by the polymerase chain reaction ( PCR ) and restriction fragment length polymorphism .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Genetic alterations in the PABPN1 gene were identified using PCR and DNA sequencing .

Example answer:
{"entities": [{"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The result of PCR associated with restriction fragment length polymorphism analysis also suggested that this mutation is heterozygous .

Example answer:
{"entities": []}

Example input:
Sentence: The genotypes of the polymorphism were determined by restriction fragment length polymorphism PCR .

Example answer:
{"entities": []}

Example input:
Sentence: TS genotyping methods were polymerase chain reaction ( PCR ) for VNTR and PCR , followed by restriction length fragment polymorphism ( PCR-RFLP ) for SNP and ins/del 6 bp .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "ins/del 6 bp", "type": "SequenceVariant"}]}

Example input:
Sentence: We also designed a rapid polymerase chain reaction-restriction fragment length polymorphism ( PCR-RFLP ) method to analyze the same mutation , amplifying exon 4 and digesting with PstI restriction enzyme .

Example answer:
{"entities": [{"text": "PstI", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Genotyping was determined by the polymerase chain reaction-restriction fragment length polymorphism ( PCR-RFLP ) technique .

Example answer:
{"entities": []}

Input:
Sentence: DNA typing of DBP locus was performed by the PCR-restriction fragment length polymorphism method ( RFLP ) .

## Item biored:test:99
Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: The patient showed an R227Q mutation that has been described in an Asian population and MPH patients , along with a novel frameshift mutation , Tdel219 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "R227Q", "type": "SequenceVariant"}, {"text": "MPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Tdel219", "type": "SequenceVariant"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: We report a novel heterozygous missense mutation , H194Q , in a familial case of Shprintzen syndrome and show that this and the two previously reported missense mutations result in gain of function , possibly through stabilization of the protein dimer DNA complex .

Example answer:
{"entities": [{"text": "H194Q", "type": "SequenceVariant"}, {"text": "Shprintzen syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In contrast , the mutations detected here in patients with NPHP and associated liver fibrosis are exclusively missense mutations .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "NPHP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Single stranded conformational polymorphism ( SSCP ) analysis and sequencing revealed a novel heterozygous C139T transition in PAX9 in the affected members of the family .

Example answer:
{"entities": [{"text": "C139T", "type": "SequenceVariant"}, {"text": "PAX9", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This mutation was responsible for the familial disorder through the substitution of a highly conserved arginine to tryptophan at codon 198 ( p.R198W ) .

Example answer:
{"entities": [{"text": "arginine to tryptophan at codon 198", "type": "SequenceVariant"}, {"text": "p.R198W", "type": "SequenceVariant"}]}

Example input:
Sentence: The first is the frameshift mutation ( P686fs ) caused by the insertion of the four nucleotides CCCC in exon 16 ( 2172_2173insCCCC ) that is predicted to terminate translation before the catalytic serine .

Example answer:
{"entities": [{"text": "P686fs", "type": "SequenceVariant"}, {"text": "insertion of the four nucleotides CCCC", "type": "SequenceVariant"}, {"text": "2172_2173insCCCC", "type": "SequenceVariant"}]}

Example input:
Sentence: A novel missense mutation c.643T > C ( p.S216P ) was detected in the anterior segment malformation group .

Example answer:
{"entities": [{"text": "c.643T > C", "type": "SequenceVariant"}, {"text": "p.S216P", "type": "SequenceVariant"}, {"text": "anterior segment malformation", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Upon screening 30 candidate genes , we identified a missense mutation , p.Ser63Asn in SSH1 in one family , a frameshift mutation , p.Ser19CysfsX24 in an alternative variant ( isoform f ) of SSH1 in another family , and a frameshift mutation , p.Pro27ProfsX54 in the same alternative variant in one non-familial case with DSAP .

## Item biored:test:143
Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "MPTP", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "METH-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: By unbiased genome-wide RNAi screening , we found that among 10 resistant ALL clones , six hits were for opioid receptor mu 1 ( oprm1 ) , two hits were for carbonic anhydrase 1 ( ca1 ) and another two hits were for ubiquitin-conjugating enzyme E2C ( ube2c ) .

Example answer:
{"entities": [{"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "opioid receptor mu 1", "type": "GeneOrGeneProduct"}, {"text": "oprm1", "type": "GeneOrGeneProduct"}, {"text": "carbonic anhydrase 1", "type": "GeneOrGeneProduct"}, {"text": "ca1", "type": "GeneOrGeneProduct"}, {"text": "ubiquitin-conjugating enzyme E2C", "type": "GeneOrGeneProduct"}, {"text": "ube2c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DESIGN : Dose response curves for nonsedating doses of morphine and CNSB002 given intraperitoneally alone and together in combinations were constructed for antihyperalgesic effect using paw withdrawal from noxious heat in two rat pain models : carrageenan-induced paw inflammation and streptozotocin ( STZ ) -induced diabetic neuropathy .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "carrageenan-induced", "type": "ChemicalEntity"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "streptozotocin", "type": "ChemicalEntity"}, {"text": "STZ", "type": "ChemicalEntity"}, {"text": "diabetic neuropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Haloperidol-induced catalepsy was challenged with prior intracollicular microinjections of glutamate NMDA receptor antagonists , MK-801 ( 15 or 30 mmol/0.5 microl ) and AP7 ( 10 or 20 nmol/0.5 microl ) , or of the NMDA receptor agonist N-methyl-d-aspartate ( NMDA , 20 or 30 nmol/0.5 microl ) .

Example answer:
{"entities": [{"text": "Haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glutamate NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "N-methyl-d-aspartate", "type": "ChemicalEntity"}, {"text": "NMDA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Effects of ginsenosides on opioid-induced hyperalgesia in mice .

Example answer:
{"entities": [{"text": "ginsenosides", "type": "ChemicalEntity"}, {"text": "opioid-induced", "type": "ChemicalEntity"}, {"text": "hyperalgesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Opioid-induced hyperalgesia ( OIH ) is characterized by nociceptive sensitization caused by the cessation of chronic opioid use .

Example answer:
{"entities": [{"text": "Opioid-induced", "type": "ChemicalEntity"}, {"text": "hyperalgesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OIH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "opioid", "type": "ChemicalEntity"}]}

Example input:
Sentence: We have previously reported that CCK-8 significantly alleviated morphine-induced amnesia and reversed spine density decreases in the CA1 region of the hippocampus in morphine-treated animals .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "morphine-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: Cholecystokinin-octapeptide restored morphine-induced hippocampal long-term potentiation impairment in rats .

Example answer:
{"entities": [{"text": "Cholecystokinin-octapeptide", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Glutamatergic neurotransmission mediated by NMDA receptors in the inferior colliculus can modulate haloperidol-induced catalepsy .

Example answer:
{"entities": [{"text": "NMDA receptors", "type": "GeneOrGeneProduct"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We suggest that opioids may be neurotoxic in the setting of spinal cord ischemia via NMDA receptor activation .

## Item biored:test:115
Example input:
Sentence: At dose levels of ( + ) -propranolol which attenuated the responses to isoprenaline , there was a significant prolongation of the PR interval of the electrocardiogram.3 .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: The current data showed that pilocarpine significantly delayed onset of arrhythmias , decreased the time course of ventricular tachycardia and fibrillation , reduced arrhythmia score , and increased the survival time of arrhythmic rats and guinea pigs .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "arrhythmias", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ventricular tachycardia and fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arrhythmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arrhythmic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "guinea pigs", "type": "OrganismTaxon"}]}

Example input:
Sentence: Generally , atropine reduced contractions , but in contrast to controls , it also reduced responses to low electrical field stimulation intensity ( 1-5 Hz ) in inflamed preparations .

Example answer:
{"entities": [{"text": "atropine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Amiodarone represents an effective antiarrhythmic drug for cardioversion of recent-onset atrial fibrillation ( AF ) and maintenance of sinus rhythm .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "ChemicalEntity"}, {"text": "antiarrhythmic drug", "type": "ChemicalEntity"}, {"text": "atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The left ventricular dysfunction was significantly lower in the groups treated with 25 and 50mg/kg of metformin .

Example answer:
{"entities": [{"text": "left ventricular dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Blockade of arrhythmias with both isomers was surmountable by increasing the dose of adrenaline.7 .

Example answer:
{"entities": [{"text": "arrhythmias", "type": "DiseaseOrPhenotypicFeature"}, {"text": "adrenaline.7", "type": "ChemicalEntity"}]}

Example input:
Sentence: In blocking the positive inotropic and chronotropic responses to isoprenaline , ( + ) -propranolol had less than one hundredth the potency of ( - ) -propranolol .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: Isoproterenol alone decreased left ventricular systolic pressure and myocardial contractility indexed as LVdp/dtmax and LVdp/dtmin .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Both isomers of propranolol were capable of preventing adrenaline-induced cardiac arrhythmias in cats anaesthetized with halothane , but the mean dose of ( - ) -propranolol was 0.09+/-0.02 mg/kg whereas that of ( + ) -propranolol was 4.2+/-1.2 mg/kg .

Example answer:
{"entities": [{"text": "propranolol", "type": "ChemicalEntity"}, {"text": "adrenaline-induced", "type": "ChemicalEntity"}, {"text": "cardiac arrhythmias", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cats", "type": "OrganismTaxon"}, {"text": "halothane", "type": "ChemicalEntity"}]}

Example input:
Sentence: Both isomers of propranolol were also capable of reversing ventricular tachycardia caused by ouabain in anaesthetized cats and dogs .

Example answer:
{"entities": [{"text": "propranolol", "type": "ChemicalEntity"}, {"text": "ventricular tachycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "cats", "type": "OrganismTaxon"}, {"text": "dogs", "type": "OrganismTaxon"}]}

Input:
Sentence: The 2:1 atrioventricular block improved to 1:1 conduction only after intravenous lidocaine infusion or a high dose of mexiletine , which also controlled the ventricular tachycardia .

## Item biored:test:145
Example input:
Sentence: Amiodarone and atazanavir are recognized CYP3A4 inhibitors .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "ChemicalEntity"}, {"text": "atazanavir", "type": "ChemicalEntity"}, {"text": "CYP3A4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Severe rhabdomyolysis and acute renal failure secondary to concomitant use of simvastatin , amiodarone , and atazanavir .

Example answer:
{"entities": [{"text": "rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acute renal failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "atazanavir", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHOD : Data were obtained from two clinical trials : 1 ) acute Epo exposure ( rHuEpo , 400 IU/kg ) followed by WAT biopsies after 1 h and 2 ) 10 weeks treatment with the erythropoiesis-stimulating agent ( ESA ) Darbepoietin-alpha .

Example answer:
{"entities": [{"text": "Epo", "type": "GeneOrGeneProduct"}, {"text": "erythropoiesis-stimulating agent", "type": "ChemicalEntity"}, {"text": "ESA", "type": "ChemicalEntity"}, {"text": "Darbepoietin-alpha", "type": "ChemicalEntity"}]}

Example input:
Sentence: The patient 's observations were within normal limits , he was administered oxygen via a face mask and glyceryl trinitrate ( GTN ) .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "oxygen", "type": "ChemicalEntity"}, {"text": "glyceryl trinitrate", "type": "ChemicalEntity"}, {"text": "GTN", "type": "ChemicalEntity"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Forty patients with a diagnosis consistent with a hematologic/oncologic disorder that required treatment with an aminoglycoside were randomized to either conventional or extended-interval amikacin .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "hematologic/oncologic disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "aminoglycoside", "type": "ChemicalEntity"}, {"text": "amikacin", "type": "ChemicalEntity"}]}

Example input:
Sentence: OBJECTIVE : This is to present reversible inferior colliculus lesions in metronidazole-induced encephalopathy , to focus on the diffusion-weighted imaging ( DWI ) and fluid attenuated inversion recovery ( FLAIR ) imaging .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metronidazole-induced", "type": "ChemicalEntity"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVE : To report a case of a severe interaction between simvastatin , amiodarone , and atazanavir resulting in rhabdomyolysis and acute renal failure .

Example answer:
{"entities": [{"text": "simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "atazanavir", "type": "ChemicalEntity"}, {"text": "rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acute renal failure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "ChemicalEntity"}, {"text": "AraG", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "VP", "type": "ChemicalEntity"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CPM", "type": "ChemicalEntity"}, {"text": "T-cell leukaemia or lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}]}

Input:
Sentence: OBJECTIVE : To describe the unmasking of pheochromocytoma in a patient treated with amisulpride and tiapride .

## Item biored:test:61
Example input:
Sentence: RESULTS : Nontoxic doses of dexrazoxane reduced myelosuppression and weight loss from daunorubicin and etoposide in mice and antagonized their antiproliferative effects in the colony assay ; however , dexrazoxane neither reduced myelosuppression , weight loss , nor the in vitro cytotoxicity from doxorubicin .

Example answer:
{"entities": [{"text": "dexrazoxane", "type": "ChemicalEntity"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "weight loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "daunorubicin", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cytotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "doxorubicin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Diazepam- , scopolamine- and ageing-induced amnesia served as the interoceptive behavioral models .

Example answer:
{"entities": [{"text": "Diazepam-", "type": "ChemicalEntity"}, {"text": "scopolamine-", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Crocin improves lipid dysregulation in subacute diazinon exposure through ERK1/2 pathway in rat liver .

Example answer:
{"entities": [{"text": "Crocin", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "diazinon", "type": "ChemicalEntity"}, {"text": "ERK1/2", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : 24 Rats were divided into 4 groups and received following treatments for 4 weeks ; Corn oil ( control ) , diazinon ( 15mg/kg per day , orally ) and crocin ( 12.5 and 25mg/kg per day , intraperitoneally ) in combination with diazinon ( 15 mg/kg ) .

Example answer:
{"entities": [{"text": "Rats", "type": "OrganismTaxon"}, {"text": "Corn oil", "type": "ChemicalEntity"}, {"text": "diazinon", "type": "ChemicalEntity"}, {"text": "crocin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The aim of this study was to evaluate changes in the regulation of lipid metabolism , ERK and LDLr expression in the liver of rats exposed to subacute diazinon .

Example answer:
{"entities": [{"text": "lipid", "type": "ChemicalEntity"}, {"text": "ERK", "type": "GeneOrGeneProduct"}, {"text": "LDLr", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "diazinon", "type": "ChemicalEntity"}]}

Example input:
Sentence: To determine whether there was a temporal relationship between VPA-associated oxidative stress and hepatotoxicity , adult male Sprague-Dawley rats were treated ip with VPA ( 500 mg/kg ) or 0.9 % saline ( vehicle ) once daily for 2 , 4 , 7 , 10 , or 14 days .

Example answer:
{"entities": [{"text": "VPA-associated", "type": "ChemicalEntity"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "VPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: A single dose of valproic acid ( VPA ) , which is a widely used antiepileptic drug , is associated with oxidative stress in rats , as recently demonstrated by elevated levels of 15-F ( 2t ) -isoprostane ( 15-F ( 2t ) -IsoP ) .

Example answer:
{"entities": [{"text": "valproic acid", "type": "ChemicalEntity"}, {"text": "VPA", "type": "ChemicalEntity"}, {"text": "antiepileptic drug", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "15-F ( 2t ) -isoprostane", "type": "ChemicalEntity"}, {"text": "15-F ( 2t ) -IsoP", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Exposure to azathioprine ( > or =2 microg/mL ) for 48 hours increased cytosolic Ca2+ activity and annexin V binding and decreased forward scatter .

Example answer:
{"entities": [{"text": "azathioprine", "type": "ChemicalEntity"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "annexin V", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The present study examined the influence of excitatory amino acid-mediated mechanisms in the IC on the catalepsy induced by the dopamine receptor blocker haloperidol administered systemically ( 1 or 0.5 mg/kg ) in rats .

Example answer:
{"entities": [{"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dopamine receptor", "type": "GeneOrGeneProduct"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In conclusion , administration of isoproterenol to rats results in primary loss of dystrophin , the most sensitive among the structural proteins that form the DGC that connects the extracellular matrix and the cytoskeleton in cardiomyocyte .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "dystrophin", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: In conclusion , CPA , diazepam and 2PAM in combination with atropine prevented the occurrence of serious signs of poisoning and thus reduced the toxicity of DFP in rat .

## Item biored:test:150
Example input:
Sentence: Of 13 documented fractures , 3 occurred after risperidone and SSRIs were started , and none occurred in patients with hyperprolactinemia .

Example answer:
{"entities": [{"text": "fractures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "risperidone", "type": "ChemicalEntity"}, {"text": "SSRIs", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hyperprolactinemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Hyperprolactinemia was present in 49 % of 83 boys ( n = 41 ) treated with risperidone for a mean of 2.9 years .

Example answer:
{"entities": [{"text": "Hyperprolactinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : This is the first study to link risperidone-induced hyperprolactinemia and SSRI treatment to lower BMD in children and adolescents .

Example answer:
{"entities": [{"text": "risperidone-induced", "type": "ChemicalEntity"}, {"text": "hyperprolactinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SSRI", "type": "ChemicalEntity"}]}

Example input:
Sentence: The homeostasis model assessment of insulin resistance also differed significantly among groups ( F ( 33 ) = 4.92 ; P = .01 ) ( clozapine > olanzapine > risperidone ) ( clozapine vs risperidone , t ( 33 ) = 2.94 ; P = .006 ; olanzapine vs risperidone , t ( 33 ) = 2.42 ; P = .02 ) .

Example answer:
{"entities": [{"text": "insulin resistance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clozapine", "type": "ChemicalEntity"}, {"text": "olanzapine", "type": "ChemicalEntity"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Telaprevir was considered the probable causative agent of an interaction with simvastatin according to the Drug Interaction Probability Scale .

Example answer:
{"entities": [{"text": "Telaprevir", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Multivariate logistic regression revealed the common haplotypes H1 ( AGACT ) , H2 ( AGAWT ) , and H3 ( AGAWC ) were associated with the persistent postoperative hypertension ( P = .01 , 0.03 , 0.005 after Bonferroni correction ) .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The incidence of discontinuations for hypertension-related and oedema-related AEs were significantly higher with etoricoxib ( 2.5 % and 1.1 % respectively ) compared with diclofenac ( 1.5 % and 0.4 % respectively ; p < 0.001 for hypertension and p < 0.01 for oedema ) .

Example answer:
{"entities": [{"text": "hypertension-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oedema-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oedema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : In a pooled analysis of 1460 ICH and 3817 IS/TIA , MB were more frequent in ICH vs IS/TIA in all treatment groups , but the excess increased from 2.8 ( odds ratio ; range , 2.3-3.5 ) in nonantithrombotic users to 5.7 ( range , 3.4-9.7 ) in antiplatelet users and 8.0 ( range , 3.5-17.8 ) in warfarin users ( P difference=0.01 ) .

Example answer:
{"entities": [{"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IS/TIA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The adverse drug reaction score obtained by the Naranjo algorithm was 6 in our case , indicating a probable relationship between the patient 's NMS-like adverse symptoms and the combined treatment used in this case .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "NMS-like", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: In our case , use of the Naranjo probability scale indicated a possible relationship between the hypertensive crisis and amisulpride and tiapride therapy .

## Item biored:test:53
Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "MPTP", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "METH-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: These results indicate that the TSPO ligand etifoxine attenuates brain injury and inflammation after ICH .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "etifoxine", "type": "ChemicalEntity"}, {"text": "brain injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cholecystokinin-octapeptide restored morphine-induced hippocampal long-term potentiation impairment in rats .

Example answer:
{"entities": [{"text": "Cholecystokinin-octapeptide", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Instead , ETO-induced OCT4A was concomitant with activation of AMPK , a key component of metabolic stress and autophagy regulation .

Example answer:
{"entities": [{"text": "ETO-induced", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this study , we determined the impact of a TSPO ligand , etifoxine , on brain injury and inflammation in 2 mouse models of ICH .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "etifoxine", "type": "ChemicalEntity"}, {"text": "brain injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Alpha-lipoic acid exerts neuroprotective effects against chemotherapy induced neurotoxicity in sensory neurons : it rescues the mitochondrial toxicity and induces the expression of frataxin , an essential mitochondrial protein with anti-oxidant and chaperone properties .

Example answer:
{"entities": [{"text": "Alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mitochondrial toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "frataxin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mechanistic studies revealed that OB rats are sensitized due to : ( 1 ) higher oxyradical stress leading to upregulation of uncoupling proteins 2 and 3 , ( 2 ) downregulation of cardiac peroxisome proliferators activated receptor-alpha , ( 3 ) decreased plasma adiponectin levels , ( 4 ) decreased cardiac fatty-acid oxidation ( 666.9+/-14.0 nmol/min/g heart in ND versus 400.2+/-11.8 nmol/min/g heart in OB ) , ( 5 ) decreased mitochondrial AMP-alpha2 protein kinase , and ( 6 ) 86 % drop in cardiac ATP levels accompanied by decreased ATP/ADP ratio after doxorubicin administration .

Example answer:
{"entities": [{"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "uncoupling proteins 2 and 3", "type": "GeneOrGeneProduct"}, {"text": "peroxisome proliferators activated receptor-alpha", "type": "GeneOrGeneProduct"}, {"text": "adiponectin", "type": "GeneOrGeneProduct"}, {"text": "fatty-acid", "type": "ChemicalEntity"}, {"text": "AMP-alpha2 protein kinase", "type": "GeneOrGeneProduct"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "ATP/ADP", "type": "ChemicalEntity"}, {"text": "doxorubicin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Acute morphine ( 30mg/kg , s.c. ) treatment significantly attenuated hippocampal LTP and CCK-8 ( 1ug , i.c.v . )

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CCK-8", "type": "ChemicalEntity"}]}

Example input:
Sentence: Acute analgesic and antiinflammatory activities were ascertained using acetic acid induced writhing model ( mice ) and carrageenan-induced rat paw edema model , respectively .

Example answer:
{"entities": [{"text": "acetic acid", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "carrageenan-induced", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although the underlying mechanism ( s ) are not well understood , these effects may involve an increase in acetylcholine ( ACh ) levels .

Example answer:
{"entities": [{"text": "acetylcholine", "type": "ChemicalEntity"}, {"text": "ACh", "type": "ChemicalEntity"}]}

Input:
Sentence: The acute toxicity of OPs is the result of their irreversible binding with AChEs in the central nervous system ( CNS ) , which elevates acetylcholine ( ACh ) levels .

## Item biored:test:147
Example input:
Sentence: The authors report here a depressed patient comorbid with postprandial dyspepsia who developed RLS after mirtazapine had been added to his domperidone therapy .

Example answer:
{"entities": [{"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "postprandial dyspepsia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RLS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mirtazapine", "type": "ChemicalEntity"}, {"text": "domperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Co-administration of lidocaine , bupivacaine or tricaine with desipramine reversed this effect .

Example answer:
{"entities": [{"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "bupivacaine", "type": "ChemicalEntity"}, {"text": "tricaine", "type": "ChemicalEntity"}, {"text": "desipramine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Optimal control of the absences was achieved with sodium valproate , lamotrigine , or ethosuximide alone or in combination .

Example answer:
{"entities": [{"text": "sodium valproate", "type": "ChemicalEntity"}, {"text": "lamotrigine", "type": "ChemicalEntity"}, {"text": "ethosuximide", "type": "ChemicalEntity"}]}

Example input:
Sentence: We describe a 70-year-old Hispanic woman who developed fulminant hepatic failure necessitating liver transplantation 10 weeks after conversion from simvastatin 40 mg/day to simvastatin 10 mg-ezetimibe 40 mg/day .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "fulminant hepatic failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: After discontinuing the oral alendronate , the patient underwent six cycles of hemodialysis and four cycles of LDL apheresis .

Example answer:
{"entities": [{"text": "alendronate", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Follow-up MRIs were performed on 5 patients from third to 14th days after discontinuation of metronidazole administration .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "metronidazole", "type": "ChemicalEntity"}]}

Example input:
Sentence: At admission simvastatin and all antiviral drugs were discontinued because toxicity due to a drug-drug interaction was suspected .

Example answer:
{"entities": [{"text": "simvastatin", "type": "ChemicalEntity"}, {"text": "antiviral drugs", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Simvastatinezetimibe and escitalopram ( which she was taking for depression ) were discontinued , and other potential causes of hepatotoxicity were excluded .

Example answer:
{"entities": [{"text": "Simvastatinezetimibe", "type": "ChemicalEntity"}, {"text": "escitalopram", "type": "ChemicalEntity"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}]}

Input:
Sentence: Both drugs were immediately discontinued , and the patient recovered after subsequent nicardipine and verapamil treatment .

## Item biored:test:185
Example input:
Sentence: Though FAS-670 polymorphisms did not show any significant difference , the proportion of subjects with IL1B-31TT ( or IL1B-511CC ) increased according to stage ( trend P=0.019 ) .

Example answer:
{"entities": [{"text": "FAS-670", "type": "GeneOrGeneProduct"}, {"text": "IL1B-31TT", "type": "GeneOrGeneProduct"}, {"text": "IL1B-511CC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We performed 2 sets of case-control comparisons using Japanese subjects ( first set : 830 patients with RA and 658 controls ; second set : 1112 patients with RA and 940 controls ) , and then performed a stratified analysis using human leukocyte antigen ( HLA ) -DRB1 shared epitope ( SE ) status .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "leukocyte antigen ( HLA ) -DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: None of the studied polymorphisms alone affected overall or progression-free survival ( PFS ) .

Example answer:
{"entities": []}

Example input:
Sentence: Subgroup analysis shows a higher incidence of the heterozygous ArgGly genotype in cancer cases than in the combined group of BPH and controls ( P < 0.05 ) ; this difference is statistically significant between cancer and BPH patients but not between cancer cases and community controls .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: No Hardy Weinberg disequilibrium and no significant difference in allele frequencies between patients and controls were observed for any variation .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Significant differences were detected in genotypic distribution ( p = 0.04 ) as well as the allelic frequency ( p = 0.003 ) between the SHCM patients and controls .

Example answer:
{"entities": [{"text": "SHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: A statistically significant difference in allele frequency between cases and controls was observed for 2 of the SNPs ( +3100 T/G and +8365 C/T ) , with an odds ratio of 0.78 ( 95 % CI=0.64-0.96 ) and 0.65 ( 95 % CI=0.45-0.94 ) respectively .

Example answer:
{"entities": [{"text": "+3100 T/G", "type": "SequenceVariant"}, {"text": "+8365 C/T", "type": "SequenceVariant"}]}

Example input:
Sentence: Whereas allele frequencies for the other two polymorphisms did not differ significantly between any of the groups , the 111G allele frequency was significantly higher in subjects with extreme morning preference ( 0.14 ) than in subjects with extreme evening preference ( 0.03 ) ( Fisher 's exact test , two-sided P value=0.031 , odds ratio=5.67 ) .

Example answer:
{"entities": [{"text": "111G", "type": "SequenceVariant"}]}

Example input:
Sentence: Both polymorphisms were in strong linkage disequilibrium ( D ' = 0.71 , P < .001 ) , and the 3R/-6 base pair ( bp ) haplotype showed a significant overall survival benefit compared with the most prevalent haplotype 2R/+6bp ( HR = 0.42 ; 95 % CI , 0.20 to 0.85 ; P = .017 ) .

Example answer:
{"entities": []}

Input:
Sentence: We found no statistically significant difference in either genotype or allele frequencies between cases and controls overall or between male and female cases for the BRAF polymorphism in the two incident case series .

## Item biored:test:173
Example input:
Sentence: Both minor alleles , adjusted for sex , age , BMI and insulin sensitivity were associated with elevated AUCproinsulin and AUCproinsulin/AUCinsulin ( rs6235 : p ( additive ) model < or= 0.009 , effect sizes 8/8 % , rs6232 : pdominant model < or= 0.01 , effect sizes 10/21 % ) .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "rs6235", "type": "SequenceVariant"}, {"text": "rs6232", "type": "SequenceVariant"}]}

Example input:
Sentence: The antibody reacted with the 80 kDa band protein in control fibroblasts , while no bands were detected in the fibroblasts from a patient with ALD ( # 163 ) , in which mRNA of the ALD gene was undetectable based on Northern blot analysis .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "ALD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALD", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The risk of developing T2D was approximately 2-fold in individuals with genotypes associated with higher 2-hour plasma glucose levels ; the hazard ratios were 2.192 ( p = 0.025 ) for rs2073162-A , 2.191 ( p = 0.027 ) for rs2073163-C , and 1.998 ( p = 0.054 ) for rs1155974-T .

Example answer:
{"entities": [{"text": "T2D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "rs2073162-A", "type": "SequenceVariant"}, {"text": "rs2073163-C", "type": "SequenceVariant"}, {"text": "rs1155974-T", "type": "SequenceVariant"}]}

Example input:
Sentence: We conclude that the SNPs of SLC2A2 predict the conversion to diabetes in obese subjects with IGT .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: An opposite effect was observed for the TLR4 D299G and TLR2 P631H variants , with a lower prevalence of ACCA antibodies ( 23.4 % versus 35 % , p = 0.013 ) and Omp antibodies ( 20.5 % versus 34.6 % , p = 0.009 ) , respectively .

Example answer:
{"entities": [{"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "D299G", "type": "SequenceVariant"}, {"text": "TLR2", "type": "GeneOrGeneProduct"}, {"text": "P631H", "type": "SequenceVariant"}]}

Example input:
Sentence: Significantly lower frequency of the A-C-C-G with higher frequency of A-C-A-G haplotypes was also noticed in subjects with DS ( P value =0.02089 and 0.00588 respectively ) .

Example answer:
{"entities": [{"text": "DS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All four SNPs of SLC2A2 predicted the conversion to diabetes , and rs5393 ( AA genotype ) increased the risk of type 2 diabetes in the entire study population by threefold ( odds ratio 3.04 , 95 % CI 1.34-6.88 , P = 0.008 ) .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs5393", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The p.A1369S variant was associated with a significantly lower risk of type 2 diabetes ( odds ratio [ OR ] 0.93 ; 95 % CI 0.91 , 0.95 ; P = 1.2 x 10 ( -11 ) ) .

Example answer:
{"entities": [{"text": "p.A1369S", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: RESULTS : The frequencies of the Asp/Glu and Glu/Glu were significantly increased in diabetic subjects with detectable IA-2 antibodies ( P < 0.01 ) .

## Item biored:test:142
Example input:
Sentence: Here , we investigated the effects of CCK-8 on long-term potentiation ( LTP ) in the lateral perforant path ( LPP ) -granule cell synapse of rat dentate gyrus ( DG ) in acute saline or morphine-treated rats .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "morphine-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Studies of synergy between morphine and a novel sodium channel blocker , CNSB002 , in rat models of inflammatory and neuropathic pain .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "sodium channel blocker", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathic pain", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DESIGN : Dose response curves for nonsedating doses of morphine and CNSB002 given intraperitoneally alone and together in combinations were constructed for antihyperalgesic effect using paw withdrawal from noxious heat in two rat pain models : carrageenan-induced paw inflammation and streptozotocin ( STZ ) -induced diabetic neuropathy .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "carrageenan-induced", "type": "ChemicalEntity"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "streptozotocin", "type": "ChemicalEntity"}, {"text": "STZ", "type": "ChemicalEntity"}, {"text": "diabetic neuropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present results demonstrate that CCK-8 attenuates the effect of morphine on hippocampal LTP through CCK2 receptors and suggest an ameliorative function of CCK-8 on morphine-induced memory impairment .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "morphine", "type": "ChemicalEntity"}, {"text": "CCK2 receptors", "type": "GeneOrGeneProduct"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "memory impairment", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Haloperidol-induced catalepsy was challenged with prior intracollicular microinjections of glutamate NMDA receptor antagonists , MK-801 ( 15 or 30 mmol/0.5 microl ) and AP7 ( 10 or 20 nmol/0.5 microl ) , or of the NMDA receptor agonist N-methyl-d-aspartate ( NMDA , 20 or 30 nmol/0.5 microl ) .

Example answer:
{"entities": [{"text": "Haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glutamate NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "N-methyl-d-aspartate", "type": "ChemicalEntity"}, {"text": "NMDA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Acute morphine ( 30mg/kg , s.c. ) treatment significantly attenuated hippocampal LTP and CCK-8 ( 1ug , i.c.v . )

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CCK-8", "type": "ChemicalEntity"}]}

Example input:
Sentence: The antinociception after morphine ( 3.2 mg/kg ) was increased by co-administration with CNSB002 from 28.0 and 31.7 % to 114.6 and 56.9 % reversal of hyperalgesia in the inflammatory and neuropathic models , respectively ( P < 0.01 ; one-way analysis of variance-significantly greater than either drug given alone ) .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "hyperalgesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We have previously reported that CCK-8 significantly alleviated morphine-induced amnesia and reversed spine density decreases in the CA1 region of the hippocampus in morphine-treated animals .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "morphine-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: Cholecystokinin-octapeptide restored morphine-induced hippocampal long-term potentiation impairment in rats .

Example answer:
{"entities": [{"text": "Cholecystokinin-octapeptide", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Glutamatergic neurotransmission mediated by NMDA receptors in the inferior colliculus can modulate haloperidol-induced catalepsy .

Example answer:
{"entities": [{"text": "NMDA receptors", "type": "GeneOrGeneProduct"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: These data indicate that IT morphine induces spastic paraparesis with a concomitant increase in CSF glutamate , which is involved in NMDA receptor activation .

## Item biored:test:159
Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: An intronic SNP , rs2622604 , in ABCG2 showed P ( Fisher ) =0.0419 in the second stage and indicated a significant association with severe myelosuppression in the combined study ( P ( Fisher ) =0.000237 ; P ( Corrected ) =0.036 ) .

Example answer:
{"entities": [{"text": "rs2622604", "type": "SequenceVariant"}, {"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We concluded that the CASP8 -652 6N del variant allele may contribute to the risk of developing SCCHN in non-Hispanic white populations .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In more than 98 % of cases , the disease is associated with a G to A or G to C substitution at nucleotide position 1138 ( p.G380R ) of the fibroblast growth factor receptor 3 ( FGFR3 ) gene .

Example answer:
{"entities": [{"text": "G to A or G to C substitution at nucleotide position 1138", "type": "SequenceVariant"}, {"text": "p.G380R", "type": "SequenceVariant"}, {"text": "fibroblast growth factor receptor 3", "type": "GeneOrGeneProduct"}, {"text": "FGFR3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: An analysis of the multiple single-nucleotide polymorphisms in SP-A demonstrated that homozygosity for alleles encoding lysine ( in 1A1 ) rather than glutamine ( in 1A5 ) at amino acid 223 in the carbohydrate recognition domain was associated with an increased risk of meningococcal disease ( OR , 6.7 ; 95 % CI , 1.4-31.5 ) .

Example answer:
{"entities": [{"text": "SP-A", "type": "GeneOrGeneProduct"}, {"text": "lysine ( in 1A1 ) rather than glutamine ( in 1A5 ) at amino acid 223", "type": "SequenceVariant"}, {"text": "carbohydrate", "type": "ChemicalEntity"}, {"text": "meningococcal disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DNA analysis revealed compound heterozygosity for mutations of GHR , including a previously reported R211H mutation and a novel duplication of a nucleotide in exon 9 ( 899dupC ) , the latter resulting in a frameshift and a premature stop codon .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "R211H", "type": "SequenceVariant"}, {"text": "899dupC", "type": "SequenceVariant"}]}

Example input:
Sentence: We describe in a BSS patient the first case of homozygous four bases deletion ( TGAG ) in the gpIbalpha gene coding sequence , leading to a premature stop codon .

Example answer:
{"entities": [{"text": "BSS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion ( TGAG )", "type": "SequenceVariant"}, {"text": "gpIbalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : A heterozygous germline T to C transition in exon 10 of the TSHR gene ( c.1358T -- > C ) resulting in the substitution of methionine ( ATG ) by threonine ( ACG ) at codon 453 ( p.M453T ) was identified in the father and his two children .

Example answer:
{"entities": [{"text": "T to C", "type": "SequenceVariant"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}, {"text": "c.1358T -- > C", "type": "SequenceVariant"}, {"text": "methionine ( ATG ) by threonine ( ACG ) at codon 453", "type": "SequenceVariant"}, {"text": "p.M453T", "type": "SequenceVariant"}]}

Example input:
Sentence: The allele frequencies of polymorphisms at codon 787 CAG/CAA ( Gln/Gln ) in glioblastomas in Japan were G/G ( 82.4 % ) , G/A ( 10.8 % ) , A/A ( 6.8 % ) , corresponding to G 0.878 versus A 0.122 , significantly different from those in glioblastomas in Switzerland : G/G ( 27.2 % ) , G/A ( 28.4 % ) , A/A ( 44.4 % ) , corresponding to G 0.414 versus A 0.586 ( p < 0.0001 ) .

Example answer:
{"entities": [{"text": "codon 787 CAG/CAA", "type": "SequenceVariant"}, {"text": "Gln/Gln", "type": "SequenceVariant"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A common A/G transition -1,071 bp from the transcriptional start site was genotyped and showed no evidence of association with prostate cancer .

Example answer:
{"entities": [{"text": "A/G transition -1,071 bp", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: RESULTS : Sporadic chondrocalcinosis was associated with a G-to-A transition in the ANKH 5'-untranslated region ( 5'-UTR ) at 4 bp upstream of the start codon ( in homozygotes of the minor allele , genotype relative risk 6.0 , P = 0.0006 ; overall genotype association P = 0.02 ) .

## Item biored:test:211
Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "Ato-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Serotonin was depleted beginning on postnatal day 26 with parachlorophenylalanine ( PCPA 100 mg/kg , every other day ) ; controls received saline .

Example answer:
{"entities": [{"text": "Serotonin", "type": "ChemicalEntity"}, {"text": "parachlorophenylalanine", "type": "ChemicalEntity"}, {"text": "PCPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHOD : Twenty cocaine-dependent participants were randomly assigned to receive modafinil , 400 mg ( N=10 ) , or placebo ( N=10 ) every morning at 7:30 a.m. for 16 days in an inpatient , double-blind randomized trial .

Example answer:
{"entities": [{"text": "cocaine-dependent", "type": "ChemicalEntity"}, {"text": "modafinil", "type": "ChemicalEntity"}, {"text": "inpatient", "type": "OrganismTaxon"}]}

Example input:
Sentence: They had been taking metronidazole ( total dosage , 45-120 g ; duration , 30 days to 2 months ) to treat the infection in various organs .

Example answer:
{"entities": [{"text": "metronidazole", "type": "ChemicalEntity"}, {"text": "infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: After three days , a cumulative dosage of 200 mg of CE in refracted doses were given .

Example answer:
{"entities": [{"text": "CE", "type": "ChemicalEntity"}]}

Example input:
Sentence: together for 30 consecutive days and challenged with ISO on the day 29th and 30th , showed a significant ( P < 0.05 ) decrease in heart weight , serum marker enzymes , lipid peroxidation , Ca+2 ATPase and a significant increase in the body weight , endogenous antioxidants , Na+/K+ ATPase and Mg+2 ATPase when compared with ISO treated group and green tea or vitamin E alone treated groups .

Example answer:
{"entities": [{"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}, {"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}]}

Example input:
Sentence: The patient was taking 80 mg simvastatin at bedtime ( initiated 27 days earlier ) ; amiodarone at a dose of 400 mg daily for 7 days , then 200 mg daily ( initiated 19 days earlier ) ; and 400 mg atazanavir daily ( initiated at least 2 years previously ) .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "atazanavir", "type": "ChemicalEntity"}]}

Example input:
Sentence: Doses were flexibly titrated up to 0.6 mg/day for clonidine and 60 mg/day for methylphenidate ( both with divided dosing ) .

Example answer:
{"entities": [{"text": "clonidine", "type": "ChemicalEntity"}, {"text": "methylphenidate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Instead , oral administration of S-1 ( a derivative of 5-FU ) , at 200 mg/day twice a week , was instituted , because S-1 has a strong inhibitory effect on dihydropyrimidine dehydrogenase , which catalyzes the degradative of 5-FU into FBAL .

Example answer:
{"entities": [{"text": "S-1", "type": "ChemicalEntity"}, {"text": "5-FU", "type": "ChemicalEntity"}, {"text": "dihydropyrimidine", "type": "ChemicalEntity"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: After 2-3 days , a single dose of 200 mg was administered .

Example answer:
{"entities": []}

Input:
Sentence: with 200mgkg ( -1 ) twice daily for 7 days .

## Item biored:test:193
Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mice were treated with saline or RAMH for 44 days and tumor volume was measured .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "RAMH", "type": "ChemicalEntity"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Continuous tracking of individual HSCs and their progeny via time-lapse microscopy elucidated that once GADD45A was expressed , HSCs differentiate into committed progenitors within 29 hours .

Example answer:
{"entities": [{"text": "GADD45A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: To determine the pathogenic importance of CB depletions in AD models , we crossed 5 familial AD mutations ( 5XFAD ; Tg ) mice with CB knock-out ( CBKO ) mice and generated a novel line CBKO.5XFAD ( CBKOTg ) mice .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "CBKO", "type": "GeneOrGeneProduct"}, {"text": "CBKO.5XFAD", "type": "GeneOrGeneProduct"}, {"text": "CBKOTg", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The brains were sectioned along coronal planes spanning the distribution of ischemia produced by MCAO .

Example answer:
{"entities": [{"text": "ischemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunohistochemistry showed that CBKOTg mice had significant neuronal loss in the subiculum area without changing the magnitude ( number ) of amyloid b-peptide ( Ab ) plaques deposition and elicited significant apoptotic features and mitochondrial dysfunction compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "neuronal loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "amyloid b-peptide", "type": "GeneOrGeneProduct"}, {"text": "Ab", "type": "GeneOrGeneProduct"}, {"text": "mitochondrial dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Four hours after MCAO , the rats were killed and the brains harvested .

Example answer:
{"entities": [{"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: A rat model of IUGR was established by PCE , male fetuses and adult offspring at the age of postnatal week 24 were euthanized .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "IUGR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Four animal groups ( n = 6 ) were tested during 9 weeks : control , CsA , SRL , and conversion ( CsA for 3 weeks followed by SRL for 6 weeks ) .

Example answer:
{"entities": [{"text": "CsA", "type": "ChemicalEntity"}, {"text": "SRL", "type": "ChemicalEntity"}]}

Example input:
Sentence: Animals were killed after 6 or 12 weeks , respectively .

Example answer:
{"entities": []}

Input:
Sentence: Animals were killed between 30 and 60 days later , and brain sections were processed for GAP43 immunohistochemistry .

## Item biored:test:168
Example input:
Sentence: The 1858T risk allele occurred on only a single haplotype that was strongly associated with type 1 diabetes ( P = 7.9 x 10 ( -5 ) ) .

Example answer:
{"entities": [{"text": "1858T", "type": "SequenceVariant"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We therefore examined the associations with AD of the DBH -1021T allele and of the above interactions in the Epistasis Project , with 1757 cases of AD and 6294 elderly controls .

Example answer:
{"entities": [{"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "-1021T", "type": "SequenceVariant"}]}

Example input:
Sentence: After controlling for the effects of this allele , two other haplotypes were observed to be weakly associated with type 1 diabetes ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , evidence supporting a role for PTPN22 in type 1 diabetes derives entirely from the study of just one coding single nucleotide polymorphism , 1858C/T .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "1858C/T", "type": "SequenceVariant"}]}

Example input:
Sentence: In the current study , the haplotype structure of the PTPN22 region was determined , and individual haplotypes were tested for association with type 1 diabetes in family-based tests .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Our results showed substantial evidence of association between -1607 promoter polymorphism of MMP1 and DDD in the Southern Chinese subjects .

Example answer:
{"entities": [{"text": "MMP1", "type": "GeneOrGeneProduct"}, {"text": "DDD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Interactions have been reported between the low-activity -1021T allele ( rs1611115 ) of DBH and polymorphisms of the pro-inflammatory cytokine genes , IL1A and IL6 , contributing to the risk of AD .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "rs1611115", "type": "SequenceVariant"}, {"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "IL1A", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results support the conclusion that the 1858C/T allele is the major risk variant for type 1 diabetes in the PTPN22 locus , but they suggest that additional infrequent coding variants at PTPN22 may also contribute to type 1 diabetes risk .

Example answer:
{"entities": [{"text": "1858C/T", "type": "SequenceVariant"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: D allelic was significantly associated with DDD ( p value = 0.027 , odds ratio = 1.41 with 95 % CI = 1.04-1.90 ) while Genotypic association on the presence of D allele was also significantly associated with DDD ( p value = 0.046 , odds ratio = 1.50 with 95 % CI = 1.01-2.24 ) .

Example answer:
{"entities": [{"text": "DDD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : We demonstrated that individuals with the presence of D allele for the -1607 promoter polymorphism of MMP1 are about 1.5 times more susceptible to develop DDD when compared with those having G allele only .

Example answer:
{"entities": [{"text": "D allele for the -1607", "type": "SequenceVariant"}, {"text": "MMP1", "type": "GeneOrGeneProduct"}, {"text": "DDD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Correlations between DBP alleles and type 1 diabetes have been described in different populations .

## Item biored:test:133
Example input:
Sentence: These findings suggest that glutamate-mediated mechanisms in the neural circuits at the IC level influence haloperidol-induced catalepsy and participate in the regulation of motor activity .

Example answer:
{"entities": [{"text": "glutamate-mediated", "type": "ChemicalEntity"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In aspartate , glutamine and glutamate levels detected a decrease of 5.21 % , 13.55 % and 21.80 % , respectively in mice hippocampus treated with GFC75 plus P400 when compared with seized mice .

Example answer:
{"entities": [{"text": "aspartate", "type": "ChemicalEntity"}, {"text": "glutamine", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}]}

Example input:
Sentence: Acute morphine ( 30mg/kg , s.c. ) treatment significantly attenuated hippocampal LTP and CCK-8 ( 1ug , i.c.v . )

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CCK-8", "type": "ChemicalEntity"}]}

Example input:
Sentence: The antinociception after morphine ( 3.2 mg/kg ) was increased by co-administration with CNSB002 from 28.0 and 31.7 % to 114.6 and 56.9 % reversal of hyperalgesia in the inflammatory and neuropathic models , respectively ( P < 0.01 ; one-way analysis of variance-significantly greater than either drug given alone ) .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "hyperalgesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Glutamatergic neurotransmission mediated by NMDA receptors in the inferior colliculus can modulate haloperidol-induced catalepsy .

Example answer:
{"entities": [{"text": "NMDA receptors", "type": "GeneOrGeneProduct"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DESIGN : Dose response curves for nonsedating doses of morphine and CNSB002 given intraperitoneally alone and together in combinations were constructed for antihyperalgesic effect using paw withdrawal from noxious heat in two rat pain models : carrageenan-induced paw inflammation and streptozotocin ( STZ ) -induced diabetic neuropathy .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "carrageenan-induced", "type": "ChemicalEntity"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "streptozotocin", "type": "ChemicalEntity"}, {"text": "STZ", "type": "ChemicalEntity"}, {"text": "diabetic neuropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Previous experiments in this laboratory have shown that microinjection of methyldopa onto the ventrolateral cells of the B3 serotonin neurons in the medulla elicits a hypotensive response mediated by a projection descending into the spinal cord .

Example answer:
{"entities": [{"text": "methyldopa", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "hypotensive", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "MPTP", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "METH-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: Cholecystokinin-octapeptide restored morphine-induced hippocampal long-term potentiation impairment in rats .

Example answer:
{"entities": [{"text": "Cholecystokinin-octapeptide", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: We have previously reported that CCK-8 significantly alleviated morphine-induced amnesia and reversed spine density decreases in the CA1 region of the hippocampus in morphine-treated animals .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "morphine-treated", "type": "ChemicalEntity"}]}

Input:
Sentence: The activation of spinal N-methyl-D-aspartate receptors may contribute to degeneration of spinal motor neurons induced by neuraxial morphine after a noninjurious interval of spinal cord ischemia .

## Item biored:test:175
Example input:
Sentence: However , evidence supporting a role for PTPN22 in type 1 diabetes derives entirely from the study of just one coding single nucleotide polymorphism , 1858C/T .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "1858C/T", "type": "SequenceVariant"}]}

Example input:
Sentence: The pathogenesis of human type 1 diabetes , characterized by immune-mediated damage of insulin-producing b-cells of pancreatic islets , may involve viral infection .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulin-producing", "type": "GeneOrGeneProduct"}, {"text": "viral infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Its +1858C > T ( R620W ) polymorphism has been shown to associate with a risk for multiple autoimmune diseases , including type 1 diabetes ( T1D ) and juvenile idiopathic arthritis ( JIA ) .

Example answer:
{"entities": [{"text": "+1858C > T", "type": "SequenceVariant"}, {"text": "R620W", "type": "SequenceVariant"}, {"text": "autoimmune diseases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "T1D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "juvenile idiopathic arthritis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "JIA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Superoxide dismutase 1 overexpression in mice abolishes maternal diabetes-induced endoplasmic reticulum stress in diabetic embryopathy .

Example answer:
{"entities": [{"text": "Superoxide dismutase 1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "maternal", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "embryopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Numerous aspects of human type 1 diabetes pathogenesis are recapitulated in the LEW.1WR1 rat model .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: Diabetes can be induced in LEW.1WR1 weanling rats challenged with virus or with the viral mimetic polyinosinic : polycytidylic acid ( poly I : C ) .

Example answer:
{"entities": [{"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "polyinosinic : polycytidylic acid", "type": "ChemicalEntity"}, {"text": "poly I : C", "type": "ChemicalEntity"}]}

Example input:
Sentence: Essential components of the innate immune antiviral response , including type I interferon ( IFN ) and IFN receptor-mediated signaling pathways , are candidates for determining susceptibility to human type 1 diabetes .

Example answer:
{"entities": [{"text": "type I interferon", "type": "GeneOrGeneProduct"}, {"text": "IFN", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Vitamin E reduces cardiovascular disease in individuals with diabetes mellitus and the haptoglobin 2-2 genotype .

Example answer:
{"entities": [{"text": "Vitamin E", "type": "ChemicalEntity"}, {"text": "cardiovascular disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "haptoglobin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A Critical Role for the Type I Interferon Receptor in Virus-Induced Autoimmune Diabetes in Rats .

Example answer:
{"entities": [{"text": "Type I Interferon Receptor", "type": "GeneOrGeneProduct"}, {"text": "Autoimmune Diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: These findings firmly establish that alterations in innate immunity influence the course of autoimmune diabetes and support the use of targeted strategies to limit or prevent the development of type 1 diabetes .

Example answer:
{"entities": [{"text": "autoimmune diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: These finding supports a role of the vitamin D endocrine system in the autoimmune process of type 1 diabetes .

## Item biored:test:144
Example input:
Sentence: Aryl hydrocarbon receptor interacting protein ( AIP ) gene mutation analysis in children and adolescents with sporadic pituitary adenomas .

Example answer:
{"entities": [{"text": "Aryl hydrocarbon receptor interacting protein", "type": "GeneOrGeneProduct"}, {"text": "AIP", "type": "GeneOrGeneProduct"}, {"text": "pituitary adenomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Forty patients with a diagnosis consistent with a hematologic/oncologic disorder that required treatment with an aminoglycoside were randomized to either conventional or extended-interval amikacin .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "hematologic/oncologic disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "aminoglycoside", "type": "ChemicalEntity"}, {"text": "amikacin", "type": "ChemicalEntity"}]}

Example input:
Sentence: A g-secretase inhibitor , DAPT , selectively depleted CD133 ( + ) cells , suppressed N1ICD and SKP2 , induced p27Kip1 , inhibited ACC growthin vivo , and sensitized CD133 ( + ) cells to radiation .

Example answer:
{"entities": [{"text": "g-secretase", "type": "GeneOrGeneProduct"}, {"text": "DAPT", "type": "ChemicalEntity"}, {"text": "CD133", "type": "GeneOrGeneProduct"}, {"text": "N1ICD", "type": "GeneOrGeneProduct"}, {"text": "SKP2", "type": "GeneOrGeneProduct"}, {"text": "p27Kip1", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: It was partially reduced by PKC- or Src-inhibition , but not with PI3K-inhibitors ( wortmannin , LY294002 ) or thapsigargin .

Example answer:
{"entities": [{"text": "PKC-", "type": "GeneOrGeneProduct"}, {"text": "Src-inhibition", "type": "GeneOrGeneProduct"}, {"text": "PI3K-inhibitors", "type": "GeneOrGeneProduct"}, {"text": "wortmannin", "type": "ChemicalEntity"}, {"text": "LY294002", "type": "ChemicalEntity"}, {"text": "thapsigargin", "type": "ChemicalEntity"}]}

Example input:
Sentence: In vitro , the HK2 cells were treated with iopamidol in the presence or absence of atorvastatin , heat shock protein ( Hsp ) 27 small interfering ( si ) RNA or pcDNA3.1-Hsp27 .

Example answer:
{"entities": [{"text": "HK2", "type": "CellLine"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "heat shock protein ( Hsp ) 27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "ChemicalEntity"}, {"text": "AraG", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "VP", "type": "ChemicalEntity"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CPM", "type": "ChemicalEntity"}, {"text": "T-cell leukaemia or lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Amiodarone and atazanavir are recognized CYP3A4 inhibitors .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "ChemicalEntity"}, {"text": "atazanavir", "type": "ChemicalEntity"}, {"text": "CYP3A4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}]}

Input:
Sentence: Pheochromocytoma unmasked by amisulpride and tiapride .

## Item biored:test:169
Example input:
Sentence: No independent role of the -1123 G > C and+2740 A > G variants in the association of PTPN22 with type 1 diabetes and juvenile idiopathic arthritis in two Caucasian populations .

Example answer:
{"entities": [{"text": "-1123 G > C", "type": "SequenceVariant"}, {"text": "A > G", "type": "SequenceVariant"}, {"text": "PTPN22", "type": "GeneOrGeneProduct"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "juvenile idiopathic arthritis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Its +1858C > T ( R620W ) polymorphism has been shown to associate with a risk for multiple autoimmune diseases , including type 1 diabetes ( T1D ) and juvenile idiopathic arthritis ( JIA ) .

Example answer:
{"entities": [{"text": "+1858C > T", "type": "SequenceVariant"}, {"text": "R620W", "type": "SequenceVariant"}, {"text": "autoimmune diseases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "T1D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "juvenile idiopathic arthritis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "JIA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : In two different Caucasian populations , the Czechs and the Azeri , no independent contribution can be detected either of the -1123 promoter SNP or the +2740 3'-UTR SNP , and only the minor allele at PTPN22 codon 620 contributes to the risk of autoimmunity .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In the current study , the haplotype structure of the PTPN22 region was determined , and individual haplotypes were tested for association with type 1 diabetes in family-based tests .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Our results showed substantial evidence of association between -1607 promoter polymorphism of MMP1 and DDD in the Southern Chinese subjects .

Example answer:
{"entities": [{"text": "MMP1", "type": "GeneOrGeneProduct"}, {"text": "DDD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : We demonstrated that individuals with the presence of D allele for the -1607 promoter polymorphism of MMP1 are about 1.5 times more susceptible to develop DDD when compared with those having G allele only .

Example answer:
{"entities": [{"text": "D allele for the -1607", "type": "SequenceVariant"}, {"text": "MMP1", "type": "GeneOrGeneProduct"}, {"text": "DDD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results support the conclusion that the 1858C/T allele is the major risk variant for type 1 diabetes in the PTPN22 locus , but they suggest that additional infrequent coding variants at PTPN22 may also contribute to type 1 diabetes risk .

Example answer:
{"entities": [{"text": "1858C/T", "type": "SequenceVariant"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A recent addition to the list of widely confirmed type 1 diabetes risk loci is the PTPN22 gene encoding a lymphoid-specific phosphatase ( Lyp ) .

Example answer:
{"entities": [{"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTPN22", "type": "GeneOrGeneProduct"}, {"text": "lymphoid-specific phosphatase", "type": "GeneOrGeneProduct"}, {"text": "Lyp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: However , evidence supporting a role for PTPN22 in type 1 diabetes derives entirely from the study of just one coding single nucleotide polymorphism , 1858C/T .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "1858C/T", "type": "SequenceVariant"}]}

Example input:
Sentence: Interactions have been reported between the low-activity -1021T allele ( rs1611115 ) of DBH and polymorphisms of the pro-inflammatory cytokine genes , IL1A and IL6 , contributing to the risk of AD .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "rs1611115", "type": "SequenceVariant"}, {"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "IL1A", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Therefore , we investigated the polymorphism in codon 416 of the DBP gene for an association with autoimmune markers of type 1 diabetes .

## Item biored:test:134
Example input:
Sentence: Acute morphine ( 30mg/kg , s.c. ) treatment significantly attenuated hippocampal LTP and CCK-8 ( 1ug , i.c.v . )

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CCK-8", "type": "ChemicalEntity"}]}

Example input:
Sentence: OIH was achieved in mice after subcutaneous administration of morphine for 7 consecutive days three times per day .

Example answer:
{"entities": [{"text": "OIH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "morphine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "MPTP", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "METH-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: DESIGN : Dose response curves for nonsedating doses of morphine and CNSB002 given intraperitoneally alone and together in combinations were constructed for antihyperalgesic effect using paw withdrawal from noxious heat in two rat pain models : carrageenan-induced paw inflammation and streptozotocin ( STZ ) -induced diabetic neuropathy .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "carrageenan-induced", "type": "ChemicalEntity"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "streptozotocin", "type": "ChemicalEntity"}, {"text": "STZ", "type": "ChemicalEntity"}, {"text": "diabetic neuropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "a reduced locomotor activity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These findings suggest that glutamate-mediated mechanisms in the neural circuits at the IC level influence haloperidol-induced catalepsy and participate in the regulation of motor activity .

Example answer:
{"entities": [{"text": "glutamate-mediated", "type": "ChemicalEntity"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we investigated the effects of CCK-8 on long-term potentiation ( LTP ) in the lateral perforant path ( LPP ) -granule cell synapse of rat dentate gyrus ( DG ) in acute saline or morphine-treated rats .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "morphine-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Glutamatergic neurotransmission mediated by NMDA receptors in the inferior colliculus can modulate haloperidol-induced catalepsy .

Example answer:
{"entities": [{"text": "NMDA receptors", "type": "GeneOrGeneProduct"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cholecystokinin-octapeptide restored morphine-induced hippocampal long-term potentiation impairment in rats .

Example answer:
{"entities": [{"text": "Cholecystokinin-octapeptide", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: We have previously reported that CCK-8 significantly alleviated morphine-induced amnesia and reversed spine density decreases in the CA1 region of the hippocampus in morphine-treated animals .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "morphine-treated", "type": "ChemicalEntity"}]}

Input:
Sentence: We investigated the relationship between the degeneration of spinal motor neurons and activation of N-methyl-d-aspartate ( NMDA ) receptors after neuraxial morphine following a noninjurious interval of aortic occlusion in rats .

## Item biored:test:205
Example input:
Sentence: Oprm1 may also be utilized for effective treatment of L-asparaginase-resistant ALL.Oncogene advance online publication , 26 June 2017 ; doi:10.1038/onc.2017.211 .

Example answer:
{"entities": [{"text": "Oprm1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase-resistant", "type": "ChemicalEntity"}, {"text": "ALL.Oncogene", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Ten subjects with OPMD ( 6 symptomatic and 4 asymptomatic ) within the Taiwanese family carried a novel mutation in the PABPN1 gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Molecular dynamic simulations of structural changes induced by L1503R indicated that the mean value of all-atom root-mean-squared-deviation was shifted from those with wild type or another mutation L1503Q that has been reported to be a group II mutation , which is susceptible to ADAMTS13 proteolysis .

Example answer:
{"entities": [{"text": "L1503R", "type": "SequenceVariant"}, {"text": "L1503Q", "type": "SequenceVariant"}, {"text": "ADAMTS13", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also found that OPRM1 is expressed in all leukemic cells tested .

Example answer:
{"entities": [{"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "leukemic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OPMD is caused by a short trinucleotide repeat expansion encoding an expanded polyalanine tract in the polyadenylate binding-protein nuclear 1 ( PABPN1 ) gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "polyalanine", "type": "ChemicalEntity"}, {"text": "polyadenylate binding-protein nuclear 1", "type": "GeneOrGeneProduct"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: By unbiased genome-wide RNAi screening , we found that among 10 resistant ALL clones , six hits were for opioid receptor mu 1 ( oprm1 ) , two hits were for carbonic anhydrase 1 ( ca1 ) and another two hits were for ubiquitin-conjugating enzyme E2C ( ube2c ) .

Example answer:
{"entities": [{"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "opioid receptor mu 1", "type": "GeneOrGeneProduct"}, {"text": "oprm1", "type": "GeneOrGeneProduct"}, {"text": "carbonic anhydrase 1", "type": "GeneOrGeneProduct"}, {"text": "ca1", "type": "GeneOrGeneProduct"}, {"text": "ubiquitin-conjugating enzyme E2C", "type": "GeneOrGeneProduct"}, {"text": "ube2c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Consistent with this premise , patient leukemic cells with relatively high levels of OPRM1 are more sensitive to L-asparaginase treatment compared to OPRM1-depleted leukemic cells , further indicating that OPRM1 loss has a crucial role in L-asparaginase resistance in leukemic patients .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "leukemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "OPRM1-depleted", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Specific knockdown of OPRM1 confers L-asparaginase resistance , validating our genome-wide retroviral shRNA library screening data .

Example answer:
{"entities": [{"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}]}

Example input:
Sentence: Thus , our study demonstrates for the first time , a novel OPRM1-mediated mechanism for L-asparaginase resistance in ALL , and identifies OPRM1 as a functional biomarker for defining high-risk subpopulations and for the detection of evolving resistant clones .

Example answer:
{"entities": [{"text": "OPRM1-mediated", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: These results indicate that OPRM1-G118 is a functional variant with deleterious effects on both mRNA and protein yield .

## Item biored:test:116
Example input:
Sentence: Molecular dynamic ( MD ) simulations showed that the overall effect of the mutation p.Val204Asp is disruption of hydrogen bonding between Gln223 and Glu441 , leading Ser198 and His438 to move away from each other with subsequent disruption of the catalytic triad functionality regardless of the type of substrate .

Example answer:
{"entities": [{"text": "p.Val204Asp", "type": "SequenceVariant"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: Here , we report a novel natural RTH mutation ( E333D ) located in the large carboxy-terminal ligand binding domain of TRbeta .

Example answer:
{"entities": [{"text": "RTH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "E333D", "type": "SequenceVariant"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : The patient 's GR gene had a heterozygotic mutation ( G -- > A ) at nucleotide position 2141 ( exon 8 ) , which resulted in substitution of arginine by glutamine at amino acid position 714 in the ligand-binding domain ( LBD ) of the GR alpha .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "( G -- > A ) at nucleotide position 2141", "type": "SequenceVariant"}, {"text": "arginine by glutamine at amino acid position 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The C139T mutation , predicted to result in the substitution of an arginine by a tryptophan ( R47W ) in the N-terminal subdomain , affected conserved residues in the PAX9 paired domain .

Example answer:
{"entities": [{"text": "C139T", "type": "SequenceVariant"}, {"text": "arginine by a tryptophan", "type": "SequenceVariant"}, {"text": "R47W", "type": "SequenceVariant"}, {"text": "PAX9", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : A heterozygous germline T to C transition in exon 10 of the TSHR gene ( c.1358T -- > C ) resulting in the substitution of methionine ( ATG ) by threonine ( ACG ) at codon 453 ( p.M453T ) was identified in the father and his two children .

Example answer:
{"entities": [{"text": "T to C", "type": "SequenceVariant"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}, {"text": "c.1358T -- > C", "type": "SequenceVariant"}, {"text": "methionine ( ATG ) by threonine ( ACG ) at codon 453", "type": "SequenceVariant"}, {"text": "p.M453T", "type": "SequenceVariant"}]}

Example input:
Sentence: In LCD , three novel heterozygous mutations found were glycine-594-valine ( Gly594Val ) in 2 of 18 patients , valine-539-aspartic acid ( Val539Asp ) in 1 patient , and deletion of valine 624 , valine 625 ( Val624-Val625del ) in 1 patient .

Example answer:
{"entities": [{"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glycine-594-valine", "type": "SequenceVariant"}, {"text": "Gly594Val", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "valine-539-aspartic acid", "type": "SequenceVariant"}, {"text": "Val539Asp", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion of valine 624 , valine 625", "type": "SequenceVariant"}, {"text": "Val624-Val625del", "type": "SequenceVariant"}]}

Example input:
Sentence: The two transversions resulted in the substitution of a stop codon for glutamine at codon 298 ( p.Q298X ) and a missense mutation at codon 358 , tyrosine to histidine ( p.Y358H ) .

Example answer:
{"entities": [{"text": "stop codon for glutamine at codon 298", "type": "SequenceVariant"}, {"text": "p.Q298X", "type": "SequenceVariant"}, {"text": "codon 358 , tyrosine to histidine", "type": "SequenceVariant"}, {"text": "p.Y358H", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Input:
Sentence: RESULTS : A novel , spontaneous LQTS-3 mutation was identified in the transmembrane segment 6 of domain IV of the Na ( v ) 1.5 cardiac sodium channel , with a G -- > A substitution at codon 1763 , which changed a valine ( GTG ) to a methionine ( ATG ) .
