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

## Item bc5cdr:test:4000
Input:
Sentence: Color vision was defective and fundus examination revealed optic disc edema in both eyes .

## Item bc5cdr:test:4082
Input:
Sentence: Basal functioning of the hypothalamic-pituitary-adrenal ( HPA ) axis and psychological distress in recreational ecstasy polydrug users .

## Item bc5cdr:test:4154
Input:
Sentence: Multivariate analysis showed that trough TAC level was the only independent risk factor associated with the seizures .

## Item bc5cdr:test:3882
Input:
Sentence: Eighty-seven percent of the patients had received immunomodulatory drugs included in some line of therapy before bort-dex .

## Item bc5cdr:test:4162
Input:
Sentence: The saline- and apigenin-treated rats that did not step through into the dark compartment during the cut-off time ( 540 s ) were retested weekly for up to eight weeks .

## Item bc5cdr:test:4024
Input:
Sentence: CONCLUSIONS : The incidence of HIT in patients with end-stage hepatic failure is , with about 1.95 % , rare .

## Item bc5cdr:test:3768
Input:
Sentence: RESEARCH DESIGN AND METHODS : EndoMT was induced in a mouse pancreatic microvascular endothelial cell line ( MMEC ) in the presence of advanced glycation end products ( AGEs ) and in the endothelial lineage-traceble mouse line Tie2-Cre ; Loxp-EGFP by administration of AGEs , with nonglycated mouse albumin serving as a control .

## Item bc5cdr:test:3919
Input:
Sentence: Peripheral neuropathy was observed only in 2.5 % of patients and deep vein thrombosis in 5.7 % .

## Item bc5cdr:test:3764
Input:
Sentence: Blockade of endothelial-mesenchymal transition by a Smad3 inhibitor delays the early development of streptozotocin-induced diabetic nephropathy .

## Item bc5cdr:test:3934
Input:
Sentence: Risk factors and predictors of levodopa-induced dyskinesia among multiethnic Malaysians with Parkinson 's disease .

## Item bc5cdr:test:4173
Input:
Sentence: Furthermore , microinjection of CCK-8 ( 0.1 and 1ug , i.c.v . )

## Item bc5cdr:test:4023
Input:
Sentence: The platelet count exceeded 100,000/uL in most of the patients ( n = 193 ) at a medium of 7 d. Regarding HIT II , there were four ( 1.95 % ) patients with a background of HIT type II .

## Item bc5cdr:test:4088
Input:
Sentence: RESULTS : Both user groups exhibited significantly greater levels of anxiety and depression than nonusers .

## Item bc5cdr:test:3946
Input:
Sentence: Patients with dyskinesia had lower onset age ( p < 0.001 ) , longer duration of levodopa therapy ( p < 0.001 ) , longer disease duration ( p < 0.001 ) , higher total daily levodopa dose ( p < 0.001 ) , and higher total UPDRS scores ( p = 0.005 ) than patients without dyskinesia .

## Item bc5cdr:test:4279
Input:
Sentence: Upon leaving the sedation area , the patient collapsed , with no apparent inciting event .

## Item bc5cdr:test:3387
Input:
Sentence: STUDY SELECTION : English-language randomized , controlled trials ( RCTs ) ; case-control studies ; meta-analyses ; and systematic reviews of aspirin versus control for the primary prevention of cardiovascular disease ( CVD ) were selected to answer the following questions : Does aspirin decrease coronary heart events , strokes , death from coronary heart events or stroke , or all-cause mortality in adults without known CVD ?

## Item bc5cdr:test:4310
Input:
Sentence: The median ( IQR [ range ] ) time after surgery when the seizure occurred was 7 ( 6-12 [ 1-216 ] ) h and 8 ( 6-11 [ 4-18 ] ) h , respectively .

## Item bc5cdr:test:4322
Input:
Sentence: Memory recall of word pairs was evaluated before and after a period of sleep , with and without interference prior to testing .

## Item bc5cdr:test:4206
Input:
Sentence: In this study , neurocognitive outcomes and neuroradiologic evidence of leukoencephalopathy were compared in children treated with intense central nervous system ( CNS ) -directed therapy ( P9605 ) versus those receiving fewer CNS-directed treatment days during intensive consolidation ( P9201 ) .

