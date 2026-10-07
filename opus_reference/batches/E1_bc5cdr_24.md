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

## Item bc5cdr:test:4672
Example input:
Sentence: STUDY OBJECTIVE : To evaluate the frequency of venous thromboembolism ( VTE ) in patients with advanced androgen-independent prostate cancer who were treated with docetaxel alone or in combination with thalidomide .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "VTE", "type": "Disease"}, {"text": "prostate cancer", "type": "Disease"}, {"text": "docetaxel", "type": "Chemical"}, {"text": "thalidomide", "type": "Chemical"}]}

Example input:
Sentence: Forty-three ovarian cancer patients were available for analysis following six cycles of the same PAC-containing regimen : 23 had been supplemented by glutamate all along the treatment period , at a daily dose of three times 500 mg ( group G ) , and 20 had received a placebo ( group P ) .

Example answer:
{"entities": [{"text": "ovarian cancer", "type": "Disease"}, {"text": "PAC-containing", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: Treatment was comprised of VNB , 25 mg/m ( 2 ) , plus GEM , 1000 mg/m ( 2 ) , both on Days 1 , 8 , and 15 every 28 days .

Example answer:
{"entities": [{"text": "VNB", "type": "Chemical"}, {"text": "GEM", "type": "Chemical"}]}

Example input:
Sentence: Recent reports indicate that single agent therapy with vinorelbine ( VNB ) or gemcitabine ( GEM ) may obtain a response rate of 20-30 % in elderly patients , with acceptable toxicity and improvement in symptoms and quality of life .

Example answer:
{"entities": [{"text": "vinorelbine", "type": "Chemical"}, {"text": "VNB", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "GEM", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : The combination of GEM and VNB is moderately active and well tolerated except in patients age > /= 75 years .

Example answer:
{"entities": [{"text": "GEM", "type": "Chemical"}, {"text": "VNB", "type": "Chemical"}]}

Example input:
Sentence: In both cases , discontinuation of FK506 and treatment with plasma exchange , fresh frozen plasma replacement , corticosteroids , aspirin , and dipyridamole led to resolution of MAHA .

Example answer:
{"entities": [{"text": "FK506", "type": "Chemical"}, {"text": "corticosteroids", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "MAHA", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : The addition of thalidomide to docetaxel in the treatment of prostate cancer significantly increases the frequency of VTE .

Example answer:
{"entities": [{"text": "thalidomide", "type": "Chemical"}, {"text": "docetaxel", "type": "Chemical"}, {"text": "prostate cancer", "type": "Disease"}, {"text": "VTE", "type": "Disease"}]}

Example input:
Sentence: We studied 20 patients receiving long-term carbonic anhydrase inhibitor treatment for periodic paralysis and myotonia .

Example answer:
{"entities": [{"text": "paralysis", "type": "Disease"}, {"text": "myotonia", "type": "Disease"}]}

Example input:
Sentence: Although responding patients were scheduled to receive consolidation radiotherapy and 24 patients received preplanned second-line chemotherapy after disease progression , the response and toxicity rates reported refer only to the chemotherapy regimen given .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Combination chemotherapy with mitoxantrone , high-dose 5-fluorouracil ( 5-FU ) and leucovorin ( MFL regimen ) had been reported as an effective and well tolerated regimen .

Example answer:
{"entities": [{"text": "mitoxantrone", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "leucovorin", "type": "Chemical"}, {"text": "MFL regimen", "type": "Chemical"}]}

Input:
Sentence: The VTD regimen may be safe and effective as a consolidation therapy in the treatment of MM in Japanese population .

## Item bc5cdr:test:4853
Example input:
Sentence: Our findings indicate that beta2-adrenoceptor overstimulation during an early critical period results in microglial activation associated with innate neuroinflammatory pathways and behavioral abnormalities , similar to those described in autism .

Example answer:
{"entities": [{"text": "behavioral abnormalities", "type": "Disease"}, {"text": "autism", "type": "Disease"}]}

Example input:
Sentence: On a low-salt ( LS ) diet , male DS had higher levels of intrarenal angiotensinogen mRNA than females .

Example answer:
{"entities": []}

Example input:
Sentence: This toxicity appeared in patients receiving the higher doses of desferrioxamine or coincided with the normalization of ferritin or aluminium serum levels .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "desferrioxamine", "type": "Chemical"}, {"text": "aluminium", "type": "Chemical"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: Although the explanation for the association between artery calcification and growth status can not be determined from the present study , there was a relationship between higher serum phosphate and susceptibility to artery calcification , with 30 % higher levels of serum phosphate in young , ad libitum-fed rats compared with either of the groups that was resistant to Warfarin-induced artery calcification , ie , the 10-month-old rats and the restricted-diet , growth-inhibited young rats .

Example answer:
{"entities": [{"text": "artery calcification", "type": "Disease"}, {"text": "phosphate", "type": "Chemical"}, {"text": "Warfarin-induced", "type": "Chemical"}]}

Example input:
Sentence: Treatment-related adverse events ( AEs ) occurred in 44 % and 52 % , 57 % , and 41 % of the asenapine at 5 and 10 mg BID , haloperidol , and placebo groups , respectively .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: METHODS : The son of an 84-year-old male discovered a newspaper report stating clinical success with plant extracts in Alzheimer 's disease .

Example answer:
{"entities": [{"text": "Alzheimer 's disease", "type": "Disease"}]}

Example input:
Sentence: A 34-year-old lady developed a constellation of dermatitis , fever , lymphadenopathy and hepatitis , beginning on the 17th day of a course of oral sulphasalazine for sero-negative rheumatoid arthritis .

Example answer:
{"entities": [{"text": "dermatitis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "lymphadenopathy", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : This study establishes a TAA model by periarterial CaCl ( 2 ) exposure in rats , and demonstrates a significant elevation of expression of MMP-2 , MMP-9 , ADAM10 and ADAM17 in the pathogenesis of vascular remodeling .

Example answer:
{"entities": [{"text": "TAA", "type": "Disease"}, {"text": "CaCl ( 2 )", "type": "Chemical"}]}

Example input:
Sentence: In addition to genetic influences , recent studies suggest that prenatal drug or chemical exposures are risk factors for autism .

Example answer:
{"entities": [{"text": "autism", "type": "Disease"}]}

Input:
Sentence: Mechanisms Underlying Latent Disease Risk Associated with Early-Life Arsenic Exposure : Current Research Trends and Scientific Gaps .

## Item bc5cdr:test:4468
Example input:
Sentence: Intravenous administration of a single 50-mg bolus of lidocaine in a 67-year-old man resulted in profound depression of the activity of the sinoatrial and atrioventricular nodal pacemakers .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: We describe a patient who developed dilated cardiomyopathy and clinical congestive heart failure after 2 months of therapy with amphotericin B ( AmB ) for disseminated coccidioidomycosis .

Example answer:
{"entities": [{"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}, {"text": "AmB", "type": "Chemical"}, {"text": "coccidioidomycosis", "type": "Disease"}]}

Example input:
Sentence: We report the case of a 30-year-old Caucasian man who came to the emergency department in atrial fibrillation with rapid ventricular response .

Example answer:
{"entities": [{"text": "atrial fibrillation", "type": "Disease"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Amiodarone should be used with caution during long-term oral therapy in patients with or without clear intraventricular conduction defects .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "Chemical"}]}

Example input:
Sentence: A patient with sinuatrial disease and implanted pacemaker was treated with amiodarone ( maximum dose 1000 mg , maintenance dose 800 mg daily ) for 10 months , for control of supraventricular tachyarrhythmias .

Example answer:
{"entities": [{"text": "sinuatrial disease", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "supraventricular tachyarrhythmias", "type": "Disease"}]}

Example input:
Sentence: Thirty days after amiodarone discontinuation , His bundle electrograms showed atrial flutter without intra-Hisian or infra-Hisian delay .

Example answer:
{"entities": [{"text": "amiodarone", "type": "Chemical"}, {"text": "atrial flutter", "type": "Disease"}]}

Example input:
Sentence: Reduction in the dosage of amiodarone resulted in the disappearance of the sinoatrial block and the persistence of asymptomatic sinus bradycardia .

Example answer:
{"entities": [{"text": "amiodarone", "type": "Chemical"}, {"text": "sinoatrial block", "type": "Disease"}, {"text": "sinus bradycardia", "type": "Disease"}]}

Example input:
Sentence: A case is presented of a reversible intra-Hisian block occurring under amiodarone treatment for atrial tachycardia in a patient without clear intraventricular conduction abnormalities .

Example answer:
{"entities": [{"text": "intra-Hisian block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atrial tachycardia", "type": "Disease"}, {"text": "intraventricular conduction abnormalities", "type": "Disease"}]}

Example input:
Sentence: We observed sinoatrial block due to chronic amiodarone administration in a 5-year-old boy with primary cardiomyopathy , Wolff-Parkinson-White syndrome and supraventricular tachycardia .

Example answer:
{"entities": [{"text": "sinoatrial block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "primary cardiomyopathy", "type": "Disease"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "supraventricular tachycardia", "type": "Disease"}]}

Input:
Sentence: A 62-year-old man was found to have bradycardia , hypothermia and respiratory failure 3 weeks after initiation of amiodarone therapy for atrial fibrillation .

## Item bc5cdr:test:4739
Example input:
Sentence: Myopathy , associated in some cases with myoglobinuria , and in 2 cases with transient renal failure , has been rarely reported with lovastatin , especially in patients concomitantly treated with cyclosporin , gemfibrozil or niacin .

Example answer:
{"entities": [{"text": "Myopathy", "type": "Disease"}, {"text": "myoglobinuria", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}, {"text": "lovastatin", "type": "Chemical"}, {"text": "cyclosporin", "type": "Chemical"}, {"text": "gemfibrozil", "type": "Chemical"}, {"text": "niacin", "type": "Chemical"}]}

Example input:
Sentence: Simvastatinezetimibe and escitalopram ( which she was taking for depression ) were discontinued , and other potential causes of hepatotoxicity were excluded .

Example answer:
{"entities": [{"text": "Simvastatinezetimibe", "type": "Chemical"}, {"text": "escitalopram", "type": "Chemical"}, {"text": "depression", "type": "Disease"}, {"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: Severe rhabdomyolysis and acute renal failure secondary to concomitant use of simvastatin , amiodarone , and atazanavir .

Example answer:
{"entities": [{"text": "rhabdomyolysis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: Lovastatin and simvastatin are both effective and well-tolerated agents for lowering elevated levels of serum cholesterol .

Example answer:
{"entities": [{"text": "Lovastatin", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "cholesterol", "type": "Chemical"}]}

Example input:
Sentence: Amiodarone and atazanavir are recognized CYP3A4 inhibitors .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVE : To report a case of a severe interaction between simvastatin , amiodarone , and atazanavir resulting in rhabdomyolysis and acute renal failure .

Example answer:
{"entities": [{"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}, {"text": "rhabdomyolysis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: DISCUSSION : The risk of rhabdomyolysis is increased in the presence of concomitant drugs that inhibit simvastatin metabolism .

Example answer:
{"entities": [{"text": "rhabdomyolysis", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}]}

Example input:
Sentence: Lovastatin and simvastatin are the 2 best-known members of the class of hypolipidaemic agents known as HMG CoA reductase inhibitors .

Example answer:
{"entities": [{"text": "Lovastatin", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}]}

Example input:
Sentence: Simvastatin is metabolized by CYP3A4 .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}]}

Example input:
Sentence: In patients requiring the concurrent use of statins and CYP3A4 inhibitors , pravastatin , fluvastatin , and rosuvastatin carry the lowest risk of drug interactions ; atorvastatin carries moderate risk , whereas simvastatin and lovastatin have the highest risk and should be avoided in patients taking concomitant CYP3A4 inhibitors .

Example answer:
{"entities": [{"text": "statins", "type": "Chemical"}, {"text": "pravastatin", "type": "Chemical"}, {"text": "fluvastatin", "type": "Chemical"}, {"text": "rosuvastatin", "type": "Chemical"}, {"text": "atorvastatin", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "lovastatin", "type": "Chemical"}]}

Input:
Sentence: Clarithromycin is the most documented cytochrome P450 3A4 ( CYP3A4 ) inhibitor to cause an adverse interaction with simvastatin .

## Item bc5cdr:test:4740
Example input:
Sentence: Based on a score of 8 on the Naranjo adverse drug reaction probability scale , telithromycin was the probable cause of acute hepatitis in this patient , and pathological findings suggested drug-induced toxic hepatitis .

Example answer:
{"entities": [{"text": "adverse drug reaction", "type": "Disease"}, {"text": "telithromycin", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}, {"text": "toxic hepatitis", "type": "Disease"}]}

Example input:
Sentence: Although the transaminases gradually returned to baseline after withholding the beta lactam antibiotic , there was a gradual increase in serum bilirubin and a decrease in hemoglobin concentration caused by an autoimmune hemolytic anemia and erythroblastocytopenia .

Example answer:
{"entities": [{"text": "beta lactam", "type": "Chemical"}, {"text": "bilirubin", "type": "Chemical"}, {"text": "autoimmune hemolytic anemia", "type": "Disease"}, {"text": "erythroblastocytopenia", "type": "Disease"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: We have described a unique patient who had reversible and dose-related myasthenia gravis after penicillamine and chloroquine therapy for rheumatoid arthritis .

Example answer:
{"entities": [{"text": "myasthenia gravis", "type": "Disease"}, {"text": "penicillamine", "type": "Chemical"}, {"text": "chloroquine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Example input:
Sentence: Two weeks after the initiation of therapy , her hematocrit had decreased from 44.1 % to 20.4 % , and she had a positive direct Coombs antiglobulin test and an elevated indirect bilirubin .

Example answer:
{"entities": [{"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: The case of a schizophrenic patient is reported to illustrate massive rhabdomyolysis and subsequent acute renal failure following molindone administration .

Example answer:
{"entities": [{"text": "schizophrenic", "type": "Disease"}, {"text": "rhabdomyolysis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "molindone", "type": "Chemical"}]}

Example input:
Sentence: A case of massive rhabdomyolysis following molindone administration .

Example answer:
{"entities": [{"text": "rhabdomyolysis", "type": "Disease"}, {"text": "molindone", "type": "Chemical"}]}

Example input:
Sentence: Severe rhabdomyolysis and acute renal failure secondary to concomitant use of simvastatin , amiodarone , and atazanavir .

Example answer:
{"entities": [{"text": "rhabdomyolysis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: Rhabdomyolysis is a potentially lethal syndrome that psychiatric patients seem predisposed to develop .

Example answer:
{"entities": [{"text": "Rhabdomyolysis", "type": "Disease"}, {"text": "psychiatric", "type": "Disease"}]}

Example input:
Sentence: DISCUSSION : The risk of rhabdomyolysis is increased in the presence of concomitant drugs that inhibit simvastatin metabolism .

Example answer:
{"entities": [{"text": "rhabdomyolysis", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}]}

Input:
Sentence: This particular case is of interest as rhabdomyolysis only occurred after an increase in the dose of clarithromycin .

## Item bc5cdr:test:4824
Example input:
Sentence: METHODS : Neonatal rats were treated with the tricyclic antidepressant clomipramine or vehicle between days 9 and 16 twice daily and behaviorally tested in adulthood .

Example answer:
{"entities": [{"text": "antidepressant", "type": "Chemical"}, {"text": "clomipramine", "type": "Chemical"}]}

Example input:
Sentence: The effects of exercise on the severity of isoproterenol-induced myocardial infarction were studied in female albino rats of 20,40,60 and 80 weeks of age .

Example answer:
{"entities": [{"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Adult rats given dexamethasone on days 15 and 16 of gestation had more glomeruli with glomerulosclerosis than control rats .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: Six- to 9-month old rats receiving prenatal dexamethasone on days 17 and 18 of gestation had a 17 % reduction in glomeruli ( 23 380+/-587 ) compared with control rats ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Drugs were separately , orally once daily dosed to pregnant rats from day 8 to 21 ( GD1=plug day ) .

Example answer:
{"entities": []}

Example input:
Sentence: Male Wistar rats were implanted bilaterally with cannulae into the accumbens shell or core , and then were locally injected with GR 55562 ( an antagonist of 5-HT1B receptors ) or CP 93129 ( an agonist of 5-HT1B receptors ) .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Example input:
Sentence: Pregnant rats were given either vehicle or 2 daily intraperitoneal injections of dexamethasone ( 0.2 mg/kg body weight ) on gestational days 11 and 12 , 13 and 14 , 15 and 16 , 17 and 18 , or 19 and 20 .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}]}

Example input:
Sentence: Male rats that received prenatal dexamethasone on days 15 and 16 , 17 and 18 , and 13 and 14 of gestation had elevated blood pressures at 6 months of age ; the latter group did not have a reduction in glomerular number .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "elevated blood pressures", "type": "Disease"}, {"text": "reduction in glomerular number", "type": "Disease"}]}

Example input:
Sentence: Offspring of rats administered dexamethasone on days 15 and 16 gestation had a 20 % reduction in glomerular number compared with control at 6 to 9 months of age ( 22 527+/-509 versus 28 050+/-561 , P < 0.05 ) , which was comparable to the percent reduction in glomeruli measured at 3 weeks of age .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "reduction in glomerular number", "type": "Disease"}]}

Example input:
Sentence: Pregnant rats were administered one of these calcium channel blockers during the period of cardiac morphogenesis and the offspring examined on day 20 of gestation for cardiovascular malformations .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "cardiovascular malformations", "type": "Disease"}]}

Input:
Sentence: A rat model of IUGR was established by PCE , male fetuses and adult offspring at the age of postnatal week 24 were euthanized .

## Item bc5cdr:test:4766
Example input:
Sentence: Isoproterenol-treated rats showed significant increases in the levels of lactate dehydrogenase , aspartate transaminase , creatine kinase and malondialdehyde and significant decreases in the activities of superoxide dismutase , catalase and glutathione peroxidase in serum and heart .

Example answer:
{"entities": [{"text": "Isoproterenol-treated", "type": "Chemical"}, {"text": "lactate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "creatine", "type": "Chemical"}, {"text": "malondialdehyde", "type": "Chemical"}, {"text": "superoxide", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}]}

Example input:
Sentence: The results show that pretreatment with TCR may be useful in preventing the damage induced by isoproterenol in rat heart .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/", "type": "Chemical"}, {"text": "K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}]}

Example input:
Sentence: Pretreatment of TCR , at a dose of 0.5 mL/100 g bodyweight per day , orally for 30 days , prevented the increase in lipid peroxidation and activity of marker enzymes observed in isoproterenol-induced rats ( 85 mg kg ( -1 ) s. c. for 2 days at an interval of 24 h ) .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: In isolated perfused heart preparations from isoproterenol-pretreated rats , the isoproterenol-induced maximal increase in left ventricular systolic pressure was significantly reduced , compared with saline-pretreated rats ( the EC50 of the isoproterenol-induced increase in left ventricular systolic pressure was enhanced approximately 22-fold ) .

Example answer:
{"entities": [{"text": "isoproterenol-pretreated", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: Isoproterenol pretreatment for 15 days caused cardiac hypertrophy without affecting baseline blood pressure and heart rate .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "Chemical"}, {"text": "cardiac hypertrophy", "type": "Disease"}]}

Example input:
Sentence: Effect of green tea and vitamin E combination in isoproterenol induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: 99mTc-glucarate for detection of isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "99mTc-glucarate", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: The effects of exercise on the severity of isoproterenol-induced myocardial infarction were studied in female albino rats of 20,40,60 and 80 weeks of age .

Example answer:
{"entities": [{"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Histological studies demonstrated that the rats developed an infarct 18 h after isoproterenol administration .

Example answer:
{"entities": [{"text": "infarct", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}]}

Input:
Sentence: Acute myocardial ischemic injury was induced in rats by subcutaneous injection of isoproterenol ( 85 mg/kg ) , for two consecutive days .

## Item bc5cdr:test:4784
Example input:
Sentence: We report an undiagnosed case of myotonia congenita in a 24-year-old previously healthy primigravida , who developed life threatening masseter spasm following a standard dose of intravenous suxamethonium for induction of anaesthesia .

Example answer:
{"entities": [{"text": "myotonia congenita", "type": "Disease"}, {"text": "masseter spasm", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: Anticoagulant-induced femoral nerve palsy represents the most common form of warfarin-induced peripheral neuropathy ; it is characterized by severe pain in the inguinal region , varying degrees of motor and sensory impairment , and flexure contracture of the involved extremity .

Example answer:
{"entities": [{"text": "femoral nerve palsy", "type": "Disease"}, {"text": "warfarin-induced", "type": "Chemical"}, {"text": "peripheral neuropathy", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "motor and sensory impairment", "type": "Disease"}, {"text": "contracture", "type": "Disease"}]}

Example input:
Sentence: Surgery revealed the right radial nerve to be severely compressed by the densely fibrotic lateral head of the triceps .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : We present the first case report of a woman with hyperthyroidism treated with propylthiouracil in whom a syndrome of pericarditis , fever , and glomerulonephritis developed .

Example answer:
{"entities": [{"text": "hyperthyroidism", "type": "Disease"}, {"text": "propylthiouracil", "type": "Chemical"}, {"text": "pericarditis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "glomerulonephritis", "type": "Disease"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: We present the case of a 28-year-old man on chronic warfarin therapy who sustained a minor muscle tear and developed increasing pain and a flexure contracture of the right hip .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "muscle tear", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "contracture", "type": "Disease"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Example input:
Sentence: In a 37-year-old woman with documented pentazocine-induced fibrous myopathy of triceps and deltoid muscles bilaterally and a three-week history of right wrist drop , electrodiagnostic examination showed a severe but partial lesion of the right radial nerve distal to the branches to the triceps , in addition to the fibrous myopathy .

Example answer:
{"entities": [{"text": "pentazocine-induced", "type": "Chemical"}, {"text": "fibrous myopathy", "type": "Disease"}]}

Example input:
Sentence: A 49-year-old woman was transferred to our department because of quadriparesis , lancinating pain , sensory loss , and paresthesia of the distal limbs .

Example answer:
{"entities": [{"text": "quadriparesis", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "sensory loss", "type": "Disease"}, {"text": "paresthesia", "type": "Disease"}]}

Example input:
Sentence: CLINICAL FEATURES : A 50-year-old woman with low back and right leg pain was scheduled for epidural steroid injection .

Example answer:
{"entities": [{"text": "steroid", "type": "Chemical"}]}

Input:
Sentence: MATERIAL AND METHOD : A 40-year-old woman presented with decreased sensation and paresthesia over her right lateral forearm ; the paresthesia had occurred after a steroid injection in the right lateral epicondyle 3 months before .

## Item bc5cdr:test:4855
Example input:
Sentence: Thyroid disorders , illicit drug or stimulant use , and acute alcohol intoxication are among these causes .

Example answer:
{"entities": [{"text": "Thyroid disorders", "type": "Disease"}, {"text": "acute alcohol intoxication", "type": "Disease"}]}

Example input:
Sentence: Unlike general toxicity data , their prenatal toxic effects were not extensively studied before .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Comparative cognitive and subjective side effects of immediate-release oxycodone in healthy middle-aged and older adults .

Example answer:
{"entities": [{"text": "oxycodone", "type": "Chemical"}]}

Example input:
Sentence: Thyroid-stimulating hormone , magnesium , and potassium levels were within normal limits , urine drug screen was negative , and alcohol use was denied .

Example answer:
{"entities": [{"text": "magnesium", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}, {"text": "alcohol", "type": "Chemical"}]}

Example input:
Sentence: Less frequent toxic effects included thrombocytopenia , anemia , nausea , mild alopecia , phlebitis , and mucositis .

Example answer:
{"entities": [{"text": "thrombocytopenia", "type": "Disease"}, {"text": "anemia", "type": "Disease"}, {"text": "nausea", "type": "Disease"}, {"text": "alopecia", "type": "Disease"}, {"text": "phlebitis", "type": "Disease"}, {"text": "mucositis", "type": "Disease"}]}

Example input:
Sentence: This toxicity appeared in patients receiving the higher doses of desferrioxamine or coincided with the normalization of ferritin or aluminium serum levels .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "desferrioxamine", "type": "Chemical"}, {"text": "aluminium", "type": "Chemical"}]}

Example input:
Sentence: Grade 3-4 adverse effects included myelosuppression , fatigue , somnolence/depressed mood , neuropathy and dyspnea .

Example answer:
{"entities": [{"text": "myelosuppression", "type": "Disease"}, {"text": "fatigue", "type": "Disease"}, {"text": "somnolence/depressed mood", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}, {"text": "dyspnea", "type": "Disease"}]}

Example input:
Sentence: This animal model may be useful to explore the mechanisms by which prenatal nutritional deficiency enhances risk for schizophrenia in humans and may also have implications for developmental processes leading to differential sensitivity to drugs of abuse .

Example answer:
{"entities": [{"text": "nutritional deficiency", "type": "Disease"}, {"text": "schizophrenia", "type": "Disease"}]}

Example input:
Sentence: PERSPECTIVE : Study findings indicate that the metabolism , neurocognitive effects , and physical side effects of oral oxycodone are similar for healthy middle-aged and older adults .

Example answer:
{"entities": [{"text": "oxycodone", "type": "Chemical"}]}

Example input:
Sentence: Long-term use was associated with daytime and night-time symptoms indicative of poorer health and potentially caused by the adverse effects of these drugs .

Example answer:
{"entities": []}

Input:
Sentence: Inorganic As exposure during key developmental periods is associated with a variety of adverse health effects including those that are evident in adulthood .

## Item bc5cdr:test:4811
Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: These 13 included cases of malignant hypertension , thrombotic microangiopathy , lupus nephritis , Henoch-Schonlein nephritis , crescentic glomerulonephritis , and cocaine-related acute renal failure .

Example answer:
{"entities": [{"text": "malignant hypertension", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "lupus nephritis", "type": "Disease"}, {"text": "Henoch-Schonlein nephritis", "type": "Disease"}, {"text": "glomerulonephritis", "type": "Disease"}, {"text": "cocaine-related", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: This report documents the unusual occurrence of rapidly progressive glomerulonephritis with crescents and fibrillar glomerulonephritis in a patient treated with rifampin .

Example answer:
{"entities": [{"text": "glomerulonephritis", "type": "Disease"}, {"text": "rifampin", "type": "Chemical"}]}

Example input:
Sentence: This drug occasionally has been associated with acute interstitial nephritis in native kidneys .

Example answer:
{"entities": [{"text": "interstitial nephritis", "type": "Disease"}]}

Example input:
Sentence: Nested within the cohort , a matched case-control study was performed to estimate the association between cyclophosphamide and bladder cancer using odds ratios ( ORs ) as relative risk .

Example answer:
{"entities": [{"text": "cyclophosphamide", "type": "Chemical"}, {"text": "bladder cancer", "type": "Disease"}]}

Example input:
Sentence: The risk of developing renal papillary necrosis or cancer of the renal pelvis , ureter or bladder associated with consumption of either phenacetin or paracetamol was calculated from data acquired by questionnaire from 381 cases and 808 controls .

Example answer:
{"entities": [{"text": "renal papillary necrosis", "type": "Disease"}, {"text": "phenacetin", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: This case study reveals an unusual finding of rapidly proliferative crescentic glomerulonephritis in a patient treated with rifampin who had no other identifiable causes for developing this disease .

Example answer:
{"entities": [{"text": "glomerulonephritis", "type": "Disease"}, {"text": "rifampin", "type": "Chemical"}]}

Example input:
Sentence: PTCR also occurs in certain native kidney diseases , though the association is not as strong as that for TG .

Example answer:
{"entities": [{"text": "kidney diseases", "type": "Disease"}, {"text": "TG", "type": "Disease"}]}

Example input:
Sentence: The risk of renal papillary necrosis was increased nearly 20-fold by consumption of phenacetin , which also increased the risk for cancer of the renal pelvis and bladder but not for ureteric cancer .

Example answer:
{"entities": [{"text": "renal papillary necrosis", "type": "Disease"}, {"text": "phenacetin", "type": "Chemical"}, {"text": "ureteric cancer", "type": "Disease"}]}

Example input:
Sentence: By contrast , we were unable to substantiate an increased risk from paracetamol consumption for renal papillary necrosis or any of these cancers although there was a suggestion of an association with cancer of the ureter .

Example answer:
{"entities": [{"text": "paracetamol", "type": "Chemical"}, {"text": "renal papillary necrosis", "type": "Disease"}, {"text": "cancers", "type": "Disease"}, {"text": "cancer of the ureter", "type": "Disease"}]}

Input:
Sentence: Newly identified links to kidney cancer and associations with aggressive prostate cancer require further evaluation .

## Item bc5cdr:test:4692
Example input:
Sentence: Twenty children with acute lymphoblastic leukemia who developed meningeal disease were treated with a high-dose intravenous methotrexate regimen that was designed to achieve and maintain CSF methotrexate concentrations of 10 ( -5 ) mol/L without the need for concomitant intrathecal dosing .

Example answer:
{"entities": [{"text": "acute lymphoblastic leukemia", "type": "Disease"}, {"text": "meningeal disease", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: The patient 's ophthalmological symptoms improved rapidly 3 weeks after discontinuation of pegylated IFN alpha-2b and ribavirin .

Example answer:
{"entities": [{"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: Oral administration of CBZ as an aqueous suspension every 8 h at a dose of 250 mg/kg was continuously protective against HFDE-induced seizures and was minimally toxic as measured by weight gain over 8 weeks of treatment .

Example answer:
{"entities": [{"text": "CBZ", "type": "Chemical"}, {"text": "HFDE-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}]}

Example input:
Sentence: However , we experienced a case of severe ocular and orbital toxicity after intracarotid injection of carboplatin , which is infrequently reported .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : When performing intracarotid injection of carboplatin , we must be aware of its potentially blinding ocular toxicity .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}, {"text": "ocular toxicity", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Currently accepted intravitreal antibiotic regimens may cause retinal toxicity and macular ischaemia .

Example answer:
{"entities": [{"text": "retinal toxicity", "type": "Disease"}, {"text": "ischaemia", "type": "Disease"}]}

Example input:
Sentence: The ocular hypotensive effects were statistically significant for apraclonidine-treated eyes throughout the study and also statistically significant for contralateral eyes from three hours after topical administration of 1 % apraclonidine .

Example answer:
{"entities": [{"text": "ocular hypotensive", "type": "Disease"}, {"text": "apraclonidine-treated", "type": "Chemical"}, {"text": "apraclonidine", "type": "Chemical"}]}

Example input:
Sentence: The ocular myasthenia associated with combination therapy of pegylated IFN alpha-2b and ribavirin for CHC is very rarely reported ; therefore , we present this case with a review of the various eye complications of IFN therapy .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "CHC", "type": "Disease"}, {"text": "IFN", "type": "Chemical"}]}

Example input:
Sentence: Severe ocular and orbital toxicity after intracarotid injection of carboplatin for recurrent glioblastomas .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}, {"text": "glioblastomas", "type": "Disease"}]}

Example input:
Sentence: Development of ocular myasthenia during pegylated interferon and ribavirin treatment for chronic hepatitis C. A 63-year-old male experienced sudden diplopia after 9 weeks of administration of pegylated interferon ( IFN ) alpha-2b and ribavirin for chronic hepatitis C ( CHC ) .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated interferon", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "chronic hepatitis", "type": "Disease"}, {"text": "diplopia", "type": "Disease"}, {"text": "pegylated interferon ( IFN ) alpha-2b", "type": "Chemical"}, {"text": "chronic hepatitis C", "type": "Disease"}, {"text": "CHC", "type": "Disease"}]}

Input:
Sentence: Safety and efficacy of fluocinolone acetonide intravitreal implant ( 0.59 mg ) in birdshot retinochoroidopathy .

## Item bc5cdr:test:4758
Example input:
Sentence: Echocardiographic data from the experimental group of 21 patients ( mean age 16 +/- 5 years ) treated from 1.6 to 14.3 years ( median 5.3 ) before this study with 27 to 532 mg/m2 of doxorubicin ( mean 196 ) were compared with echocardiographic data from 12 normal age-matched control subjects .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "Chemical"}]}

Example input:
Sentence: A 17-day-old infant on isoniazid therapy 13 mg/kg daily from birth because of maternal tuberculosis was admitted after 4 days of clonic fits .

Example answer:
{"entities": [{"text": "isoniazid", "type": "Chemical"}, {"text": "tuberculosis", "type": "Disease"}, {"text": "clonic fits", "type": "Disease"}]}

Example input:
Sentence: METHODS : a total of 13 patients were referred to the Danish Cholinesterase Research Unit after ECT during 38 months .

Example answer:
{"entities": []}

Example input:
Sentence: In the bolus group , 26.0 % ( 13/50 ) had akathisia compared with 32.7 % ( 16/49 ) in the infusion group ( Delta=-6.7 % ; 95 % confidence interval [ CI ] -24.6 % to 11.2 % ) .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: The mean age of patients in the 16 probable cases was 57.9 , with hepatotoxicity being more common in women .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: Five females and 6 males , 21-59 years of age , were examined with a 1.5-T whole-body system using a circular polarized head coil .

Example answer:
{"entities": []}

Example input:
Sentence: Ages ranged from 4 months to 17 years ; 58 patients were males and 42 females .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : Forty-nine patients with advanced NSCLC were included , 38 of whom were age > /= 70 years and 11 were age < 70 years but who had some contraindication to receiving cisplatin .

Example answer:
{"entities": [{"text": "NSCLC", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: Eleven patients ( six male ) with median age 47 years ( range 27-73 ) , median disease duration 50 months ( range 9-178 ) and median follow-up period of patients 13.8 months ( range 5-27 ) were enrolled in this study .

Example answer:
{"entities": []}

Input:
Sentence: A total of 350 patients ( 215 [ 61.4 % ] < 5 years of age and 135 [ 38.6 % ] > 5 years of age ) were followed-up after treatment with injectable artesunate for severe malaria in hospitals and health centers of the Democratic Republic of the Congo .

## Item bc5cdr:test:4631
Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: In this study , we investigated whether increased generation of FR during status epilepticus would be sufficient to provoke abnormalities in mtDNA and in the expression and activity of cytochrome c oxidase ( CCO ) , complex IV of the respiratory chain , in the chronic phase of the pilocarpine model of temporal lobe epilepsy .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}, {"text": "temporal lobe epilepsy", "type": "Disease"}]}

Example input:
Sentence: The in vitro data suggest that the site responsible for the decrease in seizure activity 24 h after gamma-HCH may be the GABA-A receptor-linked chloride channel .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}, {"text": "GABA-A", "type": "Chemical"}]}

Example input:
Sentence: Treatment with 150 mg/kg PDTC before and following status epilepticus significantly increased the mortality rate to 100 % .

Example answer:
{"entities": [{"text": "PDTC", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: The effect of PDTC on status epilepticus-associated cell loss in the hippocampus and piriform cortex was evaluated in the rat fractionated pilocarpine model .

Example answer:
{"entities": [{"text": "PDTC", "type": "Chemical"}, {"text": "status", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: Similar to rats , systemic pilocarpine injection causes status epilepticus ( SE ) and the eventual development of spontaneous seizures and mossy fiber sprouting in C57BL/6 and CD1 mice , but the physiological correlates of these events have not been identified in mice .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Based on the finding that VPU and VPA could protect the animals against pilocarpine-induced seizure it is suggested that the reduction of inhibitory amino acid neurotransmitters was comparatively minor and offset by a pronounced reduction of glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: Therefore , like VPA , the finding that VPU could drastically reduce pilocarpine-induced increases in glutamate and aspartate should account , at least partly , for its anticonvulsant activity observed in pilocarpine-induced seizure in experimental animals .

Example answer:
{"entities": [{"text": "VPA", "type": "Chemical"}, {"text": "VPU", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Input:
Sentence: The results indicate that GFC can exert anticonvulsant activity and reduce the frequency of installation of pilocarpine-induced status epilepticus , as demonstrated by increase in latency to first seizure and decrease in mortality rate of animals .

## Item bc5cdr:test:4719
Example input:
Sentence: When comparing all lithium treated versus non-lithium-treated groups , lithium caused a reduction in glomerular filtration rate ( GFR ) without significant changes in effective renal plasma flow ( as determined by a marker secreted into the proximal tubules ) or lithium clearance .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: The effect of amiloride on lithium-induced polydipsia and polyuria and on the lithium concentration in the plasma , brain , kidney , thyroid and red blood cells was investigated in rats , chronically treated with LiCl .

Example answer:
{"entities": [{"text": "amiloride", "type": "Chemical"}, {"text": "lithium-induced", "type": "Chemical"}, {"text": "polydipsia", "type": "Disease"}, {"text": "polyuria", "type": "Disease"}, {"text": "lithium", "type": "Chemical"}, {"text": "LiCl", "type": "Chemical"}]}

Example input:
Sentence: Upregulation of the expression of vasopressin gene in the paraventricular and supraoptic nuclei of the lithium-induced diabetes insipidus rat .

Example answer:
{"entities": [{"text": "vasopressin", "type": "Chemical"}, {"text": "lithium-induced", "type": "Chemical"}, {"text": "diabetes insipidus", "type": "Disease"}]}

Example input:
Sentence: It is concluded that acute amiloride administration to lithium-treated patients suffering from polydipsia and polyuria might relieve these patients but prolonged amiloride supplementation would result in elevated lithium levels and might be hazardous .

Example answer:
{"entities": [{"text": "amiloride", "type": "Chemical"}, {"text": "lithium-treated", "type": "Chemical"}, {"text": "polydipsia", "type": "Disease"}, {"text": "polyuria", "type": "Disease"}, {"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : We report seven cases where substitution of lithium , either fully or partially , with divalproex sodium was extremely helpful in reducing the cognitive , motivational , or creative deficits attributed to lithium in our bipolar patients .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}, {"text": "divalproex sodium", "type": "Chemical"}, {"text": "cognitive , motivational , or creative deficits", "type": "Disease"}, {"text": "bipolar", "type": "Disease"}]}

Example input:
Sentence: Lithium-associated cognitive and functional deficits reduced by a switch to divalproex sodium : a case series .

Example answer:
{"entities": [{"text": "Lithium-associated", "type": "Chemical"}, {"text": "cognitive and functional deficits", "type": "Disease"}, {"text": "divalproex sodium", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : In this preliminary report , divalproex sodium was a superior alternative to lithium in bipolar patients experiencing cognitive deficits , loss of creativity , and functional impairments .

Example answer:
{"entities": [{"text": "divalproex sodium", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "bipolar", "type": "Disease"}, {"text": "cognitive deficits", "type": "Disease"}, {"text": "loss of creativity", "type": "Disease"}, {"text": "functional impairments", "type": "Disease"}]}

Example input:
Sentence: Rats with lithium-induced nephropathy were subjected to high protein ( HP ) feeding , uninephrectomy ( NX ) or a combination of these , in an attempt to induce glomerular hyperfiltration and further progression of renal failure .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: Attenuation of the lithium-induced diabetes-insipidus-like syndrome by amiloride in rats .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "Chemical"}, {"text": "diabetes-insipidus-like syndrome", "type": "Disease"}, {"text": "amiloride", "type": "Chemical"}]}

Example input:
Sentence: In all the experiments , the attenuation of the lithium-induced diabetes-insipidus-like syndrome by amiloride was accompanied by a reduction of the ratio between the lithium concentration in the renal medulla and its levels in the blood and an elevation in the plasma potassium level .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "Chemical"}, {"text": "diabetes-insipidus-like syndrome", "type": "Disease"}, {"text": "amiloride", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}]}

Input:
Sentence: Lithium , an effective antipsychotic , induces nephrogenic diabetes insipidus ( NDI ) in 40 % of patients .

## Item bc5cdr:test:4736
Example input:
Sentence: Nimodipine treatment resulted in a statistically significant reduction in systolic BP ( SBP ) and diastolic BP ( DBP ) from baseline compared with placebo during the first few days .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "Chemical"}, {"text": "reduction in systolic BP", "type": "Disease"}]}

Example input:
Sentence: Amantadine treatment produced a biphasic effect on mouse motility .

Example answer:
{"entities": [{"text": "Amantadine", "type": "Chemical"}]}

Example input:
Sentence: L-DOPA-induced dyskinesia ( LID ) is among the motor complications that arise in Parkinson 's disease ( PD ) patients after a prolonged treatment with L-DOPA .

Example answer:
{"entities": [{"text": "L-DOPA-induced", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "LID", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "L-DOPA", "type": "Chemical"}]}

Example input:
Sentence: Levodopa-induced dyskinesias ( LIDs ) present a major problem for the long-term management of Parkinson 's disease ( PD ) patients .

Example answer:
{"entities": [{"text": "Levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "LIDs", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: Acute reserpine and subchronic haloperidol treatments change synaptosomal brain glutamate uptake and elicit orofacial dyskinesia in rats .

Example answer:
{"entities": [{"text": "reserpine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "orofacial dyskinesia", "type": "Disease"}]}

Example input:
Sentence: In a placebo-controlled , single-blinded , crossover study , we assessed the effect of `` real '' repetitive transcranial magnetic stimulation ( rTMS ) versus `` sham '' rTMS ( placebo ) on peak dose dyskinesias in patients with Parkinson 's disease ( PD ) .

Example answer:
{"entities": [{"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: In the present study , the authors induced orofacial dyskinesia by acute reserpine and subchronic haloperidol administration to rats .

Example answer:
{"entities": [{"text": "orofacial dyskinesia", "type": "Disease"}, {"text": "reserpine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: Reserpine- and haloperidol-induced orofacial dyskinesia are putative animal models of tardive dyskinesia ( TD ) whose pathophysiology has been related to free radical generation and oxidative stress .

Example answer:
{"entities": [{"text": "Reserpine-", "type": "Chemical"}, {"text": "haloperidol-induced", "type": "Chemical"}, {"text": "orofacial dyskinesia", "type": "Disease"}, {"text": "tardive dyskinesia", "type": "Disease"}, {"text": "TD", "type": "Disease"}]}

Input:
Sentence: We conclude that amlodipine can cause dysguesia .

## Item bc5cdr:test:4832
Example input:
Sentence: Severe hematologic toxicity ( neutrophil count < 1000/mm3 and/or hemoglobin < 8 g/dl ) occurred in 4 patients assigned to group I and 7 assigned to group II .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: The aim of the study was to assess the clinical significance of genetic variants in butyrylcholinesterase gene ( BCHE ) in patients with a suspected prolonged duration of action of succinylcholine after ECT .

Example answer:
{"entities": [{"text": "succinylcholine", "type": "Chemical"}]}

Example input:
Sentence: Beyond 8 days of DES exposure , the immunochemically PRL-positive proportion of cells increased to over 50 % of the total population .

Example answer:
{"entities": [{"text": "DES", "type": "Chemical"}]}

Example input:
Sentence: Autoantibodies against P450 2E1 or P58 , previously associated with halothane hepatitis , were detected in the serum of five affected workers .

Example answer:
{"entities": [{"text": "halothane hepatitis", "type": "Disease"}]}

Example input:
Sentence: An experiment was performed to test whether inclusion of phenobarbital in a choline-devoid diet would increase the hepatocarcinogenicity of the diet .

Example answer:
{"entities": [{"text": "phenobarbital", "type": "Chemical"}, {"text": "choline-devoid", "type": "Chemical"}]}

Example input:
Sentence: Cancer patients who are chronic carriers of HBV have a higher hepatic complication rate while receiving cytotoxic chemotherapy ( CT ) and this has mainly been attributed to HBV reactivation .

Example answer:
{"entities": [{"text": "Cancer", "type": "Disease"}, {"text": "hepatic complication", "type": "Disease"}]}

Example input:
Sentence: INTERPRETATION : Repeated exposure of human beings to HCFCs 123 and 124 can result in serious liver injury in a large proportion of the exposed population .

Example answer:
{"entities": [{"text": "liver injury", "type": "Disease"}]}

Example input:
Sentence: Patients treated with alkylating agents have an increased risk of development of acute nonlymphocytic leukemia , and both alkylating agents and azathioprine are associated with the development of non-Hodgkin 's lymphoma .

Example answer:
{"entities": [{"text": "alkylating agents", "type": "Chemical"}, {"text": "acute nonlymphocytic leukemia", "type": "Disease"}, {"text": "azathioprine", "type": "Chemical"}, {"text": "non-Hodgkin 's lymphoma", "type": "Disease"}]}

Example input:
Sentence: The incidence of preneoplastic nodules and of hepatocellular carcinomas was 10 % and 37 % , respectively , in rats fed the plain choline-devoid diet , and 17 % and 30 % , in rats fed the phenobarbital-containing choline-devoid diet .

Example answer:
{"entities": [{"text": "hepatocellular carcinomas", "type": "Disease"}, {"text": "choline-devoid", "type": "Chemical"}, {"text": "phenobarbital-containing", "type": "Chemical"}]}

Example input:
Sentence: We investigated an epidemic of liver disease in nine industrial workers who had had repeated accidental exposure to a mixture of 1,1-dichloro-2,2,2-trifluoroethane ( HCFC 123 ) and 1-chloro-1,2,2,2-tetrafluoroethane ( HCFC 124 ) .

Example answer:
{"entities": [{"text": "liver disease", "type": "Disease"}, {"text": "1,1-dichloro-2,2,2-trifluoroethane", "type": "Chemical"}, {"text": "HCFC 123", "type": "Chemical"}, {"text": "1-chloro-1,2,2,2-tetrafluoroethane", "type": "Chemical"}, {"text": "HCFC 124", "type": "Chemical"}]}

Input:
Sentence: UNASSIGNED : Epidemiological studies of 1,3-butadiene have suggest that exposures to humans are associated with chronic myeloid leukemia ( CML ) .

## Item bc5cdr:test:4610
Example input:
Sentence: These data indicate that a critical percentage of NTE inhibition in brain and spinal cord sampled shortly after Mipafox exposure can predict neuropathic damage in rats several weeks later .

Example answer:
{"entities": [{"text": "Mipafox", "type": "Chemical"}, {"text": "neuropathic damage", "type": "Disease"}]}

Example input:
Sentence: Peripheral neuropathy has been noted as a complication of therapy with perhexiline maleate , a drug widely used in France ( and in clinical trials in the United States ) for the prophylactic treatment of angina pectoris .

Example answer:
{"entities": [{"text": "Peripheral neuropathy", "type": "Disease"}, {"text": "perhexiline maleate", "type": "Chemical"}, {"text": "angina pectoris", "type": "Disease"}]}

Example input:
Sentence: This pilot trial aimed to evaluate the role of glutamate supplementation for preventing PAC-induced peripheral neuropathy in a randomized , placebo-controlled , double-blinded clinical and electro-diagnostic study .

Example answer:
{"entities": [{"text": "glutamate", "type": "Chemical"}, {"text": "PAC-induced", "type": "Chemical"}, {"text": "peripheral neuropathy", "type": "Disease"}]}

Example input:
Sentence: In six of the probable cases the neurological disturbance consisted of an acute reversible encephalopathy usually related to the ingestion of a high dose of clioquinol over a short period .

Example answer:
{"entities": [{"text": "neurological disturbance", "type": "Disease"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "clioquinol", "type": "Chemical"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: This was a case of acute palsy of the recurrent laryngeal nerve and superimposed severe acute sensorimotor axonal polyneuropathy caused by high-dose disulfiram intoxication .

Example answer:
{"entities": [{"text": "palsy", "type": "Disease"}, {"text": "polyneuropathy", "type": "Disease"}, {"text": "disulfiram", "type": "Chemical"}]}

Example input:
Sentence: Isoniazid was the most frequent agent in drug-induced neuropathy .

Example answer:
{"entities": [{"text": "Isoniazid", "type": "Chemical"}, {"text": "neuropathy", "type": "Disease"}]}

Example input:
Sentence: The correlation between neuropathic damage and inhibition of neurotoxic esterase or neuropathy target enzyme ( NTE ) was examined in rats acutely exposed to Mipafox ( N , N'-diisopropylphosphorodiamidofluoridate ) , a neurotoxic organophosphate .

Example answer:
{"entities": [{"text": "neuropathic damage", "type": "Disease"}, {"text": "neurotoxic", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}, {"text": "Mipafox", "type": "Chemical"}, {"text": "N , N'-diisopropylphosphorodiamidofluoridate", "type": "Chemical"}, {"text": "organophosphate", "type": "Chemical"}]}

Example input:
Sentence: The full syndrome of subacute myelo-optic neuropathy was more frequent in women , but they tended to have taken greater quantities of the drug .

Example answer:
{"entities": []}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Input:
Sentence: Ethambutol is known to cause optic neuropathy and , more rarely , axonal polyneuropathy .

## Item bc5cdr:test:4846
Example input:
Sentence: METHODS : Forty-nine patients with advanced NSCLC were included , 38 of whom were age > /= 70 years and 11 were age < 70 years but who had some contraindication to receiving cisplatin .

Example answer:
{"entities": [{"text": "NSCLC", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: Based on this principle a 27-year old woman , classified as being in the high-risk group ( Goldstein and Berkowitz score : 11 ) , was treated with multiple cytotoxic drugs .

Example answer:
{"entities": []}

Example input:
Sentence: It has shown promising results alone or in combination with other chemotherapeutic agents in colorectal , breast , pancreaticobiliary , gastric , renal cell and head and neck cancers .

Example answer:
{"entities": []}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : The combination of paclitaxel , cisplatin , and gemcitabine is well tolerated and shows high activity in metastatic NSCLC .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "NSCLC", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Although the prevalence of nonsmall cell lung carcinoma ( NSCLC ) is high among elderly patients , few data are available regarding the efficacy and toxicity of chemotherapy in this group of patients .

Example answer:
{"entities": [{"text": "nonsmall cell lung carcinoma", "type": "Disease"}, {"text": "NSCLC", "type": "Disease"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Associated factors were co-treatment with other centrally antimuscarinic agents , poor clinical outcome , older age , and longer hospitalization ( by 17.5 days , increasing cost ) ; sex , diagnosis or medical co-morbidity , and daily clozapine dose , which fell with age , were unrelated .

Example answer:
{"entities": [{"text": "clozapine", "type": "Chemical"}]}

Example input:
Sentence: The MFL regimen achieves little palliative benefit and induces severe toxicity at a fairly high rate .

Example answer:
{"entities": [{"text": "MFL regimen", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Treatment duration longer than 1 year was associated with an eightfold increased risk ( OR = 7.7 , 95 % CI 0.9 to 69 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Preliminary results of an Eastern Cooperative Oncology Group study of single-agent paclitaxel ( Taxol ; Bristol-Myers Squibb Company , Princeton , NJ ) reported a 37 % response rate in patients with head and neck cancer , and the paclitaxel/cisplatin combination has been used successfully and has significantly improved median response duration in ovarian cancer patients .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "Taxol", "type": "Chemical"}, {"text": "head and neck cancer", "type": "Disease"}, {"text": "paclitaxel/cisplatin", "type": "Chemical"}, {"text": "ovarian cancer", "type": "Disease"}]}

Input:
Sentence: We saw no association between metolachlor use and incidence of all cancers combined ( n = 5,701 with a 5-year lag ) or most site-specific cancers .

## Item bc5cdr:test:4608
Example input:
Sentence: However , L-dopa restored the bradycardia caused by norepinephrine in addition to decreasing blood pressure and heart rate .

Example answer:
{"entities": [{"text": "L-dopa", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}]}

Example input:
Sentence: Three months later the patient was exposed to a single dose of metoprolol , diltiazem , propafenone ( since he had received this drug in the past ) , and sparteine ( as a probe for the debrisoquine/sparteine type polymorphism of oxidative drug metabolism ) .

Example answer:
{"entities": [{"text": "metoprolol", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "propafenone", "type": "Chemical"}, {"text": "sparteine", "type": "Chemical"}, {"text": "debrisoquine/sparteine", "type": "Chemical"}]}

Example input:
Sentence: glycopyrrolate and atropine in the prevention of bradycardia and arrhythmias following repeated doses of suxamethonium in children .

Example answer:
{"entities": [{"text": "glycopyrrolate", "type": "Chemical"}, {"text": "atropine", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "arrhythmias", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: It has been shown that bromocriptine-induced tachycardia , which persisted after adrenalectomy , is ( i ) mediated by central dopamine D2 receptor activation and ( ii ) reduced by 5-day isoproterenol pretreatment , supporting therefore the hypothesis that this effect is dependent on sympathetic outflow to the heart .

Example answer:
{"entities": [{"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: Reduction in the dosage of amiodarone resulted in the disappearance of the sinoatrial block and the persistence of asymptomatic sinus bradycardia .

Example answer:
{"entities": [{"text": "amiodarone", "type": "Chemical"}, {"text": "sinoatrial block", "type": "Disease"}, {"text": "sinus bradycardia", "type": "Disease"}]}

Example input:
Sentence: TCR prevented the isoproterenol-induced decrease in antioxidant enzymes in the heart and increased the rate of ADP-stimulated oxygen uptake and respiratory coupling ratio .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "ADP-stimulated", "type": "Chemical"}, {"text": "oxygen", "type": "Chemical"}]}

Example input:
Sentence: Bromocriptine-induced hypotension was unaffected by isoproterenol pretreatment , while tachycardia was reversed to significant bradycardia , an effect that was partly reduced by i.v .

Example answer:
{"entities": [{"text": "Bromocriptine-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: Four compounds known to increase QT interval and cause TDP were investigated : terfenadine , terodiline , cisapride and E4031 .

Example answer:
{"entities": [{"text": "TDP", "type": "Disease"}, {"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}, {"text": "E4031", "type": "Chemical"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Input:
Sentence: By inhibiting the cytochrome P450 2D6 , terbinafine had decreased metoprolol 's clearance , leading in metoprolol accumulation which has resulted in clinically significant sinus bradycardia .

## Item bc5cdr:test:4850
Example input:
Sentence: BACKGROUND : Cisplatin-based chemotherapy combinations improve quality of life and survival in advanced nonsmall cell lung carcinoma ( NSCLC ) .

Example answer:
{"entities": [{"text": "Cisplatin-based", "type": "Chemical"}, {"text": "nonsmall cell lung carcinoma", "type": "Disease"}, {"text": "NSCLC", "type": "Disease"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: Preliminary results of an Eastern Cooperative Oncology Group study of single-agent paclitaxel ( Taxol ; Bristol-Myers Squibb Company , Princeton , NJ ) reported a 37 % response rate in patients with head and neck cancer , and the paclitaxel/cisplatin combination has been used successfully and has significantly improved median response duration in ovarian cancer patients .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "Taxol", "type": "Chemical"}, {"text": "head and neck cancer", "type": "Disease"}, {"text": "paclitaxel/cisplatin", "type": "Chemical"}, {"text": "ovarian cancer", "type": "Disease"}]}

Example input:
Sentence: New chemotherapy combinations with higher activity and lower toxicity are needed for elderly patients with advanced NSCLC .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "NSCLC", "type": "Disease"}]}

Example input:
Sentence: We initiated a phase I/II trial to determine the response and toxicity of escalating paclitaxel doses combined with fixed-dose cisplatin with granulocyte colony-stimulating factor support in patients with untreated locally advanced inoperable head and neck carcinoma .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "head and neck carcinoma", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : The combination of paclitaxel , cisplatin , and gemcitabine is well tolerated and shows high activity in metastatic NSCLC .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "NSCLC", "type": "Disease"}]}

Example input:
Sentence: MMP-2 , MMP-9 , ADAM-10 and ADAM-17 mRNA levels were increased in CaCl ( 2 ) -treated segments ( all p < 0.01 ) , with trends of elevation in CaCl ( 2 ) -untreated segments , as compared with NaCl-treated segments .

Example answer:
{"entities": [{"text": "CaCl ( 2 )", "type": "Chemical"}, {"text": "NaCl-treated", "type": "Chemical"}]}

Example input:
Sentence: The MFL regimen achieves little palliative benefit and induces severe toxicity at a fairly high rate .

Example answer:
{"entities": [{"text": "MFL regimen", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Gemcitabine plus vinorelbine in nonsmall cell lung carcinoma patients age 70 years or older or patients who can not receive cisplatin .

Example answer:
{"entities": [{"text": "Gemcitabine", "type": "Chemical"}, {"text": "vinorelbine", "type": "Chemical"}, {"text": "nonsmall cell lung carcinoma", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Although the prevalence of nonsmall cell lung carcinoma ( NSCLC ) is high among elderly patients , few data are available regarding the efficacy and toxicity of chemotherapy in this group of patients .

Example answer:
{"entities": [{"text": "nonsmall cell lung carcinoma", "type": "Disease"}, {"text": "NSCLC", "type": "Disease"}, {"text": "toxicity", "type": "Disease"}]}

Input:
Sentence: An earlier suggestion of increased lung cancer risk at high levels of metolachlor use in this cohort was not confirmed in this update .

## Item bc5cdr:test:4682
Example input:
Sentence: Heavy proteinuria was common after the use of SRL as rescue therapy for renal transplantation .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: Serum creatinine values did not change significantly : 1.98 +/- 0.8 mg/dL before SRL therapy and 2.53 +/- 1.9 mg/dL at last follow-up ( P = .14 ) .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: The possibility of de novo glomerular pathology under SRL treatment requires further investigation by renal biopsy .

Example answer:
{"entities": [{"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: The novel immunosuppressive ( IS ) drug sirolmus ( Srl ) lacks nephrotoxic effects ; however , proteinuria associated with Srl has been reported following renal transplantation .

Example answer:
{"entities": [{"text": "sirolmus", "type": "Chemical"}, {"text": "Srl", "type": "Chemical"}, {"text": "nephrotoxic", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: The aim of this study was to examine further the renal function , including morphological analysis of the kidneys of male Sprague-Dawley rats treated with either cyclosporine A ( CsA ) , tacrolimus ( FK506 ) or SRL as monotherapies or in different combinations .

Example answer:
{"entities": [{"text": "cyclosporine A", "type": "Chemical"}, {"text": "CsA", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: The semi-quantitative scoring was significantly worst in the group treated with CsA plus SRL ( P < 0.001 compared with controls ) and the analysis of the total grade of fibrosis also showed the highest proportion in the same group and was significantly different from controls ( P < 0.02 ) .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: We retrospectively examined the records of 25 renal transplant patients , who developed or displayed increased proteinuria after SRL conversion .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: A further deterioration was seen when CsA was combined with either FK506 or SRL , whereas the GFR remained unchanged in the group treated with FK506 plus SRL when compared with treatment with any of the single substances .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: The patient cohort ( 14 men , 11 women ) was treated with SRL as conversion therapy , due to chronic allograft nephropathy ( CAN ) ( n = 15 ) neoplasia ( n = 8 ) ; Kaposi 's sarcoma , Four skin cancers , One intestinal tumors , One renal cell carsinom ) or BK virus nephropathy ( n = 2 ) .

Example answer:
{"entities": [{"text": "SRL", "type": "Chemical"}, {"text": "chronic allograft nephropathy", "type": "Disease"}, {"text": "CAN", "type": "Disease"}, {"text": "neoplasia", "type": "Disease"}, {"text": "Kaposi 's sarcoma", "type": "Disease"}, {"text": "skin cancers", "type": "Disease"}, {"text": "intestinal tumors", "type": "Disease"}, {"text": "renal cell carsinom", "type": "Disease"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : This rat study demonstrated a synergistic nephrotoxic effect of CsA plus SRL , whereas FK506 plus SRL was better tolerated .

Example answer:
{"entities": [{"text": "nephrotoxic", "type": "Disease"}, {"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}]}

Input:
Sentence: Conversion to SRL prevented CsA-induced renal damage evolution ( absent/mild grade lesions ) , while NGAL ( serum versus urine ) seems to be a feasible biomarker of CsA replacement to SRL .

## Item bc5cdr:test:4841
Example input:
Sentence: A rat model was developed to examine the effects of chronic CBZ treatment on folate concentrations in the rat .

Example answer:
{"entities": [{"text": "CBZ", "type": "Chemical"}, {"text": "folate", "type": "Chemical"}]}

Example input:
Sentence: The effects of METH in CX3CR1 knockout mice were not gender-dependent and did not extend beyond the striatum .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}]}

Example input:
Sentence: Comparison of developmental toxicity of selective and non-selective cyclooxygenase-2 inhibitors in CRL : ( WI ) WUBR Wistar rats -- DFU and piroxicam study .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "DFU", "type": "Chemical"}, {"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: The yield of severe cirrhosis of the liver ( defined as a shrunken finely nodular liver with micronodular histology , ascites greater than 30 ml , plasma albumin less than 2.2 g/dl , splenomegaly 2-3 times normal , and testicular atrophy approximately half normal weight ) after 12 doses of carbon tetrachloride given intragastrically in the phenobarbitone-primed rat was increased from 25 % to 56 % by giving the initial `` calibrating '' dose of carbon tetrachloride at the peak of the phenobarbitone-induced enlargement of the liver .

Example answer:
{"entities": [{"text": "cirrhosis of the liver", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "splenomegaly", "type": "Disease"}, {"text": "atrophy", "type": "Disease"}, {"text": "carbon tetrachloride", "type": "Chemical"}, {"text": "phenobarbitone-primed", "type": "Chemical"}, {"text": "phenobarbitone-induced", "type": "Chemical"}, {"text": "enlargement of the liver", "type": "Disease"}]}

Example input:
Sentence: The results obtained indicate that with all three carcinogens , administration of 5-AzC during repair synthesis increased the incidence of initiated hepatocytes , for example 10-20 foci/cm2 in 5-AzC and carcinogen-treated rats compared with 3-5 foci/cm2 in rats treated with carcinogen only .

Example answer:
{"entities": [{"text": "5-AzC", "type": "Chemical"}]}

Example input:
Sentence: We investigated an epidemic of liver disease in nine industrial workers who had had repeated accidental exposure to a mixture of 1,1-dichloro-2,2,2-trifluoroethane ( HCFC 123 ) and 1-chloro-1,2,2,2-tetrafluoroethane ( HCFC 124 ) .

Example answer:
{"entities": [{"text": "liver disease", "type": "Disease"}, {"text": "1,1-dichloro-2,2,2-trifluoroethane", "type": "Chemical"}, {"text": "HCFC 123", "type": "Chemical"}, {"text": "1-chloro-1,2,2,2-tetrafluoroethane", "type": "Chemical"}, {"text": "HCFC 124", "type": "Chemical"}]}

Example input:
Sentence: To test the validity of the hypothesis that hypomethylation of DNA plays an important role in the initiation of carcinogenic process , 5-azacytidine ( 5-AzC ) ( 10 mg/kg ) , an inhibitor of DNA methylation , was given to rats during the phase of repair synthesis induced by the three carcinogens , benzo [ a ] -pyrene ( 200 mg/kg ) , N-methyl-N-nitrosourea ( 60 mg/kg ) and 1,2-dimethylhydrazine ( 1,2-DMH ) ( 100 mg/kg ) .

Example answer:
{"entities": [{"text": "initiation of carcinogenic process", "type": "Disease"}, {"text": "5-azacytidine", "type": "Chemical"}, {"text": "5-AzC", "type": "Chemical"}, {"text": "benzo [ a ] -pyrene", "type": "Chemical"}, {"text": "N-methyl-N-nitrosourea", "type": "Chemical"}, {"text": "1,2-dimethylhydrazine", "type": "Chemical"}, {"text": "1,2-DMH", "type": "Chemical"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: No hepatic preneoplastic nodules or hepatocellular carcinomas developed in rats fed the plain choline-supplemented diet , while one preneoplastic nodule and one hepatocellular carcinoma developed in two rats fed the same diet containing phenobarbital .

Example answer:
{"entities": [{"text": "hepatocellular carcinomas", "type": "Disease"}, {"text": "choline-supplemented", "type": "Chemical"}, {"text": "hepatocellular carcinoma", "type": "Disease"}, {"text": "phenobarbital", "type": "Chemical"}]}

Example input:
Sentence: The incidence of preneoplastic nodules and of hepatocellular carcinomas was 10 % and 37 % , respectively , in rats fed the plain choline-devoid diet , and 17 % and 30 % , in rats fed the phenobarbital-containing choline-devoid diet .

Example answer:
{"entities": [{"text": "hepatocellular carcinomas", "type": "Disease"}, {"text": "choline-devoid", "type": "Chemical"}, {"text": "phenobarbital-containing", "type": "Chemical"}]}

Input:
Sentence: UNASSIGNED : Metolachlor , a widely used herbicide , is classified as a Group C carcinogen by the U.S. Environmental Protection Agency based on increased liver neoplasms in female rats .

## Item bc5cdr:test:4769
Example input:
Sentence: TCR prevented the isoproterenol-induced decrease in antioxidant enzymes in the heart and increased the rate of ADP-stimulated oxygen uptake and respiratory coupling ratio .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "ADP-stimulated", "type": "Chemical"}, {"text": "oxygen", "type": "Chemical"}]}

Example input:
Sentence: The results of our study suggest that salvianolic acid A possessing antioxidant activity has a significant protective effect against isoproterenol-induced myocardial infarction .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: The effects of exercise on the severity of isoproterenol-induced myocardial infarction were studied in female albino rats of 20,40,60 and 80 weeks of age .

Example answer:
{"entities": [{"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Isoproterenol pretreatment for 15 days caused cardiac hypertrophy without affecting baseline blood pressure and heart rate .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "Chemical"}, {"text": "cardiac hypertrophy", "type": "Disease"}]}

Example input:
Sentence: The present study was designed to evaluate the cardioprotective potential of salvianolic acid A on isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Effects of long-term pretreatment with isoproterenol on bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: The protective role of salvianolic acid A against isoproterenol-induced myocardial damage was further confirmed by histopathological examination .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial damage", "type": "Disease"}]}

Example input:
Sentence: Isoproterenol-treated rats showed significant increases in the levels of lactate dehydrogenase , aspartate transaminase , creatine kinase and malondialdehyde and significant decreases in the activities of superoxide dismutase , catalase and glutathione peroxidase in serum and heart .

Example answer:
{"entities": [{"text": "Isoproterenol-treated", "type": "Chemical"}, {"text": "lactate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "creatine", "type": "Chemical"}, {"text": "malondialdehyde", "type": "Chemical"}, {"text": "superoxide", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Input:
Sentence: Western blot analysis showed that isoproterenol-induced phosphorylation of STAT3 was maintained or further enhanced by betaine treatment in myocardium .

## Item bc5cdr:test:4481
Example input:
Sentence: CONCLUSIONS : Correlation of plasma argatroban concentration versus the patient 's coagulation variables and clinical course suggest that prolonged elevated levels of plasma argatroban may have contributed to the patient 's extended coagulopathy .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "coagulopathy", "type": "Disease"}]}

Example input:
Sentence: Antituberculosis therapy ( ATT ) -associated acute liver failure ( ATT-ALF ) is the commonest drug-induced ALF in South Asia .

Example answer:
{"entities": [{"text": "Antituberculosis", "type": "Chemical"}, {"text": "acute liver failure", "type": "Disease"}, {"text": "ALF", "type": "Disease"}]}

Example input:
Sentence: Increased frequency of venous thromboembolism with the combination of docetaxel and thalidomide in patients with metastatic androgen-independent prostate cancer .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "docetaxel", "type": "Chemical"}, {"text": "thalidomide", "type": "Chemical"}, {"text": "prostate cancer", "type": "Disease"}]}

Example input:
Sentence: CASE : A 58-year-old man received an intracarotid injection of carboplatin for recurrent glioblastomas in his left temporal lobe .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}, {"text": "glioblastomas", "type": "Disease"}]}

Example input:
Sentence: This is the first report to measure plasma argatroban concentration in the context of CPB and extended coagulopathy .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "coagulopathy", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Direct thrombin inhibitors ( DTIs ) provide an alternative method of anticoagulation for patients with a history of heparin-induced thrombocytopenia ( HIT ) or HIT with thrombosis ( HITT ) undergoing cardiopulmonary bypass ( CPB ) .

Example answer:
{"entities": [{"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "HIT", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}, {"text": "HITT", "type": "Disease"}]}

Example input:
Sentence: STUDY OBJECTIVE : To evaluate the frequency of venous thromboembolism ( VTE ) in patients with advanced androgen-independent prostate cancer who were treated with docetaxel alone or in combination with thalidomide .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "VTE", "type": "Disease"}, {"text": "prostate cancer", "type": "Disease"}, {"text": "docetaxel", "type": "Chemical"}, {"text": "thalidomide", "type": "Chemical"}]}

Example input:
Sentence: Five patients with carcinoma developed thrombotic microangiopathy ( characterized by renal insufficiency , microangiopathic hemolytic anemia , and usually thrombocytopenia ) after treatment with cisplatin , bleomycin , and a vinca alkaloid .

Example answer:
{"entities": [{"text": "carcinoma", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "microangiopathic hemolytic anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "bleomycin", "type": "Chemical"}, {"text": "vinca alkaloid", "type": "Chemical"}]}

Example input:
Sentence: In the following report , a 65-year-old critically ill patient with a suspected history of HITT was administered argatroban for anticoagulation on bypass during heart transplantation .

Example answer:
{"entities": [{"text": "critically ill", "type": "Disease"}, {"text": "HITT", "type": "Disease"}, {"text": "argatroban", "type": "Chemical"}]}

Example input:
Sentence: Prolonged elevation of plasma argatroban in a cardiac transplant patient with a suspected history of heparin-induced thrombocytopenia with thrombosis .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}]}

Input:
Sentence: PURPOSE : The case of an oncology patient who developed heparin-induced thrombocytopenia with thrombosis ( HITT ) and was treated with argatroban plus catheter-directed thrombolysis ( CDT ) with alteplase is presented .

## Item bc5cdr:test:4628
Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: In vitro , gamma-HCH , pentylenetetrazol and picrotoxin were shown to inhibit 3H-TBOB binding in mouse whole brain , with IC50 values of 4.6 , 404 and 9.4 microM , respectively .

Example answer:
{"entities": [{"text": "gamma-HCH", "type": "Chemical"}, {"text": "pentylenetetrazol", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "3H-TBOB", "type": "Chemical"}]}

Example input:
Sentence: A comparable overexpression of Pgp in the BBB was obtained after pilocarpine-induced seizures in wild-type Wistar rats .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Swiss albino mice prepared with intrajugular catheters were tested in photocell cages after administration of 93 mg/kg ( LD50 ) of cocaine and GNC92H2 infusions ranging from 30 to 190 mg/kg .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "GNC92H2", "type": "Chemical"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: Population responses in granule cells of the dentate gyrus were examined in transverse slices of the ventral hippocampus from pilocarpine-treated and untreated mice .

Example answer:
{"entities": [{"text": "pilocarpine-treated", "type": "Chemical"}]}

Example input:
Sentence: In this study , the severity of response to other seizure-inducing agents was tested in mice 1 and 24 h after intraperitoneal administration of 80 mg/kg gamma-HCH .

Example answer:
{"entities": [{"text": "seizure-inducing", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: When hippocampal ACh was measured during testing for handling-induced convulsions , extracellular ACh was significantly elevated ( 192 % ) in WSP mice , but was nonsignificantly elevated ( 59 % ) in WSR mice .

Example answer:
{"entities": [{"text": "ACh", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}]}

Example input:
Sentence: BMCs obtained from green fluorescent protein ( GFP ) transgenic mice or rats were transplanted intravenously after induction of status epilepticus ( SE ) .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}]}

Input:
Sentence: In addition , GABA content of mice hippocampus treated with GFC75 plus P400 showed an increase of 46.90 % when compared with seized mice .

## Item bc5cdr:test:4776
Example input:
Sentence: Simvastatinezetimibe and escitalopram ( which she was taking for depression ) were discontinued , and other potential causes of hepatotoxicity were excluded .

Example answer:
{"entities": [{"text": "Simvastatinezetimibe", "type": "Chemical"}, {"text": "escitalopram", "type": "Chemical"}, {"text": "depression", "type": "Disease"}, {"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: We report the case of a patient with amoxicillin-clavulanic acid-induced hepatitis with histologic multiple granulomas .

Example answer:
{"entities": [{"text": "amoxicillin-clavulanic", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}, {"text": "granulomas", "type": "Disease"}]}

Example input:
Sentence: A case of veno-occlusive disease of the liver with fatal outcome after dacarbazine ( DTIC ) therapy for melanoma is reported .

Example answer:
{"entities": [{"text": "veno-occlusive disease of the liver", "type": "Disease"}, {"text": "dacarbazine", "type": "Chemical"}, {"text": "DTIC", "type": "Chemical"}, {"text": "melanoma", "type": "Disease"}]}

Example input:
Sentence: Diagnosis of this potentially fatal complication may be delayed or missed if renal tissue or the peripheral blood smear is not examined , because renal failure may be ascribed to cisplatin nephrotoxicity and the anemia and thrombocytopenia to drug-induced bone marrow suppression .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "bone marrow suppression", "type": "Disease"}]}

Example input:
Sentence: We have reported a case of acute oliguric renal failure with hyperkalemia in a patient with cirrhosis , ascites , and cor pulmonale after indomethacin therapy .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "cor pulmonale", "type": "Disease"}, {"text": "indomethacin", "type": "Chemical"}]}

Example input:
Sentence: She subsequently died some 5 weeks after the commencement of her drug therapy.Post-mortem examination showed evidence of massive hepatocellular necrosis , acute hypersensitivity myocarditis , focal acute tubulo-interstitial nephritis and extensive bone marrow necrosis , with no evidence of malignancy .

Example answer:
{"entities": [{"text": "massive hepatocellular necrosis", "type": "Disease"}, {"text": "myocarditis", "type": "Disease"}, {"text": "nephritis", "type": "Disease"}, {"text": "bone marrow necrosis", "type": "Disease"}, {"text": "malignancy", "type": "Disease"}]}

Example input:
Sentence: We report a woman with coronary artery disease who developed a markedly prolonged QT interval and torsades de pointes ( TdP ) after taking ketoconazole for treatment of fungal infection .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "prolonged QT interval", "type": "Disease"}, {"text": "torsades de pointes", "type": "Disease"}, {"text": "TdP", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "fungal infection", "type": "Disease"}]}

Example input:
Sentence: Prolonged elevation of plasma argatroban in a cardiac transplant patient with a suspected history of heparin-induced thrombocytopenia with thrombosis .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: Five patients with carcinoma developed thrombotic microangiopathy ( characterized by renal insufficiency , microangiopathic hemolytic anemia , and usually thrombocytopenia ) after treatment with cisplatin , bleomycin , and a vinca alkaloid .

Example answer:
{"entities": [{"text": "carcinoma", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "microangiopathic hemolytic anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "bleomycin", "type": "Chemical"}, {"text": "vinca alkaloid", "type": "Chemical"}]}

Example input:
Sentence: We report the case of a patient who developed acute hepatitis with extensive hepatocellular necrosis , 7 months after the onset of administration of clotiazepam , a thienodiazepine derivative .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}, {"text": "extensive hepatocellular necrosis", "type": "Disease"}, {"text": "clotiazepam", "type": "Chemical"}, {"text": "thienodiazepine", "type": "Chemical"}]}

Input:
Sentence: A case of a patient with hepatocellular carcinoma that developed neutropenia after treatment with quetiapine is described here .

## Item bc5cdr:test:4801
Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: The results indicated that concomitant treatment with gum Arabic and GM significantly increased creatinine and urea by about 183 and 239 % , respectively ( compared to 432 and 346 % , respectively , in rats treated with cellulose and GM ) , and decreased that of cortical GSH by 21 % ( compared to 27 % in the cellulose plus GM group ) The GM-induced proximal tubular necrosis appeared to be slightly less severe in rats given GM together with gum Arabic than in those given GM and cellulose .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}, {"text": "urea", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "GM-induced", "type": "Chemical"}, {"text": "tubular necrosis", "type": "Disease"}]}

Example input:
Sentence: It could be inferred that gum Arabic treatment has induced a modest amelioration of some of the histological and biochemical indices of GM nephrotoxicity .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: Concomitant curcumin administration prevented the cognitive impairment and decreased the increased oxidative stress induced by these antiepileptic drugs .

Example answer:
{"entities": [{"text": "curcumin", "type": "Chemical"}, {"text": "cognitive impairment", "type": "Disease"}]}

Example input:
Sentence: The findings suggest that curcumin can be considered as a potential safe and effective adjuvant to phenobarbitone and carbamazepine therapy in preventing cognitive impairment associated with these drugs .

Example answer:
{"entities": [{"text": "curcumin", "type": "Chemical"}, {"text": "phenobarbitone", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "cognitive impairment", "type": "Disease"}]}

Example input:
Sentence: Therefore , the present study was carried out to investigate the effect of chronic curcumin administration on phenobarbitone- and carbamazepine-induced cognitive impairment and oxidative stress in rats .

Example answer:
{"entities": [{"text": "curcumin", "type": "Chemical"}, {"text": "phenobarbitone-", "type": "Chemical"}, {"text": "carbamazepine-induced", "type": "Chemical"}, {"text": "cognitive impairment", "type": "Disease"}]}

Example input:
Sentence: These results show that curcumin has beneficial effect in mitigating the deterioration of cognitive functions and oxidative damage in rats treated with phenobarbitone and carbamazepine without significantly altering their serum concentrations .

Example answer:
{"entities": [{"text": "curcumin", "type": "Chemical"}, {"text": "deterioration of cognitive functions", "type": "Disease"}, {"text": "phenobarbitone", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}]}

Example input:
Sentence: Curcumin has shown antioxidant , anti-inflammatory and neuro-protective properties .

Example answer:
{"entities": [{"text": "Curcumin", "type": "Chemical"}]}

Example input:
Sentence: Curcumin ameliorates cognitive dysfunction and oxidative damage in phenobarbitone and carbamazepine administered rats .

Example answer:
{"entities": [{"text": "Curcumin", "type": "Chemical"}, {"text": "cognitive dysfunction", "type": "Disease"}, {"text": "phenobarbitone", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}]}

Input:
Sentence: It is concluded that curcumin is able to attenuate in vivo maleate-induced nephropathy and in vitro cell damage .

## Item bc5cdr:test:4804
Example input:
Sentence: The aim of the study was to assess the clinical significance of genetic variants in butyrylcholinesterase gene ( BCHE ) in patients with a suspected prolonged duration of action of succinylcholine after ECT .

Example answer:
{"entities": [{"text": "succinylcholine", "type": "Chemical"}]}

Example input:
Sentence: The risk of renal papillary necrosis was increased nearly 20-fold by consumption of phenacetin , which also increased the risk for cancer of the renal pelvis and bladder but not for ureteric cancer .

Example answer:
{"entities": [{"text": "renal papillary necrosis", "type": "Disease"}, {"text": "phenacetin", "type": "Chemical"}, {"text": "ureteric cancer", "type": "Disease"}]}

Example input:
Sentence: In conclusion mitochondrial toxicity is an early common event both in paclitaxel and cisplatin induced neurotoxicity .

Example answer:
{"entities": [{"text": "mitochondrial toxicity", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Early trials of cisplatin and amifostine also suggested that the incidence and severity of cisplatin-induced nephrotoxicity , ototoxicity , and neuropathy were reduced .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "amifostine", "type": "Chemical"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "ototoxicity", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}]}

Example input:
Sentence: Nested within the cohort , a matched case-control study was performed to estimate the association between cyclophosphamide and bladder cancer using odds ratios ( ORs ) as relative risk .

Example answer:
{"entities": [{"text": "cyclophosphamide", "type": "Chemical"}, {"text": "bladder cancer", "type": "Disease"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: The present results are consistent with the carcinogenicity experiment suggesting that different mechanisms are involved in FANFT carcinogenesis in the bladder and forestomach , and that aspirin 's effect on FANFT in the forestomach is not due to an irritant effect associated with increased cell proliferation .

Example answer:
{"entities": [{"text": "FANFT", "type": "Chemical"}, {"text": "carcinogenesis", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: The co-administration of aspirin with N- [ 4- ( 5-nitro-2-furyl ) -2-thiazolyl ] -formamide ( FANFT ) to rats resulted in a reduced incidence of FANFT-induced bladder carcinomas but a concomitant induction of forestomach tumors .

Example answer:
{"entities": [{"text": "aspirin", "type": "Chemical"}, {"text": "N- [ 4- ( 5-nitro-2-furyl ) -2-thiazolyl ] -formamide", "type": "Chemical"}, {"text": "FANFT", "type": "Chemical"}, {"text": "FANFT-induced", "type": "Chemical"}, {"text": "bladder carcinomas", "type": "Disease"}, {"text": "forestomach tumors", "type": "Disease"}]}

Example input:
Sentence: To test the validity of the hypothesis that hypomethylation of DNA plays an important role in the initiation of carcinogenic process , 5-azacytidine ( 5-AzC ) ( 10 mg/kg ) , an inhibitor of DNA methylation , was given to rats during the phase of repair synthesis induced by the three carcinogens , benzo [ a ] -pyrene ( 200 mg/kg ) , N-methyl-N-nitrosourea ( 60 mg/kg ) and 1,2-dimethylhydrazine ( 1,2-DMH ) ( 100 mg/kg ) .

Example answer:
{"entities": [{"text": "initiation of carcinogenic process", "type": "Disease"}, {"text": "5-azacytidine", "type": "Chemical"}, {"text": "5-AzC", "type": "Chemical"}, {"text": "benzo [ a ] -pyrene", "type": "Chemical"}, {"text": "N-methyl-N-nitrosourea", "type": "Chemical"}, {"text": "1,2-dimethylhydrazine", "type": "Chemical"}, {"text": "1,2-DMH", "type": "Chemical"}]}

Example input:
Sentence: In vivo protection of dna damage associated apoptotic and necrotic cell deaths during acetaminophen-induced nephrotoxicity , amiodarone-induced lung toxicity and doxorubicin-induced cardiotoxicity by a novel IH636 grape seed proanthocyanidin extract .

Example answer:
{"entities": [{"text": "necrotic", "type": "Disease"}, {"text": "acetaminophen-induced", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "amiodarone-induced", "type": "Chemical"}, {"text": "lung toxicity", "type": "Disease"}, {"text": "doxorubicin-induced", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}, {"text": "IH636 grape seed proanthocyanidin extract", "type": "Chemical"}]}

Input:
Sentence: OBJECTIVE : Diazinon , a common organophosphate insecticide with genotoxic properties , was previously associated with lung cancer in the Agricultural Health Study ( AHS ) cohort , but few other epidemiological studies have examined diazinon-associated cancer risk .

## Item bc5cdr:test:4857
Example input:
Sentence: In conclusion , ENaC mRNA expression , especially alphaENaC , is increased in the very early phase of the experimental model of PAN-induced nephrotic syndrome in rats , but appears to escape from the regulation by aldosterone after day 3 .

Example answer:
{"entities": [{"text": "PAN-induced", "type": "Chemical"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "aldosterone", "type": "Chemical"}]}

Example input:
Sentence: This animal model may be useful to explore the mechanisms by which prenatal nutritional deficiency enhances risk for schizophrenia in humans and may also have implications for developmental processes leading to differential sensitivity to drugs of abuse .

Example answer:
{"entities": [{"text": "nutritional deficiency", "type": "Disease"}, {"text": "schizophrenia", "type": "Disease"}]}

Example input:
Sentence: The goal of these studies was to use an animal model to examine the effects of prenatal protein deprivation on behaviors and receptor binding with relevance to schizophrenia .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "Disease"}]}

Example input:
Sentence: Its activity is believed to be due modulation of the tumour milieu , including downregulation of angiogenesis and inflammatory cytokines .

Example answer:
{"entities": [{"text": "tumour", "type": "Disease"}]}

Example input:
Sentence: In vivo protection of dna damage associated apoptotic and necrotic cell deaths during acetaminophen-induced nephrotoxicity , amiodarone-induced lung toxicity and doxorubicin-induced cardiotoxicity by a novel IH636 grape seed proanthocyanidin extract .

Example answer:
{"entities": [{"text": "necrotic", "type": "Disease"}, {"text": "acetaminophen-induced", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "amiodarone-induced", "type": "Chemical"}, {"text": "lung toxicity", "type": "Disease"}, {"text": "doxorubicin-induced", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}, {"text": "IH636 grape seed proanthocyanidin extract", "type": "Chemical"}]}

Example input:
Sentence: This age group had an increased risk of myelosuppression .

Example answer:
{"entities": [{"text": "myelosuppression", "type": "Disease"}]}

Example input:
Sentence: Severe toxicity was correlated with the higher cumulative dose of 60 g/m2 of ifosfamide , a younger age ( less than 2 1/2 years old ) , and a predominance of vesicoprostatic tumor involvement .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "tumor", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : This study establishes a TAA model by periarterial CaCl ( 2 ) exposure in rats , and demonstrates a significant elevation of expression of MMP-2 , MMP-9 , ADAM10 and ADAM17 in the pathogenesis of vascular remodeling .

Example answer:
{"entities": [{"text": "TAA", "type": "Disease"}, {"text": "CaCl ( 2 )", "type": "Chemical"}]}

Example input:
Sentence: Perhaps two events might be necessary for initiation , the first caused by the carcinogen and a second involving hypomethylation of DNA .

Example answer:
{"entities": []}

Example input:
Sentence: Development of clear cell adenocarcinoma in DES-exposed offspring under observation .

Example answer:
{"entities": [{"text": "clear cell adenocarcinoma", "type": "Disease"}, {"text": "DES-exposed", "type": "Chemical"}]}

Input:
Sentence: OBJECTIVES : This work summarizes research on the molecular mechanisms that underlie the increased risk of cancer development in adulthood that is associated with early-life iAs exposure .

## Item bc5cdr:test:4858
Example input:
Sentence: Her red blood cells ( RBCs ) had increased incubated Heinz body formation , decreased reduced glutathione ( GSH ) , and decreased GSH stability .

Example answer:
{"entities": [{"text": "glutathione", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}]}

Example input:
Sentence: A reproducible model for producing diffuse myocardial injury ( epinephrine infusion ) has been developed to study the cardioprotective effects of agents or maneuvers which might alter the evolution of acute myocardial infarction .

Example answer:
{"entities": [{"text": "myocardial injury", "type": "Disease"}, {"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: This animal model may be useful to explore the mechanisms by which prenatal nutritional deficiency enhances risk for schizophrenia in humans and may also have implications for developmental processes leading to differential sensitivity to drugs of abuse .

Example answer:
{"entities": [{"text": "nutritional deficiency", "type": "Disease"}, {"text": "schizophrenia", "type": "Disease"}]}

Example input:
Sentence: In addition , its ' presumed contribution to DNA repair may be another important attribute , which played a role in the chemoprevention process .

Example answer:
{"entities": []}

Example input:
Sentence: Development of clear cell adenocarcinoma in DES-exposed offspring under observation .

Example answer:
{"entities": [{"text": "clear cell adenocarcinoma", "type": "Disease"}, {"text": "DES-exposed", "type": "Chemical"}]}

Example input:
Sentence: After EE treatment , changes in immunostaining for 7H6 and ZO-1 were similar to those seen in periportal hepatocytes after BDL , but distributed more diffusely throughout the lobule .

Example answer:
{"entities": [{"text": "EE", "type": "Chemical"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: To test the validity of the hypothesis that hypomethylation of DNA plays an important role in the initiation of carcinogenic process , 5-azacytidine ( 5-AzC ) ( 10 mg/kg ) , an inhibitor of DNA methylation , was given to rats during the phase of repair synthesis induced by the three carcinogens , benzo [ a ] -pyrene ( 200 mg/kg ) , N-methyl-N-nitrosourea ( 60 mg/kg ) and 1,2-dimethylhydrazine ( 1,2-DMH ) ( 100 mg/kg ) .

Example answer:
{"entities": [{"text": "initiation of carcinogenic process", "type": "Disease"}, {"text": "5-azacytidine", "type": "Chemical"}, {"text": "5-AzC", "type": "Chemical"}, {"text": "benzo [ a ] -pyrene", "type": "Chemical"}, {"text": "N-methyl-N-nitrosourea", "type": "Chemical"}, {"text": "1,2-dimethylhydrazine", "type": "Chemical"}, {"text": "1,2-DMH", "type": "Chemical"}]}

Example input:
Sentence: Its activity is believed to be due modulation of the tumour milieu , including downregulation of angiogenesis and inflammatory cytokines .

Example answer:
{"entities": [{"text": "tumour", "type": "Disease"}]}

Example input:
Sentence: Perhaps two events might be necessary for initiation , the first caused by the carcinogen and a second involving hypomethylation of DNA .

Example answer:
{"entities": []}

Input:
Sentence: DISCUSSION : Epigenetic reprogramming that imparts functional changes in gene expression , the development of cancer stem cells , and immunomodulation are plausible underlying mechanisms by which early-life iAs exposure elicits latent carcinogenic effects .

## Item bc5cdr:test:4763
Example input:
Sentence: The effects of exercise on the severity of isoproterenol-induced myocardial infarction were studied in female albino rats of 20,40,60 and 80 weeks of age .

Example answer:
{"entities": [{"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: The results show that pretreatment with TCR may be useful in preventing the damage induced by isoproterenol in rat heart .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: The protective role of salvianolic acid A against isoproterenol-induced myocardial damage was further confirmed by histopathological examination .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial damage", "type": "Disease"}]}

Example input:
Sentence: TCR protected against pathological changes induced by isoproterenol in rat heart .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: The present study was designed to evaluate the cardioprotective potential of salvianolic acid A on isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Isoproterenol-treated rats showed significant increases in the levels of lactate dehydrogenase , aspartate transaminase , creatine kinase and malondialdehyde and significant decreases in the activities of superoxide dismutase , catalase and glutathione peroxidase in serum and heart .

Example answer:
{"entities": [{"text": "Isoproterenol-treated", "type": "Chemical"}, {"text": "lactate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "creatine", "type": "Chemical"}, {"text": "malondialdehyde", "type": "Chemical"}, {"text": "superoxide", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}]}

Example input:
Sentence: Cardioprotective effect of salvianolic acid A on isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Effects of long-term pretreatment with isoproterenol on bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Input:
Sentence: Regulation of signal transducer and activator of transcription 3 and apoptotic pathways by betaine attenuates isoproterenol-induced acute myocardial injury in rats .

## Item bc5cdr:test:4482
Example input:
Sentence: Three yr after transplantation she developed renal Fanconi syndrome with severe metabolic acidosis , hypophosphatemia , glycosuria , and aminoaciduria .

Example answer:
{"entities": [{"text": "renal Fanconi syndrome", "type": "Disease"}, {"text": "metabolic acidosis", "type": "Disease"}, {"text": "hypophosphatemia", "type": "Disease"}, {"text": "glycosuria", "type": "Disease"}, {"text": "aminoaciduria", "type": "Disease"}]}

Example input:
Sentence: In this report we describe the case of a 37-year-old white woman with Ebstein 's anomaly , who developed a rare syndrome called platypnea-orthodeoxia , characterized by massive right-to-left interatrial shunting with transient profound hypoxia and cyanosis .

Example answer:
{"entities": [{"text": "Ebstein 's anomaly", "type": "Disease"}, {"text": "platypnea-orthodeoxia", "type": "Disease"}, {"text": "hypoxia", "type": "Disease"}, {"text": "cyanosis", "type": "Disease"}]}

Example input:
Sentence: These 13 included cases of malignant hypertension , thrombotic microangiopathy , lupus nephritis , Henoch-Schonlein nephritis , crescentic glomerulonephritis , and cocaine-related acute renal failure .

Example answer:
{"entities": [{"text": "malignant hypertension", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "lupus nephritis", "type": "Disease"}, {"text": "Henoch-Schonlein nephritis", "type": "Disease"}, {"text": "glomerulonephritis", "type": "Disease"}, {"text": "cocaine-related", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: We report the case of a 30-year-old Caucasian man who came to the emergency department in atrial fibrillation with rapid ventricular response .

Example answer:
{"entities": [{"text": "atrial fibrillation", "type": "Disease"}]}

Example input:
Sentence: A 61-year-old Japanese man with nephrotic syndrome due to focal segmental glomerulosclerosis was initially responding well to steroid therapy .

Example answer:
{"entities": [{"text": "nephrotic syndrome", "type": "Disease"}, {"text": "focal segmental glomerulosclerosis", "type": "Disease"}, {"text": "steroid", "type": "Chemical"}]}

Example input:
Sentence: Five patients with carcinoma developed thrombotic microangiopathy ( characterized by renal insufficiency , microangiopathic hemolytic anemia , and usually thrombocytopenia ) after treatment with cisplatin , bleomycin , and a vinca alkaloid .

Example answer:
{"entities": [{"text": "carcinoma", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "microangiopathic hemolytic anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "bleomycin", "type": "Chemical"}, {"text": "vinca alkaloid", "type": "Chemical"}]}

Example input:
Sentence: We report a case of a living donor renal transplant recipient who developed cyclosporine-induced TMA that responded to the withdrawal of cyclosporine in conjunction with plasmapheresis and fresh frozen plasma replacement therapy .

Example answer:
{"entities": [{"text": "cyclosporine-induced", "type": "Chemical"}, {"text": "TMA", "type": "Disease"}, {"text": "cyclosporine", "type": "Chemical"}]}

Example input:
Sentence: We report a case of severe citrate toxicity during volunteer donor apheresis platelet collection .

Example answer:
{"entities": [{"text": "citrate", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: A 54-year-old hypothyroid male taking thyroxine and simvastatin presented with bilateral leg compartment syndrome and myonecrosis .

Example answer:
{"entities": [{"text": "hypothyroid", "type": "Disease"}, {"text": "thyroxine", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "compartment syndrome", "type": "Disease"}, {"text": "myonecrosis", "type": "Disease"}]}

Example input:
Sentence: Prolonged elevation of plasma argatroban in a cardiac transplant patient with a suspected history of heparin-induced thrombocytopenia with thrombosis .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}]}

Input:
Sentence: SUMMARY : A 63-year-old Caucasian man with renal amyloidosis undergoing peripheral blood stem cell collection for an autologous stem cell transplant developed extensive bilateral upper-extremity deep venous thrombosis ( DVT ) and pulmonary embolism secondary to heparin-induced thrombocytopenia .

## Item bc5cdr:test:4662
Example input:
Sentence: Severe rhabdomyolysis and acute renal failure secondary to concomitant use of simvastatin , amiodarone , and atazanavir .

Example answer:
{"entities": [{"text": "rhabdomyolysis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: What is less well known is a phenomenon whereby statins may induce a myopathy , which persists or may progress after stopping the drug .

Example answer:
{"entities": [{"text": "statins", "type": "Chemical"}, {"text": "myopathy", "type": "Disease"}]}

Example input:
Sentence: These observations suggest that statins may initiate an immune-mediated myopathy that persists after withdrawal of the drug and responds to immunosuppressive therapy .

Example answer:
{"entities": [{"text": "statins", "type": "Chemical"}, {"text": "myopathy", "type": "Disease"}]}

Example input:
Sentence: Simvastatin is metabolized by CYP3A4 .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}]}

Example input:
Sentence: A 54-year-old hypothyroid male taking thyroxine and simvastatin presented with bilateral leg compartment syndrome and myonecrosis .

Example answer:
{"entities": [{"text": "hypothyroid", "type": "Disease"}, {"text": "thyroxine", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "compartment syndrome", "type": "Disease"}, {"text": "myonecrosis", "type": "Disease"}]}

Example input:
Sentence: The patient 's lipid panel had been maintained with simvastatin for 18 months before the conversion without evidence of hepatotoxicity .

Example answer:
{"entities": [{"text": "simvastatin", "type": "Chemical"}, {"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: Abstract Serum aminotransferase elevations are a commonly known adverse effect of 3-hydroxy-3-methylglutaryl coenzyme A reductase inhibitor ( statin ) therapy .

Example answer:
{"entities": [{"text": "statin", "type": "Chemical"}]}

Example input:
Sentence: DISCUSSION : The risk of rhabdomyolysis is increased in the presence of concomitant drugs that inhibit simvastatin metabolism .

Example answer:
{"entities": [{"text": "rhabdomyolysis", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}]}

Example input:
Sentence: Statins can cause a necrotizing myopathy and hyperCKaemia which is reversible on cessation of the drug .

Example answer:
{"entities": [{"text": "Statins", "type": "Chemical"}, {"text": "myopathy", "type": "Disease"}, {"text": "hyperCKaemia", "type": "Disease"}]}

Example input:
Sentence: Simvastatin-induced bilateral leg compartment syndrome and myonecrosis associated with hypothyroidism .

Example answer:
{"entities": [{"text": "Simvastatin-induced", "type": "Chemical"}, {"text": "compartment syndrome", "type": "Disease"}, {"text": "myonecrosis", "type": "Disease"}, {"text": "hypothyroidism", "type": "Disease"}]}

Input:
Sentence: Simvastatin plasma concentration increased 30 times in this patient and statin induced muscle toxicity is related to the concentration of the statin in blood .

## Item bc5cdr:test:4497
Example input:
Sentence: A single MPEP ( 5 mg/kg ip ) injection reduced the basal extracellular dopamine level in the striatum , as well as dopamine release stimulated either by methamphetamine ( 10 mg/kg sc ) or by intrastriatally administered veratridine ( 100 microM ) .

Example answer:
{"entities": [{"text": "MPEP", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "veratridine", "type": "Chemical"}]}

Example input:
Sentence: On the contrary , the cataleptogenic effect of haloperidol was significantly reduced in rats treated with desipramine and 6-OHDA but not in rats treated with 6-OHDA or in rats with lesions of the locus coeruleus .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "desipramine", "type": "Chemical"}, {"text": "6-OHDA", "type": "Chemical"}]}

Example input:
Sentence: This study aimed at investigating the potential antipsychotic-like properties of SSR103800 , with a particular focus on models of hyperactivity , involving either drug challenge ( ie , amphetamine and MK-801 ) or transgenic mice ( ie , NMDA Nr1 ( neo-/- ) and DAT ( -/- ) ) .

Example answer:
{"entities": [{"text": "SSR103800", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "MK-801", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}]}

Example input:
Sentence: No changes in haloperidol-induced catalepsy or MK-801-induced locomotion were seen following PD .

Example answer:
{"entities": [{"text": "haloperidol-induced", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "MK-801-induced", "type": "Chemical"}]}

Example input:
Sentence: in the rat haloperidol-induced catalepsy model for Parkinson 's disease .

Example answer:
{"entities": [{"text": "haloperidol-induced", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: The subcutaneous administration of 10 mg/kg of morphine-HC1 produced a marked increase in locomotor activity in mice .

Example answer:
{"entities": [{"text": "morphine-HC1", "type": "Chemical"}, {"text": "increase in locomotor activity", "type": "Disease"}]}

Example input:
Sentence: Catalepsy was induced by haloperidol ( 2 mg/kg p.o .

Example answer:
{"entities": [{"text": "Catalepsy", "type": "Disease"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: The present study was designed to study the effect of histamine H ( 3 ) -receptor ligands on neuroleptic-induced catalepsy , apomorphine-induced climbing behavior and amphetamine-induced locomotor activities in mice .

Example answer:
{"entities": [{"text": "histamine", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "apomorphine-induced", "type": "Chemical"}, {"text": "amphetamine-induced", "type": "Chemical"}]}

Example input:
Sentence: ) , while apomorphine ( 1.5 mg/kg s.c. ) and amphetamine ( 2 mg/kg s.c. ) were used for studying climbing behavior and locomotor activities , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: THP exhibited an antipsychotic-like profile by potentiating haloperidol-induced catalepsy , reducing amphetamine-induced hyperactivity and reducing apomorphine-induced climbing in mice .

Example answer:
{"entities": []}

Input:
Sentence: Amphetamine ( 3 mg/kg ip ) induced hyper locomotion , apomorphine ( 1.5 mg/kg subcutaneously [ sc ] ) induced climbing , and haloperidol ( 1.5 mg/kg sc ) induced catalepsy tests were used as animal models of schizophrenia .

## Item bc5cdr:test:4792
Example input:
Sentence: We suggest that our patient 's tubular dysfunction and myopathy may have resulted from mitochondrial dysfunction which is triggered by tacrolimus and augmented by lamivudine .

Example answer:
{"entities": [{"text": "tubular dysfunction", "type": "Disease"}, {"text": "myopathy", "type": "Disease"}, {"text": "mitochondrial dysfunction", "type": "Disease"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: The findings suggest that curcumin can be considered as a potential safe and effective adjuvant to phenobarbitone and carbamazepine therapy in preventing cognitive impairment associated with these drugs .

Example answer:
{"entities": [{"text": "curcumin", "type": "Chemical"}, {"text": "phenobarbitone", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "cognitive impairment", "type": "Disease"}]}

Example input:
Sentence: The nephrotoxic action of anticancer drugs such as nitrogranulogen ( NG ) , methotrexate ( MTX ) , 5-fluorouracil ( 5-FU ) and cyclophosphamide ( CY ) administered alone or in combination [ MTX + 5-FU + CY ( CMF ) ] was evaluated in experiments on Wistar rats .

Example answer:
{"entities": [{"text": "nephrotoxic", "type": "Disease"}, {"text": "nitrogranulogen", "type": "Chemical"}, {"text": "NG", "type": "Chemical"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "MTX", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CY", "type": "Chemical"}]}

Example input:
Sentence: Reactive oxygen species have been implicated in the pathogenesis of acute puromycin aminonucleoside ( PAN ) -induced nephropathy , with antioxidants significantly reducing the proteinuria .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: Concomitant curcumin administration prevented the cognitive impairment and decreased the increased oxidative stress induced by these antiepileptic drugs .

Example answer:
{"entities": [{"text": "curcumin", "type": "Chemical"}, {"text": "cognitive impairment", "type": "Disease"}]}

Example input:
Sentence: Therefore , the present study was carried out to investigate the effect of chronic curcumin administration on phenobarbitone- and carbamazepine-induced cognitive impairment and oxidative stress in rats .

Example answer:
{"entities": [{"text": "curcumin", "type": "Chemical"}, {"text": "phenobarbitone-", "type": "Chemical"}, {"text": "carbamazepine-induced", "type": "Chemical"}, {"text": "cognitive impairment", "type": "Disease"}]}

Example input:
Sentence: These results show that curcumin has beneficial effect in mitigating the deterioration of cognitive functions and oxidative damage in rats treated with phenobarbitone and carbamazepine without significantly altering their serum concentrations .

Example answer:
{"entities": [{"text": "curcumin", "type": "Chemical"}, {"text": "deterioration of cognitive functions", "type": "Disease"}, {"text": "phenobarbitone", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}]}

Example input:
Sentence: Curcumin has shown antioxidant , anti-inflammatory and neuro-protective properties .

Example answer:
{"entities": [{"text": "Curcumin", "type": "Chemical"}]}

Example input:
Sentence: Curcumin ameliorates cognitive dysfunction and oxidative damage in phenobarbitone and carbamazepine administered rats .

Example answer:
{"entities": [{"text": "Curcumin", "type": "Chemical"}, {"text": "cognitive dysfunction", "type": "Disease"}, {"text": "phenobarbitone", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}]}

Input:
Sentence: Curcumin prevents maleate-induced nephrotoxicity : relation to hemodynamic alterations , oxidative stress , mitochondrial oxygen consumption and activity of respiratory complex I .

## Item bc5cdr:test:4798
Example input:
Sentence: In the present study , we investigated whether maltolyl p-coumarate could improve cognitive decline in scopolamine-injected rats and in amyloid beta peptide ( 1-42 ) -infused rats .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "cognitive decline", "type": "Disease"}, {"text": "scopolamine-injected", "type": "Chemical"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}]}

Example input:
Sentence: Taking these in vitro and in vivo results together , our study suggests that maltolyl p-coumarate is a potentially effective candidate against Alzheimer 's disease that is characterized by wide spread neuronal death and progressive decline of cognitive function .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "Alzheimer 's disease", "type": "Disease"}, {"text": "neuronal death", "type": "Disease"}, {"text": "decline of cognitive function", "type": "Disease"}]}

Example input:
Sentence: A novel compound , maltolyl p-coumarate , attenuates cognitive deficits and shows neuroprotective effects in vitro and in vivo dementia models .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "cognitive deficits", "type": "Disease"}, {"text": "dementia", "type": "Disease"}]}

Example input:
Sentence: Cells were pretreated with maltolyl p-coumarate , before exposed to amyloid beta peptide ( 1-42 ) , glutamate or H2O2 .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "H2O2", "type": "Chemical"}]}

Example input:
Sentence: The lung weights were lower and PaO2 was improved in rats given this enzyme-blocking agent .

Example answer:
{"entities": []}

Example input:
Sentence: Such systemic lipopolysaccharide treatment mitigated methamphetamine-induced striatal dopamine and 3,4-dihydroxyphenylacetic acid depletions in a dose-dependent manner .

Example answer:
{"entities": [{"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "methamphetamine-induced", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "3,4-dihydroxyphenylacetic acid", "type": "Chemical"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/", "type": "Chemical"}, {"text": "K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}]}

Example input:
Sentence: In addition , mitochondrial respiratory dysfunction characterized by decreased respiratory control ratio and ADP/O was observed in isoproterenol-treated rats .

Example answer:
{"entities": [{"text": "respiratory dysfunction", "type": "Disease"}, {"text": "ADP/O", "type": "Chemical"}, {"text": "isoproterenol-treated", "type": "Chemical"}]}

Example input:
Sentence: Maltolyl p-coumarate was found to attenuate cognitive deficits in both rat models using passive avoidance test and to reduce apoptotic cell death observed in the hippocampus of the amyloid beta peptide ( 1-42 ) -infused rats .

Example answer:
{"entities": [{"text": "Maltolyl p-coumarate", "type": "Chemical"}, {"text": "cognitive deficits", "type": "Disease"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}]}

Example input:
Sentence: We found that maltolyl p-coumarate significantly decreased apoptotic cell death and reduced reactive oxygen species , cytochrome c release , and caspase 3 activation .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}]}

Input:
Sentence: In addition , maleate treatment reduced oxygen consumption in ADP-stimulated mitochondria and diminished respiratory control index when using malate/glutamate as substrate .

## Item bc5cdr:test:4539
Example input:
Sentence: In the absence of caffeine , acetaminophen ( up to 300 mg/kg ) did not modify the seizures induced by maximal electroshock and did not alter the convulsant dose of pentylenetetrezol in mice ( tests performed by the Anticonvulsant Screening Project of NINCDS ) .

Example answer:
{"entities": [{"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "pentylenetetrezol", "type": "Chemical"}]}

Example input:
Sentence: Ginsenoside Rg1 restores the impairment of learning induced by chronic morphine administration in rats .

Example answer:
{"entities": [{"text": "Ginsenoside Rg1", "type": "Chemical"}, {"text": "impairment of learning", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: Protective efficacy of neuroactive steroids against cocaine kindled-seizures in mice .

Example answer:
{"entities": [{"text": "steroids", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Gamma-hexachlorocyclohexane ( gamma-HCH ) , the active ingredient of the insecticide lindane , has been shown to decrease seizure threshold to pentylenetrazol ( PTZ ) 3 h after exposure to gamma-HCH and conversely increase threshold to PTZ-induced seizures 24 h after exposure to gamma-HCH ( Vohland et al .

Example answer:
{"entities": [{"text": "Gamma-hexachlorocyclohexane", "type": "Chemical"}, {"text": "gamma-HCH", "type": "Chemical"}, {"text": "lindane", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "PTZ", "type": "Chemical"}, {"text": "PTZ-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: In vitro , gamma-HCH , pentylenetetrazol and picrotoxin were shown to inhibit 3H-TBOB binding in mouse whole brain , with IC50 values of 4.6 , 404 and 9.4 microM , respectively .

Example answer:
{"entities": [{"text": "gamma-HCH", "type": "Chemical"}, {"text": "pentylenetetrazol", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "3H-TBOB", "type": "Chemical"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: Seizure activity due to PTZ and picrotoxin ( PTX ) was significantly decreased ; however , seizure activity due to 3-mercaptopropionic acid ( MPA ) , bicuculline ( BCC ) , methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate ( DMCM ) , or strychnine ( STR ) was not different from control .

Example answer:
{"entities": [{"text": "Seizure", "type": "Disease"}, {"text": "PTZ", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "PTX", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "3-mercaptopropionic acid", "type": "Chemical"}, {"text": "MPA", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "BCC", "type": "Chemical"}, {"text": "methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate", "type": "Chemical"}, {"text": "DMCM", "type": "Chemical"}, {"text": "strychnine", "type": "Chemical"}, {"text": "STR", "type": "Chemical"}]}

Example input:
Sentence: All of these positive GABA ( A ) modulators suppressed the expression of kindled seizures , whereas only allopregnanolone and ganaxolone inhibited the development of kindling .

Example answer:
{"entities": [{"text": "GABA", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "allopregnanolone", "type": "Chemical"}, {"text": "ganaxolone", "type": "Chemical"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "Disease"}, {"text": "METH", "type": "Chemical"}, {"text": "MPTP", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "METH-induced", "type": "Chemical"}]}

Input:
Sentence: Metformin protects against seizures , learning and memory impairments and oxidative damage induced by pentylenetetrazole-induced kindling in mice .

## Item bc5cdr:test:4681
Example input:
Sentence: The aim of this study was to examine further the renal function , including morphological analysis of the kidneys of male Sprague-Dawley rats treated with either cyclosporine A ( CsA ) , tacrolimus ( FK506 ) or SRL as monotherapies or in different combinations .

Example answer:
{"entities": [{"text": "cyclosporine A", "type": "Chemical"}, {"text": "CsA", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: METHODS : For a period of 2 weeks , CsA 15 mg/kg/day ( given orally ) , FK506 3.0 mg/kg/day ( given orally ) or SRL 0.4 mg/kg/day ( given intraperitoneally ) was administered once a day as these doses have earlier been found to achieve a significant immunosuppressive effect in Sprague-Dawley rats .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: Histologic changes were found in rat kidneys after administration of MTX , CY and NG , while no such change was observed after 5-FU and joint administration of MTX + 5-FU + CY compared to controls .

Example answer:
{"entities": [{"text": "MTX", "type": "Chemical"}, {"text": "CY", "type": "Chemical"}, {"text": "NG", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}]}

Example input:
Sentence: The semi-quantitative scoring was significantly worst in the group treated with CsA plus SRL ( P < 0.001 compared with controls ) and the analysis of the total grade of fibrosis also showed the highest proportion in the same group and was significantly different from controls ( P < 0.02 ) .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: Diagnosis of this potentially fatal complication may be delayed or missed if renal tissue or the peripheral blood smear is not examined , because renal failure may be ascribed to cisplatin nephrotoxicity and the anemia and thrombocytopenia to drug-induced bone marrow suppression .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "bone marrow suppression", "type": "Disease"}]}

Example input:
Sentence: HS diet for 4 wk caused a progressive increase in BP , protein and albumin excretion , and glomerular sclerosis in male DS rats , which were attenuated by castration .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: In conclusion , reductions in creatinine clearance and renal amphotericin B accumulation after chronic amphotericin B administration were enhanced by salt depletion and attenuated by sodium loading in rats .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "amphotericin B", "type": "Chemical"}, {"text": "sodium", "type": "Chemical"}]}

Example input:
Sentence: A further deterioration was seen when CsA was combined with either FK506 or SRL , whereas the GFR remained unchanged in the group treated with FK506 plus SRL when compared with treatment with any of the single substances .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : This rat study demonstrated a synergistic nephrotoxic effect of CsA plus SRL , whereas FK506 plus SRL was better tolerated .

Example answer:
{"entities": [{"text": "nephrotoxic", "type": "Disease"}, {"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}]}

Input:
Sentence: Prolonged CsA exposure aggravated renal damage , without clear changes on the traditional markers , but with changes in serums TGF- b and IL-7 , TBARs clearance , and kidney TGF-b and mTOR .

## Item bc5cdr:test:3904
Example input:
Sentence: The present study was aimed to investigate the combined effects of green tea and vitamin E on heart weight , body weight , serum marker enzymes , lipid peroxidation , endogenous antioxidants and membrane bound ATPases in isoproterenol ( ISO ) -induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "ISO", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Isoproterenol pretreatment for 15 days caused cardiac hypertrophy without affecting baseline blood pressure and heart rate .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "Chemical"}, {"text": "cardiac hypertrophy", "type": "Disease"}]}

Example input:
Sentence: Histological studies demonstrated that the rats developed an infarct 18 h after isoproterenol administration .

Example answer:
{"entities": [{"text": "infarct", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: In isolated perfused heart preparations from isoproterenol-pretreated rats , the isoproterenol-induced maximal increase in left ventricular systolic pressure was significantly reduced , compared with saline-pretreated rats ( the EC50 of the isoproterenol-induced increase in left ventricular systolic pressure was enhanced approximately 22-fold ) .

Example answer:
{"entities": [{"text": "isoproterenol-pretreated", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: The effects of exercise on the severity of isoproterenol-induced myocardial infarction were studied in female albino rats of 20,40,60 and 80 weeks of age .

Example answer:
{"entities": [{"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: TCR prevented the isoproterenol-induced decrease in antioxidant enzymes in the heart and increased the rate of ADP-stimulated oxygen uptake and respiratory coupling ratio .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "ADP-stimulated", "type": "Chemical"}, {"text": "oxygen", "type": "Chemical"}]}

Example input:
Sentence: In addition , mitochondrial respiratory dysfunction characterized by decreased respiratory control ratio and ADP/O was observed in isoproterenol-treated rats .

Example answer:
{"entities": [{"text": "respiratory dysfunction", "type": "Disease"}, {"text": "ADP/O", "type": "Chemical"}, {"text": "isoproterenol-treated", "type": "Chemical"}]}

Example input:
Sentence: Pretreatment of TCR , at a dose of 0.5 mL/100 g bodyweight per day , orally for 30 days , prevented the increase in lipid peroxidation and activity of marker enzymes observed in isoproterenol-induced rats ( 85 mg kg ( -1 ) s. c. for 2 days at an interval of 24 h ) .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/", "type": "Chemical"}, {"text": "K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}]}

Example input:
Sentence: Isoproterenol-treated rats showed significant increases in the levels of lactate dehydrogenase , aspartate transaminase , creatine kinase and malondialdehyde and significant decreases in the activities of superoxide dismutase , catalase and glutathione peroxidase in serum and heart .

Example answer:
{"entities": [{"text": "Isoproterenol-treated", "type": "Chemical"}, {"text": "lactate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "creatine", "type": "Chemical"}, {"text": "malondialdehyde", "type": "Chemical"}, {"text": "superoxide", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}]}

Input:
Sentence: The subcutaneous injection of isoproterenol ( 30 mg/kg ) into rats twice at an interval of 24 h , for two consecutive days , led to a significant increase in serum lactate dehydrogenase , creatine phosphokinase , alanine transaminase , aspartate transaminase , and angiotensin-converting enzyme activities , total cholesterol , triglycerides , free serum fatty acid , cardiac tissue malondialdehyde ( MDA ) , and nitric oxide levels and a significant decrease in levels of glutathione and superoxide dismutase in cardiac tissue as compared to the normal control group ( P < 0.05 ) .

## Item bc5cdr:test:4795
Example input:
Sentence: Massive urinary protein excretion has been observed after conversion from calcineurin inhibitors to mammalian target of rapamycin ( mToR ) inhibitors , especially sirolimus , in renal transplant recipients with chronic allograft nephropathy .

Example answer:
{"entities": [{"text": "rapamycin", "type": "Chemical"}, {"text": "sirolimus", "type": "Chemical"}, {"text": "chronic allograft nephropathy", "type": "Disease"}]}

Example input:
Sentence: Nephrotoxicity was assessed by measuring the concentrations of creatinine and urea in the plasma and reduced glutathione ( GSH ) in the kidney cortex , and by light microscopic examination of kidney sections .

Example answer:
{"entities": [{"text": "Nephrotoxicity", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "urea", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}]}

Example input:
Sentence: Testosterone contributes to the development of hypertension and renal injury in male DS rats on HS diet possibly through upregulation of the intrarenal renin-angiotensin system .

Example answer:
{"entities": [{"text": "Testosterone", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "renal injury", "type": "Disease"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: The time courses of urinary sodium excretion , plasma aldosterone concentration and proteinuria were studied in male Sprague-Dawley rats treated with a single dose of either PAN or vehicle .

Example answer:
{"entities": [{"text": "sodium", "type": "Chemical"}, {"text": "aldosterone", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: In this study , the hypothesis was tested that there is a sexual dimorphism in HS-induced upregulation of intrarenal angiotensinogen mediated by testosterone that also causes increases in BP and renal injury .

Example answer:
{"entities": [{"text": "testosterone", "type": "Chemical"}, {"text": "renal injury", "type": "Disease"}]}

Example input:
Sentence: This study supports the role of lipid peroxidation in mediating the proteinuric injury in PAN nephropathy .

Example answer:
{"entities": [{"text": "proteinuric injury", "type": "Disease"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: Reactive oxygen species have been implicated in the pathogenesis of acute puromycin aminonucleoside ( PAN ) -induced nephropathy , with antioxidants significantly reducing the proteinuria .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: HS diet for 4 wk caused a progressive increase in BP , protein and albumin excretion , and glomerular sclerosis in male DS rats , which were attenuated by castration .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Input:
Sentence: Maleate-induced renal injury included increase in renal vascular resistance and in the urinary excretion of total protein , glucose , sodium , neutrophil gelatinase-associated lipocalin ( NGAL ) and N-acetyl b-D-glucosaminidase ( NAG ) , upregulation of kidney injury molecule ( KIM ) -1 , decrease in renal blood flow and claudin-2 expression besides of necrosis and apoptosis of tubular cells on 24 h. Oxidative stress was determined by measuring the oxidation of lipids and proteins and diminution in renal Nrf2 levels .
