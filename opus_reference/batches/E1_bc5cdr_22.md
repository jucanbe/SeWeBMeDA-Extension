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

## Item bc5cdr:test:4382
Example input:
Sentence: Visual and auditory neurotoxicity was previously documented in 42 of 89 patients with transfusion-dependent anemia who were receiving iron chelation therapy with daily subcutaneous deferoxamine .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "iron", "type": "Chemical"}, {"text": "deferoxamine", "type": "Chemical"}]}

Example input:
Sentence: CNS complications included posterior reversible leukoencephalopathy syndrome ( n = 10 ) , stroke ( n = 5 ) , temporal lobe epilepsy ( n = 2 ) , high-dose methotrexate toxicity ( n = 2 ) , syndrome of inappropriate antidiuretic hormone secretion ( n = 1 ) , and other unclassified events ( n = 7 ) .

Example answer:
{"entities": [{"text": "leukoencephalopathy", "type": "Disease"}, {"text": "stroke", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "inappropriate antidiuretic hormone secretion", "type": "Disease"}]}

Example input:
Sentence: Isoniazid was the most frequent agent in drug-induced neuropathy .

Example answer:
{"entities": [{"text": "Isoniazid", "type": "Chemical"}, {"text": "neuropathy", "type": "Disease"}]}

Example input:
Sentence: The most commonly reported toxic effects of capecitabine are diarrhea , nausea , vomiting , stomatitis and hand-foot syndrome .

Example answer:
{"entities": [{"text": "capecitabine", "type": "Chemical"}, {"text": "diarrhea", "type": "Disease"}, {"text": "nausea", "type": "Disease"}, {"text": "vomiting", "type": "Disease"}, {"text": "stomatitis", "type": "Disease"}, {"text": "hand-foot syndrome", "type": "Disease"}]}

Example input:
Sentence: In conclusion mitochondrial toxicity is an early common event both in paclitaxel and cisplatin induced neurotoxicity .