## Item bc5cdr:test:4323
Input:
Sentence: In addition , we assessed neurocognitive performances across tasks of learning , memory and executive functioning .

## Item bc5cdr:test:4096
Input:
Sentence: Encephalopathy has been reported in 10-40 % of patients receiving high-dose IV ifosfamide .

## Item bc5cdr:test:3638
Input:
Sentence: Fourth group received a single dose of ZnSO ( 4 ) ( 0.1 micromol/10 microl normal saline , i.c.v ) then BCNU ( 20 mg/kg , i.v , once ) after 24 h. The obtained data revealed that BCNU administration resulted in deterioration of learning and short-term memory ( STM ) , as measured by using radial arm water maze , accompanied with decreased hippocampal glutathione reductase ( GR ) activity and reduced glutathione ( GSH ) content .

## Item bc5cdr:test:4099
Input:
Sentence: RESULTS : All five patients experienced symptoms of encephalopathy soon after ( within 12 h-2 days ) receiving ifosfamide .

## Item bc5cdr:test:3301
Input:
Sentence: BACKGROUND : The aim of the study was to investigate the antihypertensive effects of angiotensin II type-1 receptor blocker , losartan , and its potential in slowing down renal disease progression in spontaneously hypertensive rats ( SHR ) with adriamycin ( ADR ) nephropathy .

## Item bc5cdr:test:3959
Input:
Sentence: One month of oral galactose treatment initiated immediately after the STZ-icv administration , successfully prevented development of the STZ-icv-induced cognitive deficits .

## Item bc5cdr:test:4104
Input:
Sentence: CONCLUSIONS : Severity of ifosfamide related encephalopathy correlates with EEG changes .

## Item bc5cdr:test:4171
Input:
Sentence: Acute morphine ( 30mg/kg , s.c. ) treatment significantly attenuated hippocampal LTP and CCK-8 ( 1ug , i.c.v . )

## Item bc5cdr:test:4240
Input:
Sentence: The liver biochemistries eventually normalized within 3 weeks of stopping the fluvastatin .

## Item bc5cdr:test:4115
Input:
Sentence: CIN more frequently developed in patients who had undergone CT within 45 days after the last chemotherapy ( P = 0.005 ) ; it was also an independent risk factor ( P = 0.017 ) .

## Item bc5cdr:test:4350
Input:
Sentence: This drug is rapidly absorbed from the gastrointestinal tract , and most of it is excreted from the kidney .

## Item bc5cdr:test:4160
Input:
Sentence: There were no differences between saline- and apigenin-treated groups in the 24 h retention trial .

## Item bc5cdr:test:4268
Input:
Sentence: Myoclonic movements are evaluated , which were observed and graded according to clinical severity during the 2 minutes after etomidate injection .

## Item bc5cdr:test:4257
Input:
Sentence: RESULTS : Fourteen patients ( 18.67 % ) developed cardiotoxicity after treatment .

## Item bc5cdr:test:3871
Input:
Sentence: Perfusion of bladder with P2X3 and NK1 receptors antagonists ameliorated the bladder function .

## Item bc5cdr:test:4381
Input:
Sentence: She is currently being treated with best supportive care .

## Item bc5cdr:test:4169
Input:
Sentence: Here , we investigated the effects of CCK-8 on long-term potentiation ( LTP ) in the lateral perforant path ( LPP ) -granule cell synapse of rat dentate gyrus ( DG ) in acute saline or morphine-treated rats .

## Item bc5cdr:test:3846
Input:
Sentence: The plasticity of primary motor cortex ( M1 ) in patients with Parkinson 's disease ( PD ) and levodopa-induced dyskinesias ( LIDs ) is severely impaired .

## Item bc5cdr:test:4393
Input:
Sentence: Despite immediate intravenous antimicrobial therapy , he succumbed 23 h after the onset .

## Item bc5cdr:test:4092
Input:
Sentence: CONCLUSIONS : The increases in anxiety and depression are in line with previous observations in recreational ecstasy-polydrug users .

## Item bc5cdr:test:4283
Input:
Sentence: Unanticipated and previously unreported outcomes may be witnessed as we expand the use of certain sedatives to alternative routes of administration .

