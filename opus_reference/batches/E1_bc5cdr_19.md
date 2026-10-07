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

## Item bc5cdr:test:3311
Example input:
Sentence: This case report highlights the fact that the angiotensin II receptor antagonist losartan can cause serious unexpected complications in patients with renovascular disease and should be used with extreme caution in this setting .

Example answer:
{"entities": [{"text": "angiotensin II", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "renovascular disease", "type": "Disease"}]}

Example input:
Sentence: We propose that amphotericin , in the setting of reduced effective arterial volume , may activate tubuloglomerular feedback , thereby contributing to acute renal failure .

Example answer:
{"entities": [{"text": "amphotericin", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: ACE inhibitor and angiotensin-releasing blocker ( ARB ) therapy reduced proteinuria development .

Example answer:
{"entities": [{"text": "ACE inhibitor", "type": "Chemical"}, {"text": "angiotensin-releasing blocker", "type": "Chemical"}, {"text": "ARB", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: Massive proteinuria and acute renal failure after oral bisphosphonate ( alendronate ) administration in a patient with focal segmental glomerulosclerosis .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "bisphosphonate", "type": "Chemical"}, {"text": "alendronate", "type": "Chemical"}, {"text": "focal segmental glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: One week later , by mistake , losartan was prescribed again and after the second dose of 50 mg , the patient developed a second episode of transient anuria lasting 10 hours .

Example answer:
{"entities": [{"text": "losartan", "type": "Chemical"}, {"text": "anuria", "type": "Disease"}]}

Example input:
Sentence: Repeated transient anuria following losartan administration in a patient with a solitary kidney .

Example answer:
{"entities": [{"text": "anuria", "type": "Disease"}, {"text": "losartan", "type": "Chemical"}]}

Example input:
Sentence: Surprisingly , the first dose of 50 mg of losartan resulted in a sudden anuria , which lasted eight hours despite high-dose furosemide and amine infusion .

Example answer:
{"entities": [{"text": "losartan", "type": "Chemical"}, {"text": "anuria", "type": "Disease"}, {"text": "furosemide", "type": "Chemical"}, {"text": "amine", "type": "Chemical"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: Under such conditions , angiotensin II receptor blockade by losartan probably induced a critical fall in glomerular filtration pressure .

Example answer:
{"entities": [{"text": "angiotensin II", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}]}

Example input:
Sentence: We report the case of a 70-year-old hypertensive man with a solitary kidney and chronic renal insufficiency who developed two episodes of transient anuria after losartan administration .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}, {"text": "chronic renal insufficiency", "type": "Disease"}, {"text": "anuria", "type": "Disease"}, {"text": "losartan", "type": "Chemical"}]}

Input:
Sentence: Prolonged treatment with losartan showed further reduction of glomerulosclerosis associated with reduced progression of tubular atrophy and interstitial fibrosis , thus preventing heavy proteinuria and chronic renal failure .

## Item bc5cdr:test:3916
Example input:
Sentence: Treatment duration longer than 1 year was associated with an eightfold increased risk ( OR = 7.7 , 95 % CI 0.9 to 69 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 1 patient with squamous cell carcinoma achieved a partial response lasting 5 months .

Example answer:
{"entities": [{"text": "squamous cell carcinoma", "type": "Disease"}]}

Example input:
Sentence: The median duration of survival in the 12 patients was 54 weeks ( range 21 to more than 156 weeks ) , with an 18-month survival rate of 42 % .

Example answer:
{"entities": []}

Example input:
Sentence: Eleven patients ( six male ) with median age 47 years ( range 27-73 ) , median disease duration 50 months ( range 9-178 ) and median follow-up period of patients 13.8 months ( range 5-27 ) were enrolled in this study .

Example answer:
{"entities": []}

Example input:
Sentence: Seventeen of these had a response or were stable for a median of 20 weeks ( range 6 to more than 66 weeks ) .

Example answer:
{"entities": []}

Example input:
Sentence: After a median follow-up of 22 months , the median progression free survival rate was 7 months , and the median survival time was 16 months .

Example answer:
{"entities": []}

Example input:
Sentence: The median time to progression was 16 weeks and the 1-year survival rate was 33 % .

Example answer:
{"entities": []}

Example input:
Sentence: One of 16 patients ( 6 % ) with prior chemotherapy had a complete response ( CR ) of 31 weeks ' duration ( 95 % CI , 0 % to 30 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: In the nine responders , median duration of chemotherapy response from the time of operation was 25 weeks ( range 12 to more than 91 weeks ) .

Example answer:
{"entities": []}

Example input:
Sentence: The median duration of response was 21 weeks ( range , 17 to 28 ) .

Example answer:
{"entities": []}

Input:
Sentence: Median duration of response was 34.4 months , and it was higher in patients who received RD until progression ( not reached versus 19 months , p < 0.001 ) .

## Item bc5cdr:test:3882
Example input:
Sentence: CONCLUSIONS : The rate of contrast-induced nephropathy , defined by multiple end points , is not statistically different after the intraarterial administration of iopamidol or iodixanol to high-risk patients , with or without diabetes mellitus .

Example answer:
{"entities": [{"text": "nephropathy", "type": "Disease"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}, {"text": "diabetes mellitus", "type": "Disease"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Long-term use and concomitant use of more than one BZD/RD were common in elderly patients hospitalised because of acute illnesses .

Example answer:
{"entities": []}

Example input:
Sentence: SCr increases > or = 0.5 mg/dL occurred in 4.4 % ( 9 of 204 patients ) after iopamidol and 6.7 % ( 14 of 210 patients ) after iodixanol ( P=0.39 ) , whereas rates of SCr increases > or = 25 % were 9.8 % and 12.4 % , respectively ( P=0.44 ) .

Example answer:
{"entities": [{"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}]}

Example input:
Sentence: Tacrolimus , MMF , and steroids were given as immunosuppressant .

Example answer:
{"entities": [{"text": "Tacrolimus", "type": "Chemical"}, {"text": "MMF", "type": "Chemical"}, {"text": "steroids", "type": "Chemical"}]}

Example input:
Sentence: Thirty male Sprague-Dawley rats were divided randomly into four treatment groups : saline , dexamethasone ( dex ) , allopurinol plus saline , and allopurinol plus dex .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "dex", "type": "Chemical"}, {"text": "allopurinol", "type": "Chemical"}]}

Example input:
Sentence: In patients with diabetes , SCr increases > or = 0.5 mg/dL were 5.1 % ( 4 of 78 patients ) with iopamidol and 13.0 % ( 12 of 92 patients ) with iodixanol ( P=0.11 ) , whereas SCr increases > or = 25 % were 10.3 % and 15.2 % , respectively ( P=0.37 ) .

Example answer:
{"entities": [{"text": "diabetes", "type": "Disease"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}]}

Example input:
Sentence: A Phase I study of intravenous ( IV ) bolus 4'-0-tetrahydropyranyladriamycin ( Pirarubicin ) was done in 55 patients in good performance status with refractory tumors .

Example answer:
{"entities": [{"text": "4'-0-tetrahydropyranyladriamycin", "type": "Chemical"}, {"text": "Pirarubicin", "type": "Chemical"}, {"text": "tumors", "type": "Disease"}]}

Example input:
Sentence: Two weeks after the initiation of therapy , her hematocrit had decreased from 44.1 % to 20.4 % , and she had a positive direct Coombs antiglobulin test and an elevated indirect bilirubin .

Example answer:
{"entities": [{"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: From June 2004 to October 2006 , 11 HBs Ag positive patients with rheumatologic diseases , who were on both immunosuppressive and prophylactic lamivudine therapies , were retrospectively assessed .

Example answer:
{"entities": [{"text": "HBs Ag", "type": "Chemical"}, {"text": "rheumatologic diseases", "type": "Disease"}, {"text": "lamivudine", "type": "Chemical"}]}

Input:
Sentence: Eighty-seven percent of the patients had received immunomodulatory drugs included in some line of therapy before bort-dex .

## Item bc5cdr:test:3635
Example input:
Sentence: RESULTS : Sensitivity to several convulsion endpoints induced by nicotine , carbachol , and neostigmine were significantly greater in WSR versus WSP mice .

Example answer:
{"entities": [{"text": "convulsion", "type": "Disease"}, {"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}]}

Example input:
Sentence: The present study was aimed at investigating the effects of Daucus carota seeds on cognitive functions , total serum cholesterol levels and brain cholinesterase activity in mice .

Example answer:
{"entities": [{"text": "cholesterol", "type": "Chemical"}]}

Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: Curcumin ameliorates cognitive dysfunction and oxidative damage in phenobarbitone and carbamazepine administered rats .

Example answer:
{"entities": [{"text": "Curcumin", "type": "Chemical"}, {"text": "cognitive dysfunction", "type": "Disease"}, {"text": "phenobarbitone", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}]}

Example input:
Sentence: Therefore , the present study was carried out to investigate the effect of chronic curcumin administration on phenobarbitone- and carbamazepine-induced cognitive impairment and oxidative stress in rats .

Example answer:
{"entities": [{"text": "curcumin", "type": "Chemical"}, {"text": "phenobarbitone-", "type": "Chemical"}, {"text": "carbamazepine-induced", "type": "Chemical"}, {"text": "cognitive impairment", "type": "Disease"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "Disease"}, {"text": "METH", "type": "Chemical"}, {"text": "MPTP", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "METH-induced", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Clomipramine exposure in immature rats produced significant behavioral and biochemical changes that include enhanced anxiety ( elevated plus maze and marble burying ) , behavioral inflexibility ( perseveration in the spontaneous alternation task and impaired reversal learning ) , working memory impairment ( e.g. , win-shift paradigm ) , hoarding , and corticostriatal dysfunction .

Example answer:
{"entities": [{"text": "Clomipramine", "type": "Chemical"}, {"text": "anxiety", "type": "Disease"}, {"text": "behavioral inflexibility", "type": "Disease"}, {"text": "memory impairment", "type": "Disease"}, {"text": "hoarding", "type": "Disease"}, {"text": "corticostriatal dysfunction", "type": "Disease"}]}

Example input:
Sentence: Maltolyl p-coumarate was found to attenuate cognitive deficits in both rat models using passive avoidance test and to reduce apoptotic cell death observed in the hippocampus of the amyloid beta peptide ( 1-42 ) -infused rats .

Example answer:
{"entities": [{"text": "Maltolyl p-coumarate", "type": "Chemical"}, {"text": "cognitive deficits", "type": "Disease"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}]}

Example input:
Sentence: In the present study , we investigated whether maltolyl p-coumarate could improve cognitive decline in scopolamine-injected rats and in amyloid beta peptide ( 1-42 ) -infused rats .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "cognitive decline", "type": "Disease"}, {"text": "scopolamine-injected", "type": "Chemical"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}]}

Input:
Sentence: The present study aimed to explore the effect of MT induction on carmustine ( BCNU ) -induced hippocampal cognitive dysfunction in rats .

## Item bc5cdr:test:3724
Example input:
Sentence: Five females and 6 males , 21-59 years of age , were examined with a 1.5-T whole-body system using a circular polarized head coil .

Example answer:
{"entities": []}

Example input:
Sentence: We describe a case of transient neurological deficit that occurred after unilateral spinal anaesthesia with 8 mg of 1 % hyperbaric bupivacaine slowly injected through a 25-gauge pencil-point spinal needle .

Example answer:
{"entities": [{"text": "neurological deficit", "type": "Disease"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: We report an undiagnosed case of myotonia congenita in a 24-year-old previously healthy primigravida , who developed life threatening masseter spasm following a standard dose of intravenous suxamethonium for induction of anaesthesia .

Example answer:
{"entities": [{"text": "myotonia congenita", "type": "Disease"}, {"text": "masseter spasm", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: A 49-year-old woman was transferred to our department because of quadriparesis , lancinating pain , sensory loss , and paresthesia of the distal limbs .

Example answer:
{"entities": [{"text": "quadriparesis", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "sensory loss", "type": "Disease"}, {"text": "paresthesia", "type": "Disease"}]}

Example input:
Sentence: A 54-year-old hypothyroid male taking thyroxine and simvastatin presented with bilateral leg compartment syndrome and myonecrosis .

Example answer:
{"entities": [{"text": "hypothyroid", "type": "Disease"}, {"text": "thyroxine", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "compartment syndrome", "type": "Disease"}, {"text": "myonecrosis", "type": "Disease"}]}

Example input:
Sentence: Of the 20 animals that received subarachnoid injection of 2-chloroprocaine-CE seven ( 35 % ) developed hind-limb paralysis .

Example answer:
{"entities": [{"text": "2-chloroprocaine-CE", "type": "Chemical"}, {"text": "paralysis", "type": "Disease"}]}

Example input:
Sentence: Reports of persistent paralysis after the discontinuance of these drugs have most often involved aminosteroid-based NMBAs such as vecuronium bromide , especially when used in conjunction with corticosteroids .

Example answer:
{"entities": [{"text": "paralysis", "type": "Disease"}, {"text": "vecuronium bromide", "type": "Chemical"}]}

Example input:
Sentence: We report a case of a 31 year old female who required admission to the Intensive Care Unit for ventilation and full supportive therapy , following ingestion of 13.5g bupropion .

Example answer:
{"entities": [{"text": "bupropion", "type": "Chemical"}]}

Example input:
Sentence: None of the animals that received bupivacaine , normal saline , or normal saline titrated to a pH 3.0 developed hind-limb paralysis .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}, {"text": "paralysis", "type": "Disease"}]}

Input:
Sentence: For patients with bilateral abductor paralysis , age , sex , paralytic Botox dose , prior Botox dose , and course following paralysis were noted .

## Item bc5cdr:test:3883
Example input:
Sentence: Total cumulative doses were 36 or 60 g/m2 of ifosfamide ( six or 10 cycles of ifosfamide , vincristine , and dactinomycin [ IVA ] ) .

Example answer:
{"entities": [{"text": "ifosfamide", "type": "Chemical"}, {"text": "ifosfamide , vincristine , and dactinomycin", "type": "Chemical"}, {"text": "IVA", "type": "Chemical"}]}

Example input:
Sentence: Median number of courses of MFL regimen given was six and the median cumulative dose of mitoxantrone was 68.35 mg/m2 .

Example answer:
{"entities": [{"text": "MFL regimen", "type": "Chemical"}, {"text": "mitoxantrone", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Thirty-five Wistar rats were given 1.5 mg/kg DOX , i.v. , weekly for up to 8 weeks for a total cumulative dose of 12 mg/kg BW .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Long-term use and concomitant use of more than one BZD/RD were common in elderly patients hospitalised because of acute illnesses .

Example answer:
{"entities": []}

Example input:
Sentence: A median of 2 cycles of therapy was administered to the 37 eligible patients .

Example answer:
{"entities": []}

Example input:
Sentence: Two or three BZDs/RDs were concomitantly taken by 26 % of users ( n = 20 ) .

Example answer:
{"entities": [{"text": "BZDs/RDs", "type": "Chemical"}]}

Example input:
Sentence: Dex increased SBP ( 110 +/- 2-126 +/- 3 mmHg ; P < 0.001 ) and decreased thymus ( P < 0.001 ) and bodyweights ( P '' < 0.01 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}, {"text": "increased SBP", "type": "Disease"}, {"text": "decreased thymus ( P < 0.001 ) and bodyweights", "type": "Disease"}]}

Example input:
Sentence: In the bolus group , 26.0 % ( 13/50 ) had akathisia compared with 32.7 % ( 16/49 ) in the infusion group ( Delta=-6.7 % ; 95 % confidence interval [ CI ] -24.6 % to 11.2 % ) .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}, {"text": "Dex", "type": "Chemical"}]}

Input:
Sentence: The median number of bort-dex cycles was 6 , up to a maximum of 12 cycles .

## Item bc5cdr:test:3981
Example input:
Sentence: Twenty-six had minimal prior therapy ( good risk ) , 23 had extensive prior therapy ( poor risk ) , and six had renal and/or hepatic dysfunction .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Sixty percent in Group A developed postoperative emetic symptoms , headache , or both ; 1 patient in Group B developed symptoms .

Example answer:
{"entities": [{"text": "postoperative emetic symptoms", "type": "Disease"}, {"text": "headache", "type": "Disease"}]}

Example input:
Sentence: However , an increase of serum creatinine at various times postoperatively is more predictive of the development of CRF or ESRD .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Compared with control patients , CRF and ESRD patients had higher preoperative serum creatinine levels , a greater percentage of patients with hepatorenal syndrome , higher percentage requirement for dialysis in the first 3 months postoperatively , and a higher 1-year serum creatinine .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "hepatorenal syndrome", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Delirium was found in 10 % of clozapine-treated inpatients , particularly in older patients exposed to other central anticholinergics .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}, {"text": "clozapine-treated", "type": "Chemical"}]}

Example input:
Sentence: Delirium was inconsistently recognized clinically in milder cases and was associated with increased length-of-stay and higher costs , and inferior clinical outcome .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}]}

Example input:
Sentence: Delirium during clozapine treatment : incidence and associated risk factors .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}]}

Example input:
Sentence: Delirium was diagnosed in 14 ( 10.1 % incidence , or 1.48 cases/person-years of exposure ) ; 71.4 % of cases were moderate or severe .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Incidence and risk factors for delirium during clozapine treatment require further clarification .

Example answer:
{"entities": [{"text": "delirium", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}]}

Example input:
Sentence: Multivariate stepwise logistic regression analysis using preoperative and postoperative variables identified that an increase of serum creatinine compared with average at 1 year , 3 months , and 4 weeks postoperatively were independent risk factors for the development of CRF or ESRD with odds ratios of 2.6 , 2.2 , and 1.6 , respectively .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Input:
Sentence: Early postoperative delirium incidence risk factors were then assessed through three different multiple regression models .

## Item bc5cdr:test:3725
Example input:
Sentence: The drug was withdrawn on presentation to hospital in 11 patients , with rapid clinical improvement in 9 .

Example answer:
{"entities": []}

Example input:
Sentence: METHOD : In a 16-week multicenter , double-blind trial , 122 children with ADHD were randomly assigned to clonidine ( n = 31 ) , methylphenidate ( n = 29 ) , clonidine and methylphenidate ( n = 32 ) , or placebo ( n = 30 ) .

Example answer:
{"entities": [{"text": "ADHD", "type": "Disease"}, {"text": "clonidine", "type": "Chemical"}, {"text": "methylphenidate", "type": "Chemical"}]}

Example input:
Sentence: Prolactin results were compared with those of a previous personal cohort of 1,340 patients with erectile dysfunction and systematic prolactin determination .

Example answer:
{"entities": [{"text": "erectile dysfunction", "type": "Disease"}]}

Example input:
Sentence: All the patients were skin test negative to BPO ; 49 of 51 ( 96 % ) were also negative to MDM , and 44 of 46 ( 96 % ) to PG .

Example answer:
{"entities": [{"text": "BPO", "type": "Chemical"}, {"text": "MDM", "type": "Disease"}, {"text": "PG", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Two hundred sixty-five patients were included in this analysis ( n=92 , 93 , and 80 for placebo , low dose , and high dose , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: A total of sixty patients were trated with bromperidol first in open conditions ( 20 patients ) , then on a double blind basis ( 40 patients ) with haloperidol as the reference substance .

Example answer:
{"entities": [{"text": "bromperidol", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: During an 18-month period of study 41 hemodialyzed patients receiving desferrioxamine ( 10-40 mg/kg BW/3 times weekly ) for the first time were monitored for detection of audiovisual toxicity .

Example answer:
{"entities": [{"text": "desferrioxamine", "type": "Chemical"}, {"text": "audiovisual toxicity", "type": "Disease"}]}

Example input:
Sentence: RAST was positive for AX in 22 patients ( 41 % ) and to BPO in just 5 ( 9 % ) .

Example answer:
{"entities": [{"text": "AX", "type": "Chemical"}, {"text": "BPO", "type": "Chemical"}]}

Example input:
Sentence: From January 1986 to January 2009 , 1223 consecutive ALF patients were evaluated : ATT alone was the cause in 70 ( 5.7 % ) patients .

Example answer:
{"entities": [{"text": "ALF", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Nine hundred one patients were randomized to treatment , 447 who received the lozenge and 454 who received the gum ( safety population ) .

Example answer:
{"entities": []}

Input:
Sentence: RESULTS : From a database of 452 patients receiving Botox , 352 patients had been diagnosed with ADSD .

## Item bc5cdr:test:3972
Example input:
Sentence: Patients who developed renal insufficiency had lower baseline body weight and higher baseline serum creatinine , required higher doses of loop diuretics , and were more likely to be treated with thiazide diuretics than controls .

Example answer:
{"entities": [{"text": "renal insufficiency", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "thiazide", "type": "Chemical"}]}

Example input:
Sentence: The serum creatinine levels of patients in the mild-type chronic FK506 nephropathy group , which included 7 episode biopsies , were statistically higher than those in the minimum-type chronic FK506-nephropathy group ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "FK506-nephropathy", "type": "Chemical"}]}

Example input:
Sentence: These 13 included cases of malignant hypertension , thrombotic microangiopathy , lupus nephritis , Henoch-Schonlein nephritis , crescentic glomerulonephritis , and cocaine-related acute renal failure .

Example answer:
{"entities": [{"text": "malignant hypertension", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "lupus nephritis", "type": "Disease"}, {"text": "Henoch-Schonlein nephritis", "type": "Disease"}, {"text": "glomerulonephritis", "type": "Disease"}, {"text": "cocaine-related", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : This study demonstrates that chronic FK506 nephropathy consists primarily of arteriolopathy manifesting as insudative hyalinosis of the arteriolar wall , and suggests that mild-type chronic FK506 nephropathy is a condition which may lead to deterioration of renal allograft function .

Example answer:
{"entities": [{"text": "FK506", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: The rat biodistribution studies showed a rapid blood clearance via the kidneys .

Example answer:
{"entities": []}

Example input:
Sentence: Native kidney specimens included a wide range of glomerulopathies as well as cases of thrombotic microangiopathy , malignant hypertension , acute interstitial nephritis , and acute tubular necrosis .

Example answer:
{"entities": [{"text": "glomerulopathies", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "malignant hypertension", "type": "Disease"}, {"text": "interstitial nephritis", "type": "Disease"}, {"text": "acute tubular necrosis", "type": "Disease"}]}

Example input:
Sentence: PTCR also occurs in certain native kidney diseases , though the association is not as strong as that for TG .

Example answer:
{"entities": [{"text": "kidney diseases", "type": "Disease"}, {"text": "TG", "type": "Disease"}]}

Example input:
Sentence: RESULTS : The main pathologic diagnoses ( some overlap ) were acute rejection ( AR ; n = 4 ) , chronic rejection ( CR ; n=5 ) , AR+CR ( n =4 ) , recurrent IgA nephropathy ( n =5 ) , normal findings ( n =2 ) , minimal-type chronic FK506 nephropathy ( n = 9 ) , and mild-type FK506 nephropathy ( n = 11 ) .

Example answer:
{"entities": [{"text": "IgA nephropathy", "type": "Disease"}, {"text": "FK506", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: Cases were patients who developed hyperkalemia ( K ( + ) > 5.0 mEq/L ) or renal insufficiency ( Cr > or=2.5 mg/dL ) , and they were compared to 2 randomly selected controls per case .

Example answer:
{"entities": [{"text": "hyperkalemia", "type": "Disease"}, {"text": "K", "type": "Chemical"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "Cr", "type": "Chemical"}]}

Example input:
Sentence: Fifty-eight patients ( 78 % ) had normal renal tests , whereas 16 patients ( 22 % ) had renal abnormalities .

Example answer:
{"entities": [{"text": "renal abnormalities", "type": "Disease"}]}

Input:
Sentence: The pattern of kidney syndromes in this population series mirrors that reported in randomised clinical trials .

## Item bc5cdr:test:3615
Example input:
Sentence: Both , production of reactive oxygen species as well as activation of NF-kappaB have been implicated in severe neuronal damage in different sub-regions of the hippocampus as well as in the surrounding cortices .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "neuronal damage", "type": "Disease"}]}

Example input:
Sentence: We tested the sulfated polysaccharide fucoidan , which has been reported to reduce inflammatory brain damage , in a rat model of intracerebral hemorrhage induced by injection of bacterial collagenase into the caudate nucleus .

Example answer:
{"entities": [{"text": "fucoidan", "type": "Chemical"}, {"text": "brain damage", "type": "Disease"}, {"text": "intracerebral hemorrhage", "type": "Disease"}]}

Example input:
Sentence: Inflammatory cells are postulated to mediate some of the brain damage following ischemic stroke .

Example answer:
{"entities": [{"text": "brain damage", "type": "Disease"}, {"text": "ischemic stroke", "type": "Disease"}]}

Example input:
Sentence: We conclude from these studies that CX3CR1 signaling does not modulate METH neurotoxicity or microglial activation .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "Disease"}, {"text": "METH", "type": "Chemical"}, {"text": "MPTP", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "METH-induced", "type": "Chemical"}]}

Example input:
Sentence: Our findings indicate that beta2-adrenoceptor overstimulation during an early critical period results in microglial activation associated with innate neuroinflammatory pathways and behavioral abnormalities , similar to those described in autism .

Example answer:
{"entities": [{"text": "behavioral abnormalities", "type": "Disease"}, {"text": "autism", "type": "Disease"}]}

Example input:
Sentence: This data suggests that E2 modifies the expression of CD36 at the level of protein expression in monocyte-derived macrophages resulting in reduced cholesteryl ester accumulation following ritonavir treatment .

Example answer:
{"entities": [{"text": "E2", "type": "Chemical"}, {"text": "cholesteryl ester", "type": "Chemical"}, {"text": "ritonavir", "type": "Chemical"}]}

Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: Because such a compensatory mechanism most likely occurs to reduce injury to the brain from cytotoxic compounds , the present data substantiate the concept that MRP2 performs a protective role in the BBB .

Example answer:
{"entities": [{"text": "injury to the brain", "type": "Disease"}]}

Example input:
Sentence: 9 ( 2006 ) , 917 ] recently identified the microglial-specific fractalkine receptor ( CX3CR1 ) as an important mediator of MPTP-induced neurodegeneration of DA neurons .

Example answer:
{"entities": [{"text": "MPTP-induced", "type": "Chemical"}, {"text": "neurodegeneration", "type": "Disease"}, {"text": "DA", "type": "Chemical"}]}

Input:
Sentence: CCR2 is a chemokine receptor for CCL2 and their interaction mediates monocyte infiltration in the neuroinflammatory cascade triggered in different brain pathologies .

## Item bc5cdr:test:4031
Example input:
Sentence: Proximal muscle weakness has developed during her follow-up .

Example answer:
{"entities": [{"text": "muscle weakness", "type": "Disease"}]}

Example input:
Sentence: She had no previous beta-blocking drug exposure .

Example answer:
{"entities": []}

Example input:
Sentence: A 49-year-old woman was transferred to our department because of quadriparesis , lancinating pain , sensory loss , and paresthesia of the distal limbs .

Example answer:
{"entities": [{"text": "quadriparesis", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "sensory loss", "type": "Disease"}, {"text": "paresthesia", "type": "Disease"}]}

Example input:
Sentence: She was not an alcoholic .

Example answer:
{"entities": []}

Example input:
Sentence: Motor behavior , passive avoidance , and skilled forelimb function were tested repeatedly for six weeks .

Example answer:
{"entities": []}

Example input:
Sentence: The neurologic evaluation revealed loss of sensation in the saddle area and medial aspect of her right leg .

Example answer:
{"entities": [{"text": "loss of sensation", "type": "Disease"}]}

Example input:
Sentence: Her acetylcholine receptor antibody level was markedly elevated .

Example answer:
{"entities": [{"text": "acetylcholine", "type": "Chemical"}]}

Example input:
Sentence: She had a gradual return of motor function and ability of feeling Foley catheter .

Example answer:
{"entities": []}

Example input:
Sentence: After her strength returned , repetitive stimulation was normal , but single fiber EMG revealed increased jitter and blocking .

Example answer:
{"entities": []}

Example input:
Sentence: She was unable to urinate .

Example answer:
{"entities": []}

Input:
Sentence: She otherwise reported that she is quite active , rides horses , and does show jumping without any limitations in her physical activity .

## Item bc5cdr:test:3783
Example input:
Sentence: CONCLUSIONS : Patients who are more than 10 years post-OLTX have CRF and ESRD at a high rate .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: A 78-year-old with healed septal necrosis suffered a recurrent myocardial infarction of the anterior wall following the administration of isosorbide dinitrate 5 mg sublingually .

Example answer:
{"entities": [{"text": "necrosis", "type": "Disease"}, {"text": "myocardial infarction", "type": "Disease"}, {"text": "isosorbide dinitrate", "type": "Chemical"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: Renal structure and concentrating ability were examined after a recovery period of up to 18 weeks , when no analgesics were given , to investigate whether the analgesic-induced changes were reversible .

Example answer:
{"entities": []}

Example input:
Sentence: The rigidity was considerably decreased in both groups after 20 days ' treatment .

Example answer:
{"entities": [{"text": "rigidity", "type": "Disease"}]}

Example input:
Sentence: Five of 8 patients ( 63 % ) improved during fusidic acid treatment : 3 at two weeks and 2 after four weeks .

Example answer:
{"entities": [{"text": "fusidic acid", "type": "Chemical"}]}

Example input:
Sentence: Bone marrow recovery and peripheral blood recovery were complete 1 month and 3 months , respectively , after treatment , and blood transfusion or other therapies were not necessary in a follow-up period of more than 2 years .

Example answer:
{"entities": []}

Example input:
Sentence: There was no evidence of repair to the damaged medullary interstitial matrix , or proliferation of remaining undamaged type 1 medullary interstitial cells after the recovery period following analgesic treatment .

Example answer:
{"entities": []}

Example input:
Sentence: She subsequently died some 5 weeks after the commencement of her drug therapy.Post-mortem examination showed evidence of massive hepatocellular necrosis , acute hypersensitivity myocarditis , focal acute tubulo-interstitial nephritis and extensive bone marrow necrosis , with no evidence of malignancy .

Example answer:
{"entities": [{"text": "massive hepatocellular necrosis", "type": "Disease"}, {"text": "myocarditis", "type": "Disease"}, {"text": "nephritis", "type": "Disease"}, {"text": "bone marrow necrosis", "type": "Disease"}, {"text": "malignancy", "type": "Disease"}]}

Example input:
Sentence: Within 8 hours after initiation of therapy the patient died with a clinical picture resembling massive pulmonary obstruction due to choriocarcinomic tissue plugs , probably originating from the uterus .

Example answer:
{"entities": [{"text": "pulmonary obstruction", "type": "Disease"}]}

Input:
Sentence: Moreover , numerous patchy , well-limited fibrotic areas , compatible with post-necrotic tissue repair , were found after 6-month temsirolimus therapy .

## Item bc5cdr:test:3831
Example input:
Sentence: Brain MR studies , including DW imaging , were prospectively performed in 14 organ transplant patients receiving tacrolimus who developed neurologic complications .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "neurologic complications", "type": "Disease"}]}

Example input:
Sentence: Patients who are switched from cyclosporine to tacrolimus or vice versa should be closely monitored for the signs and symptoms of recurrent TMA .

Example answer:
{"entities": [{"text": "cyclosporine", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "TMA", "type": "Disease"}]}

Example input:
Sentence: Two groups of patients receiving tacrolimus were compared over a period of 1 year , one group comprising hypertensive patients who were receiving nifedipine , and the other comprising nonhypertensive patients not receiving nifedipine .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "hypertensive", "type": "Disease"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : The calcineurin inhibitors cyclosporine and tacrolimus are both known to be nephrotoxic .

Example answer:
{"entities": [{"text": "cyclosporine", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "nephrotoxic", "type": "Disease"}]}

Example input:
Sentence: -Tacrolimus ( FK 506 ) is a powerful , widely used immunosuppressant .

Example answer:
{"entities": [{"text": "FK 506", "type": "Chemical"}]}

Example input:
Sentence: The aim of this study was to examine further the renal function , including morphological analysis of the kidneys of male Sprague-Dawley rats treated with either cyclosporine A ( CsA ) , tacrolimus ( FK506 ) or SRL as monotherapies or in different combinations .

Example answer:
{"entities": [{"text": "cyclosporine A", "type": "Chemical"}, {"text": "CsA", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: Diffusion-weighted imaging may be useful in predicting the outcomes of the lesions of tacrolimus-induced neurotoxicity .

Example answer:
{"entities": [{"text": "tacrolimus-induced", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: The last decade has seen the emergence of tacrolimus as a potent immunosuppressive agent with mechanisms of action virtually identical to those of cyclosporine .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "cyclosporine", "type": "Chemical"}]}

Example input:
Sentence: Introduction of tacrolimus as an alternative immunosuppressive agent resulted in the recurrence of TMA and the subsequent loss of the renal allograft .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "TMA", "type": "Disease"}]}

Example input:
Sentence: As a result , switching to tacrolimus has been reported to be a viable therapeutic option in the setting of cyclosporine-induced TMA .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "cyclosporine-induced", "type": "Chemical"}, {"text": "TMA", "type": "Disease"}]}

Input:
Sentence: The aim of this work is to call attention to the risk of tacrolimus use in patients with SSc .

## Item bc5cdr:test:3876
Example input:
Sentence: Our patients developed jaundice following treatment with ticlopidine and showed the clinical and laboratory characteristics of cholestatic hepatitis , which resolved after discontinuation of the drug .

Example answer:
{"entities": [{"text": "jaundice", "type": "Disease"}, {"text": "ticlopidine", "type": "Chemical"}]}

Example input:
Sentence: We postulate that the mechanism of the simvastatinezetimibe-induced hepatotoxicity is the increased simvastatin exposure by ezetimibe inhibition of UGT enzymes .

Example answer:
{"entities": [{"text": "simvastatinezetimibe-induced", "type": "Chemical"}, {"text": "hepatotoxicity", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "ezetimibe", "type": "Chemical"}]}

Example input:
Sentence: This observation shows that clotiazepam can induce acute hepatitis and suggests that there is no cross hepatotoxicity between clotiazepam and several benzodiazepines .

Example answer:
{"entities": [{"text": "clotiazepam", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}, {"text": "hepatotoxicity", "type": "Disease"}, {"text": "benzodiazepines", "type": "Chemical"}]}

Example input:
Sentence: This complication will be observed even less often in the future as ticlopidine is being replaced by the newer antiplatelet agent clopidogrel .

Example answer:
{"entities": [{"text": "ticlopidine", "type": "Chemical"}, {"text": "clopidogrel", "type": "Chemical"}]}

Example input:
Sentence: CASE SUMMARIES : Two patients developed prolonged cholestatic hepatitis after receiving ticlopidine following percutaneous coronary angioplasty , with complete remission during the follow-up period .

Example answer:
{"entities": [{"text": "ticlopidine", "type": "Chemical"}]}

Example input:
Sentence: Drug-induced hepatotoxicity , although common , has been reported only infrequently with sulfonylureas .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}, {"text": "sulfonylureas", "type": "Chemical"}]}

Example input:
Sentence: DISCUSSION : Cholestatic hepatitis is a rare complication of the antiplatelet agent ticlopidine ; several cases have been reported but few in the English literature .

Example answer:
{"entities": [{"text": "ticlopidine", "type": "Chemical"}]}

Example input:
Sentence: By November 1984 the Committee on Safety of Medicines had received 82 reports of possible hepatotoxicity associated with the drug , including five deaths .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}, {"text": "deaths", "type": "Disease"}]}

Example input:
Sentence: Simvastatinezetimibe and escitalopram ( which she was taking for depression ) were discontinued , and other potential causes of hepatotoxicity were excluded .

Example answer:
{"entities": [{"text": "Simvastatinezetimibe", "type": "Chemical"}, {"text": "escitalopram", "type": "Chemical"}, {"text": "depression", "type": "Disease"}, {"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: We report the case of a patient who developed acute hepatitis with extensive hepatocellular necrosis , 7 months after the onset of administration of clotiazepam , a thienodiazepine derivative .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}, {"text": "extensive hepatocellular necrosis", "type": "Disease"}, {"text": "clotiazepam", "type": "Chemical"}, {"text": "thienodiazepine", "type": "Chemical"}]}

Input:
Sentence: Reports about cases of hepatotoxicity due to clopidogrel are increasing in the last few years , after the increased use of this drug .

## Item bc5cdr:test:3665
Example input:
Sentence: The acute renal dysfunction associated with sirolimus ( such as in delayed graft function ) may be due to suppression of compensatory renal cell proliferation and survival/repair processes .

Example answer:
{"entities": [{"text": "acute renal dysfunction", "type": "Disease"}, {"text": "sirolimus", "type": "Chemical"}]}

Example input:
Sentence: In this patient , renal artery stenosis combined with heart failure and diuretic therapy certainly resulted in a strong activation of the renin-angiotensin system ( RAS ) .

Example answer:
{"entities": [{"text": "renal artery stenosis", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}]}

Example input:
Sentence: We report a case of ranitidine-induced acute interstitial nephritis in a recipient of a cadaveric renal allograft presenting with acute allograft dysfunction within 48 hours of exposure to the drug .

Example answer:
{"entities": [{"text": "ranitidine-induced", "type": "Chemical"}, {"text": "interstitial nephritis", "type": "Disease"}]}

Example input:
Sentence: Patients who developed renal insufficiency had lower baseline body weight and higher baseline serum creatinine , required higher doses of loop diuretics , and were more likely to be treated with thiazide diuretics than controls .

Example answer:
{"entities": [{"text": "renal insufficiency", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "thiazide", "type": "Chemical"}]}

Example input:
Sentence: We propose that amphotericin , in the setting of reduced effective arterial volume , may activate tubuloglomerular feedback , thereby contributing to acute renal failure .

Example answer:
{"entities": [{"text": "amphotericin", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: Cardiac Angiography in Renally Impaired Patients ( CARE ) study : a randomized double-blind trial of contrast-induced nephropathy in patients with chronic kidney disease .

Example answer:
{"entities": [{"text": "nephropathy", "type": "Disease"}, {"text": "chronic kidney disease", "type": "Disease"}]}

Example input:
Sentence: Diagnosis of this potentially fatal complication may be delayed or missed if renal tissue or the peripheral blood smear is not examined , because renal failure may be ascribed to cisplatin nephrotoxicity and the anemia and thrombocytopenia to drug-induced bone marrow suppression .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "bone marrow suppression", "type": "Disease"}]}

Example input:
Sentence: METHODS AND RESULTS : The present study is a multicenter , randomized , double-blind comparison of iopamidol and iodixanol in patients with chronic kidney disease ( estimated glomerular filtration rate , 20 to 59 mL/min ) who underwent cardiac angiography or percutaneous coronary interventions .

Example answer:
{"entities": [{"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}, {"text": "chronic kidney disease", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : No direct comparisons exist of the renal tolerability of the low-osmolality contrast medium iopamidol with that of the iso-osmolality contrast medium iodixanol in high-risk patients .

Example answer:
{"entities": [{"text": "contrast medium", "type": "Chemical"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : The rate of contrast-induced nephropathy , defined by multiple end points , is not statistically different after the intraarterial administration of iopamidol or iodixanol to high-risk patients , with or without diabetes mellitus .

Example answer:
{"entities": [{"text": "nephropathy", "type": "Disease"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}, {"text": "diabetes mellitus", "type": "Disease"}]}

Input:
Sentence: BACKGROUND : Renal dysfunction induced by iodinated contrast medium ( CM ) administration can minimize the benefit of the interventional procedure in patients undergoing renal angioplasty ( PTRA ) .

## Item bc5cdr:test:3338
Example input:
Sentence: Following instrumentation , halothane was discontinued and alfentanil ( 125 mu/kg ) administered iv during emergence from halothane anesthesia .

Example answer:
{"entities": [{"text": "halothane", "type": "Chemical"}, {"text": "alfentanil", "type": "Chemical"}]}

Example input:
Sentence: This demonstrates the participation of the renin -- angiotensin system in antagonizing the combined hypotensive effects of halothane and SNP .

Example answer:
{"entities": [{"text": "angiotensin", "type": "Chemical"}, {"text": "hypotensive", "type": "Disease"}, {"text": "halothane", "type": "Chemical"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: VPU was more potent than VPA , exhibiting the median effective dose ( ED ( 50 ) ) of 49 mg/kg in protecting rats against pilocarpine-induced seizure whereas the corresponding value for VPA was 322 mg/kg .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: UM-272 ( N , N-dimethylpropranolol ) , a quaternary antiarrhythmic agent , was administered sublingually to dogs with ouabain-induced ventricular tachycardias .

Example answer:
{"entities": [{"text": "UM-272", "type": "Chemical"}, {"text": "N , N-dimethylpropranolol", "type": "Chemical"}, {"text": "ouabain-induced", "type": "Chemical"}, {"text": "ventricular tachycardias", "type": "Disease"}]}

Example input:
Sentence: In isolated perfused heart preparations from isoproterenol-pretreated rats , the isoproterenol-induced maximal increase in left ventricular systolic pressure was significantly reduced , compared with saline-pretreated rats ( the EC50 of the isoproterenol-induced increase in left ventricular systolic pressure was enhanced approximately 22-fold ) .

Example answer:
{"entities": [{"text": "isoproterenol-pretreated", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: Seven patients suffering from Parkinson 's disease ( PD ) with severely disabling dyskinesia received low-dose propranolol as an adjunct to the currently used medical treatment .

Example answer:
{"entities": [{"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "propranolol", "type": "Chemical"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: 1 h prior to haloperidol resulted in a dose-dependent increase in the catalepsy times ( P < 0.05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: The effects of oral doses of diazepam ( single dose of 10 mg and a median dose of 30 mg/day for 2 weeks ) and propranolol ( single dose of 80 mg and a median dose of 240 mg/day for 2 weeks ) on psychological performance of patients with panic disorders and agoraphobia were investigated in a double-blind , randomized and crossover design .

Example answer:
{"entities": [{"text": "diazepam", "type": "Chemical"}, {"text": "propranolol", "type": "Chemical"}, {"text": "panic disorders", "type": "Disease"}, {"text": "agoraphobia", "type": "Disease"}]}

Example input:
Sentence: METHODS : Following induction of anesthesia by fentanyl ( 0.15 mg kg ( -1 ) ) and propofol ( 2.0 mg kg ( -1 ) ) , 13 patients received phenylephrine ( 0.1 mg iv ) and 12 patients received ephedrine ( 10 mg iv ) to restore mean arterial pressure ( MAP ) .

Example answer:
{"entities": [{"text": "fentanyl", "type": "Chemical"}, {"text": "propofol", "type": "Chemical"}, {"text": "phenylephrine", "type": "Chemical"}, {"text": "ephedrine", "type": "Chemical"}]}

Input:
Sentence: Both isomers of propranolol were capable of preventing adrenaline-induced cardiac arrhythmias in cats anaesthetized with halothane , but the mean dose of ( - ) -propranolol was 0.09+/-0.02 mg/kg whereas that of ( + ) -propranolol was 4.2+/-1.2 mg/kg .

## Item bc5cdr:test:3753
Example input:
Sentence: These seven cases demonstrate that procainamide can produce an acquired prolonged Q-T syndrome with polymorphous ventricular tachycardia .

Example answer:
{"entities": [{"text": "procainamide", "type": "Chemical"}, {"text": "prolonged Q-T syndrome", "type": "Disease"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: Prolactin results were compared with those of a previous personal cohort of 1,340 patients with erectile dysfunction and systematic prolactin determination .

Example answer:
{"entities": [{"text": "erectile dysfunction", "type": "Disease"}]}

Example input:
Sentence: Also the enhancement of verapamil effects on atrial beating was more pronounced at LNa than at LCa .

Example answer:
{"entities": [{"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: Possible mechanisms that involve a verapamil-related increase in platelet and/or vascular alpha 2-adrenoreceptor affinity for catecholamines are discussed .

Example answer:
{"entities": [{"text": "verapamil-related", "type": "Chemical"}, {"text": "catecholamines", "type": "Chemical"}]}

Example input:
Sentence: Dose-dependent bradycardia induced by verapamil was potentiated by LNa , LCa , and HCa .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: Prolactin should be determined only in cases of low sexual desire , gynecomastia and/or testosterone less than 4 ng./ml .

Example answer:
{"entities": [{"text": "low sexual desire", "type": "Disease"}, {"text": "gynecomastia", "type": "Disease"}, {"text": "testosterone", "type": "Chemical"}]}

Example input:
Sentence: Every patient was screened for testosterone and 451 were screened for prolactin on the basis of low sexual desire , gynecomastia or testosterone less than 4 ng./ml .

Example answer:
{"entities": [{"text": "testosterone", "type": "Chemical"}, {"text": "low sexual desire", "type": "Disease"}, {"text": "gynecomastia", "type": "Disease"}]}

Example input:
Sentence: Hyperprolactinemia can reduce fertility and libido .

Example answer:
{"entities": [{"text": "Hyperprolactinemia", "type": "Disease"}]}

Example input:
Sentence: Chronic hyperprolactinemia induced by the dopamine antagonist sulpiride caused a 40 % reduction LH pulse frequency in ovariectomized rats , but only in the presence of chronic low levels of estradiol .

Example answer:
{"entities": [{"text": "hyperprolactinemia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "sulpiride", "type": "Chemical"}, {"text": "estradiol", "type": "Chemical"}]}

Example input:
Sentence: We first tested whether chronic hyperprolactinemia inhibited two neuroendocrine parameters necessary for female fertility : pulsatile LH secretion and the estrogen-induced LH surge .

Example answer:
{"entities": [{"text": "hyperprolactinemia", "type": "Disease"}, {"text": "estrogen-induced", "type": "Chemical"}]}

Input:
Sentence: AIM : Verapamil stimulation test was previously investigated as a tool for differential diagnosis of hyperprolactinemia , but with conflicting results .

## Item bc5cdr:test:3991
Example input:
Sentence: As the most potent dose ( 1 mg/kg ) of lipopolysaccharide was administered two weeks , one day before or after the methamphetamine dosing regimen , methamphetamine-induced striatal dopamine and 3,4-dihydroxyphenylacetic acid depletions remained unaltered .

Example answer:
{"entities": [{"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "methamphetamine-induced", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "3,4-dihydroxyphenylacetic acid", "type": "Chemical"}]}

Example input:
Sentence: One hour after the administration of gamma-HCH , the activity of seizure-inducing agents was increased , regardless of their mechanism , while 24 h after gamma-HCH a differential response was observed .

Example answer:
{"entities": [{"text": "gamma-HCH", "type": "Chemical"}, {"text": "seizure-inducing", "type": "Disease"}]}

Example input:
Sentence: Depletion of dopamine in the striatum was also antagonized when LY274614 was given after the injection of amphetamine ; LY274614 protected when given up to 4 hr after but not when given 8 or 24 hr after amphetamine .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "LY274614", "type": "Chemical"}, {"text": "amphetamine", "type": "Chemical"}]}

Example input:
Sentence: After 2 weeks of treatment , patients tested 5-8 h after the last dose of medication did not show any decrement of performance .

Example answer:
{"entities": []}

Example input:
Sentence: She reported her use of methamphetamine for five years and had not experienced any major carious episodes before she started using the drug .

Example answer:
{"entities": [{"text": "methamphetamine", "type": "Chemical"}, {"text": "carious episodes", "type": "Disease"}]}

Example input:
Sentence: Methamphetamine ( 10 mg/kg sc ) , administered five times , reduced the levels of dopamine and its metabolites in striatal tissue when measured 72 h after the last injection .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: The open study lasted for four weeks ; the drug was administrated in the form of 1 mg tablets .

Example answer:
{"entities": []}

Example input:
Sentence: They showed significantly more rapid improvement of motor function in the first week following hemorrhage and better memory retention in the passive avoidance test .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "Disease"}]}

Example input:
Sentence: Initial testing in a time-dependent forgetting task employing a 24-h delay between training and testing showed that metrifonate improved object recognition ( at 10 and 30 mg/kg , p.o .

Example answer:
{"entities": [{"text": "metrifonate", "type": "Chemical"}]}

Example input:
Sentence: Rats treated for 11 days with morphine and withdrawn for 36-40 h showed differences in the development of tolerance : about half of the animals showed a rigidity after the test dose of morphine that was not significantly less than in the controls and were akinetic ( A group ) .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "rigidity", "type": "Disease"}, {"text": "akinetic", "type": "Disease"}]}

Input:
Sentence: However , METH significantly increased the immobility time in the tail suspension test at 3 and 49 days post-administration .

## Item bc5cdr:test:3762
Example input:
Sentence: Independent but not additive effects of Na and Ca are shown by decreases in the values of [ verapamil ] o needed to reduce BF by 30 % ( IC30 ) with the following order of inhibitory potency : LNa > LCa > HCa > N , resulting LNa+HCa similar to LNa .

Example answer:
{"entities": [{"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: Bromocriptine was definitely effective in cases with prolactin greater than 35 ng./ml .

Example answer:
{"entities": [{"text": "Bromocriptine", "type": "Chemical"}]}

Example input:
Sentence: Possible mechanisms that involve a verapamil-related increase in platelet and/or vascular alpha 2-adrenoreceptor affinity for catecholamines are discussed .

Example answer:
{"entities": [{"text": "verapamil-related", "type": "Chemical"}, {"text": "catecholamines", "type": "Chemical"}]}

Example input:
Sentence: Every patient was screened for testosterone and 451 were screened for prolactin on the basis of low sexual desire , gynecomastia or testosterone less than 4 ng./ml .

Example answer:
{"entities": [{"text": "testosterone", "type": "Chemical"}, {"text": "low sexual desire", "type": "Disease"}, {"text": "gynecomastia", "type": "Disease"}]}

Example input:
Sentence: The patient 's clinical course is described and correlated with initial urodynamic studies while on prazosin and subsequent studies while taking verapamil .

Example answer:
{"entities": [{"text": "prazosin", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: Prolactin should be determined only in cases of low sexual desire , gynecomastia and/or testosterone less than 4 ng./ml .

Example answer:
{"entities": [{"text": "low sexual desire", "type": "Disease"}, {"text": "gynecomastia", "type": "Disease"}, {"text": "testosterone", "type": "Chemical"}]}

Example input:
Sentence: Dose-dependent bradycardia induced by verapamil was potentiated by LNa , LCa , and HCa .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: Hyperprolactinemia can reduce fertility and libido .

Example answer:
{"entities": [{"text": "Hyperprolactinemia", "type": "Disease"}]}

Example input:
Sentence: We first tested whether chronic hyperprolactinemia inhibited two neuroendocrine parameters necessary for female fertility : pulsatile LH secretion and the estrogen-induced LH surge .

Example answer:
{"entities": [{"text": "hyperprolactinemia", "type": "Disease"}, {"text": "estrogen-induced", "type": "Chemical"}]}

Example input:
Sentence: Chronic hyperprolactinemia induced by the dopamine antagonist sulpiride caused a 40 % reduction LH pulse frequency in ovariectomized rats , but only in the presence of chronic low levels of estradiol .

Example answer:
{"entities": [{"text": "hyperprolactinemia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "sulpiride", "type": "Chemical"}, {"text": "estradiol", "type": "Chemical"}]}

Input:
Sentence: CONCLUSION : Verapamil responsiveness is not a reliable finding for the differential diagnosis of hyperprolactinemia .

## Item bc5cdr:test:4101
Example input:
Sentence: DISCUSSION : To our knowledge , this is the first reported case of venlafaxine overdose that resulted in a generalized seizure .

Example answer:
{"entities": [{"text": "venlafaxine", "type": "Chemical"}, {"text": "overdose", "type": "Disease"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Repeated cerebral perfusion SPECT scans revealed decreased basal ganglia perfusion while the movement disorder was present , and a return to normal perfusion when the rabbit syndrome resolved .

Example answer:
{"entities": [{"text": "decreased basal ganglia perfusion", "type": "Disease"}, {"text": "movement disorder", "type": "Disease"}, {"text": "rabbit syndrome", "type": "Disease"}]}

Example input:
Sentence: Ten patients with PD and prominent dyskinesias had rTMS ( 1,800 pulses ; 1 Hz rate ) delivered over the motor cortex for 4 consecutive days twice , once real stimuli and once sham stimulation were used ; evaluations were done at the baseline and 1 day after the end of each of the treatment series .

Example answer:
{"entities": [{"text": "PD", "type": "Disease"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: In 24 patients with this complication , the marked slowing of motor nerve conduction velocity and the electromyographic changes imply mainly a demyelinating disorder .

Example answer:
{"entities": [{"text": "demyelinating disorder", "type": "Disease"}]}

Example input:
Sentence: One patient had focal seizures and transient hemiparesis but recovered completely .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "transient hemiparesis", "type": "Disease"}]}

Example input:
Sentence: Electrical recordings from the hippocampus showed a rhythmic progression in EEG frequency and voltage with clinical seizure expression .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: All three had been diagnosed earlier with epilepsy , and their electroencephalogram ( EEG ) findings were abnormal .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}]}

Example input:
Sentence: The interictal electroencephalogram ( EEG ) showed a generalized slowing to 5 per second theta rhythms with bilateral generalized high-amplitude discharges .

Example answer:
{"entities": []}

Example input:
Sentence: The EEG shows characteristic triphasic waves in most patients with this complication .

Example answer:
{"entities": []}

Example input:
Sentence: An electroencephalogram showed continuous , generalized irregular slowing with admixed periodic triphasic waves indicating symptomatic encephalopathy .

Example answer:
{"entities": [{"text": "encephalopathy", "type": "Disease"}]}

Input:
Sentence: Initial EEG showed epileptiform discharges in three patients ; run of triphasic waves in one patient and moderate degree diffuse generalized slowing .

## Item bc5cdr:test:3682
Example input:
Sentence: The possibility that habitual use of acetaminophen alone increases the risk of ESRD has not been clearly demonstrated , but can not be dismissed .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Antituberculosis therapy ( ATT ) -associated acute liver failure ( ATT-ALF ) is the commonest drug-induced ALF in South Asia .

Example answer:
{"entities": [{"text": "Antituberculosis", "type": "Chemical"}, {"text": "acute liver failure", "type": "Disease"}, {"text": "ALF", "type": "Disease"}]}

Example input:
Sentence: This article describes two critically ill patients in whom transient episodes of hypotension reproducibly developed after administration of acetaminophen .

Example answer:
{"entities": [{"text": "critically ill", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}, {"text": "acetaminophen", "type": "Chemical"}]}

Example input:
Sentence: Over the long-term chronic phase ( 120 days after transplantation ) , only 25 % of BMC-treated epileptic animals had seizures , but with a lower frequency and duration compared to the epileptic control group .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Hypertensive patients with psychiatric histories had a higher prevalence of depression than the comparison patients .

Example answer:
{"entities": [{"text": "Hypertensive", "type": "Disease"}, {"text": "psychiatric", "type": "Disease"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: Two patients with similar clinical features are presented : both patients had chronic renal failure , on hemodialysis for many years but recently begun on a high-flux dialyzer ; both had been receiving a carbidopa/levodopa preparation ; and both had the onset of hallucinosis and recurrent seizures , which were refractory to anticonvulsants .

Example answer:
{"entities": [{"text": "chronic renal failure", "type": "Disease"}, {"text": "carbidopa/levodopa", "type": "Chemical"}, {"text": "hallucinosis", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: End-stage renal disease ( ESRD ) after orthotopic liver transplantation ( OLTX ) using calcineurin-based immunotherapy : risk of development and treatment .

Example answer:
{"entities": [{"text": "End-stage renal disease", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: From January 1986 to January 2009 , 1223 consecutive ALF patients were evaluated : ATT alone was the cause in 70 ( 5.7 % ) patients .

Example answer:
{"entities": [{"text": "ALF", "type": "Disease"}]}

Example input:
Sentence: However , three case control studies , one each in North Carolina , northern Maryland , and West Berlin , Germany , showed that habitual use of acetaminophen is also associated with chronic renal failure and ESRD , with a relative risk in the range of 2 to 4 .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "chronic renal failure", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Input:
Sentence: CONCLUSIONS : Despite a high prevalence of psychiatric disturbance , outcomes for patients transplanted emergently for acetaminophen-induced ALF were comparable to those transplanted for non-acetaminophen-induced ALF and electively for CLD .

## Item bc5cdr:test:3680
Example input:
Sentence: Multivariate stepwise logistic regression analysis using preoperative and postoperative variables identified that an increase of serum creatinine compared with average at 1 year , 3 months , and 4 weeks postoperatively were independent risk factors for the development of CRF or ESRD with odds ratios of 2.6 , 2.2 , and 1.6 , respectively .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Upon rechallenge with either cephalosporin , the hematologic syndrome was reproduced in most dogs tested ; cefonicid ( but not cefazedone ) -treated dogs showed a substantially reduced induction period ( 15 +/- 5 days ) compared to that of the first exposure to the drug ( 61 +/- 24 days ) .

Example answer:
{"entities": [{"text": "cephalosporin", "type": "Chemical"}, {"text": "hematologic syndrome", "type": "Disease"}, {"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}]}

Example input:
Sentence: Two groups of patients receiving tacrolimus were compared over a period of 1 year , one group comprising hypertensive patients who were receiving nifedipine , and the other comprising nonhypertensive patients not receiving nifedipine .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "hypertensive", "type": "Disease"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: However , three case control studies , one each in North Carolina , northern Maryland , and West Berlin , Germany , showed that habitual use of acetaminophen is also associated with chronic renal failure and ESRD , with a relative risk in the range of 2 to 4 .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "chronic renal failure", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Antituberculosis therapy ( ATT ) -associated acute liver failure ( ATT-ALF ) is the commonest drug-induced ALF in South Asia .

Example answer:
{"entities": [{"text": "Antituberculosis", "type": "Chemical"}, {"text": "acute liver failure", "type": "Disease"}, {"text": "ALF", "type": "Disease"}]}

Example input:
Sentence: RESULTS : At 13 years after OLTX , the incidence of severe renal dysfunction was 18.1 % ( CRF 8.6 % and ESRD 9.5 % ) .

Example answer:
{"entities": [{"text": "renal dysfunction", "type": "Disease"}, {"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Patients who are more than 10 years post-OLTX have CRF and ESRD at a high rate .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: ATT-ALF patients were younger ( 32.87 [ +/-15.8 ] years ) , and 49 ( 70 % ) of them were women .

Example answer:
{"entities": []}

Example input:
Sentence: The mortality rate among patients with ATT-ALF was high ( 67.1 % , n = 47 ) , and only 23 ( 32.9 % ) patients recovered with medical treatment .

Example answer:
{"entities": []}

Example input:
Sentence: From January 1986 to January 2009 , 1223 consecutive ALF patients were evaluated : ATT alone was the cause in 70 ( 5.7 % ) patients .

Example answer:
{"entities": [{"text": "ALF", "type": "Disease"}]}

Input:
Sentence: During follow-up ( median 5 years ) , there were no significant differences in rejection ( acute and chronic ) , graft failure or survival between the groups ( acetaminophen-induced ALF 1 year 87 % , 5 years 75 % ; non-acetaminophen-induced ALF 88 % , 78 % ; CLD 93 % , 82 % : P > 0.6 log rank ) .

## Item bc5cdr:test:3764
Example input:
Sentence: BACKGROUND : Sirolimus is the latest immunosuppressive agent used to prevent rejection , and may have less nephrotoxicity than calcineurin inhibitor ( CNI ) -based regimens .

Example answer:
{"entities": [{"text": "Sirolimus", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : This rat study demonstrated a synergistic nephrotoxic effect of CsA plus SRL , whereas FK506 plus SRL was better tolerated .

Example answer:
{"entities": [{"text": "nephrotoxic", "type": "Disease"}, {"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}]}

Example input:
Sentence: Using puromycin aminonucleoside nephrosis ( PAN ) rats , we studied early ultrastructural and permeability changes in relation to the expression of the podocyte-associated molecules nephrin , a-actinin , dendrin , and plekhh2 , the last two of which were only recently discovered in podocytes .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: The effect of a 6-week treatment with the calcium channel blocker nitrendipine or the angiotensin converting enzyme inhibitor enalapril on blood pressure , albuminuria , renal hemodynamics , and morphology of the nonclipped kidney was studied in rats with two-kidney , one clip renovascular hypertension .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "nitrendipine", "type": "Chemical"}, {"text": "angiotensin", "type": "Chemical"}, {"text": "enalapril", "type": "Chemical"}, {"text": "albuminuria", "type": "Disease"}, {"text": "renovascular hypertension", "type": "Disease"}]}

Example input:
Sentence: Heparan sulphate-associated anionic sites in the glomerular basement membrane were studied in rats 8 months after induction of diabetes by streptozotocin and in age- adn sex-matched control rats , employing the cationic dye cuprolinic blue .

Example answer:
{"entities": [{"text": "Heparan", "type": "Chemical"}, {"text": "diabetes", "type": "Disease"}, {"text": "streptozotocin", "type": "Chemical"}, {"text": "cuprolinic blue", "type": "Chemical"}]}

Example input:
Sentence: Reduction of heparan sulphate-associated anionic sites in the glomerular basement membrane of rats with streptozotocin-induced diabetic nephropathy .

Example answer:
{"entities": [{"text": "heparan", "type": "Chemical"}, {"text": "streptozotocin-induced", "type": "Chemical"}, {"text": "diabetic nephropathy", "type": "Disease"}]}

Example input:
Sentence: We conclude that in streptozotocin-diabetic rats with an increased urinary albumin excretion , a reduced heparan sulphate charge barrier/density is found at the lamina rara externa of the glomerular basement membrane .

Example answer:
{"entities": [{"text": "streptozotocin-diabetic", "type": "Chemical"}, {"text": "heparan sulphate", "type": "Chemical"}]}

Example input:
Sentence: Dup 753 prevents the development of puromycin aminonucleoside-induced nephrosis .

Example answer:
{"entities": [{"text": "Dup 753", "type": "Chemical"}, {"text": "puromycin", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : The rate of contrast-induced nephropathy , defined by multiple end points , is not statistically different after the intraarterial administration of iopamidol or iodixanol to high-risk patients , with or without diabetes mellitus .

Example answer:
{"entities": [{"text": "nephropathy", "type": "Disease"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}, {"text": "diabetes mellitus", "type": "Disease"}]}

Input:
Sentence: Blockade of endothelial-mesenchymal transition by a Smad3 inhibitor delays the early development of streptozotocin-induced diabetic nephropathy .

## Item bc5cdr:test:3919
Example input:
Sentence: Peripheral neuropathy has been noted as a complication of therapy with perhexiline maleate , a drug widely used in France ( and in clinical trials in the United States ) for the prophylactic treatment of angina pectoris .

Example answer:
{"entities": [{"text": "Peripheral neuropathy", "type": "Disease"}, {"text": "perhexiline maleate", "type": "Chemical"}, {"text": "angina pectoris", "type": "Disease"}]}

Example input:
Sentence: Isolated myelopathy or peripheral neuropathy , or these manifestations occurring together , were infrequent .

Example answer:
{"entities": [{"text": "myelopathy", "type": "Disease"}, {"text": "peripheral neuropathy", "type": "Disease"}]}

Example input:
Sentence: Other side effects were rare , and peripheral neurotoxicity has been minor ( 26 % grade 1 ) .

Example answer:
{"entities": [{"text": "peripheral neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Anticoagulant-induced femoral nerve palsy represents the most common form of warfarin-induced peripheral neuropathy ; it is characterized by severe pain in the inguinal region , varying degrees of motor and sensory impairment , and flexure contracture of the involved extremity .

Example answer:
{"entities": [{"text": "femoral nerve palsy", "type": "Disease"}, {"text": "warfarin-induced", "type": "Chemical"}, {"text": "peripheral neuropathy", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "motor and sensory impairment", "type": "Disease"}, {"text": "contracture", "type": "Disease"}]}

Example input:
Sentence: Sensori-motor neuropathy was the commonest presentation ( 50 % ) .

Example answer:
{"entities": [{"text": "Sensori-motor neuropathy", "type": "Disease"}]}

Example input:
Sentence: Guillain-Barr syndrome was the commonest identifiable cause ( 15.6 % ) , accounting for half of the cases with motor neuropathy .

Example answer:
{"entities": [{"text": "Guillain-Barr syndrome", "type": "Disease"}, {"text": "motor neuropathy", "type": "Disease"}]}

Example input:
Sentence: In 26.5 % of all the cases , the aetiology of the neuropathy was undetermined .

Example answer:
{"entities": [{"text": "neuropathy", "type": "Disease"}]}

Example input:
Sentence: In the remaining cases , a combination of myelopathy , visual disturbance , and peripheral neuropathy was the most common manifestation .

Example answer:
{"entities": [{"text": "myelopathy", "type": "Disease"}, {"text": "visual disturbance", "type": "Disease"}, {"text": "peripheral neuropathy", "type": "Disease"}]}

Example input:
Sentence: Peripheral neuropathy due to nutritional deficiency of thiamine and riboflavin was common ( 10.1 % ) and presented mainly as sensory and sensori-motor neuropathy .

Example answer:
{"entities": [{"text": "Peripheral neuropathy", "type": "Disease"}, {"text": "nutritional deficiency", "type": "Disease"}, {"text": "thiamine", "type": "Chemical"}, {"text": "riboflavin", "type": "Chemical"}, {"text": "sensori-motor neuropathy", "type": "Disease"}]}

Example input:
Sentence: Peripheral neuropathy occurred in 12 patients and pancreatitis in six .

Example answer:
{"entities": [{"text": "Peripheral neuropathy", "type": "Disease"}, {"text": "pancreatitis", "type": "Disease"}]}

Input:
Sentence: Peripheral neuropathy was observed only in 2.5 % of patients and deep vein thrombosis in 5.7 % .

## Item bc5cdr:test:3901
Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/", "type": "Chemical"}, {"text": "K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}]}

Example input:
Sentence: The results indicated that concomitant treatment with gum Arabic and GM significantly increased creatinine and urea by about 183 and 239 % , respectively ( compared to 432 and 346 % , respectively , in rats treated with cellulose and GM ) , and decreased that of cortical GSH by 21 % ( compared to 27 % in the cellulose plus GM group ) The GM-induced proximal tubular necrosis appeared to be slightly less severe in rats given GM together with gum Arabic than in those given GM and cellulose .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}, {"text": "urea", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "GM-induced", "type": "Chemical"}, {"text": "tubular necrosis", "type": "Disease"}]}

Example input:
Sentence: Acetylsalicylic acid , dipyridamole , and hydrocortisone all appear to have cardioprotective effects when tested in this model .

Example answer:
{"entities": [{"text": "Acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}]}

Example input:
Sentence: The cardiotoxic effects of adriamycin were studied in mammalian myocardial cells in culture as a model system .

Example answer:
{"entities": [{"text": "cardiotoxic", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}]}

Example input:
Sentence: These findings indicate the synergistic protective effect of green tea and vitamin E during ISO induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}, {"text": "ISO", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: together for 30 consecutive days and challenged with ISO on the day 29th and 30th , showed a significant ( P < 0.05 ) decrease in heart weight , serum marker enzymes , lipid peroxidation , Ca+2 ATPase and a significant increase in the body weight , endogenous antioxidants , Na+/K+ ATPase and Mg+2 ATPase when compared with ISO treated group and green tea or vitamin E alone treated groups .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}, {"text": "green tea", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}]}

Example input:
Sentence: The present study was aimed to investigate the combined effects of green tea and vitamin E on heart weight , body weight , serum marker enzymes , lipid peroxidation , endogenous antioxidants and membrane bound ATPases in isoproterenol ( ISO ) -induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "ISO", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Cardioprotective effect of tincture of Crataegus on isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "tincture of Crataegus", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: In vivo protection of dna damage associated apoptotic and necrotic cell deaths during acetaminophen-induced nephrotoxicity , amiodarone-induced lung toxicity and doxorubicin-induced cardiotoxicity by a novel IH636 grape seed proanthocyanidin extract .

Example answer:
{"entities": [{"text": "necrotic", "type": "Disease"}, {"text": "acetaminophen-induced", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "amiodarone-induced", "type": "Chemical"}, {"text": "lung toxicity", "type": "Disease"}, {"text": "doxorubicin-induced", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}, {"text": "IH636 grape seed proanthocyanidin extract", "type": "Chemical"}]}

Example input:
Sentence: This study assessed the ability of IH636 grape seed proanthocyanidin extract ( GSPE ) to prevent acetaminophen ( AAP ) -induced nephrotoxicity , amiodarone ( AMI ) -induced lung toxicity , and doxorubicin ( DOX ) -induced cardiotoxicity in mice .

Example answer:
{"entities": [{"text": "IH636 grape seed proanthocyanidin extract", "type": "Chemical"}, {"text": "GSPE", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "AAP", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "AMI", "type": "Chemical"}, {"text": "lung toxicity", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Input:
Sentence: Biochemical effects of Solidago virgaurea extract on experimental cardiotoxicity .

## Item bc5cdr:test:3937
Example input:
Sentence: METHOD : This was a cross-sectional study of 85 patients from a lithium clinic who received different dose schedules .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: Seven patients suffering from Parkinson 's disease ( PD ) with severely disabling dyskinesia received low-dose propranolol as an adjunct to the currently used medical treatment .

Example answer:
{"entities": [{"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "propranolol", "type": "Chemical"}]}

Example input:
Sentence: Of 24 evaluable patients , two achieved a complete remission and one achieved a partial remission for an overall response rate of 12.5 % ( 95 % confidence interval : 2.6-32.4 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: While there is no single correct starting dose for levodopa therapy , many individuals can be started on either the 25/100 or controlled-release formula , following the general rule not to attempt to titrate carbidopa-levodopa to the point of `` normality , '' which can lead to toxicity .

Example answer:
{"entities": [{"text": "levodopa", "type": "Chemical"}, {"text": "carbidopa-levodopa", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Ten patients with PD and prominent dyskinesias had rTMS ( 1,800 pulses ; 1 Hz rate ) delivered over the motor cortex for 4 consecutive days twice , once real stimuli and once sham stimulation were used ; evaluations were done at the baseline and 1 day after the end of each of the treatment series .

Example answer:
{"entities": [{"text": "PD", "type": "Disease"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: In contrast , monkeys with long-term MPTP exposure , slow symptom progression and/or long symptom duration prior to initiation of levodopa therapy were more resistant to developing LIDs ( e.g. , dyskinesia developed no sooner than 146 days of chronic levodopa administration ) .

Example answer:
{"entities": [{"text": "MPTP", "type": "Chemical"}, {"text": "levodopa", "type": "Chemical"}, {"text": "LIDs", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Levodopa is the most effective drug for the treatment of Parkinson 's disease .

Example answer:
{"entities": [{"text": "Levodopa", "type": "Chemical"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: Monkeys with acute ( short-term ) MPTP exposure , rapid symptom onset and short symptom duration prior to initiation of levodopa therapy developed dyskinesia between 11 and 24 days of daily levodopa administration .

Example answer:
{"entities": [{"text": "MPTP", "type": "Chemical"}, {"text": "levodopa", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : The United Kingdom Parkinson 's Disease Research Group ( UKPDRG ) trial found an increased mortality in patients with Parkinson 's disease ( PD ) randomized to receive 10 mg selegiline per day and L-dopa compared with those taking L-dopa alone .

Example answer:
{"entities": [{"text": "Parkinson 's Disease", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "selegiline", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}]}

Example input:
Sentence: Thirty PD patients participated in the study .

Example answer:
{"entities": [{"text": "PD", "type": "Disease"}]}

Input:
Sentence: METHODS : This is a cross-sectional study involving 95 patients with PD on uninterrupted levodopa therapy for at least 6 months .

## Item bc5cdr:test:4139
Example input:
Sentence: At termination of the experiments , mice underwent echocardiography , quantitation of abundance of molecular markers of CM ( ventricular mRNA encoding atrial natriuretic factor [ ANF ] and sarcoplasmic calcium ATPase [ SERCA2 ] ) , and determination of plasma LA .

Example answer:
{"entities": [{"text": "CM", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "LA", "type": "Chemical"}]}

Example input:
Sentence: 2 and 10 mg/kg/i.p. , or an equal volume of saline for the control group ( n = 20 ) ; 15 minutes later , all the animals were injected with a single 50 mg/kg/i.p .

Example answer:
{"entities": []}

Example input:
Sentence: For the cytoprotection study , animals were orally gavaged 100 mg/Kg GSPE for 7-10 days followed by i.p .

Example answer:
{"entities": [{"text": "GSPE", "type": "Chemical"}]}

Example input:
Sentence: 99mTc-glucarate was easy to prepare , stable for 96 h and was used to study its biodistribution in rats with isoproterenol-induced acute myocardial infarction .

Example answer:
{"entities": [{"text": "99mTc-glucarate", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: RESULTS : The selected doses of WR242511 , which produced significant methemoglobinemia in beagle dogs in earlier studies conducted elsewhere , produced very little MHb ( mean < 2.0 % ) in the rhesus monkey .

Example answer:
{"entities": [{"text": "WR242511", "type": "Chemical"}, {"text": "methemoglobinemia", "type": "Disease"}]}

Example input:
Sentence: Mitochondrial radiocalcium uptakes were significantly decreased in animals pretreated with acetylsalicylic acid or dipyridamole or when hydrocortisone was added to the epinephrine infusion ( 2,682,2,803 , and 3,424 counts per minute per gram of dried fraction , respectively ) .

Example answer:
{"entities": [{"text": "radiocalcium", "type": "Chemical"}, {"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine", "type": "Chemical"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: After a 30-min baseline measure of locomotor activity ( day 0 ) , animals were maintained on a cyclic diet of 12-h deprivation followed by 12-h access to 10 % sucrose solution and chow pellets ( 12 h access starting 4 h after onset of the dark period ) for 21 days .

Example answer:
{"entities": [{"text": "sucrose", "type": "Chemical"}]}

Example input:
Sentence: Using this rationale , the 8-aminoquinoline WR242511 , a potent long-lasting MHb former in rodents and beagle dogs , was studied in the rhesus monkey for advanced development as a potential CN pretreatment .

Example answer:
{"entities": [{"text": "8-aminoquinoline", "type": "Chemical"}, {"text": "WR242511", "type": "Chemical"}]}

Example input:
Sentence: The animals were mechanically ventilated to achieve normocarbia ( PCO2 = 42 +/- 1 mmHg , mean +/- SE ) .

Example answer:
{"entities": []}

Input:
Sentence: Animals used at M0 ( n = 8 ) were also used at moment -24 h of acute study .

## Item bc5cdr:test:4004
Example input:
Sentence: RESULTS : At 13 years after OLTX , the incidence of severe renal dysfunction was 18.1 % ( CRF 8.6 % and ESRD 9.5 % ) .

Example answer:
{"entities": [{"text": "renal dysfunction", "type": "Disease"}, {"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Follow-up MRIs were performed on 5 patients from third to 14th days after discontinuation of metronidazole administration .

Example answer:
{"entities": [{"text": "metronidazole", "type": "Chemical"}]}

Example input:
Sentence: The ocular hypotensive effects were statistically significant for apraclonidine-treated eyes throughout the study and also statistically significant for contralateral eyes from three hours after topical administration of 1 % apraclonidine .

Example answer:
{"entities": [{"text": "ocular hypotensive", "type": "Disease"}, {"text": "apraclonidine-treated", "type": "Chemical"}, {"text": "apraclonidine", "type": "Chemical"}]}

Example input:
Sentence: Whereas patient 1 showed lesions of up to 1 cm readily detectable on magnetic resonance imaging under prolonged co-trimoxazole treatment , therapy of patient 2 was switched early .

Example answer:
{"entities": [{"text": "co-trimoxazole", "type": "Chemical"}]}

Example input:
Sentence: Severe and long lasting cholestasis after high-dose co-trimoxazole treatment for Pneumocystis pneumonia in HIV-infected patients -- a report of two cases .

Example answer:
{"entities": [{"text": "cholestasis", "type": "Disease"}, {"text": "co-trimoxazole", "type": "Chemical"}, {"text": "Pneumocystis pneumonia", "type": "Disease"}, {"text": "HIV-infected", "type": "Disease"}]}

Example input:
Sentence: Amiodarone should be used with caution during long-term oral therapy in patients with or without clear intraventricular conduction defects .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "Chemical"}]}

Example input:
Sentence: OUTCOME : Following discontinuation of LEV , EEG and neuropsychological findings improved and seizure frequency decreased .

Example answer:
{"entities": [{"text": "LEV", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Although intravitreal aminoglycosides have substantially improved visual prognosis in endophthalmitis , macular infarction may impair full visual recovery .

Example answer:
{"entities": [{"text": "aminoglycosides", "type": "Chemical"}, {"text": "endophthalmitis", "type": "Disease"}, {"text": "infarction", "type": "Disease"}]}

Example input:
Sentence: Reports of persistent paralysis after the discontinuance of these drugs have most often involved aminosteroid-based NMBAs such as vecuronium bromide , especially when used in conjunction with corticosteroids .

Example answer:
{"entities": [{"text": "paralysis", "type": "Disease"}, {"text": "vecuronium bromide", "type": "Chemical"}]}

Example input:
Sentence: The patient 's ophthalmological symptoms improved rapidly 3 weeks after discontinuation of pegylated IFN alpha-2b and ribavirin .

Example answer:
{"entities": [{"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}]}

Input:
Sentence: Our report emphasizes the need for monitoring of visual function in patients on long-term linezolid treatment .

## Item bc5cdr:test:3943
Example input:
Sentence: Although preclinical and clinical findings suggest pulsatile stimulation of striatal postsynaptic receptors as a key mechanism underlying levodopa-induced dyskinesias , their pathogenesis is still unclear .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: Recent preclinical and clinical data from promising lines of research focus on the differential role of presynaptic versus postsynaptic mechanisms , dopamine receptor subtypes , ionotropic and metabotropic glutamate receptors , and non-dopaminergic neurotransmitter systems in the pathophysiology of levodopa-induced dyskinesias .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: Improvement of levodopa-induced dyskinesia by propranolol in Parkinson 's disease .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "propranolol", "type": "Chemical"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: Development of levodopa-induced dyskinesias in parkinsonian monkeys may depend upon rate of symptom onset and/or duration of symptoms .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "parkinsonian", "type": "Disease"}]}

Example input:
Sentence: There was a significant 40 % improvement in the dyskinesia score without increase of parkinsonian motor disability .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}, {"text": "parkinsonian", "type": "Disease"}, {"text": "motor disability", "type": "Disease"}]}

Example input:
Sentence: In contrast , monkeys with long-term MPTP exposure , slow symptom progression and/or long symptom duration prior to initiation of levodopa therapy were more resistant to developing LIDs ( e.g. , dyskinesia developed no sooner than 146 days of chronic levodopa administration ) .

Example answer:
{"entities": [{"text": "MPTP", "type": "Chemical"}, {"text": "levodopa", "type": "Chemical"}, {"text": "LIDs", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Repetitive transcranial magnetic stimulation for levodopa-induced dyskinesias in Parkinson 's disease .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: Levodopa-induced dyskinesias ( LIDs ) present a major problem for the long-term management of Parkinson 's disease ( PD ) patients .

Example answer:
{"entities": [{"text": "Levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "LIDs", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: Monkeys with acute ( short-term ) MPTP exposure , rapid symptom onset and short symptom duration prior to initiation of levodopa therapy developed dyskinesia between 11 and 24 days of daily levodopa administration .

Example answer:
{"entities": [{"text": "MPTP", "type": "Chemical"}, {"text": "levodopa", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Levodopa-induced dyskinesias in patients with Parkinson 's disease : filling the bench-to-bedside gap .

Example answer:
{"entities": [{"text": "Levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Input:
Sentence: Dyskinesia was present in 44 % ( n = 42 ) with median levodopa therapy of 3 years .

## Item bc5cdr:test:3945
Example input:
Sentence: Levodopa-induced dyskinesias in patients with Parkinson 's disease : filling the bench-to-bedside gap .

Example answer:
{"entities": [{"text": "Levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Switches to hypomania or mania occurred in 27 % of all patients ( N = 12 ) ( and in 24 % of the subgroup of patients treated with SSRIs [ 8/33 ] ) ; 16 % ( N = 7 ) experienced manic episodes , and 11 % ( N = 5 ) experienced hypomanic episodes .

Example answer:
{"entities": [{"text": "hypomania", "type": "Disease"}, {"text": "mania", "type": "Disease"}, {"text": "SSRIs", "type": "Chemical"}, {"text": "manic", "type": "Disease"}, {"text": "hypomanic", "type": "Disease"}]}

Example input:
Sentence: In a placebo-controlled , single-blinded , crossover study , we assessed the effect of `` real '' repetitive transcranial magnetic stimulation ( rTMS ) versus `` sham '' rTMS ( placebo ) on peak dose dyskinesias in patients with Parkinson 's disease ( PD ) .

Example answer:
{"entities": [{"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: However , comparison with the baseline showed small but significant reduction in dyskinesia severity following real rTMS but not placebo .

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
Sentence: However , the long-term use of this dopamine precursor is complicated by highly disabling fluctuations and dyskinesias .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: Ten patients with PD and prominent dyskinesias had rTMS ( 1,800 pulses ; 1 Hz rate ) delivered over the motor cortex for 4 consecutive days twice , once real stimuli and once sham stimulation were used ; evaluations were done at the baseline and 1 day after the end of each of the treatment series .

Example answer:
{"entities": [{"text": "PD", "type": "Disease"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: Similarly , in patient diaries , although both treatments caused reduction in subjective dyskinesia scores during the days of intervention , the effect was sustained for 3 days after the intervention for the real rTMS only .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: There was a significant 40 % improvement in the dyskinesia score without increase of parkinsonian motor disability .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}, {"text": "parkinsonian", "type": "Disease"}, {"text": "motor disability", "type": "Disease"}]}

Input:
Sentence: Eighty-one percent of patients with dyskinesia had clinical fluctuations .

## Item bc5cdr:test:3946
Example input:
Sentence: Seven patients suffering from Parkinson 's disease ( PD ) with severely disabling dyskinesia received low-dose propranolol as an adjunct to the currently used medical treatment .

Example answer:
{"entities": [{"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "propranolol", "type": "Chemical"}]}

Example input:
Sentence: Recent preclinical and clinical data from promising lines of research focus on the differential role of presynaptic versus postsynaptic mechanisms , dopamine receptor subtypes , ionotropic and metabotropic glutamate receptors , and non-dopaminergic neurotransmitter systems in the pathophysiology of levodopa-induced dyskinesias .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : The United Kingdom Parkinson 's Disease Research Group ( UKPDRG ) trial found an increased mortality in patients with Parkinson 's disease ( PD ) randomized to receive 10 mg selegiline per day and L-dopa compared with those taking L-dopa alone .

Example answer:
{"entities": [{"text": "Parkinson 's Disease", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "selegiline", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}]}

Example input:
Sentence: Repetitive transcranial magnetic stimulation for levodopa-induced dyskinesias in Parkinson 's disease .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: Improvement of levodopa-induced dyskinesia by propranolol in Parkinson 's disease .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "propranolol", "type": "Chemical"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: Levodopa-induced dyskinesias ( LIDs ) present a major problem for the long-term management of Parkinson 's disease ( PD ) patients .

Example answer:
{"entities": [{"text": "Levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "LIDs", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: In contrast , monkeys with long-term MPTP exposure , slow symptom progression and/or long symptom duration prior to initiation of levodopa therapy were more resistant to developing LIDs ( e.g. , dyskinesia developed no sooner than 146 days of chronic levodopa administration ) .

Example answer:
{"entities": [{"text": "MPTP", "type": "Chemical"}, {"text": "levodopa", "type": "Chemical"}, {"text": "LIDs", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: There was a significant 40 % improvement in the dyskinesia score without increase of parkinsonian motor disability .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}, {"text": "parkinsonian", "type": "Disease"}, {"text": "motor disability", "type": "Disease"}]}

Example input:
Sentence: Monkeys with acute ( short-term ) MPTP exposure , rapid symptom onset and short symptom duration prior to initiation of levodopa therapy developed dyskinesia between 11 and 24 days of daily levodopa administration .

Example answer:
{"entities": [{"text": "MPTP", "type": "Chemical"}, {"text": "levodopa", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Levodopa-induced dyskinesias in patients with Parkinson 's disease : filling the bench-to-bedside gap .

Example answer:
{"entities": [{"text": "Levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Input:
Sentence: Patients with dyskinesia had lower onset age ( p < 0.001 ) , longer duration of levodopa therapy ( p < 0.001 ) , longer disease duration ( p < 0.001 ) , higher total daily levodopa dose ( p < 0.001 ) , and higher total UPDRS scores ( p = 0.005 ) than patients without dyskinesia .

## Item bc5cdr:test:3834
Example input:
Sentence: Cerebral vasculitis associated with amphetamine abuse is well documented , and in rare cases ischaemic stroke has been reported after methylphenidate intake in children .

Example answer:
{"entities": [{"text": "Cerebral vasculitis", "type": "Disease"}, {"text": "amphetamine abuse", "type": "Disease"}, {"text": "ischaemic stroke", "type": "Disease"}, {"text": "methylphenidate", "type": "Chemical"}]}

Example input:
Sentence: Immunological activation has been proposed to play a role in methamphetamine-induced dopaminergic terminal damage .

Example answer:
{"entities": [{"text": "methamphetamine-induced", "type": "Chemical"}, {"text": "dopaminergic terminal damage", "type": "Disease"}]}

Example input:
Sentence: The prolonged depletion of dopamine in the striatum in mice , given multiple injections of methamphetamine , was also antagonized dose-dependently and completely by LY274614 .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "LY274614", "type": "Chemical"}]}

Example input:
Sentence: Cocaine-induced mood disorder : prevalence rates and psychiatric symptoms in an outpatient cocaine-dependent sample .

Example answer:
{"entities": [{"text": "Cocaine-induced", "type": "Chemical"}, {"text": "mood disorder", "type": "Disease"}, {"text": "psychiatric", "type": "Disease"}, {"text": "cocaine-dependent", "type": "Chemical"}]}

Example input:
Sentence: Attenuation of methamphetamine-induced nigrostriatal dopaminergic neurotoxicity in mice by lipopolysaccharide pretreatment .

Example answer:
{"entities": [{"text": "methamphetamine-induced", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "lipopolysaccharide", "type": "Chemical"}]}

Example input:
Sentence: Such systemic lipopolysaccharide treatment mitigated methamphetamine-induced striatal dopamine and 3,4-dihydroxyphenylacetic acid depletions in a dose-dependent manner .

Example answer:
{"entities": [{"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "methamphetamine-induced", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "3,4-dihydroxyphenylacetic acid", "type": "Chemical"}]}

Example input:
Sentence: In this study , we examined the roles of lipopolysaccharide , a pro-inflammatory and inflammatory factor , treatment in modulating the methamphetamine-induced nigrostriatal dopamine neurotoxicity .

Example answer:
{"entities": [{"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "methamphetamine-induced", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Dental patients abusing methamphetamine can present with poor oral hygiene , xerostomia , rampant caries ( `` meth mouth '' ) , and excessive tooth wear .

Example answer:
{"entities": [{"text": "methamphetamine", "type": "Chemical"}, {"text": "xerostomia", "type": "Disease"}, {"text": "caries", "type": "Disease"}, {"text": "meth", "type": "Chemical"}, {"text": "mouth", "type": "Disease"}, {"text": "tooth wear", "type": "Disease"}]}

Example input:
Sentence: Schizophrenia has been initially associated with dysfunction in dopamine neurotransmission .

Example answer:
{"entities": [{"text": "Schizophrenia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Methamphetamine is a very addictive , powerful stimulant that increases wakefulness and physical activity and can produce other effects such as cardiac dysrhythmias , hypertension , hallucinations , and violent behavior .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "Chemical"}, {"text": "cardiac dysrhythmias", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "hallucinations", "type": "Disease"}, {"text": "violent behavior", "type": "Disease"}]}

Input:
Sentence: The association between psychiatric co-morbidity and methamphetamine-induced psychosis was also studied .

## Item bc5cdr:test:3845
Example input:
Sentence: Although preclinical and clinical findings suggest pulsatile stimulation of striatal postsynaptic receptors as a key mechanism underlying levodopa-induced dyskinesias , their pathogenesis is still unclear .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: Ballistic and choreic dyskinesia were markedly ameliorated , whereas dystonia was not .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}, {"text": "dystonia", "type": "Disease"}]}

Example input:
Sentence: In 24 patients with this complication , the marked slowing of motor nerve conduction velocity and the electromyographic changes imply mainly a demyelinating disorder .

Example answer:
{"entities": [{"text": "demyelinating disorder", "type": "Disease"}]}

Example input:
Sentence: Development of levodopa-induced dyskinesias in parkinsonian monkeys may depend upon rate of symptom onset and/or duration of symptoms .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "parkinsonian", "type": "Disease"}]}

Example input:
Sentence: Levodopa-induced dyskinesias ( LIDs ) present a major problem for the long-term management of Parkinson 's disease ( PD ) patients .

Example answer:
{"entities": [{"text": "Levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "LIDs", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: L-DOPA-induced dyskinesia ( LID ) is among the motor complications that arise in Parkinson 's disease ( PD ) patients after a prolonged treatment with L-DOPA .

Example answer:
{"entities": [{"text": "L-DOPA-induced", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "LID", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "L-DOPA", "type": "Chemical"}]}

Example input:
Sentence: In a placebo-controlled , single-blinded , crossover study , we assessed the effect of `` real '' repetitive transcranial magnetic stimulation ( rTMS ) versus `` sham '' rTMS ( placebo ) on peak dose dyskinesias in patients with Parkinson 's disease ( PD ) .

Example answer:
{"entities": [{"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: Levodopa-induced dyskinesias in patients with Parkinson 's disease : filling the bench-to-bedside gap .

Example answer:
{"entities": [{"text": "Levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: Repetitive transcranial magnetic stimulation for levodopa-induced dyskinesias in Parkinson 's disease .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: In recent years , evidence from animal models of Parkinson 's disease has provided important information to understand the effect of specific receptor and post-receptor molecular mechanisms underlying the development of dyskinetic movements .

Example answer:
{"entities": [{"text": "Parkinson 's disease", "type": "Disease"}, {"text": "dyskinetic movements", "type": "Disease"}]}

Input:
Sentence: Cerebellar sensory processing alterations impact motor cortical plasticity in Parkinson 's disease : clues from dyskinetic patients .

## Item bc5cdr:test:4020
Example input:
Sentence: From January 1986 to January 2009 , 1223 consecutive ALF patients were evaluated : ATT alone was the cause in 70 ( 5.7 % ) patients .

Example answer:
{"entities": [{"text": "ALF", "type": "Disease"}]}

Example input:
Sentence: We describe a 15-yr-old girl who had orthotopic liver transplantation because of Wilson 's disease .

Example answer:
{"entities": [{"text": "Wilson 's disease", "type": "Disease"}]}

Example input:
Sentence: Twelve patients with liver disease related to methyldopa were seen between 1967 and 1977 .

Example answer:
{"entities": [{"text": "liver disease", "type": "Disease"}, {"text": "methyldopa", "type": "Chemical"}]}

Example input:
Sentence: Thirteen biopsies were performed from stable functioning renal allografts with informed consent ( nonepisode biopsy ) and the other 13 were from dysfunctional renal allografts with a clinical indication for biopsy ( episode biopsy ) .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : Twenty-six renal allograft biopsy specimens from 1 9 renal transplant patients who underwent transplantations between 1991 and 1993 were evaluated .

Example answer:
{"entities": []}

Example input:
Sentence: Hepatitis was usually reversible when treatment was stopped , with the results of liver function tests returning to normal after an average of 3.1 months .

Example answer:
{"entities": [{"text": "Hepatitis", "type": "Disease"}]}

Example input:
Sentence: Twenty-six had minimal prior therapy ( good risk ) , 23 had extensive prior therapy ( poor risk ) , and six had renal and/or hepatic dysfunction .

Example answer:
{"entities": []}

Example input:
Sentence: We describe a 70-year-old Hispanic woman who developed fulminant hepatic failure necessitating liver transplantation 10 weeks after conversion from simvastatin 40 mg/day to simvastatin 10 mg-ezetimibe 40 mg/day .

Example answer:
{"entities": [{"text": "fulminant hepatic failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "simvastatin 10 mg-ezetimibe 40", "type": "Chemical"}]}

Example input:
Sentence: Of 24 evaluable patients , two achieved a complete remission and one achieved a partial remission for an overall response rate of 12.5 % ( 95 % confidence interval : 2.6-32.4 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: She underwent liver transplantation with an uneventful postoperative course .

Example answer:
{"entities": []}

Input:
Sentence: METHOD : We retrospectively evaluated the medical records of 205 consecutive adult patients who underwent full-size liver transplantation between January 2006 and December 2010 due to end-stage or malignant liver disease .

## Item bc5cdr:test:4041
Example input:
Sentence: Fifteen polydrug ecstasy users and 15 polydrug non-ecstasy user controls completed a general drug use questionnaire , the Brixton Spatial Anticipation task ( set shifting ) , Backward Digit Span procedure ( memory updating ) , Inhibition of Return ( inhibition ) , an emotional intelligence scale , the Tromso Social Intelligence Scale and the Dysexecutive Questionnaire ( DEX ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: Ecstasy-specific hypoactivity was evident in the right dorsal anterior cingulated cortex ( ACC ) and left posterior cingulated cortex .

Example answer:
{"entities": [{"text": "Ecstasy-specific", "type": "Chemical"}]}

Example input:
Sentence: She reported her use of methamphetamine for five years and had not experienced any major carious episodes before she started using the drug .

Example answer:
{"entities": [{"text": "methamphetamine", "type": "Chemical"}, {"text": "carious episodes", "type": "Disease"}]}

Example input:
Sentence: These results elucidated ecstasy-related deficits , only some of which might be attributed to cannabis use .

Example answer:
{"entities": [{"text": "ecstasy-related", "type": "Chemical"}, {"text": "cannabis", "type": "Chemical"}]}

Example input:
Sentence: To address the potential confounding effects of the cannabis use of the ecstasy using group , a second analysis included 14 previously tested cannabis users ( Nestor , L. , Roberts , G. , Garavan , H. , Hester , R. , 2008 .

Example answer:
{"entities": [{"text": "cannabis", "type": "Chemical"}, {"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: These data lend further support to the proposal that cognitive processes mediated by the prefrontal cortex may be impaired by recreational ecstasy use .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: Learning and memory deficits in ecstasy users and their neural correlates during a face-learning task .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: In addition , working memory processing in ecstasy users has been shown to be associated with neural alterations in hippocampal and/or cortical regions as measured by functional magnetic resonance imaging ( fMRI ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: Ecstasy users performed significantly worse in learning and memory compared to controls and cannabis users .

Example answer:
{"entities": [{"text": "Ecstasy", "type": "Chemical"}, {"text": "cannabis", "type": "Chemical"}]}

Example input:
Sentence: It has been consistently shown that ecstasy users display impairments in learning and memory performance .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Input:
Sentence: Strikingly , despite prolonged abstinence ( mean , 4.98 ; range , 4-9 years ) , past ecstasy users showed few signs of recovery .

## Item bc5cdr:test:3264
Example input:
Sentence: Further studies are needed to determine the most appropriate nucleoside or nucleotide analogue for antiviral prophylaxis during CT and the optimal duration of administration after completion of CT .

Example answer:
{"entities": [{"text": "nucleoside", "type": "Chemical"}, {"text": "nucleotide", "type": "Chemical"}]}

Example input:
Sentence: The drugs commonly used are cyclophosphamide and chlorambucil ( alkylating agents ) , azathioprine ( purine analogue ) , and methotrexate ( folic acid analogue ) .

Example answer:
{"entities": [{"text": "cyclophosphamide", "type": "Chemical"}, {"text": "chlorambucil", "type": "Chemical"}, {"text": "alkylating agents", "type": "Chemical"}, {"text": "azathioprine", "type": "Chemical"}, {"text": "purine", "type": "Chemical"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "folic acid", "type": "Chemical"}]}

Example input:
Sentence: Recent reports indicate that single agent therapy with vinorelbine ( VNB ) or gemcitabine ( GEM ) may obtain a response rate of 20-30 % in elderly patients , with acceptable toxicity and improvement in symptoms and quality of life .

Example answer:
{"entities": [{"text": "vinorelbine", "type": "Chemical"}, {"text": "VNB", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "GEM", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: After 154 courses of therapy , the median dose intensity was 131 mg/m ( 2 ) for paclitaxel ( 97.3 % ) , 117 mg/m ( 2 ) for cisplatin ( 97.3 % ) , and 1378 mg/m ( 2 ) for gemcitabine ( 86.2 % ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Example input:
Sentence: Thirty-five consecutive chemotherapy-naive patients with Stage IV NSCLC and an Eastern Cooperative Oncology Group performance status of 0-2 were treated with a combination of paclitaxel ( 135 mg/m ( 2 ) given intravenously in 3 hours ) on Day 1 , cisplatin ( 120 mg/m ( 2 ) given intravenously in 6 hours ) on Day 1 , and gemcitabine ( 800 mg/m ( 2 ) given intravenously in 30 minutes ) on Days 1 and 8 , every 4 weeks .

Example answer:
{"entities": [{"text": "NSCLC", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}]}

Example input:
Sentence: Mean peak forced expiratory volume in 1 second ( FEV1 ) increases over baseline and the proportion of patients attaining at least a 15 % increase in the FEV1 ( responders ) were 31 % and 90 % , respectively , for ipratropium and 17 % and 50 % , respectively , for theophylline .

Example answer:
{"entities": [{"text": "ipratropium", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}]}

Example input:
Sentence: Combination chemotherapy with mitoxantrone , high-dose 5-fluorouracil ( 5-FU ) and leucovorin ( MFL regimen ) had been reported as an effective and well tolerated regimen .

Example answer:
{"entities": [{"text": "mitoxantrone", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "leucovorin", "type": "Chemical"}, {"text": "MFL regimen", "type": "Chemical"}]}

Example input:
Sentence: Seventy-five human immunodeficiency virus ( HIV ) -infected patients with CD4+ cell counts < 500/mm3 were randomized to receive either ZDV ( 500 mg daily ) alone ( group I , n = 38 ) or in combination with folinic acid ( 15 mg daily ) and intramascular vitamin B12 ( 1000 micrograms monthly ) ( group II , n = 37 ) .

Example answer:
{"entities": [{"text": "human immunodeficiency virus ( HIV ) -infected", "type": "Disease"}, {"text": "ZDV", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}, {"text": "vitamin B12", "type": "Chemical"}]}

Example input:
Sentence: The use and toxicity of didanosine ( ddI ) in HIV antibody-positive individuals intolerant to zidovudine ( AZT ) One hundred and fifty-one patients intolerant to zidovudine ( AZT ) received didanosine ( ddI ) to a maximum dose of 12.5 mg/kg/day .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "didanosine", "type": "Chemical"}, {"text": "ddI", "type": "Chemical"}, {"text": "HIV antibody-positive", "type": "Disease"}, {"text": "zidovudine", "type": "Chemical"}, {"text": "AZT", "type": "Chemical"}]}

Input:
Sentence: The most common regimens were 3TC + d4T + nevirapine ( NVP ) ( 54.8 % ) , zidovudine ( AZT ) + 3TC + NVP ( 14.5 % ) , 3TC + d4T + efavirenz ( EFV ) ( 20.1 % ) , and AZT + 3TC + EFV ( 5.4 % ) .

## Item bc5cdr:test:4195
Example input:
Sentence: The mean age of these patients was the same as for the entire group , 64 years .

Example answer:
{"entities": []}

Example input:
Sentence: Eight Crohn 's disease patients were included .

Example answer:
{"entities": [{"text": "Crohn 's disease", "type": "Disease"}]}

Example input:
Sentence: The characteristics of the 48 patients in the possible cases were similar .

Example answer:
{"entities": []}

Example input:
Sentence: Patients received a minimum of three courses unless progressive disease was detected .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : One hundred patients were enrolled .

Example answer:
{"entities": []}

Example input:
Sentence: PG was well tolerated by all 54 patients .

Example answer:
{"entities": [{"text": "PG", "type": "Chemical"}]}

Example input:
Sentence: Nineteen patients finished the trial , and in 18 cases the therapeutic result was considered very good to good .

Example answer:
{"entities": []}

Example input:
Sentence: Three patients had no change and disease progressed in two .

Example answer:
{"entities": []}

Example input:
Sentence: The patients were randomly allocated to one of three groups ; those in group A ( n = 10 ) were subjected to controlled hypotension alone , those in group B ( n = 10 ) to haemodilution alone and those in group C ( n = 10 ) to both controlled hypotension and haemodilution .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}]}

Example input:
Sentence: Finally , 15 patients were excluded from the study ( noncompliance 14 , death 1 ) ; thus , 60 patients ( 31 in group I and 29 in group II ) were eligible for analysis .

Example answer:
{"entities": [{"text": "death", "type": "Disease"}]}

Input:
Sentence: Patients were divided into three groups and each group had 20 patients .

## Item bc5cdr:test:3730
Example input:
Sentence: The rats received AChE reactivator pralidoxime-2-chloride ( 2PAM ) ( 30.0 mg/kg BW ) , anticonvulsant diazepam ( 2.0 mg/kg BW ) , A ( 1 ) -adenosine receptor agonist N ( 6 ) -cyclopentyl adenosine ( CPA ) ( 2.0 mg/kg BW ) , NMDA-receptor antagonist dizocilpine maleate ( +-MK801 hydrogen maleate ) ( 2.0 mg/kg BW ) or their combinations with cholinolytic drug atropine sulfate ( 50.0 mg/kg BW ) immediately or 30 min after the single SC injection of DFP .

Example answer:
{"entities": [{"text": "pralidoxime-2-chloride", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "N ( 6 ) -cyclopentyl adenosine", "type": "Chemical"}, {"text": "CPA", "type": "Chemical"}, {"text": "NMDA-receptor", "type": "Chemical"}, {"text": "dizocilpine maleate", "type": "Chemical"}, {"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: We report an undiagnosed case of myotonia congenita in a 24-year-old previously healthy primigravida , who developed life threatening masseter spasm following a standard dose of intravenous suxamethonium for induction of anaesthesia .

Example answer:
{"entities": [{"text": "myotonia congenita", "type": "Disease"}, {"text": "masseter spasm", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: The full syndrome of subacute myelo-optic neuropathy was more frequent in women , but they tended to have taken greater quantities of the drug .

Example answer:
{"entities": []}

Example input:
Sentence: In all of 7 patients examined acutely , gallbladder contractility was inhibited after a single 100-micrograms injection .

Example answer:
{"entities": []}

Example input:
Sentence: Monkeys with acute ( short-term ) MPTP exposure , rapid symptom onset and short symptom duration prior to initiation of levodopa therapy developed dyskinesia between 11 and 24 days of daily levodopa administration .

Example answer:
{"entities": [{"text": "MPTP", "type": "Chemical"}, {"text": "levodopa", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: In contrast , monkeys with long-term MPTP exposure , slow symptom progression and/or long symptom duration prior to initiation of levodopa therapy were more resistant to developing LIDs ( e.g. , dyskinesia developed no sooner than 146 days of chronic levodopa administration ) .

Example answer:
{"entities": [{"text": "MPTP", "type": "Chemical"}, {"text": "levodopa", "type": "Chemical"}, {"text": "LIDs", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Reports of persistent paralysis after the discontinuance of these drugs have most often involved aminosteroid-based NMBAs such as vecuronium bromide , especially when used in conjunction with corticosteroids .

Example answer:
{"entities": [{"text": "paralysis", "type": "Disease"}, {"text": "vecuronium bromide", "type": "Chemical"}]}

Example input:
Sentence: Of the 20 animals that received subarachnoid injection of 2-chloroprocaine-CE seven ( 35 % ) developed hind-limb paralysis .

Example answer:
{"entities": [{"text": "2-chloroprocaine-CE", "type": "Chemical"}, {"text": "paralysis", "type": "Disease"}]}

Example input:
Sentence: None of the animals that received bupivacaine , normal saline , or normal saline titrated to a pH 3.0 developed hind-limb paralysis .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}, {"text": "paralysis", "type": "Disease"}]}

Input:
Sentence: The incidence of abductor paralysis after Botox injection for ADSD was 0.34 % .

## Item bc5cdr:test:4032
Example input:
Sentence: Mild hypoxia ( SO2 < 90 % ) was the most common event ( 11 patients ) ; 3 patients ( 2 % ) presented transient hypoxia due to upper airway obstruction by probe introduction and 8 ( 5.8 % ) due to hypoxia caused by MZ use .

Example answer:
{"entities": [{"text": "hypoxia", "type": "Disease"}, {"text": "airway obstruction", "type": "Disease"}, {"text": "MZ", "type": "Chemical"}]}

Example input:
Sentence: A brain imaging study and repetitive nerve stimulation test indicated no abnormality .

Example answer:
{"entities": []}

Example input:
Sentence: However , use of BZDs/RDs was associated with dizziness , inability to sleep after awaking at night and tiredness in the mornings during the week prior to admission and with stronger depressive symptoms measured at the beginning of the hospital stay .

Example answer:
{"entities": [{"text": "BZDs/RDs", "type": "Chemical"}, {"text": "dizziness", "type": "Disease"}, {"text": "inability to sleep", "type": "Disease"}, {"text": "tiredness", "type": "Disease"}, {"text": "depressive symptoms", "type": "Disease"}]}

Example input:
Sentence: Pneumonitis , bilateral pleural effusions , echocardiographic evidence of cardiac tamponade , and positive autoantibodies developed in a 43-year-old man , who was receiving long-term sulfasalazine therapy for chronic ulcerative colitis .

Example answer:
{"entities": [{"text": "Pneumonitis", "type": "Disease"}, {"text": "pleural effusions", "type": "Disease"}, {"text": "cardiac tamponade", "type": "Disease"}, {"text": "sulfasalazine", "type": "Chemical"}, {"text": "ulcerative colitis", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : A 72-year-old white man with underlying human immunodeficiency virus , atrial fibrillation , coronary artery disease , and hyperlipidemia presented with generalized pain , fatigue , and dark orange urine for 3 days .

Example answer:
{"entities": [{"text": "human immunodeficiency virus", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "coronary artery disease", "type": "Disease"}, {"text": "hyperlipidemia", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "fatigue", "type": "Disease"}]}

Example input:
Sentence: Severe distress was noted in the recovery phase in two patients .

Example answer:
{"entities": []}

Example input:
Sentence: Further signs were hyperhidrosis , hypersalivation , bronchorrhoea , and severe miosis ; the electrocardiographic finding was atrio-ventricular dissociation .

Example answer:
{"entities": [{"text": "hyperhidrosis", "type": "Disease"}, {"text": "hypersalivation", "type": "Disease"}, {"text": "bronchorrhoea", "type": "Disease"}, {"text": "miosis", "type": "Disease"}, {"text": "atrio-ventricular dissociation", "type": "Disease"}]}

Example input:
Sentence: A case of genuine stress incontinence due to prazosin , a common antihypertensive drug , is presented .

Example answer:
{"entities": [{"text": "stress incontinence", "type": "Disease"}, {"text": "prazosin", "type": "Chemical"}]}

Example input:
Sentence: One patient was prematurely discontinued from the study for severe headache and abdominal pain .

Example answer:
{"entities": [{"text": "headache", "type": "Disease"}, {"text": "abdominal pain", "type": "Disease"}]}

Example input:
Sentence: He was awake , revealed no changes of mental status and at rest there were no further motor symptoms .

Example answer:
{"entities": []}

Input:
Sentence: There was no evidence of any recent stress or status migrainosus .

## Item bc5cdr:test:3898
Example input:
Sentence: We also used microdialysis to measure basal and potassium-stimulated acetylcholine ( ACh ) release in the CA1 region of the hippocampus .

Example answer:
{"entities": [{"text": "potassium-stimulated", "type": "Chemical"}, {"text": "acetylcholine", "type": "Chemical"}, {"text": "ACh", "type": "Chemical"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: The density of hippocampal neurons in the brains of animals treated with BMCs was markedly preserved .

Example answer:
{"entities": []}

Example input:
Sentence: NRA0160 and clozapine antagonized locomotor hyperactivity induced by methamphetamine ( MAP ) in mice .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "MAP", "type": "Chemical"}]}

Example input:
Sentence: In both ecstasy and cannabis groups brain activation was decreased in the right medial frontal gyrus , left parahippocampal gyrus , left dorsal cingulate gyrus , and left caudate .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}, {"text": "cannabis", "type": "Chemical"}]}

Example input:
Sentence: In vitro , gamma-HCH , pentylenetetrazol and picrotoxin were shown to inhibit 3H-TBOB binding in mouse whole brain , with IC50 values of 4.6 , 404 and 9.4 microM , respectively .

Example answer:
{"entities": [{"text": "gamma-HCH", "type": "Chemical"}, {"text": "pentylenetetrazol", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "3H-TBOB", "type": "Chemical"}]}

Example input:
Sentence: Alpha2ABC-/- mice were completely unresponsive to the analgesic and hypnotic effects of clonidine ; however , clonidine significantly lowered heart rate in alpha2ABC-/- mice by up to 150 bpm .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: NFkappaB activity was decreased in the frontal cortex of cocaine treated rats , as well as GSH concentration and glutathione peroxidase activity in the hippocampus , whereas nNOS activity in the hippocampus was increased .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}]}

Example input:
Sentence: reduced significantly the brain acetylcholinesterase activity and cholesterol levels in young and aged mice .

Example answer:
{"entities": [{"text": "cholesterol", "type": "Chemical"}]}

Example input:
Sentence: When hippocampal ACh was measured during testing for handling-induced convulsions , extracellular ACh was significantly elevated ( 192 % ) in WSP mice , but was nonsignificantly elevated ( 59 % ) in WSR mice .

Example answer:
{"entities": [{"text": "ACh", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}]}

Input:
Sentence: AChE activity was significantly decreased in the hippocampus of mice with BPA compared to control mice , whereas no difference was found in the prefrontal cortex , hypothalamus and cerebellum .
