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

## Item bc5cdr:test:117
Example input:
Sentence: This study shows that prolonged analgesic treatment in Fischer 344 rats causes progressive and irreversible damage to the interstitial matrix and type 1 interstitial cells leading to RPN .

Example answer:
{"entities": [{"text": "RPN", "type": "Disease"}]}

Example input:
Sentence: In the five rats that developed somatic rigidity , ICP and CVP increased significantly above baseline ( delta ICP 7.5 +/- 1.0 mmHg , delta CVP 5.9 +/- 1.3 mmHg ) .

Example answer:
{"entities": [{"text": "somatic rigidity", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Immunofluorescence staining with the MRP2 antibody was found to label a high number of microvessels throughout the brain in normal Wistar rats , whereas such labeling was absent in TR ( - ) rats .

Example answer:
{"entities": []}

Example input:
Sentence: In 7 of the 18 rats , degeneration and myocyte vacuolisation were found .

Example answer:
{"entities": []}

Example input:
Sentence: What is less well known is a phenomenon whereby statins may induce a myopathy , which persists or may progress after stopping the drug .

Example answer:
{"entities": [{"text": "statins", "type": "Chemical"}, {"text": "myopathy", "type": "Disease"}]}

Example input:
Sentence: Myopathy , associated in some cases with myoglobinuria , and in 2 cases with transient renal failure , has been rarely reported with lovastatin , especially in patients concomitantly treated with cyclosporin , gemfibrozil or niacin .

Example answer:
{"entities": [{"text": "Myopathy", "type": "Disease"}, {"text": "myoglobinuria", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}, {"text": "lovastatin", "type": "Chemical"}, {"text": "cyclosporin", "type": "Chemical"}, {"text": "gemfibrozil", "type": "Chemical"}, {"text": "niacin", "type": "Chemical"}]}

Example input:
Sentence: However , compression neuropathy due to fibrotic muscle affected by pentazocine-induced myopathy has not previously been reported .

Example answer:
{"entities": [{"text": "compression neuropathy", "type": "Disease"}, {"text": "pentazocine-induced", "type": "Chemical"}, {"text": "myopathy", "type": "Disease"}]}

Example input:
Sentence: We investigated the muscle pathology in 8 such cases .

Example answer:
{"entities": []}

Example input:
Sentence: The development of tolerance to the muscular rigidity produced by morphine was studied in rats .

Example answer:
{"entities": [{"text": "muscular rigidity", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: The mechanism of this myopathy is uncertain but may involve the induction by statins of an endoplasmic reticulum stress response with associated up-regulation of MHC-I expression and antigen presentation by muscle fibres .

Example answer:
{"entities": [{"text": "myopathy", "type": "Disease"}, {"text": "statins", "type": "Chemical"}]}

Input:
Sentence: It is thus confirmed that the histological characteristics of myopathic rat muscle induced experimentally are extraordinarily similar to those of human myopathy as confirmed during biopsies performed at the Orthopaedic Traumatological Centre , Florence .

## Item bc5cdr:test:483
Example input:
Sentence: All four recovered completely without neurological sequelae following the withdrawal of the offending agents .

Example answer:
{"entities": [{"text": "neurological sequelae", "type": "Disease"}]}

Example input:
Sentence: Since adverse reactions are frequent , less than 50 percent of patients are able to continue a particular drug for more than one year .

Example answer:
{"entities": []}

Example input:
Sentence: One patient died , having presented in hepatic failure , and another , who had been taking methyldopa for 7 years , showed slower clinical and biochemical resolution over a period of several months .

Example answer:
{"entities": [{"text": "hepatic failure", "type": "Disease"}, {"text": "methyldopa", "type": "Chemical"}]}

Example input:
Sentence: The drug was withdrawn on presentation to hospital in 11 patients , with rapid clinical improvement in 9 .

Example answer:
{"entities": []}

Example input:
Sentence: The first patient died without a diagnosis ; the second patient had a dramatic recovery following the administration of vitamin B6 .

Example answer:
{"entities": [{"text": "vitamin B6", "type": "Chemical"}]}

Example input:
Sentence: She subsequently died some 5 weeks after the commencement of her drug therapy.Post-mortem examination showed evidence of massive hepatocellular necrosis , acute hypersensitivity myocarditis , focal acute tubulo-interstitial nephritis and extensive bone marrow necrosis , with no evidence of malignancy .

Example answer:
{"entities": [{"text": "massive hepatocellular necrosis", "type": "Disease"}, {"text": "myocarditis", "type": "Disease"}, {"text": "nephritis", "type": "Disease"}, {"text": "bone marrow necrosis", "type": "Disease"}, {"text": "malignancy", "type": "Disease"}]}

Example input:
Sentence: All patients recovered without sequelae .

Example answer:
{"entities": []}

Example input:
Sentence: Eight patients were dead in the last follow-up ; two of them died of treatment-related toxicity .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: No long-term sequelae were noted , and no patients had hallucinations or nightmares .

Example answer:
{"entities": [{"text": "hallucinations", "type": "Disease"}]}

Example input:
Sentence: An analysis of the 75 cases that had been adequately followed up suggested that 16 , including three deaths , were probably related to treatment with the drug .

Example answer:
{"entities": [{"text": "deaths", "type": "Disease"}]}

Input:
Sentence: No patient has died or suffered any apparent long-term sequelae that were directly attributable to the drug .

## Item bc5cdr:test:480
Example input:
Sentence: The majority of patients ( > 60 % ) experienced no change in their disease status from baseline .

Example answer:
{"entities": []}

Example input:
Sentence: The tolerance was evaluated in these 110 patients , and 29 patients presented with local side-effects .

Example answer:
{"entities": []}

Example input:
Sentence: Anaphylaxis was seen in 37 patients ( 69 % ) , the other 17 ( 31 % ) having urticaria and/or angioedema .

Example answer:
{"entities": [{"text": "Anaphylaxis", "type": "Disease"}, {"text": "urticaria", "type": "Disease"}, {"text": "angioedema", "type": "Disease"}]}

Example input:
Sentence: The most common adverse events were nausea ( 17.2 % and 16.1 % ; 95 % CI , -3.7 to 6.0 ) , hiccups ( 10.7 % and 6.6 % ; 95 % CI , 0.5 to 7.8 ) , and headache ( 8.7 % and 9.9 % ; 95 % Cl , -5.0 to 2.6 ) .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "hiccups", "type": "Disease"}, {"text": "headache", "type": "Disease"}]}

Example input:
Sentence: All patients were evaluable for response and toxicity .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Serious adverse events were reported in 11 and 13 patients in the respective groups .

Example answer:
{"entities": []}

Example input:
Sentence: During treatment , adverse cardiac effects were observed in 14 patients ( 18 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Clinical tolerability of both agents has been good , with fewer than 3 % of patients withdrawn from treatment because of clinical adverse experiences .

Example answer:
{"entities": []}

Example input:
Sentence: There were 13 cases of adverse reactions ( 0.34 % ) , ten of which were mild reactions such as nausea , exanthema , urtication , itchiness , and urgency to defecate , and did not require treatment .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "exanthema", "type": "Disease"}, {"text": "urtication", "type": "Disease"}, {"text": "itchiness", "type": "Disease"}]}

Example input:
Sentence: Since adverse reactions are frequent , less than 50 percent of patients are able to continue a particular drug for more than one year .

Example answer:
{"entities": []}

Input:
Sentence: Virtually all patients experienced one or more adverse reactions .

## Item bc5cdr:test:347
Example input:
Sentence: Sulpiride induced only SOCS-1 in the medial preoptic area , where GnRH neurons are regulated , but in the arcuate nucleus and choroid plexus , PRL-R , SOCS-3 , and CIS mRNA levels were also induced .

Example answer:
{"entities": [{"text": "Sulpiride", "type": "Chemical"}]}

Example input:
Sentence: Lesions reduced the extent of immunohistological staining for choline acetyltransferase in the interpeduncular nucleus ( p < 0.025 ) , but not for tyrosine hydroxylase in the surrounding catecholaminergic A10 region .

Example answer:
{"entities": []}

Example input:
Sentence: Damage to the capillary was accompanied by marked damage to neuroglial cells , mainly to perivascular processes of astrocytes .

Example answer:
{"entities": []}

Example input:
Sentence: Immunohistochemical staining for NFs showed characteristic terminal clubs of axons in the borderzone of lesions .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : The expression of MRP2 and Pgp in brain and liver sections of TR ( - ) rats and normal Wistar rats was determined with immunohistochemistry , by using a novel , highly selective monoclonal MRP2 antibody and the monoclonal Pgp antibody C219 , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: The proliferation of astrocytes ( Bergmann 's in particular ) and occasionally of oligodendrocytes was found .

Example answer:
{"entities": []}

Example input:
Sentence: Immunohistochemical studies with antibodies to neurofilament proteins on axonal damage in experimental focal lesions in rat .

Example answer:
{"entities": [{"text": "axonal damage", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Immunofluorescence staining with the MRP2 antibody was found to label a high number of microvessels throughout the brain in normal Wistar rats , whereas such labeling was absent in TR ( - ) rats .

Example answer:
{"entities": []}

Example input:
Sentence: These immunohistochemical changes of NFs can serve as a marker for axonal damage in various experimental traumatic or ischemic lesions .

Example answer:
{"entities": [{"text": "axonal damage", "type": "Disease"}, {"text": "traumatic", "type": "Disease"}]}

Example input:
Sentence: Immunohistochemistry with monoclonal antibodies against neurofilament ( NF ) proteins of middle and high molecular weight class , NF-M and NF-H , was used to study axonal injury in the borderzone of focal lesions in rats .

Example answer:
{"entities": [{"text": "axonal injury", "type": "Disease"}]}

Input:
Sentence: The neuropathology of SNR was investigated using immunohistochemical techniques with the major emphasis on the time-course of changes in neurons and astrocytes .

## Item bc5cdr:test:46
Example input:
Sentence: Conjunctival blanching and mydriasis were commonly found .

Example answer:
{"entities": [{"text": "Conjunctival blanching", "type": "Disease"}, {"text": "mydriasis", "type": "Disease"}]}

Example input:
Sentence: The sG145R mutation strongly reduced HBsAg levels and was able to fully restore the impaired replication of LAM-resistant HBV mutants to the levels of wild-type HBV , and PC or BCP mutations further enhanced viral replication .

Example answer:
{"entities": [{"text": "HBsAg", "type": "Chemical"}, {"text": "LAM-resistant", "type": "Chemical"}]}

Example input:
Sentence: The semi-quantitative scoring was significantly worst in the group treated with CsA plus SRL ( P < 0.001 compared with controls ) and the analysis of the total grade of fibrosis also showed the highest proportion in the same group and was significantly different from controls ( P < 0.02 ) .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: Gastrointestinal bleed , seizures , infection , and acute renal failure were documented in seven ( 10 % ) , five ( 7.1 % ) , 26 ( 37.1 % ) , and seven ( 10 % ) patients , respectively .

Example answer:
{"entities": [{"text": "Gastrointestinal bleed", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "infection", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: Respiratory insufficiency was further worsened by Proteus mirabilis infection and severe bronchoconstriction .

Example answer:
{"entities": [{"text": "Respiratory insufficiency", "type": "Disease"}, {"text": "Proteus mirabilis infection", "type": "Disease"}]}

Example input:
Sentence: A grade 2 or 3 infection occurred in 16 % of patients , but no toxic deaths occurred .

Example answer:
{"entities": [{"text": "infection", "type": "Disease"}, {"text": "deaths", "type": "Disease"}]}

Example input:
Sentence: Neutropenia grade greater than or equal to 3 was seen in 15 patients , infections with recovery in 3 , and grand mal seizures in 1 patient .

Example answer:
{"entities": [{"text": "Neutropenia", "type": "Disease"}, {"text": "infections", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: All the patients were skin test negative to BPO ; 49 of 51 ( 96 % ) were also negative to MDM , and 44 of 46 ( 96 % ) to PG .

Example answer:
{"entities": [{"text": "BPO", "type": "Chemical"}, {"text": "MDM", "type": "Disease"}, {"text": "PG", "type": "Chemical"}]}

Example input:
Sentence: Guillain-Barr syndrome was the commonest identifiable cause ( 15.6 % ) , accounting for half of the cases with motor neuropathy .

Example answer:
{"entities": [{"text": "Guillain-Barr syndrome", "type": "Disease"}, {"text": "motor neuropathy", "type": "Disease"}]}

Example input:
Sentence: The leading causes of death were pneumonia and bronchitis ( 44.1 % ) , malignant neoplasms ( 11.6 % ) , heart diseases ( 4.1 % ) , cerebral infarction ( 3.7 % ) and septicaemia ( 3.3 % ) .

Example answer:
{"entities": [{"text": "death", "type": "Disease"}, {"text": "pneumonia", "type": "Disease"}, {"text": "bronchitis", "type": "Disease"}, {"text": "neoplasms", "type": "Disease"}, {"text": "heart diseases", "type": "Disease"}, {"text": "cerebral infarction", "type": "Disease"}, {"text": "septicaemia", "type": "Disease"}]}

Input:
Sentence: Gram-negative bacilli were the most common causative organisms and 69 % of these infections were cured .

## Item bc5cdr:test:96
Example input:
Sentence: To determine sensitivity we assessed tremor in 44 patients with obstructive lung disease after administration of cumulative doses of salbutamol .

Example answer:
{"entities": [{"text": "tremor", "type": "Disease"}, {"text": "obstructive lung disease", "type": "Disease"}, {"text": "salbutamol", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Salbutamol significantly increased tremor severity in patients in a dose-dependent way .

Example answer:
{"entities": [{"text": "Salbutamol", "type": "Chemical"}, {"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: Animals were administered nicotine , carbachol , or neostigmine via timed tail vein infusion , and the latencies to onset of tremor and clonus were recorded and converted to threshold dose .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}, {"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVE : To study tremor side effects of salbutamol an easily applicable , quick and low-priced method is needed .

Example answer:
{"entities": [{"text": "tremor", "type": "Disease"}, {"text": "salbutamol", "type": "Chemical"}]}

Example input:
Sentence: In another series of measurements , reproducibility and reference values of the tremor was assessed in 65 healthy subjects in three sessions , at 9 a.m. , 4 p.m. and 9 a.m. , respectively , 1 week later .

Example answer:
{"entities": [{"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: Tremor was measured simultaneously by two independent observers .

Example answer:
{"entities": [{"text": "Tremor", "type": "Disease"}]}

Example input:
Sentence: Tremor side effects of salbutamol , quantified by a laser pointer technique .

Example answer:
{"entities": [{"text": "Tremor", "type": "Disease"}, {"text": "salbutamol", "type": "Chemical"}]}

Example input:
Sentence: DISCUSSION : Quantifying tremor by using an inexpensive laser pointer is , with the exception of children ( < 12 years ) a sensitive and reproducible method .

Example answer:
{"entities": [{"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: Postural tremor was measured with the arm horizontally outstretched rest tremor with the arm supported by an armrest and finally tremor was measured after holding a 2-kg weight until exhaustion .

Example answer:
{"entities": [{"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: METHODS : Tremor was measured using a laser pointer technique .

Example answer:
{"entities": [{"text": "Tremor", "type": "Disease"}]}

Input:
Sentence: A method for the measurement of tremor , and a comparison of the effects of tocolytic beta-mimetics .

## Item bc5cdr:test:85
Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: These results show that ipratropium is a more potent bronchodilator than oral theophylline in patients with chronic airflow obstruction .

Example answer:
{"entities": [{"text": "ipratropium", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}, {"text": "chronic airflow obstruction", "type": "Disease"}]}

Example input:
Sentence: Improvement of levodopa-induced dyskinesia by propranolol in Parkinson 's disease .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "propranolol", "type": "Chemical"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: A randomized comparison of labetalol and nitroprusside for induced hypotension .

Example answer:
{"entities": [{"text": "labetalol", "type": "Chemical"}, {"text": "nitroprusside", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : This study confirms our previous finding that selegiline in combination with L-dopa is associated with selective orthostatic hypotension .

Example answer:
{"entities": [{"text": "selegiline", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}, {"text": "orthostatic hypotension", "type": "Disease"}]}

Example input:
Sentence: Recently , we found that therapy with selegiline and L-dopa was associated with selective systolic orthostatic hypotension which was abolished by withdrawal of selegiline .

Example answer:
{"entities": [{"text": "selegiline", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}, {"text": "systolic orthostatic hypotension", "type": "Disease"}]}

Example input:
Sentence: Since the introduction of angiotensin converting enzyme ( ACE ) inhibitors into the adjunctive treatment of patients with congestive heart failure , cases of severe hypotension , especially on the first day of treatment , have occasionally been reported .

Example answer:
{"entities": [{"text": "angiotensin converting enzyme ( ACE ) inhibitors", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: In a randomized study , labetalol-induced hypotension and nitroprusside-induced hypotension were compared in 20 patients ( 10 in each group ) scheduled for major orthopedic procedures .

Example answer:
{"entities": [{"text": "labetalol-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "nitroprusside-induced", "type": "Chemical"}]}

Example input:
Sentence: Seven patients suffering from Parkinson 's disease ( PD ) with severely disabling dyskinesia received low-dose propranolol as an adjunct to the currently used medical treatment .

Example answer:
{"entities": [{"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "propranolol", "type": "Chemical"}]}

Input:
Sentence: The studies suggest that propranolol is a useful drug in selected patients with severe idiopathic orthostatic hypotension .

## Item bc5cdr:test:238
Example input:
Sentence: The effects of oral doses of diazepam ( single dose of 10 mg and a median dose of 30 mg/day for 2 weeks ) and propranolol ( single dose of 80 mg and a median dose of 240 mg/day for 2 weeks ) on psychological performance of patients with panic disorders and agoraphobia were investigated in a double-blind , randomized and crossover design .

Example answer:
{"entities": [{"text": "diazepam", "type": "Chemical"}, {"text": "propranolol", "type": "Chemical"}, {"text": "panic disorders", "type": "Disease"}, {"text": "agoraphobia", "type": "Disease"}]}

Example input:
Sentence: Male rats were subcutaneously injected with morphine ( 10 mg/kg ) twice a day at 12 hour intervals for 10 days , and Rg1 ( 30 mg/kg ) was intraperitoneally injected 2 hours after the second injection of morphine once a day for 10 days .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "Rg1", "type": "Chemical"}]}

Example input:
Sentence: Rats treated for 11 days with morphine and withdrawn for 36-40 h showed differences in the development of tolerance : about half of the animals showed a rigidity after the test dose of morphine that was not significantly less than in the controls and were akinetic ( A group ) .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "rigidity", "type": "Disease"}, {"text": "akinetic", "type": "Disease"}]}

Example input:
Sentence: Injection of Captopril ( 1 mg/kg ) , an inhibitor of angiotensin converting enzyme ( ACE ) , reduced both pulmonary and renal insufficiency in this rat model .

Example answer:
{"entities": [{"text": "Captopril", "type": "Chemical"}, {"text": "angiotensin", "type": "Chemical"}]}

Example input:
Sentence: injections of organ specific three drugs ( AAP : 500 mg/Kg for 24 h ; AMI : 50 mg/Kg/day for four days ; DOX : 20 mg/Kg for 48 h ) .

Example answer:
{"entities": [{"text": "AAP", "type": "Chemical"}, {"text": "AMI", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: Antinociceptive effect of morphine was reduced in chronically treated rats ( 39+/-10 vs. 18+/-5 au ) while the combination-induced antinociception was remained similar as an acute treatment ( 298+/-7 vs. 280+/-17 au ) .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: This work evaluates the antinociceptive and constipating effects of the combination of 3.2 mg/kg s.c. morphine with 177.8 mg/kg s.c. metamizol in acutely and chronically treated ( once a day for 12 days ) rats .

Example answer:
{"entities": [{"text": "constipating", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}, {"text": "metamizol", "type": "Chemical"}]}

Example input:
Sentence: In conclusion , CPA , diazepam and 2PAM in combination with atropine prevented the occurrence of serious signs of poisoning and thus reduced the toxicity of DFP in rat .

Example answer:
{"entities": [{"text": "CPA", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "atropine", "type": "Chemical"}, {"text": "poisoning", "type": "Disease"}, {"text": "toxicity", "type": "Disease"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: METHODS : For a period of 2 weeks , CsA 15 mg/kg/day ( given orally ) , FK506 3.0 mg/kg/day ( given orally ) or SRL 0.4 mg/kg/day ( given intraperitoneally ) was administered once a day as these doses have earlier been found to achieve a significant immunosuppressive effect in Sprague-Dawley rats .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: The rats received AChE reactivator pralidoxime-2-chloride ( 2PAM ) ( 30.0 mg/kg BW ) , anticonvulsant diazepam ( 2.0 mg/kg BW ) , A ( 1 ) -adenosine receptor agonist N ( 6 ) -cyclopentyl adenosine ( CPA ) ( 2.0 mg/kg BW ) , NMDA-receptor antagonist dizocilpine maleate ( +-MK801 hydrogen maleate ) ( 2.0 mg/kg BW ) or their combinations with cholinolytic drug atropine sulfate ( 50.0 mg/kg BW ) immediately or 30 min after the single SC injection of DFP .

Example answer:
{"entities": [{"text": "pralidoxime-2-chloride", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "N ( 6 ) -cyclopentyl adenosine", "type": "Chemical"}, {"text": "CPA", "type": "Chemical"}, {"text": "NMDA-receptor", "type": "Chemical"}, {"text": "dizocilpine maleate", "type": "Chemical"}, {"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Input:
Sentence: injection to rats , abecarnil and diazepam decreased in a time-dependent and dose-related ( 0.25-20 mg/kg i.p . )

## Item bc5cdr:test:210
Example input:
Sentence: We report a case of a 31 year old female who required admission to the Intensive Care Unit for ventilation and full supportive therapy , following ingestion of 13.5g bupropion .

Example answer:
{"entities": [{"text": "bupropion", "type": "Chemical"}]}

Example input:
Sentence: Controlled hypotension to an average MAP of 50-55 mm Hg was induced by increasing the dose of isoflurane , and maintained at an inspired concentration of 2.2 +/- 0.2 % .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "Hg", "type": "Chemical"}, {"text": "isoflurane", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Patients with a DBP reduction of > or =20 % in the high-dose group had a significantly increased adjusted OR for the compound outcome variable death or dependency ( Barthel Index < 60 ) ( n/N=25/26 , OR 10 .

Example answer:
{"entities": [{"text": "DBP reduction", "type": "Disease"}, {"text": "death", "type": "Disease"}]}

Example input:
Sentence: infusion of morphine ( mean 73.6 mg ) and five patients receiving a continuous extradural infusion of 0.25 % bupivacaine ( mean 192 mg ) in the 24-h period following upper abdominal surgery .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: We investigated this association , according to the type of progestagen included in third-generation ( i.e. , desogestrel or gestodene ) and second-generation ( i.e. , levonorgestrel ) oral contraceptives , the dose of estrogen , and the presence or absence of prothrombotic mutations METHODS : In a nationwide , population-based , case-control study , we identified and enrolled 248 women 18 through 49 years of age who had had a first myocardial infarction between 1990 and 1995 and 925 control women who had not had a myocardial infarction and who were matched for age , calendar year of the index event , and area of residence .

Example answer:
{"entities": [{"text": "progestagen", "type": "Chemical"}, {"text": "desogestrel", "type": "Chemical"}, {"text": "gestodene", "type": "Chemical"}, {"text": "levonorgestrel", "type": "Chemical"}, {"text": "oral contraceptives", "type": "Chemical"}, {"text": "estrogen", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: The average hearing loss for speech frequencies was about 10 dB after prilocaine and 15 dB after bupivacaine .

Example answer:
{"entities": [{"text": "hearing loss", "type": "Disease"}, {"text": "prilocaine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Ninety patients classified as American Society of Anesthesiologists physical status I or II who were scheduled for short gynecologic procedures under spinal anesthesia were randomly allocated to receive 2.5 ml 2 % lidocaine in 7.5 % glucose , 2 % prilocaine in 7.5 % glucose , or 0.5 % bupivacaine in 7.5 % glucose .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "glucose", "type": "Chemical"}, {"text": "prilocaine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: Two groups of 22 similar patients were studied : one group received 6 mL prilocaine 2 % ; and the other received 3 mL bupivacaine 0.5 % .

Example answer:
{"entities": [{"text": "prilocaine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Input:
Sentence: Each concentration of progesterone ( 6.25 , 12.5 , 25 , and 50 micrograms/ml ) caused a significant and concentration-dependent reduction in the AD50 for bupivacaine .

## Item bc5cdr:test:226
Example input:
Sentence: In control rats , intravenous bromocriptine ( 150 microg/kg ) induced significant hypotension and tachycardia .

Example answer:
{"entities": [{"text": "bromocriptine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: Reports of persistent paralysis after the discontinuance of these drugs have most often involved aminosteroid-based NMBAs such as vecuronium bromide , especially when used in conjunction with corticosteroids .

Example answer:
{"entities": [{"text": "paralysis", "type": "Disease"}, {"text": "vecuronium bromide", "type": "Chemical"}]}

Example input:
Sentence: One patient was prematurely discontinued from the study for severe headache and abdominal pain .

Example answer:
{"entities": [{"text": "headache", "type": "Disease"}, {"text": "abdominal pain", "type": "Disease"}]}

Example input:
Sentence: In the present paper the authors describe 2 female patients who developed incontinence secondary to the selective serotonin reuptake inhibitors paroxetine and sertraline , as well as a third who developed this side effect on venlafaxine .

Example answer:
{"entities": [{"text": "incontinence", "type": "Disease"}, {"text": "serotonin", "type": "Chemical"}, {"text": "paroxetine", "type": "Chemical"}, {"text": "sertraline", "type": "Chemical"}, {"text": "venlafaxine", "type": "Chemical"}]}

Example input:
Sentence: Simvastatinezetimibe and escitalopram ( which she was taking for depression ) were discontinued , and other potential causes of hepatotoxicity were excluded .

Example answer:
{"entities": [{"text": "Simvastatinezetimibe", "type": "Chemical"}, {"text": "escitalopram", "type": "Chemical"}, {"text": "depression", "type": "Disease"}, {"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: These findings suggest that lowered serum prolactin levels in the early phase of bromocriptine treatment may result from an impaired secretion of prolactin due to decreasing numbers of cytoplasmic microtubules .

Example answer:
{"entities": [{"text": "bromocriptine", "type": "Chemical"}]}

Example input:
Sentence: Bromocriptine was definitely effective in cases with prolactin greater than 35 ng./ml .

Example answer:
{"entities": [{"text": "Bromocriptine", "type": "Chemical"}]}

Example input:
Sentence: It has been shown that bromocriptine-induced tachycardia , which persisted after adrenalectomy , is ( i ) mediated by central dopamine D2 receptor activation and ( ii ) reduced by 5-day isoproterenol pretreatment , supporting therefore the hypothesis that this effect is dependent on sympathetic outflow to the heart .

Example answer:
{"entities": [{"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: Bromocriptine-induced hypotension was unaffected by isoproterenol pretreatment , while tachycardia was reversed to significant bradycardia , an effect that was partly reduced by i.v .

Example answer:
{"entities": [{"text": "Bromocriptine-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Input:
Sentence: One woman , however , developed worsened psychiatric symptoms while taking bromocriptine , and it was discontinued .

## Item bc5cdr:test:519
Example input:
Sentence: The co-primary endpoint of being pain free at 2 h was also in favor of rizatriptan .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "rizatriptan", "type": "Chemical"}]}

Example input:
Sentence: Findings suggest a potential for H ( 3 ) -receptor antagonists in improving the refractory cases of schizophrenia .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSIONS : The results indicated a favorable therapeutic profile for haloperidol in doses of 2-3 mg/day , although a subgroup developed moderate to severe extrapyramidal signs .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "extrapyramidal signs", "type": "Disease"}]}

Example input:
Sentence: RESULTS : For the 60 patients who completed phase A , standard-dose haloperidol was efficacious and superior to both low-dose haloperidol and placebo for scores on the Brief Psychiatric Rating Scale psychosis factor and on psychomotor agitation .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "psychosis", "type": "Disease"}, {"text": "psychomotor agitation", "type": "Disease"}]}

Example input:
Sentence: On the other hand , pretreatment with p-chlorophenylalamine ( 3 X 320 mg/kg i.p. , 24 hr ) , a serotonin depletor , caused no significant change in the hyperactivity .

Example answer:
{"entities": [{"text": "p-chlorophenylalamine", "type": "Chemical"}, {"text": "serotonin", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}]}

Example input:
Sentence: Oral diphenhydramine and prednisone were ineffective in preventing the recurrence of the allergic reaction .

Example answer:
{"entities": [{"text": "diphenhydramine", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "allergic reaction", "type": "Disease"}]}

Example input:
Sentence: Twenty-six had minimal prior therapy ( good risk ) , 23 had extensive prior therapy ( poor risk ) , and six had renal and/or hepatic dysfunction .

Example answer:
{"entities": []}

Example input:
Sentence: A lower relative risk would be expected for acetaminophen if the risk of both drugs in combination with other analgesics was higher than the risk of either agent alone .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}]}

Example input:
Sentence: 1 h prior to haloperidol resulted in a dose-dependent increase in the catalepsy times ( P < 0.05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Based on these observations , it is concluded that 5-HT2 blockade obtained with risperidone at D2 occupancy rates of 60 % and above does not appear to protect against the risk for extrapyramidal side effects .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}]}

Input:
Sentence: Thus prior dosing with H1- and H2-antagonists provides only partial protection .

## Item bc5cdr:test:533
Example input:
Sentence: Of 24 evaluable patients , two achieved a complete remission and one achieved a partial remission for an overall response rate of 12.5 % ( 95 % confidence interval : 2.6-32.4 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Secondary outcomes were a postdose SCr increase > or = 25 % , a postdose estimated glomerular filtration rate decrease of > or = 25 % , and the mean peak change in SCr .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSIONS : The combination of cisplatin and amifostine in this study resulted in an overall response rate of 16 % .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "amifostine", "type": "Chemical"}]}

Example input:
Sentence: MAIN OUTCOME MEASURE : Odds ratios ( ORs ) measuring the association between antibacterial use and selected birth defects adjusted for potential confounders .

Example answer:
{"entities": [{"text": "birth defects", "type": "Disease"}]}

Example input:
Sentence: In multivariate analysis , three factors independently predicted mortality : serum bilirubin ( > or=10.8 mg/dL ) , prothrombin time ( PT ) prolongation ( > or=26 seconds ) , and grade III/IV encephalopathy at presentation .

Example answer:
{"entities": [{"text": "bilirubin", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Six of 30 patients ( 20 % ) without prior chemotherapy achieved a partial response ( PR ) ( 95 % confidence interval [ CI ] , 8 % to 39 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: An objective response was observed in 73.5 % of the patients ( 95 % confidence interval [ CI ] , 55.6-87.1 % ) , including 4 complete responses ( 11.7 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Prospective multicentre studies with a large population and a long follow-up should be performed in order to evaluate the incidence of this unusual side effect .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : 3MA significantly improved cardiac function and reduced mitochondrial injury .

Example answer:
{"entities": [{"text": "3MA", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Fourteen subjects completed both treatment arms .

Example answer:
{"entities": []}

Input:
Sentence: Three major results are reported .

## Item bc5cdr:test:400
Example input:
Sentence: These findings suggest that overgrowth of the exencephalic neural tissue causes the altered distribution patterns of vessels , subsequent peripheral circulatory failure and/or hemorrhaging in various parts of the exencephalic head , leading to the multiple modes of tissue reduction during transformation from exencephaly to anencephaly .

Example answer:
{"entities": [{"text": "exencephalic", "type": "Disease"}, {"text": "circulatory failure", "type": "Disease"}, {"text": "hemorrhaging", "type": "Disease"}, {"text": "exencephaly", "type": "Disease"}, {"text": "anencephaly", "type": "Disease"}]}

Example input:
Sentence: Hypertension was observed in animals that had a reduction in glomeruli as well as in a group that did not have a reduction in glomerular number , suggesting that a reduction in glomerular number is not the sole cause for the development of hypertension .

Example answer:
{"entities": [{"text": "Hypertension", "type": "Disease"}, {"text": "reduction in glomerular number", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVE : This is to present reversible inferior colliculus lesions in metronidazole-induced encephalopathy , to focus on the diffusion-weighted imaging ( DWI ) and fluid attenuated inversion recovery ( FLAIR ) imaging .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "Disease"}, {"text": "metronidazole-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: OUTCOME : Following discontinuation of LEV , EEG and neuropsychological findings improved and seizure frequency decreased .

Example answer:
{"entities": [{"text": "LEV", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Reversible inferior colliculus lesions could be considered as the characteristic for metronidazole-induced encephalopathy , next to the dentate nucleus involvement .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "Disease"}, {"text": "metronidazole-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: There is still no proof of causative effect of VPA in patients with encephalopathy , but only of an association with an assumed causal relation .

Example answer:
{"entities": [{"text": "VPA", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Two subsets of patients were identified from this latter group : the first included four patients ( 5 % of the total population ) who developed major toxicity resulting in Fanconi 's syndrome ( TDFS ) ; and the second group included five patients with elevated beta 2 microglobulinuria and low phosphate reabsorption .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "Fanconi 's syndrome", "type": "Disease"}, {"text": "TDFS", "type": "Disease"}, {"text": "phosphate", "type": "Chemical"}]}

Example input:
Sentence: Reduction in GFR was associated with the development of glomerular sclerosis in both treated and untreated rats .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: Importantly , a decrease in glutamate uptake correlates negatively with an increase in the incidence of orofacial diskinesia .

Example answer:
{"entities": [{"text": "glutamate", "type": "Chemical"}, {"text": "orofacial diskinesia", "type": "Disease"}]}

Example input:
Sentence: At presentation , advanced encephalopathy and cerebral edema were present in 51 ( 76 % ) and 29 ( 41.4 % ) patients , respectively .

Example answer:
{"entities": [{"text": "encephalopathy", "type": "Disease"}, {"text": "cerebral edema", "type": "Disease"}]}

Input:
Sentence: The relationship between the occurrence of encephalitis and the decrease in microfilaremia is evident .

## Item bc5cdr:test:405
Example input:
Sentence: We describe a 70-year-old Hispanic woman who developed fulminant hepatic failure necessitating liver transplantation 10 weeks after conversion from simvastatin 40 mg/day to simvastatin 10 mg-ezetimibe 40 mg/day .

Example answer:
{"entities": [{"text": "fulminant hepatic failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "simvastatin 10 mg-ezetimibe 40", "type": "Chemical"}]}

Example input:
Sentence: Based on this principle a 27-year old woman , classified as being in the high-risk group ( Goldstein and Berkowitz score : 11 ) , was treated with multiple cytotoxic drugs .

Example answer:
{"entities": []}

Example input:
Sentence: We report on two fatal cases of accidental intrathecal vincristine instillation in a 5-year old girl with recurrent acute lymphoblastic leucemia and a 57-year old man with lymphoblastic lymphoma .

Example answer:
{"entities": [{"text": "vincristine", "type": "Chemical"}, {"text": "acute lymphoblastic leucemia", "type": "Disease"}, {"text": "lymphoblastic lymphoma", "type": "Disease"}]}

Example input:
Sentence: CASE SUMMARY : A 40-year-old woman with major depression took an overdose of venlafaxine in an apparent suicide attempt .

Example answer:
{"entities": [{"text": "major depression", "type": "Disease"}, {"text": "overdose", "type": "Disease"}, {"text": "venlafaxine", "type": "Chemical"}]}

Example input:
Sentence: We report the case of a 63-year-old female who was treated with methylphenidate due to hyperactivity and suffered from multiple ischaemic strokes .

Example answer:
{"entities": [{"text": "methylphenidate", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "ischaemic strokes", "type": "Disease"}]}

Example input:
Sentence: A 49-year-old woman was transferred to our department because of quadriparesis , lancinating pain , sensory loss , and paresthesia of the distal limbs .

Example answer:
{"entities": [{"text": "quadriparesis", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "sensory loss", "type": "Disease"}, {"text": "paresthesia", "type": "Disease"}]}

Example input:
Sentence: Within 8 hours after initiation of therapy the patient died with a clinical picture resembling massive pulmonary obstruction due to choriocarcinomic tissue plugs , probably originating from the uterus .

Example answer:
{"entities": [{"text": "pulmonary obstruction", "type": "Disease"}]}

Example input:
Sentence: CASE : A 58-year-old man received an intracarotid injection of carboplatin for recurrent glioblastomas in his left temporal lobe .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}, {"text": "glioblastomas", "type": "Disease"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: We report a case of a 31 year old female who required admission to the Intensive Care Unit for ventilation and full supportive therapy , following ingestion of 13.5g bupropion .

Example answer:
{"entities": [{"text": "bupropion", "type": "Chemical"}]}

Input:
Sentence: We present a case in which an 89-year-old woman in a long-term care facility became confused after the initiation of misoprostol therapy .

## Item bc5cdr:test:411
Example input:
Sentence: The patient had suffered a previous episode of `` acute hepatitis of unknown origin , '' that occurred after telithromycin usage .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}, {"text": "telithromycin", "type": "Chemical"}]}

Example input:
Sentence: Histopathology analyses in the 2 animals that died revealed liver and kidney toxicity , with greater severity in the orally-treated animal .

Example answer:
{"entities": []}

Example input:
Sentence: Immune mechanisms may be involved in the drug 's hepatotoxicity , as suggested by the T-cell stimulation study reported here .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: This study is the first to demonstrate that impairment of hepatocyte TJs occurs heterogenously in the liver lobule after BDL and suggests that BDL and EE treatments produce different lobular distributions of increased paracellular permeability .

Example answer:
{"entities": [{"text": "EE", "type": "Chemical"}]}

Example input:
Sentence: Based on a score of 8 on the Naranjo adverse drug reaction probability scale , telithromycin was the probable cause of acute hepatitis in this patient , and pathological findings suggested drug-induced toxic hepatitis .

Example answer:
{"entities": [{"text": "adverse drug reaction", "type": "Disease"}, {"text": "telithromycin", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}, {"text": "toxic hepatitis", "type": "Disease"}]}

Example input:
Sentence: This type of lesion broadens the spectrum of liver injury due to this drug combination , mainly represented by a benign cholestatic syndrome .

Example answer:
{"entities": [{"text": "liver injury", "type": "Disease"}, {"text": "cholestatic syndrome", "type": "Disease"}]}

Example input:
Sentence: We report the case of a patient who developed acute hepatitis with extensive hepatocellular necrosis , 7 months after the onset of administration of clotiazepam , a thienodiazepine derivative .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}, {"text": "extensive hepatocellular necrosis", "type": "Disease"}, {"text": "clotiazepam", "type": "Chemical"}, {"text": "thienodiazepine", "type": "Chemical"}]}

Example input:
Sentence: The results suggest that a prolonged combination of more than 120 min of PGE1-induced hypotension and moderate haemodilution would cause impairment of hepatic function .

Example answer:
{"entities": [{"text": "PGE1-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}, {"text": "impairment of hepatic function", "type": "Disease"}]}

Example input:
Sentence: FINDINGS : The liver biopsy sample showed hepatocellular necrosis which was prominent in perivenular zone three and extended focally from portal tracts to portal tracts and centrilobular areas ( bridging necrosis ) .

Example answer:
{"entities": [{"text": "necrosis", "type": "Disease"}]}

Example input:
Sentence: Biochemical liver function tests indicated hepatocellular necrosis and correlated with histopathological evidence of hepatic injury , the spectrum of which ranged from fatty change and focal hepatocellular necrosis to massive hepatic necrosis .

Example answer:
{"entities": [{"text": "necrosis", "type": "Disease"}, {"text": "hepatic injury", "type": "Disease"}, {"text": "fatty change", "type": "Disease"}, {"text": "massive hepatic necrosis", "type": "Disease"}]}

Input:
Sentence: The pathophysiology underlying this acute hepatic injury is unknown .

## Item bc5cdr:test:434
Example input:
Sentence: Two patients with similar clinical features are presented : both patients had chronic renal failure , on hemodialysis for many years but recently begun on a high-flux dialyzer ; both had been receiving a carbidopa/levodopa preparation ; and both had the onset of hallucinosis and recurrent seizures , which were refractory to anticonvulsants .

Example answer:
{"entities": [{"text": "chronic renal failure", "type": "Disease"}, {"text": "carbidopa/levodopa", "type": "Chemical"}, {"text": "hallucinosis", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: The present report describes a case of cardiac arrest and subsequent death as a result of hyperkalaemia following the use of suxamethonium in a 23-year-old Malawian woman .

Example answer:
{"entities": [{"text": "cardiac arrest", "type": "Disease"}, {"text": "death", "type": "Disease"}, {"text": "hyperkalaemia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: This patient underwent a 10-month regimen of rifampin and isoniazid for pulmonary tuberculosis and was discovered to have developed signs of severe renal failure five weeks after completion of therapy .

Example answer:
{"entities": [{"text": "rifampin", "type": "Chemical"}, {"text": "isoniazid", "type": "Chemical"}, {"text": "pulmonary tuberculosis", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: RESULTS : At 13 years after OLTX , the incidence of severe renal dysfunction was 18.1 % ( CRF 8.6 % and ESRD 9.5 % ) .

Example answer:
{"entities": [{"text": "renal dysfunction", "type": "Disease"}, {"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: A patient with cryptogenic cirrhosis and disseminated sporotrichosis developed acute renal failure immediately following the administration of amphotericin B on four separate occasions .

Example answer:
{"entities": [{"text": "cirrhosis", "type": "Disease"}, {"text": "sporotrichosis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}]}

Example input:
Sentence: The second episode was more severe than the first ; and although both were treated with intensive corticosteroid therapy , renal function remained impaired .

Example answer:
{"entities": []}

Example input:
Sentence: She subsequently died some 5 weeks after the commencement of her drug therapy.Post-mortem examination showed evidence of massive hepatocellular necrosis , acute hypersensitivity myocarditis , focal acute tubulo-interstitial nephritis and extensive bone marrow necrosis , with no evidence of malignancy .

Example answer:
{"entities": [{"text": "massive hepatocellular necrosis", "type": "Disease"}, {"text": "myocarditis", "type": "Disease"}, {"text": "nephritis", "type": "Disease"}, {"text": "bone marrow necrosis", "type": "Disease"}, {"text": "malignancy", "type": "Disease"}]}

Example input:
Sentence: Two patients developed acute tubular necrosis , characterized clinically by acute oliguric renal failure , while they were receiving a combination of cephalothin sodium and gentamicin sulfate therapy .

Example answer:
{"entities": [{"text": "acute tubular necrosis", "type": "Disease"}, {"text": "cephalothin sodium", "type": "Chemical"}, {"text": "gentamicin sulfate", "type": "Chemical"}]}

Example input:
Sentence: We have reported a case of acute oliguric renal failure with hyperkalemia in a patient with cirrhosis , ascites , and cor pulmonale after indomethacin therapy .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "cor pulmonale", "type": "Disease"}, {"text": "indomethacin", "type": "Chemical"}]}

Example input:
Sentence: Gastrointestinal bleed , seizures , infection , and acute renal failure were documented in seven ( 10 % ) , five ( 7.1 % ) , 26 ( 37.1 % ) , and seven ( 10 % ) patients , respectively .

Example answer:
{"entities": [{"text": "Gastrointestinal bleed", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "infection", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}]}

Input:
Sentence: The last such episode was of acute renal failure at which stage the patient was seen by the authors of this report .

## Item bc5cdr:test:409
Example input:
Sentence: We report the case of a patient who developed acute hepatitis with extensive hepatocellular necrosis , 7 months after the onset of administration of clotiazepam , a thienodiazepine derivative .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}, {"text": "extensive hepatocellular necrosis", "type": "Disease"}, {"text": "clotiazepam", "type": "Chemical"}, {"text": "thienodiazepine", "type": "Chemical"}]}

Example input:
Sentence: Atherosclerosis could produce gastric hemorrhagic ulcer via aggravation of gastric acid back-diffusion , LPO generation , histamine release and microvascular permeability that could be ameliorated by verapamil in rats .

Example answer:
{"entities": [{"text": "Atherosclerosis", "type": "Disease"}, {"text": "gastric hemorrhagic", "type": "Disease"}, {"text": "ulcer", "type": "Disease"}, {"text": "histamine", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: After EE treatment , changes in immunostaining for 7H6 and ZO-1 were similar to those seen in periportal hepatocytes after BDL , but distributed more diffusely throughout the lobule .

Example answer:
{"entities": [{"text": "EE", "type": "Chemical"}]}

Example input:
Sentence: Although hepatocyte TJs are impaired in cholestasis , attempts to localize the precise site of hepatocyte TJ damage by freeze-fracture electron microscopy have produced limited information .

Example answer:
{"entities": [{"text": "cholestasis", "type": "Disease"}]}

Example input:
Sentence: Combined effects of prolonged prostaglandin E1 ( PGE1 ) -induced hypotension and haemodilution on hepatic function were studied in 30 patients undergoing hip surgery .

Example answer:
{"entities": [{"text": "prostaglandin E1", "type": "Chemical"}, {"text": "PGE1", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}]}

Example input:
Sentence: The results suggest that a prolonged combination of more than 120 min of PGE1-induced hypotension and moderate haemodilution would cause impairment of hepatic function .

Example answer:
{"entities": [{"text": "PGE1-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}, {"text": "impairment of hepatic function", "type": "Disease"}]}

Example input:
Sentence: Biochemical liver function tests indicated hepatocellular necrosis and correlated with histopathological evidence of hepatic injury , the spectrum of which ranged from fatty change and focal hepatocellular necrosis to massive hepatic necrosis .

Example answer:
{"entities": [{"text": "necrosis", "type": "Disease"}, {"text": "hepatic injury", "type": "Disease"}, {"text": "fatty change", "type": "Disease"}, {"text": "massive hepatic necrosis", "type": "Disease"}]}

Example input:
Sentence: Combined effects of prolonged prostaglandin E1-induced hypotension and haemodilution on human hepatic function .

Example answer:
{"entities": [{"text": "prostaglandin", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}]}

Example input:
Sentence: The aim of this study is to examine the role of gastric acid back-diffusion , mast cell histamine release , lipid peroxide ( LPO ) generation and mucosal microvascular permeability in modulating gastric hemorrhage and ulcer in rats with atherosclerosis induced by coadministration of vitamin D2 and cholesterol .

Example answer:
{"entities": [{"text": "histamine", "type": "Chemical"}, {"text": "gastric hemorrhage", "type": "Disease"}, {"text": "ulcer", "type": "Disease"}, {"text": "atherosclerosis", "type": "Disease"}, {"text": "vitamin D2", "type": "Chemical"}, {"text": "cholesterol", "type": "Chemical"}]}

Example input:
Sentence: This study is the first to demonstrate that impairment of hepatocyte TJs occurs heterogenously in the liver lobule after BDL and suggests that BDL and EE treatments produce different lobular distributions of increased paracellular permeability .

Example answer:
{"entities": [{"text": "EE", "type": "Chemical"}]}

Input:
Sentence: Hepatocellular oxidant stress following intestinal ischemia-reperfusion injury .

## Item bc5cdr:test:438
Example input:
Sentence: In a 37-year-old woman with documented pentazocine-induced fibrous myopathy of triceps and deltoid muscles bilaterally and a three-week history of right wrist drop , electrodiagnostic examination showed a severe but partial lesion of the right radial nerve distal to the branches to the triceps , in addition to the fibrous myopathy .

Example answer:
{"entities": [{"text": "pentazocine-induced", "type": "Chemical"}, {"text": "fibrous myopathy", "type": "Disease"}]}

Example input:
Sentence: One of the twins developed complete heart block and dilated cardiomyopathy related to lopinavir/ritonavir therapy , a boosted protease-inhibitor agent , while the other twin developed mild bradycardia .

Example answer:
{"entities": [{"text": "heart block", "type": "Disease"}, {"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "lopinavir/ritonavir", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Histological and immunohistochemical investigations ( HE-LFB , CD-68 , Neurofilament ) revealed degeneration of myelin and axons as well as pseudocystic transformation in areas exposed to vincristine , accompanied by secondary changes with numerous prominent macrophages .

Example answer:
{"entities": [{"text": "pseudocystic transformation", "type": "Disease"}, {"text": "vincristine", "type": "Chemical"}]}

Example input:
Sentence: Isoniazid was the most frequent agent in drug-induced neuropathy .

Example answer:
{"entities": [{"text": "Isoniazid", "type": "Chemical"}, {"text": "neuropathy", "type": "Disease"}]}

Example input:
Sentence: Anticoagulant-induced femoral nerve palsy represents the most common form of warfarin-induced peripheral neuropathy ; it is characterized by severe pain in the inguinal region , varying degrees of motor and sensory impairment , and flexure contracture of the involved extremity .

Example answer:
{"entities": [{"text": "femoral nerve palsy", "type": "Disease"}, {"text": "warfarin-induced", "type": "Chemical"}, {"text": "peripheral neuropathy", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "motor and sensory impairment", "type": "Disease"}, {"text": "contracture", "type": "Disease"}]}

Example input:
Sentence: The full syndrome of subacute myelo-optic neuropathy was more frequent in women , but they tended to have taken greater quantities of the drug .

Example answer:
{"entities": []}

Example input:
Sentence: We report a case of a 51-year-old man who developed severe , disabling negative myoclonus of the upper and lower extremities after the infusion of ifosfamide for plasmacytoma .

Example answer:
{"entities": [{"text": "myoclonus", "type": "Disease"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "plasmacytoma", "type": "Disease"}]}

Example input:
Sentence: This was a case of acute palsy of the recurrent laryngeal nerve and superimposed severe acute sensorimotor axonal polyneuropathy caused by high-dose disulfiram intoxication .

Example answer:
{"entities": [{"text": "palsy", "type": "Disease"}, {"text": "polyneuropathy", "type": "Disease"}, {"text": "disulfiram", "type": "Chemical"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Input:
Sentence: Both cases developed axonal neuropathy with motor predominance in the lower extremities 1 and 6 months after IT chemotherapy was administered .

## Item bc5cdr:test:8
Example input:
Sentence: These data indicate that a critical percentage of NTE inhibition in brain and spinal cord sampled shortly after Mipafox exposure can predict neuropathic damage in rats several weeks later .

Example answer:
{"entities": [{"text": "Mipafox", "type": "Chemical"}, {"text": "neuropathic damage", "type": "Disease"}]}

Example input:
Sentence: Following major intracranial surgery in a 35-year-old man , sodium pentothal was intravenously infused to minimize cerebral ischaemia .

Example answer:
{"entities": [{"text": "sodium pentothal", "type": "Chemical"}, {"text": "cerebral ischaemia", "type": "Disease"}]}

Example input:
Sentence: NRA0160 and clozapine significantly shortened the phencyclidine ( PCP ) -induced prolonged swimming latency in rats in a water maze task .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "phencyclidine", "type": "Chemical"}, {"text": "PCP", "type": "Chemical"}]}

Example input:
Sentence: NFkappaB activity was decreased in the frontal cortex of cocaine treated rats , as well as GSH concentration and glutathione peroxidase activity in the hippocampus , whereas nNOS activity in the hippocampus was increased .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}]}

Example input:
Sentence: Brain and spinal cord NTE activities were measured in Long-Evans male rats 1 hr post-exposure to various dosages of Mipafox ( ip , 1-15 mg/kg ) .

Example answer:
{"entities": [{"text": "Mipafox", "type": "Chemical"}]}

Example input:
Sentence: In the absence of caffeine , acetaminophen ( up to 300 mg/kg ) did not modify the seizures induced by maximal electroshock and did not alter the convulsant dose of pentylenetetrezol in mice ( tests performed by the Anticonvulsant Screening Project of NINCDS ) .

Example answer:
{"entities": [{"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "pentylenetetrezol", "type": "Chemical"}]}

Example input:
Sentence: Fibrous myopathy is a common , well-known side effect of repeated pentazocine injection .

Example answer:
{"entities": [{"text": "Fibrous myopathy", "type": "Disease"}, {"text": "pentazocine", "type": "Chemical"}]}

Example input:
Sentence: Dissociated learning of rats in the normal state and the state of amnesia produced by pentobarbital ( 15 mg/kg , ip ) was carried out .

Example answer:
{"entities": [{"text": "amnesia", "type": "Disease"}, {"text": "pentobarbital", "type": "Chemical"}]}

Example input:
Sentence: Compression neuropathy of the radial nerve due to pentazocine-induced fibrous myopathy .

Example answer:
{"entities": [{"text": "pentazocine-induced", "type": "Chemical"}, {"text": "fibrous myopathy", "type": "Disease"}]}

Example input:
Sentence: However , compression neuropathy due to fibrotic muscle affected by pentazocine-induced myopathy has not previously been reported .

Example answer:
{"entities": [{"text": "compression neuropathy", "type": "Disease"}, {"text": "pentazocine-induced", "type": "Chemical"}, {"text": "myopathy", "type": "Disease"}]}

Input:
Sentence: Pentazocine dose-dependently decreased the brain level of NA .

## Item bc5cdr:test:55
Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Histological studies demonstrated that the rats developed an infarct 18 h after isoproterenol administration .

Example answer:
{"entities": [{"text": "infarct", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: Changes evoked by a single intraperitoneal injection of rilmenidine ( 600 microg/kg ) or alpha-methyldopa ( 100 mg/kg ) , selective I1- and alpha2-receptor agonists , respectively , in blood pressure , hemodynamic variability , and locomotor activity were assessed in radiotelemetered sham-operated and ovariectomized ( Ovx ) Sprague-Dawley female rats with or without 12-wk estrogen replacement .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "estrogen", "type": "Chemical"}]}

Example input:
Sentence: In isolated perfused heart preparations from isoproterenol-pretreated rats , the isoproterenol-induced maximal increase in left ventricular systolic pressure was significantly reduced , compared with saline-pretreated rats ( the EC50 of the isoproterenol-induced increase in left ventricular systolic pressure was enhanced approximately 22-fold ) .

Example answer:
{"entities": [{"text": "isoproterenol-pretreated", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: The rats received AChE reactivator pralidoxime-2-chloride ( 2PAM ) ( 30.0 mg/kg BW ) , anticonvulsant diazepam ( 2.0 mg/kg BW ) , A ( 1 ) -adenosine receptor agonist N ( 6 ) -cyclopentyl adenosine ( CPA ) ( 2.0 mg/kg BW ) , NMDA-receptor antagonist dizocilpine maleate ( +-MK801 hydrogen maleate ) ( 2.0 mg/kg BW ) or their combinations with cholinolytic drug atropine sulfate ( 50.0 mg/kg BW ) immediately or 30 min after the single SC injection of DFP .

Example answer:
{"entities": [{"text": "pralidoxime-2-chloride", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "N ( 6 ) -cyclopentyl adenosine", "type": "Chemical"}, {"text": "CPA", "type": "Chemical"}, {"text": "NMDA-receptor", "type": "Chemical"}, {"text": "dizocilpine maleate", "type": "Chemical"}, {"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/", "type": "Chemical"}, {"text": "K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}]}

Example input:
Sentence: d-1 given for 4 weeks , elevated blood pressure from 102+/-13 to 152+/-15 mm Hg and increased the synthesis of ET-1 and the levels of ET-1 mRNA in the mesenteric artery ( 240 % and 230 % , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: In unanesthetized , spontaneously hypertensive rats the decrease in blood pressure and heart rate produced by intravenous clonidine , 5 to 20 micrograms/kg , was inhibited or reversed by nalozone , 0.2 to 2 mg/kg .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}, {"text": "clonidine", "type": "Chemical"}, {"text": "nalozone", "type": "Chemical"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Rats were given a single dose of adriamycin and one month later divided into four groups matched for albuminuria , blood pressure , and plasma albumin concentration .

Example answer:
{"entities": [{"text": "adriamycin", "type": "Chemical"}, {"text": "albuminuria", "type": "Disease"}]}

Input:
Sentence: After a single oral dose of 4 mg/kg indomethacin ( IDM ) to sodium and volume depleted rats plasma renin activity ( PRA ) and systolic blood pressure fell significantly within four hours .

## Item bc5cdr:test:583
Example input:
Sentence: Doses were set at 0.3 , 3.0 and 30.0mg/kg for piroxicam and 0.2 , 2.0 and 20.0mg/kg for DFU .

Example answer:
{"entities": [{"text": "piroxicam", "type": "Chemical"}, {"text": "DFU", "type": "Chemical"}]}

Example input:
Sentence: Six additional patients received a 30-mg i.v .

Example answer:
{"entities": []}

Example input:
Sentence: or theophylline ( 3 mg/kg i.v . ) .

Example answer:
{"entities": [{"text": "theophylline", "type": "Chemical"}]}

Example input:
Sentence: Both , Ro4368554 ( 3 and 10 mg/kg , intraperitoneally ( i.p . ) )

Example answer:
{"entities": []}

Example input:
Sentence: For compounds that have shown TDP in the clinic ( terfenadine , terodiline , cisapride ) there is little differentiation between the dog ED50 and the efficacious free plasma concentrations in man ( < 10-fold ) reflecting their limited safety margins .

Example answer:
{"entities": [{"text": "TDP", "type": "Disease"}, {"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}]}

Example input:
Sentence: The median dose-intensity ( DI ) was 20 mg/m2/wk .

Example answer:
{"entities": []}

Example input:
Sentence: In the in vivo study , the administration ( 50 mg/kg , i.p . )

Example answer:
{"entities": []}

Example input:
Sentence: These data indicate that the free ED50 in plasma for terfenadine ( 1.9 nM ) , terodiline ( 76 nM ) , cisapride ( 11 nM ) and E4031 ( 1.9 nM ) closely correlate with the free concentration in man causing QT effects .

Example answer:
{"entities": [{"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}, {"text": "E4031", "type": "Chemical"}]}

Example input:
Sentence: A dose of 50 mg/kg is recommended in those without audiogram abnormalities .

Example answer:
{"entities": []}

Example input:
Sentence: Finally , we examined the low dose of 150 mg/kg ( 50 mg/kg per day ) using a similar washout period .

Example answer:
{"entities": []}

Input:
Sentence: The ED50 doses were 16 mg/kg for i.v .

## Item bc5cdr:test:29
Example input:
Sentence: Analysis was performed on 61 women with chemotherapy-responsive metastatic breast cancer receiving 96-h infusional cyclophosphamide as part of a triple sequential high-dose regimen to assess association between presence of peritransplant congestive heart failure ( CHF ) and the following pretreatment characteristics : presence of electrocardiogram ( EKG ) abnormalities , age , hypertension , prior cardiac history , smoking , diabetes mellitus , prior use of anthracyclines , and left-sided chest irradiation .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "CHF", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "diabetes mellitus", "type": "Disease"}, {"text": "anthracyclines", "type": "Chemical"}]}

Example input:
Sentence: Endocrine therapy consisted of testosterone heptylate or human chorionic gonadotropin for hypogonadism and bromocriptine for hyperprolactinemia .

Example answer:
{"entities": [{"text": "testosterone heptylate", "type": "Chemical"}, {"text": "hypogonadism", "type": "Disease"}, {"text": "bromocriptine", "type": "Chemical"}, {"text": "hyperprolactinemia", "type": "Disease"}]}

Example input:
Sentence: Multiple cytotoxic drug administration is the generally accepted treatment of patients with a high-risk stage of choriocarcinoma .

Example answer:
{"entities": [{"text": "choriocarcinoma", "type": "Disease"}]}

Example input:
Sentence: It has shown promising results alone or in combination with other chemotherapeutic agents in colorectal , breast , pancreaticobiliary , gastric , renal cell and head and neck cancers .

Example answer:
{"entities": []}

Example input:
Sentence: Forty-three ovarian cancer patients were available for analysis following six cycles of the same PAC-containing regimen : 23 had been supplemented by glutamate all along the treatment period , at a daily dose of three times 500 mg ( group G ) , and 20 had received a placebo ( group P ) .

Example answer:
{"entities": [{"text": "ovarian cancer", "type": "Disease"}, {"text": "PAC-containing", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: Five patients with carcinoma developed thrombotic microangiopathy ( characterized by renal insufficiency , microangiopathic hemolytic anemia , and usually thrombocytopenia ) after treatment with cisplatin , bleomycin , and a vinca alkaloid .

Example answer:
{"entities": [{"text": "carcinoma", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "microangiopathic hemolytic anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "bleomycin", "type": "Chemical"}, {"text": "vinca alkaloid", "type": "Chemical"}]}

Example input:
Sentence: Tamoxifen ( TAM ) , the antiestrogenic drug most widely prescribed in the chemotherapy of breast cancer , induces changes in normal discoid shape of erythrocytes and hemolytic anemia .

Example answer:
{"entities": [{"text": "Tamoxifen", "type": "Chemical"}, {"text": "TAM", "type": "Chemical"}, {"text": "breast cancer", "type": "Disease"}, {"text": "hemolytic anemia", "type": "Disease"}]}

Example input:
Sentence: Within 8 hours after initiation of therapy the patient died with a clinical picture resembling massive pulmonary obstruction due to choriocarcinomic tissue plugs , probably originating from the uterus .

Example answer:
{"entities": [{"text": "pulmonary obstruction", "type": "Disease"}]}

Example input:
Sentence: Two cases of clear cell adenocarcinoma of the vagina detected at follow-up in young women exposed in utero to diethylstilbestrol are reported .

Example answer:
{"entities": [{"text": "diethylstilbestrol", "type": "Chemical"}]}

Example input:
Sentence: Outcomes included venous thromboembolism , cataracts , gallbladder disease , and endometrial hyperplasia or cancer .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "cataracts", "type": "Disease"}, {"text": "gallbladder disease", "type": "Disease"}]}

Input:
Sentence: 4 cases of endometrial carcinoma referred from elsewhere demonstrated the problems of inappropriate and unsupervised unopposed oestrogen therapy and the difficulty in distinguishing severe hyperplasia from malignancy .

## Item bc5cdr:test:202
Example input:
Sentence: PD female rats also showed increased ( 3 ) H-haloperidol binding and decreased dopamine transporter binding in striatum .

Example answer:
{"entities": [{"text": "H-haloperidol", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: Across the doses and pretreatment times examined , enhancement was not observed in females .

Example answer:
{"entities": []}

Example input:
Sentence: The effects of METH in CX3CR1 knockout mice were not gender-dependent and did not extend beyond the striatum .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}]}

Example input:
Sentence: Despite therapy with ursodeoxycholic acid , prednisone , and then tacrolimus , her cholestatic disease was unrelenting , with cirrhosis shown by biopsy 6 months after presentation .

Example answer:
{"entities": [{"text": "ursodeoxycholic acid", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "cholestatic disease", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}]}

Example input:
Sentence: In conclusion , the present study demonstrates gender differences in the development of the apomorphine-induced aggressive behavior and indicates that the female rats do not fill the validation criteria for use in this method .

Example answer:
{"entities": [{"text": "apomorphine-induced", "type": "Chemical"}, {"text": "aggressive behavior", "type": "Disease"}]}

Example input:
Sentence: In males , the non-competitive NMDA antagonist dextromethorphan enhanced the antihyperalgesic effect of low to moderate doses of morphine in a dose-and time-dependent manner .

Example answer:
{"entities": [{"text": "NMDA", "type": "Chemical"}, {"text": "dextromethorphan", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: In the present study , we have investigated the molecular mechanisms by which female hormones influence cholesterol metabolism in macrophages in response to the HIV protease inhibitor ritonavir .

Example answer:
{"entities": [{"text": "cholesterol", "type": "Chemical"}, {"text": "ritonavir", "type": "Chemical"}]}

Example input:
Sentence: Enhancement of morphine antinociception by dextromethorphan was seen in both males and females in the acute pain models , with the magnitude of this effect being greater in males .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "dextromethorphan", "type": "Chemical"}, {"text": "acute pain", "type": "Disease"}]}

Example input:
Sentence: Sex differences in NMDA antagonist enhancement of morphine antihyperalgesia in a capsaicin model of persistent pain : comparisons to two models of acute pain .

Example answer:
{"entities": [{"text": "NMDA", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}, {"text": "capsaicin", "type": "Chemical"}, {"text": "pain", "type": "Disease"}, {"text": "acute pain", "type": "Disease"}]}

Example input:
Sentence: In males , estradiol increased the total damage score .

Example answer:
{"entities": [{"text": "estradiol", "type": "Chemical"}]}

Input:
Sentence: These differences between the sexes could not be related to altered disposition of tetracycline or altered uptake of oleic acid .

## Item bc5cdr:test:201
Example input:
Sentence: Phenobarbitone-induced enlargement of the liver in the rat : its relationship to carbon tetrachloride-induced cirrhosis .

Example answer:
{"entities": [{"text": "Phenobarbitone-induced", "type": "Chemical"}, {"text": "enlargement of the liver", "type": "Disease"}, {"text": "carbon", "type": "Chemical"}, {"text": "cirrhosis", "type": "Disease"}]}

Example input:
Sentence: The incidence of preneoplastic nodules and of hepatocellular carcinomas was 10 % and 37 % , respectively , in rats fed the plain choline-devoid diet , and 17 % and 30 % , in rats fed the phenobarbital-containing choline-devoid diet .

Example answer:
{"entities": [{"text": "hepatocellular carcinomas", "type": "Disease"}, {"text": "choline-devoid", "type": "Chemical"}, {"text": "phenobarbital-containing", "type": "Chemical"}]}

Example input:
Sentence: PD female rats also showed increased ( 3 ) H-haloperidol binding and decreased dopamine transporter binding in striatum .

Example answer:
{"entities": [{"text": "H-haloperidol", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: The cataleptogenic effect of THC was significantly reduced in rats treated with 6-OHDA and in rats with lesions of the locus coeruleus but not in rats treated with desipramine and 6-OHDA , as compared with control rats .

Example answer:
{"entities": [{"text": "THC", "type": "Chemical"}, {"text": "6-OHDA", "type": "Chemical"}, {"text": "desipramine", "type": "Chemical"}]}

Example input:
Sentence: The effects of METH in CX3CR1 knockout mice were not gender-dependent and did not extend beyond the striatum .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}]}

Example input:
Sentence: Pregnant rats were administered one of these calcium channel blockers during the period of cardiac morphogenesis and the offspring examined on day 20 of gestation for cardiovascular malformations .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "cardiovascular malformations", "type": "Disease"}]}

Example input:
Sentence: Pregnant rats were given either vehicle or 2 daily intraperitoneal injections of dexamethasone ( 0.2 mg/kg body weight ) on gestational days 11 and 12 , 13 and 14 , 15 and 16 , 17 and 18 , or 19 and 20 .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}]}

Example input:
Sentence: We report that prenatally protein deprived ( PD ) female rats showed an increased stereotypic response to apomorphine and an increased locomotor response to amphetamine in adulthood .

Example answer:
{"entities": [{"text": "apomorphine", "type": "Chemical"}, {"text": "amphetamine", "type": "Chemical"}]}

Example input:
Sentence: Male Wistar rats were challenged intragastrically once daily for 9 days with 1.0 ml/kg of corn oil containing vitamin D2 and cholesterol to induce atherosclerosis .

Example answer:
{"entities": [{"text": "vitamin D2", "type": "Chemical"}, {"text": "cholesterol", "type": "Chemical"}, {"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: The yield of severe cirrhosis of the liver ( defined as a shrunken finely nodular liver with micronodular histology , ascites greater than 30 ml , plasma albumin less than 2.2 g/dl , splenomegaly 2-3 times normal , and testicular atrophy approximately half normal weight ) after 12 doses of carbon tetrachloride given intragastrically in the phenobarbitone-primed rat was increased from 25 % to 56 % by giving the initial `` calibrating '' dose of carbon tetrachloride at the peak of the phenobarbitone-induced enlargement of the liver .

Example answer:
{"entities": [{"text": "cirrhosis of the liver", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "splenomegaly", "type": "Disease"}, {"text": "atrophy", "type": "Disease"}, {"text": "carbon tetrachloride", "type": "Chemical"}, {"text": "phenobarbitone-primed", "type": "Chemical"}, {"text": "phenobarbitone-induced", "type": "Chemical"}, {"text": "enlargement of the liver", "type": "Disease"}]}

Input:
Sentence: However , livers from female , and especially pregnant female rats , were strikingly resistant to the effects of tetracycline on depression of output of triglyceride under these experimental conditions .

## Item bc5cdr:test:119
Example input:
Sentence: Statins can cause a necrotizing myopathy and hyperCKaemia which is reversible on cessation of the drug .

Example answer:
{"entities": [{"text": "Statins", "type": "Chemical"}, {"text": "myopathy", "type": "Disease"}, {"text": "hyperCKaemia", "type": "Disease"}]}

Example input:
Sentence: The first patient died without a diagnosis ; the second patient had a dramatic recovery following the administration of vitamin B6 .

Example answer:
{"entities": [{"text": "vitamin B6", "type": "Chemical"}]}

Example input:
Sentence: The fits ceased within 4 hours of administering intramuscular pyridoxine , suggesting an aetiology of pyridoxine deficiency secondary to isoniazid medication .

Example answer:
{"entities": [{"text": "fits", "type": "Disease"}, {"text": "pyridoxine", "type": "Chemical"}, {"text": "isoniazid", "type": "Chemical"}]}

Example input:
Sentence: Estrogen replacement ( 17beta-estradiol subcutaneous pellet , 14.2 microg/day , 12 wk ) of Ovx rats restored the hemodynamic and locomotor effects of alpha-methyldopa to sham-operated levels .

Example answer:
{"entities": [{"text": "17beta-estradiol", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}]}

Example input:
Sentence: The mechanism of this myopathy is uncertain but may involve the induction by statins of an endoplasmic reticulum stress response with associated up-regulation of MHC-I expression and antigen presentation by muscle fibres .

Example answer:
{"entities": [{"text": "myopathy", "type": "Disease"}, {"text": "statins", "type": "Chemical"}]}

Example input:
Sentence: These observations suggest that statins may initiate an immune-mediated myopathy that persists after withdrawal of the drug and responds to immunosuppressive therapy .

Example answer:
{"entities": [{"text": "statins", "type": "Chemical"}, {"text": "myopathy", "type": "Disease"}]}

Example input:
Sentence: GSPE+drug exposed tissues exhibited minor residual damage or near total recovery .

Example answer:
{"entities": [{"text": "GSPE+drug", "type": "Chemical"}]}

Example input:
Sentence: Liver enlargement and muscle wastage occurred in Wistar rats following the subcutaneous administration of prednisolone .

Example answer:
{"entities": [{"text": "Liver enlargement", "type": "Disease"}, {"text": "muscle wastage", "type": "Disease"}, {"text": "prednisolone", "type": "Chemical"}]}

Example input:
Sentence: What is less well known is a phenomenon whereby statins may induce a myopathy , which persists or may progress after stopping the drug .

Example answer:
{"entities": [{"text": "statins", "type": "Chemical"}, {"text": "myopathy", "type": "Disease"}]}

Example input:
Sentence: This view supports the contention that the liver and muscle are independent sites of prednisolone action .

Example answer:
{"entities": [{"text": "prednisolone", "type": "Chemical"}]}

Input:
Sentence: The authors conclude by affirming the undoubted efficacy of the anabolizing steroids in experimental myopathic disease , but they have reservations as to the transfer of the results into the human field , where high dosage can not be carried out continuously because of the effects of the drug on virility ; because the tissue injury too often occurs at an irreversible stage vis-a-vis the `` regeneration '' of the muscle tissue ; and finally because the dystrophic injurious agent is certainly not the lack of vitamin E but something as yet unknown .

## Item bc5cdr:test:34
Example input:
Sentence: Oral diphenhydramine and prednisone were ineffective in preventing the recurrence of the allergic reaction .

Example answer:
{"entities": [{"text": "diphenhydramine", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "allergic reaction", "type": "Disease"}]}

Example input:
Sentence: Azathioprine treatment benefited 19 ( 66 % ) out of 29 patients suffering from severe psoriasis .

Example answer:
{"entities": [{"text": "Azathioprine", "type": "Chemical"}, {"text": "psoriasis", "type": "Disease"}]}

Example input:
Sentence: This case suggests that the psychotic symptoms that occur following phenytoin treatment in some epileptic patients may be the direct result of medication , unrelated to seizures .

Example answer:
{"entities": [{"text": "psychotic symptoms", "type": "Disease"}, {"text": "phenytoin", "type": "Chemical"}, {"text": "epileptic", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Nitrofurantoins were associated with anophthalmia or microphthalmos ( AOR = 3.7 ; 95 % CI , 1.1-12.2 ) , hypoplastic left heart syndrome ( AOR = 4.2 ; 95 % CI , 1.9-9.1 ) , atrial septal defects ( AOR = 1.9 ; 95 % CI , 1.1-3.4 ) , and cleft lip with cleft palate ( AOR = 2.1 ; 95 % CI , 1.2-3.9 ) .

Example answer:
{"entities": [{"text": "Nitrofurantoins", "type": "Chemical"}, {"text": "anophthalmia", "type": "Disease"}, {"text": "microphthalmos", "type": "Disease"}, {"text": "hypoplastic left heart syndrome", "type": "Disease"}, {"text": "atrial septal defects", "type": "Disease"}, {"text": "cleft lip", "type": "Disease"}, {"text": "cleft palate", "type": "Disease"}]}

Example input:
Sentence: Veno-occlusive liver disease after dacarbazine therapy ( DTIC ) for melanoma .

Example answer:
{"entities": [{"text": "Veno-occlusive liver disease", "type": "Disease"}, {"text": "dacarbazine", "type": "Chemical"}, {"text": "DTIC", "type": "Chemical"}, {"text": "melanoma", "type": "Disease"}]}

Example input:
Sentence: A case of veno-occlusive disease of the liver with fatal outcome after dacarbazine ( DTIC ) therapy for melanoma is reported .

Example answer:
{"entities": [{"text": "veno-occlusive disease of the liver", "type": "Disease"}, {"text": "dacarbazine", "type": "Chemical"}, {"text": "DTIC", "type": "Chemical"}, {"text": "melanoma", "type": "Disease"}]}

Example input:
Sentence: Pneumonitis , bilateral pleural effusions , echocardiographic evidence of cardiac tamponade , and positive autoantibodies developed in a 43-year-old man , who was receiving long-term sulfasalazine therapy for chronic ulcerative colitis .

Example answer:
{"entities": [{"text": "Pneumonitis", "type": "Disease"}, {"text": "pleural effusions", "type": "Disease"}, {"text": "cardiac tamponade", "type": "Disease"}, {"text": "sulfasalazine", "type": "Chemical"}, {"text": "ulcerative colitis", "type": "Disease"}]}

Example input:
Sentence: The case of a nonepileptic patient who developed psychosis following phenytoin treatment for trigeminal neuralgia is described .

Example answer:
{"entities": [{"text": "psychosis", "type": "Disease"}, {"text": "phenytoin", "type": "Chemical"}, {"text": "trigeminal neuralgia", "type": "Disease"}]}

Example input:
Sentence: Disulfiram-like syndrome after hydrogen cyanamide professional skin exposure : two case reports in France .

Example answer:
{"entities": [{"text": "Disulfiram-like", "type": "Chemical"}, {"text": "hydrogen cyanamide", "type": "Chemical"}]}

Example input:
Sentence: A 34-year-old lady developed a constellation of dermatitis , fever , lymphadenopathy and hepatitis , beginning on the 17th day of a course of oral sulphasalazine for sero-negative rheumatoid arthritis .

Example answer:
{"entities": [{"text": "dermatitis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "lymphadenopathy", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Input:
Sentence: Skin rash is a well-known complication of diphenylhydantoin treatment as is benign and malignant lymphadenopathy .

## Item bc5cdr:test:121
Example input:
Sentence: Severe rhabdomyolysis and acute renal failure secondary to concomitant use of simvastatin , amiodarone , and atazanavir .

Example answer:
{"entities": [{"text": "rhabdomyolysis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND/AIMS : Recently ribavirin has been found to inhibit angiogenesis and a number of angiogenesis inhibitors such as sunitinib and sorafenib have been found to cause acute hemolysis .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "sunitinib", "type": "Chemical"}, {"text": "sorafenib", "type": "Chemical"}, {"text": "hemolysis", "type": "Disease"}]}

Example input:
Sentence: A case is reported of the hemolytic uremic syndrome ( HUS ) in a woman taking oral contraceptives .

Example answer:
{"entities": [{"text": "hemolytic uremic syndrome", "type": "Disease"}, {"text": "HUS", "type": "Disease"}, {"text": "oral contraceptives", "type": "Chemical"}]}

Example input:
Sentence: Acute hepatitis , autoimmune hemolytic anemia , and erythroblastocytopenia induced by ceftriaxone .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}, {"text": "autoimmune hemolytic anemia", "type": "Disease"}, {"text": "erythroblastocytopenia", "type": "Disease"}, {"text": "ceftriaxone", "type": "Chemical"}]}

Example input:
Sentence: The mechanism by which omeprazole caused the patient 's hemolytic anemia is uncertain , but physicians should be alerted to this possible adverse effect .

Example answer:
{"entities": [{"text": "omeprazole", "type": "Chemical"}, {"text": "hemolytic anemia", "type": "Disease"}]}

Example input:
Sentence: A Cambodian woman with hemoglobin E trait ( AE ) and leprosy developed a Heinz body hemolytic anemia while taking a dose of dapsone ( 50 mg/day ) not usually associated with clinical hemolysis .

Example answer:
{"entities": [{"text": "leprosy", "type": "Disease"}, {"text": "hemolytic anemia", "type": "Disease"}, {"text": "dapsone", "type": "Chemical"}, {"text": "hemolysis", "type": "Disease"}]}

Example input:
Sentence: Although the transaminases gradually returned to baseline after withholding the beta lactam antibiotic , there was a gradual increase in serum bilirubin and a decrease in hemoglobin concentration caused by an autoimmune hemolytic anemia and erythroblastocytopenia .

Example answer:
{"entities": [{"text": "beta lactam", "type": "Chemical"}, {"text": "bilirubin", "type": "Chemical"}, {"text": "autoimmune hemolytic anemia", "type": "Disease"}, {"text": "erythroblastocytopenia", "type": "Disease"}]}

Example input:
Sentence: Two patients developed acute tubular necrosis , characterized clinically by acute oliguric renal failure , while they were receiving a combination of cephalothin sodium and gentamicin sulfate therapy .

Example answer:
{"entities": [{"text": "acute tubular necrosis", "type": "Disease"}, {"text": "cephalothin sodium", "type": "Chemical"}, {"text": "gentamicin sulfate", "type": "Chemical"}]}

Example input:
Sentence: A patient with cryptogenic cirrhosis and disseminated sporotrichosis developed acute renal failure immediately following the administration of amphotericin B on four separate occasions .

Example answer:
{"entities": [{"text": "cirrhosis", "type": "Disease"}, {"text": "sporotrichosis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}]}

Example input:
Sentence: Two weeks after the initiation of therapy , her hematocrit had decreased from 44.1 % to 20.4 % , and she had a positive direct Coombs antiglobulin test and an elevated indirect bilirubin .

Example answer:
{"entities": [{"text": "bilirubin", "type": "Chemical"}]}

Input:
Sentence: A patient with renal disease developed Coombs-positive hemolytic anemia while receiving cephalothin therapy .

## Item bc5cdr:test:593
Example input:
Sentence: Increasing doses of catecholamines , sedatives , and muscle relaxants administered through a central venous catheter were ineffective .

Example answer:
{"entities": [{"text": "catecholamines", "type": "Chemical"}]}

Example input:
Sentence: infusions of morphine and regional analgesia by extradural block .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: Stroke followed cocaine use by inhalation , intranasal , intravenous , and intramuscular routes .

Example answer:
{"entities": [{"text": "Stroke", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: The sudden onset of respiratory distress , rash , and a history of a new medicine led the two paramedics on the scene to administer subcutaneous epinephrine .

Example answer:
{"entities": [{"text": "respiratory distress", "type": "Disease"}, {"text": "rash", "type": "Disease"}, {"text": "epinephrine", "type": "Chemical"}]}

Example input:
Sentence: A board-certified emergency physician skilled in airway management supervised administration of the anesthetic , and the patients were monitored by a registered nurse .

Example answer:
{"entities": []}

Example input:
Sentence: Based on these data , a plan of management was developed that allows effective yet safe administration of deferoxamine .

Example answer:
{"entities": [{"text": "deferoxamine", "type": "Chemical"}]}

Example input:
Sentence: administration does not contribute to bladder damage .

Example answer:
{"entities": [{"text": "bladder damage", "type": "Disease"}]}

Example input:
Sentence: The management options in the ED , as exemplified by four individual case reports , in particular the use of a minimally invasive method of intracorporal epinephrine instillation , are discussed .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}]}

Example input:
Sentence: administration were apparent earlier and sometimes lasted longer than those following oral administration .

Example answer:
{"entities": []}

Example input:
Sentence: routes to groups of volunteers and its effects compared .

Example answer:
{"entities": []}

Input:
Sentence: routes of administration .

## Item bc5cdr:test:156
Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: The results indicated that concomitant treatment with gum Arabic and GM significantly increased creatinine and urea by about 183 and 239 % , respectively ( compared to 432 and 346 % , respectively , in rats treated with cellulose and GM ) , and decreased that of cortical GSH by 21 % ( compared to 27 % in the cellulose plus GM group ) The GM-induced proximal tubular necrosis appeared to be slightly less severe in rats given GM together with gum Arabic than in those given GM and cellulose .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}, {"text": "urea", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "GM-induced", "type": "Chemical"}, {"text": "tubular necrosis", "type": "Disease"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/", "type": "Chemical"}, {"text": "K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : This rat study demonstrated a synergistic nephrotoxic effect of CsA plus SRL , whereas FK506 plus SRL was better tolerated .

Example answer:
{"entities": [{"text": "nephrotoxic", "type": "Disease"}, {"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: In the present work we assessed the effect of treatment of rats with gum Arabic on acute renal failure induced by gentamicin ( GM ) nephrotoxicity .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}]}

Example input:
Sentence: Thirty minutes after 99mTc-glucarate administration the standardised heart uptake value S ( h ) UV was 4.7 in infarcted rat heart which is six times more than in normal rats .

Example answer:
{"entities": [{"text": "99mTc-glucarate", "type": "Chemical"}]}

Example input:
Sentence: HS diet for 4 wk caused a progressive increase in BP , protein and albumin excretion , and glomerular sclerosis in male DS rats , which were attenuated by castration .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: 99mTc-glucarate for detection of isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "99mTc-glucarate", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: 99mTc-glucarate was easy to prepare , stable for 96 h and was used to study its biodistribution in rats with isoproterenol-induced acute myocardial infarction .

Example answer:
{"entities": [{"text": "99mTc-glucarate", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Input:
Sentence: Effect of D-Glucarates on basic antibiotic-induced renal damage in rats .

## Item bc5cdr:test:208
Example input:
Sentence: Histological studies demonstrated that the rats developed an infarct 18 h after isoproterenol administration .

Example answer:
{"entities": [{"text": "infarct", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: Bromocriptine-induced hypotension was unaffected by isoproterenol pretreatment , while tachycardia was reversed to significant bradycardia , an effect that was partly reduced by i.v .

Example answer:
{"entities": [{"text": "Bromocriptine-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: It has been shown that bromocriptine-induced tachycardia , which persisted after adrenalectomy , is ( i ) mediated by central dopamine D2 receptor activation and ( ii ) reduced by 5-day isoproterenol pretreatment , supporting therefore the hypothesis that this effect is dependent on sympathetic outflow to the heart .

Example answer:
{"entities": [{"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: Chronic hyperprolactinemia induced by the dopamine antagonist sulpiride caused a 40 % reduction LH pulse frequency in ovariectomized rats , but only in the presence of chronic low levels of estradiol .

Example answer:
{"entities": [{"text": "hyperprolactinemia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "sulpiride", "type": "Chemical"}, {"text": "estradiol", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: In isolated perfused heart preparations from isoproterenol-pretreated rats , the isoproterenol-induced maximal increase in left ventricular systolic pressure was significantly reduced , compared with saline-pretreated rats ( the EC50 of the isoproterenol-induced increase in left ventricular systolic pressure was enhanced approximately 22-fold ) .

Example answer:
{"entities": [{"text": "isoproterenol-pretreated", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: The effects of exercise on the severity of isoproterenol-induced myocardial infarction were studied in female albino rats of 20,40,60 and 80 weeks of age .

Example answer:
{"entities": [{"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Effects of long-term pretreatment with isoproterenol on bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Input:
Sentence: The effects of progesterone treatment on bupivacaine arrhythmogenicity in beating rat heart myocyte cultures and on anesthetized rats were determined .

## Item bc5cdr:test:374
Example input:
Sentence: To develop a more sensitive echocardiographic screening test for cardiac damage due to doxorubicin , a cohort study was performed using dobutamine infusion to differentiate asymptomatic long-term survivors of childhood cancer treated with doxorubicin from healthy control subjects .

Example answer:
{"entities": [{"text": "cardiac damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: Interestingly , all the drugs , such as , AAP , AMI and DOX induced apoptotic death in addition to necrosis in the respective organs which was very effectively blocked by GSPE .

Example answer:
{"entities": [{"text": "AAP", "type": "Chemical"}, {"text": "AMI", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "necrosis", "type": "Disease"}, {"text": "GSPE", "type": "Chemical"}]}

Example input:
Sentence: In the present study , we investigated the changes occurring at the protein level in striatal samples obtained from the unilaterally 6-hydroxydopamine-lesion rat model of PD treated with saline , L-DOPA or bromocriptine using two-dimensional difference gel electrophoresis and mass spectrometry ( MS ) .

Example answer:
{"entities": [{"text": "6-hydroxydopamine-lesion", "type": "Chemical"}, {"text": "PD", "type": "Disease"}, {"text": "L-DOPA", "type": "Chemical"}, {"text": "bromocriptine", "type": "Chemical"}]}

Example input:
Sentence: We investigated the diagnostic value of cTnI and cTnT for the diagnosis of myocardial damage in a rat model of doxorubicin ( DOX ) -induced cardiomyopathy , and we examined the relationship between serial cTnI and cTnT with the development of cardiac disorders monitored by echocardiography and histological examinations in this model .

Example answer:
{"entities": [{"text": "myocardial damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiac disorders", "type": "Disease"}]}

Example input:
Sentence: Histologic changes were found in rat kidneys after administration of MTX , CY and NG , while no such change was observed after 5-FU and joint administration of MTX + 5-FU + CY compared to controls .

Example answer:
{"entities": [{"text": "MTX", "type": "Chemical"}, {"text": "CY", "type": "Chemical"}, {"text": "NG", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}]}

Example input:
Sentence: Dopamine turnover ratios ( DOPAC : DA and HVA : DA ) were found to be lower in those animals exposed to the exploratory box when compared to their home cage counterparts .

Example answer:
{"entities": [{"text": "Dopamine", "type": "Chemical"}, {"text": "DOPAC", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}, {"text": "HVA", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Eighteen of the DOX rats died prematurely of general toxicity during the 9-week period .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Histological evaluation of hearts from all rats given DOX revealed significant slight degrees of perivascular and interstitial fibrosis .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: Although there was a discrepancy between the amount of cTnI and cTnT after DOX , probably due to heterogeneity in cross-reactivities of mAbs to various cTnI and cTnT forms , it is likely that cTnT in rats after DOX indicates cell damage determined by the magnitude of injury induced and that cTnT should be a useful marker for the prediction of experimentally induced cardiotoxicity and possibly for cardioprotective experiments .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Among markers of ischemic injury after DOX in rats , cTnT showed the greatest ability to detect myocardial damage assessed by echocardiographic detection and histological changes .

Example answer:
{"entities": [{"text": "ischemic injury", "type": "Disease"}, {"text": "DOX", "type": "Chemical"}, {"text": "myocardial damage", "type": "Disease"}]}

Input:
Sentence: In addition , no significant histological change was observed in the heart of animals that received DOX in the form of HPMA copolymer conjugates and were killed at the end of the study .

## Item bc5cdr:test:58
Example input:
Sentence: Twenty-four patients with recurrent Grade I to IV astrocytomas , whose resection and irradiation therapy had failed , received two to eight courses of intra-arterial BCNU therapy .

Example answer:
{"entities": [{"text": "astrocytomas", "type": "Disease"}, {"text": "BCNU", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVE : The outcome of subarachnoid hemorrhage associated with cocaine abuse is reportedly poor .

Example answer:
{"entities": [{"text": "subarachnoid hemorrhage", "type": "Disease"}, {"text": "cocaine abuse", "type": "Disease"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: A 78-year-old with healed septal necrosis suffered a recurrent myocardial infarction of the anterior wall following the administration of isosorbide dinitrate 5 mg sublingually .

Example answer:
{"entities": [{"text": "necrosis", "type": "Disease"}, {"text": "myocardial infarction", "type": "Disease"}, {"text": "isosorbide dinitrate", "type": "Chemical"}]}

Example input:
Sentence: The results suggest a possible involvement of the renin-angiotensin system in the development of puromycin aminonucleoside-induced nephrosis .

Example answer:
{"entities": [{"text": "puromycin", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: Reactive oxygen species have been implicated in the pathogenesis of acute puromycin aminonucleoside ( PAN ) -induced nephropathy , with antioxidants significantly reducing the proteinuria .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: Induction of intravascular coagulation and inhibition of fibrinolysis by injection of thrombin and tranexamic acid ( AMCA ) in the rat gives rise to pulmonary and renal insufficiency resembling that occurring after trauma or sepsis in man .

Example answer:
{"entities": [{"text": "intravascular coagulation", "type": "Disease"}, {"text": "tranexamic acid", "type": "Chemical"}, {"text": "AMCA", "type": "Chemical"}, {"text": "trauma", "type": "Disease"}, {"text": "sepsis", "type": "Disease"}]}

Example input:
Sentence: Puromycin aminonucleoside nephrosis was induced by single intraperitoneal injection of puromycin aminonucleoside ( PAN , 20 mg/100g BW ) .

Example answer:
{"entities": [{"text": "Puromycin aminonucleoside", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: Five patients with carcinoma developed thrombotic microangiopathy ( characterized by renal insufficiency , microangiopathic hemolytic anemia , and usually thrombocytopenia ) after treatment with cisplatin , bleomycin , and a vinca alkaloid .

Example answer:
{"entities": [{"text": "carcinoma", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "microangiopathic hemolytic anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "bleomycin", "type": "Chemical"}, {"text": "vinca alkaloid", "type": "Chemical"}]}

Example input:
Sentence: Thrombotic microangiopathy and renal failure associated with antineoplastic chemotherapy .

Example answer:
{"entities": [{"text": "Thrombotic microangiopathy", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Input:
Sentence: Recurrent subarachnoid hemorrhage associated with aminocaproic acid therapy and acute renal artery thrombosis .

## Item bc5cdr:test:505
Example input:
Sentence: The authors present three patients with de novo absence epilepsy after administration of carbamazepine and vigabatrin .

Example answer:
{"entities": [{"text": "absence epilepsy", "type": "Disease"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "vigabatrin", "type": "Chemical"}]}

Example input:
Sentence: Similar to rats , systemic pilocarpine injection causes status epilepticus ( SE ) and the eventual development of spontaneous seizures and mossy fiber sprouting in C57BL/6 and CD1 mice , but the physiological correlates of these events have not been identified in mice .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: NRA0160 and clozapine significantly induced catalepsy in rats , although their effects did not exceed 50 % induction even at the highest dose given .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}]}

Example input:
Sentence: Animals were administered nicotine , carbachol , or neostigmine via timed tail vein infusion , and the latencies to onset of tremor and clonus were recorded and converted to threshold dose .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}, {"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: Infarcts in substantia nigra pars reticulata were evoked by prolonged pilocarpine-induced status epilepticus .

Example answer:
{"entities": [{"text": "Infarcts in substantia nigra pars reticulata", "type": "Disease"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}]}

Example input:
Sentence: He developed acute neurologic symptoms of mental confusion , disorientation and irritability , and then lapsed into a deep coma , lasting for approximately 40 hours during the first dose ( day 2 ) of 5-fluorouracil and folinic acid infusion .

Example answer:
{"entities": [{"text": "confusion", "type": "Disease"}, {"text": "disorientation", "type": "Disease"}, {"text": "irritability", "type": "Disease"}, {"text": "coma", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: The administration of several benzodiazepines , chemically related to clotiazepam , did not interfere with recovery and did not induce any relapse of hepatitis .

Example answer:
{"entities": [{"text": "benzodiazepines", "type": "Chemical"}, {"text": "clotiazepam", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: In six of the probable cases the neurological disturbance consisted of an acute reversible encephalopathy usually related to the ingestion of a high dose of clioquinol over a short period .

Example answer:
{"entities": [{"text": "neurological disturbance", "type": "Disease"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "clioquinol", "type": "Chemical"}]}

Example input:
Sentence: We report the case of a patient who developed acute hepatitis with extensive hepatocellular necrosis , 7 months after the onset of administration of clotiazepam , a thienodiazepine derivative .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}, {"text": "extensive hepatocellular necrosis", "type": "Disease"}, {"text": "clotiazepam", "type": "Chemical"}, {"text": "thienodiazepine", "type": "Chemical"}]}

Example input:
Sentence: The patient with nitrazepam overdose and two of those with chlormethiazole intoxication conformed to the criteria of 'alpha coma ' , showing non-reactive generalized or frontally predominant alpha activity in the EEG .

Example answer:
{"entities": [{"text": "nitrazepam", "type": "Chemical"}, {"text": "overdose", "type": "Disease"}, {"text": "chlormethiazole", "type": "Chemical"}, {"text": "coma", "type": "Disease"}]}

Input:
Sentence: infusion of clonazepam ; none had any neurological symptoms .

## Item bc5cdr:test:525
Example input:
Sentence: In Mg ( 2+ ) -free bathing medium containing bicuculline , conditions designed to increase excitability in the slices , electrical stimulation of the hilus resulted in a single population spike in granule cells from control mice and pilocarpine-treated mice that did not experience SE .

Example answer:
{"entities": [{"text": "Mg", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "pilocarpine-treated", "type": "Chemical"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Given alone to any accumbal subregion , GR 55562 ( 0.1-10 microg/side ) or CP 93129 ( 0.1-10 microg/side ) did not change basal locomotor activity .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: The results indicated that concomitant treatment with gum Arabic and GM significantly increased creatinine and urea by about 183 and 239 % , respectively ( compared to 432 and 346 % , respectively , in rats treated with cellulose and GM ) , and decreased that of cortical GSH by 21 % ( compared to 27 % in the cellulose plus GM group ) The GM-induced proximal tubular necrosis appeared to be slightly less severe in rats given GM together with gum Arabic than in those given GM and cellulose .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}, {"text": "urea", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "GM-induced", "type": "Chemical"}, {"text": "tubular necrosis", "type": "Disease"}]}

Example input:
Sentence: In control rats , immunostaining for 7H6 and ZO-1 colocalized to outline bile canaliculi in a continuous fashion .

Example answer:
{"entities": []}

Example input:
Sentence: The in vitro data suggest that the site responsible for the decrease in seizure activity 24 h after gamma-HCH may be the GABA-A receptor-linked chloride channel .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}, {"text": "GABA-A", "type": "Chemical"}]}

Example input:
Sentence: Such attenuation was not found in animals which had been injected with GR 55562 into the accumbens core .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}]}

Example input:
Sentence: A decreased glutamate uptake was observed in the subcortical parts of animals treated with reserpine and haloperidol , compared to the control .

Example answer:
{"entities": [{"text": "glutamate", "type": "Chemical"}, {"text": "reserpine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: We found that ( i ) gabapentin reduced the activations in the bilateral operculoinsular cortex , independently of the presence of central sensitization ; ( ii ) gabapentin reduced the activation in the brainstem , only during central sensitization ; ( iii ) gabapentin suppressed stimulus-induced deactivations , only during central sensitization ; this effect was more robust than the effect on brain activation .

Example answer:
{"entities": [{"text": "gabapentin", "type": "Chemical"}]}

Example input:
Sentence: In addition , a statistically significant reduction was also observed on the level of GABA and glycine but less than a drastic reduction of glutamate and aspartate level .

Example answer:
{"entities": [{"text": "GABA", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Input:
Sentence: The concentration of GABA was only slightly but significantly decreased in the colliculi without modifications in the other areas .

## Item bc5cdr:test:205
Example input:
Sentence: Five patients with carcinoma developed thrombotic microangiopathy ( characterized by renal insufficiency , microangiopathic hemolytic anemia , and usually thrombocytopenia ) after treatment with cisplatin , bleomycin , and a vinca alkaloid .

Example answer:
{"entities": [{"text": "carcinoma", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "microangiopathic hemolytic anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "bleomycin", "type": "Chemical"}, {"text": "vinca alkaloid", "type": "Chemical"}]}

Example input:
Sentence: Central nervous system ( CNS ) complications during treatment of childhood acute lymphoblastic leukemia ( ALL ) remain a challenging clinical problem .

Example answer:
{"entities": [{"text": "Central nervous system ( CNS ) complications", "type": "Disease"}, {"text": "acute lymphoblastic leukemia", "type": "Disease"}, {"text": "ALL", "type": "Disease"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Example input:
Sentence: Twenty children with acute lymphoblastic leukemia who developed meningeal disease were treated with a high-dose intravenous methotrexate regimen that was designed to achieve and maintain CSF methotrexate concentrations of 10 ( -5 ) mol/L without the need for concomitant intrathecal dosing .

Example answer:
{"entities": [{"text": "acute lymphoblastic leukemia", "type": "Disease"}, {"text": "meningeal disease", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: Valproic acid induced encephalopathy -- 19 new cases in Germany from 1994 to 2003 -- a side effect associated to VPA-therapy not only in young children .

Example answer:
{"entities": [{"text": "Valproic acid", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "VPA-therapy", "type": "Chemical"}]}

Example input:
Sentence: A better controlled regimen for administering vincristine and intrathecal chemotherapy is recommended .

Example answer:
{"entities": [{"text": "vincristine", "type": "Chemical"}]}

Example input:
Sentence: The girl died seven days , the man four weeks after intrathecal injection of vincristine .

Example answer:
{"entities": [{"text": "vincristine", "type": "Chemical"}]}

Example input:
Sentence: Histological and immunohistochemical investigations ( HE-LFB , CD-68 , Neurofilament ) revealed degeneration of myelin and axons as well as pseudocystic transformation in areas exposed to vincristine , accompanied by secondary changes with numerous prominent macrophages .

Example answer:
{"entities": [{"text": "pseudocystic transformation", "type": "Disease"}, {"text": "vincristine", "type": "Chemical"}]}

Example input:
Sentence: Fatal myeloencephalopathy due to accidental intrathecal vincristin administration : a report of two cases .

Example answer:
{"entities": [{"text": "myeloencephalopathy", "type": "Disease"}, {"text": "vincristin", "type": "Chemical"}]}

Example input:
Sentence: We report on two fatal cases of accidental intrathecal vincristine instillation in a 5-year old girl with recurrent acute lymphoblastic leucemia and a 57-year old man with lymphoblastic lymphoma .

Example answer:
{"entities": [{"text": "vincristine", "type": "Chemical"}, {"text": "acute lymphoblastic leucemia", "type": "Disease"}, {"text": "lymphoblastic lymphoma", "type": "Disease"}]}

Input:
Sentence: Vincristine was accidentally given intrathecally to a child with leukaemia , producing sensory and motor dysfunction followed by encephalopathy and death .

## Item bc5cdr:test:298
Example input:
Sentence: In this patient , renal artery stenosis combined with heart failure and diuretic therapy certainly resulted in a strong activation of the renin-angiotensin system ( RAS ) .

Example answer:
{"entities": [{"text": "renal artery stenosis", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}]}

Example input:
Sentence: This case study reveals an unusual finding of rapidly proliferative crescentic glomerulonephritis in a patient treated with rifampin who had no other identifiable causes for developing this disease .

Example answer:
{"entities": [{"text": "glomerulonephritis", "type": "Disease"}, {"text": "rifampin", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND/AIMS : Recently ribavirin has been found to inhibit angiogenesis and a number of angiogenesis inhibitors such as sunitinib and sorafenib have been found to cause acute hemolysis .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "sunitinib", "type": "Chemical"}, {"text": "sorafenib", "type": "Chemical"}, {"text": "hemolysis", "type": "Disease"}]}

Example input:
Sentence: We report a case of ranitidine-induced acute interstitial nephritis in a recipient of a cadaveric renal allograft presenting with acute allograft dysfunction within 48 hours of exposure to the drug .

Example answer:
{"entities": [{"text": "ranitidine-induced", "type": "Chemical"}, {"text": "interstitial nephritis", "type": "Disease"}]}

Example input:
Sentence: Two patients developed acute tubular necrosis , characterized clinically by acute oliguric renal failure , while they were receiving a combination of cephalothin sodium and gentamicin sulfate therapy .

Example answer:
{"entities": [{"text": "acute tubular necrosis", "type": "Disease"}, {"text": "cephalothin sodium", "type": "Chemical"}, {"text": "gentamicin sulfate", "type": "Chemical"}]}

Example input:
Sentence: Severe rhabdomyolysis and acute renal failure secondary to concomitant use of simvastatin , amiodarone , and atazanavir .

Example answer:
{"entities": [{"text": "rhabdomyolysis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: A patient with cryptogenic cirrhosis and disseminated sporotrichosis developed acute renal failure immediately following the administration of amphotericin B on four separate occasions .

Example answer:
{"entities": [{"text": "cirrhosis", "type": "Disease"}, {"text": "sporotrichosis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}]}

Example input:
Sentence: Crescentic fibrillary glomerulonephritis associated with intermittent rifampin therapy for pulmonary tuberculosis .

Example answer:
{"entities": [{"text": "glomerulonephritis", "type": "Disease"}, {"text": "rifampin", "type": "Chemical"}, {"text": "pulmonary tuberculosis", "type": "Disease"}]}

Example input:
Sentence: We propose that amphotericin , in the setting of reduced effective arterial volume , may activate tubuloglomerular feedback , thereby contributing to acute renal failure .

Example answer:
{"entities": [{"text": "amphotericin", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: This patient underwent a 10-month regimen of rifampin and isoniazid for pulmonary tuberculosis and was discovered to have developed signs of severe renal failure five weeks after completion of therapy .

Example answer:
{"entities": [{"text": "rifampin", "type": "Chemical"}, {"text": "isoniazid", "type": "Chemical"}, {"text": "pulmonary tuberculosis", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Input:
Sentence: Intravascular hemolysis and acute renal failure following intermittent rifampin therapy .

## Item bc5cdr:test:303
Example input:
Sentence: A 34-year-old lady developed a constellation of dermatitis , fever , lymphadenopathy and hepatitis , beginning on the 17th day of a course of oral sulphasalazine for sero-negative rheumatoid arthritis .

Example answer:
{"entities": [{"text": "dermatitis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "lymphadenopathy", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Example input:
Sentence: We report the case of a patient with amoxicillin-clavulanic acid-induced hepatitis with histologic multiple granulomas .

Example answer:
{"entities": [{"text": "amoxicillin-clavulanic", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}, {"text": "granulomas", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : Here we report a case of acute hepatitis probably associated with the administration of telithromycin .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}, {"text": "telithromycin", "type": "Chemical"}]}

Example input:
Sentence: The remaining patient in the series developed fulminant hepatitis when the drug was accidentally recommenced 1 year after a prior episode of methyldopa-induced hepatitis .

Example answer:
{"entities": [{"text": "fulminant hepatitis", "type": "Disease"}, {"text": "methyldopa-induced", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: We describe a 70-year-old Hispanic woman who developed fulminant hepatic failure necessitating liver transplantation 10 weeks after conversion from simvastatin 40 mg/day to simvastatin 10 mg-ezetimibe 40 mg/day .

Example answer:
{"entities": [{"text": "fulminant hepatic failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "simvastatin 10 mg-ezetimibe 40", "type": "Chemical"}]}

Example input:
Sentence: Two patients with type II diabetes mellitus developed an acute hepatitis-like syndrome soon after initiation of glyburide therapy .

Example answer:
{"entities": [{"text": "type II diabetes mellitus", "type": "Disease"}, {"text": "acute hepatitis-like syndrome", "type": "Disease"}, {"text": "glyburide", "type": "Chemical"}]}

Example input:
Sentence: Here , we report two cases of severely immunocompromised HIV-infected patients who developed severe intrahepatic cholestasis , and in one patient lesions mimicking liver abscess formation on radiologic exams , during co-trimoxazole treatment for PCP .

Example answer:
{"entities": [{"text": "HIV-infected", "type": "Disease"}, {"text": "intrahepatic cholestasis", "type": "Disease"}, {"text": "liver abscess", "type": "Disease"}, {"text": "co-trimoxazole", "type": "Chemical"}, {"text": "PCP", "type": "Disease"}]}

Example input:
Sentence: Based on a score of 8 on the Naranjo adverse drug reaction probability scale , telithromycin was the probable cause of acute hepatitis in this patient , and pathological findings suggested drug-induced toxic hepatitis .

Example answer:
{"entities": [{"text": "adverse drug reaction", "type": "Disease"}, {"text": "telithromycin", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}, {"text": "toxic hepatitis", "type": "Disease"}]}

Example input:
Sentence: We report the case of a patient who developed acute hepatitis with extensive hepatocellular necrosis , 7 months after the onset of administration of clotiazepam , a thienodiazepine derivative .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}, {"text": "extensive hepatocellular necrosis", "type": "Disease"}, {"text": "clotiazepam", "type": "Chemical"}, {"text": "thienodiazepine", "type": "Chemical"}]}

Example input:
Sentence: An 80-yr-old man developed acute hepatitis shortly after ingesting oral ceftriaxone .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}, {"text": "ceftriaxone", "type": "Chemical"}]}

Input:
Sentence: A case of acute hepatitis induced by zidovudine in a 38-year-old patient with AIDS is presented .

## Item bc5cdr:test:241
Example input:
Sentence: NRA0160 and clozapine significantly shortened the phencyclidine ( PCP ) -induced prolonged swimming latency in rats in a water maze task .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "phencyclidine", "type": "Chemical"}, {"text": "PCP", "type": "Chemical"}]}

Example input:
Sentence: The present study was designed to study the effect of histamine H ( 3 ) -receptor ligands on neuroleptic-induced catalepsy , apomorphine-induced climbing behavior and amphetamine-induced locomotor activities in mice .

Example answer:
{"entities": [{"text": "histamine", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "apomorphine-induced", "type": "Chemical"}, {"text": "amphetamine-induced", "type": "Chemical"}]}

Example input:
Sentence: Acetaminophen ( up to 150 micrograms/mL ) did not retard the incorporation of radioactive adenosine into ATP in slices of rat cerebral cortex .

Example answer:
{"entities": [{"text": "Acetaminophen", "type": "Chemical"}, {"text": "adenosine", "type": "Chemical"}, {"text": "ATP", "type": "Chemical"}]}

Example input:
Sentence: The locomotor activity was decreased from corresponding controls in all strains studied , except for the ICR mice , during an overnight drug-free period following the fourth amantadine treatment .

Example answer:
{"entities": [{"text": "amantadine", "type": "Chemical"}]}

Example input:
Sentence: The initial dose of amantadine depressed locomotor activity in all mouse strains studied with the BALB/C mice being the most sensitive .

Example answer:
{"entities": [{"text": "amantadine", "type": "Chemical"}, {"text": "depressed", "type": "Disease"}]}

Example input:
Sentence: The rats received AChE reactivator pralidoxime-2-chloride ( 2PAM ) ( 30.0 mg/kg BW ) , anticonvulsant diazepam ( 2.0 mg/kg BW ) , A ( 1 ) -adenosine receptor agonist N ( 6 ) -cyclopentyl adenosine ( CPA ) ( 2.0 mg/kg BW ) , NMDA-receptor antagonist dizocilpine maleate ( +-MK801 hydrogen maleate ) ( 2.0 mg/kg BW ) or their combinations with cholinolytic drug atropine sulfate ( 50.0 mg/kg BW ) immediately or 30 min after the single SC injection of DFP .

Example answer:
{"entities": [{"text": "pralidoxime-2-chloride", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "N ( 6 ) -cyclopentyl adenosine", "type": "Chemical"}, {"text": "CPA", "type": "Chemical"}, {"text": "NMDA-receptor", "type": "Chemical"}, {"text": "dizocilpine maleate", "type": "Chemical"}, {"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: Mouse strain-dependent effect of amantadine on motility and brain biogenic amines .

Example answer:
{"entities": [{"text": "amantadine", "type": "Chemical"}, {"text": "amines", "type": "Chemical"}]}

Example input:
Sentence: In vitro , gamma-HCH , pentylenetetrazol and picrotoxin were shown to inhibit 3H-TBOB binding in mouse whole brain , with IC50 values of 4.6 , 404 and 9.4 microM , respectively .

Example answer:
{"entities": [{"text": "gamma-HCH", "type": "Chemical"}, {"text": "pentylenetetrazol", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "3H-TBOB", "type": "Chemical"}]}

Example input:
Sentence: Subsequent amantadine treatments produced enhancement of motility from corresponding control in all mouse strains with the BALB/C mice being the least sensitive .

Example answer:
{"entities": [{"text": "amantadine", "type": "Chemical"}]}

Example input:
Sentence: Amantadine treatment produced a biphasic effect on mouse motility .

Example answer:
{"entities": [{"text": "Amantadine", "type": "Chemical"}]}

Input:
Sentence: To better correlate the biochemical and the pharmacological effects , we studied the action of abecarnil on [ 35S ] TBPS binding , exploratory motility and on isoniazid-induced biochemical and pharmacological effects in mice .

## Item bc5cdr:test:385
Example input:
Sentence: Furthermore , it was found that the magnitude of attentional modulation in secondary hyperalgesia is very similar to that of capsaicin-untreated , control condition .

Example answer:
{"entities": [{"text": "hyperalgesia", "type": "Disease"}, {"text": "capsaicin-untreated", "type": "Chemical"}]}

Example input:
Sentence: Attentional modulation of perceived pain intensity in capsaicin-induced secondary hyperalgesia .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "capsaicin-induced", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}]}

Example input:
Sentence: In order to address long-term pain memory , nine healthy male volunteers received intradermal injections of three doses of capsaicin ( 0.05 , 1 and 20 microg , separated by 15 min breaks ) , each given three times in a balanced design across three sessions at one week intervals .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: Capsaicin ( 0.01-1 mm ) applied to oral or nasal mucosa induced increases in dural and cortical blood flow and provoked lacrimation .

Example answer:
{"entities": [{"text": "Capsaicin", "type": "Chemical"}, {"text": "increases in dural and cortical blood flow", "type": "Disease"}]}

Example input:
Sentence: To this end , persistent hyperalgesia was induced by administration of capsaicin in the tail of gonadally intact F344 rats , following which the tail was immersed in a mildly noxious thermal stimulus , and tail-withdrawal latencies measured .

Example answer:
{"entities": [{"text": "hyperalgesia", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: Our findings , showing no interaction between capsaicin treatment and attentional modulation suggest that capsaicin-induced secondary hyperalgesia and attention might affect mechanical pain through independent mechanisms .

Example answer:
{"entities": [{"text": "capsaicin", "type": "Chemical"}, {"text": "capsaicin-induced", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: However , it is not known that how pain intensity ratings are affected by attention in capsaicin-induced secondary hyperalgesia .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "capsaicin-induced", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}]}

Example input:
Sentence: Explicit episodic memory for sensory-discriminative components of capsaicin-induced pain : immediate and delayed ratings .

Example answer:
{"entities": [{"text": "capsaicin-induced", "type": "Chemical"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: Subjects were able to reliably discriminate pain magnitude and duration across capsaicin doses ( both p < 0.001 ) , regardless of whether first-time ratings were requested immediately , after one hour or after one day .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: Capsaicin injection reliably induced a dose-dependent flare ( p < 0.001 ) without any difference within or across sessions .

Example answer:
{"entities": [{"text": "Capsaicin", "type": "Chemical"}]}

Input:
Sentence: Treatment response was not correlated with the incidence , time-course or severity of capsaicin-induced burning .

## Item bc5cdr:test:495
Example input:
Sentence: The area under the plasma concentration time curve at 90 min was 4-12 times greater than for oral drug , suggesting the existence of an absorption-limiting process in the intestine , and providing an alternate form of administration for quaternary drugs .

Example answer:
{"entities": []}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Increasing doses of catecholamines , sedatives , and muscle relaxants administered through a central venous catheter were ineffective .

Example answer:
{"entities": [{"text": "catecholamines", "type": "Chemical"}]}

Example input:
Sentence: For the cytoprotection study , animals were orally gavaged 100 mg/Kg GSPE for 7-10 days followed by i.p .

Example answer:
{"entities": [{"text": "GSPE", "type": "Chemical"}]}

Example input:
Sentence: Anaesthesia was maintained with an inspired isoflurane concentration of 0.75 % ( plus 67 % nitrous oxide in oxygen ) , during which CBF and CMRO2 were 34.3 +/- 2.1 ml/100 g min-1 and 2.32 +/- 0.16 ml/100 g min-1 at PaCO2 4.1 +/- 0.1 kPa ( mean +/- SEM ) .

Example answer:
{"entities": [{"text": "isoflurane", "type": "Chemical"}, {"text": "nitrous oxide", "type": "Chemical"}, {"text": "oxygen", "type": "Chemical"}]}

Example input:
Sentence: This resulted in a significant decrease in CMRO2 ( to 1.73 +/- 0.16 ml/100 g min-1 ) , while CBF was unchanged .

Example answer:
{"entities": []}

Example input:
Sentence: Response rates according to three sets of criteria were greater with the standard dose ( 55 % -60 % ) than the low dose ( 25 % -35 % ) and placebo ( 25 % -30 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: A slow bolus of subhypnotic doses of ketamine ( 0.25 mg/kg or 0.50 mg/kg ) was given to 10 cancer patients whose pain was unrelieved by morphine in a randomized , double-blind , crossover , double-dose study .

Example answer:
{"entities": [{"text": "ketamine", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: Rats were treated with the vehicle ( 2 mL/kg of distilled water and 5 % w/v cellulose , 10 days ) , gum Arabic ( 2 mL/kg of a 10 % w/v aqueous suspension of gum Arabic powder , orally for 10 days ) , or gum Arabic concomitantly with GM ( 80mg/kg/day intramuscularly , during the last six days of the treatment period ) .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}]}

Example input:
Sentence: For compounds that have shown TDP in the clinic ( terfenadine , terodiline , cisapride ) there is little differentiation between the dog ED50 and the efficacious free plasma concentrations in man ( < 10-fold ) reflecting their limited safety margins .

Example answer:
{"entities": [{"text": "TDP", "type": "Disease"}, {"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}]}

Input:
Sentence: It was concluded that formulations at or below 0.5 per cent CHP may prove acceptable for wound care , but the vehicle system needs pharmaceutical improvement to render it more tolerable and easier to use .
