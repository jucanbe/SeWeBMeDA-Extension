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

## Item bc5cdr:test:2380
Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: To this end , persistent hyperalgesia was induced by administration of capsaicin in the tail of gonadally intact F344 rats , following which the tail was immersed in a mildly noxious thermal stimulus , and tail-withdrawal latencies measured .

Example answer:
{"entities": [{"text": "hyperalgesia", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "a reduced locomotor activity", "type": "Disease"}]}

Example input:
Sentence: Therefore , like VPA , the finding that VPU could drastically reduce pilocarpine-induced increases in glutamate and aspartate should account , at least partly , for its anticonvulsant activity observed in pilocarpine-induced seizure in experimental animals .

Example answer:
{"entities": [{"text": "VPA", "type": "Chemical"}, {"text": "VPU", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: In addition , mitochondrial respiratory dysfunction characterized by decreased respiratory control ratio and ADP/O was observed in isoproterenol-treated rats .

Example answer:
{"entities": [{"text": "respiratory dysfunction", "type": "Disease"}, {"text": "ADP/O", "type": "Chemical"}, {"text": "isoproterenol-treated", "type": "Chemical"}]}

Example input:
Sentence: Based on the finding that VPU and VPA could protect the animals against pilocarpine-induced seizure it is suggested that the reduction of inhibitory amino acid neurotransmitters was comparatively minor and offset by a pronounced reduction of glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: Similar to rats , systemic pilocarpine injection causes status epilepticus ( SE ) and the eventual development of spontaneous seizures and mossy fiber sprouting in C57BL/6 and CD1 mice , but the physiological correlates of these events have not been identified in mice .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: When respiratory failure was produced by hypoventilation ( pH 7.05 to 7.25 ; PC02 70 to 100 mm Hg : P02 20 to 40 mm Hg ) , infusion of aminophylline resulted in an even greater decrease in ventricular fibrillation threshold to 60 percent of the control level .

Example answer:
{"entities": [{"text": "respiratory failure", "type": "Disease"}, {"text": "hypoventilation", "type": "Disease"}, {"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Input:
Sentence: RESULTS : The hyperventilation maneuver caused a decrease in spontaneous ventilation in pilocarpine-treated and control rats .

## Item bc5cdr:test:2382
Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: The SPV during hypotension was 15.7 +/- 6.7 mm Hg in the HEM group , compared with 9.1 +/- 2.0 mm Hg in the SNP group ( P less than 0.02 ) .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "HEM", "type": "Disease"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Head-up tilt caused systolic orthostatic hypotension which was marked in six of 20 PD patients on selegiline , one of whom lost consciousness with unrecordable blood pressures .

Example answer:
{"entities": [{"text": "systolic orthostatic hypotension", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "selegiline", "type": "Chemical"}]}

Example input:
Sentence: It is concluded that increases in the SPV and the delta down are characteristic of a hypotensive state due to a predominant decrease in preload .

Example answer:
{"entities": [{"text": "hypotensive", "type": "Disease"}]}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "a reduced locomotor activity", "type": "Disease"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Iatrogenically induced intractable atrioventricular reentrant tachycardia after verapamil and catheter ablation in a patient with Wolff-Parkinson-White syndrome and idiopathic dilated cardiomyopathy .

Example answer:
{"entities": [{"text": "atrioventricular reentrant tachycardia", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "idiopathic dilated cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: The evoked increases in dural blood flow were also abolished by topical pre-administration of atropine ( 1 mm ) and [ Lys1 , Pro2,5 , Arg3,4 , Tyr6 ] -VIP ( 0.1 mm ) , a vasoactive intestinal polypeptide ( VIP ) antagonist , onto the exposed dura mater .

Example answer:
{"entities": [{"text": "increases in dural blood flow", "type": "Disease"}, {"text": "atropine", "type": "Chemical"}]}

Example input:
Sentence: During HEM-induced hypotension the cardiac output was significantly lower and systemic vascular resistance higher compared with that in the SNP group .

Example answer:
{"entities": [{"text": "HEM-induced", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: When respiratory failure was produced by hypoventilation ( pH 7.05 to 7.25 ; PC02 70 to 100 mm Hg : P02 20 to 40 mm Hg ) , infusion of aminophylline resulted in an even greater decrease in ventricular fibrillation threshold to 60 percent of the control level .

Example answer:
{"entities": [{"text": "respiratory failure", "type": "Disease"}, {"text": "hypoventilation", "type": "Disease"}, {"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}]}

Input:
Sentence: The hypoventilation maneuver led to an increase in the arterial Paco2 , followed by an increase in VE .

## Item bc5cdr:test:2385
Example input:
Sentence: A decreased glutamate uptake was observed in the subcortical parts of animals treated with reserpine and haloperidol , compared to the control .

Example answer:
{"entities": [{"text": "glutamate", "type": "Chemical"}, {"text": "reserpine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Mediation of enhanced reflex vagal bradycardia by L-dopa via central dopamine formation in dogs .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "L-dopa", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: Similar to rats , systemic pilocarpine injection causes status epilepticus ( SE ) and the eventual development of spontaneous seizures and mossy fiber sprouting in C57BL/6 and CD1 mice , but the physiological correlates of these events have not been identified in mice .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Population responses in granule cells of the dentate gyrus were examined in transverse slices of the ventral hippocampus from pilocarpine-treated and untreated mice .

Example answer:
{"entities": [{"text": "pilocarpine-treated", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : The utilization of phenylephrine to correct hypotension induced by anesthesia has a negative impact on S ( c ) O ( 2 ) while ephedrine maintains frontal lobe oxygenation potentially related to an increase in CO .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: The effects of continuous positive airway pressure ( CPAP ) on cardiovascular dynamics and pulmonary shunt ( QS/QT ) were investigated in 12 dogs before and during sodium nitroprusside infusion that decreased mean arterial blood pressure 40-50 per cent .

Example answer:
{"entities": [{"text": "sodium nitroprusside", "type": "Chemical"}]}

Example input:
Sentence: The animals were mechanically ventilated to achieve normocarbia ( PCO2 = 42 +/- 1 mmHg , mean +/- SE ) .

Example answer:
{"entities": []}

Example input:
Sentence: Therefore , like VPA , the finding that VPU could drastically reduce pilocarpine-induced increases in glutamate and aspartate should account , at least partly , for its anticonvulsant activity observed in pilocarpine-induced seizure in experimental animals .

Example answer:
{"entities": [{"text": "VPA", "type": "Chemical"}, {"text": "VPU", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Based on the finding that VPU and VPA could protect the animals against pilocarpine-induced seizure it is suggested that the reduction of inhibitory amino acid neurotransmitters was comparatively minor and offset by a pronounced reduction of glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Input:
Sentence: CONCLUSIONS : The data indicate that pilocarpine-treated animals have an altered ability to react to ( or compensate for ) blood gas changes with changes in ventilation and suggest that it is centrally determined .

## Item bc5cdr:test:2532
Example input:
Sentence: Within 8 hours after initiation of therapy the patient died with a clinical picture resembling massive pulmonary obstruction due to choriocarcinomic tissue plugs , probably originating from the uterus .

Example answer:
{"entities": [{"text": "pulmonary obstruction", "type": "Disease"}]}

Example input:
Sentence: Severe cardiovascular complications occurred in eight of 160 patients treated with terbutaline for preterm labor .

Example answer:
{"entities": [{"text": "cardiovascular complications", "type": "Disease"}, {"text": "terbutaline", "type": "Chemical"}, {"text": "preterm labor", "type": "Disease"}]}

Example input:
Sentence: A 49-year-old woman was transferred to our department because of quadriparesis , lancinating pain , sensory loss , and paresthesia of the distal limbs .

Example answer:
{"entities": [{"text": "quadriparesis", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "sensory loss", "type": "Disease"}, {"text": "paresthesia", "type": "Disease"}]}

Example input:
Sentence: Organic mental disorder was observed in a 29-year-old female in the prognostic period after the onset of carmofur-induced leukoencephalopathy .

Example answer:
{"entities": [{"text": "Organic mental disorder", "type": "Disease"}, {"text": "carmofur-induced", "type": "Chemical"}, {"text": "leukoencephalopathy", "type": "Disease"}]}

Example input:
Sentence: Based on this principle a 27-year old woman , classified as being in the high-risk group ( Goldstein and Berkowitz score : 11 ) , was treated with multiple cytotoxic drugs .

Example answer:
{"entities": []}

Example input:
Sentence: In this report we describe the case of a 37-year-old white woman with Ebstein 's anomaly , who developed a rare syndrome called platypnea-orthodeoxia , characterized by massive right-to-left interatrial shunting with transient profound hypoxia and cyanosis .

Example answer:
{"entities": [{"text": "Ebstein 's anomaly", "type": "Disease"}, {"text": "platypnea-orthodeoxia", "type": "Disease"}, {"text": "hypoxia", "type": "Disease"}, {"text": "cyanosis", "type": "Disease"}]}

Example input:
Sentence: PATIENT ( S ) : A 36-year-old woman referred from the infertility clinic for blurred vision .

Example answer:
{"entities": [{"text": "infertility", "type": "Disease"}, {"text": "blurred vision", "type": "Disease"}]}

Example input:
Sentence: Terbutaline , a beta2-adrenoceptor agonist used to arrest preterm labor , has been associated with increased concordance for autism in dizygotic twins .

Example answer:
{"entities": [{"text": "Terbutaline", "type": "Chemical"}, {"text": "preterm labor", "type": "Disease"}, {"text": "autism", "type": "Disease"}]}

Example input:
Sentence: In the singleton pregnancy , the mother had ulcerative colitis , and the infant , a male , had coarctation of the aorta and a ventricular septal defect .

Example answer:
{"entities": [{"text": "ulcerative colitis", "type": "Disease"}, {"text": "coarctation of the aorta", "type": "Disease"}, {"text": "ventricular septal defect", "type": "Disease"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Input:
Sentence: A multiparous woman in good psychological health underwent urgent caesarean section in labour .

## Item bc5cdr:test:1802
Example input:
Sentence: CONCLUSIONS : Direct inhibition of cardiac HCN pacemaker channels contributes to the bradycardic effects of clonidine gene-targeted mice in vivo , and thus , clonidine-like drugs represent novel structures for future HCN channel inhibitors .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}, {"text": "clonidine-like", "type": "Chemical"}]}

Example input:
Sentence: Direct inhibition of cardiac hyperpolarization-activated cyclic nucleotide-gated pacemaker channels by clonidine .

Example answer:
{"entities": [{"text": "cyclic", "type": "Chemical"}, {"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: For each of the three tested calcium channel blockers ( diltiazem , verapamil and bepridil ) 6 groups of mice were treated by two different doses , i.e .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "bepridil", "type": "Chemical"}]}

Example input:
Sentence: The effects of aminophylline on the ventricular fibrillation threshold during normal acid-base conditions and during respiratory failure were studied in anesthetized open chest dogs .

Example answer:
{"entities": [{"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}, {"text": "respiratory failure", "type": "Disease"}]}

Example input:
Sentence: We studied three calcium channel blockers of different structure , nifedipine , diltiazem , and verapamil , along with the new agent .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "nifedipine", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: Using this rationale , the 8-aminoquinoline WR242511 , a potent long-lasting MHb former in rodents and beagle dogs , was studied in the rhesus monkey for advanced development as a potential CN pretreatment .

Example answer:
{"entities": [{"text": "8-aminoquinoline", "type": "Chemical"}, {"text": "WR242511", "type": "Chemical"}]}

Example input:
Sentence: During the infusion of aminophylline , the ventricular fibrillation threshold was reduced by 30 to 40 percent of the control when pH and partial pressures of oxygen ( PO2 ) and carbon dioxide ( CO2 ) were kept within normal limits .

Example answer:
{"entities": [{"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}, {"text": "oxygen", "type": "Chemical"}, {"text": "PO2", "type": "Chemical"}, {"text": "carbon dioxide", "type": "Chemical"}, {"text": "CO2", "type": "Chemical"}]}

Example input:
Sentence: As a consequence of blocking I ( f ) , clonidine reduced the slope of the diastolic depolarization and the frequency of pacemaker potentials in sinoatrial node cells from wild-type and alpha2ABC-knockout mice .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: Clonidine inhibited the native pacemaker current ( I ( f ) ) in isolated sinoatrial node pacemaker cells and the I ( f ) -generating hyperpolarization-activated cyclic nucleotide-gated ( HCN ) 2 and HCN4 channels in transfected HEK293 cells .

Example answer:
{"entities": [{"text": "Clonidine", "type": "Chemical"}, {"text": "cyclic", "type": "Chemical"}]}

Example input:
Sentence: Although the United States Food and Drug Administration banned its use for nocturnal leg cramps due to lack of safety and efficacy , quinine is widely available in beverages including tonic water and bitter lemon .

Example answer:
{"entities": [{"text": "nocturnal leg cramps", "type": "Disease"}, {"text": "quinine", "type": "Chemical"}]}

Input:
Sentence: Quinine is known to block voltage- , calcium- and ATP-sensitive K ( + ) -channels while 4-aminopyridine is known to block voltage-sensitive K ( + ) -channels .

## Item bc5cdr:test:1609
Example input:
Sentence: METHODS : The objective of this study was to determine the feasibility , response rate , and toxicity of a paclitaxel , cisplatin , and gemcitabine combination to treat metastatic NSCLC .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "NSCLC", "type": "Disease"}]}

Example input:
Sentence: Paclitaxel/cisplatin is an effective first-line regimen for locoregionally advanced head and neck cancer and continued study is warranted .

Example answer:
{"entities": [{"text": "Paclitaxel/cisplatin", "type": "Chemical"}, {"text": "head and neck cancer", "type": "Disease"}]}

Example input:
Sentence: From October 1993 to November 1995 , we treated 13 patients with previously chemotherapy-treated metastatic breast cancer by mitoxantrone , 12 mg/m2 , on day 1 and continuous infusion of 5-FU , 3000 mg/m2 , together with leucovorin , 300 mg/m2 , for 48 h from day 1 to 2 .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "mitoxantrone", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "leucovorin", "type": "Chemical"}]}

Example input:
Sentence: Paclitaxel , cisplatin , and gemcitabine combination chemotherapy within a multidisciplinary therapeutic approach in metastatic nonsmall cell lung carcinoma .

Example answer:
{"entities": [{"text": "Paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "nonsmall cell lung carcinoma", "type": "Disease"}]}

Example input:
Sentence: Treatment of previously treated metastatic breast cancer by mitoxantrone and 48-hour continuous infusion of high-dose 5-FU and leucovorin ( MFL ) : low palliative benefit and high treatment-related toxicity .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "mitoxantrone", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "leucovorin", "type": "Chemical"}, {"text": "MFL", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: High-dose 5-fluorouracil/folinic acid infusion therapy has recently become a popular regimen for various cancers .

Example answer:
{"entities": [{"text": "5-fluorouracil/folinic acid", "type": "Chemical"}, {"text": "cancers", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : The combination of paclitaxel , cisplatin , and gemcitabine is well tolerated and shows high activity in metastatic NSCLC .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "NSCLC", "type": "Disease"}]}

Example input:
Sentence: STUDY DESIGN : We combined paclitaxel , melphalan and high-dose cyclophosphamide , thiotepa , and carboplatin in a triple sequential high-dose regimen for patients with metastatic breast cancer .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "melphalan", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "thiotepa", "type": "Chemical"}, {"text": "carboplatin", "type": "Chemical"}, {"text": "breast cancer", "type": "Disease"}]}

Example input:
Sentence: IMPORTANCE OF THE FIELD : Fluoropyrimidines , in particular 5-fluorouracil ( 5-FU ) , have been the mainstay of treatment for several solid tumors , including colorectal , breast and head and neck cancers , for > 40 years .

Example answer:
{"entities": [{"text": "Fluoropyrimidines", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "tumors", "type": "Disease"}]}

Example input:
Sentence: Preliminary results of an Eastern Cooperative Oncology Group study of single-agent paclitaxel ( Taxol ; Bristol-Myers Squibb Company , Princeton , NJ ) reported a 37 % response rate in patients with head and neck cancer , and the paclitaxel/cisplatin combination has been used successfully and has significantly improved median response duration in ovarian cancer patients .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "Taxol", "type": "Chemical"}, {"text": "head and neck cancer", "type": "Disease"}, {"text": "paclitaxel/cisplatin", "type": "Chemical"}, {"text": "ovarian cancer", "type": "Disease"}]}

Input:
Sentence: 5-Fluorouracil plus folinic acid and paclitaxel ( Taxol ; Bristol-Myers Squibb Company , Princeton , NJ ) are effective salvage therapies for metastatic breast cancer patients .

## Item bc5cdr:test:2159
Example input:
Sentence: In males , the non-competitive NMDA antagonist dextromethorphan enhanced the antihyperalgesic effect of low to moderate doses of morphine in a dose-and time-dependent manner .

Example answer:
{"entities": [{"text": "NMDA", "type": "Chemical"}, {"text": "dextromethorphan", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Example input:
Sentence: Inhibition of NO-synthase induced a reversible hypertension accompanied by depressed Na+-extrusion from cardiac cells as a consequence of deteriorated Na+-binding properties of the ( Na , K ) -ATPase .

Example answer:
{"entities": [{"text": "NO-synthase", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "depressed", "type": "Disease"}, {"text": "Na+-extrusion", "type": "Chemical"}, {"text": "Na+-binding", "type": "Chemical"}, {"text": "Na", "type": "Chemical"}, {"text": "K", "type": "Chemical"}]}

Example input:
Sentence: As an alpha-blocker , it also exerts a significant relaxant effect on the bladder neck and urethra .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : The results of this paper confirm that inhibition of bradykinin receptors and inducible NO synthase but not neuronal NO synthase activity reduces diabetic hyperalgesia .

Example answer:
{"entities": [{"text": "bradykinin", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}, {"text": "diabetic hyperalgesia", "type": "Disease"}]}

Example input:
Sentence: In streptozotocin-induced hyperalgesia , inducible NO synthase participates in pronociceptive activity of bradykinin , whereas in vincristine-induced hyperalgesia bradykinin seemed to activate neuronal NO synthase pathway .

Example answer:
{"entities": [{"text": "streptozotocin-induced", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "NO", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}, {"text": "vincristine-induced", "type": "Chemical"}]}

Example input:
Sentence: Endothelial-dependent relaxation and eNOS mRNA expression were greater in the Dex + Ato group than in the Dex only group ( P < 0.05 and P < 0.0001 , respectively ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}, {"text": "Ato", "type": "Chemical"}]}

Example input:
Sentence: Bradykinin receptors antagonists and nitric oxide synthase inhibitors in vincristine and streptozotocin induced hyperalgesia in chemotherapy and diabetic neuropathy rat model .

Example answer:
{"entities": [{"text": "Bradykinin", "type": "Chemical"}, {"text": "nitric oxide", "type": "Chemical"}, {"text": "vincristine", "type": "Chemical"}, {"text": "streptozotocin", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "diabetic neuropathy", "type": "Disease"}]}

Example input:
Sentence: Tamoxifen ( TAM ) , the antiestrogenic drug most widely prescribed in the chemotherapy of breast cancer , induces changes in normal discoid shape of erythrocytes and hemolytic anemia .

Example answer:
{"entities": [{"text": "Tamoxifen", "type": "Chemical"}, {"text": "TAM", "type": "Chemical"}, {"text": "breast cancer", "type": "Disease"}, {"text": "hemolytic anemia", "type": "Disease"}]}

Example input:
Sentence: PURPOSE : The influence of an irreversible inhibitor of constitutive NO synthase ( L-NOArg ; 1.0 mg/kg ip ) , a relatively selective inhibitor of inducible NO synthase ( L-NIL ; 1.0 mg/kg ip ) and a relatively specific inhibitor of neuronal NO synthase ( 7-NI ; 0.1 mg/kg ip ) , on antihyperalgesic action of selective antagonists of B2 and B1 receptors : D-Arg- [ Hyp3 , Thi5 , D-Tic7 , Oic8 ] bradykinin ( HOE 140 ; 70 nmol/kg ip ) or des Arg10 HOE 140 ( 70 nmol/kg ip ) respectively , in model of diabetic ( streptozotocin-induced ) and toxic ( vincristine-induced ) neuropathy was investigated .

Example answer:
{"entities": [{"text": "NO", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}, {"text": "HOE 140", "type": "Chemical"}, {"text": "des Arg10 HOE 140", "type": "Chemical"}]}

Input:
Sentence: However , in vivo and in vitro studies have demonstrated that myometrial cells are also targets of the relaxant effects of nitric oxide ( NO ) .

## Item bc5cdr:test:2555
Example input:
Sentence: All patients received CAB [ leuprolide acetate ( LHRH-A ) 3.75 mg , intramuscularly , every 28 days plus 250 mg flutamide , tid , per Os ] and were evaluated for anemia by physical examination and laboratory tests at baseline and 4 subsequent intervals ( 1 , 2 , 3 and 6 months post-CAB ) .

Example answer:
{"entities": [{"text": "leuprolide acetate", "type": "Chemical"}, {"text": "LHRH-A", "type": "Chemical"}, {"text": "flutamide", "type": "Chemical"}, {"text": "anemia", "type": "Disease"}]}

Example input:
Sentence: Hemoglobin levels also decreased but insignificantly by treatment .

Example answer:
{"entities": []}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: All patients were on a regular transfusion-chelation program maintaining a mean hemoglobin level of 9.5 gr/dl .

Example answer:
{"entities": []}

Example input:
Sentence: At six months post-CAB , patients with severe anemia had a Hb mean value of 10.2 +/- 0.1 g/dl ( X +/- SE ) , whereas the other patients had mild anemia with Hb mean value of 13.2 +/- 0.17 ( X +/- SE ) .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}]}

Example input:
Sentence: The development of severe anemia at 6 months post-CAB was predictable by the reduction of Hb baseline value of more than 2.5 g/dl after 3 months of CAB ( p = 0.01 ) .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}]}

Example input:
Sentence: After 2 weeks of treatment , patients tested 5-8 h after the last dose of medication did not show any decrement of performance .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : We observed a significant decrease in haptoglobin levels at the end of the treatment period .

Example answer:
{"entities": []}

Example input:
Sentence: Two weeks after the initiation of therapy , her hematocrit had decreased from 44.1 % to 20.4 % , and she had a positive direct Coombs antiglobulin test and an elevated indirect bilirubin .

Example answer:
{"entities": [{"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : The mean hemoglobin ( Hb ) levels were significantly declined in all patients from baseline of 14.2 g/dl to 14.0 g/dl , 13.5 g/dl , 13.2 g/dl and 12.7 g/dl at 1 , 2 , 3 and 6 months post-CAB , respectively .

Example answer:
{"entities": []}

Input:
Sentence: Patients who experience a fall in hemoglobin concentrations of 2 g/dL or more at week 2 after the start of treatment should be monitored with particular care .

## Item bc5cdr:test:1988
Example input:
Sentence: We report on two fatal cases of accidental intrathecal vincristine instillation in a 5-year old girl with recurrent acute lymphoblastic leucemia and a 57-year old man with lymphoblastic lymphoma .

Example answer:
{"entities": [{"text": "vincristine", "type": "Chemical"}, {"text": "acute lymphoblastic leucemia", "type": "Disease"}, {"text": "lymphoblastic lymphoma", "type": "Disease"}]}

Example input:
Sentence: A 78-year-old with healed septal necrosis suffered a recurrent myocardial infarction of the anterior wall following the administration of isosorbide dinitrate 5 mg sublingually .

Example answer:
{"entities": [{"text": "necrosis", "type": "Disease"}, {"text": "myocardial infarction", "type": "Disease"}, {"text": "isosorbide dinitrate", "type": "Chemical"}]}

Example input:
Sentence: In the singleton pregnancy , the mother had ulcerative colitis , and the infant , a male , had coarctation of the aorta and a ventricular septal defect .

Example answer:
{"entities": [{"text": "ulcerative colitis", "type": "Disease"}, {"text": "coarctation of the aorta", "type": "Disease"}, {"text": "ventricular septal defect", "type": "Disease"}]}

Example input:
Sentence: One of the twins developed complete heart block and dilated cardiomyopathy related to lopinavir/ritonavir therapy , a boosted protease-inhibitor agent , while the other twin developed mild bradycardia .

Example answer:
{"entities": [{"text": "heart block", "type": "Disease"}, {"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "lopinavir/ritonavir", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Three infants , born of two mothers with inflammatory bowel disease who received treatment with sulphasalazine throughout pregnancy , were found to have major congenital anomalies .

Example answer:
{"entities": [{"text": "inflammatory bowel disease", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "congenital anomalies", "type": "Disease"}]}

Example input:
Sentence: Transient platypnea-orthodeoxia-like syndrome induced by propafenone overdose in a young woman with Ebstein 's anomaly .

Example answer:
{"entities": [{"text": "platypnea-orthodeoxia-like syndrome", "type": "Disease"}, {"text": "propafenone", "type": "Chemical"}, {"text": "overdose", "type": "Disease"}, {"text": "Ebstein 's anomaly", "type": "Disease"}]}

Example input:
Sentence: Nitrofurantoins were associated with anophthalmia or microphthalmos ( AOR = 3.7 ; 95 % CI , 1.1-12.2 ) , hypoplastic left heart syndrome ( AOR = 4.2 ; 95 % CI , 1.9-9.1 ) , atrial septal defects ( AOR = 1.9 ; 95 % CI , 1.1-3.4 ) , and cleft lip with cleft palate ( AOR = 2.1 ; 95 % CI , 1.2-3.9 ) .

Example answer:
{"entities": [{"text": "Nitrofurantoins", "type": "Chemical"}, {"text": "anophthalmia", "type": "Disease"}, {"text": "microphthalmos", "type": "Disease"}, {"text": "hypoplastic left heart syndrome", "type": "Disease"}, {"text": "atrial septal defects", "type": "Disease"}, {"text": "cleft lip", "type": "Disease"}, {"text": "cleft palate", "type": "Disease"}]}

Example input:
Sentence: Simvastatin-induced bilateral leg compartment syndrome and myonecrosis associated with hypothyroidism .

Example answer:
{"entities": [{"text": "Simvastatin-induced", "type": "Chemical"}, {"text": "compartment syndrome", "type": "Disease"}, {"text": "myonecrosis", "type": "Disease"}, {"text": "hypothyroidism", "type": "Disease"}]}

Example input:
Sentence: A 54-year-old hypothyroid male taking thyroxine and simvastatin presented with bilateral leg compartment syndrome and myonecrosis .

Example answer:
{"entities": [{"text": "hypothyroid", "type": "Disease"}, {"text": "thyroxine", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "compartment syndrome", "type": "Disease"}, {"text": "myonecrosis", "type": "Disease"}]}

Example input:
Sentence: In this report we describe the case of a 37-year-old white woman with Ebstein 's anomaly , who developed a rare syndrome called platypnea-orthodeoxia , characterized by massive right-to-left interatrial shunting with transient profound hypoxia and cyanosis .

Example answer:
{"entities": [{"text": "Ebstein 's anomaly", "type": "Disease"}, {"text": "platypnea-orthodeoxia", "type": "Disease"}, {"text": "hypoxia", "type": "Disease"}, {"text": "cyanosis", "type": "Disease"}]}

Input:
Sentence: A case of isotretinoin embryopathy with bilateral anotia and Taussig-Bing malformation .

## Item bc5cdr:test:2401
Example input:
Sentence: The timing of papaverine application and ongoing operative events was reviewed relative to changes in neurophysiological recordings .

Example answer:
{"entities": [{"text": "papaverine", "type": "Chemical"}]}

Example input:
Sentence: In the present study , we investigated the changes occurring at the protein level in striatal samples obtained from the unilaterally 6-hydroxydopamine-lesion rat model of PD treated with saline , L-DOPA or bromocriptine using two-dimensional difference gel electrophoresis and mass spectrometry ( MS ) .

Example answer:
{"entities": [{"text": "6-hydroxydopamine-lesion", "type": "Chemical"}, {"text": "PD", "type": "Disease"}, {"text": "L-DOPA", "type": "Chemical"}, {"text": "bromocriptine", "type": "Chemical"}]}

Example input:
Sentence: After starting PGE1 or TMP , MAP and rate pressure product ( RPP ) decreased significantly compared with preinfusion values ( P < 0.01 ) , and the degree of hypotension due to PGE1 remained constant until 60 min after its discontinuation .

Example answer:
{"entities": [{"text": "PGE1", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Compared with control patients , CRF and ESRD patients had higher preoperative serum creatinine levels , a greater percentage of patients with hepatorenal syndrome , higher percentage requirement for dialysis in the first 3 months postoperatively , and a higher 1-year serum creatinine .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "hepatorenal syndrome", "type": "Disease"}]}

Example input:
Sentence: Preoperative assessment should focus on cardiovascular status and serum potassium level .

Example answer:
{"entities": [{"text": "potassium", "type": "Chemical"}]}

Example input:
Sentence: Similarly , in patient diaries , although both treatments caused reduction in subjective dyskinesia scores during the days of intervention , the effect was sustained for 3 days after the intervention for the real rTMS only .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Significant declines in simple and sustained attention , working memory , and verbal memory were observed at 1 hour postdose compared to baseline for both age groups with a trend toward return to baseline by 5 hours postdose .

Example answer:
{"entities": []}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: Twenty-three h postoperatively he developed a brief self-limited seizure .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : The United Kingdom Parkinson 's Disease Research Group ( UKPDRG ) trial found an increased mortality in patients with Parkinson 's disease ( PD ) randomized to receive 10 mg selegiline per day and L-dopa compared with those taking L-dopa alone .

Example answer:
{"entities": [{"text": "Parkinson 's Disease", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "selegiline", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}]}

Input:
Sentence: Preoperative and postoperative assessments of these patients at 1 , 3 , 6 and 12 months follow-up , in `` on '' and `` off '' drug conditions , was carried out using Unified Parkinson 's Disease Rating Scale , Hoehn and Yahr staging , England activities of daily living score and video recordings .

## Item bc5cdr:test:2461
Example input:
Sentence: In the current study the efficacy and toxicity of the combination of GEM and VNB in elderly patients with advanced NSCLC or those with some contraindication to receiving cisplatin were assessed .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "GEM", "type": "Chemical"}, {"text": "VNB", "type": "Chemical"}, {"text": "NSCLC", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: It has shown promising results alone or in combination with other chemotherapeutic agents in colorectal , breast , pancreaticobiliary , gastric , renal cell and head and neck cancers .

Example answer:
{"entities": []}

Example input:
Sentence: This apparent difference in risk may not be due to differences in nephrotoxic potential of the drugs themselves .

Example answer:
{"entities": [{"text": "nephrotoxic", "type": "Disease"}]}

Example input:
Sentence: RESULTS : During a mean follow-up of 3.3 years , raloxifene was associated with an increased risk for venous thromboembolism ( relative risk [ RR ] 2.1 ; 95 % confidence interval [ CI ] 1.2-3.8 ) .

Example answer:
{"entities": [{"text": "raloxifene", "type": "Chemical"}, {"text": "venous thromboembolism", "type": "Disease"}]}

Example input:
Sentence: Given its excellent tolerance profile and low toxicity , further evaluation of VNB in combination therapy is warranted .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "VNB", "type": "Chemical"}]}

Example input:
Sentence: Recent reports indicate that single agent therapy with vinorelbine ( VNB ) or gemcitabine ( GEM ) may obtain a response rate of 20-30 % in elderly patients , with acceptable toxicity and improvement in symptoms and quality of life .

Example answer:
{"entities": [{"text": "vinorelbine", "type": "Chemical"}, {"text": "VNB", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "GEM", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: VNB was well tolerated and zero instances of WHO grade 4 nonhematologic toxicity occurred .

Example answer:
{"entities": [{"text": "VNB", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : These data indicate that VNB is an active agent in metastatic esophageal squamous cell carcinoma .

Example answer:
{"entities": [{"text": "VNB", "type": "Chemical"}, {"text": "esophageal squamous cell carcinoma", "type": "Disease"}]}

Example input:
Sentence: We conclude that second and third generation agents are associated with equivalent risks of VTE when the same agent is used repeatedly after interruption periods or when users are switched between the two generations of pills .

Example answer:
{"entities": [{"text": "VTE", "type": "Disease"}]}

Example input:
Sentence: A lower relative risk would be expected for acetaminophen if the risk of both drugs in combination with other analgesics was higher than the risk of either agent alone .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}]}

Input:
Sentence: However , the risk associated with VNR seems to be similar to that of other chemotherapeutic agents in the same indications .

## Item bc5cdr:test:2164
Example input:
Sentence: METHODS : Seventeen subjects who were genotyped as CYP2D6 extensive metabolizers were enrolled in this randomized , open-label , crossover study to receive a single oral dose of desipramine ( 50 mg ) on two separate occasions , once alone and once after multiple doses of cinacalcet ( 90 mg for 7 days ) .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}]}

Example input:
Sentence: An initial dose of 0.1 microgram.kg-1.min-1 of PGE1 ( 15 patients ) , or 10 micrograms.kg-1.min-1 of TMP ( 15 patients ) was administered intravenously after the dural opening and the dose was adjusted to maintain the mean arterial blood pressure ( MAP ) at about 60 mmHg .

Example answer:
{"entities": [{"text": "PGE1", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}]}

Example input:
Sentence: Treatment was comprised of VNB , 25 mg/m ( 2 ) , plus GEM , 1000 mg/m ( 2 ) , both on Days 1 , 8 , and 15 every 28 days .

Example answer:
{"entities": [{"text": "VNB", "type": "Chemical"}, {"text": "GEM", "type": "Chemical"}]}

Example input:
Sentence: Thirty-five consecutive chemotherapy-naive patients with Stage IV NSCLC and an Eastern Cooperative Oncology Group performance status of 0-2 were treated with a combination of paclitaxel ( 135 mg/m ( 2 ) given intravenously in 3 hours ) on Day 1 , cisplatin ( 120 mg/m ( 2 ) given intravenously in 6 hours ) on Day 1 , and gemcitabine ( 800 mg/m ( 2 ) given intravenously in 30 minutes ) on Days 1 and 8 , every 4 weeks .

Example answer:
{"entities": [{"text": "NSCLC", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}]}

Example input:
Sentence: In the present study , cis-platin ( 80-120 mg/m2BSA ) and 5-FU ( 1000 mg/m2BSA daily as a continuous infusion during 5 days ) were given to 76 patients before radiotherapy and surgery .

Example answer:
{"entities": [{"text": "cis-platin", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}]}

Example input:
Sentence: Forty-three ovarian cancer patients were available for analysis following six cycles of the same PAC-containing regimen : 23 had been supplemented by glutamate all along the treatment period , at a daily dose of three times 500 mg ( group G ) , and 20 had received a placebo ( group P ) .

Example answer:
{"entities": [{"text": "ovarian cancer", "type": "Disease"}, {"text": "PAC-containing", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: With paclitaxel doses of 200 mg/m2 and higher , granulocyte colony-stimulating factor 5 micrograms/kg/d is given ( days 4 through 12 ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}]}

Example input:
Sentence: Subjects were receiving desferrioxamine ( DFO ) chelation treatment with a mean daily dose of 50-60 mg/kg , 5-6 days a week during the first six years of the study , which was then reduced to 40-50 mg/kg for the following eight years .

Example answer:
{"entities": [{"text": "desferrioxamine", "type": "Chemical"}, {"text": "DFO", "type": "Chemical"}]}

Example input:
Sentence: INTERVENTION : Each patient received either intravenous docetaxel 30 mg/m2/week for 3 consecutive weeks , followed by 1 week off , or the combination of continuous oral thalidomide 200 mg every evening plus the same docetaxel regimen .

Example answer:
{"entities": [{"text": "docetaxel", "type": "Chemical"}, {"text": "thalidomide", "type": "Chemical"}]}

Example input:
Sentence: Treatment , given every 21 days for a maximum of three cycles , consisted of paclitaxel by 3-hour infusion followed the next day by a fixed dose of cisplatin ( 75 mg/m2 ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Input:
Sentence: Patients received up to 3 doses/day of 50 mg DCF or 2.5 mg/24 h transdermal GTN for the first 3 days of the cycle , according to their needs .

## Item bc5cdr:test:2336
Example input:
Sentence: Preliminary results of an Eastern Cooperative Oncology Group study of single-agent paclitaxel ( Taxol ; Bristol-Myers Squibb Company , Princeton , NJ ) reported a 37 % response rate in patients with head and neck cancer , and the paclitaxel/cisplatin combination has been used successfully and has significantly improved median response duration in ovarian cancer patients .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "Taxol", "type": "Chemical"}, {"text": "head and neck cancer", "type": "Disease"}, {"text": "paclitaxel/cisplatin", "type": "Chemical"}, {"text": "ovarian cancer", "type": "Disease"}]}

Example input:
Sentence: Forty-three ovarian cancer patients were available for analysis following six cycles of the same PAC-containing regimen : 23 had been supplemented by glutamate all along the treatment period , at a daily dose of three times 500 mg ( group G ) , and 20 had received a placebo ( group P ) .

Example answer:
{"entities": [{"text": "ovarian cancer", "type": "Disease"}, {"text": "PAC-containing", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: PATIENTS : Seventy men , aged 50-80 years , with advanced androgen-independent prostate cancer .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "Disease"}]}

Example input:
Sentence: Thalidomide has limited single-agent activity in relapsed or refractory indolent non-Hodgkin lymphomas : a phase II trial of the Cancer and Leukemia Group B. Thalidomide is an immunomodulatory agent with demonstrated activity in multiple myeloma , mantle cell lymphoma and lymphoplasmacytic lymphoma .

Example answer:
{"entities": [{"text": "Thalidomide", "type": "Chemical"}, {"text": "non-Hodgkin lymphomas", "type": "Disease"}, {"text": "Cancer", "type": "Disease"}, {"text": "Leukemia", "type": "Disease"}, {"text": "multiple myeloma", "type": "Disease"}, {"text": "mantle cell lymphoma", "type": "Disease"}, {"text": "lymphoplasmacytic lymphoma", "type": "Disease"}]}

Example input:
Sentence: The men were randomly assigned to bupropion SR ( 150 mg twice daily , 117 ) or placebo ( twice daily , 117 ) for 12 weeks .

Example answer:
{"entities": [{"text": "bupropion", "type": "Chemical"}]}

Example input:
Sentence: INTERVENTION : Each patient received either intravenous docetaxel 30 mg/m2/week for 3 consecutive weeks , followed by 1 week off , or the combination of continuous oral thalidomide 200 mg every evening plus the same docetaxel regimen .

Example answer:
{"entities": [{"text": "docetaxel", "type": "Chemical"}, {"text": "thalidomide", "type": "Chemical"}]}

Example input:
Sentence: STUDY OBJECTIVE : To evaluate the frequency of venous thromboembolism ( VTE ) in patients with advanced androgen-independent prostate cancer who were treated with docetaxel alone or in combination with thalidomide .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "VTE", "type": "Disease"}, {"text": "prostate cancer", "type": "Disease"}, {"text": "docetaxel", "type": "Chemical"}, {"text": "thalidomide", "type": "Chemical"}]}

Example input:
Sentence: Increased frequency of venous thromboembolism with the combination of docetaxel and thalidomide in patients with metastatic androgen-independent prostate cancer .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "docetaxel", "type": "Chemical"}, {"text": "thalidomide", "type": "Chemical"}, {"text": "prostate cancer", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : The addition of thalidomide to docetaxel in the treatment of prostate cancer significantly increases the frequency of VTE .

Example answer:
{"entities": [{"text": "thalidomide", "type": "Chemical"}, {"text": "docetaxel", "type": "Chemical"}, {"text": "prostate cancer", "type": "Disease"}, {"text": "VTE", "type": "Disease"}]}

Example input:
Sentence: Between July 2001 and April 2004 , 24 patients with relapsed/refractory indolent lymphomas received thalidomide 200 mg daily with escalation by 100 mg daily every 1-2 weeks as tolerated , up to a maximum of 800 mg daily .

Example answer:
{"entities": [{"text": "lymphomas", "type": "Disease"}, {"text": "thalidomide", "type": "Chemical"}]}

Input:
Sentence: We undertook an open-label study using thalidomide 100 mg once daily for up to 6 months in 20 men with androgen-independent prostate cancer .

## Item bc5cdr:test:2254
Example input:
Sentence: Clinical and experimental data published to date suggest several possible mechanisms by which cocaine may result in acute myocardial infarction .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : Cocaine use predisposed aneurysmal rupture at a significantly earlier age and in much smaller aneurysms .

Example answer:
{"entities": [{"text": "Cocaine", "type": "Chemical"}, {"text": "aneurysmal rupture", "type": "Disease"}, {"text": "aneurysms", "type": "Disease"}]}

Example input:
Sentence: In individuals with preexisting , high-grade coronary arterial narrowing , acute myocardial infarction may result from an increase in myocardial oxygen demand associated with cocaine-induced increase in rate-pressure product .

Example answer:
{"entities": [{"text": "acute myocardial infarction", "type": "Disease"}, {"text": "oxygen", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}]}

Example input:
Sentence: A 45-year-old man , an admitted frequent cocaine user , presented to the Emergency Department ( ED ) on two separate occasions with a history of priapism after cocaine use .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "priapism", "type": "Disease"}]}

Example input:
Sentence: Stroke followed cocaine use by inhalation , intranasal , intravenous , and intramuscular routes .

Example answer:
{"entities": [{"text": "Stroke", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVE : The outcome of subarachnoid hemorrhage associated with cocaine abuse is reportedly poor .

Example answer:
{"entities": [{"text": "subarachnoid hemorrhage", "type": "Disease"}, {"text": "cocaine abuse", "type": "Disease"}]}

Example input:
Sentence: METHODS : A review of admissions during a 6-year period revealed 14 patients with cocaine-related aneurysms .

Example answer:
{"entities": [{"text": "cocaine-related", "type": "Chemical"}, {"text": "aneurysms", "type": "Disease"}]}

Example input:
Sentence: Intracranial aneurysms and cocaine abuse : analysis of prognostic indicators .

Example answer:
{"entities": [{"text": "Intracranial aneurysms", "type": "Disease"}, {"text": "cocaine abuse", "type": "Disease"}]}

Example input:
Sentence: Eleven of the cocaine abusers and none of the controls had ECG evidence of significant myocardial injury defined as myocardial infarction , ischemia , and bundle branch block .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "myocardial injury", "type": "Disease"}, {"text": "myocardial infarction", "type": "Disease"}, {"text": "ischemia", "type": "Disease"}, {"text": "bundle branch block", "type": "Disease"}]}

Example input:
Sentence: Electrocardiographic evidence of myocardial injury in psychiatrically hospitalized cocaine abusers .

Example answer:
{"entities": [{"text": "myocardial injury", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Input:
Sentence: METHODS : Outcomes were examined in patients admitted for possible MI after cocaine use .

## Item bc5cdr:test:2325
Example input:
Sentence: Based on a score of 8 on the Naranjo adverse drug reaction probability scale , telithromycin was the probable cause of acute hepatitis in this patient , and pathological findings suggested drug-induced toxic hepatitis .

Example answer:
{"entities": [{"text": "adverse drug reaction", "type": "Disease"}, {"text": "telithromycin", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}, {"text": "toxic hepatitis", "type": "Disease"}]}

Example input:
Sentence: METHODS : We present the first case report of a woman with hyperthyroidism treated with propylthiouracil in whom a syndrome of pericarditis , fever , and glomerulonephritis developed .

Example answer:
{"entities": [{"text": "hyperthyroidism", "type": "Disease"}, {"text": "propylthiouracil", "type": "Chemical"}, {"text": "pericarditis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "glomerulonephritis", "type": "Disease"}]}

Example input:
Sentence: Simvastatinezetimibe and escitalopram ( which she was taking for depression ) were discontinued , and other potential causes of hepatotoxicity were excluded .

Example answer:
{"entities": [{"text": "Simvastatinezetimibe", "type": "Chemical"}, {"text": "escitalopram", "type": "Chemical"}, {"text": "depression", "type": "Disease"}, {"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: We have reported a case of acute oliguric renal failure with hyperkalemia in a patient with cirrhosis , ascites , and cor pulmonale after indomethacin therapy .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "cor pulmonale", "type": "Disease"}, {"text": "indomethacin", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : Raloxifene was associated with an increased risk for venous thromboembolism , but there was no increased risk for cataracts , gallbladder disease , endometrial hyperplasia , or endometrial cancer .

Example answer:
{"entities": [{"text": "Raloxifene", "type": "Chemical"}, {"text": "venous thromboembolism", "type": "Disease"}, {"text": "cataracts", "type": "Disease"}, {"text": "gallbladder disease", "type": "Disease"}, {"text": "endometrial hyperplasia", "type": "Disease"}, {"text": "endometrial cancer", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : We suggest that the increased risk of venous thromboembolism due to raloxifene treatment may be related to increased tPA levels , but not TAFI levels .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "raloxifene", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : Here we report a case of acute hepatitis probably associated with the administration of telithromycin .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}, {"text": "telithromycin", "type": "Chemical"}]}

Example input:
Sentence: Prompt restoration of renal function followed drug withdrawal , while re-exposure to a single dose of indomethacin caused recurrence of acute reversible oliguria .

Example answer:
{"entities": [{"text": "indomethacin", "type": "Chemical"}, {"text": "oliguria", "type": "Disease"}]}

Example input:
Sentence: Indomethacin-induced renal insufficiency : recurrence on rechallenge .

Example answer:
{"entities": [{"text": "Indomethacin-induced", "type": "Chemical"}, {"text": "renal insufficiency", "type": "Disease"}]}

Example input:
Sentence: Hyperkalemia has recently been recognized as a complication of nonsteroidal antiinflammatory agents ( NSAID ) such as indomethacin .

Example answer:
{"entities": [{"text": "Hyperkalemia", "type": "Disease"}, {"text": "indomethacin", "type": "Chemical"}]}

Input:
Sentence: In addition to tiaprofenic acid , indomethacin has been reported to be associated with this condition .

## Item bc5cdr:test:2402
Example input:
Sentence: While she was weak , 2-Hz repetitive stimulation revealed a decrement without significant facilitation at rapid rates or after exercise , suggesting postsynaptic neuromuscular blockade .

Example answer:
{"entities": [{"text": "postsynaptic neuromuscular blockade", "type": "Disease"}]}

Example input:
Sentence: Repetitive transcranial magnetic stimulation for levodopa-induced dyskinesias in Parkinson 's disease .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: In SE survivors , similar stimulation resulted in a population spike followed , at a variable latency , by negative DC shifts and repetitive afterdischarges of 3-60 s duration , which were blocked by ionotropic glutamate receptor antagonists .

Example answer:
{"entities": [{"text": "SE", "type": "Disease"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: The results suggest the existence of residual beneficial clinical aftereffects of consecutive daily applications of low-frequency rTMS on dyskinesias in PD .

Example answer:
{"entities": [{"text": "dyskinesias", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: RESULTS : After 12 weeks of treatment , the mean ( sd ) scores for CGI-SF were significantly lower , i.e .

Example answer:
{"entities": []}

Example input:
Sentence: Similarly , in patient diaries , although both treatments caused reduction in subjective dyskinesia scores during the days of intervention , the effect was sustained for 3 days after the intervention for the real rTMS only .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : The United Kingdom Parkinson 's Disease Research Group ( UKPDRG ) trial found an increased mortality in patients with Parkinson 's disease ( PD ) randomized to receive 10 mg selegiline per day and L-dopa compared with those taking L-dopa alone .

Example answer:
{"entities": [{"text": "Parkinson 's Disease", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "selegiline", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}]}

Example input:
Sentence: There was a significant 40 % improvement in the dyskinesia score without increase of parkinsonian motor disability .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}, {"text": "parkinsonian", "type": "Disease"}, {"text": "motor disability", "type": "Disease"}]}

Example input:
Sentence: In a placebo-controlled , single-blinded , crossover study , we assessed the effect of `` real '' repetitive transcranial magnetic stimulation ( rTMS ) versus `` sham '' rTMS ( placebo ) on peak dose dyskinesias in patients with Parkinson 's disease ( PD ) .

Example answer:
{"entities": [{"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: Ten patients with PD and prominent dyskinesias had rTMS ( 1,800 pulses ; 1 Hz rate ) delivered over the motor cortex for 4 consecutive days twice , once real stimuli and once sham stimulation were used ; evaluations were done at the baseline and 1 day after the end of each of the treatment series .

Example answer:
{"entities": [{"text": "PD", "type": "Disease"}, {"text": "dyskinesias", "type": "Disease"}]}

Input:
Sentence: RESULTS : After one year of electrical stimulation of the STN , the patients ' scores for activities of daily living and motor examination scores ( Unified Parkinson 's Disease Rating Scale parts II and III ) off medication improved by 62 % and 61 % respectively ( p < 0.0005 ) .

## Item bc5cdr:test:2147
Example input:
Sentence: Triazolam-induced brief episodes of secondary mania in a depressed patient .

Example answer:
{"entities": [{"text": "Triazolam-induced", "type": "Chemical"}, {"text": "mania", "type": "Disease"}, {"text": "depressed", "type": "Disease"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: RESULTS : A 20-year-old male with schizophrenia developed a sudden onset of myocarditis after commencement of clozapine .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "Disease"}, {"text": "myocarditis", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}]}

Example input:
Sentence: Patients who experienced a manic or hypomanic switch were compared with those who did not on several variables including age , sex , diagnosis ( DSM-IV bipolar I vs. bipolar II ) , number of previous manic episodes , type of antidepressant therapy used ( electroconvulsive therapy vs. antidepressant drugs and , more particularly , selective serotonin reuptake inhibitors [ SSRIs ] ) , use and type of mood stabilizers ( lithium vs. anticonvulsants ) , and temperament of the patient , assessed during a normothymic period using the hyperthymia component of the Semi-structured Affective Temperament Interview .

Example answer:
{"entities": [{"text": "manic", "type": "Disease"}, {"text": "hypomanic", "type": "Disease"}, {"text": "DSM-IV bipolar I", "type": "Disease"}, {"text": "bipolar II", "type": "Disease"}, {"text": "antidepressant", "type": "Chemical"}, {"text": "serotonin reuptake inhibitors", "type": "Chemical"}, {"text": "SSRIs", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: In six of the probable cases the neurological disturbance consisted of an acute reversible encephalopathy usually related to the ingestion of a high dose of clioquinol over a short period .

Example answer:
{"entities": [{"text": "neurological disturbance", "type": "Disease"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "clioquinol", "type": "Chemical"}]}

Example input:
Sentence: Fewer subjects reported adverse events following treatment with desipramine alone than when receiving desipramine with cinacalcet ( 33 versus 86 % ) , the most frequent of which ( nausea and headache ) have been reported for patients treated with either desipramine or cinacalcet .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}, {"text": "nausea", "type": "Disease"}, {"text": "headache", "type": "Disease"}]}

Example input:
Sentence: Large doses of triazolam repeatedly induced brief episodes of mania in a depressed elderly woman .

Example answer:
{"entities": [{"text": "triazolam", "type": "Chemical"}, {"text": "mania", "type": "Disease"}, {"text": "depressed", "type": "Disease"}]}

Example input:
Sentence: FINDINGS : FS containing tAMCA caused paroxysmal brain activity which was associated with distinct convulsive behaviours .

Example answer:
{"entities": [{"text": "tAMCA", "type": "Chemical"}, {"text": "convulsive", "type": "Disease"}]}

Example input:
Sentence: Antidepressant-induced mania in bipolar patients : identification of risk factors .

Example answer:
{"entities": [{"text": "Antidepressant-induced", "type": "Chemical"}, {"text": "mania", "type": "Disease"}, {"text": "bipolar", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Switches to hypomania or mania occurred in 27 % of all patients ( N = 12 ) ( and in 24 % of the subgroup of patients treated with SSRIs [ 8/33 ] ) ; 16 % ( N = 7 ) experienced manic episodes , and 11 % ( N = 5 ) experienced hypomanic episodes .

Example answer:
{"entities": [{"text": "hypomania", "type": "Disease"}, {"text": "mania", "type": "Disease"}, {"text": "SSRIs", "type": "Chemical"}, {"text": "manic", "type": "Disease"}, {"text": "hypomanic", "type": "Disease"}]}

Input:
Sentence: Cases reported by the FDA showed clarithromycin and ciprofloxacin to be the most frequently associated with the development of mania .

## Item bc5cdr:test:2063
Example input:
Sentence: Angina and ischemic electrocardiographic changes occurred after administration of oral dipyridamole in four patients awaiting urgent myocardial revascularization procedures .

Example answer:
{"entities": [{"text": "Angina", "type": "Disease"}, {"text": "dipyridamole", "type": "Chemical"}]}

Example input:
Sentence: Effects of long-term pretreatment with isoproterenol on bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: We report a woman with coronary artery disease who developed a markedly prolonged QT interval and torsades de pointes ( TdP ) after taking ketoconazole for treatment of fungal infection .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "prolonged QT interval", "type": "Disease"}, {"text": "torsades de pointes", "type": "Disease"}, {"text": "TdP", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "fungal infection", "type": "Disease"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: As a consequence of blocking I ( f ) , clonidine reduced the slope of the diastolic depolarization and the frequency of pacemaker potentials in sinoatrial node cells from wild-type and alpha2ABC-knockout mice .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: We postulate that by virtue of its direct blocking action on IKr , ketoconazole alone may prolong QT interval and induce TdP .

Example answer:
{"entities": [{"text": "ketoconazole", "type": "Chemical"}, {"text": "TdP", "type": "Disease"}]}

Example input:
Sentence: Therefore , we studied the hyperemic response to dipyridamole in seven open-chest anesthetized dogs after pretreatment with either pentoxifylline ( 0 , 7.5 , or 15 mg/kg i.v . )

Example answer:
{"entities": [{"text": "dipyridamole", "type": "Chemical"}, {"text": "pentoxifylline", "type": "Chemical"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: UM-272 ( N , N-dimethylpropranolol ) , a quaternary antiarrhythmic agent , was administered sublingually to dogs with ouabain-induced ventricular tachycardias .

Example answer:
{"entities": [{"text": "UM-272", "type": "Chemical"}, {"text": "N , N-dimethylpropranolol", "type": "Chemical"}, {"text": "ouabain-induced", "type": "Chemical"}, {"text": "ventricular tachycardias", "type": "Disease"}]}

Example input:
Sentence: Four compounds known to increase QT interval and cause TDP were investigated : terfenadine , terodiline , cisapride and E4031 .

Example answer:
{"entities": [{"text": "TDP", "type": "Disease"}, {"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}, {"text": "E4031", "type": "Chemical"}]}

Input:
Sentence: Although both dl-sotalol and azimilide rarely induced EADs in canine left ventricles , they produced frequent EADs in rabbits , in which more pronounced QT prolongation was seen .

## Item bc5cdr:test:2114
Example input:
Sentence: Moreover , systemic lipopolysaccharide pretreatment ( 1 mg/kg ) attenuated local methamphetamine infusion-produced dopamine and 3,4-dihydroxyphenylacetic acid depletions in the striatum , indicating that the protective effect of lipopolysaccharide is less likely due to interrupted peripheral distribution or metabolism of methamphetamine .

Example answer:
{"entities": [{"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "3,4-dihydroxyphenylacetic acid", "type": "Chemical"}]}

Example input:
Sentence: Alpha-lipoic acid exerts neuroprotective effects against chemotherapy induced neurotoxicity in sensory neurons : it rescues the mitochondrial toxicity and induces the expression of frataxin , an essential mitochondrial protein with anti-oxidant and chaperone properties .

Example answer:
{"entities": [{"text": "Alpha-lipoic acid", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "mitochondrial toxicity", "type": "Disease"}]}

Example input:
Sentence: L-NAME reduced gentamicin-induced hearing loss in the high-frequency range , but gave no protection in the middle or low frequencies .

Example answer:
{"entities": [{"text": "L-NAME", "type": "Chemical"}, {"text": "gentamicin-induced", "type": "Chemical"}, {"text": "hearing loss", "type": "Disease"}]}

Example input:
Sentence: Alpha-lipoic acid protects sensory neurons through its anti-oxidant and mitochondrial regulatory functions , possibly inducing the expression of frataxin .

Example answer:
{"entities": [{"text": "Alpha-lipoic acid", "type": "Chemical"}]}

Example input:
Sentence: Following recovery , the monkeys were selectively deafened for high frequencies using kanamycin and furosemide .

Example answer:
{"entities": [{"text": "kanamycin", "type": "Chemical"}, {"text": "furosemide", "type": "Chemical"}]}

Example input:
Sentence: Nitro-L-arginine methyl ester : a potential protector against gentamicin ototoxicity .

Example answer:
{"entities": [{"text": "Nitro-L-arginine methyl ester", "type": "Chemical"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "ototoxicity", "type": "Disease"}]}

Example input:
Sentence: Gentamicin sulfate and tobramycin sulfate continue to demonstrate ototoxicity and nephrotoxicity in both animal and clinical studies .

Example answer:
{"entities": [{"text": "Gentamicin sulfate", "type": "Chemical"}, {"text": "tobramycin sulfate", "type": "Chemical"}, {"text": "ototoxicity", "type": "Disease"}, {"text": "nephrotoxicity", "type": "Disease"}]}

Example input:
Sentence: The nitric oxide ( NO ) inhibitor nitro-L-arginine methyl ester ( L-NAME ) may act as an otoprotectant against high-frequency hearing loss caused by gentamicin , but further studies are needed to confirm this.Aminoglycoside antibiotics are still widely used by virtue of their efficacy and low cost .

Example answer:
{"entities": [{"text": "nitric oxide", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}, {"text": "nitro-L-arginine methyl ester", "type": "Chemical"}, {"text": "L-NAME", "type": "Chemical"}, {"text": "high-frequency hearing loss", "type": "Disease"}, {"text": "gentamicin", "type": "Chemical"}]}

Example input:
Sentence: Ototoxicity appeared closely related to a prolonged administration and higher total dose of ototoxic drugs , particularly aminoglycosides and furosemide .

Example answer:
{"entities": [{"text": "Ototoxicity", "type": "Disease"}, {"text": "ototoxic", "type": "Disease"}, {"text": "aminoglycosides", "type": "Chemical"}, {"text": "furosemide", "type": "Chemical"}]}

Example input:
Sentence: Their ototoxicity is a serious health problem and , as their ototoxic mechanism involves the production of NO , we need to assess the use of NO inhibitors for the prevention of aminoglycoside-induced sensorineural hearing loss .

Example answer:
{"entities": [{"text": "ototoxicity", "type": "Disease"}, {"text": "ototoxic", "type": "Disease"}, {"text": "NO", "type": "Chemical"}, {"text": "aminoglycoside-induced", "type": "Chemical"}, {"text": "sensorineural hearing loss", "type": "Disease"}]}

Input:
Sentence: The protection by overexpression of superoxide dismutase supports the hypothesis that oxidant stress plays a significant role in aminoglycoside-induced ototoxicity .

## Item bc5cdr:test:2349
Example input:
Sentence: Fatal myeloencephalopathy due to accidental intrathecal vincristin administration : a report of two cases .

Example answer:
{"entities": [{"text": "myeloencephalopathy", "type": "Disease"}, {"text": "vincristin", "type": "Chemical"}]}

Example input:
Sentence: One of the twins developed complete heart block and dilated cardiomyopathy related to lopinavir/ritonavir therapy , a boosted protease-inhibitor agent , while the other twin developed mild bradycardia .

Example answer:
{"entities": [{"text": "heart block", "type": "Disease"}, {"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "lopinavir/ritonavir", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Intravenous administration of a single 50-mg bolus of lidocaine in a 67-year-old man resulted in profound depression of the activity of the sinoatrial and atrioventricular nodal pacemakers .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: We describe a case of transient neurological deficit that occurred after unilateral spinal anaesthesia with 8 mg of 1 % hyperbaric bupivacaine slowly injected through a 25-gauge pencil-point spinal needle .

Example answer:
{"entities": [{"text": "neurological deficit", "type": "Disease"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: However , tAMCA has been shown to cause epileptic seizures .

Example answer:
{"entities": [{"text": "tAMCA", "type": "Chemical"}, {"text": "epileptic seizures", "type": "Disease"}]}

Example input:
Sentence: Long-term intragastric application of the antiepileptic drug sodium valproate ( Vupral `` Polfa '' ) at the effective dose of 200 mg/kg b. w. once daily to rats for 1 , 3 , 6 , 9 and 12 months revealed neurological disorders indicating cerebellum damage ( `` valproate encephalopathy '' ) .

Example answer:
{"entities": [{"text": "sodium valproate", "type": "Chemical"}, {"text": "neurological disorders", "type": "Disease"}, {"text": "cerebellum damage", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: We describe a 25-year-old woman with pre-existing mitral valve prolapse who developed intractable ventricular fibrillation after consuming a `` natural energy '' guarana health drink containing a high concentration of caffeine .

Example answer:
{"entities": [{"text": "mitral valve prolapse", "type": "Disease"}, {"text": "ventricular fibrillation", "type": "Disease"}, {"text": "caffeine", "type": "Chemical"}]}

Example input:
Sentence: Serial epilepsy caused by levodopa/carbidopa administration in two patients on hemodialysis .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "levodopa/carbidopa", "type": "Chemical"}]}

Example input:
Sentence: We report on two fatal cases of accidental intrathecal vincristine instillation in a 5-year old girl with recurrent acute lymphoblastic leucemia and a 57-year old man with lymphoblastic lymphoma .

Example answer:
{"entities": [{"text": "vincristine", "type": "Chemical"}, {"text": "acute lymphoblastic leucemia", "type": "Disease"}, {"text": "lymphoblastic lymphoma", "type": "Disease"}]}

Example input:
Sentence: FINDINGS : A 28-year-old man suffering from idiopathic epilepsy with generalized seizures was treated with LEV ( 3000 mg ) added to valproate ( VPA ) ( 2000 mg ) .

Example answer:
{"entities": [{"text": "idiopathic epilepsy", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "LEV", "type": "Chemical"}, {"text": "valproate", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}]}

Input:
Sentence: We describe 2 cases of grand mal seizures following accidental intravascular injection of levobupivacaine .

## Item bc5cdr:test:1779
Example input:
Sentence: Torsades de pointes ( TDP ) is a potentially fatal ventricular tachycardia associated with increases in QT interval and monophasic action potential duration ( MAPD ) .

Example answer:
{"entities": [{"text": "Torsades de pointes", "type": "Disease"}, {"text": "TDP", "type": "Disease"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: Cardiomyopathy is frequent when the total dose exceeds 600 mg/m2 and occurs within one to six months after cessation of therapy .

Example answer:
{"entities": [{"text": "Cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: Four compounds known to increase QT interval and cause TDP were investigated : terfenadine , terodiline , cisapride and E4031 .

Example answer:
{"entities": [{"text": "TDP", "type": "Disease"}, {"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}, {"text": "E4031", "type": "Chemical"}]}

Example input:
Sentence: A patient is reported who developed progressive cardiomyopathy two and one-half years after receiving 580 mg/m2 which apparently represents late , late cardiotoxicity .

Example answer:
{"entities": [{"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: Dobutamine stress echocardiography : a sensitive indicator of diminished myocardial function in asymptomatic doxorubicin-treated long-term survivors of childhood cancer .

Example answer:
{"entities": [{"text": "Dobutamine", "type": "Chemical"}, {"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Electrocardiography has a very low sensitivity in detecting dobutamine-induced myocardial ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}]}

Example input:
Sentence: Dobutamine infusion at 10 micrograms/kg per min was discontinued after six studies secondary to a 50 % incidence rate of adverse symptoms .

Example answer:
{"entities": [{"text": "Dobutamine", "type": "Chemical"}]}

Example input:
Sentence: These seven cases demonstrate that procainamide can produce an acquired prolonged Q-T syndrome with polymorphous ventricular tachycardia .

Example answer:
{"entities": [{"text": "procainamide", "type": "Chemical"}, {"text": "prolonged Q-T syndrome", "type": "Disease"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: We describe a patient who developed dilated cardiomyopathy and clinical congestive heart failure after 2 months of therapy with amphotericin B ( AmB ) for disseminated coccidioidomycosis .

Example answer:
{"entities": [{"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}, {"text": "AmB", "type": "Chemical"}, {"text": "coccidioidomycosis", "type": "Disease"}]}

Example input:
Sentence: We report a woman with coronary artery disease who developed a markedly prolonged QT interval and torsades de pointes ( TdP ) after taking ketoconazole for treatment of fungal infection .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "prolonged QT interval", "type": "Disease"}, {"text": "torsades de pointes", "type": "Disease"}, {"text": "TdP", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "fungal infection", "type": "Disease"}]}

Input:
Sentence: The authors describe the case of a 56-year-old woman with chronic , severe heart failure secondary to dilated cardiomyopathy and absence of significant ventricular arrhythmias who developed QT prolongation and torsade de pointes ventricular tachycardia during one cycle of intermittent low dose ( 2.5 mcg/kg per min ) dobutamine .

## Item bc5cdr:test:2185
Example input:
Sentence: Effects of an inhibitor of angiotensin converting enzyme ( Captopril ) on pulmonary and renal insufficiency due to intravascular coagulation in the rat .

Example answer:
{"entities": [{"text": "angiotensin", "type": "Chemical"}, {"text": "Captopril", "type": "Chemical"}, {"text": "intravascular coagulation", "type": "Disease"}]}

Example input:
Sentence: Nifedipine significantly improved kidney function as indicated by a significant lowering of serum creatinine levels at 6 and 12 months .

Example answer:
{"entities": [{"text": "Nifedipine", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: Captopril may , by the same mechanism , reduce the increase in glomerular filtration that is known to occur after an injection of thrombin , thereby diminishing the aggregation of fibrin monomers in the glomeruli , with the result that less fibrin will be deposited and thus less kidney damage will be produced .

Example answer:
{"entities": [{"text": "Captopril", "type": "Chemical"}, {"text": "kidney damage", "type": "Disease"}]}

Example input:
Sentence: The aim of this study was to examine further the renal function , including morphological analysis of the kidneys of male Sprague-Dawley rats treated with either cyclosporine A ( CsA ) , tacrolimus ( FK506 ) or SRL as monotherapies or in different combinations .

Example answer:
{"entities": [{"text": "cyclosporine A", "type": "Chemical"}, {"text": "CsA", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: Using puromycin aminonucleoside nephrosis ( PAN ) rats , we studied early ultrastructural and permeability changes in relation to the expression of the podocyte-associated molecules nephrin , a-actinin , dendrin , and plekhh2 , the last two of which were only recently discovered in podocytes .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: Six weeks after clipping of one renal artery , hypertensive rats ( 178 +/- 4 mm Hg ) were randomly assigned to three groups : untreated hypertensive controls ( n = 8 ) , enalapril-treated ( n = 8 ) , or nitrendipine-treated ( n = 10 ) .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}, {"text": "enalapril-treated", "type": "Chemical"}, {"text": "nitrendipine-treated", "type": "Chemical"}]}

Example input:
Sentence: Renal papillary necrosis ( RPN ) and a decreased urinary concentrating ability developed during continuous long-term treatment with aspirin and paracetamol in female Fischer 344 rats .

Example answer:
{"entities": [{"text": "Renal papillary necrosis", "type": "Disease"}, {"text": "RPN", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: GLEPP1 receptor tyrosine phosphatase ( Ptpro ) in rat PAN nephrosis .

Example answer:
{"entities": [{"text": "tyrosine", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: The effect of a 6-week treatment with the calcium channel blocker nitrendipine or the angiotensin converting enzyme inhibitor enalapril on blood pressure , albuminuria , renal hemodynamics , and morphology of the nonclipped kidney was studied in rats with two-kidney , one clip renovascular hypertension .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "nitrendipine", "type": "Chemical"}, {"text": "angiotensin", "type": "Chemical"}, {"text": "enalapril", "type": "Chemical"}, {"text": "albuminuria", "type": "Disease"}, {"text": "renovascular hypertension", "type": "Disease"}]}

Input:
Sentence: It appears that temocapril was effective in retarding renal progression and protected renal function in PAN neprotic rats .

## Item bc5cdr:test:2605
Example input:
Sentence: Histologic changes were found in rat kidneys after administration of MTX , CY and NG , while no such change was observed after 5-FU and joint administration of MTX + 5-FU + CY compared to controls .

Example answer:
{"entities": [{"text": "MTX", "type": "Chemical"}, {"text": "CY", "type": "Chemical"}, {"text": "NG", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}]}

Example input:
Sentence: Tissues were analyzed at 0 , 5 , 7 , 11 , 21 , 45 , 80 and 126 days after PAN injection so as to include both the acute phase of proteinuria associated with foot process effacement ( days 5-11 ) and the chronic phase of proteinuria associated with glomerulosclerosis ( days 45-126 ) .

Example answer:
{"entities": [{"text": "PAN", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: After 6 weeks of treatment , renal hemodynamics ( glomerular filtration rate and renal plasma flow ) were measured in the anesthetized rats .

Example answer:
{"entities": []}

Example input:
Sentence: Upon rechallenge with either cephalosporin , the hematologic syndrome was reproduced in most dogs tested ; cefonicid ( but not cefazedone ) -treated dogs showed a substantially reduced induction period ( 15 +/- 5 days ) compared to that of the first exposure to the drug ( 61 +/- 24 days ) .

Example answer:
{"entities": [{"text": "cephalosporin", "type": "Chemical"}, {"text": "hematologic syndrome", "type": "Disease"}, {"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}]}

Example input:
Sentence: After 12weeks , animals were euthanized , and CaCl ( 2 ) -treated , CaCl ( 2 ) -untreated ( n=12 ) and NaCl-treated aortic segments ( n=12 ) were collected for histological and molecular assessments .

Example answer:
{"entities": [{"text": "CaCl ( 2 )", "type": "Chemical"}, {"text": "NaCl-treated", "type": "Chemical"}]}

Example input:
Sentence: All rats were terminated either 24 h or 3 weeks after the DFP injection .

Example answer:
{"entities": [{"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: She subsequently died some 5 weeks after the commencement of her drug therapy.Post-mortem examination showed evidence of massive hepatocellular necrosis , acute hypersensitivity myocarditis , focal acute tubulo-interstitial nephritis and extensive bone marrow necrosis , with no evidence of malignancy .

Example answer:
{"entities": [{"text": "massive hepatocellular necrosis", "type": "Disease"}, {"text": "myocarditis", "type": "Disease"}, {"text": "nephritis", "type": "Disease"}, {"text": "bone marrow necrosis", "type": "Disease"}, {"text": "malignancy", "type": "Disease"}]}

Example input:
Sentence: Rats were treated with a single IV injection of puromycin aminonucleoside , ( PAN , 7.5 mg/kg ) and 24 hour urine samples were obtained prior to sacrifice on days 3,5,7,10,17,27,41 ( N = 5-10 per group ) .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: Histopathology analyses in the 2 animals that died revealed liver and kidney toxicity , with greater severity in the orally-treated animal .

Example answer:
{"entities": []}

Example input:
Sentence: After 12 weeks , rats were sacrificed and their kidneys harvested .

Example answer:
{"entities": []}

Input:
Sentence: The animals were killed 5 and 30 days after these injections and the kidneys were removed for histological and immunohistochemical studies .

## Item bc5cdr:test:2455
Example input:
Sentence: A Phase I study of intravenous ( IV ) bolus 4'-0-tetrahydropyranyladriamycin ( Pirarubicin ) was done in 55 patients in good performance status with refractory tumors .

Example answer:
{"entities": [{"text": "4'-0-tetrahydropyranyladriamycin", "type": "Chemical"}, {"text": "Pirarubicin", "type": "Chemical"}, {"text": "tumors", "type": "Disease"}]}

Example input:
Sentence: Of 24 evaluable patients , two achieved a complete remission and one achieved a partial remission for an overall response rate of 12.5 % ( 95 % confidence interval : 2.6-32.4 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Nine hundred one patients were randomized to treatment , 447 who received the lozenge and 454 who received the gum ( safety population ) .

Example answer:
{"entities": []}

Example input:
Sentence: All 20 patients responded to this regimen , 16/20 ( 80 % ) achieved a complete remission , and 20 % obtained a partial remission .

Example answer:
{"entities": []}

Example input:
Sentence: Treatment was comprised of VNB , 25 mg/m ( 2 ) , plus GEM , 1000 mg/m ( 2 ) , both on Days 1 , 8 , and 15 every 28 days .

Example answer:
{"entities": [{"text": "VNB", "type": "Chemical"}, {"text": "GEM", "type": "Chemical"}]}

Example input:
Sentence: In a randomized , double-blind , placebo-controlled , crossover study , we studied 12 volunteers in three experiments .

Example answer:
{"entities": []}

Example input:
Sentence: Nineteen patients finished the trial , and in 18 cases the therapeutic result was considered very good to good .

Example answer:
{"entities": []}

Example input:
Sentence: Over the period 1993-1996 , 551 cases of VTE were identified in Germany and the UK along with 2066 controls .

Example answer:
{"entities": [{"text": "VTE", "type": "Disease"}]}

Example input:
Sentence: Thirteen patients with acute leukemia were treated with a DNR-containing regimen .

Example answer:
{"entities": [{"text": "acute leukemia", "type": "Disease"}, {"text": "DNR-containing", "type": "Chemical"}]}

Example input:
Sentence: Recent reports indicate that single agent therapy with vinorelbine ( VNB ) or gemcitabine ( GEM ) may obtain a response rate of 20-30 % in elderly patients , with acceptable toxicity and improvement in symptoms and quality of life .

Example answer:
{"entities": [{"text": "vinorelbine", "type": "Chemical"}, {"text": "VNB", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "GEM", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Input:
Sentence: We found 19 trials , involving 2441 patients treated by VNR and 2050 control patients .

## Item bc5cdr:test:2500
Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "Disease"}, {"text": "METH", "type": "Chemical"}, {"text": "MPTP", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "METH-induced", "type": "Chemical"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: Alpha-lipoic acid exerts neuroprotective effects against chemotherapy induced neurotoxicity in sensory neurons : it rescues the mitochondrial toxicity and induces the expression of frataxin , an essential mitochondrial protein with anti-oxidant and chaperone properties .

Example answer:
{"entities": [{"text": "Alpha-lipoic acid", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "mitochondrial toxicity", "type": "Disease"}]}

Example input:
Sentence: Maltolyl p-coumarate was found to attenuate cognitive deficits in both rat models using passive avoidance test and to reduce apoptotic cell death observed in the hippocampus of the amyloid beta peptide ( 1-42 ) -infused rats .

Example answer:
{"entities": [{"text": "Maltolyl p-coumarate", "type": "Chemical"}, {"text": "cognitive deficits", "type": "Disease"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}]}

Example input:
Sentence: Reduction in the dosage of amiodarone resulted in the disappearance of the sinoatrial block and the persistence of asymptomatic sinus bradycardia .

Example answer:
{"entities": [{"text": "amiodarone", "type": "Chemical"}, {"text": "sinoatrial block", "type": "Disease"}, {"text": "sinus bradycardia", "type": "Disease"}]}

Example input:
Sentence: Amiodarone and atazanavir are recognized CYP3A4 inhibitors .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: Severe rhabdomyolysis and acute renal failure secondary to concomitant use of simvastatin , amiodarone , and atazanavir .

Example answer:
{"entities": [{"text": "rhabdomyolysis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: We observed sinoatrial block due to chronic amiodarone administration in a 5-year-old boy with primary cardiomyopathy , Wolff-Parkinson-White syndrome and supraventricular tachycardia .

Example answer:
{"entities": [{"text": "sinoatrial block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "primary cardiomyopathy", "type": "Disease"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "supraventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVE : To report a case of a severe interaction between simvastatin , amiodarone , and atazanavir resulting in rhabdomyolysis and acute renal failure .

Example answer:
{"entities": [{"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}, {"text": "rhabdomyolysis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: In vivo protection of dna damage associated apoptotic and necrotic cell deaths during acetaminophen-induced nephrotoxicity , amiodarone-induced lung toxicity and doxorubicin-induced cardiotoxicity by a novel IH636 grape seed proanthocyanidin extract .

Example answer:
{"entities": [{"text": "necrotic", "type": "Disease"}, {"text": "acetaminophen-induced", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "amiodarone-induced", "type": "Chemical"}, {"text": "lung toxicity", "type": "Disease"}, {"text": "doxorubicin-induced", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}, {"text": "IH636 grape seed proanthocyanidin extract", "type": "Chemical"}]}

Input:
Sentence: Disruption of hepatic lipid homeostasis in mice after amiodarone treatment is associated with peroxisome proliferator-activated receptor-alpha target gene activation .

## Item bc5cdr:test:2618
Example input:
Sentence: METHOD : The sample for the study consisted of 50 patients to whom subcutaneous heparin was administered .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: Five hundred fifty-three patients , 264 taking the lozenge and 289 taking the gum , used the study product for > or =4 days per week during the first 2 weeks ( evaluable population ) .

Example answer:
{"entities": []}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: Finally , 15 patients were excluded from the study ( noncompliance 14 , death 1 ) ; thus , 60 patients ( 31 in group I and 29 in group II ) were eligible for analysis .

Example answer:
{"entities": [{"text": "death", "type": "Disease"}]}

Example input:
Sentence: Of 24 evaluable patients , two achieved a complete remission and one achieved a partial remission for an overall response rate of 12.5 % ( 95 % confidence interval : 2.6-32.4 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Thirty PD patients participated in the study .

Example answer:
{"entities": [{"text": "PD", "type": "Disease"}]}

Example input:
Sentence: The tolerance was evaluated in these 110 patients , and 29 patients presented with local side-effects .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Nine hundred one patients were randomized to treatment , 447 who received the lozenge and 454 who received the gum ( safety population ) .

Example answer:
{"entities": []}

Example input:
Sentence: Seven patients developed glucose tolerance curves characteristic of diabetes but these were mild , did not require treatment and returned to normal on ceasing didanosine .

Example answer:
{"entities": [{"text": "glucose tolerance curves", "type": "Disease"}, {"text": "diabetes", "type": "Disease"}, {"text": "didanosine", "type": "Chemical"}]}

Example input:
Sentence: PG was well tolerated by all 54 patients .

Example answer:
{"entities": [{"text": "PG", "type": "Chemical"}]}

Input:
Sentence: Patients Fifty subjects signed informed consent and 41 underwent the frequently sampled intravenous glucose tolerance test .

## Item bc5cdr:test:2660
Example input:
Sentence: Patients had a median performance status of 1 ( WHO ) , and median age of 61 years .

Example answer:
{"entities": []}

Example input:
Sentence: The mean age of these patients was the same as for the entire group , 64 years .

Example answer:
{"entities": []}

Example input:
Sentence: The mean age of patients in the 16 probable cases was 57.9 , with hepatotoxicity being more common in women .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: To date , 23 men with a median age of 50 years and good performance status have entered the trial .

Example answer:
{"entities": []}

Example input:
Sentence: 164 patients ( mean age +/- standard deviation [ SD ] 81.6 +/- 6.8 years ) were admitted .

Example answer:
{"entities": []}

Example input:
Sentence: Ages ranged from 4 months to 17 years ; 58 patients were males and 42 females .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : One hundred and four ( 104 ) patients aged 6-35 years ( mean 17,2 years ) participated in the study .

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
Sentence: RESULTS : All patients ( 65+/-16 yrs ; 58 % males ) finished the examination .

Example answer:
{"entities": []}

Input:
Sentence: RESULTS : Two hundred twenty-eight patients ( 42 % men ) with a mean age of 81.1 ( range 76-94 ) were included in the analysis .

## Item bc5cdr:test:2245
Example input:
Sentence: Development of proteinuria after switch to sirolimus-based immunosuppression in long-term cardiac transplant patients .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "sirolimus-based", "type": "Chemical"}]}

Example input:
Sentence: Baseline renal ACE positively correlated with the relative rise in proteinuria after adriamycin ( r = 0.62 , P < 0.01 ) , renal interstitial alpha-smooth muscle actin ( r = 0.49 , P < 0.05 ) , interstitial macrophage influx ( r = 0.56 , P < 0.05 ) , interstitial collagen III ( r = 0.53 , P < 0.05 ) , glomerular alpha-smooth muscle actin ( r = 0.74 , P < 0.01 ) and glomerular desmin ( r = 0.48 , P < 0.05 ) .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}]}

Example input:
Sentence: Massive urinary protein excretion has been observed after conversion from calcineurin inhibitors to mammalian target of rapamycin ( mToR ) inhibitors , especially sirolimus , in renal transplant recipients with chronic allograft nephropathy .

Example answer:
{"entities": [{"text": "rapamycin", "type": "Chemical"}, {"text": "sirolimus", "type": "Chemical"}, {"text": "chronic allograft nephropathy", "type": "Disease"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: After 1 week of recovery , proteinuria was induced by adriamycin [ 1.5 mg/kg intravenously ( i.v . )

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}]}

Example input:
Sentence: Whether proteinuria was due to sirolimus or only a consequence of calcineurin inhibitors withdrawal remained unsolved until high range proteinuria has been observed during sirolimus therapy in islet transplantation and in patients who received sirolimus de novo .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "sirolimus", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : As anticipated , adriamycin elicited nephrotic range proteinuria , renal interstitial damage and mild focal glomerulosclerosis .

Example answer:
{"entities": [{"text": "adriamycin", "type": "Chemical"}, {"text": "nephrotic", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "renal interstitial damage", "type": "Disease"}, {"text": "focal glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Disease"}]}

Example input:
Sentence: This paper describes the clinical features of six children who developed the haemolytic-uraemic syndrome after treatment with metronidazole .

Example answer:
{"entities": [{"text": "haemolytic-uraemic syndrome", "type": "Disease"}, {"text": "metronidazole", "type": "Chemical"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Input:
Sentence: CONCLUSIONS : Children treated with indinavir have a high cumulative incidence of persistent sterile leukocyturia .

## Item bc5cdr:test:2687
Example input:
Sentence: The mean age of patients in the 16 probable cases was 57.9 , with hepatotoxicity being more common in women .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: The epidemiological studies that assessed the risk of venous thromboembolism ( VTE ) associated with newer oral contraceptives ( OC ) did not distinguish between patterns of OC use , namely first-time users , repeaters and switchers .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "VTE", "type": "Disease"}, {"text": "oral contraceptives", "type": "Chemical"}, {"text": "OC", "type": "Chemical"}]}

Example input:
Sentence: Impotence was more common among male patients than controls and was found to be associated with co-morbidity and the taking of methotrexate .

Example answer:
{"entities": [{"text": "Impotence", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: Sexual dysfunctions were found to be common among patients and controls , the majority in both groups reporting one or more dysfunctions .

Example answer:
{"entities": [{"text": "Sexual dysfunctions", "type": "Disease"}]}

Example input:
Sentence: Two groups of supine subjects were studied under placebo-controlled conditions , one during the night , when sleeping ( n = 7 ) and the other at daytime , when awake ( n = 6 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Data from a Transnational case-control study were used to assess the risk of VTE for the latter patterns of use , while accounting for duration of use .

Example answer:
{"entities": [{"text": "VTE", "type": "Disease"}]}

Example input:
Sentence: The patients were randomly allocated to one of three groups ; those in group A ( n = 10 ) were subjected to controlled hypotension alone , those in group B ( n = 10 ) to haemodilution alone and those in group C ( n = 10 ) to both controlled hypotension and haemodilution .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}]}

Example input:
Sentence: RESULTS : The patients in the study group were significantly younger than the patients in the control group ( P < 0.002 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Age-matched controls ( n = 14 ) were given only calcium .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}]}

Example input:
Sentence: Controls were age- and sex-matched non-PD patients referred to the cardiology department .

Example answer:
{"entities": []}

Input:
Sentence: Controls were patients admitted to the same hospitals from where the cases arose , also matched by age and sex .

## Item bc5cdr:test:2688
Example input:
Sentence: The semi-quantitative scoring was significantly worst in the group treated with CsA plus SRL ( P < 0.001 compared with controls ) and the analysis of the total grade of fibrosis also showed the highest proportion in the same group and was significantly different from controls ( P < 0.02 ) .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: Fewer than 6 % of patients in either group were considered by the investigator to have a worsening of their overall disease condition during the study .

Example answer:
{"entities": []}

Example input:
Sentence: In multivariate analysis , three factors independently predicted mortality : serum bilirubin ( > or=10.8 mg/dL ) , prothrombin time ( PT ) prolongation ( > or=26 seconds ) , and grade III/IV encephalopathy at presentation .

Example answer:
{"entities": [{"text": "bilirubin", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Multivariate stepwise logistic regression analysis using preoperative and postoperative variables identified that an increase of serum creatinine compared with average at 1 year , 3 months , and 4 weeks postoperatively were independent risk factors for the development of CRF or ESRD with odds ratios of 2.6 , 2.2 , and 1.6 , respectively .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Nested within the cohort , a matched case-control study was performed to estimate the association between cyclophosphamide and bladder cancer using odds ratios ( ORs ) as relative risk .

Example answer:
{"entities": [{"text": "cyclophosphamide", "type": "Chemical"}, {"text": "bladder cancer", "type": "Disease"}]}

Example input:
Sentence: Using as the reference group women who were not using oral contraception , had no recent pregnancy or menopausal symptoms , the case-control analysis gave an adjusted odds ratio ( OR ( adj ) ) of 7.44 ( 95 % CI 3.67-15.08 ) for CPA/EE use compared with an OR ( adj ) of 2.58 ( 95 % CI 1.60-4.18 ) for use of conventional COCs .

Example answer:
{"entities": [{"text": "CPA/EE", "type": "Chemical"}]}

Example input:
Sentence: Among women who used oral contraceptives , the odds ratio was 2.1 ( 95 percent confidence interval , 1.5 to 3.0 ) for those without a prothrombotic mutation and 1.9 ( 95 percent confidence interval , 0.6 to 5.5 ) for those with a mutation CONCLUSIONS : The risk of myocardial infarction was increased among women who used second-generation oral contraceptives .

Example answer:
{"entities": [{"text": "oral contraceptives", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: The adjusted odds ratio was 2.5 ( 95 percent confidence interval , 1.5 to 4.1 ) among women who used second-generation oral contraceptives and 1.3 ( 95 percent confidence interval , 0.7 to 2.5 ) among those who used third-generation oral contraceptives .

Example answer:
{"entities": [{"text": "oral contraceptives", "type": "Chemical"}]}

Example input:
Sentence: MAIN OUTCOME MEASURE : Odds ratios ( ORs ) measuring the association between antibacterial use and selected birth defects adjusted for potential confounders .

Example answer:
{"entities": [{"text": "birth defects", "type": "Disease"}]}

Input:
Sentence: Odds ratios were calculated using a conditional logistic model , including potential confounding factors , both for the whole study population and for the various underlying diseases .

## Item bc5cdr:test:2411
Example input:
Sentence: Development of ocular myasthenia during pegylated interferon and ribavirin treatment for chronic hepatitis C. A 63-year-old male experienced sudden diplopia after 9 weeks of administration of pegylated interferon ( IFN ) alpha-2b and ribavirin for chronic hepatitis C ( CHC ) .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated interferon", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "chronic hepatitis", "type": "Disease"}, {"text": "diplopia", "type": "Disease"}, {"text": "pegylated interferon ( IFN ) alpha-2b", "type": "Chemical"}, {"text": "chronic hepatitis C", "type": "Disease"}, {"text": "CHC", "type": "Disease"}]}

Example input:
Sentence: The ocular hypotensive effects were statistically significant for apraclonidine-treated eyes throughout the study and also statistically significant for contralateral eyes from three hours after topical administration of 1 % apraclonidine .

Example answer:
{"entities": [{"text": "ocular hypotensive", "type": "Disease"}, {"text": "apraclonidine-treated", "type": "Chemical"}, {"text": "apraclonidine", "type": "Chemical"}]}

Example input:
Sentence: The patient 's ophthalmological symptoms improved rapidly 3 weeks after discontinuation of pegylated IFN alpha-2b and ribavirin .

Example answer:
{"entities": [{"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : When performing intracarotid injection of carboplatin , we must be aware of its potentially blinding ocular toxicity .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}, {"text": "ocular toxicity", "type": "Disease"}]}

Example input:
Sentence: PURPOSE : To assess the incidence of postoperative emetic side effects after the administration of methylprednisolone and gentamicin into the posterior sub-Tenon 's space at the end of routine cataract surgery .

Example answer:
{"entities": [{"text": "methylprednisolone", "type": "Chemical"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "cataract", "type": "Disease"}]}

Example input:
Sentence: Generally , carboplatin is said to have milder side effects than cisplatin , whose ocular and orbital toxicity are well known .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: Various ocular symptoms and findings caused by carboplatin toxicity were seen .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: However , we experienced a case of severe ocular and orbital toxicity after intracarotid injection of carboplatin , which is infrequently reported .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}]}

Example input:
Sentence: Severe ocular and orbital toxicity after intracarotid injection of carboplatin for recurrent glioblastomas .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}, {"text": "glioblastomas", "type": "Disease"}]}

Input:
Sentence: Ocular motility changes after subtenon carboplatin chemotherapy for retinoblastoma .

## Item bc5cdr:test:2553
Example input:
Sentence: BACKGROUND/AIMS : Recently ribavirin has been found to inhibit angiogenesis and a number of angiogenesis inhibitors such as sunitinib and sorafenib have been found to cause acute hemolysis .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "sunitinib", "type": "Chemical"}, {"text": "sorafenib", "type": "Chemical"}, {"text": "hemolysis", "type": "Disease"}]}

Example input:
Sentence: Multivariate analysis showed a 2.8-fold increased risk of thrombosis in females .

Example answer:
{"entities": [{"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: In the present study , we have investigated the molecular mechanisms by which female hormones influence cholesterol metabolism in macrophages in response to the HIV protease inhibitor ritonavir .

Example answer:
{"entities": [{"text": "cholesterol", "type": "Chemical"}, {"text": "ritonavir", "type": "Chemical"}]}

Example input:
Sentence: In multivariate analysis , three factors independently predicted mortality : serum bilirubin ( > or=10.8 mg/dL ) , prothrombin time ( PT ) prolongation ( > or=26 seconds ) , and grade III/IV encephalopathy at presentation .

Example answer:
{"entities": [{"text": "bilirubin", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Tolerance and antiviral effect of ribavirin in patients with Argentine hemorrhagic fever .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "Argentine hemorrhagic fever", "type": "Disease"}]}

Example input:
Sentence: Uni- and multivariate analyses were used to test the influence of the clinical variables : age , sex , stroke , myocardiopathy ( MP ) , duration of the test , mitral regurgitation ( MR ) and the MZ dose .

Example answer:
{"entities": [{"text": "stroke", "type": "Disease"}, {"text": "myocardiopathy", "type": "Disease"}, {"text": "MP", "type": "Disease"}, {"text": "mitral regurgitation", "type": "Disease"}, {"text": "MR", "type": "Disease"}, {"text": "MZ", "type": "Chemical"}]}

Example input:
Sentence: Based on this principle a 27-year old woman , classified as being in the high-risk group ( Goldstein and Berkowitz score : 11 ) , was treated with multiple cytotoxic drugs .

Example answer:
{"entities": []}

Example input:
Sentence: Administration of ribavirin resulted in a neutralization of viremia and a drop of endogenous interferon titers .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "viremia", "type": "Disease"}]}

Example input:
Sentence: Tolerance and antiviral effect of ribavirin was studied in 6 patients with Argentine hemorrhagic fever ( AHF ) of more than 8 days of evolution .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "Argentine hemorrhagic fever", "type": "Disease"}, {"text": "AHF", "type": "Disease"}]}

Example input:
Sentence: Future research with larger number of patients is needed to find out modifiable factors that will improve the safety of ribavirin therapy .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}]}

Input:
Sentence: Such factors as sex ( female ) , age ( > or =60 years old ) , and the ribavirin dose by body weight ( 12 mg/kg or more ) were significant by univariate analysis .

## Item bc5cdr:test:2430
Example input:
Sentence: The hypotensive drug was discontinued at the completion of the operative procedure .

Example answer:
{"entities": [{"text": "hypotensive", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Sub-chronic low dose GVG potentiates and extends the inhibition of cocaine-induced increases in dopamine , effectively reducing cumulative exposures and the risk for VFDS .

Example answer:
{"entities": [{"text": "GVG", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: Eight glaucomatous patients chronically treated with timolol 0.5 % /12h , suffering from depression diagnosed through DMS-III-R criteria , were included in the study .

Example answer:
{"entities": [{"text": "glaucomatous", "type": "Disease"}, {"text": "timolol", "type": "Chemical"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: It is therefore suggested that caution should be exercised when prescribing vasodilator drugs in diabetic patients , particularly those with autonomic neuropathy .

Example answer:
{"entities": [{"text": "diabetic", "type": "Disease"}, {"text": "autonomic neuropathy", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : Given its preclinical success for treating substance abuse and the increased risk of visual field defects ( VFD ) associated with cumulative lifetime exposure , we explored the effects of sub-chronic low dose GVG on cocaine-induced increases in nucleus accumbens ( NAcc ) dopamine ( DA ) .

Example answer:
{"entities": [{"text": "substance abuse", "type": "Disease"}, {"text": "visual field defects", "type": "Disease"}, {"text": "VFD", "type": "Disease"}, {"text": "GVG", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: For the subsequent 6-week double-blind crossover phase ( phase B ) , patients taking standard- or low-dose haloperidol were switched to placebo , and patients taking placebo were randomly assigned to standard- or low-dose haloperidol .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: The patient 's ophthalmological symptoms improved rapidly 3 weeks after discontinuation of pegylated IFN alpha-2b and ribavirin .

Example answer:
{"entities": [{"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Sixty-seven of 926 patients ( 7.2 % ) required discontinuation of spironolactone due to hyperkalemia ( n = 33 ) or renal failure ( n = 34 ) .

Example answer:
{"entities": [{"text": "spironolactone", "type": "Chemical"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: In those with symptoms of hearing loss , the drug should be stopped for four weeks , and when the audiogram is stable or improved , therapy should be restarted at 10 to 25 mg/kg per dose .

Example answer:
{"entities": [{"text": "hearing loss", "type": "Disease"}]}

Example input:
Sentence: With either discontinuation or decreased dosage of the drug the symptoms disappeared and did not recur .

Example answer:
{"entities": []}

Input:
Sentence: A low dose and prompt discontinuation of the drug is recommended particularly in individuals with diabetes mellitus , glaucoma or who are heavy smokers .

## Item bc5cdr:test:1916
Example input:
Sentence: Patients were admitted to the hospital for measurement of lithium level , creatinine clearance , urine volume , and maximum osmolality .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: Rats with lithium-induced nephropathy were subjected to high protein ( HP ) feeding , uninephrectomy ( NX ) or a combination of these , in an attempt to induce glomerular hyperfiltration and further progression of renal failure .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: When comparing all lithium treated versus non-lithium-treated groups , lithium caused a reduction in glomerular filtration rate ( GFR ) without significant changes in effective renal plasma flow ( as determined by a marker secreted into the proximal tubules ) or lithium clearance .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: In contrast , mood switches were less frequent in patients receiving lithium ( 15 % , 4/26 ) than in patients not treated with lithium ( 44 % , 8/18 ; p = .04 ) .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: In all the experiments , the attenuation of the lithium-induced diabetes-insipidus-like syndrome by amiloride was accompanied by a reduction of the ratio between the lithium concentration in the renal medulla and its levels in the blood and an elevation in the plasma potassium level .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "Chemical"}, {"text": "diabetes-insipidus-like syndrome", "type": "Disease"}, {"text": "amiloride", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}]}

Example input:
Sentence: This report summarizes our experience in switching bipolar patients from lithium to divalproex sodium to alleviate such cognitive and functional impairments .

Example answer:
{"entities": [{"text": "bipolar", "type": "Disease"}, {"text": "lithium", "type": "Chemical"}, {"text": "divalproex sodium", "type": "Chemical"}, {"text": "cognitive and functional impairments", "type": "Disease"}]}

Example input:
Sentence: Lithium-associated cognitive and functional deficits reduced by a switch to divalproex sodium : a case series .

Example answer:
{"entities": [{"text": "Lithium-associated", "type": "Chemical"}, {"text": "cognitive and functional deficits", "type": "Disease"}, {"text": "divalproex sodium", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : We report seven cases where substitution of lithium , either fully or partially , with divalproex sodium was extremely helpful in reducing the cognitive , motivational , or creative deficits attributed to lithium in our bipolar patients .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}, {"text": "divalproex sodium", "type": "Chemical"}, {"text": "cognitive , motivational , or creative deficits", "type": "Disease"}, {"text": "bipolar", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : In this preliminary report , divalproex sodium was a superior alternative to lithium in bipolar patients experiencing cognitive deficits , loss of creativity , and functional impairments .

Example answer:
{"entities": [{"text": "divalproex sodium", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "bipolar", "type": "Disease"}, {"text": "cognitive deficits", "type": "Disease"}, {"text": "loss of creativity", "type": "Disease"}, {"text": "functional impairments", "type": "Disease"}]}

Example input:
Sentence: Lithium also caused proteinuria and systolic hypertension in absence of glomerulosclerosis .

Example answer:
{"entities": [{"text": "Lithium", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "glomerulosclerosis", "type": "Disease"}]}

Input:
Sentence: Patients with hypercalcemia resulting from medical diseases and bipolar patients with lithium-associated hypercalcemia had significantly higher frequencies of conduction defects .

## Item bc5cdr:test:2565
Example input:
Sentence: Although hepatocyte TJs are impaired in cholestasis , attempts to localize the precise site of hepatocyte TJ damage by freeze-fracture electron microscopy have produced limited information .

Example answer:
{"entities": [{"text": "cholestasis", "type": "Disease"}]}

Example input:
Sentence: The study investigates if alpha-lipoic acid is neuroprotective against chemotherapy induced neurotoxicity , if mitochondrial damage plays a critical role in toxic neurodegenerative cascade , and if neuroprotective effects of alpha-lipoic acid depend on mitochondria protection .

Example answer:
{"entities": [{"text": "alpha-lipoic acid", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "mitochondrial damage", "type": "Disease"}, {"text": "toxic neurodegenerative cascade", "type": "Disease"}]}

Example input:
Sentence: Mitochondrial abnormalities have been associated with several aspects of epileptogenesis , such as energy generation , control of cell death , neurotransmitter synthesis , and free radical ( FR ) production .

Example answer:
{"entities": [{"text": "Mitochondrial abnormalities", "type": "Disease"}, {"text": "death", "type": "Disease"}]}

Example input:
Sentence: We also assessed cell viability , mitochondrial membrane potential changes and counted autophagic vacuoles in cultured cardiomyocytes .

Example answer:
{"entities": []}

Example input:
Sentence: Our results demonstrate that both cisplatin and paclitaxel cause early mitochondrial impairment with loss of membrane potential and induction of autophagic vacuoles in neurons .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "mitochondrial impairment", "type": "Disease"}]}

Example input:
Sentence: Although evidences of mitochondrial abnormalities were found in previously published studies , our results do not suggest that the FRs , generated during the acute phase , determined important abnormalities in mtDNA , in expression of CCO-I , and in CCO activity .

Example answer:
{"entities": [{"text": "mitochondrial abnormalities", "type": "Disease"}]}

Example input:
Sentence: In conclusion mitochondrial toxicity is an early common event both in paclitaxel and cisplatin induced neurotoxicity .

Example answer:
{"entities": [{"text": "mitochondrial toxicity", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Pathologically , granular cytoplasmic changes were found in cardiac myocytes , indicating enlarged , damaged mitochondria .

Example answer:
{"entities": []}

Example input:
Sentence: Mitochondrial injury may be involved in the progression of heart failure caused by adriamycin via the autophagy pathway .

Example answer:
{"entities": [{"text": "heart failure", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}]}

Example input:
Sentence: Organelles of these cells , in particular the mitochondria ( increased number and size , distinct degeneration of their matrix and cristae ) and Golgi apparatus were altered .

Example answer:
{"entities": []}

Input:
Sentence: The progressive nature of mitochondrial injury suggests that mitochondria , not other subcellular organelles , are the major site of intracellular injury .

## Item bc5cdr:test:2417
Example input:
Sentence: The ocular hypotensive effects were statistically significant for apraclonidine-treated eyes throughout the study and also statistically significant for contralateral eyes from three hours after topical administration of 1 % apraclonidine .

Example answer:
{"entities": [{"text": "ocular hypotensive", "type": "Disease"}, {"text": "apraclonidine-treated", "type": "Chemical"}, {"text": "apraclonidine", "type": "Chemical"}]}

Example input:
Sentence: The renal function of 74 children with malignant mesenchymal tumors in complete remission and who have received the same ifosfamide chemotherapy protocol ( International Society of Pediatric Oncology Malignant Mesenchymal Tumor Study 84 [ SIOP MMT 84 ] ) were studied 1 year after the completion of treatment .

Example answer:
{"entities": [{"text": "malignant mesenchymal tumors", "type": "Disease"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "Malignant Mesenchymal Tumor", "type": "Disease"}]}

Example input:
Sentence: The patient 's ophthalmological symptoms improved rapidly 3 weeks after discontinuation of pegylated IFN alpha-2b and ribavirin .

Example answer:
{"entities": [{"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: In contrast , monkeys with long-term MPTP exposure , slow symptom progression and/or long symptom duration prior to initiation of levodopa therapy were more resistant to developing LIDs ( e.g. , dyskinesia developed no sooner than 146 days of chronic levodopa administration ) .

Example answer:
{"entities": [{"text": "MPTP", "type": "Chemical"}, {"text": "levodopa", "type": "Chemical"}, {"text": "LIDs", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Development of ocular myasthenia during pegylated interferon and ribavirin treatment for chronic hepatitis C. A 63-year-old male experienced sudden diplopia after 9 weeks of administration of pegylated interferon ( IFN ) alpha-2b and ribavirin for chronic hepatitis C ( CHC ) .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated interferon", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "chronic hepatitis", "type": "Disease"}, {"text": "diplopia", "type": "Disease"}, {"text": "pegylated interferon ( IFN ) alpha-2b", "type": "Chemical"}, {"text": "chronic hepatitis C", "type": "Disease"}, {"text": "CHC", "type": "Disease"}]}

Example input:
Sentence: The ocular myasthenia associated with combination therapy of pegylated IFN alpha-2b and ribavirin for CHC is very rarely reported ; therefore , we present this case with a review of the various eye complications of IFN therapy .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "CHC", "type": "Disease"}, {"text": "IFN", "type": "Chemical"}]}

Example input:
Sentence: CASE : A 58-year-old man received an intracarotid injection of carboplatin for recurrent glioblastomas in his left temporal lobe .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}, {"text": "glioblastomas", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : When performing intracarotid injection of carboplatin , we must be aware of its potentially blinding ocular toxicity .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}, {"text": "ocular toxicity", "type": "Disease"}]}

Example input:
Sentence: However , we experienced a case of severe ocular and orbital toxicity after intracarotid injection of carboplatin , which is infrequently reported .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}]}

Example input:
Sentence: Severe ocular and orbital toxicity after intracarotid injection of carboplatin for recurrent glioblastomas .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}, {"text": "glioblastomas", "type": "Disease"}]}

Input:
Sentence: RESULTS : Limitation of ocular motility was detected in all 12 eyes of 10 patients treated for intraocular retinoblastoma with 1 to 6 injections of subtenon carboplatin as part of multimodality therapy .

## Item bc5cdr:test:2312
Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: The patient was admitted to the hospital , anticoagulated with unfractionated heparin , and given intravenous diltiazem for rate control and intravenous amiodarone for rate and rhythm control .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}]}

Example input:
Sentence: Amiodarone-induced sinoatrial block .

Example answer:
{"entities": [{"text": "Amiodarone-induced", "type": "Chemical"}, {"text": "sinoatrial block", "type": "Disease"}]}

Example input:
Sentence: Thirty days after amiodarone discontinuation , His bundle electrograms showed atrial flutter without intra-Hisian or infra-Hisian delay .

Example answer:
{"entities": [{"text": "amiodarone", "type": "Chemical"}, {"text": "atrial flutter", "type": "Disease"}]}

Example input:
Sentence: Angiotensin-converting enzyme inhibitors and angiotensin II receptor-blocking drugs hold promise in atrial fibrillation through cardiac remodelling .

Example answer:
{"entities": [{"text": "Angiotensin-converting", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "cardiac remodelling", "type": "Disease"}]}

Example input:
Sentence: We observed sinoatrial block due to chronic amiodarone administration in a 5-year-old boy with primary cardiomyopathy , Wolff-Parkinson-White syndrome and supraventricular tachycardia .

Example answer:
{"entities": [{"text": "sinoatrial block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "primary cardiomyopathy", "type": "Disease"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "supraventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: A case is presented of a reversible intra-Hisian block occurring under amiodarone treatment for atrial tachycardia in a patient without clear intraventricular conduction abnormalities .

Example answer:
{"entities": [{"text": "intra-Hisian block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atrial tachycardia", "type": "Disease"}, {"text": "intraventricular conduction abnormalities", "type": "Disease"}]}

Example input:
Sentence: Amiodarone should be used with caution during long-term oral therapy in patients with or without clear intraventricular conduction defects .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "Chemical"}]}

Example input:
Sentence: A patient with sinuatrial disease and implanted pacemaker was treated with amiodarone ( maximum dose 1000 mg , maintenance dose 800 mg daily ) for 10 months , for control of supraventricular tachyarrhythmias .

Example answer:
{"entities": [{"text": "sinuatrial disease", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "supraventricular tachyarrhythmias", "type": "Disease"}]}

Example input:
Sentence: Reduction in the dosage of amiodarone resulted in the disappearance of the sinoatrial block and the persistence of asymptomatic sinus bradycardia .

Example answer:
{"entities": [{"text": "amiodarone", "type": "Chemical"}, {"text": "sinoatrial block", "type": "Disease"}, {"text": "sinus bradycardia", "type": "Disease"}]}

Input:
Sentence: OBJECTIVES : The aim of this study was to determine whether the use of amiodarone in patients with atrial fibrillation ( AF ) increases the risk of bradyarrhythmia requiring a permanent pacemaker .

## Item bc5cdr:test:2435
Example input:
Sentence: METHODS : We present the first case report of a woman with hyperthyroidism treated with propylthiouracil in whom a syndrome of pericarditis , fever , and glomerulonephritis developed .

Example answer:
{"entities": [{"text": "hyperthyroidism", "type": "Disease"}, {"text": "propylthiouracil", "type": "Chemical"}, {"text": "pericarditis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "glomerulonephritis", "type": "Disease"}]}

Example input:
Sentence: Abnormal brain responses to somatosensory stimuli have been found in patients with hyperalgesia as well as in normal subjects during experimental central sensitization .

Example answer:
{"entities": [{"text": "hyperalgesia", "type": "Disease"}]}

Example input:
Sentence: Five hours after exposure , he developed disulfiram-like syndrome with flushing , tachycardia , and arterial hypotension after consuming three glasses of wine .

Example answer:
{"entities": [{"text": "disulfiram-like", "type": "Chemical"}, {"text": "flushing", "type": "Disease"}, {"text": "tachycardia", "type": "Disease"}, {"text": "arterial hypotension", "type": "Disease"}]}

Example input:
Sentence: Removal of the carotid sinuses caused an elevation blood pressure and heart rate and abolished the negative chronotropic effect of norepinephrine .

Example answer:
{"entities": [{"text": "norepinephrine", "type": "Chemical"}]}

Example input:
Sentence: It has been shown that bromocriptine-induced tachycardia , which persisted after adrenalectomy , is ( i ) mediated by central dopamine D2 receptor activation and ( ii ) reduced by 5-day isoproterenol pretreatment , supporting therefore the hypothesis that this effect is dependent on sympathetic outflow to the heart .

Example answer:
{"entities": [{"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: Furthermore , it was found that the magnitude of attentional modulation in secondary hyperalgesia is very similar to that of capsaicin-untreated , control condition .

Example answer:
{"entities": [{"text": "hyperalgesia", "type": "Disease"}, {"text": "capsaicin-untreated", "type": "Chemical"}]}

Example input:
Sentence: Noxious chemical stimulation of rat facial mucosa increases intracranial blood flow through a trigemino-parasympathetic reflex -- an experimental model for vascular dysfunctions in cluster headache .

Example answer:
{"entities": [{"text": "vascular dysfunctions", "type": "Disease"}, {"text": "cluster headache", "type": "Disease"}]}

Example input:
Sentence: Ecstasy-specific hypoactivity was evident in the right dorsal anterior cingulated cortex ( ACC ) and left posterior cingulated cortex .

Example answer:
{"entities": [{"text": "Ecstasy-specific", "type": "Chemical"}]}

Example input:
Sentence: To this end , persistent hyperalgesia was induced by administration of capsaicin in the tail of gonadally intact F344 rats , following which the tail was immersed in a mildly noxious thermal stimulus , and tail-withdrawal latencies measured .

Example answer:
{"entities": [{"text": "hyperalgesia", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: Further signs were hyperhidrosis , hypersalivation , bronchorrhoea , and severe miosis ; the electrocardiographic finding was atrio-ventricular dissociation .

Example answer:
{"entities": [{"text": "hyperhidrosis", "type": "Disease"}, {"text": "hypersalivation", "type": "Disease"}, {"text": "bronchorrhoea", "type": "Disease"}, {"text": "miosis", "type": "Disease"}, {"text": "atrio-ventricular dissociation", "type": "Disease"}]}

Input:
Sentence: All patients had gustatory hyperhidrosis , which interfered with their social activities , after transthroacic endoscopic sympathectomy , and which was associated with compensatory focal hyperhidrosis .

## Item bc5cdr:test:2705
Example input:
Sentence: The density of hippocampal neurons in the brains of animals treated with BMCs was markedly preserved .

Example answer:
{"entities": []}

Example input:
Sentence: Population responses in granule cells of the dentate gyrus were examined in transverse slices of the ventral hippocampus from pilocarpine-treated and untreated mice .

Example answer:
{"entities": [{"text": "pilocarpine-treated", "type": "Chemical"}]}

Example input:
Sentence: After 12 weeks , rats were sacrificed and their kidneys harvested .

Example answer:
{"entities": []}

Example input:
Sentence: Using this rationale , the 8-aminoquinoline WR242511 , a potent long-lasting MHb former in rodents and beagle dogs , was studied in the rhesus monkey for advanced development as a potential CN pretreatment .

Example answer:
{"entities": [{"text": "8-aminoquinoline", "type": "Chemical"}, {"text": "WR242511", "type": "Chemical"}]}

Example input:
Sentence: METHODS : The expression of MRP2 and Pgp in brain and liver sections of TR ( - ) rats and normal Wistar rats was determined with immunohistochemistry , by using a novel , highly selective monoclonal MRP2 antibody and the monoclonal Pgp antibody C219 , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: Over a range of 1-150 days of DES treatment , pairs of control and DES-treated rats were sacrificed , and their pituitaries dissociated enzymatically into single-cell preparations .

Example answer:
{"entities": [{"text": "DES", "type": "Chemical"}, {"text": "DES-treated", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Immunofluorescence staining with the MRP2 antibody was found to label a high number of microvessels throughout the brain in normal Wistar rats , whereas such labeling was absent in TR ( - ) rats .

Example answer:
{"entities": []}

Example input:
Sentence: After 12weeks , animals were euthanized , and CaCl ( 2 ) -treated , CaCl ( 2 ) -untreated ( n=12 ) and NaCl-treated aortic segments ( n=12 ) were collected for histological and molecular assessments .

Example answer:
{"entities": [{"text": "CaCl ( 2 )", "type": "Chemical"}, {"text": "NaCl-treated", "type": "Chemical"}]}

Example input:
Sentence: They became more severe in the later months of the experiment , and were most severe after 12 months , located mainly in the molecular layer of the cerebellar cortex .

Example answer:
{"entities": []}

Example input:
Sentence: For the cytoprotection study , animals were orally gavaged 100 mg/Kg GSPE for 7-10 days followed by i.p .

Example answer:
{"entities": [{"text": "GSPE", "type": "Chemical"}]}

Input:
Sentence: Animals were killed between 30 and 60 days later , and brain sections were processed for GAP43 immunohistochemistry .

## Item bc5cdr:test:1849
Example input:
Sentence: Bradykinin receptors antagonists and nitric oxide synthase inhibitors in vincristine and streptozotocin induced hyperalgesia in chemotherapy and diabetic neuropathy rat model .

Example answer:
{"entities": [{"text": "Bradykinin", "type": "Chemical"}, {"text": "nitric oxide", "type": "Chemical"}, {"text": "vincristine", "type": "Chemical"}, {"text": "streptozotocin", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "diabetic neuropathy", "type": "Disease"}]}

Example input:
Sentence: In streptozotocin-induced hyperalgesia , inducible NO synthase participates in pronociceptive activity of bradykinin , whereas in vincristine-induced hyperalgesia bradykinin seemed to activate neuronal NO synthase pathway .

Example answer:
{"entities": [{"text": "streptozotocin-induced", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "NO", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}, {"text": "vincristine-induced", "type": "Chemical"}]}

Example input:
Sentence: On the contrary , the cataleptogenic effect of haloperidol was significantly reduced in rats treated with desipramine and 6-OHDA but not in rats treated with 6-OHDA or in rats with lesions of the locus coeruleus .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "desipramine", "type": "Chemical"}, {"text": "6-OHDA", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Bilateral infusions of neurotensin into the globus pallidus reversed haloperidol-induced parkinsonian catalepsy in rats .

Example answer:
{"entities": [{"text": "neurotensin", "type": "Chemical"}, {"text": "haloperidol-induced", "type": "Chemical"}, {"text": "parkinsonian catalepsy", "type": "Disease"}]}

Example input:
Sentence: Catalepsy was induced by haloperidol ( 2 mg/kg p.o .

Example answer:
{"entities": [{"text": "Catalepsy", "type": "Disease"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: These results indicate that noradrenergic neurons have an important role in the manifestation of catalepsy induced by THC , whereas dopaminergic neurons are important in catalepsy induced by haloperidol .

Example answer:
{"entities": [{"text": "catalepsy", "type": "Disease"}, {"text": "THC", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: in the rat haloperidol-induced catalepsy model for Parkinson 's disease .

Example answer:
{"entities": [{"text": "haloperidol-induced", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: Noradrenergic involvement in catalepsy induced by delta 9-tetrahydrocannabinol .

Example answer:
{"entities": [{"text": "catalepsy", "type": "Disease"}, {"text": "delta 9-tetrahydrocannabinol", "type": "Chemical"}]}

Example input:
Sentence: PURPOSE : The influence of an irreversible inhibitor of constitutive NO synthase ( L-NOArg ; 1.0 mg/kg ip ) , a relatively selective inhibitor of inducible NO synthase ( L-NIL ; 1.0 mg/kg ip ) and a relatively specific inhibitor of neuronal NO synthase ( 7-NI ; 0.1 mg/kg ip ) , on antihyperalgesic action of selective antagonists of B2 and B1 receptors : D-Arg- [ Hyp3 , Thi5 , D-Tic7 , Oic8 ] bradykinin ( HOE 140 ; 70 nmol/kg ip ) or des Arg10 HOE 140 ( 70 nmol/kg ip ) respectively , in model of diabetic ( streptozotocin-induced ) and toxic ( vincristine-induced ) neuropathy was investigated .

Example answer:
{"entities": [{"text": "NO", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}, {"text": "HOE 140", "type": "Chemical"}, {"text": "des Arg10 HOE 140", "type": "Chemical"}]}

Example input:
Sentence: NRA0160 and clozapine significantly induced catalepsy in rats , although their effects did not exceed 50 % induction even at the highest dose given .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}]}

Input:
Sentence: RATIONALE : NG-nitro-L-arginine ( L-NOARG ) , an inhibitor of nitric-oxide synthase ( NOS ) , induces catalepsy in mice .