## Item bc5cdr:test:4307
Input:
Sentence: Multivariate regression analysis was performed to identify independent predictors of postoperative seizures .

## Item bc5cdr:test:4223
Input:
Sentence: Thus , the precipitating cause of convulsions was believed to be an overdose of TNA .

## Item bc5cdr:test:4192
Input:
Sentence: INTRODUCTION AND OBJECTIVE : Contrast-induced nephropathy ( CIN ) significantly increases the morbidity and mortality of patients .

## Item bc5cdr:test:4111
Input:
Sentence: CIN was defined as an increase in serum creatinine ( Cr ) of 0.5 mg/dl or more , or elevation of Cr to 25 % over baseline .

## Item bc5cdr:test:4207
Input:
Sentence: A total of 66 children from 16 Pediatric Oncology Group institutions with `` standard-risk '' acute lymphoblastic leukemia , 1.00 to 9.99 years at diagnosis , without evidence of CNS leukemia at diagnosis were enrolled on ACCL0131 : 28 from P9201 and 38 from P9605 .

## Item bc5cdr:test:3950
Input:
Sentence: An unexpected diagnosis in a renal-transplant patient with proteinuria treated with everolimus : AL amyloidosis .

## Item bc5cdr:test:4449
Input:
Sentence: SETTING : Neurocritical care units at two academic medical centers with dedicated neurocritical care teams and board-certified neurointensivists .

## Item bc5cdr:test:4217
Input:
Sentence: Tranexamic acid ( TNA ) 1 g 8-hourly was administered to her to control bleeding per vaginum .

## Item bc5cdr:test:4118
Input:
Sentence: CIN developed 4.5-times more frequently in patients with cancer who had undergone recent chemotherapy .

## Item bc5cdr:test:3765
Input:
Sentence: OBJECTIVE : A multicenter , controlled trial showed that early blockade of the renin-angiotensin system in patients with type 1 diabetes and normoalbuminuria did not retard the progression of nephropathy , suggesting that other mechanism ( s ) are involved in the pathogenesis of early diabetic nephropathy ( diabetic nephropathy ) .

## Item bc5cdr:test:4015
Input:
Sentence: Epinephrine alone or in combination with lipid was associated with an increased number of ECG abnormalities compared with lipid emulsion alone .

## Item bc5cdr:test:4256
Input:
Sentence: Cardiotoxicity was defined as a reduction of the LVEF of > 5 % to < 55 % with symptoms of heart failure or an asymptomatic reduction of the LVEF of > 10 % to < 55 % .

## Item bc5cdr:test:4101
Input:
Sentence: Initial EEG showed epileptiform discharges in three patients ; run of triphasic waves in one patient and moderate degree diffuse generalized slowing .

## Item bc5cdr:test:3811
Input:
Sentence: DISCUSSION : Daptomycin was initiated in our patient secondary to possible nafcillin-induced acute interstitial nephritis and relapsing bacteremia .

## Item bc5cdr:test:4272
Input:
Sentence: Cholestatic presentation of yellow phosphorus poisoning .

## Item bc5cdr:test:4373
Input:
Sentence: At the time of treatment , she was on continuous renal replacement therapy due to sequelae of tumor lysis syndrome ( TLS ) .

## Item bc5cdr:test:4369
Input:
Sentence: A 37-year-old Caucasian woman with a history of T-cell lymphoblastic lymphoma was admitted for relapsed disease .

## Item bc5cdr:test:4426
Input:
Sentence: Here , we developed a murine model of glucocorticoid-induced glaucoma that exhibits glaucoma features that are observed in patients .

## Item bc5cdr:test:4522
Input:
Sentence: Toxicity included embryolethality , teratogenicity , and growth retardation .

## Item bc5cdr:test:4177
Input:
Sentence: Glial activation and post-synaptic neurotoxicity : the key events in Streptozotocin ( ICV ) induced memory impairment in rats .

## Item bc5cdr:test:4288
Input:
Sentence: The diagnoses of manic shift and akathisia were dismissed .