Example answer:
{"entities": [{"text": "mitochondrial toxicity", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: The pathogenesis of 5-fluorouracil neurotoxicity may be due to a Krebs cycle blockade by fluoroacetate and fluorocitrate , thiamine deficiency , or dihydrouracil dehydrogenase deficiency .

Example answer:
{"entities": [{"text": "5-fluorouracil", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "fluoroacetate", "type": "Chemical"}, {"text": "fluorocitrate", "type": "Chemical"}, {"text": "thiamine", "type": "Chemical"}, {"text": "dihydrouracil", "type": "Chemical"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: Because folinic acid was unlikely to be associated with this condition , neurotoxicity due to high-dose 5-fluorouracil was highly suspected .

Example answer:
{"entities": [{"text": "folinic acid", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Input:
Sentence: To our knowledge , this is the first published case report of severe neurotoxicity caused by nelarabine in a patient who received concurrent IT chemotherapy .

## Item bc5cdr:test:4518
Example input:
Sentence: Sulfonamides and nitrofurantoins were associated with several birth defects , indicating a need for additional scrutiny .

Example answer:
{"entities": [{"text": "Sulfonamides", "type": "Chemical"}, {"text": "nitrofurantoins", "type": "Chemical"}, {"text": "birth defects", "type": "Disease"}]}

Example input:
Sentence: Unlike general toxicity data , their prenatal toxic effects were not extensively studied before .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: This toxicity appeared in patients receiving the higher doses of desferrioxamine or coincided with the normalization of ferritin or aluminium serum levels .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "desferrioxamine", "type": "Chemical"}, {"text": "aluminium", "type": "Chemical"}]}

Example input:
Sentence: The present results are consistent with the carcinogenicity experiment suggesting that different mechanisms are involved in FANFT carcinogenesis in the bladder and forestomach , and that aspirin 's effect on FANFT in the forestomach is not due to an irritant effect associated with increased cell proliferation .

Example answer:
{"entities": [{"text": "FANFT", "type": "Chemical"}, {"text": "carcinogenesis", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: Comparison of developmental toxicity of selective and non-selective cyclooxygenase-2 inhibitors in CRL : ( WI ) WUBR Wistar rats -- DFU and piroxicam study .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "DFU", "type": "Chemical"}, {"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: Preclinical toxicologic investigation suggested that a new calcium channel blocker , Ro 40-5967 , induced cardiovascular alterations in rat fetuses exposed to this agent during organogenesis .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "Ro 40-5967", "type": "Chemical"}, {"text": "cardiovascular alterations", "type": "Disease"}]}

Example input:
Sentence: Decrease of fetal length was the only signs of the DFU developmental toxicity observed in pups exposed to the highest compound dose .

Example answer:
{"entities": [{"text": "DFU", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: The major teratogenic outcome is arthrogryposis , presumably due to nicotinic receptor blockade .

Example answer:
{"entities": [{"text": "arthrogryposis", "type": "Disease"}]}

Example input:
Sentence: Both compounds caused deformations and lethality in a dose-dependent manner .

Example answer:
{"entities": [{"text": "deformations", "type": "Disease"}]}

Example input:
Sentence: The aim of the experiment was to evaluate the developmental toxicity of the non-selective ( piroxicam ) and selective ( DFU ; 5,5-dimethyl-3- ( 3-fluorophenyl ) -4- ( 4-methylsulphonyl ) phenyl-2 ( 5H ) -furanon ) COX-2 inhibitors .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "piroxicam", "type": "Chemical"}, {"text": "DFU", "type": "Chemical"}, {"text": "5,5-dimethyl-3- ( 3-fluorophenyl ) -4- ( 4-methylsulphonyl ) phenyl-2 ( 5H ) -furanon", "type": "Chemical"}]}

Input:
Sentence: Our objective in this study was to investigate whether the compounds induce developmental toxicity via the dermal route , which is more relevant to occupational exposure , hence better addressing human health risks .

## Item bc5cdr:test:4383
Example input:
Sentence: Three yr after transplantation she developed renal Fanconi syndrome with severe metabolic acidosis , hypophosphatemia , glycosuria , and aminoaciduria .

Example answer:
{"entities": [{"text": "renal Fanconi syndrome", "type": "Disease"}, {"text": "metabolic acidosis", "type": "Disease"}, {"text": "hypophosphatemia", "type": "Disease"}, {"text": "glycosuria", "type": "Disease"}, {"text": "aminoaciduria", "type": "Disease"}]}

Example input:
Sentence: Long-term intragastric application of the antiepileptic drug sodium valproate ( Vupral `` Polfa '' ) at the effective dose of 200 mg/kg b. w. once daily to rats for 1 , 3 , 6 , 9 and 12 months revealed neurological disorders indicating cerebellum damage ( `` valproate encephalopathy '' ) .

Example answer:
{"entities": [{"text": "sodium valproate", "type": "Chemical"}, {"text": "neurological disorders", "type": "Disease"}, {"text": "cerebellum damage", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Encephalopathy induced by levetiracetam added to valproate .

Example answer:
{"entities": [{"text": "Encephalopathy", "type": "Disease"}, {"text": "levetiracetam", "type": "Chemical"}, {"text": "valproate", "type": "Chemical"}]}

Example input:
Sentence: Morphological features of encephalopathy after chronic administration of the antiepileptic drug valproate to rats .

Example answer:
{"entities": [{"text": "encephalopathy", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}]}

Example input:
Sentence: FINDINGS : A 28-year-old man suffering from idiopathic epilepsy with generalized seizures was treated with LEV ( 3000 mg ) added to valproate ( VPA ) ( 2000 mg ) .

Example answer:
{"entities": [{"text": "idiopathic epilepsy", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "LEV", "type": "Chemical"}, {"text": "valproate", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}]}

Example input:
Sentence: Valproic acid induced encephalopathy -- 19 new cases in Germany from 1994 to 2003 -- a side effect associated to VPA-therapy not only in young children .

Example answer:
{"entities": [{"text": "Valproic acid", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "VPA-therapy", "type": "Chemical"}]}

Example input:
Sentence: A case of valproate-induced encephalopathy is presented .

Example answer:
{"entities": [{"text": "valproate-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Valproate-induced encephalopathy .

Example answer:
{"entities": [{"text": "Valproate-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Valproate-induced encephalopathy is a rare syndrome that may manifest in otherwise normal epileptic individuals .

Example answer:
{"entities": [{"text": "Valproate-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "epileptic", "type": "Disease"}]}

Example input:
Sentence: The possible influence of the hepatic damage , mainly hyperammonemia , upon the development of valproate encephalopathy is discussed .

Example answer:
{"entities": [{"text": "hepatic damage", "type": "Disease"}, {"text": "hyperammonemia", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Input:
Sentence: Valproate-induced hyperammonemic encephalopathy in a renal transplanted patient .

## Item bc5cdr:test:4312
Example input:
Sentence: All of the rats in the saline-treated epileptic control group developed SRS , whereas none of the BMC-treated epileptic animals had seizures in the short term ( 15 days after transplantation ) , regardless of the BMC source .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}, {"text": "SRS", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Pethidine-associated seizure in a healthy adolescent receiving pethidine for postoperative pain control .

Example answer:
{"entities": [{"text": "Pethidine-associated", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "pethidine", "type": "Chemical"}, {"text": "postoperative pain", "type": "Disease"}]}

Example input:
Sentence: Seizure end points included latency to forelimb or hindlimb clonus , latency to clonic running seizure and latency to jumping bouncing seizure .

Example answer:
{"entities": [{"text": "Seizure", "type": "Disease"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Sixty percent in Group A developed postoperative emetic symptoms , headache , or both ; 1 patient in Group B developed symptoms .

Example answer:
{"entities": [{"text": "postoperative emetic symptoms", "type": "Disease"}, {"text": "headache", "type": "Disease"}]}

Example input:
Sentence: OUTCOME : Following discontinuation of LEV , EEG and neuropsychological findings improved and seizure frequency decreased .

Example answer:
{"entities": [{"text": "LEV", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Over the long-term chronic phase ( 120 days after transplantation ) , only 25 % of BMC-treated epileptic animals had seizures , but with a lower frequency and duration compared to the epileptic control group .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Epileptic seizures following cortical application of fibrin sealants containing tranexamic acid in rats .

Example answer:
{"entities": [{"text": "Epileptic seizures", "type": "Disease"}, {"text": "tranexamic acid", "type": "Chemical"}]}

Example input:
Sentence: The in vitro data suggest that the site responsible for the decrease in seizure activity 24 h after gamma-HCH may be the GABA-A receptor-linked chloride channel .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}, {"text": "GABA-A", "type": "Chemical"}]}

Example input:
Sentence: Multivariate stepwise logistic regression analysis using preoperative and postoperative variables identified that an increase of serum creatinine compared with average at 1 year , 3 months , and 4 weeks postoperatively were independent risk factors for the development of CRF or ESRD with odds ratios of 2.6 , 2.2 , and 1.6 , respectively .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Twenty-three h postoperatively he developed a brief self-limited seizure .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}]}

Input:
Sentence: Independent predictors of postoperative seizures included age , female sex , redo cardiac surgery , calcification of ascending aorta , congestive heart failure , deep hypothermic circulatory arrest , duration of aortic cross-clamp and tranexamic acid .

## Item bc5cdr:test:3846
Example input:
Sentence: Improvement of levodopa-induced dyskinesia by propranolol in Parkinson 's disease .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "propranolol", "type": "Chemical"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: These data suggest distinct differences in the propensity to develop LIDs in monkeys with different rates of symptom progression or symptom durations prior to levodopa and demonstrate the value of these models for further studying the pathophysiology of LIDs .

Example answer:
{"entities": [{"text": "LIDs", "type": "Disease"}, {"text": "levodopa", "type": "Chemical"}]}

Example input:
Sentence: Development of levodopa-induced dyskinesias in parkinsonian monkeys may depend upon rate of symptom onset and/or duration of symptoms .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "parkinsonian", "type": "Disease"}]}

Example input:
Sentence: Monkeys with acute ( short-term ) MPTP exposure , rapid symptom onset and short symptom duration prior to initiation of levodopa therapy developed dyskinesia between 11 and 24 days of daily levodopa administration .

Example answer:
{"entities": [{"text": "MPTP", "type": "Chemical"}, {"text": "levodopa", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Repetitive transcranial magnetic stimulation for levodopa-induced dyskinesias in Parkinson 's disease .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: Levodopa-induced dyskinesias in patients with Parkinson 's disease : filling the bench-to-bedside gap .

Example answer:
{"entities": [{"text": "Levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: In contrast , monkeys with long-term MPTP exposure , slow symptom progression and/or long symptom duration prior to initiation of levodopa therapy were more resistant to developing LIDs ( e.g. , dyskinesia developed no sooner than 146 days of chronic levodopa administration ) .

Example answer:
{"entities": [{"text": "MPTP", "type": "Chemical"}, {"text": "levodopa", "type": "Chemical"}, {"text": "LIDs", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Using macaque monkeys with different types of MPTP-induced parkinsonism , the current study evaluated the degree to which rate of symptom progression , symptom severity , and response to and duration of levodopa therapy may be involved in the development of LIDs .

Example answer:
{"entities": [{"text": "MPTP-induced", "type": "Chemical"}, {"text": "parkinsonism", "type": "Disease"}, {"text": "levodopa", "type": "Chemical"}, {"text": "LIDs", "type": "Disease"}]}

Example input:
Sentence: L-DOPA-induced dyskinesia ( LID ) is among the motor complications that arise in Parkinson 's disease ( PD ) patients after a prolonged treatment with L-DOPA .

Example answer:
{"entities": [{"text": "L-DOPA-induced", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "LID", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "L-DOPA", "type": "Chemical"}]}

Example input:
Sentence: Levodopa-induced dyskinesias ( LIDs ) present a major problem for the long-term management of Parkinson 's disease ( PD ) patients .

Example answer:
{"entities": [{"text": "Levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "LIDs", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Input:
Sentence: The plasticity of primary motor cortex ( M1 ) in patients with Parkinson 's disease ( PD ) and levodopa-induced dyskinesias ( LIDs ) is severely impaired .

## Item bc5cdr:test:4338
Example input:
Sentence: Various reported side effects of fentanyl administration include chest wall rigidity , hypotension , respiratory depression , and bradycardia .

Example answer:
{"entities": [{"text": "fentanyl", "type": "Chemical"}, {"text": "chest wall rigidity", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}, {"text": "respiratory depression", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Less frequent toxic effects included thrombocytopenia , anemia , nausea , mild alopecia , phlebitis , and mucositis .

Example answer:
{"entities": [{"text": "thrombocytopenia", "type": "Disease"}, {"text": "anemia", "type": "Disease"}, {"text": "nausea", "type": "Disease"}, {"text": "alopecia", "type": "Disease"}, {"text": "phlebitis", "type": "Disease"}, {"text": "mucositis", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Minutes after oral administration , the patient developed nausea , sweating and hypotension , and finally collapsed .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Other possible adverse effects -- such as gastrointestinal disorders , orthostatic hypotension , levodopa-induced psychosis , sleep disturbances or parasomnias , or drug interactions -- also require carefully monitored individual treatment .

Example answer:
{"entities": [{"text": "gastrointestinal disorders", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "levodopa-induced", "type": "Chemical"}, {"text": "psychosis", "type": "Disease"}, {"text": "sleep disturbances", "type": "Disease"}, {"text": "parasomnias", "type": "Disease"}]}

Example input:
Sentence: Conventional agents are associated with unwanted central nervous system effects , including extrapyramidal symptoms ( EPS ) , tardive dyskinesia , sedation , and possible impairment of some cognitive measures , as well as cardiac effects , orthostatic hypotension , hepatic changes , anticholinergic side effects , sexual dysfunction , and weight gain .

Example answer:
{"entities": [{"text": "extrapyramidal symptoms", "type": "Disease"}, {"text": "EPS", "type": "Disease"}, {"text": "tardive dyskinesia", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}]}

Example input:
Sentence: Patients should be warned about the side effects of vertigo and vomiting , which subsides gradually with every new instillation , and that the tinnitus may not disappear but will be alleviated , enabling them to cope more easily with the disease and lead a more normal life .

Example answer:
{"entities": [{"text": "vertigo", "type": "Disease"}, {"text": "vomiting", "type": "Disease"}, {"text": "tinnitus", "type": "Disease"}]}

Example input:
Sentence: There were no serious clinical side effects , but dose reduction was required in two patients because of nausea .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}]}

Example input:
Sentence: The most common side-effect was diarrhoea , which resulted in cessation of therapy in 19 individuals .

Example answer:
{"entities": [{"text": "diarrhoea", "type": "Disease"}]}

Example input:
Sentence: The most common adverse events were nausea ( 17.2 % and 16.1 % ; 95 % CI , -3.7 to 6.0 ) , hiccups ( 10.7 % and 6.6 % ; 95 % CI , 0.5 to 7.8 ) , and headache ( 8.7 % and 9.9 % ; 95 % Cl , -5.0 to 2.6 ) .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "hiccups", "type": "Disease"}, {"text": "headache", "type": "Disease"}]}

Example input:
Sentence: Minor side effects included nausea ( thirteen patients ) , emesis ( eight of the thirteen patients with nausea ) , clumsiness ( evident as ataxic movements in ten patients ) , and dysphoric reaction ( one patient ) .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "emesis", "type": "Disease"}, {"text": "clumsiness", "type": "Disease"}, {"text": "ataxic movements", "type": "Disease"}, {"text": "dysphoric reaction", "type": "Disease"}]}

Input:
Sentence: Common side effects include nausea , vomiting and hypotension .

## Item bc5cdr:test:4227
Example input:
Sentence: Rats were treated with the vehicle ( 2 mL/kg of distilled water and 5 % w/v cellulose , 10 days ) , gum Arabic ( 2 mL/kg of a 10 % w/v aqueous suspension of gum Arabic powder , orally for 10 days ) , or gum Arabic concomitantly with GM ( 80mg/kg/day intramuscularly , during the last six days of the treatment period ) .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}]}

Example input:
Sentence: Rats were treated with a single IV injection of puromycin aminonucleoside , ( PAN , 7.5 mg/kg ) and 24 hour urine samples were obtained prior to sacrifice on days 3,5,7,10,17,27,41 ( N = 5-10 per group ) .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: Sodium chloride solution ( 0.9 % ) or noradrenaline in doses of 4 , 12 and 36 micrograms h-1 kg-1 was infused for five consecutive days , either intrarenally ( by a new technique ) or intravenously into rats with one kidney removed .

Example answer:
{"entities": [{"text": "Sodium chloride", "type": "Chemical"}, {"text": "noradrenaline", "type": "Chemical"}]}

Example input:
Sentence: The control rats received atropine sulfate , but also saline and olive oil instead of other antidotes and DFP , respectively .

Example answer:
{"entities": [{"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: Rats were treated with seven day intravenous infusion of fucoidan ( 30 micrograms h-1 ) or vehicle .

Example answer:
{"entities": [{"text": "fucoidan", "type": "Chemical"}]}

Example input:
Sentence: Thirty male Sprague-Dawley rats were divided randomly into four treatment groups : saline , dexamethasone ( dex ) , allopurinol plus saline , and allopurinol plus dex .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "dex", "type": "Chemical"}, {"text": "allopurinol", "type": "Chemical"}]}

Example input:
Sentence: 2 and 10 mg/kg/i.p. , or an equal volume of saline for the control group ( n = 20 ) ; 15 minutes later , all the animals were injected with a single 50 mg/kg/i.p .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : Following induction of anesthesia by fentanyl ( 0.15 mg kg ( -1 ) ) and propofol ( 2.0 mg kg ( -1 ) ) , 13 patients received phenylephrine ( 0.1 mg iv ) and 12 patients received ephedrine ( 10 mg iv ) to restore mean arterial pressure ( MAP ) .

Example answer:
{"entities": [{"text": "fentanyl", "type": "Chemical"}, {"text": "propofol", "type": "Chemical"}, {"text": "phenylephrine", "type": "Chemical"}, {"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: infusion of ketamine ( bolus 0.1 mg kg-1 over 10 min followed by infusion of 7 micrograms kg-1 min-1 ) , lidocaine 5 mg kg-1 or saline for 50 min .

Example answer:
{"entities": [{"text": "ketamine", "type": "Chemical"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: Control rats received halothane anesthesia ( 1 MAC ) for one hour , followed by SNP infusion , 40 microgram/kg/min , for 30 min , followed by a 30-min recovery period .

Example answer:
{"entities": [{"text": "halothane", "type": "Chemical"}, {"text": "SNP", "type": "Chemical"}]}

Input:
Sentence: METHODS : Rats were anaesthetised with ketamine and were given 0.5 mg/kg/min propofol in intralipid ( Group P ) , propofol in medialipid ( Group L ) , or saline ( Group C ) over 20 min .

## Item bc5cdr:test:3638
Example input:
Sentence: Initial testing in a time-dependent forgetting task employing a 24-h delay between training and testing showed that metrifonate improved object recognition ( at 10 and 30 mg/kg , p.o .

Example answer:
{"entities": [{"text": "metrifonate", "type": "Chemical"}]}

Example input:
Sentence: In the present study , we investigated whether maltolyl p-coumarate could improve cognitive decline in scopolamine-injected rats and in amyloid beta peptide ( 1-42 ) -infused rats .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "cognitive decline", "type": "Disease"}, {"text": "scopolamine-injected", "type": "Chemical"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: The present study was carried out to test the effects of L-alpha-glycerylphosphorylcholine ( L-alpha-GFC ) on memory impairment induced by scopolamine in man .

Example answer:
{"entities": [{"text": "L-alpha-glycerylphosphorylcholine", "type": "Chemical"}, {"text": "L-alpha-GFC", "type": "Chemical"}, {"text": "memory impairment", "type": "Disease"}, {"text": "scopolamine", "type": "Chemical"}]}

Example input:
Sentence: The administration of phenobarbitone and carbamazepine for 21days caused a significant impairment of learning and memory as well as an increased oxidative stress .

Example answer:
{"entities": [{"text": "phenobarbitone", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "impairment of learning and memory", "type": "Disease"}]}

Example input:
Sentence: HS diet for 4 wk caused a progressive increase in BP , protein and albumin excretion , and glomerular sclerosis in male DS rats , which were attenuated by castration .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: The extent of memory improvement evoked by DCE was 23 % at the dose of 200 mg/kg and 35 % at the dose of 400 mg/kg in young mice using elevated plus maze .

Example answer:
{"entities": [{"text": "DCE", "type": "Chemical"}]}

Example input:
Sentence: and metrifonate ( 10 mg/kg , p.o. , respectively ) reversed memory deficits induced by scopolamine and TRP depletion ( 10 mg/kg , i.p. , and 3 mg/kg , p.o. , respectively ) .

Example answer:
{"entities": [{"text": "memory", "type": "Disease"}]}

Example input:
Sentence: In contrast , learning of new tasks was enhanced and correlated with the increase of nNOS activity and the decrease of glutathione peroxidase .

Example answer:
{"entities": [{"text": "glutathione", "type": "Chemical"}]}

Example input:
Sentence: NFkappaB activity was decreased in the frontal cortex of cocaine treated rats , as well as GSH concentration and glutathione peroxidase activity in the hippocampus , whereas nNOS activity in the hippocampus was increased .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}]}

Input:
Sentence: Fourth group received a single dose of ZnSO ( 4 ) ( 0.1 micromol/10 microl normal saline , i.c.v ) then BCNU ( 20 mg/kg , i.v , once ) after 24 h. The obtained data revealed that BCNU administration resulted in deterioration of learning and short-term memory ( STM ) , as measured by using radial arm water maze , accompanied with decreased hippocampal glutathione reductase ( GR ) activity and reduced glutathione ( GSH ) content .

## Item bc5cdr:test:4511
Example input:
Sentence: Under such conditions , angiotensin II receptor blockade by losartan probably induced a critical fall in glomerular filtration pressure .

Example answer:
{"entities": [{"text": "angiotensin II", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : The rate of contrast-induced nephropathy , defined by multiple end points , is not statistically different after the intraarterial administration of iopamidol or iodixanol to high-risk patients , with or without diabetes mellitus .

Example answer:
{"entities": [{"text": "nephropathy", "type": "Disease"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}, {"text": "diabetes mellitus", "type": "Disease"}]}

Example input:
Sentence: In patients with diabetes , SCr increases > or = 0.5 mg/dL were 5.1 % ( 4 of 78 patients ) with iopamidol and 13.0 % ( 12 of 92 patients ) with iodixanol ( P=0.11 ) , whereas SCr increases > or = 25 % were 10.3 % and 15.2 % , respectively ( P=0.37 ) .

Example answer:
{"entities": [{"text": "diabetes", "type": "Disease"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}]}

Example input:
Sentence: We studied three calcium channel blockers of different structure , nifedipine , diltiazem , and verapamil , along with the new agent .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "nifedipine", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: Mean post-SCr increases were significantly less with iopamidol ( all patients : 0.07 versus 0.12 mg/dL , 6.2 versus 10.6 micromol/L , P=0.03 ; patients with diabetes : 0.07 versus 0.16 mg/dL , 6.2 versus 14.1 micromol/L , P=0.01 ) .

Example answer:
{"entities": [{"text": "iopamidol", "type": "Chemical"}, {"text": "diabetes", "type": "Disease"}]}

Example input:
Sentence: While contractions to carbachol and ATP were the same in inflamed and in control strips when related to a reference potassium response , isoprenaline-induced relaxations were smaller in inflamed strips .

Example answer:
{"entities": [{"text": "carbachol", "type": "Chemical"}, {"text": "ATP", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}, {"text": "isoprenaline-induced", "type": "Chemical"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: A low incidence of cardiovascular malformations was observed after exposure to each of the four calcium channel blockers , but this incidence was statistically significant only for verapamil and nifedipine .

Example answer:
{"entities": [{"text": "cardiovascular malformations", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: As a consequence of blocking I ( f ) , clonidine reduced the slope of the diastolic depolarization and the frequency of pacemaker potentials in sinoatrial node cells from wild-type and alpha2ABC-knockout mice .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: We postulate that by virtue of its direct blocking action on IKr , ketoconazole alone may prolong QT interval and induce TdP .

Example answer:
{"entities": [{"text": "ketoconazole", "type": "Chemical"}, {"text": "TdP", "type": "Disease"}]}

Input:
Sentence: IKr and IKs blockers concentration-dependently prolonged corrected FPD ( FPDc ) , whereas Ca ( 2+ ) channel blockers concentration-dependently shortened FPDc .

## Item bc5cdr:test:4190
Example input:
Sentence: In SE survivors , similar stimulation resulted in a population spike followed , at a variable latency , by negative DC shifts and repetitive afterdischarges of 3-60 s duration , which were blocked by ionotropic glutamate receptor antagonists .

Example answer:
{"entities": [{"text": "SE", "type": "Disease"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: 9 ( 2006 ) , 917 ] recently identified the microglial-specific fractalkine receptor ( CX3CR1 ) as an important mediator of MPTP-induced neurodegeneration of DA neurons .

Example answer:
{"entities": [{"text": "MPTP-induced", "type": "Chemical"}, {"text": "neurodegeneration", "type": "Disease"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: These data might indicate that the generation of reactive oxygen species and activation of NF-kappaB plays a more central role in seizure-associated neuronal damage in the temporal cortex as compared to the hippocampal hilus .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "seizure-associated", "type": "Disease"}, {"text": "neuronal damage", "type": "Disease"}]}

Example input:
Sentence: Striatal microglia expressing eGFP constitutively show morphological changes after METH that are characteristic of activation .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}]}

Example input:
Sentence: The present study was carried out to test the effects of L-alpha-glycerylphosphorylcholine ( L-alpha-GFC ) on memory impairment induced by scopolamine in man .

Example answer:
{"entities": [{"text": "L-alpha-glycerylphosphorylcholine", "type": "Chemical"}, {"text": "L-alpha-GFC", "type": "Chemical"}, {"text": "memory impairment", "type": "Disease"}, {"text": "scopolamine", "type": "Chemical"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: Both , production of reactive oxygen species as well as activation of NF-kappaB have been implicated in severe neuronal damage in different sub-regions of the hippocampus as well as in the surrounding cortices .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "neuronal damage", "type": "Disease"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "Disease"}, {"text": "METH", "type": "Chemical"}, {"text": "MPTP", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "METH-induced", "type": "Chemical"}]}

Example input:
Sentence: Furthermore , it appears that striatal-resident microglia respond to METH with an activation cascade and then return to a surveying state without undergoing apoptosis or migration .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Input:
Sentence: Present study clearly suggests that glial activation and post synaptic neurotoxicity are the key factors in STZ induced memory impairment and neuronal cell death .

## Item bc5cdr:test:4555
Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: The pooled statistical analysis for ventricular septal ( VSD ) and midline ( MD ) defects was performed for rat fetuses exposed to piroxicam , selective and non-selective COX-2 inhibitor based on present and historic data .

Example answer:
{"entities": [{"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Seventeen subjects who were genotyped as CYP2D6 extensive metabolizers were enrolled in this randomized , open-label , crossover study to receive a single oral dose of desipramine ( 50 mg ) on two separate occasions , once alone and once after multiple doses of cinacalcet ( 90 mg for 7 days ) .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}]}

Example input:
Sentence: In contrast , SSR103800 failed to affect hyperactivity induced by amphetamine or naturally observed in dopamine transporter ( DAT ( -/- ) ) knockout mice ( 10-30 mg/kg p.o . ) .

Example answer:
{"entities": [{"text": "SSR103800", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: Using this rationale , the 8-aminoquinoline WR242511 , a potent long-lasting MHb former in rodents and beagle dogs , was studied in the rhesus monkey for advanced development as a potential CN pretreatment .

Example answer:
{"entities": [{"text": "8-aminoquinoline", "type": "Chemical"}, {"text": "WR242511", "type": "Chemical"}]}

Example input:
Sentence: Swiss albino mice prepared with intrajugular catheters were tested in photocell cages after administration of 93 mg/kg ( LD50 ) of cocaine and GNC92H2 infusions ranging from 30 to 190 mg/kg .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "GNC92H2", "type": "Chemical"}]}

Example input:
Sentence: It was administered by 15 min infusion to 16 evaluable patients with non-small cell lung cancer ( NSCLC ) ( 7 with no prior treatment , 9 patients in relapse following surgery/radiotherapy ) at a dose ( 648 mg/m2 divided over 3 days , repeated every 3 weeks ) determined by phase I trial .

Example answer:
{"entities": [{"text": "non-small cell lung cancer", "type": "Disease"}, {"text": "NSCLC", "type": "Disease"}]}

Example input:
Sentence: To determine mitochondrial events from HAART in vivo , 8-week-old hemizygous transgenic AIDS mice ( NL4-3Delta gag/pol ; TG ) and wild-type FVB/n littermates were treated with the HAART combination of zidovudine , lamivudine , and indinavir or vehicle control for 10 days or 35 days .

Example answer:
{"entities": [{"text": "AIDS", "type": "Disease"}, {"text": "zidovudine", "type": "Chemical"}, {"text": "lamivudine", "type": "Chemical"}, {"text": "indinavir", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Thirty-five Wistar rats were given 1.5 mg/kg DOX , i.v. , weekly for up to 8 weeks for a total cumulative dose of 12 mg/kg BW .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "Chemical"}]}

Input:
Sentence: METHODS AND RESULTS : Two-week-old MHC-CB7 mice ( which express dominant-interfering p53 in cardiomyocytes ) and their non-transgenic ( NON-TXG ) littermates received weekly DOX injections for 5 weeks ( 25 mg/kg cumulative dose ) .

## Item bc5cdr:test:4546
Example input:
Sentence: The extent of inhibition of brain cholinesterase activity evoked by DCE at the dose of 400 mg/kg was 22 % in young and 19 % in aged mice .

Example answer:
{"entities": [{"text": "DCE", "type": "Chemical"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Male Sprague-Dawley rats were treated with D-penicillamine ( D-pen ) 500 mg/kg/day for 10 or 42 days .

Example answer:
{"entities": [{"text": "D-penicillamine", "type": "Chemical"}, {"text": "D-pen", "type": "Chemical"}]}

Example input:
Sentence: In this study , the severity of response to other seizure-inducing agents was tested in mice 1 and 24 h after intraperitoneal administration of 80 mg/kg gamma-HCH .

Example answer:
{"entities": [{"text": "seizure-inducing", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}]}

Example input:
Sentence: Mature male and female mice from six inbred stains were tested for susceptibility to behavioral seizures induced by a single injection of cocaine .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Three hundred fifty-five adult male CSS mice , 58 B6 , and 39 A/J were tested for susceptibility to pilocarpine-induced seizures .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: In vitro , gamma-HCH , pentylenetetrazol and picrotoxin were shown to inhibit 3H-TBOB binding in mouse whole brain , with IC50 values of 4.6 , 404 and 9.4 microM , respectively .

Example answer:
{"entities": [{"text": "gamma-HCH", "type": "Chemical"}, {"text": "pentylenetetrazol", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "3H-TBOB", "type": "Chemical"}]}

Example input:
Sentence: Gamma-hexachlorocyclohexane ( gamma-HCH ) , the active ingredient of the insecticide lindane , has been shown to decrease seizure threshold to pentylenetrazol ( PTZ ) 3 h after exposure to gamma-HCH and conversely increase threshold to PTZ-induced seizures 24 h after exposure to gamma-HCH ( Vohland et al .

Example answer:
{"entities": [{"text": "Gamma-hexachlorocyclohexane", "type": "Chemical"}, {"text": "gamma-HCH", "type": "Chemical"}, {"text": "lindane", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "PTZ", "type": "Chemical"}, {"text": "PTZ-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Swiss albino mice prepared with intrajugular catheters were tested in photocell cages after administration of 93 mg/kg ( LD50 ) of cocaine and GNC92H2 infusions ranging from 30 to 190 mg/kg .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "GNC92H2", "type": "Chemical"}]}

Example input:
Sentence: In the absence of caffeine , acetaminophen ( up to 300 mg/kg ) did not modify the seizures induced by maximal electroshock and did not alter the convulsant dose of pentylenetetrezol in mice ( tests performed by the Anticonvulsant Screening Project of NINCDS ) .

Example answer:
{"entities": [{"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "pentylenetetrezol", "type": "Chemical"}]}

Input:
Sentence: Male C57BL/6 mice were administered with subconvulsive dose of pentylenetetrazole ( 37 mg/kg , i.p . )

## Item bc5cdr:test:4275
Example input:
Sentence: Severe and long lasting cholestasis after high-dose co-trimoxazole treatment for Pneumocystis pneumonia in HIV-infected patients -- a report of two cases .

Example answer:
{"entities": [{"text": "cholestasis", "type": "Disease"}, {"text": "co-trimoxazole", "type": "Chemical"}, {"text": "Pneumocystis pneumonia", "type": "Disease"}, {"text": "HIV-infected", "type": "Disease"}]}

Example input:
Sentence: This observation demonstrates that prolonged cholestasis can follow troleandomycin-induced acute hepatitis .

Example answer:
{"entities": [{"text": "cholestasis", "type": "Disease"}, {"text": "troleandomycin-induced", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: We investigated an epidemic of liver disease in nine industrial workers who had had repeated accidental exposure to a mixture of 1,1-dichloro-2,2,2-trifluoroethane ( HCFC 123 ) and 1-chloro-1,2,2,2-tetrafluoroethane ( HCFC 124 ) .

Example answer:
{"entities": [{"text": "liver disease", "type": "Disease"}, {"text": "1,1-dichloro-2,2,2-trifluoroethane", "type": "Chemical"}, {"text": "HCFC 123", "type": "Chemical"}, {"text": "1-chloro-1,2,2,2-tetrafluoroethane", "type": "Chemical"}, {"text": "HCFC 124", "type": "Chemical"}]}

Example input:
Sentence: The remaining patient in the series developed fulminant hepatitis when the drug was accidentally recommenced 1 year after a prior episode of methyldopa-induced hepatitis .

Example answer:
{"entities": [{"text": "fulminant hepatitis", "type": "Disease"}, {"text": "methyldopa-induced", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: Minimal cholestasis was seen in two cases and portal fibrosis of a reversible degree in eight .

Example answer:
{"entities": [{"text": "cholestasis", "type": "Disease"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: We report the case of a patient who developed acute hepatitis with extensive hepatocellular necrosis , 7 months after the onset of administration of clotiazepam , a thienodiazepine derivative .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}, {"text": "extensive hepatocellular necrosis", "type": "Disease"}, {"text": "clotiazepam", "type": "Chemical"}, {"text": "thienodiazepine", "type": "Chemical"}]}

Example input:
Sentence: DISCUSSION : Cholestatic hepatitis is a rare complication of the antiplatelet agent ticlopidine ; several cases have been reported but few in the English literature .

Example answer:
{"entities": [{"text": "ticlopidine", "type": "Chemical"}]}

Example input:
Sentence: Despite therapy with ursodeoxycholic acid , prednisone , and then tacrolimus , her cholestatic disease was unrelenting , with cirrhosis shown by biopsy 6 months after presentation .

Example answer:
{"entities": [{"text": "ursodeoxycholic acid", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "cholestatic disease", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}]}

Example input:
Sentence: Here , we report two cases of severely immunocompromised HIV-infected patients who developed severe intrahepatic cholestasis , and in one patient lesions mimicking liver abscess formation on radiologic exams , during co-trimoxazole treatment for PCP .

Example answer:
{"entities": [{"text": "HIV-infected", "type": "Disease"}, {"text": "intrahepatic cholestasis", "type": "Disease"}, {"text": "liver abscess", "type": "Disease"}, {"text": "co-trimoxazole", "type": "Chemical"}, {"text": "PCP", "type": "Disease"}]}

Example input:
Sentence: Two subsets of patients were identified from this latter group : the first included four patients ( 5 % of the total population ) who developed major toxicity resulting in Fanconi 's syndrome ( TDFS ) ; and the second group included five patients with elevated beta 2 microglobulinuria and low phosphate reabsorption .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "Fanconi 's syndrome", "type": "Disease"}, {"text": "TDFS", "type": "Disease"}, {"text": "phosphate", "type": "Chemical"}]}

Input:
Sentence: We present a case of yellow phosphorus poisoning in which a patient presented with florid clinical features of cholestasis highlighting the fact that cholestasis can rarely be a presenting feature of yellow phosphorus hepatotoxicity .

## Item bc5cdr:test:4636
Example input:
Sentence: The MFL regimen achieves little palliative benefit and induces severe toxicity at a fairly high rate .

Example answer:
{"entities": [{"text": "MFL regimen", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Associated factors were co-treatment with other centrally antimuscarinic agents , poor clinical outcome , older age , and longer hospitalization ( by 17.5 days , increasing cost ) ; sex , diagnosis or medical co-morbidity , and daily clozapine dose , which fell with age , were unrelated .

Example answer:
{"entities": [{"text": "clozapine", "type": "Chemical"}]}

Example input:
Sentence: The differences in mortality and morbidity between the two groups were not significant .

Example answer:
{"entities": []}

Example input:
Sentence: In multivariate analysis , three factors independently predicted mortality : serum bilirubin ( > or=10.8 mg/dL ) , prothrombin time ( PT ) prolongation ( > or=26 seconds ) , and grade III/IV encephalopathy at presentation .

Example answer:
{"entities": [{"text": "bilirubin", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Because the mortality rate is so high , determining which factors are predictors is less important .

Example answer:
{"entities": []}

Example input:
Sentence: Atrial fibrillation is associated with substantial morbidity and mortality .

Example answer:
{"entities": [{"text": "Atrial fibrillation", "type": "Disease"}]}

Example input:
Sentence: Outcome improvement with more intensive chemotherapy has significantly increased the incidence and severity of adverse events .

Example answer:
{"entities": []}

Example input:
Sentence: The development of ESRD decreases survival , particularly in those patients treated with dialysis only .

Example answer:
{"entities": [{"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Treatment duration longer than 1 year was associated with an eightfold increased risk ( OR = 7.7 , 95 % CI 0.9 to 69 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Delirium was inconsistently recognized clinically in milder cases and was associated with increased length-of-stay and higher costs , and inferior clinical outcome .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}]}

Input:
Sentence: It increases mortality , hospital length of stay , and costs .

## Item bc5cdr:test:4457
Example input:
Sentence: Patients tapped faster after propranolol than diazepam and they were more sedated after diazepam than propranolol .

Example answer:
{"entities": [{"text": "propranolol", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: The hypotensive episodes were severe enough to require vasopressor administration .

Example answer:
{"entities": [{"text": "hypotensive", "type": "Disease"}]}

Example input:
Sentence: A frequency of bradycardia of 50 % was noted in the control group , but this was not significantly different from the frequency with the active drugs .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Since the introduction of angiotensin converting enzyme ( ACE ) inhibitors into the adjunctive treatment of patients with congestive heart failure , cases of severe hypotension , especially on the first day of treatment , have occasionally been reported .

Example answer:
{"entities": [{"text": "angiotensin converting enzyme ( ACE ) inhibitors", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: immediately before the induction of anaesthesia , to prevent arrhythmia and bradycardia following repeated doses of suxamethonium in children , was studied .

Example answer:
{"entities": [{"text": "arrhythmia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: Bromocriptine-induced hypotension was unaffected by isoproterenol pretreatment , while tachycardia was reversed to significant bradycardia , an effect that was partly reduced by i.v .

Example answer:
{"entities": [{"text": "Bromocriptine-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: RESULTS : There were more incidents of bradycardia in subjects treated with clonidine compared with those not treated with clonidine ( 17.5 % versus 3.4 % ; p =.02 ) , but no other significant group differences regarding electrocardiogram and other cardiovascular outcomes .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: The patient had no apparent associated conditions which might have predisposed him to the development of bradyarrhythmias ; and , thus , this probably represented a true idiosyncrasy to lidocaine .

Example answer:
{"entities": [{"text": "bradyarrhythmias", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: Physicians prescribing clonidine should monitor for bradycardia and advise patients about the high likelihood of initial drowsiness .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "drowsiness", "type": "Disease"}]}

Input:
Sentence: Providers should similarly consider the likelihood of hypotension or bradycardia before starting either sedative .

## Item bc5cdr:test:4422
Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: Application of a delayed feedback signal , in the form of a 2-h systemic corticosterone infusion in urethane-anesthetized rats with pharmacological blockade of glucocorticoid synthesis , is without effect on the resting secretion of arginine vasopressin and oxytocin at any corticosterone feedback dose tested .

Example answer:
{"entities": [{"text": "corticosterone", "type": "Chemical"}, {"text": "urethane-anesthetized", "type": "Chemical"}, {"text": "arginine vasopressin", "type": "Chemical"}, {"text": "oxytocin", "type": "Chemical"}]}

Example input:
Sentence: The aldosterone-sensitive serum- and glucocorticoid-inducible kinase SGK1 has been shown to participate in the stimulation of ENaC and to mediate renal fibrosis following mineralocorticoid and salt excess .

Example answer:
{"entities": [{"text": "aldosterone-sensitive", "type": "Chemical"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Although intravitreal aminoglycosides have substantially improved visual prognosis in endophthalmitis , macular infarction may impair full visual recovery .

Example answer:
{"entities": [{"text": "aminoglycosides", "type": "Chemical"}, {"text": "endophthalmitis", "type": "Disease"}, {"text": "infarction", "type": "Disease"}]}

Example input:
Sentence: Eight glaucomatous patients chronically treated with timolol 0.5 % /12h , suffering from depression diagnosed through DMS-III-R criteria , were included in the study .

Example answer:
{"entities": [{"text": "glaucomatous", "type": "Disease"}, {"text": "timolol", "type": "Chemical"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: The ocular myasthenia associated with combination therapy of pegylated IFN alpha-2b and ribavirin for CHC is very rarely reported ; therefore , we present this case with a review of the various eye complications of IFN therapy .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "CHC", "type": "Disease"}, {"text": "IFN", "type": "Chemical"}]}

Example input:
Sentence: Estrogens protect ovariectomized rats from hippocampal injury induced by kainic acid-induced status epilepticus ( SE ) .

Example answer:
{"entities": [{"text": "hippocampal injury", "type": "Disease"}, {"text": "kainic", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Sulpiride induced only SOCS-1 in the medial preoptic area , where GnRH neurons are regulated , but in the arcuate nucleus and choroid plexus , PRL-R , SOCS-3 , and CIS mRNA levels were also induced .

Example answer:
{"entities": [{"text": "Sulpiride", "type": "Chemical"}]}

Example input:
Sentence: Although the intraocular pressure elevation caused by secondary acute angle-closure glaucoma decreased and ocular pain diminished , inexorable papilledema and exudative retinal detachment continued for 3 weeks .

Example answer:
{"entities": [{"text": "glaucoma", "type": "Disease"}, {"text": "ocular pain", "type": "Disease"}, {"text": "papilledema", "type": "Disease"}, {"text": "retinal detachment", "type": "Disease"}]}

Input:
Sentence: Ocular-specific ER stress reduction rescues glaucoma in murine glucocorticoid-induced glaucoma .

## Item bc5cdr:test:4641
Example input:
Sentence: In the bolus group , 26.0 % ( 13/50 ) had akathisia compared with 32.7 % ( 16/49 ) in the infusion group ( Delta=-6.7 % ; 95 % confidence interval [ CI ] -24.6 % to 11.2 % ) .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: An objective response was observed in 73.5 % of the patients ( 95 % confidence interval [ CI ] , 55.6-87.1 % ) , including 4 complete responses ( 11.7 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: The semi-quantitative scoring was significantly worst in the group treated with CsA plus SRL ( P < 0.001 compared with controls ) and the analysis of the total grade of fibrosis also showed the highest proportion in the same group and was significantly different from controls ( P < 0.02 ) .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: The incidence of adverse events in the 2 groups was similar during the first 2 weeks of product use ( evaluation population : 55.3 % lozenge , 54.7 % gum ) , as well as during the entire study ( safety population : 63.8 % and 58.6 % , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: Patients with a DBP reduction of > or =20 % in the high-dose group had a significantly increased adjusted OR for the compound outcome variable death or dependency ( Barthel Index < 60 ) ( n/N=25/26 , OR 10 .

Example answer:
{"entities": [{"text": "DBP reduction", "type": "Disease"}, {"text": "death", "type": "Disease"}]}

Example input:
Sentence: In the five rats that developed somatic rigidity , ICP and CVP increased significantly above baseline ( delta ICP 7.5 +/- 1.0 mmHg , delta CVP 5.9 +/- 1.3 mmHg ) .

Example answer:
{"entities": [{"text": "somatic rigidity", "type": "Disease"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}, {"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: Two groups of supine subjects were studied under placebo-controlled conditions , one during the night , when sleeping ( n = 7 ) and the other at daytime , when awake ( n = 6 ) .

Example answer:
{"entities": []}

Example input:
Sentence: PG was well tolerated by all 54 patients .

Example answer:
{"entities": [{"text": "PG", "type": "Chemical"}]}

Example input:
Sentence: Of 24 evaluable patients , two achieved a complete remission and one achieved a partial remission for an overall response rate of 12.5 % ( 95 % confidence interval : 2.6-32.4 % ) .

Example answer:
{"entities": []}

Input:
Sentence: Patients with an adherence to SOP > 70 % were classified into the high adherence group ( HAG ) and patients with an adherence of < 70 % into the low adherence group ( LAG ) .

## Item bc5cdr:test:4274
Example input:
Sentence: We describe a 15-yr-old girl who had orthotopic liver transplantation because of Wilson 's disease .

Example answer:
{"entities": [{"text": "Wilson 's disease", "type": "Disease"}]}

Example input:
Sentence: In this latter patient , and in 2 others , the causal relationship between methyldopa and hepatic dysfunction was proved with the recurrence of hepatitis within 2 weeks of re-exposure to the drug .

Example answer:
{"entities": [{"text": "methyldopa", "type": "Chemical"}, {"text": "hepatic dysfunction", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: When CPA , diazepam or 2PAM was given immediately after DFP-atropine , these treatments prevented , delayed or shortened the occurrence of serious signs of poisoning .

Example answer:
{"entities": [{"text": "CPA", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "DFP-atropine", "type": "Chemical"}, {"text": "poisoning", "type": "Disease"}]}

Example input:
Sentence: An 80-yr-old man developed acute hepatitis shortly after ingesting oral ceftriaxone .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}, {"text": "ceftriaxone", "type": "Chemical"}]}

Example input:
Sentence: Based on a score of 8 on the Naranjo adverse drug reaction probability scale , telithromycin was the probable cause of acute hepatitis in this patient , and pathological findings suggested drug-induced toxic hepatitis .

Example answer:
{"entities": [{"text": "adverse drug reaction", "type": "Disease"}, {"text": "telithromycin", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}, {"text": "toxic hepatitis", "type": "Disease"}]}

Example input:
Sentence: Clotiazepam-induced acute hepatitis .

Example answer:
{"entities": [{"text": "Clotiazepam-induced", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: A patient with cryptogenic cirrhosis and disseminated sporotrichosis developed acute renal failure immediately following the administration of amphotericin B on four separate occasions .

Example answer:
{"entities": [{"text": "cirrhosis", "type": "Disease"}, {"text": "sporotrichosis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}]}

Example input:
Sentence: We investigated an epidemic of liver disease in nine industrial workers who had had repeated accidental exposure to a mixture of 1,1-dichloro-2,2,2-trifluoroethane ( HCFC 123 ) and 1-chloro-1,2,2,2-tetrafluoroethane ( HCFC 124 ) .

Example answer:
{"entities": [{"text": "liver disease", "type": "Disease"}, {"text": "1,1-dichloro-2,2,2-trifluoroethane", "type": "Chemical"}, {"text": "HCFC 123", "type": "Chemical"}, {"text": "1-chloro-1,2,2,2-tetrafluoroethane", "type": "Chemical"}, {"text": "HCFC 124", "type": "Chemical"}]}

Example input:
Sentence: The remaining patient in the series developed fulminant hepatitis when the drug was accidentally recommenced 1 year after a prior episode of methyldopa-induced hepatitis .

Example answer:
{"entities": [{"text": "fulminant hepatitis", "type": "Disease"}, {"text": "methyldopa-induced", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: We report the case of a patient who developed acute hepatitis with extensive hepatocellular necrosis , 7 months after the onset of administration of clotiazepam , a thienodiazepine derivative .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}, {"text": "extensive hepatocellular necrosis", "type": "Disease"}, {"text": "clotiazepam", "type": "Chemical"}, {"text": "thienodiazepine", "type": "Chemical"}]}

Input:
Sentence: Poisoning with yellow phosphorus classically manifests with acute hepatitis leading to acute liver failure which may need liver transplantation .

## Item bc5cdr:test:4373
Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Example input:
Sentence: Therefore , in adult patients affected by HUS , dialysis should not be discontinued prematurely ; moreover , bilateral nephrectomy , for treatment of severe hypertension and microangiopathic hemolytic anemia , should be performed with caution .

Example answer:
{"entities": [{"text": "HUS", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "microangiopathic hemolytic anemia", "type": "Disease"}]}

Example input:
Sentence: Five patients with carcinoma developed thrombotic microangiopathy ( characterized by renal insufficiency , microangiopathic hemolytic anemia , and usually thrombocytopenia ) after treatment with cisplatin , bleomycin , and a vinca alkaloid .

Example answer:
{"entities": [{"text": "carcinoma", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "microangiopathic hemolytic anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "bleomycin", "type": "Chemical"}, {"text": "vinca alkaloid", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : At 13 years after OLTX , the incidence of severe renal dysfunction was 18.1 % ( CRF 8.6 % and ESRD 9.5 % ) .

Example answer:
{"entities": [{"text": "renal dysfunction", "type": "Disease"}, {"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: The renal function of 74 children with malignant mesenchymal tumors in complete remission and who have received the same ifosfamide chemotherapy protocol ( International Society of Pediatric Oncology Malignant Mesenchymal Tumor Study 84 [ SIOP MMT 84 ] ) were studied 1 year after the completion of treatment .

Example answer:
{"entities": [{"text": "malignant mesenchymal tumors", "type": "Disease"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "Malignant Mesenchymal Tumor", "type": "Disease"}]}

Example input:
Sentence: She subsequently died some 5 weeks after the commencement of her drug therapy.Post-mortem examination showed evidence of massive hepatocellular necrosis , acute hypersensitivity myocarditis , focal acute tubulo-interstitial nephritis and extensive bone marrow necrosis , with no evidence of malignancy .

Example answer:
{"entities": [{"text": "massive hepatocellular necrosis", "type": "Disease"}, {"text": "myocarditis", "type": "Disease"}, {"text": "nephritis", "type": "Disease"}, {"text": "bone marrow necrosis", "type": "Disease"}, {"text": "malignancy", "type": "Disease"}]}

Example input:
Sentence: Despite therapy with ursodeoxycholic acid , prednisone , and then tacrolimus , her cholestatic disease was unrelenting , with cirrhosis shown by biopsy 6 months after presentation .

Example answer:
{"entities": [{"text": "ursodeoxycholic acid", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "cholestatic disease", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}]}

Example input:
Sentence: Introduction of tacrolimus as an alternative immunosuppressive agent resulted in the recurrence of TMA and the subsequent loss of the renal allograft .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "TMA", "type": "Disease"}]}

Example input:
Sentence: The patient cohort ( 14 men , 11 women ) was treated with SRL as conversion therapy , due to chronic allograft nephropathy ( CAN ) ( n = 15 ) neoplasia ( n = 8 ) ; Kaposi 's sarcoma , Four skin cancers , One intestinal tumors , One renal cell carsinom ) or BK virus nephropathy ( n = 2 ) .

Example answer:
{"entities": [{"text": "SRL", "type": "Chemical"}, {"text": "chronic allograft nephropathy", "type": "Disease"}, {"text": "CAN", "type": "Disease"}, {"text": "neoplasia", "type": "Disease"}, {"text": "Kaposi 's sarcoma", "type": "Disease"}, {"text": "skin cancers", "type": "Disease"}, {"text": "intestinal tumors", "type": "Disease"}, {"text": "renal cell carsinom", "type": "Disease"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: We report a case of a living donor renal transplant recipient who developed cyclosporine-induced TMA that responded to the withdrawal of cyclosporine in conjunction with plasmapheresis and fresh frozen plasma replacement therapy .

Example answer:
{"entities": [{"text": "cyclosporine-induced", "type": "Chemical"}, {"text": "TMA", "type": "Disease"}, {"text": "cyclosporine", "type": "Chemical"}]}

Input:
Sentence: At the time of treatment , she was on continuous renal replacement therapy due to sequelae of tumor lysis syndrome ( TLS ) .

## Item bc5cdr:test:4489
Example input:
Sentence: Orthostatic hypotension was ameliorated 4 days after withdrawal of selegiline and totally abolished 7 days after discontinuation of the drug .

Example answer:
{"entities": [{"text": "Orthostatic hypotension", "type": "Disease"}, {"text": "selegiline", "type": "Chemical"}]}

Example input:
Sentence: Five patients with carcinoma developed thrombotic microangiopathy ( characterized by renal insufficiency , microangiopathic hemolytic anemia , and usually thrombocytopenia ) after treatment with cisplatin , bleomycin , and a vinca alkaloid .

Example answer:
{"entities": [{"text": "carcinoma", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "microangiopathic hemolytic anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "bleomycin", "type": "Chemical"}, {"text": "vinca alkaloid", "type": "Chemical"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: Adriamycin ( 50 mg/50 ml ) was administered intravesically within 24 h after transurethral resection of TA-T1 ( O-A ) bladder tumors .

Example answer:
{"entities": [{"text": "Adriamycin", "type": "Chemical"}, {"text": "bladder tumors", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Unexpectedly high concentrations of argatroban were measured in these samples ( range , 0-32 microg/mL ) , and a prolonged plasma argatroban half life ( t ( 1/2 ) ) of 514 minutes was observed ( published elimination t ( 1/2 ) is 39-51 minutes [ < or = 181 minutes with hepatic impairment ] ) .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "hepatic impairment", "type": "Disease"}]}

Example input:
Sentence: This is the first report to measure plasma argatroban concentration in the context of CPB and extended coagulopathy .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "coagulopathy", "type": "Disease"}]}

Example input:
Sentence: Prolonged elevation of plasma argatroban in a cardiac transplant patient with a suspected history of heparin-induced thrombocytopenia with thrombosis .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: In the following report , a 65-year-old critically ill patient with a suspected history of HITT was administered argatroban for anticoagulation on bypass during heart transplantation .

Example answer:
{"entities": [{"text": "critically ill", "type": "Disease"}, {"text": "HITT", "type": "Disease"}, {"text": "argatroban", "type": "Chemical"}]}

Example input:
Sentence: STUDY DESIGN AND METHODS : Plasma samples from before and after CPB were analyzed postoperatively for argatroban concentration using a modified ecarin clotting time ( ECT ) assay .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}]}

Input:
Sentence: Postthrombectomy continuous CDT with alteplase was commenced while argatroban was withheld , and complete patency of the SVC and central veins was achieved after three days of therapy .

## Item bc5cdr:test:4435
Example input:
Sentence: Comparative cognitive and subjective side effects of immediate-release oxycodone in healthy middle-aged and older adults .

Example answer:
{"entities": [{"text": "oxycodone", "type": "Chemical"}]}

Example input:
Sentence: Acute antinociceptive effects of the combination were partially prevented by 3.2 mg/kg naloxone s.c. ( P < 0.05 ) , suggesting the partial involvement of the opioidergic system in the synergism observed .

Example answer:
{"entities": [{"text": "naloxone", "type": "Chemical"}]}

Example input:
Sentence: This study measured the objective and subjective neurocognitive effects of a single 10-mg dose of immediate-release oxycodone in healthy , older ( > 65 years ) , and middle-aged ( 35 to 55 years ) adults who were not suffering from chronic or significant daily pain .

Example answer:
{"entities": [{"text": "oxycodone", "type": "Chemical"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: Fentanyl , an opioid analgesic , is frequently used in the neonatal intensive care unit setting for these very purposes .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "Chemical"}]}

Example input:
Sentence: This study suggests that for healthy older adults who are not suffering from chronic pain , neurocognitive and pharmacodynamic changes in response to a 10-mg dose of immediate-release oxycodone are similar to those observed for middle-aged adults .

Example answer:
{"entities": [{"text": "chronic pain", "type": "Disease"}, {"text": "oxycodone", "type": "Chemical"}]}

Example input:
Sentence: Combining the two fentanyl groups revealed further significant benefits from the avoidance of opioids , reducing postoperative nausea and vomiting and nausea prior to discharge from 35 % and 33 % to 22 % and 19 % ( P = 0.049 and P = 0.035 ) , respectively , while nausea in the first 24 h was decreased from 42 % to 27 % ( P = 0.034 ) .

Example answer:
{"entities": [{"text": "fentanyl", "type": "Chemical"}, {"text": "postoperative nausea and vomiting", "type": "Disease"}, {"text": "nausea", "type": "Disease"}]}

Example input:
Sentence: This is a case report of euphoria and choreoathetoid movements both transiently induced by rapid adjustment to the selective mu-opioid receptor agonist methadone in an inpatient previously abusing heroine and cocaine .

Example answer:
{"entities": [{"text": "choreoathetoid movements", "type": "Disease"}, {"text": "methadone", "type": "Chemical"}, {"text": "heroine", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Prompt restoration of renal function followed drug withdrawal , while re-exposure to a single dose of indomethacin caused recurrence of acute reversible oliguria .

Example answer:
{"entities": [{"text": "indomethacin", "type": "Chemical"}, {"text": "oliguria", "type": "Disease"}]}

Example input:
Sentence: Animal and clinical studies have suggested that N-methyl-D-aspartate ( NMDA ) antagonists , such as ketamine , may be effective in improving opioid analgesia in difficult pain syndromes , such as neuropathic pain .

Example answer:
{"entities": [{"text": "N-methyl-D-aspartate", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "ketamine", "type": "Chemical"}, {"text": "pain", "type": "Disease"}, {"text": "neuropathic pain", "type": "Disease"}]}

Example input:
Sentence: Therefore , clinicians should not avoid prescribing oral opioids to older adults based on the belief that older adults are at higher risk for side effects than younger adults .

Example answer:
{"entities": []}

Input:
Sentence: OIH can limit the clinical use of opioid analgesics and complicate withdrawal from opioid addiction .

## Item bc5cdr:test:4485
Example input:
Sentence: We describe a patient who developed dilated cardiomyopathy and clinical congestive heart failure after 2 months of therapy with amphotericin B ( AmB ) for disseminated coccidioidomycosis .

Example answer:
{"entities": [{"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}, {"text": "AmB", "type": "Chemical"}, {"text": "coccidioidomycosis", "type": "Disease"}]}

Example input:
Sentence: These seven cases demonstrate that procainamide can produce an acquired prolonged Q-T syndrome with polymorphous ventricular tachycardia .

Example answer:
{"entities": [{"text": "procainamide", "type": "Chemical"}, {"text": "prolonged Q-T syndrome", "type": "Disease"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: Development of ocular myasthenia during pegylated interferon and ribavirin treatment for chronic hepatitis C. A 63-year-old male experienced sudden diplopia after 9 weeks of administration of pegylated interferon ( IFN ) alpha-2b and ribavirin for chronic hepatitis C ( CHC ) .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated interferon", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "chronic hepatitis", "type": "Disease"}, {"text": "diplopia", "type": "Disease"}, {"text": "pegylated interferon ( IFN ) alpha-2b", "type": "Chemical"}, {"text": "chronic hepatitis C", "type": "Disease"}, {"text": "CHC", "type": "Disease"}]}

Example input:
Sentence: In a patient with WPW syndrome and idiopathic dilated cardiomyopathy , intractable atrioventricular reentrant tachycardia ( AVRT ) was iatrogenically induced .

Example answer:
{"entities": [{"text": "WPW syndrome", "type": "Disease"}, {"text": "idiopathic dilated cardiomyopathy", "type": "Disease"}, {"text": "atrioventricular reentrant tachycardia", "type": "Disease"}, {"text": "AVRT", "type": "Disease"}]}

Example input:
Sentence: In the seventh patient , a permanent ventricular pacemaker was inserted and , despite continuation of procainamide therapy , polymorphous ventricular tachycardia did not reoccur .

Example answer:
{"entities": [{"text": "procainamide", "type": "Chemical"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: A previously healthy child who developed acute , severe , rapidly progressive vanishing bile duct syndrome shortly after Stevens-Johnson syndrome is described ; this was temporally associated with ibuprofen use .

Example answer:
{"entities": [{"text": "vanishing bile duct syndrome", "type": "Disease"}, {"text": "Stevens-Johnson syndrome", "type": "Disease"}, {"text": "ibuprofen", "type": "Chemical"}]}

Example input:
Sentence: In four patients , polymorphous ventricular tachycardia appeared after intravenous administration of 200 to 400 mg of procainamide for the treatment of sustained ventricular tachycardia .

Example answer:
{"entities": [{"text": "ventricular tachycardia", "type": "Disease"}, {"text": "procainamide", "type": "Chemical"}]}

Example input:
Sentence: A 47-year-old patient suffering from coronary artery disease was admitted to the CCU in shock with III .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "shock", "type": "Disease"}]}

Example input:
Sentence: Iatrogenically induced intractable atrioventricular reentrant tachycardia after verapamil and catheter ablation in a patient with Wolff-Parkinson-White syndrome and idiopathic dilated cardiomyopathy .

Example answer:
{"entities": [{"text": "atrioventricular reentrant tachycardia", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "idiopathic dilated cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: Twenty-three hours after heart transplantation , life-threatening acute right heart failure was diagnosed in a patient requiring continuous venovenous hemodiafiltration ( CVVHDF ) .

Example answer:
{"entities": [{"text": "right heart failure", "type": "Disease"}]}

Input:
Sentence: After one week of therapy , he was transferred to the intensive care unit with cardiopulmonary compromise related to superior vena cava ( SVC ) syndrome .

## Item bc5cdr:test:4558
Example input:
Sentence: In our experience and according to the literature , FK506 does not seem to cross-react with cyclosporin A ( CyA ) , an immuno-suppressive drug already known to induce MAHA .

Example answer:
{"entities": [{"text": "FK506", "type": "Chemical"}, {"text": "cyclosporin A", "type": "Chemical"}, {"text": "CyA", "type": "Chemical"}, {"text": "MAHA", "type": "Disease"}]}

Example input:
Sentence: Progressive myopathy with up-regulation of MHC-I associated with statin therapy .

Example answer:
{"entities": [{"text": "myopathy", "type": "Disease"}, {"text": "statin", "type": "Chemical"}]}

Example input:
Sentence: Pyrrolidine dithiocarbamate ( PDTC ) has a dual mechanism of action as an antioxidant and an inhibitor of the transcription factor kappa-beta .

Example answer:
{"entities": [{"text": "Pyrrolidine dithiocarbamate", "type": "Chemical"}, {"text": "PDTC", "type": "Chemical"}]}

Example input:
Sentence: Dup 753 prevents the development of puromycin aminonucleoside-induced nephrosis .

Example answer:
{"entities": [{"text": "Dup 753", "type": "Chemical"}, {"text": "puromycin", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: In contrast , SSR103800 failed to affect hyperactivity induced by amphetamine or naturally observed in dopamine transporter ( DAT ( -/- ) ) knockout mice ( 10-30 mg/kg p.o . ) .

Example answer:
{"entities": [{"text": "SSR103800", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : This study establishes a TAA model by periarterial CaCl ( 2 ) exposure in rats , and demonstrates a significant elevation of expression of MMP-2 , MMP-9 , ADAM10 and ADAM17 in the pathogenesis of vascular remodeling .

Example answer:
{"entities": [{"text": "TAA", "type": "Disease"}, {"text": "CaCl ( 2 )", "type": "Chemical"}]}

Example input:
Sentence: To test the validity of the hypothesis that hypomethylation of DNA plays an important role in the initiation of carcinogenic process , 5-azacytidine ( 5-AzC ) ( 10 mg/kg ) , an inhibitor of DNA methylation , was given to rats during the phase of repair synthesis induced by the three carcinogens , benzo [ a ] -pyrene ( 200 mg/kg ) , N-methyl-N-nitrosourea ( 60 mg/kg ) and 1,2-dimethylhydrazine ( 1,2-DMH ) ( 100 mg/kg ) .

Example answer:
{"entities": [{"text": "initiation of carcinogenic process", "type": "Disease"}, {"text": "5-azacytidine", "type": "Chemical"}, {"text": "5-AzC", "type": "Chemical"}, {"text": "benzo [ a ] -pyrene", "type": "Chemical"}, {"text": "N-methyl-N-nitrosourea", "type": "Chemical"}, {"text": "1,2-dimethylhydrazine", "type": "Chemical"}, {"text": "1,2-DMH", "type": "Chemical"}]}

Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "Chemical"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Input:
Sentence: p53 inhibition blocked transient DOX-induced STAT3 activation in MHC-CB7 mice , which was associated with enhanced induction of the DNA repair proteins Ku70 and Ku80 .

## Item bc5cdr:test:4559
Example input:
Sentence: The pooled statistical analysis for ventricular septal ( VSD ) and midline ( MD ) defects was performed for rat fetuses exposed to piroxicam , selective and non-selective COX-2 inhibitor based on present and historic data .

Example answer:
{"entities": [{"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: Adriamycin-induced autophagic cardiomyocyte death plays a pathogenic role in a rat model of heart failure .

Example answer:
{"entities": [{"text": "Adriamycin-induced", "type": "Chemical"}, {"text": "death", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}]}

Example input:
Sentence: Neonatal cardiomyocytes were isolated from Sprague-Dawley rat hearts and randomly divided into controls , an adriamycin-treated group , and a 3MA plus adriamycin-treated group .

Example answer:
{"entities": [{"text": "adriamycin-treated", "type": "Chemical"}, {"text": "3MA", "type": "Chemical"}]}

Example input:
Sentence: At termination of the experiments , mice underwent echocardiography , quantitation of abundance of molecular markers of CM ( ventricular mRNA encoding atrial natriuretic factor [ ANF ] and sarcoplasmic calcium ATPase [ SERCA2 ] ) , and determination of plasma LA .

Example answer:
{"entities": [{"text": "CM", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "LA", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Among markers of ischemic injury after DOX in rats , cTnT showed the greatest ability to detect myocardial damage assessed by echocardiographic detection and histological changes .

Example answer:
{"entities": [{"text": "ischemic injury", "type": "Disease"}, {"text": "DOX", "type": "Chemical"}, {"text": "myocardial damage", "type": "Disease"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: We investigated the diagnostic value of cTnI and cTnT for the diagnosis of myocardial damage in a rat model of doxorubicin ( DOX ) -induced cardiomyopathy , and we examined the relationship between serial cTnI and cTnT with the development of cardiac disorders monitored by echocardiography and histological examinations in this model .

Example answer:
{"entities": [{"text": "myocardial damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiac disorders", "type": "Disease"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "Chemical"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Input:
Sentence: Mice with cardiomyocyte-restricted deletion of STAT3 exhibited worse cardiac function , higher levels of cardiomyocyte apoptosis , and a greater induction of Ku70 and Ku80 in response to DOX treatment during the acute stage when compared with control animals .

## Item bc5cdr:test:4386
Example input:
Sentence: Suxamethonium causes prolonged apnea in patients in whom pseudocholinesterase enzyme gets deactivated by organophosphorus ( OP ) poisons .

Example answer:
{"entities": [{"text": "Suxamethonium", "type": "Chemical"}, {"text": "apnea", "type": "Disease"}, {"text": "organophosphorus ( OP ) poisons", "type": "Chemical"}]}

Example input:
Sentence: Long-term intragastric application of the antiepileptic drug sodium valproate ( Vupral `` Polfa '' ) at the effective dose of 200 mg/kg b. w. once daily to rats for 1 , 3 , 6 , 9 and 12 months revealed neurological disorders indicating cerebellum damage ( `` valproate encephalopathy '' ) .

Example answer:
{"entities": [{"text": "sodium valproate", "type": "Chemical"}, {"text": "neurological disorders", "type": "Disease"}, {"text": "cerebellum damage", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: FINDINGS : A 28-year-old man suffering from idiopathic epilepsy with generalized seizures was treated with LEV ( 3000 mg ) added to valproate ( VPA ) ( 2000 mg ) .

Example answer:
{"entities": [{"text": "idiopathic epilepsy", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "LEV", "type": "Chemical"}, {"text": "valproate", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}]}

Example input:
Sentence: Encephalopathy induced by levetiracetam added to valproate .

Example answer:
{"entities": [{"text": "Encephalopathy", "type": "Disease"}, {"text": "levetiracetam", "type": "Chemical"}, {"text": "valproate", "type": "Chemical"}]}

Example input:
Sentence: Morphological features of encephalopathy after chronic administration of the antiepileptic drug valproate to rats .

Example answer:
{"entities": [{"text": "encephalopathy", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}]}

Example input:
Sentence: Valproic acid induced encephalopathy -- 19 new cases in Germany from 1994 to 2003 -- a side effect associated to VPA-therapy not only in young children .

Example answer:
{"entities": [{"text": "Valproic acid", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "VPA-therapy", "type": "Chemical"}]}

Example input:
Sentence: A case of valproate-induced encephalopathy is presented .

Example answer:
{"entities": [{"text": "valproate-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Valproate-induced encephalopathy .

Example answer:
{"entities": [{"text": "Valproate-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Valproate-induced encephalopathy is a rare syndrome that may manifest in otherwise normal epileptic individuals .

Example answer:
{"entities": [{"text": "Valproate-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "epileptic", "type": "Disease"}]}

Example input:
Sentence: The possible influence of the hepatic damage , mainly hyperammonemia , upon the development of valproate encephalopathy is discussed .

Example answer:
{"entities": [{"text": "hepatic damage", "type": "Disease"}, {"text": "hyperammonemia", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Input:
Sentence: Valproate-induced hyperammonemic encephalopathy is an uncommon but serious effect of valproate treatment .

## Item bc5cdr:test:4604
Example input:
Sentence: A frequency of bradycardia of 50 % was noted in the control group , but this was not significantly different from the frequency with the active drugs .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: The ventricular fibrillation threshold was measured by passing a gated train of 12 constant current pulses through the ventricular myocardium during the vulnerable period of the cardiac cycle .

Example answer:
{"entities": [{"text": "ventricular fibrillation", "type": "Disease"}]}

Example input:
Sentence: The interictal electroencephalogram ( EEG ) showed a generalized slowing to 5 per second theta rhythms with bilateral generalized high-amplitude discharges .

Example answer:
{"entities": []}

Example input:
Sentence: Further signs were hyperhidrosis , hypersalivation , bronchorrhoea , and severe miosis ; the electrocardiographic finding was atrio-ventricular dissociation .

Example answer:
{"entities": [{"text": "hyperhidrosis", "type": "Disease"}, {"text": "hypersalivation", "type": "Disease"}, {"text": "bronchorrhoea", "type": "Disease"}, {"text": "miosis", "type": "Disease"}, {"text": "atrio-ventricular dissociation", "type": "Disease"}]}

Example input:
Sentence: The primary response variable was based on central reading of 24 hour ambulatory electrocardiographic recordings and was defined as the occurrence of 30 or more single premature ventricular complexes in any two consecutive 30 minute blocks or one or more runs of two or more premature ventricular complexes in the entire 24 hour electrocardiographic recording .

Example answer:
{"entities": []}

Example input:
Sentence: Sublingual UM-272 converted ventricular tachycardia to sinus rhythm in all 5 dogs .

Example answer:
{"entities": [{"text": "UM-272", "type": "Chemical"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: Forty seconds after injection of suxamethonium , bradycardia and cardiac arrest occurred .

Example answer:
{"entities": [{"text": "suxamethonium", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "cardiac arrest", "type": "Disease"}]}

Example input:
Sentence: His bundle recordings showed an atrial tachycardia with intermittent exit block and greatly prolonged BH and HV intervals ( 40 and 100 msec , respectively ) .

Example answer:
{"entities": [{"text": "atrial tachycardia", "type": "Disease"}]}

Example input:
Sentence: Basal frequency ( BF ) evaluated by surface electrogram was 223 +/- 4 beats/min .

Example answer:
{"entities": []}

Example input:
Sentence: Bradycardia ( defined as a decrease in heart rate to less than 50 beat min-1 ) was prevented when the larger dose of either active drug was used .

Example answer:
{"entities": [{"text": "Bradycardia", "type": "Disease"}]}

Input:
Sentence: The electrocardiogram revealed a 37 beats/min sinus bradycardia .

## Item bc5cdr:test:4532
Example input:
Sentence: Thirty-five consecutive chemotherapy-naive patients with Stage IV NSCLC and an Eastern Cooperative Oncology Group performance status of 0-2 were treated with a combination of paclitaxel ( 135 mg/m ( 2 ) given intravenously in 3 hours ) on Day 1 , cisplatin ( 120 mg/m ( 2 ) given intravenously in 6 hours ) on Day 1 , and gemcitabine ( 800 mg/m ( 2 ) given intravenously in 30 minutes ) on Days 1 and 8 , every 4 weeks .

Example answer:
{"entities": [{"text": "NSCLC", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}]}

Example input:
Sentence: In the present study , cis-platin ( 80-120 mg/m2BSA ) and 5-FU ( 1000 mg/m2BSA daily as a continuous infusion during 5 days ) were given to 76 patients before radiotherapy and surgery .

Example answer:
{"entities": [{"text": "cis-platin", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}]}

Example input:
Sentence: Paclitaxel/cisplatin is an effective first-line regimen for locoregionally advanced head and neck cancer and continued study is warranted .

Example answer:
{"entities": [{"text": "Paclitaxel/cisplatin", "type": "Chemical"}, {"text": "head and neck cancer", "type": "Disease"}]}

Example input:
Sentence: METHODS : A Phase II study of the combination of cisplatin plus amifostine was conducted in patients with progressive metastatic breast carcinoma who had received one , but not more than one , chemotherapy regimen for metastatic disease .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "amifostine", "type": "Chemical"}, {"text": "breast carcinoma", "type": "Disease"}]}

Example input:
Sentence: Older reports suggest an objective response rate of 8 % when 60-120 mg/m2 of cisplatin is administered every 3-4 weeks .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Forty-nine patients with advanced NSCLC were included , 38 of whom were age > /= 70 years and 11 were age < 70 years but who had some contraindication to receiving cisplatin .

Example answer:
{"entities": [{"text": "NSCLC", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : The combination of cisplatin and amifostine in this study resulted in an overall response rate of 16 % .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "amifostine", "type": "Chemical"}]}

Example input:
Sentence: None of them had received cisplatin chemotherapy .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: Thirty patients without prior chemotherapy and 16 pretreated with cisplatin-based chemotherapy were assessable for toxicity and response .

Example answer:
{"entities": [{"text": "cisplatin-based", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Preliminary results of an Eastern Cooperative Oncology Group study of single-agent paclitaxel ( Taxol ; Bristol-Myers Squibb Company , Princeton , NJ ) reported a 37 % response rate in patients with head and neck cancer , and the paclitaxel/cisplatin combination has been used successfully and has significantly improved median response duration in ovarian cancer patients .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "Taxol", "type": "Chemical"}, {"text": "head and neck cancer", "type": "Disease"}, {"text": "paclitaxel/cisplatin", "type": "Chemical"}, {"text": "ovarian cancer", "type": "Disease"}]}

Input:
Sentence: Data were collected on adult cancer patients receiving single-agent cisplatin as an outpatient from January 2011 to September 2012 .

## Item bc5cdr:test:4576
Example input:
Sentence: A possible involvement of energy metabolism was suggested previously , and in this study the adenylate energy charge and phosphorylcreatine mole fraction were determined in the adriamycin-treated cells .

Example answer:
{"entities": [{"text": "phosphorylcreatine", "type": "Chemical"}, {"text": "adriamycin-treated", "type": "Chemical"}]}

Example input:
Sentence: A similar bradycardic effect of clonidine was observed in isolated spontaneously beating right atria from alpha2ABC-knockout and wild-type mice .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: This approach allowed investigating the efficacy of alpha-lipoic acid in preventing axonal damage and apoptosis and the function and ultrastructural morphology of mitochondria after exposure to toxic agents and alpha-lipoic acid .

Example answer:
{"entities": [{"text": "alpha-lipoic acid", "type": "Chemical"}, {"text": "axonal damage", "type": "Disease"}]}

Example input:
Sentence: Clonidine-induced bradycardia in conscious alpha2ABC-/- mice was 32.3 % ( 10 microg/kg ) and 26.6 % ( 100 microg/kg ) of the effect in wild-type mice .

Example answer:
{"entities": [{"text": "Clonidine-induced", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Alpha2ABC-/- mice were completely unresponsive to the analgesic and hypnotic effects of clonidine ; however , clonidine significantly lowered heart rate in alpha2ABC-/- mice by up to 150 bpm .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Interestingly , all the drugs , such as , AAP , AMI and DOX induced apoptotic death in addition to necrosis in the respective organs which was very effectively blocked by GSPE .

Example answer:
{"entities": [{"text": "AAP", "type": "Chemical"}, {"text": "AMI", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "necrosis", "type": "Disease"}, {"text": "GSPE", "type": "Chemical"}]}

Example input:
Sentence: In vivo protection of dna damage associated apoptotic and necrotic cell deaths during acetaminophen-induced nephrotoxicity , amiodarone-induced lung toxicity and doxorubicin-induced cardiotoxicity by a novel IH636 grape seed proanthocyanidin extract .

Example answer:
{"entities": [{"text": "necrotic", "type": "Disease"}, {"text": "acetaminophen-induced", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "amiodarone-induced", "type": "Chemical"}, {"text": "lung toxicity", "type": "Disease"}, {"text": "doxorubicin-induced", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}, {"text": "IH636 grape seed proanthocyanidin extract", "type": "Chemical"}]}

Example input:
Sentence: Additionally , this may have been the first report on AMI-induced apoptotic death in the lung tissue .

Example answer:
{"entities": [{"text": "AMI-induced", "type": "Chemical"}]}

Example input:
Sentence: We found that maltolyl p-coumarate significantly decreased apoptotic cell death and reduced reactive oxygen species , cytochrome c release , and caspase 3 activation .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}]}

Input:
Sentence: The results showed that aconitine stimulated apoptosis time-dependently .

## Item bc5cdr:test:4710
Example input:
Sentence: A total of sixty patients were trated with bromperidol first in open conditions ( 20 patients ) , then on a double blind basis ( 40 patients ) with haloperidol as the reference substance .

Example answer:
{"entities": [{"text": "bromperidol", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Nine hundred one patients were randomized to treatment , 447 who received the lozenge and 454 who received the gum ( safety population ) .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : One hundred and four ( 104 ) patients aged 6-35 years ( mean 17,2 years ) participated in the study .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : A non-randomised clinical study of patients aged > or =65 years admitted to acute hospital wards during 1 month .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Forty-four patients were enrolled in the study of which 7 ( 16 % ) were ineligible .

Example answer:
{"entities": []}

Example input:
Sentence: PATIENTS AND METHODS : The randomized sample consisted of 234 euthymic men who were receiving some type of SSRI .

Example answer:
{"entities": [{"text": "SSRI", "type": "Chemical"}]}

Example input:
Sentence: Finally , 15 patients were excluded from the study ( noncompliance 14 , death 1 ) ; thus , 60 patients ( 31 in group I and 29 in group II ) were eligible for analysis .

Example answer:
{"entities": [{"text": "death", "type": "Disease"}]}

Example input:
Sentence: The patients were randomly allocated to one of three groups ; those in group A ( n = 10 ) were subjected to controlled hypotension alone , those in group B ( n = 10 ) to haemodilution alone and those in group C ( n = 10 ) to both controlled hypotension and haemodilution .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}]}

Example input:
Sentence: In a randomized , double-blind , placebo-controlled , crossover study , we studied 12 volunteers in three experiments .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : We conducted a prospective , randomized , double-blind study in the emergency department of a central-city teaching hospital .

Example answer:
{"entities": []}

Input:
Sentence: METHODS : This randomized , double-blinded study was conducted in 100 patients randomly allocated into five groups of 20 patients each .

## Item bc5cdr:test:4366
Example input:
Sentence: METHODS : Thirty-five Wistar rats were given 1.5 mg/kg DOX , i.v. , weekly for up to 8 weeks for a total cumulative dose of 12 mg/kg BW .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: Subjects were receiving desferrioxamine ( DFO ) chelation treatment with a mean daily dose of 50-60 mg/kg , 5-6 days a week during the first six years of the study , which was then reduced to 40-50 mg/kg for the following eight years .

Example answer:
{"entities": [{"text": "desferrioxamine", "type": "Chemical"}, {"text": "DFO", "type": "Chemical"}]}

Example input:
Sentence: In four subacute toxicity studies , the intravenous administration of cefonicid or cefazedone to beagle dogs caused a dose-dependent incidence of anemia , neutropenia , and thrombocytopenia after 1-3 months of treatment .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}, {"text": "anemia", "type": "Disease"}, {"text": "neutropenia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}]}

Example input:
Sentence: Mitochondrial radiocalcium uptakes were significantly decreased in animals pretreated with acetylsalicylic acid or dipyridamole or when hydrocortisone was added to the epinephrine infusion ( 2,682,2,803 , and 3,424 counts per minute per gram of dried fraction , respectively ) .

Example answer:
{"entities": [{"text": "radiocalcium", "type": "Chemical"}, {"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine", "type": "Chemical"}]}

Example input:
Sentence: The risk of bladder cancer doubled for every 10 g increment in cyclophosphamide ( OR = 2.0 , 95 % confidence interval ( CI ) 0.8 to 4.9 ) .

Example answer:
{"entities": [{"text": "bladder cancer", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}]}

Example input:
Sentence: Thirty-six patients were treated with BCNU every 6 to 8 weeks , either by transfemoral catheterization of the internal carotid or vertebral artery or through a fully implantable intracarotid drug delivery system , beginning with a dose of 200 mg/sq m body surface area .

Example answer:
{"entities": [{"text": "BCNU", "type": "Chemical"}]}

Example input:
Sentence: cTnT found in rats after 12 mg/kg were significantly greater than that found after 7.5 mg/kg DOX .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: Upon rechallenge with either cephalosporin , the hematologic syndrome was reproduced in most dogs tested ; cefonicid ( but not cefazedone ) -treated dogs showed a substantially reduced induction period ( 15 +/- 5 days ) compared to that of the first exposure to the drug ( 61 +/- 24 days ) .

Example answer:
{"entities": [{"text": "cephalosporin", "type": "Chemical"}, {"text": "hematologic syndrome", "type": "Disease"}, {"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}]}

Example input:
Sentence: A significant rise in cTnT was found in DOX rats after cumulative doses of 7.5 and 12 mg/kg in comparison with baseline ( p < 0.05 ) .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: A nonregenerative anemia was the most compromising of the cytopenias and occurred in approximately 50 % of dogs receiving 400-500 mg/kg cefonicid or 540-840 mg/kg cefazedone .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "cytopenias", "type": "Disease"}, {"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}]}

Input:
Sentence: On the basis of the findings reported herein , a dose of 60 mg/m ( 2 ) of CCNU combined with 250 mg/m ( 2 ) of CTX ( divided over 5 days ) q 4 wk is tolerable in tumor-bearing dogs .

## Item bc5cdr:test:4394
Example input:
Sentence: Intravenous administration of a single 50-mg bolus of lidocaine in a 67-year-old man resulted in profound depression of the activity of the sinoatrial and atrioventricular nodal pacemakers .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: Three months later the patient was exposed to a single dose of metoprolol , diltiazem , propafenone ( since he had received this drug in the past ) , and sparteine ( as a probe for the debrisoquine/sparteine type polymorphism of oxidative drug metabolism ) .

Example answer:
{"entities": [{"text": "metoprolol", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "propafenone", "type": "Chemical"}, {"text": "sparteine", "type": "Chemical"}, {"text": "debrisoquine/sparteine", "type": "Chemical"}]}

Example input:
Sentence: CASE SUMMARY : A 13-year-old boy was treated with ampicillin and gentamicin because of suspected septicemia .

Example answer:
{"entities": [{"text": "ampicillin", "type": "Chemical"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "septicemia", "type": "Disease"}]}

Example input:
Sentence: Pneumonitis , bilateral pleural effusions , echocardiographic evidence of cardiac tamponade , and positive autoantibodies developed in a 43-year-old man , who was receiving long-term sulfasalazine therapy for chronic ulcerative colitis .

Example answer:
{"entities": [{"text": "Pneumonitis", "type": "Disease"}, {"text": "pleural effusions", "type": "Disease"}, {"text": "cardiac tamponade", "type": "Disease"}, {"text": "sulfasalazine", "type": "Chemical"}, {"text": "ulcerative colitis", "type": "Disease"}]}

Example input:
Sentence: The present report describes a case of cardiac arrest and subsequent death as a result of hyperkalaemia following the use of suxamethonium in a 23-year-old Malawian woman .

Example answer:
{"entities": [{"text": "cardiac arrest", "type": "Disease"}, {"text": "death", "type": "Disease"}, {"text": "hyperkalaemia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: Based on this principle a 27-year old woman , classified as being in the high-risk group ( Goldstein and Berkowitz score : 11 ) , was treated with multiple cytotoxic drugs .

Example answer:
{"entities": []}

Example input:
Sentence: A 78-year-old with healed septal necrosis suffered a recurrent myocardial infarction of the anterior wall following the administration of isosorbide dinitrate 5 mg sublingually .

Example answer:
{"entities": [{"text": "necrosis", "type": "Disease"}, {"text": "myocardial infarction", "type": "Disease"}, {"text": "isosorbide dinitrate", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Long-term use and concomitant use of more than one BZD/RD were common in elderly patients hospitalised because of acute illnesses .

Example answer:
{"entities": []}

Example input:
Sentence: We report a case of a 31 year old female who required admission to the Intensive Care Unit for ventilation and full supportive therapy , following ingestion of 13.5g bupropion .

Example answer:
{"entities": [{"text": "bupropion", "type": "Chemical"}]}

Example input:
Sentence: High doses of this antibiotic combination should be avoided especially in elderly patients .

Example answer:
{"entities": []}

Input:
Sentence: Physicians should recognise the possibility of fatal bacterial infections related to bortezomib plus high-dose dexamethasone in elderly patients , and we believe this case warrants further investigation .

## Item bc5cdr:test:4549
Example input:
Sentence: Pooled data from trials comparing antithrombotic treatment with placebo have shown that warfarin reduces the risk of stroke by 62 % , and that aspirin alone reduces the risk by 22 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "stroke", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: We conclude from these studies that CX3CR1 signaling does not modulate METH neurotoxicity or microglial activation .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: In conclusion , the NF-kappaB inhibitor and antioxidant PDTC protected the piriform cortex , whereas it did not affect hilar neuronal loss .

Example answer:
{"entities": [{"text": "PDTC", "type": "Chemical"}, {"text": "neuronal loss", "type": "Disease"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: The increase in free radical generation has been implicated as one of the important mechanisms of cognitive impairment by antiepileptic drugs .

Example answer:
{"entities": [{"text": "cognitive impairment", "type": "Disease"}]}

Example input:
Sentence: Rg1 , as a ginsenoside extracted from Panax ginseng , could ameliorate spatial learning impairment .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "ginsenoside", "type": "Chemical"}, {"text": "learning impairment", "type": "Disease"}]}

Example input:
Sentence: Concomitant curcumin administration prevented the cognitive impairment and decreased the increased oxidative stress induced by these antiepileptic drugs .

Example answer:
{"entities": [{"text": "curcumin", "type": "Chemical"}, {"text": "cognitive impairment", "type": "Disease"}]}

Example input:
Sentence: All of these positive GABA ( A ) modulators suppressed the expression of kindled seizures , whereas only allopregnanolone and ganaxolone inhibited the development of kindling .

Example answer:
{"entities": [{"text": "GABA", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "allopregnanolone", "type": "Chemical"}, {"text": "ganaxolone", "type": "Chemical"}]}

Example input:
Sentence: Allopregnanolone and pregnanolone , but not ganaxolone , also reduced cumulative lethality associated with kindling .

Example answer:
{"entities": [{"text": "Allopregnanolone", "type": "Chemical"}, {"text": "pregnanolone", "type": "Chemical"}, {"text": "ganaxolone", "type": "Chemical"}]}

Input:
Sentence: We found that metformin suppressed the progression of kindling , ameliorated the cognitive impairment and decreased brain oxidative stress .

## Item bc5cdr:test:4577
Example input:
Sentence: Based on clinical data , indicating that chloroacetaldehyde ( CAA ) is an important metabolite of oxazaphosphorine cytostatics , an experimental study was carried out in order to elucidate the role of CAA in the development of hemorrhagic cystitis .

Example answer:
{"entities": [{"text": "chloroacetaldehyde", "type": "Chemical"}, {"text": "CAA", "type": "Chemical"}]}

Example input:
Sentence: Out of these 67 proteins , LID significantly changed the expression level of five proteins : alphabeta-crystalin , gamma-enolase , guanidoacetate methyltransferase , vinculin , and proteasome alpha-2 subunit .

Example answer:
{"entities": [{"text": "LID", "type": "Disease"}]}

Example input:
Sentence: Activation of presynaptic alpha2-adrenoceptors is the most widely accepted mechanism of action of the antisympathetic drug clonidine ; however , other target proteins have been postulated to contribute to the in vivo actions of clonidine .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: PURPOSE : This study was designed to establish a rat model of thoracic aortic aneurysm ( TAA ) by calcium chloride ( CaCl ( 2 ) ) -induced arterial injury and to explore the potential role of a disintegrin and metalloproteinase ( ADAM ) , matrix metalloproteinases ( MMPs ) and their endogenous inhibitors ( TIMPs ) in TAA formation .

Example answer:
{"entities": [{"text": "thoracic aortic aneurysm", "type": "Disease"}, {"text": "TAA", "type": "Disease"}, {"text": "calcium chloride", "type": "Chemical"}, {"text": "CaCl ( 2 )", "type": "Chemical"}, {"text": "arterial injury", "type": "Disease"}]}

Example input:
Sentence: Immunohistochemistry displayed significantly increased expressions of MMP-2 , MMP-9 , ADAM-10 and ADAM-17 ( all p < 0.01 ) in intima and media for CaCl ( 2 ) -treated segments .

Example answer:
{"entities": [{"text": "CaCl ( 2 )", "type": "Chemical"}]}

Example input:
Sentence: Mitochondrial radiocalcium uptakes were significantly decreased in animals pretreated with acetylsalicylic acid or dipyridamole or when hydrocortisone was added to the epinephrine infusion ( 2,682,2,803 , and 3,424 counts per minute per gram of dried fraction , respectively ) .

Example answer:
{"entities": [{"text": "radiocalcium", "type": "Chemical"}, {"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine", "type": "Chemical"}]}

Example input:
Sentence: In conclusion , ENaC mRNA expression , especially alphaENaC , is increased in the very early phase of the experimental model of PAN-induced nephrotic syndrome in rats , but appears to escape from the regulation by aldosterone after day 3 .

Example answer:
{"entities": [{"text": "PAN-induced", "type": "Chemical"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "aldosterone", "type": "Chemical"}]}

Example input:
Sentence: The therapeutic potential of the anticocaine antibody GNC92H2 was examined using a model of cocaine overdose .

Example answer:
{"entities": [{"text": "GNC92H2", "type": "Chemical"}, {"text": "cocaine overdose", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : This study establishes a TAA model by periarterial CaCl ( 2 ) exposure in rats , and demonstrates a significant elevation of expression of MMP-2 , MMP-9 , ADAM10 and ADAM17 in the pathogenesis of vascular remodeling .

Example answer:
{"entities": [{"text": "TAA", "type": "Disease"}, {"text": "CaCl ( 2 )", "type": "Chemical"}]}

Example input:
Sentence: MMP-2 , MMP-9 , ADAM-10 and ADAM-17 mRNA levels were increased in CaCl ( 2 ) -treated segments ( all p < 0.01 ) , with trends of elevation in CaCl ( 2 ) -untreated segments , as compared with NaCl-treated segments .

Example answer:
{"entities": [{"text": "CaCl ( 2 )", "type": "Chemical"}, {"text": "NaCl-treated", "type": "Chemical"}]}

Input:
Sentence: The expression analysis of Ca ( 2+ ) handling proteins demonstrated that aconitine promoted Ca ( 2+ ) overload through the expression regulation of Ca ( 2+ ) handling proteins .

## Item bc5cdr:test:4505
Example input:
Sentence: However , the observation that antagonists of the glutamate N-methyl-D-aspartate ( NMDA ) receptor produce schizophrenic-like symptoms in humans has led to the idea of a dysfunctioning of the glutamatergic system via its NMDA receptor .

Example answer:
{"entities": [{"text": "glutamate", "type": "Chemical"}, {"text": "N-methyl-D-aspartate", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "schizophrenic-like", "type": "Disease"}]}

Example input:
Sentence: Together these findings show that the GlyT1 inhibitor , SSR103800 , produces antipsychotic-like effects , which differ from those observed with compounds primarily targeting the dopaminergic system , and has a reduced side-effect potential as compared with these latter drugs .

Example answer:
{"entities": [{"text": "SSR103800", "type": "Chemical"}]}

Example input:
Sentence: Risperidone is an antipsychotic drug with high affinity at dopamine D2 and serotonin 5-HT2 receptors .

Example answer:
{"entities": [{"text": "Risperidone", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "serotonin 5-HT2", "type": "Chemical"}]}

Example input:
Sentence: In a double-blind 6-week trial , 458 patients with acute schizophrenia were randomly assigned to fixed-dose treatment with asenapine at 5 mg twice daily ( BID ) , asenapine at 10 mg BID , placebo , or haloperidol at 4 mg BID ( to verify assay sensitivity ) .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "Disease"}, {"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: As a result , there is a growing interest in the development of pharmacological agents with potential antipsychotic properties that enhance the activity of the glutamatergic system via a modulation of the NMDA receptor .

Example answer:
{"entities": [{"text": "NMDA", "type": "Chemical"}]}

Example input:
Sentence: THP exhibited an antipsychotic-like profile by potentiating haloperidol-induced catalepsy , reducing amphetamine-induced hyperactivity and reducing apomorphine-induced climbing in mice .

Example answer:
{"entities": []}

Example input:
Sentence: This study aimed at investigating the potential antipsychotic-like properties of SSR103800 , with a particular focus on models of hyperactivity , involving either drug challenge ( ie , amphetamine and MK-801 ) or transgenic mice ( ie , NMDA Nr1 ( neo-/- ) and DAT ( -/- ) ) .

Example answer:
{"entities": [{"text": "SSR103800", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "MK-801", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}]}

Example input:
Sentence: Previous clinical studies have proposed that risperidone 's pharmacologic profile may produce improved efficacy for negative psychotic symptoms and decreased propensity for extrapyramidal side effects ; features shared by so-called 'atypical ' neuroleptics .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}, {"text": "psychotic symptoms", "type": "Disease"}]}

Example input:
Sentence: In the double blind study with haloperidol , both substances were found to be highly effective in the treatment of psychotic syndromes belonging predominantly to the schizophrenia group .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "psychotic syndromes belonging predominantly to the schizophrenia group", "type": "Disease"}]}

Example input:
Sentence: Findings suggest a potential for H ( 3 ) -receptor antagonists in improving the refractory cases of schizophrenia .

Example answer:
{"entities": []}

Input:
Sentence: We suggest that DHEA displays typical neuroleptic-like effects , and may be used in the treatment of schizophrenia .

## Item bc5cdr:test:4556
Example input:
Sentence: Histological evaluation of hearts from all rats given DOX revealed significant slight degrees of perivascular and interstitial fibrosis .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "Chemical"}]}

Example input:
Sentence: Interestingly , all the drugs , such as , AAP , AMI and DOX induced apoptotic death in addition to necrosis in the respective organs which was very effectively blocked by GSPE .

Example answer:
{"entities": [{"text": "AAP", "type": "Chemical"}, {"text": "AMI", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "necrosis", "type": "Disease"}, {"text": "GSPE", "type": "Chemical"}]}

Example input:
Sentence: We describe a patient who developed dilated cardiomyopathy and clinical congestive heart failure after 2 months of therapy with amphotericin B ( AmB ) for disseminated coccidioidomycosis .

Example answer:
{"entities": [{"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}, {"text": "AmB", "type": "Chemical"}, {"text": "coccidioidomycosis", "type": "Disease"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Eighteen of the DOX rats died prematurely of general toxicity during the 9-week period .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Doxorubicin is an effective anticancer chemotherapeutic agent known to cause acute and chronic cardiomyopathy .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: We investigated the diagnostic value of cTnI and cTnT for the diagnosis of myocardial damage in a rat model of doxorubicin ( DOX ) -induced cardiomyopathy , and we examined the relationship between serial cTnI and cTnT with the development of cardiac disorders monitored by echocardiography and histological examinations in this model .

Example answer:
{"entities": [{"text": "myocardial damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiac disorders", "type": "Disease"}]}

Example input:
Sentence: Although there was a discrepancy between the amount of cTnI and cTnT after DOX , probably due to heterogeneity in cross-reactivities of mAbs to various cTnI and cTnT forms , it is likely that cTnT in rats after DOX indicates cell damage determined by the magnitude of injury induced and that cTnT should be a useful marker for the prediction of experimentally induced cardiotoxicity and possibly for cardioprotective experiments .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Among markers of ischemic injury after DOX in rats , cTnT showed the greatest ability to detect myocardial damage assessed by echocardiographic detection and histological changes .

Example answer:
{"entities": [{"text": "ischemic injury", "type": "Disease"}, {"text": "DOX", "type": "Chemical"}, {"text": "myocardial damage", "type": "Disease"}]}

Input:
Sentence: One week after the last DOX treatment ( acute stage ) , MHC-CB7 mice exhibited improved cardiac function and lower levels of cardiomyocyte apoptosis when compared with the NON-TXG mice .

## Item bc5cdr:test:4329
Example input:
Sentence: RESULTS : Head-up tilt caused systolic orthostatic hypotension which was marked in six of 20 PD patients on selegiline , one of whom lost consciousness with unrecordable blood pressures .

Example answer:
{"entities": [{"text": "systolic orthostatic hypotension", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "selegiline", "type": "Chemical"}]}

Example input:
Sentence: A case of valproate-induced encephalopathy is presented .

Example answer:
{"entities": [{"text": "valproate-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: One patient had focal seizures and transient hemiparesis but recovered completely .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "transient hemiparesis", "type": "Disease"}]}

Example input:
Sentence: We describe a case of transient neurological deficit that occurred after unilateral spinal anaesthesia with 8 mg of 1 % hyperbaric bupivacaine slowly injected through a 25-gauge pencil-point spinal needle .

Example answer:
{"entities": [{"text": "neurological deficit", "type": "Disease"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : 272 cases of confusion were reported with valproic acid : 153 women and 119 men .

Example answer:
{"entities": [{"text": "confusion", "type": "Disease"}, {"text": "valproic acid", "type": "Chemical"}]}

Example input:
Sentence: Long-term intragastric application of the antiepileptic drug sodium valproate ( Vupral `` Polfa '' ) at the effective dose of 200 mg/kg b. w. once daily to rats for 1 , 3 , 6 , 9 and 12 months revealed neurological disorders indicating cerebellum damage ( `` valproate encephalopathy '' ) .

Example answer:
{"entities": [{"text": "sodium valproate", "type": "Chemical"}, {"text": "neurological disorders", "type": "Disease"}, {"text": "cerebellum damage", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: Valproate-induced encephalopathy is a rare syndrome that may manifest in otherwise normal epileptic individuals .

Example answer:
{"entities": [{"text": "Valproate-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "epileptic", "type": "Disease"}]}

Example input:
Sentence: Valproic acid induced encephalopathy -- 19 new cases in Germany from 1994 to 2003 -- a side effect associated to VPA-therapy not only in young children .

Example answer:
{"entities": [{"text": "Valproic acid", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "VPA-therapy", "type": "Chemical"}]}

Example input:
Sentence: FINDINGS : A 28-year-old man suffering from idiopathic epilepsy with generalized seizures was treated with LEV ( 3000 mg ) added to valproate ( VPA ) ( 2000 mg ) .

Example answer:
{"entities": [{"text": "idiopathic epilepsy", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "LEV", "type": "Chemical"}, {"text": "valproate", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}]}

Input:
Sentence: In the preceding months , the patient had a number of admissions with transient unilateral hemiparesis with facial droop , and had been started on valproate for presumed hemiplegic migraine .

## Item bc5cdr:test:4724
Example input:
Sentence: Lesions reduced the extent of immunohistological staining for choline acetyltransferase in the interpeduncular nucleus ( p < 0.025 ) , but not for tyrosine hydroxylase in the surrounding catecholaminergic A10 region .

Example answer:
{"entities": []}

Example input:
Sentence: MMP-2 , MMP-9 , ADAM-10 and ADAM-17 mRNA levels were increased in CaCl ( 2 ) -treated segments ( all p < 0.01 ) , with trends of elevation in CaCl ( 2 ) -untreated segments , as compared with NaCl-treated segments .

Example answer:
{"entities": [{"text": "CaCl ( 2 )", "type": "Chemical"}, {"text": "NaCl-treated", "type": "Chemical"}]}

Example input:
Sentence: Immunohistochemistry displayed significantly increased expressions of MMP-2 , MMP-9 , ADAM-10 and ADAM-17 ( all p < 0.01 ) in intima and media for CaCl ( 2 ) -treated segments .

Example answer:
{"entities": [{"text": "CaCl ( 2 )", "type": "Chemical"}]}

Example input:
Sentence: The expression of arginine vasopressin ( AVP ) gene in the paraventricular ( PVN ) and supraoptic nuclei ( SON ) was investigated in rats with lithium ( Li ) -induced polyuria , using in situ hybridization histochemistry and radioimmunoassay .

Example answer:
{"entities": [{"text": "arginine vasopressin", "type": "Chemical"}, {"text": "AVP", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "Li", "type": "Chemical"}, {"text": "polyuria", "type": "Disease"}]}

Example input:
Sentence: Molecularly , ANF mRNA increased 250 % and SERCA2 mRNA decreased 57 % .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Immunofluorescence staining with the MRP2 antibody was found to label a high number of microvessels throughout the brain in normal Wistar rats , whereas such labeling was absent in TR ( - ) rats .

Example answer:
{"entities": []}

Example input:
Sentence: However , the increase in release of ACh produced by the first application of KCl was 2-fold higher in WSP versus WSR mice .

Example answer:
{"entities": [{"text": "ACh", "type": "Chemical"}, {"text": "KCl", "type": "Chemical"}]}

Example input:
Sentence: At termination of the experiments , mice underwent echocardiography , quantitation of abundance of molecular markers of CM ( ventricular mRNA encoding atrial natriuretic factor [ ANF ] and sarcoplasmic calcium ATPase [ SERCA2 ] ) , and determination of plasma LA .

Example answer:
{"entities": [{"text": "CM", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "LA", "type": "Chemical"}]}

Example input:
Sentence: METHODS : The expression of MRP2 and Pgp in brain and liver sections of TR ( - ) rats and normal Wistar rats was determined with immunohistochemistry , by using a novel , highly selective monoclonal MRP2 antibody and the monoclonal Pgp antibody C219 , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSION : This study establishes a TAA model by periarterial CaCl ( 2 ) exposure in rats , and demonstrates a significant elevation of expression of MMP-2 , MMP-9 , ADAM10 and ADAM17 in the pathogenesis of vascular remodeling .

Example answer:
{"entities": [{"text": "TAA", "type": "Disease"}, {"text": "CaCl ( 2 )", "type": "Chemical"}]}

Input:
Sentence: Western blot analysis revealed that AQP2 expression in medullary tissues was lowered after 3 and 5 days in WT mice ; however , AQP2 was unchanged in PKCa KO .

## Item bc5cdr:test:4361
Example input:
Sentence: RESULTS : Six of 61 women ( 10 % ) developed clinically reversible grade 3 CHF following infusional cyclophosphamide with a median percent decline in ejection fraction of 31 % .

Example answer:
{"entities": [{"text": "CHF", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}]}

Example input:
Sentence: We investigated the diagnostic value of cTnI and cTnT for the diagnosis of myocardial damage in a rat model of doxorubicin ( DOX ) -induced cardiomyopathy , and we examined the relationship between serial cTnI and cTnT with the development of cardiac disorders monitored by echocardiography and histological examinations in this model .

Example answer:
{"entities": [{"text": "myocardial damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiac disorders", "type": "Disease"}]}

Example input:
Sentence: Our studies indicate that nephrotoxicity of MTX + 5-FU + CY administered jointly is lower than in monotherapy .

Example answer:
{"entities": [{"text": "nephrotoxicity", "type": "Disease"}, {"text": "MTX", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "CY", "type": "Chemical"}]}

Example input:
Sentence: Maximal cTnI ( pg/ml ) and cTnT levels were significantly increased in DOX rats compared with controls ( p=0.006 , 0.007 ) .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: Severe hematologic toxicity ( neutrophil count < 1000/mm3 and/or hemoglobin < 8 g/dl ) occurred in 4 patients assigned to group I and 7 assigned to group II .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: The median age of those patients developing Grade 3-4 neutropenia was significantly higher than that of the remaining patients ( 75 years vs. 72 years ; P = 0.047 ) .

Example answer:
{"entities": [{"text": "neutropenia", "type": "Disease"}]}

Example input:
Sentence: Neutropenia grade greater than or equal to 3 was seen in 15 patients , infections with recovery in 3 , and grand mal seizures in 1 patient .

Example answer:
{"entities": [{"text": "Neutropenia", "type": "Disease"}, {"text": "infections", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Although there was a discrepancy between the amount of cTnI and cTnT after DOX , probably due to heterogeneity in cross-reactivities of mAbs to various cTnI and cTnT forms , it is likely that cTnT in rats after DOX indicates cell damage determined by the magnitude of injury induced and that cTnT should be a useful marker for the prediction of experimentally induced cardiotoxicity and possibly for cardioprotective experiments .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: Six patients ( 12 % ) had World Health Organization Grade 3-4 neutropenia , 2 patients ( 4 % ) had Grade 3-4 thrombocytopenia , and 2 patients ( 4 % ) had Grade 3 neurotoxicity .

Example answer:
{"entities": [{"text": "neutropenia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: World Health Organization Grade 3-4 neutropenia and thrombocytopenia occurred in 39.9 % and 11.4 % of patients , respectively .

Example answer:
{"entities": [{"text": "neutropenia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}]}

Input:
Sentence: Neutropenia was the principal toxic effect , and the overall frequency of grade 4 neutropenia after the first treatment of CCNU/CTX was 30 % ( 95 % confidence interval , 19-43 % ) .

## Item bc5cdr:test:4519
Example input:
Sentence: VPU was more potent than VPA , exhibiting the median effective dose ( ED ( 50 ) ) of 49 mg/kg in protecting rats against pilocarpine-induced seizure whereas the corresponding value for VPA was 322 mg/kg .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Male Sprague-Dawley rats were treated with D-penicillamine ( D-pen ) 500 mg/kg/day for 10 or 42 days .

Example answer:
{"entities": [{"text": "D-penicillamine", "type": "Chemical"}, {"text": "D-pen", "type": "Chemical"}]}

Example input:
Sentence: Those dosages ( greater than or equal to 10 mg/kg ) that inhibited mean NTE activity in the spinal cord greater than or equal to 73 % and brain greater than or equal to 67 % of control values produced severe ( greater than or equal to 3 ) cervical cord pathology in 85 % of the rats .

Example answer:
{"entities": []}

Example input:
Sentence: Male SD rats ( n = 30 ) were treated with Ato ( 50 mg/kg per day in drinking water ) or tap water for 15 days .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}]}

Example input:
Sentence: Rats were treated with a single IV injection of puromycin aminonucleoside , ( PAN , 7.5 mg/kg ) and 24 hour urine samples were obtained prior to sacrifice on days 3,5,7,10,17,27,41 ( N = 5-10 per group ) .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: Brain and spinal cord NTE activities were measured in Long-Evans male rats 1 hr post-exposure to various dosages of Mipafox ( ip , 1-15 mg/kg ) .

Example answer:
{"entities": [{"text": "Mipafox", "type": "Chemical"}]}

Example input:
Sentence: The protective action of subcutaneously ( SC ) administered antidotes or their combinations in DFP ( 2.0 mg/kg BW ) intoxication was studied in 9-10-weeks-old Han-Wistar male rats .

Example answer:
{"entities": [{"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Thirty-five Wistar rats were given 1.5 mg/kg DOX , i.v. , weekly for up to 8 weeks for a total cumulative dose of 12 mg/kg BW .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: Streptomycin sulfate ( 300 mg/kg s.c. ) was injected for various periods into preweanling rats and for 3 weeks into weanling rats .

Example answer:
{"entities": [{"text": "Streptomycin", "type": "Chemical"}]}

Example input:
Sentence: METHODS : For a period of 2 weeks , CsA 15 mg/kg/day ( given orally ) , FK506 3.0 mg/kg/day ( given orally ) or SRL 0.4 mg/kg/day ( given intraperitoneally ) was administered once a day as these doses have earlier been found to achieve a significant immunosuppressive effect in Sprague-Dawley rats .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Input:
Sentence: METHODS : S-53482 was administered dermally to rats at 30 , 100 , and 300 mg/kg during organogenesis , and S-23121 was administered at 200 , 400 , and 800 mg/kg ( the maximum applicable dose level ) .

## Item bc5cdr:test:4725
Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: Immunohistochemistry displayed significantly increased expressions of MMP-2 , MMP-9 , ADAM-10 and ADAM-17 ( all p < 0.01 ) in intima and media for CaCl ( 2 ) -treated segments .

Example answer:
{"entities": [{"text": "CaCl ( 2 )", "type": "Chemical"}]}

Example input:
Sentence: The expression of arginine vasopressin ( AVP ) gene in the paraventricular ( PVN ) and supraoptic nuclei ( SON ) was investigated in rats with lithium ( Li ) -induced polyuria , using in situ hybridization histochemistry and radioimmunoassay .

Example answer:
{"entities": [{"text": "arginine vasopressin", "type": "Chemical"}, {"text": "AVP", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "Li", "type": "Chemical"}, {"text": "polyuria", "type": "Disease"}]}

Example input:
Sentence: The results indicate that the deprived area of A1 undergoes extensive reorganization and becomes responsive to intact cochlear frequencies .

Example answer:
{"entities": []}

Example input:
Sentence: During the course of nephrotic syndrome , serum urea concentrations increased significantly faster in sgk1 ( -/- ) mice than in sgk1 ( +/+ ) mice leading to uremia and a reduced median survival in sgk1 ( -/- ) mice ( 29 vs. 40 days in sgk1 ( +/+ ) mice ) .

Example answer:
{"entities": [{"text": "nephrotic syndrome", "type": "Disease"}, {"text": "urea", "type": "Chemical"}, {"text": "uremia", "type": "Disease"}]}

Example input:
Sentence: MMP-TIMP and ADAM mRNAs were semi-quantitatively analyzed and protein expressions were determined by immunohistochemistry .

Example answer:
{"entities": []}

Example input:
Sentence: We conclude that GLEPP1 expression , unlike podocalyxin , reflects podocyte injury induced by PAN .

Example answer:
{"entities": [{"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: MMP-2 , MMP-9 , ADAM-10 and ADAM-17 mRNA levels were increased in CaCl ( 2 ) -treated segments ( all p < 0.01 ) , with trends of elevation in CaCl ( 2 ) -untreated segments , as compared with NaCl-treated segments .

Example answer:
{"entities": [{"text": "CaCl ( 2 )", "type": "Chemical"}, {"text": "NaCl-treated", "type": "Chemical"}]}

Example input:
Sentence: Using in situ hybridization probes for the alpha3 and alpha5 subunits , we showed that alpha5 mRNA levels are unchanged , whereas alpha3 mRNA levels are selectively decreased in the mitral cell layer of the olfactory bulb , and the inferior and the superior colliculus of beta4 -/- brains .

Example answer:
{"entities": []}

Example input:
Sentence: In conclusion , ENaC mRNA expression , especially alphaENaC , is increased in the very early phase of the experimental model of PAN-induced nephrotic syndrome in rats , but appears to escape from the regulation by aldosterone after day 3 .

Example answer:
{"entities": [{"text": "PAN-induced", "type": "Chemical"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "aldosterone", "type": "Chemical"}]}

Input:
Sentence: Similar results were observed with UT-A1 expression .
