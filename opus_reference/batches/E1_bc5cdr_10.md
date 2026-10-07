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

## Item bc5cdr:test:2284
Example input:
Sentence: Ten rats had arterial , central venous ( CVP ) , and subdural cannulae inserted under halothane anesthesia .

Example answer:
{"entities": [{"text": "halothane", "type": "Chemical"}]}

Example input:
Sentence: Repeated cerebral perfusion SPECT scans revealed decreased basal ganglia perfusion while the movement disorder was present , and a return to normal perfusion when the rabbit syndrome resolved .

Example answer:
{"entities": [{"text": "decreased basal ganglia perfusion", "type": "Disease"}, {"text": "movement disorder", "type": "Disease"}, {"text": "rabbit syndrome", "type": "Disease"}]}

Example input:
Sentence: A comparable overexpression of Pgp in the BBB was obtained after pilocarpine-induced seizures in wild-type Wistar rats .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Bilateral infusions of neurotensin into the globus pallidus reversed haloperidol-induced parkinsonian catalepsy in rats .

Example answer:
{"entities": [{"text": "neurotensin", "type": "Chemical"}, {"text": "haloperidol-induced", "type": "Chemical"}, {"text": "parkinsonian catalepsy", "type": "Disease"}]}

Example input:
Sentence: The other rats showed a strong decrease in the rigidity and the occurrence of stereotyped ( S ) licking and/or gnawing in presence of akinetic or hyperkinetic ( K ) behaviour ( AS/KS group ) , suggesting signs of dopaminergic activation .

Example answer:
{"entities": [{"text": "rigidity", "type": "Disease"}, {"text": "akinetic", "type": "Disease"}, {"text": "hyperkinetic", "type": "Disease"}]}

Example input:
Sentence: was examined in mice , rats and guinea pigs by use of the hot-plate , abdominal-constriction , tail-flick and paw-pressure tests .

Example answer:
{"entities": []}

Example input:
Sentence: The rat biodistribution studies showed a rapid blood clearance via the kidneys .

Example answer:
{"entities": []}

Example input:
Sentence: In the five rats that developed somatic rigidity , ICP and CVP increased significantly above baseline ( delta ICP 7.5 +/- 1.0 mmHg , delta CVP 5.9 +/- 1.3 mmHg ) .

Example answer:
{"entities": [{"text": "somatic rigidity", "type": "Disease"}]}

Example input:
Sentence: An experimental model was developed in the rat to measure changes in lacrimation and intracranial blood flow following noxious chemical stimulation of facial mucosa .

Example answer:
{"entities": []}

Example input:
Sentence: Noxious chemical stimulation of rat facial mucosa increases intracranial blood flow through a trigemino-parasympathetic reflex -- an experimental model for vascular dysfunctions in cluster headache .

Example answer:
{"entities": [{"text": "vascular dysfunctions", "type": "Disease"}, {"text": "cluster headache", "type": "Disease"}]}

Input:
Sentence: These results were explained by an asymmetric cerebral blood flow depending upon the paw preference in rats .

## Item bc5cdr:test:2112
Example input:
Sentence: Massive urinary protein excretion has been observed after conversion from calcineurin inhibitors to mammalian target of rapamycin ( mToR ) inhibitors , especially sirolimus , in renal transplant recipients with chronic allograft nephropathy .

Example answer:
{"entities": [{"text": "rapamycin", "type": "Chemical"}, {"text": "sirolimus", "type": "Chemical"}, {"text": "chronic allograft nephropathy", "type": "Disease"}]}

Example input:
Sentence: Subsequent amantadine treatments produced enhancement of motility from corresponding control in all mouse strains with the BALB/C mice being the least sensitive .

Example answer:
{"entities": [{"text": "amantadine", "type": "Chemical"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: To determine mitochondrial events from HAART in vivo , 8-week-old hemizygous transgenic AIDS mice ( NL4-3Delta gag/pol ; TG ) and wild-type FVB/n littermates were treated with the HAART combination of zidovudine , lamivudine , and indinavir or vehicle control for 10 days or 35 days .

Example answer:
{"entities": [{"text": "AIDS", "type": "Disease"}, {"text": "zidovudine", "type": "Chemical"}, {"text": "lamivudine", "type": "Chemical"}, {"text": "indinavir", "type": "Chemical"}]}

Example input:
Sentence: To test the validity of the hypothesis that hypomethylation of DNA plays an important role in the initiation of carcinogenic process , 5-azacytidine ( 5-AzC ) ( 10 mg/kg ) , an inhibitor of DNA methylation , was given to rats during the phase of repair synthesis induced by the three carcinogens , benzo [ a ] -pyrene ( 200 mg/kg ) , N-methyl-N-nitrosourea ( 60 mg/kg ) and 1,2-dimethylhydrazine ( 1,2-DMH ) ( 100 mg/kg ) .

Example answer:
{"entities": [{"text": "initiation of carcinogenic process", "type": "Disease"}, {"text": "5-azacytidine", "type": "Chemical"}, {"text": "5-AzC", "type": "Chemical"}, {"text": "benzo [ a ] -pyrene", "type": "Chemical"}, {"text": "N-methyl-N-nitrosourea", "type": "Chemical"}, {"text": "1,2-dimethylhydrazine", "type": "Chemical"}, {"text": "1,2-DMH", "type": "Chemical"}]}

Example input:
Sentence: However , the threshold ( 61.6 +/- 8.7 mg. l ( -1 ) ) during 1.6 % sevoflurane was not significant from that during 0.8 % sevoflurane , indicating a celling effect .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "Chemical"}]}

Example input:
Sentence: BMCs obtained from green fluorescent protein ( GFP ) transgenic mice or rats were transplanted intravenously after induction of status epilepticus ( SE ) .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Apamin ( 10 ng ) had a tendency to decrease the convulsive threshold ( 21.6 +/- 2.2 to 19.9 +/- 2.5 mg. l ( -1 ) ) but this was not statistically significant .

Example answer:
{"entities": [{"text": "Apamin", "type": "Chemical"}, {"text": "convulsive", "type": "Disease"}]}

Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "Chemical"}]}

Example input:
Sentence: Following recovery , the monkeys were selectively deafened for high frequencies using kanamycin and furosemide .

Example answer:
{"entities": [{"text": "kanamycin", "type": "Chemical"}, {"text": "furosemide", "type": "Chemical"}]}

Input:
Sentence: In the transgenic group , kanamycin increased the threshold by only 15 dB over the respective controls .

## Item bc5cdr:test:1899
Example input:
Sentence: Other side effects were rare , and peripheral neurotoxicity has been minor ( 26 % grade 1 ) .