## Item bc5cdr:test:3264
Input:
Sentence: The most common regimens were 3TC + d4T + nevirapine ( NVP ) ( 54.8 % ) , zidovudine ( AZT ) + 3TC + NVP ( 14.5 % ) , 3TC + d4T + efavirenz ( EFV ) ( 20.1 % ) , and AZT + 3TC + EFV ( 5.4 % ) .

## Item bc5cdr:test:4027
Input:
Sentence: Takotsubo syndrome ( TS ) , also known as broken heart syndrome , is characterized by left ventricle apical ballooning with elevated cardiac biomarkers and electrocardiographic changes suggestive of an acute coronary syndrome ( ie , ST-segment elevation , T wave inversions , and pathologic Q waves ) .

## Item bc5cdr:test:4128
Input:
Sentence: Her medications included desvenlafaxine , and symptoms included nausea , anxiety and confusion .

## Item bc5cdr:test:4026
Input:
Sentence: Takotsubo syndrome ( or apical ballooning syndrome ) secondary to Zolmitriptan .

## Item bc5cdr:test:4025
Input:
Sentence: For further reduction of HIT type II , the use of intravenous heparin should be avoided and the prophylactic anticoagulation should be performed with low-molecular-weight heparin after normalization of platelet count .

## Item bc5cdr:test:4346
Input:
Sentence: To the best of our knowledge , this is the first reported case of ketoconazole-induced baboon syndrome in the English literature .

## Item bc5cdr:test:4338
Input:
Sentence: Common side effects include nausea , vomiting and hypotension .

## Item bc5cdr:test:4500
Input:
Sentence: RESULTS : In the amphetamine-induced locomotion test , there were significant increases in all movements compared with the amphetamine-free group .

## Item bc5cdr:test:4274
Input:
Sentence: Poisoning with yellow phosphorus classically manifests with acute hepatitis leading to acute liver failure which may need liver transplantation .

## Item bc5cdr:test:3956
Input:
Sentence: An alternative source of energy is d-galactose ( the C-4-epimer of d-glucose ) which is transported into the brain by insulin-independent GLUT3 transporter where it might be metabolized to glucose via the Leloir pathway .

## Item bc5cdr:test:4565
Input:
Sentence: Magnetic resonance imaging ( MRI ) brain showed abnormal signal intensity involving both dentate nuclei of cerebellum and splenium of corpus callosum .

## Item bc5cdr:test:4382
Input:
Sentence: To our knowledge , this is the first published case report of severe neurotoxicity caused by nelarabine in a patient who received concurrent IT chemotherapy .

## Item bc5cdr:test:3459
Input:
Sentence: On admission the patient was taking carvedilol 12 mg twice daily , warfarin 2 mg/day , folic acid 1 mg/day , levothyroxine 100 microg/day , pantoprazole 40 mg/day , paroxetine 40 mg/day , and flecainide 100 mg twice daily .

## Item bc5cdr:test:4421
Input:
Sentence: In conclusion , glutamate and capsaicin yield reproducible hyperalgesic and allodynic responses , and the present model is well suited for basic research , as well as for assessing the modulation of central phenomena .

## Item bc5cdr:test:4190
Input:
Sentence: Present study clearly suggests that glial activation and post synaptic neurotoxicity are the key factors in STZ induced memory impairment and neuronal cell death .

## Item bc5cdr:test:4518
Input:
Sentence: Our objective in this study was to investigate whether the compounds induce developmental toxicity via the dermal route , which is more relevant to occupational exposure , hence better addressing human health risks .

## Item bc5cdr:test:4485
Input:
Sentence: After one week of therapy , he was transferred to the intensive care unit with cardiopulmonary compromise related to superior vena cava ( SVC ) syndrome .

## Item bc5cdr:test:3799
Input:
Sentence: OBJECTIVE : To report a case of methicillin-sensitive Staphylococcus aureus ( MSSA ) bacteremia with suspected MSSA meningitis treated with high-dose daptomycin assessed with concurrent serum and cerebrospinal fluid ( CSF ) concentrations .

## Item bc5cdr:test:3999
Input:
Sentence: A 45-year-old male patient who was on treatment with multiple second-line anti-tuberculous drugs including linezolid and ethambutol for extensively drug-resistant tuberculosis ( XDR-TB ) presented to us with painless progressive loss of vision in both eyes .

