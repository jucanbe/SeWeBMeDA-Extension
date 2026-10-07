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

## Item bc5cdr:test:3092
Example input:
Sentence: Upon rechallenge with either cephalosporin , the hematologic syndrome was reproduced in most dogs tested ; cefonicid ( but not cefazedone ) -treated dogs showed a substantially reduced induction period ( 15 +/- 5 days ) compared to that of the first exposure to the drug ( 61 +/- 24 days ) .

Example answer:
{"entities": [{"text": "cephalosporin", "type": "Chemical"}, {"text": "hematologic syndrome", "type": "Disease"}, {"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}]}

Example input:
Sentence: Since the introduction of angiotensin converting enzyme ( ACE ) inhibitors into the adjunctive treatment of patients with congestive heart failure , cases of severe hypotension , especially on the first day of treatment , have occasionally been reported .

Example answer:
{"entities": [{"text": "angiotensin converting enzyme ( ACE ) inhibitors", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: The animal model used to produce infarction implies artery ligation but chemical induction can be easily obtained with isoproterenol .

Example answer:
{"entities": [{"text": "infarction", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: Design and analysis of the HYPREN-trial : safety of enalapril and prazosin in the initial treatment phase of patients with congestive heart failure .

Example answer:
{"entities": [{"text": "enalapril", "type": "Chemical"}, {"text": "prazosin", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}]}

Example input:
Sentence: The effects of continuous positive airway pressure ( CPAP ) on cardiovascular dynamics and pulmonary shunt ( QS/QT ) were investigated in 12 dogs before and during sodium nitroprusside infusion that decreased mean arterial blood pressure 40-50 per cent .

Example answer:
{"entities": [{"text": "sodium nitroprusside", "type": "Chemical"}]}

Example input:
Sentence: Effects of acetylsalicylic acid , dipyridamole , and hydrocortisone on epinephrine-induced myocardial injury in dogs .

Example answer:
{"entities": [{"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine-induced", "type": "Chemical"}, {"text": "myocardial injury", "type": "Disease"}]}

Example input:
Sentence: The aim of this study was to investigate whether autophagy was involved in the progression of heart failure induced by adriamycin , so that we can develop a novel treatment strategy for heart failure .

Example answer:
{"entities": [{"text": "heart failure", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}]}

Example input:
Sentence: A reproducible model for producing diffuse myocardial injury ( epinephrine infusion ) has been developed to study the cardioprotective effects of agents or maneuvers which might alter the evolution of acute myocardial infarction .

Example answer:
{"entities": [{"text": "myocardial injury", "type": "Disease"}, {"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Nitroglycerin has been shown to reduce ST-segment elevation during acute myocardial infarction , an effect potentiated in the dog by agents that reverse nitroglycerin-induced hypotension .

Example answer:
{"entities": [{"text": "Nitroglycerin", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}, {"text": "nitroglycerin-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Input:
Sentence: The study aim was to identify these benefits in a canine model of acute heart failure .

## Item bc5cdr:test:2975
Example input:
Sentence: Post hoc analyses indicated that efficacy was similar with asenapine and haloperidol ; greater contrasts were seen in AEs , especially extrapyramidal symptoms .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}, {"text": "extrapyramidal symptoms", "type": "Disease"}]}

Example input:
Sentence: To determine if routine risperidone treatment is associated with a unique degree of D2 receptor occupancy and pattern of clinical effects , we used [ 123I ] IBZM SPECT to determine D2 occupancy in subjects treated with routine clinical doses of risperidone ( n = 12 ) or haloperidol ( n = 7 ) .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: This change resulted within 2-4 weeks in the 50-200 % increase in the plasma levels of these neuroleptics and the appearance of extrapyramidal symptoms .

Example answer:
{"entities": [{"text": "extrapyramidal symptoms", "type": "Disease"}]}

Example input:
Sentence: Based on these observations , it is concluded that 5-HT2 blockade obtained with risperidone at D2 occupancy rates of 60 % and above does not appear to protect against the risk for extrapyramidal side effects .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}]}

Example input:
Sentence: Nine patients exhibited mild to moderate extrapyramidal concomitant symptoms ; no other side effects were observed .

Example answer:
{"entities": [{"text": "extrapyramidal concomitant symptoms", "type": "Disease"}]}

Example input:
Sentence: Conventional agents are associated with unwanted central nervous system effects , including extrapyramidal symptoms ( EPS ) , tardive dyskinesia , sedation , and possible impairment of some cognitive measures , as well as cardiac effects , orthostatic hypotension , hepatic changes , anticholinergic side effects , sexual dysfunction , and weight gain .

Example answer:
{"entities": [{"text": "extrapyramidal symptoms", "type": "Disease"}, {"text": "EPS", "type": "Disease"}, {"text": "tardive dyskinesia", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}]}

Example input:
Sentence: In phase A , extrapyramidal signs tended to be greater with the standard dose than in the other two conditions , primarily because of a subgroup ( 20 % ) who developed moderate to severe signs .

Example answer:
{"entities": [{"text": "extrapyramidal signs", "type": "Disease"}]}

Example input:
Sentence: Extrapyramidal symptoms reported as AEs occurred in 15 % and 18 % , 34 % , and 10 % of the asenapine at 5 and 10 mg BID , haloperidol , and placebo groups , respectively .

Example answer:
{"entities": [{"text": "Extrapyramidal symptoms", "type": "Disease"}, {"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Previous clinical studies have proposed that risperidone 's pharmacologic profile may produce improved efficacy for negative psychotic symptoms and decreased propensity for extrapyramidal side effects ; features shared by so-called 'atypical ' neuroleptics .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}, {"text": "psychotic symptoms", "type": "Disease"}]}

Example input:
Sentence: Extrapyramidal side effects with risperidone and haloperidol at comparable D2 receptor occupancy levels .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Input:
Sentence: Extrapyramidal symptom severity scores were 1.4 ( 95 % CI=1.2-1.6 ) with risperidone and 1.2 ( 95 % CI=1.0-1.4 ) with olanzapine .

## Item bc5cdr:test:3119
Example input:
Sentence: Reports of persistent paralysis after the discontinuance of these drugs have most often involved aminosteroid-based NMBAs such as vecuronium bromide , especially when used in conjunction with corticosteroids .

Example answer:
{"entities": [{"text": "paralysis", "type": "Disease"}, {"text": "vecuronium bromide", "type": "Chemical"}]}

Example input:
Sentence: In 24 patients with this complication , the marked slowing of motor nerve conduction velocity and the electromyographic changes imply mainly a demyelinating disorder .

Example answer:
{"entities": [{"text": "demyelinating disorder", "type": "Disease"}]}

Example input:
Sentence: Extra caution is warranted in treating infertility patients with CC , and patients should be well informed of this side effect before commencement of therapy .

Example answer:
{"entities": [{"text": "infertility", "type": "Disease"}, {"text": "CC", "type": "Chemical"}]}

Example input:
Sentence: None of the animals that received bupivacaine , normal saline , or normal saline titrated to a pH 3.0 developed hind-limb paralysis .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}, {"text": "paralysis", "type": "Disease"}]}

Example input:
Sentence: CNS complications included posterior reversible leukoencephalopathy syndrome ( n = 10 ) , stroke ( n = 5 ) , temporal lobe epilepsy ( n = 2 ) , high-dose methotrexate toxicity ( n = 2 ) , syndrome of inappropriate antidiuretic hormone secretion ( n = 1 ) , and other unclassified events ( n = 7 ) .

Example answer:
{"entities": [{"text": "leukoencephalopathy", "type": "Disease"}, {"text": "stroke", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "inappropriate antidiuretic hormone secretion", "type": "Disease"}]}

Example input:
Sentence: Cauda equina syndrome is a rare complication of epidural anesthesia .

Example answer:
{"entities": [{"text": "Cauda equina syndrome", "type": "Disease"}]}

Example input:
Sentence: A delayed complication in nine patients has been unilateral loss of vision secondary to a retinal vasculitis .

Example answer:
{"entities": [{"text": "loss of vision", "type": "Disease"}, {"text": "retinal vasculitis", "type": "Disease"}]}

Example input:
Sentence: Decompression and neurolysis were performed with good subsequent recovery of function .

Example answer:
{"entities": []}

Example input:
Sentence: It is necessary that both oncologists and neurologists be fully aware of this unusual complication .

Example answer:
{"entities": []}

Example input:
Sentence: In conclusion , CNS complications are frequent events during ALL therapy , and require rapid detection and prompt treatment to limit permanent damage .

Example answer:
{"entities": [{"text": "ALL", "type": "Disease"}]}

Input:
Sentence: Such complications are most important in situations where there is a pre-existing contralateral paralysis .

## Item bc5cdr:test:2978
Example input:
Sentence: Rizatriptan was also superior to ergotamine/caffeine in the proportions of patients with no nausea , vomiting , phonophobia or photophobia and for patients with normal function 2 h after drug intake ( p < or = 0.001 ) .

Example answer:
{"entities": [{"text": "Rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}, {"text": "nausea", "type": "Disease"}, {"text": "vomiting", "type": "Disease"}, {"text": "phonophobia", "type": "Disease"}, {"text": "photophobia", "type": "Disease"}]}

Example input:
Sentence: Drug-induced parkinsonism was observed in subjects treated with risperidone ( 42 % ) and haloperidol ( 29 % ) and was observed at occupancy levels above 60 % .

Example answer:
{"entities": [{"text": "Drug-induced parkinsonism", "type": "Disease"}, {"text": "risperidone", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: More patients were ( completely , very or somewhat ) satisfied 2 h after treatment with rizatriptan ( 69.8 % ) than at 2 h after treatment with ergotamine/caffeine ( 38.6 % , p < or = 0.001 ) .

Example answer:
{"entities": [{"text": "rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}]}

Example input:
Sentence: Importantly , both classical ( haloperidol ) and atypical ( olanzapine , clozapine and aripiprazole ) antipsychotics were effective in all these models of hyperactivity .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "olanzapine", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "aripiprazole", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}]}

Example input:
Sentence: Based on these observations , it is concluded that 5-HT2 blockade obtained with risperidone at D2 occupancy rates of 60 % and above does not appear to protect against the risk for extrapyramidal side effects .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}]}

Example input:
Sentence: Both risperidone and haloperidol produced D2 occupancy levels between approximately 60 and 90 % at standard clinical doses .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: To determine if routine risperidone treatment is associated with a unique degree of D2 receptor occupancy and pattern of clinical effects , we used [ 123I ] IBZM SPECT to determine D2 occupancy in subjects treated with routine clinical doses of risperidone ( n = 12 ) or haloperidol ( n = 7 ) .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Risperidone is an antipsychotic drug with high affinity at dopamine D2 and serotonin 5-HT2 receptors .

Example answer:
{"entities": [{"text": "Risperidone", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "serotonin 5-HT2", "type": "Chemical"}]}

Example input:
Sentence: There was no significant difference between occupancy levels obtained with haloperidol or risperidone .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "risperidone", "type": "Chemical"}]}

Example input:
Sentence: Previous clinical studies have proposed that risperidone 's pharmacologic profile may produce improved efficacy for negative psychotic symptoms and decreased propensity for extrapyramidal side effects ; features shared by so-called 'atypical ' neuroleptics .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}, {"text": "psychotic symptoms", "type": "Disease"}]}

Input:
Sentence: CONCLUSIONS : Clinical outcomes with risperidone were equal to those with olanzapine , and response may be more stable .

## Item bc5cdr:test:3138
Example input:
Sentence: There was no significant difference in the frequency of signs or symptoms between the two groups although neurotoxicity symptoms presented mostly with lower scores of severity in group G. However , this difference reached statistical significance only with regard to reported pain sensation ( P = 0.011 ) .

Example answer:
{"entities": [{"text": "neurotoxicity", "type": "Disease"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: Drug-induced gross activity counts were increased in the novel exploratory box only , while measures of stereotypic behavior were similar in both .

Example answer:
{"entities": []}

Example input:
Sentence: MDMA polydrug users show process-specific central executive impairments coupled with impaired social and emotional judgement processes .

Example answer:
{"entities": [{"text": "MDMA", "type": "Chemical"}, {"text": "impaired social and emotional judgement processes", "type": "Disease"}]}

Example input:
Sentence: These data lend further support to the proposal that cognitive processes mediated by the prefrontal cortex may be impaired by recreational ecstasy use .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: A conjunction analysis of the encode and recall phases of the task revealed ecstasy-specific hyperactivity in bilateral frontal regions , left temporal , right parietal , bilateral temporal , and bilateral occipital brain regions .

Example answer:
{"entities": [{"text": "ecstasy-specific", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}]}

Example input:
Sentence: Ecstasy users performed significantly worse in learning and memory compared to controls and cannabis users .

Example answer:
{"entities": [{"text": "Ecstasy", "type": "Chemical"}, {"text": "cannabis", "type": "Chemical"}]}

Example input:
Sentence: Memory retrieval of experiences acquired prior to cocaine administration was impaired and negatively correlated with NFkappaB activity in the frontal cortex .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Fifteen polydrug ecstasy users and 15 polydrug non-ecstasy user controls completed a general drug use questionnaire , the Brixton Spatial Anticipation task ( set shifting ) , Backward Digit Span procedure ( memory updating ) , Inhibition of Return ( inhibition ) , an emotional intelligence scale , the Tromso Social Intelligence Scale and the Dysexecutive Questionnaire ( DEX ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : We found that cocaine dose-dependently increased anxiety-like behavior in control ( Dbh +/- ) mice , as measured by a decrease in open arm exploration .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "anxiety-like", "type": "Disease"}]}

Example input:
Sentence: Using functional imaging and a face-learning task , we investigated neural correlates of encoding and recalling face-name associations in 20 recreational drug users whose predominant drug use was ecstasy and 20 controls .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Input:
Sentence: RESULTS : There were no group differences in psychopathology or `` eyes task '' performance , but the RC group , who otherwise had similar illicit substance use histories to the OC group , exhibited impaired fear recognition accuracy compared to the OC and CN groups .

## Item bc5cdr:test:3000
Example input:
Sentence: Nitroprusside caused significant decreases in arterial blood pressure and systemic vascular resistance and increases in heart rate , but did not change cardiac output or QS/QT .

Example answer:
{"entities": [{"text": "Nitroprusside", "type": "Chemical"}, {"text": "decreases in arterial blood pressure", "type": "Disease"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: Since nonsteroidal anti-inflammatory agents interfere with this compensatory mechanism and may cause acute renal failure , they should be used with caution in such patients .

Example answer:
{"entities": [{"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: These studies suggest that both phenacetin and acetaminophen may contribute to the burden of ESRD , with the risk of the latter being somewhat less than that of the former .

Example answer:
{"entities": [{"text": "phenacetin", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: The aim of the experiment was to evaluate the developmental toxicity of the non-selective ( piroxicam ) and selective ( DFU ; 5,5-dimethyl-3- ( 3-fluorophenyl ) -4- ( 4-methylsulphonyl ) phenyl-2 ( 5H ) -furanon ) COX-2 inhibitors .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "piroxicam", "type": "Chemical"}, {"text": "DFU", "type": "Chemical"}, {"text": "5,5-dimethyl-3- ( 3-fluorophenyl ) -4- ( 4-methylsulphonyl ) phenyl-2 ( 5H ) -furanon", "type": "Chemical"}]}

Example input:
Sentence: The pooled statistical analysis for ventricular septal ( VSD ) and midline ( MD ) defects was performed for rat fetuses exposed to piroxicam , selective and non-selective COX-2 inhibitor based on present and historic data .

Example answer:
{"entities": [{"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: Comparison of developmental toxicity of selective and non-selective cyclooxygenase-2 inhibitors in CRL : ( WI ) WUBR Wistar rats -- DFU and piroxicam study .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "DFU", "type": "Chemical"}, {"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : Both selective and non-selective COX-2 inhibitors were toxic for rats fetuses when administered in the highest dose .

Example answer:
{"entities": []}

Example input:
Sentence: Prenatal exposure to selective COX-2 inhibitors does not increase the risk of ventricular septal and midline defects in rat when compared to non-selective drugs and historic control .

Example answer:
{"entities": []}

Example input:
Sentence: Prenatal exposure to non-selective COX inhibitors increases the risk of VSD and MD when compared to historic control but not with selective COX-2 inhibitors .

Example answer:
{"entities": []}

Input:
Sentence: Risks and benefits of COX-2 inhibitors vs non-selective NSAIDs : does their cardiovascular risk exceed their gastrointestinal benefit ?

## Item bc5cdr:test:3162
Example input:
Sentence: Propylthiouracil therapy was withdrawn , and she was treated with a 1-month course of prednisone , which alleviated her symptoms .

Example answer:
{"entities": [{"text": "Propylthiouracil", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : This study demonstrates that chronic FK506 nephropathy consists primarily of arteriolopathy manifesting as insudative hyalinosis of the arteriolar wall , and suggests that mild-type chronic FK506 nephropathy is a condition which may lead to deterioration of renal allograft function .

Example answer:
{"entities": [{"text": "FK506", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: The patient cohort ( 14 men , 11 women ) was treated with SRL as conversion therapy , due to chronic allograft nephropathy ( CAN ) ( n = 15 ) neoplasia ( n = 8 ) ; Kaposi 's sarcoma , Four skin cancers , One intestinal tumors , One renal cell carsinom ) or BK virus nephropathy ( n = 2 ) .

Example answer:
{"entities": [{"text": "SRL", "type": "Chemical"}, {"text": "chronic allograft nephropathy", "type": "Disease"}, {"text": "CAN", "type": "Disease"}, {"text": "neoplasia", "type": "Disease"}, {"text": "Kaposi 's sarcoma", "type": "Disease"}, {"text": "skin cancers", "type": "Disease"}, {"text": "intestinal tumors", "type": "Disease"}, {"text": "renal cell carsinom", "type": "Disease"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : An association has been found between transplant glomerulopathy ( TG ) and reduplication of peritubular capillary basement membranes ( PTCR ) .

Example answer:
{"entities": [{"text": "transplant glomerulopathy", "type": "Disease"}, {"text": "TG", "type": "Disease"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Example input:
Sentence: A case of triamterene nephrolithiasis is reported in a man after 4 years of hydrochlorothiazide-triamterene therapy for hypertension .

Example answer:
{"entities": [{"text": "triamterene", "type": "Chemical"}, {"text": "nephrolithiasis", "type": "Disease"}, {"text": "hydrochlorothiazide-triamterene", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: Peritubular capillary basement membrane reduplication in allografts and native kidney disease : a clinicopathologic study of 278 consecutive renal specimens .

Example answer:
{"entities": [{"text": "kidney disease", "type": "Disease"}]}

Example input:
Sentence: In this report we describe the case of a 37-year-old white woman with Ebstein 's anomaly , who developed a rare syndrome called platypnea-orthodeoxia , characterized by massive right-to-left interatrial shunting with transient profound hypoxia and cyanosis .

Example answer:
{"entities": [{"text": "Ebstein 's anomaly", "type": "Disease"}, {"text": "platypnea-orthodeoxia", "type": "Disease"}, {"text": "hypoxia", "type": "Disease"}, {"text": "cyanosis", "type": "Disease"}]}

Example input:
Sentence: Extracorporeal lithotripsy successfully removed a renal calculus in one patient and surgery removed a staghorn calculus in another , permitting continued treatment .

Example answer:
{"entities": [{"text": "renal calculus", "type": "Disease"}, {"text": "calculus", "type": "Disease"}]}

Example input:
Sentence: METHODS : A double-blind double-armed prospective study comprised 40 patients who had uneventful sutureless phacoemulsification under sub-Tenon 's local infiltration of 3 mL of plain lignocaine .

Example answer:
{"entities": [{"text": "lignocaine", "type": "Chemical"}]}

Input:
Sentence: Two patients needed a lateral tarsorrhaphy for persistent epithelial defects .

## Item bc5cdr:test:3156
Example input:
Sentence: METHODS : We used computerized pharmacy records to identify all adult psychiatric inpatients treated with clozapine ( 1995-96 ) , reviewed their medical records to score incidence and severity of delirium , and tested associations with potential risk factors .

Example answer:
{"entities": [{"text": "psychiatric", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "delirium", "type": "Disease"}]}

Example input:
Sentence: METHODS : Retrospective review of medical records of 236 patients with hyperthyroidism admitted in our department ( in- or out-patients ) from 1986 to 1992 .

Example answer:
{"entities": [{"text": "hyperthyroidism", "type": "Disease"}]}

Example input:
Sentence: A 34-year-old lady developed a constellation of dermatitis , fever , lymphadenopathy and hepatitis , beginning on the 17th day of a course of oral sulphasalazine for sero-negative rheumatoid arthritis .

Example answer:
{"entities": [{"text": "dermatitis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "lymphadenopathy", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Example input:
Sentence: Skin tests were performed with benzylpenicilloyl-poly-L-lysine ( BPO-PLL ) , benzylpenicilloate , benzylpenicillin ( PG ) , ampicillin ( AMP ) , and AX .

Example answer:
{"entities": [{"text": "benzylpenicilloyl-poly-L-lysine", "type": "Chemical"}, {"text": "BPO-PLL", "type": "Chemical"}, {"text": "benzylpenicilloate", "type": "Chemical"}, {"text": "benzylpenicillin", "type": "Chemical"}, {"text": "PG", "type": "Chemical"}, {"text": "ampicillin", "type": "Chemical"}, {"text": "AMP", "type": "Chemical"}, {"text": "AX", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : The main pathologic diagnoses ( some overlap ) were acute rejection ( AR ; n = 4 ) , chronic rejection ( CR ; n=5 ) , AR+CR ( n =4 ) , recurrent IgA nephropathy ( n =5 ) , normal findings ( n =2 ) , minimal-type chronic FK506 nephropathy ( n = 9 ) , and mild-type FK506 nephropathy ( n = 11 ) .

Example answer:
{"entities": [{"text": "IgA nephropathy", "type": "Disease"}, {"text": "FK506", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: METHODS : A review of admissions during a 6-year period revealed 14 patients with cocaine-related aneurysms .

Example answer:
{"entities": [{"text": "cocaine-related", "type": "Chemical"}, {"text": "aneurysms", "type": "Disease"}]}

Example input:
Sentence: These 13 included cases of malignant hypertension , thrombotic microangiopathy , lupus nephritis , Henoch-Schonlein nephritis , crescentic glomerulonephritis , and cocaine-related acute renal failure .

Example answer:
{"entities": [{"text": "malignant hypertension", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "lupus nephritis", "type": "Disease"}, {"text": "Henoch-Schonlein nephritis", "type": "Disease"}, {"text": "glomerulonephritis", "type": "Disease"}, {"text": "cocaine-related", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: A few minutes after administration of the drugs , they presented urticaria ( patients 1 and 2 ) and conjunctivitis ( patient 1 ) .

Example answer:
{"entities": [{"text": "urticaria", "type": "Disease"}, {"text": "conjunctivitis", "type": "Disease"}]}

Example input:
Sentence: A 45-year-old man , an admitted frequent cocaine user , presented to the Emergency Department ( ED ) on two separate occasions with a history of priapism after cocaine use .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "priapism", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : This case started with a media report in a popular newspaper , initiated by published , peer-reviewed research on herbals , and involved human failure in a case history , medical examination and clinical treatment .

Example answer:
{"entities": []}

Input:
Sentence: METHODS : Review of all cases of corneal ulcers associated with drug abuse seen at our institution from July 2006 to December 2006 .

## Item bc5cdr:test:3281
Example input:
Sentence: A nerve conduction study was consistent with severe sensorimotor axonal polyneuropathy .

Example answer:
{"entities": [{"text": "polyneuropathy", "type": "Disease"}]}

Example input:
Sentence: In SE survivors , similar stimulation resulted in a population spike followed , at a variable latency , by negative DC shifts and repetitive afterdischarges of 3-60 s duration , which were blocked by ionotropic glutamate receptor antagonists .

Example answer:
{"entities": [{"text": "SE", "type": "Disease"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: Enalapril treatment blunted but did not prevent reduction in GFR in group 4 ( 0.86 +/- 0.15 ml/min at 4 months , 0.69 +/- 0.13 ml/min at 6 months , both P less than 0.05 vs. group 3 ) .

Example answer:
{"entities": [{"text": "Enalapril", "type": "Chemical"}]}

Example input:
Sentence: Rg1 , as a ginsenoside extracted from Panax ginseng , could ameliorate spatial learning impairment .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "ginsenoside", "type": "Chemical"}, {"text": "learning impairment", "type": "Disease"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: Desferrioxamine withdrawal resulted in a complete recovery of visual function in 1 patient and partial recovery in 3 , and a complete reversal of hearing loss in 3 patients and partial recovery in 3 .

Example answer:
{"entities": [{"text": "Desferrioxamine", "type": "Chemical"}, {"text": "hearing loss", "type": "Disease"}]}

Example input:
Sentence: In both types , purinoceptor desensitization with alpha , beta-methylene adenosine-5'-triphosphate ( alpha , beta-meATP ) caused further reductions at low frequencies ( < 10 Hz ) .

Example answer:
{"entities": [{"text": "alpha , beta-methylene adenosine-5'-triphosphate", "type": "Chemical"}, {"text": "alpha , beta-meATP", "type": "Chemical"}]}

Example input:
Sentence: Decompression and neurolysis were performed with good subsequent recovery of function .

Example answer:
{"entities": []}

Example input:
Sentence: The normalized reflex amplitude was significantly higher during pain , but only at faster stretches in the painful muscle .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "painful muscle", "type": "Disease"}]}

Example input:
Sentence: Up until now , the only factor studied has been the effect of the diameter of the spinal needle on post-operative sensorineural hearing loss .

Example answer:
{"entities": [{"text": "sensorineural hearing loss", "type": "Disease"}]}

Input:
Sentence: CONCLUSIONS : Sural nerve SAP amplitude reduction is a reliable and sensitive marker of degeneration and recovery of sensory fibres .

## Item bc5cdr:test:3091
Example input:
Sentence: BACKGROUND : Although intravitreal aminoglycosides have substantially improved visual prognosis in endophthalmitis , macular infarction may impair full visual recovery .

Example answer:
{"entities": [{"text": "aminoglycosides", "type": "Chemical"}, {"text": "endophthalmitis", "type": "Disease"}, {"text": "infarction", "type": "Disease"}]}

Example input:
Sentence: We suggest that our patient 's tubular dysfunction and myopathy may have resulted from mitochondrial dysfunction which is triggered by tacrolimus and augmented by lamivudine .

Example answer:
{"entities": [{"text": "tubular dysfunction", "type": "Disease"}, {"text": "myopathy", "type": "Disease"}, {"text": "mitochondrial dysfunction", "type": "Disease"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: The objectives were to assess the efficacy of lamivudine in reducing the incidence of HBV reactivation , and diminishing morbidity and mortality during CT. Two groups were compared in this study .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: By implantation of electrodes and electrophysiological recording in vivo , the results showed that Rg1 restored the long-term potentiation ( LTP ) impaired by morphine in both freely moving and anaesthetised rats .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: In a placebo-controlled , single-blinded , crossover study , we assessed the effect of `` real '' repetitive transcranial magnetic stimulation ( rTMS ) versus `` sham '' rTMS ( placebo ) on peak dose dyskinesias in patients with Parkinson 's disease ( PD ) .

Example answer:
{"entities": [{"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: It is concluded that L-dopa enhances reflex bradycardia through central alpha-receptor stimulation .

Example answer:
{"entities": [{"text": "L-dopa", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: The electrophysiological recording in vitro showed that Rg1 restored the LTP in slices from the rats treated with morphine , but not changed LTP in the slices from normal saline- or morphine/Rg1-treated rats ; this restoration could be inhibited by N-methyl-D-aspartate ( NMDA ) receptor antagonist MK801 .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}, {"text": "morphine/Rg1-treated", "type": "Chemical"}, {"text": "N-methyl-D-aspartate", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "MK801", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVE : This is to present reversible inferior colliculus lesions in metronidazole-induced encephalopathy , to focus on the diffusion-weighted imaging ( DWI ) and fluid attenuated inversion recovery ( FLAIR ) imaging .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "Disease"}, {"text": "metronidazole-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: We conclude that Rg1 may significantly improve the spatial learning capacity impaired by chonic morphine administration and restore the morphine-inhibited LTP .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}, {"text": "morphine-inhibited", "type": "Chemical"}]}

Example input:
Sentence: Because such a compensatory mechanism most likely occurs to reduce injury to the brain from cytotoxic compounds , the present data substantiate the concept that MRP2 performs a protective role in the BBB .

Example answer:
{"entities": [{"text": "injury to the brain", "type": "Disease"}]}

Input:
Sentence: However , the direct benefits of this possible reshaping on LV function in the absence of underlying MR remain incompletely understood .

## Item bc5cdr:test:3303
Example input:
Sentence: The latter group was further sub-divided into 13 occult HBV ( HBsAg-negative ) and 7 overt HBV ( HBsAg- positive ) patients .

Example answer:
{"entities": [{"text": "HBsAg-negative", "type": "Chemical"}, {"text": "HBsAg-", "type": "Chemical"}]}

Example input:
Sentence: Groups 1 and 3 remained untreated while groups 2 and 4 received enalapril .

Example answer:
{"entities": [{"text": "enalapril", "type": "Chemical"}]}

Example input:
Sentence: Analysis of neurotransmitter concentration in some brain regions on the test day showed that dopamine concentration of the vehicle/scopolamine group was significantly lower than that of the vehicle/vehicle group , but this phenomenon was reversed when s-limonene or s-perillyl alcohol were administered before the injection of scopolamine .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "s-limonene", "type": "Chemical"}, {"text": "s-perillyl alcohol", "type": "Chemical"}, {"text": "scopolamine", "type": "Chemical"}]}

Example input:
Sentence: Ten rats received saline as a control group .

Example answer:
{"entities": []}

Example input:
Sentence: However , by comparing each subgroup to control group , we found statistically significant decreases of TEOAEs amplitudes at 4000Hz for all three groups .

Example answer:
{"entities": [{"text": "decreases of TEOAEs amplitudes", "type": "Disease"}]}

Example input:
Sentence: The patients were randomly allocated to one of three groups ; those in group A ( n = 10 ) were subjected to controlled hypotension alone , those in group B ( n = 10 ) to haemodilution alone and those in group C ( n = 10 ) to both controlled hypotension and haemodilution .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}]}

Example input:
Sentence: However , the concomitant occurrence of HBeAg negativity ( PC/BCP ) , sP120T , and LAM resistance resulted in the restoration of replication to levels of wild-type HBV .

Example answer:
{"entities": [{"text": "HBeAg", "type": "Chemical"}, {"text": "LAM", "type": "Chemical"}]}

Example input:
Sentence: Replication-competent HBV strains with sG145R or sP120T and LAM resistance ( rtM204I or rtL180M/rtM204V ) were generated on an HBeAg-positive and an HBeAg-negative background with precore ( PC ) and basal core promoter ( BCP ) mutants .

Example answer:
{"entities": [{"text": "LAM", "type": "Chemical"}, {"text": "HBeAg-positive", "type": "Chemical"}, {"text": "HBeAg-negative", "type": "Chemical"}]}

Example input:
Sentence: In the control group neither ischemic ST change nor localized spasm occurred .

Example answer:
{"entities": [{"text": "spasm", "type": "Disease"}]}

Example input:
Sentence: Experimental design consisted of four groups : control ( vehicle alone ) , GSPE alone , drug alone and GSPE+drug .

Example answer:
{"entities": [{"text": "GSPE", "type": "Chemical"}, {"text": "GSPE+drug", "type": "Chemical"}]}

Input:
Sentence: Two control groups ( SH ( 6 ) , SH ( 12 ) ) received vehicle .

## Item bc5cdr:test:3306
Example input:
Sentence: Treatment , given every 21 days for a maximum of three cycles , consisted of paclitaxel by 3-hour infusion followed the next day by a fixed dose of cisplatin ( 75 mg/m2 ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: INTERVENTION : Each patient received either intravenous docetaxel 30 mg/m2/week for 3 consecutive weeks , followed by 1 week off , or the combination of continuous oral thalidomide 200 mg every evening plus the same docetaxel regimen .

Example answer:
{"entities": [{"text": "docetaxel", "type": "Chemical"}, {"text": "thalidomide", "type": "Chemical"}]}

Example input:
Sentence: Serial audiograms should be performed every six months in those without problems and more frequently in young patients with normal serum ferritin values and in those with auditory dysfunction .

Example answer:
{"entities": [{"text": "auditory dysfunction", "type": "Disease"}]}

Example input:
Sentence: One week later , the patient was again extubated and 3 days later was transferred to a peripheral ward .

Example answer:
{"entities": []}

Example input:
Sentence: A second echocardiography was performed ( median interval : 13 months ) after pergolide withdrawal ( n=10 patients ) .

Example answer:
{"entities": [{"text": "pergolide", "type": "Chemical"}]}

Example input:
Sentence: Most had hyperacute presentation ; the median icterus encephalopathy interval was 4.5 ( 0-30 ) days .

Example answer:
{"entities": [{"text": "icterus", "type": "Disease"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Participants underwent polysomnographic sleep recordings on days 1 to 3 , 7 to 9 , and 14 to 16 ( first , second , and third weeks of abstinence ) .

Example answer:
{"entities": []}

Example input:
Sentence: The 3-week sulphasalazine syndrome strikes again .

Example answer:
{"entities": [{"text": "sulphasalazine", "type": "Chemical"}]}

Example input:
Sentence: Instillation was repeated twice during the first week , then weekly during the first month and afterwards monthly for 1 year .

Example answer:
{"entities": []}

Example input:
Sentence: This 4-week cycle was repeated until there was evidence of excessive toxicity or disease progression .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Input:
Sentence: twice in a 3-week interval .

## Item bc5cdr:test:3021
Example input:
Sentence: Infusion regimens were designed that rapidly achieved and maintained target-free concentrations of these drugs in plasma and data on the relationship between free concentration and changes in MAPD were obtained for these compounds .

Example answer:
{"entities": []}

Example input:
Sentence: Animals were administered nicotine , carbachol , or neostigmine via timed tail vein infusion , and the latencies to onset of tremor and clonus were recorded and converted to threshold dose .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}, {"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: High-dose 5-fluorouracil/folinic acid infusion therapy has recently become a popular regimen for various cancers .

Example answer:
{"entities": [{"text": "5-fluorouracil/folinic acid", "type": "Chemical"}, {"text": "cancers", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Sixty-seven of 926 patients ( 7.2 % ) required discontinuation of spironolactone due to hyperkalemia ( n = 33 ) or renal failure ( n = 34 ) .

Example answer:
{"entities": [{"text": "spironolactone", "type": "Chemical"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: Numerous anecdotal reports suggest that products containing quinine may produce neurological complications , including confusion , altered mental status , seizures , and coma , particularly in older women .

Example answer:
{"entities": [{"text": "quinine", "type": "Chemical"}, {"text": "neurological complications", "type": "Disease"}, {"text": "confusion", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "coma", "type": "Disease"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Disease"}]}

Example input:
Sentence: Psychologists need to inquire about consumption of quinine-containing beverages as part of an evaluation process .

Example answer:
{"entities": [{"text": "quinine-containing", "type": "Chemical"}]}

Example input:
Sentence: Dobutamine infusion at 10 micrograms/kg per min was discontinued after six studies secondary to a 50 % incidence rate of adverse symptoms .

Example answer:
{"entities": [{"text": "Dobutamine", "type": "Chemical"}]}

Example input:
Sentence: Although the United States Food and Drug Administration banned its use for nocturnal leg cramps due to lack of safety and efficacy , quinine is widely available in beverages including tonic water and bitter lemon .

Example answer:
{"entities": [{"text": "nocturnal leg cramps", "type": "Disease"}, {"text": "quinine", "type": "Chemical"}]}

Example input:
Sentence: The infusion was discontinued either when there was no muscular response to tetanic stimulation of the ulnar nerve or when Sch 120 mg was exceeded .

Example answer:
{"entities": [{"text": "tetanic", "type": "Disease"}, {"text": "Sch", "type": "Chemical"}]}

Input:
Sentence: Quinine infusion was discontinued and changed with sulfate quinine tablets .

## Item bc5cdr:test:2795
Example input:
Sentence: In the present study , cis-platin ( 80-120 mg/m2BSA ) and 5-FU ( 1000 mg/m2BSA daily as a continuous infusion during 5 days ) were given to 76 patients before radiotherapy and surgery .

Example answer:
{"entities": [{"text": "cis-platin", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}]}

Example input:
Sentence: After the administration of NG , 5-FU and CY neither a statistically significant increase in creatinine concentration nor an increase in creatinine clearance was observed compared to the group receiving no cytostatics .

Example answer:
{"entities": [{"text": "NG", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "CY", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: A 78-year-old with healed septal necrosis suffered a recurrent myocardial infarction of the anterior wall following the administration of isosorbide dinitrate 5 mg sublingually .

Example answer:
{"entities": [{"text": "necrosis", "type": "Disease"}, {"text": "myocardial infarction", "type": "Disease"}, {"text": "isosorbide dinitrate", "type": "Chemical"}]}

Example input:
Sentence: It is concluded that patients on 5-FU treatment should be under close supervision and that the treatment should be discontinued if chest pain or tachyarrhythmia is observed .

Example answer:
{"entities": [{"text": "5-FU", "type": "Chemical"}, {"text": "chest pain", "type": "Disease"}, {"text": "tachyarrhythmia", "type": "Disease"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: This complication reappeared on day 25 during the second dose of 5-fluorouracil and folinic acid , which were then the only drugs given .

Example answer:
{"entities": [{"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: Because folinic acid was unlikely to be associated with this condition , neurotoxicity due to high-dose 5-fluorouracil was highly suspected .

Example answer:
{"entities": [{"text": "folinic acid", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}]}

Example input:
Sentence: An allergic reaction consisting of angioneurotic edema secondary to continuous infusion 5-fluorouracil occurred in a patient with recurrent carcinoma of the oral cavity , cirrhosis , and cisplatin-induced impaired renal function .

Example answer:
{"entities": [{"text": "allergic reaction", "type": "Disease"}, {"text": "angioneurotic edema", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "carcinoma of the oral cavity", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "impaired renal function", "type": "Disease"}]}

Example input:
Sentence: Acute confusion induced by a high-dose infusion of 5-fluorouracil and folinic acid .

Example answer:
{"entities": [{"text": "confusion", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: He developed acute neurologic symptoms of mental confusion , disorientation and irritability , and then lapsed into a deep coma , lasting for approximately 40 hours during the first dose ( day 2 ) of 5-fluorouracil and folinic acid infusion .

Example answer:
{"entities": [{"text": "confusion", "type": "Disease"}, {"text": "disorientation", "type": "Disease"}, {"text": "irritability", "type": "Disease"}, {"text": "coma", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Input:
Sentence: After admission , the patient received a continuous intravenous infusion of 5-FU ( 1000 mg/day ) , during which precordial pain with right bundle branch block occurred concomitantly with a high serum FBAL concentration of 1955 ng/ml .

## Item bc5cdr:test:2960
Example input:
Sentence: CONCLUSIONS : Clonidine , used alone or with methylphenidate , appears safe and well tolerated in childhood ADHD .

Example answer:
{"entities": [{"text": "Clonidine", "type": "Chemical"}, {"text": "methylphenidate", "type": "Chemical"}, {"text": "ADHD", "type": "Disease"}]}

Example input:
Sentence: The present study was designed to study the effect of histamine H ( 3 ) -receptor ligands on neuroleptic-induced catalepsy , apomorphine-induced climbing behavior and amphetamine-induced locomotor activities in mice .

Example answer:
{"entities": [{"text": "histamine", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "apomorphine-induced", "type": "Chemical"}, {"text": "amphetamine-induced", "type": "Chemical"}]}

Example input:
Sentence: The alpha3 and beta4 nicotinic acetylcholine receptor subunits are necessary for nicotine-induced seizures and hypolocomotion in mice .

Example answer:
{"entities": [{"text": "acetylcholine", "type": "Chemical"}, {"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "hypolocomotion", "type": "Disease"}]}

Example input:
Sentence: A 3-year-old girl had behavioral deterioration , with hyperkinesis , irritability , and sleeping difficulties after the therapeutic administration of isoniazid .

Example answer:
{"entities": [{"text": "behavioral deterioration", "type": "Disease"}, {"text": "hyperkinesis", "type": "Disease"}, {"text": "irritability", "type": "Disease"}, {"text": "sleeping difficulties", "type": "Disease"}, {"text": "isoniazid", "type": "Chemical"}]}

Example input:
Sentence: The present study was designed to evaluate two endogenous and one synthetic neuroactive steroid that positively modulate the gamma-aminobutyric acid ( GABA ( A ) ) receptor against the increase in sensitivity to the convulsant effects of cocaine engendered by repeated cocaine administration ( seizure kindling ) .

Example answer:
{"entities": [{"text": "steroid", "type": "Chemical"}, {"text": "gamma-aminobutyric acid", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: METHOD : In a 16-week multicenter , double-blind trial , 122 children with ADHD were randomly assigned to clonidine ( n = 31 ) , methylphenidate ( n = 29 ) , clonidine and methylphenidate ( n = 32 ) , or placebo ( n = 30 ) .

Example answer:
{"entities": [{"text": "ADHD", "type": "Disease"}, {"text": "clonidine", "type": "Chemical"}, {"text": "methylphenidate", "type": "Chemical"}]}

Example input:
Sentence: Terbutaline , a beta2-adrenoceptor agonist used to arrest preterm labor , has been associated with increased concordance for autism in dizygotic twins .

Example answer:
{"entities": [{"text": "Terbutaline", "type": "Chemical"}, {"text": "preterm labor", "type": "Disease"}, {"text": "autism", "type": "Disease"}]}

Example input:
Sentence: Galanthamine hydrobromide , a longer acting anticholinesterase drug , in the treatment of the central effects of scopolamine ( Hyoscine ) .

Example answer:
{"entities": [{"text": "Galanthamine hydrobromide", "type": "Chemical"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "Hyoscine", "type": "Chemical"}]}

Example input:
Sentence: Neuroinflammation and behavioral abnormalities after neonatal terbutaline treatment in rats : implications for autism .

Example answer:
{"entities": [{"text": "Neuroinflammation", "type": "Disease"}, {"text": "behavioral abnormalities", "type": "Disease"}, {"text": "terbutaline", "type": "Chemical"}, {"text": "autism", "type": "Disease"}]}

Example input:
Sentence: Galanthamine hydrobromide , an anticholinesterase drug capable of penetrating the blood-brain barrier , was used in a patient demonstrating central effects of scopolamine ( hyoscine ) overdosage .

Example answer:
{"entities": [{"text": "Galanthamine hydrobromide", "type": "Chemical"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "hyoscine", "type": "Chemical"}, {"text": "overdosage", "type": "Disease"}]}

Input:
Sentence: The purpose of this study was to assess the use of galantamine , an acetylcholinesterase inhibitor and nicotinic receptor modulator , in the treatment of interfering behaviors in children with autism .

## Item bc5cdr:test:3206
Example input:
Sentence: Pretreatment with L-NOArg and L-NIL but not 7-NI , significantly increases antihyperalgesic activity both HOE 140 and des Arg10 HOE 140 .

Example answer:
{"entities": [{"text": "HOE 140", "type": "Chemical"}, {"text": "des Arg10 HOE 140", "type": "Chemical"}]}

Example input:
Sentence: Ketamine reduced both the area of brush-evoked and punctate-evoked hyperalgesia significantly and it tended to reduce brush-evoked pain .

Example answer:
{"entities": [{"text": "Ketamine", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: PURPOSE : The influence of an irreversible inhibitor of constitutive NO synthase ( L-NOArg ; 1.0 mg/kg ip ) , a relatively selective inhibitor of inducible NO synthase ( L-NIL ; 1.0 mg/kg ip ) and a relatively specific inhibitor of neuronal NO synthase ( 7-NI ; 0.1 mg/kg ip ) , on antihyperalgesic action of selective antagonists of B2 and B1 receptors : D-Arg- [ Hyp3 , Thi5 , D-Tic7 , Oic8 ] bradykinin ( HOE 140 ; 70 nmol/kg ip ) or des Arg10 HOE 140 ( 70 nmol/kg ip ) respectively , in model of diabetic ( streptozotocin-induced ) and toxic ( vincristine-induced ) neuropathy was investigated .

Example answer:
{"entities": [{"text": "NO", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}, {"text": "HOE 140", "type": "Chemical"}, {"text": "des Arg10 HOE 140", "type": "Chemical"}]}

Example input:
Sentence: Animal and clinical studies have suggested that N-methyl-D-aspartate ( NMDA ) antagonists , such as ketamine , may be effective in improving opioid analgesia in difficult pain syndromes , such as neuropathic pain .

Example answer:
{"entities": [{"text": "N-methyl-D-aspartate", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "ketamine", "type": "Chemical"}, {"text": "pain", "type": "Disease"}, {"text": "neuropathic pain", "type": "Disease"}]}

Example input:
Sentence: We conclude that lidocaine reduces the incidence and severity of propofol injection pain in ambulatory patients whereas thiopentone only reduces its severity .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "propofol", "type": "Chemical"}, {"text": "pain", "type": "Disease"}, {"text": "thiopentone", "type": "Chemical"}]}

Example input:
Sentence: To determine if the addition of a buffering solution to adjust the pH of lidocaine into the physiologic range would reduce pain during injection , we performed a blinded randomized study in patients undergoing cardiac catheterization .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: The local anesthetic-induced mortality was significantly increased by the three different calcium channel blockers .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}]}

Example input:
Sentence: We have examined the effect of systemic administration of ketamine and lidocaine on brush-evoked ( dynamic ) pain and punctate-evoked ( static ) hyperalgesia induced by capsaicin .

Example answer:
{"entities": [{"text": "ketamine", "type": "Chemical"}, {"text": "lidocaine", "type": "Chemical"}, {"text": "pain", "type": "Disease"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: Reduction in injection pain using buffered lidocaine as a local anesthetic before cardiac catheterization .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: Lidocaine reduced the area of punctate-evoked hyperalgesia significantly .

Example answer:
{"entities": [{"text": "Lidocaine", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}]}

Input:
Sentence: BACKGROUND : In addition to blocking nociceptive input from surgical sites , long-acting local anesthetics might directly modulate inflammation .

## Item bc5cdr:test:3322
Example input:
Sentence: Using as the reference group women who were not using oral contraception , had no recent pregnancy or menopausal symptoms , the case-control analysis gave an adjusted odds ratio ( OR ( adj ) ) of 7.44 ( 95 % CI 3.67-15.08 ) for CPA/EE use compared with an OR ( adj ) of 2.58 ( 95 % CI 1.60-4.18 ) for use of conventional COCs .

Example answer:
{"entities": [{"text": "CPA/EE", "type": "Chemical"}]}

Example input:
Sentence: Mean peak forced expiratory volume in 1 second ( FEV1 ) increases over baseline and the proportion of patients attaining at least a 15 % increase in the FEV1 ( responders ) were 31 % and 90 % , respectively , for ipratropium and 17 % and 50 % , respectively , for theophylline .

Example answer:
{"entities": [{"text": "ipratropium", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}]}

Example input:
Sentence: Before the switch , 11.5 % of patients had high-grade proteinuria ( > 1.0 g/day ) ; this increased to 22.9 % postswitch ( p = 0.006 ) .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: Multivariate stepwise logistic regression analysis using preoperative and postoperative variables identified that an increase of serum creatinine compared with average at 1 year , 3 months , and 4 weeks postoperatively were independent risk factors for the development of CRF or ESRD with odds ratios of 2.6 , 2.2 , and 1.6 , respectively .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: The Receiver Operative Characteristic Curve showed that OD > 1.27 in the isolated-HIT group had a significantly higher chance of developing thrombosis by day 30 .

Example answer:
{"entities": [{"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: Among women who used oral contraceptives , the odds ratio was 2.1 ( 95 percent confidence interval , 1.5 to 3.0 ) for those without a prothrombotic mutation and 1.9 ( 95 percent confidence interval , 0.6 to 5.5 ) for those with a mutation CONCLUSIONS : The risk of myocardial infarction was increased among women who used second-generation oral contraceptives .

Example answer:
{"entities": [{"text": "oral contraceptives", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Compared to controls , aortic regurgitation ( OR : 3.1 ; 95 % IC : 1.1-8.8 ) and mitral regurgitation ( OR : 10.7 ; 95 % IC : 2.1-53 ) were more frequent in PD patients ( tricuspid : NS ) .

Example answer:
{"entities": [{"text": "aortic regurgitation", "type": "Disease"}, {"text": "mitral regurgitation", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: The incidence of venous discomfort was lower in Group L ( 76.6 % ; P < 0.05 ) than in Group C ( 100 % ) but not different from Group T ( 90 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: The number of affected valves ( n=2.4+/-0.7 ) and the sum of regurgitation grades ( n=2.8+/-1.09 ) were higher ( p=0.008 and p=0.006 , respectively ) in the pergolide group .

Example answer:
{"entities": [{"text": "pergolide", "type": "Chemical"}]}

Input:
Sentence: This difference was also significant in the primary valve surgery and the high risk surgery subgroups ( 7.9 % vs 1.2 % , P = 0.003 ; 7.3 % vs 2.4 % , P = 0.035 , respectively ) .

## Item bc5cdr:test:3221
Example input:
Sentence: RESULTS : Initial MRIs showed abnormal high signal intensities on DWI and FLAIR ( or T2-weighted image ) at the dentate nucleus ( 8/8 ) , inferior colliculus ( 6/8 ) , corpus callosum ( 2/8 ) , pons ( 2/8 ) , medulla ( 1/8 ) , and bilateral cerebral white matter ( 1/8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Renal biopsy revealed severe glomerulonephritis with crescents , electron dense fibrillar deposits and moderate lymphocytic interstitial infiltrate .

Example answer:
{"entities": [{"text": "glomerulonephritis", "type": "Disease"}]}

Example input:
Sentence: In the remaining 12 patients , localised computed tomography of the gall bladder showed that eight had stones with maximum attenuation scores of < 100 Hounsfield units ( values of < 100 HU predict cholesterol rich , dissolvable stones ) .

Example answer:
{"entities": [{"text": "cholesterol", "type": "Chemical"}]}

Example input:
Sentence: Heparan sulphate-associated anionic sites in the glomerular basement membrane were studied in rats 8 months after induction of diabetes by streptozotocin and in age- adn sex-matched control rats , employing the cationic dye cuprolinic blue .

Example answer:
{"entities": [{"text": "Heparan", "type": "Chemical"}, {"text": "diabetes", "type": "Disease"}, {"text": "streptozotocin", "type": "Chemical"}, {"text": "cuprolinic blue", "type": "Chemical"}]}

Example input:
Sentence: In contrast , 7H6 and ZO-1 immunostaining was more discontinuous , outlining the bile canaliculi after BDL .

Example answer:
{"entities": []}

Example input:
Sentence: FANFT-induced cell proliferation in the bladder was significantly suppressed by aspirin co-administration after 4 weeks but not after 12 weeks .

Example answer:
{"entities": [{"text": "FANFT-induced", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: The cell populations were examined regarding total cell recovery correlated with gland weight , intracellular prolactin ( PRL ) content and subsequent release in primary culture , immunocytochemical PRL staining , density and/or size alterations via separation on Ficoll-Hypaque and by unit gravity sedimentation , and cell cycle analysis , after acriflavine DNA staining , by laser flow cytometry .

Example answer:
{"entities": [{"text": "acriflavine", "type": "Chemical"}]}

Example input:
Sentence: The expression of arginine vasopressin ( AVP ) gene in the paraventricular ( PVN ) and supraoptic nuclei ( SON ) was investigated in rats with lithium ( Li ) -induced polyuria , using in situ hybridization histochemistry and radioimmunoassay .

Example answer:
{"entities": [{"text": "arginine vasopressin", "type": "Chemical"}, {"text": "AVP", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "Li", "type": "Chemical"}, {"text": "polyuria", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Immunofluorescence staining with the MRP2 antibody was found to label a high number of microvessels throughout the brain in normal Wistar rats , whereas such labeling was absent in TR ( - ) rats .

Example answer:
{"entities": []}

Example input:
Sentence: OBJECTIVE : This is to present reversible inferior colliculus lesions in metronidazole-induced encephalopathy , to focus on the diffusion-weighted imaging ( DWI ) and fluid attenuated inversion recovery ( FLAIR ) imaging .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "Disease"}, {"text": "metronidazole-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Input:
Sentence: Retrograde dye-tracing techniques with Fastblue were used to identify presumptive bladder afferent cells in the lumbosacral DRG .

## Item bc5cdr:test:2855
Example input:
Sentence: Choreoathetoid movements associated with rapid adjustment to methadone .

Example answer:
{"entities": [{"text": "Choreoathetoid movements", "type": "Disease"}, {"text": "methadone", "type": "Chemical"}]}

Example input:
Sentence: Ketoconazole is not known to be proarrhythmic without concomitant use of QT interval-prolonging drugs .

Example answer:
{"entities": [{"text": "Ketoconazole", "type": "Chemical"}]}

Example input:
Sentence: The results suggest that a prolonged combination of more than 120 min of PGE1-induced hypotension and moderate haemodilution would cause impairment of hepatic function .

Example answer:
{"entities": [{"text": "PGE1-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}, {"text": "impairment of hepatic function", "type": "Disease"}]}

Example input:
Sentence: This is a case report of euphoria and choreoathetoid movements both transiently induced by rapid adjustment to the selective mu-opioid receptor agonist methadone in an inpatient previously abusing heroine and cocaine .

Example answer:
{"entities": [{"text": "choreoathetoid movements", "type": "Disease"}, {"text": "methadone", "type": "Chemical"}, {"text": "heroine", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Ketoconazole induced torsades de pointes without concomitant use of QT interval-prolonging drug .

Example answer:
{"entities": [{"text": "Ketoconazole", "type": "Chemical"}, {"text": "torsades de pointes", "type": "Disease"}]}

Example input:
Sentence: Ximelagatran , an oral direct thrombin inhibitor , was found to be as efficient as vitamin K antagonist drugs in the prevention of embolic events , but has been recently withdrawn because of abnormal liver function tests .

Example answer:
{"entities": [{"text": "Ximelagatran", "type": "Chemical"}, {"text": "vitamin K", "type": "Chemical"}, {"text": "embolic events", "type": "Disease"}, {"text": "abnormal liver function", "type": "Disease"}]}

Example input:
Sentence: These data indicate that the free ED50 in plasma for terfenadine ( 1.9 nM ) , terodiline ( 76 nM ) , cisapride ( 11 nM ) and E4031 ( 1.9 nM ) closely correlate with the free concentration in man causing QT effects .

Example answer:
{"entities": [{"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}, {"text": "E4031", "type": "Chemical"}]}

Example input:
Sentence: We report a woman with coronary artery disease who developed a markedly prolonged QT interval and torsades de pointes ( TdP ) after taking ketoconazole for treatment of fungal infection .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "prolonged QT interval", "type": "Disease"}, {"text": "torsades de pointes", "type": "Disease"}, {"text": "TdP", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "fungal infection", "type": "Disease"}]}

Example input:
Sentence: We postulate that by virtue of its direct blocking action on IKr , ketoconazole alone may prolong QT interval and induce TdP .

Example answer:
{"entities": [{"text": "ketoconazole", "type": "Chemical"}, {"text": "TdP", "type": "Disease"}]}

Example input:
Sentence: Four compounds known to increase QT interval and cause TDP were investigated : terfenadine , terodiline , cisapride and E4031 .

Example answer:
{"entities": [{"text": "TDP", "type": "Disease"}, {"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}, {"text": "E4031", "type": "Chemical"}]}

Input:
Sentence: Methadone dose , presence of cytochrome P-450 3A4 inhibitors , potassium level , and liver function contribute to QT prolongation .

## Item bc5cdr:test:3225
Example input:
Sentence: Podocyte injury and focal segmental glomerulosclerosis have been related to mToR inhibition in some patients , but the pathways underlying these lesions remain hypothetic .

Example answer:
{"entities": [{"text": "glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: In vitro characterization of parasympathetic and sympathetic responses in cyclophosphamide-induced cystitis in the rat .

Example answer:
{"entities": [{"text": "cyclophosphamide-induced", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Example input:
Sentence: Renal papillary necrosis ( RPN ) and a decreased urinary concentrating ability developed during continuous long-term treatment with aspirin and paracetamol in female Fischer 344 rats .

Example answer:
{"entities": [{"text": "Renal papillary necrosis", "type": "Disease"}, {"text": "RPN", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: FANFT-induced cell proliferation in the bladder was significantly suppressed by aspirin co-administration after 4 weeks but not after 12 weeks .

Example answer:
{"entities": [{"text": "FANFT-induced", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: Responses of urinary strip preparations from control and cyclophosphamide-pretreated rats to electrical field stimulation and to agonists were assessed in the absence and presence of muscarinic , adrenergic and purinergic receptor antagonists .

Example answer:
{"entities": [{"text": "cyclophosphamide-pretreated", "type": "Chemical"}]}

Example input:
Sentence: Using puromycin aminonucleoside nephrosis ( PAN ) rats , we studied early ultrastructural and permeability changes in relation to the expression of the podocyte-associated molecules nephrin , a-actinin , dendrin , and plekhh2 , the last two of which were only recently discovered in podocytes .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: Dup 753 prevents the development of puromycin aminonucleoside-induced nephrosis .

Example answer:
{"entities": [{"text": "Dup 753", "type": "Chemical"}, {"text": "puromycin", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: Thus , in cystitis substantial changes of the efferent functional responses occur .

Example answer:
{"entities": [{"text": "cystitis", "type": "Disease"}]}

Example input:
Sentence: Animal studies suggest that incontinence secondary to serotonergic antidepressants could be mediated by the 5HT4 receptors found on the bladder .

Example answer:
{"entities": [{"text": "incontinence", "type": "Disease"}, {"text": "serotonergic antidepressants", "type": "Chemical"}]}

Example input:
Sentence: In cyclophosphamide-induced cystitis in the rat , detrusor function is impaired and the expression and effects of muscarinic receptors altered .

Example answer:
{"entities": [{"text": "cyclophosphamide-induced", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Input:
Sentence: These studies demonstrate that p75 ( NTR ) expression in micturition reflexes is present constitutively and modified by bladder inflammation .

## Item bc5cdr:test:3228
Example input:
Sentence: In a 6-week double-blind parallel treatment study , dothiepin and amitriptyline were compared to placebo in the treatment of 33 depressed outpatients .

Example answer:
{"entities": [{"text": "dothiepin", "type": "Chemical"}, {"text": "amitriptyline", "type": "Chemical"}, {"text": "depressed", "type": "Disease"}]}

Example input:
Sentence: Tacrolimus , MMF , and steroids were given as immunosuppressant .

Example answer:
{"entities": [{"text": "Tacrolimus", "type": "Chemical"}, {"text": "MMF", "type": "Chemical"}, {"text": "steroids", "type": "Chemical"}]}

Example input:
Sentence: -Tacrolimus ( FK 506 ) is a powerful , widely used immunosuppressant .

Example answer:
{"entities": [{"text": "FK 506", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Sirolimus is the latest immunosuppressive agent used to prevent rejection , and may have less nephrotoxicity than calcineurin inhibitor ( CNI ) -based regimens .

Example answer:
{"entities": [{"text": "Sirolimus", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}]}

Example input:
Sentence: Liver biopsies should be undertaken at regular intervals if azathioprine therapy is continued so that structural liver damage may be detected at an early and reversible stage .

Example answer:
{"entities": [{"text": "azathioprine", "type": "Chemical"}, {"text": "liver damage", "type": "Disease"}]}

Example input:
Sentence: The drugs commonly used are cyclophosphamide and chlorambucil ( alkylating agents ) , azathioprine ( purine analogue ) , and methotrexate ( folic acid analogue ) .

Example answer:
{"entities": [{"text": "cyclophosphamide", "type": "Chemical"}, {"text": "chlorambucil", "type": "Chemical"}, {"text": "alkylating agents", "type": "Chemical"}, {"text": "azathioprine", "type": "Chemical"}, {"text": "purine", "type": "Chemical"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "folic acid", "type": "Chemical"}]}

Example input:
Sentence: Treatment of psoriasis with azathioprine .

Example answer:
{"entities": [{"text": "psoriasis", "type": "Disease"}, {"text": "azathioprine", "type": "Chemical"}]}

Example input:
Sentence: There have been several long-term studies of patients with rheumatoid arthritis treated with azathioprine and cyclophosphamide and the incidence of most of the common cancers is not increased .

Example answer:
{"entities": [{"text": "rheumatoid arthritis", "type": "Disease"}, {"text": "azathioprine", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "cancers", "type": "Disease"}]}

Example input:
Sentence: Immunosuppressive drugs have been used during the last 30 years in treatment of patients with severe rheumatoid arthritis .

Example answer:
{"entities": [{"text": "rheumatoid arthritis", "type": "Disease"}]}

Example input:
Sentence: Azathioprine treatment benefited 19 ( 66 % ) out of 29 patients suffering from severe psoriasis .

Example answer:
{"entities": [{"text": "Azathioprine", "type": "Chemical"}, {"text": "psoriasis", "type": "Disease"}]}

Input:
Sentence: BACKGROUND : Azathioprine is widely used as an immunosuppressive drug .

## Item bc5cdr:test:2802
Example input:
Sentence: CY caused hemorrhagic cystitis in 40 % of rats , but it did not cause this complication when combined with 5-FU and MTX .

Example answer:
{"entities": [{"text": "CY", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "MTX", "type": "Chemical"}]}

Example input:
Sentence: The pathogenesis of 5-fluorouracil neurotoxicity may be due to a Krebs cycle blockade by fluoroacetate and fluorocitrate , thiamine deficiency , or dihydrouracil dehydrogenase deficiency .

Example answer:
{"entities": [{"text": "5-fluorouracil", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "fluoroacetate", "type": "Chemical"}, {"text": "fluorocitrate", "type": "Chemical"}, {"text": "thiamine", "type": "Chemical"}, {"text": "dihydrouracil", "type": "Chemical"}]}

Example input:
Sentence: He developed acute neurologic symptoms of mental confusion , disorientation and irritability , and then lapsed into a deep coma , lasting for approximately 40 hours during the first dose ( day 2 ) of 5-fluorouracil and folinic acid infusion .

Example answer:
{"entities": [{"text": "confusion", "type": "Disease"}, {"text": "disorientation", "type": "Disease"}, {"text": "irritability", "type": "Disease"}, {"text": "coma", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: Adverse cardiac effects during induction chemotherapy treatment with cis-platin and 5-fluorouracil .

Example answer:
{"entities": [{"text": "cis-platin", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}]}

Example input:
Sentence: We describe a 25-year-old woman with pre-existing mitral valve prolapse who developed intractable ventricular fibrillation after consuming a `` natural energy '' guarana health drink containing a high concentration of caffeine .

Example answer:
{"entities": [{"text": "mitral valve prolapse", "type": "Disease"}, {"text": "ventricular fibrillation", "type": "Disease"}, {"text": "caffeine", "type": "Chemical"}]}

Example input:
Sentence: This complication reappeared on day 25 during the second dose of 5-fluorouracil and folinic acid , which were then the only drugs given .

Example answer:
{"entities": [{"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: Acute confusion induced by a high-dose infusion of 5-fluorouracil and folinic acid .

Example answer:
{"entities": [{"text": "confusion", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: An allergic reaction consisting of angioneurotic edema secondary to continuous infusion 5-fluorouracil occurred in a patient with recurrent carcinoma of the oral cavity , cirrhosis , and cisplatin-induced impaired renal function .

Example answer:
{"entities": [{"text": "allergic reaction", "type": "Disease"}, {"text": "angioneurotic edema", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "carcinoma of the oral cavity", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "impaired renal function", "type": "Disease"}]}

Example input:
Sentence: Because folinic acid was unlikely to be associated with this condition , neurotoxicity due to high-dose 5-fluorouracil was highly suspected .

Example answer:
{"entities": [{"text": "folinic acid", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}]}

Example input:
Sentence: It is concluded that patients on 5-FU treatment should be under close supervision and that the treatment should be discontinued if chest pain or tachyarrhythmia is observed .

Example answer:
{"entities": [{"text": "5-FU", "type": "Chemical"}, {"text": "chest pain", "type": "Disease"}, {"text": "tachyarrhythmia", "type": "Disease"}]}

Input:
Sentence: The experience of this case , together with a review of the literature , suggests that FBAL is related to 5-FU-induced cardiotoxicity .

## Item bc5cdr:test:3022
Example input:
Sentence: An initial dose of 0.1 microgram.kg-1.min-1 of PGE1 ( 15 patients ) , or 10 micrograms.kg-1.min-1 of TMP ( 15 patients ) was administered intravenously after the dural opening and the dose was adjusted to maintain the mean arterial blood pressure ( MAP ) at about 60 mmHg .

Example answer:
{"entities": [{"text": "PGE1", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: During the infusion of aminophylline , the ventricular fibrillation threshold was reduced by 30 to 40 percent of the control when pH and partial pressures of oxygen ( PO2 ) and carbon dioxide ( CO2 ) were kept within normal limits .

Example answer:
{"entities": [{"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}, {"text": "oxygen", "type": "Chemical"}, {"text": "PO2", "type": "Chemical"}, {"text": "carbon dioxide", "type": "Chemical"}, {"text": "CO2", "type": "Chemical"}]}

Example input:
Sentence: Ten patients with acute transmural myocardial infarctions received intravenous nitroglycerin , sufficient to reduce mean arterial pressure from 107 +/- 6 to 85 +/- 6 mm Hg ( P less than 0.001 ) , for 60 minutes .

Example answer:
{"entities": [{"text": "myocardial infarctions", "type": "Disease"}, {"text": "nitroglycerin", "type": "Chemical"}]}

Example input:
Sentence: After 3 days of combined treatment , a marked elevation in plasma and tissue lithium levels accompanied a reduction in water intake .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: Symptoms persisted for three months despite TAC dose reduction , administration of IVIG and four doses of methylprednisolone pulse therapy .

Example answer:
{"entities": [{"text": "TAC", "type": "Chemical"}, {"text": "methylprednisolone", "type": "Chemical"}]}

Example input:
Sentence: In four patients , polymorphous ventricular tachycardia appeared after intravenous administration of 200 to 400 mg of procainamide for the treatment of sustained ventricular tachycardia .

Example answer:
{"entities": [{"text": "ventricular tachycardia", "type": "Disease"}, {"text": "procainamide", "type": "Chemical"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: In all of them normal serum potassium levels reached within 2 to 4 days of stopping sulindac .

Example answer:
{"entities": [{"text": "potassium", "type": "Chemical"}, {"text": "sulindac", "type": "Chemical"}]}

Input:
Sentence: Three hours later the patient felt better , the frequency of PVC reduced to 4 - 5 x/minute and on the third day ECG was normal , potassium level was 3.34 meq/L .

## Item bc5cdr:test:3086
Example input:
Sentence: Caffeine-induced cardiac arrhythmia : an unrecognised danger of healthfood products .

Example answer:
{"entities": [{"text": "Caffeine-induced", "type": "Chemical"}, {"text": "cardiac arrhythmia", "type": "Disease"}]}

Example input:
Sentence: Forty-nine percent of patients were pain free 2 h after rizatriptan , compared with 24.3 % treated with ergotamine/caffeine ( p < or = 0.001 ) , rizatriptan being superior within 1 h of treatment .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}]}

Example input:
Sentence: Because salicylates have been reported to augment the stimulatory effects of caffeine on the CNS , attention was focused on the possibility that the presence of acetaminophen ( 52 micrograms/mL ) reduced the CNS toxicity of caffeine .

Example answer:
{"entities": [{"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: METHOD : In London and Toronto 154 patients who met DSM-III criteria for panic disorder with agoraphobia were randomised to alprazolam or placebo .

Example answer:
{"entities": [{"text": "panic disorder", "type": "Disease"}, {"text": "agoraphobia", "type": "Disease"}, {"text": "alprazolam", "type": "Chemical"}]}

Example input:
Sentence: A patient who allegedly consumed 100 tablets of an over-the-counter analgesic containing sodium acetylsalicylate , caffeine , and acetaminophen displayed no significant CNS stimulation despite the presence of 175 micrograms of caffeine per mL of serum .

Example answer:
{"entities": [{"text": "sodium acetylsalicylate", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}]}

Example input:
Sentence: We describe a 25-year-old woman with pre-existing mitral valve prolapse who developed intractable ventricular fibrillation after consuming a `` natural energy '' guarana health drink containing a high concentration of caffeine .

Example answer:
{"entities": [{"text": "mitral valve prolapse", "type": "Disease"}, {"text": "ventricular fibrillation", "type": "Disease"}, {"text": "caffeine", "type": "Chemical"}]}

Example input:
Sentence: Rizatriptan was also superior to ergotamine/caffeine in the proportions of patients with no nausea , vomiting , phonophobia or photophobia and for patients with normal function 2 h after drug intake ( p < or = 0.001 ) .

Example answer:
{"entities": [{"text": "Rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}, {"text": "nausea", "type": "Disease"}, {"text": "vomiting", "type": "Disease"}, {"text": "phonophobia", "type": "Disease"}, {"text": "photophobia", "type": "Disease"}]}

Example input:
Sentence: In the absence of caffeine , acetaminophen ( up to 300 mg/kg ) did not modify the seizures induced by maximal electroshock and did not alter the convulsant dose of pentylenetetrezol in mice ( tests performed by the Anticonvulsant Screening Project of NINCDS ) .

Example answer:
{"entities": [{"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "pentylenetetrezol", "type": "Chemical"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: The frequency of sound-induced seizures after 12.5 or 25 mg/kg caffeine was reduced from 50 to 5 % by acetaminophen .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}]}

Input:
Sentence: No panic attack was observed after the caffeine-free solution intake .

## Item bc5cdr:test:3256
Example input:
Sentence: The ocular hypotensive effects were statistically significant for apraclonidine-treated eyes throughout the study and also statistically significant for contralateral eyes from three hours after topical administration of 1 % apraclonidine .

Example answer:
{"entities": [{"text": "ocular hypotensive", "type": "Disease"}, {"text": "apraclonidine-treated", "type": "Chemical"}, {"text": "apraclonidine", "type": "Chemical"}]}

Example input:
Sentence: A lesser degree of orthostatic hypotension occurred with standing .

Example answer:
{"entities": [{"text": "orthostatic hypotension", "type": "Disease"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: Controlled hypotension to an average MAP of 50-55 mm Hg was induced by increasing the dose of isoflurane , and maintained at an inspired concentration of 2.2 +/- 0.2 % .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "Hg", "type": "Chemical"}, {"text": "isoflurane", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Overall , 21 out of 104 patients ( 20.2 % ) presented with high frequency sensorineural hearing loss ( SNHL ) , either unilateral or bilateral .

Example answer:
{"entities": [{"text": "sensorineural hearing loss", "type": "Disease"}, {"text": "SNHL", "type": "Disease"}]}

Example input:
Sentence: Controlled hypotension in groups A and C was induced with PGE1 to maintain mean arterial blood pressure at 55 mmHg for 180 min .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "PGE1", "type": "Chemical"}]}

Example input:
Sentence: The SPV during hypotension was 15.7 +/- 6.7 mm Hg in the HEM group , compared with 9.1 +/- 2.0 mm Hg in the SNP group ( P less than 0.02 ) .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "HEM", "type": "Disease"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: Patients who received enalapril experienced clinically and statistically significantly less symptomatic hypotension ( 5.2 % ) than the patients who received prazosin ( 12.9 % ) .

Example answer:
{"entities": [{"text": "enalapril", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "prazosin", "type": "Chemical"}]}

Example input:
Sentence: Transient hypotension ( SAP < 90mmHg ) occurred in 1 patient ( 0.7 % ) .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: The patients were randomly allocated to one of three groups ; those in group A ( n = 10 ) were subjected to controlled hypotension alone , those in group B ( n = 10 ) to haemodilution alone and those in group C ( n = 10 ) to both controlled hypotension and haemodilution .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}]}

Input:
Sentence: RESULTS : Three patients ( 8.1 % ) in the unilateral group and 5 ( 13.5 % ) in the conventional group developed hypotension , P= 0.71 .

## Item bc5cdr:test:3360
Example input:
Sentence: This paper presents the results of treating IST by intratympanic instillation of lignocaine ( lidocaine ) 2 per cent through a grommet , for five weekly courses .

Example answer:
{"entities": [{"text": "IST", "type": "Disease"}, {"text": "lignocaine", "type": "Chemical"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: Laryngeal electromyography ( thyroarytenoid muscle ) showed ample denervation potentials .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : Ninety patients classified as American Society of Anesthesiologists physical status I or II who were scheduled for short gynecologic procedures under spinal anesthesia were randomly allocated to receive 2.5 ml 2 % lidocaine in 7.5 % glucose , 2 % prilocaine in 7.5 % glucose , or 0.5 % bupivacaine in 7.5 % glucose .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "glucose", "type": "Chemical"}, {"text": "prilocaine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: It is longer acting than physostigmine and is used in anaesthesia to reverse the non-depolarizing neuromuscular block .

Example answer:
{"entities": [{"text": "physostigmine", "type": "Chemical"}]}

Example input:
Sentence: METHODS : A double-blind double-armed prospective study comprised 40 patients who had uneventful sutureless phacoemulsification under sub-Tenon 's local infiltration of 3 mL of plain lignocaine .

Example answer:
{"entities": [{"text": "lignocaine", "type": "Chemical"}]}

Example input:
Sentence: Accordingly , the present , prospective double-blind study compares prilocaine with lidocaine and bupivacaine with respect to duration of action and relative risk of TNSs .

Example answer:
{"entities": [{"text": "prilocaine", "type": "Chemical"}, {"text": "lidocaine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}, {"text": "TNSs", "type": "Disease"}]}

Example input:
Sentence: Treatment of tinnitus by intratympanic instillation of lignocaine ( lidocaine ) 2 per cent through ventilation tubes .

Example answer:
{"entities": [{"text": "tinnitus", "type": "Disease"}, {"text": "lignocaine", "type": "Chemical"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: These results show that ipratropium is a more potent bronchodilator than oral theophylline in patients with chronic airflow obstruction .

Example answer:
{"entities": [{"text": "ipratropium", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}, {"text": "chronic airflow obstruction", "type": "Disease"}]}

Example input:
Sentence: These results suggest that PGE1 may be preferable to TMP for hypotensive anaesthesia in spinal surgery because TMP decreased EBF .

Example answer:
{"entities": [{"text": "PGE1", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}, {"text": "hypotensive", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Prilocaine may be preferable to lidocaine for short surgical procedures because it has a similar duration of action but a lower incidence of TNSs .

Example answer:
{"entities": [{"text": "Prilocaine", "type": "Chemical"}, {"text": "lidocaine", "type": "Chemical"}, {"text": "TNSs", "type": "Disease"}]}

Input:
Sentence: Comparison of laryngeal mask with endotracheal tube for anesthesia in endoscopic sinus surgery .

## Item bc5cdr:test:2902
Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: 9 ( 2006 ) , 917 ] recently identified the microglial-specific fractalkine receptor ( CX3CR1 ) as an important mediator of MPTP-induced neurodegeneration of DA neurons .

Example answer:
{"entities": [{"text": "MPTP-induced", "type": "Chemical"}, {"text": "neurodegeneration", "type": "Disease"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: Histological and immunohistochemical investigations ( HE-LFB , CD-68 , Neurofilament ) revealed degeneration of myelin and axons as well as pseudocystic transformation in areas exposed to vincristine , accompanied by secondary changes with numerous prominent macrophages .

Example answer:
{"entities": [{"text": "pseudocystic transformation", "type": "Disease"}, {"text": "vincristine", "type": "Chemical"}]}

Example input:
Sentence: The results suggest a possible involvement of the renin-angiotensin system in the development of puromycin aminonucleoside-induced nephrosis .

Example answer:
{"entities": [{"text": "puromycin", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVE : To describe a case of propylthiouracil-induced vasculitis manifesting with pericarditis .

Example answer:
{"entities": [{"text": "propylthiouracil-induced", "type": "Chemical"}, {"text": "vasculitis", "type": "Disease"}, {"text": "pericarditis", "type": "Disease"}]}

Example input:
Sentence: Puromycin aminonucleoside nephrosis was induced by single intraperitoneal injection of puromycin aminonucleoside ( PAN , 20 mg/100g BW ) .

Example answer:
{"entities": [{"text": "Puromycin aminonucleoside", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: Propylthiouracil-induced perinuclear-staining antineutrophil cytoplasmic autoantibody-positive vasculitis in conjunction with pericarditis .

Example answer:
{"entities": [{"text": "Propylthiouracil-induced", "type": "Chemical"}, {"text": "vasculitis", "type": "Disease"}, {"text": "pericarditis", "type": "Disease"}]}

Example input:
Sentence: We conclude that methylphenidate mediated vasculitis should be considered in patients with neurological symptoms and a history of methylphenidate therapy .

Example answer:
{"entities": [{"text": "methylphenidate", "type": "Chemical"}, {"text": "vasculitis", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : Pericarditis may be the initial manifestation of drug-induced vasculitis attributable to propylthio- uracil therapy .

Example answer:
{"entities": [{"text": "Pericarditis", "type": "Disease"}, {"text": "vasculitis", "type": "Disease"}, {"text": "propylthio- uracil", "type": "Chemical"}]}

Example input:
Sentence: A literature review revealed no prior reports of pericarditis in anti-MPO pANCA-positive vasculitis associated with propylthio- uracil therapy .

Example answer:
{"entities": [{"text": "pericarditis", "type": "Disease"}, {"text": "vasculitis", "type": "Disease"}, {"text": "propylthio- uracil", "type": "Chemical"}]}

Input:
Sentence: Minocycline-induced vasculitis fulfilling the criteria of polyarteritis nodosa .

## Item bc5cdr:test:3175
Example input:
Sentence: Extrapyramidal symptoms reported as AEs occurred in 15 % and 18 % , 34 % , and 10 % of the asenapine at 5 and 10 mg BID , haloperidol , and placebo groups , respectively .

Example answer:
{"entities": [{"text": "Extrapyramidal symptoms", "type": "Disease"}, {"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Most patients ( 57 % ) stopped treatment because of disease progression .

Example answer:
{"entities": []}

Example input:
Sentence: Since the incidence and severity of specific adverse effects differ among the various atypicals , the clinician should carefully consider which side effects are most likely to lead to the individual 's dissatisfaction and noncompliance before choosing an antipsychotic for a particular patient .

Example answer:
{"entities": []}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: A high proportion of patients had consumed ATT empirically , which could have been prevented .

Example answer:
{"entities": []}

Example input:
Sentence: From January 1986 to January 2009 , 1223 consecutive ALF patients were evaluated : ATT alone was the cause in 70 ( 5.7 % ) patients .

Example answer:
{"entities": [{"text": "ALF", "type": "Disease"}]}

Example input:
Sentence: With either discontinuation or decreased dosage of the drug the symptoms disappeared and did not recur .

Example answer:
{"entities": []}

Example input:
Sentence: Atorvastatin ( Ato ) possesses pleiotropic properties that have been reported to improve endothelial function through increased availability of NO and reduced O2- production in various forms of hypertension .

Example answer:
{"entities": [{"text": "Atorvastatin", "type": "Chemical"}, {"text": "Ato", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}, {"text": "O2-", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: Her symptoms totally regressed after drug withdrawal and reappeared when acitretin was reintroduced .

Example answer:
{"entities": [{"text": "acitretin", "type": "Chemical"}]}

Example input:
Sentence: What is less well known is a phenomenon whereby statins may induce a myopathy , which persists or may progress after stopping the drug .

Example answer:
{"entities": [{"text": "statins", "type": "Chemical"}, {"text": "myopathy", "type": "Disease"}]}

Input:
Sentence: Overall , as an entity , ATIN remains under-diagnosed , as symptoms resolve spontaneously if the medication is stopped .

## Item bc5cdr:test:2976
Example input:
Sentence: Importantly , both classical ( haloperidol ) and atypical ( olanzapine , clozapine and aripiprazole ) antipsychotics were effective in all these models of hyperactivity .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "olanzapine", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "aripiprazole", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}]}

Example input:
Sentence: Based on these observations , it is concluded that 5-HT2 blockade obtained with risperidone at D2 occupancy rates of 60 % and above does not appear to protect against the risk for extrapyramidal side effects .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}]}

Example input:
Sentence: Risperidone is an antipsychotic drug with high affinity at dopamine D2 and serotonin 5-HT2 receptors .

Example answer:
{"entities": [{"text": "Risperidone", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "serotonin 5-HT2", "type": "Chemical"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: This change resulted within 2-4 weeks in the 50-200 % increase in the plasma levels of these neuroleptics and the appearance of extrapyramidal symptoms .

Example answer:
{"entities": [{"text": "extrapyramidal symptoms", "type": "Disease"}]}

Example input:
Sentence: To determine if routine risperidone treatment is associated with a unique degree of D2 receptor occupancy and pattern of clinical effects , we used [ 123I ] IBZM SPECT to determine D2 occupancy in subjects treated with routine clinical doses of risperidone ( n = 12 ) or haloperidol ( n = 7 ) .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Drug-induced parkinsonism was observed in subjects treated with risperidone ( 42 % ) and haloperidol ( 29 % ) and was observed at occupancy levels above 60 % .

Example answer:
{"entities": [{"text": "Drug-induced parkinsonism", "type": "Disease"}, {"text": "risperidone", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: There was no significant difference between occupancy levels obtained with haloperidol or risperidone .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "risperidone", "type": "Chemical"}]}

Example input:
Sentence: Both risperidone and haloperidol produced D2 occupancy levels between approximately 60 and 90 % at standard clinical doses .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Previous clinical studies have proposed that risperidone 's pharmacologic profile may produce improved efficacy for negative psychotic symptoms and decreased propensity for extrapyramidal side effects ; features shared by so-called 'atypical ' neuroleptics .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}, {"text": "psychotic symptoms", "type": "Disease"}]}

Input:
Sentence: Significantly more weight gain occurred with olanzapine than with risperidone : the increase in weight at 4 months relative to baseline weight was 17.3 % ( 95 % CI=14.2 % -20.5 % ) with olanzapine and 11.3 % ( 95 % CI=8.4 % -14.3 % ) with risperidone .

## Item bc5cdr:test:3386
Example input:
Sentence: METHODS : This was a multicenter , randomized , open-label study in adult smokers with heart disease , hypertension not controlled by medication , and/or diabetes mellitus .

Example answer:
{"entities": [{"text": "heart disease", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "diabetes mellitus", "type": "Disease"}]}

Example input:
Sentence: Aim of the study was to determine sensitivity , reproducibility , reference values and the agreement with a questionnaire .

Example answer:
{"entities": []}

Example input:
Sentence: The duration of apnea was compared with published data on normal subjects .

Example answer:
{"entities": [{"text": "apnea", "type": "Disease"}]}

Example input:
Sentence: Published cases from the literature are reviewed and pertinent features discussed .

Example answer:
{"entities": []}

Example input:
Sentence: 1981 ) .

Example answer:
{"entities": []}

Example input:
Sentence: A review of all reported cases in the literature is given .

Example answer:
{"entities": []}

Example input:
Sentence: Clinical characteristics , medications , and serum chemistries at baseline and follow-up time periods were compared .

Example answer:
{"entities": []}

Example input:
Sentence: Our prospectively collected database was the source of information .

Example answer:
{"entities": []}

Example input:
Sentence: Some case reports are published in the literature but no systematic study from a sample of patients has been published .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSION : This case started with a media report in a popular newspaper , initiated by published , peer-reviewed research on herbals , and involved human failure in a case history , medical examination and clinical treatment .

Example answer:
{"entities": []}

Input:
Sentence: DATA SOURCES : MEDLINE and Cochrane Library ( search dates , 1 January 2001 to 28 August 2008 ) , recent systematic reviews , reference lists of retrieved articles , and suggestions from experts .

## Item bc5cdr:test:3108
Example input:
Sentence: At termination of the experiments , mice underwent echocardiography , quantitation of abundance of molecular markers of CM ( ventricular mRNA encoding atrial natriuretic factor [ ANF ] and sarcoplasmic calcium ATPase [ SERCA2 ] ) , and determination of plasma LA .

Example answer:
{"entities": [{"text": "CM", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "LA", "type": "Chemical"}]}

Example input:
Sentence: The most common toxicities encountered were transient serum transaminase and bilirubin elevations , neutropenia , and mucositis .

Example answer:
{"entities": [{"text": "toxicities", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}, {"text": "neutropenia", "type": "Disease"}, {"text": "mucositis", "type": "Disease"}]}

Example input:
Sentence: Hemolysis caused by TAM was not preceded by the leakage of K ( + ) from the cells , also excluding a colloid-osmotic type mechanism of hemolysis , according to the effects on osmotic fragility curves .

Example answer:
{"entities": [{"text": "Hemolysis", "type": "Disease"}, {"text": "TAM", "type": "Chemical"}, {"text": "K", "type": "Chemical"}, {"text": "hemolysis", "type": "Disease"}]}

Example input:
Sentence: Cases were patients who developed hyperkalemia ( K ( + ) > 5.0 mEq/L ) or renal insufficiency ( Cr > or=2.5 mg/dL ) , and they were compared to 2 randomly selected controls per case .

Example answer:
{"entities": [{"text": "hyperkalemia", "type": "Disease"}, {"text": "K", "type": "Chemical"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "Cr", "type": "Chemical"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: Renal function was investigated by measuring plasma and urinary electrolytes , glucosuria , proteinuria , aminoaciduria , urinary pH , osmolarity , creatinine clearance , phosphate tubular reabsorption , beta 2 microglobulinuria , and lysozymuria .

Example answer:
{"entities": [{"text": "glucosuria", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "aminoaciduria", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "phosphate", "type": "Chemical"}]}

Example input:
Sentence: Admission laboratory tests were as follows : alanine aminotransferase , 67 U/L ( reference range , 10-37 U/L ) ; aspartate aminotransferase , 98 U/L ( 10-40 U/L ) ; alkaline phosphatase , 513 U/L ( 0-270 U/L ) ; gamma-glutamyltransferase , 32 U/L ( 7-49 U/L ) ; amylase , 46 U/L ( 0-220 U/L ) ; total bilirubin , 20.1 mg/dL ( 0.2-1.0 mg/dL ) ; direct bilirubin , 14.8 mg/dL ( 0-0.3 mg/dL ) ; and albumin , 4.7 mg/dL ( 3.5-5.4 mg/dL ) .

Example answer:
{"entities": [{"text": "alanine", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: Acute normal tissue toxicities ( i.e. , leukopenia and thrombocytopenia ) and late normal tissue toxicities ( i.e. , myocardial and kidney injury ) were evaluated by functional/physiological assays and by morphological techniques .

Example answer:
{"entities": [{"text": "toxicities", "type": "Disease"}, {"text": "leukopenia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}]}

Example input:
Sentence: Severe hematologic toxicity ( neutrophil count < 1000/mm3 and/or hemoglobin < 8 g/dl ) occurred in 4 patients assigned to group I and 7 assigned to group II .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Laboratory evaluation revealed 66,680 U/L creatine kinase , 93 mg/dL blood urea nitrogen , 4.6 mg/dL creatinine , 1579 U/L aspartate aminotransferase , and 738 U/L alanine aminotransferase .

Example answer:
{"entities": [{"text": "creatine", "type": "Chemical"}, {"text": "blood urea nitrogen", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "alanine", "type": "Chemical"}]}

Input:
Sentence: The laboratory data revealed normal plasma electrolyte and ammonia levels but leukocytosis .

## Item bc5cdr:test:3118
Example input:
Sentence: CONCLUSIONS : Topical papaverine for the treatment of vasospasm was associated with the onset of a transient disturbance in neurophysiological function of the ascending auditory brainstem pathway .

Example answer:
{"entities": [{"text": "papaverine", "type": "Chemical"}, {"text": "vasospasm", "type": "Disease"}]}

Example input:
Sentence: None of the animals that received bupivacaine , normal saline , or normal saline titrated to a pH 3.0 developed hind-limb paralysis .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}, {"text": "paralysis", "type": "Disease"}]}

Example input:
Sentence: We report an undiagnosed case of myotonia congenita in a 24-year-old previously healthy primigravida , who developed life threatening masseter spasm following a standard dose of intravenous suxamethonium for induction of anaesthesia .

Example answer:
{"entities": [{"text": "myotonia congenita", "type": "Disease"}, {"text": "masseter spasm", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: Transient cranial nerve dysfunction has been described in a few cases with topical papaverine .

Example answer:
{"entities": [{"text": "cranial nerve dysfunction", "type": "Disease"}, {"text": "papaverine", "type": "Chemical"}]}

Example input:
Sentence: Transient neurologic symptoms after spinal anesthesia : a lower incidence with prilocaine and bupivacaine than with lidocaine .

Example answer:
{"entities": [{"text": "Transient neurologic symptoms", "type": "Disease"}, {"text": "prilocaine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Recent evidence suggests that transient neurologic symptoms ( TNSs ) frequently follow lidocaine spinal anesthesia but are infrequent with bupivacaine .

Example answer:
{"entities": [{"text": "transient neurologic symptoms", "type": "Disease"}, {"text": "TNSs", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: Acute vocal fold palsy after acute disulfiram intoxication .

Example answer:
{"entities": [{"text": "vocal fold palsy", "type": "Disease"}, {"text": "disulfiram", "type": "Chemical"}]}

Example input:
Sentence: This was a case of acute palsy of the recurrent laryngeal nerve and superimposed severe acute sensorimotor axonal polyneuropathy caused by high-dose disulfiram intoxication .

Example answer:
{"entities": [{"text": "palsy", "type": "Disease"}, {"text": "polyneuropathy", "type": "Disease"}, {"text": "disulfiram", "type": "Chemical"}]}

Example input:
Sentence: Acute peripheral neuropathy caused by a disulfiram overdose is very rare and there is no report of it leading to vocal fold palsy .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "disulfiram", "type": "Chemical"}, {"text": "overdose", "type": "Disease"}, {"text": "vocal fold palsy", "type": "Disease"}]}

Input:
Sentence: Temporary ipsilateral vocal nerve palsies due to local anesthetics have been described , however .

## Item bc5cdr:test:2875
Example input:
Sentence: This study aimed at investigating the potential antipsychotic-like properties of SSR103800 , with a particular focus on models of hyperactivity , involving either drug challenge ( ie , amphetamine and MK-801 ) or transgenic mice ( ie , NMDA Nr1 ( neo-/- ) and DAT ( -/- ) ) .

Example answer:
{"entities": [{"text": "SSR103800", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "MK-801", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}]}

Example input:
Sentence: However , the observation that antagonists of the glutamate N-methyl-D-aspartate ( NMDA ) receptor produce schizophrenic-like symptoms in humans has led to the idea of a dysfunctioning of the glutamatergic system via its NMDA receptor .

Example answer:
{"entities": [{"text": "glutamate", "type": "Chemical"}, {"text": "N-methyl-D-aspartate", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "schizophrenic-like", "type": "Disease"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : A 50 % reduction in the incidence of akathisia when prochlorperazine was administered by means of 15-minute intravenous infusion versus a 2-minute intravenous push was not detected .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}, {"text": "prochlorperazine", "type": "Chemical"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: These results indicate that noradrenergic neurons have an important role in the manifestation of catalepsy induced by THC , whereas dopaminergic neurons are important in catalepsy induced by haloperidol .

Example answer:
{"entities": [{"text": "catalepsy", "type": "Disease"}, {"text": "THC", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "Disease"}, {"text": "METH", "type": "Chemical"}, {"text": "MPTP", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "METH-induced", "type": "Chemical"}]}

Example input:
Sentence: Experimental and clinical evidence points to a role of central histaminergic system in the pathogenesis of schizophrenia .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "Disease"}]}

Example input:
Sentence: THP exhibited an antipsychotic-like profile by potentiating haloperidol-induced catalepsy , reducing amphetamine-induced hyperactivity and reducing apomorphine-induced climbing in mice .

Example answer:
{"entities": []}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Input:
Sentence: In this study , we evaluate the role DRD2 plays in chlorpromazine-induced EPS in schizophrenic patients .

## Item bc5cdr:test:3166
Example input:
Sentence: Thus , clinicians should address patients ' concerns about adverse effects and attempt to choose medications that will improve their patients ' quality of life as well as overall health .

Example answer:
{"entities": []}

Example input:
Sentence: Clinical tolerability of both agents has been good , with fewer than 3 % of patients withdrawn from treatment because of clinical adverse experiences .

Example answer:
{"entities": []}

Example input:
Sentence: IMPORTANCE OF THE FIELD : Fluoropyrimidines , in particular 5-fluorouracil ( 5-FU ) , have been the mainstay of treatment for several solid tumors , including colorectal , breast and head and neck cancers , for > 40 years .

Example answer:
{"entities": [{"text": "Fluoropyrimidines", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "tumors", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Progressive abstinence from cocaine was associated with worsening of all measured polysomnographic sleep outcomes .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Based on this principle a 27-year old woman , classified as being in the high-risk group ( Goldstein and Berkowitz score : 11 ) , was treated with multiple cytotoxic drugs .

Example answer:
{"entities": []}

Example input:
Sentence: GSPE+drug exposed tissues exhibited minor residual damage or near total recovery .

Example answer:
{"entities": [{"text": "GSPE+drug", "type": "Chemical"}]}

Example input:
Sentence: Capecitabine has a well-established safety profile and can be given safely to patients with advanced age , hepatic and renal dysfunctions .

Example answer:
{"entities": [{"text": "Capecitabine", "type": "Chemical"}]}

Example input:
Sentence: Discontinuance of effective chemotherapy in this patient during partial remission resulted in fatal disease progression .

Example answer:
{"entities": []}

Example input:
Sentence: Most patients ( 57 % ) stopped treatment because of disease progression .

Example answer:
{"entities": []}

Example input:
Sentence: OBJECTIVES : Given its preclinical success for treating substance abuse and the increased risk of visual field defects ( VFD ) associated with cumulative lifetime exposure , we explored the effects of sub-chronic low dose GVG on cocaine-induced increases in nucleus accumbens ( NAcc ) dopamine ( DA ) .

Example answer:
{"entities": [{"text": "substance abuse", "type": "Disease"}, {"text": "visual field defects", "type": "Disease"}, {"text": "VFD", "type": "Disease"}, {"text": "GVG", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Input:
Sentence: Comprehensive care may provide the patient the opportunity to discontinue their substance abuse , improve their overall health , and prevent future corneal complications .

## Item bc5cdr:test:2738
Example input:
Sentence: In almost half of these women severe atherosclerosis of the aorta was present ( n=11 ) , while in women without hormone use severe atherosclerosis of the aorta was present in less than 20 % ( OR 3.1 ; 95 % CI , 1.1-8.5 , adjusted for age , years since menopause , smoking , and body mass index ) .

Example answer:
{"entities": [{"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: Recurrent use of newer oral contraceptives and the risk of venous thromboembolism .

Example answer:
{"entities": [{"text": "oral contraceptives", "type": "Chemical"}, {"text": "venous thromboembolism", "type": "Disease"}]}

Example input:
Sentence: Two weeks after the initiation of therapy , her hematocrit had decreased from 44.1 % to 20.4 % , and she had a positive direct Coombs antiglobulin test and an elevated indirect bilirubin .

Example answer:
{"entities": [{"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: Despite therapy with ursodeoxycholic acid , prednisone , and then tacrolimus , her cholestatic disease was unrelenting , with cirrhosis shown by biopsy 6 months after presentation .

Example answer:
{"entities": [{"text": "ursodeoxycholic acid", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "cholestatic disease", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}]}

Example input:
Sentence: High-dose testosterone is associated with atherosclerosis in postmenopausal women .

Example answer:
{"entities": [{"text": "testosterone", "type": "Chemical"}, {"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: The risk of venous thromboembolism in women prescribed cyproterone acetate in combination with ethinyl estradiol : a nested cohort analysis and case-control study .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "cyproterone acetate", "type": "Chemical"}, {"text": "ethinyl estradiol", "type": "Chemical"}]}

Example input:
Sentence: Analysis was performed on 61 women with chemotherapy-responsive metastatic breast cancer receiving 96-h infusional cyclophosphamide as part of a triple sequential high-dose regimen to assess association between presence of peritransplant congestive heart failure ( CHF ) and the following pretreatment characteristics : presence of electrocardiogram ( EKG ) abnormalities , age , hypertension , prior cardiac history , smoking , diabetes mellitus , prior use of anthracyclines , and left-sided chest irradiation .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "CHF", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "diabetes mellitus", "type": "Disease"}, {"text": "anthracyclines", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : Our results suggest that high-dose testosterone therapy may adversely affect atherosclerosis in postmenopausal women and indicate that androgen replacement in these women may not be harmless .

Example answer:
{"entities": [{"text": "testosterone", "type": "Chemical"}, {"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: METHODS : In a population-based study in 513 naturally postmenopausal women aged 54-67 years , we studied the association between self-reported intramuscularly administered high-dose estrogen-testosterone therapy ( estradiol- and testosterone esters ) and aortic atherosclerosis .

Example answer:
{"entities": [{"text": "estrogen-testosterone", "type": "Chemical"}, {"text": "estradiol- and testosterone esters", "type": "Chemical"}, {"text": "atherosclerosis", "type": "Disease"}]}

Input:
Sentence: In relatively healthy women , combined continuous HT significantly increased the risk of venous thromboembolism or coronary event ( after one year 's use ) , stroke ( after 3 years ) , breast cancer ( after 5 years ) and gallbladder disease .

## Item bc5cdr:test:3419
Example input:
Sentence: The physician should also determine the proper use of any adjunctive medications ; such combined therapy has become the standard approach to treatment .

Example answer:
{"entities": []}

Example input:
Sentence: Current clinical experience .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSION : This case started with a media report in a popular newspaper , initiated by published , peer-reviewed research on herbals , and involved human failure in a case history , medical examination and clinical treatment .

Example answer:
{"entities": []}

Example input:
Sentence: An experimental study/short communication .

Example answer:
{"entities": []}

Example input:
Sentence: The clinical course and histopathological results of the two cases are presented .

Example answer:
{"entities": []}

Example input:
Sentence: A report of two cases .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : Behavioral experiments and electrophysiological recordings were performed in the present study .

Example answer:
{"entities": []}

Example input:
Sentence: DESIGN : Case study .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : A non-randomised clinical study of patients aged > or =65 years admitted to acute hospital wards during 1 month .

Example answer:
{"entities": []}

Example input:
Sentence: METHOD : Open , case series design .

Example answer:
{"entities": []}

Input:
Sentence: METHOD : A clinical case description .

## Item bc5cdr:test:3173
Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : As anticipated , adriamycin elicited nephrotic range proteinuria , renal interstitial damage and mild focal glomerulosclerosis .

Example answer:
{"entities": [{"text": "adriamycin", "type": "Chemical"}, {"text": "nephrotic", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "renal interstitial damage", "type": "Disease"}, {"text": "focal glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: Crescentic fibrillary glomerulonephritis associated with intermittent rifampin therapy for pulmonary tuberculosis .

Example answer:
{"entities": [{"text": "glomerulonephritis", "type": "Disease"}, {"text": "rifampin", "type": "Chemical"}, {"text": "pulmonary tuberculosis", "type": "Disease"}]}

Example input:
Sentence: Recurrent acute interstitial nephritis induced by azithromycin .

Example answer:
{"entities": [{"text": "interstitial nephritis", "type": "Disease"}, {"text": "azithromycin", "type": "Chemical"}]}

Example input:
Sentence: Two patients developed acute tubular necrosis , characterized clinically by acute oliguric renal failure , while they were receiving a combination of cephalothin sodium and gentamicin sulfate therapy .

Example answer:
{"entities": [{"text": "acute tubular necrosis", "type": "Disease"}, {"text": "cephalothin sodium", "type": "Chemical"}, {"text": "gentamicin sulfate", "type": "Chemical"}]}

Example input:
Sentence: Although most cases of antibiotic induced acute interstitial nephritis are benign and self-limited , some patients are at risk for permanent renal injury .

Example answer:
{"entities": [{"text": "interstitial nephritis", "type": "Disease"}, {"text": "renal injury", "type": "Disease"}]}

Example input:
Sentence: Ranitidine-induced acute interstitial nephritis in a cadaveric renal allograft .

Example answer:
{"entities": [{"text": "Ranitidine-induced", "type": "Chemical"}, {"text": "interstitial nephritis", "type": "Disease"}]}

Example input:
Sentence: We report a case of ranitidine-induced acute interstitial nephritis in a recipient of a cadaveric renal allograft presenting with acute allograft dysfunction within 48 hours of exposure to the drug .

Example answer:
{"entities": [{"text": "ranitidine-induced", "type": "Chemical"}, {"text": "interstitial nephritis", "type": "Disease"}]}

Example input:
Sentence: Since nonsteroidal anti-inflammatory agents interfere with this compensatory mechanism and may cause acute renal failure , they should be used with caution in such patients .

Example answer:
{"entities": [{"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: This drug occasionally has been associated with acute interstitial nephritis in native kidneys .

Example answer:
{"entities": [{"text": "interstitial nephritis", "type": "Disease"}]}

Input:
Sentence: Non-steroidal anti-inflammatory drugs-associated acute interstitial nephritis with granular tubular basement membrane deposits .

## Item bc5cdr:test:3423
Example input:
Sentence: SCr increases > or = 0.5 mg/dL occurred in 4.4 % ( 9 of 204 patients ) after iopamidol and 6.7 % ( 14 of 210 patients ) after iodixanol ( P=0.39 ) , whereas rates of SCr increases > or = 25 % were 9.8 % and 12.4 % , respectively ( P=0.44 ) .

Example answer:
{"entities": [{"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}]}

Example input:
Sentence: During an 18-month period of study 41 hemodialyzed patients receiving desferrioxamine ( 10-40 mg/kg BW/3 times weekly ) for the first time were monitored for detection of audiovisual toxicity .

Example answer:
{"entities": [{"text": "desferrioxamine", "type": "Chemical"}, {"text": "audiovisual toxicity", "type": "Disease"}]}

Example input:
Sentence: He had been prescribed telithromycin 400 mg/d PO to treat an upper respiratory tract infection 7 days prior .

Example answer:
{"entities": [{"text": "telithromycin", "type": "Chemical"}, {"text": "upper respiratory tract infection", "type": "Disease"}]}

Example input:
Sentence: Both , Ro4368554 ( 3 and 10 mg/kg , intraperitoneally ( i.p . ) )

Example answer:
{"entities": []}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Example input:
Sentence: These 6 patients had both renal and liver dysfunction ( P less than 0.05 ) , as well as cimetidine trough-concentrations of more than 1.25 microgram/ml ( P less than 0.05 ) .

Example answer:
{"entities": [{"text": "cimetidine", "type": "Chemical"}]}

Example input:
Sentence: We report a case of a 31 year old female who required admission to the Intensive Care Unit for ventilation and full supportive therapy , following ingestion of 13.5g bupropion .

Example answer:
{"entities": [{"text": "bupropion", "type": "Chemical"}]}

Example input:
Sentence: This study measured the objective and subjective neurocognitive effects of a single 10-mg dose of immediate-release oxycodone in healthy , older ( > 65 years ) , and middle-aged ( 35 to 55 years ) adults who were not suffering from chronic or significant daily pain .

Example answer:
{"entities": [{"text": "oxycodone", "type": "Chemical"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: infusion of morphine ( mean 73.6 mg ) and five patients receiving a continuous extradural infusion of 0.25 % bupivacaine ( mean 192 mg ) in the 24-h period following upper abdominal surgery .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: A 45-year-old man , an admitted frequent cocaine user , presented to the Emergency Department ( ED ) on two separate occasions with a history of priapism after cocaine use .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "priapism", "type": "Disease"}]}

Input:
Sentence: In the ER , his opiate level was 4497 ng/ml .

## Item bc5cdr:test:3029
Example input:
Sentence: The effect of high dose D-penicillamine treatment on aortic permeability to albumin and on the ultrastructure of the vessel .

Example answer:
{"entities": [{"text": "D-penicillamine", "type": "Chemical"}]}

Example input:
Sentence: Seizure activity due to PTZ and picrotoxin ( PTX ) was significantly decreased ; however , seizure activity due to 3-mercaptopropionic acid ( MPA ) , bicuculline ( BCC ) , methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate ( DMCM ) , or strychnine ( STR ) was not different from control .

Example answer:
{"entities": [{"text": "Seizure", "type": "Disease"}, {"text": "PTZ", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "PTX", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "3-mercaptopropionic acid", "type": "Chemical"}, {"text": "MPA", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "BCC", "type": "Chemical"}, {"text": "methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate", "type": "Chemical"}, {"text": "DMCM", "type": "Chemical"}, {"text": "strychnine", "type": "Chemical"}, {"text": "STR", "type": "Chemical"}]}

Example input:
Sentence: Oral diphenhydramine and prednisone were ineffective in preventing the recurrence of the allergic reaction .

Example answer:
{"entities": [{"text": "diphenhydramine", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "allergic reaction", "type": "Disease"}]}

Example input:
Sentence: Antithymocyte globulin in the treatment of D-penicillamine-induced aplastic anemia .

Example answer:
{"entities": [{"text": "Antithymocyte globulin", "type": "Chemical"}, {"text": "D-penicillamine-induced", "type": "Chemical"}, {"text": "aplastic anemia", "type": "Disease"}]}

Example input:
Sentence: Gamma-hexachlorocyclohexane ( gamma-HCH ) , the active ingredient of the insecticide lindane , has been shown to decrease seizure threshold to pentylenetrazol ( PTZ ) 3 h after exposure to gamma-HCH and conversely increase threshold to PTZ-induced seizures 24 h after exposure to gamma-HCH ( Vohland et al .

Example answer:
{"entities": [{"text": "Gamma-hexachlorocyclohexane", "type": "Chemical"}, {"text": "gamma-HCH", "type": "Chemical"}, {"text": "lindane", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "PTZ", "type": "Chemical"}, {"text": "PTZ-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Many of these patients are taking pentoxifylline ( Trental ) , a methylxanthine derivative which may improve intermittent claudication .

Example answer:
{"entities": [{"text": "pentoxifylline", "type": "Chemical"}, {"text": "Trental", "type": "Chemical"}, {"text": "methylxanthine", "type": "Chemical"}, {"text": "intermittent claudication", "type": "Disease"}]}

Example input:
Sentence: Male Sprague-Dawley rats were treated with D-penicillamine ( D-pen ) 500 mg/kg/day for 10 or 42 days .

Example answer:
{"entities": [{"text": "D-penicillamine", "type": "Chemical"}, {"text": "D-pen", "type": "Chemical"}]}

Example input:
Sentence: Use of antithymocyte globulin may be the optimal treatment of D-penicillamine-induced aplastic anemia .

Example answer:
{"entities": [{"text": "antithymocyte globulin", "type": "Chemical"}, {"text": "D-penicillamine-induced", "type": "Chemical"}, {"text": "aplastic anemia", "type": "Disease"}]}

Example input:
Sentence: We have described a unique patient who had reversible and dose-related myasthenia gravis after penicillamine and chloroquine therapy for rheumatoid arthritis .

Example answer:
{"entities": [{"text": "myasthenia gravis", "type": "Disease"}, {"text": "penicillamine", "type": "Chemical"}, {"text": "chloroquine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Example input:
Sentence: A patient who received antithymocyte globulin therapy for aplastic anemia due to D-penicillamine therapy is described .

Example answer:
{"entities": [{"text": "antithymocyte globulin", "type": "Chemical"}, {"text": "aplastic anemia", "type": "Disease"}, {"text": "D-penicillamine", "type": "Chemical"}]}

Input:
Sentence: During the follow-up of our patient , penicillamine was interrupted after the appearance of a lichenoid dermatitis , and zinc acetate permitted to continue the successful treatment of the patient without side-effects .

## Item bc5cdr:test:3325
Example input:
Sentence: Risk in the raloxifene group was higher than in the placebo group for the first 2 years , but decreased to about the same rate as in the placebo group thereafter .

Example answer:
{"entities": [{"text": "raloxifene", "type": "Chemical"}]}

Example input:
Sentence: Moderate or severe adverse events were more common in subjects on clonidine ( 79.4 % versus 49.2 % ; p =.0006 ) but not associated with higher rates of early study withdrawal .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: Patients who received enalapril experienced clinically and statistically significantly less symptomatic hypotension ( 5.2 % ) than the patients who received prazosin ( 12.9 % ) .

Example answer:
{"entities": [{"text": "enalapril", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "prazosin", "type": "Chemical"}]}

Example input:
Sentence: Overall , in high-risk patients , warfarin is superior to aspirin in preventing strokes , with a relative risk reduction of 36 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "strokes", "type": "Disease"}]}

Example input:
Sentence: Recent reports indicate that single agent therapy with vinorelbine ( VNB ) or gemcitabine ( GEM ) may obtain a response rate of 20-30 % in elderly patients , with acceptable toxicity and improvement in symptoms and quality of life .

Example answer:
{"entities": [{"text": "vinorelbine", "type": "Chemical"}, {"text": "VNB", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "GEM", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: Patients with a DBP reduction of > or =20 % in the high-dose group had a significantly increased adjusted OR for the compound outcome variable death or dependency ( Barthel Index < 60 ) ( n/N=25/26 , OR 10 .

Example answer:
{"entities": [{"text": "DBP reduction", "type": "Disease"}, {"text": "death", "type": "Disease"}]}

Example input:
Sentence: Treatment duration longer than 1 year was associated with an eightfold increased risk ( OR = 7.7 , 95 % CI 0.9 to 69 ) .

Example answer:
{"entities": []}

Example input:
Sentence: The mortality rate among patients with ATT-ALF was high ( 67.1 % , n = 47 ) , and only 23 ( 32.9 % ) patients recovered with medical treatment .

Example answer:
{"entities": []}

Example input:
Sentence: Based on this principle a 27-year old woman , classified as being in the high-risk group ( Goldstein and Berkowitz score : 11 ) , was treated with multiple cytotoxic drugs .

Example answer:
{"entities": []}

Input:
Sentence: The 1-yr mortality was significantly higher after aprotinin treatment in the high risk surgery group ( 17.7 % vs 9.8 % , P = 0.034 ) .