Example answer:
{"entities": [{"text": "peripheral neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: A low incidence of cardiovascular malformations was observed after exposure to each of the four calcium channel blockers , but this incidence was statistically significant only for verapamil and nifedipine .

Example answer:
{"entities": [{"text": "cardiovascular malformations", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: Other possible adverse effects -- such as gastrointestinal disorders , orthostatic hypotension , levodopa-induced psychosis , sleep disturbances or parasomnias , or drug interactions -- also require carefully monitored individual treatment .

Example answer:
{"entities": [{"text": "gastrointestinal disorders", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "levodopa-induced", "type": "Chemical"}, {"text": "psychosis", "type": "Disease"}, {"text": "sleep disturbances", "type": "Disease"}, {"text": "parasomnias", "type": "Disease"}]}

Example input:
Sentence: The most common adverse events were nausea ( 17.2 % and 16.1 % ; 95 % CI , -3.7 to 6.0 ) , hiccups ( 10.7 % and 6.6 % ; 95 % CI , 0.5 to 7.8 ) , and headache ( 8.7 % and 9.9 % ; 95 % Cl , -5.0 to 2.6 ) .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "hiccups", "type": "Disease"}, {"text": "headache", "type": "Disease"}]}

Example input:
Sentence: Conventional agents are associated with unwanted central nervous system effects , including extrapyramidal symptoms ( EPS ) , tardive dyskinesia , sedation , and possible impairment of some cognitive measures , as well as cardiac effects , orthostatic hypotension , hepatic changes , anticholinergic side effects , sexual dysfunction , and weight gain .

Example answer:
{"entities": [{"text": "extrapyramidal symptoms", "type": "Disease"}, {"text": "EPS", "type": "Disease"}, {"text": "tardive dyskinesia", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}]}

Example input:
Sentence: AIM : This study was carried out to determine the effect of injection duration on bruising and pain following the administration of the subcutaneous injection of heparin .

Example answer:
{"entities": [{"text": "bruising", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : It was determined that injection duration had an effect on bruising and pain following the subcutaneous administration of heparin .

Example answer:
{"entities": [{"text": "bruising", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Although different methods to prevent bruising and pain following the subcutaneous injection of heparin have been widely studied and described , the effect of injection duration on the occurrence of bruising and pain is little documented .

Example answer:
{"entities": [{"text": "bruising", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: PATIENTS AND METHODS : Patients with more than 50 % decrease in platelet count or thrombocytopenia ( < 150 x 10 ( 9 ) /L ) after exposure to heparin , who had a positive two-step antigen assay [ optical density ( OD ) > 0.4 and > 50 inhibition with high concentration of heparin ] were included in the study .

Example answer:
{"entities": [{"text": "thrombocytopenia", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Input:
Sentence: Although reasonable incidences of many of these side effects can be `` softly '' deduced from current reports dealing with unfractionated heparin , at present the incidences of these side effects with newer low molecular weight heparins appear to be much less common .

## Item bc5cdr:test:1372
Example input:
Sentence: In conclusion , gene-targeted mice lacking SGK1 showed blunted volume retention , yet were not protected against renal fibrosis during experimental nephrotic syndrome .

Example answer:
{"entities": [{"text": "volume retention", "type": "Disease"}, {"text": "fibrosis", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}]}

Example input:
Sentence: Treatment with Ato improved endothelial function , reduced superoxide production and reduced SBP in Dex-treated SD rats .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}, {"text": "superoxide", "type": "Chemical"}, {"text": "Dex-treated", "type": "Chemical"}]}

Example input:
Sentence: It has also been suggested that sirolimus directly causes increased glomerular permeability/injury , but evidence for this mechanism is currently inconclusive .

Example answer:
{"entities": [{"text": "sirolimus", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : This rat study demonstrated a synergistic nephrotoxic effect of CsA plus SRL , whereas FK506 plus SRL was better tolerated .

Example answer:
{"entities": [{"text": "nephrotoxic", "type": "Disease"}, {"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}]}

Example input:
Sentence: During the course of nephrotic syndrome , serum urea concentrations increased significantly faster in sgk1 ( -/- ) mice than in sgk1 ( +/+ ) mice leading to uremia and a reduced median survival in sgk1 ( -/- ) mice ( 29 vs. 40 days in sgk1 ( +/+ ) mice ) .

Example answer:
{"entities": [{"text": "nephrotic syndrome", "type": "Disease"}, {"text": "urea", "type": "Chemical"}, {"text": "uremia", "type": "Disease"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: Our case supports the hypothesis that endogenous renal prostaglandins play a role in the maintenance of renal blood flow when circulating plasma volume is diminished .

Example answer:
{"entities": [{"text": "prostaglandins", "type": "Chemical"}]}

Example input:
Sentence: It could be inferred that gum Arabic treatment has induced a modest amelioration of some of the histological and biochemical indices of GM nephrotoxicity .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}]}

Example input:
Sentence: Reactive oxygen species have been implicated in the pathogenesis of acute puromycin aminonucleoside ( PAN ) -induced nephropathy , with antioxidants significantly reducing the proteinuria .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: We propose that amphotericin , in the setting of reduced effective arterial volume , may activate tubuloglomerular feedback , thereby contributing to acute renal failure .

Example answer:
{"entities": [{"text": "amphotericin", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Input:
Sentence: These results suggest that 1 ) both SOD and DMTU have protective effects on GM-mediated nephropathy , 2 ) the mechanisms for the protective effects differ for SOD and DMTU , and 3 ) superoxide anions play a critical role in GM-induced renal vasoconstriction .

## Item bc5cdr:test:2026
Example input:
Sentence: In this study , we examined the roles of lipopolysaccharide , a pro-inflammatory and inflammatory factor , treatment in modulating the methamphetamine-induced nigrostriatal dopamine neurotoxicity .

Example answer:
{"entities": [{"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "methamphetamine-induced", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Based on the finding that VPU and VPA could protect the animals against pilocarpine-induced seizure it is suggested that the reduction of inhibitory amino acid neurotransmitters was comparatively minor and offset by a pronounced reduction of glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: Sub-chronic low dose gamma-vinyl GABA ( vigabatrin ) inhibits cocaine-induced increases in nucleus accumbens dopamine .

Example answer:
{"entities": [{"text": "gamma-vinyl GABA", "type": "Chemical"}, {"text": "vigabatrin", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: In the present study , we investigated whether maltolyl p-coumarate could improve cognitive decline in scopolamine-injected rats and in amyloid beta peptide ( 1-42 ) -infused rats .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "cognitive decline", "type": "Disease"}, {"text": "scopolamine-injected", "type": "Chemical"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}]}

Example input:
Sentence: Therefore , like VPA , the finding that VPU could drastically reduce pilocarpine-induced increases in glutamate and aspartate should account , at least partly , for its anticonvulsant activity observed in pilocarpine-induced seizure in experimental animals .

Example answer:
{"entities": [{"text": "VPA", "type": "Chemical"}, {"text": "VPU", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: The effects of varying the extracellular concentrations of Na and Ca ( [ Na ] o and [ Ca ] o ) on both , the spontaneous beating and the negative chronotropic action of verapamil , were studied in the isolated rat atria .

Example answer:
{"entities": [{"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: THP exhibited an antipsychotic-like profile by potentiating haloperidol-induced catalepsy , reducing amphetamine-induced hyperactivity and reducing apomorphine-induced climbing in mice .

Example answer:
{"entities": []}

Example input:
Sentence: Possible mechanisms that involve a verapamil-related increase in platelet and/or vascular alpha 2-adrenoreceptor affinity for catecholamines are discussed .

Example answer:
{"entities": [{"text": "verapamil-related", "type": "Chemical"}, {"text": "catecholamines", "type": "Chemical"}]}

Example input:
Sentence: Such systemic lipopolysaccharide treatment mitigated methamphetamine-induced striatal dopamine and 3,4-dihydroxyphenylacetic acid depletions in a dose-dependent manner .

Example answer:
{"entities": [{"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "methamphetamine-induced", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "3,4-dihydroxyphenylacetic acid", "type": "Chemical"}]}

Example input:
Sentence: A single MPEP ( 5 mg/kg ip ) injection reduced the basal extracellular dopamine level in the striatum , as well as dopamine release stimulated either by methamphetamine ( 10 mg/kg sc ) or by intrastriatally administered veratridine ( 100 microM ) .

Example answer:
{"entities": [{"text": "MPEP", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "veratridine", "type": "Chemical"}]}

Input:
Sentence: We emphasize the anti-dopaminergic effect of veralipride .

## Item bc5cdr:test:1973
Example input:
Sentence: RESULTS : Subjects ( n = 139 ) were 72 women and 67 men , aged 40.8 +/- 12.1 years , hospitalized for 24.9 +/- 23.3 days , and given clozapine , gradually increased to an average daily dose of 282 +/- 203 mg ( 3.45 +/- 2.45 mg/kg ) for 18.9 +/- 16.4 days .

Example answer:
{"entities": [{"text": "clozapine", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : For the 60 patients who completed phase A , standard-dose haloperidol was efficacious and superior to both low-dose haloperidol and placebo for scores on the Brief Psychiatric Rating Scale psychosis factor and on psychomotor agitation .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "psychosis", "type": "Disease"}, {"text": "psychomotor agitation", "type": "Disease"}]}

Example input:
Sentence: On the Positive and Negative Syndrome Scale positive subscale , all treatments were superior to placebo with LOCF and MMRM ; asenapine at 5 mg BID was superior to placebo on the negative subscale with MMRM and on the general psychopathology subscale with LOCF and MMRM .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}]}

Example input:
Sentence: SCr increases > or = 0.5 mg/dL occurred in 4.4 % ( 9 of 204 patients ) after iopamidol and 6.7 % ( 14 of 210 patients ) after iodixanol ( P=0.39 ) , whereas rates of SCr increases > or = 25 % were 9.8 % and 12.4 % , respectively ( P=0.44 ) .

Example answer:
{"entities": [{"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}]}

Example input:
Sentence: In a double-blind 6-week trial , 458 patients with acute schizophrenia were randomly assigned to fixed-dose treatment with asenapine at 5 mg twice daily ( BID ) , asenapine at 10 mg BID , placebo , or haloperidol at 4 mg BID ( to verify assay sensitivity ) .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "Disease"}, {"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Compared with placebo subjects , alprazolam patients developed more adverse reactions ( 21 % v. 0 % ) of depression , enuresis , disinhibition and aggression ; and more side-effects , particularly sedation , irritability , impaired memory , weight loss and ataxia .

Example answer:
{"entities": [{"text": "alprazolam", "type": "Chemical"}, {"text": "depression", "type": "Disease"}, {"text": "enuresis", "type": "Disease"}, {"text": "aggression", "type": "Disease"}, {"text": "irritability", "type": "Disease"}, {"text": "impaired memory", "type": "Disease"}, {"text": "weight loss", "type": "Disease"}, {"text": "ataxia", "type": "Disease"}]}

Example input:
Sentence: better , in patients on bupropion SR , at 2.4 ( 1.2 ) , than in the placebo group , at 3.9 ( 1.1 ) ( P= 0.01 ) .

Example answer:
{"entities": [{"text": "bupropion", "type": "Chemical"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: better , among men who received bupropion than placebo , at 15.5 ( 4.3 ) vs 21.5 ( 4.7 ) ( P= 0.002 ) .

Example answer:
{"entities": [{"text": "bupropion", "type": "Chemical"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Input:
Sentence: However , olanzapine-treated patients had a statistically significant greater mean ( +/- SD ) weight gain than placebo-treated patients ( 2.1 +/- 2.8 vs 0.45 +/- 2.3 kg , respectively ) and also experienced more treatment-emergent somnolence ( 21 patients [ 38.2 % ] vs 5 [ 8.3 % ] , respectively ) .

## Item bc5cdr:test:1517
Example input:
Sentence: Nitroglycerin has been shown to reduce ST-segment elevation during acute myocardial infarction , an effect potentiated in the dog by agents that reverse nitroglycerin-induced hypotension .

Example answer:
{"entities": [{"text": "Nitroglycerin", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}, {"text": "nitroglycerin-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Angina and ischemic electrocardiographic changes occurred after administration of oral dipyridamole in four patients awaiting urgent myocardial revascularization procedures .

Example answer:
{"entities": [{"text": "Angina", "type": "Disease"}, {"text": "dipyridamole", "type": "Chemical"}]}

Example input:
Sentence: A nonregenerative anemia was the most compromising of the cytopenias and occurred in approximately 50 % of dogs receiving 400-500 mg/kg cefonicid or 540-840 mg/kg cefazedone .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "cytopenias", "type": "Disease"}, {"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: Effect of green tea and vitamin E combination in isoproterenol induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: The animal model used to produce infarction implies artery ligation but chemical induction can be easily obtained with isoproterenol .

Example answer:
{"entities": [{"text": "infarction", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: 99mTc-glucarate for detection of isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "99mTc-glucarate", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: In four subacute toxicity studies , the intravenous administration of cefonicid or cefazedone to beagle dogs caused a dose-dependent incidence of anemia , neutropenia , and thrombocytopenia after 1-3 months of treatment .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}, {"text": "anemia", "type": "Disease"}, {"text": "neutropenia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}]}

Example input:
Sentence: To our knowledge , this has not previously been reported as a side effect of preoperative dipyridamole therapy , although dipyridamole-induced myocardial ischemia has been demonstrated to occur in animals and humans with coronary artery disease .

Example answer:
{"entities": [{"text": "dipyridamole", "type": "Chemical"}, {"text": "dipyridamole-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "coronary artery disease", "type": "Disease"}]}

Example input:
Sentence: Therefore , we studied the hyperemic response to dipyridamole in seven open-chest anesthetized dogs after pretreatment with either pentoxifylline ( 0 , 7.5 , or 15 mg/kg i.v . )

Example answer:
{"entities": [{"text": "dipyridamole", "type": "Chemical"}, {"text": "pentoxifylline", "type": "Chemical"}]}

Input:
Sentence: Effects of CD-832 on isoproterenol ( ISO ) -induced myocardial ischemia were studied in dogs with partial coronary stenosis of the left circumflex coronary artery and findings were compared with those for nifedipine or diltiazem .

## Item bc5cdr:test:2029
Example input:
Sentence: Combined antiretroviral therapy causes cardiomyopathy and elevates plasma lactate in transgenic AIDS mice .

Example answer:
{"entities": [{"text": "cardiomyopathy", "type": "Disease"}, {"text": "lactate", "type": "Chemical"}, {"text": "AIDS", "type": "Disease"}]}

Example input:
Sentence: Forty seconds after injection of suxamethonium , bradycardia and cardiac arrest occurred .

Example answer:
{"entities": [{"text": "suxamethonium", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "cardiac arrest", "type": "Disease"}]}

Example input:
Sentence: FINDINGS : A 28-year-old man suffering from idiopathic epilepsy with generalized seizures was treated with LEV ( 3000 mg ) added to valproate ( VPA ) ( 2000 mg ) .

Example answer:
{"entities": [{"text": "idiopathic epilepsy", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "LEV", "type": "Chemical"}, {"text": "valproate", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : A 72-year-old white man with underlying human immunodeficiency virus , atrial fibrillation , coronary artery disease , and hyperlipidemia presented with generalized pain , fatigue , and dark orange urine for 3 days .

Example answer:
{"entities": [{"text": "human immunodeficiency virus", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "coronary artery disease", "type": "Disease"}, {"text": "hyperlipidemia", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "fatigue", "type": "Disease"}]}

Example input:
Sentence: Iatrogenically induced intractable atrioventricular reentrant tachycardia after verapamil and catheter ablation in a patient with Wolff-Parkinson-White syndrome and idiopathic dilated cardiomyopathy .

Example answer:
{"entities": [{"text": "atrioventricular reentrant tachycardia", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "idiopathic dilated cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: We describe a patient who developed dilated cardiomyopathy and clinical congestive heart failure after 2 months of therapy with amphotericin B ( AmB ) for disseminated coccidioidomycosis .

Example answer:
{"entities": [{"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}, {"text": "AmB", "type": "Chemical"}, {"text": "coccidioidomycosis", "type": "Disease"}]}

Example input:
Sentence: Bradycardia ( defined as a decrease in heart rate to less than 50 beat min-1 ) was prevented when the larger dose of either active drug was used .

Example answer:
{"entities": [{"text": "Bradycardia", "type": "Disease"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Dose-dependent bradycardia induced by verapamil was potentiated by LNa , LCa , and HCa .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: One of the twins developed complete heart block and dilated cardiomyopathy related to lopinavir/ritonavir therapy , a boosted protease-inhibitor agent , while the other twin developed mild bradycardia .

Example answer:
{"entities": [{"text": "heart block", "type": "Disease"}, {"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "lopinavir/ritonavir", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Input:
Sentence: Bradycardia occurred in a 45-year-old male patient who was Viracept in combination with other anti-HIV drugs .

## Item bc5cdr:test:2001
Example input:
Sentence: For compounds that have shown TDP in the clinic ( terfenadine , terodiline , cisapride ) there is little differentiation between the dog ED50 and the efficacious free plasma concentrations in man ( < 10-fold ) reflecting their limited safety margins .

Example answer:
{"entities": [{"text": "TDP", "type": "Disease"}, {"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : No direct comparisons exist of the renal tolerability of the low-osmolality contrast medium iopamidol with that of the iso-osmolality contrast medium iodixanol in high-risk patients .

Example answer:
{"entities": [{"text": "contrast medium", "type": "Chemical"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}]}

Example input:
Sentence: Based on these observations , it is concluded that 5-HT2 blockade obtained with risperidone at D2 occupancy rates of 60 % and above does not appear to protect against the risk for extrapyramidal side effects .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}]}

Example input:
Sentence: Analysis was performed on 61 women with chemotherapy-responsive metastatic breast cancer receiving 96-h infusional cyclophosphamide as part of a triple sequential high-dose regimen to assess association between presence of peritransplant congestive heart failure ( CHF ) and the following pretreatment characteristics : presence of electrocardiogram ( EKG ) abnormalities , age , hypertension , prior cardiac history , smoking , diabetes mellitus , prior use of anthracyclines , and left-sided chest irradiation .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "CHF", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "diabetes mellitus", "type": "Disease"}, {"text": "anthracyclines", "type": "Chemical"}]}

Example input:
Sentence: A low incidence of cardiovascular malformations was observed after exposure to each of the four calcium channel blockers , but this incidence was statistically significant only for verapamil and nifedipine .

Example answer:
{"entities": [{"text": "cardiovascular malformations", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: METHODS AND RESULTS : The present study is a multicenter , randomized , double-blind comparison of iopamidol and iodixanol in patients with chronic kidney disease ( estimated glomerular filtration rate , 20 to 59 mL/min ) who underwent cardiac angiography or percutaneous coronary interventions .

Example answer:
{"entities": [{"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}, {"text": "chronic kidney disease", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : A previous randomized controlled trial evaluating the use of spironolactone in heart failure patients reported a low risk of hyperkalemia ( 2 % ) and renal insufficiency ( 0 % ) .

Example answer:
{"entities": [{"text": "spironolactone", "type": "Chemical"}, {"text": "heart failure", "type": "Disease"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}]}

Example input:
Sentence: In patients requiring the concurrent use of statins and CYP3A4 inhibitors , pravastatin , fluvastatin , and rosuvastatin carry the lowest risk of drug interactions ; atorvastatin carries moderate risk , whereas simvastatin and lovastatin have the highest risk and should be avoided in patients taking concomitant CYP3A4 inhibitors .

Example answer:
{"entities": [{"text": "statins", "type": "Chemical"}, {"text": "pravastatin", "type": "Chemical"}, {"text": "fluvastatin", "type": "Chemical"}, {"text": "rosuvastatin", "type": "Chemical"}, {"text": "atorvastatin", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "lovastatin", "type": "Chemical"}]}

Example input:
Sentence: Design and analysis of the HYPREN-trial : safety of enalapril and prazosin in the initial treatment phase of patients with congestive heart failure .

Example answer:
{"entities": [{"text": "enalapril", "type": "Chemical"}, {"text": "prazosin", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}]}

Example input:
Sentence: The authors present a 10-year-old boy chronically treated with lisinopril , an angiotensin converting enzyme inhibitor , to control hypertension who developed hypotension following the addition of tizanidine , an alpha-2 agonist , for the treatment of spasticity .

Example answer:
{"entities": [{"text": "lisinopril", "type": "Chemical"}, {"text": "angiotensin", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}, {"text": "tizanidine", "type": "Chemical"}, {"text": "spasticity", "type": "Disease"}]}

Input:
Sentence: The present study examines the safety and tolerability of high- compared with low-dose lisinopril in CHF .

## Item bc5cdr:test:1390
Example input:
Sentence: Mitochondrial radiocalcium uptakes were significantly decreased in animals pretreated with acetylsalicylic acid or dipyridamole or when hydrocortisone was added to the epinephrine infusion ( 2,682,2,803 , and 3,424 counts per minute per gram of dried fraction , respectively ) .

Example answer:
{"entities": [{"text": "radiocalcium", "type": "Chemical"}, {"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine", "type": "Chemical"}]}

Example input:
Sentence: A comparable overexpression of Pgp in the BBB was obtained after pilocarpine-induced seizures in wild-type Wistar rats .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: When hippocampal ACh was measured during testing for handling-induced convulsions , extracellular ACh was significantly elevated ( 192 % ) in WSP mice , but was nonsignificantly elevated ( 59 % ) in WSR mice .

Example answer:
{"entities": [{"text": "ACh", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}]}

Example input:
Sentence: THP exhibited an antipsychotic-like profile by potentiating haloperidol-induced catalepsy , reducing amphetamine-induced hyperactivity and reducing apomorphine-induced climbing in mice .

Example answer:
{"entities": []}

Example input:
Sentence: Climbing behavior induced by apomorphine was reduced in animals treated with THP .

Example answer:
{"entities": []}

Example input:
Sentence: Therefore , like VPA , the finding that VPU could drastically reduce pilocarpine-induced increases in glutamate and aspartate should account , at least partly , for its anticonvulsant activity observed in pilocarpine-induced seizure in experimental animals .

Example answer:
{"entities": [{"text": "VPA", "type": "Chemical"}, {"text": "VPU", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: The administration of ephedrine led to a similar increase in MAP ( 53 +/- 9 to 79 +/- 8 mmHg ; P < 0.001 ) , restored CO ( 3.2 +/- 1.2 to 5.0 +/- 1.3 l min ( -1 ) ) , and preserved S ( c ) O ( 2 ) .

Example answer:
{"entities": [{"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: However , the increase in release of ACh produced by the first application of KCl was 2-fold higher in WSP versus WSR mice .

Example answer:
{"entities": [{"text": "ACh", "type": "Chemical"}, {"text": "KCl", "type": "Chemical"}]}

Example input:
Sentence: Pretreatment with either VPU ( 50 and 100 mg/kg ) or VPA ( 300 and 600 mg/kg ) completely abolished pilocarpine-evoked increases in extracellular glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-evoked", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: After administration of phenylephrine , MAP increased ( 51 +/- 12 to 81 +/- 13 mmHg ; P < 0.001 ; mean +/- SD ) .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}]}

Input:
Sentence: In SHR but not in WKY administration of ANP , AVP and ANP + AVP decreased CCB during Phe-induced MAP elevation .

## Item bc5cdr:test:2008
Example input:
Sentence: Maximum tolerated dose in good-risk patients was 70 mg/m2 , and in poor-risk patients , 60 mg/m2 .

Example answer:
{"entities": []}

Example input:
Sentence: In the bolus group , 26.0 % ( 13/50 ) had akathisia compared with 32.7 % ( 16/49 ) in the infusion group ( Delta=-6.7 % ; 95 % confidence interval [ CI ] -24.6 % to 11.2 % ) .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: It is therefore suggested that caution should be exercised when prescribing vasodilator drugs in diabetic patients , particularly those with autonomic neuropathy .

Example answer:
{"entities": [{"text": "diabetic", "type": "Disease"}, {"text": "autonomic neuropathy", "type": "Disease"}]}

Example input:
Sentence: Patients who developed hyperkalemia were older and more likely to have diabetes , had higher baseline serum potassium levels and lower baseline potassium supplement doses , and were more likely to be treated with beta-blockers than controls ( n = 134 ) .

Example answer:
{"entities": [{"text": "hyperkalemia", "type": "Disease"}, {"text": "diabetes", "type": "Disease"}, {"text": "potassium", "type": "Chemical"}]}

Example input:
Sentence: Patients were divided into three groups : Controls , no CRF or ESRD , n=748 ; CRF , sustained serum creatinine > 2.5 mg/dl , n=41 ; and ESRD , n=45 .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: Since the introduction of angiotensin converting enzyme ( ACE ) inhibitors into the adjunctive treatment of patients with congestive heart failure , cases of severe hypotension , especially on the first day of treatment , have occasionally been reported .

Example answer:
{"entities": [{"text": "angiotensin converting enzyme ( ACE ) inhibitors", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: The estimated incidence of angioedema during angiotensin-converting enzyme ( ACE ) inhibitor treatment is between 1 and 7 per thousand patients .

Example answer:
{"entities": [{"text": "angioedema", "type": "Disease"}, {"text": "angiotensin-converting enzyme ( ACE ) inhibitor", "type": "Chemical"}]}

Example input:
Sentence: Mean post-SCr increases were significantly less with iopamidol ( all patients : 0.07 versus 0.12 mg/dL , 6.2 versus 10.6 micromol/L , P=0.03 ; patients with diabetes : 0.07 versus 0.16 mg/dL , 6.2 versus 14.1 micromol/L , P=0.01 ) .

Example answer:
{"entities": [{"text": "iopamidol", "type": "Chemical"}, {"text": "diabetes", "type": "Disease"}]}

Example input:
Sentence: Based on this principle a 27-year old woman , classified as being in the high-risk group ( Goldstein and Berkowitz score : 11 ) , was treated with multiple cytotoxic drugs .

Example answer:
{"entities": []}

Example input:
Sentence: In patients with diabetes , SCr increases > or = 0.5 mg/dL were 5.1 % ( 4 of 78 patients ) with iopamidol and 13.0 % ( 12 of 92 patients ) with iodixanol ( P=0.11 ) , whereas SCr increases > or = 25 % were 10.3 % and 15.2 % , respectively ( P=0.37 ) .

Example answer:
{"entities": [{"text": "diabetes", "type": "Disease"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}]}

Input:
Sentence: Subgroups presumed to be at higher risk for ACE inhibitor intolerance ( blood pressure , < 120 mm Hg ; creatinine , > or =132.6 micromol/L [ > or =1.5 mg/dL ] ; age , > or =70 years ; and patients with diabetes ) generally tolerated the high-dose strategy .

## Item bc5cdr:test:2177
Example input:
Sentence: Male SD rats ( n = 30 ) were treated with Ato ( 50 mg/kg per day in drinking water ) or tap water for 15 days .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}]}

Example input:
Sentence: Rats were treated with seven day intravenous infusion of fucoidan ( 30 micrograms h-1 ) or vehicle .

Example answer:
{"entities": [{"text": "fucoidan", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Neonatal rats were treated with the tricyclic antidepressant clomipramine or vehicle between days 9 and 16 twice daily and behaviorally tested in adulthood .

Example answer:
{"entities": [{"text": "antidepressant", "type": "Chemical"}, {"text": "clomipramine", "type": "Chemical"}]}

Example input:
Sentence: Male Sprague-Dawley rats were treated with D-penicillamine ( D-pen ) 500 mg/kg/day for 10 or 42 days .

Example answer:
{"entities": [{"text": "D-penicillamine", "type": "Chemical"}, {"text": "D-pen", "type": "Chemical"}]}

Example input:
Sentence: Streptomycin sulfate ( 300 mg/kg s.c. ) was injected for various periods into preweanling rats and for 3 weeks into weanling rats .

Example answer:
{"entities": [{"text": "Streptomycin", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Thirty-five Wistar rats were given 1.5 mg/kg DOX , i.v. , weekly for up to 8 weeks for a total cumulative dose of 12 mg/kg BW .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: Pregnant rats were given either vehicle or 2 daily intraperitoneal injections of dexamethasone ( 0.2 mg/kg body weight ) on gestational days 11 and 12 , 13 and 14 , 15 and 16 , 17 and 18 , or 19 and 20 .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Drugs were separately , orally once daily dosed to pregnant rats from day 8 to 21 ( GD1=plug day ) .

Example answer:
{"entities": []}

Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "Chemical"}, {"text": "Ato-treated", "type": "Chemical"}]}

Example input:
Sentence: Newborn rats were given terbutaline ( 10 mg/kg ) daily on postnatal days ( PN ) 2 to 5 or PN 11 to 14 and examined 24 h after the last dose and at PN 30 .

Example answer:
{"entities": [{"text": "terbutaline", "type": "Chemical"}]}

Input:
Sentence: Temocapril ( 8 mg/kg/day ) was administered to the rats which were killed at weeks 4 , 14 or 20 .

## Item bc5cdr:test:2129
Example input:
Sentence: Depression is a major clinical feature of Parkinson 's disease .

Example answer:
{"entities": [{"text": "Depression", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : The United Kingdom Parkinson 's Disease Research Group ( UKPDRG ) trial found an increased mortality in patients with Parkinson 's disease ( PD ) randomized to receive 10 mg selegiline per day and L-dopa compared with those taking L-dopa alone .

Example answer:
{"entities": [{"text": "Parkinson 's Disease", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "selegiline", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}]}

Example input:
Sentence: Seven patients suffering from Parkinson 's disease ( PD ) with severely disabling dyskinesia received low-dose propranolol as an adjunct to the currently used medical treatment .

Example answer:
{"entities": [{"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "propranolol", "type": "Chemical"}]}

Example input:
Sentence: Treatment with 150 mg/kg PDTC before and following status epilepticus significantly increased the mortality rate to 100 % .

Example answer:
{"entities": [{"text": "PDTC", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}]}

Example input:
Sentence: METHODS : All PD patients in the Amiens area treated with pergolide were invited to attend a cardiologic assessment including transthoracic echocardiography .

Example answer:
{"entities": [{"text": "PD", "type": "Disease"}, {"text": "pergolide", "type": "Chemical"}]}

Example input:
Sentence: Low-dose PDTC treatment almost completely protected from lesions in the piriform cortex .

Example answer:
{"entities": [{"text": "PDTC", "type": "Chemical"}]}

Example input:
Sentence: No statistically significant changes in behavior or receptor binding were found in PD males with the exception of increased ( 3 ) H-MK-801 binding in cortex .

Example answer:
{"entities": [{"text": "H-MK-801", "type": "Chemical"}]}

Example input:
Sentence: However , future investigations are necessary to exactly analyze the biochemical mechanisms by which PDTC exerted its beneficial effects in the piriform cortex .

Example answer:
{"entities": [{"text": "PDTC", "type": "Chemical"}]}

Example input:
Sentence: The effect of PDTC on status epilepticus-associated cell loss in the hippocampus and piriform cortex was evaluated in the rat fractionated pilocarpine model .

Example answer:
{"entities": [{"text": "PDTC", "type": "Chemical"}, {"text": "status", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: The most important findings were that compared with values in control subjects , end-systolic left ventricular posterior wall dimension and percent of left ventricular posterior wall thickening in doxorubicin-treated patients were decreased at baseline study and these findings were more clearly delineated with dobutamine stimulation .

Example answer:
{"entities": [{"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}]}

Input:
Sentence: The relevance of these features for patients using PDN remains to be elucidated .

## Item bc5cdr:test:2083
Example input:
Sentence: Prenatal exposure to selective COX-2 inhibitors does not increase the risk of ventricular septal and midline defects in rat when compared to non-selective drugs and historic control .

Example answer:
{"entities": []}

Example input:
Sentence: Eleven of the cocaine abusers and none of the controls had ECG evidence of significant myocardial injury defined as myocardial infarction , ischemia , and bundle branch block .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "myocardial injury", "type": "Disease"}, {"text": "myocardial infarction", "type": "Disease"}, {"text": "ischemia", "type": "Disease"}, {"text": "bundle branch block", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : Given its preclinical success for treating substance abuse and the increased risk of visual field defects ( VFD ) associated with cumulative lifetime exposure , we explored the effects of sub-chronic low dose GVG on cocaine-induced increases in nucleus accumbens ( NAcc ) dopamine ( DA ) .

Example answer:
{"entities": [{"text": "substance abuse", "type": "Disease"}, {"text": "visual field defects", "type": "Disease"}, {"text": "VFD", "type": "Disease"}, {"text": "GVG", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: The present study was designed to evaluate two endogenous and one synthetic neuroactive steroid that positively modulate the gamma-aminobutyric acid ( GABA ( A ) ) receptor against the increase in sensitivity to the convulsant effects of cocaine engendered by repeated cocaine administration ( seizure kindling ) .

Example answer:
{"entities": [{"text": "steroid", "type": "Chemical"}, {"text": "gamma-aminobutyric acid", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Mature male and female mice from six inbred stains were tested for susceptibility to behavioral seizures induced by a single injection of cocaine .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Prenatal exposure to non-selective COX inhibitors increases the risk of VSD and MD when compared to historic control but not with selective COX-2 inhibitors .

Example answer:
{"entities": []}

Example input:
Sentence: With regard to spasm , the clinical findings are largely circumstantial , and the locus of cocaine-induced vasoconstriction remains speculative .

Example answer:
{"entities": [{"text": "spasm", "type": "Disease"}, {"text": "cocaine-induced", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVE : The outcome of subarachnoid hemorrhage associated with cocaine abuse is reportedly poor .

Example answer:
{"entities": [{"text": "subarachnoid hemorrhage", "type": "Disease"}, {"text": "cocaine abuse", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : Cocaine use predisposed aneurysmal rupture at a significantly earlier age and in much smaller aneurysms .

Example answer:
{"entities": [{"text": "Cocaine", "type": "Chemical"}, {"text": "aneurysmal rupture", "type": "Disease"}, {"text": "aneurysms", "type": "Disease"}]}

Example input:
Sentence: A 45-year-old man , an admitted frequent cocaine user , presented to the Emergency Department ( ED ) on two separate occasions with a history of priapism after cocaine use .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "priapism", "type": "Disease"}]}

Input:
Sentence: We sought to determine if prenatal cocaine exposure increases the incidence of subependymal cysts in preterm infants .

## Item bc5cdr:test:1381
Example input:
Sentence: The effects of varying the extracellular concentrations of Na and Ca ( [ Na ] o and [ Ca ] o ) on both , the spontaneous beating and the negative chronotropic action of verapamil , were studied in the isolated rat atria .

Example answer:
{"entities": [{"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: TR ( - ) rats exhibited a significant up-regulation of Pgp in brain capillary endothelial cells compared with wild-type controls .

Example answer:
{"entities": []}

Example input:
Sentence: The [ verapamil ] o that arrested atrial beating ( AC ) was also potentiated with the order LNa = LNa+LCa = LNa+HCa = LCa > HCa = N. The results indicate that rat atrial spontaneous beating is more dependent on [ Na ] o than on [ Ca ] o in a range of +/- 50 % of their normal concentration .

Example answer:
{"entities": [{"text": "verapamil", "type": "Chemical"}, {"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}]}

Example input:
Sentence: Application of a delayed feedback signal , in the form of a 2-h systemic corticosterone infusion in urethane-anesthetized rats with pharmacological blockade of glucocorticoid synthesis , is without effect on the resting secretion of arginine vasopressin and oxytocin at any corticosterone feedback dose tested .

Example answer:
{"entities": [{"text": "corticosterone", "type": "Chemical"}, {"text": "urethane-anesthetized", "type": "Chemical"}, {"text": "arginine vasopressin", "type": "Chemical"}, {"text": "oxytocin", "type": "Chemical"}]}

Example input:
Sentence: Six weeks after clipping of one renal artery , hypertensive rats ( 178 +/- 4 mm Hg ) were randomly assigned to three groups : untreated hypertensive controls ( n = 8 ) , enalapril-treated ( n = 8 ) , or nitrendipine-treated ( n = 10 ) .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}, {"text": "enalapril-treated", "type": "Chemical"}, {"text": "nitrendipine-treated", "type": "Chemical"}]}

Example input:
Sentence: In the present study , we investigated whether 50 mg/kg per day , p.o. , Ato could prevent endothelial NO synthase ( eNOS ) downregulation and the increase in O2- in Sprague-Dawley ( SD ) rats , thereby reducing blood pressure .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}, {"text": "O2-", "type": "Chemical"}]}

Example input:
Sentence: In unanesthetized , spontaneously hypertensive rats the decrease in blood pressure and heart rate produced by intravenous clonidine , 5 to 20 micrograms/kg , was inhibited or reversed by nalozone , 0.2 to 2 mg/kg .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}, {"text": "clonidine", "type": "Chemical"}, {"text": "nalozone", "type": "Chemical"}]}

Example input:
Sentence: These results suggest that dehydration and/or the activation of visceral afferent inputs may contribute to the elevation of plasma AVP and the upregulation of AVP gene expression in the PVN and the SON of the Li-induced diabetes insipidus rat .

Example answer:
{"entities": [{"text": "dehydration", "type": "Disease"}, {"text": "AVP", "type": "Chemical"}, {"text": "Li-induced", "type": "Chemical"}, {"text": "diabetes insipidus", "type": "Disease"}]}

Example input:
Sentence: Following discontinuation of SNP , blood pressure in the control animals rebounded to 94 torr , as compared with 78 torr in the saralasin-treated rats .

Example answer:
{"entities": [{"text": "SNP", "type": "Chemical"}, {"text": "saralasin-treated", "type": "Chemical"}]}

Example input:
Sentence: The expression of arginine vasopressin ( AVP ) gene in the paraventricular ( PVN ) and supraoptic nuclei ( SON ) was investigated in rats with lithium ( Li ) -induced polyuria , using in situ hybridization histochemistry and radioimmunoassay .

Example answer:
{"entities": [{"text": "arginine vasopressin", "type": "Chemical"}, {"text": "AVP", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "Li", "type": "Chemical"}, {"text": "polyuria", "type": "Disease"}]}

Input:
Sentence: The purpose of the present study was to compare influence of central arginine vasopressin ( AVP ) and of atrial natriuretic peptide ( ANP ) on control of arterial blood pressure ( MAP ) and heart rate ( HR ) in normotensive ( WKY ) and spontaneously hypertensive ( SHR ) rats .

## Item bc5cdr:test:2027
Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: The pooled statistical analysis for ventricular septal ( VSD ) and midline ( MD ) defects was performed for rat fetuses exposed to piroxicam , selective and non-selective COX-2 inhibitor based on present and historic data .

Example answer:
{"entities": [{"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: glycopyrrolate and atropine in the prevention of bradycardia and arrhythmias following repeated doses of suxamethonium in children .

Example answer:
{"entities": [{"text": "glycopyrrolate", "type": "Chemical"}, {"text": "atropine", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "arrhythmias", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: In a patient with WPW syndrome and idiopathic dilated cardiomyopathy , intractable atrioventricular reentrant tachycardia ( AVRT ) was iatrogenically induced .

Example answer:
{"entities": [{"text": "WPW syndrome", "type": "Disease"}, {"text": "idiopathic dilated cardiomyopathy", "type": "Disease"}, {"text": "atrioventricular reentrant tachycardia", "type": "Disease"}, {"text": "AVRT", "type": "Disease"}]}

Example input:
Sentence: The administration of intermittent intravenous infusions of cimetidine is infrequently associated with the development of bradyarrhythmias .

Example answer:
{"entities": [{"text": "cimetidine", "type": "Chemical"}, {"text": "bradyarrhythmias", "type": "Disease"}]}

Example input:
Sentence: A low incidence of cardiovascular malformations was observed after exposure to each of the four calcium channel blockers , but this incidence was statistically significant only for verapamil and nifedipine .

Example answer:
{"entities": [{"text": "cardiovascular malformations", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: One of the twins developed complete heart block and dilated cardiomyopathy related to lopinavir/ritonavir therapy , a boosted protease-inhibitor agent , while the other twin developed mild bradycardia .

Example answer:
{"entities": [{"text": "heart block", "type": "Disease"}, {"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "lopinavir/ritonavir", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: QRS without preexcitation , caused by junctional escape beats after verapamil or unidirectional antegrade block of accessory pathway after catheter ablation , established frequent AVRT attack .

Example answer:
{"entities": [{"text": "verapamil", "type": "Chemical"}, {"text": "AVRT", "type": "Disease"}]}

Example input:
Sentence: Iatrogenically induced intractable atrioventricular reentrant tachycardia after verapamil and catheter ablation in a patient with Wolff-Parkinson-White syndrome and idiopathic dilated cardiomyopathy .

Example answer:
{"entities": [{"text": "atrioventricular reentrant tachycardia", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "idiopathic dilated cardiomyopathy", "type": "Disease"}]}

Input:
Sentence: Viracept and irregular heartbeat warning .

## Item bc5cdr:test:2391
Example input:
Sentence: At termination of the experiments , mice underwent echocardiography , quantitation of abundance of molecular markers of CM ( ventricular mRNA encoding atrial natriuretic factor [ ANF ] and sarcoplasmic calcium ATPase [ SERCA2 ] ) , and determination of plasma LA .

Example answer:
{"entities": [{"text": "CM", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "LA", "type": "Chemical"}]}

Example input:
Sentence: There was a significant reduction of thymidine incorporation into both erythroid and endothelial cells in cultures pre-treated with IGF-IL-3 and EPO .

Example answer:
{"entities": [{"text": "thymidine", "type": "Chemical"}]}

Example input:
Sentence: The serum level of potassium was observed to be 8.4 mequiv L-1 .

Example answer:
{"entities": [{"text": "potassium", "type": "Chemical"}]}

Example input:
Sentence: The initiated hepatocytes in the liver were assayed as the gamma-glutamyltransferase ( gamma-GT ) positive foci formed following a 2-week selection regimen consisting of dietary 0.02 % 2-acetylaminofluorene coupled with a necrogenic dose of CCl4 .

Example answer:
{"entities": [{"text": "2-acetylaminofluorene", "type": "Chemical"}, {"text": "CCl4", "type": "Chemical"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: The blood amounts and hematoma volumes were significantly correlated , and the hematoma induced by 0.014-unit collagenase was adequate to detect ICH deterioration .

Example answer:
{"entities": [{"text": "hematoma", "type": "Disease"}, {"text": "ICH", "type": "Disease"}]}

Example input:
Sentence: The relative amounts of alphaENaC , betaENaC and gammaENaC mRNAs were determined in kidneys from these rats by real-time quantitative TaqMan PCR , and the amounts of proteins by Western blot .

Example answer:
{"entities": []}

Example input:
Sentence: The serum of six affected workers and five controls was tested for autoantibodies that react with human liver cytochrome-P450 2E1 ( P450 2E1 ) and P58 protein disulphide isomerase isoform ( P58 ) .

Example answer:
{"entities": []}

Example input:
Sentence: In contrast with the literature , serum levels of angiogenesis factors did not change significantly by pegylated interferon and ribavirin therapy .

Example answer:
{"entities": [{"text": "pegylated interferon", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: Plasma TAFI , tPA , and PAI-1 antigen levels were measured at baseline and after 3 months of treatment by commercially available ELISA kits .

Example answer:
{"entities": []}

Input:
Sentence: Serum levels of tumor necrosis factor-alpha and interferon-gamma were also determined by ELISA .

## Item bc5cdr:test:2090
Example input:
Sentence: We observed the exencephaly induced by 5-azacytidine at embryonic day 13.5 ( E13.5 ) , let the embryos develop exo utero until E18.5 , and re-observed the same embryos at E18.5 .

Example answer:
{"entities": [{"text": "exencephaly", "type": "Disease"}, {"text": "5-azacytidine", "type": "Chemical"}]}

Example input:
Sentence: Eleven of the cocaine abusers and none of the controls had ECG evidence of significant myocardial injury defined as myocardial infarction , ischemia , and bundle branch block .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "myocardial injury", "type": "Disease"}, {"text": "myocardial infarction", "type": "Disease"}, {"text": "ischemia", "type": "Disease"}, {"text": "bundle branch block", "type": "Disease"}]}

Example input:
Sentence: The finding of cocaine-induced vasoconstriction in segments of ( noninnervated ) human umbilical artery suggests that the presence or absence of intact innervation is not sufficient to explain the discrepant data involving the possibility of alpha-mediated effects .

Example answer:
{"entities": [{"text": "cocaine-induced", "type": "Chemical"}]}

Example input:
Sentence: Mature male and female mice from six inbred stains were tested for susceptibility to behavioral seizures induced by a single injection of cocaine .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Sub-chronic GVG exposure inhibited the effect of cocaine for 3 days , which exceeded in magnitude and duration the identical acute dose .

Example answer:
{"entities": [{"text": "GVG", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Progressive abstinence from cocaine was associated with worsening of all measured polysomnographic sleep outcomes .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: With regard to spasm , the clinical findings are largely circumstantial , and the locus of cocaine-induced vasoconstriction remains speculative .

Example answer:
{"entities": [{"text": "spasm", "type": "Disease"}, {"text": "cocaine-induced", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVE : The outcome of subarachnoid hemorrhage associated with cocaine abuse is reportedly poor .

Example answer:
{"entities": [{"text": "subarachnoid hemorrhage", "type": "Disease"}, {"text": "cocaine abuse", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : Cocaine use predisposed aneurysmal rupture at a significantly earlier age and in much smaller aneurysms .

Example answer:
{"entities": [{"text": "Cocaine", "type": "Chemical"}, {"text": "aneurysmal rupture", "type": "Disease"}, {"text": "aneurysms", "type": "Disease"}]}

Example input:
Sentence: A 45-year-old man , an admitted frequent cocaine user , presented to the Emergency Department ( ED ) on two separate occasions with a history of priapism after cocaine use .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "priapism", "type": "Disease"}]}

Input:
Sentence: CONCLUSIONS : We found an increased incidence of subependymal cyst formation in preterm infants who were exposed to cocaine prenatally .

## Item bc5cdr:test:2406
Example input:
Sentence: Decompression and neurolysis were performed with good subsequent recovery of function .

Example answer:
{"entities": []}

Example input:
Sentence: Similarly , significant improvements in memory scores were observed using passive avoidance apparatus and aged mice .

Example answer:
{"entities": []}

Example input:
Sentence: Accumulation of drugs was not reflected in prolonged behavioral impairment .

Example answer:
{"entities": [{"text": "behavioral impairment", "type": "Disease"}]}

Example input:
Sentence: They showed significantly more rapid improvement of motor function in the first week following hemorrhage and better memory retention in the passive avoidance test .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "Disease"}]}

Example input:
Sentence: There was a significant increase in CBF , although CMRO2 was unchanged , compared with pre-hypotensive values .

Example answer:
{"entities": []}

Example input:
Sentence: Health , physical abilities and cognitive function were compared between BZD/RD users and non-users , and adjustments were made for confounding variables .

Example answer:
{"entities": []}

Example input:
Sentence: For almost all cognitive measures , there were no medication by age-interaction effects , which indicates that the 2 age groups exhibited similar responses to the medication challenge .

Example answer:
{"entities": []}

Example input:
Sentence: Passive avoidance paradigm and elevated plus maze test were used to assess cognitive function .

Example answer:
{"entities": []}

Example input:
Sentence: Significant declines in simple and sustained attention , working memory , and verbal memory were observed at 1 hour postdose compared to baseline for both age groups with a trend toward return to baseline by 5 hours postdose .

Example answer:
{"entities": []}

Example input:
Sentence: After adjustment for these variables as confounders , use of BZDs/RDs was not associated with cognitive function as measured by the MMSE .

Example answer:
{"entities": [{"text": "BZDs/RDs", "type": "Chemical"}]}

Input:
Sentence: The cognitive functions remained unchanged .

## Item bc5cdr:test:1769
Example input:
Sentence: Ovx significantly enhanced the hypotensive response to alpha-methyldopa , in contrast to no effect on rilmenidine hypotension .

Example answer:
{"entities": [{"text": "hypotensive", "type": "Disease"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "rilmenidine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Controlled hypotension in groups A and C was induced with PGE1 to maintain mean arterial blood pressure at 55 mmHg for 180 min .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "PGE1", "type": "Chemical"}]}

Example input:
Sentence: In addition , reflex bradycardia caused by injected norepinephrine was significantly enhanced by L-dopa , DL-Threo-dihydroxyphenylserine had no effect on blood pressure , heart rate or reflex responses to norepinephrine .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}, {"text": "DL-Threo-dihydroxyphenylserine", "type": "Chemical"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: We describe the effect of phenylephrine and ephedrine on frontal lobe oxygenation ( S ( c ) O ( 2 ) ) following anesthesia-induced hypotension .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "ephedrine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Bromocriptine-induced hypotension was unaffected by isoproterenol pretreatment , while tachycardia was reversed to significant bradycardia , an effect that was partly reduced by i.v .

Example answer:
{"entities": [{"text": "Bromocriptine-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Combined effects of prolonged prostaglandin E1-induced hypotension and haemodilution on human hepatic function .

Example answer:
{"entities": [{"text": "prostaglandin", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}]}

Example input:
Sentence: During HEM-induced hypotension the cardiac output was significantly lower and systemic vascular resistance higher compared with that in the SNP group .

Example answer:
{"entities": [{"text": "HEM-induced", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: Phenylephrine but not ephedrine reduces frontal lobe oxygenation following anesthesia-induced hypotension .

Example answer:
{"entities": [{"text": "Phenylephrine", "type": "Chemical"}, {"text": "ephedrine", "type": "Chemical"}, {"text": "reduces frontal lobe oxygenation", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : The utilization of phenylephrine to correct hypotension induced by anesthesia has a negative impact on S ( c ) O ( 2 ) while ephedrine maintains frontal lobe oxygenation potentially related to an increase in CO .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "ephedrine", "type": "Chemical"}]}

Input:
Sentence: Oxyhemoglobin did not affect helodermin-induced hypotension , whereas it shortened the duration of acetylcholine ( ACh ) -produced hypotension .

## Item bc5cdr:test:2404
Example input:
Sentence: The systolic pressure variation ( SPV ) , which is the difference between the maximal and minimal values of the systolic blood pressure ( SBP ) after one positive-pressure breath , was studied in ventilated dogs subjected to hypotension .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: However , a 14 % ( from 70 +/- 8 % to 60 +/- 7 % ) reduction in S ( c ) O ( 2 ) ( P < 0.05 ) followed with no change in CO ( 3.7 +/- 1.1 to 3.4 +/- 0.9 l min ( -1 ) ) .

Example answer:
{"entities": []}

Example input:
Sentence: The delta down , which is the measure of decrease of SBP after a mechanical breath , was 20.3 +/- 8.4 and 10.1 +/- 3.8 mm Hg in the HEM and SNP groups , respectively , during hypotension ( P less than 0.02 ) .

Example answer:
{"entities": [{"text": "HEM", "type": "Disease"}, {"text": "SNP", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: 5-HTP ( 5 mg/kg i.v . )

Example answer:
{"entities": [{"text": "5-HTP", "type": "Chemical"}]}

Example input:
Sentence: The area under the curve was 537 +/- 149 ng/ml x hours , volume of distribution ( Vd ) 3504 +/- 644 l/m2 , and total clearance ( ClT ) was 204 + 39.3 l/hour/m2 .

Example answer:
{"entities": []}

Example input:
Sentence: Results showed that SSR103800 ( 10-30 mg/kg p.o . )

Example answer:
{"entities": [{"text": "SSR103800", "type": "Chemical"}]}

Example input:
Sentence: 60 min : 30 +/- 7.5 ml/100 g/min ( P < 0.05 ) ) .

Example answer:
{"entities": []}

Example input:
Sentence: 30 min : 32.3 +/- 9.9 ml/100 g/min ( P < 0.05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: The study was designed to have a power of greater than 0.90 to detect a slowing to 25 % of the expected rate of progression of weakness at P less than 0.05 .

Example answer:
{"entities": [{"text": "weakness", "type": "Disease"}]}

Example input:
Sentence: pentoxifylline ( p less than 0.002 ) .

Example answer:
{"entities": [{"text": "pentoxifylline", "type": "Chemical"}]}

Input:
Sentence: ( p < 0.0005 ) .

## Item bc5cdr:test:2103
Example input:
Sentence: The underlying mechanism causing the neuropathy is not yet fully known , although some evidence indicates that it may be a lipid storage process .

Example answer:
{"entities": [{"text": "neuropathy", "type": "Disease"}]}

Example input:
Sentence: Diabetes mellitus was the major cause of autonomic neuropathy .

Example answer:
{"entities": [{"text": "Diabetes mellitus", "type": "Disease"}, {"text": "autonomic neuropathy", "type": "Disease"}]}

Example input:
Sentence: Migraine ( 20 % ) was not an uncommon cause of cranial neuropathy although malignancies arising from the reticuloendothelial system or related structures of the head and neck were more frequent ( 26 % ) .

Example answer:
{"entities": [{"text": "Migraine", "type": "Disease"}, {"text": "cranial neuropathy", "type": "Disease"}, {"text": "malignancies", "type": "Disease"}]}

Example input:
Sentence: Peripheral neuropathy due to nutritional deficiency of thiamine and riboflavin was common ( 10.1 % ) and presented mainly as sensory and sensori-motor neuropathy .

Example answer:
{"entities": [{"text": "Peripheral neuropathy", "type": "Disease"}, {"text": "nutritional deficiency", "type": "Disease"}, {"text": "thiamine", "type": "Chemical"}, {"text": "riboflavin", "type": "Chemical"}, {"text": "sensori-motor neuropathy", "type": "Disease"}]}

Example input:
Sentence: A 49-year-old woman was transferred to our department because of quadriparesis , lancinating pain , sensory loss , and paresthesia of the distal limbs .

Example answer:
{"entities": [{"text": "quadriparesis", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "sensory loss", "type": "Disease"}, {"text": "paresthesia", "type": "Disease"}]}

Example input:
Sentence: Peripheral neuropathy has been noted as a complication of therapy with perhexiline maleate , a drug widely used in France ( and in clinical trials in the United States ) for the prophylactic treatment of angina pectoris .

Example answer:
{"entities": [{"text": "Peripheral neuropathy", "type": "Disease"}, {"text": "perhexiline maleate", "type": "Chemical"}, {"text": "angina pectoris", "type": "Disease"}]}

Example input:
Sentence: Peripheral neuropathy occurred in 12 patients and pancreatitis in six .

Example answer:
{"entities": [{"text": "Peripheral neuropathy", "type": "Disease"}, {"text": "pancreatitis", "type": "Disease"}]}

Example input:
Sentence: The full syndrome of subacute myelo-optic neuropathy was more frequent in women , but they tended to have taken greater quantities of the drug .

Example answer:
{"entities": []}

Example input:
Sentence: Isoniazid was the most frequent agent in drug-induced neuropathy .

Example answer:
{"entities": [{"text": "Isoniazid", "type": "Chemical"}, {"text": "neuropathy", "type": "Disease"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Input:
Sentence: Neuropathy may thus be a common complication of thalidomide in older patients .

## Item bc5cdr:test:1770
Example input:
Sentence: It has been shown that bromocriptine-induced tachycardia , which persisted after adrenalectomy , is ( i ) mediated by central dopamine D2 receptor activation and ( ii ) reduced by 5-day isoproterenol pretreatment , supporting therefore the hypothesis that this effect is dependent on sympathetic outflow to the heart .

Example answer:
{"entities": [{"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: Atherosclerosis could produce gastric hemorrhagic ulcer via aggravation of gastric acid back-diffusion , LPO generation , histamine release and microvascular permeability that could be ameliorated by verapamil in rats .

Example answer:
{"entities": [{"text": "Atherosclerosis", "type": "Disease"}, {"text": "gastric hemorrhagic", "type": "Disease"}, {"text": "ulcer", "type": "Disease"}, {"text": "histamine", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: To assess the molecular basis of disturbances in transmembraneous transport of Na+ , we studied the response of cardiac ( Na , K ) -ATPase to NO-deficient hypertension induced in rats by NO-synthase inhibition with 40 mg/kg/day N ( G ) -nitro-L-arginine methyl ester ( L-NAME ) for 4 four weeks .

Example answer:
{"entities": [{"text": "Na+", "type": "Chemical"}, {"text": "Na", "type": "Chemical"}, {"text": "K", "type": "Chemical"}, {"text": "NO-deficient", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "NO-synthase", "type": "Chemical"}, {"text": "N ( G ) -nitro-L-arginine methyl ester", "type": "Chemical"}, {"text": "L-NAME", "type": "Chemical"}]}

Example input:
Sentence: In Mg ( 2+ ) -free bathing medium containing bicuculline , conditions designed to increase excitability in the slices , electrical stimulation of the hilus resulted in a single population spike in granule cells from control mice and pilocarpine-treated mice that did not experience SE .

Example answer:
{"entities": [{"text": "Mg", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "pilocarpine-treated", "type": "Chemical"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Heparan sulphate-associated anionic sites in the glomerular basement membrane were studied in rats 8 months after induction of diabetes by streptozotocin and in age- adn sex-matched control rats , employing the cationic dye cuprolinic blue .

Example answer:
{"entities": [{"text": "Heparan", "type": "Chemical"}, {"text": "diabetes", "type": "Disease"}, {"text": "streptozotocin", "type": "Chemical"}, {"text": "cuprolinic blue", "type": "Chemical"}]}

Example input:
Sentence: Phenylephrine infusion increased arterial pressure , arteriolar diameter and clearance of fluorescent dextran by a similar magnitude in both groups .

Example answer:
{"entities": [{"text": "Phenylephrine", "type": "Chemical"}, {"text": "dextran", "type": "Chemical"}]}

Example input:
Sentence: During HEM-induced hypotension the cardiac output was significantly lower and systemic vascular resistance higher compared with that in the SNP group .

Example answer:
{"entities": [{"text": "HEM-induced", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: Clonidine inhibited the native pacemaker current ( I ( f ) ) in isolated sinoatrial node pacemaker cells and the I ( f ) -generating hyperpolarization-activated cyclic nucleotide-gated ( HCN ) 2 and HCN4 channels in transfected HEK293 cells .

Example answer:
{"entities": [{"text": "Clonidine", "type": "Chemical"}, {"text": "cyclic", "type": "Chemical"}]}

Example input:
Sentence: Nitroprusside-induced hypotension evokes ACTH secretion which is primarily mediated by enhanced secretion of immunoreactive corticotropin-releasing factor ( irCRF ) into the hypophysial-portal circulation .

Example answer:
{"entities": [{"text": "Nitroprusside-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: While contractions to carbachol and ATP were the same in inflamed and in control strips when related to a reference potassium response , isoprenaline-induced relaxations were smaller in inflamed strips .

Example answer:
{"entities": [{"text": "carbachol", "type": "Chemical"}, {"text": "ATP", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}, {"text": "isoprenaline-induced", "type": "Chemical"}]}

Input:
Sentence: These findings suggest that helodermin-produced hypotension is partly attributable to the activation of glibenclamide-sensitive K+ channels ( K ( ATP ) channels ) , which presumably exist on arterial smooth muscle cells .

## Item bc5cdr:test:2416
Example input:
Sentence: The patient 's ophthalmological symptoms improved rapidly 3 weeks after discontinuation of pegylated IFN alpha-2b and ribavirin .

Example answer:
{"entities": [{"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: Twenty-four patients with recurrent Grade I to IV astrocytomas , whose resection and irradiation therapy had failed , received two to eight courses of intra-arterial BCNU therapy .

Example answer:
{"entities": [{"text": "astrocytomas", "type": "Disease"}, {"text": "BCNU", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : This case started with a media report in a popular newspaper , initiated by published , peer-reviewed research on herbals , and involved human failure in a case history , medical examination and clinical treatment .

Example answer:
{"entities": []}

Example input:
Sentence: She subsequently died some 5 weeks after the commencement of her drug therapy.Post-mortem examination showed evidence of massive hepatocellular necrosis , acute hypersensitivity myocarditis , focal acute tubulo-interstitial nephritis and extensive bone marrow necrosis , with no evidence of malignancy .

Example answer:
{"entities": [{"text": "massive hepatocellular necrosis", "type": "Disease"}, {"text": "myocarditis", "type": "Disease"}, {"text": "nephritis", "type": "Disease"}, {"text": "bone marrow necrosis", "type": "Disease"}, {"text": "malignancy", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVE : This is to present reversible inferior colliculus lesions in metronidazole-induced encephalopathy , to focus on the diffusion-weighted imaging ( DWI ) and fluid attenuated inversion recovery ( FLAIR ) imaging .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "Disease"}, {"text": "metronidazole-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: The pooled statistical analysis for ventricular septal ( VSD ) and midline ( MD ) defects was performed for rat fetuses exposed to piroxicam , selective and non-selective COX-2 inhibitor based on present and historic data .

Example answer:
{"entities": [{"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: Nitrofurantoins were associated with anophthalmia or microphthalmos ( AOR = 3.7 ; 95 % CI , 1.1-12.2 ) , hypoplastic left heart syndrome ( AOR = 4.2 ; 95 % CI , 1.9-9.1 ) , atrial septal defects ( AOR = 1.9 ; 95 % CI , 1.1-3.4 ) , and cleft lip with cleft palate ( AOR = 2.1 ; 95 % CI , 1.2-3.9 ) .

Example answer:
{"entities": [{"text": "Nitrofurantoins", "type": "Chemical"}, {"text": "anophthalmia", "type": "Disease"}, {"text": "microphthalmos", "type": "Disease"}, {"text": "hypoplastic left heart syndrome", "type": "Disease"}, {"text": "atrial septal defects", "type": "Disease"}, {"text": "cleft lip", "type": "Disease"}, {"text": "cleft palate", "type": "Disease"}]}

Example input:
Sentence: Finally , 6 weeks later , diffuse chorioretinal atrophy with optic atrophy occurred and the vision in his left eye was lost .

Example answer:
{"entities": [{"text": "chorioretinal atrophy", "type": "Disease"}, {"text": "optic atrophy", "type": "Disease"}]}

Example input:
Sentence: Diagnosis of this potentially fatal complication may be delayed or missed if renal tissue or the peripheral blood smear is not examined , because renal failure may be ascribed to cisplatin nephrotoxicity and the anemia and thrombocytopenia to drug-induced bone marrow suppression .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "bone marrow suppression", "type": "Disease"}]}

Example input:
Sentence: While the elevations of the upper lid margin in most subjects were not more than 2 mm and did not cause noticeable change in appearance , one subject suffered from mechanical entropion and marked corneal abrasion 3 hours after instillation of the medication .

Example answer:
{"entities": [{"text": "entropion", "type": "Disease"}, {"text": "corneal abrasion", "type": "Disease"}]}

Input:
Sentence: Eyes subsequently enucleated because of treatment failure ( n = 4 ) were examined histologically .

## Item bc5cdr:test:1902
Example input:
Sentence: End-stage renal disease ( ESRD ) after orthotopic liver transplantation ( OLTX ) using calcineurin-based immunotherapy : risk of development and treatment .

Example answer:
{"entities": [{"text": "End-stage renal disease", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Development of ocular myasthenia during pegylated interferon and ribavirin treatment for chronic hepatitis C. A 63-year-old male experienced sudden diplopia after 9 weeks of administration of pegylated interferon ( IFN ) alpha-2b and ribavirin for chronic hepatitis C ( CHC ) .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated interferon", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "chronic hepatitis", "type": "Disease"}, {"text": "diplopia", "type": "Disease"}, {"text": "pegylated interferon ( IFN ) alpha-2b", "type": "Chemical"}, {"text": "chronic hepatitis C", "type": "Disease"}, {"text": "CHC", "type": "Disease"}]}

Example input:
Sentence: Introduction of tacrolimus as an alternative immunosuppressive agent resulted in the recurrence of TMA and the subsequent loss of the renal allograft .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "TMA", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : We clinically and pathologically analyzed renal allografts from 1 9 renal transplant patients treated with tacrolimus ( FK506 ) for more than 1 year .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}]}

Example input:
Sentence: Clinical and histopathologic examination of renal allografts treated with tacrolimus ( FK506 ) for at least one year .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}]}

Example input:
Sentence: Recovery of tacrolimus-associated brachial neuritis after conversion to everolimus in a pediatric renal transplant recipient -- case report and review of the literature .

Example answer:
{"entities": [{"text": "tacrolimus-associated", "type": "Chemical"}, {"text": "brachial neuritis", "type": "Disease"}, {"text": "everolimus", "type": "Chemical"}]}

Example input:
Sentence: MR imaging with quantitative diffusion mapping of tacrolimus-induced neurotoxicity in organ transplant patients .

Example answer:
{"entities": [{"text": "tacrolimus-induced", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: -Tacrolimus ( FK 506 ) is a powerful , widely used immunosuppressant .

Example answer:
{"entities": [{"text": "FK 506", "type": "Chemical"}]}

Example input:
Sentence: Our objective was to investigate brain MR imaging findings and the utility of diffusion-weighted ( DW ) imaging in organ transplant patients who developed neurologic symptoms during tacrolimus therapy .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}]}

Example input:
Sentence: Brain MR studies , including DW imaging , were prospectively performed in 14 organ transplant patients receiving tacrolimus who developed neurologic complications .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "neurologic complications", "type": "Disease"}]}

Input:
Sentence: PURPOSE : To report a case of bilateral optic neuropathy in a patient receiving tacrolimus ( FK 506 , Prograf ; Fujisawa USA , Inc , Deerfield , Illinois ) for immunosuppression after orthotropic liver transplantation .

## Item bc5cdr:test:2203
Example input:
Sentence: The extent of inhibition of brain cholinesterase activity evoked by DCE at the dose of 400 mg/kg was 22 % in young and 19 % in aged mice .

Example answer:
{"entities": [{"text": "DCE", "type": "Chemical"}]}

Example input:
Sentence: Further studies on the effects of certain irrigating fluids on the rat bladder for 18 hours are reported .

Example answer:
{"entities": []}

Example input:
Sentence: In Mg ( 2+ ) -free bathing medium containing bicuculline , conditions designed to increase excitability in the slices , electrical stimulation of the hilus resulted in a single population spike in granule cells from control mice and pilocarpine-treated mice that did not experience SE .

Example answer:
{"entities": [{"text": "Mg", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "pilocarpine-treated", "type": "Chemical"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: The pooled statistical analysis for ventricular septal ( VSD ) and midline ( MD ) defects was performed for rat fetuses exposed to piroxicam , selective and non-selective COX-2 inhibitor based on present and historic data .

Example answer:
{"entities": [{"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "Chemical"}]}

Example input:
Sentence: The Dbh -/- mice had normal baseline performance in the EPM but were completely resistant to the anxiogenic effects of cocaine .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: FANFT-induced cell proliferation in the bladder was significantly suppressed by aspirin co-administration after 4 weeks but not after 12 weeks .

Example answer:
{"entities": [{"text": "FANFT-induced", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: Swiss albino mice prepared with intrajugular catheters were tested in photocell cages after administration of 93 mg/kg ( LD50 ) of cocaine and GNC92H2 infusions ranging from 30 to 190 mg/kg .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "GNC92H2", "type": "Chemical"}]}

Example input:
Sentence: Mature male and female mice from six inbred stains were tested for susceptibility to behavioral seizures induced by a single injection of cocaine .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Input:
Sentence: Inbred DBA/2 and C57BL/6 female mice were injected with CY , and the effect of the drug on the bladder was assessed during 100 days by light microscopy using different staining procedures , and after 30 days by conventional electron microscopy .

## Item bc5cdr:test:2031
Example input:
Sentence: We describe 3 episodes of microangiopathic hemolytic anemia ( MAHA ) in 2 solid organ recipients under FK506 ( tacrolimus ) therapy .

Example answer:
{"entities": [{"text": "microangiopathic hemolytic anemia", "type": "Disease"}, {"text": "MAHA", "type": "Disease"}, {"text": "FK506", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}]}

Example input:
Sentence: Liver disease caused by propylthiouracil .

Example answer:
{"entities": [{"text": "Liver disease", "type": "Disease"}, {"text": "propylthiouracil", "type": "Chemical"}]}

Example input:
Sentence: Propylthiouracil therapy was withdrawn , and she was treated with a 1-month course of prednisone , which alleviated her symptoms .

Example answer:
{"entities": [{"text": "Propylthiouracil", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}]}

Example input:
Sentence: This report presents the clinical , laboratory , and light and electron microscopic observations on a patient with chronic active ( aggressive ) hepatitis caused by the administration of propylthiouracil .

Example answer:
{"entities": [{"text": "chronic active ( aggressive ) hepatitis", "type": "Disease"}, {"text": "propylthiouracil", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVE : To describe a case of propylthiouracil-induced vasculitis manifesting with pericarditis .

Example answer:
{"entities": [{"text": "propylthiouracil-induced", "type": "Chemical"}, {"text": "vasculitis", "type": "Disease"}, {"text": "pericarditis", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : Pericarditis may be the initial manifestation of drug-induced vasculitis attributable to propylthio- uracil therapy .

Example answer:
{"entities": [{"text": "Pericarditis", "type": "Disease"}, {"text": "vasculitis", "type": "Disease"}, {"text": "propylthio- uracil", "type": "Chemical"}]}

Example input:
Sentence: METHODS : We present the first case report of a woman with hyperthyroidism treated with propylthiouracil in whom a syndrome of pericarditis , fever , and glomerulonephritis developed .

Example answer:
{"entities": [{"text": "hyperthyroidism", "type": "Disease"}, {"text": "propylthiouracil", "type": "Chemical"}, {"text": "pericarditis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "glomerulonephritis", "type": "Disease"}]}

Example input:
Sentence: Serologic evaluation revealed the presence of perinuclear-staining antineutrophil cytoplasmic autoantibodies ( pANCA ) against myeloperoxidase ( MPO ) .

Example answer:
{"entities": []}

Example input:
Sentence: Propylthiouracil-induced perinuclear-staining antineutrophil cytoplasmic autoantibody-positive vasculitis in conjunction with pericarditis .

Example answer:
{"entities": [{"text": "Propylthiouracil-induced", "type": "Chemical"}, {"text": "vasculitis", "type": "Disease"}, {"text": "pericarditis", "type": "Disease"}]}

Example input:
Sentence: A literature review revealed no prior reports of pericarditis in anti-MPO pANCA-positive vasculitis associated with propylthio- uracil therapy .

Example answer:
{"entities": [{"text": "pericarditis", "type": "Disease"}, {"text": "vasculitis", "type": "Disease"}, {"text": "propylthio- uracil", "type": "Chemical"}]}

Input:
Sentence: Frequency of appearance of myeloperoxidase-antineutrophil cytoplasmic antibody ( MPO-ANCA ) in Graves ' disease patients treated with propylthiouracil and the relationship between MPO-ANCA and clinical manifestations .

## Item bc5cdr:test:2321
Example input:
Sentence: Angina and ischemic electrocardiographic changes occurred after administration of oral dipyridamole in four patients awaiting urgent myocardial revascularization procedures .

Example answer:
{"entities": [{"text": "Angina", "type": "Disease"}, {"text": "dipyridamole", "type": "Chemical"}]}

Example input:
Sentence: Intravenous administration of a single 50-mg bolus of lidocaine in a 67-year-old man resulted in profound depression of the activity of the sinoatrial and atrioventricular nodal pacemakers .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: Due to the risk of this tachycardia inducing myocardial ischemia , we would not recommend the use in elderly patients of any of the ephedrine/propofol/mixtures studied .

Example answer:
{"entities": [{"text": "tachycardia", "type": "Disease"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "ephedrine/propofol/mixtures", "type": "Chemical"}]}

Example input:
Sentence: A case is presented of a reversible intra-Hisian block occurring under amiodarone treatment for atrial tachycardia in a patient without clear intraventricular conduction abnormalities .

Example answer:
{"entities": [{"text": "intra-Hisian block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atrial tachycardia", "type": "Disease"}, {"text": "intraventricular conduction abnormalities", "type": "Disease"}]}

Example input:
Sentence: The patient was admitted to the hospital , anticoagulated with unfractionated heparin , and given intravenous diltiazem for rate control and intravenous amiodarone for rate and rhythm control .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}]}

Example input:
Sentence: Amiodarone-induced sinoatrial block .

Example answer:
{"entities": [{"text": "Amiodarone-induced", "type": "Chemical"}, {"text": "sinoatrial block", "type": "Disease"}]}

Example input:
Sentence: Reduction in the dosage of amiodarone resulted in the disappearance of the sinoatrial block and the persistence of asymptomatic sinus bradycardia .

Example answer:
{"entities": [{"text": "amiodarone", "type": "Chemical"}, {"text": "sinoatrial block", "type": "Disease"}, {"text": "sinus bradycardia", "type": "Disease"}]}

Example input:
Sentence: We observed sinoatrial block due to chronic amiodarone administration in a 5-year-old boy with primary cardiomyopathy , Wolff-Parkinson-White syndrome and supraventricular tachycardia .

Example answer:
{"entities": [{"text": "sinoatrial block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "primary cardiomyopathy", "type": "Disease"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "supraventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: Amiodarone should be used with caution during long-term oral therapy in patients with or without clear intraventricular conduction defects .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "Chemical"}]}

Example input:
Sentence: A patient with sinuatrial disease and implanted pacemaker was treated with amiodarone ( maximum dose 1000 mg , maintenance dose 800 mg daily ) for 10 months , for control of supraventricular tachyarrhythmias .

Example answer:
{"entities": [{"text": "sinuatrial disease", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "supraventricular tachyarrhythmias", "type": "Disease"}]}

Input:
Sentence: The finding of an augmented risk of pacemaker insertion in elderly women receiving amiodarone requires further investigation .

## Item bc5cdr:test:2142
Example input:
Sentence: Delirium , which may be induced by tricyclic drug therapy in the elderly , can be caused by tricyclics with low anticholinergic potency .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}]}

Example input:
Sentence: THP exhibited an antipsychotic-like profile by potentiating haloperidol-induced catalepsy , reducing amphetamine-induced hyperactivity and reducing apomorphine-induced climbing in mice .

Example answer:
{"entities": []}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: Patients who experienced a manic or hypomanic switch were compared with those who did not on several variables including age , sex , diagnosis ( DSM-IV bipolar I vs. bipolar II ) , number of previous manic episodes , type of antidepressant therapy used ( electroconvulsive therapy vs. antidepressant drugs and , more particularly , selective serotonin reuptake inhibitors [ SSRIs ] ) , use and type of mood stabilizers ( lithium vs. anticonvulsants ) , and temperament of the patient , assessed during a normothymic period using the hyperthymia component of the Semi-structured Affective Temperament Interview .

Example answer:
{"entities": [{"text": "manic", "type": "Disease"}, {"text": "hypomanic", "type": "Disease"}, {"text": "DSM-IV bipolar I", "type": "Disease"}, {"text": "bipolar II", "type": "Disease"}, {"text": "antidepressant", "type": "Chemical"}, {"text": "serotonin reuptake inhibitors", "type": "Chemical"}, {"text": "SSRIs", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: Drug-induced parkinsonism was observed in subjects treated with risperidone ( 42 % ) and haloperidol ( 29 % ) and was observed at occupancy levels above 60 % .

Example answer:
{"entities": [{"text": "Drug-induced parkinsonism", "type": "Disease"}, {"text": "risperidone", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: In a double-blind 6-week trial , 458 patients with acute schizophrenia were randomly assigned to fixed-dose treatment with asenapine at 5 mg twice daily ( BID ) , asenapine at 10 mg BID , placebo , or haloperidol at 4 mg BID ( to verify assay sensitivity ) .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "Disease"}, {"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Triazolam-induced brief episodes of secondary mania in a depressed patient .

Example answer:
{"entities": [{"text": "Triazolam-induced", "type": "Chemical"}, {"text": "mania", "type": "Disease"}, {"text": "depressed", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Switches to hypomania or mania occurred in 27 % of all patients ( N = 12 ) ( and in 24 % of the subgroup of patients treated with SSRIs [ 8/33 ] ) ; 16 % ( N = 7 ) experienced manic episodes , and 11 % ( N = 5 ) experienced hypomanic episodes .

Example answer:
{"entities": [{"text": "hypomania", "type": "Disease"}, {"text": "mania", "type": "Disease"}, {"text": "SSRIs", "type": "Chemical"}, {"text": "manic", "type": "Disease"}, {"text": "hypomanic", "type": "Disease"}]}

Example input:
Sentence: Antidepressant-induced mania in bipolar patients : identification of risk factors .

Example answer:
{"entities": [{"text": "Antidepressant-induced", "type": "Chemical"}, {"text": "mania", "type": "Disease"}, {"text": "bipolar", "type": "Disease"}]}

Example input:
Sentence: Large doses of triazolam repeatedly induced brief episodes of mania in a depressed elderly woman .

Example answer:
{"entities": [{"text": "triazolam", "type": "Chemical"}, {"text": "mania", "type": "Disease"}, {"text": "depressed", "type": "Disease"}]}

Input:
Sentence: Twenty-one reports of antimicrobial-induced mania were found in the literature .

## Item bc5cdr:test:2324
Example input:
Sentence: The Calcineurin-inhibitor Induced Pain Syndrome ( CIPS ) is a rare but severe side effect of cyclosporine or tacrolimus and is accurately diagnosed by its typical presentation , magnetic resonance imaging and bone scans .

Example answer:
{"entities": [{"text": "Pain", "type": "Disease"}, {"text": "CIPS", "type": "Disease"}, {"text": "cyclosporine", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}]}

Example input:
Sentence: The results have shown that the degradation product p-choloroaniline is not a significant factor in chlorhexidine-digluconate associated erosive cystitis .

Example answer:
{"entities": [{"text": "p-choloroaniline", "type": "Chemical"}, {"text": "chlorhexidine-digluconate", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Example input:
Sentence: In cyclophosphamide-induced cystitis in the rat , detrusor function is impaired and the expression and effects of muscarinic receptors altered .

Example answer:
{"entities": [{"text": "cyclophosphamide-induced", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Example input:
Sentence: Pneumonitis , bilateral pleural effusions , echocardiographic evidence of cardiac tamponade , and positive autoantibodies developed in a 43-year-old man , who was receiving long-term sulfasalazine therapy for chronic ulcerative colitis .

Example answer:
{"entities": [{"text": "Pneumonitis", "type": "Disease"}, {"text": "pleural effusions", "type": "Disease"}, {"text": "cardiac tamponade", "type": "Disease"}, {"text": "sulfasalazine", "type": "Chemical"}, {"text": "ulcerative colitis", "type": "Disease"}]}

Example input:
Sentence: We report a case of intractable hemorrhagic cystitis due to cyclophosphamide therapy for Wegener 's granulomatosis .

Example answer:
{"entities": [{"text": "cyclophosphamide", "type": "Chemical"}, {"text": "Wegener 's granulomatosis", "type": "Disease"}]}

Example input:
Sentence: Picloxydine irrigations appeared to have a lower incidence of erosive cystitis but further studies would have to be performed before it could be recommended for use in urological procedures .

Example answer:
{"entities": [{"text": "Picloxydine", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Example input:
Sentence: CY caused hemorrhagic cystitis in 40 % of rats , but it did not cause this complication when combined with 5-FU and MTX .

Example answer:
{"entities": [{"text": "CY", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "MTX", "type": "Chemical"}]}

Example input:
Sentence: Hyperkalemia has recently been recognized as a complication of nonsteroidal antiinflammatory agents ( NSAID ) such as indomethacin .

Example answer:
{"entities": [{"text": "Hyperkalemia", "type": "Disease"}, {"text": "indomethacin", "type": "Chemical"}]}

Example input:
Sentence: A high percentage of kanamycin-colistin and povidone-iodine irrigations were associated with erosive cystitis and suggested a possible complication with human usage .

Example answer:
{"entities": [{"text": "kanamycin-colistin", "type": "Chemical"}, {"text": "povidone-iodine", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Example input:
Sentence: Since nonsteroidal anti-inflammatory agents interfere with this compensatory mechanism and may cause acute renal failure , they should be used with caution in such patients .

Example answer:
{"entities": [{"text": "acute renal failure", "type": "Disease"}]}

Input:
Sentence: Nonsteroidal anti-inflammatory drug-induced cystitis is a poorly recognized and under-reported condition .

## Item bc5cdr:test:2322
Example input:
Sentence: Animal studies suggest that incontinence secondary to serotonergic antidepressants could be mediated by the 5HT4 receptors found on the bladder .

Example answer:
{"entities": [{"text": "incontinence", "type": "Disease"}, {"text": "serotonergic antidepressants", "type": "Chemical"}]}

Example input:
Sentence: Using puromycin aminonucleoside nephrosis ( PAN ) rats , we studied early ultrastructural and permeability changes in relation to the expression of the podocyte-associated molecules nephrin , a-actinin , dendrin , and plekhh2 , the last two of which were only recently discovered in podocytes .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: Renal papillary necrosis ( RPN ) and a decreased urinary concentrating ability developed during continuous long-term treatment with aspirin and paracetamol in female Fischer 344 rats .

Example answer:
{"entities": [{"text": "Renal papillary necrosis", "type": "Disease"}, {"text": "RPN", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: This study shows that prolonged analgesic treatment in Fischer 344 rats causes progressive and irreversible damage to the interstitial matrix and type 1 interstitial cells leading to RPN .

Example answer:
{"entities": [{"text": "RPN", "type": "Disease"}]}

Example input:
Sentence: Indomethacin-induced renal insufficiency : recurrence on rechallenge .

Example answer:
{"entities": [{"text": "Indomethacin-induced", "type": "Chemical"}, {"text": "renal insufficiency", "type": "Disease"}]}

Example input:
Sentence: The co-administration of aspirin with N- [ 4- ( 5-nitro-2-furyl ) -2-thiazolyl ] -formamide ( FANFT ) to rats resulted in a reduced incidence of FANFT-induced bladder carcinomas but a concomitant induction of forestomach tumors .

Example answer:
{"entities": [{"text": "aspirin", "type": "Chemical"}, {"text": "N- [ 4- ( 5-nitro-2-furyl ) -2-thiazolyl ] -formamide", "type": "Chemical"}, {"text": "FANFT", "type": "Chemical"}, {"text": "FANFT-induced", "type": "Chemical"}, {"text": "bladder carcinomas", "type": "Disease"}, {"text": "forestomach tumors", "type": "Disease"}]}

Example input:
Sentence: Prompt restoration of renal function followed drug withdrawal , while re-exposure to a single dose of indomethacin caused recurrence of acute reversible oliguria .

Example answer:
{"entities": [{"text": "indomethacin", "type": "Chemical"}, {"text": "oliguria", "type": "Disease"}]}

Example input:
Sentence: In cyclophosphamide-induced cystitis in the rat , detrusor function is impaired and the expression and effects of muscarinic receptors altered .

Example answer:
{"entities": [{"text": "cyclophosphamide-induced", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Example input:
Sentence: Histologic changes were found in rat kidneys after administration of MTX , CY and NG , while no such change was observed after 5-FU and joint administration of MTX + 5-FU + CY compared to controls .

Example answer:
{"entities": [{"text": "MTX", "type": "Chemical"}, {"text": "CY", "type": "Chemical"}, {"text": "NG", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}]}

Example input:
Sentence: Effect of aspirin on N- [ 4- ( 5-nitro-2-furyl ) -2-thiazolyl ] -formamide-induced epithelial proliferation in the urinary bladder and forestomach of the rat .

Example answer:
{"entities": [{"text": "aspirin", "type": "Chemical"}, {"text": "N- [ 4- ( 5-nitro-2-furyl ) -2-thiazolyl ]", "type": "Chemical"}]}

Input:
Sentence: Indomethacin-induced morphologic changes in the rat urinary bladder epithelium .

## Item bc5cdr:test:2446
Example input:
Sentence: For compounds that have shown TDP in the clinic ( terfenadine , terodiline , cisapride ) there is little differentiation between the dog ED50 and the efficacious free plasma concentrations in man ( < 10-fold ) reflecting their limited safety margins .

Example answer:
{"entities": [{"text": "TDP", "type": "Disease"}, {"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}]}

Example input:
Sentence: The mean steady-state plasma and CSF methotrexate concentrations achieved were 1.1 X 10 ( -3 ) mol/L and 3.6 X 10 ( -5 ) mol/L , respectively .

Example answer:
{"entities": [{"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: Analyses of a blood sample revealed unusually high plasma concentrations of metoprolol ( greater than 3000 ng/ml ) and diltiazem ( 526 ng/ml ) .

Example answer:
{"entities": [{"text": "metoprolol", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}]}

Example input:
Sentence: Concentrations of amphotericin B in plasma were not significantly different among the three groups at any time during the study .

Example answer:
{"entities": [{"text": "amphotericin B", "type": "Chemical"}]}

Example input:
Sentence: Comparison of the subjective effects and plasma concentrations following oral and i.m .

Example answer:
{"entities": []}

Example input:
Sentence: Portal plasma concentrations of neither arginine vasopressin nor oxytocin are significantly altered in this paradigm .

Example answer:
{"entities": [{"text": "arginine vasopressin", "type": "Chemical"}, {"text": "oxytocin", "type": "Chemical"}]}

Example input:
Sentence: Plasma concentrations of the drug were estimated by gas-liquid chromatography , in a smaller number of the subjects .

Example answer:
{"entities": []}

Example input:
Sentence: On the basis that only free drug in the systemic circulation will elicit a pharmacological response target , free concentrations in plasma were selected to mimic the free drug exposures in man .

Example answer:
{"entities": []}

Example input:
Sentence: The area under the plasma concentration time curve at 90 min was 4-12 times greater than for oral drug , suggesting the existence of an absorption-limiting process in the intestine , and providing an alternate form of administration for quaternary drugs .

Example answer:
{"entities": []}

Example input:
Sentence: Plasma concentrations varied with dose and route and corresponded qualitatively with the subjective effects .

Example answer:
{"entities": []}

Input:
Sentence: Plasma concentrations did not differ significantly between the two formulations .

## Item bc5cdr:test:2437
Example input:
Sentence: Two patients are presented with tingling or burning sensations limited to areas of heat exposure or sunburn .

Example answer:
{"entities": [{"text": "tingling or burning sensations", "type": "Disease"}, {"text": "sunburn", "type": "Disease"}]}

Example input:
Sentence: An allergic reaction consisting of angioneurotic edema secondary to continuous infusion 5-fluorouracil occurred in a patient with recurrent carcinoma of the oral cavity , cirrhosis , and cisplatin-induced impaired renal function .

Example answer:
{"entities": [{"text": "allergic reaction", "type": "Disease"}, {"text": "angioneurotic edema", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "carcinoma of the oral cavity", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "impaired renal function", "type": "Disease"}]}

Example input:
Sentence: High incidence of primary pulmonary hypertension associated with appetite suppressants in Belgium .

Example answer:
{"entities": [{"text": "primary pulmonary hypertension", "type": "Disease"}, {"text": "appetite suppressants", "type": "Chemical"}]}

Example input:
Sentence: Anaphylaxis was seen in 37 patients ( 69 % ) , the other 17 ( 31 % ) having urticaria and/or angioedema .

Example answer:
{"entities": [{"text": "Anaphylaxis", "type": "Disease"}, {"text": "urticaria", "type": "Disease"}, {"text": "angioedema", "type": "Disease"}]}

Example input:
Sentence: Five hours after exposure , he developed disulfiram-like syndrome with flushing , tachycardia , and arterial hypotension after consuming three glasses of wine .

Example answer:
{"entities": [{"text": "disulfiram-like", "type": "Chemical"}, {"text": "flushing", "type": "Disease"}, {"text": "tachycardia", "type": "Disease"}, {"text": "arterial hypotension", "type": "Disease"}]}

Example input:
Sentence: In 8 patients the diagnosis of primary pulmonary hypertension was uncertain , 5 of them had taken appetite suppressants .

Example answer:
{"entities": [{"text": "primary pulmonary hypertension", "type": "Disease"}, {"text": "appetite suppressants", "type": "Chemical"}]}

Example input:
Sentence: Allergic manifestations such as rash and eosinophilia were rare .

Example answer:
{"entities": [{"text": "rash", "type": "Disease"}, {"text": "eosinophilia", "type": "Disease"}]}

Example input:
Sentence: The patients who had been exposed to appetite suppressants tended to be on average more severely ill , and to have a shorter median delay between onset of symptoms and diagnosis .

Example answer:
{"entities": [{"text": "appetite suppressants", "type": "Chemical"}]}

Example input:
Sentence: The first case involved a 59-year-old man who used Dormex , which contains hydrogen cyanamide , without protection after consuming a large amount of alcohol during a meal .

Example answer:
{"entities": [{"text": "Dormex", "type": "Chemical"}, {"text": "hydrogen cyanamide", "type": "Chemical"}, {"text": "alcohol", "type": "Chemical"}]}

Example input:
Sentence: There were 13 cases of adverse reactions ( 0.34 % ) , ten of which were mild reactions such as nausea , exanthema , urtication , itchiness , and urgency to defecate , and did not require treatment .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "exanthema", "type": "Disease"}, {"text": "urtication", "type": "Disease"}, {"text": "itchiness", "type": "Disease"}]}

Input:
Sentence: All had reported incidents of being very embarrassed whilst eating hot spicy foods .

## Item bc5cdr:test:2326
Example input:
Sentence: METHODS : Seventeen subjects who were genotyped as CYP2D6 extensive metabolizers were enrolled in this randomized , open-label , crossover study to receive a single oral dose of desipramine ( 50 mg ) on two separate occasions , once alone and once after multiple doses of cinacalcet ( 90 mg for 7 days ) .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}]}

Example input:
Sentence: Treatment , given every 21 days for a maximum of three cycles , consisted of paclitaxel by 3-hour infusion followed the next day by a fixed dose of cisplatin ( 75 mg/m2 ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: METHODS : For a period of 2 weeks , CsA 15 mg/kg/day ( given orally ) , FK506 3.0 mg/kg/day ( given orally ) or SRL 0.4 mg/kg/day ( given intraperitoneally ) was administered once a day as these doses have earlier been found to achieve a significant immunosuppressive effect in Sprague-Dawley rats .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: Rats were treated with a single IV injection of puromycin aminonucleoside , ( PAN , 7.5 mg/kg ) and 24 hour urine samples were obtained prior to sacrifice on days 3,5,7,10,17,27,41 ( N = 5-10 per group ) .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: In order to address long-term pain memory , nine healthy male volunteers received intradermal injections of three doses of capsaicin ( 0.05 , 1 and 20 microg , separated by 15 min breaks ) , each given three times in a balanced design across three sessions at one week intervals .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: 2 and 10 mg/kg/i.p. , or an equal volume of saline for the control group ( n = 20 ) ; 15 minutes later , all the animals were injected with a single 50 mg/kg/i.p .

Example answer:
{"entities": []}

Example input:
Sentence: Ketamine hydrochloride was administered intravenously ( at a dose of two milligrams per kilogram of body weight ) in ninety-nine of the patients and intramuscularly ( at a dose of four milligrams per kilogram of body weight ) in the other fifteen .

Example answer:
{"entities": [{"text": "Ketamine hydrochloride", "type": "Chemical"}]}

Example input:
Sentence: At the end of the procedure , Group A ( n = 20 ) had 20 mg/0.5 mL of methylprednisolone and 10 mg/0.5 mL of gentamicin injected into the posterior sub-Tenon 's space and Group B ( n = 20 ) had the same combination injected into the anterior sub-Tenon 's space .

Example answer:
{"entities": [{"text": "methylprednisolone", "type": "Chemical"}, {"text": "gentamicin", "type": "Chemical"}]}

Example input:
Sentence: The patients were randomly allocated to one of three groups ; those in group A ( n = 10 ) were subjected to controlled hypotension alone , those in group B ( n = 10 ) to haemodilution alone and those in group C ( n = 10 ) to both controlled hypotension and haemodilution .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}]}

Example input:
Sentence: INTERVENTION : Each patient received either intravenous docetaxel 30 mg/m2/week for 3 consecutive weeks , followed by 1 week off , or the combination of continuous oral thalidomide 200 mg every evening plus the same docetaxel regimen .

Example answer:
{"entities": [{"text": "docetaxel", "type": "Chemical"}, {"text": "thalidomide", "type": "Chemical"}]}

Input:
Sentence: METHODS : Three groups were established : a control group ( n = 10 ) , a high-dose group ( n = 10 ) , treated with one intraperitoneal injection of indomethacin 20 mg/kg , and a therapeutic dose group ( n = 10 ) in which oral indomethacin was administered 3.25 mg/kg body weight daily for 3 weeks .

## Item bc5cdr:test:2055
Example input:
Sentence: Effect of green tea and vitamin E combination in isoproterenol induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Effects of long-term pretreatment with isoproterenol on bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: Isoproterenol-treated rats showed significant increases in the levels of lactate dehydrogenase , aspartate transaminase , creatine kinase and malondialdehyde and significant decreases in the activities of superoxide dismutase , catalase and glutathione peroxidase in serum and heart .

Example answer:
{"entities": [{"text": "Isoproterenol-treated", "type": "Chemical"}, {"text": "lactate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "creatine", "type": "Chemical"}, {"text": "malondialdehyde", "type": "Chemical"}, {"text": "superoxide", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: In isolated perfused heart preparations from isoproterenol-pretreated rats , the isoproterenol-induced maximal increase in left ventricular systolic pressure was significantly reduced , compared with saline-pretreated rats ( the EC50 of the isoproterenol-induced increase in left ventricular systolic pressure was enhanced approximately 22-fold ) .

Example answer:
{"entities": [{"text": "isoproterenol-pretreated", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: The results show that pretreatment with TCR may be useful in preventing the damage induced by isoproterenol in rat heart .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: The effects of exercise on the severity of isoproterenol-induced myocardial infarction were studied in female albino rats of 20,40,60 and 80 weeks of age .

Example answer:
{"entities": [{"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Isoproterenol pretreatment for 15 days caused cardiac hypertrophy without affecting baseline blood pressure and heart rate .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "Chemical"}, {"text": "cardiac hypertrophy", "type": "Disease"}]}

Example input:
Sentence: Pretreatment of TCR , at a dose of 0.5 mL/100 g bodyweight per day , orally for 30 days , prevented the increase in lipid peroxidation and activity of marker enzymes observed in isoproterenol-induced rats ( 85 mg kg ( -1 ) s. c. for 2 days at an interval of 24 h ) .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: Histological studies demonstrated that the rats developed an infarct 18 h after isoproterenol administration .

Example answer:
{"entities": [{"text": "infarct", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}]}

Input:
Sentence: Oral pre-treatment with PK ( 80 mg kg ( -1 ) day ( -1 ) for 15 days ) significantly prevented the isoproterenol-induced myocardial infarction and maintained the rats at near normal status .

## Item bc5cdr:test:2080
Example input:
Sentence: CONCLUSIONS : These results indicate that noradrenergic signaling via beta-adrenergic receptors is required for cocaine-induced anxiety in mice .

Example answer:
{"entities": [{"text": "cocaine-induced", "type": "Chemical"}, {"text": "anxiety", "type": "Disease"}]}

Example input:
Sentence: It has been shown that bromocriptine-induced tachycardia , which persisted after adrenalectomy , is ( i ) mediated by central dopamine D2 receptor activation and ( ii ) reduced by 5-day isoproterenol pretreatment , supporting therefore the hypothesis that this effect is dependent on sympathetic outflow to the heart .

Example answer:
{"entities": [{"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: The mechanism of chest pain related to cocaine use is discussed and treatment dilemmas are discussed .

Example answer:
{"entities": [{"text": "chest pain", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Electrocardiography has a very low sensitivity in detecting dobutamine-induced myocardial ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}]}

Example input:
Sentence: In addition , reflex bradycardia caused by injected norepinephrine was significantly enhanced by L-dopa , DL-Threo-dihydroxyphenylserine had no effect on blood pressure , heart rate or reflex responses to norepinephrine .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}, {"text": "DL-Threo-dihydroxyphenylserine", "type": "Chemical"}]}

Example input:
Sentence: Norepinephrine signaling through beta-adrenergic receptors is critical for expression of cocaine-induced anxiety .

Example answer:
{"entities": [{"text": "Norepinephrine", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "anxiety", "type": "Disease"}]}

Example input:
Sentence: To develop a more sensitive echocardiographic screening test for cardiac damage due to doxorubicin , a cohort study was performed using dobutamine infusion to differentiate asymptomatic long-term survivors of childhood cancer treated with doxorubicin from healthy control subjects .

Example answer:
{"entities": [{"text": "cardiac damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: Dobutamine stress echocardiography : a sensitive indicator of diminished myocardial function in asymptomatic doxorubicin-treated long-term survivors of childhood cancer .

Example answer:
{"entities": [{"text": "Dobutamine", "type": "Chemical"}, {"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: Eleven of the cocaine abusers and none of the controls had ECG evidence of significant myocardial injury defined as myocardial infarction , ischemia , and bundle branch block .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "myocardial injury", "type": "Disease"}, {"text": "myocardial infarction", "type": "Disease"}, {"text": "ischemia", "type": "Disease"}, {"text": "bundle branch block", "type": "Disease"}]}

Example input:
Sentence: In particular , the tendency of cocaine to produce chest pain ought to be in the mind of the emergency nurse when faced with a young victim of chest pain who is otherwise at low risk .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "chest pain", "type": "Disease"}]}

Input:
Sentence: CONCLUSION : No exaggerated adrenergic response was detected when dobutamine was administered to patients with cocaine-related chest pain .

## Item bc5cdr:test:1960
Example input:
Sentence: IMPORTANCE OF THE FIELD : Fluoropyrimidines , in particular 5-fluorouracil ( 5-FU ) , have been the mainstay of treatment for several solid tumors , including colorectal , breast and head and neck cancers , for > 40 years .

Example answer:
{"entities": [{"text": "Fluoropyrimidines", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "tumors", "type": "Disease"}]}

Example input:
Sentence: Paclitaxel , cisplatin , and gemcitabine combination chemotherapy within a multidisciplinary therapeutic approach in metastatic nonsmall cell lung carcinoma .

Example answer:
{"entities": [{"text": "Paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "nonsmall cell lung carcinoma", "type": "Disease"}]}

Example input:
Sentence: It has shown promising results alone or in combination with other chemotherapeutic agents in colorectal , breast , pancreaticobiliary , gastric , renal cell and head and neck cancers .

Example answer:
{"entities": []}

Example input:
Sentence: BACKGROUND : Cisplatin has minimal antitumor activity when used as second- or third-line treatment of metastatic breast carcinoma .

Example answer:
{"entities": [{"text": "Cisplatin", "type": "Chemical"}, {"text": "breast carcinoma", "type": "Disease"}]}

Example input:
Sentence: Forty-three ovarian cancer patients were available for analysis following six cycles of the same PAC-containing regimen : 23 had been supplemented by glutamate all along the treatment period , at a daily dose of three times 500 mg ( group G ) , and 20 had received a placebo ( group P ) .

Example answer:
{"entities": [{"text": "ovarian cancer", "type": "Disease"}, {"text": "PAC-containing", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: We initiated a phase I/II trial to determine the response and toxicity of escalating paclitaxel doses combined with fixed-dose cisplatin with granulocyte colony-stimulating factor support in patients with untreated locally advanced inoperable head and neck carcinoma .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "head and neck carcinoma", "type": "Disease"}]}

Example input:
Sentence: A phase I/II study of paclitaxel plus cisplatin as first-line therapy for head and neck cancers : preliminary results .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "head and neck cancers", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : The combination of paclitaxel , cisplatin , and gemcitabine is well tolerated and shows high activity in metastatic NSCLC .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "NSCLC", "type": "Disease"}]}

Example input:
Sentence: Paclitaxel/cisplatin is an effective first-line regimen for locoregionally advanced head and neck cancer and continued study is warranted .

Example answer:
{"entities": [{"text": "Paclitaxel/cisplatin", "type": "Chemical"}, {"text": "head and neck cancer", "type": "Disease"}]}

Example input:
Sentence: Preliminary results of an Eastern Cooperative Oncology Group study of single-agent paclitaxel ( Taxol ; Bristol-Myers Squibb Company , Princeton , NJ ) reported a 37 % response rate in patients with head and neck cancer , and the paclitaxel/cisplatin combination has been used successfully and has significantly improved median response duration in ovarian cancer patients .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "Taxol", "type": "Chemical"}, {"text": "head and neck cancer", "type": "Disease"}, {"text": "paclitaxel/cisplatin", "type": "Chemical"}, {"text": "ovarian cancer", "type": "Disease"}]}

Input:
Sentence: Definite , although limited , antineoplastic activity is observed in patients with well-defined platinum- and paclitaxel-refractory ovarian cancer .

## Item bc5cdr:test:2105
Example input:
Sentence: Abnormal movements and deafness occurred only in rats treated during the preweaning period ; within this period the greatest sensitivities for these abnormalities occurred from 2 to 11-17 and 5 to 11 days of age , respectively , indicating that the cochlea is more sensitive to streptomycin than the site ( vestibular or central ) responsible for the dyskinesias .

Example answer:
{"entities": [{"text": "Abnormal movements", "type": "Disease"}, {"text": "deafness", "type": "Disease"}, {"text": "streptomycin", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: Nitro-L-arginine methyl ester : a potential protector against gentamicin ototoxicity .

Example answer:
{"entities": [{"text": "Nitro-L-arginine methyl ester", "type": "Chemical"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "ototoxicity", "type": "Disease"}]}

Example input:
Sentence: Early trials of cisplatin and amifostine also suggested that the incidence and severity of cisplatin-induced nephrotoxicity , ototoxicity , and neuropathy were reduced .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "amifostine", "type": "Chemical"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "ototoxicity", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}]}

Example input:
Sentence: Patients with SNHL presented with relatively lower serum ferritin levels than those with normal hearing , however , no statistically significant difference was observed .

Example answer:
{"entities": [{"text": "SNHL", "type": "Disease"}]}

Example input:
Sentence: Visual and auditory neurotoxicity was previously documented in 42 of 89 patients with transfusion-dependent anemia who were receiving iron chelation therapy with daily subcutaneous deferoxamine .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "iron", "type": "Chemical"}, {"text": "deferoxamine", "type": "Chemical"}]}

Example input:
Sentence: L-NAME reduced gentamicin-induced hearing loss in the high-frequency range , but gave no protection in the middle or low frequencies .

Example answer:
{"entities": [{"text": "L-NAME", "type": "Chemical"}, {"text": "gentamicin-induced", "type": "Chemical"}, {"text": "hearing loss", "type": "Disease"}]}

Example input:
Sentence: Their ototoxicity is a serious health problem and , as their ototoxic mechanism involves the production of NO , we need to assess the use of NO inhibitors for the prevention of aminoglycoside-induced sensorineural hearing loss .

Example answer:
{"entities": [{"text": "ototoxicity", "type": "Disease"}, {"text": "ototoxic", "type": "Disease"}, {"text": "NO", "type": "Chemical"}, {"text": "aminoglycoside-induced", "type": "Chemical"}, {"text": "sensorineural hearing loss", "type": "Disease"}]}

Example input:
Sentence: Gentamicin sulfate and tobramycin sulfate continue to demonstrate ototoxicity and nephrotoxicity in both animal and clinical studies .

Example answer:
{"entities": [{"text": "Gentamicin sulfate", "type": "Chemical"}, {"text": "tobramycin sulfate", "type": "Chemical"}, {"text": "ototoxicity", "type": "Disease"}, {"text": "nephrotoxicity", "type": "Disease"}]}

Example input:
Sentence: The nitric oxide ( NO ) inhibitor nitro-L-arginine methyl ester ( L-NAME ) may act as an otoprotectant against high-frequency hearing loss caused by gentamicin , but further studies are needed to confirm this.Aminoglycoside antibiotics are still widely used by virtue of their efficacy and low cost .

Example answer:
{"entities": [{"text": "nitric oxide", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}, {"text": "nitro-L-arginine methyl ester", "type": "Chemical"}, {"text": "L-NAME", "type": "Chemical"}, {"text": "high-frequency hearing loss", "type": "Disease"}, {"text": "gentamicin", "type": "Chemical"}]}

Example input:
Sentence: Following recovery , the monkeys were selectively deafened for high frequencies using kanamycin and furosemide .

Example answer:
{"entities": [{"text": "kanamycin", "type": "Chemical"}, {"text": "furosemide", "type": "Chemical"}]}

Input:
Sentence: Overexpression of copper/zinc-superoxide dismutase protects from kanamycin-induced hearing loss .

## Item bc5cdr:test:1857
Example input:
Sentence: NIN-induced midpontine activation may correspond to activation of the dorsomedial pontine nuclei and the nucleus reticularis tegmenti pontis , structures known to participate in the generation of multidirectional saccades and smooth pursuit eye movements .

Example answer:
{"entities": [{"text": "NIN-induced", "type": "Disease"}]}

Example input:
Sentence: The extent of inhibition of brain cholinesterase activity evoked by DCE at the dose of 400 mg/kg was 22 % in young and 19 % in aged mice .

Example answer:
{"entities": [{"text": "DCE", "type": "Chemical"}]}

Example input:
Sentence: The biochemical results of brain biogenic amines of BALB/C mouse strain suggest a probable decrease of catecholamine turnover rate and/or metabolism by monoamine oxidase and a resulting increase in O-methylation of norepinephrine which may account for a behavioral depression caused by amantadine in the BALB/C mice .

Example answer:
{"entities": [{"text": "amines", "type": "Chemical"}, {"text": "catecholamine", "type": "Chemical"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "behavioral depression", "type": "Disease"}, {"text": "amantadine", "type": "Chemical"}]}

Example input:
Sentence: The correlation between neuropathic damage and inhibition of neurotoxic esterase or neuropathy target enzyme ( NTE ) was examined in rats acutely exposed to Mipafox ( N , N'-diisopropylphosphorodiamidofluoridate ) , a neurotoxic organophosphate .

Example answer:
{"entities": [{"text": "neuropathic damage", "type": "Disease"}, {"text": "neurotoxic", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}, {"text": "Mipafox", "type": "Chemical"}, {"text": "N , N'-diisopropylphosphorodiamidofluoridate", "type": "Chemical"}, {"text": "organophosphate", "type": "Chemical"}]}

Example input:
Sentence: The alpha3 and beta4 nicotinic acetylcholine receptor subunits are necessary for nicotine-induced seizures and hypolocomotion in mice .

Example answer:
{"entities": [{"text": "acetylcholine", "type": "Chemical"}, {"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "hypolocomotion", "type": "Disease"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: We conclude that the interpeduncular nucleus mediates nicotinic depression of locomotor activity and dampens nicotinic arousal mechanisms located elsewhere in the brain .

Example answer:
{"entities": []}

Example input:
Sentence: We examined the role of the beta4 subunits in nicotine-induced seizures and hypolocomotion in beta4 homozygous null ( beta4 -/- ) and alpha3 heterozygous ( +/- ) mice .

Example answer:
{"entities": [{"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "hypolocomotion", "type": "Disease"}]}

Example input:
Sentence: NRA0160 and clozapine antagonized locomotor hyperactivity induced by methamphetamine ( MAP ) in mice .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "MAP", "type": "Chemical"}]}

Example input:
Sentence: METHODS : In this study , we evaluated the performance of dopamine beta-hydroxylase knockout ( Dbh -/- ) mice , which lack norepinephrine ( NE ) , in the elevated plus maze ( EPM ) to examine the contribution of noradrenergic signaling to cocaine-induced anxiety .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "NE", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "anxiety", "type": "Disease"}]}

Input:
Sentence: Reduced nicotinamide adenine dinucleotide phosphate-diaphorase ( NADPH-d ) histochemistry was also employed to visualize NOS as an index of enzyme expression in mice brain regions related to motor control .

## Item bc5cdr:test:2072
Example input:
Sentence: The emergency nurse ought to be familiar with some of the cardiovascular consequences of cocaine use .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: A 45-year-old man , an admitted frequent cocaine user , presented to the Emergency Department ( ED ) on two separate occasions with a history of priapism after cocaine use .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "priapism", "type": "Disease"}]}

Example input:
Sentence: METHOD : Twenty cocaine-dependent participants were randomly assigned to receive modafinil , 400 mg ( N=10 ) , or placebo ( N=10 ) every morning at 7:30 a.m. for 16 days in an inpatient , double-blind randomized trial .

Example answer:
{"entities": [{"text": "cocaine-dependent", "type": "Chemical"}, {"text": "modafinil", "type": "Chemical"}]}

Example input:
Sentence: The mechanism of chest pain related to cocaine use is discussed and treatment dilemmas are discussed .

Example answer:
{"entities": [{"text": "chest pain", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVES : To assess the added diagnostic value of a new cardiac performance index ( dP/dtejc ) measurement , based on brachial artery flow changes , as compared to standard 12-lead ECG , for detecting dobutamine-induced myocardial ischemia , using Tc99m-Sestamibi single-photon emission computed tomography as the gold standard of comparison to assess the presence or absence of ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "Tc99m-Sestamibi", "type": "Chemical"}, {"text": "ischemia", "type": "Disease"}]}

Example input:
Sentence: Electrocardiographic evidence of myocardial injury in psychiatrically hospitalized cocaine abusers .

Example answer:
{"entities": [{"text": "myocardial injury", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: In individuals with preexisting , high-grade coronary arterial narrowing , acute myocardial infarction may result from an increase in myocardial oxygen demand associated with cocaine-induced increase in rate-pressure product .

Example answer:
{"entities": [{"text": "acute myocardial infarction", "type": "Disease"}, {"text": "oxygen", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}]}

Example input:
Sentence: The electrocardiograms ( ECG ) of 99 cocaine-abusing patients were compared with the ECGs of 50 schizophrenic controls .

Example answer:
{"entities": [{"text": "cocaine-abusing", "type": "Chemical"}, {"text": "schizophrenic", "type": "Disease"}]}

Example input:
Sentence: In particular , the tendency of cocaine to produce chest pain ought to be in the mind of the emergency nurse when faced with a young victim of chest pain who is otherwise at low risk .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "chest pain", "type": "Disease"}]}

Example input:
Sentence: Eleven of the cocaine abusers and none of the controls had ECG evidence of significant myocardial injury defined as myocardial infarction , ischemia , and bundle branch block .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "myocardial injury", "type": "Disease"}, {"text": "myocardial infarction", "type": "Disease"}, {"text": "ischemia", "type": "Disease"}, {"text": "bundle branch block", "type": "Disease"}]}

Input:
Sentence: Patients were eligible for DSE if they had used cocaine within 24 hours preceding the onset of chest pain and had a normal ECG and tropinin I level .
