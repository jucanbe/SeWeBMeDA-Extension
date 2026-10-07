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

## Item biored:test:41
Example input:
Sentence: We provide experimental data suggesting PCC to be an effective acute treatment for W-ICH in terms of reducing hemorrhagic blood volume .

Example answer:
{"entities": [{"text": "PCC", "type": "ChemicalEntity"}, {"text": "W-ICH", "type": "ChemicalEntity"}]}

Example input:
Sentence: The results showed that intracollicular microinjection of MK-801 and AP7 previous to systemic injections of haloperidol significantly attenuated the catalepsy , as indicated by a reduced latency to step down from a horizontal bar .

Example answer:
{"entities": [{"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: As tranexamic acid is the only modifiable factor , its administration , particularly in doses exceeding 80 mg.kg ( -1 ) , should be weighed against the risk of postoperative seizures .

Example answer:
{"entities": [{"text": "tranexamic acid", "type": "ChemicalEntity"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To determine whether there was a temporal relationship between VPA-associated oxidative stress and hepatotoxicity , adult male Sprague-Dawley rats were treated ip with VPA ( 500 mg/kg ) or 0.9 % saline ( vehicle ) once daily for 2 , 4 , 7 , 10 , or 14 days .

Example answer:
{"entities": [{"text": "VPA-associated", "type": "ChemicalEntity"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "VPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : These results suggest that bupivacaine stimulates COX-2 gene expression after tissue injury , which is associated with higher PGE2 production and pain after the local anesthetic effect dissipates .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "ChemicalEntity"}, {"text": "COX-2", "type": "GeneOrGeneProduct"}, {"text": "tissue injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Omission of fentanyl did not reduce the overall incidence of postoperative nausea and vomiting , but did reduce the incidence of vomiting and/or moderate to severe nausea prior to discharge from 20 % and 17 % with fentanyl and fentanyl-dexamethasone , respectively , to 5 % ( P = 0.013 ) .

Example answer:
{"entities": [{"text": "fentanyl", "type": "ChemicalEntity"}, {"text": "postoperative nausea and vomiting", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vomiting", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nausea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fentanyl-dexamethasone", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Ninety-three patients with APA were assessed for postoperative resolution of hypertension .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "APA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Combining the two fentanyl groups revealed further significant benefits from the avoidance of opioids , reducing postoperative nausea and vomiting and nausea prior to discharge from 35 % and 33 % to 22 % and 19 % ( P = 0.049 and P = 0.035 ) , respectively , while nausea in the first 24 h was decreased from 42 % to 27 % ( P = 0.034 ) .

Example answer:
{"entities": [{"text": "fentanyl", "type": "ChemicalEntity"}, {"text": "postoperative nausea and vomiting", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nausea", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the present study , we describe the proinflammatory effects of bupivacaine on local prostaglandin E2 ( PGE2 ) production and cyclooxygenase ( COX ) gene expression that increases postoperative pain in human subjects .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "ChemicalEntity"}, {"text": "prostaglandin E2", "type": "GeneOrGeneProduct"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}, {"text": "cyclooxygenase", "type": "GeneOrGeneProduct"}, {"text": "COX", "type": "GeneOrGeneProduct"}, {"text": "postoperative pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}]}

Input:
Sentence: The routine use of pethidine via PCA even for a brief postoperative analgesia should be reconsidered .

## Item biored:test:3
Example input:
Sentence: To our knowledge , there is no previous report regarding whether domperidone , a peripheral dopamine D2 receptor antagonist , can also induce or aggravate symptoms of RLS .

Example answer:
{"entities": [{"text": "domperidone", "type": "ChemicalEntity"}, {"text": "dopamine D2 receptor", "type": "GeneOrGeneProduct"}, {"text": "RLS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These findings suggest that estrogen downregulates alpha2- but not I1-receptor-mediated hypotension and highlight a role for the cardiac autonomic control in alpha-methyldopa-estrogen interaction .

Example answer:
{"entities": [{"text": "estrogen", "type": "ChemicalEntity"}, {"text": "alpha2- but not", "type": "GeneOrGeneProduct"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-methyldopa-estrogen", "type": "ChemicalEntity"}]}

Example input:
Sentence: At dose levels of ( + ) -propranolol which attenuated the responses to isoprenaline , there was a significant prolongation of the PR interval of the electrocardiogram.3 .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: The optical isomers of propranolol have been compared for their beta-blocking and antiarrhythmic activities.2 .

Example answer:
{"entities": [{"text": "propranolol", "type": "ChemicalEntity"}]}

Example input:
Sentence: While postjunctional beta-adrenoceptor-mediated relaxations are reduced , effects by prejunctional inhibitory muscarinic receptors may be increased .

Example answer:
{"entities": [{"text": "beta-adrenoceptor-mediated", "type": "GeneOrGeneProduct"}, {"text": "muscarinic receptors", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The beta-adrenergic receptors ( beta-AR ) are G protein-coupled receptors activated by epinephrine and norepinephrine and are involved in a variety of their physiological functions .

Example answer:
{"entities": [{"text": "beta-adrenergic receptors", "type": "GeneOrGeneProduct"}, {"text": "beta-AR", "type": "GeneOrGeneProduct"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "norepinephrine", "type": "ChemicalEntity"}]}

Example input:
Sentence: The dose of ( - ) -propranolol was significantly smaller than that of ( + ) -propranolol in both species but much higher than that required to produce evidence of beta-blockade.8 .

Example answer:
{"entities": []}

Example input:
Sentence: In blocking the positive inotropic and chronotropic responses to isoprenaline , ( + ) -propranolol had less than one hundredth the potency of ( - ) -propranolol .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: In experiments using specific adrenergic antagonists , we found that pretreatment with the beta-adrenergic receptor antagonist propranolol blocked cocaine-induced anxiety-like behavior in Dbh +/- and wild-type C57BL6/J mice , while the alpha ( 1 ) antagonist prazosin and the alpha ( 2 ) antagonist yohimbine had no effect .

Example answer:
{"entities": [{"text": "adrenergic antagonists", "type": "ChemicalEntity"}, {"text": "beta-adrenergic receptor", "type": "GeneOrGeneProduct"}, {"text": "propranolol", "type": "ChemicalEntity"}, {"text": "cocaine-induced", "type": "ChemicalEntity"}, {"text": "anxiety-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "alpha ( 1 )", "type": "GeneOrGeneProduct"}, {"text": "prazosin", "type": "ChemicalEntity"}, {"text": "alpha ( 2 )", "type": "GeneOrGeneProduct"}, {"text": "yohimbine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Metfromin markedly lowered isoproterenol-induced elevation in the levels of TLR4 mRNA , myeloid differentiation protein 88 ( MyD88 ) , tumor necrosis factor-alpha ( TNF-a ) , and interleukin 6 ( IL-6 ) in the heart tissues .

Example answer:
{"entities": [{"text": "Metfromin", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "myeloid differentiation protein 88", "type": "GeneOrGeneProduct"}, {"text": "MyD88", "type": "GeneOrGeneProduct"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}, {"text": "interleukin 6", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: We investigated if the latter also applies to the beta-2 adrenoceptor antagonism by metoprolol .

## Item biored:test:1
Example input:
Sentence: Characterization of a novel BCHE `` silent '' allele : point mutation ( p.Val204Asp ) causes loss of activity and prolonged apnea with suxamethonium .

Example answer:
{"entities": [{"text": "BCHE", "type": "GeneOrGeneProduct"}, {"text": "p.Val204Asp", "type": "SequenceVariant"}, {"text": "apnea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "suxamethonium", "type": "ChemicalEntity"}]}

Example input:
Sentence: Changes evoked by a single intraperitoneal injection of rilmenidine ( 600 microg/kg ) or alpha-methyldopa ( 100 mg/kg ) , selective I1- and alpha2-receptor agonists , respectively , in blood pressure , hemodynamic variability , and locomotor activity were assessed in radiotelemetered sham-operated and ovariectomized ( Ovx ) Sprague-Dawley female rats with or without 12-wk estrogen replacement .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "I1- and alpha2-receptor", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "estrogen", "type": "ChemicalEntity"}]}

Example input:
Sentence: Notably , the same mutation is associated with the Hamel cerebropalatocardiac syndrome , another form of S-XLMR .

Example answer:
{"entities": [{"text": "Hamel cerebropalatocardiac syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Low activity of patient plasma butyrylcholinesterase with butyrylthiocholine ( BTC ) and benzoylcholine , and values of dibucaine and fluoride numbers fit with heterozygous atypical silent genotype .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "butyrylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "butyrylthiocholine", "type": "ChemicalEntity"}, {"text": "BTC", "type": "ChemicalEntity"}, {"text": "benzoylcholine", "type": "ChemicalEntity"}, {"text": "dibucaine", "type": "ChemicalEntity"}, {"text": "fluoride", "type": "ChemicalEntity"}]}

Example input:
Sentence: A heterozygous caveolin-1 c.474delA mutation has been identified in a family with heritable pulmonary arterial hypertension ( PAH ) .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "pulmonary arterial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Butyrylcholinesterase deficiency is characterized by prolonged apnea after the use of muscle relaxants ( suxamethonium or mivacurium ) in patients who have mutations in the BCHE gene .

Example answer:
{"entities": [{"text": "Butyrylcholinesterase deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "apnea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "muscle relaxants", "type": "ChemicalEntity"}, {"text": "suxamethonium", "type": "ChemicalEntity"}, {"text": "mivacurium", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "BCHE", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Aberrant caveolin-1-mediated Smad signaling and proliferation identified by analysis of adenine 474 deletion mutation ( c.474delA ) in patient fibroblasts : a new perspective on the mechanism of pulmonary hypertension .

Example answer:
{"entities": [{"text": "caveolin-1-mediated", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "adenine 474 deletion", "type": "SequenceVariant"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "pulmonary hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Metfromin markedly lowered isoproterenol-induced elevation in the levels of TLR4 mRNA , myeloid differentiation protein 88 ( MyD88 ) , tumor necrosis factor-alpha ( TNF-a ) , and interleukin 6 ( IL-6 ) in the heart tissues .

Example answer:
{"entities": [{"text": "Metfromin", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "myeloid differentiation protein 88", "type": "GeneOrGeneProduct"}, {"text": "MyD88", "type": "GeneOrGeneProduct"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}, {"text": "interleukin 6", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Several studies have reported that , compared with wild-type individuals , CYP2C19 variant allele carriers exhibit a significantly lower capacity to metabolize clopidogrel into its active metabolite and inhibit platelet activation , and are therefore at significantly higher risk of adverse cardiovascular events .

Example answer:
{"entities": [{"text": "CYP2C19", "type": "GeneOrGeneProduct"}, {"text": "clopidogrel", "type": "ChemicalEntity"}]}

Input:
Sentence: The metabolism of the cardioselective beta-blocker metoprolol is under genetic control of the debrisoquine/sparteine type .

## Item biored:test:63
Example input:
Sentence: A novel missense mutation c.643T > C ( p.S216P ) was detected in the anterior segment malformation group .

Example answer:
{"entities": [{"text": "c.643T > C", "type": "SequenceVariant"}, {"text": "p.S216P", "type": "SequenceVariant"}, {"text": "anterior segment malformation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel mutation in the connexin 26 gene ( GJB2 ) in a child with clinical and histological features of keratitis-ichthyosis-deafness ( KID ) syndrome .

Example answer:
{"entities": [{"text": "connexin 26", "type": "GeneOrGeneProduct"}, {"text": "GJB2", "type": "GeneOrGeneProduct"}, {"text": "keratitis-ichthyosis-deafness ( KID ) syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Of them , two patients carrying E359K mutation were from two generations in one family with ventricular septal defect ( VSD ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Macular corneal dystrophy in a Chinese family related with novel mutations of CHST6 .

Example answer:
{"entities": [{"text": "Macular corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CHST6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The result expands the mutation spectrum of GJA8 in associated with congenital cataract and microcornea , and implies that this gene has direct involvement with the development of the lens as well as the other anterior segment of the eye .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcornea", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the current study , a three generation Asian Indian family with 15 congenital microcoria ( pupils with a diameter < 2 mm ) affected members was studied for linkage to candidate microsatellite markers at the 13q31-q32 locus .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : To identify the genetic basis of recessive inheritance of high hyperopia and Leber congenital amaurosis ( LCA ) in a family of Middle Eastern origin .

Example answer:
{"entities": [{"text": "high hyperopia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Leber congenital amaurosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LCA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel mutation in GJA8 causing congenital cataract-microcornea syndrome in a Chinese pedigree .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : To identify the underlying genetic defect in a four-generation family of Chinese origin with autosomal dominant congenital cataract-microcornea syndrome ( CCMC ) .

Example answer:
{"entities": [{"text": "genetic defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CCMC", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: PURPOSE : To identify the genetic defect leading to the congenital nuclear cataract affecting a large five-generation Swiss family .

## Item biored:test:0
Example input:
Sentence: On the Positive and Negative Syndrome Scale positive subscale , all treatments were superior to placebo with LOCF and MMRM ; asenapine at 5 mg BID was superior to placebo on the negative subscale with MMRM and on the general psychopathology subscale with LOCF and MMRM .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: and metrifonate ( 10 mg/kg , p.o. , respectively ) reversed memory deficits induced by scopolamine and TRP depletion ( 10 mg/kg , i.p. , and 3 mg/kg , p.o. , respectively ) .

Example answer:
{"entities": [{"text": "memory", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Haloperidol-induced catalepsy was challenged with prior intracollicular microinjections of glutamate NMDA receptor antagonists , MK-801 ( 15 or 30 mmol/0.5 microl ) and AP7 ( 10 or 20 nmol/0.5 microl ) , or of the NMDA receptor agonist N-methyl-d-aspartate ( NMDA , 20 or 30 nmol/0.5 microl ) .

Example answer:
{"entities": [{"text": "Haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glutamate NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "N-methyl-d-aspartate", "type": "ChemicalEntity"}, {"text": "NMDA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Changes evoked by a single intraperitoneal injection of rilmenidine ( 600 microg/kg ) or alpha-methyldopa ( 100 mg/kg ) , selective I1- and alpha2-receptor agonists , respectively , in blood pressure , hemodynamic variability , and locomotor activity were assessed in radiotelemetered sham-operated and ovariectomized ( Ovx ) Sprague-Dawley female rats with or without 12-wk estrogen replacement .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "I1- and alpha2-receptor", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "estrogen", "type": "ChemicalEntity"}]}

Example input:
Sentence: Compound 1 is a potent A ( 2A ) /A ( 1 ) receptor antagonist in vitro ( A ( 2A ) K ( i ) = 4.1 nM ; A ( 1 ) K ( i ) = 17.0 nM ) that has excellent activity , after oral administration , across a number of animal models of Parkinson 's disease including mouse and rat models of haloperidol-induced catalepsy , mouse model of reserpine-induced akinesia , rat 6-hydroxydopamine ( 6-OHDA ) lesion model of drug-induced rotation , and MPTP-treated non-human primate model .

Example answer:
{"entities": [{"text": "A ( 2A ) /A ( 1 ) receptor antagonist", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "reserpine-induced", "type": "ChemicalEntity"}, {"text": "akinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "6-hydroxydopamine", "type": "ChemicalEntity"}, {"text": "6-OHDA", "type": "ChemicalEntity"}, {"text": "MPTP-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Several studies have reported that , compared with wild-type individuals , CYP2C19 variant allele carriers exhibit a significantly lower capacity to metabolize clopidogrel into its active metabolite and inhibit platelet activation , and are therefore at significantly higher risk of adverse cardiovascular events .

Example answer:
{"entities": [{"text": "CYP2C19", "type": "GeneOrGeneProduct"}, {"text": "clopidogrel", "type": "ChemicalEntity"}]}

Example input:
Sentence: Low activity of patient plasma butyrylcholinesterase with butyrylthiocholine ( BTC ) and benzoylcholine , and values of dibucaine and fluoride numbers fit with heterozygous atypical silent genotype .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "butyrylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "butyrylthiocholine", "type": "ChemicalEntity"}, {"text": "BTC", "type": "ChemicalEntity"}, {"text": "benzoylcholine", "type": "ChemicalEntity"}, {"text": "dibucaine", "type": "ChemicalEntity"}, {"text": "fluoride", "type": "ChemicalEntity"}]}

Example input:
Sentence: Metfromin markedly lowered isoproterenol-induced elevation in the levels of TLR4 mRNA , myeloid differentiation protein 88 ( MyD88 ) , tumor necrosis factor-alpha ( TNF-a ) , and interleukin 6 ( IL-6 ) in the heart tissues .

Example answer:
{"entities": [{"text": "Metfromin", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "myeloid differentiation protein 88", "type": "GeneOrGeneProduct"}, {"text": "MyD88", "type": "GeneOrGeneProduct"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}, {"text": "interleukin 6", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Debrisoquine phenotype and the pharmacokinetics and beta-2 receptor pharmacodynamics of metoprolol and its enantiomers .

## Item biored:test:6
Example input:
Sentence: In a double-blind 6-week trial , 458 patients with acute schizophrenia were randomly assigned to fixed-dose treatment with asenapine at 5 mg twice daily ( BID ) , asenapine at 10 mg BID , placebo , or haloperidol at 4 mg BID ( to verify assay sensitivity ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Extrapyramidal symptoms reported as AEs occurred in 15 % and 18 % , 34 % , and 10 % of the asenapine at 5 and 10 mg BID , haloperidol , and placebo groups , respectively .

Example answer:
{"entities": [{"text": "Extrapyramidal symptoms", "type": "DiseaseOrPhenotypicFeature"}, {"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: On the Positive and Negative Syndrome Scale positive subscale , all treatments were superior to placebo with LOCF and MMRM ; asenapine at 5 mg BID was superior to placebo on the negative subscale with MMRM and on the general psychopathology subscale with LOCF and MMRM .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Treatment-related adverse events ( AEs ) occurred in 44 % and 52 % , 57 % , and 41 % of the asenapine at 5 and 10 mg BID , haloperidol , and placebo groups , respectively .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: The patient was taking 80 mg simvastatin at bedtime ( initiated 27 days earlier ) ; amiodarone at a dose of 400 mg daily for 7 days , then 200 mg daily ( initiated 19 days earlier ) ; and 400 mg atazanavir daily ( initiated at least 2 years previously ) .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "atazanavir", "type": "ChemicalEntity"}]}

Example input:
Sentence: Severe cardiovascular complications occurred in eight of 160 patients treated with terbutaline for preterm labor .

Example answer:
{"entities": [{"text": "cardiovascular complications", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "terbutaline", "type": "ChemicalEntity"}, {"text": "preterm labor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The mean reduction in MSSBP/MSDBP with VAL/HCTZ 320/25 mg was 24.7/16.6 mm Hg , compared with 5.9/7.0 mm Hg with placebo .

Example answer:
{"entities": [{"text": "VAL/HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: One week later , they received repeatedly vehicles ( saline , DMSO , saline+DMSO ) , scopolamine ( 2 microg/0.5 microl saline/side ; 30 min before training ) , ritanserin ( 2 , 4 and 8 microg/0.5 microl DMSO/side ; 20 min before training ) and scopolamine ( 2 microg/0.5 microl ; 30 min before ritanserin injection ) +ritanserin ( 4 microg/0.5 microl DMSO ) through cannulae each day .

Example answer:
{"entities": [{"text": "DMSO", "type": "ChemicalEntity"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "DMSO/side", "type": "ChemicalEntity"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Input:
Sentence: Six EMs received 0.5 mg of terbutaline s.c. on two different occasions : 1 ) 1 hr after administration of a placebo and 2 ) 1 hr after 150 mg of metoprolol p.o .

## Item biored:test:71
Example input:
Sentence: RESULTS : Direct sequencing of the encoding regions of the candidate genes revealed a heterozygous mutation c.592C -- > T in exon 2 of the gap junction protein , alpha 8 ( GJA8 ) gene .

Example answer:
{"entities": [{"text": "c.592C -- > T", "type": "SequenceVariant"}, {"text": "gap junction protein , alpha 8", "type": "GeneOrGeneProduct"}, {"text": "GJA8", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Thus , the same deletion patterns covered the entire p14 gene for all cases except for one case , which suggested the hemizygous deletion of exons 1beta and 2 and homozygous deletion of exon 3 .

Example answer:
{"entities": [{"text": "p14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Subsequent mutation analysis of PQBP1 , located within the delineated linkage interval in Xp11.23 , revealed a 2-bp deletion , c.461_462delAG , that cosegregated with the disease .

Example answer:
{"entities": [{"text": "PQBP1", "type": "GeneOrGeneProduct"}, {"text": "c.461_462delAG", "type": "SequenceVariant"}]}

Example input:
Sentence: A deletion of 84,682 base pairs covering the CFHR1 and CFHR3 genes was detected by direct polymerase chain reaction and gel electrophoresis .

Example answer:
{"entities": [{"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: V311fs is an 8-bp nucleotide ( TTAAATGG ) deletion in exon 5 .

Example answer:
{"entities": [{"text": "V311fs", "type": "SequenceVariant"}, {"text": "8-bp nucleotide ( TTAAATGG ) deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: We found a single nucleotide deletion c.342delA , located in exon 3 , which resulted in a frameshift at amino acid position 58 ( p.Arg58fs or p.R58fs ) .

Example answer:
{"entities": [{"text": "c.342delA", "type": "SequenceVariant"}, {"text": "p.Arg58fs", "type": "SequenceVariant"}, {"text": "p.R58fs", "type": "SequenceVariant"}]}

Input:
Sentence: Direct sequencing of CRYBA3/A1 , which maps to the vicinity , revealed an in-frame 3-bp deletion in exon 4 ( 279delGAG ) .

## Item biored:test:4
Example input:
Sentence: CONCLUSIONS : This is the first study to link risperidone-induced hyperprolactinemia and SSRI treatment to lower BMD in children and adolescents .

Example answer:
{"entities": [{"text": "risperidone-induced", "type": "ChemicalEntity"}, {"text": "hyperprolactinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SSRI", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : In this study population , combination therapies with VAL/HCTZ were associated with significantly greater BP reductions compared with either monotherapy , were well tolerated , and were associated with less hypokalemia than HCTZ alone .

Example answer:
{"entities": [{"text": "VAL/HCTZ", "type": "ChemicalEntity"}, {"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: Metfromin markedly lowered isoproterenol-induced elevation in the levels of TLR4 mRNA , myeloid differentiation protein 88 ( MyD88 ) , tumor necrosis factor-alpha ( TNF-a ) , and interleukin 6 ( IL-6 ) in the heart tissues .

Example answer:
{"entities": [{"text": "Metfromin", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "myeloid differentiation protein 88", "type": "GeneOrGeneProduct"}, {"text": "MyD88", "type": "GeneOrGeneProduct"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}, {"text": "interleukin 6", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: While contractions to carbachol and ATP were the same in inflamed and in control strips when related to a reference potassium response , isoprenaline-induced relaxations were smaller in inflamed strips .

Example answer:
{"entities": [{"text": "carbachol", "type": "ChemicalEntity"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "potassium", "type": "ChemicalEntity"}, {"text": "isoprenaline-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: Haloperidol-induced catalepsy was challenged with prior intracollicular microinjections of glutamate NMDA receptor antagonists , MK-801 ( 15 or 30 mmol/0.5 microl ) and AP7 ( 10 or 20 nmol/0.5 microl ) , or of the NMDA receptor agonist N-methyl-d-aspartate ( NMDA , 20 or 30 nmol/0.5 microl ) .

Example answer:
{"entities": [{"text": "Haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glutamate NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "N-methyl-d-aspartate", "type": "ChemicalEntity"}, {"text": "NMDA", "type": "ChemicalEntity"}]}

Example input:
Sentence: The results showed that intracollicular microinjection of MK-801 and AP7 previous to systemic injections of haloperidol significantly attenuated the catalepsy , as indicated by a reduced latency to step down from a horizontal bar .

Example answer:
{"entities": [{"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study sought to characterize the cognitive-enhancing effects of the 5-HT ( 6 ) antagonist Ro4368554 ( 3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole ) in a rat object recognition task employing a cholinergic ( scopolamine pretreatment ) and a serotonergic- ( tryptophan ( TRP ) depletion ) deficient model , and compared its pattern of action with that of the acetylcholinesterase inhibitor metrifonate .

Example answer:
{"entities": [{"text": "5-HT ( 6 )", "type": "GeneOrGeneProduct"}, {"text": "Ro4368554", "type": "ChemicalEntity"}, {"text": "3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "cholinergic", "type": "ChemicalEntity"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "serotonergic-", "type": "ChemicalEntity"}, {"text": "tryptophan", "type": "ChemicalEntity"}, {"text": "TRP", "type": "ChemicalEntity"}, {"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "metrifonate", "type": "ChemicalEntity"}]}

Example input:
Sentence: The incidence of hypokalemia was lower with VAL/HCTZ combinations ( 1.8 % -6.1 % ) than with HCTZ monotherapies ( 7.1 % -13.3 % ) .

Example answer:
{"entities": [{"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VAL/HCTZ", "type": "ChemicalEntity"}, {"text": "HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: Finally , the IKr blockers , Terfenadine and Citalopram , which are reported to cause Torsade de Pointes ( TdP ) in clinical practice , produced early afterdepolarization ( EAD ) .

Example answer:
{"entities": [{"text": "Terfenadine", "type": "ChemicalEntity"}, {"text": "Citalopram", "type": "ChemicalEntity"}, {"text": "Torsade de Pointes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TdP", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The drug effect studied was the antagonism by metoprolol of terbutaline-induced hypokalemia .

## Item biored:test:32
Example input:
Sentence: We have previously reported that CCK-8 significantly alleviated morphine-induced amnesia and reversed spine density decreases in the CA1 region of the hippocampus in morphine-treated animals .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "morphine-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: In conclusion , although Ro4368554 did not improve a time-related retention deficit , it reversed a cholinergic and a serotonergic memory deficit , suggesting that both mechanisms may be involved in the facilitation of object memory by Ro4368554 and , possibly , other 5-HT ( 6 ) receptor antagonists .

Example answer:
{"entities": [{"text": "memory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5-HT ( 6 ) receptor", "type": "ChemicalEntity"}]}

Example input:
Sentence: Furthermore , DCE reversed the amnesia induced by scopolamine ( 0.4 mg/kg , i.p . )

Example answer:
{"entities": [{"text": "DCE", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "scopolamine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Diazepam- , scopolamine- and ageing-induced amnesia served as the interoceptive behavioral models .

Example answer:
{"entities": [{"text": "Diazepam-", "type": "ChemicalEntity"}, {"text": "scopolamine-", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : In a PA retention paradigm , the injection of NTG immediately after learning produced a significant impairment of long-term associative memory in mice , whereas delayed induced hypotension had no effect .

Example answer:
{"entities": [{"text": "NTG", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The effect of ritanserin ( 5-HT2 antagonist ) on scopolamine ( muscarinic cholinergic antagonist ) -induced amnesia in Morris water maze ( MWM ) was investigated .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "5-HT2", "type": "GeneOrGeneProduct"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "muscarinic cholinergic", "type": "GeneOrGeneProduct"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Initial testing in a time-dependent forgetting task employing a 24-h delay between training and testing showed that metrifonate improved object recognition ( at 10 and 30 mg/kg , p.o .

Example answer:
{"entities": [{"text": "metrifonate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Microinjection of ritanserin into the CA1 region of hippocampus improves scopolamine-induced amnesia in adult male rats .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Our findings show that microinjection of ritanserin into the CA1 region of the hippocampus improves the scopolamine-induced amnesia .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: However , administration of nefiracetam during training completely reversed the amnesia induced by apomorphine at the 10h post-training time and the converse was also true .

## Item biored:test:13
Example input:
Sentence: We used high-resolution karyotyping to confirm a deletion ( 10-12Mb ) [ del ( 1 ) ( p31.2p32.3 ) ] and found no structural abnormalities in the father , suggesting a de novo event .

Example answer:
{"entities": [{"text": "deletion ( 10-12Mb )", "type": "SequenceVariant"}, {"text": "del ( 1 ) ( p31.2p32.3 )", "type": "SequenceVariant"}]}

Example input:
Sentence: Molecular diagnosis of 46 , XY DSD and identification of a novel 8 nucleotide deletion in exon 1 of the SRD5A2 gene .

Example answer:
{"entities": [{"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "8 nucleotide deletion", "type": "SequenceVariant"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Deletion 22q11.2 syndrome is the most frequent known microdeletion syndrome and is associated with a highly variable phenotype , including DiGeorge and Shprintzen ( velocardiofacial ) syndromes .

Example answer:
{"entities": [{"text": "Deletion 22q11.2 syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DiGeorge and Shprintzen ( velocardiofacial ) syndromes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The phenotype co-segregates with short-tandem repeat markers flanking the TMC1 gene at the DFNA36 locus on chromosome 9q31-q21 .

Example answer:
{"entities": [{"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "DFNA36", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We conducted a screening of the MHC region for 1,536 single nucleotide polymorphisms ( SNPs ) and the deletion of the C4A gene in a SLE case-control study ( 380 cases , 765 age-matched controls ) nested within the prospective Black Women 's Health Study .

Example answer:
{"entities": [{"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "C4A", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Molecular characterization by DNA sequencing analysis and multiplex ligation-dependent probe amplification of the MLYCD gene revealed a heterozygous mutation ( c.920T > G , p.Leu307Arg ) in the patient and his father and a heterozygous deletion comprising exon 1 in the patient and his mother .

Example answer:
{"entities": [{"text": "MLYCD", "type": "GeneOrGeneProduct"}, {"text": "c.920T > G", "type": "SequenceVariant"}, {"text": "p.Leu307Arg", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: In the original MB-DRM German family , we demonstrated a linkage of the disease to the SEPN1 locus ( 1p36 ) , and subsequently a homozygous SEPN1 deletion ( del 92 nucleotide -19/+73 ) in the affected patients .

Example answer:
{"entities": [{"text": "SEPN1", "type": "GeneOrGeneProduct"}, {"text": "del 92 nucleotide -19/+73", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Myotonic dystrophy ( DM ) , the most prevalent muscular disorder in adults , is caused by ( CTG ) n-repeat expansion in a gene encoding a protein kinase ( DM protein kinase ; DMPK ) and involves changes in cytoarchitecture and ion homeostasis .

Example answer:
{"entities": [{"text": "Myotonic dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "muscular disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM protein kinase", "type": "GeneOrGeneProduct"}, {"text": "DMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Through MLPA analysis , a large deletion including the whole PAX6 gene and DKFZ p686k1684 gene was detected in one sporadic patient from the AN group .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}, {"text": "DKFZ p686k1684", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Molecular and phenotypic analysis of patients with deletions within the deletion-rich region of the Duchenne muscular dystrophy ( DMD ) gene .

## Item biored:test:80
Example input:
Sentence: In a hospital-based study of non-Hispanic whites , we genotyped CASP8 -652 6N del and 302H variants in 1,023 patients with squamous cell carcinoma of the head and neck ( SCCHN ) and 1,052 cancer-free controls .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "302H", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conclude that GSTP1 Ile/Val polymorphism is involved in the risk of prostate cancer development in our population .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile/Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The study group consisted of 66 Polish families with cancer who have at least three related females affected with breast or ovarian cancer and who had cancer diagnosed , in at least one of the three affected females , at age < 50 years .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast or ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The estimated relative risk was significantly high for individuals with w1/m1 genotype at 3'UTR of CYP1A1 gene ( OR-4.64 ; 95 % CI = 1.51-14.86 ; P < 0.01 ) whereas the CYP1A1 Ile/Val genotype ( w2/m2 ) on exon 7 was found to be associated with a decreased risk for prostate cancer ( OR-0.17 ; 95 % CI = 0.02-0.89 ; P=0.03 ) .

Example answer:
{"entities": [{"text": "CYP1A1", "type": "GeneOrGeneProduct"}, {"text": "Ile/Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: VNTR and ins/del 6 bp genotypes varied with tumour anatomical site : 2R/2R genotype was rare in left-sided tumours ( 7.0 % vs. 26.3 % of right-sided and 24.1 % of rectal cancers ; P < 0.01 ) , where the variant allele 6- was very frequent ( 69.0 % ) .

Example answer:
{"entities": [{"text": "ins/del 6 bp", "type": "SequenceVariant"}, {"text": "tumour", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumours", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rectal cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Study-specific associations of 68 single nucleotide polymorphisms ( SNPs ) in 8 alcohol-metabolising genes ( Alcohol Dehydrogenases ( ADHs ) and Aldehyde Dehydrogenases ( ALDHs ) ) with prostate cancer diagnosis and prostate cancer-specific mortality , by grade , were assessed using logistic and Cox regression models , respectively .

Example answer:
{"entities": [{"text": "alcohol-metabolising", "type": "ChemicalEntity"}, {"text": "Alcohol Dehydrogenases", "type": "GeneOrGeneProduct"}, {"text": "ADHs", "type": "GeneOrGeneProduct"}, {"text": "Aldehyde Dehydrogenases", "type": "GeneOrGeneProduct"}, {"text": "ALDHs", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "prostate", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To investigate the GSTP1 Ile105Val genotype frequency in prostate cancer cases in the Kashmiri population , we designed a case-control study , in which 50 prostate cancer cases and 45 benign prostate hyperplasia cases were studied for GSTP1 Ile105Val polymorphism , compared to 80 controls taken from the general population , employing the PCR-RFLP technique .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile105Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We found the frequency of the three different genotypes of GSTP1 Ile105Val in our ethnic Kashmir population , i.e. , Ile/Ile , Ile/Val and Val/Val , to be 52.4 , 33.3 and 14.3 % among prostate cancer cases , 48.5 , 37.5 and 14 % among benign prostate hyperplasia cases and 73.8 , 21.3 and 5 % in the control population , respectively .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile105Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We analyzed a large population-based case-control study , cancer prostate in Sweden ( CAPS ) consisting of 1,378 cases and 782 controls .

Example answer:
{"entities": [{"text": "cancer prostate", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Through linkage with the Swedish Cancer Register , all subjects in this cohort diagnosed with bladder cancer were identified .

## Item biored:test:62
Example input:
Sentence: One patient with a severe cellular and clinical phenotype was a compound heterozygote with POLG1 mutations in the polymerase and exonuclease domain intrans .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Novel CACNA1S mutation causes autosomal dominant hypokalemic periodic paralysis in a South American family .

Example answer:
{"entities": [{"text": "CACNA1S", "type": "GeneOrGeneProduct"}, {"text": "hypokalemic periodic paralysis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Anticipation in familial lattice corneal dystrophy type I with R124C mutation in the TGFBI ( BIGH3 ) gene .

Example answer:
{"entities": [{"text": "lattice corneal dystrophy type I", "type": "DiseaseOrPhenotypicFeature"}, {"text": "R124C", "type": "SequenceVariant"}, {"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "BIGH3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We investigated clinical and cellular phenotypes of 24 children with mutations in the catalytic ( alpha ) subunit of the mitochondrial DNA ( mtDNA ) gamma polymerase ( POLG1 ) .

Example answer:
{"entities": [{"text": "mitochondrial DNA ( mtDNA ) gamma polymerase", "type": "GeneOrGeneProduct"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We studied the PAX6 gene mutations in a cohort of affected individuals with different clinical phenotype including AN , coloboma of iris and choroid , or anterior segment malformations .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coloboma of iris and choroid", "type": "DiseaseOrPhenotypicFeature"}, {"text": "anterior segment malformations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : To identify the underlying genetic defect in a four-generation family of Chinese origin with autosomal dominant congenital cataract-microcornea syndrome ( CCMC ) .

Example answer:
{"entities": [{"text": "genetic defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CCMC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The result expands the mutation spectrum of GJA8 in associated with congenital cataract and microcornea , and implies that this gene has direct involvement with the development of the lens as well as the other anterior segment of the eye .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcornea", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A G1103R mutation in CRB1 is co-inherited with high hyperopia and Leber congenital amaurosis .

Example answer:
{"entities": [{"text": "G1103R", "type": "SequenceVariant"}, {"text": "CRB1", "type": "GeneOrGeneProduct"}, {"text": "hyperopia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Leber congenital amaurosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel mutation in GJA8 causing congenital cataract-microcornea syndrome in a Chinese pedigree .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CRYBA3/A1 gene mutation associated with suture-sparing autosomal dominant congenital nuclear cataract : a novel phenotype .

## Item biored:test:38
Example input:
Sentence: Alterations of norepinephrine transporter ( NET ) function by chronic inhibition of NET in relation to sensitization to seizures induce by cocaine and local anesthetics were studied in mice .

Example answer:
{"entities": [{"text": "norepinephrine transporter", "type": "GeneOrGeneProduct"}, {"text": "NET", "type": "GeneOrGeneProduct"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cocaine", "type": "ChemicalEntity"}, {"text": "anesthetics", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: DESIGN : Dose response curves for nonsedating doses of morphine and CNSB002 given intraperitoneally alone and together in combinations were constructed for antihyperalgesic effect using paw withdrawal from noxious heat in two rat pain models : carrageenan-induced paw inflammation and streptozotocin ( STZ ) -induced diabetic neuropathy .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "carrageenan-induced", "type": "ChemicalEntity"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "streptozotocin", "type": "ChemicalEntity"}, {"text": "STZ", "type": "ChemicalEntity"}, {"text": "diabetic neuropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Daily administration of desipramine , an inhibitor of the NET , for 5 days decreased [ ( 3 ) H ] norepinephrine uptake in the P2 fractions of hippocampus but not cortex , striatum or amygdalae .

Example answer:
{"entities": [{"text": "desipramine", "type": "ChemicalEntity"}, {"text": "NET", "type": "GeneOrGeneProduct"}, {"text": "[ ( 3 ) H ] norepinephrine", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : In this study , we evaluated the performance of dopamine beta-hydroxylase knockout ( Dbh -/- ) mice , which lack norepinephrine ( NE ) , in the elevated plus maze ( EPM ) to examine the contribution of noradrenergic signaling to cocaine-induced anxiety .

Example answer:
{"entities": [{"text": "dopamine beta-hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "norepinephrine", "type": "ChemicalEntity"}, {"text": "NE", "type": "ChemicalEntity"}, {"text": "cocaine-induced", "type": "ChemicalEntity"}, {"text": "anxiety", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Haloperidol-induced catalepsy was challenged with prior intracollicular microinjections of glutamate NMDA receptor antagonists , MK-801 ( 15 or 30 mmol/0.5 microl ) and AP7 ( 10 or 20 nmol/0.5 microl ) , or of the NMDA receptor agonist N-methyl-d-aspartate ( NMDA , 20 or 30 nmol/0.5 microl ) .

Example answer:
{"entities": [{"text": "Haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glutamate NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "N-methyl-d-aspartate", "type": "ChemicalEntity"}, {"text": "NMDA", "type": "ChemicalEntity"}]}

Example input:
Sentence: We suggest that trazodone ( 5 , 10 and 20 mg/kg ) , by blocking the 5-HT 2C receptors , releases the nigrostriatal DAergic neurons from tonic inhibition caused by 5-HT , and thereby potentiates dexamphetamine stereotypy and antagonizes haloperidol catalepsy .

Example answer:
{"entities": [{"text": "5-HT 2C", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These include augmented endothelin-1 ( ET-1 ) release , increased sympathetic nervous system activity , and elevated tissue oxidative stress .

Example answer:
{"entities": [{"text": "endothelin-1", "type": "GeneOrGeneProduct"}, {"text": "ET-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These findings suggest that glutamate-mediated mechanisms in the neural circuits at the IC level influence haloperidol-induced catalepsy and participate in the regulation of motor activity .

Example answer:
{"entities": [{"text": "glutamate-mediated", "type": "ChemicalEntity"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study examined the influence of excitatory amino acid-mediated mechanisms in the IC on the catalepsy induced by the dopamine receptor blocker haloperidol administered systemically ( 1 or 0.5 mg/kg ) in rats .

Example answer:
{"entities": [{"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dopamine receptor", "type": "GeneOrGeneProduct"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Glutamatergic neurotransmission mediated by NMDA receptors in the inferior colliculus can modulate haloperidol-induced catalepsy .

Example answer:
{"entities": [{"text": "NMDA receptors", "type": "GeneOrGeneProduct"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Both plasma pethidine and norpethidine were elevated in the range associated with clinical manifestations of central nervous system excitation .

## Item biored:test:31
Example input:
Sentence: The administration of phenobarbitone and carbamazepine for 21days caused a significant impairment of learning and memory as well as an increased oxidative stress .

Example answer:
{"entities": [{"text": "phenobarbitone", "type": "ChemicalEntity"}, {"text": "carbamazepine", "type": "ChemicalEntity"}, {"text": "impairment of learning and memory", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A number of small scale clinical trials have unequivocally shown that intermittent subcutaneous apomorphine injections produce antiparkinsonian benefit close if not identical to that seen with levodopa and that apomorphine rescue injections can reliably revert off-periods even in patients with complex on-off motor swings .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}, {"text": "levodopa", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: However , scopolamine and ritanserin co-administration resulted in a significant decrease in escape latencies and traveled distances as compared to the scopolamine-treated rats .

Example answer:
{"entities": [{"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Nimodipine prevents memory impairment caused by nitroglycerin-induced hypotension in adult mice .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "ChemicalEntity"}, {"text": "memory impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nitroglycerin-induced", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Initial testing in a time-dependent forgetting task employing a 24-h delay between training and testing showed that metrifonate improved object recognition ( at 10 and 30 mg/kg , p.o .

Example answer:
{"entities": [{"text": "metrifonate", "type": "ChemicalEntity"}]}

Example input:
Sentence: The effect of ritanserin ( 5-HT2 antagonist ) on scopolamine ( muscarinic cholinergic antagonist ) -induced amnesia in Morris water maze ( MWM ) was investigated .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "5-HT2", "type": "GeneOrGeneProduct"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "muscarinic cholinergic", "type": "GeneOrGeneProduct"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our findings show that microinjection of ritanserin into the CA1 region of the hippocampus improves the scopolamine-induced amnesia .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Continuous subcutaneous apomorphine infusions can reduce daily off-time by more than 50 % in this group of patients , which appears to be a stronger effect than that generally seen with add-on therapy with oral dopamine agonists or COMT inhibitors .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "dopamine agonists", "type": "ChemicalEntity"}, {"text": "COMT inhibitors", "type": "ChemicalEntity"}]}

Example input:
Sentence: Microinjection of ritanserin into the CA1 region of hippocampus improves scopolamine-induced amnesia in adult male rats .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Co-administration of nefiracetam and apomorphine during training or 10h thereafter produced no significant anti-amnesic effect .

## Item biored:test:58
Example input:
Sentence: Isoproterenol-treated rats showed significant increases in the levels of lactate dehydrogenase , aspartate transaminase , creatine kinase and malondialdehyde and significant decreases in the activities of superoxide dismutase , catalase and glutathione peroxidase in serum and heart .

Example answer:
{"entities": [{"text": "Isoproterenol-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "aspartate transaminase", "type": "GeneOrGeneProduct"}, {"text": "creatine kinase", "type": "GeneOrGeneProduct"}, {"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "catalase", "type": "GeneOrGeneProduct"}, {"text": "glutathione peroxidase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: To determine whether there was a temporal relationship between VPA-associated oxidative stress and hepatotoxicity , adult male Sprague-Dawley rats were treated ip with VPA ( 500 mg/kg ) or 0.9 % saline ( vehicle ) once daily for 2 , 4 , 7 , 10 , or 14 days .

Example answer:
{"entities": [{"text": "VPA-associated", "type": "ChemicalEntity"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "VPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: In conclusion , HFD-induced obese rats are highly sensitized to doxorubicin-induced cardiotoxicity by substantially downregulating cardiac mitochondrial ATP generation , increasing oxidative stress and downregulating the JAK/STAT3 pathway .

Example answer:
{"entities": [{"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "doxorubicin-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "JAK/STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In the current study , we investigated whether a physiological intervention by feeding 40 % high fat diet ( HFD ) , which induces obesity in male Sprague-Dawley rats ( 250-275 g ) , sensitizes to doxorubicin-induced cardiotoxicity .

Example answer:
{"entities": [{"text": "fat", "type": "ChemicalEntity"}, {"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "doxorubicin-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/ K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , mitochondrial respiratory dysfunction characterized by decreased respiratory control ratio and ADP/O was observed in isoproterenol-treated rats .

Example answer:
{"entities": [{"text": "mitochondrial respiratory dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ADP/O", "type": "ChemicalEntity"}, {"text": "isoproterenol-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Male SD rats ( n = 30 ) were treated with Ato ( 50 mg/kg per day in drinking water ) or tap water for 15 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Ato", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mechanistic studies revealed that OB rats are sensitized due to : ( 1 ) higher oxyradical stress leading to upregulation of uncoupling proteins 2 and 3 , ( 2 ) downregulation of cardiac peroxisome proliferators activated receptor-alpha , ( 3 ) decreased plasma adiponectin levels , ( 4 ) decreased cardiac fatty-acid oxidation ( 666.9+/-14.0 nmol/min/g heart in ND versus 400.2+/-11.8 nmol/min/g heart in OB ) , ( 5 ) decreased mitochondrial AMP-alpha2 protein kinase , and ( 6 ) 86 % drop in cardiac ATP levels accompanied by decreased ATP/ADP ratio after doxorubicin administration .

Example answer:
{"entities": [{"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "uncoupling proteins 2 and 3", "type": "GeneOrGeneProduct"}, {"text": "peroxisome proliferators activated receptor-alpha", "type": "GeneOrGeneProduct"}, {"text": "adiponectin", "type": "GeneOrGeneProduct"}, {"text": "fatty-acid", "type": "ChemicalEntity"}, {"text": "AMP-alpha2 protein kinase", "type": "GeneOrGeneProduct"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "ATP/ADP", "type": "ChemicalEntity"}, {"text": "doxorubicin", "type": "ChemicalEntity"}]}

Example input:
Sentence: A LD ( 10 ) dose ( 8 mg doxorubicin/kg , ip ) administered on day 43 of the HFD feeding regimen led to higher cardiotoxicity , cardiac dysfunction , lipid peroxidation , and 80 % mortality in the obese ( OB ) rats in the absence of any significant renal or hepatic toxicity .

Example answer:
{"entities": [{"text": "doxorubicin/kg", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "renal or hepatic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In conclusion , administration of isoproterenol to rats results in primary loss of dystrophin , the most sensitive among the structural proteins that form the DGC that connects the extracellular matrix and the cytoskeleton in cardiomyocyte .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "dystrophin", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The rats treated with DFP-atropine showed severe typical OP-induced toxicity signs .

## Item biored:test:51
Example input:
Sentence: Daily administration of desipramine increased the incidence of appearance of lidocaine-induced convulsions and decreased that of cocaine-induced convulsions .

Example answer:
{"entities": [{"text": "desipramine", "type": "ChemicalEntity"}, {"text": "lidocaine-induced", "type": "ChemicalEntity"}, {"text": "convulsions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cocaine-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: Here , we investigated the effects of CCK-8 on long-term potentiation ( LTP ) in the lateral perforant path ( LPP ) -granule cell synapse of rat dentate gyrus ( DG ) in acute saline or morphine-treated rats .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "morphine-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Pilocarpine on either day induced status epilepticus ; status epilepticus at P45 resulted in CA3 cell loss and spontaneous seizures , whereas P20 rats had no cell loss or spontaneous seizures .

Example answer:
{"entities": [{"text": "Pilocarpine", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CA3", "type": "CellLine"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: These findings suggest that glutamate-mediated mechanisms in the neural circuits at the IC level influence haloperidol-induced catalepsy and participate in the regulation of motor activity .

Example answer:
{"entities": [{"text": "glutamate-mediated", "type": "ChemicalEntity"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A TSPO ligand attenuates brain injury after intracerebral hemorrhage .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "brain injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A TSPO ligand attenuates brain injury after intracerebral hemorrhage .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "brain injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The results indicate that GFC can exert anticonvulsant activity and reduce the frequency of installation of pilocarpine-induced status epilepticus , as demonstrated by increase in latency to first seizure and decrease in mortality rate of animals .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cholecystokinin-octapeptide restored morphine-induced hippocampal long-term potentiation impairment in rats .

Example answer:
{"entities": [{"text": "Cholecystokinin-octapeptide", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "MPTP", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "METH-induced", "type": "ChemicalEntity"}]}

Input:
Sentence: Organophosphate-induced convulsions and prevention of neuropathological damages .

## Item biored:test:97
Example input:
Sentence: A major disease-causing gene for HypoPP has been identified as CACNA1S , which encodes the skeletal muscle calcium channel alpha-subunit with four transmembrane domains ( I-IV ) , each with six transmembrane segments ( S1-S6 ) .

Example answer:
{"entities": [{"text": "HypoPP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CACNA1S", "type": "GeneOrGeneProduct"}, {"text": "skeletal muscle calcium channel alpha-subunit", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: More than 20 DNA mutations with different inheritance pattern have been described in patients with Bernard-Soulier Syndrome ( BSS ) , leading to abnormal or absent synthesis and/or expression of GPIbalpha .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "Bernard-Soulier Syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BSS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GPIbalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Gene polymorphism resulting in the substitution of glutamine with lysine at residue 223 in the carbohydrate recognition domain of SP-A2 increases susceptibility to meningococcal disease , as well as the risk of death .

Example answer:
{"entities": [{"text": "glutamine with lysine at residue 223", "type": "SequenceVariant"}, {"text": "carbohydrate", "type": "ChemicalEntity"}, {"text": "SP-A2", "type": "GeneOrGeneProduct"}, {"text": "meningococcal disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "death", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations of TP53 and dysfunction of the Brca1 and/or Brca2 tumor-suppressor proteins have been implicated in the molecular pathogenesis of a large fraction of OSCs , but frequent somatic mutations in other well-established tumor-suppressor genes have not been identified .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "Brca1", "type": "GeneOrGeneProduct"}, {"text": "Brca2", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: With the advent of next-generation sequencing technologies , the homozygous mutations T71N and A190T in the neuronal calcium sensor ( NCS ) hippocalcin were identified as the genetic cause of primary isolated dystonia ( DYT2 dystonia ) .

Example answer:
{"entities": [{"text": "T71N", "type": "SequenceVariant"}, {"text": "A190T", "type": "SequenceVariant"}, {"text": "neuronal calcium sensor", "type": "GeneOrGeneProduct"}, {"text": "NCS", "type": "GeneOrGeneProduct"}, {"text": "hippocalcin", "type": "GeneOrGeneProduct"}, {"text": "primary isolated dystonia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DYT2", "type": "GeneOrGeneProduct"}, {"text": "dystonia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The non-synonymous SNP rs2230912 ( resulting in amino-acid polymorphism Q460R ) showed the strongest association and has been postulated to be pathogenically relevant .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "Q460R", "type": "SequenceVariant"}]}

Example input:
Sentence: Genetic variation of SP-A1 and SP-D was not associated with meningococcal disease .

Example answer:
{"entities": [{"text": "SP-A1", "type": "GeneOrGeneProduct"}, {"text": "SP-D", "type": "GeneOrGeneProduct"}, {"text": "meningococcal disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In the present investigation four SNPs in two transcription factors , Single minded 2 ( SIM2 ) and V-ets erythroblastosis virus E26 oncogene homolog2 ( ETS2 ) , located in the 21 { st } chromosome were genotyped to understand their role in DS .

Example answer:
{"entities": [{"text": "Single minded 2", "type": "GeneOrGeneProduct"}, {"text": "SIM2", "type": "GeneOrGeneProduct"}, {"text": "V-ets erythroblastosis virus E26 oncogene homolog2", "type": "GeneOrGeneProduct"}, {"text": "ETS2", "type": "GeneOrGeneProduct"}, {"text": "DS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Genome-wide association studies have identified genomic loci , whose single-nucleotide polymorphisms ( SNPs ) predispose to prostate cancer ( PCa ) .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Thus far , although two loci for DSAP have been identified , the genetic basis and pathogenesis of this disorder have not been elucidated yet .

## Item biored:test:114
Example input:
Sentence: The coding sequences and flanking intron/UTR sequences of PDE6C and KCNV2 were screened for mutations by means of DHPLC and direct DNA sequencing of PCR-amplified genomic DNA .

Example answer:
{"entities": [{"text": "PDE6C", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Genotyping was performed by kinetic polymerase chain-reaction or TaqMan assays .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Example input:
Sentence: METHODS : Genomic DNA was screened for GLDC , AMT , and GCSH gene mutations .

Example answer:
{"entities": [{"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "AMT", "type": "GeneOrGeneProduct"}, {"text": "GCSH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Sequencing of genomic DNA from the affected individual and both parents to search for pathogenic mutations in PORCN gene .

Example answer:
{"entities": [{"text": "PORCN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DESIGN : Genomic DNA was analysed for mutations in the AIP gene , by PCR amplification and direct sequencing .

Example answer:
{"entities": [{"text": "AIP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: GENETIC ANALYSIS : Genomic DNA was extracted from peripheral blood leukocytes and mutation analysis of the entire coding sequence of the TSHR gene was performed in both children and their parents by direct DNA sequencing .

Example answer:
{"entities": [{"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS AND FINDINGS : Cord blood mononuclear cells ( CBMCs ) of 200 neonates were genotyped for two TBX21 and three HLX1 SNPs .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Direct sequencing was used for mutation analysis .

Example answer:
{"entities": []}

Example input:
Sentence: Mutation analysis enabled prenatal diagnosis of three unaffected and one affected pregnancies .

Example answer:
{"entities": []}

Input:
Sentence: METHODS : Mutational analysis and DNA sequencing were conducted in a newborn .

## Item biored:test:84
Example input:
Sentence: Coenzyme Q10 significantly reduced blood urea nitrogen and serum creatinine levels which were increased by cisplatin .

Example answer:
{"entities": [{"text": "Coenzyme Q10", "type": "ChemicalEntity"}, {"text": "blood urea nitrogen", "type": "ChemicalEntity"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "ChemicalEntity"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ascites", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoalbuminemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Curcumin also decreased bladder tumor growth in athymic nude mice bearing KU7 cells as xenografts and this was accompanied by decreased Sp1 , Sp3 , and Sp4 protein levels in tumors .

Example answer:
{"entities": [{"text": "Curcumin", "type": "ChemicalEntity"}, {"text": "bladder tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "KU7", "type": "CellLine"}, {"text": "Sp1", "type": "GeneOrGeneProduct"}, {"text": "Sp3", "type": "GeneOrGeneProduct"}, {"text": "Sp4", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CYP treatment significantly ( p < or = 0.001 ) increased expression of CXCL1 and IL-1beta in the urinary bladder of WT and VIP ( -/- ) mice , but expression in VIP ( -/- ) mice with CYP treatment was significantly ( p < or = 0.001 ) greater ( 4.2- to 13-fold increase ) than that observed in WT urinary bladder ( 3.6- to 5-fold increase ) .

Example answer:
{"entities": []}

Example input:
Sentence: It was concluded that coenzyme Q10 represents a potential therapeutic option to protect against acute cisplatin nephrotoxicity commonly encountered in clinical practice .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "nephrotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Odds ratios and 95 % confidence intervals for cancer risk by MLH1 -93 polymorphism status , and stratified by previous exposure to methylating chemotherapy , were calculated using unconditional logistic regression .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: VIP ( -/- ) mice exhibit altered bladder function and neurochemical properties in micturition pathways after cyclophosphamide ( CYP ) -induced cystitis .

Example answer:
{"entities": [{"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CYP", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Coenzyme Q10 treatment ameliorates acute cisplatin nephrotoxicity in mice .

Example answer:
{"entities": [{"text": "Coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "nephrotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : We found a significantly higher PSA/GG distribution in PC ( 30 % ) than either benign prostatic hyperplasia ( BPH ) ( 18 % ) or population controls ( 16 % ) ( P = 0.025 ) .

Example answer:
{"entities": [{"text": "PSA/GG", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostatic hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The hazard of developing CAD ( 95 % CI ) associated with initial treatment increased by 2.4-fold ( 1.3-4.3 , P=0.004 ) with glibenclamide ; 2-fold ( 0.9-4.6 , P=0.099 ) with glipizide ; 2.9-fold ( 1.6-5.1 , P=0.000 ) with either , and was unchanged with metformin .

Example answer:
{"entities": [{"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glibenclamide", "type": "ChemicalEntity"}, {"text": "glipizide", "type": "ChemicalEntity"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Input:
Sentence: The risk of bladder cancer doubled for every 10 g increment in cyclophosphamide ( OR = 2.0 , 95 % confidence interval ( CI ) 0.8 to 4.9 ) .

## Item biored:test:82
Example input:
Sentence: CONCLUSIONS : Using patient demographics , tumor characteristics , and CGP , we show that GIST lacking alterations in canonical genes occur in younger patients , frequently metastasize to lymph nodes , and most contain deleterious genomic alterations , including gene fusions involving FGFR1 and NTRK3 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GIST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "metastasize to lymph nodes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FGFR1", "type": "GeneOrGeneProduct"}, {"text": "NTRK3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: To investigate the GSTP1 Ile105Val genotype frequency in prostate cancer cases in the Kashmiri population , we designed a case-control study , in which 50 prostate cancer cases and 45 benign prostate hyperplasia cases were studied for GSTP1 Ile105Val polymorphism , compared to 80 controls taken from the general population , employing the PCR-RFLP technique .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile105Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: During the course of nephrotic syndrome , serum urea concentrations increased significantly faster in sgk1 ( -/- ) mice than in sgk1 ( +/+ ) mice leading to uremia and a reduced median survival in sgk1 ( -/- ) mice ( 29 vs. 40 days in sgk1 ( +/+ ) mice ) .

Example answer:
{"entities": [{"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "urea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "uremia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A Stratified analysis of the genotypes with age of onset and tumor grade showed the w1/m1 genotype to be significantly associated with an early age of onset ; however the tumor grades did not have significant association with the variant genotypes .

Example answer:
{"entities": [{"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : We found a significantly higher PSA/GG distribution in PC ( 30 % ) than either benign prostatic hyperplasia ( BPH ) ( 18 % ) or population controls ( 16 % ) ( P = 0.025 ) .

Example answer:
{"entities": [{"text": "PSA/GG", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostatic hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : We performed comprehensive genomic profiling ( CGP ) for coding regions in more than 300 cancer-related genes of 186 GISTs to assess for their somatic alterations .

Example answer:
{"entities": [{"text": "cancer-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GISTs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "ChemicalEntity"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ascites", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoalbuminemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The estimated relative risk was significantly high for individuals with w1/m1 genotype at 3'UTR of CYP1A1 gene ( OR-4.64 ; 95 % CI = 1.51-14.86 ; P < 0.01 ) whereas the CYP1A1 Ile/Val genotype ( w2/m2 ) on exon 7 was found to be associated with a decreased risk for prostate cancer ( OR-0.17 ; 95 % CI = 0.02-0.89 ; P=0.03 ) .

Example answer:
{"entities": [{"text": "CYP1A1", "type": "GeneOrGeneProduct"}, {"text": "Ile/Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Variation in IL10 , CRP , GSTP1 , IL1B , and NOS2 was associated with prostate cancer recurrence independent of pathologic prognostic factors .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "NOS2", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Subgroup analysis shows a higher incidence of the heterozygous ArgGly genotype in cancer cases than in the combined group of BPH and controls ( P < 0.05 ) ; this difference is statistically significant between cancer and BPH patients but not between cancer cases and community controls .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: In the cohort the cumulative risk of bladder cancer after Wegener 's granulomatosis , and the relative prevalence of a history of bladder cancer at the time of diagnosis of Wegener 's granulomatosis , were also estimated .

## Item biored:test:117
Example input:
Sentence: The same mutation was seen in heterozygosis in both parents .

Example answer:
{"entities": []}

Example input:
Sentence: The six unaffected family individuals carried alternative heterozygous mutations .

Example answer:
{"entities": []}

Example input:
Sentence: In Southern blot analysis , from the signal densities of the hybridized bands and their similarities to those of exons 2 and 3 in our previous quantitative study , we found that exon 1beta was homozygously deleted in four cases , hemizygously deleted in five cases and not deleted in one case .

Example answer:
{"entities": []}

Example input:
Sentence: Probands had at least one developmentally missing tooth , excluding third molars .

Example answer:
{"entities": []}

Example input:
Sentence: Using PCR-RFLP , we confirmed the heterozygous mutation in six affected family members and excluded it in three healthy members .

Example answer:
{"entities": []}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Her mother was heterozygous for the Asn45Ser mutation , and her father , for the nine-nucleotide deletion .

Example answer:
{"entities": [{"text": "Asn45Ser", "type": "SequenceVariant"}]}

Example input:
Sentence: The exon 4 sequence of TGFBI of the proband exhibits the heterozygous single-nucleotide mutation , C417T , leading to amino acid substitution ( R124C ) in the encoded TGF-induced protein .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "C417T", "type": "SequenceVariant"}, {"text": "R124C", "type": "SequenceVariant"}, {"text": "TGF-induced protein", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : The mother and daughter were each heterozygous for PPARG nonsense mutation Y355X , whose protein product in vitro was transcriptionally inactive with no dominant-negative activity against the wild-type receptor .

Example answer:
{"entities": [{"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "Y355X", "type": "SequenceVariant"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Input:
Sentence: The proband was heterozygous but the mutation was absent in the parents and the sister .

## Item biored:test:42
Example input:
Sentence: The CFHR1 and CFHR3 deletion was not polymorphic in the Chinese population and was not associated with wet AMD or drusen .

Example answer:
{"entities": [{"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "drusen", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SSCP followed by DNA sequencing of the kinase domain ( exons 18-21 ) of the EGFR gene revealed mutations in 2 ou of 69 ( 3 % ) glioblastomas in Japan and in 4 of 81 ( 5 % ) glioblastomas in Switzerland .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Exonic and intronic segments , 5 ' and 3 ' flanking regions of IRS2 ( 14.5 kb ) , were bidirectionally sequenced for single nucleotide polymorphism ( SNP ) discovery in 934 Hispanic children using 3730XL DNA Sequencers .

Example answer:
{"entities": [{"text": "IRS2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Single stranded conformational polymorphism ( SSCP ) analysis and sequencing revealed a novel heterozygous C139T transition in PAX9 in the affected members of the family .

Example answer:
{"entities": [{"text": "C139T", "type": "SequenceVariant"}, {"text": "PAX9", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: X-linked mental retardation has been traditionally divided into syndromic ( S-XLMR ) and non-syndromic forms ( NS-XLMR ) , although the borderlines between these phenotypes begin to vanish and mutations in a single gene , for example PQBP1 , can cause S-XLMR as well as NS-XLMR .

Example answer:
{"entities": [{"text": "X-linked mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PQBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The allele frequencies of polymorphisms at codon 787 CAG/CAA ( Gln/Gln ) in glioblastomas in Japan were G/G ( 82.4 % ) , G/A ( 10.8 % ) , A/A ( 6.8 % ) , corresponding to G 0.878 versus A 0.122 , significantly different from those in glioblastomas in Switzerland : G/G ( 27.2 % ) , G/A ( 28.4 % ) , A/A ( 44.4 % ) , corresponding to G 0.414 versus A 0.586 ( p < 0.0001 ) .

Example answer:
{"entities": [{"text": "codon 787 CAG/CAA", "type": "SequenceVariant"}, {"text": "Gln/Gln", "type": "SequenceVariant"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Based on recent papers describing the prognostic roles of the polymorphisms and the NFkappaB functions on cancer development , we sought to determine if Japanese gastric cancer patients were affected by the IL1B -31/-511 and FAS-670 polymorphisms .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "FAS-670", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: After restricting the candidate region in chromosome 16q22.1 by haplotype analysis , we found that all patients from 52 unrelated Japanese families harbor a heterozygous C -- > T single-nucleotide substitution , 16 nt upstream of the putative translation initiation site of the gene for a hypothetical protein DKFZP434I216 , which we have called `` puratrophin-1 '' ( Purkinje cell atrophy associated protein-1 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "C -- > T", "type": "SequenceVariant"}, {"text": "DKFZP434I216", "type": "GeneOrGeneProduct"}, {"text": "puratrophin-1", "type": "GeneOrGeneProduct"}, {"text": "Purkinje cell atrophy associated protein-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : The single nucleotide polymorphisms ( SNP ) at positions -1123 ( rs2488457 ) , +1858 ( rs2476601 , the R620W substitution ) , and +2740 ( rs1217412 ) were genotyped using TaqMan assays in 372 subjects with childhood-onset T1D , 130 subjects with JIA , and 400 control subjects of Czech origin , and in 160 subjects with T1D and 271 healthy controls of Azeri origin .

Example answer:
{"entities": [{"text": "rs2488457", "type": "SequenceVariant"}, {"text": "rs2476601", "type": "SequenceVariant"}, {"text": "R620W", "type": "SequenceVariant"}, {"text": "rs1217412", "type": "SequenceVariant"}, {"text": "T1D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "JIA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Polymerase chain reaction was carried out and single nucleotide polymorphisms of FGFR4 were identified by restriction enzyme digestion .

Example answer:
{"entities": [{"text": "FGFR4", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Single-strand conformation polymorphism analysis of the FMR1 gene in autistic and mentally retarded children in Japan .

## Item biored:test:79
Example input:
Sentence: METHODS : One hundred and fifty-eight patients with wet AMD , 80 patients with soft drusen , and 220 matched control subjects were recruited among Han Chinese in mainland China .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "drusen", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report the mutational spectrum in 68 Italian patients .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: PATIENTS : A population-based cohort consisting of 36 apparently sporadic paediatric pituitary adenoma patients , referred to two medical centres in Italy , was included in the study .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "pituitary adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We performed 2 sets of case-control comparisons using Japanese subjects ( first set : 830 patients with RA and 658 controls ; second set : 1112 patients with RA and 940 controls ) , and then performed a stratified analysis using human leukocyte antigen ( HLA ) -DRB1 shared epitope ( SE ) status .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "leukocyte antigen ( HLA ) -DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : A total of 1346 patients were randomized into the 8-week core study ( 734 men , 612 women ; 924 white , 291 black , 23 Asian , 108 other ; mean age , 52.7 years ; mean weight , 92.6 kg ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: The frequency of D90A-SOD1 is 50 times higher in Scandinavia ( 2.5 % ) than elsewhere , though ALS prevalence is not raised there .

Example answer:
{"entities": [{"text": "D90A-SOD1", "type": "SequenceVariant"}, {"text": "ALS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We hereafter used an independent sample of 541 Danish individuals from the oldest cohort and confirmed the initial findings ( hazard rate : 1.38 , P = 0.09 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Results : Forty seven patients ( 50 % ) had the genotype G1359G ( wild type group ) and 47 ( 50 % ) patients G1359A ( 41 patients , 43.6 % ) or A1359A ( 6 patients , 6.4 % ) ( mutant type group ) had the genotype .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "G1359G", "type": "SequenceVariant"}, {"text": "G1359A", "type": "SequenceVariant"}, {"text": "A1359A", "type": "SequenceVariant"}]}

Example input:
Sentence: METHODS : We genotyped 1498 German subjects for SNPs rs6232 and rs6235 within PCSK1 .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "rs6235", "type": "SequenceVariant"}, {"text": "PCSK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We analyzed a large population-based case-control study , cancer prostate in Sweden ( CAPS ) consisting of 1,378 cases and 782 controls .

Example answer:
{"entities": [{"text": "cancer prostate", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: METHODS : In the population based , nationwide Swedish Inpatient Register a cohort of 1065 patients with Wegener 's granulomatosis , 1969-95 , was identified .

## Item biored:test:35
Example input:
Sentence: This report describes a patient with mild language delay and mental retardation , who was found to have nonketotic hyperglycinemia following her presentation with acute encephalopathy and chorea shortly after initiation of valproate therapy .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "language delay", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nonketotic hyperglycinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chorea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "valproate", "type": "ChemicalEntity"}]}

Example input:
Sentence: As tranexamic acid is the only modifiable factor , its administration , particularly in doses exceeding 80 mg.kg ( -1 ) , should be weighed against the risk of postoperative seizures .

Example answer:
{"entities": [{"text": "tranexamic acid", "type": "ChemicalEntity"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The patient ( TJ ) presented with a generalized seizure associated with hypoglycemia and hypokalemia .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoglycemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : This is the first study to link risperidone-induced hyperprolactinemia and SSRI treatment to lower BMD in children and adolescents .

Example answer:
{"entities": [{"text": "risperidone-induced", "type": "ChemicalEntity"}, {"text": "hyperprolactinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SSRI", "type": "ChemicalEntity"}]}

Example input:
Sentence: Pilocarpine on either day induced status epilepticus ; status epilepticus at P45 resulted in CA3 cell loss and spontaneous seizures , whereas P20 rats had no cell loss or spontaneous seizures .

Example answer:
{"entities": [{"text": "Pilocarpine", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CA3", "type": "CellLine"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Haloperidol-induced catalepsy was challenged with prior intracollicular microinjections of glutamate NMDA receptor antagonists , MK-801 ( 15 or 30 mmol/0.5 microl ) and AP7 ( 10 or 20 nmol/0.5 microl ) , or of the NMDA receptor agonist N-methyl-d-aspartate ( NMDA , 20 or 30 nmol/0.5 microl ) .

Example answer:
{"entities": [{"text": "Haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glutamate NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "N-methyl-d-aspartate", "type": "ChemicalEntity"}, {"text": "NMDA", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Hyperprolactinemia was present in 49 % of 83 boys ( n = 41 ) treated with risperidone for a mean of 2.9 years .

Example answer:
{"entities": [{"text": "Hyperprolactinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: The association between tranexamic acid and convulsive seizures after cardiac surgery : a multivariate analysis in 11 529 patients .

Example answer:
{"entities": [{"text": "tranexamic acid", "type": "ChemicalEntity"}, {"text": "convulsive seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Glutamatergic neurotransmission mediated by NMDA receptors in the inferior colliculus can modulate haloperidol-induced catalepsy .

Example answer:
{"entities": [{"text": "NMDA receptors", "type": "GeneOrGeneProduct"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All 24 patients with seizures received high doses of TXA intraoperatively ranging from 61 to 259 mg/kg , had a mean age of 69.9 years , and 21 of 24 had undergone open chamber rather than coronary bypass procedures .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TXA", "type": "ChemicalEntity"}]}

Input:
Sentence: Pethidine-associated seizure in a healthy adolescent receiving pethidine for postoperative pain control .

## Item biored:test:8
Example input:
Sentence: Methadone prolongs the QT interval in vitro in a dose-dependent manner .

Example answer:
{"entities": [{"text": "Methadone", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Methadone dose was associated with longer QT interval of 0.140 ms/mg ( p = 0.002 ) .

Example answer:
{"entities": [{"text": "Methadone", "type": "ChemicalEntity"}, {"text": "longer QT interval", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Methadone dose , presence of cytochrome P-450 3A4 inhibitors , potassium level , and liver function contribute to QT prolongation .

Example answer:
{"entities": [{"text": "Methadone", "type": "ChemicalEntity"}, {"text": "cytochrome P-450 3A4 inhibitors", "type": "ChemicalEntity"}, {"text": "potassium", "type": "ChemicalEntity"}, {"text": "QT prolongation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All of the patients ' plasma blood urea nitrogen ( BUN ) and creatinine levels were measured on the second and seventh day after the administration of intravenous contrast material .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "blood urea nitrogen", "type": "ChemicalEntity"}, {"text": "BUN", "type": "ChemicalEntity"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "contrast", "type": "ChemicalEntity"}]}

Example input:
Sentence: and metrifonate ( 10 mg/kg , p.o. , respectively ) reversed memory deficits induced by scopolamine and TRP depletion ( 10 mg/kg , i.p. , and 3 mg/kg , p.o. , respectively ) .

Example answer:
{"entities": [{"text": "memory", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: At the end of study period , serum phenobarbitone and carbamazepine , whole brain malondialdehyde and reduced glutathione levels were estimated .

Example answer:
{"entities": [{"text": "phenobarbitone", "type": "ChemicalEntity"}, {"text": "carbamazepine", "type": "ChemicalEntity"}, {"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "glutathione", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male Wistar rats were randomly assigned to one of 5 groups ( n=6 ) : normal control and groups were injected isoproterenol after chronic pre-treatment with 0 , 25 , 50 , or 100mg/kg of metformin twice daily for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Changes evoked by a single intraperitoneal injection of rilmenidine ( 600 microg/kg ) or alpha-methyldopa ( 100 mg/kg ) , selective I1- and alpha2-receptor agonists , respectively , in blood pressure , hemodynamic variability , and locomotor activity were assessed in radiotelemetered sham-operated and ovariectomized ( Ovx ) Sprague-Dawley female rats with or without 12-wk estrogen replacement .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "I1- and alpha2-receptor", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "estrogen", "type": "ChemicalEntity"}]}

Example input:
Sentence: Isoproterenol ( 100mg/kg ) was injected subcutaneously on the 13th and 14th days to induce acute myocardial infarction .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}, {"text": "acute myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Blood samples for the analysis of plasma potassium , terbutaline , metoprolol ( racemic , R- and S-isomer ) , and alpha-hydroxymetoprolol concentrations were taken at regular time intervals , during 8 hr after metoprolol .

## Item biored:test:86
Example input:
Sentence: We found the frequency of the three different genotypes of GSTP1 Ile105Val in our ethnic Kashmir population , i.e. , Ile/Ile , Ile/Val and Val/Val , to be 52.4 , 33.3 and 14.3 % among prostate cancer cases , 48.5 , 37.5 and 14 % among benign prostate hyperplasia cases and 73.8 , 21.3 and 5 % in the control population , respectively .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile105Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To investigate the GSTP1 Ile105Val genotype frequency in prostate cancer cases in the Kashmiri population , we designed a case-control study , in which 50 prostate cancer cases and 45 benign prostate hyperplasia cases were studied for GSTP1 Ile105Val polymorphism , compared to 80 controls taken from the general population , employing the PCR-RFLP technique .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile105Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conclude that GSTP1 Ile/Val polymorphism is involved in the risk of prostate cancer development in our population .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile/Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Using patient demographics , tumor characteristics , and CGP , we show that GIST lacking alterations in canonical genes occur in younger patients , frequently metastasize to lymph nodes , and most contain deleterious genomic alterations , including gene fusions involving FGFR1 and NTRK3 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GIST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "metastasize to lymph nodes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FGFR1", "type": "GeneOrGeneProduct"}, {"text": "NTRK3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : We found a significantly higher PSA/GG distribution in PC ( 30 % ) than either benign prostatic hyperplasia ( BPH ) ( 18 % ) or population controls ( 16 % ) ( P = 0.025 ) .

Example answer:
{"entities": [{"text": "PSA/GG", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostatic hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Variation in IL10 , CRP , GSTP1 , IL1B , and NOS2 was associated with prostate cancer recurrence independent of pathologic prognostic factors .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "NOS2", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A common A/G transition -1,071 bp from the transcriptional start site was genotyped and showed no evidence of association with prostate cancer .

Example answer:
{"entities": [{"text": "A/G transition -1,071 bp", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Subgroup analysis shows a higher incidence of the heterozygous ArgGly genotype in cancer cases than in the combined group of BPH and controls ( P < 0.05 ) ; this difference is statistically significant between cancer and BPH patients but not between cancer cases and community controls .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The estimated relative risk was significantly high for individuals with w1/m1 genotype at 3'UTR of CYP1A1 gene ( OR-4.64 ; 95 % CI = 1.51-14.86 ; P < 0.01 ) whereas the CYP1A1 Ile/Val genotype ( w2/m2 ) on exon 7 was found to be associated with a decreased risk for prostate cancer ( OR-0.17 ; 95 % CI = 0.02-0.89 ; P=0.03 ) .

Example answer:
{"entities": [{"text": "CYP1A1", "type": "GeneOrGeneProduct"}, {"text": "Ile/Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "ChemicalEntity"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ascites", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoalbuminemia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The absolute risk for bladder cancer in the cohort reached 10 % 16 years after diagnosis of Wegener 's granulomatosis , and a history of bladder cancer was ( non-significantly ) twice as common as expected at the time of diagnosis of Wegener 's granulomatosis .

## Item biored:test:107
Example input:
Sentence: Conditional haplotype analysis revealed three other SNPs , rs204890 ( OR = 1.86 , p = 1.2 10 ( -4 ) ) , rs2071349 ( OR = 1.53 , p = 1.0 10 ( -3 ) ) , and rs2844580 ( OR = 1.43 , p = 1.3 10 ( -3 ) ) , to be associated with SLE independent of the rs9271366 SNP .

Example answer:
{"entities": [{"text": "rs204890", "type": "SequenceVariant"}, {"text": "rs2071349", "type": "SequenceVariant"}, {"text": "rs2844580", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}]}

Example input:
Sentence: Both polymorphisms were in strong linkage disequilibrium ( D ' = 0.71 , P < .001 ) , and the 3R/-6 base pair ( bp ) haplotype showed a significant overall survival benefit compared with the most prevalent haplotype 2R/+6bp ( HR = 0.42 ; 95 % CI , 0.20 to 0.85 ; P = .017 ) .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : In the Czechs , all three SNPs were in a tight linkage disequlibrium , while in the Azeri , the linkage disequlibrium was limited to between the promoter and 3'-UTR polymorphism , D ' ( -1123 , +2740 ) =0.99 , r ( 2 ) =0.72 .

Example answer:
{"entities": []}

Example input:
Sentence: Results : Forty seven patients ( 50 % ) had the genotype G1359G ( wild type group ) and 47 ( 50 % ) patients G1359A ( 41 patients , 43.6 % ) or A1359A ( 6 patients , 6.4 % ) ( mutant type group ) had the genotype .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "G1359G", "type": "SequenceVariant"}, {"text": "G1359A", "type": "SequenceVariant"}, {"text": "A1359A", "type": "SequenceVariant"}]}

Example input:
Sentence: No differences were observed in the PAI-1 4G/5G promoter genotypes frequencies ( p = 0.12 ) .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : The minor allele ( A ) in IL10 rs1800872 , known to produce less interleukin-10 ( IL-10 ) , was associated with a higher risk of recurrence ( OR = 1.76 , 95 % CI : 1.00-3.10 ) , and the minor allele ( G ) in rs1800896 , known to produce more IL-10 , was associated with a lower risk of recurrence ( OR = 0.66 , 95 % CI : 0.48-0.91 ) .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "rs1800872", "type": "SequenceVariant"}, {"text": "interleukin-10", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "rs1800896", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : In two different Caucasian populations , the Czechs and the Azeri , no independent contribution can be detected either of the -1123 promoter SNP or the +2740 3'-UTR SNP , and only the minor allele at PTPN22 codon 620 contributes to the risk of autoimmunity .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Though FAS-670 polymorphisms did not show any significant difference , the proportion of subjects with IL1B-31TT ( or IL1B-511CC ) increased according to stage ( trend P=0.019 ) .

Example answer:
{"entities": [{"text": "FAS-670", "type": "GeneOrGeneProduct"}, {"text": "IL1B-31TT", "type": "GeneOrGeneProduct"}, {"text": "IL1B-511CC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In particular , subjects with stage IV had a two times higher probability of having either IL1B-31TT ( or IL1B-511CC ) genotype compared with stage I subjects .

Example answer:
{"entities": [{"text": "IL1B-31TT", "type": "GeneOrGeneProduct"}, {"text": "IL1B-511CC", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: RESULTS : The proportion of IL12B promoter and 3'-UTR genotypes did not differ significantly between the different cohorts .

## Item biored:test:11
Example input:
Sentence: RESULTS : In a pooled analysis of 1460 ICH and 3817 IS/TIA , MB were more frequent in ICH vs IS/TIA in all treatment groups , but the excess increased from 2.8 ( odds ratio ; range , 2.3-3.5 ) in nonantithrombotic users to 5.7 ( range , 3.4-9.7 ) in antiplatelet users and 8.0 ( range , 3.5-17.8 ) in warfarin users ( P difference=0.01 ) .

Example answer:
{"entities": [{"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IS/TIA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The reduction in MSSBP was significantly greater with VAL/HCTZ 320/25 mg compared with VAL/HCTZ 160/12.5 mg ( P < 0.002 ) .

Example answer:
{"entities": [{"text": "VAL/HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: Serum levels of TPO and chemokines were lower , whereas M30 was significantly higher in cirrhotic patients than in HCs .

Example answer:
{"entities": [{"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Compared with those carrying at least one variant 326Ile allele , carriers with the Met326Met genotype had higher serum 17-hydroxyprogesterone ( 17-OHP ) { 1.1 [ 95 % confidence interval ( CI ) 1.1-1.3 ] ng/ml in those with the Met326Met genotype versus 0.8 ( 95 % CI 0.7-1.0 ) ng/ml in those with Ile326Ile and Met326Ile genotypes , P = 0.0073 } and free testosterone levels [ 1.2 ( 95 % CI 1.1-1.4 ) pg/ml for Met326Met genotype versus 0.9 ( 95 % CI 0.6-1.3 ) pg/ml for Ile326Ile and Met326Ile genotypes , P = 0.038 ] .

Example answer:
{"entities": [{"text": "326Ile", "type": "SequenceVariant"}, {"text": "Met326Met", "type": "SequenceVariant"}, {"text": "17-hydroxyprogesterone", "type": "ChemicalEntity"}, {"text": "17-OHP", "type": "ChemicalEntity"}, {"text": "Ile326Ile", "type": "SequenceVariant"}, {"text": "Met326Ile", "type": "SequenceVariant"}, {"text": "testosterone", "type": "ChemicalEntity"}]}

Example input:
Sentence: and metrifonate ( 10 mg/kg , p.o. , respectively ) reversed memory deficits induced by scopolamine and TRP depletion ( 10 mg/kg , i.p. , and 3 mg/kg , p.o. , respectively ) .

Example answer:
{"entities": [{"text": "memory", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: In blocking the positive inotropic and chronotropic responses to isoprenaline , ( + ) -propranolol had less than one hundredth the potency of ( - ) -propranolol .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: On the Positive and Negative Syndrome Scale positive subscale , all treatments were superior to placebo with LOCF and MMRM ; asenapine at 5 mg BID was superior to placebo on the negative subscale with MMRM and on the general psychopathology subscale with LOCF and MMRM .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}]}

Example input:
Sentence: hiPS-CMs were seeded onto MEA and FPD was measured for 2min every 10min for 30min after drug exposure for the vehicle and each drug concentration .

Example answer:
{"entities": []}

Example input:
Sentence: Metfromin markedly lowered isoproterenol-induced elevation in the levels of TLR4 mRNA , myeloid differentiation protein 88 ( MyD88 ) , tumor necrosis factor-alpha ( TNF-a ) , and interleukin 6 ( IL-6 ) in the heart tissues .

Example answer:
{"entities": [{"text": "Metfromin", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "myeloid differentiation protein 88", "type": "GeneOrGeneProduct"}, {"text": "MyD88", "type": "GeneOrGeneProduct"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}, {"text": "interleukin 6", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: There was a difference in metoprolol potency with higher racemic metoprolol IC50 values in PMs ( 72 +/- 7 ng.ml-1 ) than EMs ( 42 +/- 8 ng.ml-1 , P less than .001 ) .

## Item biored:test:81
Example input:
Sentence: RESULTS : We found a significantly higher PSA/GG distribution in PC ( 30 % ) than either benign prostatic hyperplasia ( BPH ) ( 18 % ) or population controls ( 16 % ) ( P = 0.025 ) .

Example answer:
{"entities": [{"text": "PSA/GG", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostatic hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Four variants in two genes exceeded the multiple testing threshold for associations with prostate cancer mortality in fixed-effect meta-analyses .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A meta-analysis of previous and our present study revealed that this polymorphism is positively associated with adenocarcinoma , although suggestive associations were also found for squamous- and small-cell lung cancers .

Example answer:
{"entities": [{"text": "adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "squamous- and small-cell lung cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the haplotype analysis , 1 haplotype carrying the variant allele from both +3100 T/G and +8365 C/T , with a population frequency of 3 % , was also significantly associated with decreased risk of prostate cancer ( p=0.036 , global simulated p-value=0.046 ) .

Example answer:
{"entities": [{"text": "+3100 T/G", "type": "SequenceVariant"}, {"text": "+8365 C/T", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Variation in IL10 , CRP , GSTP1 , IL1B , and NOS2 was associated with prostate cancer recurrence independent of pathologic prognostic factors .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "NOS2", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study supports the hypothesis that inflammation is involved in prostate carcinogenesis and that sequence variation within the COX-2 gene influence the risk of prostate cancer .

Example answer:
{"entities": [{"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "prostate carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "COX-2", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: By histology-based analysis , the Cys/Cys genotype showed a significantly positive association with small-cell carcinoma ( OR=2.40 , 95 % CI=1.32-4.49 ) and marginally significant association with adenocarcinoma ( OR=1.32 , 95 % CI=0.98-1.77 ) .

Example answer:
{"entities": [{"text": "small-cell carcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The estimated relative risk was significantly high for individuals with w1/m1 genotype at 3'UTR of CYP1A1 gene ( OR-4.64 ; 95 % CI = 1.51-14.86 ; P < 0.01 ) whereas the CYP1A1 Ile/Val genotype ( w2/m2 ) on exon 7 was found to be associated with a decreased risk for prostate cancer ( OR-0.17 ; 95 % CI = 0.02-0.89 ; P=0.03 ) .

Example answer:
{"entities": [{"text": "CYP1A1", "type": "GeneOrGeneProduct"}, {"text": "Ile/Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In overall analysis , the homozygous Cys/Cys genotype showed a significant association with lung cancer compared to Ser allele carrier status ( odds ratio ( OR ) =1.31 , 95 % confidence interval ( CI ) =1.02-1.69 ) .

Example answer:
{"entities": [{"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Odds ratios and 95 % confidence intervals for cancer risk by MLH1 -93 polymorphism status , and stratified by previous exposure to methylating chemotherapy , were calculated using unconditional logistic regression .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Nested within the cohort , a matched case-control study was performed to estimate the association between cyclophosphamide and bladder cancer using odds ratios ( ORs ) as relative risk .

## Item biored:test:75
Example input:
Sentence: Recent studies indicate that genetic ablation of mouse uroplakin ( UP ) III gene , which encodes a 47 kD urothelial-specific integral membrane protein forming urothelial plaques , causes VUR and hydronephrosis .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "uroplakin ( UP ) III", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hydronephrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Anticipation in familial lattice corneal dystrophy type I with R124C mutation in the TGFBI ( BIGH3 ) gene .

Example answer:
{"entities": [{"text": "lattice corneal dystrophy type I", "type": "DiseaseOrPhenotypicFeature"}, {"text": "R124C", "type": "SequenceVariant"}, {"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "BIGH3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Using direct sequencing a point mutation ( 144 G > A ) resulting in a Q48H substitution in exon 1 of the MYOC gene was observed in five of the eight glaucoma patients , but not in unaffected family members and 100 unrelated controls .

Example answer:
{"entities": [{"text": "144 G > A", "type": "SequenceVariant"}, {"text": "Q48H", "type": "SequenceVariant"}, {"text": "MYOC", "type": "GeneOrGeneProduct"}, {"text": "glaucoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We also found that the c.463-6T > G mutation leads to aberrant mRNA splicing , but no stable truncated protein was detected in the corresponding patient-derived fibroblasts .

Example answer:
{"entities": [{"text": "c.463-6T > G", "type": "SequenceVariant"}, {"text": "patient-derived", "type": "OrganismTaxon"}]}

Example input:
Sentence: Here , we report on two hemizygous mutations in OGT in individuals with X-linked intellectual disability ( XLID ) and dysmorphic features : one missense mutation ( p.Arg284Pro ) and one mutation leading to a splicing defect ( c.463-6T > G ) .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "X-linked intellectual disability", "type": "DiseaseOrPhenotypicFeature"}, {"text": "XLID", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "c.463-6T > G", "type": "SequenceVariant"}]}

Example input:
Sentence: We studied the PAX6 gene mutations in a cohort of affected individuals with different clinical phenotype including AN , coloboma of iris and choroid , or anterior segment malformations .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coloboma of iris and choroid", "type": "DiseaseOrPhenotypicFeature"}, {"text": "anterior segment malformations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The fact that no truncation or frame shift mutations have been found in any of the VUR patients , coupled with our recent finding that some breeding pairs of UP III knockout mice yield litters that show not only VUR , but also severe hydronephrosis and neonatal death , raises the possibility that major uroplakin mutations could be embryonically or postnatally lethal in humans .

Example answer:
{"entities": [{"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hydronephrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neonatal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: A novel mutation in GJA8 causing congenital cataract-microcornea syndrome in a Chinese pedigree .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The result expands the mutation spectrum of GJA8 in associated with congenital cataract and microcornea , and implies that this gene has direct involvement with the development of the lens as well as the other anterior segment of the eye .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcornea", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel missense mutation c.643T > C ( p.S216P ) was detected in the anterior segment malformation group .

Example answer:
{"entities": [{"text": "c.643T > C", "type": "SequenceVariant"}, {"text": "p.S216P", "type": "SequenceVariant"}, {"text": "anterior segment malformation", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: A splice mutation ( IVS3+1G/A ) in this gene has been reported in a zonular cataract with sutural opacities .

## Item biored:test:127
Example input:
Sentence: A genotype score combining the four newly identified SNPs showed an additive risk according to the number of high-risk alleles ( OR = 1.67 per high-risk allele , p < 0.0001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Presence or absence of a CCR5 wt/DD32 genotype and progressive or long-term nonprogressive course of infection stratify the clinical populations in a two-way design .

Example answer:
{"entities": [{"text": "CCR5", "type": "GeneOrGeneProduct"}, {"text": "infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A haplotype containing these four SNPs ( CATA ) significantly increased protection of wet AMD with a P value of 0.0005 and an odds ratio of 0.29 ( 95 % confidence interval : 0.15-0.60 ) .

Example answer:
{"entities": [{"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: C_6+/6+ and G_6+/6+ combined genotypes were respectively associated to the best and worst PFS ( P=0.03 when compared with each other ) , while combinations carrying the allele 6- determined an intermediate evolution that might be indicative of a variable response to chemotherapy .

Example answer:
{"entities": []}

Example input:
Sentence: Median progression-free survivals ( PFSs ) were 2.6 ( stratum 1 ) and 2.7 months ( stratum 2 ) .

Example answer:
{"entities": []}

Example input:
Sentence: PATIENTS AND METHODS : We examined associations between 54 polymorphisms that tag the known common variants ( minor allele frequency > 0.05 ) in 10 genes involved in oxidative damage repair ( CAT , SOD1 , SOD2 , GPX1 , GPX4 , GSR , TXN , TXN2 , TXNRD1 , and TXNRD2 ) and survival in 4,470 women with breast cancer .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "TXN", "type": "GeneOrGeneProduct"}, {"text": "TXN2", "type": "GeneOrGeneProduct"}, {"text": "TXNRD1", "type": "GeneOrGeneProduct"}, {"text": "TXNRD2", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: None of the studied polymorphisms alone affected overall or progression-free survival ( PFS ) .

Example answer:
{"entities": []}

Example input:
Sentence: Both polymorphisms were in strong linkage disequilibrium ( D ' = 0.71 , P < .001 ) , and the 3R/-6 base pair ( bp ) haplotype showed a significant overall survival benefit compared with the most prevalent haplotype 2R/+6bp ( HR = 0.42 ; 95 % CI , 0.20 to 0.85 ; P = .017 ) .

Example answer:
{"entities": []}

Example input:
Sentence: However , a longitudinal follow-up study on survival in the same sample indicated that 192RR homozygotes have a poorer survival compared to QQ homozygotes ( hazard rate : 1.38 , P = 0.04 ) .

Example answer:
{"entities": [{"text": "192RR", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Genotypes were analyzed by disease-free survival analysis using a Cox proportional hazards model .

## Item biored:test:74
Example input:
Sentence: In LCD , three novel heterozygous mutations found were glycine-594-valine ( Gly594Val ) in 2 of 18 patients , valine-539-aspartic acid ( Val539Asp ) in 1 patient , and deletion of valine 624 , valine 625 ( Val624-Val625del ) in 1 patient .

Example answer:
{"entities": [{"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glycine-594-valine", "type": "SequenceVariant"}, {"text": "Gly594Val", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "valine-539-aspartic acid", "type": "SequenceVariant"}, {"text": "Val539Asp", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion of valine 624 , valine 625", "type": "SequenceVariant"}, {"text": "Val624-Val625del", "type": "SequenceVariant"}]}

Example input:
Sentence: Genomic DNA was extracted from peripheral leukocytes from six affected and three unaffected members of a family with lattice corneal dystrophy type I. Exon 4 of the transforming growth factor-induced gene ( TGFBI ) was screened for the most frequent mutation , R124C , in the proband by sequencing .

Example answer:
{"entities": [{"text": "lattice corneal dystrophy type", "type": "DiseaseOrPhenotypicFeature"}, {"text": "transforming growth factor-induced gene", "type": "GeneOrGeneProduct"}, {"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "R124C", "type": "SequenceVariant"}]}

Example input:
Sentence: Anticipation in familial lattice corneal dystrophy type I with R124C mutation in the TGFBI ( BIGH3 ) gene .

Example answer:
{"entities": [{"text": "lattice corneal dystrophy type I", "type": "DiseaseOrPhenotypicFeature"}, {"text": "R124C", "type": "SequenceVariant"}, {"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "BIGH3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : The R124C mutation in TGFBI cosegregated with LCD type I in the investigated family .

Example answer:
{"entities": [{"text": "R124C", "type": "SequenceVariant"}, {"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "LCD type I", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We investigated clinical and cellular phenotypes of 24 children with mutations in the catalytic ( alpha ) subunit of the mitochondrial DNA ( mtDNA ) gamma polymerase ( POLG1 ) .

Example answer:
{"entities": [{"text": "mitochondrial DNA ( mtDNA ) gamma polymerase", "type": "GeneOrGeneProduct"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PURPOSE : To identify the underlying genetic defect in a four-generation family of Chinese origin with autosomal dominant congenital cataract-microcornea syndrome ( CCMC ) .

Example answer:
{"entities": [{"text": "genetic defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CCMC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The result expands the mutation spectrum of GJA8 in associated with congenital cataract and microcornea , and implies that this gene has direct involvement with the development of the lens as well as the other anterior segment of the eye .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcornea", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A G1103R mutation in CRB1 is co-inherited with high hyperopia and Leber congenital amaurosis .

Example answer:
{"entities": [{"text": "G1103R", "type": "SequenceVariant"}, {"text": "CRB1", "type": "GeneOrGeneProduct"}, {"text": "hyperopia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Leber congenital amaurosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel mutation in GJA8 causing congenital cataract-microcornea syndrome in a Chinese pedigree .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CONCLUSIONS : The DeltaG91 mutation in CRYBA3/A1 is associated with an autosomal dominant congenital nuclear lactescent cataract .

## Item biored:test:60
Example input:
Sentence: In our study , 17-dimethylaminoethylamino-17-demethoxygeldanamycin ( 17-DMAG ) or Hsp90beta knockdown dramatically alleviated the high-salt-diet-induced proteinuria and renal damage without altering blood pressure significantly , when it reversed activations of NF-kappaB , mTOR and p38 signalling cascades .

Example answer:
{"entities": [{"text": "17-dimethylaminoethylamino-17-demethoxygeldanamycin", "type": "ChemicalEntity"}, {"text": "17-DMAG", "type": "ChemicalEntity"}, {"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "p38", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Likewise , in vivo , B6D2F1 mice were treated with etoposide , daunorubicin , and doxorubicin , with or without dexrazoxane over a wide range of doses : posttreatment , a full hematologic evaluation was done .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "daunorubicin", "type": "ChemicalEntity"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "dexrazoxane", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Exposure to azathioprine ( > or =2 microg/mL ) for 48 hours increased cytosolic Ca2+ activity and annexin V binding and decreased forward scatter .

Example answer:
{"entities": [{"text": "azathioprine", "type": "ChemicalEntity"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "annexin V", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Nontoxic doses of dexrazoxane reduced myelosuppression and weight loss from daunorubicin and etoposide in mice and antagonized their antiproliferative effects in the colony assay ; however , dexrazoxane neither reduced myelosuppression , weight loss , nor the in vitro cytotoxicity from doxorubicin .

Example answer:
{"entities": [{"text": "dexrazoxane", "type": "ChemicalEntity"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "weight loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "daunorubicin", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cytotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "doxorubicin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Dexrazoxane protects against myelosuppression from the DNA cleavage-enhancing drugs etoposide and daunorubicin but not doxorubicin .

Example answer:
{"entities": [{"text": "Dexrazoxane", "type": "ChemicalEntity"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "daunorubicin", "type": "ChemicalEntity"}, {"text": "doxorubicin", "type": "ChemicalEntity"}]}

Example input:
Sentence: A LD ( 10 ) dose ( 8 mg doxorubicin/kg , ip ) administered on day 43 of the HFD feeding regimen led to higher cardiotoxicity , cardiac dysfunction , lipid peroxidation , and 80 % mortality in the obese ( OB ) rats in the absence of any significant renal or hepatic toxicity .

Example answer:
{"entities": [{"text": "doxorubicin/kg", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "renal or hepatic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Haloperidol-induced catalepsy was challenged with prior intracollicular microinjections of glutamate NMDA receptor antagonists , MK-801 ( 15 or 30 mmol/0.5 microl ) and AP7 ( 10 or 20 nmol/0.5 microl ) , or of the NMDA receptor agonist N-methyl-d-aspartate ( NMDA , 20 or 30 nmol/0.5 microl ) .

Example answer:
{"entities": [{"text": "Haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glutamate NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "N-methyl-d-aspartate", "type": "ChemicalEntity"}, {"text": "NMDA", "type": "ChemicalEntity"}]}

Example input:
Sentence: and metrifonate ( 10 mg/kg , p.o. , respectively ) reversed memory deficits induced by scopolamine and TRP depletion ( 10 mg/kg , i.p. , and 3 mg/kg , p.o. , respectively ) .

Example answer:
{"entities": [{"text": "memory", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In conclusion , administration of isoproterenol to rats results in primary loss of dystrophin , the most sensitive among the structural proteins that form the DGC that connects the extracellular matrix and the cytoskeleton in cardiomyocyte .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "dystrophin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The results showed that intracollicular microinjection of MK-801 and AP7 previous to systemic injections of haloperidol significantly attenuated the catalepsy , as indicated by a reduced latency to step down from a horizontal bar .

Example answer:
{"entities": [{"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Atropine-MK801 did not offer any additional protection against DFP toxicity .

## Item biored:test:28
Example input:
Sentence: In conclusion , although Ro4368554 did not improve a time-related retention deficit , it reversed a cholinergic and a serotonergic memory deficit , suggesting that both mechanisms may be involved in the facilitation of object memory by Ro4368554 and , possibly , other 5-HT ( 6 ) receptor antagonists .

Example answer:
{"entities": [{"text": "memory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5-HT ( 6 ) receptor", "type": "ChemicalEntity"}]}

Example input:
Sentence: However , scopolamine and ritanserin co-administration resulted in a significant decrease in escape latencies and traveled distances as compared to the scopolamine-treated rats .

Example answer:
{"entities": [{"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: and metrifonate ( 10 mg/kg , p.o. , respectively ) reversed memory deficits induced by scopolamine and TRP depletion ( 10 mg/kg , i.p. , and 3 mg/kg , p.o. , respectively ) .

Example answer:
{"entities": [{"text": "memory", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study sought to characterize the cognitive-enhancing effects of the 5-HT ( 6 ) antagonist Ro4368554 ( 3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole ) in a rat object recognition task employing a cholinergic ( scopolamine pretreatment ) and a serotonergic- ( tryptophan ( TRP ) depletion ) deficient model , and compared its pattern of action with that of the acetylcholinesterase inhibitor metrifonate .

Example answer:
{"entities": [{"text": "5-HT ( 6 )", "type": "GeneOrGeneProduct"}, {"text": "Ro4368554", "type": "ChemicalEntity"}, {"text": "3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "cholinergic", "type": "ChemicalEntity"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "serotonergic-", "type": "ChemicalEntity"}, {"text": "tryptophan", "type": "ChemicalEntity"}, {"text": "TRP", "type": "ChemicalEntity"}, {"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "metrifonate", "type": "ChemicalEntity"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Nimodipine prevents memory impairment caused by nitroglycerin-induced hypotension in adult mice .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "ChemicalEntity"}, {"text": "memory impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nitroglycerin-induced", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Therefore NFkappaB activity , oxidative stress , neuronal nitric oxide synthase ( nNOS ) activity , spatial learning and memory as well as the effect of topiramate , a previously proposed therapy for cocaine addiction , were evaluated in an experimental model of cocaine administration in rats .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "neuronal nitric oxide synthase", "type": "GeneOrGeneProduct"}, {"text": "nNOS", "type": "GeneOrGeneProduct"}, {"text": "topiramate", "type": "ChemicalEntity"}, {"text": "cocaine addiction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cocaine", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The effect of ritanserin ( 5-HT2 antagonist ) on scopolamine ( muscarinic cholinergic antagonist ) -induced amnesia in Morris water maze ( MWM ) was investigated .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "5-HT2", "type": "GeneOrGeneProduct"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "muscarinic cholinergic", "type": "GeneOrGeneProduct"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Microinjection of ritanserin into the CA1 region of hippocampus improves scopolamine-induced amnesia in adult male rats .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Our findings show that microinjection of ritanserin into the CA1 region of the hippocampus improves the scopolamine-induced amnesia .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Nefiracetam is a novel pyrrolidone derivative which attenuates scopolamine-induced learning and post-training consolidation deficits .

## Item biored:test:78
Example input:
Sentence: CONCLUSION : Variation in IL10 , CRP , GSTP1 , IL1B , and NOS2 was associated with prostate cancer recurrence independent of pathologic prognostic factors .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "NOS2", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ubiquitin carboxyl-terminal esterase L1 ( UCHL1 ) is associated with stem-like cancer cell functions in pediatric high-grade glioma .

Example answer:
{"entities": [{"text": "Ubiquitin carboxyl-terminal esterase L1", "type": "GeneOrGeneProduct"}, {"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glioma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A mouse inflammatory cytokine and receptor RT2 profiler array was used to determine regulated transcripts in the urinary bladder of wild type ( WT ) and VIP ( -/- ) mice with or without CYP-induced cystitis ( 150 mg/kg ; i.p .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "CYP-induced", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: It was concluded that coenzyme Q10 represents a potential therapeutic option to protect against acute cisplatin nephrotoxicity commonly encountered in clinical practice .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "nephrotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Curcumin also decreased bladder tumor growth in athymic nude mice bearing KU7 cells as xenografts and this was accompanied by decreased Sp1 , Sp3 , and Sp4 protein levels in tumors .

Example answer:
{"entities": [{"text": "Curcumin", "type": "ChemicalEntity"}, {"text": "bladder tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "KU7", "type": "CellLine"}, {"text": "Sp1", "type": "GeneOrGeneProduct"}, {"text": "Sp3", "type": "GeneOrGeneProduct"}, {"text": "Sp4", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conclude that GSTP1 Ile/Val polymorphism is involved in the risk of prostate cancer development in our population .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile/Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The d-myo-inositol 1,4,5-trisphosphate ( IP ( 3 ) ) /Ca ( 2+ ) /protein kinase C ( PKC ) /mitogen-activated protein kinase pathway regulates cholangiocarcinoma growth .

Example answer:
{"entities": [{"text": "d-myo-inositol 1,4,5-trisphosphate", "type": "ChemicalEntity"}, {"text": "IP ( 3 )", "type": "ChemicalEntity"}, {"text": "( 2+ )", "type": "ChemicalEntity"}, {"text": "kinase C", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "protein kinase", "type": "GeneOrGeneProduct"}, {"text": "cholangiocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: VIP ( -/- ) mice exhibit altered bladder function and neurochemical properties in micturition pathways after cyclophosphamide ( CYP ) -induced cystitis .

Example answer:
{"entities": [{"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CYP", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "ChemicalEntity"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ascites", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoalbuminemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : The purpose of this study was to analyze the value of germline and tumor thymidylate synthase ( TS ) genotyping as a prognostic marker in a series of colorectal cancer patients receiving adjuvant fluorouracil ( FU ) -based treatment .

Example answer:
{"entities": [{"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thymidylate synthase", "type": "GeneOrGeneProduct"}, {"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "fluorouracil", "type": "ChemicalEntity"}, {"text": "FU", "type": "ChemicalEntity"}]}

Input:
Sentence: OBJECTIVE : To assess and characterise the risk of bladder cancer , and its relation to cyclophosphamide , in patients with Wegener 's granulomatosis .

## Item biored:test:54
Example input:
Sentence: Upon pretreatment with mangiferin ( 100 mg/kg body weight suspended in 2 ml of dimethyl sulphoxide ) given intraperitoneally for 28 days to MI rats protected the above-mentioned parameters to fall from the normal levels .

Example answer:
{"entities": [{"text": "mangiferin", "type": "ChemicalEntity"}, {"text": "dimethyl sulphoxide", "type": "ChemicalEntity"}, {"text": "MI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Male SD rats ( n = 30 ) were treated with Ato ( 50 mg/kg per day in drinking water ) or tap water for 15 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Ato", "type": "ChemicalEntity"}]}

Example input:
Sentence: A total of 60 male Wistar albino rats were randomly divided into four groups ( 15/group ) : The control group injected with single doses of normal saline ( i.c.v ) followed 24 h later by BCNU solvent ( i.v ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "BCNU", "type": "ChemicalEntity"}]}

Example input:
Sentence: A LD ( 10 ) dose ( 8 mg doxorubicin/kg , ip ) administered on day 43 of the HFD feeding regimen led to higher cardiotoxicity , cardiac dysfunction , lipid peroxidation , and 80 % mortality in the obese ( OB ) rats in the absence of any significant renal or hepatic toxicity .

Example answer:
{"entities": [{"text": "doxorubicin/kg", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "renal or hepatic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/ K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male Sprague-Dawley rats were injected with saline on postnatal day ( P ) 20 , or a convulsant dose of pilocarpine on P20 or P45 .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Subcutaneous injection of ISPH ( 200 mg/kg body weight in 1 ml saline ) to rats for 2 consecutive days caused myocardial damage in rat heart , which was determined by the increased activity of serum lactate dehydrogenase ( LDH ) and creatine phosphokinase isoenzymes ( CK-MB ) , increased uric acid level and reduced plasma iron binding capacity .

Example answer:
{"entities": [{"text": "ISPH", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "myocardial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "LDH", "type": "GeneOrGeneProduct"}, {"text": "creatine phosphokinase isoenzymes", "type": "GeneOrGeneProduct"}, {"text": "CK-MB", "type": "GeneOrGeneProduct"}, {"text": "uric acid", "type": "ChemicalEntity"}, {"text": "iron", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male Wistar rats were treated by Dex ( 30 u g/kg/day subcutaneously ) or saline for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : Adult male Wistar rats were intracerebroventricularly ( icv ) infused with STZ ( 750 ug ) on d 1 and d 3 , and a passive avoidance task was assessed 2 weeks after the first injection of STZ .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "STZ", "type": "ChemicalEntity"}]}

Input:
Sentence: The protective action of subcutaneously ( SC ) administered antidotes or their combinations in DFP ( 2.0 mg/kg BW ) intoxication was studied in 9-10-weeks-old Han-Wistar male rats .

## Item biored:test:101
Example input:
Sentence: In cells stained with fluorescent dyes targeting lysosomes , CAA induced an increase in lysosomal size and lysosomal leakage .

Example answer:
{"entities": [{"text": "CAA", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : KCa3.1 expression was markedly associated with endoplasmic reticulum ( ER ) stress and unfolded protein response ( UPR ) in both Abeta-stimulated primary astrocytes and brain lysates of AD patients and APP/PS1 AD mice .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Abeta-stimulated", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Ectodermal dysplasia-skin fragility syndrome resulting from a new homozygous mutation , 888delC , in the desmosomal protein plakophilin 1 .

Example answer:
{"entities": [{"text": "Ectodermal dysplasia-skin fragility syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "888delC", "type": "SequenceVariant"}, {"text": "plakophilin 1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: TSPO was up-regulated in Iba1 ( + ) cells from brains of patients with ICH and in CD11b ( + ) CD45 ( int ) cells from mice subjected to collagenase-induced ICH .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "Iba1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD11b", "type": "GeneOrGeneProduct"}, {"text": "CD45", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "collagenase-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : HAT adipose tissue demonstrated increased lipid related genes for storage ( CD36 , DGAT1 , DGAT2 , SCD1 , FASN , and LPL ) , lipolysis ( HSL , CES1 , perilipin ) , fatty acid binding proteins ( FABP1 , FABP3 ) and adipocyte differentiation markers ( CEBPalpha , CEBPbeta , PPARgamma ) .

Example answer:
{"entities": [{"text": "lipid", "type": "ChemicalEntity"}, {"text": "CD36", "type": "GeneOrGeneProduct"}, {"text": "DGAT1", "type": "GeneOrGeneProduct"}, {"text": "DGAT2", "type": "GeneOrGeneProduct"}, {"text": "SCD1", "type": "GeneOrGeneProduct"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "LPL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CES1", "type": "GeneOrGeneProduct"}, {"text": "perilipin", "type": "GeneOrGeneProduct"}, {"text": "fatty acid binding proteins", "type": "GeneOrGeneProduct"}, {"text": "FABP1", "type": "GeneOrGeneProduct"}, {"text": "FABP3", "type": "GeneOrGeneProduct"}, {"text": "CEBPalpha", "type": "GeneOrGeneProduct"}, {"text": "CEBPbeta", "type": "GeneOrGeneProduct"}, {"text": "PPARgamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Those novel compound heterozygous mutations were thought to contribute to the loss of CHST6 function , which induced the abnormal metabolism of keratan sulfate ( KS ) that deposited in the corneal stroma .

Example answer:
{"entities": [{"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "keratan sulfate", "type": "ChemicalEntity"}, {"text": "KS", "type": "ChemicalEntity"}]}

Example input:
Sentence: This instability possibly resulted in reduced expression levels of differentiation markers , such as keratin 1 and filaggrin , in the perineal epithelia .

Example answer:
{"entities": [{"text": "keratin 1", "type": "GeneOrGeneProduct"}, {"text": "filaggrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We report an unusual case of an inherited disorder of the desmosomal protein plakophilin 1 , resulting in ectodermal dysplasia-skin fragility syndrome .

Example answer:
{"entities": [{"text": "inherited disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "plakophilin 1", "type": "GeneOrGeneProduct"}, {"text": "ectodermal dysplasia-skin fragility syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Skin biopsy revealed widening of intercellular spaces in the epidermis and a reduced number of small , poorly formed desmosomes .

Example answer:
{"entities": []}

Input:
Sentence: Our data suggested that cytoskeleton disorganization in epidermal cells is likely associated with the pathogenesis of DSAP .

## Item biored:test:106
Example input:
Sentence: METHODS : Ag-globin gene sequencing was performed on genomic DNA isolated from a total of 75 b-thalassemia patients , including 31 b ( 0 ) 39/b ( 0 ) 39 , 33 b ( 0 ) 39/b ( + ) IVSI-110 , 9 b ( + ) IVSI-110/b ( + ) IVSI-110 , one b ( 0 ) IVSI-1/b ( + ) IVSI-6 and one b ( 0 ) 39/b ( + ) IVSI-6 .

Example answer:
{"entities": [{"text": "Ag-globin", "type": "GeneOrGeneProduct"}, {"text": "b-thalassemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: DNA from peripheral nuclear blood cells was genotyped for 5-HTTLPR using standard polymerase chain reaction methods.A significant group effect was observed only on memory function tasks ( p = 0.04 ) but not on reaction times ( p = 0.61 ) or attention/executive functioning ( p = 0.59 ) .

Example answer:
{"entities": [{"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Genotyping was determined by the polymerase chain reaction-restriction fragment length polymorphism ( PCR-RFLP ) technique .

Example answer:
{"entities": []}

Example input:
Sentence: Microsatellite markers at 13q31-q32 were PCR amplified and run on an ABI Prism 310 genetic analyzer and genotyped with the GeneScan analysis .

Example answer:
{"entities": []}

Example input:
Sentence: We have developed a sensitive single tube tetra-primer PCR assay to detect both the c.1138G > A and c.1138G > C mutations and can successfully distinguish DNA samples that are homozygous and heterozygous for the c.1138G > A mutation .

Example answer:
{"entities": [{"text": "c.1138G > A", "type": "SequenceVariant"}, {"text": "c.1138G > C", "type": "SequenceVariant"}]}

Example input:
Sentence: The -930A > G polymorphism was genotyped using the TaqMan - Pre-designed SNP Genotyping Assay ( Applied Biosystems ) .

Example answer:
{"entities": [{"text": "-930A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: TS genotyping methods were polymerase chain reaction ( PCR ) for VNTR and PCR , followed by restriction length fragment polymorphism ( PCR-RFLP ) for SNP and ins/del 6 bp .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "ins/del 6 bp", "type": "SequenceVariant"}]}

Example input:
Sentence: We genotyped the SNPs using TaqMan assays .

Example answer:
{"entities": []}

Example input:
Sentence: Patients were genotyped for rs4704559 , rs10942891 and rs4704560 by allelic discrimination with Taqman assays .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "rs4704559", "type": "SequenceVariant"}, {"text": "rs10942891", "type": "SequenceVariant"}, {"text": "rs4704560", "type": "SequenceVariant"}]}

Example input:
Sentence: Genotyping was performed by kinetic polymerase chain-reaction or TaqMan assays .

Example answer:
{"entities": []}

Input:
Sentence: IL12B 3'-UTR and promoter genotyping was performed by Taqman-based assays with allele-specific oligonucleotide probes and PCR-based allele-specific DNA-amplification , respectively .

## Item biored:test:130
Example input:
Sentence: However , a longitudinal follow-up study on survival in the same sample indicated that 192RR homozygotes have a poorer survival compared to QQ homozygotes ( hazard rate : 1.38 , P = 0.04 ) .

Example answer:
{"entities": [{"text": "192RR", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: The challenge was considered positive if one or more of the following appeared : erythema , rush or urticaria-angioedema .

Example answer:
{"entities": [{"text": "erythema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "urticaria-angioedema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Meta-analysis of the two trials demonstrated a significant overall reduction in the composite end point in Hp 2-2 DM individuals with vitamin E ( odds ratio : 0.58 ; 95 % CI : 0.40-0.86 ; p = 0.006 ) .

Example answer:
{"entities": [{"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vitamin E", "type": "ChemicalEntity"}]}

Example input:
Sentence: A Kruskal-Wallis 1-way analysis of variance indicated a significant difference among the 4 treatment groups ( H = 15.34 ; P < 0.001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: In Southern blot analysis , from the signal densities of the hybridized bands and their similarities to those of exons 2 and 3 in our previous quantitative study , we found that exon 1beta was homozygously deleted in four cases , hemizygously deleted in five cases and not deleted in one case .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSION : In a PA retention paradigm , the injection of NTG immediately after learning produced a significant impairment of long-term associative memory in mice , whereas delayed induced hypotension had no effect .

Example answer:
{"entities": [{"text": "NTG", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Hallmarks of constitutive activity were all reversed by a specific PrlR antagonist , which opens potential therapeutic approaches for MFA , or any other disease that could be associated with this mutation in future .

Example answer:
{"entities": [{"text": "PrlR antagonist", "type": "ChemicalEntity"}, {"text": "MFA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The fixed effects also correct for nonindependence of data between populations and results in even further shrinkage of individual patient estimates .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}]}

Input:
Sentence: In contrast to the result of Healey et al .

## Item biored:test:45
Example input:
Sentence: The entire coding region of BRCA1 and BRCA2 was screened for the presence of germline mutations , by use of SSCP followed by direct sequencing of observed variants .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "BRCA2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We analyzed the nucleotidic sequence of the CYP2F1 gene in DNA samples from 90 French Caucasians consisting in 44 patients with lung cancer and 46 control individuals , using single-strand conformation polymorphism analysis of PCR products ( PCR-SSCP ) .

Example answer:
{"entities": [{"text": "CYP2F1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Polymerase chain reaction ( PCR ) showed EGFR amplification in 25 of 77 ( 32 % ) cases and p16 homozygous deletion in 32 of 77 ( 42 % ) cases .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Exonic and intronic segments , 5 ' and 3 ' flanking regions of IRS2 ( 14.5 kb ) , were bidirectionally sequenced for single nucleotide polymorphism ( SNP ) discovery in 934 Hispanic children using 3730XL DNA Sequencers .

Example answer:
{"entities": [{"text": "IRS2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Single stranded conformational polymorphism ( SSCP ) analysis and sequencing revealed a novel heterozygous C139T transition in PAX9 in the affected members of the family .

Example answer:
{"entities": [{"text": "C139T", "type": "SequenceVariant"}, {"text": "PAX9", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also designed a rapid polymerase chain reaction-restriction fragment length polymorphism ( PCR-RFLP ) method to analyze the same mutation , amplifying exon 4 and digesting with PstI restriction enzyme .

Example answer:
{"entities": [{"text": "PstI", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Polymerase chain reaction was carried out and single nucleotide polymorphisms of FGFR4 were identified by restriction enzyme digestion .

Example answer:
{"entities": [{"text": "FGFR4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SSCP followed by DNA sequencing of the kinase domain ( exons 18-21 ) of the EGFR gene revealed mutations in 2 ou of 69 ( 3 % ) glioblastomas in Japan and in 4 of 81 ( 5 % ) glioblastomas in Switzerland .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: We screened all 17 exons of the FMR1 gene for mutations in 90 autistic or mentally retarded children using polymerase chain reaction ( PCR ) -single strand conformation polymorphism ( SSCP ) analysis .
