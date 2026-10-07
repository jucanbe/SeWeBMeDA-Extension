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

## Item bc5cdr:test:1342
Example input:
Sentence: Five patients with carcinoma developed thrombotic microangiopathy ( characterized by renal insufficiency , microangiopathic hemolytic anemia , and usually thrombocytopenia ) after treatment with cisplatin , bleomycin , and a vinca alkaloid .

Example answer:
{"entities": [{"text": "carcinoma", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "microangiopathic hemolytic anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "bleomycin", "type": "Chemical"}, {"text": "vinca alkaloid", "type": "Chemical"}]}

Example input:
Sentence: The first case involved a 59-year-old man who used Dormex , which contains hydrogen cyanamide , without protection after consuming a large amount of alcohol during a meal .

Example answer:
{"entities": [{"text": "Dormex", "type": "Chemical"}, {"text": "hydrogen cyanamide", "type": "Chemical"}, {"text": "alcohol", "type": "Chemical"}]}

Example input:
Sentence: We describe a 25-year-old woman with pre-existing mitral valve prolapse who developed intractable ventricular fibrillation after consuming a `` natural energy '' guarana health drink containing a high concentration of caffeine .

Example answer:
{"entities": [{"text": "mitral valve prolapse", "type": "Disease"}, {"text": "ventricular fibrillation", "type": "Disease"}, {"text": "caffeine", "type": "Chemical"}]}

Example input:
Sentence: We present a 43-year-old man who developed a coronary aneurysm in the right coronary artery 6 months after receiving a paclitaxel-eluting stent .

Example answer:
{"entities": [{"text": "coronary aneurysm", "type": "Disease"}, {"text": "paclitaxel-eluting", "type": "Chemical"}]}

Example input:
Sentence: The present report describes a case of cardiac arrest and subsequent death as a result of hyperkalaemia following the use of suxamethonium in a 23-year-old Malawian woman .

Example answer:
{"entities": [{"text": "cardiac arrest", "type": "Disease"}, {"text": "death", "type": "Disease"}, {"text": "hyperkalaemia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: A 78-year-old with healed septal necrosis suffered a recurrent myocardial infarction of the anterior wall following the administration of isosorbide dinitrate 5 mg sublingually .

Example answer:
{"entities": [{"text": "necrosis", "type": "Disease"}, {"text": "myocardial infarction", "type": "Disease"}, {"text": "isosorbide dinitrate", "type": "Chemical"}]}

Example input:
Sentence: We report the case of a 63-year-old female who was treated with methylphenidate due to hyperactivity and suffered from multiple ischaemic strokes .

Example answer:
{"entities": [{"text": "methylphenidate", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "ischaemic strokes", "type": "Disease"}]}

Example input:
Sentence: Her medical history included coronary artery disease with previous myocardial infarctions , hypertension , and diabetes mellitus .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "myocardial infarctions", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "diabetes mellitus", "type": "Disease"}]}

Example input:
Sentence: Pneumonitis , bilateral pleural effusions , echocardiographic evidence of cardiac tamponade , and positive autoantibodies developed in a 43-year-old man , who was receiving long-term sulfasalazine therapy for chronic ulcerative colitis .

Example answer:
{"entities": [{"text": "Pneumonitis", "type": "Disease"}, {"text": "pleural effusions", "type": "Disease"}, {"text": "cardiac tamponade", "type": "Disease"}, {"text": "sulfasalazine", "type": "Chemical"}, {"text": "ulcerative colitis", "type": "Disease"}]}

Example input:
Sentence: In this report we describe the case of a 37-year-old white woman with Ebstein 's anomaly , who developed a rare syndrome called platypnea-orthodeoxia , characterized by massive right-to-left interatrial shunting with transient profound hypoxia and cyanosis .

Example answer:
{"entities": [{"text": "Ebstein 's anomaly", "type": "Disease"}, {"text": "platypnea-orthodeoxia", "type": "Disease"}, {"text": "hypoxia", "type": "Disease"}, {"text": "cyanosis", "type": "Disease"}]}

Input:
Sentence: The patient had no history of underlying ischaemic heart disease or Prinzmetal 's angina .

## Item bc5cdr:test:1690
Example input:
Sentence: In the pre-treatment evaluation , signs of cardiovascular disease were found in 33 patients ( 43 % ) .

Example answer:
{"entities": [{"text": "cardiovascular disease", "type": "Disease"}]}

Example input:
Sentence: The effects of continuous positive airway pressure ( CPAP ) on cardiovascular dynamics and pulmonary shunt ( QS/QT ) were investigated in 12 dogs before and during sodium nitroprusside infusion that decreased mean arterial blood pressure 40-50 per cent .

Example answer:
{"entities": [{"text": "sodium nitroprusside", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : There were more incidents of bradycardia in subjects treated with clonidine compared with those not treated with clonidine ( 17.5 % versus 3.4 % ; p =.02 ) , but no other significant group differences regarding electrocardiogram and other cardiovascular outcomes .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: Since the introduction of angiotensin converting enzyme ( ACE ) inhibitors into the adjunctive treatment of patients with congestive heart failure , cases of severe hypotension , especially on the first day of treatment , have occasionally been reported .

Example answer:
{"entities": [{"text": "angiotensin converting enzyme ( ACE ) inhibitors", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: The incidence of cardiotoxicity was not higher in patients with signs of cardiovascular disease than in those without in the pre-treatment evaluation .

Example answer:
{"entities": [{"text": "cardiotoxicity", "type": "Disease"}, {"text": "cardiovascular disease", "type": "Disease"}]}

Example input:
Sentence: Analysis was performed on 61 women with chemotherapy-responsive metastatic breast cancer receiving 96-h infusional cyclophosphamide as part of a triple sequential high-dose regimen to assess association between presence of peritransplant congestive heart failure ( CHF ) and the following pretreatment characteristics : presence of electrocardiogram ( EKG ) abnormalities , age , hypertension , prior cardiac history , smoking , diabetes mellitus , prior use of anthracyclines , and left-sided chest irradiation .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "CHF", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "diabetes mellitus", "type": "Disease"}, {"text": "anthracyclines", "type": "Chemical"}]}

Example input:
Sentence: Subjects were 1210 inpatients with New York Heart Association ( NYHA ) functional class II and III .

Example answer:
{"entities": []}

Example input:
Sentence: On the other hand , BNP did not increase in the patients without heart failure given DNR , even at more than 700 mg/m ( 2 ) .

Example answer:
{"entities": [{"text": "heart failure", "type": "Disease"}, {"text": "DNR", "type": "Chemical"}]}

Example input:
Sentence: During treatment , adverse cardiac effects were observed in 14 patients ( 18 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: We measured the plasma level of brain natriuretic peptide ( BNP ) to determine whether BNP might serve as a simple diagnostic indicator of anthracycline-induced cardiotoxicity in patients with acute leukemia treated with a daunorubicin ( DNR ) -containing regimen .

Example answer:
{"entities": [{"text": "anthracycline-induced", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}, {"text": "acute leukemia", "type": "Disease"}, {"text": "daunorubicin", "type": "Chemical"}, {"text": "DNR", "type": "Chemical"}]}

Input:
Sentence: CNA patients had higher heart rates during treatment , which may reflect severity of illness .

## Item bc5cdr:test:1691
Example input:
Sentence: A 72-year-old woman was admitted to the hospital with `` flash '' pulmonary edema , preceded by chest pain , requiring intubation .

Example answer:
{"entities": [{"text": "pulmonary edema", "type": "Disease"}, {"text": "chest pain", "type": "Disease"}]}

Example input:
Sentence: The patient had no apparent associated conditions which might have predisposed him to the development of bradyarrhythmias ; and , thus , this probably represented a true idiosyncrasy to lidocaine .

Example answer:
{"entities": [{"text": "bradyarrhythmias", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: In the singleton pregnancy , the mother had ulcerative colitis , and the infant , a male , had coarctation of the aorta and a ventricular septal defect .

Example answer:
{"entities": [{"text": "ulcerative colitis", "type": "Disease"}, {"text": "coarctation of the aorta", "type": "Disease"}, {"text": "ventricular septal defect", "type": "Disease"}]}

Example input:
Sentence: During the first day of hospitalization ( while intubated ) , intravenous metoprolol was given , resulting in severe angioedema .

Example answer:
{"entities": [{"text": "metoprolol", "type": "Chemical"}, {"text": "angioedema", "type": "Disease"}]}

Example input:
Sentence: There was also a higher incidence of tachyarrhythmias ( P less than 0.05 ) and ventricular ectopic beats ( P less than 0.05 ) in the morphine infusion group .

Example answer:
{"entities": [{"text": "tachyarrhythmias", "type": "Disease"}, {"text": "ventricular ectopic beats", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: The incidence of postoperative respiratory apnoea was compared between five patients receiving a continuous i.v .

Example answer:
{"entities": [{"text": "apnoea", "type": "Disease"}]}

Example input:
Sentence: Mild hypoxia ( SO2 < 90 % ) was the most common event ( 11 patients ) ; 3 patients ( 2 % ) presented transient hypoxia due to upper airway obstruction by probe introduction and 8 ( 5.8 % ) due to hypoxia caused by MZ use .

Example answer:
{"entities": [{"text": "hypoxia", "type": "Disease"}, {"text": "airway obstruction", "type": "Disease"}, {"text": "MZ", "type": "Chemical"}]}

Example input:
Sentence: The incidence of cardiotoxicity was not higher in patients with signs of cardiovascular disease than in those without in the pre-treatment evaluation .

Example answer:
{"entities": [{"text": "cardiotoxicity", "type": "Disease"}, {"text": "cardiovascular disease", "type": "Disease"}]}

Example input:
Sentence: Five days after the onset of the symptoms of meningitis , the patient aspirated stomach contents and needed endotracheal intubation .

Example answer:
{"entities": [{"text": "meningitis", "type": "Disease"}]}

Example input:
Sentence: The incidence of coronary events was similar in both groups .

Example answer:
{"entities": []}

Input:
Sentence: The incidence of intubation was similar .

## Item bc5cdr:test:1106
Example input:
Sentence: Galanthamine hydrobromide , an anticholinesterase drug capable of penetrating the blood-brain barrier , was used in a patient demonstrating central effects of scopolamine ( hyoscine ) overdosage .

Example answer:
{"entities": [{"text": "Galanthamine hydrobromide", "type": "Chemical"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "hyoscine", "type": "Chemical"}, {"text": "overdosage", "type": "Disease"}]}

Example input:
Sentence: Galanthamine hydrobromide , a longer acting anticholinesterase drug , in the treatment of the central effects of scopolamine ( Hyoscine ) .

Example answer:
{"entities": [{"text": "Galanthamine hydrobromide", "type": "Chemical"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "Hyoscine", "type": "Chemical"}]}

Example input:
Sentence: While she was weak , 2-Hz repetitive stimulation revealed a decrement without significant facilitation at rapid rates or after exercise , suggesting postsynaptic neuromuscular blockade .

Example answer:
{"entities": [{"text": "postsynaptic neuromuscular blockade", "type": "Disease"}]}

Example input:
Sentence: As a consequence of blocking I ( f ) , clonidine reduced the slope of the diastolic depolarization and the frequency of pacemaker potentials in sinoatrial node cells from wild-type and alpha2ABC-knockout mice .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: Such organophosphorus ( OP ) compounds as diisopropylfluorophosphate ( DFP ) , sarin and soman are potent inhibitors of acetylcholinesterases ( AChEs ) and butyrylcholinesterases ( BChEs ) .

Example answer:
{"entities": [{"text": "organophosphorus", "type": "Chemical"}, {"text": "OP", "type": "Chemical"}, {"text": "diisopropylfluorophosphate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}, {"text": "sarin", "type": "Chemical"}, {"text": "soman", "type": "Chemical"}]}

Example input:
Sentence: Reports of persistent paralysis after the discontinuance of these drugs have most often involved aminosteroid-based NMBAs such as vecuronium bromide , especially when used in conjunction with corticosteroids .

Example answer:
{"entities": [{"text": "paralysis", "type": "Disease"}, {"text": "vecuronium bromide", "type": "Chemical"}]}

Example input:
Sentence: The extent of inhibition of brain cholinesterase activity evoked by DCE at the dose of 400 mg/kg was 22 % in young and 19 % in aged mice .

Example answer:
{"entities": [{"text": "DCE", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : eleven of 13 patients with a prolonged duration of action of succinylcholine had mutations in BCHE , indicating that this is the possible reason for a prolonged period of apnea .

Example answer:
{"entities": [{"text": "succinylcholine", "type": "Chemical"}, {"text": "apnea", "type": "Disease"}]}

Example input:
Sentence: Butyrylcholinesterase gene mutations in patients with prolonged apnea after succinylcholine for electroconvulsive therapy .

Example answer:
{"entities": [{"text": "apnea", "type": "Disease"}, {"text": "succinylcholine", "type": "Chemical"}]}

Example input:
Sentence: Suxamethonium causes prolonged apnea in patients in whom pseudocholinesterase enzyme gets deactivated by organophosphorus ( OP ) poisons .

Example answer:
{"entities": [{"text": "Suxamethonium", "type": "Chemical"}, {"text": "apnea", "type": "Disease"}, {"text": "organophosphorus ( OP ) poisons", "type": "Chemical"}]}

Input:
Sentence: It is concluded that anticholinesterases are only partially effective in restoring neuromuscular function in succinylcholine apnoea despite muscle twitch activity typical of phase II block .

## Item bc5cdr:test:1396
Example input:
Sentence: The pooled statistical analysis for ventricular septal ( VSD ) and midline ( MD ) defects was performed for rat fetuses exposed to piroxicam , selective and non-selective COX-2 inhibitor based on present and historic data .

Example answer:
{"entities": [{"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: The aim of the experiment was to evaluate the developmental toxicity of the non-selective ( piroxicam ) and selective ( DFU ; 5,5-dimethyl-3- ( 3-fluorophenyl ) -4- ( 4-methylsulphonyl ) phenyl-2 ( 5H ) -furanon ) COX-2 inhibitors .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "piroxicam", "type": "Chemical"}, {"text": "DFU", "type": "Chemical"}, {"text": "5,5-dimethyl-3- ( 3-fluorophenyl ) -4- ( 4-methylsulphonyl ) phenyl-2 ( 5H ) -furanon", "type": "Chemical"}]}

Example input:
Sentence: Haematological adverse reactions associated with fatal outcome are rare during treatment with ciprofloxacin .

Example answer:
{"entities": [{"text": "ciprofloxacin", "type": "Chemical"}]}

Example input:
Sentence: Lack of teratogenicity was found in piroxicam and DFU-exposed groups .

Example answer:
{"entities": [{"text": "piroxicam", "type": "Chemical"}, {"text": "DFU-exposed", "type": "Chemical"}]}

Example input:
Sentence: A warfarin-drug interaction could have contributed to the haemorrhage in 24 ( 41 % ) of the warfarin patients and in 7 of these ( 12 % ) the bleeding complication was considered being possible to avoid .

Example answer:
{"entities": [{"text": "warfarin-drug", "type": "Chemical"}, {"text": "haemorrhage", "type": "Disease"}, {"text": "warfarin", "type": "Chemical"}, {"text": "bleeding", "type": "Disease"}]}

Example input:
Sentence: This case report shows that ciprofloxacin may precipitate life-threatening thrombocytopenia and haemolytic anaemia , even in the early phases of treatment and without apparent previous exposures .

Example answer:
{"entities": [{"text": "ciprofloxacin", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "haemolytic anaemia", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Correlation of plasma argatroban concentration versus the patient 's coagulation variables and clinical course suggest that prolonged elevated levels of plasma argatroban may have contributed to the patient 's extended coagulopathy .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "coagulopathy", "type": "Disease"}]}

Example input:
Sentence: RESULTS : During a mean follow-up of 3.3 years , raloxifene was associated with an increased risk for venous thromboembolism ( relative risk [ RR ] 2.1 ; 95 % confidence interval [ CI ] 1.2-3.8 ) .

Example answer:
{"entities": [{"text": "raloxifene", "type": "Chemical"}, {"text": "venous thromboembolism", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : Raloxifene was associated with an increased risk for venous thromboembolism , but there was no increased risk for cataracts , gallbladder disease , endometrial hyperplasia , or endometrial cancer .

Example answer:
{"entities": [{"text": "Raloxifene", "type": "Chemical"}, {"text": "venous thromboembolism", "type": "Disease"}, {"text": "cataracts", "type": "Disease"}, {"text": "gallbladder disease", "type": "Disease"}, {"text": "endometrial hyperplasia", "type": "Disease"}, {"text": "endometrial cancer", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Maternal toxicity , intrauterine growth retardation , and increase of external and skeletal variations were found in rats treated with the highest dose of piroxicam .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "intrauterine growth retardation", "type": "Disease"}, {"text": "increase of external and skeletal variations", "type": "Disease"}, {"text": "piroxicam", "type": "Chemical"}]}

Input:
Sentence: An adverse drug interaction with piroxicam , which she took occasionally , may have exacerbated the coagulopathy .

## Item bc5cdr:test:1713
Example input:
Sentence: PEG 400 impressively decreased both acute high-dose and chronic low-dose-ADR-associated lethality .

Example answer:
{"entities": [{"text": "PEG 400", "type": "Chemical"}]}

Example input:
Sentence: The median dose-intensity ( DI ) was 20 mg/m2/wk .

Example answer:
{"entities": []}

Example input:
Sentence: With mild toxicity , a reduction to 30 or 40 mg/kg per dose should result in a reversal of the abnormal results to normal within four weeks .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: The protective effect of LY274614 was dose-dependent , being maximum at 10-40 mgkg ( i.p . ) .

Example answer:
{"entities": [{"text": "LY274614", "type": "Chemical"}]}

Example input:
Sentence: Response rates according to three sets of criteria were greater with the standard dose ( 55 % -60 % ) than the low dose ( 25 % -35 % ) and placebo ( 25 % -30 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Severe toxicity was correlated with the higher cumulative dose of 60 g/m2 of ifosfamide , a younger age ( less than 2 1/2 years old ) , and a predominance of vesicoprostatic tumor involvement .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "tumor", "type": "Disease"}]}

Example input:
Sentence: All patients were on a regular transfusion-chelation program maintaining a mean hemoglobin level of 9.5 gr/dl .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : The mean hemoglobin ( Hb ) levels were significantly declined in all patients from baseline of 14.2 g/dl to 14.0 g/dl , 13.5 g/dl , 13.2 g/dl and 12.7 g/dl at 1 , 2 , 3 and 6 months post-CAB , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: After 154 courses of therapy , the median dose intensity was 131 mg/m ( 2 ) for paclitaxel ( 97.3 % ) , 117 mg/m ( 2 ) for cisplatin ( 97.3 % ) , and 1378 mg/m ( 2 ) for gemcitabine ( 86.2 % ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}]}

Example input:
Sentence: Maximum tolerated dose in good-risk patients was 70 mg/m2 , and in poor-risk patients , 60 mg/m2 .

Example answer:
{"entities": []}

Input:
Sentence: Maximum blood loss was greatest at the upper and lower dose levels , and lowest in the 70-125 microg dose range .

## Item bc5cdr:test:1714
Example input:
Sentence: These 13 included cases of malignant hypertension , thrombotic microangiopathy , lupus nephritis , Henoch-Schonlein nephritis , crescentic glomerulonephritis , and cocaine-related acute renal failure .

Example answer:
{"entities": [{"text": "malignant hypertension", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "lupus nephritis", "type": "Disease"}, {"text": "Henoch-Schonlein nephritis", "type": "Disease"}, {"text": "glomerulonephritis", "type": "Disease"}, {"text": "cocaine-related", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: All patients were on a regular transfusion-chelation program maintaining a mean hemoglobin level of 9.5 gr/dl .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : The mean hemoglobin ( Hb ) levels were significantly declined in all patients from baseline of 14.2 g/dl to 14.0 g/dl , 13.5 g/dl , 13.2 g/dl and 12.7 g/dl at 1 , 2 , 3 and 6 months post-CAB , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: Severe and clinically evident anemia of Hb < 11 g/dl with clinical symptoms was detected in 6 patients ( 14.3 % ) .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: Transient hypotension ( SAP < 90mmHg ) occurred in 1 patient ( 0.7 % ) .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: These 6 patients had both renal and liver dysfunction ( P less than 0.05 ) , as well as cimetidine trough-concentrations of more than 1.25 microgram/ml ( P less than 0.05 ) .

Example answer:
{"entities": [{"text": "cimetidine", "type": "Chemical"}]}

Example input:
Sentence: Cases were patients who developed hyperkalemia ( K ( + ) > 5.0 mEq/L ) or renal insufficiency ( Cr > or=2.5 mg/dL ) , and they were compared to 2 randomly selected controls per case .

Example answer:
{"entities": [{"text": "hyperkalemia", "type": "Disease"}, {"text": "K", "type": "Chemical"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "Cr", "type": "Chemical"}]}

Example input:
Sentence: Two subsets of patients were identified from this latter group : the first included four patients ( 5 % of the total population ) who developed major toxicity resulting in Fanconi 's syndrome ( TDFS ) ; and the second group included five patients with elevated beta 2 microglobulinuria and low phosphate reabsorption .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "Fanconi 's syndrome", "type": "Disease"}, {"text": "TDFS", "type": "Disease"}, {"text": "phosphate", "type": "Chemical"}]}

Example input:
Sentence: Severe hematologic toxicity ( neutrophil count < 1000/mm3 and/or hemoglobin < 8 g/dl ) occurred in 4 patients assigned to group I and 7 assigned to group II .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Input:
Sentence: Four out of six cases with blood loss > or = 1000 ml occurred in the 200 microg group .

## Item bc5cdr:test:1240
Example input:
Sentence: We describe 4 patients in whom hyperkalemia ranging from 6.1 to 6.9 mEq/l developed within 3 to 8 days of sulindac administration .

Example answer:
{"entities": [{"text": "hyperkalemia", "type": "Disease"}, {"text": "sulindac", "type": "Chemical"}]}

Example input:
Sentence: Prompt restoration of renal function followed drug withdrawal , while re-exposure to a single dose of indomethacin caused recurrence of acute reversible oliguria .

Example answer:
{"entities": [{"text": "indomethacin", "type": "Chemical"}, {"text": "oliguria", "type": "Disease"}]}

Example input:
Sentence: Hyperkalemia associated with sulindac therapy .

Example answer:
{"entities": [{"text": "Hyperkalemia", "type": "Disease"}, {"text": "sulindac", "type": "Chemical"}]}

Example input:
Sentence: We therefore sought to determine the prevalence and clinical associations of hyperkalemia and renal insufficiency in heart failure patients treated with spironolactone .

Example answer:
{"entities": [{"text": "hyperkalemia", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}, {"text": "spironolactone", "type": "Chemical"}]}

Example input:
Sentence: Spironolactone-induced renal insufficiency and hyperkalemia in patients with heart failure .

Example answer:
{"entities": [{"text": "Spironolactone-induced", "type": "Chemical"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}]}

Example input:
Sentence: Indomethacin-induced renal insufficiency : recurrence on rechallenge .

Example answer:
{"entities": [{"text": "Indomethacin-induced", "type": "Chemical"}, {"text": "renal insufficiency", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Spironolactone-induced hyperkalemia and renal insufficiency are more common in our clinical experience than reported previously .

Example answer:
{"entities": [{"text": "Spironolactone-induced", "type": "Chemical"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}]}

Example input:
Sentence: The present report describes a case of cardiac arrest and subsequent death as a result of hyperkalaemia following the use of suxamethonium in a 23-year-old Malawian woman .

Example answer:
{"entities": [{"text": "cardiac arrest", "type": "Disease"}, {"text": "death", "type": "Disease"}, {"text": "hyperkalaemia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: Hyperkalemia has recently been recognized as a complication of nonsteroidal antiinflammatory agents ( NSAID ) such as indomethacin .

Example answer:
{"entities": [{"text": "Hyperkalemia", "type": "Disease"}, {"text": "indomethacin", "type": "Chemical"}]}

Example input:
Sentence: We have reported a case of acute oliguric renal failure with hyperkalemia in a patient with cirrhosis , ascites , and cor pulmonale after indomethacin therapy .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "cor pulmonale", "type": "Disease"}, {"text": "indomethacin", "type": "Chemical"}]}

Input:
Sentence: Indomethacin-induced hyperkalemia in three patients with gouty arthritis .

## Item bc5cdr:test:1400
Example input:
Sentence: As a result , switching to tacrolimus has been reported to be a viable therapeutic option in the setting of cyclosporine-induced TMA .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "cyclosporine-induced", "type": "Chemical"}, {"text": "TMA", "type": "Disease"}]}

Example input:
Sentence: We report a case of a living donor renal transplant recipient who developed cyclosporine-induced TMA that responded to the withdrawal of cyclosporine in conjunction with plasmapheresis and fresh frozen plasma replacement therapy .

Example answer:
{"entities": [{"text": "cyclosporine-induced", "type": "Chemical"}, {"text": "TMA", "type": "Disease"}, {"text": "cyclosporine", "type": "Chemical"}]}

Example input:
Sentence: Treatments have included discontinuation or reduction of cyclosporine dose with or without concurrent plasma exchange , plasma infusion , anticoagulation , and intravenous immunoglobulin G infusion .

Example answer:
{"entities": [{"text": "cyclosporine", "type": "Chemical"}]}

Example input:
Sentence: The aim of this study was to examine further the renal function , including morphological analysis of the kidneys of male Sprague-Dawley rats treated with either cyclosporine A ( CsA ) , tacrolimus ( FK506 ) or SRL as monotherapies or in different combinations .

Example answer:
{"entities": [{"text": "cyclosporine A", "type": "Chemical"}, {"text": "CsA", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Example input:
Sentence: The reduction of cyclosporine- or tacrolimus trough levels and the administration of calcium channel blockers led to relief of pain .

Example answer:
{"entities": [{"text": "cyclosporine-", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: In this study , long-term cardiac transplant patients were switched from cyclosporine to Srl-based IS .

Example answer:
{"entities": [{"text": "cyclosporine", "type": "Chemical"}, {"text": "Srl-based", "type": "Chemical"}]}

Example input:
Sentence: The drugs commonly used are cyclophosphamide and chlorambucil ( alkylating agents ) , azathioprine ( purine analogue ) , and methotrexate ( folic acid analogue ) .

Example answer:
{"entities": [{"text": "cyclophosphamide", "type": "Chemical"}, {"text": "chlorambucil", "type": "Chemical"}, {"text": "alkylating agents", "type": "Chemical"}, {"text": "azathioprine", "type": "Chemical"}, {"text": "purine", "type": "Chemical"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "folic acid", "type": "Chemical"}]}

Example input:
Sentence: There have been several long-term studies of patients with rheumatoid arthritis treated with azathioprine and cyclophosphamide and the incidence of most of the common cancers is not increased .

Example answer:
{"entities": [{"text": "rheumatoid arthritis", "type": "Disease"}, {"text": "azathioprine", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "cancers", "type": "Disease"}]}

Example input:
Sentence: Azathioprine treatment benefited 19 ( 66 % ) out of 29 patients suffering from severe psoriasis .

Example answer:
{"entities": [{"text": "Azathioprine", "type": "Chemical"}, {"text": "psoriasis", "type": "Disease"}]}

Input:
Sentence: Patients were managed with cyclosporine and azathioprine .

## Item bc5cdr:test:1253
Example input:
Sentence: Monkeys with acute ( short-term ) MPTP exposure , rapid symptom onset and short symptom duration prior to initiation of levodopa therapy developed dyskinesia between 11 and 24 days of daily levodopa administration .

Example answer:
{"entities": [{"text": "MPTP", "type": "Chemical"}, {"text": "levodopa", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Recent preclinical and clinical data from promising lines of research focus on the differential role of presynaptic versus postsynaptic mechanisms , dopamine receptor subtypes , ionotropic and metabotropic glutamate receptors , and non-dopaminergic neurotransmitter systems in the pathophysiology of levodopa-induced dyskinesias .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: Repetitive transcranial magnetic stimulation for levodopa-induced dyskinesias in Parkinson 's disease .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: This study suggests that administration of low doses of beta-blockers may improve levodopa-induced ballistic and choreic dyskinesia in PD .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: Although preclinical and clinical findings suggest pulsatile stimulation of striatal postsynaptic receptors as a key mechanism underlying levodopa-induced dyskinesias , their pathogenesis is still unclear .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: Levodopa-induced dyskinesias ( LIDs ) present a major problem for the long-term management of Parkinson 's disease ( PD ) patients .

Example answer:
{"entities": [{"text": "Levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "LIDs", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: Increase of Parkinson disability after fluoxetine medication .

Example answer:
{"entities": [{"text": "Parkinson disability", "type": "Disease"}, {"text": "fluoxetine", "type": "Chemical"}]}

Example input:
Sentence: Levodopa-induced dyskinesias in patients with Parkinson 's disease : filling the bench-to-bedside gap .

Example answer:
{"entities": [{"text": "Levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: Improvement of levodopa-induced dyskinesia by propranolol in Parkinson 's disease .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "propranolol", "type": "Chemical"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: We report the increased amount of motor disability in four patients with idiopathic Parkinson 's disease after exposure to the antidepressant fluoxetine .

Example answer:
{"entities": [{"text": "motor disability", "type": "Disease"}, {"text": "idiopathic Parkinson 's disease", "type": "Disease"}, {"text": "antidepressant", "type": "Chemical"}, {"text": "fluoxetine", "type": "Chemical"}]}

Input:
Sentence: Levodopa-induced dyskinesias are improved by fluoxetine .

## Item bc5cdr:test:1411
Example input:
Sentence: A 61-year-old man was treated with combination chemotherapy incorporating cisplatinum , etoposide , high-dose 5-fluorouracil ( 2,250 mg/m2/24 hours ) and folinic acid for an inoperable gastric adenocarcinoma .

Example answer:
{"entities": [{"text": "cisplatinum", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}, {"text": "gastric adenocarcinoma", "type": "Disease"}]}

Example input:
Sentence: A Phase I study of intravenous ( IV ) bolus 4'-0-tetrahydropyranyladriamycin ( Pirarubicin ) was done in 55 patients in good performance status with refractory tumors .

Example answer:
{"entities": [{"text": "4'-0-tetrahydropyranyladriamycin", "type": "Chemical"}, {"text": "Pirarubicin", "type": "Chemical"}, {"text": "tumors", "type": "Disease"}]}

Example input:
Sentence: The patient cohort ( 14 men , 11 women ) was treated with SRL as conversion therapy , due to chronic allograft nephropathy ( CAN ) ( n = 15 ) neoplasia ( n = 8 ) ; Kaposi 's sarcoma , Four skin cancers , One intestinal tumors , One renal cell carsinom ) or BK virus nephropathy ( n = 2 ) .

Example answer:
{"entities": [{"text": "SRL", "type": "Chemical"}, {"text": "chronic allograft nephropathy", "type": "Disease"}, {"text": "CAN", "type": "Disease"}, {"text": "neoplasia", "type": "Disease"}, {"text": "Kaposi 's sarcoma", "type": "Disease"}, {"text": "skin cancers", "type": "Disease"}, {"text": "intestinal tumors", "type": "Disease"}, {"text": "renal cell carsinom", "type": "Disease"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: METHODS : a total of 13 patients were referred to the Danish Cholinesterase Research Unit after ECT during 38 months .

Example answer:
{"entities": []}

Example input:
Sentence: Further studies are needed to determine the most appropriate nucleoside or nucleotide analogue for antiviral prophylaxis during CT and the optimal duration of administration after completion of CT .

Example answer:
{"entities": [{"text": "nucleoside", "type": "Chemical"}, {"text": "nucleotide", "type": "Chemical"}]}

Example input:
Sentence: Pneumocystis pneumonia ( PCP ) , a common opportunistic infection in HIV-infected individuals , is generally treated with high doses of co-trimoxazole .

Example answer:
{"entities": [{"text": "Pneumocystis pneumonia", "type": "Disease"}, {"text": "PCP", "type": "Disease"}, {"text": "opportunistic infection", "type": "Disease"}, {"text": "HIV-infected", "type": "Disease"}, {"text": "co-trimoxazole", "type": "Chemical"}]}

Example input:
Sentence: In this study , cancer patients who have solid and hematological malignancies with chronic HBV infection received the antiviral agent lamivudine prior and during CT compared with historical control group who did not receive lamivudine .

Example answer:
{"entities": [{"text": "cancer", "type": "Disease"}, {"text": "hematological malignancies", "type": "Disease"}, {"text": "HBV infection", "type": "Disease"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: From June 2004 to October 2006 , 11 HBs Ag positive patients with rheumatologic diseases , who were on both immunosuppressive and prophylactic lamivudine therapies , were retrospectively assessed .

Example answer:
{"entities": [{"text": "HBs Ag", "type": "Chemical"}, {"text": "rheumatologic diseases", "type": "Disease"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: Azathioprine treatment benefited 19 ( 66 % ) out of 29 patients suffering from severe psoriasis .

Example answer:
{"entities": [{"text": "Azathioprine", "type": "Chemical"}, {"text": "psoriasis", "type": "Disease"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Input:
Sentence: Cytomegalovirus infections were treated successfully with ganciclovir in 11 patients .

## Item bc5cdr:test:1369
Example input:
Sentence: We propose that amphotericin , in the setting of reduced effective arterial volume , may activate tubuloglomerular feedback , thereby contributing to acute renal failure .

Example answer:
{"entities": [{"text": "amphotericin", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: In the five rats that developed somatic rigidity , ICP and CVP increased significantly above baseline ( delta ICP 7.5 +/- 1.0 mmHg , delta CVP 5.9 +/- 1.3 mmHg ) .

Example answer:
{"entities": [{"text": "somatic rigidity", "type": "Disease"}]}

Example input:
Sentence: Despite inducing extensive erythrocyte lysis , TAM does not shift the osmotic fragility curves of erythrocytes .

Example answer:
{"entities": [{"text": "TAM", "type": "Chemical"}]}

Example input:
Sentence: Two patients developed acute tubular necrosis , characterized clinically by acute oliguric renal failure , while they were receiving a combination of cephalothin sodium and gentamicin sulfate therapy .

Example answer:
{"entities": [{"text": "acute tubular necrosis", "type": "Disease"}, {"text": "cephalothin sodium", "type": "Chemical"}, {"text": "gentamicin sulfate", "type": "Chemical"}]}

Example input:
Sentence: We suggest that our patient 's tubular dysfunction and myopathy may have resulted from mitochondrial dysfunction which is triggered by tacrolimus and augmented by lamivudine .

Example answer:
{"entities": [{"text": "tubular dysfunction", "type": "Disease"}, {"text": "myopathy", "type": "Disease"}, {"text": "mitochondrial dysfunction", "type": "Disease"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: Histopathological examination of kidney , heart and lung sections revealed moderate to massive tissue damage with a variety of morphological aberrations by all the three drugs in the absence of GSPE preexposure than in its presence .

Example answer:
{"entities": [{"text": "tissue damage", "type": "Disease"}, {"text": "GSPE", "type": "Chemical"}]}

Example input:
Sentence: The fractional reabsorption of tubular fluid by the proximal tubules is reduced , leaving the distal delivery unchanged .

Example answer:
{"entities": []}

Example input:
Sentence: The pooled statistical analysis for ventricular septal ( VSD ) and midline ( MD ) defects was performed for rat fetuses exposed to piroxicam , selective and non-selective COX-2 inhibitor based on present and historic data .

Example answer:
{"entities": [{"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: All rats in the sodium-depleted group had histopathological evidence of patchy tubular cytoplasmic degeneration in tubules that was not observed in any normal-salt or salt-loaded rat .

Example answer:
{"entities": [{"text": "sodium-depleted", "type": "Chemical"}]}

Example input:
Sentence: GSPE+drug exposed tissues exhibited minor residual damage or near total recovery .

Example answer:
{"entities": [{"text": "GSPE+drug", "type": "Chemical"}]}

Input:
Sentence: SOD did not attenuate the tubular damage .

## Item bc5cdr:test:1613
Example input:
Sentence: In high doses , its nonhematological dose-limiting toxicity is cardiomyopathy .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: Neurologic toxicity was reported in 52 % of patients .

Example answer:
{"entities": [{"text": "Neurologic toxicity", "type": "Disease"}]}

Example input:
Sentence: World Health Organization Grade 3-4 neutropenia and thrombocytopenia occurred in 39.9 % and 11.4 % of patients , respectively .

Example answer:
{"entities": [{"text": "neutropenia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}]}

Example input:
Sentence: Of 20 patients evaluable for toxicity , four had stage III and 16 had stage IV disease .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Grade 3-4 adverse effects included myelosuppression , fatigue , somnolence/depressed mood , neuropathy and dyspnea .

Example answer:
{"entities": [{"text": "myelosuppression", "type": "Disease"}, {"text": "fatigue", "type": "Disease"}, {"text": "somnolence/depressed mood", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}, {"text": "dyspnea", "type": "Disease"}]}

Example input:
Sentence: Six patients ( 12 % ) had World Health Organization Grade 3-4 neutropenia , 2 patients ( 4 % ) had Grade 3-4 thrombocytopenia , and 2 patients ( 4 % ) had Grade 3 neurotoxicity .

Example answer:
{"entities": [{"text": "neutropenia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Severe hematologic toxicity ( neutrophil count < 1000/mm3 and/or hemoglobin < 8 g/dl ) occurred in 4 patients assigned to group I and 7 assigned to group II .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: A grade 2 or 3 infection occurred in 16 % of patients , but no toxic deaths occurred .

Example answer:
{"entities": [{"text": "infection", "type": "Disease"}, {"text": "deaths", "type": "Disease"}]}

Example input:
Sentence: VNB was well tolerated and zero instances of WHO grade 4 nonhematologic toxicity occurred .

Example answer:
{"entities": [{"text": "VNB", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Nonhematologic toxicities were mild .

Example answer:
{"entities": [{"text": "toxicities", "type": "Disease"}]}

Input:
Sentence: Grade 3/4 nonhematologic toxicities were uncommon .

## Item bc5cdr:test:1470
Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: The effects of continuous positive airway pressure ( CPAP ) on cardiovascular dynamics and pulmonary shunt ( QS/QT ) were investigated in 12 dogs before and during sodium nitroprusside infusion that decreased mean arterial blood pressure 40-50 per cent .

Example answer:
{"entities": [{"text": "sodium nitroprusside", "type": "Chemical"}]}

Example input:
Sentence: Patients given prilocaine were more likely to develop hearing loss ( 10 out of 22 ) than those given bupivacaine ( 4 out of 22 ) ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "prilocaine", "type": "Chemical"}, {"text": "hearing loss", "type": "Disease"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Epinephrine has a proven role in cardiac arrest in prehospital care ; however , use by paramedics in patients with suspected allergic reaction and severe hypertension should be viewed with caution .

Example answer:
{"entities": [{"text": "Epinephrine", "type": "Chemical"}, {"text": "cardiac arrest", "type": "Disease"}, {"text": "allergic reaction", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: None of the animals that received bupivacaine , normal saline , or normal saline titrated to a pH 3.0 developed hind-limb paralysis .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}, {"text": "paralysis", "type": "Disease"}]}

Example input:
Sentence: The convulsant activity of bupivacaine was not significantly modified but calcium channel blockers decreased the time of latency to obtain bupivacaine-induced convulsions ; this effect was less pronounced with bepridil .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "bupivacaine-induced", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "bepridil", "type": "Chemical"}]}

Example input:
Sentence: Phenylephrine but not ephedrine reduces frontal lobe oxygenation following anesthesia-induced hypotension .

Example answer:
{"entities": [{"text": "Phenylephrine", "type": "Chemical"}, {"text": "ephedrine", "type": "Chemical"}, {"text": "reduces frontal lobe oxygenation", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : The utilization of phenylephrine to correct hypotension induced by anesthesia has a negative impact on S ( c ) O ( 2 ) while ephedrine maintains frontal lobe oxygenation potentially related to an increase in CO .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Input:
Sentence: Epinephrine shortened QT less after bupivacaine than in control animals .

## Item bc5cdr:test:1365
Example input:
Sentence: Male Wistar rats were challenged intragastrically once daily for 9 days with 1.0 ml/kg of corn oil containing vitamin D2 and cholesterol to induce atherosclerosis .

Example answer:
{"entities": [{"text": "vitamin D2", "type": "Chemical"}, {"text": "cholesterol", "type": "Chemical"}, {"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/", "type": "Chemical"}, {"text": "K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}]}

Example input:
Sentence: Untreated group 3 rats exhibited a progressive reduction in GFR ( 0.35 +/- 0.08 ml/min at 4 months , 0.27 +/- 0.07 ml/min at 6 months ) .

Example answer:
{"entities": []}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: HS diet for 4 wk caused a progressive increase in BP , protein and albumin excretion , and glomerular sclerosis in male DS rats , which were attenuated by castration .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: METHODS : For a period of 2 weeks , CsA 15 mg/kg/day ( given orally ) , FK506 3.0 mg/kg/day ( given orally ) or SRL 0.4 mg/kg/day ( given intraperitoneally ) was administered once a day as these doses have earlier been found to achieve a significant immunosuppressive effect in Sprague-Dawley rats .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: In the present work we assessed the effect of treatment of rats with gum Arabic on acute renal failure induced by gentamicin ( GM ) nephrotoxicity .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}]}

Example input:
Sentence: Rats were treated with the vehicle ( 2 mL/kg of distilled water and 5 % w/v cellulose , 10 days ) , gum Arabic ( 2 mL/kg of a 10 % w/v aqueous suspension of gum Arabic powder , orally for 10 days ) , or gum Arabic concomitantly with GM ( 80mg/kg/day intramuscularly , during the last six days of the treatment period ) .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}]}

Example input:
Sentence: The results indicated that concomitant treatment with gum Arabic and GM significantly increased creatinine and urea by about 183 and 239 % , respectively ( compared to 432 and 346 % , respectively , in rats treated with cellulose and GM ) , and decreased that of cortical GSH by 21 % ( compared to 27 % in the cellulose plus GM group ) The GM-induced proximal tubular necrosis appeared to be slightly less severe in rats given GM together with gum Arabic than in those given GM and cellulose .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}, {"text": "urea", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "GM-induced", "type": "Chemical"}, {"text": "tubular necrosis", "type": "Disease"}]}

Input:
Sentence: Administration of GM at 40 mg/kg sc for 13 days to rats induced a significant reduction in renal blood flow ( RBF ) and inulin clearance ( CIn ) as well as marked tubular damage .

## Item bc5cdr:test:1625
Example input:
Sentence: The primary response variable was based on central reading of 24 hour ambulatory electrocardiographic recordings and was defined as the occurrence of 30 or more single premature ventricular complexes in any two consecutive 30 minute blocks or one or more runs of two or more premature ventricular complexes in the entire 24 hour electrocardiographic recording .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Compared to controls , aortic regurgitation ( OR : 3.1 ; 95 % IC : 1.1-8.8 ) and mitral regurgitation ( OR : 10.7 ; 95 % IC : 2.1-53 ) were more frequent in PD patients ( tricuspid : NS ) .

Example answer:
{"entities": [{"text": "aortic regurgitation", "type": "Disease"}, {"text": "mitral regurgitation", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: Four compounds known to increase QT interval and cause TDP were investigated : terfenadine , terodiline , cisapride and E4031 .

Example answer:
{"entities": [{"text": "TDP", "type": "Disease"}, {"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}, {"text": "E4031", "type": "Chemical"}]}

Example input:
Sentence: These data indicate that the free ED50 in plasma for terfenadine ( 1.9 nM ) , terodiline ( 76 nM ) , cisapride ( 11 nM ) and E4031 ( 1.9 nM ) closely correlate with the free concentration in man causing QT effects .

Example answer:
{"entities": [{"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}, {"text": "E4031", "type": "Chemical"}]}

Example input:
Sentence: Sublingual UM-272 converted ventricular tachycardia to sinus rhythm in all 5 dogs .

Example answer:
{"entities": [{"text": "UM-272", "type": "Chemical"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: These patients had Q-T prolongation and recurrent syncope due to polymorphous ventricular tachycardia .

Example answer:
{"entities": [{"text": "Q-T prolongation", "type": "Disease"}, {"text": "syncope", "type": "Disease"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: His bundle recordings showed an atrial tachycardia with intermittent exit block and greatly prolonged BH and HV intervals ( 40 and 100 msec , respectively ) .

Example answer:
{"entities": [{"text": "atrial tachycardia", "type": "Disease"}]}

Example input:
Sentence: We report a woman with coronary artery disease who developed a markedly prolonged QT interval and torsades de pointes ( TdP ) after taking ketoconazole for treatment of fungal infection .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "prolonged QT interval", "type": "Disease"}, {"text": "torsades de pointes", "type": "Disease"}, {"text": "TdP", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "fungal infection", "type": "Disease"}]}

Example input:
Sentence: Ketoconazole induced torsades de pointes without concomitant use of QT interval-prolonging drug .

Example answer:
{"entities": [{"text": "Ketoconazole", "type": "Chemical"}, {"text": "torsades de pointes", "type": "Disease"}]}

Example input:
Sentence: Torsades de pointes ( TDP ) is a potentially fatal ventricular tachycardia associated with increases in QT interval and monophasic action potential duration ( MAPD ) .

Example answer:
{"entities": [{"text": "Torsades de pointes", "type": "Disease"}, {"text": "TDP", "type": "Disease"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Input:
Sentence: Neither ECG [ sinus-cycle length ( SCL ) , QT or QTc interval , or U wave ] nor clinical parameters identified patients at risk for torsades de pointes .

## Item bc5cdr:test:1341
Example input:
Sentence: We report a woman with coronary artery disease who developed a markedly prolonged QT interval and torsades de pointes ( TdP ) after taking ketoconazole for treatment of fungal infection .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "prolonged QT interval", "type": "Disease"}, {"text": "torsades de pointes", "type": "Disease"}, {"text": "TdP", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "fungal infection", "type": "Disease"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Myocardial infarction following sublingual administration of isosorbide dinitrate .

Example answer:
{"entities": [{"text": "Myocardial infarction", "type": "Disease"}, {"text": "isosorbide dinitrate", "type": "Chemical"}]}

Example input:
Sentence: Atypical sensations following the use of subcutaneous sumatriptan are common , but of uncertain origin .

Example answer:
{"entities": [{"text": "Atypical sensations", "type": "Disease"}, {"text": "sumatriptan", "type": "Chemical"}]}

Example input:
Sentence: We report the case of a young woman who suffered a cerebral infarction after taking a single oral dose of PPA .

Example answer:
{"entities": [{"text": "cerebral infarction", "type": "Disease"}, {"text": "PPA", "type": "Chemical"}]}

Example input:
Sentence: The present report describes a case of cardiac arrest and subsequent death as a result of hyperkalaemia following the use of suxamethonium in a 23-year-old Malawian woman .

Example answer:
{"entities": [{"text": "cardiac arrest", "type": "Disease"}, {"text": "death", "type": "Disease"}, {"text": "hyperkalaemia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: In the following report , a 65-year-old critically ill patient with a suspected history of HITT was administered argatroban for anticoagulation on bypass during heart transplantation .

Example answer:
{"entities": [{"text": "critically ill", "type": "Disease"}, {"text": "HITT", "type": "Disease"}, {"text": "argatroban", "type": "Chemical"}]}

Example input:
Sentence: We report a case in which myocardial infarction coincided with the introduction of captopril and the withdrawal of verapamil in a previously asymptomatic woman with severe hypertension .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "captopril", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: We report the case of a 63-year-old female who was treated with methylphenidate due to hyperactivity and suffered from multiple ischaemic strokes .

Example answer:
{"entities": [{"text": "methylphenidate", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "ischaemic strokes", "type": "Disease"}]}

Example input:
Sentence: A 78-year-old with healed septal necrosis suffered a recurrent myocardial infarction of the anterior wall following the administration of isosorbide dinitrate 5 mg sublingually .

Example answer:
{"entities": [{"text": "necrosis", "type": "Disease"}, {"text": "myocardial infarction", "type": "Disease"}, {"text": "isosorbide dinitrate", "type": "Chemical"}]}

Input:
Sentence: We describe a 47-year-old woman with an acute myocardial infarction after administration of sumatriptan 6 mg subcutaneously for cluster headache .

## Item bc5cdr:test:1628
Example input:
Sentence: In two patients , the arrhythmia degenerated into irreversible ventricular fibrillation and both patients died .

Example answer:
{"entities": [{"text": "arrhythmia", "type": "Disease"}, {"text": "ventricular fibrillation", "type": "Disease"}]}

Example input:
Sentence: Of 24 evaluable patients , two achieved a complete remission and one achieved a partial remission for an overall response rate of 12.5 % ( 95 % confidence interval : 2.6-32.4 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: In four patients , polymorphous ventricular tachycardia appeared after intravenous administration of 200 to 400 mg of procainamide for the treatment of sustained ventricular tachycardia .

Example answer:
{"entities": [{"text": "ventricular tachycardia", "type": "Disease"}, {"text": "procainamide", "type": "Chemical"}]}

Example input:
Sentence: Eight patients were dead in the last follow-up ; two of them died of treatment-related toxicity .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Recurrence was studied in 82 evaluable patients after 1 year of follow-up and in 72 patients followed for 2-3 years ( mean 32 months ) .

Example answer:
{"entities": []}

Example input:
Sentence: This was followed by ventricular fibrillation in one patient and sudden death in another .

Example answer:
{"entities": [{"text": "ventricular fibrillation", "type": "Disease"}, {"text": "sudden death", "type": "Disease"}]}

Example input:
Sentence: Of the 59 cases , 26 ( 44 % ) had a fatal outcome , compared to 136 ( 25 % ) among the non-warfarin patients ( p < 0.01 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Of the 82 evaluable patients , 50 did not show any recurrence after 1 year ( 61 % ) , while 32 presented with one or more recurrences ( 39 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: In the seventh patient , a permanent ventricular pacemaker was inserted and , despite continuation of procainamide therapy , polymorphous ventricular tachycardia did not reoccur .

Example answer:
{"entities": [{"text": "procainamide", "type": "Chemical"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: These patients had Q-T prolongation and recurrent syncope due to polymorphous ventricular tachycardia .

Example answer:
{"entities": [{"text": "Q-T prolongation", "type": "Disease"}, {"text": "syncope", "type": "Disease"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Input:
Sentence: During follow-up , seven ( 20 % ) patients had a nonfatal ventricular tachycardia recurrence , and two ( 6 % ) patients died suddenly .

## Item bc5cdr:test:1291
Example input:
Sentence: Angioedema due to ACE inhibitors : common and inadequately diagnosed .

Example answer:
{"entities": [{"text": "Angioedema", "type": "Disease"}, {"text": "ACE inhibitors", "type": "Chemical"}]}

Example input:
Sentence: To assess the safety of the ACE inhibitor enalapril a multicenter , randomized , prazosin-controlled trial was designed that compared the incidence and severity of symptomatic hypotension on the first day of treatment .

Example answer:
{"entities": [{"text": "ACE inhibitor", "type": "Chemical"}, {"text": "enalapril", "type": "Chemical"}, {"text": "prazosin-controlled", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Effects of an inhibitor of angiotensin converting enzyme ( Captopril ) on pulmonary and renal insufficiency due to intravascular coagulation in the rat .

Example answer:
{"entities": [{"text": "angiotensin", "type": "Chemical"}, {"text": "Captopril", "type": "Chemical"}, {"text": "intravascular coagulation", "type": "Disease"}]}

Example input:
Sentence: Current medications did not include angiotensin-converting enzyme inhibitors or beta-blockers .

Example answer:
{"entities": [{"text": "angiotensin-converting", "type": "Chemical"}]}

Example input:
Sentence: Adults chronically treated with angiotensin converting enzyme inhibitors may have a limited ability to respond to hypotension when the sympathetic response is simultaneously blocked .

Example answer:
{"entities": [{"text": "angiotensin", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: The authors present a 10-year-old boy chronically treated with lisinopril , an angiotensin converting enzyme inhibitor , to control hypertension who developed hypotension following the addition of tizanidine , an alpha-2 agonist , for the treatment of spasticity .

Example answer:
{"entities": [{"text": "lisinopril", "type": "Chemical"}, {"text": "angiotensin", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}, {"text": "tizanidine", "type": "Chemical"}, {"text": "spasticity", "type": "Disease"}]}

Example input:
Sentence: Angiotensin-converting enzyme inhibitors and angiotensin II receptor-blocking drugs hold promise in atrial fibrillation through cardiac remodelling .

Example answer:
{"entities": [{"text": "Angiotensin-converting", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "cardiac remodelling", "type": "Disease"}]}

Example input:
Sentence: The estimated incidence of angioedema during angiotensin-converting enzyme ( ACE ) inhibitor treatment is between 1 and 7 per thousand patients .

Example answer:
{"entities": [{"text": "angioedema", "type": "Disease"}, {"text": "angiotensin-converting enzyme ( ACE ) inhibitor", "type": "Chemical"}]}

Example input:
Sentence: Injection of Captopril ( 1 mg/kg ) , an inhibitor of angiotensin converting enzyme ( ACE ) , reduced both pulmonary and renal insufficiency in this rat model .

Example answer:
{"entities": [{"text": "Captopril", "type": "Chemical"}, {"text": "angiotensin", "type": "Chemical"}]}

Example input:
Sentence: Since the introduction of angiotensin converting enzyme ( ACE ) inhibitors into the adjunctive treatment of patients with congestive heart failure , cases of severe hypotension , especially on the first day of treatment , have occasionally been reported .

Example answer:
{"entities": [{"text": "angiotensin converting enzyme ( ACE ) inhibitors", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Input:
Sentence: Angiotensin-converting enzyme ( ACE ) inhibitors , used to treat hypertension and congestive heart failure , were introduced in Europe in the middle of the eighties , and the use of these drugs has increased progressively .

## Item bc5cdr:test:1492
Example input:
Sentence: Organic mental disorder was observed in a 29-year-old female in the prognostic period after the onset of carmofur-induced leukoencephalopathy .

Example answer:
{"entities": [{"text": "Organic mental disorder", "type": "Disease"}, {"text": "carmofur-induced", "type": "Chemical"}, {"text": "leukoencephalopathy", "type": "Disease"}]}

Example input:
Sentence: Acute psychosis due to treatment with phenytoin in a nonepileptic patient .

Example answer:
{"entities": [{"text": "Acute psychosis", "type": "Disease"}, {"text": "phenytoin", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : A 20-year-old male with schizophrenia developed a sudden onset of myocarditis after commencement of clozapine .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "Disease"}, {"text": "myocarditis", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}]}

Example input:
Sentence: A 34-year-old lady developed a constellation of dermatitis , fever , lymphadenopathy and hepatitis , beginning on the 17th day of a course of oral sulphasalazine for sero-negative rheumatoid arthritis .

Example answer:
{"entities": [{"text": "dermatitis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "lymphadenopathy", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Example input:
Sentence: However , the observation that antagonists of the glutamate N-methyl-D-aspartate ( NMDA ) receptor produce schizophrenic-like symptoms in humans has led to the idea of a dysfunctioning of the glutamatergic system via its NMDA receptor .

Example answer:
{"entities": [{"text": "glutamate", "type": "Chemical"}, {"text": "N-methyl-D-aspartate", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "schizophrenic-like", "type": "Disease"}]}

Example input:
Sentence: This was a case of acute palsy of the recurrent laryngeal nerve and superimposed severe acute sensorimotor axonal polyneuropathy caused by high-dose disulfiram intoxication .

Example answer:
{"entities": [{"text": "palsy", "type": "Disease"}, {"text": "polyneuropathy", "type": "Disease"}, {"text": "disulfiram", "type": "Chemical"}]}

Example input:
Sentence: A 54-year-old hypothyroid male taking thyroxine and simvastatin presented with bilateral leg compartment syndrome and myonecrosis .

Example answer:
{"entities": [{"text": "hypothyroid", "type": "Disease"}, {"text": "thyroxine", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "compartment syndrome", "type": "Disease"}, {"text": "myonecrosis", "type": "Disease"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: The case of a nonepileptic patient who developed psychosis following phenytoin treatment for trigeminal neuralgia is described .

Example answer:
{"entities": [{"text": "psychosis", "type": "Disease"}, {"text": "phenytoin", "type": "Chemical"}, {"text": "trigeminal neuralgia", "type": "Disease"}]}

Example input:
Sentence: We report an undiagnosed case of myotonia congenita in a 24-year-old previously healthy primigravida , who developed life threatening masseter spasm following a standard dose of intravenous suxamethonium for induction of anaesthesia .

Example answer:
{"entities": [{"text": "myotonia congenita", "type": "Disease"}, {"text": "masseter spasm", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Input:
Sentence: This patient could have been diagnosed as having either neuroleptic malignant syndrome ( NMS ) or serotonin syndrome ( SS ) .

## Item bc5cdr:test:1689
Example input:
Sentence: Spironolactone-induced renal insufficiency and hyperkalemia in patients with heart failure .

Example answer:
{"entities": [{"text": "Spironolactone-induced", "type": "Chemical"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}]}

Example input:
Sentence: The hypotensive episodes were severe enough to require vasopressor administration .

Example answer:
{"entities": [{"text": "hypotensive", "type": "Disease"}]}

Example input:
Sentence: Transient hypotension ( SAP < 90mmHg ) occurred in 1 patient ( 0.7 % ) .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Hyperkalemia has recently been recognized as a complication of nonsteroidal antiinflammatory agents ( NSAID ) such as indomethacin .

Example answer:
{"entities": [{"text": "Hyperkalemia", "type": "Disease"}, {"text": "indomethacin", "type": "Chemical"}]}

Example input:
Sentence: We describe 4 patients in whom hyperkalemia ranging from 6.1 to 6.9 mEq/l developed within 3 to 8 days of sulindac administration .

Example answer:
{"entities": [{"text": "hyperkalemia", "type": "Disease"}, {"text": "sulindac", "type": "Chemical"}]}

Example input:
Sentence: Patients who developed hyperkalemia were older and more likely to have diabetes , had higher baseline serum potassium levels and lower baseline potassium supplement doses , and were more likely to be treated with beta-blockers than controls ( n = 134 ) .

Example answer:
{"entities": [{"text": "hyperkalemia", "type": "Disease"}, {"text": "diabetes", "type": "Disease"}, {"text": "potassium", "type": "Chemical"}]}

Example input:
Sentence: The present report describes a case of cardiac arrest and subsequent death as a result of hyperkalaemia following the use of suxamethonium in a 23-year-old Malawian woman .

Example answer:
{"entities": [{"text": "cardiac arrest", "type": "Disease"}, {"text": "death", "type": "Disease"}, {"text": "hyperkalaemia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Spironolactone-induced hyperkalemia and renal insufficiency are more common in our clinical experience than reported previously .

Example answer:
{"entities": [{"text": "Spironolactone-induced", "type": "Chemical"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}]}

Example input:
Sentence: Apart from the reduction in the patient 's level of consciousness , there were no signs of motor neurone damage or of any of the other known predisposing conditions for hyperkalaemia following the administration of suxamethonium .

Example answer:
{"entities": [{"text": "hyperkalaemia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: Cases were patients who developed hyperkalemia ( K ( + ) > 5.0 mEq/L ) or renal insufficiency ( Cr > or=2.5 mg/dL ) , and they were compared to 2 randomly selected controls per case .

Example answer:
{"entities": [{"text": "hyperkalemia", "type": "Disease"}, {"text": "K", "type": "Chemical"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "Cr", "type": "Chemical"}]}

Input:
Sentence: Symptomatic hypokalemia did not occur .

## Item bc5cdr:test:1388
Example input:
Sentence: Such effects of THP were reversed by RAMH indicating the involvement of histamine H ( 3 ) -receptors .

Example answer:
{"entities": []}

Example input:
Sentence: THP exhibited an antipsychotic-like profile by potentiating haloperidol-induced catalepsy , reducing amphetamine-induced hyperactivity and reducing apomorphine-induced climbing in mice .

Example answer:
{"entities": []}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "a reduced locomotor activity", "type": "Disease"}]}

Example input:
Sentence: NX caused an additive deterioration in GFR which , however , was ameliorated by HP .

Example answer:
{"entities": []}

Example input:
Sentence: The present results are consistent with the carcinogenicity experiment suggesting that different mechanisms are involved in FANFT carcinogenesis in the bladder and forestomach , and that aspirin 's effect on FANFT in the forestomach is not due to an irritant effect associated with increased cell proliferation .

Example answer:
{"entities": [{"text": "FANFT", "type": "Chemical"}, {"text": "carcinogenesis", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: The administration of ephedrine led to a similar increase in MAP ( 53 +/- 9 to 79 +/- 8 mmHg ; P < 0.001 ) , restored CO ( 3.2 +/- 1.2 to 5.0 +/- 1.3 l min ( -1 ) ) , and preserved S ( c ) O ( 2 ) .

Example answer:
{"entities": [{"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: However , the increase in release of ACh produced by the first application of KCl was 2-fold higher in WSP versus WSR mice .

Example answer:
{"entities": [{"text": "ACh", "type": "Chemical"}, {"text": "KCl", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Induction of anesthesia was followed by a decrease in MAP , HR , SV , and CO concomitant with an elevation in S ( c ) O ( 2 ) .

Example answer:
{"entities": []}

Example input:
Sentence: After administration of phenylephrine , MAP increased ( 51 +/- 12 to 81 +/- 13 mmHg ; P < 0.001 ; mean +/- SD ) .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}]}

Example input:
Sentence: In the forestomach , and also in the liver , aspirin did not affect the FANFT-induced increase in labeling index .

Example answer:
{"entities": [{"text": "aspirin", "type": "Chemical"}, {"text": "FANFT-induced", "type": "Chemical"}]}

Input:
Sentence: ANP did not cause significant changes in MAP in both strains as compared to vehicle , but it abolished AVP-induced MAP increase in WKY and SHR .

## Item bc5cdr:test:1616
Example input:
Sentence: We initiated a phase I/II trial to determine the response and toxicity of escalating paclitaxel doses combined with fixed-dose cisplatin with granulocyte colony-stimulating factor support in patients with untreated locally advanced inoperable head and neck carcinoma .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "head and neck carcinoma", "type": "Disease"}]}

Example input:
Sentence: After 154 courses of therapy , the median dose intensity was 131 mg/m ( 2 ) for paclitaxel ( 97.3 % ) , 117 mg/m ( 2 ) for cisplatin ( 97.3 % ) , and 1378 mg/m ( 2 ) for gemcitabine ( 86.2 % ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}]}

Example input:
Sentence: Plasma PRL concentrations were analysed at 10 min intervals and underlying secretory rates calculated by a deconvolution procedure .

Example answer:
{"entities": []}

Example input:
Sentence: The area under the plasma concentration time curve at 90 min was 4-12 times greater than for oral drug , suggesting the existence of an absorption-limiting process in the intestine , and providing an alternate form of administration for quaternary drugs .

Example answer:
{"entities": []}

Example input:
Sentence: After completion of the amifostine infusion , cisplatin 120 mg/m2 was administered over 30 minutes .

Example answer:
{"entities": [{"text": "amifostine", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: When discharged less than 24 hours later , he was receiving metoprolol and aspirin , with follow-up plans for echocardiography and nuclear imaging to assess perfusion .

Example answer:
{"entities": [{"text": "metoprolol", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: With paclitaxel doses of 200 mg/m2 and higher , granulocyte colony-stimulating factor 5 micrograms/kg/d is given ( days 4 through 12 ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}]}

Example input:
Sentence: Preliminary results of an Eastern Cooperative Oncology Group study of single-agent paclitaxel ( Taxol ; Bristol-Myers Squibb Company , Princeton , NJ ) reported a 37 % response rate in patients with head and neck cancer , and the paclitaxel/cisplatin combination has been used successfully and has significantly improved median response duration in ovarian cancer patients .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "Taxol", "type": "Chemical"}, {"text": "head and neck cancer", "type": "Disease"}, {"text": "paclitaxel/cisplatin", "type": "Chemical"}, {"text": "ovarian cancer", "type": "Disease"}]}

Example input:
Sentence: Thirty-five consecutive chemotherapy-naive patients with Stage IV NSCLC and an Eastern Cooperative Oncology Group performance status of 0-2 were treated with a combination of paclitaxel ( 135 mg/m ( 2 ) given intravenously in 3 hours ) on Day 1 , cisplatin ( 120 mg/m ( 2 ) given intravenously in 6 hours ) on Day 1 , and gemcitabine ( 800 mg/m ( 2 ) given intravenously in 30 minutes ) on Days 1 and 8 , every 4 weeks .

Example answer:
{"entities": [{"text": "NSCLC", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}]}

Example input:
Sentence: Treatment , given every 21 days for a maximum of three cycles , consisted of paclitaxel by 3-hour infusion followed the next day by a fixed dose of cisplatin ( 75 mg/m2 ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Input:
Sentence: Plasma paclitaxel concentrations were measured at the completion of paclitaxel infusion and at 24 hours in 19 patients .

## Item bc5cdr:test:1705
Example input:
Sentence: Importantly , GNC92H2 prevented death even post-cocaine injection .

Example answer:
{"entities": [{"text": "GNC92H2", "type": "Chemical"}, {"text": "death", "type": "Disease"}]}

Example input:
Sentence: Stroke followed cocaine use by inhalation , intranasal , intravenous , and intramuscular routes .

Example answer:
{"entities": [{"text": "Stroke", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Our findings indicate that cocaine induced hyperlocomotion is modified by 5-HT1B receptor ligands microinjected into the accumbens shell , but not core , this modification consisting in inhibitory and facilitatory effects of the 5-HT1B receptor antagonist ( GR 55562 ) and agonist ( CP 93129 ) , respectively .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "hyperlocomotion", "type": "Disease"}, {"text": "GR 55562", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Example input:
Sentence: Swiss albino mice prepared with intrajugular catheters were tested in photocell cages after administration of 93 mg/kg ( LD50 ) of cocaine and GNC92H2 infusions ranging from 30 to 190 mg/kg .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "GNC92H2", "type": "Chemical"}]}

Example input:
Sentence: Clinical and experimental data published to date suggest several possible mechanisms by which cocaine may result in acute myocardial infarction .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: When injected into the accumbens shell ( but not the core ) before cocaine , CP 93129 ( 0.1-10 microg/side ) enhanced the locomotor response to cocaine ; the maximum effect being observed after 10 microg/side of the agonist .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Example input:
Sentence: Electrocardiographic evidence of myocardial injury in psychiatrically hospitalized cocaine abusers .

Example answer:
{"entities": [{"text": "myocardial injury", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: The finding of cocaine-induced vasoconstriction in segments of ( noninnervated ) human umbilical artery suggests that the presence or absence of intact innervation is not sufficient to explain the discrepant data involving the possibility of alpha-mediated effects .

Example answer:
{"entities": [{"text": "cocaine-induced", "type": "Chemical"}]}

Example input:
Sentence: Eleven of the cocaine abusers and none of the controls had ECG evidence of significant myocardial injury defined as myocardial infarction , ischemia , and bundle branch block .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "myocardial injury", "type": "Disease"}, {"text": "myocardial infarction", "type": "Disease"}, {"text": "ischemia", "type": "Disease"}, {"text": "bundle branch block", "type": "Disease"}]}

Example input:
Sentence: In individuals with preexisting , high-grade coronary arterial narrowing , acute myocardial infarction may result from an increase in myocardial oxygen demand associated with cocaine-induced increase in rate-pressure product .

Example answer:
{"entities": [{"text": "acute myocardial infarction", "type": "Disease"}, {"text": "oxygen", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}]}

Input:
Sentence: CONCLUSIONS : In humans , the intracoronary infusion of cocaine sufficient in amount to achieve a high drug concentration in coronary sinus blood causes a deterioration of LV systolic and diastolic performance .

## Item bc5cdr:test:1786
Example input:
Sentence: In the two patients , skin and ELISA tests with paramethasone were negative , as was the prick test with each of its excipients .

Example answer:
{"entities": [{"text": "paramethasone", "type": "Chemical"}]}

Example input:
Sentence: Symptoms persisted for three months despite TAC dose reduction , administration of IVIG and four doses of methylprednisolone pulse therapy .

Example answer:
{"entities": [{"text": "TAC", "type": "Chemical"}, {"text": "methylprednisolone", "type": "Chemical"}]}

Example input:
Sentence: Beyond 8 days of DES exposure , the immunochemically PRL-positive proportion of cells increased to over 50 % of the total population .

Example answer:
{"entities": [{"text": "DES", "type": "Chemical"}]}

Example input:
Sentence: At the highest effective doses , PG-9 did not produce any collateral symptoms as revealed by the Irwin test , and it did not modify spontaneous motility and inspection activity , as revealed by the hole-board test .

Example answer:
{"entities": []}

Example input:
Sentence: Tissues were analyzed at 0 , 5 , 7 , 11 , 21 , 45 , 80 and 126 days after PAN injection so as to include both the acute phase of proteinuria associated with foot process effacement ( days 5-11 ) and the chronic phase of proteinuria associated with glomerulosclerosis ( days 45-126 ) .

Example answer:
{"entities": [{"text": "PAN", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: Skin tests were performed with benzylpenicilloyl-poly-L-lysine ( BPO-PLL ) , benzylpenicilloate , benzylpenicillin ( PG ) , ampicillin ( AMP ) , and AX .

Example answer:
{"entities": [{"text": "benzylpenicilloyl-poly-L-lysine", "type": "Chemical"}, {"text": "BPO-PLL", "type": "Chemical"}, {"text": "benzylpenicilloate", "type": "Chemical"}, {"text": "benzylpenicillin", "type": "Chemical"}, {"text": "PG", "type": "Chemical"}, {"text": "ampicillin", "type": "Chemical"}, {"text": "AMP", "type": "Chemical"}, {"text": "AX", "type": "Chemical"}]}

Example input:
Sentence: Examinations , including blood pressure , pulse rate , conjunctiva and cornea , intraocular pressure ( IOP ) , pupil diameter , basal tear secretion and margin reflex distance of both upper and lower eyelids , were performed prior to entry and at 1 , 3 , 5 and 7 hours after instillation .

Example answer:
{"entities": []}

Example input:
Sentence: The aorta/serum-ratio and the radioactive build-up 24 and 48 hours after injection of 131I-HSA was reduced in animals treated with D-pen for 42 days , indicating an impeded transmural transport of tracer which may be caused by a steric exclusion effect of abundant hyaluronate .

Example answer:
{"entities": [{"text": "D-pen", "type": "Chemical"}, {"text": "hyaluronate", "type": "Chemical"}]}

Example input:
Sentence: Groups 1 and 2 underwent micropuncture studies after 10 days .

Example answer:
{"entities": []}

Example input:
Sentence: Finally , pruritus disappeared within 19 months , and liver tests returned to normal 27 months after the onset of hepatitis .

Example answer:
{"entities": [{"text": "pruritus", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}]}

Input:
Sentence: The skin tests revealed positive delayed reactions of 24 hours and 48 hours by IDR and patch tests to only some PRC with common chains in their structures .

## Item bc5cdr:test:1708
Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Example input:
Sentence: After delivery of the infant , there should be no contraindication to the use of an alpha-adrenergic vasopressor such as phenylephrine to treat hypotensive patients with tachycardia .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "hypotensive", "type": "Disease"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: Capsaicin ( 10 micro g ) was injected into the masseter muscle to induce pain in 11 healthy volunteers .

Example answer:
{"entities": [{"text": "Capsaicin", "type": "Chemical"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: Streptomycin sulfate ( 300 mg/kg s.c. ) was injected for various periods into preweanling rats and for 3 weeks into weanling rats .

Example answer:
{"entities": [{"text": "Streptomycin", "type": "Chemical"}]}

Example input:
Sentence: In order to address long-term pain memory , nine healthy male volunteers received intradermal injections of three doses of capsaicin ( 0.05 , 1 and 20 microg , separated by 15 min breaks ) , each given three times in a balanced design across three sessions at one week intervals .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Reassuringly , penicillins , erythromycins , and cephalosporins , although used commonly by pregnant women , were not associated with many birth defects .

Example answer:
{"entities": [{"text": "penicillins", "type": "Chemical"}, {"text": "erythromycins", "type": "Chemical"}, {"text": "cephalosporins", "type": "Chemical"}, {"text": "birth defects", "type": "Disease"}]}

Example input:
Sentence: Rats were treated with a single IV injection of puromycin aminonucleoside , ( PAN , 7.5 mg/kg ) and 24 hour urine samples were obtained prior to sacrifice on days 3,5,7,10,17,27,41 ( N = 5-10 per group ) .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : He was treated with intravenous administration of corticosteroids and glycerin for 6 days after the injection .

Example answer:
{"entities": [{"text": "glycerin", "type": "Chemical"}]}

Example input:
Sentence: Pregnant rats were administered one of these calcium channel blockers during the period of cardiac morphogenesis and the offspring examined on day 20 of gestation for cardiovascular malformations .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "cardiovascular malformations", "type": "Disease"}]}

Example input:
Sentence: Pregnant rats were given either vehicle or 2 daily intraperitoneal injections of dexamethasone ( 0.2 mg/kg body weight ) on gestational days 11 and 12 , 13 and 14 , 15 and 16 , 17 and 18 , or 19 and 20 .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}]}

Input:
Sentence: MATERIALS AND METHODS : Carbetocin was given as an intramuscular injection immediately after the birth of the infant in 45 healthy women with normal singleton pregnancies who delivered vaginally at term .

## Item bc5cdr:test:1715
Example input:
Sentence: In the present study , cis-platin ( 80-120 mg/m2BSA ) and 5-FU ( 1000 mg/m2BSA daily as a continuous infusion during 5 days ) were given to 76 patients before radiotherapy and surgery .

Example answer:
{"entities": [{"text": "cis-platin", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: Haemodilution in groups B and C was produced by withdrawing approximately 1000 mL of blood and replacing it with the same amount of dextran solution , and final haematocrit values were 21 or 22 % .

Example answer:
{"entities": [{"text": "Haemodilution", "type": "Disease"}, {"text": "dextran", "type": "Chemical"}]}

Example input:
Sentence: Total fasciculation scores in the 30-mg bolus group and the 5-mg s-1 and 20-mg s-1 infusion groups were not significantly different .

Example answer:
{"entities": [{"text": "fasciculation", "type": "Disease"}]}

Example input:
Sentence: Total cumulative doses were 36 or 60 g/m2 of ifosfamide ( six or 10 cycles of ifosfamide , vincristine , and dactinomycin [ IVA ] ) .

Example answer:
{"entities": [{"text": "ifosfamide", "type": "Chemical"}, {"text": "ifosfamide , vincristine , and dactinomycin", "type": "Chemical"}, {"text": "IVA", "type": "Chemical"}]}

Example input:
Sentence: Maximum tolerated dose in good-risk patients was 70 mg/m2 , and in poor-risk patients , 60 mg/m2 .

Example answer:
{"entities": []}

Example input:
Sentence: Response rates according to three sets of criteria were greater with the standard dose ( 55 % -60 % ) than the low dose ( 25 % -35 % ) and placebo ( 25 % -30 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: After 154 courses of therapy , the median dose intensity was 131 mg/m ( 2 ) for paclitaxel ( 97.3 % ) , 117 mg/m ( 2 ) for cisplatin ( 97.3 % ) , and 1378 mg/m ( 2 ) for gemcitabine ( 86.2 % ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}]}

Example input:
Sentence: All patients were on a regular transfusion-chelation program maintaining a mean hemoglobin level of 9.5 gr/dl .

Example answer:
{"entities": []}

Example input:
Sentence: This agent was well tolerated in healthy volunteers at doses up to 100 micrograms/kg/min .

Example answer:
{"entities": []}

Input:
Sentence: The majority of additional administration of oxytocics ( 4/5 ) and blood transfusion ( 3/5 ) occurred in the dose groups of 200 microg .

## Item bc5cdr:test:1795
Example input:
Sentence: After 2 weeks of treatment , patients tested 5-8 h after the last dose of medication did not show any decrement of performance .

Example answer:
{"entities": []}

Example input:
Sentence: Delirium was diagnosed in 14 ( 10.1 % incidence , or 1.48 cases/person-years of exposure ) ; 71.4 % of cases were moderate or severe .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}]}

Example input:
Sentence: In a double-blind 6-week trial , 458 patients with acute schizophrenia were randomly assigned to fixed-dose treatment with asenapine at 5 mg twice daily ( BID ) , asenapine at 10 mg BID , placebo , or haloperidol at 4 mg BID ( to verify assay sensitivity ) .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "Disease"}, {"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: METHOD : The response of 44 patients meeting DSM-IV criteria for bipolar disorder to naturalistic treatment was assessed for at least 6 weeks using the Montgomery-Asberg Depression Rating Scale and the Bech-Rafaelson Mania Rating Scale .

Example answer:
{"entities": [{"text": "bipolar disorder", "type": "Disease"}]}

Example input:
Sentence: Significant declines in simple and sustained attention , working memory , and verbal memory were observed at 1 hour postdose compared to baseline for both age groups with a trend toward return to baseline by 5 hours postdose .

Example answer:
{"entities": []}

Example input:
Sentence: During an 18-month period of study 41 hemodialyzed patients receiving desferrioxamine ( 10-40 mg/kg BW/3 times weekly ) for the first time were monitored for detection of audiovisual toxicity .

Example answer:
{"entities": [{"text": "desferrioxamine", "type": "Chemical"}, {"text": "audiovisual toxicity", "type": "Disease"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: This change resulted within 2-4 weeks in the 50-200 % increase in the plasma levels of these neuroleptics and the appearance of extrapyramidal symptoms .

Example answer:
{"entities": [{"text": "extrapyramidal symptoms", "type": "Disease"}]}

Example input:
Sentence: He developed acute neurologic symptoms of mental confusion , disorientation and irritability , and then lapsed into a deep coma , lasting for approximately 40 hours during the first dose ( day 2 ) of 5-fluorouracil and folinic acid infusion .

Example answer:
{"entities": [{"text": "confusion", "type": "Disease"}, {"text": "disorientation", "type": "Disease"}, {"text": "irritability", "type": "Disease"}, {"text": "coma", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: When deferoxamine therapy was discontinued and serial studies were performed , audiograms in seven cases reverted to normal or near normal within two to three weeks , and nine of 13 patients with symptoms became asymptomatic .

Example answer:
{"entities": [{"text": "deferoxamine", "type": "Chemical"}]}

Input:
Sentence: In 25 out of 32 episodes ( 78 % ) , plasma ammonium levels and mental status returned to normal within 2 days after adequate management .

## Item bc5cdr:test:1584
Example input:
Sentence: MEASUREMENTS AND MAIN RESULTS : None of 23 patients who received docetaxel alone developed VTE , whereas 9 of 47 patients ( 19 % ) who received docetaxel plus thalidomide developed VTE ( p=0.025 ) .

Example answer:
{"entities": [{"text": "docetaxel", "type": "Chemical"}, {"text": "VTE", "type": "Disease"}, {"text": "thalidomide", "type": "Chemical"}]}

Example input:
Sentence: Among women who used oral contraceptives , the odds ratio was 2.1 ( 95 percent confidence interval , 1.5 to 3.0 ) for those without a prothrombotic mutation and 1.9 ( 95 percent confidence interval , 0.6 to 5.5 ) for those with a mutation CONCLUSIONS : The risk of myocardial infarction was increased among women who used second-generation oral contraceptives .

Example answer:
{"entities": [{"text": "oral contraceptives", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Using as the reference group women who were not using oral contraception , had no recent pregnancy or menopausal symptoms , the case-control analysis gave an adjusted odds ratio ( OR ( adj ) ) of 7.44 ( 95 % CI 3.67-15.08 ) for CPA/EE use compared with an OR ( adj ) of 2.58 ( 95 % CI 1.60-4.18 ) for use of conventional COCs .

Example answer:
{"entities": [{"text": "CPA/EE", "type": "Chemical"}]}

Example input:
Sentence: Forty-three ovarian cancer patients were available for analysis following six cycles of the same PAC-containing regimen : 23 had been supplemented by glutamate all along the treatment period , at a daily dose of three times 500 mg ( group G ) , and 20 had received a placebo ( group P ) .

Example answer:
{"entities": [{"text": "ovarian cancer", "type": "Disease"}, {"text": "PAC-containing", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Using the General Practice Research Database we conducted a cohort analysis and case-control study nested within a population of women aged between 15 and 39 years with acne , hirsutism or PCOS to estimate the risk of VTE associated with CPA/EE .

Example answer:
{"entities": [{"text": "acne", "type": "Disease"}, {"text": "hirsutism", "type": "Disease"}, {"text": "PCOS", "type": "Disease"}, {"text": "VTE", "type": "Disease"}, {"text": "CPA/EE", "type": "Chemical"}]}

Example input:
Sentence: Previous studies have demonstrated an increased risk of venous thromboembolism ( VTE ) associated with CPA/EE compared with conventional combined oral contraceptives ( COCs ) .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "VTE", "type": "Disease"}, {"text": "CPA/EE", "type": "Chemical"}, {"text": "oral contraceptives", "type": "Chemical"}]}

Example input:
Sentence: We investigated this association , according to the type of progestagen included in third-generation ( i.e. , desogestrel or gestodene ) and second-generation ( i.e. , levonorgestrel ) oral contraceptives , the dose of estrogen , and the presence or absence of prothrombotic mutations METHODS : In a nationwide , population-based , case-control study , we identified and enrolled 248 women 18 through 49 years of age who had had a first myocardial infarction between 1990 and 1995 and 925 control women who had not had a myocardial infarction and who were matched for age , calendar year of the index event , and area of residence .

Example answer:
{"entities": [{"text": "progestagen", "type": "Chemical"}, {"text": "desogestrel", "type": "Chemical"}, {"text": "gestodene", "type": "Chemical"}, {"text": "levonorgestrel", "type": "Chemical"}, {"text": "oral contraceptives", "type": "Chemical"}, {"text": "estrogen", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: The epidemiological studies that assessed the risk of venous thromboembolism ( VTE ) associated with newer oral contraceptives ( OC ) did not distinguish between patterns of OC use , namely first-time users , repeaters and switchers .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "VTE", "type": "Disease"}, {"text": "oral contraceptives", "type": "Chemical"}, {"text": "OC", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : We have demonstrated an increased risk of VTE associated with the use of CPA/EE in women with acne , hirsutism or PCOS although residual confounding by indication can not be excluded .

Example answer:
{"entities": [{"text": "VTE", "type": "Disease"}, {"text": "CPA/EE", "type": "Chemical"}, {"text": "acne", "type": "Disease"}, {"text": "hirsutism", "type": "Disease"}, {"text": "PCOS", "type": "Disease"}]}

Input:
Sentence: FINDINGS : 85 women met the inclusion criteria for VTE , two of whom were users of progestagen-only OCs .

## Item bc5cdr:test:1431
Example input:
Sentence: A reproducible model for producing diffuse myocardial injury ( epinephrine infusion ) has been developed to study the cardioprotective effects of agents or maneuvers which might alter the evolution of acute myocardial infarction .

Example answer:
{"entities": [{"text": "myocardial injury", "type": "Disease"}, {"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: In conclusion , CPA , diazepam and 2PAM in combination with atropine prevented the occurrence of serious signs of poisoning and thus reduced the toxicity of DFP in rat .

Example answer:
{"entities": [{"text": "CPA", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "atropine", "type": "Chemical"}, {"text": "poisoning", "type": "Disease"}, {"text": "toxicity", "type": "Disease"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: The results show that pretreatment with TCR may be useful in preventing the damage induced by isoproterenol in rat heart .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: Cardioprotective effect of tincture of Crataegus on isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "tincture of Crataegus", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: In unanesthetized , spontaneously hypertensive rats the decrease in blood pressure and heart rate produced by intravenous clonidine , 5 to 20 micrograms/kg , was inhibited or reversed by nalozone , 0.2 to 2 mg/kg .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}, {"text": "clonidine", "type": "Chemical"}, {"text": "nalozone", "type": "Chemical"}]}

Example input:
Sentence: TCR protected against pathological changes induced by isoproterenol in rat heart .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: Estrogens protect ovariectomized rats from hippocampal injury induced by kainic acid-induced status epilepticus ( SE ) .

Example answer:
{"entities": [{"text": "hippocampal injury", "type": "Disease"}, {"text": "kainic", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Effects of acetylsalicylic acid , dipyridamole , and hydrocortisone on epinephrine-induced myocardial injury in dogs .

Example answer:
{"entities": [{"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine-induced", "type": "Chemical"}, {"text": "myocardial injury", "type": "Disease"}]}

Example input:
Sentence: Epinephrine has a proven role in cardiac arrest in prehospital care ; however , use by paramedics in patients with suspected allergic reaction and severe hypertension should be viewed with caution .

Example answer:
{"entities": [{"text": "Epinephrine", "type": "Chemical"}, {"text": "cardiac arrest", "type": "Disease"}, {"text": "allergic reaction", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}]}

Input:
Sentence: Protective effect of clentiazem against epinephrine-induced cardiac injury in rats .

## Item bc5cdr:test:1441
Example input:
Sentence: A reproducible model for producing diffuse myocardial injury ( epinephrine infusion ) has been developed to study the cardioprotective effects of agents or maneuvers which might alter the evolution of acute myocardial infarction .

Example answer:
{"entities": [{"text": "myocardial injury", "type": "Disease"}, {"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: As a consequence of blocking I ( f ) , clonidine reduced the slope of the diastolic depolarization and the frequency of pacemaker potentials in sinoatrial node cells from wild-type and alpha2ABC-knockout mice .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: Clonidine inhibited the native pacemaker current ( I ( f ) ) in isolated sinoatrial node pacemaker cells and the I ( f ) -generating hyperpolarization-activated cyclic nucleotide-gated ( HCN ) 2 and HCN4 channels in transfected HEK293 cells .

Example answer:
{"entities": [{"text": "Clonidine", "type": "Chemical"}, {"text": "cyclic", "type": "Chemical"}]}

Example input:
Sentence: We describe the effect of phenylephrine and ephedrine on frontal lobe oxygenation ( S ( c ) O ( 2 ) ) following anesthesia-induced hypotension .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "ephedrine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Direct inhibition of cardiac HCN pacemaker channels contributes to the bradycardic effects of clonidine gene-targeted mice in vivo , and thus , clonidine-like drugs represent novel structures for future HCN channel inhibitors .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}, {"text": "clonidine-like", "type": "Chemical"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : The utilization of phenylephrine to correct hypotension induced by anesthesia has a negative impact on S ( c ) O ( 2 ) while ephedrine maintains frontal lobe oxygenation potentially related to an increase in CO .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: Effects of acetylsalicylic acid , dipyridamole , and hydrocortisone on epinephrine-induced myocardial injury in dogs .

Example answer:
{"entities": [{"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine-induced", "type": "Chemical"}, {"text": "myocardial injury", "type": "Disease"}]}

Example input:
Sentence: Epinephrine has a proven role in cardiac arrest in prehospital care ; however , use by paramedics in patients with suspected allergic reaction and severe hypertension should be viewed with caution .

Example answer:
{"entities": [{"text": "Epinephrine", "type": "Chemical"}, {"text": "cardiac arrest", "type": "Disease"}, {"text": "allergic reaction", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}]}

Input:
Sentence: In conclusion , clentiazem attenuated epinephrine-induced cardiac injury , possibly through its effect on the adrenergic pathway .

## Item bc5cdr:test:1834
Example input:
Sentence: Rats were treated with seven day intravenous infusion of fucoidan ( 30 micrograms h-1 ) or vehicle .

Example answer:
{"entities": [{"text": "fucoidan", "type": "Chemical"}]}

Example input:
Sentence: Thirty milliliters of blood was obtained for isolation of peripheral blood mononuclear cells after each treatment period .

Example answer:
{"entities": []}

Example input:
Sentence: Briefly , cells were differentiated for 72 h with 100 nM PMA to obtain a macrophage-like phenotype in the presence or absence of 1 nM 17beta-estradiol ( E2 ) , 100 nM progesterone or vehicle ( 0.01 % ethanol ) .

Example answer:
{"entities": [{"text": "17beta-estradiol", "type": "Chemical"}, {"text": "E2", "type": "Chemical"}, {"text": "progesterone", "type": "Chemical"}, {"text": "ethanol", "type": "Chemical"}]}

Example input:
Sentence: In Mg ( 2+ ) -free bathing medium containing bicuculline , conditions designed to increase excitability in the slices , electrical stimulation of the hilus resulted in a single population spike in granule cells from control mice and pilocarpine-treated mice that did not experience SE .

Example answer:
{"entities": [{"text": "Mg", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "pilocarpine-treated", "type": "Chemical"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Rats were treated with the vehicle ( 2 mL/kg of distilled water and 5 % w/v cellulose , 10 days ) , gum Arabic ( 2 mL/kg of a 10 % w/v aqueous suspension of gum Arabic powder , orally for 10 days ) , or gum Arabic concomitantly with GM ( 80mg/kg/day intramuscularly , during the last six days of the treatment period ) .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: In microdialysis experiments , the lines did not differ in basal release of ACh , and 50 mM KCl increased ACh output in both lines of mice .

Example answer:
{"entities": [{"text": "ACh", "type": "Chemical"}, {"text": "KCl", "type": "Chemical"}]}

Example input:
Sentence: Cells were then treated with 30 ng/ml ritonavir or vehicle in the presence of aggregated LDL for 24 h. Cell extracts were harvested , and lipid or total RNA was isolated .

Example answer:
{"entities": [{"text": "ritonavir", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Using in vivo microdialysis , we compared acute exposure ( 450 mg/kg ) to an identical sub-chronic exposure ( 150 mg/kg per day for 3 days ) , followed by 1- or 3-day washout .

Example answer:
{"entities": []}

Example input:
Sentence: Treatment was comprised of VNB , 25 mg/m ( 2 ) , plus GEM , 1000 mg/m ( 2 ) , both on Days 1 , 8 , and 15 every 28 days .

Example answer:
{"entities": [{"text": "VNB", "type": "Chemical"}, {"text": "GEM", "type": "Chemical"}]}

Input:
Sentence: Cells were treated for 0-24 h with each compound ( 0-200 microM ) .

## Item bc5cdr:test:1836
Example input:
Sentence: The aim of the study was to assess the clinical significance of genetic variants in butyrylcholinesterase gene ( BCHE ) in patients with a suspected prolonged duration of action of succinylcholine after ECT .

Example answer:
{"entities": [{"text": "succinylcholine", "type": "Chemical"}]}

Example input:
Sentence: BMCs obtained from green fluorescent protein ( GFP ) transgenic mice or rats were transplanted intravenously after induction of status epilepticus ( SE ) .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: After EE treatment , changes in immunostaining for 7H6 and ZO-1 were similar to those seen in periportal hepatocytes after BDL , but distributed more diffusely throughout the lobule .

Example answer:
{"entities": [{"text": "EE", "type": "Chemical"}]}

Example input:
Sentence: Thirty milliliters of blood was obtained for isolation of peripheral blood mononuclear cells after each treatment period .

Example answer:
{"entities": []}

Example input:
Sentence: Results indicate that GSPE preexposure prior to AAP , AMI and DOX , provided near complete protection in terms of serum chemistry changes ( ALT , BUN and CPK ) , and significantly reduced DNA fragmentation .

Example answer:
{"entities": [{"text": "GSPE", "type": "Chemical"}, {"text": "AAP", "type": "Chemical"}, {"text": "AMI", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: In ICH intrastriatally induced by 0.014-unit , 0.070-unit , and 0.350-unit collagenase , the amount of bleeding was measured using a hemoglobin assay developed in the present study and was compared with the morphologically determined hematoma volume .

Example answer:
{"entities": [{"text": "ICH", "type": "Disease"}, {"text": "bleeding", "type": "Disease"}, {"text": "hematoma", "type": "Disease"}]}

Example input:
Sentence: The results suggest that hypomethylation of DNA per se may not be sufficient for initiation .

Example answer:
{"entities": []}

Example input:
Sentence: At termination of the experiments , mice underwent echocardiography , quantitation of abundance of molecular markers of CM ( ventricular mRNA encoding atrial natriuretic factor [ ANF ] and sarcoplasmic calcium ATPase [ SERCA2 ] ) , and determination of plasma LA .

Example answer:
{"entities": [{"text": "CM", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "LA", "type": "Chemical"}]}

Example input:
Sentence: Parameters of study included analysis of serum chemistry ( ALT , BUN and CPK ) , and orderly fragmentation of genomic DNA ( both endonuclease-dependent and independent ) in addition to microscopic evaluation of damage and/or protection in corresponding PAS stained tissues .

Example answer:
{"entities": []}

Example input:
Sentence: Serum samples were PCR amplified with HBV reverse transcriptase ( RT ) primers , followed by direct sequencing across the tyrosine-methionine-aspartate-aspartate ( YMDD ) motif of the major catalytic region in the C domain of the HBV RT enzyme .

Example answer:
{"entities": [{"text": "tyrosine-methionine-aspartate-aspartate", "type": "Chemical"}]}

Input:
Sentence: Results were confirmed by determination of internucleosomal DNA fragmentation using gel electrophoresis for HL60 cell samples and terminal deoxynucleotidyl transferase assay in HBMP cells .

## Item bc5cdr:test:1157
Example input:
Sentence: METHODS : A review of admissions during a 6-year period revealed 14 patients with cocaine-related aneurysms .

Example answer:
{"entities": [{"text": "cocaine-related", "type": "Chemical"}, {"text": "aneurysms", "type": "Disease"}]}

Example input:
Sentence: Her medical history included coronary artery disease with previous myocardial infarctions , hypertension , and diabetes mellitus .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "myocardial infarctions", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "diabetes mellitus", "type": "Disease"}]}

Example input:
Sentence: In this report we describe the case of a 37-year-old white woman with Ebstein 's anomaly , who developed a rare syndrome called platypnea-orthodeoxia , characterized by massive right-to-left interatrial shunting with transient profound hypoxia and cyanosis .

Example answer:
{"entities": [{"text": "Ebstein 's anomaly", "type": "Disease"}, {"text": "platypnea-orthodeoxia", "type": "Disease"}, {"text": "hypoxia", "type": "Disease"}, {"text": "cyanosis", "type": "Disease"}]}

Example input:
Sentence: CASE DESCRIPTION : A 30-year-old Caucasian woman presented with dental pain , bad breath , and self-reported poor esthetics .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "bad breath", "type": "Disease"}]}

Example input:
Sentence: Intracranial aneurysms or arteriovenous malformations were present in 17 of 32 patients studied angiographically or at autopsy ; cerebral vasculitis was present in two patients .

Example answer:
{"entities": [{"text": "Intracranial aneurysms", "type": "Disease"}, {"text": "arteriovenous malformations", "type": "Disease"}, {"text": "cerebral vasculitis", "type": "Disease"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: We report the case of a 63-year-old female who was treated with methylphenidate due to hyperactivity and suffered from multiple ischaemic strokes .

Example answer:
{"entities": [{"text": "methylphenidate", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "ischaemic strokes", "type": "Disease"}]}

Example input:
Sentence: We describe a 25-year-old woman with pre-existing mitral valve prolapse who developed intractable ventricular fibrillation after consuming a `` natural energy '' guarana health drink containing a high concentration of caffeine .

Example answer:
{"entities": [{"text": "mitral valve prolapse", "type": "Disease"}, {"text": "ventricular fibrillation", "type": "Disease"}, {"text": "caffeine", "type": "Chemical"}]}

Example input:
Sentence: We present a 43-year-old man who developed a coronary aneurysm in the right coronary artery 6 months after receiving a paclitaxel-eluting stent .

Example answer:
{"entities": [{"text": "coronary aneurysm", "type": "Disease"}, {"text": "paclitaxel-eluting", "type": "Chemical"}]}

Example input:
Sentence: A case is reported of the hemolytic uremic syndrome ( HUS ) in a woman taking oral contraceptives .

Example answer:
{"entities": [{"text": "hemolytic uremic syndrome", "type": "Disease"}, {"text": "HUS", "type": "Disease"}, {"text": "oral contraceptives", "type": "Chemical"}]}

Input:
Sentence: A case of nontraumatic dissecting aneurysm of the basilar artery in association with hypertension , smoke , and oral contraceptives is reported in a young female patient with a locked-in syndrome .

## Item bc5cdr:test:1592
Example input:
Sentence: These studies suggest that both phenacetin and acetaminophen may contribute to the burden of ESRD , with the risk of the latter being somewhat less than that of the former .

Example answer:
{"entities": [{"text": "phenacetin", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: In patients with diabetes , SCr increases > or = 0.5 mg/dL were 5.1 % ( 4 of 78 patients ) with iopamidol and 13.0 % ( 12 of 92 patients ) with iodixanol ( P=0.11 ) , whereas SCr increases > or = 25 % were 10.3 % and 15.2 % , respectively ( P=0.37 ) .

Example answer:
{"entities": [{"text": "diabetes", "type": "Disease"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}]}

Example input:
Sentence: SCr increases > or = 0.5 mg/dL occurred in 4.4 % ( 9 of 204 patients ) after iopamidol and 6.7 % ( 14 of 210 patients ) after iodixanol ( P=0.39 ) , whereas rates of SCr increases > or = 25 % were 9.8 % and 12.4 % , respectively ( P=0.44 ) .

Example answer:
{"entities": [{"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}]}

Example input:
Sentence: Mean post-SCr increases were significantly less with iopamidol ( all patients : 0.07 versus 0.12 mg/dL , 6.2 versus 10.6 micromol/L , P=0.03 ; patients with diabetes : 0.07 versus 0.16 mg/dL , 6.2 versus 14.1 micromol/L , P=0.01 ) .

Example answer:
{"entities": [{"text": "iopamidol", "type": "Chemical"}, {"text": "diabetes", "type": "Disease"}]}

Example input:
Sentence: Using as the reference group women who were not using oral contraception , had no recent pregnancy or menopausal symptoms , the case-control analysis gave an adjusted odds ratio ( OR ( adj ) ) of 7.44 ( 95 % CI 3.67-15.08 ) for CPA/EE use compared with an OR ( adj ) of 2.58 ( 95 % CI 1.60-4.18 ) for use of conventional COCs .

Example answer:
{"entities": [{"text": "CPA/EE", "type": "Chemical"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: The adjusted odds ratio was 2.5 ( 95 percent confidence interval , 1.5 to 4.1 ) among women who used second-generation oral contraceptives and 1.3 ( 95 percent confidence interval , 0.7 to 2.5 ) among those who used third-generation oral contraceptives .

Example answer:
{"entities": [{"text": "oral contraceptives", "type": "Chemical"}]}

Example input:
Sentence: We investigated this association , according to the type of progestagen included in third-generation ( i.e. , desogestrel or gestodene ) and second-generation ( i.e. , levonorgestrel ) oral contraceptives , the dose of estrogen , and the presence or absence of prothrombotic mutations METHODS : In a nationwide , population-based , case-control study , we identified and enrolled 248 women 18 through 49 years of age who had had a first myocardial infarction between 1990 and 1995 and 925 control women who had not had a myocardial infarction and who were matched for age , calendar year of the index event , and area of residence .

Example answer:
{"entities": [{"text": "progestagen", "type": "Chemical"}, {"text": "desogestrel", "type": "Chemical"}, {"text": "gestodene", "type": "Chemical"}, {"text": "levonorgestrel", "type": "Chemical"}, {"text": "oral contraceptives", "type": "Chemical"}, {"text": "estrogen", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Among women who used oral contraceptives , the odds ratio was 2.1 ( 95 percent confidence interval , 1.5 to 3.0 ) for those without a prothrombotic mutation and 1.9 ( 95 percent confidence interval , 0.6 to 5.5 ) for those with a mutation CONCLUSIONS : The risk of myocardial infarction was increased among women who used second-generation oral contraceptives .

Example answer:
{"entities": [{"text": "oral contraceptives", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Input:
Sentence: The increased odds ratio associated with products containing 20 micrograms ethinyloestradiol and desogestrel compared with the 30 micrograms product is biologically implausible , and is likely to be the result of preferential prescribing and , thus , confounding .

## Item bc5cdr:test:1596
Example input:
Sentence: In this study , the severity of response to other seizure-inducing agents was tested in mice 1 and 24 h after intraperitoneal administration of 80 mg/kg gamma-HCH .

Example answer:
{"entities": [{"text": "seizure-inducing", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}]}

Example input:
Sentence: Investigation of mitochondrial involvement in the experimental model of epilepsy induced by pilocarpine .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: Three hundred fifty-five adult male CSS mice , 58 B6 , and 39 A/J were tested for susceptibility to pilocarpine-induced seizures .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Pretreatment with either VPU ( 50 and 100 mg/kg ) or VPA ( 300 and 600 mg/kg ) completely abolished pilocarpine-evoked increases in extracellular glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-evoked", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: Therefore , like VPA , the finding that VPU could drastically reduce pilocarpine-induced increases in glutamate and aspartate should account , at least partly , for its anticonvulsant activity observed in pilocarpine-induced seizure in experimental animals .

Example answer:
{"entities": [{"text": "VPA", "type": "Chemical"}, {"text": "VPU", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Similar to rats , systemic pilocarpine injection causes status epilepticus ( SE ) and the eventual development of spontaneous seizures and mossy fiber sprouting in C57BL/6 and CD1 mice , but the physiological correlates of these events have not been identified in mice .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: VPU was more potent than VPA , exhibiting the median effective dose ( ED ( 50 ) ) of 49 mg/kg in protecting rats against pilocarpine-induced seizure whereas the corresponding value for VPA was 322 mg/kg .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Based on the finding that VPU and VPA could protect the animals against pilocarpine-induced seizure it is suggested that the reduction of inhibitory amino acid neurotransmitters was comparatively minor and offset by a pronounced reduction of glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Input:
Sentence: Intraperitoneal injection of pilocarpine ( 400 mg/kg ) induced tonic and clonic seizure .

## Item bc5cdr:test:1736
Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: Secondary outcomes were a postdose SCr increase > or = 25 % , a postdose estimated glomerular filtration rate decrease of > or = 25 % , and the mean peak change in SCr .

Example answer:
{"entities": []}

Example input:
Sentence: In the present study , we investigated the changes occurring at the protein level in striatal samples obtained from the unilaterally 6-hydroxydopamine-lesion rat model of PD treated with saline , L-DOPA or bromocriptine using two-dimensional difference gel electrophoresis and mass spectrometry ( MS ) .

Example answer:
{"entities": [{"text": "6-hydroxydopamine-lesion", "type": "Chemical"}, {"text": "PD", "type": "Disease"}, {"text": "L-DOPA", "type": "Chemical"}, {"text": "bromocriptine", "type": "Chemical"}]}

Example input:
Sentence: In a placebo-controlled , single-blinded , crossover study , we assessed the effect of `` real '' repetitive transcranial magnetic stimulation ( rTMS ) versus `` sham '' rTMS ( placebo ) on peak dose dyskinesias in patients with Parkinson 's disease ( PD ) .

Example answer:
{"entities": [{"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: Decompression and neurolysis were performed with good subsequent recovery of function .

Example answer:
{"entities": []}

Example input:
Sentence: Postoperatively , the patient refused DC cardioversion and was treated medically .

Example answer:
{"entities": []}

Example input:
Sentence: Preoperative assessment should focus on cardiovascular status and serum potassium level .

Example answer:
{"entities": [{"text": "potassium", "type": "Chemical"}]}

Example input:
Sentence: Compared with control patients , CRF and ESRD patients had higher preoperative serum creatinine levels , a greater percentage of patients with hepatorenal syndrome , higher percentage requirement for dialysis in the first 3 months postoperatively , and a higher 1-year serum creatinine .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "hepatorenal syndrome", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : The United Kingdom Parkinson 's Disease Research Group ( UKPDRG ) trial found an increased mortality in patients with Parkinson 's disease ( PD ) randomized to receive 10 mg selegiline per day and L-dopa compared with those taking L-dopa alone .

Example answer:
{"entities": [{"text": "Parkinson 's Disease", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "selegiline", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}]}

Example input:
Sentence: Multivariate stepwise logistic regression analysis using preoperative and postoperative variables identified that an increase of serum creatinine compared with average at 1 year , 3 months , and 4 weeks postoperatively were independent risk factors for the development of CRF or ESRD with odds ratios of 2.6 , 2.2 , and 1.6 , respectively .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Input:
Sentence: Clinical assessment as well as blinded ratings of Unified Parkinson 's Disease Rating Scale ( UPDRS ) scores were carried out pre- and postoperatively .

## Item bc5cdr:test:1738
Example input:
Sentence: Although preclinical and clinical findings suggest pulsatile stimulation of striatal postsynaptic receptors as a key mechanism underlying levodopa-induced dyskinesias , their pathogenesis is still unclear .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: There was a significant 40 % improvement in the dyskinesia score without increase of parkinsonian motor disability .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}, {"text": "parkinsonian", "type": "Disease"}, {"text": "motor disability", "type": "Disease"}]}

Example input:
Sentence: Repetitive transcranial magnetic stimulation for levodopa-induced dyskinesias in Parkinson 's disease .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: However , comparison with the baseline showed small but significant reduction in dyskinesia severity following real rTMS but not placebo .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Seven patients suffering from Parkinson 's disease ( PD ) with severely disabling dyskinesia received low-dose propranolol as an adjunct to the currently used medical treatment .

Example answer:
{"entities": [{"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "propranolol", "type": "Chemical"}]}

Example input:
Sentence: In a placebo-controlled , single-blinded , crossover study , we assessed the effect of `` real '' repetitive transcranial magnetic stimulation ( rTMS ) versus `` sham '' rTMS ( placebo ) on peak dose dyskinesias in patients with Parkinson 's disease ( PD ) .

Example answer:
{"entities": [{"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: Similarly , in patient diaries , although both treatments caused reduction in subjective dyskinesia scores during the days of intervention , the effect was sustained for 3 days after the intervention for the real rTMS only .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Ballistic and choreic dyskinesia were markedly ameliorated , whereas dystonia was not .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}, {"text": "dystonia", "type": "Disease"}]}

Example input:
Sentence: The results suggest the existence of residual beneficial clinical aftereffects of consecutive daily applications of low-frequency rTMS on dyskinesias in PD .

Example answer:
{"entities": [{"text": "dyskinesias", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: Ten patients with PD and prominent dyskinesias had rTMS ( 1,800 pulses ; 1 Hz rate ) delivered over the motor cortex for 4 consecutive days twice , once real stimuli and once sham stimulation were used ; evaluations were done at the baseline and 1 day after the end of each of the treatment series .

Example answer:
{"entities": [{"text": "PD", "type": "Disease"}, {"text": "dyskinesias", "type": "Disease"}]}

Input:
Sentence: 85 percent of patients with dyskinesias were relieved of symptoms , regardless of whether the pallidotomies were performed with the Gamma Knife or radiofrequency methods .

## Item bc5cdr:test:1742
Example input:
Sentence: Drug-induced parkinsonism was observed in subjects treated with risperidone ( 42 % ) and haloperidol ( 29 % ) and was observed at occupancy levels above 60 % .

Example answer:
{"entities": [{"text": "Drug-induced parkinsonism", "type": "Disease"}, {"text": "risperidone", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Repetitive transcranial magnetic stimulation for levodopa-induced dyskinesias in Parkinson 's disease .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: Ten patients with PD and prominent dyskinesias had rTMS ( 1,800 pulses ; 1 Hz rate ) delivered over the motor cortex for 4 consecutive days twice , once real stimuli and once sham stimulation were used ; evaluations were done at the baseline and 1 day after the end of each of the treatment series .

Example answer:
{"entities": [{"text": "PD", "type": "Disease"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: in the rat haloperidol-induced catalepsy model for Parkinson 's disease .

Example answer:
{"entities": [{"text": "haloperidol-induced", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: Seven patients suffering from Parkinson 's disease ( PD ) with severely disabling dyskinesia received low-dose propranolol as an adjunct to the currently used medical treatment .

Example answer:
{"entities": [{"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "propranolol", "type": "Chemical"}]}

Example input:
Sentence: The present study aimed to investigate the effects of pallidal neurotensin on haloperidol-induced parkinsonian symptoms .

Example answer:
{"entities": [{"text": "neurotensin", "type": "Chemical"}, {"text": "haloperidol-induced", "type": "Chemical"}, {"text": "parkinsonian symptoms", "type": "Disease"}]}

Example input:
Sentence: Effects of pallidal neurotensin on haloperidol-induced parkinsonian catalepsy : behavioral and electrophysiological studies .

Example answer:
{"entities": [{"text": "neurotensin", "type": "Chemical"}, {"text": "haloperidol-induced", "type": "Chemical"}, {"text": "parkinsonian catalepsy", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : The United Kingdom Parkinson 's Disease Research Group ( UKPDRG ) trial found an increased mortality in patients with Parkinson 's disease ( PD ) randomized to receive 10 mg selegiline per day and L-dopa compared with those taking L-dopa alone .

Example answer:
{"entities": [{"text": "Parkinson 's Disease", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "selegiline", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}]}

Example input:
Sentence: In a placebo-controlled , single-blinded , crossover study , we assessed the effect of `` real '' repetitive transcranial magnetic stimulation ( rTMS ) versus `` sham '' rTMS ( placebo ) on peak dose dyskinesias in patients with Parkinson 's disease ( PD ) .

Example answer:
{"entities": [{"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Bilateral infusions of neurotensin into the globus pallidus reversed haloperidol-induced parkinsonian catalepsy in rats .

Example answer:
{"entities": [{"text": "neurotensin", "type": "Chemical"}, {"text": "haloperidol-induced", "type": "Chemical"}, {"text": "parkinsonian catalepsy", "type": "Disease"}]}

Input:
Sentence: Gamma Knife pallidotomy is as effective as radiofrequency pallidotomy in controlling certain of the symptoms of Parkinson 's disease .

## Item bc5cdr:test:1506
Example input:
Sentence: These data indicate that a critical percentage of NTE inhibition in brain and spinal cord sampled shortly after Mipafox exposure can predict neuropathic damage in rats several weeks later .

Example answer:
{"entities": [{"text": "Mipafox", "type": "Chemical"}, {"text": "neuropathic damage", "type": "Disease"}]}

Example input:
Sentence: Responses of urinary strip preparations from control and cyclophosphamide-pretreated rats to electrical field stimulation and to agonists were assessed in the absence and presence of muscarinic , adrenergic and purinergic receptor antagonists .

Example answer:
{"entities": [{"text": "cyclophosphamide-pretreated", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Immunofluorescence staining with the MRP2 antibody was found to label a high number of microvessels throughout the brain in normal Wistar rats , whereas such labeling was absent in TR ( - ) rats .

Example answer:
{"entities": []}

Example input:
Sentence: In streptozotocin-induced hyperalgesia , inducible NO synthase participates in pronociceptive activity of bradykinin , whereas in vincristine-induced hyperalgesia bradykinin seemed to activate neuronal NO synthase pathway .

Example answer:
{"entities": [{"text": "streptozotocin-induced", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "NO", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}, {"text": "vincristine-induced", "type": "Chemical"}]}

Example input:
Sentence: In control rats , immunostaining for 7H6 and ZO-1 colocalized to outline bile canaliculi in a continuous fashion .

Example answer:
{"entities": []}

Example input:
Sentence: In cyclophosphamide-induced cystitis in the rat , detrusor function is impaired and the expression and effects of muscarinic receptors altered .

Example answer:
{"entities": [{"text": "cyclophosphamide-induced", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Example input:
Sentence: Electron microscopical immunohistochemistry revealed positive reaction products noted on the secretory granules , Golgi cisternae , and endoplasmic reticulum of the untreated rat prolactinoma cells .

Example answer:
{"entities": [{"text": "prolactinoma", "type": "Disease"}]}

Example input:
Sentence: In vitro characterization of parasympathetic and sympathetic responses in cyclophosphamide-induced cystitis in the rat .

Example answer:
{"entities": [{"text": "cyclophosphamide-induced", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Example input:
Sentence: Noxious chemical stimulation of rat facial mucosa increases intracranial blood flow through a trigemino-parasympathetic reflex -- an experimental model for vascular dysfunctions in cluster headache .

Example answer:
{"entities": [{"text": "vascular dysfunctions", "type": "Disease"}, {"text": "cluster headache", "type": "Disease"}]}

Example input:
Sentence: An experimental model was developed in the rat to measure changes in lacrimation and intracranial blood flow following noxious chemical stimulation of facial mucosa .

Example answer:
{"entities": []}

Input:
Sentence: Immunocytochemical techniques were used to examine alterations in the expression of neuronal nitric oxide synthase ( NOS ) in bladder pathways following acute and chronic irritation of the urinary tract of the rat .