## Item bc5cdr:test:4546
Input:
Sentence: Male C57BL/6 mice were administered with subconvulsive dose of pentylenetetrazole ( 37 mg/kg , i.p . )

## Item bc5cdr:test:3967
Input:
Sentence: We undertook a descriptive analysis of Yellow Card records of 407 HIV-positive persons taking tenofovir disoproxil fumarate ( TDF ) as part of their antiretroviral therapy regimen and submitted to the Medicines and Healthcare Products Regulatory Agency ( MHRA ) with suspected kidney adverse effects .

## Item bc5cdr:test:4367
Input:
Sentence: Nelarabine neurotoxicity with concurrent intrathecal chemotherapy : Case report and review of literature .

## Item bc5cdr:test:4558
Input:
Sentence: p53 inhibition blocked transient DOX-induced STAT3 activation in MHC-CB7 mice , which was associated with enhanced induction of the DNA repair proteins Ku70 and Ku80 .

## Item bc5cdr:test:4196
Input:
Sentence: The first group of patients was administered isotonic sodium chloride ; the second group was administered a solution that of 5 % dextrose and sodium bicarbonate , while the third group was administered isotonic sodium chloride before and after the contrast injection .

## Item bc5cdr:test:4327
Input:
Sentence: Normoammonemic encephalopathy : solely valproate induced or multiple mechanisms ?

## Item bc5cdr:test:4394
Input:
Sentence: Physicians should recognise the possibility of fatal bacterial infections related to bortezomib plus high-dose dexamethasone in elderly patients , and we believe this case warrants further investigation .

## Item bc5cdr:test:4062
Input:
Sentence: RESULTS : Our data showed that subacute exposure to diazinon significantly increased concentrations of cholesterol , triglyceride and LDL .

## Item bc5cdr:test:4505
Input:
Sentence: We suggest that DHEA displays typical neuroleptic-like effects , and may be used in the treatment of schizophrenia .

## Item bc5cdr:test:4568
Input:
Sentence: Aconitine is a major bioactive diterpenoid alkaloid with high content derived from herbal aconitum plants .

## Item bc5cdr:test:4636
Input:
Sentence: It increases mortality , hospital length of stay , and costs .

## Item bc5cdr:test:4641
Input:
Sentence: Patients with an adherence to SOP > 70 % were classified into the high adherence group ( HAG ) and patients with an adherence of < 70 % into the low adherence group ( LAG ) .

## Item bc5cdr:test:4071
Input:
Sentence: In this retrospective single-centre analysis , patients with relapsed or refractory HL treated with gemcitabine 1,000 mg/m ( 2 ) day ( D ) 1 , D8 and D15 ; methylprednisolone 1,000 mg D1-5 ; and cisplatin 100 mg/m ( 2 ) D15 , every 28 days ( GEM-P ) were included .

## Item bc5cdr:test:4577
Input:
Sentence: The expression analysis of Ca ( 2+ ) handling proteins demonstrated that aconitine promoted Ca ( 2+ ) overload through the expression regulation of Ca ( 2+ ) handling proteins .

## Item bc5cdr:test:4435
Input:
Sentence: OIH can limit the clinical use of opioid analgesics and complicate withdrawal from opioid addiction .

## Item bc5cdr:test:4532
Input:
Sentence: Data were collected on adult cancer patients receiving single-agent cisplatin as an outpatient from January 2011 to September 2012 .

## Item bc5cdr:test:4603
Input:
Sentence: On the 49th day of terbinafine therapy , he was brought to the emergency room for a decrease of his global health status , confusion and falls .

## Item bc5cdr:test:4422
Input:
Sentence: Ocular-specific ER stress reduction rescues glaucoma in murine glucocorticoid-induced glaucoma .

## Item bc5cdr:test:4615
Input:
Sentence: METHODS : Adult male Wistar rats were intracerebroventricularly ( icv ) infused with STZ ( 750 ug ) on d 1 and d 3 , and a passive avoidance task was assessed 2 weeks after the first injection of STZ .

## Item bc5cdr:test:4604
Input:
Sentence: The electrocardiogram revealed a 37 beats/min sinus bradycardia .
