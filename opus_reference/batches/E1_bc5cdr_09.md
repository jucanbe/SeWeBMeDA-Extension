# Task
You are a biomedical named entity recognition system for the BC5CDR annotation scheme.
Identify every mention of the following entity types in the sentence:
- Chemical: Drug, compound, molecule, medication (e.g., cisplatin, aspirin).
- Disease: Pathological or medical condition (e.g., diabetes, lymphoma).

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

## Item bc5cdr:test:1995
Example input:
Sentence: Changes evoked by a single intraperitoneal injection of rilmenidine ( 600 microg/kg ) or alpha-methyldopa ( 100 mg/kg ) , selective I1- and alpha2-receptor agonists , respectively , in blood pressure , hemodynamic variability , and locomotor activity were assessed in radiotelemetered sham-operated and ovariectomized ( Ovx ) Sprague-Dawley female rats with or without 12-wk estrogen replacement .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "estrogen", "type": "Chemical"}]}

Example input:
Sentence: d-1 given for 4 weeks , elevated blood pressure from 102+/-13 to 152+/-15 mm Hg and increased the synthesis of ET-1 and the levels of ET-1 mRNA in the mesenteric artery ( 240 % and 230 % , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: The hypotensive effect of 100 mg/kg alpha-methyldopa was also partially reversed by naloxone .

Example answer:
{"entities": [{"text": "hypotensive", "type": "Disease"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "naloxone", "type": "Chemical"}]}

Example input:
Sentence: During an 18-month period of study 41 hemodialyzed patients receiving desferrioxamine ( 10-40 mg/kg BW/3 times weekly ) for the first time were monitored for detection of audiovisual toxicity .

Example answer:
{"entities": [{"text": "desferrioxamine", "type": "Chemical"}, {"text": "audiovisual toxicity", "type": "Disease"}]}

Example input:
Sentence: A single MPEP ( 5 mg/kg ip ) injection reduced the basal extracellular dopamine level in the striatum , as well as dopamine release stimulated either by methamphetamine ( 10 mg/kg sc ) or by intrastriatally administered veratridine ( 100 microM ) .

Example answer:
{"entities": [{"text": "MPEP", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "veratridine", "type": "Chemical"}]}

Example input:
Sentence: In contrast to controls , methoctramine increased -- instead of decreased -- the tonic responses at high frequencies .

Example answer:
{"entities": [{"text": "methoctramine", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Ovx significantly enhanced the hypotensive response to alpha-methyldopa , in contrast to no effect on rilmenidine hypotension .

Example answer:
{"entities": [{"text": "hypotensive", "type": "Disease"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "rilmenidine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: NX+HP caused a further rise in blood pressure in Li-pretreated rats .

Example answer:
{"entities": [{"text": "Li-pretreated", "type": "Chemical"}]}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "a reduced locomotor activity", "type": "Disease"}]}

Input:
Sentence: Methoxamine evoked non-significant increases in MUP and diastolic blood pressure but caused a significant rise in systolic blood pressure and significant fall in heart rate at maximum dosage .

## Item bc5cdr:test:1368
Example input:
Sentence: The aldosterone-sensitive serum- and glucocorticoid-inducible kinase SGK1 has been shown to participate in the stimulation of ENaC and to mediate renal fibrosis following mineralocorticoid and salt excess .

Example answer:
{"entities": [{"text": "aldosterone-sensitive", "type": "Chemical"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: Captopril may , by the same mechanism , reduce the increase in glomerular filtration that is known to occur after an injection of thrombin , thereby diminishing the aggregation of fibrin monomers in the glomeruli , with the result that less fibrin will be deposited and thus less kidney damage will be produced .

Example answer:
{"entities": [{"text": "Captopril", "type": "Chemical"}, {"text": "kidney damage", "type": "Disease"}]}

Example input:
Sentence: Furthermore , glomerulosclerosis index was significantly increased in the nitrendipine-treated group compared with the hypertensive controls ( 0.38 +/- 0.1 versus 0.13 +/- 0.04 ) .

Example answer:
{"entities": [{"text": "glomerulosclerosis", "type": "Disease"}, {"text": "nitrendipine-treated", "type": "Chemical"}, {"text": "hypertensive", "type": "Disease"}]}

Example input:
Sentence: It has also been suggested that sirolimus directly causes increased glomerular permeability/injury , but evidence for this mechanism is currently inconclusive .

Example answer:
{"entities": [{"text": "sirolimus", "type": "Chemical"}]}

Example input:
Sentence: HP failed to accentuante progression of renal failure and in fact tended to increase GFR and decrease plasma creatinine levels in lithium pretreated rats .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: When comparing all lithium treated versus non-lithium-treated groups , lithium caused a reduction in glomerular filtration rate ( GFR ) without significant changes in effective renal plasma flow ( as determined by a marker secreted into the proximal tubules ) or lithium clearance .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: Renal plasma flow increased , but albumin excretion and glomerulosclerosis did not change after enalapril treatment .

Example answer:
{"entities": [{"text": "glomerulosclerosis", "type": "Disease"}, {"text": "enalapril", "type": "Chemical"}]}

Example input:
Sentence: Reduction in GFR was associated with the development of glomerular sclerosis in both treated and untreated rats .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: Secondary outcomes were a postdose SCr increase > or = 25 % , a postdose estimated glomerular filtration rate decrease of > or = 25 % , and the mean peak change in SCr .

Example answer:
{"entities": []}

Example input:
Sentence: HS diet for 4 wk caused a progressive increase in BP , protein and albumin excretion , and glomerular sclerosis in male DS rats , which were attenuated by castration .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Input:
Sentence: The SOD-induced increase in glomerular filtration rate was associated with a marked improvement in RBF , an increase in urinary cGMP excretion , and a decrease in renal renin and endothelin-1 content .

## Item bc5cdr:test:1864
Example input:
Sentence: BACKGROUND : Electrocardiography has a very low sensitivity in detecting dobutamine-induced myocardial ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}]}

Example input:
Sentence: A reproducible model for producing diffuse myocardial injury ( epinephrine infusion ) has been developed to study the cardioprotective effects of agents or maneuvers which might alter the evolution of acute myocardial infarction .

Example answer:
{"entities": [{"text": "myocardial injury", "type": "Disease"}, {"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: To develop a more sensitive echocardiographic screening test for cardiac damage due to doxorubicin , a cohort study was performed using dobutamine infusion to differentiate asymptomatic long-term survivors of childhood cancer treated with doxorubicin from healthy control subjects .

Example answer:
{"entities": [{"text": "cardiac damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: Severe reversible left ventricular systolic and diastolic dysfunction due to accidental iatrogenic epinephrine overdose .

Example answer:
{"entities": [{"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "epinephrine", "type": "Chemical"}, {"text": "overdose", "type": "Disease"}]}

Example input:
Sentence: Simultaneous measurements of ECG and brachial artery dP/dtejc were performed at each dobutamine level .

Example answer:
{"entities": [{"text": "dobutamine", "type": "Chemical"}]}

Example input:
Sentence: Assessment of a new non-invasive index of cardiac performance for detection of dobutamine-induced myocardial ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}]}

Example input:
Sentence: Dobutamine stress echocardiography : a sensitive indicator of diminished myocardial function in asymptomatic doxorubicin-treated long-term survivors of childhood cancer .

Example answer:
{"entities": [{"text": "Dobutamine", "type": "Chemical"}, {"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: End-systolic left ventricular posterior wall dimension at the 5-micrograms/kg per min dobutamine infusion for the doxorubicin-treated group was 14.1 +/- 2.4 mm versus 19.3 +/- 2.6 mm for control subjects ( p less than 0.01 ) .

Example answer:
{"entities": [{"text": "dobutamine", "type": "Chemical"}, {"text": "doxorubicin-treated", "type": "Chemical"}]}

Example input:
Sentence: The most important findings were that compared with values in control subjects , end-systolic left ventricular posterior wall dimension and percent of left ventricular posterior wall thickening in doxorubicin-treated patients were decreased at baseline study and these findings were more clearly delineated with dobutamine stimulation .

Example answer:
{"entities": [{"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVES : To assess the added diagnostic value of a new cardiac performance index ( dP/dtejc ) measurement , based on brachial artery flow changes , as compared to standard 12-lead ECG , for detecting dobutamine-induced myocardial ischemia , using Tc99m-Sestamibi single-photon emission computed tomography as the gold standard of comparison to assess the presence or absence of ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "Tc99m-Sestamibi", "type": "Chemical"}, {"text": "ischemia", "type": "Disease"}]}

Input:
Sentence: DESIGN : A randomised crossover study of recovery time of systolic and diastolic left ventricular function after exercise and dobutamine induced ischaemia .

## Item bc5cdr:test:1972
Example input:
Sentence: In the bolus group , 26.0 % ( 13/50 ) had akathisia compared with 32.7 % ( 16/49 ) in the infusion group ( Delta=-6.7 % ; 95 % confidence interval [ CI ] -24.6 % to 11.2 % ) .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: The differences in mortality and morbidity between the two groups were not significant .

Example answer:
{"entities": []}

Example input:
Sentence: None of these groups showed significant difference in percent inhibition .

Example answer:
{"entities": []}

Example input:
Sentence: However , by comparing each subgroup to control group , we found statistically significant decreases of TEOAEs amplitudes at 4000Hz for all three groups .

Example answer:
{"entities": [{"text": "decreases of TEOAEs amplitudes", "type": "Disease"}]}

Example input:
Sentence: In phase A , extrapyramidal signs tended to be greater with the standard dose than in the other two conditions , primarily because of a subgroup ( 20 % ) who developed moderate to severe signs .

Example answer:
{"entities": [{"text": "extrapyramidal signs", "type": "Disease"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: The EF was 40 % , in the group with MP and 44 % in the group with severe MR and it can be a factor associated with clinical events in the last group .

Example answer:
{"entities": [{"text": "MP", "type": "Disease"}, {"text": "MR", "type": "Disease"}]}

Example input:
Sentence: Comparisons between exposed newborns ' subgroups revealed no significant differences .

Example answer:
{"entities": []}

Example input:
Sentence: Also the frequency of abnormal electro-diagnostic findings showed similarity between the two groups ( G : 7/23 = 30.4 % ; P : 6/20 = 30 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: No significant differences between groups were found at enrollment .

Example answer:
{"entities": []}

Input:
Sentence: There were no statistically significant differences in EPSs between groups .

## Item bc5cdr:test:1835
Example input:
Sentence: Focal glutamate photostimulation of the granule cell layer at sites distant from the recording pipette resulted in population responses of 1-30 s duration in slices from SE survivors but not other groups .

Example answer:
{"entities": [{"text": "glutamate", "type": "Chemical"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Electron microscopical immunohistochemistry revealed positive reaction products noted on the secretory granules , Golgi cisternae , and endoplasmic reticulum of the untreated rat prolactinoma cells .

Example answer:
{"entities": [{"text": "prolactinoma", "type": "Disease"}]}

Example input:
Sentence: Interestingly , all the drugs , such as , AAP , AMI and DOX induced apoptotic death in addition to necrosis in the respective organs which was very effectively blocked by GSPE .

Example answer:
{"entities": [{"text": "AAP", "type": "Chemical"}, {"text": "AMI", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "necrosis", "type": "Disease"}, {"text": "GSPE", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Immunofluorescence staining with the MRP2 antibody was found to label a high number of microvessels throughout the brain in normal Wistar rats , whereas such labeling was absent in TR ( - ) rats .

Example answer:
{"entities": []}

Example input:
Sentence: In vivo protection of dna damage associated apoptotic and necrotic cell deaths during acetaminophen-induced nephrotoxicity , amiodarone-induced lung toxicity and doxorubicin-induced cardiotoxicity by a novel IH636 grape seed proanthocyanidin extract .

Example answer:
{"entities": [{"text": "necrotic", "type": "Disease"}, {"text": "acetaminophen-induced", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "amiodarone-induced", "type": "Chemical"}, {"text": "lung toxicity", "type": "Disease"}, {"text": "doxorubicin-induced", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}, {"text": "IH636 grape seed proanthocyanidin extract", "type": "Chemical"}]}

Example input:
Sentence: Cells were pretreated with maltolyl p-coumarate , before exposed to amyloid beta peptide ( 1-42 ) , glutamate or H2O2 .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "H2O2", "type": "Chemical"}]}

Example input:
Sentence: Trifluoroacetyl-adducted proteins were detected in surviving hepatocytes .

Example answer:
{"entities": [{"text": "Trifluoroacetyl-adducted", "type": "Chemical"}]}

Example input:
Sentence: The cell populations were examined regarding total cell recovery correlated with gland weight , intracellular prolactin ( PRL ) content and subsequent release in primary culture , immunocytochemical PRL staining , density and/or size alterations via separation on Ficoll-Hypaque and by unit gravity sedimentation , and cell cycle analysis , after acriflavine DNA staining , by laser flow cytometry .

Example answer:
{"entities": [{"text": "acriflavine", "type": "Chemical"}]}

Example input:
Sentence: We also assessed cell viability , mitochondrial membrane potential changes and counted autophagic vacuoles in cultured cardiomyocytes .

Example answer:
{"entities": []}

Example input:
Sentence: Additionally , this may have been the first report on AMI-induced apoptotic death in the lung tissue .

Example answer:
{"entities": [{"text": "AMI-induced", "type": "Chemical"}]}

Input:
Sentence: Apoptosis was assessed by fluorescence microscopy in Hoechst 33342- and propidium iodide stained cell samples .

## Item bc5cdr:test:2091
Example input:
Sentence: Among 547 preterm infants of < or = 34 weeks gestation born between 1987 and 1991 , 8 children ( 1.46 % ) developed severe progressive and bilateral sensorineural hearing loss .

Example answer:
{"entities": [{"text": "sensorineural hearing loss", "type": "Disease"}]}

Example input:
Sentence: Visual analogue scores ( mean +/- SD ) during induction were lower in Groups L ( 3.3 +/- 2.5 ) and T ( 4.1 +/- 2.7 ) than in Group C ( 5.6 +/- 2.3 ) ; P = 0.0031 .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : In exposed neonates , TEOAEs mean response ( across frequency ) and mean amplitude at 4000Hz was significantly lower than in non-exposed neonates .

Example answer:
{"entities": []}

Example input:
Sentence: During a 9-year period , we retrospectively collected 27 neurological events ( 11 % ) in as many patients , from 253 children enrolled in the ALL front-line protocol .

Example answer:
{"entities": [{"text": "ALL", "type": "Disease"}]}

Example input:
Sentence: RESULTS : After 12 weeks of treatment , the mean ( sd ) scores for CGI-SF were significantly lower , i.e .

Example answer:
{"entities": []}

Example input:
Sentence: Sulfonamides were associated with anencephaly ( adjusted OR [ AOR ] = 3.4 ; 95 % confidence interval [ CI ] , 1.3-8.8 ) , hypoplastic left heart syndrome ( AOR = 3.2 ; 95 % CI , 1.3-7.6 ) , coarctation of the aorta ( AOR = 2.7 ; 95 % CI , 1.3-5.6 ) , choanal atresia ( AOR = 8.0 ; 95 % CI , 2.7-23.5 ) , transverse limb deficiency ( AOR = 2.5 ; 95 % CI , 1.0-5.9 ) , and diaphragmatic hernia ( AOR = 2.4 ; 95 % CI , 1.1-5.4 ) .

Example answer:
{"entities": [{"text": "Sulfonamides", "type": "Chemical"}, {"text": "anencephaly", "type": "Disease"}, {"text": "hypoplastic left heart syndrome", "type": "Disease"}, {"text": "coarctation of the aorta", "type": "Disease"}, {"text": "choanal atresia", "type": "Disease"}, {"text": "transverse limb deficiency", "type": "Disease"}, {"text": "diaphragmatic hernia", "type": "Disease"}]}

Example input:
Sentence: Mean TEOAEs responses of highly exposed newborns were also significantly lower in comparison to our control group .

Example answer:
{"entities": []}

Example input:
Sentence: Comparisons between exposed newborns ' subgroups revealed no significant differences .

Example answer:
{"entities": []}

Example input:
Sentence: These effects seem to be equally true for all exposed newborns , regardless of the degree of exposure .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : The patients in the study group were significantly younger than the patients in the control group ( P < 0.002 ) .

Example answer:
{"entities": []}

Input:
Sentence: This result is consistent with results of similar studies in term infants .

## Item bc5cdr:test:1764
Example input:
Sentence: On the contrary , the cataleptogenic effect of haloperidol was significantly reduced in rats treated with desipramine and 6-OHDA but not in rats treated with 6-OHDA or in rats with lesions of the locus coeruleus .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "desipramine", "type": "Chemical"}, {"text": "6-OHDA", "type": "Chemical"}]}

Example input:
Sentence: Galanthamine hydrobromide , an anticholinesterase drug capable of penetrating the blood-brain barrier , was used in a patient demonstrating central effects of scopolamine ( hyoscine ) overdosage .

Example answer:
{"entities": [{"text": "Galanthamine hydrobromide", "type": "Chemical"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "hyoscine", "type": "Chemical"}, {"text": "overdosage", "type": "Disease"}]}

Example input:
Sentence: Controlled hypotension to an average MAP of 50-55 mm Hg was induced by increasing the dose of isoflurane , and maintained at an inspired concentration of 2.2 +/- 0.2 % .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "Hg", "type": "Chemical"}, {"text": "isoflurane", "type": "Chemical"}]}

Example input:
Sentence: In unanesthetized , spontaneously hypertensive rats the decrease in blood pressure and heart rate produced by intravenous clonidine , 5 to 20 micrograms/kg , was inhibited or reversed by nalozone , 0.2 to 2 mg/kg .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}, {"text": "clonidine", "type": "Chemical"}, {"text": "nalozone", "type": "Chemical"}]}

Example input:
Sentence: Glucocorticoid-induced hypertension ( GC-HT ) in the rat is associated with nitric oxide-redox imbalance .

Example answer:
{"entities": [{"text": "hypertension", "type": "Disease"}, {"text": "nitric", "type": "Chemical"}]}

Example input:
Sentence: Differential modulation by estrogen of alpha2-adrenergic and I1-imidazoline receptor-mediated hypotension in female rats .

Example answer:
{"entities": [{"text": "estrogen", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Chronic hyperprolactinemia induced by the dopamine antagonist sulpiride caused a 40 % reduction LH pulse frequency in ovariectomized rats , but only in the presence of chronic low levels of estradiol .

Example answer:
{"entities": [{"text": "hyperprolactinemia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "sulpiride", "type": "Chemical"}, {"text": "estradiol", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Bilateral infusions of neurotensin into the globus pallidus reversed haloperidol-induced parkinsonian catalepsy in rats .

Example answer:
{"entities": [{"text": "neurotensin", "type": "Chemical"}, {"text": "haloperidol-induced", "type": "Chemical"}, {"text": "parkinsonian catalepsy", "type": "Disease"}]}

Example input:
Sentence: In control rats , intravenous bromocriptine ( 150 microg/kg ) induced significant hypotension and tachycardia .

Example answer:
{"entities": [{"text": "bromocriptine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Input:
Sentence: Glibenclamide-sensitive hypotension produced by helodermin assessed in the rat .

## Item bc5cdr:test:1865
Example input:
Sentence: RESULTS : Compared to controls , aortic regurgitation ( OR : 3.1 ; 95 % IC : 1.1-8.8 ) and mitral regurgitation ( OR : 10.7 ; 95 % IC : 2.1-53 ) were more frequent in PD patients ( tricuspid : NS ) .

Example answer:
{"entities": [{"text": "aortic regurgitation", "type": "Disease"}, {"text": "mitral regurgitation", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: Echocardiographic data from the experimental group of 21 patients ( mean age 16 +/- 5 years ) treated from 1.6 to 14.3 years ( median 5.3 ) before this study with 27 to 532 mg/m2 of doxorubicin ( mean 196 ) were compared with echocardiographic data from 12 normal age-matched control subjects .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "Chemical"}]}

Example input:
Sentence: Among the 5 patients with white matter abnormalities , 4 patients ( 80.0 % ) showed higher than normal ADC values on initial MR images , and all showed complete resolution on follow-up images .

Example answer:
{"entities": [{"text": "white matter abnormalities", "type": "Disease"}]}

Example input:
Sentence: Her medical history included coronary artery disease with previous myocardial infarctions , hypertension , and diabetes mellitus .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "myocardial infarctions", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "diabetes mellitus", "type": "Disease"}]}

Example input:
Sentence: The remaining 1 patient ( 20.0 % ) showed lower than normal ADC value and showed incomplete resolution with cortical laminar necrosis .

Example answer:
{"entities": [{"text": "cortical laminar necrosis", "type": "Disease"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: One patient had complete response , seven had stable disease , none had partial response and five had progressive disease .

Example answer:
{"entities": []}

Example input:
Sentence: Subjects were 1210 inpatients with New York Heart Association ( NYHA ) functional class II and III .

Example answer:
{"entities": []}

Example input:
Sentence: In the pre-treatment evaluation , signs of cardiovascular disease were found in 33 patients ( 43 % ) .

Example answer:
{"entities": [{"text": "cardiovascular disease", "type": "Disease"}]}

Example input:
Sentence: The high image quality suggests that high contrast images can be obtained in humans and the 96 h stability makes it an ideal agent to detect , in patients , early cardiac infarction .

Example answer:
{"entities": [{"text": "cardiac infarction", "type": "Disease"}]}

Input:
Sentence: SUBJECTS : 10 patients with stable angina , angiographically proven coronary artery disease , and normal left ventricular function .

## Item bc5cdr:test:1526
Example input:
Sentence: Using puromycin aminonucleoside nephrosis ( PAN ) rats , we studied early ultrastructural and permeability changes in relation to the expression of the podocyte-associated molecules nephrin , a-actinin , dendrin , and plekhh2 , the last two of which were only recently discovered in podocytes .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: HP failed to accentuante progression of renal failure and in fact tended to increase GFR and decrease plasma creatinine levels in lithium pretreated rats .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: Patients who developed renal insufficiency had lower baseline body weight and higher baseline serum creatinine , required higher doses of loop diuretics , and were more likely to be treated with thiazide diuretics than controls .

Example answer:
{"entities": [{"text": "renal insufficiency", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "thiazide", "type": "Chemical"}]}

Example input:
Sentence: Renal papillary necrosis ( RPN ) and a decreased urinary concentrating ability developed during continuous long-term treatment with aspirin and paracetamol in female Fischer 344 rats .

Example answer:
{"entities": [{"text": "Renal papillary necrosis", "type": "Disease"}, {"text": "RPN", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: Rats with lithium-induced nephropathy were subjected to high protein ( HP ) feeding , uninephrectomy ( NX ) or a combination of these , in an attempt to induce glomerular hyperfiltration and further progression of renal failure .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: Reactive oxygen species have been implicated in the pathogenesis of acute puromycin aminonucleoside ( PAN ) -induced nephropathy , with antioxidants significantly reducing the proteinuria .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: HS diet for 4 wk caused a progressive increase in BP , protein and albumin excretion , and glomerular sclerosis in male DS rats , which were attenuated by castration .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: Rats were treated with a single IV injection of puromycin aminonucleoside , ( PAN , 7.5 mg/kg ) and 24 hour urine samples were obtained prior to sacrifice on days 3,5,7,10,17,27,41 ( N = 5-10 per group ) .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Input:
Sentence: Therefore , we examined whether recombinant human ( rh ) IGF-I is a safer alternative for the treatment of growth failure in rats with chronic PAN nephropathy .

## Item bc5cdr:test:1750
Example input:
Sentence: Recurrent seizures were treated with diazepam and broad complex tachycardia was successfully treated with adenosine .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "diazepam", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "adenosine", "type": "Chemical"}]}

Example input:
Sentence: Reports of persistent paralysis after the discontinuance of these drugs have most often involved aminosteroid-based NMBAs such as vecuronium bromide , especially when used in conjunction with corticosteroids .

Example answer:
{"entities": [{"text": "paralysis", "type": "Disease"}, {"text": "vecuronium bromide", "type": "Chemical"}]}

Example input:
Sentence: The present study was designed to evaluate two endogenous and one synthetic neuroactive steroid that positively modulate the gamma-aminobutyric acid ( GABA ( A ) ) receptor against the increase in sensitivity to the convulsant effects of cocaine engendered by repeated cocaine administration ( seizure kindling ) .

Example answer:
{"entities": [{"text": "steroid", "type": "Chemical"}, {"text": "gamma-aminobutyric acid", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: RATIONALE : gamma-Vinyl GABA ( GVG ) irreversibly inhibits GABA-transaminase .

Example answer:
{"entities": [{"text": "gamma-Vinyl GABA", "type": "Chemical"}, {"text": "GVG", "type": "Chemical"}, {"text": "GABA-transaminase", "type": "Chemical"}]}

Example input:
Sentence: The effects of oral doses of diazepam ( single dose of 10 mg and a median dose of 30 mg/day for 2 weeks ) and propranolol ( single dose of 80 mg and a median dose of 240 mg/day for 2 weeks ) on psychological performance of patients with panic disorders and agoraphobia were investigated in a double-blind , randomized and crossover design .

Example answer:
{"entities": [{"text": "diazepam", "type": "Chemical"}, {"text": "propranolol", "type": "Chemical"}, {"text": "panic disorders", "type": "Disease"}, {"text": "agoraphobia", "type": "Disease"}]}

Example input:
Sentence: In conclusion , CPA , diazepam and 2PAM in combination with atropine prevented the occurrence of serious signs of poisoning and thus reduced the toxicity of DFP in rat .

Example answer:
{"entities": [{"text": "CPA", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "atropine", "type": "Chemical"}, {"text": "poisoning", "type": "Disease"}, {"text": "toxicity", "type": "Disease"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: Rizatriptan was also superior to ergotamine/caffeine in the proportions of patients with no nausea , vomiting , phonophobia or photophobia and for patients with normal function 2 h after drug intake ( p < or = 0.001 ) .

Example answer:
{"entities": [{"text": "Rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}, {"text": "nausea", "type": "Disease"}, {"text": "vomiting", "type": "Disease"}, {"text": "phonophobia", "type": "Disease"}, {"text": "photophobia", "type": "Disease"}]}

Example input:
Sentence: These episodes reversed after the administration of diazepam 1 mg intravenously .

Example answer:
{"entities": [{"text": "diazepam", "type": "Chemical"}]}

Example input:
Sentence: Diazepam- , scopolamine- and ageing-induced amnesia served as the interoceptive behavioral models .

Example answer:
{"entities": [{"text": "Diazepam-", "type": "Chemical"}, {"text": "scopolamine-", "type": "Chemical"}, {"text": "amnesia", "type": "Disease"}]}

Example input:
Sentence: Results presented here show that the differential sensitivities of BS and BR lines to beta-CCM can be extended to diazepam , picrotoxin , and pentylenetetrazol , suggesting a genetic selection of a general sensitivity and resistance to several ligands of the GABA ( A ) receptor .

Example answer:
{"entities": [{"text": "beta-CCM", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "pentylenetetrazol", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Input:
Sentence: A relative gamma-aminobutyric acid-ergic deficiency might occur because diazepam , a gamma-aminobutyric acid-mimetic agent , was strikingly effective .

## Item bc5cdr:test:1905
Example input:
Sentence: CNS complications included posterior reversible leukoencephalopathy syndrome ( n = 10 ) , stroke ( n = 5 ) , temporal lobe epilepsy ( n = 2 ) , high-dose methotrexate toxicity ( n = 2 ) , syndrome of inappropriate antidiuretic hormone secretion ( n = 1 ) , and other unclassified events ( n = 7 ) .

Example answer:
{"entities": [{"text": "leukoencephalopathy", "type": "Disease"}, {"text": "stroke", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "inappropriate antidiuretic hormone secretion", "type": "Disease"}]}

Example input:
Sentence: Outcomes included venous thromboembolism , cataracts , gallbladder disease , and endometrial hyperplasia or cancer .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "cataracts", "type": "Disease"}, {"text": "gallbladder disease", "type": "Disease"}]}

Example input:
Sentence: The most common manifestation , observed in 15 further cases , was isolated optic atrophy .

Example answer:
{"entities": [{"text": "optic atrophy", "type": "Disease"}]}

Example input:
Sentence: Development of ocular myasthenia during pegylated interferon and ribavirin treatment for chronic hepatitis C. A 63-year-old male experienced sudden diplopia after 9 weeks of administration of pegylated interferon ( IFN ) alpha-2b and ribavirin for chronic hepatitis C ( CHC ) .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated interferon", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "chronic hepatitis", "type": "Disease"}, {"text": "diplopia", "type": "Disease"}, {"text": "pegylated interferon ( IFN ) alpha-2b", "type": "Chemical"}, {"text": "chronic hepatitis C", "type": "Disease"}, {"text": "CHC", "type": "Disease"}]}

Example input:
Sentence: A delayed complication in nine patients has been unilateral loss of vision secondary to a retinal vasculitis .

Example answer:
{"entities": [{"text": "loss of vision", "type": "Disease"}, {"text": "retinal vasculitis", "type": "Disease"}]}

Example input:
Sentence: In the remaining cases , a combination of myelopathy , visual disturbance , and peripheral neuropathy was the most common manifestation .

Example answer:
{"entities": [{"text": "myelopathy", "type": "Disease"}, {"text": "visual disturbance", "type": "Disease"}, {"text": "peripheral neuropathy", "type": "Disease"}]}

Example input:
Sentence: In this report we describe the case of a 37-year-old white woman with Ebstein 's anomaly , who developed a rare syndrome called platypnea-orthodeoxia , characterized by massive right-to-left interatrial shunting with transient profound hypoxia and cyanosis .

Example answer:
{"entities": [{"text": "Ebstein 's anomaly", "type": "Disease"}, {"text": "platypnea-orthodeoxia", "type": "Disease"}, {"text": "hypoxia", "type": "Disease"}, {"text": "cyanosis", "type": "Disease"}]}

Example input:
Sentence: RESULT ( S ) : A 36-year-old Chinese woman developed central retinal vein occlusion after eight courses of CC .

Example answer:
{"entities": [{"text": "retinal vein occlusion", "type": "Disease"}, {"text": "CC", "type": "Chemical"}]}

Example input:
Sentence: The patient 's ophthalmological symptoms improved rapidly 3 weeks after discontinuation of pegylated IFN alpha-2b and ribavirin .

Example answer:
{"entities": [{"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: Finally , 6 weeks later , diffuse chorioretinal atrophy with optic atrophy occurred and the vision in his left eye was lost .

Example answer:
{"entities": [{"text": "chorioretinal atrophy", "type": "Disease"}, {"text": "optic atrophy", "type": "Disease"}]}

Input:
Sentence: RESULTS : The patient had episodic deterioration of vision in both eyes , with clinical features resembling ischemic optic neuropathies .

## Item bc5cdr:test:2110
Example input:
Sentence: The actual frequencies deafened were determined by the loss of tone-burst elicited auditory brainstem responses .

Example answer:
{"entities": []}

Example input:
Sentence: Twenty-two patients in the affected group had abnormal audiograms with deficits mostly in the high frequency range of 4,000 to 8,000 Hz and in the hearing threshold levels of 30 to 100 decibels .

Example answer:
{"entities": [{"text": "abnormal audiograms with deficits mostly in the high frequency range of 4,000 to 8,000 Hz", "type": "Disease"}]}

Example input:
Sentence: METHODS : This study was undertaken as part of neonatal screening for hearing impairment and involved both ears of 200 newborns .

Example answer:
{"entities": [{"text": "hearing impairment", "type": "Disease"}]}

Example input:
Sentence: The objective of this study was to determine the effects of maternal smoking on transient evoked otoacoustic emissions ( TEOAEs ) of healthy neonates .

Example answer:
{"entities": [{"text": "smoking", "type": "Chemical"}]}

Example input:
Sentence: Does smoking during pregnancy affect the amplitudes of transient evoked otoacoustic emissions in newborns ?

Example answer:
{"entities": [{"text": "smoking", "type": "Chemical"}]}

Example input:
Sentence: Brainstem auditory evoked potentials ( BAEPs ) were routinely used to monitor cochlear nerve function during these operations .

Example answer:
{"entities": []}

Example input:
Sentence: Among 547 preterm infants of < or = 34 weeks gestation born between 1987 and 1991 , 8 children ( 1.46 % ) developed severe progressive and bilateral sensorineural hearing loss .

Example answer:
{"entities": [{"text": "sensorineural hearing loss", "type": "Disease"}]}

Example input:
Sentence: Beginning at 8 days of age , body movement and hearing were examined for 6 and up to 17 weeks , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : In exposed neonates , TEOAEs mean response ( across frequency ) and mean amplitude at 4000Hz was significantly lower than in non-exposed neonates .

Example answer:
{"entities": []}

Example input:
Sentence: Abnormal movements and deafness occurred only in rats treated during the preweaning period ; within this period the greatest sensitivities for these abnormalities occurred from 2 to 11-17 and 5 to 11 days of age , respectively , indicating that the cochlea is more sensitive to streptomycin than the site ( vestibular or central ) responsible for the dyskinesias .

Example answer:
{"entities": [{"text": "Abnormal movements", "type": "Disease"}, {"text": "deafness", "type": "Disease"}, {"text": "streptomycin", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}]}

Input:
Sentence: Auditory thresholds were tested by evoked auditory brain stem responses at 1 month after birth .

## Item bc5cdr:test:1536
Example input:
Sentence: In this model of chronic renal failure the decline in GFR is not accompanied by a corresponding fall in effective renal plasma flow , which may be the functional expression of the formation of nonfiltrating atubular glomeruli .

Example answer:
{"entities": [{"text": "chronic renal failure", "type": "Disease"}]}

Example input:
Sentence: In conclusion , reductions in creatinine clearance and renal amphotericin B accumulation after chronic amphotericin B administration were enhanced by salt depletion and attenuated by sodium loading in rats .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "amphotericin B", "type": "Chemical"}, {"text": "sodium", "type": "Chemical"}]}

Example input:
Sentence: It could be inferred that gum Arabic treatment has induced a modest amelioration of some of the histological and biochemical indices of GM nephrotoxicity .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: The results indicated that concomitant treatment with gum Arabic and GM significantly increased creatinine and urea by about 183 and 239 % , respectively ( compared to 432 and 346 % , respectively , in rats treated with cellulose and GM ) , and decreased that of cortical GSH by 21 % ( compared to 27 % in the cellulose plus GM group ) The GM-induced proximal tubular necrosis appeared to be slightly less severe in rats given GM together with gum Arabic than in those given GM and cellulose .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}, {"text": "urea", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "GM-induced", "type": "Chemical"}, {"text": "tubular necrosis", "type": "Disease"}]}

Example input:
Sentence: Renal papillary necrosis ( RPN ) and a decreased urinary concentrating ability developed during continuous long-term treatment with aspirin and paracetamol in female Fischer 344 rats .

Example answer:
{"entities": [{"text": "Renal papillary necrosis", "type": "Disease"}, {"text": "RPN", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: Reduction in GFR was associated with the development of glomerular sclerosis in both treated and untreated rats .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: HS diet for 4 wk caused a progressive increase in BP , protein and albumin excretion , and glomerular sclerosis in male DS rats , which were attenuated by castration .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: During the course of nephrotic syndrome , serum urea concentrations increased significantly faster in sgk1 ( -/- ) mice than in sgk1 ( +/+ ) mice leading to uremia and a reduced median survival in sgk1 ( -/- ) mice ( 29 vs. 40 days in sgk1 ( +/+ ) mice ) .

Example answer:
{"entities": [{"text": "nephrotic syndrome", "type": "Disease"}, {"text": "urea", "type": "Chemical"}, {"text": "uremia", "type": "Disease"}]}

Example input:
Sentence: HP failed to accentuante progression of renal failure and in fact tended to increase GFR and decrease plasma creatinine levels in lithium pretreated rats .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}]}

Input:
Sentence: We conclude that : 1 ) administration of rhIGF-I improves growth and GFR in rats with chronic PAN nephropathy and 2 ) unlike rhGH , long-term use of rhIGF-I does not worsen renal functional and structural injury in this disease model .

## Item bc5cdr:test:1561
Example input:
Sentence: In this study , cancer patients who have solid and hematological malignancies with chronic HBV infection received the antiviral agent lamivudine prior and during CT compared with historical control group who did not receive lamivudine .

Example answer:
{"entities": [{"text": "cancer", "type": "Disease"}, {"text": "hematological malignancies", "type": "Disease"}, {"text": "HBV infection", "type": "Disease"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: This was an exploratory study to investigate lamivudine-resistant hepatitis B virus ( HBV ) strains in selected lamivudine-na ve HBV carriers with and without human immunodeficiency virus ( HIV ) co-infection in South African patients .

Example answer:
{"entities": [{"text": "lamivudine-resistant", "type": "Chemical"}, {"text": "hepatitis B", "type": "Disease"}, {"text": "lamivudine-na", "type": "Chemical"}, {"text": "human immunodeficiency virus ( HIV ) co-infection", "type": "Disease"}]}

Example input:
Sentence: Mutations associated with lamivudine-resistance in therapy-na ve hepatitis B virus ( HBV ) infected patients with and without HIV co-infection : implications for antiretroviral therapy in HBV and HIV co-infected South African patients .

Example answer:
{"entities": [{"text": "lamivudine-resistance", "type": "Chemical"}, {"text": "hepatitis B virus ( HBV ) infected", "type": "Disease"}, {"text": "HIV co-infection", "type": "Disease"}]}

Example input:
Sentence: HBV lamivudine-resistant strains were detected in 3 of 15 mono-infected chronic hepatitis B patients and 10 of 20 HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "lamivudine-resistant", "type": "Chemical"}, {"text": "hepatitis B", "type": "Disease"}]}

Example input:
Sentence: Prophylactic administration of lamivudine in patients who required immunosuppressive therapy seems to be safe , well tolerated and effective in preventing HBV reactivation .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: The objectives were to assess the efficacy of lamivudine in reducing the incidence of HBV reactivation , and diminishing morbidity and mortality during CT. Two groups were compared in this study .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: Our study suggests that prophylactic lamivudine significantly decreases the incidence of HBV reactivation and overall morbidity in cancer patients during and after immunosuppressive therapy .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: The objective of this study was to report our experience concerning the effectiveness of the prophylactic administration of lamivudine in hepatitis B virus surface antigen ( HBs Ag ) positive patients with rheumatologic disease .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}, {"text": "hepatitis B virus surface antigen", "type": "Chemical"}, {"text": "HBs Ag", "type": "Chemical"}, {"text": "rheumatologic disease", "type": "Disease"}]}

Example input:
Sentence: Lamivudine was added because of de nova hepatitis B infection during her follow-up .

Example answer:
{"entities": [{"text": "Lamivudine", "type": "Chemical"}, {"text": "hepatitis B infection", "type": "Disease"}]}

Example input:
Sentence: Lamivudine for the prevention of hepatitis B virus reactivation in hepatitis-B surface antigen ( HBSAG ) seropositive cancer patients undergoing cytotoxic chemotherapy .

Example answer:
{"entities": [{"text": "Lamivudine", "type": "Chemical"}, {"text": "hepatitis B", "type": "Disease"}, {"text": "hepatitis-B surface antigen", "type": "Chemical"}, {"text": "HBSAG", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Input:
Sentence: Lamivudine is a novel 2',3'-dideoxy cytosine analogue that has potent inhibitory effects on hepatitis B virus replication in vitro and in vivo .

## Item bc5cdr:test:1882
Example input:
Sentence: Phenylpropanolamine ( PPA ) , a synthetic sympathomimetic that is structurally similar to amphetamine , is available over the counter in anorectics , nasal congestants , and cold preparations .

Example answer:
{"entities": [{"text": "Phenylpropanolamine", "type": "Chemical"}, {"text": "PPA", "type": "Chemical"}, {"text": "amphetamine", "type": "Chemical"}]}

Example input:
Sentence: METHODS : We present the first case report of a woman with hyperthyroidism treated with propylthiouracil in whom a syndrome of pericarditis , fever , and glomerulonephritis developed .

Example answer:
{"entities": [{"text": "hyperthyroidism", "type": "Disease"}, {"text": "propylthiouracil", "type": "Chemical"}, {"text": "pericarditis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "glomerulonephritis", "type": "Disease"}]}

Example input:
Sentence: High incidence of primary pulmonary hypertension associated with appetite suppressants in Belgium .

Example answer:
{"entities": [{"text": "primary pulmonary hypertension", "type": "Disease"}, {"text": "appetite suppressants", "type": "Chemical"}]}

Example input:
Sentence: He was hospitalized for a myocardial infarction with pulmonary edema , treated with high-dose diuretics .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "pulmonary edema", "type": "Disease"}]}

Example input:
Sentence: This shunt of blood via a patent foramen ovale occurred in the presence of a normal pulmonary artery pressure , and was probably precipitated by a propafenone overdose .

Example answer:
{"entities": [{"text": "patent foramen ovale", "type": "Disease"}, {"text": "propafenone", "type": "Chemical"}, {"text": "overdose", "type": "Disease"}]}

Example input:
Sentence: Pulmonary hypertension developed after administration of a somatostatin analogue , octreotide , to enhance resolution of the fistula .

Example answer:
{"entities": [{"text": "Pulmonary hypertension", "type": "Disease"}, {"text": "octreotide", "type": "Chemical"}, {"text": "fistula", "type": "Disease"}]}

Example input:
Sentence: A policy of unrestricted prescription of appetite suppressants may lead to a high incidence of associated primary pulmonary hypertension .

Example answer:
{"entities": [{"text": "appetite suppressants", "type": "Chemical"}, {"text": "primary pulmonary hypertension", "type": "Disease"}]}

Example input:
Sentence: Thirty-five patients with primary pulmonary hypertension and 85 matched controls were recruited over 32 months ( 1992-1994 ) in Belgium .

Example answer:
{"entities": [{"text": "primary pulmonary hypertension", "type": "Disease"}]}

Example input:
Sentence: In 8 patients the diagnosis of primary pulmonary hypertension was uncertain , 5 of them had taken appetite suppressants .

Example answer:
{"entities": [{"text": "primary pulmonary hypertension", "type": "Disease"}, {"text": "appetite suppressants", "type": "Chemical"}]}

Example input:
Sentence: Primary pulmonary hypertension is a rare , progressive and incurable disease , which has been associated with the intake of appetite suppressant drugs .

Example answer:
{"entities": [{"text": "Primary pulmonary hypertension", "type": "Disease"}, {"text": "appetite suppressant", "type": "Chemical"}]}

Input:
Sentence: Patients with no identifiable cause of pulmonary hypertension were classed as PPH .

## Item bc5cdr:test:2134
Example input:
Sentence: A complete responder had relapse-free survival up to 17 months .

Example answer:
{"entities": []}

Example input:
Sentence: The overall objective response rate was 7.6 % .

Example answer:
{"entities": []}

Example input:
Sentence: The overall response rate was 26 % ( 95 % confidence interval , 15-41 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: In the nine responders , median duration of chemotherapy response from the time of operation was 25 weeks ( range 12 to more than 91 weeks ) .

Example answer:
{"entities": []}

Example input:
Sentence: The overall response rate is 72 % .

Example answer:
{"entities": []}

Example input:
Sentence: The median time to progression was 16 weeks and the 1-year survival rate was 33 % .

Example answer:
{"entities": []}

Example input:
Sentence: After a median follow-up of 22 months , the median progression free survival rate was 7 months , and the median survival time was 16 months .

Example answer:
{"entities": []}

Example input:
Sentence: Seventeen of these had a response or were stable for a median of 20 weeks ( range 6 to more than 66 weeks ) .

Example answer:
{"entities": []}

Example input:
Sentence: The median duration of survival in the 12 patients was 54 weeks ( range 21 to more than 156 weeks ) , with an 18-month survival rate of 42 % .

Example answer:
{"entities": []}

Example input:
Sentence: The median duration of response was 21 weeks ( range , 17 to 28 ) .

Example answer:
{"entities": []}

Input:
Sentence: The overall response rate was 38 % , the median time to response was 10 weeks , the median duration of response was 26 weeks , and the median survival was 37 weeks .

## Item bc5cdr:test:2049
Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: End-systolic left ventricular posterior wall dimension at baseline for the doxorubicin-treated group was 11 +/- 1.9 mm versus 13.1 +/- 1.5 mm for control subjects ( p less than 0.01 ) .

Example answer:
{"entities": [{"text": "doxorubicin-treated", "type": "Chemical"}]}

Example input:
Sentence: After 35 days in the TG + HAART cohort , left ventricular mass increased 160 % by echocardiography .

Example answer:
{"entities": []}

Example input:
Sentence: In each group , SNP infusion resulted in an initial decrease in blood pressure from 86 torr and 83 torr , respectively , to 48 torr .

Example answer:
{"entities": [{"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: Decreases in systolic blood pressure were statistically , but not clinically , significant .

Example answer:
{"entities": [{"text": "Decreases in systolic blood pressure", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Compared to controls , aortic regurgitation ( OR : 3.1 ; 95 % IC : 1.1-8.8 ) and mitral regurgitation ( OR : 10.7 ; 95 % IC : 2.1-53 ) were more frequent in PD patients ( tricuspid : NS ) .

Example answer:
{"entities": [{"text": "aortic regurgitation", "type": "Disease"}, {"text": "mitral regurgitation", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: End-diastolic ( ED ) and end-systolic ( ES ) LV diameters/BW significantly increased , whereas LV FS was decreased after 9 weeks in the DOX group ( p < 0.001 ) .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: These rats also showed declines in left ventricular systolic pressure , maximum and minimum rate of developed left ventricular pressure , and elevation of left ventricular end-diastolic pressure and ST-segment .

Example answer:
{"entities": []}

Example input:
Sentence: The most important findings were that compared with values in control subjects , end-systolic left ventricular posterior wall dimension and percent of left ventricular posterior wall thickening in doxorubicin-treated patients were decreased at baseline study and these findings were more clearly delineated with dobutamine stimulation .

Example answer:
{"entities": [{"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}]}

Example input:
Sentence: Left ventricular filling pressure decreased from 19 +/- 2 to 11 +/- 2 mm Hg ( P less than 0.001 ) .

Example answer:
{"entities": []}

Input:
Sentence: Decreased left ventricular systolic function was demonstrated in 5 ( 14 % ) patients , but in none of the controls ( p = 0.055 ) .

## Item bc5cdr:test:1799
Example input:
Sentence: Pretreatment of mice with alpha-methyltyrosine ( 20 mg/kg i.p. , one hour ) , an inhibitor of tyrosine hydroxylase , significantly decreased the activity-increasing effects of morphine .

Example answer:
{"entities": [{"text": "alpha-methyltyrosine", "type": "Chemical"}, {"text": "tyrosine", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: Rats treated for 11 days with morphine and withdrawn for 36-40 h showed differences in the development of tolerance : about half of the animals showed a rigidity after the test dose of morphine that was not significantly less than in the controls and were akinetic ( A group ) .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "rigidity", "type": "Disease"}, {"text": "akinetic", "type": "Disease"}]}

Example input:
Sentence: The present study was designed to study the effect of histamine H ( 3 ) -receptor ligands on neuroleptic-induced catalepsy , apomorphine-induced climbing behavior and amphetamine-induced locomotor activities in mice .

Example answer:
{"entities": [{"text": "histamine", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "apomorphine-induced", "type": "Chemical"}, {"text": "amphetamine-induced", "type": "Chemical"}]}

Example input:
Sentence: TRI given repeatedly to rats increases the locomotor hyperactivity induced by d-amphetamine , quinpirole and ( + ) -7-hydroxy-dipropyloaminotetralin ( dopamine D2 and D3 effects ) .

Example answer:
{"entities": [{"text": "TRI", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "d-amphetamine", "type": "Chemical"}, {"text": "quinpirole", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: The morphine-induced hyperactivity was potentiated by scopolamine and attenuated by physostigmine .

Example answer:
{"entities": [{"text": "morphine-induced", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "physostigmine", "type": "Chemical"}]}

Example input:
Sentence: Antinociceptive effect of morphine was reduced in chronically treated rats ( 39+/-10 vs. 18+/-5 au ) while the combination-induced antinociception was remained similar as an acute treatment ( 298+/-7 vs. 280+/-17 au ) .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: Nicotine ( 1.0 mg/kg ) caused a significant increase in locomotor activity in rats that were habituated to the test environment , but had only a weak and delayed stimulant action in rats that were unfamiliar with the test environment .

Example answer:
{"entities": [{"text": "Nicotine", "type": "Chemical"}, {"text": "increase in locomotor activity", "type": "Disease"}]}

Example input:
Sentence: The effect of humoral modulators on the morphine-induced increase in locomotor activity of mice was studied .

Example answer:
{"entities": [{"text": "morphine-induced", "type": "Chemical"}, {"text": "increase in locomotor activity", "type": "Disease"}]}

Example input:
Sentence: The results showed that rats treated with Morphine/Rg1 decreased escape latency and increased the time spent in platform quadrant and entering frequency .

Example answer:
{"entities": [{"text": "Morphine/Rg1", "type": "Chemical"}]}

Example input:
Sentence: The subcutaneous administration of 10 mg/kg of morphine-HC1 produced a marked increase in locomotor activity in mice .

Example answer:
{"entities": [{"text": "morphine-HC1", "type": "Chemical"}, {"text": "increase in locomotor activity", "type": "Disease"}]}

Input:
Sentence: The effects of quinine and 4-aminopyridine on conditioned place preference and changes in motor activity induced by morphine in rats .

## Item bc5cdr:test:2144
Example input:
Sentence: The excess event rate was 1.8 per 1,000 woman-years ( 95 % CI -0.5-4.1 ) , and the number needed to treat to cause 1 event was 170 ( 95 % CI 100-582 ) over 3.3 years .

Example answer:
{"entities": []}

Example input:
Sentence: From January 1986 to January 2009 , 1223 consecutive ALF patients were evaluated : ATT alone was the cause in 70 ( 5.7 % ) patients .

Example answer:
{"entities": [{"text": "ALF", "type": "Disease"}]}

Example input:
Sentence: Seventy patients developed major opportunistic infections whilst on therapy ; this was the first AIDS diagnosis in 17 .

Example answer:
{"entities": [{"text": "opportunistic infections", "type": "Disease"}, {"text": "AIDS", "type": "Disease"}]}

Example input:
Sentence: The overall response rate ( World Health Organization [ WHO ] criteria ) was 15 % ( CR , 2 % ; PR 13 % ; 95 % CI , 6 % to 29 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: The mean age of patients in the 16 probable cases was 57.9 , with hepatotoxicity being more common in women .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: Delirium was diagnosed in 14 ( 10.1 % incidence , or 1.48 cases/person-years of exposure ) ; 71.4 % of cases were moderate or severe .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}]}

Example input:
Sentence: Serious adverse events were reported in 11 and 13 patients in the respective groups .

Example answer:
{"entities": []}

Example input:
Sentence: An analysis of the 75 cases that had been adequately followed up suggested that 16 , including three deaths , were probably related to treatment with the drug .

Example answer:
{"entities": [{"text": "deaths", "type": "Disease"}]}

Example input:
Sentence: In the initial 6 months since it 's introduction , 12 overdose cases have been reported to The National Poisons Information Centre .

Example answer:
{"entities": [{"text": "overdose", "type": "Disease"}]}

Example input:
Sentence: Over the period 1993-1996 , 551 cases of VTE were identified in Germany and the UK along with 2066 controls .

Example answer:
{"entities": [{"text": "VTE", "type": "Disease"}]}

Input:
Sentence: The WHO reported 82 cases .

## Item bc5cdr:test:1727
Example input:
Sentence: The use and toxicity of didanosine ( ddI ) in HIV antibody-positive individuals intolerant to zidovudine ( AZT ) One hundred and fifty-one patients intolerant to zidovudine ( AZT ) received didanosine ( ddI ) to a maximum dose of 12.5 mg/kg/day .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "didanosine", "type": "Chemical"}, {"text": "ddI", "type": "Chemical"}, {"text": "HIV antibody-positive", "type": "Disease"}, {"text": "zidovudine", "type": "Chemical"}, {"text": "AZT", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Sirolimus is the latest immunosuppressive agent used to prevent rejection , and may have less nephrotoxicity than calcineurin inhibitor ( CNI ) -based regimens .

Example answer:
{"entities": [{"text": "Sirolimus", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}]}

Example input:
Sentence: Patients who developed renal insufficiency had lower baseline body weight and higher baseline serum creatinine , required higher doses of loop diuretics , and were more likely to be treated with thiazide diuretics than controls .

Example answer:
{"entities": [{"text": "renal insufficiency", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "thiazide", "type": "Chemical"}]}

Example input:
Sentence: METHODS AND RESULTS : The present study is a multicenter , randomized , double-blind comparison of iopamidol and iodixanol in patients with chronic kidney disease ( estimated glomerular filtration rate , 20 to 59 mL/min ) who underwent cardiac angiography or percutaneous coronary interventions .

Example answer:
{"entities": [{"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}, {"text": "chronic kidney disease", "type": "Disease"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : No direct comparisons exist of the renal tolerability of the low-osmolality contrast medium iopamidol with that of the iso-osmolality contrast medium iodixanol in high-risk patients .

Example answer:
{"entities": [{"text": "contrast medium", "type": "Chemical"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}]}

Example input:
Sentence: Seventy-five human immunodeficiency virus ( HIV ) -infected patients with CD4+ cell counts < 500/mm3 were randomized to receive either ZDV ( 500 mg daily ) alone ( group I , n = 38 ) or in combination with folinic acid ( 15 mg daily ) and intramascular vitamin B12 ( 1000 micrograms monthly ) ( group II , n = 37 ) .

Example answer:
{"entities": [{"text": "human immunodeficiency virus ( HIV ) -infected", "type": "Disease"}, {"text": "ZDV", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}, {"text": "vitamin B12", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : A 72-year-old white man with underlying human immunodeficiency virus , atrial fibrillation , coronary artery disease , and hyperlipidemia presented with generalized pain , fatigue , and dark orange urine for 3 days .

Example answer:
{"entities": [{"text": "human immunodeficiency virus", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "coronary artery disease", "type": "Disease"}, {"text": "hyperlipidemia", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "fatigue", "type": "Disease"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : The rate of contrast-induced nephropathy , defined by multiple end points , is not statistically different after the intraarterial administration of iopamidol or iodixanol to high-risk patients , with or without diabetes mellitus .

Example answer:
{"entities": [{"text": "nephropathy", "type": "Disease"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}, {"text": "diabetes mellitus", "type": "Disease"}]}

Input:
Sentence: contrast material to enable diagnosis of ureteric stones or obstruction in patients with HIV infection who receive indinavir therapy .

## Item bc5cdr:test:1811
Example input:
Sentence: Nuclear factor kappa B ( NFkappaB ) is a sensor of oxidative stress and participates in memory formation that could be involved in drug toxicity and addiction mechanisms .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Bradykinin receptors antagonists and nitric oxide synthase inhibitors in vincristine and streptozotocin induced hyperalgesia in chemotherapy and diabetic neuropathy rat model .

Example answer:
{"entities": [{"text": "Bradykinin", "type": "Chemical"}, {"text": "nitric oxide", "type": "Chemical"}, {"text": "vincristine", "type": "Chemical"}, {"text": "streptozotocin", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "diabetic neuropathy", "type": "Disease"}]}

Example input:
Sentence: Using functional magnetic resonance imaging ( fMRI ) in normal volunteers , we studied the gabapentin-induced modulation of brain activity in response to nociceptive mechanical stimulation of normal skin and capsaicin-induced secondary hyperalgesia .

Example answer:
{"entities": [{"text": "gabapentin-induced", "type": "Chemical"}, {"text": "capsaicin-induced", "type": "Chemical"}, {"text": "secondary hyperalgesia", "type": "Disease"}]}

Example input:
Sentence: 9 ( 2006 ) , 917 ] recently identified the microglial-specific fractalkine receptor ( CX3CR1 ) as an important mediator of MPTP-induced neurodegeneration of DA neurons .

Example answer:
{"entities": [{"text": "MPTP-induced", "type": "Chemical"}, {"text": "neurodegeneration", "type": "Disease"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: Animal and clinical studies have suggested that N-methyl-D-aspartate ( NMDA ) antagonists , such as ketamine , may be effective in improving opioid analgesia in difficult pain syndromes , such as neuropathic pain .

Example answer:
{"entities": [{"text": "N-methyl-D-aspartate", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "ketamine", "type": "Chemical"}, {"text": "pain", "type": "Disease"}, {"text": "neuropathic pain", "type": "Disease"}]}

Example input:
Sentence: Sulpiride induced only SOCS-1 in the medial preoptic area , where GnRH neurons are regulated , but in the arcuate nucleus and choroid plexus , PRL-R , SOCS-3 , and CIS mRNA levels were also induced .

Example answer:
{"entities": [{"text": "Sulpiride", "type": "Chemical"}]}

Example input:
Sentence: The aim of this study was to assess the effects of gabapentin , a drug effective in neuropathic pain patients , on brain processing of nociceptive information in normal and central sensitization states .

Example answer:
{"entities": [{"text": "gabapentin", "type": "Chemical"}, {"text": "neuropathic pain", "type": "Disease"}]}

Example input:
Sentence: In streptozotocin-induced hyperalgesia , inducible NO synthase participates in pronociceptive activity of bradykinin , whereas in vincristine-induced hyperalgesia bradykinin seemed to activate neuronal NO synthase pathway .

Example answer:
{"entities": [{"text": "streptozotocin-induced", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "NO", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}, {"text": "vincristine-induced", "type": "Chemical"}]}

Example input:
Sentence: The alpha3 and beta4 nicotinic acetylcholine receptor subunits are necessary for nicotine-induced seizures and hypolocomotion in mice .

Example answer:
{"entities": [{"text": "acetylcholine", "type": "Chemical"}, {"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "hypolocomotion", "type": "Disease"}]}

Example input:
Sentence: PURPOSE : The influence of an irreversible inhibitor of constitutive NO synthase ( L-NOArg ; 1.0 mg/kg ip ) , a relatively selective inhibitor of inducible NO synthase ( L-NIL ; 1.0 mg/kg ip ) and a relatively specific inhibitor of neuronal NO synthase ( 7-NI ; 0.1 mg/kg ip ) , on antihyperalgesic action of selective antagonists of B2 and B1 receptors : D-Arg- [ Hyp3 , Thi5 , D-Tic7 , Oic8 ] bradykinin ( HOE 140 ; 70 nmol/kg ip ) or des Arg10 HOE 140 ( 70 nmol/kg ip ) respectively , in model of diabetic ( streptozotocin-induced ) and toxic ( vincristine-induced ) neuropathy was investigated .

Example answer:
{"entities": [{"text": "NO", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}, {"text": "HOE 140", "type": "Chemical"}, {"text": "des Arg10 HOE 140", "type": "Chemical"}]}

Input:
Sentence: Nociceptin , also known as orphanin FQ , is an endogenous ligand for the orphan opioid receptor-like receptor 1 ( ORL1 ) and involves in various functions in the central nervous system ( CNS ) .

## Item bc5cdr:test:1986
Example input:
Sentence: Significant declines in simple and sustained attention , working memory , and verbal memory were observed at 1 hour postdose compared to baseline for both age groups with a trend toward return to baseline by 5 hours postdose .

Example answer:
{"entities": []}

Example input:
Sentence: Modafinil was associated with increased daytime sleep latency , as measured by the Multiple Sleep Latency Test , and a nearly significant decrease in subjective daytime sleepiness .

Example answer:
{"entities": [{"text": "Modafinil", "type": "Chemical"}, {"text": "daytime sleepiness", "type": "Disease"}]}

Example input:
Sentence: Use of BZDs/RDs tended to be associated with a reduced ability to walk and shorter night-time sleep during the week prior to admission .

Example answer:
{"entities": [{"text": "BZDs/RDs", "type": "Chemical"}]}

Example input:
Sentence: He complained of pain and visual disturbance in the ipsilateral eye 30 h after the injection .

Example answer:
{"entities": []}

Example input:
Sentence: Long-term use was associated with daytime and night-time symptoms indicative of poorer health and potentially caused by the adverse effects of these drugs .

Example answer:
{"entities": []}

Example input:
Sentence: Finally , 6 weeks later , diffuse chorioretinal atrophy with optic atrophy occurred and the vision in his left eye was lost .

Example answer:
{"entities": [{"text": "chorioretinal atrophy", "type": "Disease"}, {"text": "optic atrophy", "type": "Disease"}]}

Example input:
Sentence: The frequency of visual loss decreased after the concentration of the ethanol diluent was lowered .

Example answer:
{"entities": [{"text": "visual loss", "type": "Disease"}, {"text": "ethanol", "type": "Chemical"}]}

Example input:
Sentence: While postjunctional beta-adrenoceptor-mediated relaxations are reduced , effects by prejunctional inhibitory muscarinic receptors may be increased .

Example answer:
{"entities": []}

Example input:
Sentence: Eight healthy volunteers inhaled nicotine in darkness during a functional magnetic resonance imaging ( fMRI ) experiment ; eye movements were registered using video-oculography .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}]}

Example input:
Sentence: Examinations , including blood pressure , pulse rate , conjunctiva and cornea , intraocular pressure ( IOP ) , pupil diameter , basal tear secretion and margin reflex distance of both upper and lower eyelids , were performed prior to entry and at 1 , 3 , 5 and 7 hours after instillation .

Example answer:
{"entities": []}

Input:
Sentence: CONCLUSIONS : Pupillary dilation may lead to a decrease in vision and daylight driving performance in young people .

## Item bc5cdr:test:2085
Example input:
Sentence: Two separate equimolar doses ( 0.2 and 0.4 mumol ) of either cocaine or BE were injected ventricularly in unanesthetized juvenile rats .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "BE", "type": "Chemical"}]}

Example input:
Sentence: Eleven of the cocaine abusers and none of the controls had ECG evidence of significant myocardial injury defined as myocardial infarction , ischemia , and bundle branch block .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "myocardial injury", "type": "Disease"}, {"text": "myocardial infarction", "type": "Disease"}, {"text": "ischemia", "type": "Disease"}, {"text": "bundle branch block", "type": "Disease"}]}

Example input:
Sentence: The half-life ( t1/2 ) of cocaine is relatively short , but some of the consequences of its use , such as seizures and strokes , can occur hours after exposure .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "strokes", "type": "Disease"}]}

Example input:
Sentence: In particular , the tendency of cocaine to produce chest pain ought to be in the mind of the emergency nurse when faced with a young victim of chest pain who is otherwise at low risk .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "chest pain", "type": "Disease"}]}

Example input:
Sentence: Whereas cocaine-induced seizures were best characterized as brief , generalized , and tonic and resulted in death , those induced by BE were prolonged , often multiple and mixed in type , and rarely resulted in death .

Example answer:
{"entities": [{"text": "cocaine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "death", "type": "Disease"}, {"text": "BE", "type": "Chemical"}]}

Example input:
Sentence: Comparisons between exposed newborns ' subgroups revealed no significant differences .

Example answer:
{"entities": []}

Example input:
Sentence: BACKGROUND : Cocaine is a widely abused psychostimulant that has both rewarding and aversive properties .

Example answer:
{"entities": [{"text": "Cocaine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : Cocaine use predisposed aneurysmal rupture at a significantly earlier age and in much smaller aneurysms .

Example answer:
{"entities": [{"text": "Cocaine", "type": "Chemical"}, {"text": "aneurysmal rupture", "type": "Disease"}, {"text": "aneurysms", "type": "Disease"}]}

Example input:
Sentence: Additionally , levels of cocaine determined in hippocampus and cortex were not different between sensitive and resistant strains .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: A 45-year-old man , an admitted frequent cocaine user , presented to the Emergency Department ( ED ) on two separate occasions with a history of priapism after cocaine use .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "priapism", "type": "Disease"}]}

Input:
Sentence: Infants were categorized into 1 of 2 groups : those exposed to cocaine and those not exposed to cocaine .

## Item bc5cdr:test:2178
Example input:
Sentence: In the present study , we investigated the changes occurring at the protein level in striatal samples obtained from the unilaterally 6-hydroxydopamine-lesion rat model of PD treated with saline , L-DOPA or bromocriptine using two-dimensional difference gel electrophoresis and mass spectrometry ( MS ) .

Example answer:
{"entities": [{"text": "6-hydroxydopamine-lesion", "type": "Chemical"}, {"text": "PD", "type": "Disease"}, {"text": "L-DOPA", "type": "Chemical"}, {"text": "bromocriptine", "type": "Chemical"}]}

Example input:
Sentence: HS diet for 4 wk caused a progressive increase in BP , protein and albumin excretion , and glomerular sclerosis in male DS rats , which were attenuated by castration .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: Renal biopsy revealed severe glomerulonephritis with crescents , electron dense fibrillar deposits and moderate lymphocytic interstitial infiltrate .

Example answer:
{"entities": [{"text": "glomerulonephritis", "type": "Disease"}]}

Example input:
Sentence: In these patients , the magnitude of proteinuria was assessed on morning urine samples by turbidometric measurement or random urine protein : creatinine ratios , an estimate of grams of proteinuria/day .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "proteinuria/day", "type": "Disease"}]}

Example input:
Sentence: Systolic blood pressure ( SBP ) was measured on alternate days using the tail-cuff method .

Example answer:
{"entities": []}

Example input:
Sentence: Renal function was investigated by measuring plasma and urinary electrolytes , glucosuria , proteinuria , aminoaciduria , urinary pH , osmolarity , creatinine clearance , phosphate tubular reabsorption , beta 2 microglobulinuria , and lysozymuria .

Example answer:
{"entities": [{"text": "glucosuria", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "aminoaciduria", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "phosphate", "type": "Chemical"}]}

Example input:
Sentence: Biopsies performed in five patients revealed new pathological changes : One membranoproliferative glomerulopathy and interstitial nephritis .

Example answer:
{"entities": [{"text": "membranoproliferative glomerulopathy", "type": "Disease"}, {"text": "interstitial nephritis", "type": "Disease"}]}

Example input:
Sentence: Morphometric analysis at the ultrastructural level was performed using a computerized image processor .

Example answer:
{"entities": []}

Example input:
Sentence: Systolic blood pressures ( SBP ) and bodyweights were recorded each alternate day .

Example answer:
{"entities": []}

Example input:
Sentence: The morphological analysis of the kidneys included a semi-quantitative scoring system analysing the degree of striped fibrosis , subcapsular fibrosis and the number of basophilic tubules , plus an additional stereological analysis of the total grade of fibrosis in the cortex stained with Sirius Red .

Example answer:
{"entities": [{"text": "fibrosis", "type": "Disease"}]}

Input:
Sentence: At each time point , systolic blood pressure ( BP ) , urinary protein excretion and renal histopathological findings were evaluated , and morphometric image analysis was done .

## Item bc5cdr:test:1430
Example input:
Sentence: Our experience supports the safety of giving AraG as salvage therapy in synchrony with etoposide and cyclophosphamide , although neurological toxicity must be closely monitored .

Example answer:
{"entities": [{"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "neurological toxicity", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : This study establishes a TAA model by periarterial CaCl ( 2 ) exposure in rats , and demonstrates a significant elevation of expression of MMP-2 , MMP-9 , ADAM10 and ADAM17 in the pathogenesis of vascular remodeling .

Example answer:
{"entities": [{"text": "TAA", "type": "Disease"}, {"text": "CaCl ( 2 )", "type": "Chemical"}]}

Example input:
Sentence: The effects of PG-9 ( 3alpha-tropyl 2- ( p-bromophenyl ) propionate ) , the acetylcholine releaser , on memory processes and nerve growth factor ( NGF ) synthesis were evaluated .

Example answer:
{"entities": [{"text": "PG-9", "type": "Chemical"}, {"text": "3alpha-tropyl 2- ( p-bromophenyl ) propionate", "type": "Chemical"}, {"text": "acetylcholine", "type": "Chemical"}]}

Example input:
Sentence: An allergic reaction consisting of angioneurotic edema secondary to continuous infusion 5-fluorouracil occurred in a patient with recurrent carcinoma of the oral cavity , cirrhosis , and cisplatin-induced impaired renal function .

Example answer:
{"entities": [{"text": "allergic reaction", "type": "Disease"}, {"text": "angioneurotic edema", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "carcinoma of the oral cavity", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "impaired renal function", "type": "Disease"}]}

Example input:
Sentence: This data suggests that E2 modifies the expression of CD36 at the level of protein expression in monocyte-derived macrophages resulting in reduced cholesteryl ester accumulation following ritonavir treatment .

Example answer:
{"entities": [{"text": "E2", "type": "Chemical"}, {"text": "cholesteryl ester", "type": "Chemical"}, {"text": "ritonavir", "type": "Chemical"}]}

Example input:
Sentence: When hippocampal ACh was measured during testing for handling-induced convulsions , extracellular ACh was significantly elevated ( 192 % ) in WSP mice , but was nonsignificantly elevated ( 59 % ) in WSR mice .

Example answer:
{"entities": [{"text": "ACh", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Haematological toxicity was greater for the combination than AraG alone , although median time to neutrophil and platelet recovery was consistent with other salvage therapies .

Example answer:
{"entities": [{"text": "Haematological toxicity", "type": "Disease"}, {"text": "AraG", "type": "Chemical"}]}

Example input:
Sentence: From these results , we conclude that ribavirin has an antiviral effect in advanced cases of AHF , and that anemia , the only secondary reaction observed , can be easily managed .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "AHF", "type": "Disease"}, {"text": "anemia", "type": "Disease"}]}

Example input:
Sentence: Based on clinical data , indicating that chloroacetaldehyde ( CAA ) is an important metabolite of oxazaphosphorine cytostatics , an experimental study was carried out in order to elucidate the role of CAA in the development of hemorrhagic cystitis .

Example answer:
{"entities": [{"text": "chloroacetaldehyde", "type": "Chemical"}, {"text": "CAA", "type": "Chemical"}]}

Input:
Sentence: As TNF and PAF are thought to be involved in the development of septic shock and adult respiratory distress syndrome , we hypothesize that high-dose Ara-C may be associated with cytokine release .

## Item bc5cdr:test:2183
Example input:
Sentence: At day 5 , GLEPP1 protein and mRNA were reduced from the normal range ( 265.2 +/- 79.6 x 10 ( 6 ) moles/glomerulus and 100 % ) to 15 % of normal ( 41.8 +/- 4.8 x 10 ( 6 ) moles/glomerulus , p < 0.005 ) .

Example answer:
{"entities": []}

Example input:
Sentence: The amount of daily urinary protein decreased from 15.6 to 2.8 g. Within 14 days of the oral bisphosphonate ( alendronate sodium ) administration , the amount of daily urinary protein increased rapidly up to 12.8 g with acute renal failure .

Example answer:
{"entities": [{"text": "bisphosphonate", "type": "Chemical"}, {"text": "alendronate sodium", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: Proteinuria correlated most strongly with sirolimus therapy when compared to other demographic and clinical variables .

Example answer:
{"entities": [{"text": "Proteinuria", "type": "Disease"}, {"text": "sirolimus", "type": "Chemical"}]}

Example input:
Sentence: Urinary sodium excretion reached signficantly lower values in sgk1 ( +/+ ) mice ( 15 +/- 5 mumol/mg crea ) than in sgk1 ( -/- ) mice ( 35 +/- 5 mumol/mg crea ) and was associated with a significantly higher body weight gain in sgk1 ( +/+ ) compared with sgk1 ( -/- ) mice ( +6.6 +/- 0.7 vs. +4.1 +/- 0.8 g ) .

Example answer:
{"entities": [{"text": "sodium", "type": "Chemical"}, {"text": "weight gain", "type": "Disease"}]}

Example input:
Sentence: Patients without proteinuria had increased renal function ( median 42.5 vs. 64.1 , p = 0.25 ) , whereas patients who developed high-grade proteinuria showed decreased renal function at the end of follow-up ( median 39.6 vs. 29.2 , p = 0.125 ) .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: Massive urinary protein excretion has been observed after conversion from calcineurin inhibitors to mammalian target of rapamycin ( mToR ) inhibitors , especially sirolimus , in renal transplant recipients with chronic allograft nephropathy .

Example answer:
{"entities": [{"text": "rapamycin", "type": "Chemical"}, {"text": "sirolimus", "type": "Chemical"}, {"text": "chronic allograft nephropathy", "type": "Disease"}]}

Example input:
Sentence: Proteinuria increased significantly from a median of 0.13 g/day ( range 0-5.7 ) preswitch to 0.23 g/day ( 0-9.88 ) at 24 months postswitch ( p = 0.0024 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Mean urinary protein of patients who returned to dialysis was 1.26 ( 0.5 to 3.5 ) g/d before and 4.7 ( 3 to 12 ) g/d after conversion ( P = .01 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Proteinuria increased from 0.445 ( 0 to 1.5 ) g/d before conversion to 3.2 g/dL ( 0.2 to 12 ) after conversion ( P = 0.001 ) .

Example answer:
{"entities": [{"text": "Proteinuria", "type": "Disease"}]}

Example input:
Sentence: This occurred in association with an increase in urinary protein content from 1.8 +/- 1 to 99.0 +/- 61 mg/day ( p < 0.001 ) .

Example answer:
{"entities": []}

Input:
Sentence: There was a significant correlation between urinary protein excretion and GSI ( r = 0.808 , p < 0.0001 ) .

## Item bc5cdr:test:1597
Example input:
Sentence: was able to prevent amnesia induced by scopolamine ( 1 mg kg-1 i.p . )

Example answer:
{"entities": []}

Example input:
Sentence: Three hundred fifty-five adult male CSS mice , 58 B6 , and 39 A/J were tested for susceptibility to pilocarpine-induced seizures .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Pretreatment with either VPU ( 50 and 100 mg/kg ) or VPA ( 300 and 600 mg/kg ) completely abolished pilocarpine-evoked increases in extracellular glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-evoked", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: Dissociated learning of rats in the normal state and the state of amnesia produced by pentobarbital ( 15 mg/kg , ip ) was carried out .

Example answer:
{"entities": [{"text": "amnesia", "type": "Disease"}, {"text": "pentobarbital", "type": "Chemical"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Therefore , like VPA , the finding that VPU could drastically reduce pilocarpine-induced increases in glutamate and aspartate should account , at least partly , for its anticonvulsant activity observed in pilocarpine-induced seizure in experimental animals .

Example answer:
{"entities": [{"text": "VPA", "type": "Chemical"}, {"text": "VPU", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Based on the finding that VPU and VPA could protect the animals against pilocarpine-induced seizure it is suggested that the reduction of inhibitory amino acid neurotransmitters was comparatively minor and offset by a pronounced reduction of glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: In the absence of caffeine , acetaminophen ( up to 300 mg/kg ) did not modify the seizures induced by maximal electroshock and did not alter the convulsant dose of pentylenetetrezol in mice ( tests performed by the Anticonvulsant Screening Project of NINCDS ) .

Example answer:
{"entities": [{"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "pentylenetetrezol", "type": "Chemical"}]}

Example input:
Sentence: VPU was more potent than VPA , exhibiting the median effective dose ( ED ( 50 ) ) of 49 mg/kg in protecting rats against pilocarpine-induced seizure whereas the corresponding value for VPA was 322 mg/kg .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Input:
Sentence: Scopolamine ( 10 mg/kg ) and pentobarbital ( 5 mg/kg ) prevented development of pilocarpine-induced behavioral seizure but MK-801 ( 0.5 mg/kg ) did not .

## Item bc5cdr:test:1044
Example input:
Sentence: Three hundred fifty-five adult male CSS mice , 58 B6 , and 39 A/J were tested for susceptibility to pilocarpine-induced seizures .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Similar to rats , systemic pilocarpine injection causes status epilepticus ( SE ) and the eventual development of spontaneous seizures and mossy fiber sprouting in C57BL/6 and CD1 mice , but the physiological correlates of these events have not been identified in mice .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Specifically , WSP mice may have lower sensitivity to cholinergic convulsants compared with WSR because of postsynaptic receptor desensitization brought on by higher activity of cholinergic neurons .

Example answer:
{"entities": [{"text": "convulsants", "type": "Disease"}]}

Example input:
Sentence: In the absence of caffeine , acetaminophen ( up to 300 mg/kg ) did not modify the seizures induced by maximal electroshock and did not alter the convulsant dose of pentylenetetrezol in mice ( tests performed by the Anticonvulsant Screening Project of NINCDS ) .

Example answer:
{"entities": [{"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "pentylenetetrezol", "type": "Chemical"}]}

Example input:
Sentence: Based on the finding that VPU and VPA could protect the animals against pilocarpine-induced seizure it is suggested that the reduction of inhibitory amino acid neurotransmitters was comparatively minor and offset by a pronounced reduction of glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Sensitivity to several convulsion endpoints induced by nicotine , carbachol , and neostigmine were significantly greater in WSR versus WSP mice .

Example answer:
{"entities": [{"text": "convulsion", "type": "Disease"}, {"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: METHODS : Cholinergic convulsant sensitivity was examined in alcohol-na ve Withdrawal Seizure-Prone ( WSP ) and-Resistant ( WSR ) mice .

Example answer:
{"entities": [{"text": "alcohol-na", "type": "Chemical"}, {"text": "Seizure-Prone", "type": "Disease"}]}

Example input:
Sentence: Seizure activity due to PTZ and picrotoxin ( PTX ) was significantly decreased ; however , seizure activity due to 3-mercaptopropionic acid ( MPA ) , bicuculline ( BCC ) , methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate ( DMCM ) , or strychnine ( STR ) was not different from control .

Example answer:
{"entities": [{"text": "Seizure", "type": "Disease"}, {"text": "PTZ", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "PTX", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "3-mercaptopropionic acid", "type": "Chemical"}, {"text": "MPA", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "BCC", "type": "Chemical"}, {"text": "methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate", "type": "Chemical"}, {"text": "DMCM", "type": "Chemical"}, {"text": "strychnine", "type": "Chemical"}, {"text": "STR", "type": "Chemical"}]}

Example input:
Sentence: In this study , the severity of response to other seizure-inducing agents was tested in mice 1 and 24 h after intraperitoneal administration of 80 mg/kg gamma-HCH .

Example answer:
{"entities": [{"text": "seizure-inducing", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}]}

Input:
Sentence: Intraperitoneal administration of cholecystokinin octapeptide sulphate ester ( CCK-8-SE ) and nonsulphated cholecystokinin octapeptide ( CCK-8-NS ) enhanced the latency of seizures induced by picrotoxin in mice .

## Item bc5cdr:test:1892
Example input:
Sentence: A study on the effect of the duration of subcutaneous heparin injection on bruising and pain .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}, {"text": "bruising", "type": "Disease"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: RELEVANCE TO CLINICAL PRACTICE : When administering subcutaneous heparin injections , it is important to extend the duration of the injection .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: METHOD : The sample for the study consisted of 50 patients to whom subcutaneous heparin was administered .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: Overall , in high-risk patients , warfarin is superior to aspirin in preventing strokes , with a relative risk reduction of 36 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "strokes", "type": "Disease"}]}

Example input:
Sentence: AIM : This study was carried out to determine the effect of injection duration on bruising and pain following the administration of the subcutaneous injection of heparin .

Example answer:
{"entities": [{"text": "bruising", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Although different methods to prevent bruising and pain following the subcutaneous injection of heparin have been widely studied and described , the effect of injection duration on the occurrence of bruising and pain is little documented .

Example answer:
{"entities": [{"text": "bruising", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: The patient was admitted to the hospital , anticoagulated with unfractionated heparin , and given intravenous diltiazem for rate control and intravenous amiodarone for rate and rhythm control .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}]}

Example input:
Sentence: PATIENTS AND METHODS : Patients with more than 50 % decrease in platelet count or thrombocytopenia ( < 150 x 10 ( 9 ) /L ) after exposure to heparin , who had a positive two-step antigen assay [ optical density ( OD ) > 0.4 and > 50 inhibition with high concentration of heparin ] were included in the study .

Example answer:
{"entities": [{"text": "thrombocytopenia", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: Warfarin is the most widely used oral anticoagulant and is indicated for many clinical conditions .

Example answer:
{"entities": [{"text": "Warfarin", "type": "Chemical"}]}

Example input:
Sentence: Pooled data from trials comparing antithrombotic treatment with placebo have shown that warfarin reduces the risk of stroke by 62 % , and that aspirin alone reduces the risk by 22 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "stroke", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}]}

Input:
Sentence: Heparin , first used to prevent the clotting of blood in vitro , has been clinically used to treat thrombosis for more than 50 years .

## Item bc5cdr:test:2061
Example input:
Sentence: Administration of salvianolic acid A for a period of 8 days significantly attenuated isoproterenol-induced cardiac dysfunction and myocardial injury and improved mitochondrial respiratory function .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "cardiac dysfunction", "type": "Disease"}, {"text": "myocardial injury", "type": "Disease"}]}

Example input:
Sentence: The area under the plasma concentration time curve at 90 min was 4-12 times greater than for oral drug , suggesting the existence of an absorption-limiting process in the intestine , and providing an alternate form of administration for quaternary drugs .

Example answer:
{"entities": []}

Example input:
Sentence: As a consequence of blocking I ( f ) , clonidine reduced the slope of the diastolic depolarization and the frequency of pacemaker potentials in sinoatrial node cells from wild-type and alpha2ABC-knockout mice .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : A 50 % reduction in the incidence of akathisia when prochlorperazine was administered by means of 15-minute intravenous infusion versus a 2-minute intravenous push was not detected .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}, {"text": "prochlorperazine", "type": "Chemical"}]}

Example input:
Sentence: The fits ceased within 4 hours of administering intramuscular pyridoxine , suggesting an aetiology of pyridoxine deficiency secondary to isoniazid medication .

Example answer:
{"entities": [{"text": "fits", "type": "Disease"}, {"text": "pyridoxine", "type": "Chemical"}, {"text": "isoniazid", "type": "Chemical"}]}

Example input:
Sentence: together for 30 consecutive days and challenged with ISO on the day 29th and 30th , showed a significant ( P < 0.05 ) decrease in heart weight , serum marker enzymes , lipid peroxidation , Ca+2 ATPase and a significant increase in the body weight , endogenous antioxidants , Na+/K+ ATPase and Mg+2 ATPase when compared with ISO treated group and green tea or vitamin E alone treated groups .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}, {"text": "green tea", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}]}

Example input:
Sentence: The use and toxicity of didanosine ( ddI ) in HIV antibody-positive individuals intolerant to zidovudine ( AZT ) One hundred and fifty-one patients intolerant to zidovudine ( AZT ) received didanosine ( ddI ) to a maximum dose of 12.5 mg/kg/day .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "didanosine", "type": "Chemical"}, {"text": "ddI", "type": "Chemical"}, {"text": "HIV antibody-positive", "type": "Disease"}, {"text": "zidovudine", "type": "Chemical"}, {"text": "AZT", "type": "Chemical"}]}

Example input:
Sentence: We report a woman with coronary artery disease who developed a markedly prolonged QT interval and torsades de pointes ( TdP ) after taking ketoconazole for treatment of fungal infection .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "prolonged QT interval", "type": "Disease"}, {"text": "torsades de pointes", "type": "Disease"}, {"text": "TdP", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "fungal infection", "type": "Disease"}]}

Example input:
Sentence: These data indicate that the free ED50 in plasma for terfenadine ( 1.9 nM ) , terodiline ( 76 nM ) , cisapride ( 11 nM ) and E4031 ( 1.9 nM ) closely correlate with the free concentration in man causing QT effects .

Example answer:
{"entities": [{"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}, {"text": "E4031", "type": "Chemical"}]}

Example input:
Sentence: Four compounds known to increase QT interval and cause TDP were investigated : terfenadine , terodiline , cisapride and E4031 .

Example answer:
{"entities": [{"text": "TDP", "type": "Disease"}, {"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}, {"text": "E4031", "type": "Chemical"}]}

Input:
Sentence: Azimilide , however , significantly prolonged APD and QT interval at concentrations from 0.1 to 10 micromol/L but shortened them at 30 micromol/L .

## Item bc5cdr:test:2015
Example input:
Sentence: METHODS : In this study , WR242511 was administered intravenously ( IV ) in 2 female and 4 male rhesus monkeys in doses of 3.5 and/or 7.0 mg/kg ; a single male also received WR242511 orally ( PO ) at 7.0 mg/kg .

Example answer:
{"entities": [{"text": "WR242511", "type": "Chemical"}]}

Example input:
Sentence: Stroke followed cocaine use by inhalation , intranasal , intravenous , and intramuscular routes .

Example answer:
{"entities": [{"text": "Stroke", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: The animals that had experienced cyclic sucrose and chow were hyperactive in response to amphetamine compared with four control groups ( ad libitum 10 % sucrose and chow followed by amphetamine injection , cyclic chow followed by amphetamine injection , ad libitum chow with amphetamine , or cyclic 10 % sucrose and chow with a saline injection ) .

Example answer:
{"entities": [{"text": "sucrose", "type": "Chemical"}, {"text": "hyperactive", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}]}

Example input:
Sentence: Animals were administered nicotine , carbachol , or neostigmine via timed tail vein infusion , and the latencies to onset of tremor and clonus were recorded and converted to threshold dose .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}, {"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: Two separate equimolar doses ( 0.2 and 0.4 mumol ) of either cocaine or BE were injected ventricularly in unanesthetized juvenile rats .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "BE", "type": "Chemical"}]}

Example input:
Sentence: The 65 dogs in the study received injections in the subarachnoid space as follows : 6 to 8 ml of bupivacaine ( N = 15 ) , 2-chloroprocaine-CE ( N = 20 ) , low pH normal saline ( pH 3.0 ) ( N = 20 ) , or normal saline ( N = 10 ) .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}, {"text": "2-chloroprocaine-CE", "type": "Chemical"}]}

Example input:
Sentence: 2 and 10 mg/kg/i.p. , or an equal volume of saline for the control group ( n = 20 ) ; 15 minutes later , all the animals were injected with a single 50 mg/kg/i.p .

Example answer:
{"entities": []}

Example input:
Sentence: A nonregenerative anemia was the most compromising of the cytopenias and occurred in approximately 50 % of dogs receiving 400-500 mg/kg cefonicid or 540-840 mg/kg cefazedone .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "cytopenias", "type": "Disease"}, {"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}]}

Example input:
Sentence: Cocaine was injected ip over a range of doses ( 50-100 mg/kg ) and behavior was monitored for 20 minutes .

Example answer:
{"entities": [{"text": "Cocaine", "type": "Chemical"}]}

Example input:
Sentence: Swiss albino mice prepared with intrajugular catheters were tested in photocell cages after administration of 93 mg/kg ( LD50 ) of cocaine and GNC92H2 infusions ranging from 30 to 190 mg/kg .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "GNC92H2", "type": "Chemical"}]}

Input:
Sentence: METHODS : Twenty-three dogs were randomized to receive either 1 ) three intravenous ( IV ) boluses of cocaine 7.5 mg/kg with ethanol ( 1 g/kg ) as an IV infusion ( C+E , n = 8 ) , 2 ) three cocaine boluses only ( C , n = 6 ) , 3 ) ethanol infusion only ( E , n = 5 ) , or 4 ) placebo boluses and infusion ( n = 4 ) .

## Item bc5cdr:test:2207
Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "Chemical"}]}

Example input:
Sentence: The effects of METH in CX3CR1 knockout mice were not gender-dependent and did not extend beyond the striatum .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}]}

Example input:
Sentence: Subsequent amantadine treatments produced enhancement of motility from corresponding control in all mouse strains with the BALB/C mice being the least sensitive .

Example answer:
{"entities": [{"text": "amantadine", "type": "Chemical"}]}

Example input:
Sentence: An autoradiographic study was performed on male F-344 rats fed diet containing FANFT at a level of 0.2 % and/or aspirin at a level of 0.5 % to evaluate the effect of aspirin on the increased cell proliferation induced by FANFT in the forestomach and bladder .

Example answer:
{"entities": [{"text": "FANFT", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: In experimental animals excess deposition of collagen and glycoaminoglycans was observed in the subendothelial and medial layer of the aortic wall , together with prominent basal membrane substance around aortic smooth muscle cells .

Example answer:
{"entities": []}

Example input:
Sentence: The Dbh -/- mice had normal baseline performance in the EPM but were completely resistant to the anxiogenic effects of cocaine .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: FANFT-induced cell proliferation in the bladder was significantly suppressed by aspirin co-administration after 4 weeks but not after 12 weeks .

Example answer:
{"entities": [{"text": "FANFT-induced", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: In Mg ( 2+ ) -free bathing medium containing bicuculline , conditions designed to increase excitability in the slices , electrical stimulation of the hilus resulted in a single population spike in granule cells from control mice and pilocarpine-treated mice that did not experience SE .

Example answer:
{"entities": [{"text": "Mg", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "pilocarpine-treated", "type": "Chemical"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: In microdialysis experiments , the lines did not differ in basal release of ACh , and 50 mM KCl increased ACh output in both lines of mice .

Example answer:
{"entities": [{"text": "ACh", "type": "Chemical"}, {"text": "KCl", "type": "Chemical"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Input:
Sentence: Mast cells appeared in the connective and muscular layers of the bladder at a much higher number in DBA/2 mice than in C57BL/6 mice or untreated controls .

## Item bc5cdr:test:2021
Example input:
Sentence: These results provide evidence for a possible mechanistic role of oxidative and nitrosative stress and NFkappaB in the alterations induced by cocaine .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Progressive abstinence from cocaine was associated with worsening of all measured polysomnographic sleep outcomes .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: While the mechanisms underlying cocaine 's rewarding effects have been studied extensively , less attention has been paid to the unpleasant behavioral states induced by cocaine , such as anxiety .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "anxiety", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : Cocaine use predisposed aneurysmal rupture at a significantly earlier age and in much smaller aneurysms .

Example answer:
{"entities": [{"text": "Cocaine", "type": "Chemical"}, {"text": "aneurysmal rupture", "type": "Disease"}, {"text": "aneurysms", "type": "Disease"}]}

Example input:
Sentence: This led us to hypothesize that a metabolite of cocaine may be responsible for some of those delayed sequelae .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Whereas cocaine-induced seizures were best characterized as brief , generalized , and tonic and resulted in death , those induced by BE were prolonged , often multiple and mixed in type , and rarely resulted in death .

Example answer:
{"entities": [{"text": "cocaine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "death", "type": "Disease"}, {"text": "BE", "type": "Chemical"}]}

Example input:
Sentence: No toxin , alcohol , or other drugs were reported .

Example answer:
{"entities": [{"text": "alcohol", "type": "Chemical"}]}

Example input:
Sentence: Significant blockade of cocaine toxicity was observed with the higher dose of GNC92H2 ( 190 mg/kg ) , where premorbid behaviors were reduced up to 40 % , seizures up to 77 % and death by 72 % .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "GNC92H2", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "death", "type": "Disease"}]}

Example input:
Sentence: Different mechanisms have been suggested for cocaine toxicity including an increase in oxidative stress but the association between oxidative status in the brain and cocaine induced-behaviour is poorly understood .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Cocaine is a widely abused psychostimulant that has both rewarding and aversive properties .

Example answer:
{"entities": [{"text": "Cocaine", "type": "Chemical"}]}

Input:
Sentence: CONCLUSIONS : Cocaine and ethanol in combination were more toxic than either substance alone .

## Item bc5cdr:test:1507
Example input:
Sentence: Hyperbaric oxygen therapy for control of intractable cyclophosphamide-induced hemorrhagic cystitis .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "cyclophosphamide-induced", "type": "Chemical"}]}

Example input:
Sentence: The similarity between the histologic appearances of busulfan cystitis and both radiation and cyclophosphamide-induced cystitis is discussed and the world literature reviewed .

Example answer:
{"entities": [{"text": "busulfan", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}, {"text": "cyclophosphamide-induced", "type": "Chemical"}]}

Example input:
Sentence: Cyclophosphamide therapy increases the risk of carcinoma of the bladder .

Example answer:
{"entities": [{"text": "Cyclophosphamide", "type": "Chemical"}]}

Example input:
Sentence: In future , this form of therapy can offer a safe alternative in the treatment of cyclophosphamide-induced hemorrhagic cystitis .

Example answer:
{"entities": [{"text": "cyclophosphamide-induced", "type": "Chemical"}]}

Example input:
Sentence: CY caused hemorrhagic cystitis in 40 % of rats , but it did not cause this complication when combined with 5-FU and MTX .

Example answer:
{"entities": [{"text": "CY", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "MTX", "type": "Chemical"}]}

Example input:
Sentence: Chloroacetaldehyde and its contribution to urotoxicity during treatment with cyclophosphamide or ifosfamide .

Example answer:
{"entities": [{"text": "Chloroacetaldehyde", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "ifosfamide", "type": "Chemical"}]}

Example input:
Sentence: Based on clinical data , indicating that chloroacetaldehyde ( CAA ) is an important metabolite of oxazaphosphorine cytostatics , an experimental study was carried out in order to elucidate the role of CAA in the development of hemorrhagic cystitis .

Example answer:
{"entities": [{"text": "chloroacetaldehyde", "type": "Chemical"}, {"text": "CAA", "type": "Chemical"}]}

Example input:
Sentence: We report a case of intractable hemorrhagic cystitis due to cyclophosphamide therapy for Wegener 's granulomatosis .

Example answer:
{"entities": [{"text": "cyclophosphamide", "type": "Chemical"}, {"text": "Wegener 's granulomatosis", "type": "Disease"}]}

Example input:
Sentence: In vitro characterization of parasympathetic and sympathetic responses in cyclophosphamide-induced cystitis in the rat .

Example answer:
{"entities": [{"text": "cyclophosphamide-induced", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Example input:
Sentence: In cyclophosphamide-induced cystitis in the rat , detrusor function is impaired and the expression and effects of muscarinic receptors altered .

Example answer:
{"entities": [{"text": "cyclophosphamide-induced", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Input:
Sentence: Chemical cystitis was induced by cyclophosphamide ( CYP ) which is metabolized to acrolein , an irritant eliminated in the urine .

## Item bc5cdr:test:2046
Example input:
Sentence: The electrocardiograms ( ECG ) of 99 cocaine-abusing patients were compared with the ECGs of 50 schizophrenic controls .

Example answer:
{"entities": [{"text": "cocaine-abusing", "type": "Chemical"}, {"text": "schizophrenic", "type": "Disease"}]}

Example input:
Sentence: Cocaine-induced myocardial infarction : clinical observations and pathogenetic considerations .

Example answer:
{"entities": [{"text": "Cocaine-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Clinical and experimental data published to date suggest several possible mechanisms by which cocaine may result in acute myocardial infarction .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: A 45-year-old man , an admitted frequent cocaine user , presented to the Emergency Department ( ED ) on two separate occasions with a history of priapism after cocaine use .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "priapism", "type": "Disease"}]}

Example input:
Sentence: These data indicate that ( 1 ) the apparent incidence of stroke related to cocaine use is increasing ; ( 2 ) cocaine-associated stroke occurs primarily in young adults ; ( 3 ) stroke may follow any route of cocaine administration ; ( 4 ) stroke after cocaine use is frequently associated with intracranial aneurysms and arteriovenous malformations ; and ( 5 ) in cocaine-associated stroke , the frequency of intracranial hemorrhage exceeds that of cerebral infarction .

Example answer:
{"entities": [{"text": "stroke", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}, {"text": "cocaine-associated", "type": "Chemical"}, {"text": "intracranial aneurysms", "type": "Disease"}, {"text": "arteriovenous malformations", "type": "Disease"}, {"text": "intracranial hemorrhage", "type": "Disease"}, {"text": "cerebral infarction", "type": "Disease"}]}

Example input:
Sentence: In particular , the tendency of cocaine to produce chest pain ought to be in the mind of the emergency nurse when faced with a young victim of chest pain who is otherwise at low risk .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "chest pain", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : Cocaine use predisposed aneurysmal rupture at a significantly earlier age and in much smaller aneurysms .

Example answer:
{"entities": [{"text": "Cocaine", "type": "Chemical"}, {"text": "aneurysmal rupture", "type": "Disease"}, {"text": "aneurysms", "type": "Disease"}]}

Example input:
Sentence: Electrocardiographic evidence of myocardial injury in psychiatrically hospitalized cocaine abusers .

Example answer:
{"entities": [{"text": "myocardial injury", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: In individuals with preexisting , high-grade coronary arterial narrowing , acute myocardial infarction may result from an increase in myocardial oxygen demand associated with cocaine-induced increase in rate-pressure product .

Example answer:
{"entities": [{"text": "acute myocardial infarction", "type": "Disease"}, {"text": "oxygen", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}]}

Example input:
Sentence: Eleven of the cocaine abusers and none of the controls had ECG evidence of significant myocardial injury defined as myocardial infarction , ischemia , and bundle branch block .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "myocardial injury", "type": "Disease"}, {"text": "myocardial infarction", "type": "Disease"}, {"text": "ischemia", "type": "Disease"}, {"text": "bundle branch block", "type": "Disease"}]}

Input:
Sentence: Prevalence of heart disease in asymptomatic chronic cocaine users .

## Item bc5cdr:test:1876
Example input:
Sentence: Doxorubicin is an effective anticancer chemotherapeutic agent known to cause acute and chronic cardiomyopathy .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: Epicardial coronary collateral vessels were demonstrated in all four patients ; a coronary `` steal '' phenomenon may be the mechanism of the dipyridamole-induced ischemia observed .

Example answer:
{"entities": [{"text": "dipyridamole-induced", "type": "Chemical"}, {"text": "ischemia", "type": "Disease"}]}

Example input:
Sentence: Dobutamine infusion at 10 micrograms/kg per min was discontinued after six studies secondary to a 50 % incidence rate of adverse symptoms .

Example answer:
{"entities": [{"text": "Dobutamine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Among markers of ischemic injury after DOX in rats , cTnT showed the greatest ability to detect myocardial damage assessed by echocardiographic detection and histological changes .

Example answer:
{"entities": [{"text": "ischemic injury", "type": "Disease"}, {"text": "DOX", "type": "Chemical"}, {"text": "myocardial damage", "type": "Disease"}]}

Example input:
Sentence: Dobutamine stress echocardiography : a sensitive indicator of diminished myocardial function in asymptomatic doxorubicin-treated long-term survivors of childhood cancer .

Example answer:
{"entities": [{"text": "Dobutamine", "type": "Chemical"}, {"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : To assess the added diagnostic value of a new cardiac performance index ( dP/dtejc ) measurement , based on brachial artery flow changes , as compared to standard 12-lead ECG , for detecting dobutamine-induced myocardial ischemia , using Tc99m-Sestamibi single-photon emission computed tomography as the gold standard of comparison to assess the presence or absence of ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "Tc99m-Sestamibi", "type": "Chemical"}, {"text": "ischemia", "type": "Disease"}]}

Example input:
Sentence: To develop a more sensitive echocardiographic screening test for cardiac damage due to doxorubicin , a cohort study was performed using dobutamine infusion to differentiate asymptomatic long-term survivors of childhood cancer treated with doxorubicin from healthy control subjects .

Example answer:
{"entities": [{"text": "cardiac damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: The increase in dP/dtejc during infusion of dobutamine in this group was severely impaired as compared to the non-ischemic group .

Example answer:
{"entities": [{"text": "dobutamine", "type": "Chemical"}]}

Example input:
Sentence: Assessment of a new non-invasive index of cardiac performance for detection of dobutamine-induced myocardial ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Electrocardiography has a very low sensitivity in detecting dobutamine-induced myocardial ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}]}

Input:
Sentence: Dobutamine induced ischaemia could therefore be used to study the pathophysiology of this phenomenon further in patients with coronary artery disease .

## Item bc5cdr:test:2221
Example input:
Sentence: Patients ' mean age was 53.9 years , their mean weight was 193.9 pounds , and they smoked a mean of 25.2 cigarettes per day at baseline .

Example answer:
{"entities": []}

Example input:
Sentence: Based on this principle a 27-year old woman , classified as being in the high-risk group ( Goldstein and Berkowitz score : 11 ) , was treated with multiple cytotoxic drugs .

Example answer:
{"entities": []}

Example input:
Sentence: 164 patients ( mean age +/- standard deviation [ SD ] 81.6 +/- 6.8 years ) were admitted .

Example answer:
{"entities": []}

Example input:
Sentence: ATT-ALF patients were younger ( 32.87 [ +/-15.8 ] years ) , and 49 ( 70 % ) of them were women .

Example answer:
{"entities": []}

Example input:
Sentence: The mean age of patients in the 16 probable cases was 57.9 , with hepatotoxicity being more common in women .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: RESULTS : All patients ( 65+/-16 yrs ; 58 % males ) finished the examination .

Example answer:
{"entities": []}

Example input:
Sentence: Ages ranged from 4 months to 17 years ; 58 patients were males and 42 females .

Example answer:
{"entities": []}

Example input:
Sentence: Eleven patients ( six male ) with median age 47 years ( range 27-73 ) , median disease duration 50 months ( range 9-178 ) and median follow-up period of patients 13.8 months ( range 5-27 ) were enrolled in this study .

Example answer:
{"entities": []}

Example input:
Sentence: Among these 47 patients the mean ( +/- SD ) age was 32.5 +/- 12.1 years ; 76 % ( 34/45 ) were men .

Example answer:
{"entities": []}

Example input:
Sentence: Patients had a median performance status of 1 ( WHO ) , and median age of 61 years .

Example answer:
{"entities": []}

Input:
Sentence: Patients ' characteristics were : male/female ratio 20/13 ; median age 57 ( 27-75 ) years ; median WHO status 1 ( 0-2 ) .

## Item bc5cdr:test:2088
Example input:
Sentence: It was `` serious '' for almost 2/3 of the patients ( 62.5 % ) and its outcome favourable in most of the cases ( 82 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Of 24 evaluable patients , two achieved a complete remission and one achieved a partial remission for an overall response rate of 12.5 % ( 95 % confidence interval : 2.6-32.4 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Among 547 preterm infants of < or = 34 weeks gestation born between 1987 and 1991 , 8 children ( 1.46 % ) developed severe progressive and bilateral sensorineural hearing loss .

Example answer:
{"entities": [{"text": "sensorineural hearing loss", "type": "Disease"}]}

Example input:
Sentence: The prevalence rate for CIMD was 12 % at baseline .

Example answer:
{"entities": [{"text": "CIMD", "type": "Disease"}]}

Example input:
Sentence: It was found that the transformation of exencephalic tissue was not simply size-dependent , and all cases of anencephaly at E18.5 resulted from embryos with a large amount of exencephalic tissue at E13.5 .

Example answer:
{"entities": [{"text": "exencephalic", "type": "Disease"}, {"text": "anencephaly", "type": "Disease"}]}

Example input:
Sentence: At presentation , advanced encephalopathy and cerebral edema were present in 51 ( 76 % ) and 29 ( 41.4 % ) patients , respectively .

Example answer:
{"entities": [{"text": "encephalopathy", "type": "Disease"}, {"text": "cerebral edema", "type": "Disease"}]}

Example input:
Sentence: Microscopic observation showed the configuration of exencephaly at E13.5 , frequent hemorrhaging and detachment of the neural plate from surface ectoderm in the exencephalic head at E15.5 , and multiple modes of reduction in the exencephalic tissue at E18.5 .

Example answer:
{"entities": [{"text": "exencephaly", "type": "Disease"}, {"text": "hemorrhaging", "type": "Disease"}, {"text": "exencephalic", "type": "Disease"}]}

Example input:
Sentence: Ninety-nine percent ( sixty-eight ) of the sixty-nine parents present during the reduction were pleased with the sedation and would allow it to be used again in a similar situation .

Example answer:
{"entities": []}

Example input:
Sentence: Cerebral infarction occurred in 10 patients ( 22 % ) , intracerebral hemorrhage in 22 ( 49 % ) , and subarachnoid hemorrhage in 13 ( 29 % ) .

Example answer:
{"entities": [{"text": "Cerebral infarction", "type": "Disease"}, {"text": "intracerebral hemorrhage", "type": "Disease"}, {"text": "subarachnoid hemorrhage", "type": "Disease"}]}

Example input:
Sentence: During a 9-year period , we retrospectively collected 27 neurological events ( 11 % ) in as many patients , from 253 children enrolled in the ALL front-line protocol .

Example answer:
{"entities": [{"text": "ALL", "type": "Disease"}]}

Input:
Sentence: The incidence of subependymal cysts in the 117 remaining infants was 14 % ( 16 of 117 ) .

## Item bc5cdr:test:2098
Example input:
Sentence: Clinical tolerability of both agents has been good , with fewer than 3 % of patients withdrawn from treatment because of clinical adverse experiences .

Example answer:
{"entities": []}

Example input:
Sentence: The drug was withdrawn on presentation to hospital in 11 patients , with rapid clinical improvement in 9 .

Example answer:
{"entities": []}

Example input:
Sentence: Improvement and eventually full recovery only occurred after TAC was completely discontinued and successfully replaced by everolimus .

Example answer:
{"entities": [{"text": "TAC", "type": "Chemical"}, {"text": "everolimus", "type": "Chemical"}]}

Example input:
Sentence: MEASUREMENTS AND MAIN RESULTS : None of 23 patients who received docetaxel alone developed VTE , whereas 9 of 47 patients ( 19 % ) who received docetaxel plus thalidomide developed VTE ( p=0.025 ) .

Example answer:
{"entities": [{"text": "docetaxel", "type": "Chemical"}, {"text": "VTE", "type": "Disease"}, {"text": "thalidomide", "type": "Chemical"}]}

Example input:
Sentence: Our results failed to demonstrate an important response rate to single agent thalidomide in indolent lymphomas and contrast with the higher activity level reported with the second generation immunomodulatory agent , lenalidomide .

Example answer:
{"entities": [{"text": "thalidomide", "type": "Chemical"}, {"text": "lymphomas", "type": "Disease"}, {"text": "lenalidomide", "type": "Chemical"}]}

Example input:
Sentence: When the metoclopramide administration was discontinued , the abnormal movements gradually improved to a considerable extent .

Example answer:
{"entities": [{"text": "metoclopramide", "type": "Chemical"}, {"text": "abnormal movements", "type": "Disease"}]}

Example input:
Sentence: INTERVENTION : Each patient received either intravenous docetaxel 30 mg/m2/week for 3 consecutive weeks , followed by 1 week off , or the combination of continuous oral thalidomide 200 mg every evening plus the same docetaxel regimen .

Example answer:
{"entities": [{"text": "docetaxel", "type": "Chemical"}, {"text": "thalidomide", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : The addition of thalidomide to docetaxel in the treatment of prostate cancer significantly increases the frequency of VTE .

Example answer:
{"entities": [{"text": "thalidomide", "type": "Chemical"}, {"text": "docetaxel", "type": "Chemical"}, {"text": "prostate cancer", "type": "Disease"}, {"text": "VTE", "type": "Disease"}]}

Example input:
Sentence: Thalidomide has limited single-agent activity in relapsed or refractory indolent non-Hodgkin lymphomas : a phase II trial of the Cancer and Leukemia Group B. Thalidomide is an immunomodulatory agent with demonstrated activity in multiple myeloma , mantle cell lymphoma and lymphoplasmacytic lymphoma .

Example answer:
{"entities": [{"text": "Thalidomide", "type": "Chemical"}, {"text": "non-Hodgkin lymphomas", "type": "Disease"}, {"text": "Cancer", "type": "Disease"}, {"text": "Leukemia", "type": "Disease"}, {"text": "multiple myeloma", "type": "Disease"}, {"text": "mantle cell lymphoma", "type": "Disease"}, {"text": "lymphoplasmacytic lymphoma", "type": "Disease"}]}

Example input:
Sentence: Between July 2001 and April 2004 , 24 patients with relapsed/refractory indolent lymphomas received thalidomide 200 mg daily with escalation by 100 mg daily every 1-2 weeks as tolerated , up to a maximum of 800 mg daily .

Example answer:
{"entities": [{"text": "lymphomas", "type": "Disease"}, {"text": "thalidomide", "type": "Chemical"}]}

Input:
Sentence: Thalidomide was discontinued in 55 patients for lack of therapeutic response .

## Item bc5cdr:test:2099
Example input:
Sentence: Since adverse reactions are frequent , less than 50 percent of patients are able to continue a particular drug for more than one year .

Example answer:
{"entities": []}

Example input:
Sentence: Both patients recovered quickly after stopping glyburide therapy and have remained well for a follow-up period of 1 year .

Example answer:
{"entities": [{"text": "glyburide", "type": "Chemical"}]}

Example input:
Sentence: The median duration of survival in the 12 patients was 54 weeks ( range 21 to more than 156 weeks ) , with an 18-month survival rate of 42 % .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : a total of 13 patients were referred to the Danish Cholinesterase Research Unit after ECT during 38 months .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSION : The addition of thalidomide to docetaxel in the treatment of prostate cancer significantly increases the frequency of VTE .

Example answer:
{"entities": [{"text": "thalidomide", "type": "Chemical"}, {"text": "docetaxel", "type": "Chemical"}, {"text": "prostate cancer", "type": "Disease"}, {"text": "VTE", "type": "Disease"}]}

Example input:
Sentence: Clinical experience with lovastatin includes over 5000 patients , 700 of whom have been treated for 2 years or more , and experience with simvastatin includes over 3500 patients , of whom 350 have been treated for 18 months or more .

Example answer:
{"entities": [{"text": "lovastatin", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}]}

Example input:
Sentence: Illness occurred within 1 -- 9 weeks of commencement of therapy in 9 patients , the remaining 3 patients having received the drug for 13 months , 15 months and 7 years before experiencing symptoms .

Example answer:
{"entities": []}

Example input:
Sentence: MEASUREMENTS AND MAIN RESULTS : None of 23 patients who received docetaxel alone developed VTE , whereas 9 of 47 patients ( 19 % ) who received docetaxel plus thalidomide developed VTE ( p=0.025 ) .

Example answer:
{"entities": [{"text": "docetaxel", "type": "Chemical"}, {"text": "VTE", "type": "Disease"}, {"text": "thalidomide", "type": "Chemical"}]}

Example input:
Sentence: INTERVENTION : Each patient received either intravenous docetaxel 30 mg/m2/week for 3 consecutive weeks , followed by 1 week off , or the combination of continuous oral thalidomide 200 mg every evening plus the same docetaxel regimen .

Example answer:
{"entities": [{"text": "docetaxel", "type": "Chemical"}, {"text": "thalidomide", "type": "Chemical"}]}

Example input:
Sentence: Between July 2001 and April 2004 , 24 patients with relapsed/refractory indolent lymphomas received thalidomide 200 mg daily with escalation by 100 mg daily every 1-2 weeks as tolerated , up to a maximum of 800 mg daily .

Example answer:
{"entities": [{"text": "lymphomas", "type": "Disease"}, {"text": "thalidomide", "type": "Chemical"}]}

Input:
Sentence: Of 67 patients initially enrolled , 24 remained on thalidomide for 3 months , 8 remained at 6 months , and 3 remained at 9 months .
