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

## Item bc5cdr:test:657
Example input:
Sentence: In the absence of caffeine , acetaminophen ( up to 300 mg/kg ) did not modify the seizures induced by maximal electroshock and did not alter the convulsant dose of pentylenetetrezol in mice ( tests performed by the Anticonvulsant Screening Project of NINCDS ) .

Example answer:
{"entities": [{"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "pentylenetetrezol", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: The efficacy of alprazolam and placebo in panic disorder with agoraphobia , and the side-effect and adverse effect profiles of both drug groups were measured .

Example answer:
{"entities": [{"text": "alprazolam", "type": "Chemical"}, {"text": "panic disorder", "type": "Disease"}, {"text": "agoraphobia", "type": "Disease"}]}

Example input:
Sentence: METHOD : In London and Toronto 154 patients who met DSM-III criteria for panic disorder with agoraphobia were randomised to alprazolam or placebo .

Example answer:
{"entities": [{"text": "panic disorder", "type": "Disease"}, {"text": "agoraphobia", "type": "Disease"}, {"text": "alprazolam", "type": "Chemical"}]}

Example input:
Sentence: Behavioral effects of diazepam and propranolol in patients with panic disorder and agoraphobia .

Example answer:
{"entities": [{"text": "diazepam", "type": "Chemical"}, {"text": "propranolol", "type": "Chemical"}, {"text": "panic disorder", "type": "Disease"}, {"text": "agoraphobia", "type": "Disease"}]}

Example input:
Sentence: A patient who allegedly consumed 100 tablets of an over-the-counter analgesic containing sodium acetylsalicylate , caffeine , and acetaminophen displayed no significant CNS stimulation despite the presence of 175 micrograms of caffeine per mL of serum .

Example answer:
{"entities": [{"text": "sodium acetylsalicylate", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}]}

Example input:
Sentence: Because salicylates have been reported to augment the stimulatory effects of caffeine on the CNS , attention was focused on the possibility that the presence of acetaminophen ( 52 micrograms/mL ) reduced the CNS toxicity of caffeine .

Example answer:
{"entities": [{"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: The frequency of sound-induced seizures after 12.5 or 25 mg/kg caffeine was reduced from 50 to 5 % by acetaminophen .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: The effects of oral doses of diazepam ( single dose of 10 mg and a median dose of 30 mg/day for 2 weeks ) and propranolol ( single dose of 80 mg and a median dose of 240 mg/day for 2 weeks ) on psychological performance of patients with panic disorders and agoraphobia were investigated in a double-blind , randomized and crossover design .

Example answer:
{"entities": [{"text": "diazepam", "type": "Chemical"}, {"text": "propranolol", "type": "Chemical"}, {"text": "panic disorders", "type": "Disease"}, {"text": "agoraphobia", "type": "Disease"}]}

Input:
Sentence: The effects of oral administration of caffeine ( 10 mg/kg ) on behavioral ratings , somatic symptoms , blood pressure and plasma levels of 3-methoxy-4-hydroxyphenethyleneglycol ( MHPG ) and cortisol were determined in 17 healthy subjects and 21 patients meeting DSM-III criteria for agoraphobia with panic attacks or panic disorder .

## Item bc5cdr:test:1456
Example input:
Sentence: In each patient who had abnormalities on the initial MR study , a follow-up MR study was performed 1 month later .

Example answer:
{"entities": []}

Example input:
Sentence: The patient recovered spontaneously in 3 hours under surveillance in the hospital .

Example answer:
{"entities": []}

Example input:
Sentence: Illness occurred within 1 -- 9 weeks of commencement of therapy in 9 patients , the remaining 3 patients having received the drug for 13 months , 15 months and 7 years before experiencing symptoms .

Example answer:
{"entities": []}

Example input:
Sentence: Sensation in this area returned to normal over the following 2 weeks .

Example answer:
{"entities": []}

Example input:
Sentence: The open study lasted for four weeks ; the drug was administrated in the form of 1 mg tablets .

Example answer:
{"entities": []}

Example input:
Sentence: They were followed up during and for 8 weeks after CT .

Example answer:
{"entities": []}

Example input:
Sentence: Participants underwent polysomnographic sleep recordings on days 1 to 3 , 7 to 9 , and 14 to 16 ( first , second , and third weeks of abstinence ) .

Example answer:
{"entities": []}

Example input:
Sentence: Groups 1 and 2 underwent micropuncture studies after 10 days .

Example answer:
{"entities": []}

Example input:
Sentence: This 4-week cycle was repeated until there was evidence of excessive toxicity or disease progression .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Beginning at 8 days of age , body movement and hearing were examined for 6 and up to 17 weeks , respectively .

Example answer:
{"entities": []}

Input:
Sentence: plus 2 weeks of observation ) .

## Item bc5cdr:test:1446
Example input:
Sentence: BACKGROUND : Sirolimus is the latest immunosuppressive agent used to prevent rejection , and may have less nephrotoxicity than calcineurin inhibitor ( CNI ) -based regimens .

Example answer:
{"entities": [{"text": "Sirolimus", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}]}

Example input:
Sentence: When both skin test and RAST for BPO were negative , single-blind , placebo-controlled challenge tests were done to ensure tolerance of PG or sensitivity to AX .

Example answer:
{"entities": [{"text": "BPO", "type": "Chemical"}, {"text": "PG", "type": "Chemical"}, {"text": "AX", "type": "Chemical"}]}

Example input:
Sentence: Results indicate that GSPE preexposure prior to AAP , AMI and DOX , provided near complete protection in terms of serum chemistry changes ( ALT , BUN and CPK ) , and significantly reduced DNA fragmentation .

Example answer:
{"entities": [{"text": "GSPE", "type": "Chemical"}, {"text": "AAP", "type": "Chemical"}, {"text": "AMI", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: A detailed clinical history , together with skin tests , RAST ( radioallergosorbent test ) , and controlled challenge tests , was used to establish whether patients allergic to beta-lactam antibiotics had selective immediate allergic responses to amoxicillin ( AX ) or were cross-reacting with other penicillin derivatives .

Example answer:
{"entities": [{"text": "allergic", "type": "Disease"}, {"text": "beta-lactam", "type": "Chemical"}, {"text": "amoxicillin", "type": "Chemical"}, {"text": "AX", "type": "Chemical"}, {"text": "penicillin", "type": "Chemical"}]}

Example input:
Sentence: We have utilized the human monocyte cell line , THP-1 as a model to address this question .

Example answer:
{"entities": []}

Example input:
Sentence: Pyrrolidine dithiocarbamate protects the piriform cortex in the pilocarpine status epilepticus model .

Example answer:
{"entities": [{"text": "Pyrrolidine dithiocarbamate", "type": "Chemical"}, {"text": "pilocarpine", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}]}

Example input:
Sentence: They offer protection against seizures in a range of models and seem to inhibit certain stages of drug dependence in preclinical assessments .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "drug dependence", "type": "Disease"}]}

Example input:
Sentence: Skin tests were performed with benzylpenicilloyl-poly-L-lysine ( BPO-PLL ) , benzylpenicilloate , benzylpenicillin ( PG ) , ampicillin ( AMP ) , and AX .

Example answer:
{"entities": [{"text": "benzylpenicilloyl-poly-L-lysine", "type": "Chemical"}, {"text": "BPO-PLL", "type": "Chemical"}, {"text": "benzylpenicilloate", "type": "Chemical"}, {"text": "benzylpenicillin", "type": "Chemical"}, {"text": "PG", "type": "Chemical"}, {"text": "ampicillin", "type": "Chemical"}, {"text": "AMP", "type": "Chemical"}, {"text": "AX", "type": "Chemical"}]}

Example input:
Sentence: We therefore established sensitive quantification methods and provided a rat ICH model for detection of ICH deterioration .

Example answer:
{"entities": [{"text": "ICH", "type": "Disease"}]}

Example input:
Sentence: Elevated plus maze and passive avoidance apparatus served as the exteroceptive behavioral models for testing memory .

Example answer:
{"entities": []}

Input:
Sentence: A new model to test potential protectors .

## Item bc5cdr:test:1035
Example input:
Sentence: The patient cohort ( 14 men , 11 women ) was treated with SRL as conversion therapy , due to chronic allograft nephropathy ( CAN ) ( n = 15 ) neoplasia ( n = 8 ) ; Kaposi 's sarcoma , Four skin cancers , One intestinal tumors , One renal cell carsinom ) or BK virus nephropathy ( n = 2 ) .

Example answer:
{"entities": [{"text": "SRL", "type": "Chemical"}, {"text": "chronic allograft nephropathy", "type": "Disease"}, {"text": "CAN", "type": "Disease"}, {"text": "neoplasia", "type": "Disease"}, {"text": "Kaposi 's sarcoma", "type": "Disease"}, {"text": "skin cancers", "type": "Disease"}, {"text": "intestinal tumors", "type": "Disease"}, {"text": "renal cell carsinom", "type": "Disease"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: Gastrointestinal bleed , seizures , infection , and acute renal failure were documented in seven ( 10 % ) , five ( 7.1 % ) , 26 ( 37.1 % ) , and seven ( 10 % ) patients , respectively .

Example answer:
{"entities": [{"text": "Gastrointestinal bleed", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "infection", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: Calcineurin-inhibitor therapy can lead to renal dysfunction in heart transplantation patients .

Example answer:
{"entities": [{"text": "renal dysfunction", "type": "Disease"}]}

Example input:
Sentence: Patients who developed renal insufficiency had lower baseline body weight and higher baseline serum creatinine , required higher doses of loop diuretics , and were more likely to be treated with thiazide diuretics than controls .

Example answer:
{"entities": [{"text": "renal insufficiency", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "thiazide", "type": "Chemical"}]}

Example input:
Sentence: In this study , long-term cardiac transplant patients were switched from cyclosporine to Srl-based IS .

Example answer:
{"entities": [{"text": "cyclosporine", "type": "Chemical"}, {"text": "Srl-based", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : We found PTCR in 14 of 15 cases of TG , in 7 transplant biopsy specimens without TG , and in 13 of 143 native kidney biopsy specimens .

Example answer:
{"entities": [{"text": "TG", "type": "Disease"}]}

Example input:
Sentence: Massive urinary protein excretion has been observed after conversion from calcineurin inhibitors to mammalian target of rapamycin ( mToR ) inhibitors , especially sirolimus , in renal transplant recipients with chronic allograft nephropathy .

Example answer:
{"entities": [{"text": "rapamycin", "type": "Chemical"}, {"text": "sirolimus", "type": "Chemical"}, {"text": "chronic allograft nephropathy", "type": "Disease"}]}

Example input:
Sentence: We report a case of a living donor renal transplant recipient who developed cyclosporine-induced TMA that responded to the withdrawal of cyclosporine in conjunction with plasmapheresis and fresh frozen plasma replacement therapy .

Example answer:
{"entities": [{"text": "cyclosporine-induced", "type": "Chemical"}, {"text": "TMA", "type": "Disease"}, {"text": "cyclosporine", "type": "Chemical"}]}

Example input:
Sentence: The aim of this study was to examine further the renal function , including morphological analysis of the kidneys of male Sprague-Dawley rats treated with either cyclosporine A ( CsA ) , tacrolimus ( FK506 ) or SRL as monotherapies or in different combinations .

Example answer:
{"entities": [{"text": "cyclosporine A", "type": "Chemical"}, {"text": "CsA", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : The calcineurin inhibitors cyclosporine and tacrolimus are both known to be nephrotoxic .

Example answer:
{"entities": [{"text": "cyclosporine", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "nephrotoxic", "type": "Disease"}]}

Input:
Sentence: Renal patients on cyclosporine had the fewest bacteremias .

## Item bc5cdr:test:1310
Example input:
Sentence: The high image quality suggests that high contrast images can be obtained in humans and the 96 h stability makes it an ideal agent to detect , in patients , early cardiac infarction .

Example answer:
{"entities": [{"text": "cardiac infarction", "type": "Disease"}]}

Example input:
Sentence: Before treatment all patients had a cardiac evaluation and during treatment serial ECG recordings were performed .

Example answer:
{"entities": []}

Example input:
Sentence: Ten patients with acute transmural myocardial infarctions received intravenous nitroglycerin , sufficient to reduce mean arterial pressure from 107 +/- 6 to 85 +/- 6 mm Hg ( P less than 0.001 ) , for 60 minutes .

Example answer:
{"entities": [{"text": "myocardial infarctions", "type": "Disease"}, {"text": "nitroglycerin", "type": "Chemical"}]}

Example input:
Sentence: Amiodarone should be used with caution during long-term oral therapy in patients with or without clear intraventricular conduction defects .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "Chemical"}]}

Example input:
Sentence: Initial cardiopulmonary resuscitation and immediate treatment with adrenaline ( epinephrine ) , atropine and furosemide was successful .

Example answer:
{"entities": [{"text": "adrenaline", "type": "Chemical"}, {"text": "epinephrine", "type": "Chemical"}, {"text": "atropine", "type": "Chemical"}, {"text": "furosemide", "type": "Chemical"}]}

Example input:
Sentence: immediately before the induction of anaesthesia , to prevent arrhythmia and bradycardia following repeated doses of suxamethonium in children , was studied .

Example answer:
{"entities": [{"text": "arrhythmia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: The cardiotoxicity of conventional anthracycline therapy highlights a need to search for methods that are highly sensitive and capable of predicting cardiac dysfunction .

Example answer:
{"entities": [{"text": "cardiotoxicity", "type": "Disease"}, {"text": "anthracycline", "type": "Chemical"}, {"text": "cardiac dysfunction", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Inhibition of cardiac sympathetic tone represents an important strategy for treatment of cardiovascular disease , including arrhythmia , coronary heart disease , and chronic heart failure .

Example answer:
{"entities": [{"text": "cardiovascular disease", "type": "Disease"}, {"text": "arrhythmia", "type": "Disease"}, {"text": "coronary heart disease", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}]}

Example input:
Sentence: A patient with sinuatrial disease and implanted pacemaker was treated with amiodarone ( maximum dose 1000 mg , maintenance dose 800 mg daily ) for 10 months , for control of supraventricular tachyarrhythmias .

Example answer:
{"entities": [{"text": "sinuatrial disease", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "supraventricular tachyarrhythmias", "type": "Disease"}]}

Example input:
Sentence: In the seventh patient , a permanent ventricular pacemaker was inserted and , despite continuation of procainamide therapy , polymorphous ventricular tachycardia did not reoccur .

Example answer:
{"entities": [{"text": "procainamide", "type": "Chemical"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Input:
Sentence: We conclude that cardiac pacing during resuscitative efforts in pediatric patients suffering from acute myocardial dysfunction may not have long-term value in and of itself ; however , if temporary hemodynamic stability is achieved by this procedure , it may provide additional time needed to institute other therapeutic modalities .

## Item bc5cdr:test:1051
Example input:
Sentence: In this study , the hypothesis was tested that there is a sexual dimorphism in HS-induced upregulation of intrarenal angiotensinogen mediated by testosterone that also causes increases in BP and renal injury .

Example answer:
{"entities": [{"text": "testosterone", "type": "Chemical"}, {"text": "renal injury", "type": "Disease"}]}

Example input:
Sentence: This , together with our previous findings that allopurinol failed to prevent adrenocorticotrophic hormone induced hypertension , suggests that XO activity is not a major determinant of GC-HT in the rat .

Example answer:
{"entities": [{"text": "allopurinol", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Vasopressor agents are used to correct anesthesia-induced hypotension .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Pulmonary hypertension developed after administration of a somatostatin analogue , octreotide , to enhance resolution of the fistula .

Example answer:
{"entities": [{"text": "Pulmonary hypertension", "type": "Disease"}, {"text": "octreotide", "type": "Chemical"}, {"text": "fistula", "type": "Disease"}]}

Example input:
Sentence: Anti-oxidant effects of atorvastatin in dexamethasone-induced hypertension in the rat .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "Chemical"}, {"text": "dexamethasone-induced", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: Upregulation of the expression of vasopressin gene in the paraventricular and supraoptic nuclei of the lithium-induced diabetes insipidus rat .

Example answer:
{"entities": [{"text": "vasopressin", "type": "Chemical"}, {"text": "lithium-induced", "type": "Chemical"}, {"text": "diabetes insipidus", "type": "Disease"}]}

Example input:
Sentence: Dexamethasone ( Dex ) -induced hypertension is characterized by endothelial dysfunction associated with nitric oxide ( NO ) deficiency and increased superoxide ( O2- ) production .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "Chemical"}, {"text": "Dex", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "nitric oxide", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}, {"text": "superoxide", "type": "Chemical"}, {"text": "O2-", "type": "Chemical"}]}

Example input:
Sentence: A deficient L-arginine-nitric oxide system is implicated in cortisol-induced hypertension .

Example answer:
{"entities": [{"text": "L-arginine-nitric oxide", "type": "Chemical"}, {"text": "cortisol-induced", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: Hypertension was observed in animals that had a reduction in glomeruli as well as in a group that did not have a reduction in glomerular number , suggesting that a reduction in glomerular number is not the sole cause for the development of hypertension .

Example answer:
{"entities": [{"text": "Hypertension", "type": "Disease"}, {"text": "reduction in glomerular number", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: The hypotensive episodes were severe enough to require vasopressor administration .

Example answer:
{"entities": [{"text": "hypotensive", "type": "Disease"}]}

Input:
Sentence: Vasopressin as a possible contributor to hypertension .

## Item bc5cdr:test:743
Example input:
Sentence: Dothiepin and amitriptyline were equally effective in alleviating the symptoms of depressive illness , and both were significantly superior to placebo .

Example answer:
{"entities": [{"text": "Dothiepin", "type": "Chemical"}, {"text": "amitriptyline", "type": "Chemical"}, {"text": "depressive illness", "type": "Disease"}]}

Example input:
Sentence: Two groups of patients receiving tacrolimus were compared over a period of 1 year , one group comprising hypertensive patients who were receiving nifedipine , and the other comprising nonhypertensive patients not receiving nifedipine .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "hypertensive", "type": "Disease"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: Nitroglycerin has been shown to reduce ST-segment elevation during acute myocardial infarction , an effect potentiated in the dog by agents that reverse nitroglycerin-induced hypotension .

Example answer:
{"entities": [{"text": "Nitroglycerin", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}, {"text": "nitroglycerin-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: We studied three calcium channel blockers of different structure , nifedipine , diltiazem , and verapamil , along with the new agent .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "nifedipine", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: The effect of a 6-week treatment with the calcium channel blocker nitrendipine or the angiotensin converting enzyme inhibitor enalapril on blood pressure , albuminuria , renal hemodynamics , and morphology of the nonclipped kidney was studied in rats with two-kidney , one clip renovascular hypertension .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "nitrendipine", "type": "Chemical"}, {"text": "angiotensin", "type": "Chemical"}, {"text": "enalapril", "type": "Chemical"}, {"text": "albuminuria", "type": "Disease"}, {"text": "renovascular hypertension", "type": "Disease"}]}

Example input:
Sentence: Angina and ischemic electrocardiographic changes occurred after administration of oral dipyridamole in four patients awaiting urgent myocardial revascularization procedures .

Example answer:
{"entities": [{"text": "Angina", "type": "Disease"}, {"text": "dipyridamole", "type": "Chemical"}]}

Example input:
Sentence: Nimodipine treatment resulted in a statistically significant reduction in systolic BP ( SBP ) and diastolic BP ( DBP ) from baseline compared with placebo during the first few days .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "Chemical"}, {"text": "reduction in systolic BP", "type": "Disease"}]}

Example input:
Sentence: The observed positive impact of nifedipine on reducing the nephrotoxicity associated with tacrolimus in liver transplant recipients should be an important factor in selecting an agent to treat hypertension in this population .

Example answer:
{"entities": [{"text": "nifedipine", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: A low incidence of cardiovascular malformations was observed after exposure to each of the four calcium channel blockers , but this incidence was statistically significant only for verapamil and nifedipine .

Example answer:
{"entities": [{"text": "cardiovascular malformations", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: Nifedipine significantly improved kidney function as indicated by a significant lowering of serum creatinine levels at 6 and 12 months .

Example answer:
{"entities": [{"text": "Nifedipine", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}]}

Input:
Sentence: As the first dihydropyridine available for use in the United States , nifedipine controls angina and hypertension with minimal depression of cardiac function .

## Item bc5cdr:test:941
Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: Cardiomyopathy is frequent when the total dose exceeds 600 mg/m2 and occurs within one to six months after cessation of therapy .

Example answer:
{"entities": [{"text": "Cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Inhibition of NO-synthase induced a reversible hypertension accompanied by depressed Na+-extrusion from cardiac cells as a consequence of deteriorated Na+-binding properties of the ( Na , K ) -ATPase .

Example answer:
{"entities": [{"text": "NO-synthase", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "depressed", "type": "Disease"}, {"text": "Na+-extrusion", "type": "Chemical"}, {"text": "Na+-binding", "type": "Chemical"}, {"text": "Na", "type": "Chemical"}, {"text": "K", "type": "Chemical"}]}

Example input:
Sentence: To assess the molecular basis of disturbances in transmembraneous transport of Na+ , we studied the response of cardiac ( Na , K ) -ATPase to NO-deficient hypertension induced in rats by NO-synthase inhibition with 40 mg/kg/day N ( G ) -nitro-L-arginine methyl ester ( L-NAME ) for 4 four weeks .

Example answer:
{"entities": [{"text": "Na+", "type": "Chemical"}, {"text": "Na", "type": "Chemical"}, {"text": "K", "type": "Chemical"}, {"text": "NO-deficient", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "NO-synthase", "type": "Chemical"}, {"text": "N ( G ) -nitro-L-arginine methyl ester", "type": "Chemical"}, {"text": "L-NAME", "type": "Chemical"}]}

Example input:
Sentence: Catecholamine-induced cardiomyopathy due to chronic excess of endogenous catecholamines has been recognized for decades as a clinical phenomenon .

Example answer:
{"entities": [{"text": "Catecholamine-induced", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}, {"text": "catecholamines", "type": "Chemical"}]}

Example input:
Sentence: Serious adverse effects are uncommon and mainly have been related to the depression of cardiac contractility and conduction , especially when the drug is combined with beta-blocking agents .

Example answer:
{"entities": [{"text": "depression", "type": "Disease"}]}

Example input:
Sentence: A patient is reported who developed progressive cardiomyopathy two and one-half years after receiving 580 mg/m2 which apparently represents late , late cardiotoxicity .

Example answer:
{"entities": [{"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: The effects of varying the extracellular concentrations of Na and Ca ( [ Na ] o and [ Ca ] o ) on both , the spontaneous beating and the negative chronotropic action of verapamil , were studied in the isolated rat atria .

Example answer:
{"entities": [{"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: This drug caused biventricular dysfunction , due to its negative inotropic effect , and hypotension , due to its peripheral vasodilatory effect .

Example answer:
{"entities": [{"text": "biventricular dysfunction", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Input:
Sentence: Overall , the altered cardiac contractility and excitability characteristics , the myocardial metabolic disturbances , and the hypersensitivity of the cardiovascular system to sodium pentobarbital suggest the existence of a heretofore undescribed cardiomyopathic disorder induced by chronic barium exposure .

## Item bc5cdr:test:1054
Example input:
Sentence: On the other hand , BNP did not increase in the patients without heart failure given DNR , even at more than 700 mg/m ( 2 ) .

Example answer:
{"entities": [{"text": "heart failure", "type": "Disease"}, {"text": "DNR", "type": "Chemical"}]}

Example input:
Sentence: Before nitroprusside infusion , 5 cm H2O CPAP significantly , P less than .05 , decreased arterial blood pressure , but did not significantly alter heart rate , cardiac output , systemic vascular resistance , or QS/QT .

Example answer:
{"entities": [{"text": "nitroprusside", "type": "Chemical"}, {"text": "H2O", "type": "Chemical"}]}

Example input:
Sentence: In addition , reflex bradycardia caused by injected norepinephrine was significantly enhanced by L-dopa , DL-Threo-dihydroxyphenylserine had no effect on blood pressure , heart rate or reflex responses to norepinephrine .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}, {"text": "DL-Threo-dihydroxyphenylserine", "type": "Chemical"}]}

Example input:
Sentence: These results suggest that dehydration and/or the activation of visceral afferent inputs may contribute to the elevation of plasma AVP and the upregulation of AVP gene expression in the PVN and the SON of the Li-induced diabetes insipidus rat .

Example answer:
{"entities": [{"text": "dehydration", "type": "Disease"}, {"text": "AVP", "type": "Chemical"}, {"text": "Li-induced", "type": "Chemical"}, {"text": "diabetes insipidus", "type": "Disease"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Vasopressor agents are used to correct anesthesia-induced hypotension .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Nimodipine treatment resulted in a statistically significant reduction in systolic BP ( SBP ) and diastolic BP ( DBP ) from baseline compared with placebo during the first few days .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "Chemical"}, {"text": "reduction in systolic BP", "type": "Disease"}]}

Example input:
Sentence: The evoked increases in dural blood flow were also abolished by topical pre-administration of atropine ( 1 mm ) and [ Lys1 , Pro2,5 , Arg3,4 , Tyr6 ] -VIP ( 0.1 mm ) , a vasoactive intestinal polypeptide ( VIP ) antagonist , onto the exposed dura mater .

Example answer:
{"entities": [{"text": "increases in dural blood flow", "type": "Disease"}, {"text": "atropine", "type": "Chemical"}]}

Example input:
Sentence: d-1 given for 4 weeks , elevated blood pressure from 102+/-13 to 152+/-15 mm Hg and increased the synthesis of ET-1 and the levels of ET-1 mRNA in the mesenteric artery ( 240 % and 230 % , respectively ) .

Example answer:
{"entities": []}

Input:
Sentence: Administration of DDAVP which has antidiuretic action but minimal vasopressor effect failed to increase blood pressure to the levels observed after administration of AVP .

## Item bc5cdr:test:1207
Example input:
Sentence: While she was weak , 2-Hz repetitive stimulation revealed a decrement without significant facilitation at rapid rates or after exercise , suggesting postsynaptic neuromuscular blockade .

Example answer:
{"entities": [{"text": "postsynaptic neuromuscular blockade", "type": "Disease"}]}

Example input:
Sentence: In inflamed preparations , the muscarinic receptor antagonism on the phasic component of the electrical field stimulation-evoked contraction was decreased and the pirenzepine and 4-DAMP antagonism on the tonic component was much less efficient than in controls .

Example answer:
{"entities": [{"text": "pirenzepine", "type": "Chemical"}, {"text": "4-DAMP", "type": "Chemical"}]}

Example input:
Sentence: In contrast , dosages of Mipafox ( less than or equal to 5 mg/kg ) which inhibited mean NTE activity in spinal cord less than or equal to 61 % and brain less than or equal to 60 % produced this degree of cord damage in only 9 % of the animals .

Example answer:
{"entities": [{"text": "Mipafox", "type": "Chemical"}, {"text": "cord damage", "type": "Disease"}]}

Example input:
Sentence: Atracurium besylate , a short-acting benzylisoquinolinium NMBA that is eliminated independently of renal or hepatic function , has also been associated with persistent paralysis , but only when used with corticosteroids .

Example answer:
{"entities": [{"text": "Atracurium besylate", "type": "Chemical"}, {"text": "benzylisoquinolinium", "type": "Chemical"}, {"text": "paralysis", "type": "Disease"}]}

Example input:
Sentence: The antinociception produced by ( +/- ) -PG-9 was prevented by the unselective muscarinic antagonist atropine , the M1-selective antagonists pirenzepine and dicyclomine and the acetylcholine depletor hemicholinium-3 , but not by the opioid antagonist naloxone , the gamma-aminobutyric acidB antagonist 3-aminopropyl-diethoxy-methyl-phosphinic acid , the H3 agonist R- ( alpha ) -methylhistamine , the D2 antagonist quinpirole , the 5-hydroxytryptamine4 antagonist 2-methoxy-4-amino-5-chlorobenzoic acid 2- ( diethylamino ) ethyl ester hydrochloride , the 5-hydroxytryptamin1A antagonist 1- ( 2-methoxyphenyl ) -4- [ 4- ( 2-phthalimido ) butyl ] piperazine hydrobromide and the polyamines depletor reserpine .

Example answer:
{"entities": [{"text": ")", "type": "Chemical"}, {"text": "gamma-aminobutyric", "type": "Chemical"}, {"text": "3-aminopropyl-diethoxy-methyl-phosphinic", "type": "Chemical"}, {"text": "R- ( alpha )", "type": "Chemical"}, {"text": "2-methoxy-4-amino-5-chlorobenzoic acid 2- ( diethylamino ) ethyl", "type": "Chemical"}, {"text": "1- ( 2-methoxyphenyl ) -4- [ 4- ( 2-phthalimido ) butyl ]", "type": "Chemical"}]}

Example input:
Sentence: The reduction of cyclosporine- or tacrolimus trough levels and the administration of calcium channel blockers led to relief of pain .

Example answer:
{"entities": [{"text": "cyclosporine-", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: A patient who allegedly consumed 100 tablets of an over-the-counter analgesic containing sodium acetylsalicylate , caffeine , and acetaminophen displayed no significant CNS stimulation despite the presence of 175 micrograms of caffeine per mL of serum .

Example answer:
{"entities": [{"text": "sodium acetylsalicylate", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}]}

Example input:
Sentence: SCr increases > or = 0.5 mg/dL occurred in 4.4 % ( 9 of 204 patients ) after iopamidol and 6.7 % ( 14 of 210 patients ) after iodixanol ( P=0.39 ) , whereas rates of SCr increases > or = 25 % were 9.8 % and 12.4 % , respectively ( P=0.44 ) .

Example answer:
{"entities": [{"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}]}

Example input:
Sentence: Forty-nine percent of patients were pain free 2 h after rizatriptan , compared with 24.3 % treated with ergotamine/caffeine ( p < or = 0.001 ) , rizatriptan being superior within 1 h of treatment .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}]}

Example input:
Sentence: The infusion was discontinued either when there was no muscular response to tetanic stimulation of the ulnar nerve or when Sch 120 mg was exceeded .

Example answer:
{"entities": [{"text": "tetanic", "type": "Disease"}, {"text": "Sch", "type": "Chemical"}]}

Input:
Sentence: The abolition of muscle fasciculations ( by 0.075mg/kg dose of Fazadinium ) did not influence the occurrence of scoline pain .

## Item bc5cdr:test:1336
Example input:
Sentence: Fusidic acid was administered orally in a dose of 500 mg t.d.s .

Example answer:
{"entities": [{"text": "Fusidic acid", "type": "Chemical"}]}

Example input:
Sentence: Total cumulative doses were 36 or 60 g/m2 of ifosfamide ( six or 10 cycles of ifosfamide , vincristine , and dactinomycin [ IVA ] ) .

Example answer:
{"entities": [{"text": "ifosfamide", "type": "Chemical"}, {"text": "ifosfamide , vincristine , and dactinomycin", "type": "Chemical"}, {"text": "IVA", "type": "Chemical"}]}

Example input:
Sentence: and diazepam ( 1 mg/kg , i.p . ) .

Example answer:
{"entities": [{"text": "diazepam", "type": "Chemical"}]}

Example input:
Sentence: Thirty-four patients with juvenile rheumatoid arthritis , who were treated with flurbiprofen at a maximum dose of 4 mg/kg/day , had statistically significant decreases from baseline in 6 arthritis indices after 12 weeks of treatment .

Example answer:
{"entities": [{"text": "juvenile rheumatoid arthritis", "type": "Disease"}, {"text": "flurbiprofen", "type": "Chemical"}, {"text": "arthritis", "type": "Disease"}]}

Example input:
Sentence: In a further series of experiments , haloperidol ( 0.2 mg/kg i.p . )

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: or theophylline ( 3 mg/kg i.v . ) .

Example answer:
{"entities": [{"text": "theophylline", "type": "Chemical"}]}

Example input:
Sentence: domperidone ( 0.5 mg/kg ) .

Example answer:
{"entities": [{"text": "domperidone", "type": "Chemical"}]}

Example input:
Sentence: FK 506 , 5 mg. kg-1 .

Example answer:
{"entities": [{"text": "FK 506", "type": "Chemical"}]}

Example input:
Sentence: The mean doses of MZ and FL were 4.3+/-1.9 mg and 0.28+/-0.2 mg , respectively .

Example answer:
{"entities": [{"text": "MZ", "type": "Chemical"}, {"text": "FL", "type": "Chemical"}]}

Example input:
Sentence: Flunitrazepam 0.5 , 1.0 or 2.0 mg was given by the oral or i.m .

Example answer:
{"entities": [{"text": "Flunitrazepam", "type": "Chemical"}]}

Input:
Sentence: and 15.0 ( 10.2-23.7 ) mg/kg , p.o. , respectively , while that of flunarizine was 34.0 ( 26.0-44.8 ) mg/kg , p.o .

## Item bc5cdr:test:1484
Example input:
Sentence: Totals of 128 cases and 650 controls were analysed for repeat use and 135 cases and 622 controls for switching patterns .

Example answer:
{"entities": []}

Example input:
Sentence: The characteristics of the 48 patients in the possible cases were similar .

Example answer:
{"entities": []}

Example input:
Sentence: One patient had complete response , seven had stable disease , none had partial response and five had progressive disease .

Example answer:
{"entities": []}

Example input:
Sentence: Determination was repeated in case of abnormal first results .

Example answer:
{"entities": []}

Example input:
Sentence: A review of all reported cases in the literature is given .

Example answer:
{"entities": []}

Example input:
Sentence: Patients received a minimum of three courses unless progressive disease was detected .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSION : This case started with a media report in a popular newspaper , initiated by published , peer-reviewed research on herbals , and involved human failure in a case history , medical examination and clinical treatment .

Example answer:
{"entities": []}

Example input:
Sentence: Published cases from the literature are reviewed and pertinent features discussed .

Example answer:
{"entities": []}

Example input:
Sentence: A report of two cases .

Example answer:
{"entities": []}

Example input:
Sentence: METHOD : Open , case series design .

Example answer:
{"entities": []}

Input:
Sentence: A series of six cases .

## Item bc5cdr:test:1350
Example input:
Sentence: A nonregenerative anemia was the most compromising of the cytopenias and occurred in approximately 50 % of dogs receiving 400-500 mg/kg cefonicid or 540-840 mg/kg cefazedone .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "cytopenias", "type": "Disease"}, {"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}]}

Example input:
Sentence: After a 30-min baseline measure of locomotor activity ( day 0 ) , animals were maintained on a cyclic diet of 12-h deprivation followed by 12-h access to 10 % sucrose solution and chow pellets ( 12 h access starting 4 h after onset of the dark period ) for 21 days .

Example answer:
{"entities": [{"text": "sucrose", "type": "Chemical"}]}

Example input:
Sentence: BE-Injected rats that did not have seizures had significantly more locomotor activity than cocaine-injected animals without seizures .

Example answer:
{"entities": [{"text": "BE-Injected", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "cocaine-injected", "type": "Chemical"}]}

Example input:
Sentence: The present study was designed to examine the effect of 5-HT1B receptor ligands microinjected into the subregions of the nucleus accumbens ( the shell and the core ) on the locomotor hyperactivity induced by cocaine in rats .

Example answer:
{"entities": [{"text": "locomotor hyperactivity", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Moreover , post-treatment with LR132 prevented cocaine-induced lethality in a significant proportion of animals .

Example answer:
{"entities": [{"text": "LR132", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}]}

Example input:
Sentence: Systemic cocaine ( 10 mg/kg ) significantly increased the locomotor activity of rats .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Dopamine turnover ratios ( DOPAC : DA and HVA : DA ) were found to be lower in those animals exposed to the exploratory box when compared to their home cage counterparts .

Example answer:
{"entities": [{"text": "Dopamine", "type": "Chemical"}, {"text": "DOPAC", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}, {"text": "HVA", "type": "Chemical"}]}

Example input:
Sentence: Mature male and female mice from six inbred stains were tested for susceptibility to behavioral seizures induced by a single injection of cocaine .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: The animals that had experienced cyclic sucrose and chow were hyperactive in response to amphetamine compared with four control groups ( ad libitum 10 % sucrose and chow followed by amphetamine injection , cyclic chow followed by amphetamine injection , ad libitum chow with amphetamine , or cyclic 10 % sucrose and chow with a saline injection ) .

Example answer:
{"entities": [{"text": "sucrose", "type": "Chemical"}, {"text": "hyperactive", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}]}

Example input:
Sentence: Swiss albino mice prepared with intrajugular catheters were tested in photocell cages after administration of 93 mg/kg ( LD50 ) of cocaine and GNC92H2 infusions ranging from 30 to 190 mg/kg .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "GNC92H2", "type": "Chemical"}]}

Input:
Sentence: RESULTS : In group 1 , animals received cocaine followed by vehicle .

## Item bc5cdr:test:983
Example input:
Sentence: Peritubular capillary basement membrane reduplication in allografts and native kidney disease : a clinicopathologic study of 278 consecutive renal specimens .

Example answer:
{"entities": [{"text": "kidney disease", "type": "Disease"}]}

Example input:
Sentence: Two patients developed acute tubular necrosis , characterized clinically by acute oliguric renal failure , while they were receiving a combination of cephalothin sodium and gentamicin sulfate therapy .

Example answer:
{"entities": [{"text": "acute tubular necrosis", "type": "Disease"}, {"text": "cephalothin sodium", "type": "Chemical"}, {"text": "gentamicin sulfate", "type": "Chemical"}]}

Example input:
Sentence: The results suggest a possible involvement of the renin-angiotensin system in the development of puromycin aminonucleoside-induced nephrosis .

Example answer:
{"entities": [{"text": "puromycin", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: Reactive oxygen species have been implicated in the pathogenesis of acute puromycin aminonucleoside ( PAN ) -induced nephropathy , with antioxidants significantly reducing the proteinuria .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: Does paracetamol cause urothelial cancer or renal papillary necrosis ?

Example answer:
{"entities": [{"text": "paracetamol", "type": "Chemical"}, {"text": "urothelial cancer", "type": "Disease"}, {"text": "renal papillary necrosis", "type": "Disease"}]}

Example input:
Sentence: Puromycin aminonucleoside nephrosis was induced by single intraperitoneal injection of puromycin aminonucleoside ( PAN , 20 mg/100g BW ) .

Example answer:
{"entities": [{"text": "Puromycin aminonucleoside", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: By contrast , we were unable to substantiate an increased risk from paracetamol consumption for renal papillary necrosis or any of these cancers although there was a suggestion of an association with cancer of the ureter .

Example answer:
{"entities": [{"text": "paracetamol", "type": "Chemical"}, {"text": "renal papillary necrosis", "type": "Disease"}, {"text": "cancers", "type": "Disease"}, {"text": "cancer of the ureter", "type": "Disease"}]}

Example input:
Sentence: Renal papillary necrosis ( RPN ) and a decreased urinary concentrating ability developed during continuous long-term treatment with aspirin and paracetamol in female Fischer 344 rats .

Example answer:
{"entities": [{"text": "Renal papillary necrosis", "type": "Disease"}, {"text": "RPN", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: The risk of developing renal papillary necrosis or cancer of the renal pelvis , ureter or bladder associated with consumption of either phenacetin or paracetamol was calculated from data acquired by questionnaire from 381 cases and 808 controls .

Example answer:
{"entities": [{"text": "renal papillary necrosis", "type": "Disease"}, {"text": "phenacetin", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: The risk of renal papillary necrosis was increased nearly 20-fold by consumption of phenacetin , which also increased the risk for cancer of the renal pelvis and bladder but not for ureteric cancer .

Example answer:
{"entities": [{"text": "renal papillary necrosis", "type": "Disease"}, {"text": "phenacetin", "type": "Chemical"}, {"text": "ureteric cancer", "type": "Disease"}]}

Input:
Sentence: It is concluded that PAP formation , in vivo , accounts , at least in part , for APAP-induced renal tubular necrosis .

## Item bc5cdr:test:1046
Example input:
Sentence: Maximum tolerated dose in good-risk patients was 70 mg/m2 , and in poor-risk patients , 60 mg/m2 .

Example answer:
{"entities": []}

Example input:
Sentence: In contrast , dosages of Mipafox ( less than or equal to 5 mg/kg ) which inhibited mean NTE activity in spinal cord less than or equal to 61 % and brain less than or equal to 60 % produced this degree of cord damage in only 9 % of the animals .

Example answer:
{"entities": [{"text": "Mipafox", "type": "Chemical"}, {"text": "cord damage", "type": "Disease"}]}

Example input:
Sentence: METHODS : For a period of 2 weeks , CsA 15 mg/kg/day ( given orally ) , FK506 3.0 mg/kg/day ( given orally ) or SRL 0.4 mg/kg/day ( given intraperitoneally ) was administered once a day as these doses have earlier been found to achieve a significant immunosuppressive effect in Sprague-Dawley rats .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: The rats received AChE reactivator pralidoxime-2-chloride ( 2PAM ) ( 30.0 mg/kg BW ) , anticonvulsant diazepam ( 2.0 mg/kg BW ) , A ( 1 ) -adenosine receptor agonist N ( 6 ) -cyclopentyl adenosine ( CPA ) ( 2.0 mg/kg BW ) , NMDA-receptor antagonist dizocilpine maleate ( +-MK801 hydrogen maleate ) ( 2.0 mg/kg BW ) or their combinations with cholinolytic drug atropine sulfate ( 50.0 mg/kg BW ) immediately or 30 min after the single SC injection of DFP .

Example answer:
{"entities": [{"text": "pralidoxime-2-chloride", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "N ( 6 ) -cyclopentyl adenosine", "type": "Chemical"}, {"text": "CPA", "type": "Chemical"}, {"text": "NMDA-receptor", "type": "Chemical"}, {"text": "dizocilpine maleate", "type": "Chemical"}, {"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: GR 55562 ( 0.1-10 microg/side ) , administered intra-accumbens shell prior to cocaine , dose-dependently attenuated the psychostimulant-induced locomotor hyperactivity .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}, {"text": "locomotor hyperactivity", "type": "Disease"}]}

Example input:
Sentence: When injected into the accumbens shell ( but not the core ) before cocaine , CP 93129 ( 0.1-10 microg/side ) enhanced the locomotor response to cocaine ; the maximum effect being observed after 10 microg/side of the agonist .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Example input:
Sentence: Those dosages ( greater than or equal to 10 mg/kg ) that inhibited mean NTE activity in the spinal cord greater than or equal to 73 % and brain greater than or equal to 67 % of control values produced severe ( greater than or equal to 3 ) cervical cord pathology in 85 % of the rats .

Example answer:
{"entities": []}

Example input:
Sentence: Apamin ( 10 ng ) had a tendency to decrease the convulsive threshold ( 21.6 +/- 2.2 to 19.9 +/- 2.5 mg. l ( -1 ) ) but this was not statistically significant .

Example answer:
{"entities": [{"text": "Apamin", "type": "Chemical"}, {"text": "convulsive", "type": "Disease"}]}

Example input:
Sentence: After 154 courses of therapy , the median dose intensity was 131 mg/m ( 2 ) for paclitaxel ( 97.3 % ) , 117 mg/m ( 2 ) for cisplatin ( 97.3 % ) , and 1378 mg/m ( 2 ) for gemcitabine ( 86.2 % ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}]}

Example input:
Sentence: The extent of inhibition of brain cholinesterase activity evoked by DCE at the dose of 400 mg/kg was 22 % in young and 19 % in aged mice .

Example answer:
{"entities": [{"text": "DCE", "type": "Chemical"}]}

Input:
Sentence: The analogues CCK-8-SE and CCK-8-NS ( dose range 0.2-6.4 mumol/kg ) and caerulein dose range 0.1-0.8 mumol/kg ) showed bell-shaped dose-effect curves , with the greatest maximum inhibition for CCK-8-NS .

## Item bc5cdr:test:1219
Example input:
Sentence: Furthermore , the effects are mediated through dopamine rather than norepinephrine and do not require the carotid sinus baroreceptors .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "norepinephrine", "type": "Chemical"}]}

Example input:
Sentence: We conclude that noxious stimulation of facial mucosa increases intracranial blood flow and lacrimation via a trigemino-parasympathetic reflex .

Example answer:
{"entities": []}

Example input:
Sentence: However , L-dopa restored the bradycardia caused by norepinephrine in addition to decreasing blood pressure and heart rate .

Example answer:
{"entities": [{"text": "L-dopa", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}]}

Example input:
Sentence: Removal of the carotid sinuses caused an elevation blood pressure and heart rate and abolished the negative chronotropic effect of norepinephrine .

Example answer:
{"entities": [{"text": "norepinephrine", "type": "Chemical"}]}

Example input:
Sentence: These results suggest that spasm provocation tests , which use an intracoronary injection of a relatively low dose of methylergonovine , have a high sensitivity in variant angina and the vasoreactivity of the right coronary artery may be greater than that of the other coronary arteries .

Example answer:
{"entities": [{"text": "spasm", "type": "Disease"}, {"text": "methylergonovine", "type": "Chemical"}, {"text": "variant angina", "type": "Disease"}]}

Example input:
Sentence: The finding of cocaine-induced vasoconstriction in segments of ( noninnervated ) human umbilical artery suggests that the presence or absence of intact innervation is not sufficient to explain the discrepant data involving the possibility of alpha-mediated effects .

Example answer:
{"entities": [{"text": "cocaine-induced", "type": "Chemical"}]}

Example input:
Sentence: Although certain clinical and experimental findings support the hypothesis that spasm involves the epicardial , medium-size vessels , other data suggest intramural vasoconstriction .

Example answer:
{"entities": [{"text": "spasm", "type": "Disease"}]}

Example input:
Sentence: With regard to spasm , the clinical findings are largely circumstantial , and the locus of cocaine-induced vasoconstriction remains speculative .

Example answer:
{"entities": [{"text": "spasm", "type": "Disease"}, {"text": "cocaine-induced", "type": "Chemical"}]}

Example input:
Sentence: In addition , reflex bradycardia caused by injected norepinephrine was significantly enhanced by L-dopa , DL-Threo-dihydroxyphenylserine had no effect on blood pressure , heart rate or reflex responses to norepinephrine .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}, {"text": "DL-Threo-dihydroxyphenylserine", "type": "Chemical"}]}

Example input:
Sentence: Drug-induced arterial spasm relieved by lidocaine .

Example answer:
{"entities": [{"text": "spasm", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}]}

Input:
Sentence: Medial changes in arterial spasm induced by L-norepinephrine .

## Item bc5cdr:test:1287
Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: Captopril may , by the same mechanism , reduce the increase in glomerular filtration that is known to occur after an injection of thrombin , thereby diminishing the aggregation of fibrin monomers in the glomeruli , with the result that less fibrin will be deposited and thus less kidney damage will be produced .

Example answer:
{"entities": [{"text": "Captopril", "type": "Chemical"}, {"text": "kidney damage", "type": "Disease"}]}

Example input:
Sentence: The protective effect of LY274614 was dose-dependent , being maximum at 10-40 mgkg ( i.p . ) .

Example answer:
{"entities": [{"text": "LY274614", "type": "Chemical"}]}

Example input:
Sentence: Early trials of cisplatin and amifostine also suggested that the incidence and severity of cisplatin-induced nephrotoxicity , ototoxicity , and neuropathy were reduced .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "amifostine", "type": "Chemical"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "ototoxicity", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}]}

Example input:
Sentence: We propose that amphotericin , in the setting of reduced effective arterial volume , may activate tubuloglomerular feedback , thereby contributing to acute renal failure .

Example answer:
{"entities": [{"text": "amphotericin", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: Mean post-SCr increases were significantly less with iopamidol ( all patients : 0.07 versus 0.12 mg/dL , 6.2 versus 10.6 micromol/L , P=0.03 ; patients with diabetes : 0.07 versus 0.16 mg/dL , 6.2 versus 14.1 micromol/L , P=0.01 ) .

Example answer:
{"entities": [{"text": "iopamidol", "type": "Chemical"}, {"text": "diabetes", "type": "Disease"}]}

Example input:
Sentence: Although these adverse effects occur in some patients , their occurrence could be minimised by knowledge of the molecular effects of sirolimus on the kidney , the use of sirolimus in appropriate patient populations , close monitoring of proteinuria and renal function , use of angiotensin-converting enzyme inhibitors or angiotensin II receptor blockers if proteinuria occurs and withdrawal if needed .

Example answer:
{"entities": [{"text": "sirolimus", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "angiotensin-converting", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: The novel immunosuppressive ( IS ) drug sirolmus ( Srl ) lacks nephrotoxic effects ; however , proteinuria associated with Srl has been reported following renal transplantation .

Example answer:
{"entities": [{"text": "sirolmus", "type": "Chemical"}, {"text": "Srl", "type": "Chemical"}, {"text": "nephrotoxic", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: Renal damage as reflected by an increase in serum urea and in kidney weight was prevented by Captopril .

Example answer:
{"entities": [{"text": "Renal damage", "type": "Disease"}, {"text": "urea", "type": "Chemical"}, {"text": "Captopril", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : This rat study demonstrated a synergistic nephrotoxic effect of CsA plus SRL , whereas FK506 plus SRL was better tolerated .

Example answer:
{"entities": [{"text": "nephrotoxic", "type": "Disease"}, {"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}]}

Input:
Sentence: These results suggest that the renal protective effects of misoprostol is dose-dependent .

## Item bc5cdr:test:1373
Example input:
Sentence: Neonatal cardiomyocytes were isolated from Sprague-Dawley rat hearts and randomly divided into controls , an adriamycin-treated group , and a 3MA plus adriamycin-treated group .

Example answer:
{"entities": [{"text": "adriamycin-treated", "type": "Chemical"}, {"text": "3MA", "type": "Chemical"}]}

Example input:
Sentence: Upregulation of the expression of vasopressin gene in the paraventricular and supraoptic nuclei of the lithium-induced diabetes insipidus rat .

Example answer:
{"entities": [{"text": "vasopressin", "type": "Chemical"}, {"text": "lithium-induced", "type": "Chemical"}, {"text": "diabetes insipidus", "type": "Disease"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: Combined antiretroviral therapy causes cardiomyopathy and elevates plasma lactate in transgenic AIDS mice .

Example answer:
{"entities": [{"text": "cardiomyopathy", "type": "Disease"}, {"text": "lactate", "type": "Chemical"}, {"text": "AIDS", "type": "Disease"}]}

Example input:
Sentence: Mitochondrial radiocalcium uptakes were significantly decreased in animals pretreated with acetylsalicylic acid or dipyridamole or when hydrocortisone was added to the epinephrine infusion ( 2,682,2,803 , and 3,424 counts per minute per gram of dried fraction , respectively ) .

Example answer:
{"entities": [{"text": "radiocalcium", "type": "Chemical"}, {"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine", "type": "Chemical"}]}

Example input:
Sentence: Results show that cumulative HAART caused mitochondrial CM with elevated LA in AIDS transgenic mice .

Example answer:
{"entities": [{"text": "CM", "type": "Disease"}, {"text": "LA", "type": "Chemical"}, {"text": "AIDS", "type": "Disease"}]}

Example input:
Sentence: The addition of 1 mM adenosine to the myocardial cell cultures markedly increases the ATP concentration through a pathway reportedly leading to a compartmentalized ATP pool .

Example answer:
{"entities": [{"text": "adenosine", "type": "Chemical"}, {"text": "ATP", "type": "Chemical"}]}

Example input:
Sentence: To test the validity of the hypothesis that hypomethylation of DNA plays an important role in the initiation of carcinogenic process , 5-azacytidine ( 5-AzC ) ( 10 mg/kg ) , an inhibitor of DNA methylation , was given to rats during the phase of repair synthesis induced by the three carcinogens , benzo [ a ] -pyrene ( 200 mg/kg ) , N-methyl-N-nitrosourea ( 60 mg/kg ) and 1,2-dimethylhydrazine ( 1,2-DMH ) ( 100 mg/kg ) .

Example answer:
{"entities": [{"text": "initiation of carcinogenic process", "type": "Disease"}, {"text": "5-azacytidine", "type": "Chemical"}, {"text": "5-AzC", "type": "Chemical"}, {"text": "benzo [ a ] -pyrene", "type": "Chemical"}, {"text": "N-methyl-N-nitrosourea", "type": "Chemical"}, {"text": "1,2-dimethylhydrazine", "type": "Chemical"}, {"text": "1,2-DMH", "type": "Chemical"}]}

Example input:
Sentence: We also assessed cell viability , mitochondrial membrane potential changes and counted autophagic vacuoles in cultured cardiomyocytes .

Example answer:
{"entities": []}

Example input:
Sentence: At termination of the experiments , mice underwent echocardiography , quantitation of abundance of molecular markers of CM ( ventricular mRNA encoding atrial natriuretic factor [ ANF ] and sarcoplasmic calcium ATPase [ SERCA2 ] ) , and determination of plasma LA .

Example answer:
{"entities": [{"text": "CM", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "LA", "type": "Chemical"}]}

Input:
Sentence: Assessment of cardiomyocyte DNA synthesis during hypertrophy in adult mice .

## Item bc5cdr:test:1214
Example input:
Sentence: The present results are consistent with the carcinogenicity experiment suggesting that different mechanisms are involved in FANFT carcinogenesis in the bladder and forestomach , and that aspirin 's effect on FANFT in the forestomach is not due to an irritant effect associated with increased cell proliferation .

Example answer:
{"entities": [{"text": "FANFT", "type": "Chemical"}, {"text": "carcinogenesis", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: Nested within the cohort , a matched case-control study was performed to estimate the association between cyclophosphamide and bladder cancer using odds ratios ( ORs ) as relative risk .

Example answer:
{"entities": [{"text": "cyclophosphamide", "type": "Chemical"}, {"text": "bladder cancer", "type": "Disease"}]}

Example input:
Sentence: Early adjuvant adriamycin in superficial bladder carcinoma .

Example answer:
{"entities": [{"text": "adriamycin", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVE : To assess and characterise the risk of bladder cancer , and its relation to cyclophosphamide , in patients with Wegener 's granulomatosis .

Example answer:
{"entities": [{"text": "bladder cancer", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "Wegener 's granulomatosis", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : The results indicate a dose-response relationship between cyclophosphamide and the risk of bladder cancer , high cumulative risks in the entire cohort , and also the possibility of risk factors operating even before Wegener 's granulomatosis .

Example answer:
{"entities": [{"text": "cyclophosphamide", "type": "Chemical"}, {"text": "bladder cancer", "type": "Disease"}, {"text": "Wegener 's granulomatosis", "type": "Disease"}]}

Example input:
Sentence: A multicenter study was performed in 110 patients with superficial transitional cell carcinoma of the bladder .

Example answer:
{"entities": []}

Example input:
Sentence: The risk of bladder cancer doubled for every 10 g increment in cyclophosphamide ( OR = 2.0 , 95 % confidence interval ( CI ) 0.8 to 4.9 ) .

Example answer:
{"entities": [{"text": "bladder cancer", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}]}

Example input:
Sentence: It has shown promising results alone or in combination with other chemotherapeutic agents in colorectal , breast , pancreaticobiliary , gastric , renal cell and head and neck cancers .

Example answer:
{"entities": []}

Example input:
Sentence: The co-administration of aspirin with N- [ 4- ( 5-nitro-2-furyl ) -2-thiazolyl ] -formamide ( FANFT ) to rats resulted in a reduced incidence of FANFT-induced bladder carcinomas but a concomitant induction of forestomach tumors .

Example answer:
{"entities": [{"text": "aspirin", "type": "Chemical"}, {"text": "N- [ 4- ( 5-nitro-2-furyl ) -2-thiazolyl ] -formamide", "type": "Chemical"}, {"text": "FANFT", "type": "Chemical"}, {"text": "FANFT-induced", "type": "Chemical"}, {"text": "bladder carcinomas", "type": "Disease"}, {"text": "forestomach tumors", "type": "Disease"}]}

Example input:
Sentence: Cyclophosphamide therapy increases the risk of carcinoma of the bladder .

Example answer:
{"entities": [{"text": "Cyclophosphamide", "type": "Chemical"}]}

Input:
Sentence: Twenty carcinomas of the urinary bladder and one carcinoma of the prostate have been reported in association with its use .

## Item bc5cdr:test:1549
Example input:
Sentence: A 47-year-old patient suffering from coronary artery disease was admitted to the CCU in shock with III .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "shock", "type": "Disease"}]}

Example input:
Sentence: During an 18-month period of study 41 hemodialyzed patients receiving desferrioxamine ( 10-40 mg/kg BW/3 times weekly ) for the first time were monitored for detection of audiovisual toxicity .

Example answer:
{"entities": [{"text": "desferrioxamine", "type": "Chemical"}, {"text": "audiovisual toxicity", "type": "Disease"}]}

Example input:
Sentence: Based on this principle a 27-year old woman , classified as being in the high-risk group ( Goldstein and Berkowitz score : 11 ) , was treated with multiple cytotoxic drugs .

Example answer:
{"entities": []}

Example input:
Sentence: The animals were mechanically ventilated to achieve normocarbia ( PCO2 = 42 +/- 1 mmHg , mean +/- SE ) .

Example answer:
{"entities": []}

Example input:
Sentence: Mild hypoxia ( SO2 < 90 % ) was the most common event ( 11 patients ) ; 3 patients ( 2 % ) presented transient hypoxia due to upper airway obstruction by probe introduction and 8 ( 5.8 % ) due to hypoxia caused by MZ use .

Example answer:
{"entities": [{"text": "hypoxia", "type": "Disease"}, {"text": "airway obstruction", "type": "Disease"}, {"text": "MZ", "type": "Chemical"}]}

Example input:
Sentence: The mean age of patients in the 16 probable cases was 57.9 , with hepatotoxicity being more common in women .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: Eight healthy volunteers inhaled nicotine in darkness during a functional magnetic resonance imaging ( fMRI ) experiment ; eye movements were registered using video-oculography .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}]}

Example input:
Sentence: Of 24 evaluable patients , two achieved a complete remission and one achieved a partial remission for an overall response rate of 12.5 % ( 95 % confidence interval : 2.6-32.4 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: The first case involved a 59-year-old man who used Dormex , which contains hydrogen cyanamide , without protection after consuming a large amount of alcohol during a meal .

Example answer:
{"entities": [{"text": "Dormex", "type": "Chemical"}, {"text": "hydrogen cyanamide", "type": "Chemical"}, {"text": "alcohol", "type": "Chemical"}]}

Example input:
Sentence: Thirty-two healthy young volunteers were randomly allocated to four different groups .

Example answer:
{"entities": []}

Input:
Sentence: Two subsequent CO2-rebreathing tests were performed in healthy young volunteers .

## Item bc5cdr:test:1554
Example input:
Sentence: RESULTS : The age-adjusted incidence rate ratio for CPA/EE versus conventional COCs was 2.20 [ 95 % confidence interval ( CI ) 1.35-3.58 ] .

Example answer:
{"entities": [{"text": "CPA/EE", "type": "Chemical"}]}

Example input:
Sentence: There was a significant increase in CBF , although CMRO2 was unchanged , compared with pre-hypotensive values .

Example answer:
{"entities": []}

Example input:
Sentence: The administration of ephedrine led to a similar increase in MAP ( 53 +/- 9 to 79 +/- 8 mmHg ; P < 0.001 ) , restored CO ( 3.2 +/- 1.2 to 5.0 +/- 1.3 l min ( -1 ) ) , and preserved S ( c ) O ( 2 ) .

Example answer:
{"entities": [{"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : The combination of cisplatin and amifostine in this study resulted in an overall response rate of 16 % .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "amifostine", "type": "Chemical"}]}

Example input:
Sentence: The primary response variable was based on central reading of 24 hour ambulatory electrocardiographic recordings and was defined as the occurrence of 30 or more single premature ventricular complexes in any two consecutive 30 minute blocks or one or more runs of two or more premature ventricular complexes in the entire 24 hour electrocardiographic recording .

Example answer:
{"entities": []}

Example input:
Sentence: However , a 14 % ( from 70 +/- 8 % to 60 +/- 7 % ) reduction in S ( c ) O ( 2 ) ( P < 0.05 ) followed with no change in CO ( 3.7 +/- 1.1 to 3.4 +/- 0.9 l min ( -1 ) ) .

Example answer:
{"entities": []}

Example input:
Sentence: Uni- and multivariate analyses were used to test the influence of the clinical variables : age , sex , stroke , myocardiopathy ( MP ) , duration of the test , mitral regurgitation ( MR ) and the MZ dose .

Example answer:
{"entities": [{"text": "stroke", "type": "Disease"}, {"text": "myocardiopathy", "type": "Disease"}, {"text": "MP", "type": "Disease"}, {"text": "mitral regurgitation", "type": "Disease"}, {"text": "MR", "type": "Disease"}, {"text": "MZ", "type": "Chemical"}]}

Example input:
Sentence: An objective response was observed in 73.5 % of the patients ( 95 % confidence interval [ CI ] , 55.6-87.1 % ) , including 4 complete responses ( 11.7 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: The animals were mechanically ventilated to achieve normocarbia ( PCO2 = 42 +/- 1 mmHg , mean +/- SE ) .

Example answer:
{"entities": []}

Example input:
Sentence: Response rates according to three sets of criteria were greater with the standard dose ( 55 % -60 % ) than the low dose ( 25 % -35 % ) and placebo ( 25 % -30 % ) .

Example answer:
{"entities": []}

Input:
Sentence: The CO2-response curves for the two tests were compared within the same subject .

## Item bc5cdr:test:1038
Example input:
Sentence: Pneumocystis pneumonia ( PCP ) , a common opportunistic infection in HIV-infected individuals , is generally treated with high doses of co-trimoxazole .

Example answer:
{"entities": [{"text": "Pneumocystis pneumonia", "type": "Disease"}, {"text": "PCP", "type": "Disease"}, {"text": "opportunistic infection", "type": "Disease"}, {"text": "HIV-infected", "type": "Disease"}, {"text": "co-trimoxazole", "type": "Chemical"}]}

Example input:
Sentence: From June 2004 to October 2006 , 11 HBs Ag positive patients with rheumatologic diseases , who were on both immunosuppressive and prophylactic lamivudine therapies , were retrospectively assessed .

Example answer:
{"entities": [{"text": "HBs Ag", "type": "Chemical"}, {"text": "rheumatologic diseases", "type": "Disease"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : We conclude that in transplants , there is a strong association between well-developed PTCR and TG , while the significance of mild PTCR and its predictive value in the absence of TG is unclear .

Example answer:
{"entities": [{"text": "TG", "type": "Disease"}]}

Example input:
Sentence: Liver biopsies should be undertaken at regular intervals if azathioprine therapy is continued so that structural liver damage may be detected at an early and reversible stage .

Example answer:
{"entities": [{"text": "azathioprine", "type": "Chemical"}, {"text": "liver damage", "type": "Disease"}]}

Example input:
Sentence: Here , we report two cases of severely immunocompromised HIV-infected patients who developed severe intrahepatic cholestasis , and in one patient lesions mimicking liver abscess formation on radiologic exams , during co-trimoxazole treatment for PCP .

Example answer:
{"entities": [{"text": "HIV-infected", "type": "Disease"}, {"text": "intrahepatic cholestasis", "type": "Disease"}, {"text": "liver abscess", "type": "Disease"}, {"text": "co-trimoxazole", "type": "Chemical"}, {"text": "PCP", "type": "Disease"}]}

Example input:
Sentence: A 34-year-old lady developed a constellation of dermatitis , fever , lymphadenopathy and hepatitis , beginning on the 17th day of a course of oral sulphasalazine for sero-negative rheumatoid arthritis .

Example answer:
{"entities": [{"text": "dermatitis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "lymphadenopathy", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Example input:
Sentence: We describe a 15-yr-old girl who had orthotopic liver transplantation because of Wilson 's disease .

Example answer:
{"entities": [{"text": "Wilson 's disease", "type": "Disease"}]}

Example input:
Sentence: We describe the largest group of AX-allergic patients who have tolerated PG reported so far .

Example answer:
{"entities": [{"text": "AX-allergic", "type": "Chemical"}, {"text": "PG", "type": "Chemical"}]}

Example input:
Sentence: Azathioprine treatment benefited 19 ( 66 % ) out of 29 patients suffering from severe psoriasis .

Example answer:
{"entities": [{"text": "Azathioprine", "type": "Chemical"}, {"text": "psoriasis", "type": "Disease"}]}

Example input:
Sentence: Antituberculosis therapy ( ATT ) -associated acute liver failure ( ATT-ALF ) is the commonest drug-induced ALF in South Asia .

Example answer:
{"entities": [{"text": "Antituberculosis", "type": "Chemical"}, {"text": "acute liver failure", "type": "Disease"}, {"text": "ALF", "type": "Disease"}]}

Input:
Sentence: Aza patients had significantly more staphylococcal infections than all other transplant groups ( P less than 0.005 ) , and systemic fungal infections occurred only in the liver transplant group .

## Item bc5cdr:test:1427
Example input:
Sentence: Respiratory insufficiency was further worsened by Proteus mirabilis infection and severe bronchoconstriction .

Example answer:
{"entities": [{"text": "Respiratory insufficiency", "type": "Disease"}, {"text": "Proteus mirabilis infection", "type": "Disease"}]}

Example input:
Sentence: METHODS : Using immune stainings , semiquantitative measurement was performed under the electron microscope .

Example answer:
{"entities": []}

Example input:
Sentence: Further studies are necessary to determine the exact extent of this problem and to improve the efficacy of diagnostic methods .

Example answer:
{"entities": []}

Example input:
Sentence: Neither the patient nor the anaesthetist was aware of the diagnosis before this potentially lethal complication occurred .

Example answer:
{"entities": []}

Example input:
Sentence: Despite therapy with ursodeoxycholic acid , prednisone , and then tacrolimus , her cholestatic disease was unrelenting , with cirrhosis shown by biopsy 6 months after presentation .

Example answer:
{"entities": [{"text": "ursodeoxycholic acid", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "cholestatic disease", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}]}

Example input:
Sentence: A grade 2 or 3 infection occurred in 16 % of patients , but no toxic deaths occurred .

Example answer:
{"entities": [{"text": "infection", "type": "Disease"}, {"text": "deaths", "type": "Disease"}]}

Example input:
Sentence: Gastrointestinal bleed , seizures , infection , and acute renal failure were documented in seven ( 10 % ) , five ( 7.1 % ) , 26 ( 37.1 % ) , and seven ( 10 % ) patients , respectively .

Example answer:
{"entities": [{"text": "Gastrointestinal bleed", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "infection", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: Blood and urine cultures did not show any bacterial growth .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSION : This case started with a media report in a popular newspaper , initiated by published , peer-reviewed research on herbals , and involved human failure in a case history , medical examination and clinical treatment .

Example answer:
{"entities": []}

Example input:
Sentence: There was no serologic evidence of viral infection , and a liver biopsy sample showed a histologic pattern consistent with drug-induced hepatitis .

Example answer:
{"entities": [{"text": "viral infection", "type": "Disease"}, {"text": "drug-induced hepatitis", "type": "Disease"}]}

Input:
Sentence: Thorough bacteriological screening failed to provide evidence of infection .

## Item bc5cdr:test:1122
Example input:
Sentence: Male Wistar rats were implanted bilaterally with cannulae into the accumbens shell or core , and then were locally injected with GR 55562 ( an antagonist of 5-HT1B receptors ) or CP 93129 ( an agonist of 5-HT1B receptors ) .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Example input:
Sentence: Male rats were subcutaneously injected with morphine ( 10 mg/kg ) twice a day at 12 hour intervals for 10 days , and Rg1 ( 30 mg/kg ) was intraperitoneally injected 2 hours after the second injection of morphine once a day for 10 days .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "Rg1", "type": "Chemical"}]}

Example input:
Sentence: In contrast , SSR103800 failed to affect hyperactivity induced by amphetamine or naturally observed in dopamine transporter ( DAT ( -/- ) ) knockout mice ( 10-30 mg/kg p.o . ) .

Example answer:
{"entities": [{"text": "SSR103800", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: Protection against amphetamine-induced neurotoxicity toward striatal dopamine neurons in rodents by LY274614 , an excitatory amino acid antagonist .

Example answer:
{"entities": [{"text": "amphetamine-induced", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "LY274614", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: The rats received AChE reactivator pralidoxime-2-chloride ( 2PAM ) ( 30.0 mg/kg BW ) , anticonvulsant diazepam ( 2.0 mg/kg BW ) , A ( 1 ) -adenosine receptor agonist N ( 6 ) -cyclopentyl adenosine ( CPA ) ( 2.0 mg/kg BW ) , NMDA-receptor antagonist dizocilpine maleate ( +-MK801 hydrogen maleate ) ( 2.0 mg/kg BW ) or their combinations with cholinolytic drug atropine sulfate ( 50.0 mg/kg BW ) immediately or 30 min after the single SC injection of DFP .

Example answer:
{"entities": [{"text": "pralidoxime-2-chloride", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "N ( 6 ) -cyclopentyl adenosine", "type": "Chemical"}, {"text": "CPA", "type": "Chemical"}, {"text": "NMDA-receptor", "type": "Chemical"}, {"text": "dizocilpine maleate", "type": "Chemical"}, {"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: The data strengthen the evidence that the neurotoxic effect of amphetamine and related compounds toward nigrostriatal dopamine neurons involves NMDA receptors and that LY274614 is an NMDA receptor antagonist with long-lasting in vivo effects in rats .

Example answer:
{"entities": [{"text": "neurotoxic", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "LY274614", "type": "Chemical"}]}

Example input:
Sentence: Depletion of dopamine in the striatum was also antagonized when LY274614 was given after the injection of amphetamine ; LY274614 protected when given up to 4 hr after but not when given 8 or 24 hr after amphetamine .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "LY274614", "type": "Chemical"}, {"text": "amphetamine", "type": "Chemical"}]}

Example input:
Sentence: Sodium chloride solution ( 0.9 % ) or noradrenaline in doses of 4 , 12 and 36 micrograms h-1 kg-1 was infused for five consecutive days , either intrarenally ( by a new technique ) or intravenously into rats with one kidney removed .

Example answer:
{"entities": [{"text": "Sodium chloride", "type": "Chemical"}, {"text": "noradrenaline", "type": "Chemical"}]}

Example input:
Sentence: Male Sprague-Dawley rats were treated with D-penicillamine ( D-pen ) 500 mg/kg/day for 10 or 42 days .

Example answer:
{"entities": [{"text": "D-penicillamine", "type": "Chemical"}, {"text": "D-pen", "type": "Chemical"}]}

Input:
Sentence: Male rats received the noradrenaline neurotoxin DSP4 ( 50 mg/kg ) 7 days prior to injection of D-amphetamine ( 10 or 40 mumol/kg i.p . ) .

## Item bc5cdr:test:1113
Example input:
Sentence: CONCLUSIONS : Among markers of ischemic injury after DOX in rats , cTnT showed the greatest ability to detect myocardial damage assessed by echocardiographic detection and histological changes .

Example answer:
{"entities": [{"text": "ischemic injury", "type": "Disease"}, {"text": "DOX", "type": "Chemical"}, {"text": "myocardial damage", "type": "Disease"}]}

Example input:
Sentence: Evaluation of cardiac troponin I and T levels as markers of myocardial damage in doxorubicin-induced cardiomyopathy rats , and their relationship with echocardiographic and histological findings .

Example answer:
{"entities": [{"text": "myocardial damage", "type": "Disease"}, {"text": "doxorubicin-induced", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : To assess the added diagnostic value of a new cardiac performance index ( dP/dtejc ) measurement , based on brachial artery flow changes , as compared to standard 12-lead ECG , for detecting dobutamine-induced myocardial ischemia , using Tc99m-Sestamibi single-photon emission computed tomography as the gold standard of comparison to assess the presence or absence of ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "Tc99m-Sestamibi", "type": "Chemical"}, {"text": "ischemia", "type": "Disease"}]}

Example input:
Sentence: The cardiotoxicity of conventional anthracycline therapy highlights a need to search for methods that are highly sensitive and capable of predicting cardiac dysfunction .

Example answer:
{"entities": [{"text": "cardiotoxicity", "type": "Disease"}, {"text": "anthracycline", "type": "Chemical"}, {"text": "cardiac dysfunction", "type": "Disease"}]}

Example input:
Sentence: Late , late doxorubicin cardiotoxicity .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: The most important findings were that compared with values in control subjects , end-systolic left ventricular posterior wall dimension and percent of left ventricular posterior wall thickening in doxorubicin-treated patients were decreased at baseline study and these findings were more clearly delineated with dobutamine stimulation .

Example answer:
{"entities": [{"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}]}

Example input:
Sentence: To develop a more sensitive echocardiographic screening test for cardiac damage due to doxorubicin , a cohort study was performed using dobutamine infusion to differentiate asymptomatic long-term survivors of childhood cancer treated with doxorubicin from healthy control subjects .

Example answer:
{"entities": [{"text": "cardiac damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: We investigated the diagnostic value of cTnI and cTnT for the diagnosis of myocardial damage in a rat model of doxorubicin ( DOX ) -induced cardiomyopathy , and we examined the relationship between serial cTnI and cTnT with the development of cardiac disorders monitored by echocardiography and histological examinations in this model .

Example answer:
{"entities": [{"text": "myocardial damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiac disorders", "type": "Disease"}]}

Example input:
Sentence: Dobutamine stress echocardiography : a sensitive indicator of diminished myocardial function in asymptomatic doxorubicin-treated long-term survivors of childhood cancer .

Example answer:
{"entities": [{"text": "Dobutamine", "type": "Chemical"}, {"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: Doxorubicin is an effective anticancer chemotherapeutic agent known to cause acute and chronic cardiomyopathy .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}]}

Input:
Sentence: Our findings suggest that the changes leading to an alteration of myocardial dynamic imaging with I-131 HA are not the initiating factor in doxorubicin cardiotoxicity .

## Item bc5cdr:test:1419
Example input:
Sentence: We report a favorable response to treatment with citalopram by a 15-year-old boy with major depression who exhibited palpebral twitching during his first 2 weeks of treatment .

Example answer:
{"entities": [{"text": "citalopram", "type": "Chemical"}, {"text": "major depression", "type": "Disease"}, {"text": "palpebral twitching", "type": "Disease"}]}

Example input:
Sentence: When hippocampal ACh was measured during testing for handling-induced convulsions , extracellular ACh was significantly elevated ( 192 % ) in WSP mice , but was nonsignificantly elevated ( 59 % ) in WSR mice .

Example answer:
{"entities": [{"text": "ACh", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}]}

Example input:
Sentence: Rabbit syndrome , antidepressant use , and cerebral perfusion SPECT scan findings .

Example answer:
{"entities": [{"text": "Rabbit syndrome", "type": "Disease"}, {"text": "antidepressant", "type": "Chemical"}]}

Example input:
Sentence: Compared with placebo subjects , alprazolam patients developed more adverse reactions ( 21 % v. 0 % ) of depression , enuresis , disinhibition and aggression ; and more side-effects , particularly sedation , irritability , impaired memory , weight loss and ataxia .

Example answer:
{"entities": [{"text": "alprazolam", "type": "Chemical"}, {"text": "depression", "type": "Disease"}, {"text": "enuresis", "type": "Disease"}, {"text": "aggression", "type": "Disease"}, {"text": "irritability", "type": "Disease"}, {"text": "impaired memory", "type": "Disease"}, {"text": "weight loss", "type": "Disease"}, {"text": "ataxia", "type": "Disease"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: Delirium , which may be induced by tricyclic drug therapy in the elderly , can be caused by tricyclics with low anticholinergic potency .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}]}

Example input:
Sentence: The aim of the present study was to find out whether TRI given repeatedly was able to induce adaptive changes in the dopaminergic and alpha1-adrenergic systems , demonstrated by us previously for various antidepressants .

Example answer:
{"entities": [{"text": "TRI", "type": "Chemical"}, {"text": "antidepressants", "type": "Chemical"}]}

Example input:
Sentence: Trimipramine ( TRI ) , which shows a clinical antidepressant activity , is chemically related to imipramine but does not inhibit the reuptake of noradrenaline and 5-hydroxytryptamine , nor does it induce beta-adrenergic down-regulation .

Example answer:
{"entities": [{"text": "Trimipramine", "type": "Chemical"}, {"text": "TRI", "type": "Chemical"}, {"text": "antidepressant", "type": "Chemical"}, {"text": "imipramine", "type": "Chemical"}, {"text": "noradrenaline", "type": "Chemical"}, {"text": "5-hydroxytryptamine", "type": "Chemical"}]}

Example input:
Sentence: Conventional agents are associated with unwanted central nervous system effects , including extrapyramidal symptoms ( EPS ) , tardive dyskinesia , sedation , and possible impairment of some cognitive measures , as well as cardiac effects , orthostatic hypotension , hepatic changes , anticholinergic side effects , sexual dysfunction , and weight gain .

Example answer:
{"entities": [{"text": "extrapyramidal symptoms", "type": "Disease"}, {"text": "EPS", "type": "Disease"}, {"text": "tardive dyskinesia", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}]}

Example input:
Sentence: It may be concluded that , like other tricyclic antidepressants studied previously , TRI given repeatedly increases the responsiveness of brain dopamine D2 and D3 ( locomotor activity but not stereotypy ) as well as alpha1-adrenergic receptors to their agonists .

Example answer:
{"entities": [{"text": "antidepressants", "type": "Chemical"}, {"text": "TRI", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Input:
Sentence: The correlation between high serum tricyclic antidepressant concentrations and central nervous system side effects has been well established .

## Item bc5cdr:test:1163
Example input:
Sentence: Reduction in the dosage of amiodarone resulted in the disappearance of the sinoatrial block and the persistence of asymptomatic sinus bradycardia .

Example answer:
{"entities": [{"text": "amiodarone", "type": "Chemical"}, {"text": "sinoatrial block", "type": "Disease"}, {"text": "sinus bradycardia", "type": "Disease"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: Ten cm H2O CPAP before nitroprusside infusion produced a further decrease in arterial blood pressure and significantly increased heart rate and decreased cardiac output and QS/QT .

Example answer:
{"entities": [{"text": "H2O", "type": "Chemical"}, {"text": "nitroprusside", "type": "Chemical"}, {"text": "decrease in arterial blood pressure", "type": "Disease"}, {"text": "decreased cardiac output", "type": "Disease"}]}

Example input:
Sentence: The evoked increases in dural blood flow were also abolished by topical pre-administration of atropine ( 1 mm ) and [ Lys1 , Pro2,5 , Arg3,4 , Tyr6 ] -VIP ( 0.1 mm ) , a vasoactive intestinal polypeptide ( VIP ) antagonist , onto the exposed dura mater .

Example answer:
{"entities": [{"text": "increases in dural blood flow", "type": "Disease"}, {"text": "atropine", "type": "Chemical"}]}

Example input:
Sentence: In Mg ( 2+ ) -free bathing medium containing bicuculline , conditions designed to increase excitability in the slices , electrical stimulation of the hilus resulted in a single population spike in granule cells from control mice and pilocarpine-treated mice that did not experience SE .

Example answer:
{"entities": [{"text": "Mg", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "pilocarpine-treated", "type": "Chemical"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: During the infusion of aminophylline , the ventricular fibrillation threshold was reduced by 30 to 40 percent of the control when pH and partial pressures of oxygen ( PO2 ) and carbon dioxide ( CO2 ) were kept within normal limits .

Example answer:
{"entities": [{"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}, {"text": "oxygen", "type": "Chemical"}, {"text": "PO2", "type": "Chemical"}, {"text": "carbon dioxide", "type": "Chemical"}, {"text": "CO2", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: The [ verapamil ] o that arrested atrial beating ( AC ) was also potentiated with the order LNa = LNa+LCa = LNa+HCa = LCa > HCa = N. The results indicate that rat atrial spontaneous beating is more dependent on [ Na ] o than on [ Ca ] o in a range of +/- 50 % of their normal concentration .

Example answer:
{"entities": [{"text": "verapamil", "type": "Chemical"}, {"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}]}

Example input:
Sentence: As a consequence of blocking I ( f ) , clonidine reduced the slope of the diastolic depolarization and the frequency of pacemaker potentials in sinoatrial node cells from wild-type and alpha2ABC-knockout mice .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: The convulsant activity of bupivacaine was not significantly modified but calcium channel blockers decreased the time of latency to obtain bupivacaine-induced convulsions ; this effect was less pronounced with bepridil .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "bupivacaine-induced", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "bepridil", "type": "Chemical"}]}

Input:
Sentence: In vitro perfusion of bepridil in the life-support medium for isolated sino-atrial tissue from rabbit heart , caused a reduction in action potential ( AP ) spike frequency ( recorded by KCl microelectrodes ) starting at doses of 5 X 10 ( -6 ) M. This effect was dose-dependent up to concentrations of 5 X 10 ( -5 ) M , whereupon blockade of sinus activity set in .

## Item bc5cdr:test:1415
Example input:
Sentence: PATIENTS AND METHODS : Forty-six eligible patients with measurable lesions were included and were stratified according to previous chemotherapy .

Example answer:
{"entities": []}

Example input:
Sentence: Patients with stage D2-3 disease , abnormal hemoglobin level or renal and liver function tests that were higher than the upper limits were excluded from the study .

Example answer:
{"entities": []}

Example input:
Sentence: Three patients had no change and disease progressed in two .

Example answer:
{"entities": []}

Example input:
Sentence: One patient had complete response , seven had stable disease , none had partial response and five had progressive disease .

Example answer:
{"entities": []}

Example input:
Sentence: The majority of patients ( > 60 % ) experienced no change in their disease status from baseline .

Example answer:
{"entities": []}

Example input:
Sentence: The historical controls consisted of 50 consecutive patients who underwent CT without prophylactic lamivudine .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Six of 30 patients ( 20 % ) without prior chemotherapy achieved a partial response ( PR ) ( 95 % confidence interval [ CI ] , 8 % to 39 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: From June 2004 to October 2006 , 11 HBs Ag positive patients with rheumatologic diseases , who were on both immunosuppressive and prophylactic lamivudine therapies , were retrospectively assessed .

Example answer:
{"entities": [{"text": "HBs Ag", "type": "Chemical"}, {"text": "rheumatologic diseases", "type": "Disease"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: Exclusion criteria included CNS leukemic infiltration at diagnosis , therapy-related peripheral neuropathy , late-onset encephalopathy , or long-term neurocognitive defects .

Example answer:
{"entities": [{"text": "leukemic infiltration", "type": "Disease"}, {"text": "peripheral neuropathy", "type": "Disease"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "neurocognitive defects", "type": "Disease"}]}

Example input:
Sentence: Finally , 15 patients were excluded from the study ( noncompliance 14 , death 1 ) ; thus , 60 patients ( 31 in group I and 29 in group II ) were eligible for analysis .

Example answer:
{"entities": [{"text": "death", "type": "Disease"}]}

Input:
Sentence: No patient was disabled and no lymphoproliferative disorder was observed .

## Item bc5cdr:test:1274
Example input:
Sentence: CONCLUSIONS : The combination of paclitaxel , cisplatin , and gemcitabine is well tolerated and shows high activity in metastatic NSCLC .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "NSCLC", "type": "Disease"}]}

Example input:
Sentence: Paclitaxel/cisplatin is an effective first-line regimen for locoregionally advanced head and neck cancer and continued study is warranted .

Example answer:
{"entities": [{"text": "Paclitaxel/cisplatin", "type": "Chemical"}, {"text": "head and neck cancer", "type": "Disease"}]}

Example input:
Sentence: With paclitaxel doses of 200 mg/m2 and higher , granulocyte colony-stimulating factor 5 micrograms/kg/d is given ( days 4 through 12 ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}]}

Example input:
Sentence: After 154 courses of therapy , the median dose intensity was 131 mg/m ( 2 ) for paclitaxel ( 97.3 % ) , 117 mg/m ( 2 ) for cisplatin ( 97.3 % ) , and 1378 mg/m ( 2 ) for gemcitabine ( 86.2 % ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}]}

Example input:
Sentence: After completion of the amifostine infusion , cisplatin 120 mg/m2 was administered over 30 minutes .

Example answer:
{"entities": [{"text": "amifostine", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: Preliminary results of an Eastern Cooperative Oncology Group study of single-agent paclitaxel ( Taxol ; Bristol-Myers Squibb Company , Princeton , NJ ) reported a 37 % response rate in patients with head and neck cancer , and the paclitaxel/cisplatin combination has been used successfully and has significantly improved median response duration in ovarian cancer patients .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "Taxol", "type": "Chemical"}, {"text": "head and neck cancer", "type": "Disease"}, {"text": "paclitaxel/cisplatin", "type": "Chemical"}, {"text": "ovarian cancer", "type": "Disease"}]}

Example input:
Sentence: STUDY DESIGN : We combined paclitaxel , melphalan and high-dose cyclophosphamide , thiotepa , and carboplatin in a triple sequential high-dose regimen for patients with metastatic breast cancer .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "melphalan", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "thiotepa", "type": "Chemical"}, {"text": "carboplatin", "type": "Chemical"}, {"text": "breast cancer", "type": "Disease"}]}

Example input:
Sentence: Thirty-five consecutive chemotherapy-naive patients with Stage IV NSCLC and an Eastern Cooperative Oncology Group performance status of 0-2 were treated with a combination of paclitaxel ( 135 mg/m ( 2 ) given intravenously in 3 hours ) on Day 1 , cisplatin ( 120 mg/m ( 2 ) given intravenously in 6 hours ) on Day 1 , and gemcitabine ( 800 mg/m ( 2 ) given intravenously in 30 minutes ) on Days 1 and 8 , every 4 weeks .

Example answer:
{"entities": [{"text": "NSCLC", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}]}

Example input:
Sentence: We initiated a phase I/II trial to determine the response and toxicity of escalating paclitaxel doses combined with fixed-dose cisplatin with granulocyte colony-stimulating factor support in patients with untreated locally advanced inoperable head and neck carcinoma .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "head and neck carcinoma", "type": "Disease"}]}

Example input:
Sentence: Treatment , given every 21 days for a maximum of three cycles , consisted of paclitaxel by 3-hour infusion followed the next day by a fixed dose of cisplatin ( 75 mg/m2 ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Input:
Sentence: Paclitaxel 3-hour infusion given alone and combined with carboplatin : preliminary results of dose-escalation trials .

## Item bc5cdr:test:1199
Example input:
Sentence: In the bolus group , 26.0 % ( 13/50 ) had akathisia compared with 32.7 % ( 16/49 ) in the infusion group ( Delta=-6.7 % ; 95 % confidence interval [ CI ] -24.6 % to 11.2 % ) .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: Dizziness was less marked than sedation , but increased with the dose .

Example answer:
{"entities": [{"text": "Dizziness", "type": "Disease"}]}

Example input:
Sentence: Fewer subjects reported adverse events following treatment with desipramine alone than when receiving desipramine with cinacalcet ( 33 versus 86 % ) , the most frequent of which ( nausea and headache ) have been reported for patients treated with either desipramine or cinacalcet .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}, {"text": "nausea", "type": "Disease"}, {"text": "headache", "type": "Disease"}]}

Example input:
Sentence: Conventional agents are associated with unwanted central nervous system effects , including extrapyramidal symptoms ( EPS ) , tardive dyskinesia , sedation , and possible impairment of some cognitive measures , as well as cardiac effects , orthostatic hypotension , hepatic changes , anticholinergic side effects , sexual dysfunction , and weight gain .

Example answer:
{"entities": [{"text": "extrapyramidal symptoms", "type": "Disease"}, {"text": "EPS", "type": "Disease"}, {"text": "tardive dyskinesia", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: Suxamethonium causes prolonged apnea in patients in whom pseudocholinesterase enzyme gets deactivated by organophosphorus ( OP ) poisons .

Example answer:
{"entities": [{"text": "Suxamethonium", "type": "Chemical"}, {"text": "apnea", "type": "Disease"}, {"text": "organophosphorus ( OP ) poisons", "type": "Chemical"}]}

Example input:
Sentence: In phase A , extrapyramidal signs tended to be greater with the standard dose than in the other two conditions , primarily because of a subgroup ( 20 % ) who developed moderate to severe signs .

Example answer:
{"entities": [{"text": "extrapyramidal signs", "type": "Disease"}]}

Example input:
Sentence: The most common adverse events ( incidence > or = 5 % in one group ) after rizatriptan and ergotamine/caffeine , respectively , were dizziness ( 6.7 and 5.3 % ) , nausea ( 4.2 and 8.5 % ) and somnolence ( 5.5 and 2.3 % ) .

Example answer:
{"entities": [{"text": "rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}, {"text": "dizziness", "type": "Disease"}, {"text": "nausea", "type": "Disease"}, {"text": "somnolence", "type": "Disease"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: Minor side effects included nausea ( thirteen patients ) , emesis ( eight of the thirteen patients with nausea ) , clumsiness ( evident as ataxic movements in ten patients ) , and dysphoric reaction ( one patient ) .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "emesis", "type": "Disease"}, {"text": "clumsiness", "type": "Disease"}, {"text": "ataxic movements", "type": "Disease"}, {"text": "dysphoric reaction", "type": "Disease"}]}

Input:
Sentence: The Dimer-X group had a higher incidence of nausea and dizziness .

## Item bc5cdr:test:1297
Example input:
Sentence: METHODS : Neonatal rats were treated with the tricyclic antidepressant clomipramine or vehicle between days 9 and 16 twice daily and behaviorally tested in adulthood .

Example answer:
{"entities": [{"text": "antidepressant", "type": "Chemical"}, {"text": "clomipramine", "type": "Chemical"}]}

Example input:
Sentence: Development of ocular myasthenia during pegylated interferon and ribavirin treatment for chronic hepatitis C. A 63-year-old male experienced sudden diplopia after 9 weeks of administration of pegylated interferon ( IFN ) alpha-2b and ribavirin for chronic hepatitis C ( CHC ) .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated interferon", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "chronic hepatitis", "type": "Disease"}, {"text": "diplopia", "type": "Disease"}, {"text": "pegylated interferon ( IFN ) alpha-2b", "type": "Chemical"}, {"text": "chronic hepatitis C", "type": "Disease"}, {"text": "CHC", "type": "Disease"}]}

Example input:
Sentence: We report an undiagnosed case of myotonia congenita in a 24-year-old previously healthy primigravida , who developed life threatening masseter spasm following a standard dose of intravenous suxamethonium for induction of anaesthesia .

Example answer:
{"entities": [{"text": "myotonia congenita", "type": "Disease"}, {"text": "masseter spasm", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: Intravenous administration of a single 50-mg bolus of lidocaine in a 67-year-old man resulted in profound depression of the activity of the sinoatrial and atrioventricular nodal pacemakers .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: A 17-day-old infant on isoniazid therapy 13 mg/kg daily from birth because of maternal tuberculosis was admitted after 4 days of clonic fits .

Example answer:
{"entities": [{"text": "isoniazid", "type": "Chemical"}, {"text": "tuberculosis", "type": "Disease"}, {"text": "clonic fits", "type": "Disease"}]}

Example input:
Sentence: Frequency of absences increased in four children treated with carbamazepine and two of these developed myoclonic jerks , which resolved on withdrawal of carbamazepine .

Example answer:
{"entities": [{"text": "carbamazepine", "type": "Chemical"}, {"text": "myoclonic jerks", "type": "Disease"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: One of the twins developed complete heart block and dilated cardiomyopathy related to lopinavir/ritonavir therapy , a boosted protease-inhibitor agent , while the other twin developed mild bradycardia .

Example answer:
{"entities": [{"text": "heart block", "type": "Disease"}, {"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "lopinavir/ritonavir", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: We report a case of a 51-year-old man who developed severe , disabling negative myoclonus of the upper and lower extremities after the infusion of ifosfamide for plasmacytoma .

Example answer:
{"entities": [{"text": "myoclonus", "type": "Disease"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "plasmacytoma", "type": "Disease"}]}

Example input:
Sentence: We report a favorable response to treatment with citalopram by a 15-year-old boy with major depression who exhibited palpebral twitching during his first 2 weeks of treatment .

Example answer:
{"entities": [{"text": "citalopram", "type": "Chemical"}, {"text": "major depression", "type": "Disease"}, {"text": "palpebral twitching", "type": "Disease"}]}

Input:
Sentence: Three young infants , all of birth weight < 1,500 g , experienced myoclonus following the intravenous administration of lorazepam .

## Item bc5cdr:test:1317
Example input:
Sentence: RESULTS : For the 60 patients who completed phase A , standard-dose haloperidol was efficacious and superior to both low-dose haloperidol and placebo for scores on the Brief Psychiatric Rating Scale psychosis factor and on psychomotor agitation .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "psychosis", "type": "Disease"}, {"text": "psychomotor agitation", "type": "Disease"}]}

Example input:
Sentence: Grade less than or equal to 2 nausea and vomiting occurred in 66 % courses and phlebitis in the infusion arm in 37 % .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "vomiting", "type": "Disease"}, {"text": "phlebitis", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Minutes after oral administration , the patient developed nausea , sweating and hypotension , and finally collapsed .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: There were no serious clinical side effects , but dose reduction was required in two patients because of nausea .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}]}

Example input:
Sentence: Response rates according to three sets of criteria were greater with the standard dose ( 55 % -60 % ) than the low dose ( 25 % -35 % ) and placebo ( 25 % -30 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: An initial dose of 0.1 microgram.kg-1.min-1 of PGE1 ( 15 patients ) , or 10 micrograms.kg-1.min-1 of TMP ( 15 patients ) was administered intravenously after the dural opening and the dose was adjusted to maintain the mean arterial blood pressure ( MAP ) at about 60 mmHg .

Example answer:
{"entities": [{"text": "PGE1", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}]}

Example input:
Sentence: The difference in the percentage of patients with a 50 % reduction in their nausea was 12.6 % ( 95 % CI -4.6 % to 29.8 % ) .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}]}

Example input:
Sentence: In phase A , extrapyramidal signs tended to be greater with the standard dose than in the other two conditions , primarily because of a subgroup ( 20 % ) who developed moderate to severe signs .

Example answer:
{"entities": [{"text": "extrapyramidal signs", "type": "Disease"}]}

Example input:
Sentence: Pain intensity on a 0 to 10 numerical scale ; nausea and vomiting , drowsiness , confusion , and dry mouth , using a scale from 0 to 3 ( not at all , slight , a lot , awful ) ; Mini-Mental State Examination ( MMSE ) ( 0-30 ) ; and arterial pressure were recorded before administration of drugs ( T0 ) and after 30 minutes ( T30 ) , 60 minutes ( T60 ) , 120 minutes ( T120 ) , and 180 minutes ( T180 ) .

Example answer:
{"entities": [{"text": "Pain", "type": "Disease"}, {"text": "nausea", "type": "Disease"}, {"text": "vomiting", "type": "Disease"}, {"text": "confusion", "type": "Disease"}, {"text": "dry mouth", "type": "Disease"}]}

Example input:
Sentence: Antiemetic requirements were reduced from 24 % and 31 % to 7 % ( P = 0.0012 ) .

Example answer:
{"entities": []}

Input:
Sentence: There was a statistically longer time to first episode of nausea ( P = .0015 ) and vomiting ( P = .0001 ) , and fewer patients were administered additional antiemetic medication in the 10-micrograms/kg dosing groups than in the 5-micrograms/kg dosing group .

## Item bc5cdr:test:1460
Example input:
Sentence: The incidence of cardiotoxicity was not higher in patients with signs of cardiovascular disease than in those without in the pre-treatment evaluation .

Example answer:
{"entities": [{"text": "cardiotoxicity", "type": "Disease"}, {"text": "cardiovascular disease", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Cardiac troponins I ( cTnI ) and T ( cTnT ) have been shown to be highly sensitive and specific markers of myocardial cell injury .

Example answer:
{"entities": [{"text": "myocardial cell injury", "type": "Disease"}]}

Example input:
Sentence: We investigated the diagnostic value of cTnI and cTnT for the diagnosis of myocardial damage in a rat model of doxorubicin ( DOX ) -induced cardiomyopathy , and we examined the relationship between serial cTnI and cTnT with the development of cardiac disorders monitored by echocardiography and histological examinations in this model .

Example answer:
{"entities": [{"text": "myocardial damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiac disorders", "type": "Disease"}]}

Example input:
Sentence: The cardiotoxic effects of adriamycin were studied in mammalian myocardial cells in culture as a model system .

Example answer:
{"entities": [{"text": "cardiotoxic", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVES : To assess the added diagnostic value of a new cardiac performance index ( dP/dtejc ) measurement , based on brachial artery flow changes , as compared to standard 12-lead ECG , for detecting dobutamine-induced myocardial ischemia , using Tc99m-Sestamibi single-photon emission computed tomography as the gold standard of comparison to assess the presence or absence of ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "Tc99m-Sestamibi", "type": "Chemical"}, {"text": "ischemia", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Among markers of ischemic injury after DOX in rats , cTnT showed the greatest ability to detect myocardial damage assessed by echocardiographic detection and histological changes .

Example answer:
{"entities": [{"text": "ischemic injury", "type": "Disease"}, {"text": "DOX", "type": "Chemical"}, {"text": "myocardial damage", "type": "Disease"}]}

Example input:
Sentence: Although there was a discrepancy between the amount of cTnI and cTnT after DOX , probably due to heterogeneity in cross-reactivities of mAbs to various cTnI and cTnT forms , it is likely that cTnT in rats after DOX indicates cell damage determined by the magnitude of injury induced and that cTnT should be a useful marker for the prediction of experimentally induced cardiotoxicity and possibly for cardioprotective experiments .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: The cardiotoxicity of conventional anthracycline therapy highlights a need to search for methods that are highly sensitive and capable of predicting cardiac dysfunction .

Example answer:
{"entities": [{"text": "cardiotoxicity", "type": "Disease"}, {"text": "anthracycline", "type": "Chemical"}, {"text": "cardiac dysfunction", "type": "Disease"}]}

Example input:
Sentence: The most common signs of cardiotoxicity were chest pain , ST-T wave changes and atrial fibrillation .

Example answer:
{"entities": [{"text": "cardiotoxicity", "type": "Disease"}, {"text": "chest pain", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}]}

Example input:
Sentence: These preliminary results suggest that BNP may be useful as an early and sensitive indicator of anthracycline-induced cardiotoxicity .

Example answer:
{"entities": [{"text": "anthracycline-induced", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Input:
Sentence: The results indicate that this new model is very sensitive and enables monitoring of the development of cardiotoxicity with time .

## Item bc5cdr:test:1169
Example input:
Sentence: Massive proteinuria and acute renal failure after oral bisphosphonate ( alendronate ) administration in a patient with focal segmental glomerulosclerosis .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "bisphosphonate", "type": "Chemical"}, {"text": "alendronate", "type": "Chemical"}, {"text": "focal segmental glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: Based on a score of 8 on the Naranjo adverse drug reaction probability scale , telithromycin was the probable cause of acute hepatitis in this patient , and pathological findings suggested drug-induced toxic hepatitis .

Example answer:
{"entities": [{"text": "adverse drug reaction", "type": "Disease"}, {"text": "telithromycin", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}, {"text": "toxic hepatitis", "type": "Disease"}]}

Example input:
Sentence: Here , 2 cases of urinary bladder retention leading to renal pelvocalyceal dilatation mimicking hydronephrosis as a result of continuous infusion of fentanyl are reported .

Example answer:
{"entities": [{"text": "urinary bladder retention", "type": "Disease"}, {"text": "hydronephrosis", "type": "Disease"}, {"text": "fentanyl", "type": "Chemical"}]}

Example input:
Sentence: The remaining patient in the series developed fulminant hepatitis when the drug was accidentally recommenced 1 year after a prior episode of methyldopa-induced hepatitis .

Example answer:
{"entities": [{"text": "fulminant hepatitis", "type": "Disease"}, {"text": "methyldopa-induced", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: A patient with cryptogenic cirrhosis and disseminated sporotrichosis developed acute renal failure immediately following the administration of amphotericin B on four separate occasions .

Example answer:
{"entities": [{"text": "cirrhosis", "type": "Disease"}, {"text": "sporotrichosis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}]}

Example input:
Sentence: Granulomatous hepatitis due to combination of amoxicillin and clavulanic acid .

Example answer:
{"entities": [{"text": "combination of amoxicillin and clavulanic acid", "type": "Chemical"}]}

Example input:
Sentence: A case of metabolic acidosis , acute renal failure and hepatic failure following paracetamol ingestion is presented .

Example answer:
{"entities": [{"text": "metabolic acidosis", "type": "Disease"}, {"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: METHODS : This double-blind study examined the incidence and severity of postoperative nausea and vomiting and pain in the first 24 h after sevoflurane anaesthesia in 216 adult day surgery patients .

Example answer:
{"entities": [{"text": "postoperative nausea and vomiting", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "sevoflurane", "type": "Chemical"}]}

Example input:
Sentence: We have reported a case of acute oliguric renal failure with hyperkalemia in a patient with cirrhosis , ascites , and cor pulmonale after indomethacin therapy .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "cor pulmonale", "type": "Disease"}, {"text": "indomethacin", "type": "Chemical"}]}

Example input:
Sentence: An allergic reaction consisting of angioneurotic edema secondary to continuous infusion 5-fluorouracil occurred in a patient with recurrent carcinoma of the oral cavity , cirrhosis , and cisplatin-induced impaired renal function .

Example answer:
{"entities": [{"text": "allergic reaction", "type": "Disease"}, {"text": "angioneurotic edema", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "carcinoma of the oral cavity", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "impaired renal function", "type": "Disease"}]}

Input:
Sentence: Hepatitis and renal tubular acidosis after anesthesia with methoxyflurane .

## Item bc5cdr:test:1264
Example input:
Sentence: She subsequently died some 5 weeks after the commencement of her drug therapy.Post-mortem examination showed evidence of massive hepatocellular necrosis , acute hypersensitivity myocarditis , focal acute tubulo-interstitial nephritis and extensive bone marrow necrosis , with no evidence of malignancy .

Example answer:
{"entities": [{"text": "massive hepatocellular necrosis", "type": "Disease"}, {"text": "myocarditis", "type": "Disease"}, {"text": "nephritis", "type": "Disease"}, {"text": "bone marrow necrosis", "type": "Disease"}, {"text": "malignancy", "type": "Disease"}]}

Example input:
Sentence: We report the case of a patient who developed acute hepatitis with extensive hepatocellular necrosis , 7 months after the onset of administration of clotiazepam , a thienodiazepine derivative .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}, {"text": "extensive hepatocellular necrosis", "type": "Disease"}, {"text": "clotiazepam", "type": "Chemical"}, {"text": "thienodiazepine", "type": "Chemical"}]}

Example input:
Sentence: A patient with cryptogenic cirrhosis and disseminated sporotrichosis developed acute renal failure immediately following the administration of amphotericin B on four separate occasions .

Example answer:
{"entities": [{"text": "cirrhosis", "type": "Disease"}, {"text": "sporotrichosis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}]}

Example input:
Sentence: During an 18-month period of study 41 hemodialyzed patients receiving desferrioxamine ( 10-40 mg/kg BW/3 times weekly ) for the first time were monitored for detection of audiovisual toxicity .

Example answer:
{"entities": [{"text": "desferrioxamine", "type": "Chemical"}, {"text": "audiovisual toxicity", "type": "Disease"}]}

Example input:
Sentence: A 78-year-old with healed septal necrosis suffered a recurrent myocardial infarction of the anterior wall following the administration of isosorbide dinitrate 5 mg sublingually .

Example answer:
{"entities": [{"text": "necrosis", "type": "Disease"}, {"text": "myocardial infarction", "type": "Disease"}, {"text": "isosorbide dinitrate", "type": "Chemical"}]}

Example input:
Sentence: Acute hepatitis , autoimmune hemolytic anemia , and erythroblastocytopenia induced by ceftriaxone .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}, {"text": "autoimmune hemolytic anemia", "type": "Disease"}, {"text": "erythroblastocytopenia", "type": "Disease"}, {"text": "ceftriaxone", "type": "Chemical"}]}

Example input:
Sentence: An 80-yr-old man developed acute hepatitis shortly after ingesting oral ceftriaxone .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}, {"text": "ceftriaxone", "type": "Chemical"}]}

Example input:
Sentence: A 34-year-old lady developed a constellation of dermatitis , fever , lymphadenopathy and hepatitis , beginning on the 17th day of a course of oral sulphasalazine for sero-negative rheumatoid arthritis .

Example answer:
{"entities": [{"text": "dermatitis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "lymphadenopathy", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Example input:
Sentence: A 54-year-old hypothyroid male taking thyroxine and simvastatin presented with bilateral leg compartment syndrome and myonecrosis .

Example answer:
{"entities": [{"text": "hypothyroid", "type": "Disease"}, {"text": "thyroxine", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "compartment syndrome", "type": "Disease"}, {"text": "myonecrosis", "type": "Disease"}]}

Example input:
Sentence: Two patients developed acute tubular necrosis , characterized clinically by acute oliguric renal failure , while they were receiving a combination of cephalothin sodium and gentamicin sulfate therapy .

Example answer:
{"entities": [{"text": "acute tubular necrosis", "type": "Disease"}, {"text": "cephalothin sodium", "type": "Chemical"}, {"text": "gentamicin sulfate", "type": "Chemical"}]}

Input:
Sentence: The one case of toxic epidermal necrolysis occurred in a patient who took cephalexin .

## Item bc5cdr:test:1036
Example input:
Sentence: Acute normal tissue toxicities ( i.e. , leukopenia and thrombocytopenia ) and late normal tissue toxicities ( i.e. , myocardial and kidney injury ) were evaluated by functional/physiological assays and by morphological techniques .

Example answer:
{"entities": [{"text": "toxicities", "type": "Disease"}, {"text": "leukopenia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}]}

Example input:
Sentence: Patients who develop ESRD have a higher preoperative and 1-year serum creatinine and are more likely to have hepatorenal syndrome .

Example answer:
{"entities": [{"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "hepatorenal syndrome", "type": "Disease"}]}

Example input:
Sentence: RESULTS : The main pathologic diagnoses ( some overlap ) were acute rejection ( AR ; n = 4 ) , chronic rejection ( CR ; n=5 ) , AR+CR ( n =4 ) , recurrent IgA nephropathy ( n =5 ) , normal findings ( n =2 ) , minimal-type chronic FK506 nephropathy ( n = 9 ) , and mild-type FK506 nephropathy ( n = 11 ) .

Example answer:
{"entities": [{"text": "IgA nephropathy", "type": "Disease"}, {"text": "FK506", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: Most of these patients had more than two metastatic sites , with lung metastasis predominant .

Example answer:
{"entities": []}

Example input:
Sentence: Histologic examination of the renal tissue showed evidence of intravascular coagulation , primarily affecting the small arteries , arterioles , and glomeruli .

Example answer:
{"entities": [{"text": "intravascular coagulation", "type": "Disease"}]}

Example input:
Sentence: Histopathology analyses in the 2 animals that died revealed liver and kidney toxicity , with greater severity in the orally-treated animal .

Example answer:
{"entities": []}

Example input:
Sentence: Histopathological examination of kidney , heart and lung sections revealed moderate to massive tissue damage with a variety of morphological aberrations by all the three drugs in the absence of GSPE preexposure than in its presence .

Example answer:
{"entities": [{"text": "tissue damage", "type": "Disease"}, {"text": "GSPE", "type": "Chemical"}]}

Example input:
Sentence: There was no serologic evidence of viral infection , and a liver biopsy sample showed a histologic pattern consistent with drug-induced hepatitis .

Example answer:
{"entities": [{"text": "viral infection", "type": "Disease"}, {"text": "drug-induced hepatitis", "type": "Disease"}]}

Example input:
Sentence: FINDINGS : The liver biopsy sample showed hepatocellular necrosis which was prominent in perivenular zone three and extended focally from portal tracts to portal tracts and centrilobular areas ( bridging necrosis ) .

Example answer:
{"entities": [{"text": "necrosis", "type": "Disease"}]}

Example input:
Sentence: Gastrointestinal bleed , seizures , infection , and acute renal failure were documented in seven ( 10 % ) , five ( 7.1 % ) , 26 ( 37.1 % ) , and seven ( 10 % ) patients , respectively .

Example answer:
{"entities": [{"text": "Gastrointestinal bleed", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "infection", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}]}

Input:
Sentence: Analysis of site of infection showed a preponderance of abdominal infections in liver patients , intrathoracic infections in heart patients , and urinary tract infections in renal patients .

## Item bc5cdr:test:1024
Example input:
Sentence: Tamoxifen ( TAM ) , the antiestrogenic drug most widely prescribed in the chemotherapy of breast cancer , induces changes in normal discoid shape of erythrocytes and hemolytic anemia .

Example answer:
{"entities": [{"text": "Tamoxifen", "type": "Chemical"}, {"text": "TAM", "type": "Chemical"}, {"text": "breast cancer", "type": "Disease"}, {"text": "hemolytic anemia", "type": "Disease"}]}

Example input:
Sentence: Seven patients had previously received radiotherapy and seven had received hormone therapy .

Example answer:
{"entities": []}

Example input:
Sentence: Using macaque monkeys with different types of MPTP-induced parkinsonism , the current study evaluated the degree to which rate of symptom progression , symptom severity , and response to and duration of levodopa therapy may be involved in the development of LIDs .

Example answer:
{"entities": [{"text": "MPTP-induced", "type": "Chemical"}, {"text": "parkinsonism", "type": "Disease"}, {"text": "levodopa", "type": "Chemical"}, {"text": "LIDs", "type": "Disease"}]}

Example input:
Sentence: The full syndrome of subacute myelo-optic neuropathy was more frequent in women , but they tended to have taken greater quantities of the drug .

Example answer:
{"entities": []}

Example input:
Sentence: We conducted a 12-month controlled trial of mazindol , a putative growth hormone secretion inhibitor , in 83 boys with Duchenne dystrophy .

Example answer:
{"entities": [{"text": "mazindol", "type": "Chemical"}, {"text": "Duchenne dystrophy", "type": "Disease"}]}

Example input:
Sentence: A comprehensive examination including her medical history , panoramic radiograph , and intraoral examination revealed 19 carious lesions , which is not very common for a healthy adult .

Example answer:
{"entities": [{"text": "carious lesions", "type": "Disease"}]}

Example input:
Sentence: changes increased as trough-concentrations rose , 5 patients had lumbar puncture .

Example answer:
{"entities": []}

Example input:
Sentence: Among the 5 patients with white matter abnormalities , 4 patients ( 80.0 % ) showed higher than normal ADC values on initial MR images , and all showed complete resolution on follow-up images .

Example answer:
{"entities": [{"text": "white matter abnormalities", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Initial MRIs showed abnormal high signal intensities on DWI and FLAIR ( or T2-weighted image ) at the dentate nucleus ( 8/8 ) , inferior colliculus ( 6/8 ) , corpus callosum ( 2/8 ) , pons ( 2/8 ) , medulla ( 1/8 ) , and bilateral cerebral white matter ( 1/8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: In contrast , monkeys with long-term MPTP exposure , slow symptom progression and/or long symptom duration prior to initiation of levodopa therapy were more resistant to developing LIDs ( e.g. , dyskinesia developed no sooner than 146 days of chronic levodopa administration ) .

Example answer:
{"entities": [{"text": "MPTP", "type": "Chemical"}, {"text": "levodopa", "type": "Chemical"}, {"text": "LIDs", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}]}

Input:
Sentence: Mastodynia was reported by 21 patients , and physical examination revealed a light increase in breast firmness in 12 women and a moderate increase in breast nodularity in 2 women .

## Item bc5cdr:test:1355
Example input:
Sentence: A nonregenerative anemia was the most compromising of the cytopenias and occurred in approximately 50 % of dogs receiving 400-500 mg/kg cefonicid or 540-840 mg/kg cefazedone .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "cytopenias", "type": "Disease"}, {"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}]}

Example input:
Sentence: No changes in haloperidol-induced catalepsy or MK-801-induced locomotion were seen following PD .

Example answer:
{"entities": [{"text": "haloperidol-induced", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "MK-801-induced", "type": "Chemical"}]}

Example input:
Sentence: Upon rechallenge with either cephalosporin , the hematologic syndrome was reproduced in most dogs tested ; cefonicid ( but not cefazedone ) -treated dogs showed a substantially reduced induction period ( 15 +/- 5 days ) compared to that of the first exposure to the drug ( 61 +/- 24 days ) .

Example answer:
{"entities": [{"text": "cephalosporin", "type": "Chemical"}, {"text": "hematologic syndrome", "type": "Disease"}, {"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}]}

Example input:
Sentence: Behavioral effects of diazepam and propranolol in patients with panic disorder and agoraphobia .

Example answer:
{"entities": [{"text": "diazepam", "type": "Chemical"}, {"text": "propranolol", "type": "Chemical"}, {"text": "panic disorder", "type": "Disease"}, {"text": "agoraphobia", "type": "Disease"}]}

Example input:
Sentence: The effects of oral doses of diazepam ( single dose of 10 mg and a median dose of 30 mg/day for 2 weeks ) and propranolol ( single dose of 80 mg and a median dose of 240 mg/day for 2 weeks ) on psychological performance of patients with panic disorders and agoraphobia were investigated in a double-blind , randomized and crossover design .

Example answer:
{"entities": [{"text": "diazepam", "type": "Chemical"}, {"text": "propranolol", "type": "Chemical"}, {"text": "panic disorders", "type": "Disease"}, {"text": "agoraphobia", "type": "Disease"}]}

Example input:
Sentence: We conclude that the administration of high doses of cefonicid or cefazedone to dogs can induce hematotoxicity similar to the cephalosporin-induced blood dyscrasias described in man and thus provides a useful model for studying the mechanisms of these disorders .

Example answer:
{"entities": [{"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}, {"text": "hematotoxicity", "type": "Disease"}, {"text": "cephalosporin-induced", "type": "Chemical"}, {"text": "blood dyscrasias", "type": "Disease"}]}

Example input:
Sentence: Diazepam- , scopolamine- and ageing-induced amnesia served as the interoceptive behavioral models .

Example answer:
{"entities": [{"text": "Diazepam-", "type": "Chemical"}, {"text": "scopolamine-", "type": "Chemical"}, {"text": "amnesia", "type": "Disease"}]}

Example input:
Sentence: In conclusion , CPA , diazepam and 2PAM in combination with atropine prevented the occurrence of serious signs of poisoning and thus reduced the toxicity of DFP in rat .

Example answer:
{"entities": [{"text": "CPA", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "atropine", "type": "Chemical"}, {"text": "poisoning", "type": "Disease"}, {"text": "toxicity", "type": "Disease"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: All animals were similarly symptomatic at the start of levodopa treatment and had similar therapeutic responses to the drug .

Example answer:
{"entities": [{"text": "levodopa", "type": "Chemical"}]}

Example input:
Sentence: These episodes reversed after the administration of diazepam 1 mg intravenously .

Example answer:
{"entities": [{"text": "diazepam", "type": "Chemical"}]}

Input:
Sentence: Animals became somnolent after diazepam and then active after flumazenil administration .

## Item bc5cdr:test:1503
Example input:
Sentence: In almost half of these women severe atherosclerosis of the aorta was present ( n=11 ) , while in women without hormone use severe atherosclerosis of the aorta was present in less than 20 % ( OR 3.1 ; 95 % CI , 1.1-8.5 , adjusted for age , years since menopause , smoking , and body mass index ) .

Example answer:
{"entities": [{"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: Every patient was screened for testosterone and 451 were screened for prolactin on the basis of low sexual desire , gynecomastia or testosterone less than 4 ng./ml .

Example answer:
{"entities": [{"text": "testosterone", "type": "Chemical"}, {"text": "low sexual desire", "type": "Disease"}, {"text": "gynecomastia", "type": "Disease"}]}

Example input:
Sentence: It was found that the transformation of exencephalic tissue was not simply size-dependent , and all cases of anencephaly at E18.5 resulted from embryos with a large amount of exencephalic tissue at E13.5 .

Example answer:
{"entities": [{"text": "exencephalic", "type": "Disease"}, {"text": "anencephaly", "type": "Disease"}]}

Example input:
Sentence: Transient hypotension ( SAP < 90mmHg ) occurred in 1 patient ( 0.7 % ) .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: During the study , vitamin B12 and folate levels were significantly higher in group II patients ; however , no differences in hemoglobin , hematocrit , mean corpuscular volume , and white-cell , neutrophil and platelet counts were observed between groups at 3 , 6 , 9 and 12 months .

Example answer:
{"entities": [{"text": "vitamin B12", "type": "Chemical"}, {"text": "folate", "type": "Chemical"}]}

Example input:
Sentence: Severe hematologic toxicity ( neutrophil count < 1000/mm3 and/or hemoglobin < 8 g/dl ) occurred in 4 patients assigned to group I and 7 assigned to group II .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: The Receiver Operative Characteristic Curve showed that OD > 1.27 in the isolated-HIT group had a significantly higher chance of developing thrombosis by day 30 .

Example answer:
{"entities": [{"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: Two subsets of patients were identified from this latter group : the first included four patients ( 5 % of the total population ) who developed major toxicity resulting in Fanconi 's syndrome ( TDFS ) ; and the second group included five patients with elevated beta 2 microglobulinuria and low phosphate reabsorption .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "Fanconi 's syndrome", "type": "Disease"}, {"text": "TDFS", "type": "Disease"}, {"text": "phosphate", "type": "Chemical"}]}

Example input:
Sentence: Of the 14 patients , 5 ( 35.7 % ) had white matter abnormalities , 1 ( 7.1 % ) had putaminal hemorrhage , and 8 ( 57.1 % ) had normal findings on initial MR images .

Example answer:
{"entities": [{"text": "white matter abnormalities", "type": "Disease"}, {"text": "putaminal hemorrhage", "type": "Disease"}]}

Input:
Sentence: Only 5 of the 160 F2 pituitaries exhibited the hemorrhagic phenotype ; 36 of the 160 F2 pituitaries were in the F344 range of mass , but 31 of these were not hemorrhagic , indicating that the hemorrhagic phenotype is not merely a consequence of extensive growth .

## Item bc5cdr:test:1032
Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: Seventy-five human immunodeficiency virus ( HIV ) -infected patients with CD4+ cell counts < 500/mm3 were randomized to receive either ZDV ( 500 mg daily ) alone ( group I , n = 38 ) or in combination with folinic acid ( 15 mg daily ) and intramascular vitamin B12 ( 1000 micrograms monthly ) ( group II , n = 37 ) .

Example answer:
{"entities": [{"text": "human immunodeficiency virus ( HIV ) -infected", "type": "Disease"}, {"text": "ZDV", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}, {"text": "vitamin B12", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : The main pathologic diagnoses ( some overlap ) were acute rejection ( AR ; n = 4 ) , chronic rejection ( CR ; n=5 ) , AR+CR ( n =4 ) , recurrent IgA nephropathy ( n =5 ) , normal findings ( n =2 ) , minimal-type chronic FK506 nephropathy ( n = 9 ) , and mild-type FK506 nephropathy ( n = 11 ) .

Example answer:
{"entities": [{"text": "IgA nephropathy", "type": "Disease"}, {"text": "FK506", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: RAST was positive for AX in 22 patients ( 41 % ) and to BPO in just 5 ( 9 % ) .

Example answer:
{"entities": [{"text": "AX", "type": "Chemical"}, {"text": "BPO", "type": "Chemical"}]}

Example input:
Sentence: There have been several long-term studies of patients with rheumatoid arthritis treated with azathioprine and cyclophosphamide and the incidence of most of the common cancers is not increased .

Example answer:
{"entities": [{"text": "rheumatoid arthritis", "type": "Disease"}, {"text": "azathioprine", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "cancers", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Six of 30 patients ( 20 % ) without prior chemotherapy achieved a partial response ( PR ) ( 95 % confidence interval [ CI ] , 8 % to 39 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: In our experience and according to the literature , FK506 does not seem to cross-react with cyclosporin A ( CyA ) , an immuno-suppressive drug already known to induce MAHA .

Example answer:
{"entities": [{"text": "FK506", "type": "Chemical"}, {"text": "cyclosporin A", "type": "Chemical"}, {"text": "CyA", "type": "Chemical"}, {"text": "MAHA", "type": "Disease"}]}

Example input:
Sentence: Patients who received enalapril experienced clinically and statistically significantly less symptomatic hypotension ( 5.2 % ) than the patients who received prazosin ( 12.9 % ) .

Example answer:
{"entities": [{"text": "enalapril", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "prazosin", "type": "Chemical"}]}

Example input:
Sentence: Pneumocystis pneumonia ( PCP ) , a common opportunistic infection in HIV-infected individuals , is generally treated with high doses of co-trimoxazole .

Example answer:
{"entities": [{"text": "Pneumocystis pneumonia", "type": "Disease"}, {"text": "PCP", "type": "Disease"}, {"text": "opportunistic infection", "type": "Disease"}, {"text": "HIV-infected", "type": "Disease"}, {"text": "co-trimoxazole", "type": "Chemical"}]}

Example input:
Sentence: The semi-quantitative scoring was significantly worst in the group treated with CsA plus SRL ( P < 0.001 compared with controls ) and the analysis of the total grade of fibrosis also showed the highest proportion in the same group and was significantly different from controls ( P < 0.02 ) .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "fibrosis", "type": "Disease"}]}

Input:
Sentence: The randomized Aza patients had more overall infections ( P less than 0.05 ) and more nonviral infections ( P less than 0.02 ) than the randomized cyclosporine patients .
