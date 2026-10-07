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

## Item bc5cdr:test:555
Example input:
Sentence: The aim of this study was to examine further the renal function , including morphological analysis of the kidneys of male Sprague-Dawley rats treated with either cyclosporine A ( CsA ) , tacrolimus ( FK506 ) or SRL as monotherapies or in different combinations .

Example answer:
{"entities": [{"text": "cyclosporine A", "type": "Chemical"}, {"text": "CsA", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: We compared the effects of 17beta-estradiol in adult male and ovariectomized female rats subjected to lithium-pilocarpine-induced SE .

Example answer:
{"entities": [{"text": "17beta-estradiol", "type": "Chemical"}, {"text": "lithium-pilocarpine-induced", "type": "Chemical"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Interestingly , estradiol also induced PRL-R , SOCS-3 , and CIS mRNA levels independently .

Example answer:
{"entities": [{"text": "estradiol", "type": "Chemical"}]}

Example input:
Sentence: Immunohistochemical , electron microscopic and morphometric studies of estrogen-induced rat prolactinomas after bromocriptine treatment .

Example answer:
{"entities": [{"text": "estrogen-induced", "type": "Chemical"}, {"text": "prolactinomas", "type": "Disease"}, {"text": "bromocriptine", "type": "Chemical"}]}

Example input:
Sentence: 17beta-Estradiol reduced the argyrophilic neurons in the CA1 and CA3-C sectors of ovariectomized rats .

Example answer:
{"entities": [{"text": "17beta-Estradiol", "type": "Chemical"}]}

Example input:
Sentence: Pituitary tumors were induced in F344 female rats by chronic treatment with diethylstilbestrol ( DES , 8-10 mg ) implanted subcutaneously in silastic capsules .

Example answer:
{"entities": [{"text": "Pituitary tumors", "type": "Disease"}, {"text": "diethylstilbestrol", "type": "Chemical"}, {"text": "DES", "type": "Chemical"}]}

Example input:
Sentence: We used rat models of intrahepatic cholestasis by ethinyl estradiol ( EE ) treatment and extrahepatic cholestasis by bile duct ligation ( BDL ) to precisely determine the site of TJ damage .

Example answer:
{"entities": [{"text": "intrahepatic cholestasis", "type": "Disease"}, {"text": "ethinyl estradiol", "type": "Chemical"}, {"text": "EE", "type": "Chemical"}, {"text": "extrahepatic cholestasis", "type": "Disease"}]}

Example input:
Sentence: Estrogens protect ovariectomized rats from hippocampal injury induced by kainic acid-induced status epilepticus ( SE ) .

Example answer:
{"entities": [{"text": "hippocampal injury", "type": "Disease"}, {"text": "kainic", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Tamoxifen ( TAM ) , the antiestrogenic drug most widely prescribed in the chemotherapy of breast cancer , induces changes in normal discoid shape of erythrocytes and hemolytic anemia .

Example answer:
{"entities": [{"text": "Tamoxifen", "type": "Chemical"}, {"text": "TAM", "type": "Chemical"}, {"text": "breast cancer", "type": "Disease"}, {"text": "hemolytic anemia", "type": "Disease"}]}

Example input:
Sentence: Characterization of estrogen-induced adenohypophyseal tumors in the Fischer 344 rat .

Example answer:
{"entities": [{"text": "estrogen-induced", "type": "Chemical"}, {"text": "adenohypophyseal tumors", "type": "Disease"}]}

Input:
Sentence: Estrogen binding sites were demonstrated by autoradiography in one transplantable and five primary diethylstilbesterol induced renal carcinomas in three hamsters .

## Item bc5cdr:test:589
Example input:
Sentence: injections of organ specific three drugs ( AAP : 500 mg/Kg for 24 h ; AMI : 50 mg/Kg/day for four days ; DOX : 20 mg/Kg for 48 h ) .

Example answer:
{"entities": [{"text": "AAP", "type": "Chemical"}, {"text": "AMI", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Following induction of anesthesia by fentanyl ( 0.15 mg kg ( -1 ) ) and propofol ( 2.0 mg kg ( -1 ) ) , 13 patients received phenylephrine ( 0.1 mg iv ) and 12 patients received ephedrine ( 10 mg iv ) to restore mean arterial pressure ( MAP ) .

Example answer:
{"entities": [{"text": "fentanyl", "type": "Chemical"}, {"text": "propofol", "type": "Chemical"}, {"text": "phenylephrine", "type": "Chemical"}, {"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: VPU was more potent than VPA , exhibiting the median effective dose ( ED ( 50 ) ) of 49 mg/kg in protecting rats against pilocarpine-induced seizure whereas the corresponding value for VPA was 322 mg/kg .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: The rats received AChE reactivator pralidoxime-2-chloride ( 2PAM ) ( 30.0 mg/kg BW ) , anticonvulsant diazepam ( 2.0 mg/kg BW ) , A ( 1 ) -adenosine receptor agonist N ( 6 ) -cyclopentyl adenosine ( CPA ) ( 2.0 mg/kg BW ) , NMDA-receptor antagonist dizocilpine maleate ( +-MK801 hydrogen maleate ) ( 2.0 mg/kg BW ) or their combinations with cholinolytic drug atropine sulfate ( 50.0 mg/kg BW ) immediately or 30 min after the single SC injection of DFP .

Example answer:
{"entities": [{"text": "pralidoxime-2-chloride", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "N ( 6 ) -cyclopentyl adenosine", "type": "Chemical"}, {"text": "CPA", "type": "Chemical"}, {"text": "NMDA-receptor", "type": "Chemical"}, {"text": "dizocilpine maleate", "type": "Chemical"}, {"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: A nonregenerative anemia was the most compromising of the cytopenias and occurred in approximately 50 % of dogs receiving 400-500 mg/kg cefonicid or 540-840 mg/kg cefazedone .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "cytopenias", "type": "Disease"}, {"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: In this study , the severity of response to other seizure-inducing agents was tested in mice 1 and 24 h after intraperitoneal administration of 80 mg/kg gamma-HCH .

Example answer:
{"entities": [{"text": "seizure-inducing", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}]}

Example input:
Sentence: The animals that had experienced cyclic sucrose and chow were hyperactive in response to amphetamine compared with four control groups ( ad libitum 10 % sucrose and chow followed by amphetamine injection , cyclic chow followed by amphetamine injection , ad libitum chow with amphetamine , or cyclic 10 % sucrose and chow with a saline injection ) .

Example answer:
{"entities": [{"text": "sucrose", "type": "Chemical"}, {"text": "hyperactive", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}]}

Example input:
Sentence: In six conscious , trained dogs , maintained on a normal sodium intake of 2 to 4 mEq/kg/day , sympathetic activity was assessed as the release rate of norepinephrine and epinephrine during 15-minute i.v .

Example answer:
{"entities": [{"text": "sodium", "type": "Chemical"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "epinephrine", "type": "Chemical"}]}

Example input:
Sentence: Therefore , we studied the hyperemic response to dipyridamole in seven open-chest anesthetized dogs after pretreatment with either pentoxifylline ( 0 , 7.5 , or 15 mg/kg i.v . )

Example answer:
{"entities": [{"text": "dipyridamole", "type": "Chemical"}, {"text": "pentoxifylline", "type": "Chemical"}]}

Input:
Sentence: In anesthetized dogs , a high dose of ACC-9653 ( 31 mg/kg ) was infused over 15 , 20 , and 30 min and the responses were compared to an equimolar dose of phenytoin sodium ( 21 mg/kg ) .

## Item bc5cdr:test:815
Example input:
Sentence: In the bolus group , 26.0 % ( 13/50 ) had akathisia compared with 32.7 % ( 16/49 ) in the infusion group ( Delta=-6.7 % ; 95 % confidence interval [ CI ] -24.6 % to 11.2 % ) .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Six of 30 patients ( 20 % ) without prior chemotherapy achieved a partial response ( PR ) ( 95 % confidence interval [ CI ] , 8 % to 39 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: The semi-quantitative scoring was significantly worst in the group treated with CsA plus SRL ( P < 0.001 compared with controls ) and the analysis of the total grade of fibrosis also showed the highest proportion in the same group and was significantly different from controls ( P < 0.02 ) .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: Of the 82 evaluable patients , 50 did not show any recurrence after 1 year ( 61 % ) , while 32 presented with one or more recurrences ( 39 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Eastern Cooperative Oncology Group performance status improved in 35 % of those patients with an initial value > 0 , whereas relief of at least 1 symptom without worsening of other symptoms was noted in 27 patients ( 55 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Visual analogue scores ( mean +/- SD ) during induction were lower in Groups L ( 3.3 +/- 2.5 ) and T ( 4.1 +/- 2.7 ) than in Group C ( 5.6 +/- 2.3 ) ; P = 0.0031 .

Example answer:
{"entities": []}

Example input:
Sentence: All patients were evaluable for response and toxicity .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Finally , 15 patients were excluded from the study ( noncompliance 14 , death 1 ) ; thus , 60 patients ( 31 in group I and 29 in group II ) were eligible for analysis .

Example answer:
{"entities": [{"text": "death", "type": "Disease"}]}

Example input:
Sentence: Of 18 patients evaluable for response , seven ( 39 % ) achieved a complete response and six ( 33 % ) achieved a partial response .

Example answer:
{"entities": []}

Example input:
Sentence: Of 24 evaluable patients , two achieved a complete remission and one achieved a partial remission for an overall response rate of 12.5 % ( 95 % confidence interval : 2.6-32.4 % ) .

Example answer:
{"entities": []}

Input:
Sentence: There was no difference in the rate of engraftment of evaluable patients in the two groups ( P greater than 0.5 ) .

## Item bc5cdr:test:520
Example input:
Sentence: In the absence of caffeine , acetaminophen ( up to 300 mg/kg ) did not modify the seizures induced by maximal electroshock and did not alter the convulsant dose of pentylenetetrezol in mice ( tests performed by the Anticonvulsant Screening Project of NINCDS ) .

Example answer:
{"entities": [{"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "pentylenetetrezol", "type": "Chemical"}]}

Example input:
Sentence: FINDINGS : FS containing tAMCA caused paroxysmal brain activity which was associated with distinct convulsive behaviours .

Example answer:
{"entities": [{"text": "tAMCA", "type": "Chemical"}, {"text": "convulsive", "type": "Disease"}]}

Example input:
Sentence: Thus , FS containing 47.5 mg/ml tAMCA evoked generalized seizures in all tested rats ( n=6 ) while the lowest concentration of tAMCA ( 0.5 mg/ml ) only evoked brief episodes of jerk-correlated convulsive potentials in 1 of 6 rats .

Example answer:
{"entities": [{"text": "tAMCA", "type": "Chemical"}, {"text": "generalized seizures", "type": "Disease"}, {"text": "convulsive", "type": "Disease"}]}

Example input:
Sentence: Estradiol reduces seizure-induced hippocampal injury in ovariectomized female but not in male rats .

Example answer:
{"entities": [{"text": "Estradiol", "type": "Chemical"}, {"text": "seizure-induced", "type": "Disease"}, {"text": "hippocampal injury", "type": "Disease"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: The present study was designed to evaluate two endogenous and one synthetic neuroactive steroid that positively modulate the gamma-aminobutyric acid ( GABA ( A ) ) receptor against the increase in sensitivity to the convulsant effects of cocaine engendered by repeated cocaine administration ( seizure kindling ) .

Example answer:
{"entities": [{"text": "steroid", "type": "Chemical"}, {"text": "gamma-aminobutyric acid", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Sensitivity to several convulsion endpoints induced by nicotine , carbachol , and neostigmine were significantly greater in WSR versus WSP mice .

Example answer:
{"entities": [{"text": "convulsion", "type": "Disease"}, {"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}]}

Example input:
Sentence: Evidence is accumulating that lindane can be toxic to the central nervous system and may be associated with aplastic anaemia .

Example answer:
{"entities": [{"text": "lindane", "type": "Chemical"}, {"text": "toxic to the central nervous system", "type": "Disease"}, {"text": "aplastic anaemia", "type": "Disease"}]}

Example input:
Sentence: Gamma-hexachlorocyclohexane ( gamma-HCH ) , the active ingredient of the insecticide lindane , has been shown to decrease seizure threshold to pentylenetrazol ( PTZ ) 3 h after exposure to gamma-HCH and conversely increase threshold to PTZ-induced seizures 24 h after exposure to gamma-HCH ( Vohland et al .

Example answer:
{"entities": [{"text": "Gamma-hexachlorocyclohexane", "type": "Chemical"}, {"text": "gamma-HCH", "type": "Chemical"}, {"text": "lindane", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "PTZ", "type": "Chemical"}, {"text": "PTZ-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Differential effects of gamma-hexachlorocyclohexane ( lindane ) on pharmacologically-induced seizures .

Example answer:
{"entities": [{"text": "gamma-hexachlorocyclohexane", "type": "Chemical"}, {"text": "lindane", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Input:
Sentence: Convulsant effect of lindane and regional brain concentration of GABA and dopamine .

## Item bc5cdr:test:855
Example input:
Sentence: METHODS : a total of 13 patients were referred to the Danish Cholinesterase Research Unit after ECT during 38 months .

Example answer:
{"entities": []}

Example input:
Sentence: The area under the curve was 537 +/- 149 ng/ml x hours , volume of distribution ( Vd ) 3504 +/- 644 l/m2 , and total clearance ( ClT ) was 204 + 39.3 l/hour/m2 .

Example answer:
{"entities": []}

Example input:
Sentence: For the cytoprotection study , animals were orally gavaged 100 mg/Kg GSPE for 7-10 days followed by i.p .

Example answer:
{"entities": [{"text": "GSPE", "type": "Chemical"}]}

Example input:
Sentence: It was administered by 15 min infusion to 16 evaluable patients with non-small cell lung cancer ( NSCLC ) ( 7 with no prior treatment , 9 patients in relapse following surgery/radiotherapy ) at a dose ( 648 mg/m2 divided over 3 days , repeated every 3 weeks ) determined by phase I trial .

Example answer:
{"entities": [{"text": "non-small cell lung cancer", "type": "Disease"}, {"text": "NSCLC", "type": "Disease"}]}

Example input:
Sentence: Pain recall after one week was similarly precise ( magnitude : p < 0.01 , duration : p < 0.05 ) .

Example answer:
{"entities": [{"text": "Pain", "type": "Disease"}]}

Example input:
Sentence: The t ( 1/2 , z ) of desipramine was longer when desipramine was coadministered with cinacalcet ( 21.0 versus 43.3 hs ) .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}]}

Example input:
Sentence: After completion of the amifostine infusion , cisplatin 120 mg/m2 was administered over 30 minutes .

Example answer:
{"entities": [{"text": "amifostine", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: SigmaST , the sum of ST-segment elevations in 16 precordial leads , decreased ( P less than 0.02 ) with intravenous nitroglycerin .

Example answer:
{"entities": [{"text": "nitroglycerin", "type": "Chemical"}]}

Example input:
Sentence: The duration of the examination and the mean ejection fraction ( EF ) were 16.4+/-6.1 minutes and 60+/-9 % , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: Pain intensity on a 0 to 10 numerical scale ; nausea and vomiting , drowsiness , confusion , and dry mouth , using a scale from 0 to 3 ( not at all , slight , a lot , awful ) ; Mini-Mental State Examination ( MMSE ) ( 0-30 ) ; and arterial pressure were recorded before administration of drugs ( T0 ) and after 30 minutes ( T30 ) , 60 minutes ( T60 ) , 120 minutes ( T120 ) , and 180 minutes ( T180 ) .

Example answer:
{"entities": [{"text": "Pain", "type": "Disease"}, {"text": "nausea", "type": "Disease"}, {"text": "vomiting", "type": "Disease"}, {"text": "confusion", "type": "Disease"}, {"text": "dry mouth", "type": "Disease"}]}

Input:
Sentence: ( ABSTRACT TRUNCATED AT 250 WORDS )

## Item bc5cdr:test:602
Example input:
Sentence: Control rats received halothane anesthesia ( 1 MAC ) for one hour , followed by SNP infusion , 40 microgram/kg/min , for 30 min , followed by a 30-min recovery period .

Example answer:
{"entities": [{"text": "halothane", "type": "Chemical"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: We report a case of a 31 year old female who required admission to the Intensive Care Unit for ventilation and full supportive therapy , following ingestion of 13.5g bupropion .

Example answer:
{"entities": [{"text": "bupropion", "type": "Chemical"}]}

Example input:
Sentence: Propylthiouracil therapy was withdrawn , and she was treated with a 1-month course of prednisone , which alleviated her symptoms .

Example answer:
{"entities": [{"text": "Propylthiouracil", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: The fits ceased within 4 hours of administering intramuscular pyridoxine , suggesting an aetiology of pyridoxine deficiency secondary to isoniazid medication .

Example answer:
{"entities": [{"text": "fits", "type": "Disease"}, {"text": "pyridoxine", "type": "Chemical"}, {"text": "isoniazid", "type": "Chemical"}]}

Example input:
Sentence: Leucovorin rescue was initiated 12 hours after the end of the infusion with a loading dose of 200 mg/m2 followed by 12 mg/m2 every three hours for six doses and then every six hours until the plasma methotrexate level decreased to less than 1 X 10 ( -7 ) mol/L .

Example answer:
{"entities": [{"text": "Leucovorin", "type": "Chemical"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: The mean duration of action was 3.8 hours with ipratropium and 2.4 hours with theophylline .

Example answer:
{"entities": [{"text": "ipratropium", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}]}

Example input:
Sentence: The bronchodilator effects of a single dose of ipratropium bromide aerosol ( 36 micrograms ) and short-acting theophylline tablets ( dose titrated to produce serum levels of 10-20 micrograms/mL ) were compared in a double-blind , placebo-controlled crossover study in 21 patients with stable , chronic obstructive pulmonary disease .

Example answer:
{"entities": [{"text": "ipratropium bromide", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}, {"text": "chronic obstructive pulmonary disease", "type": "Disease"}]}

Example input:
Sentence: Acute bronchodilating effects of ipratropium bromide and theophylline in chronic obstructive pulmonary disease .

Example answer:
{"entities": [{"text": "ipratropium bromide", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}, {"text": "chronic obstructive pulmonary disease", "type": "Disease"}]}

Example input:
Sentence: These results show that ipratropium is a more potent bronchodilator than oral theophylline in patients with chronic airflow obstruction .

Example answer:
{"entities": [{"text": "ipratropium", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}, {"text": "chronic airflow obstruction", "type": "Disease"}]}

Input:
Sentence: During the 14-day run-in and during washout periods , inhaled beta-agonists were withheld and ipratropium bromide was substituted for rescue purposes .

## Item bc5cdr:test:614
Example input:
Sentence: It is concluded that patients on 5-FU treatment should be under close supervision and that the treatment should be discontinued if chest pain or tachyarrhythmia is observed .

Example answer:
{"entities": [{"text": "5-FU", "type": "Chemical"}, {"text": "chest pain", "type": "Disease"}, {"text": "tachyarrhythmia", "type": "Disease"}]}

Example input:
Sentence: The drug was withdrawn on presentation to hospital in 11 patients , with rapid clinical improvement in 9 .

Example answer:
{"entities": []}

Example input:
Sentence: Hepatitis may develop weeks after discontinuation of the drug and may run a prolonged course , but complete remission was observed in all reported cases .

Example answer:
{"entities": [{"text": "Hepatitis", "type": "Disease"}]}

Example input:
Sentence: The aim of this study was to evaluate the relationship between phenytoin medication and cerebellar atrophy in patients who had experienced clinical intoxication .

Example answer:
{"entities": [{"text": "phenytoin", "type": "Chemical"}, {"text": "cerebellar atrophy", "type": "Disease"}]}

Example input:
Sentence: We report a case in which myocardial infarction coincided with the introduction of captopril and the withdrawal of verapamil in a previously asymptomatic woman with severe hypertension .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "captopril", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Disease"}]}

Example input:
Sentence: Magnetic resonance volumetry of the cerebellum in epileptic patients after phenytoin overdosages .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}, {"text": "phenytoin", "type": "Chemical"}, {"text": "overdosages", "type": "Disease"}]}

Example input:
Sentence: The case of a nonepileptic patient who developed psychosis following phenytoin treatment for trigeminal neuralgia is described .

Example answer:
{"entities": [{"text": "psychosis", "type": "Disease"}, {"text": "phenytoin", "type": "Chemical"}, {"text": "trigeminal neuralgia", "type": "Disease"}]}

Example input:
Sentence: Acute psychosis due to treatment with phenytoin in a nonepileptic patient .

Example answer:
{"entities": [{"text": "Acute psychosis", "type": "Disease"}, {"text": "phenytoin", "type": "Chemical"}]}

Example input:
Sentence: This case suggests that the psychotic symptoms that occur following phenytoin treatment in some epileptic patients may be the direct result of medication , unrelated to seizures .

Example answer:
{"entities": [{"text": "psychotic symptoms", "type": "Disease"}, {"text": "phenytoin", "type": "Chemical"}, {"text": "epileptic", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Input:
Sentence: In a patient receiving phenytoin who presents a viral-like illness , early recognition and discontinuation of the drug are mandatory .

## Item bc5cdr:test:613
Example input:
Sentence: Histopathology analyses in the 2 animals that died revealed liver and kidney toxicity , with greater severity in the orally-treated animal .

Example answer:
{"entities": []}

Example input:
Sentence: Cervical and inguinal lymph node biopsies showed the features of severe necrotising lymphadenitis , associated with erythrophagocytosis and prominent eosinophilic infiltrates , without viral inclusion bodies , suggestive of an adverse drug reaction.A week later , fulminant drug-induced hepatitis , associated with the presence of anti-nuclear autoantibodies ( but not with other markers of autoimmunity ) , and accompanied by multi-organ failure and sepsis , supervened .

Example answer:
{"entities": [{"text": "lymphadenitis", "type": "Disease"}, {"text": "adverse drug", "type": "Disease"}, {"text": "drug-induced hepatitis", "type": "Disease"}, {"text": "autoimmunity", "type": "Disease"}, {"text": "multi-organ failure", "type": "Disease"}, {"text": "sepsis", "type": "Disease"}]}

Example input:
Sentence: This study is the first to demonstrate that impairment of hepatocyte TJs occurs heterogenously in the liver lobule after BDL and suggests that BDL and EE treatments produce different lobular distributions of increased paracellular permeability .

Example answer:
{"entities": [{"text": "EE", "type": "Chemical"}]}

Example input:
Sentence: The results of serum liver function tests suggested hepatocellular injury in 10 ( 63 % ) ; the rest showed a mixed pattern .

Example answer:
{"entities": [{"text": "hepatocellular injury", "type": "Disease"}]}

Example input:
Sentence: A repeat work-up revealed further elevations in aminotransferase levels , and liver biopsy revealed evidence of moderate-to-severe drug toxicity .

Example answer:
{"entities": [{"text": "drug toxicity", "type": "Disease"}]}

Example input:
Sentence: FINDINGS : The liver biopsy sample showed hepatocellular necrosis which was prominent in perivenular zone three and extended focally from portal tracts to portal tracts and centrilobular areas ( bridging necrosis ) .

Example answer:
{"entities": [{"text": "necrosis", "type": "Disease"}]}

Example input:
Sentence: There was no serologic evidence of viral infection , and a liver biopsy sample showed a histologic pattern consistent with drug-induced hepatitis .

Example answer:
{"entities": [{"text": "viral infection", "type": "Disease"}, {"text": "drug-induced hepatitis", "type": "Disease"}]}

Example input:
Sentence: This type of lesion broadens the spectrum of liver injury due to this drug combination , mainly represented by a benign cholestatic syndrome .

Example answer:
{"entities": [{"text": "liver injury", "type": "Disease"}, {"text": "cholestatic syndrome", "type": "Disease"}]}

Example input:
Sentence: Biochemical liver function tests indicated hepatocellular necrosis and correlated with histopathological evidence of hepatic injury , the spectrum of which ranged from fatty change and focal hepatocellular necrosis to massive hepatic necrosis .

Example answer:
{"entities": [{"text": "necrosis", "type": "Disease"}, {"text": "hepatic injury", "type": "Disease"}, {"text": "fatty change", "type": "Disease"}, {"text": "massive hepatic necrosis", "type": "Disease"}]}

Example input:
Sentence: Immune mechanisms may be involved in the drug 's hepatotoxicity , as suggested by the T-cell stimulation study reported here .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}]}

Input:
Sentence: The hematologic , biochemical and pathologic features indicate a mixed hepatocellular damage due to drug hypersensitivity .

## Item bc5cdr:test:544
Example input:
Sentence: Procainamide-induced polymorphous ventricular tachycardia .

Example answer:
{"entities": [{"text": "Procainamide-induced", "type": "Chemical"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: Nitroglycerin has been shown to reduce ST-segment elevation during acute myocardial infarction , an effect potentiated in the dog by agents that reverse nitroglycerin-induced hypotension .

Example answer:
{"entities": [{"text": "Nitroglycerin", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}, {"text": "nitroglycerin-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: This drug caused biventricular dysfunction , due to its negative inotropic effect , and hypotension , due to its peripheral vasodilatory effect .

Example answer:
{"entities": [{"text": "biventricular dysfunction", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: It has been shown that bromocriptine-induced tachycardia , which persisted after adrenalectomy , is ( i ) mediated by central dopamine D2 receptor activation and ( ii ) reduced by 5-day isoproterenol pretreatment , supporting therefore the hypothesis that this effect is dependent on sympathetic outflow to the heart .

Example answer:
{"entities": [{"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: The arrhythmias were temporally related to cimetidine administration , disappeared after dechallenge , and did not recur during ranitidine treatment .

Example answer:
{"entities": [{"text": "arrhythmias", "type": "Disease"}, {"text": "cimetidine", "type": "Chemical"}, {"text": "ranitidine", "type": "Chemical"}]}

Example input:
Sentence: Nimodipine treatment resulted in a statistically significant reduction in systolic BP ( SBP ) and diastolic BP ( DBP ) from baseline compared with placebo during the first few days .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "Chemical"}, {"text": "reduction in systolic BP", "type": "Disease"}]}

Example input:
Sentence: Iatrogenically induced intractable atrioventricular reentrant tachycardia after verapamil and catheter ablation in a patient with Wolff-Parkinson-White syndrome and idiopathic dilated cardiomyopathy .

Example answer:
{"entities": [{"text": "atrioventricular reentrant tachycardia", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "idiopathic dilated cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: The magnitude and time course of the increase in heart rate and the decrease in systolic blood pressure after nitroglycerin were similar in the normal and diabetic subjects without autonomic neuropathy , whereas a lesser increase in heart rate and a greater decrease in systolic blood pressure occurred in the diabetic subjects with autonomic neuropathy .

Example answer:
{"entities": [{"text": "nitroglycerin", "type": "Chemical"}, {"text": "diabetic", "type": "Disease"}, {"text": "autonomic neuropathy", "type": "Disease"}]}

Example input:
Sentence: However , marked tachycardia associated with the use of ephedrine in combination with propofol occurred in the majority of patients , occasionally reaching high levels in individual patients .

Example answer:
{"entities": [{"text": "tachycardia", "type": "Disease"}, {"text": "ephedrine", "type": "Chemical"}, {"text": "propofol", "type": "Chemical"}]}

Example input:
Sentence: A low incidence of cardiovascular malformations was observed after exposure to each of the four calcium channel blockers , but this incidence was statistically significant only for verapamil and nifedipine .

Example answer:
{"entities": [{"text": "cardiovascular malformations", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "nifedipine", "type": "Chemical"}]}

Input:
Sentence: This is inconsistent with the well-established finding that nifedipine induces tachycardia in normally innervated hearts .

## Item bc5cdr:test:656
Example input:
Sentence: In the absence of caffeine , acetaminophen ( up to 300 mg/kg ) did not modify the seizures induced by maximal electroshock and did not alter the convulsant dose of pentylenetetrezol in mice ( tests performed by the Anticonvulsant Screening Project of NINCDS ) .

Example answer:
{"entities": [{"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "pentylenetetrezol", "type": "Chemical"}]}

Example input:
Sentence: We measured diazepam-induced anxiolysis with the elevated plus-maze test , diazepam-induced sedation by recording the vigilance states , and picrotoxin- and pentylenetetrazol-induced seizures after i.p .

Example answer:
{"entities": [{"text": "diazepam-induced", "type": "Chemical"}, {"text": "picrotoxin-", "type": "Chemical"}, {"text": "pentylenetetrazol-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: METHOD : In London and Toronto 154 patients who met DSM-III criteria for panic disorder with agoraphobia were randomised to alprazolam or placebo .

Example answer:
{"entities": [{"text": "panic disorder", "type": "Disease"}, {"text": "agoraphobia", "type": "Disease"}, {"text": "alprazolam", "type": "Chemical"}]}

Example input:
Sentence: Cocaine-induced anxiety was also attenuated in Dbh +/- mice following administration of disulfiram , a dopamine beta-hydroxylase ( DBH ) inhibitor .

Example answer:
{"entities": [{"text": "Cocaine-induced", "type": "Chemical"}, {"text": "anxiety", "type": "Disease"}, {"text": "disulfiram", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: The effects of oral doses of diazepam ( single dose of 10 mg and a median dose of 30 mg/day for 2 weeks ) and propranolol ( single dose of 80 mg and a median dose of 240 mg/day for 2 weeks ) on psychological performance of patients with panic disorders and agoraphobia were investigated in a double-blind , randomized and crossover design .

Example answer:
{"entities": [{"text": "diazepam", "type": "Chemical"}, {"text": "propranolol", "type": "Chemical"}, {"text": "panic disorders", "type": "Disease"}, {"text": "agoraphobia", "type": "Disease"}]}

Example input:
Sentence: Because salicylates have been reported to augment the stimulatory effects of caffeine on the CNS , attention was focused on the possibility that the presence of acetaminophen ( 52 micrograms/mL ) reduced the CNS toxicity of caffeine .

Example answer:
{"entities": [{"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Behavioral effects of diazepam and propranolol in patients with panic disorder and agoraphobia .

Example answer:
{"entities": [{"text": "diazepam", "type": "Chemical"}, {"text": "propranolol", "type": "Chemical"}, {"text": "panic disorder", "type": "Disease"}, {"text": "agoraphobia", "type": "Disease"}]}

Example input:
Sentence: The efficacy of alprazolam and placebo in panic disorder with agoraphobia , and the side-effect and adverse effect profiles of both drug groups were measured .

Example answer:
{"entities": [{"text": "alprazolam", "type": "Chemical"}, {"text": "panic disorder", "type": "Disease"}, {"text": "agoraphobia", "type": "Disease"}]}

Example input:
Sentence: The frequency of sound-induced seizures after 12.5 or 25 mg/kg caffeine was reduced from 50 to 5 % by acetaminophen .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Input:
Sentence: Increased anxiogenic effects of caffeine in panic disorders .

## Item bc5cdr:test:895
Example input:
Sentence: in 107 patients but normal in 40 % at repeat determination .

Example answer:
{"entities": []}

Example input:
Sentence: PG was well tolerated by all 54 patients .

Example answer:
{"entities": [{"text": "PG", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : All the patients were examined for toxicity ; 34 were examinable for response .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Serious adverse events were reported in 11 and 13 patients in the respective groups .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Forty-four patients were enrolled in the study of which 7 ( 16 % ) were ineligible .

Example answer:
{"entities": []}

Example input:
Sentence: Finally , 15 patients were excluded from the study ( noncompliance 14 , death 1 ) ; thus , 60 patients ( 31 in group I and 29 in group II ) were eligible for analysis .

Example answer:
{"entities": [{"text": "death", "type": "Disease"}]}

Example input:
Sentence: Eight Crohn 's disease patients were included .

Example answer:
{"entities": [{"text": "Crohn 's disease", "type": "Disease"}]}

Example input:
Sentence: Thirty PD patients participated in the study .

Example answer:
{"entities": [{"text": "PD", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Two hundred sixty-five patients were included in this analysis ( n=92 , 93 , and 80 for placebo , low dose , and high dose , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : One hundred patients were enrolled .

Example answer:
{"entities": []}

Input:
Sentence: Data on 9,037 patients were collected by 1,455 participating physicians .

## Item bc5cdr:test:547
Example input:
Sentence: A decreased glutamate uptake was observed in the subcortical parts of animals treated with reserpine and haloperidol , compared to the control .

Example answer:
{"entities": [{"text": "glutamate", "type": "Chemical"}, {"text": "reserpine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Acute reserpine and subchronic haloperidol treatments change synaptosomal brain glutamate uptake and elicit orofacial dyskinesia in rats .

Example answer:
{"entities": [{"text": "reserpine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "orofacial dyskinesia", "type": "Disease"}]}

Example input:
Sentence: PD female rats also showed increased ( 3 ) H-haloperidol binding and decreased dopamine transporter binding in striatum .

Example answer:
{"entities": [{"text": "H-haloperidol", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVE : The goal of this study was to compare the efficacy and side effects of two doses of haloperidol and placebo in the treatment of psychosis and disruptive behaviors in patients with Alzheimer 's disease .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "psychosis", "type": "Disease"}, {"text": "disruptive behaviors", "type": "Disease"}, {"text": "Alzheimer 's disease", "type": "Disease"}]}

Example input:
Sentence: Significant blockade of cocaine toxicity was observed with the higher dose of GNC92H2 ( 190 mg/kg ) , where premorbid behaviors were reduced up to 40 % , seizures up to 77 % and death by 72 % .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "GNC92H2", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "death", "type": "Disease"}]}

Example input:
Sentence: THP exhibited an antipsychotic-like profile by potentiating haloperidol-induced catalepsy , reducing amphetamine-induced hyperactivity and reducing apomorphine-induced climbing in mice .

Example answer:
{"entities": []}

Example input:
Sentence: 1 h prior to haloperidol resulted in a dose-dependent increase in the catalepsy times ( P < 0.05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSIONS : The results indicated a favorable therapeutic profile for haloperidol in doses of 2-3 mg/day , although a subgroup developed moderate to severe extrapyramidal signs .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "extrapyramidal signs", "type": "Disease"}]}

Example input:
Sentence: In the double blind study with haloperidol , both substances were found to be highly effective in the treatment of psychotic syndromes belonging predominantly to the schizophrenia group .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "psychotic syndromes belonging predominantly to the schizophrenia group", "type": "Disease"}]}

Example input:
Sentence: On the contrary , the cataleptogenic effect of haloperidol was significantly reduced in rats treated with desipramine and 6-OHDA but not in rats treated with 6-OHDA or in rats with lesions of the locus coeruleus .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "desipramine", "type": "Chemical"}, {"text": "6-OHDA", "type": "Chemical"}]}

Input:
Sentence: The effectiveness of haloperidol pretreatment in preventing the toxic effects of high doses of amphetamine and cocaine was studied in rats .

## Item bc5cdr:test:869
Example input:
Sentence: RESULTS : Six of 61 women ( 10 % ) developed clinically reversible grade 3 CHF following infusional cyclophosphamide with a median percent decline in ejection fraction of 31 % .

Example answer:
{"entities": [{"text": "CHF", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}]}

Example input:
Sentence: After 35 days in the TG + HAART cohort , left ventricular mass increased 160 % by echocardiography .

Example answer:
{"entities": []}

Example input:
Sentence: However , L-dopa restored the bradycardia caused by norepinephrine in addition to decreasing blood pressure and heart rate .

Example answer:
{"entities": [{"text": "L-dopa", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}]}

Example input:
Sentence: The magnitude and time course of the increase in heart rate and the decrease in systolic blood pressure after nitroglycerin were similar in the normal and diabetic subjects without autonomic neuropathy , whereas a lesser increase in heart rate and a greater decrease in systolic blood pressure occurred in the diabetic subjects with autonomic neuropathy .

Example answer:
{"entities": [{"text": "nitroglycerin", "type": "Chemical"}, {"text": "diabetic", "type": "Disease"}, {"text": "autonomic neuropathy", "type": "Disease"}]}

Example input:
Sentence: Bradycardia ( defined as a decrease in heart rate to less than 50 beat min-1 ) was prevented when the larger dose of either active drug was used .

Example answer:
{"entities": [{"text": "Bradycardia", "type": "Disease"}]}

Example input:
Sentence: By day 11 , GLEPP1 protein and mRNA had begun to return towards baseline .

Example answer:
{"entities": []}

Example input:
Sentence: With mild toxicity , a reduction to 30 or 40 mg/kg per dose should result in a reversal of the abnormal results to normal within four weeks .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Reversal by phenylephrine of the beneficial effects of intravenous nitroglycerin in patients with acute myocardial infarction .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "nitroglycerin", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Input:
Sentence: Reversal to normal heart rate was found on day 7 .

## Item bc5cdr:test:642
Example input:
Sentence: It has been shown that bromocriptine-induced tachycardia , which persisted after adrenalectomy , is ( i ) mediated by central dopamine D2 receptor activation and ( ii ) reduced by 5-day isoproterenol pretreatment , supporting therefore the hypothesis that this effect is dependent on sympathetic outflow to the heart .

Example answer:
{"entities": [{"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: The bronchodilator effects of a single dose of ipratropium bromide aerosol ( 36 micrograms ) and short-acting theophylline tablets ( dose titrated to produce serum levels of 10-20 micrograms/mL ) were compared in a double-blind , placebo-controlled crossover study in 21 patients with stable , chronic obstructive pulmonary disease .

Example answer:
{"entities": [{"text": "ipratropium bromide", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}, {"text": "chronic obstructive pulmonary disease", "type": "Disease"}]}

Example input:
Sentence: Bromocriptine-induced hypotension was unaffected by isoproterenol pretreatment , while tachycardia was reversed to significant bradycardia , an effect that was partly reduced by i.v .

Example answer:
{"entities": [{"text": "Bromocriptine-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: In experiments using specific adrenergic antagonists , we found that pretreatment with the beta-adrenergic receptor antagonist propranolol blocked cocaine-induced anxiety-like behavior in Dbh +/- and wild-type C57BL6/J mice , while the alpha ( 1 ) antagonist prazosin and the alpha ( 2 ) antagonist yohimbine had no effect .

Example answer:
{"entities": [{"text": "propranolol", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "anxiety-like", "type": "Disease"}, {"text": "prazosin", "type": "Chemical"}, {"text": "yohimbine", "type": "Chemical"}]}

Example input:
Sentence: For the subsequent 6-week double-blind crossover phase ( phase B ) , patients taking standard- or low-dose haloperidol were switched to placebo , and patients taking placebo were randomly assigned to standard- or low-dose haloperidol .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: These results show that ipratropium is a more potent bronchodilator than oral theophylline in patients with chronic airflow obstruction .

Example answer:
{"entities": [{"text": "ipratropium", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}, {"text": "chronic airflow obstruction", "type": "Disease"}]}

Example input:
Sentence: Terbutaline , a beta2-adrenoceptor agonist used to arrest preterm labor , has been associated with increased concordance for autism in dizygotic twins .

Example answer:
{"entities": [{"text": "Terbutaline", "type": "Chemical"}, {"text": "preterm labor", "type": "Disease"}, {"text": "autism", "type": "Disease"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Input:
Sentence: Procaterol , a new beta-2 adrenoceptor stimulant , was studied in a double-blind , placebo-controlled , cross-over trial in patients with bronchial asthma .

## Item bc5cdr:test:650
Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/", "type": "Chemical"}, {"text": "K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}]}

Example input:
Sentence: TCR protected against pathological changes induced by isoproterenol in rat heart .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: Effects of long-term pretreatment with isoproterenol on bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: In addition , mitochondrial respiratory dysfunction characterized by decreased respiratory control ratio and ADP/O was observed in isoproterenol-treated rats .

Example answer:
{"entities": [{"text": "respiratory dysfunction", "type": "Disease"}, {"text": "ADP/O", "type": "Chemical"}, {"text": "isoproterenol-treated", "type": "Chemical"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: In isolated perfused heart preparations from isoproterenol-pretreated rats , the isoproterenol-induced maximal increase in left ventricular systolic pressure was significantly reduced , compared with saline-pretreated rats ( the EC50 of the isoproterenol-induced increase in left ventricular systolic pressure was enhanced approximately 22-fold ) .

Example answer:
{"entities": [{"text": "isoproterenol-pretreated", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: The effects of exercise on the severity of isoproterenol-induced myocardial infarction were studied in female albino rats of 20,40,60 and 80 weeks of age .

Example answer:
{"entities": [{"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Isoproterenol pretreatment for 15 days caused cardiac hypertrophy without affecting baseline blood pressure and heart rate .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "Chemical"}, {"text": "cardiac hypertrophy", "type": "Disease"}]}

Example input:
Sentence: Isoproterenol-treated rats showed significant increases in the levels of lactate dehydrogenase , aspartate transaminase , creatine kinase and malondialdehyde and significant decreases in the activities of superoxide dismutase , catalase and glutathione peroxidase in serum and heart .

Example answer:
{"entities": [{"text": "Isoproterenol-treated", "type": "Chemical"}, {"text": "lactate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "creatine", "type": "Chemical"}, {"text": "malondialdehyde", "type": "Chemical"}, {"text": "superoxide", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}]}

Example input:
Sentence: Histological studies demonstrated that the rats developed an infarct 18 h after isoproterenol administration .

Example answer:
{"entities": [{"text": "infarct", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}]}

Input:
Sentence: The studies were performed using an experimental model of isoproterenol-induced heart hypertrophy in rats .

## Item bc5cdr:test:662
Example input:
Sentence: We describe a 25-year-old woman with pre-existing mitral valve prolapse who developed intractable ventricular fibrillation after consuming a `` natural energy '' guarana health drink containing a high concentration of caffeine .

Example answer:
{"entities": [{"text": "mitral valve prolapse", "type": "Disease"}, {"text": "ventricular fibrillation", "type": "Disease"}, {"text": "caffeine", "type": "Chemical"}]}

Example input:
Sentence: The frequency of sound-induced seizures after 12.5 or 25 mg/kg caffeine was reduced from 50 to 5 % by acetaminophen .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}]}

Example input:
Sentence: More patients were ( completely , very or somewhat ) satisfied 2 h after treatment with rizatriptan ( 69.8 % ) than at 2 h after treatment with ergotamine/caffeine ( 38.6 % , p < or = 0.001 ) .

Example answer:
{"entities": [{"text": "rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}]}

Example input:
Sentence: In patient 1 , plasma levels of deoxycorticosterone and 11-deoxycortisol were elevated .

Example answer:
{"entities": [{"text": "deoxycorticosterone", "type": "Chemical"}, {"text": "11-deoxycortisol", "type": "Chemical"}]}

Example input:
Sentence: In patient 2 , in addition to an increase in both deoxycorticosterone and 11-deoxycortisol levels , plasma aldosterone values were raised , with a concomitant suppression of renin levels .

Example answer:
{"entities": [{"text": "deoxycorticosterone", "type": "Chemical"}, {"text": "11-deoxycortisol", "type": "Chemical"}, {"text": "aldosterone", "type": "Chemical"}]}

Example input:
Sentence: Plasma cortisol concentrations were significantly raised during the active phase ( 323+/-43 to 1082+/-245 mmol/L , P < 0.05 ) .

Example answer:
{"entities": [{"text": "cortisol", "type": "Chemical"}]}

Example input:
Sentence: A patient who allegedly consumed 100 tablets of an over-the-counter analgesic containing sodium acetylsalicylate , caffeine , and acetaminophen displayed no significant CNS stimulation despite the presence of 175 micrograms of caffeine per mL of serum .

Example answer:
{"entities": [{"text": "sodium acetylsalicylate", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: In both cases normal plasma and urinary free cortisol levels had been achieved following ketoconazole therapy , yet continuous blood pressure monitoring demonstrated hypertension 31 ( patient 1 ) and 52 weeks ( patient 2 ) after treatment .

Example answer:
{"entities": [{"text": "cortisol", "type": "Chemical"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: Because salicylates have been reported to augment the stimulatory effects of caffeine on the CNS , attention was focused on the possibility that the presence of acetaminophen ( 52 micrograms/mL ) reduced the CNS toxicity of caffeine .

Example answer:
{"entities": [{"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Input:
Sentence: Caffeine increased plasma cortisol levels equally in the patient and healthy groups .

## Item bc5cdr:test:378
Example input:
Sentence: Capsaicin ( 10 micro g ) was injected into the masseter muscle to induce pain in 11 healthy volunteers .

Example answer:
{"entities": [{"text": "Capsaicin", "type": "Chemical"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: ( +/- ) -PG-9 antinociception peaked 15 min after injection and then slowly diminished .

Example answer:
{"entities": [{"text": ")", "type": "Chemical"}]}

Example input:
Sentence: Capsaicin injection reliably induced a dose-dependent flare ( p < 0.001 ) without any difference within or across sessions .

Example answer:
{"entities": [{"text": "Capsaicin", "type": "Chemical"}]}

Example input:
Sentence: Capsaicin ( 0.01-1 mm ) applied to oral or nasal mucosa induced increases in dural and cortical blood flow and provoked lacrimation .

Example answer:
{"entities": [{"text": "Capsaicin", "type": "Chemical"}, {"text": "increases in dural and cortical blood flow", "type": "Disease"}]}

Example input:
Sentence: The patient 's ophthalmological symptoms improved rapidly 3 weeks after discontinuation of pegylated IFN alpha-2b and ribavirin .

Example answer:
{"entities": [{"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: Five of 8 patients ( 63 % ) improved during fusidic acid treatment : 3 at two weeks and 2 after four weeks .

Example answer:
{"entities": [{"text": "fusidic acid", "type": "Chemical"}]}

Example input:
Sentence: To this end , persistent hyperalgesia was induced by administration of capsaicin in the tail of gonadally intact F344 rats , following which the tail was immersed in a mildly noxious thermal stimulus , and tail-withdrawal latencies measured .

Example answer:
{"entities": [{"text": "hyperalgesia", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: Propylthiouracil therapy was withdrawn , and she was treated with a 1-month course of prednisone , which alleviated her symptoms .

Example answer:
{"entities": [{"text": "Propylthiouracil", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}]}

Example input:
Sentence: Subjects were able to reliably discriminate pain magnitude and duration across capsaicin doses ( both p < 0.001 ) , regardless of whether first-time ratings were requested immediately , after one hour or after one day .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: In order to address long-term pain memory , nine healthy male volunteers received intradermal injections of three doses of capsaicin ( 0.05 , 1 and 20 microg , separated by 15 min breaks ) , each given three times in a balanced design across three sessions at one week intervals .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Input:
Sentence: In order to evaluate the efficacy , time-course of action and predictors of response to topical capsaicin , 39 patients with chronic post-herpetic neuralgia ( PHN ) , median duration 24 months , were treated with 0.025 % capsaicin cream for 8 weeks .

## Item bc5cdr:test:439
Example input:
Sentence: High-dose intravenous methotrexate is an effective treatment for the induction of remission after meningeal relapse in acute lymphoblastic leukemia .

Example answer:
{"entities": [{"text": "methotrexate", "type": "Chemical"}, {"text": "acute lymphoblastic leukemia", "type": "Disease"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: In conclusion mitochondrial toxicity is an early common event both in paclitaxel and cisplatin induced neurotoxicity .

Example answer:
{"entities": [{"text": "mitochondrial toxicity", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Remission induction of meningeal leukemia with high-dose intravenous methotrexate .

Example answer:
{"entities": [{"text": "meningeal leukemia", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "Disease"}, {"text": "METH", "type": "Chemical"}, {"text": "MPTP", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "METH-induced", "type": "Chemical"}]}

Example input:
Sentence: Neurologic toxicity was reported in 52 % of patients .

Example answer:
{"entities": [{"text": "Neurologic toxicity", "type": "Disease"}]}

Example input:
Sentence: Twenty children with acute lymphoblastic leukemia who developed meningeal disease were treated with a high-dose intravenous methotrexate regimen that was designed to achieve and maintain CSF methotrexate concentrations of 10 ( -5 ) mol/L without the need for concomitant intrathecal dosing .

Example answer:
{"entities": [{"text": "acute lymphoblastic leukemia", "type": "Disease"}, {"text": "meningeal disease", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: The correlation between neuropathic damage and inhibition of neurotoxic esterase or neuropathy target enzyme ( NTE ) was examined in rats acutely exposed to Mipafox ( N , N'-diisopropylphosphorodiamidofluoridate ) , a neurotoxic organophosphate .

Example answer:
{"entities": [{"text": "neuropathic damage", "type": "Disease"}, {"text": "neurotoxic", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}, {"text": "Mipafox", "type": "Chemical"}, {"text": "N , N'-diisopropylphosphorodiamidofluoridate", "type": "Chemical"}, {"text": "organophosphate", "type": "Chemical"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: CNS complications included posterior reversible leukoencephalopathy syndrome ( n = 10 ) , stroke ( n = 5 ) , temporal lobe epilepsy ( n = 2 ) , high-dose methotrexate toxicity ( n = 2 ) , syndrome of inappropriate antidiuretic hormone secretion ( n = 1 ) , and other unclassified events ( n = 7 ) .

Example answer:
{"entities": [{"text": "leukoencephalopathy", "type": "Disease"}, {"text": "stroke", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "inappropriate antidiuretic hormone secretion", "type": "Disease"}]}

Input:
Sentence: Neurologic toxicities have been described with IT-methotrexate , IT-cytosine arabinoside and IT-TSPA .

## Item bc5cdr:test:756
Example input:
Sentence: Renal biopsy revealed severe glomerulonephritis with crescents , electron dense fibrillar deposits and moderate lymphocytic interstitial infiltrate .

Example answer:
{"entities": [{"text": "glomerulonephritis", "type": "Disease"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: This case study reveals an unusual finding of rapidly proliferative crescentic glomerulonephritis in a patient treated with rifampin who had no other identifiable causes for developing this disease .

Example answer:
{"entities": [{"text": "glomerulonephritis", "type": "Disease"}, {"text": "rifampin", "type": "Chemical"}]}

Example input:
Sentence: Adult rats given dexamethasone on days 15 and 16 of gestation had more glomeruli with glomerulosclerosis than control rats .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: Biopsies performed in five patients revealed new pathological changes : One membranoproliferative glomerulopathy and interstitial nephritis .

Example answer:
{"entities": [{"text": "membranoproliferative glomerulopathy", "type": "Disease"}, {"text": "interstitial nephritis", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : An association has been found between transplant glomerulopathy ( TG ) and reduplication of peritubular capillary basement membranes ( PTCR ) .

Example answer:
{"entities": [{"text": "transplant glomerulopathy", "type": "Disease"}, {"text": "TG", "type": "Disease"}]}

Example input:
Sentence: Other possible causes of rapidly progressive glomerulonephritis were investigated and ruled out .

Example answer:
{"entities": [{"text": "glomerulonephritis", "type": "Disease"}]}

Example input:
Sentence: Reduction in GFR was associated with the development of glomerular sclerosis in both treated and untreated rats .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : PAN glomeruli already showed significant pathology by day 4 , despite relatively mild proteinuria .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: This report documents the unusual occurrence of rapidly progressive glomerulonephritis with crescents and fibrillar glomerulonephritis in a patient treated with rifampin .

Example answer:
{"entities": [{"text": "glomerulonephritis", "type": "Disease"}, {"text": "rifampin", "type": "Chemical"}]}

Input:
Sentence: Their glomeruli showed changes of progressive FSGS .

## Item bc5cdr:test:791
Example input:
Sentence: We report the increased amount of motor disability in four patients with idiopathic Parkinson 's disease after exposure to the antidepressant fluoxetine .

Example answer:
{"entities": [{"text": "motor disability", "type": "Disease"}, {"text": "idiopathic Parkinson 's disease", "type": "Disease"}, {"text": "antidepressant", "type": "Chemical"}, {"text": "fluoxetine", "type": "Chemical"}]}

Example input:
Sentence: However , marked tachycardia associated with the use of ephedrine in combination with propofol occurred in the majority of patients , occasionally reaching high levels in individual patients .

Example answer:
{"entities": [{"text": "tachycardia", "type": "Disease"}, {"text": "ephedrine", "type": "Chemical"}, {"text": "propofol", "type": "Chemical"}]}

Example input:
Sentence: The patient had no apparent associated conditions which might have predisposed him to the development of bradyarrhythmias ; and , thus , this probably represented a true idiosyncrasy to lidocaine .

Example answer:
{"entities": [{"text": "bradyarrhythmias", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Myocarditis is an increasingly recognized complication associated with the use of clozapine .

Example answer:
{"entities": [{"text": "Myocarditis", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Seventeen subjects who were genotyped as CYP2D6 extensive metabolizers were enrolled in this randomized , open-label , crossover study to receive a single oral dose of desipramine ( 50 mg ) on two separate occasions , once alone and once after multiple doses of cinacalcet ( 90 mg for 7 days ) .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}]}

Example input:
Sentence: An elderly patient treated with low dose Desipramine developed a delirium while her plasma level was in the `` subtherapeutic '' range .

Example answer:
{"entities": [{"text": "Desipramine", "type": "Chemical"}, {"text": "delirium", "type": "Disease"}]}

Example input:
Sentence: We report a case of variant ventricular tachycardia induced by desipramine toxicity .

Example answer:
{"entities": [{"text": "ventricular tachycardia", "type": "Disease"}, {"text": "desipramine", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Fewer subjects reported adverse events following treatment with desipramine alone than when receiving desipramine with cinacalcet ( 33 versus 86 % ) , the most frequent of which ( nausea and headache ) have been reported for patients treated with either desipramine or cinacalcet .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}, {"text": "nausea", "type": "Disease"}, {"text": "headache", "type": "Disease"}]}

Example input:
Sentence: Trimipramine ( TRI ) , which shows a clinical antidepressant activity , is chemically related to imipramine but does not inhibit the reuptake of noradrenaline and 5-hydroxytryptamine , nor does it induce beta-adrenergic down-regulation .

Example answer:
{"entities": [{"text": "Trimipramine", "type": "Chemical"}, {"text": "TRI", "type": "Chemical"}, {"text": "antidepressant", "type": "Chemical"}, {"text": "imipramine", "type": "Chemical"}, {"text": "noradrenaline", "type": "Chemical"}, {"text": "5-hydroxytryptamine", "type": "Chemical"}]}

Example input:
Sentence: Its occurrence in a patient being treated with imipramine is described , representing the first reported case of this syndrome in conjunction with antidepressants .

Example answer:
{"entities": [{"text": "imipramine", "type": "Chemical"}, {"text": "antidepressants", "type": "Chemical"}]}

Input:
Sentence: However , it has not previously been described in association with the use of Imipramine .

## Item bc5cdr:test:634
Example input:
Sentence: An allergic reaction consisting of angioneurotic edema secondary to continuous infusion 5-fluorouracil occurred in a patient with recurrent carcinoma of the oral cavity , cirrhosis , and cisplatin-induced impaired renal function .

Example answer:
{"entities": [{"text": "allergic reaction", "type": "Disease"}, {"text": "angioneurotic edema", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "carcinoma of the oral cavity", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "impaired renal function", "type": "Disease"}]}

Example input:
Sentence: The patient 's ophthalmological symptoms improved rapidly 3 weeks after discontinuation of pegylated IFN alpha-2b and ribavirin .

Example answer:
{"entities": [{"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: We prospectively evaluated the adverse reactions of apraclonidine in 20 normal volunteers by instilling a single drop of 1 % apraclonidine in their right eyes .

Example answer:
{"entities": [{"text": "apraclonidine", "type": "Chemical"}]}

Example input:
Sentence: METHODS : We present a case of presumed amikacin retinal toxicity following treatment with amikacin and vancomycin for alpha-haemolytic streptococcal endophthalmitis .

Example answer:
{"entities": [{"text": "amikacin", "type": "Chemical"}, {"text": "retinal toxicity", "type": "Disease"}, {"text": "vancomycin", "type": "Chemical"}, {"text": "streptococcal endophthalmitis", "type": "Disease"}]}

Example input:
Sentence: Nitrofurantoins were associated with anophthalmia or microphthalmos ( AOR = 3.7 ; 95 % CI , 1.1-12.2 ) , hypoplastic left heart syndrome ( AOR = 4.2 ; 95 % CI , 1.9-9.1 ) , atrial septal defects ( AOR = 1.9 ; 95 % CI , 1.1-3.4 ) , and cleft lip with cleft palate ( AOR = 2.1 ; 95 % CI , 1.2-3.9 ) .

Example answer:
{"entities": [{"text": "Nitrofurantoins", "type": "Chemical"}, {"text": "anophthalmia", "type": "Disease"}, {"text": "microphthalmos", "type": "Disease"}, {"text": "hypoplastic left heart syndrome", "type": "Disease"}, {"text": "atrial septal defects", "type": "Disease"}, {"text": "cleft lip", "type": "Disease"}, {"text": "cleft palate", "type": "Disease"}]}

Example input:
Sentence: Visual toxicity was of retinal origin and was characterized by a tritan-type dyschromatopsy , sometimes associated with a loss of visual acuity and pigmentary retinal deposits .

Example answer:
{"entities": [{"text": "Visual toxicity", "type": "Disease"}, {"text": "dyschromatopsy", "type": "Disease"}, {"text": "a loss of visual acuity", "type": "Disease"}, {"text": "pigmentary retinal deposits", "type": "Disease"}]}

Example input:
Sentence: The most common adverse events ( incidence > or = 5 % in one group ) after rizatriptan and ergotamine/caffeine , respectively , were dizziness ( 6.7 and 5.3 % ) , nausea ( 4.2 and 8.5 % ) and somnolence ( 5.5 and 2.3 % ) .

Example answer:
{"entities": [{"text": "rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}, {"text": "dizziness", "type": "Disease"}, {"text": "nausea", "type": "Disease"}, {"text": "somnolence", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Currently accepted intravitreal antibiotic regimens may cause retinal toxicity and macular ischaemia .

Example answer:
{"entities": [{"text": "retinal toxicity", "type": "Disease"}, {"text": "ischaemia", "type": "Disease"}]}

Example input:
Sentence: Development of ocular myasthenia during pegylated interferon and ribavirin treatment for chronic hepatitis C. A 63-year-old male experienced sudden diplopia after 9 weeks of administration of pegylated interferon ( IFN ) alpha-2b and ribavirin for chronic hepatitis C ( CHC ) .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated interferon", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "chronic hepatitis", "type": "Disease"}, {"text": "diplopia", "type": "Disease"}, {"text": "pegylated interferon ( IFN ) alpha-2b", "type": "Chemical"}, {"text": "chronic hepatitis C", "type": "Disease"}, {"text": "CHC", "type": "Disease"}]}

Example input:
Sentence: The ocular myasthenia associated with combination therapy of pegylated IFN alpha-2b and ribavirin for CHC is very rarely reported ; therefore , we present this case with a review of the various eye complications of IFN therapy .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "CHC", "type": "Disease"}, {"text": "IFN", "type": "Chemical"}]}

Input:
Sentence: Adverse ocular reactions possibly associated with isotretinoin .

## Item bc5cdr:test:60
Example input:
Sentence: To develop a novel and effective drug that could enhance cognitive function and neuroprotection , we newly synthesized maltolyl p-coumarate by the esterification of maltol and p-coumaric acid .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "maltol", "type": "Chemical"}, {"text": "p-coumaric acid", "type": "Chemical"}]}

Example input:
Sentence: Flow and metabolism were measured 5-13 days after the subarachnoid haemorrhage by a modification of the classical Kety-Schmidt technique using xenon-133 i.v .

Example answer:
{"entities": [{"text": "subarachnoid haemorrhage", "type": "Disease"}, {"text": "xenon-133", "type": "Chemical"}]}

Example input:
Sentence: In the present study , we investigated whether maltolyl p-coumarate could improve cognitive decline in scopolamine-injected rats and in amyloid beta peptide ( 1-42 ) -infused rats .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "cognitive decline", "type": "Disease"}, {"text": "scopolamine-injected", "type": "Chemical"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}]}

Example input:
Sentence: Recently , synthetic fibrinolysis inhibitors such as tranexamic acid ( tAMCA ) have been considered as substitutes for aprotinin .

Example answer:
{"entities": [{"text": "tranexamic acid", "type": "Chemical"}, {"text": "tAMCA", "type": "Chemical"}]}

Example input:
Sentence: Conservative treatment , including bladder irrigation with physiological saline and instillation of prostaglandin F2 alpha , failed to totally control hemorrhage .

Example answer:
{"entities": [{"text": "prostaglandin F2 alpha", "type": "Chemical"}, {"text": "hemorrhage", "type": "Disease"}]}

Example input:
Sentence: METHODS : A double-blind double-armed prospective study comprised 40 patients who had uneventful sutureless phacoemulsification under sub-Tenon 's local infiltration of 3 mL of plain lignocaine .

Example answer:
{"entities": [{"text": "lignocaine", "type": "Chemical"}]}

Example input:
Sentence: To evaluate the effect of prostaglandin E1 ( PGE1 ) or trimethaphan ( TMP ) induced hypotension on epidural blood flow ( EBF ) during spinal surgery , EBF was measured using the heat clearance method in 30 patients who underwent postero-lateral interbody fusion under isoflurane anaesthesia .

Example answer:
{"entities": [{"text": "prostaglandin E1", "type": "Chemical"}, {"text": "PGE1", "type": "Chemical"}, {"text": "trimethaphan", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "isoflurane", "type": "Chemical"}]}

Example input:
Sentence: METHOD : FS containing aprotinin or different concentrations of tAMCA ( 0.5-47.5 mg/ml ) were applied to the pial surface of the cortex of anaesthetized rats .

Example answer:
{"entities": [{"text": "tAMCA", "type": "Chemical"}]}

Example input:
Sentence: Maltolyl p-coumarate was found to attenuate cognitive deficits in both rat models using passive avoidance test and to reduce apoptotic cell death observed in the hippocampus of the amyloid beta peptide ( 1-42 ) -infused rats .

Example answer:
{"entities": [{"text": "Maltolyl p-coumarate", "type": "Chemical"}, {"text": "cognitive deficits", "type": "Disease"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}]}

Example input:
Sentence: We tested the sulfated polysaccharide fucoidan , which has been reported to reduce inflammatory brain damage , in a rat model of intracerebral hemorrhage induced by injection of bacterial collagenase into the caudate nucleus .

Example answer:
{"entities": [{"text": "fucoidan", "type": "Chemical"}, {"text": "brain damage", "type": "Disease"}, {"text": "intracerebral hemorrhage", "type": "Disease"}]}

Input:
Sentence: Epsilon aminocaproic acid ( EACA ) has been used to prevent rebleeding in patients with subarachnoid hemorrhage ( SAH ) .

## Item bc5cdr:test:235
Example input:
Sentence: Acute reserpine and subchronic haloperidol treatments change synaptosomal brain glutamate uptake and elicit orofacial dyskinesia in rats .

Example answer:
{"entities": [{"text": "reserpine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "orofacial dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Experiments with systemic administration of the Pgp substrate phenobarbital and the selective Pgp inhibitor tariquidar in TR ( - ) rats substantiated that Pgp is functional and compensates for the lack of MRP2 in the BBB .

Example answer:
{"entities": [{"text": "phenobarbital", "type": "Chemical"}, {"text": "tariquidar", "type": "Chemical"}]}

Example input:
Sentence: METHOD : FS containing aprotinin or different concentrations of tAMCA ( 0.5-47.5 mg/ml ) were applied to the pial surface of the cortex of anaesthetized rats .

Example answer:
{"entities": [{"text": "tAMCA", "type": "Chemical"}]}

Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: Mitochondrial radiocalcium uptakes were significantly decreased in animals pretreated with acetylsalicylic acid or dipyridamole or when hydrocortisone was added to the epinephrine infusion ( 2,682,2,803 , and 3,424 counts per minute per gram of dried fraction , respectively ) .

Example answer:
{"entities": [{"text": "radiocalcium", "type": "Chemical"}, {"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine", "type": "Chemical"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: MPA , BCC , DMCM , and STR showed no inhibition of 3H-TBOB ( t-butyl bicyclo-orthobenzoate ) binding at concentrations of 100 micron .

Example answer:
{"entities": [{"text": "MPA", "type": "Chemical"}, {"text": "BCC", "type": "Chemical"}, {"text": "DMCM", "type": "Chemical"}, {"text": "STR", "type": "Chemical"}, {"text": "3H-TBOB", "type": "Chemical"}, {"text": "t-butyl bicyclo-orthobenzoate", "type": "Chemical"}]}

Example input:
Sentence: The rats received AChE reactivator pralidoxime-2-chloride ( 2PAM ) ( 30.0 mg/kg BW ) , anticonvulsant diazepam ( 2.0 mg/kg BW ) , A ( 1 ) -adenosine receptor agonist N ( 6 ) -cyclopentyl adenosine ( CPA ) ( 2.0 mg/kg BW ) , NMDA-receptor antagonist dizocilpine maleate ( +-MK801 hydrogen maleate ) ( 2.0 mg/kg BW ) or their combinations with cholinolytic drug atropine sulfate ( 50.0 mg/kg BW ) immediately or 30 min after the single SC injection of DFP .

Example answer:
{"entities": [{"text": "pralidoxime-2-chloride", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "N ( 6 ) -cyclopentyl adenosine", "type": "Chemical"}, {"text": "CPA", "type": "Chemical"}, {"text": "NMDA-receptor", "type": "Chemical"}, {"text": "dizocilpine maleate", "type": "Chemical"}, {"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: In vitro , gamma-HCH , pentylenetetrazol and picrotoxin were shown to inhibit 3H-TBOB binding in mouse whole brain , with IC50 values of 4.6 , 404 and 9.4 microM , respectively .

Example answer:
{"entities": [{"text": "gamma-HCH", "type": "Chemical"}, {"text": "pentylenetetrazol", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "3H-TBOB", "type": "Chemical"}]}

Example input:
Sentence: Acetaminophen ( up to 150 micrograms/mL ) did not retard the incorporation of radioactive adenosine into ATP in slices of rat cerebral cortex .

Example answer:
{"entities": [{"text": "Acetaminophen", "type": "Chemical"}, {"text": "adenosine", "type": "Chemical"}, {"text": "ATP", "type": "Chemical"}]}

Input:
Sentence: Added in vitro to rat cortical membrane preparation , abecarnil increased [ 3H ] GABA binding , enhanced muscimol-stimulated 36Cl- uptake and reduced the binding of t- [ 35S ] butylbicyclophosphorothionate ( [ 35S ] TBPS ) .

## Item bc5cdr:test:707
Example input:
Sentence: Effect of green tea and vitamin E combination in isoproterenol induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: Effects of long-term pretreatment with isoproterenol on bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: The protective role of salvianolic acid A against isoproterenol-induced myocardial damage was further confirmed by histopathological examination .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial damage", "type": "Disease"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: 99mTc-glucarate for detection of isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "99mTc-glucarate", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: In isolated perfused heart preparations from isoproterenol-pretreated rats , the isoproterenol-induced maximal increase in left ventricular systolic pressure was significantly reduced , compared with saline-pretreated rats ( the EC50 of the isoproterenol-induced increase in left ventricular systolic pressure was enhanced approximately 22-fold ) .

Example answer:
{"entities": [{"text": "isoproterenol-pretreated", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: Histological studies demonstrated that the rats developed an infarct 18 h after isoproterenol administration .

Example answer:
{"entities": [{"text": "infarct", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: Isoproterenol pretreatment for 15 days caused cardiac hypertrophy without affecting baseline blood pressure and heart rate .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "Chemical"}, {"text": "cardiac hypertrophy", "type": "Disease"}]}

Example input:
Sentence: The effects of exercise on the severity of isoproterenol-induced myocardial infarction were studied in female albino rats of 20,40,60 and 80 weeks of age .

Example answer:
{"entities": [{"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Input:
Sentence: A morphometric study of isoproterenol induced myocardial fibrosis .

## Item bc5cdr:test:762
Example input:
Sentence: Maximal cTnI ( pg/ml ) and cTnT levels were significantly increased in DOX rats compared with controls ( p=0.006 , 0.007 ) .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: The control rats received atropine sulfate , but also saline and olive oil instead of other antidotes and DFP , respectively .

Example answer:
{"entities": [{"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: In the five rats that developed somatic rigidity , ICP and CVP increased significantly above baseline ( delta ICP 7.5 +/- 1.0 mmHg , delta CVP 5.9 +/- 1.3 mmHg ) .

Example answer:
{"entities": [{"text": "somatic rigidity", "type": "Disease"}]}

Example input:
Sentence: Pregnant rats were given either vehicle or 2 daily intraperitoneal injections of dexamethasone ( 0.2 mg/kg body weight ) on gestational days 11 and 12 , 13 and 14 , 15 and 16 , 17 and 18 , or 19 and 20 .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}]}

Example input:
Sentence: Acetaminophen ( up to 150 micrograms/mL ) did not retard the incorporation of radioactive adenosine into ATP in slices of rat cerebral cortex .

Example answer:
{"entities": [{"text": "Acetaminophen", "type": "Chemical"}, {"text": "adenosine", "type": "Chemical"}, {"text": "ATP", "type": "Chemical"}]}

Example input:
Sentence: When respiratory failure was produced by hypoventilation ( pH 7.05 to 7.25 ; PC02 70 to 100 mm Hg : P02 20 to 40 mm Hg ) , infusion of aminophylline resulted in an even greater decrease in ventricular fibrillation threshold to 60 percent of the control level .

Example answer:
{"entities": [{"text": "respiratory failure", "type": "Disease"}, {"text": "hypoventilation", "type": "Disease"}, {"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}]}

Example input:
Sentence: Streptomycin sulfate ( 300 mg/kg s.c. ) was injected for various periods into preweanling rats and for 3 weeks into weanling rats .

Example answer:
{"entities": [{"text": "Streptomycin", "type": "Chemical"}]}

Example input:
Sentence: The protective action of subcutaneously ( SC ) administered antidotes or their combinations in DFP ( 2.0 mg/kg BW ) intoxication was studied in 9-10-weeks-old Han-Wistar male rats .

Example answer:
{"entities": [{"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Reassuringly , penicillins , erythromycins , and cephalosporins , although used commonly by pregnant women , were not associated with many birth defects .

Example answer:
{"entities": [{"text": "penicillins", "type": "Chemical"}, {"text": "erythromycins", "type": "Chemical"}, {"text": "cephalosporins", "type": "Chemical"}, {"text": "birth defects", "type": "Disease"}]}

Example input:
Sentence: During the infusion of aminophylline , the ventricular fibrillation threshold was reduced by 30 to 40 percent of the control when pH and partial pressures of oxygen ( PO2 ) and carbon dioxide ( CO2 ) were kept within normal limits .

Example answer:
{"entities": [{"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}, {"text": "oxygen", "type": "Chemical"}, {"text": "PO2", "type": "Chemical"}, {"text": "carbon dioxide", "type": "Chemical"}, {"text": "CO2", "type": "Chemical"}]}

Input:
Sentence: Theophylline concentrations at this endpoint in serum ( total ) and CSF were similar but serum ( free ) and brain concentrations were slightly different in pregnant rats .

## Item bc5cdr:test:587
Example input:
Sentence: Subsequent addition of phenylephrine infusion , sufficient to re-elevate mean arterial pressure to 106 +/- 4 mm Hg ( P less than 0.001 ) for 30 minutes , increased left ventricular filling pressure to 17 +/- 2 mm Hg ( P less than 0.05 ) and also significantly increased sigmaST ( P less than 0.05 ) .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Following induction of anesthesia by fentanyl ( 0.15 mg kg ( -1 ) ) and propofol ( 2.0 mg kg ( -1 ) ) , 13 patients received phenylephrine ( 0.1 mg iv ) and 12 patients received ephedrine ( 10 mg iv ) to restore mean arterial pressure ( MAP ) .

Example answer:
{"entities": [{"text": "fentanyl", "type": "Chemical"}, {"text": "propofol", "type": "Chemical"}, {"text": "phenylephrine", "type": "Chemical"}, {"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: The patient was taking 80 mg simvastatin at bedtime ( initiated 27 days earlier ) ; amiodarone at a dose of 400 mg daily for 7 days , then 200 mg daily ( initiated 19 days earlier ) ; and 400 mg atazanavir daily ( initiated at least 2 years previously ) .

Example answer:
{"entities": [{"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: The rats received AChE reactivator pralidoxime-2-chloride ( 2PAM ) ( 30.0 mg/kg BW ) , anticonvulsant diazepam ( 2.0 mg/kg BW ) , A ( 1 ) -adenosine receptor agonist N ( 6 ) -cyclopentyl adenosine ( CPA ) ( 2.0 mg/kg BW ) , NMDA-receptor antagonist dizocilpine maleate ( +-MK801 hydrogen maleate ) ( 2.0 mg/kg BW ) or their combinations with cholinolytic drug atropine sulfate ( 50.0 mg/kg BW ) immediately or 30 min after the single SC injection of DFP .

Example answer:
{"entities": [{"text": "pralidoxime-2-chloride", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "N ( 6 ) -cyclopentyl adenosine", "type": "Chemical"}, {"text": "CPA", "type": "Chemical"}, {"text": "NMDA-receptor", "type": "Chemical"}, {"text": "dizocilpine maleate", "type": "Chemical"}, {"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: In four patients , polymorphous ventricular tachycardia appeared after intravenous administration of 200 to 400 mg of procainamide for the treatment of sustained ventricular tachycardia .

Example answer:
{"entities": [{"text": "ventricular tachycardia", "type": "Disease"}, {"text": "procainamide", "type": "Chemical"}]}

Example input:
Sentence: A dose of 50 mg/kg is recommended in those without audiogram abnormalities .

Example answer:
{"entities": []}

Example input:
Sentence: injections of organ specific three drugs ( AAP : 500 mg/Kg for 24 h ; AMI : 50 mg/Kg/day for four days ; DOX : 20 mg/Kg for 48 h ) .

Example answer:
{"entities": [{"text": "AAP", "type": "Chemical"}, {"text": "AMI", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: GR 55562 ( 0.1-10 microg/side ) , administered intra-accumbens shell prior to cocaine , dose-dependently attenuated the psychostimulant-induced locomotor hyperactivity .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}, {"text": "locomotor hyperactivity", "type": "Disease"}]}

Example input:
Sentence: A patient with sinuatrial disease and implanted pacemaker was treated with amiodarone ( maximum dose 1000 mg , maintenance dose 800 mg daily ) for 10 months , for control of supraventricular tachyarrhythmias .

Example answer:
{"entities": [{"text": "sinuatrial disease", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "supraventricular tachyarrhythmias", "type": "Disease"}]}

Input:
Sentence: The total doses of ACC-9653 or phenytoin sodium necessary to convert the arrhythmia to a normal sinus rhythm were 24 +/- 6 and 14 +/- 3 mg/kg , respectively .

## Item bc5cdr:test:730
Example input:
Sentence: Cardiac toxicity is a major complication which limits the use of adriamycin as a chemotherapeutic agent .

Example answer:
{"entities": [{"text": "Cardiac toxicity", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: A synergistic effect of etoposide and cyclosporin A was observed in a patient with acute T-lymphocytic leukemia in relapse .

Example answer:
{"entities": [{"text": "etoposide", "type": "Chemical"}, {"text": "cyclosporin A", "type": "Chemical"}, {"text": "acute T-lymphocytic leukemia", "type": "Disease"}]}

Example input:
Sentence: An allergic reaction consisting of angioneurotic edema secondary to continuous infusion 5-fluorouracil occurred in a patient with recurrent carcinoma of the oral cavity , cirrhosis , and cisplatin-induced impaired renal function .

Example answer:
{"entities": [{"text": "allergic reaction", "type": "Disease"}, {"text": "angioneurotic edema", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "carcinoma of the oral cavity", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "impaired renal function", "type": "Disease"}]}

Example input:
Sentence: In conclusion mitochondrial toxicity is an early common event both in paclitaxel and cisplatin induced neurotoxicity .

Example answer:
{"entities": [{"text": "mitochondrial toxicity", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Cardiac toxicity observed in association with high-dose cyclophosphamide-based chemotherapy for metastatic breast cancer .

Example answer:
{"entities": [{"text": "Cardiac toxicity", "type": "Disease"}, {"text": "cyclophosphamide-based", "type": "Chemical"}, {"text": "breast cancer", "type": "Disease"}]}

Example input:
Sentence: A 61-year-old man was treated with combination chemotherapy incorporating cisplatinum , etoposide , high-dose 5-fluorouracil ( 2,250 mg/m2/24 hours ) and folinic acid for an inoperable gastric adenocarcinoma .

Example answer:
{"entities": [{"text": "cisplatinum", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}, {"text": "gastric adenocarcinoma", "type": "Disease"}]}

Example input:
Sentence: CNS complications included posterior reversible leukoencephalopathy syndrome ( n = 10 ) , stroke ( n = 5 ) , temporal lobe epilepsy ( n = 2 ) , high-dose methotrexate toxicity ( n = 2 ) , syndrome of inappropriate antidiuretic hormone secretion ( n = 1 ) , and other unclassified events ( n = 7 ) .

Example answer:
{"entities": [{"text": "leukoencephalopathy", "type": "Disease"}, {"text": "stroke", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "inappropriate antidiuretic hormone secretion", "type": "Disease"}]}

Example input:
Sentence: Our experience supports the safety of giving AraG as salvage therapy in synchrony with etoposide and cyclophosphamide , although neurological toxicity must be closely monitored .

Example answer:
{"entities": [{"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "neurological toxicity", "type": "Disease"}]}

Example input:
Sentence: Severe ocular and orbital toxicity after intracarotid injection of carboplatin for recurrent glioblastomas .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}, {"text": "glioblastomas", "type": "Disease"}]}

Input:
Sentence: This complication appears to represent a significant new toxicity of high-dose etoposide therapy for malignant glioma .

## Item bc5cdr:test:74
Example input:
Sentence: Isoproterenol pretreatment for 15 days caused cardiac hypertrophy without affecting baseline blood pressure and heart rate .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "Chemical"}, {"text": "cardiac hypertrophy", "type": "Disease"}]}

Example input:
Sentence: However , L-dopa restored the bradycardia caused by norepinephrine in addition to decreasing blood pressure and heart rate .

Example answer:
{"entities": [{"text": "L-dopa", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}]}

Example input:
Sentence: Dose-dependent bradycardia induced by verapamil was potentiated by LNa , LCa , and HCa .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: Sulfonamides were associated with anencephaly ( adjusted OR [ AOR ] = 3.4 ; 95 % confidence interval [ CI ] , 1.3-8.8 ) , hypoplastic left heart syndrome ( AOR = 3.2 ; 95 % CI , 1.3-7.6 ) , coarctation of the aorta ( AOR = 2.7 ; 95 % CI , 1.3-5.6 ) , choanal atresia ( AOR = 8.0 ; 95 % CI , 2.7-23.5 ) , transverse limb deficiency ( AOR = 2.5 ; 95 % CI , 1.0-5.9 ) , and diaphragmatic hernia ( AOR = 2.4 ; 95 % CI , 1.1-5.4 ) .

Example answer:
{"entities": [{"text": "Sulfonamides", "type": "Chemical"}, {"text": "anencephaly", "type": "Disease"}, {"text": "hypoplastic left heart syndrome", "type": "Disease"}, {"text": "coarctation of the aorta", "type": "Disease"}, {"text": "choanal atresia", "type": "Disease"}, {"text": "transverse limb deficiency", "type": "Disease"}, {"text": "diaphragmatic hernia", "type": "Disease"}]}

Example input:
Sentence: RESULTS : There were more incidents of bradycardia in subjects treated with clonidine compared with those not treated with clonidine ( 17.5 % versus 3.4 % ; p =.02 ) , but no other significant group differences regarding electrocardiogram and other cardiovascular outcomes .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: A frequency of bradycardia of 50 % was noted in the control group , but this was not significantly different from the frequency with the active drugs .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Bromocriptine-induced hypotension was unaffected by isoproterenol pretreatment , while tachycardia was reversed to significant bradycardia , an effect that was partly reduced by i.v .

Example answer:
{"entities": [{"text": "Bromocriptine-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: These differences may be caused by timolol-induced bradycardia and a compensatory increase in end-diastolic volume .

Example answer:
{"entities": [{"text": "timolol-induced", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Seven patients suffering from Parkinson 's disease ( PD ) with severely disabling dyskinesia received low-dose propranolol as an adjunct to the currently used medical treatment .

Example answer:
{"entities": [{"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "propranolol", "type": "Chemical"}]}

Input:
Sentence: We conclude that previously reported hypoglycemia , hyperbilirubinemia , polycythemia , neonatal apnea , and bradycardia are not invariable and can not be statistically correlated with chronic propranolol therapy .

## Item bc5cdr:test:534
Example input:
Sentence: In behavioral studies , pre-treatment of mice with BD1018 , BD1063 , or LR132 significantly attenuated cocaine-induced convulsions and lethality .

Example answer:
{"entities": [{"text": "BD1018", "type": "Chemical"}, {"text": "BD1063", "type": "Chemical"}, {"text": "LR132", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: A comparable overexpression of Pgp in the BBB was obtained after pilocarpine-induced seizures in wild-type Wistar rats .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Apamin , a selective blocker of calcium-dependent potassium channels , was administered intracerebroventricularly in rats anesthetized with 0.8 % sevoflurane to investigate the mechanism of the anticonvulsive effects .

Example answer:
{"entities": [{"text": "Apamin", "type": "Chemical"}, {"text": "calcium-dependent", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}, {"text": "sevoflurane", "type": "Chemical"}]}

Example input:
Sentence: Investigation of mitochondrial involvement in the experimental model of epilepsy induced by pilocarpine .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: Based on the finding that VPU and VPA could protect the animals against pilocarpine-induced seizure it is suggested that the reduction of inhibitory amino acid neurotransmitters was comparatively minor and offset by a pronounced reduction of glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: VPU was more potent than VPA , exhibiting the median effective dose ( ED ( 50 ) ) of 49 mg/kg in protecting rats against pilocarpine-induced seizure whereas the corresponding value for VPA was 322 mg/kg .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Therefore , like VPA , the finding that VPU could drastically reduce pilocarpine-induced increases in glutamate and aspartate should account , at least partly , for its anticonvulsant activity observed in pilocarpine-induced seizure in experimental animals .

Example answer:
{"entities": [{"text": "VPA", "type": "Chemical"}, {"text": "VPU", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Input:
Sentence: First , pretreatment with MK-801 produced an effective and dose-dependent anticonvulsant action with the lithium-pilocarpine model but not with rats treated with pilocarpine alone , suggesting that different biochemical mechanisms control seizures in these two models .

## Item bc5cdr:test:863
Example input:
Sentence: Nimodipine treatment resulted in a statistically significant reduction in systolic BP ( SBP ) and diastolic BP ( DBP ) from baseline compared with placebo during the first few days .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "Chemical"}, {"text": "reduction in systolic BP", "type": "Disease"}]}

Example input:
Sentence: She was treated with heparin , dipyridamole and hemodialysis ; and after more than three months , her urinary output rose above 500 ml ; and six months after the onset of anuria , dialysis treatment was stopped .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "anuria", "type": "Disease"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Mitochondrial radiocalcium uptakes were significantly decreased in animals pretreated with acetylsalicylic acid or dipyridamole or when hydrocortisone was added to the epinephrine infusion ( 2,682,2,803 , and 3,424 counts per minute per gram of dried fraction , respectively ) .

Example answer:
{"entities": [{"text": "radiocalcium", "type": "Chemical"}, {"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine", "type": "Chemical"}]}

Example input:
Sentence: Dipyridamole-induced myocardial ischemia .

Example answer:
{"entities": [{"text": "Dipyridamole-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}]}

Example input:
Sentence: To our knowledge , this has not previously been reported as a side effect of preoperative dipyridamole therapy , although dipyridamole-induced myocardial ischemia has been demonstrated to occur in animals and humans with coronary artery disease .

Example answer:
{"entities": [{"text": "dipyridamole", "type": "Chemical"}, {"text": "dipyridamole-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "coronary artery disease", "type": "Disease"}]}

Example input:
Sentence: Neither dose of pentoxifylline significantly decreased the dipyridamole-induced hyperemia , while peak coronary blood flow was significantly lower after theophylline ( p less than 0.01 ) .

Example answer:
{"entities": [{"text": "pentoxifylline", "type": "Chemical"}, {"text": "dipyridamole-induced", "type": "Chemical"}, {"text": "hyperemia", "type": "Disease"}, {"text": "theophylline", "type": "Chemical"}]}

Example input:
Sentence: Angina and ischemic electrocardiographic changes occurred after administration of oral dipyridamole in four patients awaiting urgent myocardial revascularization procedures .

Example answer:
{"entities": [{"text": "Angina", "type": "Disease"}, {"text": "dipyridamole", "type": "Chemical"}]}

Example input:
Sentence: Therefore , we studied the hyperemic response to dipyridamole in seven open-chest anesthetized dogs after pretreatment with either pentoxifylline ( 0 , 7.5 , or 15 mg/kg i.v . )

Example answer:
{"entities": [{"text": "dipyridamole", "type": "Chemical"}, {"text": "pentoxifylline", "type": "Chemical"}]}

Example input:
Sentence: Dipyridamole significantly increased coronary blood flow before and after 7.5 or 15 mm/kg i.v .

Example answer:
{"entities": [{"text": "Dipyridamole", "type": "Chemical"}]}

Input:
Sentence: The increase in pressure rate product after dipyridamole was significantly less than that during the treadmill exercise .

## Item bc5cdr:test:640
Example input:
Sentence: Newborn rats were given terbutaline ( 10 mg/kg ) daily on postnatal days ( PN ) 2 to 5 or PN 11 to 14 and examined 24 h after the last dose and at PN 30 .

Example answer:
{"entities": [{"text": "terbutaline", "type": "Chemical"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: In the remaining three patients , procainamide was administered orally for treatment of chronic premature ventricular contractions or atrial flutter .

Example answer:
{"entities": [{"text": "procainamide", "type": "Chemical"}, {"text": "premature ventricular contractions", "type": "Disease"}, {"text": "atrial flutter", "type": "Disease"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Acute bronchodilating effects of ipratropium bromide and theophylline in chronic obstructive pulmonary disease .

Example answer:
{"entities": [{"text": "ipratropium bromide", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}, {"text": "chronic obstructive pulmonary disease", "type": "Disease"}]}

Example input:
Sentence: Immunohistochemical studies showed that administration of terbutaline on PN 2 to 5 produced a robust increase in microglial activation on PN 30 in the cerebral cortex , as well as in cerebellar and cerebrocortical white matter .

Example answer:
{"entities": [{"text": "terbutaline", "type": "Chemical"}]}

Example input:
Sentence: The bronchodilator effects of a single dose of ipratropium bromide aerosol ( 36 micrograms ) and short-acting theophylline tablets ( dose titrated to produce serum levels of 10-20 micrograms/mL ) were compared in a double-blind , placebo-controlled crossover study in 21 patients with stable , chronic obstructive pulmonary disease .

Example answer:
{"entities": [{"text": "ipratropium bromide", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}, {"text": "chronic obstructive pulmonary disease", "type": "Disease"}]}

Example input:
Sentence: In behavioral tests , animals treated with terbutaline on PN 2 to 5 showed consistent patterns of hyper-reactivity to novelty and aversive stimuli when assessed in a novel open field , as well as in the acoustic startle response test .

Example answer:
{"entities": [{"text": "terbutaline", "type": "Chemical"}]}

Example input:
Sentence: These results show that ipratropium is a more potent bronchodilator than oral theophylline in patients with chronic airflow obstruction .

Example answer:
{"entities": [{"text": "ipratropium", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}, {"text": "chronic airflow obstruction", "type": "Disease"}]}

Example input:
Sentence: Terbutaline , a beta2-adrenoceptor agonist used to arrest preterm labor , has been associated with increased concordance for autism in dizygotic twins .

Example answer:
{"entities": [{"text": "Terbutaline", "type": "Chemical"}, {"text": "preterm labor", "type": "Disease"}, {"text": "autism", "type": "Disease"}]}

Input:
Sentence: Procaterol and terbutaline in bronchial asthma .

## Item bc5cdr:test:551
Example input:
Sentence: METHOD : In a 6-week random-assignment , double-blind , placebo-controlled trial ( phase A ) , haloperidol , 2-3 mg/day ( standard dose ) , and haloperidol , 0.50-0.75 mg/day ( low dose ) , were compared in 71 outpatients with Alzheimer 's disease .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "Alzheimer 's disease", "type": "Disease"}]}

Example input:
Sentence: A randomized , placebo-controlled dose-comparison trial of haloperidol for psychosis and disruptive behaviors in Alzheimer 's disease .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "psychosis", "type": "Disease"}, {"text": "disruptive behaviors", "type": "Disease"}, {"text": "Alzheimer 's disease", "type": "Disease"}]}

Example input:
Sentence: Haloperidol administration ( one dose of 12 mg/kg once a week s.c. ) for 4 weeks caused an increase in vacuous chewing , tongue protrusion and duration of facial twitching observed in four weekly evaluations .

Example answer:
{"entities": [{"text": "Haloperidol", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVE : The goal of this study was to compare the efficacy and side effects of two doses of haloperidol and placebo in the treatment of psychosis and disruptive behaviors in patients with Alzheimer 's disease .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "psychosis", "type": "Disease"}, {"text": "disruptive behaviors", "type": "Disease"}, {"text": "Alzheimer 's disease", "type": "Disease"}]}

Example input:
Sentence: RESULTS : For the 60 patients who completed phase A , standard-dose haloperidol was efficacious and superior to both low-dose haloperidol and placebo for scores on the Brief Psychiatric Rating Scale psychosis factor and on psychomotor agitation .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "psychosis", "type": "Disease"}, {"text": "psychomotor agitation", "type": "Disease"}]}

Example input:
Sentence: On the contrary , the cataleptogenic effect of haloperidol was significantly reduced in rats treated with desipramine and 6-OHDA but not in rats treated with 6-OHDA or in rats with lesions of the locus coeruleus .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "desipramine", "type": "Chemical"}, {"text": "6-OHDA", "type": "Chemical"}]}

Example input:
Sentence: Significant blockade of cocaine toxicity was observed with the higher dose of GNC92H2 ( 190 mg/kg ) , where premorbid behaviors were reduced up to 40 % , seizures up to 77 % and death by 72 % .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "GNC92H2", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "death", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : The results indicated a favorable therapeutic profile for haloperidol in doses of 2-3 mg/day , although a subgroup developed moderate to severe extrapyramidal signs .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "extrapyramidal signs", "type": "Disease"}]}

Example input:
Sentence: In the double blind study with haloperidol , both substances were found to be highly effective in the treatment of psychotic syndromes belonging predominantly to the schizophrenia group .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "psychotic syndromes belonging predominantly to the schizophrenia group", "type": "Disease"}]}

Example input:
Sentence: 1 h prior to haloperidol resulted in a dose-dependent increase in the catalepsy times ( P < 0.05 ) .

Example answer:
{"entities": []}

Input:
Sentence: Haloperidol decreased the incidence of cocaine-induced seizures at the two highest doses , but the lowering of the mortality rate did not reach statistical significance at any dose .

## Item bc5cdr:test:674
Example input:
Sentence: METHODS : We present the first case report of a woman with hyperthyroidism treated with propylthiouracil in whom a syndrome of pericarditis , fever , and glomerulonephritis developed .

Example answer:
{"entities": [{"text": "hyperthyroidism", "type": "Disease"}, {"text": "propylthiouracil", "type": "Chemical"}, {"text": "pericarditis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "glomerulonephritis", "type": "Disease"}]}

Example input:
Sentence: A detailed clinical history , together with skin tests , RAST ( radioallergosorbent test ) , and controlled challenge tests , was used to establish whether patients allergic to beta-lactam antibiotics had selective immediate allergic responses to amoxicillin ( AX ) or were cross-reacting with other penicillin derivatives .

Example answer:
{"entities": [{"text": "allergic", "type": "Disease"}, {"text": "beta-lactam", "type": "Chemical"}, {"text": "amoxicillin", "type": "Chemical"}, {"text": "AX", "type": "Chemical"}, {"text": "penicillin", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVE : To report a case of erythema multiforme and hypersensitivity myocarditis caused by ampicillin .

Example answer:
{"entities": [{"text": "erythema multiforme", "type": "Disease"}, {"text": "hypersensitivity myocarditis", "type": "Disease"}, {"text": "ampicillin", "type": "Chemical"}]}

Example input:
Sentence: A large group of patients with suspected allergic reactions to beta-lactam antibiotics was evaluated .

Example answer:
{"entities": [{"text": "allergic reactions", "type": "Disease"}, {"text": "beta-lactam", "type": "Chemical"}]}

Example input:
Sentence: Anaphylaxis was seen in 37 patients ( 69 % ) , the other 17 ( 31 % ) having urticaria and/or angioedema .

Example answer:
{"entities": [{"text": "Anaphylaxis", "type": "Disease"}, {"text": "urticaria", "type": "Disease"}, {"text": "angioedema", "type": "Disease"}]}

Example input:
Sentence: A patient who received antithymocyte globulin therapy for aplastic anemia due to D-penicillamine therapy is described .

Example answer:
{"entities": [{"text": "antithymocyte globulin", "type": "Chemical"}, {"text": "aplastic anemia", "type": "Disease"}, {"text": "D-penicillamine", "type": "Chemical"}]}

Example input:
Sentence: We present a case of paramedic misjudgment in the execution of a protocol for the treatment of allergic reaction in a case of pulmonary edema with wheezing .

Example answer:
{"entities": [{"text": "allergic reaction", "type": "Disease"}, {"text": "pulmonary edema", "type": "Disease"}, {"text": "wheezing", "type": "Disease"}]}

Example input:
Sentence: However , acetaminophen has been demonstrated to produce symptoms of anaphylaxis , including hypotension , in sensitive individuals .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "anaphylaxis", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Hypersensitivity myocarditis is a rare and dangerous manifestation of allergy to penicillins .

Example answer:
{"entities": [{"text": "Hypersensitivity myocarditis", "type": "Disease"}, {"text": "allergy", "type": "Disease"}, {"text": "penicillins", "type": "Chemical"}]}

Example input:
Sentence: CASE SUMMARY : A 13-year-old boy was treated with ampicillin and gentamicin because of suspected septicemia .

Example answer:
{"entities": [{"text": "ampicillin", "type": "Chemical"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "septicemia", "type": "Disease"}]}

Input:
Sentence: A case of oral penicillin anaphylaxis is described , and the terminology , occurrence , clinical manifestations , pathogenesis , prevention , and treatment of anaphylaxis are reviewed .

## Item bc5cdr:test:679
Example input:
Sentence: CNS complications included posterior reversible leukoencephalopathy syndrome ( n = 10 ) , stroke ( n = 5 ) , temporal lobe epilepsy ( n = 2 ) , high-dose methotrexate toxicity ( n = 2 ) , syndrome of inappropriate antidiuretic hormone secretion ( n = 1 ) , and other unclassified events ( n = 7 ) .

Example answer:
{"entities": [{"text": "leukoencephalopathy", "type": "Disease"}, {"text": "stroke", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "inappropriate antidiuretic hormone secretion", "type": "Disease"}]}

Example input:
Sentence: The present study aimed to investigate the anticonvulsant activity as well as the effects on the level of hippocampal amino acid neurotransmitters ( glutamate , aspartate , glycine and GABA ) of N- ( 2-propylpentanoyl ) urea ( VPU ) in comparison to its parent compound , valproic acid ( VPA ) .

Example answer:
{"entities": [{"text": "amino acid", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}, {"text": "N- ( 2-propylpentanoyl ) urea", "type": "Chemical"}, {"text": "VPU", "type": "Chemical"}, {"text": "valproic acid", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}]}

Example input:
Sentence: Long-term intragastric application of the antiepileptic drug sodium valproate ( Vupral `` Polfa '' ) at the effective dose of 200 mg/kg b. w. once daily to rats for 1 , 3 , 6 , 9 and 12 months revealed neurological disorders indicating cerebellum damage ( `` valproate encephalopathy '' ) .

Example answer:
{"entities": [{"text": "sodium valproate", "type": "Chemical"}, {"text": "neurological disorders", "type": "Disease"}, {"text": "cerebellum damage", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Encephalopathy induced by levetiracetam added to valproate .

Example answer:
{"entities": [{"text": "Encephalopathy", "type": "Disease"}, {"text": "levetiracetam", "type": "Chemical"}, {"text": "valproate", "type": "Chemical"}]}

Example input:
Sentence: A case of valproate-induced encephalopathy is presented .

Example answer:
{"entities": [{"text": "valproate-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Valproate-induced encephalopathy .

Example answer:
{"entities": [{"text": "Valproate-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Morphological features of encephalopathy after chronic administration of the antiepileptic drug valproate to rats .

Example answer:
{"entities": [{"text": "encephalopathy", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}]}

Example input:
Sentence: Valproic acid induced encephalopathy -- 19 new cases in Germany from 1994 to 2003 -- a side effect associated to VPA-therapy not only in young children .

Example answer:
{"entities": [{"text": "Valproic acid", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "VPA-therapy", "type": "Chemical"}]}

Example input:
Sentence: Valproate-induced encephalopathy is a rare syndrome that may manifest in otherwise normal epileptic individuals .

Example answer:
{"entities": [{"text": "Valproate-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "epileptic", "type": "Disease"}]}

Example input:
Sentence: The possible influence of the hepatic damage , mainly hyperammonemia , upon the development of valproate encephalopathy is discussed .

Example answer:
{"entities": [{"text": "hepatic damage", "type": "Disease"}, {"text": "hyperammonemia", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Input:
Sentence: Possible pathophysiological mechanisms which may have been operative in this case include : a direct central nervous system ( CNS ) toxic effect of valproic acid ; a paradoxical epileptogenic effect secondary to the drug ; and an indirect CNS toxic effect mediated through valproic acid-induced hyperammonemia .

## Item bc5cdr:test:765
Example input:
Sentence: The cataleptogenic effect of THC was significantly reduced in rats treated with 6-OHDA and in rats with lesions of the locus coeruleus but not in rats treated with desipramine and 6-OHDA , as compared with control rats .

Example answer:
{"entities": [{"text": "THC", "type": "Chemical"}, {"text": "6-OHDA", "type": "Chemical"}, {"text": "desipramine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : Both selective and non-selective COX-2 inhibitors were toxic for rats fetuses when administered in the highest dose .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Maternal toxicity , intrauterine growth retardation , and increase of external and skeletal variations were found in rats treated with the highest dose of piroxicam .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "intrauterine growth retardation", "type": "Disease"}, {"text": "increase of external and skeletal variations", "type": "Disease"}, {"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: This animal model may be useful to explore the mechanisms by which prenatal nutritional deficiency enhances risk for schizophrenia in humans and may also have implications for developmental processes leading to differential sensitivity to drugs of abuse .

Example answer:
{"entities": [{"text": "nutritional deficiency", "type": "Disease"}, {"text": "schizophrenia", "type": "Disease"}]}

Example input:
Sentence: Age-dependent sensitivity of the rat to neurotoxic effects of streptomycin .

Example answer:
{"entities": [{"text": "neurotoxic", "type": "Disease"}, {"text": "streptomycin", "type": "Chemical"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Estrogens protect ovariectomized rats from hippocampal injury induced by kainic acid-induced status epilepticus ( SE ) .

Example answer:
{"entities": [{"text": "hippocampal injury", "type": "Disease"}, {"text": "kainic", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Pregnant rats were administered one of these calcium channel blockers during the period of cardiac morphogenesis and the offspring examined on day 20 of gestation for cardiovascular malformations .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "cardiovascular malformations", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Reassuringly , penicillins , erythromycins , and cephalosporins , although used commonly by pregnant women , were not associated with many birth defects .

Example answer:
{"entities": [{"text": "penicillins", "type": "Chemical"}, {"text": "erythromycins", "type": "Chemical"}, {"text": "cephalosporins", "type": "Chemical"}, {"text": "birth defects", "type": "Disease"}]}

Example input:
Sentence: We report that prenatally protein deprived ( PD ) female rats showed an increased stereotypic response to apomorphine and an increased locomotor response to amphetamine in adulthood .

Example answer:
{"entities": [{"text": "apomorphine", "type": "Chemical"}, {"text": "amphetamine", "type": "Chemical"}]}

Input:
Sentence: It is concluded that advanced pregnancy has a negligible effect on the neurotoxic response to theophylline in rats .

## Item bc5cdr:test:681
Example input:
Sentence: Acute antinociceptive effects of the combination were partially prevented by 3.2 mg/kg naloxone s.c. ( P < 0.05 ) , suggesting the partial involvement of the opioidergic system in the synergism observed .

Example answer:
{"entities": [{"text": "naloxone", "type": "Chemical"}]}

Example input:
Sentence: Diazepam- , scopolamine- and ageing-induced amnesia served as the interoceptive behavioral models .

Example answer:
{"entities": [{"text": "Diazepam-", "type": "Chemical"}, {"text": "scopolamine-", "type": "Chemical"}, {"text": "amnesia", "type": "Disease"}]}

Example input:
Sentence: The present study was designed to study the effect of histamine H ( 3 ) -receptor ligands on neuroleptic-induced catalepsy , apomorphine-induced climbing behavior and amphetamine-induced locomotor activities in mice .

Example answer:
{"entities": [{"text": "histamine", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "apomorphine-induced", "type": "Chemical"}, {"text": "amphetamine-induced", "type": "Chemical"}]}

Example input:
Sentence: In conclusion , although Ro4368554 did not improve a time-related retention deficit , it reversed a cholinergic and a serotonergic memory deficit , suggesting that both mechanisms may be involved in the facilitation of object memory by Ro4368554 and , possibly , other 5-HT ( 6 ) receptor antagonists .

Example answer:
{"entities": [{"text": "memory", "type": "Disease"}]}

Example input:
Sentence: The present study sought to characterize the cognitive-enhancing effects of the 5-HT ( 6 ) antagonist Ro4368554 ( 3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole ) in a rat object recognition task employing a cholinergic ( scopolamine pretreatment ) and a serotonergic- ( tryptophan ( TRP ) depletion ) deficient model , and compared its pattern of action with that of the acetylcholinesterase inhibitor metrifonate .

Example answer:
{"entities": [{"text": "5-HT", "type": "Chemical"}, {"text": "Ro4368554", "type": "Chemical"}, {"text": "3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole", "type": "Chemical"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "tryptophan", "type": "Chemical"}, {"text": "TRP", "type": "Chemical"}, {"text": "metrifonate", "type": "Chemical"}]}

Example input:
Sentence: The findings of this study indicate that the drug is able to antagonize impairment of attention and memory induced by scopolamine .

Example answer:
{"entities": [{"text": "impairment of attention and memory", "type": "Disease"}, {"text": "scopolamine", "type": "Chemical"}]}

Example input:
Sentence: In brain membranes from spontaneously hypertensive rats clonidine , 10 ( -8 ) to 10 ( -5 ) M , did not influence stereoselective binding of [ 3H ] -naloxone ( 8 nM ) , and naloxone , 10 ( -8 ) to 10 ( -4 ) M , did not influence clonidine-suppressible binding of [ 3H ] -dihydroergocryptine ( 1 nM ) .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}, {"text": "clonidine", "type": "Chemical"}, {"text": "[ 3H ] -naloxone", "type": "Chemical"}, {"text": "naloxone", "type": "Chemical"}, {"text": "clonidine-suppressible", "type": "Chemical"}, {"text": "[ 3H ] -dihydroergocryptine", "type": "Chemical"}]}

Example input:
Sentence: Facilitation of memory retrieval by pre-test morphine and its state dependency in the step-through type passive avoidance learning test in mice .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: As naloxone and clonidine do not appear to interact with the same receptor site , the observed functional antagonism suggests the release of an endogenous opiate by clonidine or alpha-methyldopa and the possible role of the opiate in the central control of sympathetic tone .

Example answer:
{"entities": [{"text": "naloxone", "type": "Chemical"}, {"text": "clonidine", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}]}

Example input:
Sentence: Amnesia produced by scopolamine and cycloheximide were reversed by morphine given 30 min before the test trial ( pre-test ) , and pre-test morphine also facilitated the memory retrieval in the animals administered naloxone during the training trial .

Example answer:
{"entities": [{"text": "Amnesia", "type": "Disease"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "cycloheximide", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}, {"text": "naloxone", "type": "Chemical"}]}

Input:
Sentence: In a series of five experiments , the modulating role of naloxone on a scopolamine-induced retention deficit in a passive avoidance paradigm was investigated in mice .

## Item bc5cdr:test:933
Example input:
Sentence: The [ verapamil ] o that arrested atrial beating ( AC ) was also potentiated with the order LNa = LNa+LCa = LNa+HCa = LCa > HCa = N. The results indicate that rat atrial spontaneous beating is more dependent on [ Na ] o than on [ Ca ] o in a range of +/- 50 % of their normal concentration .

Example answer:
{"entities": [{"text": "verapamil", "type": "Chemical"}, {"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}]}

Example input:
Sentence: The effects of varying the extracellular concentrations of Na and Ca ( [ Na ] o and [ Ca ] o ) on both , the spontaneous beating and the negative chronotropic action of verapamil , were studied in the isolated rat atria .

Example answer:
{"entities": [{"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: Age-related changes in ultrasound production corresponded with changes in cardiovascular variables , including baseline cardiac rate and clonidine-induced bradycardia .

Example answer:
{"entities": [{"text": "clonidine-induced", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: His bundle recordings showed an atrial tachycardia with intermittent exit block and greatly prolonged BH and HV intervals ( 40 and 100 msec , respectively ) .

Example answer:
{"entities": [{"text": "atrial tachycardia", "type": "Disease"}]}

Example input:
Sentence: A patient is reported who developed progressive cardiomyopathy two and one-half years after receiving 580 mg/m2 which apparently represents late , late cardiotoxicity .

Example answer:
{"entities": [{"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: At termination of the experiments , mice underwent echocardiography , quantitation of abundance of molecular markers of CM ( ventricular mRNA encoding atrial natriuretic factor [ ANF ] and sarcoplasmic calcium ATPase [ SERCA2 ] ) , and determination of plasma LA .

Example answer:
{"entities": [{"text": "CM", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "LA", "type": "Chemical"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Example input:
Sentence: The effects of exercise on the severity of isoproterenol-induced myocardial infarction were studied in female albino rats of 20,40,60 and 80 weeks of age .

Example answer:
{"entities": [{"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Input:
Sentence: Analysis of in vivo myocardial excitability , contractility , and metabolic characteristics at 16 months revealed other significant barium-induced disturbances within the cardiovascular system .

## Item bc5cdr:test:564
Example input:
Sentence: It is concluded that flestolol is a potent , well-tolerated , ultra-short-acting beta-adrenergic blocking agent .

Example answer:
{"entities": [{"text": "flestolol", "type": "Chemical"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Vasopressor agents are used to correct anesthesia-induced hypotension .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: The role of the renin -- angiotensin system in the maintenance of blood pressure during halothane anesthesia and sodium nitroprusside ( SNP ) -induced hypotension was evaluated .

Example answer:
{"entities": [{"text": "angiotensin", "type": "Chemical"}, {"text": "halothane", "type": "Chemical"}, {"text": "sodium nitroprusside", "type": "Chemical"}, {"text": "SNP", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: METHODS : Following induction of anesthesia by fentanyl ( 0.15 mg kg ( -1 ) ) and propofol ( 2.0 mg kg ( -1 ) ) , 13 patients received phenylephrine ( 0.1 mg iv ) and 12 patients received ephedrine ( 10 mg iv ) to restore mean arterial pressure ( MAP ) .

Example answer:
{"entities": [{"text": "fentanyl", "type": "Chemical"}, {"text": "propofol", "type": "Chemical"}, {"text": "phenylephrine", "type": "Chemical"}, {"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: Following instrumentation , halothane was discontinued and alfentanil ( 125 mu/kg ) administered iv during emergence from halothane anesthesia .

Example answer:
{"entities": [{"text": "halothane", "type": "Chemical"}, {"text": "alfentanil", "type": "Chemical"}]}

Example input:
Sentence: After intravenous administration of labetalol , metoprolol and midazolam the patient 's condition improved , and 15 min later he woke up .

Example answer:
{"entities": [{"text": "labetalol", "type": "Chemical"}, {"text": "metoprolol", "type": "Chemical"}, {"text": "midazolam", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: A randomized comparison of labetalol and nitroprusside for induced hypotension .

Example answer:
{"entities": [{"text": "labetalol", "type": "Chemical"}, {"text": "nitroprusside", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: In a randomized study , labetalol-induced hypotension and nitroprusside-induced hypotension were compared in 20 patients ( 10 in each group ) scheduled for major orthopedic procedures .

Example answer:
{"entities": [{"text": "labetalol-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "nitroprusside-induced", "type": "Chemical"}]}

Input:
Sentence: The feasibility of using labetalol , an alpha- and beta-adrenergic blocking agent , as a hypotensive agent in combination with inhalation anaesthetics ( halothane , enflurane or isoflurane ) was studied in 23 adult patients undergoing middle-ear surgery .

## Item bc5cdr:test:1012
Example input:
Sentence: Such an effect was , however , reversed in presence of RAMH .

Example answer:
{"entities": []}

Example input:
Sentence: These effects gave rise to an increase in the right atrial pressure and a decrease in the left one with a consequent stretching of the foramen ovale and the creation of massive right-to-left shunting .

Example answer:
{"entities": []}

Example input:
Sentence: A reversible anemia was the only adverse effect observed .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}]}

Example input:
Sentence: All these effects of DES were more pronounced among previously ovariectomized animals .

Example answer:
{"entities": [{"text": "DES", "type": "Chemical"}]}

Example input:
Sentence: Older subjects tended to display more side effects .

Example answer:
{"entities": []}

Example input:
Sentence: Any true difference between the agents is small and not likely to be clinically significant .

Example answer:
{"entities": []}

Example input:
Sentence: This effect was more relevant in patients treated with higher doses .

Example answer:
{"entities": []}

Example input:
Sentence: The differences in mortality and morbidity between the two groups were not significant .

Example answer:
{"entities": []}

Example input:
Sentence: The major effect was on dystonia subscore .

Example answer:
{"entities": [{"text": "dystonia", "type": "Disease"}]}

Example input:
Sentence: No differences were observed with respect to side effects and general tolerability .

Example answer:
{"entities": []}

Input:
Sentence: The difference in the effects of the two was significant .

## Item bc5cdr:test:654
Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: The pooled statistical analysis for ventricular septal ( VSD ) and midline ( MD ) defects was performed for rat fetuses exposed to piroxicam , selective and non-selective COX-2 inhibitor based on present and historic data .

Example answer:
{"entities": [{"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: As a consequence of blocking I ( f ) , clonidine reduced the slope of the diastolic depolarization and the frequency of pacemaker potentials in sinoatrial node cells from wild-type and alpha2ABC-knockout mice .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: In addition , mitochondrial respiratory dysfunction characterized by decreased respiratory control ratio and ADP/O was observed in isoproterenol-treated rats .

Example answer:
{"entities": [{"text": "respiratory dysfunction", "type": "Disease"}, {"text": "ADP/O", "type": "Chemical"}, {"text": "isoproterenol-treated", "type": "Chemical"}]}

Example input:
Sentence: TCR prevented the isoproterenol-induced decrease in antioxidant enzymes in the heart and increased the rate of ADP-stimulated oxygen uptake and respiratory coupling ratio .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "ADP-stimulated", "type": "Chemical"}, {"text": "oxygen", "type": "Chemical"}]}

Example input:
Sentence: In the five rats that developed somatic rigidity , ICP and CVP increased significantly above baseline ( delta ICP 7.5 +/- 1.0 mmHg , delta CVP 5.9 +/- 1.3 mmHg ) .

Example answer:
{"entities": [{"text": "somatic rigidity", "type": "Disease"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Isoproterenol pretreatment for 15 days caused cardiac hypertrophy without affecting baseline blood pressure and heart rate .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "Chemical"}, {"text": "cardiac hypertrophy", "type": "Disease"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/", "type": "Chemical"}, {"text": "K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Input:
Sentence: Neither propranolol nor B 24/76 could stop the changes in the characteristic myosin isoenzyme pattern of the hypertrophied rat heart .
