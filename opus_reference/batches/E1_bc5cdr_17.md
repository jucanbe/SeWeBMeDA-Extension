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

## Item bc5cdr:test:3633
Example input:
Sentence: The antiepileptic drugs , phenobarbitone and carbamazepine are well known to cause cognitive impairment on chronic use .

Example answer:
{"entities": [{"text": "phenobarbitone", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "cognitive impairment", "type": "Disease"}]}

Example input:
Sentence: Therefore , PG-9 could represent a potential useful drug able to improve the function of impaired cognitive processes .

Example answer:
{"entities": []}

Example input:
Sentence: At hippocampal Schaeffer collateral-CA1 synapses , long-term potentiation was preserved in BMC-transplanted rats compared to epileptic controls .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}]}

Example input:
Sentence: A novel compound , maltolyl p-coumarate , attenuates cognitive deficits and shows neuroprotective effects in vitro and in vivo dementia models .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "cognitive deficits", "type": "Disease"}, {"text": "dementia", "type": "Disease"}]}

Example input:
Sentence: Deficits in learning and memory : parahippocampal hyperactivity and frontocortical hypoactivity in cannabis users .

Example answer:
{"entities": [{"text": "hyperactivity", "type": "Disease"}, {"text": "cannabis", "type": "Chemical"}]}

Example input:
Sentence: Passive avoidance paradigm and elevated plus maze test were used to assess cognitive function .

Example answer:
{"entities": []}

Example input:
Sentence: To develop a novel and effective drug that could enhance cognitive function and neuroprotection , we newly synthesized maltolyl p-coumarate by the esterification of maltol and p-coumaric acid .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "maltol", "type": "Chemical"}, {"text": "p-coumaric acid", "type": "Chemical"}]}

Example input:
Sentence: The density of hippocampal neurons in the brains of animals treated with BMCs was markedly preserved .

Example answer:
{"entities": []}

Example input:
Sentence: Both , production of reactive oxygen species as well as activation of NF-kappaB have been implicated in severe neuronal damage in different sub-regions of the hippocampus as well as in the surrounding cortices .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "neuronal damage", "type": "Disease"}]}

Example input:
Sentence: Prevention of seizures and reorganization of hippocampal functions by transplantation of bone marrow cells in the acute phase of experimental epilepsy .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "epilepsy", "type": "Disease"}]}

Input:
Sentence: Hippocampal integrity is essential for cognitive functions .

## Item bc5cdr:test:3342
Example input:
Sentence: In the antinociceptive and antiamnesic dose range , ( +/- ) -PG-9 did not impair mouse performance evaluated by the rota-rod test and Animex apparatus .

Example answer:
{"entities": [{"text": ")", "type": "Chemical"}]}

Example input:
Sentence: Mean post-SCr increases were significantly less with iopamidol ( all patients : 0.07 versus 0.12 mg/dL , 6.2 versus 10.6 micromol/L , P=0.03 ; patients with diabetes : 0.07 versus 0.16 mg/dL , 6.2 versus 14.1 micromol/L , P=0.01 ) .

Example answer:
{"entities": [{"text": "iopamidol", "type": "Chemical"}, {"text": "diabetes", "type": "Disease"}]}

Example input:
Sentence: The effects of oral doses of diazepam ( single dose of 10 mg and a median dose of 30 mg/day for 2 weeks ) and propranolol ( single dose of 80 mg and a median dose of 240 mg/day for 2 weeks ) on psychological performance of patients with panic disorders and agoraphobia were investigated in a double-blind , randomized and crossover design .

Example answer:
{"entities": [{"text": "diazepam", "type": "Chemical"}, {"text": "propranolol", "type": "Chemical"}, {"text": "panic disorders", "type": "Disease"}, {"text": "agoraphobia", "type": "Disease"}]}

Example input:
Sentence: In long-term infusion studies , flestolol was well tolerated at the effective beta-blocking dose ( 5 micrograms/kg/min ) for up to seven days .

Example answer:
{"entities": [{"text": "flestolol", "type": "Chemical"}]}

Example input:
Sentence: 1 h prior to haloperidol resulted in a dose-dependent increase in the catalepsy times ( P < 0.05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: This study suggests that administration of low doses of beta-blockers may improve levodopa-induced ballistic and choreic dyskinesia in PD .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: In experiments using specific adrenergic antagonists , we found that pretreatment with the beta-adrenergic receptor antagonist propranolol blocked cocaine-induced anxiety-like behavior in Dbh +/- and wild-type C57BL6/J mice , while the alpha ( 1 ) antagonist prazosin and the alpha ( 2 ) antagonist yohimbine had no effect .

Example answer:
{"entities": [{"text": "propranolol", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "anxiety-like", "type": "Disease"}, {"text": "prazosin", "type": "Chemical"}, {"text": "yohimbine", "type": "Chemical"}]}

Example input:
Sentence: Flestolol blood concentrations increased linearly with increasing dose and good correlation exists between blood concentrations of flestolol and beta-adrenergic blockade .

Example answer:
{"entities": [{"text": "Flestolol", "type": "Chemical"}, {"text": "flestolol", "type": "Chemical"}]}

Example input:
Sentence: This difference is explained by patient comorbidities and more frequent use of beta-blockers .

Example answer:
{"entities": []}

Example input:
Sentence: Seven patients suffering from Parkinson 's disease ( PD ) with severely disabling dyskinesia received low-dose propranolol as an adjunct to the currently used medical treatment .

Example answer:
{"entities": [{"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "propranolol", "type": "Chemical"}]}

Input:
Sentence: The dose of ( - ) -propranolol was significantly smaller than that of ( + ) -propranolol in both species but much higher than that required to produce evidence of beta-blockade.8 .

## Item bc5cdr:test:3367
Example input:
Sentence: Valproic acid ( VPA ) is a broad-spectrum antiepileptic drug and is usually well-tolerated .

Example answer:
{"entities": [{"text": "Valproic acid", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}]}

Example input:
Sentence: Simvastatinezetimibe and escitalopram ( which she was taking for depression ) were discontinued , and other potential causes of hepatotoxicity were excluded .

Example answer:
{"entities": [{"text": "Simvastatinezetimibe", "type": "Chemical"}, {"text": "escitalopram", "type": "Chemical"}, {"text": "depression", "type": "Disease"}, {"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: A case of valproate-induced encephalopathy is presented .

Example answer:
{"entities": [{"text": "valproate-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: FINDINGS : A 28-year-old man suffering from idiopathic epilepsy with generalized seizures was treated with LEV ( 3000 mg ) added to valproate ( VPA ) ( 2000 mg ) .

Example answer:
{"entities": [{"text": "idiopathic epilepsy", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "LEV", "type": "Chemical"}, {"text": "valproate", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}]}

Example input:
Sentence: Valproic acid induced encephalopathy -- 19 new cases in Germany from 1994 to 2003 -- a side effect associated to VPA-therapy not only in young children .

Example answer:
{"entities": [{"text": "Valproic acid", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "VPA-therapy", "type": "Chemical"}]}

Example input:
Sentence: Morphological features of encephalopathy after chronic administration of the antiepileptic drug valproate to rats .

Example answer:
{"entities": [{"text": "encephalopathy", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}]}

Example input:
Sentence: Long-term intragastric application of the antiepileptic drug sodium valproate ( Vupral `` Polfa '' ) at the effective dose of 200 mg/kg b. w. once daily to rats for 1 , 3 , 6 , 9 and 12 months revealed neurological disorders indicating cerebellum damage ( `` valproate encephalopathy '' ) .

Example answer:
{"entities": [{"text": "sodium valproate", "type": "Chemical"}, {"text": "neurological disorders", "type": "Disease"}, {"text": "cerebellum damage", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Valproate-induced encephalopathy .

Example answer:
{"entities": [{"text": "Valproate-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: The possible influence of the hepatic damage , mainly hyperammonemia , upon the development of valproate encephalopathy is discussed .

Example answer:
{"entities": [{"text": "hepatic damage", "type": "Disease"}, {"text": "hyperammonemia", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Valproate-induced encephalopathy is a rare syndrome that may manifest in otherwise normal epileptic individuals .

Example answer:
{"entities": [{"text": "Valproate-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "epileptic", "type": "Disease"}]}

Input:
Sentence: Nonalcoholic fatty liver disease during valproate therapy .

## Item bc5cdr:test:3185
Example input:
Sentence: We examined the abundance of ENaC subunit mRNAs and proteins in puromycin aminonucleoside ( PAN ) -induced nephrotic syndrome .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephrotic syndrome", "type": "Disease"}]}

Example input:
Sentence: A literature review revealed no prior reports of pericarditis in anti-MPO pANCA-positive vasculitis associated with propylthio- uracil therapy .

Example answer:
{"entities": [{"text": "pericarditis", "type": "Disease"}, {"text": "vasculitis", "type": "Disease"}, {"text": "propylthio- uracil", "type": "Chemical"}]}

Example input:
Sentence: This patient underwent a 10-month regimen of rifampin and isoniazid for pulmonary tuberculosis and was discovered to have developed signs of severe renal failure five weeks after completion of therapy .

Example answer:
{"entities": [{"text": "rifampin", "type": "Chemical"}, {"text": "isoniazid", "type": "Chemical"}, {"text": "pulmonary tuberculosis", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: Two patients developed acute tubular necrosis , characterized clinically by acute oliguric renal failure , while they were receiving a combination of cephalothin sodium and gentamicin sulfate therapy .

Example answer:
{"entities": [{"text": "acute tubular necrosis", "type": "Disease"}, {"text": "cephalothin sodium", "type": "Chemical"}, {"text": "gentamicin sulfate", "type": "Chemical"}]}

Example input:
Sentence: Doxorubicin-induced nephropathy leads to epithelial sodium channel ( ENaC ) -dependent volume retention and renal fibrosis .

Example answer:
{"entities": [{"text": "Doxorubicin-induced", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "sodium", "type": "Chemical"}, {"text": "volume retention", "type": "Disease"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: The results suggest a possible involvement of the renin-angiotensin system in the development of puromycin aminonucleoside-induced nephrosis .

Example answer:
{"entities": [{"text": "puromycin", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: Puromycin aminonucleoside nephrosis was induced by single intraperitoneal injection of puromycin aminonucleoside ( PAN , 20 mg/100g BW ) .

Example answer:
{"entities": [{"text": "Puromycin aminonucleoside", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: This case study reveals an unusual finding of rapidly proliferative crescentic glomerulonephritis in a patient treated with rifampin who had no other identifiable causes for developing this disease .

Example answer:
{"entities": [{"text": "glomerulonephritis", "type": "Disease"}, {"text": "rifampin", "type": "Chemical"}]}

Example input:
Sentence: This report documents the unusual occurrence of rapidly progressive glomerulonephritis with crescents and fibrillar glomerulonephritis in a patient treated with rifampin .

Example answer:
{"entities": [{"text": "glomerulonephritis", "type": "Disease"}, {"text": "rifampin", "type": "Chemical"}]}

Example input:
Sentence: Crescentic fibrillary glomerulonephritis associated with intermittent rifampin therapy for pulmonary tuberculosis .

Example answer:
{"entities": [{"text": "glomerulonephritis", "type": "Disease"}, {"text": "rifampin", "type": "Chemical"}, {"text": "pulmonary tuberculosis", "type": "Disease"}]}

Input:
Sentence: Rifampicin-associated segmental necrotizing glomerulonephritis in staphylococcal endocarditis .

## Item bc5cdr:test:3406
Example input:
Sentence: This case emphasizes the possibility that HUS in adults is not invariably irreversible and that , despite prolonged oliguria , recovery of renal function can be obtained .

Example answer:
{"entities": [{"text": "HUS", "type": "Disease"}, {"text": "oliguria", "type": "Disease"}]}

Example input:
Sentence: This retrospective study examines the incidence and treatment of ESRD and chronic renal failure ( CRF ) in OLTX patients .

Example answer:
{"entities": [{"text": "ESRD", "type": "Disease"}, {"text": "chronic renal failure", "type": "Disease"}, {"text": "CRF", "type": "Disease"}]}

Example input:
Sentence: Especially in old patients , intensivists should consider intoxications ( with cholinergics ) as a cause of acute cardiovascular failure .

Example answer:
{"entities": [{"text": "acute cardiovascular failure", "type": "Disease"}]}

Example input:
Sentence: Spironolactone-induced renal insufficiency and hyperkalemia in patients with heart failure .

Example answer:
{"entities": [{"text": "Spironolactone-induced", "type": "Chemical"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}]}

Example input:
Sentence: We therefore sought to determine the prevalence and clinical associations of hyperkalemia and renal insufficiency in heart failure patients treated with spironolactone .

Example answer:
{"entities": [{"text": "hyperkalemia", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}, {"text": "spironolactone", "type": "Chemical"}]}

Example input:
Sentence: In this patient , renal artery stenosis combined with heart failure and diuretic therapy certainly resulted in a strong activation of the renin-angiotensin system ( RAS ) .

Example answer:
{"entities": [{"text": "renal artery stenosis", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}]}

Example input:
Sentence: Therefore , in adult patients affected by HUS , dialysis should not be discontinued prematurely ; moreover , bilateral nephrectomy , for treatment of severe hypertension and microangiopathic hemolytic anemia , should be performed with caution .

Example answer:
{"entities": [{"text": "HUS", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "microangiopathic hemolytic anemia", "type": "Disease"}]}

Example input:
Sentence: Patients with renal insufficiency should not be given this regimen .

Example answer:
{"entities": [{"text": "renal insufficiency", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : A previous randomized controlled trial evaluating the use of spironolactone in heart failure patients reported a low risk of hyperkalemia ( 2 % ) and renal insufficiency ( 0 % ) .

Example answer:
{"entities": [{"text": "spironolactone", "type": "Chemical"}, {"text": "heart failure", "type": "Disease"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}]}

Example input:
Sentence: Patients who developed renal insufficiency had lower baseline body weight and higher baseline serum creatinine , required higher doses of loop diuretics , and were more likely to be treated with thiazide diuretics than controls .

Example answer:
{"entities": [{"text": "renal insufficiency", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "thiazide", "type": "Chemical"}]}

Input:
Sentence: heart failure , yet are unnecessary for renal dysfunction , adult age , sex , race/ethnicity or obesity .

## Item bc5cdr:test:3518
Example input:
Sentence: Nine patients with severe pain in their feet , which was registered after transplantation , were investigated .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}]}

Example input:
Sentence: Four patients who were rendered comatose or stuporous by drug intoxication , but who were not hypoxic , are described .

Example answer:
{"entities": [{"text": "comatose", "type": "Disease"}, {"text": "stuporous", "type": "Disease"}]}

Example input:
Sentence: Calcineurin-inhibitor induced pain syndrome ( CIPS ) : a severe disabling complication after organ transplantation .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "CIPS", "type": "Disease"}]}

Example input:
Sentence: She subsequently died some 5 weeks after the commencement of her drug therapy.Post-mortem examination showed evidence of massive hepatocellular necrosis , acute hypersensitivity myocarditis , focal acute tubulo-interstitial nephritis and extensive bone marrow necrosis , with no evidence of malignancy .

Example answer:
{"entities": [{"text": "massive hepatocellular necrosis", "type": "Disease"}, {"text": "myocarditis", "type": "Disease"}, {"text": "nephritis", "type": "Disease"}, {"text": "bone marrow necrosis", "type": "Disease"}, {"text": "malignancy", "type": "Disease"}]}

Example input:
Sentence: Three yr after transplantation she developed renal Fanconi syndrome with severe metabolic acidosis , hypophosphatemia , glycosuria , and aminoaciduria .

Example answer:
{"entities": [{"text": "renal Fanconi syndrome", "type": "Disease"}, {"text": "metabolic acidosis", "type": "Disease"}, {"text": "hypophosphatemia", "type": "Disease"}, {"text": "glycosuria", "type": "Disease"}, {"text": "aminoaciduria", "type": "Disease"}]}

Example input:
Sentence: Over the long-term chronic phase ( 120 days after transplantation ) , only 25 % of BMC-treated epileptic animals had seizures , but with a lower frequency and duration compared to the epileptic control group .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Our objective was to investigate brain MR imaging findings and the utility of diffusion-weighted ( DW ) imaging in organ transplant patients who developed neurologic symptoms during tacrolimus therapy .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}]}

Example input:
Sentence: She underwent liver transplantation with an uneventful postoperative course .

Example answer:
{"entities": []}

Example input:
Sentence: The time from transplant to baseline was similar in all patients .

Example answer:
{"entities": []}

Example input:
Sentence: Twenty-three hours after heart transplantation , life-threatening acute right heart failure was diagnosed in a patient requiring continuous venovenous hemodiafiltration ( CVVHDF ) .

Example answer:
{"entities": [{"text": "right heart failure", "type": "Disease"}]}

Input:
Sentence: After an initially uneventful course after the transplant , the patient rapidly fell into deep coma .

## Item bc5cdr:test:3170
Example input:
Sentence: PURPOSE : The influence of an irreversible inhibitor of constitutive NO synthase ( L-NOArg ; 1.0 mg/kg ip ) , a relatively selective inhibitor of inducible NO synthase ( L-NIL ; 1.0 mg/kg ip ) and a relatively specific inhibitor of neuronal NO synthase ( 7-NI ; 0.1 mg/kg ip ) , on antihyperalgesic action of selective antagonists of B2 and B1 receptors : D-Arg- [ Hyp3 , Thi5 , D-Tic7 , Oic8 ] bradykinin ( HOE 140 ; 70 nmol/kg ip ) or des Arg10 HOE 140 ( 70 nmol/kg ip ) respectively , in model of diabetic ( streptozotocin-induced ) and toxic ( vincristine-induced ) neuropathy was investigated .

Example answer:
{"entities": [{"text": "NO", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}, {"text": "HOE 140", "type": "Chemical"}, {"text": "des Arg10 HOE 140", "type": "Chemical"}]}

Example input:
Sentence: In all the experiments , the attenuation of the lithium-induced diabetes-insipidus-like syndrome by amiloride was accompanied by a reduction of the ratio between the lithium concentration in the renal medulla and its levels in the blood and an elevation in the plasma potassium level .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "Chemical"}, {"text": "diabetes-insipidus-like syndrome", "type": "Disease"}, {"text": "amiloride", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}]}

Example input:
Sentence: Lithium also caused proteinuria and systolic hypertension in absence of glomerulosclerosis .

Example answer:
{"entities": [{"text": "Lithium", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: Attenuation of the lithium-induced diabetes-insipidus-like syndrome by amiloride in rats .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "Chemical"}, {"text": "diabetes-insipidus-like syndrome", "type": "Disease"}, {"text": "amiloride", "type": "Chemical"}]}

Example input:
Sentence: Less frequent lithium administration and lower urine volume .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: FINDINGS : A 28-year-old man suffering from idiopathic epilepsy with generalized seizures was treated with LEV ( 3000 mg ) added to valproate ( VPA ) ( 2000 mg ) .

Example answer:
{"entities": [{"text": "idiopathic epilepsy", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "LEV", "type": "Chemical"}, {"text": "valproate", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}]}

Example input:
Sentence: The effect of amiloride on lithium-induced polydipsia and polyuria and on the lithium concentration in the plasma , brain , kidney , thyroid and red blood cells was investigated in rats , chronically treated with LiCl .

Example answer:
{"entities": [{"text": "amiloride", "type": "Chemical"}, {"text": "lithium-induced", "type": "Chemical"}, {"text": "polydipsia", "type": "Disease"}, {"text": "polyuria", "type": "Disease"}, {"text": "lithium", "type": "Chemical"}, {"text": "LiCl", "type": "Chemical"}]}

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

Input:
Sentence: Lithium inhibits IMPase and valproate inhibits MIP synthase .

## Item bc5cdr:test:3007
Example input:
Sentence: Risk in the raloxifene group was higher than in the placebo group for the first 2 years , but decreased to about the same rate as in the placebo group thereafter .

Example answer:
{"entities": [{"text": "raloxifene", "type": "Chemical"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: These studies suggest that both phenacetin and acetaminophen may contribute to the burden of ESRD , with the risk of the latter being somewhat less than that of the former .

Example answer:
{"entities": [{"text": "phenacetin", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Extrapyramidal symptoms reported as AEs occurred in 15 % and 18 % , 34 % , and 10 % of the asenapine at 5 and 10 mg BID , haloperidol , and placebo groups , respectively .

Example answer:
{"entities": [{"text": "Extrapyramidal symptoms", "type": "Disease"}, {"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Women were randomly assigned to raloxifene 60 mg/d or 120 mg/d or placebo .

Example answer:
{"entities": [{"text": "raloxifene", "type": "Chemical"}]}

Example input:
Sentence: However , three case control studies , one each in North Carolina , northern Maryland , and West Berlin , Germany , showed that habitual use of acetaminophen is also associated with chronic renal failure and ESRD , with a relative risk in the range of 2 to 4 .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "chronic renal failure", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Pooled data from trials comparing antithrombotic treatment with placebo have shown that warfarin reduces the risk of stroke by 62 % , and that aspirin alone reduces the risk by 22 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "stroke", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: Overall , in high-risk patients , warfarin is superior to aspirin in preventing strokes , with a relative risk reduction of 36 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "strokes", "type": "Disease"}]}

Example input:
Sentence: A patient who allegedly consumed 100 tablets of an over-the-counter analgesic containing sodium acetylsalicylate , caffeine , and acetaminophen displayed no significant CNS stimulation despite the presence of 175 micrograms of caffeine per mL of serum .

Example answer:
{"entities": [{"text": "sodium acetylsalicylate", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}]}

Example input:
Sentence: Treatment-related adverse events ( AEs ) occurred in 44 % and 52 % , 57 % , and 41 % of the asenapine at 5 and 10 mg BID , haloperidol , and placebo groups , respectively .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Input:
Sentence: Among users of aspirin , they were : 14,671 to rofecoxib , 22,875 to celecoxib , 9,832 to NS-NSAIDs and 38,048 to acetaminophen .

## Item bc5cdr:test:3514
Example input:
Sentence: Our objective was to investigate brain MR imaging findings and the utility of diffusion-weighted ( DW ) imaging in organ transplant patients who developed neurologic symptoms during tacrolimus therapy .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}]}

Example input:
Sentence: Brain MR studies , including DW imaging , were prospectively performed in 14 organ transplant patients receiving tacrolimus who developed neurologic complications .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "neurologic complications", "type": "Disease"}]}

Example input:
Sentence: We describe a 15-yr-old girl who had orthotopic liver transplantation because of Wilson 's disease .

Example answer:
{"entities": [{"text": "Wilson 's disease", "type": "Disease"}]}

Example input:
Sentence: CNS complications included posterior reversible leukoencephalopathy syndrome ( n = 10 ) , stroke ( n = 5 ) , temporal lobe epilepsy ( n = 2 ) , high-dose methotrexate toxicity ( n = 2 ) , syndrome of inappropriate antidiuretic hormone secretion ( n = 1 ) , and other unclassified events ( n = 7 ) .

Example answer:
{"entities": [{"text": "leukoencephalopathy", "type": "Disease"}, {"text": "stroke", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "inappropriate antidiuretic hormone secretion", "type": "Disease"}]}

Example input:
Sentence: Calcineurin-inhibitor induced pain syndrome ( CIPS ) : a severe disabling complication after organ transplantation .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "CIPS", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Reversible inferior colliculus lesions could be considered as the characteristic for metronidazole-induced encephalopathy , next to the dentate nucleus involvement .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "Disease"}, {"text": "metronidazole-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Renal Fanconi syndrome and myopathy after liver transplantation : drug-related mitochondrial cytopathy ?

Example answer:
{"entities": [{"text": "Renal Fanconi syndrome", "type": "Disease"}, {"text": "myopathy", "type": "Disease"}, {"text": "mitochondrial cytopathy", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVE : This is to present reversible inferior colliculus lesions in metronidazole-induced encephalopathy , to focus on the diffusion-weighted imaging ( DWI ) and fluid attenuated inversion recovery ( FLAIR ) imaging .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "Disease"}, {"text": "metronidazole-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: End-stage renal disease ( ESRD ) after orthotopic liver transplantation ( OLTX ) using calcineurin-based immunotherapy : risk of development and treatment .

Example answer:
{"entities": [{"text": "End-stage renal disease", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Reversible inferior colliculus lesion in metronidazole-induced encephalopathy : magnetic resonance findings on diffusion-weighted and fluid attenuated inversion recovery imaging .

Example answer:
{"entities": [{"text": "inferior colliculus lesion", "type": "Disease"}, {"text": "metronidazole-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Input:
Sentence: Late fulminant posterior reversible encephalopathy syndrome after liver transplant .

## Item bc5cdr:test:3553
Example input:
Sentence: A 45-year-old man , an admitted frequent cocaine user , presented to the Emergency Department ( ED ) on two separate occasions with a history of priapism after cocaine use .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "priapism", "type": "Disease"}]}

Example input:
Sentence: GR 55562 ( 0.1-10 microg/side ) , administered intra-accumbens shell prior to cocaine , dose-dependently attenuated the psychostimulant-induced locomotor hyperactivity .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}, {"text": "locomotor hyperactivity", "type": "Disease"}]}

Example input:
Sentence: This group was compared with a control group of 135 patients with ruptured aneurysms and no history of cocaine abuse .

Example answer:
{"entities": [{"text": "ruptured aneurysms", "type": "Disease"}, {"text": "cocaine abuse", "type": "Disease"}]}

Example input:
Sentence: Patients ' mean age was 53.9 years , their mean weight was 193.9 pounds , and they smoked a mean of 25.2 cigarettes per day at baseline .

Example answer:
{"entities": []}

Example input:
Sentence: Cocaine was injected ip over a range of doses ( 50-100 mg/kg ) and behavior was monitored for 20 minutes .

Example answer:
{"entities": [{"text": "Cocaine", "type": "Chemical"}]}

Example input:
Sentence: When injected into the accumbens shell ( but not the core ) before cocaine , CP 93129 ( 0.1-10 microg/side ) enhanced the locomotor response to cocaine ; the maximum effect being observed after 10 microg/side of the agonist .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Example input:
Sentence: Eleven of the cocaine abusers and none of the controls had ECG evidence of significant myocardial injury defined as myocardial infarction , ischemia , and bundle branch block .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "myocardial injury", "type": "Disease"}, {"text": "myocardial infarction", "type": "Disease"}, {"text": "ischemia", "type": "Disease"}, {"text": "bundle branch block", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Progressive abstinence from cocaine was associated with worsening of all measured polysomnographic sleep outcomes .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: METHOD : Twenty cocaine-dependent participants were randomly assigned to receive modafinil , 400 mg ( N=10 ) , or placebo ( N=10 ) every morning at 7:30 a.m. for 16 days in an inpatient , double-blind randomized trial .

Example answer:
{"entities": [{"text": "cocaine-dependent", "type": "Chemical"}, {"text": "modafinil", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Sub-chronic GVG exposure inhibited the effect of cocaine for 3 days , which exceeded in magnitude and duration the identical acute dose .

Example answer:
{"entities": [{"text": "GVG", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}]}

Input:
Sentence: The mean proportion of participants who reported daily smoking of crack cocaine increased from 11.6 % in period 1 to 39.7 % in period 3 .

## Item bc5cdr:test:3353
Example input:
Sentence: Effects of uninephrectomy and high protein feeding on lithium-induced chronic renal failure in rats .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "Chemical"}, {"text": "chronic renal failure", "type": "Disease"}]}

Example input:
Sentence: Lithium-associated cognitive and functional deficits reduced by a switch to divalproex sodium : a case series .

Example answer:
{"entities": [{"text": "Lithium-associated", "type": "Chemical"}, {"text": "cognitive and functional deficits", "type": "Disease"}, {"text": "divalproex sodium", "type": "Chemical"}]}

Example input:
Sentence: The effect of amiloride on lithium-induced polydipsia and polyuria and on the lithium concentration in the plasma , brain , kidney , thyroid and red blood cells was investigated in rats , chronically treated with LiCl .

Example answer:
{"entities": [{"text": "amiloride", "type": "Chemical"}, {"text": "lithium-induced", "type": "Chemical"}, {"text": "polydipsia", "type": "Disease"}, {"text": "polyuria", "type": "Disease"}, {"text": "lithium", "type": "Chemical"}, {"text": "LiCl", "type": "Chemical"}]}

Example input:
Sentence: In all the experiments , the attenuation of the lithium-induced diabetes-insipidus-like syndrome by amiloride was accompanied by a reduction of the ratio between the lithium concentration in the renal medulla and its levels in the blood and an elevation in the plasma potassium level .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "Chemical"}, {"text": "diabetes-insipidus-like syndrome", "type": "Disease"}, {"text": "amiloride", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}]}

Example input:
Sentence: HP failed to accentuante progression of renal failure and in fact tended to increase GFR and decrease plasma creatinine levels in lithium pretreated rats .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: After 3 days of combined treatment , a marked elevation in plasma and tissue lithium levels accompanied a reduction in water intake .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: Lithium-induced polyuria seems to be related to extrarenal as well as to renal effects .

Example answer:
{"entities": [{"text": "Lithium-induced", "type": "Chemical"}, {"text": "polyuria", "type": "Disease"}]}

Example input:
Sentence: It is concluded that acute amiloride administration to lithium-treated patients suffering from polydipsia and polyuria might relieve these patients but prolonged amiloride supplementation would result in elevated lithium levels and might be hazardous .

Example answer:
{"entities": [{"text": "amiloride", "type": "Chemical"}, {"text": "lithium-treated", "type": "Chemical"}, {"text": "polydipsia", "type": "Disease"}, {"text": "polyuria", "type": "Disease"}, {"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: Lithium also caused proteinuria and systolic hypertension in absence of glomerulosclerosis .

Example answer:
{"entities": [{"text": "Lithium", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: Rats with lithium-induced nephropathy were subjected to high protein ( HP ) feeding , uninephrectomy ( NX ) or a combination of these , in an attempt to induce glomerular hyperfiltration and further progression of renal failure .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Input:
Sentence: Long-term lithium therapy leading to hyperparathyroidism : a case report .

## Item bc5cdr:test:3205
Example input:
Sentence: Twenty patients were asked to quantify the severity of pain after receiving standard lidocaine in one femoral area and buffered lidocaine in the opposite femoral area .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Nine of 30 patients receiving lidocaine experienced TNSs , 1 of 30 patients receiving prilocaine ( P = 0.03 ) had them , and none of 30 patients receiving bupivacaine had TNSs .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "TNSs", "type": "Disease"}, {"text": "prilocaine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: Differential effects of systemically administered ketamine and lidocaine on dynamic and static hyperalgesia induced by intradermal capsaicin in humans .

Example answer:
{"entities": [{"text": "ketamine", "type": "Chemical"}, {"text": "lidocaine", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: Effects of calcium channel blockers on bupivacaine-induced toxicity .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "bupivacaine-induced", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: The differential effects of ketamine and lidocaine on static and dynamic hyperalgesia suggest that the two types of hyperalgesia are mediated by separate mechanisms and have a distinct pharmacology .

Example answer:
{"entities": [{"text": "ketamine", "type": "Chemical"}, {"text": "lidocaine", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}]}

Example input:
Sentence: We conclude that lidocaine reduces the incidence and severity of propofol injection pain in ambulatory patients whereas thiopentone only reduces its severity .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "propofol", "type": "Chemical"}, {"text": "pain", "type": "Disease"}, {"text": "thiopentone", "type": "Chemical"}]}

Example input:
Sentence: The purpose of this study was to investigate the influence of calcium channel blockers on bupivacaine-induced acute toxicity .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "bupivacaine-induced", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: The mean pain score for buffered lidocaine was significantly lower than the mean score for standard lidocaine ( 2.7 +/- 1.9 vs. 3.8 +/- 2.2 , P = 0.03 ) .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: We have examined the effect of systemic administration of ketamine and lidocaine on brush-evoked ( dynamic ) pain and punctate-evoked ( static ) hyperalgesia induced by capsaicin .

Example answer:
{"entities": [{"text": "ketamine", "type": "Chemical"}, {"text": "lidocaine", "type": "Chemical"}, {"text": "pain", "type": "Disease"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: Lidocaine reduced the area of punctate-evoked hyperalgesia significantly .

Example answer:
{"entities": [{"text": "Lidocaine", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}]}

Input:
Sentence: The differential effects of bupivacaine and lidocaine on prostaglandin E2 release , cyclooxygenase gene expression and pain in a clinical pain model .

## Item bc5cdr:test:3590
Example input:
Sentence: In salt-depleted rats , amphotericin B decreased creatinine clearance linearly with time , with an 85 % reduction by week 3 .

Example answer:
{"entities": [{"text": "amphotericin B", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: The aim of this study was to examine further the renal function , including morphological analysis of the kidneys of male Sprague-Dawley rats treated with either cyclosporine A ( CsA ) , tacrolimus ( FK506 ) or SRL as monotherapies or in different combinations .

Example answer:
{"entities": [{"text": "cyclosporine A", "type": "Chemical"}, {"text": "CsA", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: The relative amounts of alphaENaC , betaENaC and gammaENaC mRNAs were determined in kidneys from these rats by real-time quantitative TaqMan PCR , and the amounts of proteins by Western blot .

Example answer:
{"entities": []}

Example input:
Sentence: Using puromycin aminonucleoside nephrosis ( PAN ) rats , we studied early ultrastructural and permeability changes in relation to the expression of the podocyte-associated molecules nephrin , a-actinin , dendrin , and plekhh2 , the last two of which were only recently discovered in podocytes .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: In the present work we assessed the effect of treatment of rats with gum Arabic on acute renal failure induced by gentamicin ( GM ) nephrotoxicity .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}]}

Example input:
Sentence: In this study , 62 patients with confirmed initial normal renal function and treated with 2 to 5 mg/kg/day of gentamicin sulfate or tobramycin sulfate for a minimum of seven days were followed up prospectively for the development of aminoglycoside-related renal failure , defined as at least a one-third reduction in renal function .

Example answer:
{"entities": [{"text": "gentamicin sulfate", "type": "Chemical"}, {"text": "tobramycin sulfate", "type": "Chemical"}, {"text": "aminoglycoside-related", "type": "Chemical"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: Epithelial sodium channel ( ENaC ) subunit mRNA and protein expression in rats with puromycin aminonucleoside-induced nephrotic syndrome .

Example answer:
{"entities": [{"text": "sodium", "type": "Chemical"}, {"text": "puromycin", "type": "Chemical"}, {"text": "nephrotic syndrome", "type": "Disease"}]}

Example input:
Sentence: Thus , gentamicin was associated with renal failure more than three times as often as was tobramycin .

Example answer:
{"entities": [{"text": "gentamicin", "type": "Chemical"}, {"text": "renal failure", "type": "Disease"}, {"text": "tobramycin", "type": "Chemical"}]}

Example input:
Sentence: Histologic changes were found in rat kidneys after administration of MTX , CY and NG , while no such change was observed after 5-FU and joint administration of MTX + 5-FU + CY compared to controls .

Example answer:
{"entities": [{"text": "MTX", "type": "Chemical"}, {"text": "CY", "type": "Chemical"}, {"text": "NG", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Input:
Sentence: Immunoblotting and immunohistochemistry revealed decreased expression of Na ( + ) /K ( + ) -ATPase , NHE3 , NBC1 , and AQP1 in the kidney of gentamicin-treated rats .

## Item bc5cdr:test:3604
Example input:
Sentence: Depressed mood was more common among patients and was associated with certain sexual difficulties , but not with impotence .

Example answer:
{"entities": [{"text": "Depressed mood", "type": "Disease"}, {"text": "impotence", "type": "Disease"}]}

Example input:
Sentence: Patients scoring > or =20 MMSE sum points were interviewed ( n = 79 ) and questioned regarding symptoms and functional abilities during the week prior to admission .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : Retrospective review of medical records of 236 patients with hyperthyroidism admitted in our department ( in- or out-patients ) from 1986 to 1992 .

Example answer:
{"entities": [{"text": "hyperthyroidism", "type": "Disease"}]}

Example input:
Sentence: Introduction of the DSM-IV diagnosis of CIMD did not substantially affect rates of the other depressive disorders .

Example answer:
{"entities": [{"text": "CIMD", "type": "Disease"}, {"text": "depressive disorders", "type": "Disease"}]}

Example input:
Sentence: Patient response was assessed using changes in CD4+ lymphocyte subset count , HIV p24 antigen , weight , and quality of life .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : We used computerized pharmacy records to identify all adult psychiatric inpatients treated with clozapine ( 1995-96 ) , reviewed their medical records to score incidence and severity of delirium , and tested associations with potential risk factors .

Example answer:
{"entities": [{"text": "psychiatric", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "delirium", "type": "Disease"}]}

Example input:
Sentence: Of 24 evaluable patients , two achieved a complete remission and one achieved a partial remission for an overall response rate of 12.5 % ( 95 % confidence interval : 2.6-32.4 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Eighty-nine new referral hypertensive out-patients and 46 new referral non-hypertensive chronically physically ill out-patients completed a mood rating scale at regular intervals for one year .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}]}

Example input:
Sentence: METHOD : The response of 44 patients meeting DSM-IV criteria for bipolar disorder to naturalistic treatment was assessed for at least 6 weeks using the Montgomery-Asberg Depression Rating Scale and the Bech-Rafaelson Mania Rating Scale .

Example answer:
{"entities": [{"text": "bipolar disorder", "type": "Disease"}]}

Example input:
Sentence: During the six-month follow up , depression was quantified through the Beck and Zung-Conde scales every two months .

Example answer:
{"entities": [{"text": "depression", "type": "Disease"}]}

Input:
Sentence: The participants had physical examination , medical record extraction , and venipuncture , CD4+T-cell counts determination , measurement of depression symptoms ( using the self-report Center for Epidemiological Studies-Depression Scale ) , and alcohol use assessment at enrollment , and semiannually until March 2000 .

## Item bc5cdr:test:3597
Example input:
Sentence: Adverse cardiac effects during induction chemotherapy treatment with cis-platin and 5-fluorouracil .

Example answer:
{"entities": [{"text": "cis-platin", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}]}

Example input:
Sentence: The animal model used to produce infarction implies artery ligation but chemical induction can be easily obtained with isoproterenol .

Example answer:
{"entities": [{"text": "infarction", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: Following major intracranial surgery in a 35-year-old man , sodium pentothal was intravenously infused to minimize cerebral ischaemia .

Example answer:
{"entities": [{"text": "sodium pentothal", "type": "Chemical"}, {"text": "cerebral ischaemia", "type": "Disease"}]}

Example input:
Sentence: In the singleton pregnancy , the mother had ulcerative colitis , and the infant , a male , had coarctation of the aorta and a ventricular septal defect .

Example answer:
{"entities": [{"text": "ulcerative colitis", "type": "Disease"}, {"text": "coarctation of the aorta", "type": "Disease"}, {"text": "ventricular septal defect", "type": "Disease"}]}

Example input:
Sentence: In ICH induction using 0.014-unit collagenase , heparin enhanced the hematoma volume 3.4-fold over that seen in control ICH animals and the bleeding 7.6-fold .

Example answer:
{"entities": [{"text": "ICH", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}, {"text": "hematoma", "type": "Disease"}, {"text": "bleeding", "type": "Disease"}]}

Example input:
Sentence: Three infants , born of two mothers with inflammatory bowel disease who received treatment with sulphasalazine throughout pregnancy , were found to have major congenital anomalies .

Example answer:
{"entities": [{"text": "inflammatory bowel disease", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "congenital anomalies", "type": "Disease"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: We report an undiagnosed case of myotonia congenita in a 24-year-old previously healthy primigravida , who developed life threatening masseter spasm following a standard dose of intravenous suxamethonium for induction of anaesthesia .

Example answer:
{"entities": [{"text": "myotonia congenita", "type": "Disease"}, {"text": "masseter spasm", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: A high percentage of kanamycin-colistin and povidone-iodine irrigations were associated with erosive cystitis and suggested a possible complication with human usage .

Example answer:
{"entities": [{"text": "kanamycin-colistin", "type": "Chemical"}, {"text": "povidone-iodine", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Example input:
Sentence: Anaesthetists ' nightmare : masseter spasm after induction in an undiagnosed case of myotonia congenita .

Example answer:
{"entities": [{"text": "masseter spasm", "type": "Disease"}, {"text": "myotonia congenita", "type": "Disease"}]}

Input:
Sentence: During induction therapy , he suffered ileal perforation and ileostomy was performed .

## Item bc5cdr:test:3403
Example input:
Sentence: In vitro , gamma-HCH , pentylenetetrazol and picrotoxin were shown to inhibit 3H-TBOB binding in mouse whole brain , with IC50 values of 4.6 , 404 and 9.4 microM , respectively .

Example answer:
{"entities": [{"text": "gamma-HCH", "type": "Chemical"}, {"text": "pentylenetetrazol", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "3H-TBOB", "type": "Chemical"}]}

Example input:
Sentence: Forty-nine percent of patients were pain free 2 h after rizatriptan , compared with 24.3 % treated with ergotamine/caffeine ( p < or = 0.001 ) , rizatriptan being superior within 1 h of treatment .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}]}

Example input:
Sentence: This randomized double- blind crossover outpatient study assessed the preference for 1 rizatriptan 10 mg tablet to 2 ergotamine 1 mg/caffeine 100 mg tablets in 439 patients treating a single migraine attack with each therapy .

Example answer:
{"entities": [{"text": "rizatriptan", "type": "Chemical"}, {"text": "ergotamine", "type": "Chemical"}, {"text": "migraine", "type": "Disease"}]}

Example input:
Sentence: Faster relief of headache was the most important reason for preference , cited by 67.3 % of patients preferring rizatriptan and 54.2 % of patients who preferred ergotamine/caffeine .

Example answer:
{"entities": [{"text": "headache", "type": "Disease"}, {"text": "rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Correlation of plasma argatroban concentration versus the patient 's coagulation variables and clinical course suggest that prolonged elevated levels of plasma argatroban may have contributed to the patient 's extended coagulopathy .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "coagulopathy", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Unexpectedly high concentrations of argatroban were measured in these samples ( range , 0-32 microg/mL ) , and a prolonged plasma argatroban half life ( t ( 1/2 ) ) of 514 minutes was observed ( published elimination t ( 1/2 ) is 39-51 minutes [ < or = 181 minutes with hepatic impairment ] ) .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "hepatic impairment", "type": "Disease"}]}

Example input:
Sentence: STUDY DESIGN AND METHODS : Plasma samples from before and after CPB were analyzed postoperatively for argatroban concentration using a modified ecarin clotting time ( ECT ) assay .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}]}

Example input:
Sentence: Prolonged elevation of plasma argatroban in a cardiac transplant patient with a suspected history of heparin-induced thrombocytopenia with thrombosis .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: This is the first report to measure plasma argatroban concentration in the context of CPB and extended coagulopathy .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "coagulopathy", "type": "Disease"}]}

Example input:
Sentence: In the following report , a 65-year-old critically ill patient with a suspected history of HITT was administered argatroban for anticoagulation on bypass during heart transplantation .

Example answer:
{"entities": [{"text": "critically ill", "type": "Disease"}, {"text": "HITT", "type": "Disease"}, {"text": "argatroban", "type": "Chemical"}]}

Input:
Sentence: The objective of this review is to summarize practical considerations of argatroban therapy in HIT .

## Item bc5cdr:test:3451
Example input:
Sentence: Haematological toxicity was greater for the combination than AraG alone , although median time to neutrophil and platelet recovery was consistent with other salvage therapies .

Example answer:
{"entities": [{"text": "Haematological toxicity", "type": "Disease"}, {"text": "AraG", "type": "Chemical"}]}

Example input:
Sentence: These 6 patients had both renal and liver dysfunction ( P less than 0.05 ) , as well as cimetidine trough-concentrations of more than 1.25 microgram/ml ( P less than 0.05 ) .

Example answer:
{"entities": [{"text": "cimetidine", "type": "Chemical"}]}

Example input:
Sentence: regular consumption of alcohol , liver failure is possible when therapeutic doses are ingested .

Example answer:
{"entities": [{"text": "alcohol", "type": "Chemical"}, {"text": "liver failure", "type": "Disease"}]}

Example input:
Sentence: Diagnosis of this potentially fatal complication may be delayed or missed if renal tissue or the peripheral blood smear is not examined , because renal failure may be ascribed to cisplatin nephrotoxicity and the anemia and thrombocytopenia to drug-induced bone marrow suppression .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "bone marrow suppression", "type": "Disease"}]}

Example input:
Sentence: We report a case of severe citrate toxicity during volunteer donor apheresis platelet collection .

Example answer:
{"entities": [{"text": "citrate", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Simvastatinezetimibe and escitalopram ( which she was taking for depression ) were discontinued , and other potential causes of hepatotoxicity were excluded .

Example answer:
{"entities": [{"text": "Simvastatinezetimibe", "type": "Chemical"}, {"text": "escitalopram", "type": "Chemical"}, {"text": "depression", "type": "Disease"}, {"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: We conclude that careful screening for medications and underlying conditions predisposing to hypocalcemia is recommended to help prevent severe reactions due to citrate toxicity .

Example answer:
{"entities": [{"text": "hypocalcemia", "type": "Disease"}, {"text": "citrate", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: The yield of severe cirrhosis of the liver ( defined as a shrunken finely nodular liver with micronodular histology , ascites greater than 30 ml , plasma albumin less than 2.2 g/dl , splenomegaly 2-3 times normal , and testicular atrophy approximately half normal weight ) after 12 doses of carbon tetrachloride given intragastrically in the phenobarbitone-primed rat was increased from 25 % to 56 % by giving the initial `` calibrating '' dose of carbon tetrachloride at the peak of the phenobarbitone-induced enlargement of the liver .

Example answer:
{"entities": [{"text": "cirrhosis of the liver", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "splenomegaly", "type": "Disease"}, {"text": "atrophy", "type": "Disease"}, {"text": "carbon tetrachloride", "type": "Chemical"}, {"text": "phenobarbitone-primed", "type": "Chemical"}, {"text": "phenobarbitone-induced", "type": "Chemical"}, {"text": "enlargement of the liver", "type": "Disease"}]}

Example input:
Sentence: The events are consistent with a severe reaction to calcium chelation by sodium citrate anticoagulant resulting in symptomatic systemic hypocalcemia .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "sodium citrate", "type": "Chemical"}, {"text": "hypocalcemia", "type": "Disease"}]}

Example input:
Sentence: Severe citrate toxicity complicating volunteer apheresis platelet donation .

Example answer:
{"entities": [{"text": "citrate", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Input:
Sentence: Systemic anticoagulation is unsafe and regional citrate anticoagulation in the absence of a functional liver carries the risk of citrate toxicity .

## Item bc5cdr:test:3549
Example input:
Sentence: She had no previous beta-blocking drug exposure .

Example answer:
{"entities": []}

Example input:
Sentence: There was no serologic evidence of viral infection , and a liver biopsy sample showed a histologic pattern consistent with drug-induced hepatitis .

Example answer:
{"entities": [{"text": "viral infection", "type": "Disease"}, {"text": "drug-induced hepatitis", "type": "Disease"}]}

Example input:
Sentence: Patient response was assessed using changes in CD4+ lymphocyte subset count , HIV p24 antigen , weight , and quality of life .

Example answer:
{"entities": []}

Example input:
Sentence: During an 18-month period of study 41 hemodialyzed patients receiving desferrioxamine ( 10-40 mg/kg BW/3 times weekly ) for the first time were monitored for detection of audiovisual toxicity .

Example answer:
{"entities": [{"text": "desferrioxamine", "type": "Chemical"}, {"text": "audiovisual toxicity", "type": "Disease"}]}

Example input:
Sentence: METHODS : We conducted a prospective , randomized , double-blind study in the emergency department of a central-city teaching hospital .

Example answer:
{"entities": []}

Example input:
Sentence: Data from a Transnational case-control study were used to assess the risk of VTE for the latter patterns of use , while accounting for duration of use .

Example answer:
{"entities": [{"text": "VTE", "type": "Disease"}]}

Example input:
Sentence: It remains to be seen whether such pre-existing antiviral mutations could result in widespread emergence of HBV resistant strains when lamivudine-containing highly active antiretroviral ( ARV ) treatment ( HAART ) regimens become widely applied in South Africa , as this is likely to have potential implications in the management of HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "lamivudine-containing", "type": "Chemical"}]}

Example input:
Sentence: Fifteen polydrug ecstasy users and 15 polydrug non-ecstasy user controls completed a general drug use questionnaire , the Brixton Spatial Anticipation task ( set shifting ) , Backward Digit Span procedure ( memory updating ) , Inhibition of Return ( inhibition ) , an emotional intelligence scale , the Tromso Social Intelligence Scale and the Dysexecutive Questionnaire ( DEX ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: The epidemiological studies that assessed the risk of venous thromboembolism ( VTE ) associated with newer oral contraceptives ( OC ) did not distinguish between patterns of OC use , namely first-time users , repeaters and switchers .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "VTE", "type": "Disease"}, {"text": "oral contraceptives", "type": "Chemical"}, {"text": "OC", "type": "Chemical"}]}

Example input:
Sentence: This was an exploratory study to investigate lamivudine-resistant hepatitis B virus ( HBV ) strains in selected lamivudine-na ve HBV carriers with and without human immunodeficiency virus ( HIV ) co-infection in South African patients .

Example answer:
{"entities": [{"text": "lamivudine-resistant", "type": "Chemical"}, {"text": "hepatitis B", "type": "Disease"}, {"text": "lamivudine-na", "type": "Chemical"}, {"text": "human immunodeficiency virus ( HIV ) co-infection", "type": "Disease"}]}

Input:
Sentence: METHODS : We included data from people participating in the Vancouver Injection Drug Users Study who reported injecting illicit drugs at least once in the month before enrolment , lived in the greater Vancouver area , were HIV-negative at enrolment and completed at least 1 follow-up study visit .

## Item bc5cdr:test:3630
Example input:
Sentence: Seizure activity due to PTZ and picrotoxin ( PTX ) was significantly decreased ; however , seizure activity due to 3-mercaptopropionic acid ( MPA ) , bicuculline ( BCC ) , methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate ( DMCM ) , or strychnine ( STR ) was not different from control .

Example answer:
{"entities": [{"text": "Seizure", "type": "Disease"}, {"text": "PTZ", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "PTX", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "3-mercaptopropionic acid", "type": "Chemical"}, {"text": "MPA", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "BCC", "type": "Chemical"}, {"text": "methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate", "type": "Chemical"}, {"text": "DMCM", "type": "Chemical"}, {"text": "strychnine", "type": "Chemical"}, {"text": "STR", "type": "Chemical"}]}

Example input:
Sentence: Our findings indicate that beta2-adrenoceptor overstimulation during an early critical period results in microglial activation associated with innate neuroinflammatory pathways and behavioral abnormalities , similar to those described in autism .

Example answer:
{"entities": [{"text": "behavioral abnormalities", "type": "Disease"}, {"text": "autism", "type": "Disease"}]}

Example input:
Sentence: The alpha3 and beta4 nicotinic acetylcholine receptor subunits are necessary for nicotine-induced seizures and hypolocomotion in mice .

Example answer:
{"entities": [{"text": "acetylcholine", "type": "Chemical"}, {"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "hypolocomotion", "type": "Disease"}]}

Example input:
Sentence: QTLs for susceptibility to pilocarpine-induced seizures , a model of temporal lobe epilepsy , have not been reported , and CSS have not previously been used to localize seizure susceptibility genes .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: These data support the hypothesis that SE-induced mossy fiber sprouting and synaptic reorganization are relevant characteristics of seizure development in these murine strains , resembling rat models of human temporal lobe epilepsy .

Example answer:
{"entities": [{"text": "SE-induced", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}]}

Example input:
Sentence: A comparable overexpression of Pgp in the BBB was obtained after pilocarpine-induced seizures in wild-type Wistar rats .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: The in vitro data suggest that the site responsible for the decrease in seizure activity 24 h after gamma-HCH may be the GABA-A receptor-linked chloride channel .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}, {"text": "GABA-A", "type": "Chemical"}]}

Example input:
Sentence: In this study , we investigated whether increased generation of FR during status epilepticus would be sufficient to provoke abnormalities in mtDNA and in the expression and activity of cytochrome c oxidase ( CCO ) , complex IV of the respiratory chain , in the chronic phase of the pilocarpine model of temporal lobe epilepsy .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}, {"text": "temporal lobe epilepsy", "type": "Disease"}]}

Example input:
Sentence: Upregulation of brain expression of P-glycoprotein in MRP2-deficient TR ( - ) rats resembles seizure-induced up-regulation of this drug efflux transporter in normal rats .

Example answer:
{"entities": [{"text": "seizure-induced", "type": "Disease"}]}

Example input:
Sentence: These data might indicate that the generation of reactive oxygen species and activation of NF-kappaB plays a more central role in seizure-associated neuronal damage in the temporal cortex as compared to the hippocampal hilus .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "seizure-associated", "type": "Disease"}, {"text": "neuronal damage", "type": "Disease"}]}

Input:
Sentence: Seizures also result in changes to CCR2 receptor expression in neurons and astrocytes .

## Item bc5cdr:test:3561
Example input:
Sentence: In addition , working memory processing in ecstasy users has been shown to be associated with neural alterations in hippocampal and/or cortical regions as measured by functional magnetic resonance imaging ( fMRI ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: The typical fluoxetine-induced symptoms of restlessness , constant pacing , purposeless movements of the feet and legs , and marked anxiety were indistinguishable from those of neuroleptic-induced akathisia .

Example answer:
{"entities": [{"text": "fluoxetine-induced", "type": "Chemical"}, {"text": "anxiety", "type": "Disease"}, {"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: Estradiol reduces seizure-induced hippocampal injury in ovariectomized female but not in male rats .

Example answer:
{"entities": [{"text": "Estradiol", "type": "Chemical"}, {"text": "seizure-induced", "type": "Disease"}, {"text": "hippocampal injury", "type": "Disease"}]}

Example input:
Sentence: Animal studies suggest that incontinence secondary to serotonergic antidepressants could be mediated by the 5HT4 receptors found on the bladder .

Example answer:
{"entities": [{"text": "incontinence", "type": "Disease"}, {"text": "serotonergic antidepressants", "type": "Chemical"}]}

Example input:
Sentence: This study aimed at investigating the potential antipsychotic-like properties of SSR103800 , with a particular focus on models of hyperactivity , involving either drug challenge ( ie , amphetamine and MK-801 ) or transgenic mice ( ie , NMDA Nr1 ( neo-/- ) and DAT ( -/- ) ) .

Example answer:
{"entities": [{"text": "SSR103800", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "MK-801", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}]}

Example input:
Sentence: Increase of Parkinson disability after fluoxetine medication .

Example answer:
{"entities": [{"text": "Parkinson disability", "type": "Disease"}, {"text": "fluoxetine", "type": "Chemical"}]}

Example input:
Sentence: The present study sought to characterize the cognitive-enhancing effects of the 5-HT ( 6 ) antagonist Ro4368554 ( 3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole ) in a rat object recognition task employing a cholinergic ( scopolamine pretreatment ) and a serotonergic- ( tryptophan ( TRP ) depletion ) deficient model , and compared its pattern of action with that of the acetylcholinesterase inhibitor metrifonate .

Example answer:
{"entities": [{"text": "5-HT", "type": "Chemical"}, {"text": "Ro4368554", "type": "Chemical"}, {"text": "3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole", "type": "Chemical"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "tryptophan", "type": "Chemical"}, {"text": "TRP", "type": "Chemical"}, {"text": "metrifonate", "type": "Chemical"}]}

Example input:
Sentence: Five patients receiving fluoxetine for the treatment of obsessive compulsive disorder or major depression developed akathisia .

Example answer:
{"entities": [{"text": "fluoxetine", "type": "Chemical"}, {"text": "obsessive compulsive disorder", "type": "Disease"}, {"text": "major depression", "type": "Disease"}, {"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: A significant decrease in neuronal density of the hippocampal hilar formation was identified in vehicle- and PDTC-treated rats following status epilepticus .

Example answer:
{"entities": [{"text": "PDTC-treated", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}]}

Example input:
Sentence: We report the increased amount of motor disability in four patients with idiopathic Parkinson 's disease after exposure to the antidepressant fluoxetine .

Example answer:
{"entities": [{"text": "motor disability", "type": "Disease"}, {"text": "idiopathic Parkinson 's disease", "type": "Disease"}, {"text": "antidepressant", "type": "Chemical"}, {"text": "fluoxetine", "type": "Chemical"}]}

Input:
Sentence: In contrast reports indicate that hippocampal dependent neurogenesis and cognition are enhanced by the SSRI antidepressant Fluoxetine .

## Item bc5cdr:test:3396
Example input:
Sentence: A low incidence of cardiovascular malformations was observed after exposure to each of the four calcium channel blockers , but this incidence was statistically significant only for verapamil and nifedipine .

Example answer:
{"entities": [{"text": "cardiovascular malformations", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: Because of the need for the development of new treatments for Crohn 's disease , a pilot study was undertaken to estimate the pharmacodynamics and tolerability of fusidic acid treatment in chronic active , therapy-resistant patients .

Example answer:
{"entities": [{"text": "Crohn 's disease", "type": "Disease"}, {"text": "fusidic acid", "type": "Chemical"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Post hoc analyses indicated that efficacy was similar with asenapine and haloperidol ; greater contrasts were seen in AEs , especially extrapyramidal symptoms .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}, {"text": "extrapyramidal symptoms", "type": "Disease"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: The ACTIVE-W ( Atrial Fibrillation Clopidogrel Trial with Irbesartan for Prevention of Vascular Events ) study has demonstrated that warfarin is superior to platelet therapy ( clopidogrel plus aspirin ) in the prevention af embolic events .

Example answer:
{"entities": [{"text": "Atrial Fibrillation", "type": "Disease"}, {"text": "Clopidogrel", "type": "Chemical"}, {"text": "Irbesartan", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}, {"text": "clopidogrel", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "embolic events", "type": "Disease"}]}

Example input:
Sentence: These studies suggest that both phenacetin and acetaminophen may contribute to the burden of ESRD , with the risk of the latter being somewhat less than that of the former .

Example answer:
{"entities": [{"text": "phenacetin", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Acetylsalicylic acid , dipyridamole , and hydrocortisone all appear to have cardioprotective effects when tested in this model .

Example answer:
{"entities": [{"text": "Acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}]}

Example input:
Sentence: Pooled data from trials comparing antithrombotic treatment with placebo have shown that warfarin reduces the risk of stroke by 62 % , and that aspirin alone reduces the risk by 22 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "stroke", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: Overall , in high-risk patients , warfarin is superior to aspirin in preventing strokes , with a relative risk reduction of 36 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "strokes", "type": "Disease"}]}

Input:
Sentence: LIMITATIONS : New evidence on aspirin for the primary prevention of CVD is limited .

## Item bc5cdr:test:3573
Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: Male SD rats ( n = 30 ) were treated with Ato ( 50 mg/kg per day in drinking water ) or tap water for 15 days .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}]}

Example input:
Sentence: The male Wistar rats consuming a diet that contained LiCl ( 60 mmol/kg ) for 4 weeks developed marked polyuria .

Example answer:
{"entities": [{"text": "LiCl", "type": "Chemical"}, {"text": "polyuria", "type": "Disease"}]}

Example input:
Sentence: In this study , the severity of response to other seizure-inducing agents was tested in mice 1 and 24 h after intraperitoneal administration of 80 mg/kg gamma-HCH .

Example answer:
{"entities": [{"text": "seizure-inducing", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}]}

Example input:
Sentence: However , at the end of 3 weeks , amphotericin B levels in the kidneys and liver were significantly higher in salt-depleted and normal-salt rats than those in salt-loaded rats , with plasma/kidney ratios of 21 , 14 , and 8 in salt-depleted , normal-salt , and salt-loaded rats , respectively .

Example answer:
{"entities": [{"text": "amphotericin B", "type": "Chemical"}]}

Example input:
Sentence: Using this rationale , the 8-aminoquinoline WR242511 , a potent long-lasting MHb former in rodents and beagle dogs , was studied in the rhesus monkey for advanced development as a potential CN pretreatment .

Example answer:
{"entities": [{"text": "8-aminoquinoline", "type": "Chemical"}, {"text": "WR242511", "type": "Chemical"}]}

Example input:
Sentence: The Dbh -/- mice had normal baseline performance in the EPM but were completely resistant to the anxiogenic effects of cocaine .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Swiss albino mice prepared with intrajugular catheters were tested in photocell cages after administration of 93 mg/kg ( LD50 ) of cocaine and GNC92H2 infusions ranging from 30 to 190 mg/kg .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "GNC92H2", "type": "Chemical"}]}

Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "Chemical"}]}

Input:
Sentence: Wild-type ( WT ) and ILK : liver-/- mice were given PB ( 0.1 % in drinking water ) for 10 days .

## Item bc5cdr:test:3465
Example input:
Sentence: Because folinic acid was unlikely to be associated with this condition , neurotoxicity due to high-dose 5-fluorouracil was highly suspected .

Example answer:
{"entities": [{"text": "folinic acid", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}]}

Example input:
Sentence: NRA0160 and clozapine significantly shortened the phencyclidine ( PCP ) -induced prolonged swimming latency in rats in a water maze task .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "phencyclidine", "type": "Chemical"}, {"text": "PCP", "type": "Chemical"}]}

Example input:
Sentence: The influence of sevoflurane on lidocaine-induced convulsions was studied in cats .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "Chemical"}, {"text": "lidocaine-induced", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : In this preliminary report , divalproex sodium was a superior alternative to lithium in bipolar patients experiencing cognitive deficits , loss of creativity , and functional impairments .

Example answer:
{"entities": [{"text": "divalproex sodium", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "bipolar", "type": "Disease"}, {"text": "cognitive deficits", "type": "Disease"}, {"text": "loss of creativity", "type": "Disease"}, {"text": "functional impairments", "type": "Disease"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Delirium was found in 10 % of clozapine-treated inpatients , particularly in older patients exposed to other central anticholinergics .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}, {"text": "clozapine-treated", "type": "Chemical"}]}

Example input:
Sentence: The convulsant activity of bupivacaine was not significantly modified but calcium channel blockers decreased the time of latency to obtain bupivacaine-induced convulsions ; this effect was less pronounced with bepridil .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "bupivacaine-induced", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "bepridil", "type": "Chemical"}]}

Example input:
Sentence: It is suggested that sevoflurane reduces the convulsive effect of lidocaine toxicity but carries some risk due to circulatory depression .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "Chemical"}, {"text": "convulsive", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: Delirium , which may be induced by tricyclic drug therapy in the elderly , can be caused by tricyclics with low anticholinergic potency .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}]}

Example input:
Sentence: Apamin , a selective blocker of calcium-dependent potassium channels , was administered intracerebroventricularly in rats anesthetized with 0.8 % sevoflurane to investigate the mechanism of the anticonvulsive effects .

Example answer:
{"entities": [{"text": "Apamin", "type": "Chemical"}, {"text": "calcium-dependent", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}, {"text": "sevoflurane", "type": "Chemical"}]}

Input:
Sentence: DISCUSSION : Flecainide and pharmacologically similar agents that interact with sodium channels may cause delirium in susceptible patients .

## Item bc5cdr:test:2919
Example input:
Sentence: Based on the finding that VPU and VPA could protect the animals against pilocarpine-induced seizure it is suggested that the reduction of inhibitory amino acid neurotransmitters was comparatively minor and offset by a pronounced reduction of glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: The present study aimed to investigate the anticonvulsant activity as well as the effects on the level of hippocampal amino acid neurotransmitters ( glutamate , aspartate , glycine and GABA ) of N- ( 2-propylpentanoyl ) urea ( VPU ) in comparison to its parent compound , valproic acid ( VPA ) .

Example answer:
{"entities": [{"text": "amino acid", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}, {"text": "N- ( 2-propylpentanoyl ) urea", "type": "Chemical"}, {"text": "VPU", "type": "Chemical"}, {"text": "valproic acid", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}]}

Example input:
Sentence: The rats received AChE reactivator pralidoxime-2-chloride ( 2PAM ) ( 30.0 mg/kg BW ) , anticonvulsant diazepam ( 2.0 mg/kg BW ) , A ( 1 ) -adenosine receptor agonist N ( 6 ) -cyclopentyl adenosine ( CPA ) ( 2.0 mg/kg BW ) , NMDA-receptor antagonist dizocilpine maleate ( +-MK801 hydrogen maleate ) ( 2.0 mg/kg BW ) or their combinations with cholinolytic drug atropine sulfate ( 50.0 mg/kg BW ) immediately or 30 min after the single SC injection of DFP .

Example answer:
{"entities": [{"text": "pralidoxime-2-chloride", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "N ( 6 ) -cyclopentyl adenosine", "type": "Chemical"}, {"text": "CPA", "type": "Chemical"}, {"text": "NMDA-receptor", "type": "Chemical"}, {"text": "dizocilpine maleate", "type": "Chemical"}, {"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: Acute effects of N- ( 2-propylpentanoyl ) urea on hippocampal amino acid neurotransmitters in pilocarpine-induced seizure in rats .

Example answer:
{"entities": [{"text": "N- ( 2-propylpentanoyl ) urea", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Therefore , like VPA , the finding that VPU could drastically reduce pilocarpine-induced increases in glutamate and aspartate should account , at least partly , for its anticonvulsant activity observed in pilocarpine-induced seizure in experimental animals .

Example answer:
{"entities": [{"text": "VPA", "type": "Chemical"}, {"text": "VPU", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Seizure activity due to PTZ and picrotoxin ( PTX ) was significantly decreased ; however , seizure activity due to 3-mercaptopropionic acid ( MPA ) , bicuculline ( BCC ) , methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate ( DMCM ) , or strychnine ( STR ) was not different from control .

Example answer:
{"entities": [{"text": "Seizure", "type": "Disease"}, {"text": "PTZ", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "PTX", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "3-mercaptopropionic acid", "type": "Chemical"}, {"text": "MPA", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "BCC", "type": "Chemical"}, {"text": "methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate", "type": "Chemical"}, {"text": "DMCM", "type": "Chemical"}, {"text": "strychnine", "type": "Chemical"}, {"text": "STR", "type": "Chemical"}]}

Example input:
Sentence: Long-term intragastric application of the antiepileptic drug sodium valproate ( Vupral `` Polfa '' ) at the effective dose of 200 mg/kg b. w. once daily to rats for 1 , 3 , 6 , 9 and 12 months revealed neurological disorders indicating cerebellum damage ( `` valproate encephalopathy '' ) .

Example answer:
{"entities": [{"text": "sodium valproate", "type": "Chemical"}, {"text": "neurological disorders", "type": "Disease"}, {"text": "cerebellum damage", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Estradiol reduces seizure-induced hippocampal injury in ovariectomized female but not in male rats .

Example answer:
{"entities": [{"text": "Estradiol", "type": "Chemical"}, {"text": "seizure-induced", "type": "Disease"}, {"text": "hippocampal injury", "type": "Disease"}]}

Input:
Sentence: Anticonvulsant effect of eslicarbazepine acetate ( BIA 2-093 ) on seizures induced by microperfusion of picrotoxin in the hippocampus of freely moving rats .

## Item bc5cdr:test:3385
Example input:
Sentence: Reversal by phenylephrine of the beneficial effects of intravenous nitroglycerin in patients with acute myocardial infarction .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "nitroglycerin", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: The results of our study suggest that salvianolic acid A possessing antioxidant activity has a significant protective effect against isoproterenol-induced myocardial infarction .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: The protective role of salvianolic acid A against isoproterenol-induced myocardial damage was further confirmed by histopathological examination .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial damage", "type": "Disease"}]}

Example input:
Sentence: The aim of the study was to clarify the incidence and severity of adverse cardiac effects to this treatment .

Example answer:
{"entities": []}

Example input:
Sentence: Oral contraceptives and the risk of myocardial infarction .

Example answer:
{"entities": [{"text": "Oral contraceptives", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: The purpose of this study was to investigate the influence of calcium channel blockers on bupivacaine-induced acute toxicity .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "bupivacaine-induced", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Acetylsalicylic acid , dipyridamole , and hydrocortisone all appear to have cardioprotective effects when tested in this model .

Example answer:
{"entities": [{"text": "Acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}]}

Example input:
Sentence: The present study was designed to evaluate the cardioprotective potential of salvianolic acid A on isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Overall , in high-risk patients , warfarin is superior to aspirin in preventing strokes , with a relative risk reduction of 36 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "strokes", "type": "Disease"}]}

Example input:
Sentence: Pooled data from trials comparing antithrombotic treatment with placebo have shown that warfarin reduces the risk of stroke by 62 % , and that aspirin alone reduces the risk by 22 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "stroke", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}]}

Input:
Sentence: PURPOSE : To determine the benefits and harms of taking aspirin for the primary prevention of myocardial infarctions , strokes , and death .

## Item bc5cdr:test:3603
Example input:
Sentence: Thirty-five lamivudine-na ve HBV infected patients with or without HIV co-infection were studied : 15 chronic HBV mono-infected patients and 20 HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "lamivudine-na", "type": "Chemical"}, {"text": "HBV infected", "type": "Disease"}, {"text": "HIV co-infection", "type": "Disease"}, {"text": "HBV mono-infected", "type": "Disease"}]}

Example input:
Sentence: METHODS : Thirty-nine postmenopausal women with osteopenia or osteoporosis were included in this prospective , controlled clinical study .

Example answer:
{"entities": [{"text": "osteopenia", "type": "Disease"}, {"text": "osteoporosis", "type": "Disease"}]}

Example input:
Sentence: Over the period 1993-1996 , 551 cases of VTE were identified in Germany and the UK along with 2066 controls .

Example answer:
{"entities": [{"text": "VTE", "type": "Disease"}]}

Example input:
Sentence: Based on this principle a 27-year old woman , classified as being in the high-risk group ( Goldstein and Berkowitz score : 11 ) , was treated with multiple cytotoxic drugs .

Example answer:
{"entities": []}

Example input:
Sentence: This was an exploratory study to investigate lamivudine-resistant hepatitis B virus ( HBV ) strains in selected lamivudine-na ve HBV carriers with and without human immunodeficiency virus ( HIV ) co-infection in South African patients .

Example answer:
{"entities": [{"text": "lamivudine-resistant", "type": "Chemical"}, {"text": "hepatitis B", "type": "Disease"}, {"text": "lamivudine-na", "type": "Chemical"}, {"text": "human immunodeficiency virus ( HIV ) co-infection", "type": "Disease"}]}

Example input:
Sentence: Seventy-five human immunodeficiency virus ( HIV ) -infected patients with CD4+ cell counts < 500/mm3 were randomized to receive either ZDV ( 500 mg daily ) alone ( group I , n = 38 ) or in combination with folinic acid ( 15 mg daily ) and intramascular vitamin B12 ( 1000 micrograms monthly ) ( group II , n = 37 ) .

Example answer:
{"entities": [{"text": "human immunodeficiency virus ( HIV ) -infected", "type": "Disease"}, {"text": "ZDV", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}, {"text": "vitamin B12", "type": "Chemical"}]}

Example input:
Sentence: The excess event rate was 1.8 per 1,000 woman-years ( 95 % CI -0.5-4.1 ) , and the number needed to treat to cause 1 event was 170 ( 95 % CI 100-582 ) over 3.3 years .

Example answer:
{"entities": []}

Example input:
Sentence: Seventy patients developed major opportunistic infections whilst on therapy ; this was the first AIDS diagnosis in 17 .

Example answer:
{"entities": [{"text": "opportunistic infections", "type": "Disease"}, {"text": "AIDS", "type": "Disease"}]}

Example input:
Sentence: In a randomized , double-blind , placebo-controlled , crossover study , we studied 12 volunteers in three experiments .

Example answer:
{"entities": []}

Example input:
Sentence: DESIGN , SETTING , AND PARTICIPANTS : Population-based , multisite , case-control study of women who had pregnancies affected by 1 of more than 30 eligible major birth defects identified via birth defect surveillance programs in 10 states ( n = 13 155 ) and control women randomly selected from the same geographical regions ( n = 4941 ) .

Example answer:
{"entities": [{"text": "birth defects", "type": "Disease"}, {"text": "birth defect", "type": "Disease"}]}

Input:
Sentence: The study included 871 women with HIV who were recruited from 1993-1995 in four US cities .

## Item bc5cdr:test:3676
Example input:
Sentence: Acute liver failure in two patients with regular alcohol consumption ingesting paracetamol at therapeutic dosage .

Example answer:
{"entities": [{"text": "Acute liver failure", "type": "Disease"}, {"text": "alcohol", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: Psychologists need to inquire about consumption of quinine-containing beverages as part of an evaluation process .

Example answer:
{"entities": [{"text": "quinine-containing", "type": "Chemical"}]}

Example input:
Sentence: Notwithstanding these facts our findings suggest that these patients might benefit from relatively mild initial treatment , especially true for patients not previously exposed to this drug .

Example answer:
{"entities": []}

Example input:
Sentence: BACKGROUND : Cocaine is a widely abused psychostimulant that has both rewarding and aversive properties .

Example answer:
{"entities": [{"text": "Cocaine", "type": "Chemical"}]}

Example input:
Sentence: Previous research in this laboratory has shown that a diet of intermittent excessive sugar consumption produces a state with neurochemical and behavioral similarities to drug dependency .

Example answer:
{"entities": [{"text": "drug dependency", "type": "Disease"}]}

Example input:
Sentence: CASE SUMMARY : A 40-year-old woman with major depression took an overdose of venlafaxine in an apparent suicide attempt .

Example answer:
{"entities": [{"text": "major depression", "type": "Disease"}, {"text": "overdose", "type": "Disease"}, {"text": "venlafaxine", "type": "Chemical"}]}

Example input:
Sentence: Clinical tolerability of both agents has been good , with fewer than 3 % of patients withdrawn from treatment because of clinical adverse experiences .

Example answer:
{"entities": []}

Example input:
Sentence: Moreover , the coadministration of these frequently used drugs is expected to be especially harmful in this subgroup of patients .

Example answer:
{"entities": []}

Example input:
Sentence: Three patients received high doses of chlormethiazole for alcohol withdrawal symptoms , and one took a suicidal overdose of nitrazepam .

Example answer:
{"entities": [{"text": "chlormethiazole", "type": "Chemical"}, {"text": "alcohol", "type": "Chemical"}, {"text": "withdrawal symptoms", "type": "Disease"}, {"text": "overdose", "type": "Disease"}, {"text": "nitrazepam", "type": "Chemical"}]}

Example input:
Sentence: regular consumption of alcohol , liver failure is possible when therapeutic doses are ingested .

Example answer:
{"entities": [{"text": "alcohol", "type": "Chemical"}, {"text": "liver failure", "type": "Disease"}]}

Input:
Sentence: Patients often consume the drug with suicidal intent or with a background of substance dependence .

## Item bc5cdr:test:3468
Example input:
Sentence: Delirium was inconsistently recognized clinically in milder cases and was associated with increased length-of-stay and higher costs , and inferior clinical outcome .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}]}

Example input:
Sentence: All patients received CAB [ leuprolide acetate ( LHRH-A ) 3.75 mg , intramuscularly , every 28 days plus 250 mg flutamide , tid , per Os ] and were evaluated for anemia by physical examination and laboratory tests at baseline and 4 subsequent intervals ( 1 , 2 , 3 and 6 months post-CAB ) .

Example answer:
{"entities": [{"text": "leuprolide acetate", "type": "Chemical"}, {"text": "LHRH-A", "type": "Chemical"}, {"text": "flutamide", "type": "Chemical"}, {"text": "anemia", "type": "Disease"}]}

Example input:
Sentence: During an 18-month period of study 41 hemodialyzed patients receiving desferrioxamine ( 10-40 mg/kg BW/3 times weekly ) for the first time were monitored for detection of audiovisual toxicity .

Example answer:
{"entities": [{"text": "desferrioxamine", "type": "Chemical"}, {"text": "audiovisual toxicity", "type": "Disease"}]}

Example input:
Sentence: Because folinic acid was unlikely to be associated with this condition , neurotoxicity due to high-dose 5-fluorouracil was highly suspected .

Example answer:
{"entities": [{"text": "folinic acid", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}]}

Example input:
Sentence: Delirium was diagnosed in 14 ( 10.1 % incidence , or 1.48 cases/person-years of exposure ) ; 71.4 % of cases were moderate or severe .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}]}

Example input:
Sentence: He developed acute neurologic symptoms of mental confusion , disorientation and irritability , and then lapsed into a deep coma , lasting for approximately 40 hours during the first dose ( day 2 ) of 5-fluorouracil and folinic acid infusion .

Example answer:
{"entities": [{"text": "confusion", "type": "Disease"}, {"text": "disorientation", "type": "Disease"}, {"text": "irritability", "type": "Disease"}, {"text": "coma", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: Delirium , which may be induced by tricyclic drug therapy in the elderly , can be caused by tricyclics with low anticholinergic potency .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}]}

Example input:
Sentence: Desipramine-induced delirium at `` subtherapeutic '' concentrations : a case report .

Example answer:
{"entities": [{"text": "Desipramine-induced", "type": "Chemical"}, {"text": "delirium", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Delirium was found in 10 % of clozapine-treated inpatients , particularly in older patients exposed to other central anticholinergics .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}, {"text": "clozapine-treated", "type": "Chemical"}]}

Example input:
Sentence: An elderly patient treated with low dose Desipramine developed a delirium while her plasma level was in the `` subtherapeutic '' range .

Example answer:
{"entities": [{"text": "Desipramine", "type": "Chemical"}, {"text": "delirium", "type": "Disease"}]}

Input:
Sentence: CONCLUSIONS : Supratherapeutic flecainide plasma concentrations may cause delirium .

## Item bc5cdr:test:3073
Example input:
Sentence: Learning of rats under amnesia caused by pentobarbital .

Example answer:
{"entities": [{"text": "amnesia", "type": "Disease"}, {"text": "pentobarbital", "type": "Chemical"}]}

Example input:
Sentence: Cocaine causes memory and learning impairments in rats : involvement of nuclear factor kappa B and oxidative stress , and prevention by topiramate .

Example answer:
{"entities": [{"text": "Cocaine", "type": "Chemical"}, {"text": "topiramate", "type": "Chemical"}]}

Example input:
Sentence: Dissociated learning of rats in the normal state and the state of amnesia produced by pentobarbital ( 15 mg/kg , ip ) was carried out .

Example answer:
{"entities": [{"text": "amnesia", "type": "Disease"}, {"text": "pentobarbital", "type": "Chemical"}]}

Example input:
Sentence: The effects of PG-9 ( 3alpha-tropyl 2- ( p-bromophenyl ) propionate ) , the acetylcholine releaser , on memory processes and nerve growth factor ( NGF ) synthesis were evaluated .

Example answer:
{"entities": [{"text": "PG-9", "type": "Chemical"}, {"text": "3alpha-tropyl 2- ( p-bromophenyl ) propionate", "type": "Chemical"}, {"text": "acetylcholine", "type": "Chemical"}]}

Example input:
Sentence: These data indicate that a critical percentage of NTE inhibition in brain and spinal cord sampled shortly after Mipafox exposure can predict neuropathic damage in rats several weeks later .

Example answer:
{"entities": [{"text": "Mipafox", "type": "Chemical"}, {"text": "neuropathic damage", "type": "Disease"}]}

Example input:
Sentence: Grade 3-4 adverse effects included myelosuppression , fatigue , somnolence/depressed mood , neuropathy and dyspnea .

Example answer:
{"entities": [{"text": "myelosuppression", "type": "Disease"}, {"text": "fatigue", "type": "Disease"}, {"text": "somnolence/depressed mood", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}, {"text": "dyspnea", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Clomipramine exposure in immature rats produced significant behavioral and biochemical changes that include enhanced anxiety ( elevated plus maze and marble burying ) , behavioral inflexibility ( perseveration in the spontaneous alternation task and impaired reversal learning ) , working memory impairment ( e.g. , win-shift paradigm ) , hoarding , and corticostriatal dysfunction .

Example answer:
{"entities": [{"text": "Clomipramine", "type": "Chemical"}, {"text": "anxiety", "type": "Disease"}, {"text": "behavioral inflexibility", "type": "Disease"}, {"text": "memory impairment", "type": "Disease"}, {"text": "hoarding", "type": "Disease"}, {"text": "corticostriatal dysfunction", "type": "Disease"}]}

Example input:
Sentence: Significant declines in simple and sustained attention , working memory , and verbal memory were observed at 1 hour postdose compared to baseline for both age groups with a trend toward return to baseline by 5 hours postdose .

Example answer:
{"entities": []}

Example input:
Sentence: The antiepileptic drugs , phenobarbitone and carbamazepine are well known to cause cognitive impairment on chronic use .

Example answer:
{"entities": [{"text": "phenobarbitone", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "cognitive impairment", "type": "Disease"}]}

Example input:
Sentence: The administration of phenobarbitone and carbamazepine for 21days caused a significant impairment of learning and memory as well as an increased oxidative stress .

Example answer:
{"entities": [{"text": "phenobarbitone", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "impairment of learning and memory", "type": "Disease"}]}

Input:
Sentence: RESULTS : Pb exposure produced lasting impairments in learning , attention , inhibitory control , and arousal regulation , paralleling the areas of dysfunction seen in Pb-exposed children .

## Item bc5cdr:test:3644
Example input:
Sentence: At the end of study period , serum phenobarbitone and carbamazepine , whole brain malondialdehyde and reduced glutathione levels were estimated .

Example answer:
{"entities": [{"text": "phenobarbitone", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "malondialdehyde", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}]}

Example input:
Sentence: This is the first report of such an unusual reaction to carbamazepine .

Example answer:
{"entities": [{"text": "carbamazepine", "type": "Chemical"}]}

Example input:
Sentence: Carbamazepine ( CBZ ) , a commonly used AED , has been implicated in some clinical studies .

Example answer:
{"entities": [{"text": "Carbamazepine", "type": "Chemical"}, {"text": "CBZ", "type": "Chemical"}]}

Example input:
Sentence: Two patients with signs of carbamazepine neurotoxicity after combined treatment with verapamil showed complete recovery after discontinuation of the calcium entry blocker .

Example answer:
{"entities": [{"text": "carbamazepine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}]}

Example input:
Sentence: The results of this case report support the idea that in contrast with carbamazepine oxcarbazepine does not induce the hepatic microsomal enzyme systems regulating the inactivation of antipsychotic drugs .

Example answer:
{"entities": [{"text": "carbamazepine", "type": "Chemical"}, {"text": "oxcarbazepine", "type": "Chemical"}]}

Example input:
Sentence: The administration of phenobarbitone and carbamazepine for 21days caused a significant impairment of learning and memory as well as an increased oxidative stress .

Example answer:
{"entities": [{"text": "phenobarbitone", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "impairment of learning and memory", "type": "Disease"}]}

Example input:
Sentence: Verapamil-induced carbamazepine neurotoxicity .

Example answer:
{"entities": [{"text": "Verapamil-induced", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Chronic carbamazepine treatment in the rat : efficacy , toxicity , and effect on plasma and tissue folate concentrations .

Example answer:
{"entities": [{"text": "carbamazepine", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "folate", "type": "Chemical"}]}

Example input:
Sentence: Hypersensitivity to carbamazepine presenting with a leukemoid reaction , eosinophilia , erythroderma , and renal failure .

Example answer:
{"entities": [{"text": "Hypersensitivity", "type": "Disease"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "leukemoid reaction", "type": "Disease"}, {"text": "eosinophilia", "type": "Disease"}, {"text": "erythroderma", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: We report a patient in whom hypersensitivity to carbamazepine presented with generalized erythroderma , a severe leukemoid reaction , eosinophilia , hyponatremia , and renal failure .

Example answer:
{"entities": [{"text": "hypersensitivity", "type": "Disease"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "erythroderma", "type": "Disease"}, {"text": "leukemoid reaction", "type": "Disease"}, {"text": "eosinophilia", "type": "Disease"}, {"text": "hyponatremia", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Input:
Sentence: The most severe adverse reactions to carbamazepine have been observed in the haemopoietic system , the liver and the cardiovascular system .

## Item bc5cdr:test:3237
Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Carbamazepine and vigabatrin are contraindicated in typical absence seizures .

Example answer:
{"entities": [{"text": "Carbamazepine", "type": "Chemical"}, {"text": "vigabatrin", "type": "Chemical"}, {"text": "absence seizures", "type": "Disease"}]}

Example input:
Sentence: In Group 1 the rats were trained under the influence of pentobarbital to run to the same shelf as in the normal state .

Example answer:
{"entities": [{"text": "pentobarbital", "type": "Chemical"}]}

Example input:
Sentence: The antiepileptic drugs , phenobarbitone and carbamazepine are well known to cause cognitive impairment on chronic use .

Example answer:
{"entities": [{"text": "phenobarbitone", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "cognitive impairment", "type": "Disease"}]}

Example input:
Sentence: In the absence of caffeine , acetaminophen ( up to 300 mg/kg ) did not modify the seizures induced by maximal electroshock and did not alter the convulsant dose of pentylenetetrezol in mice ( tests performed by the Anticonvulsant Screening Project of NINCDS ) .

Example answer:
{"entities": [{"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "pentylenetetrezol", "type": "Chemical"}]}

Example input:
Sentence: Long-term intragastric application of the antiepileptic drug sodium valproate ( Vupral `` Polfa '' ) at the effective dose of 200 mg/kg b. w. once daily to rats for 1 , 3 , 6 , 9 and 12 months revealed neurological disorders indicating cerebellum damage ( `` valproate encephalopathy '' ) .

Example answer:
{"entities": [{"text": "sodium valproate", "type": "Chemical"}, {"text": "neurological disorders", "type": "Disease"}, {"text": "cerebellum damage", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: By using this strategy to study the involvement of MRP2 in brain access of antiepileptic drugs ( AEDs ) , we recently reported that phenytoin is a substrate for MRP2 in the BBB .

Example answer:
{"entities": [{"text": "phenytoin", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : We report on the manifestation of a levetiracetam ( LEV ) -induced encephalopathy .

Example answer:
{"entities": [{"text": "levetiracetam", "type": "Chemical"}, {"text": "LEV", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: FINDINGS : A 28-year-old man suffering from idiopathic epilepsy with generalized seizures was treated with LEV ( 3000 mg ) added to valproate ( VPA ) ( 2000 mg ) .

Example answer:
{"entities": [{"text": "idiopathic epilepsy", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "LEV", "type": "Chemical"}, {"text": "valproate", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}]}

Example input:
Sentence: Encephalopathy induced by levetiracetam added to valproate .

Example answer:
{"entities": [{"text": "Encephalopathy", "type": "Disease"}, {"text": "levetiracetam", "type": "Chemical"}, {"text": "valproate", "type": "Chemical"}]}

Input:
Sentence: Levetiracetam as an adjunct to phenobarbital treatment in cats with suspected idiopathic epilepsy .

## Item bc5cdr:test:3683
Example input:
Sentence: Our objective was to investigate brain MR imaging findings and the utility of diffusion-weighted ( DW ) imaging in organ transplant patients who developed neurologic symptoms during tacrolimus therapy .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}]}

Example input:
Sentence: METHOD : The response of 44 patients meeting DSM-IV criteria for bipolar disorder to naturalistic treatment was assessed for at least 6 weeks using the Montgomery-Asberg Depression Rating Scale and the Bech-Rafaelson Mania Rating Scale .

Example answer:
{"entities": [{"text": "bipolar disorder", "type": "Disease"}]}

Example input:
Sentence: The patient cohort ( 14 men , 11 women ) was treated with SRL as conversion therapy , due to chronic allograft nephropathy ( CAN ) ( n = 15 ) neoplasia ( n = 8 ) ; Kaposi 's sarcoma , Four skin cancers , One intestinal tumors , One renal cell carsinom ) or BK virus nephropathy ( n = 2 ) .

Example answer:
{"entities": [{"text": "SRL", "type": "Chemical"}, {"text": "chronic allograft nephropathy", "type": "Disease"}, {"text": "CAN", "type": "Disease"}, {"text": "neoplasia", "type": "Disease"}, {"text": "Kaposi 's sarcoma", "type": "Disease"}, {"text": "skin cancers", "type": "Disease"}, {"text": "intestinal tumors", "type": "Disease"}, {"text": "renal cell carsinom", "type": "Disease"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: In this study , long-term cardiac transplant patients were switched from cyclosporine to Srl-based IS .

Example answer:
{"entities": [{"text": "cyclosporine", "type": "Chemical"}, {"text": "Srl-based", "type": "Chemical"}]}

Example input:
Sentence: However , for recipients of organ transplantation , removing the inciting agent is not without the attendant risk of precipitating acute rejection and graft loss .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSIONS : We conclude that in transplants , there is a strong association between well-developed PTCR and TG , while the significance of mild PTCR and its predictive value in the absence of TG is unclear .

Example answer:
{"entities": [{"text": "TG", "type": "Disease"}]}

Example input:
Sentence: End-stage renal disease ( ESRD ) after orthotopic liver transplantation ( OLTX ) using calcineurin-based immunotherapy : risk of development and treatment .

Example answer:
{"entities": [{"text": "End-stage renal disease", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Over the long-term chronic phase ( 120 days after transplantation ) , only 25 % of BMC-treated epileptic animals had seizures , but with a lower frequency and duration compared to the epileptic control group .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: We report a case of a living donor renal transplant recipient who developed cyclosporine-induced TMA that responded to the withdrawal of cyclosporine in conjunction with plasmapheresis and fresh frozen plasma replacement therapy .

Example answer:
{"entities": [{"text": "cyclosporine-induced", "type": "Chemical"}, {"text": "TMA", "type": "Disease"}, {"text": "cyclosporine", "type": "Chemical"}]}

Example input:
Sentence: Introduction of tacrolimus as an alternative immunosuppressive agent resulted in the recurrence of TMA and the subsequent loss of the renal allograft .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "TMA", "type": "Disease"}]}

Input:
Sentence: Multidisciplinary approaches with long-term psychiatric follow-up may contribute to low post-transplant suicide rates seen and low rates of graft loss because of non-compliance .

## Item bc5cdr:test:3399
Example input:
Sentence: In almost half of these women severe atherosclerosis of the aorta was present ( n=11 ) , while in women without hormone use severe atherosclerosis of the aorta was present in less than 20 % ( OR 3.1 ; 95 % CI , 1.1-8.5 , adjusted for age , years since menopause , smoking , and body mass index ) .

Example answer:
{"entities": [{"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: Nitroglycerin has been shown to reduce ST-segment elevation during acute myocardial infarction , an effect potentiated in the dog by agents that reverse nitroglycerin-induced hypotension .

Example answer:
{"entities": [{"text": "Nitroglycerin", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}, {"text": "nitroglycerin-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : An association between the use of oral contraceptives and the risk of myocardial infarction has been found in some , but not all , studies .

Example answer:
{"entities": [{"text": "oral contraceptives", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Acetylsalicylic acid , dipyridamole , and hydrocortisone all appear to have cardioprotective effects when tested in this model .

Example answer:
{"entities": [{"text": "Acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}]}

Example input:
Sentence: The ACTIVE-W ( Atrial Fibrillation Clopidogrel Trial with Irbesartan for Prevention of Vascular Events ) study has demonstrated that warfarin is superior to platelet therapy ( clopidogrel plus aspirin ) in the prevention af embolic events .

Example answer:
{"entities": [{"text": "Atrial Fibrillation", "type": "Disease"}, {"text": "Clopidogrel", "type": "Chemical"}, {"text": "Irbesartan", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}, {"text": "clopidogrel", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "embolic events", "type": "Disease"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: The risk of myocardial infarction was similar among women who used oral contraceptives whether or not they had a prothrombotic mutation .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptives", "type": "Chemical"}]}

Example input:
Sentence: Oral contraceptives and the risk of myocardial infarction .

Example answer:
{"entities": [{"text": "Oral contraceptives", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Overall , in high-risk patients , warfarin is superior to aspirin in preventing strokes , with a relative risk reduction of 36 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "strokes", "type": "Disease"}]}

Example input:
Sentence: Pooled data from trials comparing antithrombotic treatment with placebo have shown that warfarin reduces the risk of stroke by 62 % , and that aspirin alone reduces the risk by 22 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "stroke", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}]}

Input:
Sentence: CONCLUSION : Aspirin reduces the risk for myocardial infarction in men and strokes in women .

## Item bc5cdr:test:3437
Example input:
Sentence: Neuroprotection rendered by MPEP may be associated with the reduction of the methamphetamine-induced dopamine efflux in the striatum due to the blockade of extrastriatal mGluR5 , and with a decrease in hyperthermia .

Example answer:
{"entities": [{"text": "MPEP", "type": "Chemical"}, {"text": "methamphetamine-induced", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "hyperthermia", "type": "Disease"}]}

Example input:
Sentence: L-DOPA-induced dyskinesia ( LID ) is among the motor complications that arise in Parkinson 's disease ( PD ) patients after a prolonged treatment with L-DOPA .

Example answer:
{"entities": [{"text": "L-DOPA-induced", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "LID", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "L-DOPA", "type": "Chemical"}]}

Example input:
Sentence: Recent preclinical and clinical data from promising lines of research focus on the differential role of presynaptic versus postsynaptic mechanisms , dopamine receptor subtypes , ionotropic and metabotropic glutamate receptors , and non-dopaminergic neurotransmitter systems in the pathophysiology of levodopa-induced dyskinesias .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: The effect appears to be mediated by central nicotine receptors , possibly located on dopaminergic neurons , and also requires the activation of both D1 and D2 dopamine receptors .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: Evidence for an involvement of D1 and D2 dopamine receptors in mediating nicotine-induced hyperactivity in rats .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "nicotine-induced", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}]}

Example input:
Sentence: Effects of 5-HT1B receptor ligands microinjected into the accumbal shell or core on the cocaine-induced locomotor hyperactivity in rats .

Example answer:
{"entities": [{"text": "cocaine-induced", "type": "Chemical"}, {"text": "locomotor hyperactivity", "type": "Disease"}]}

Example input:
Sentence: It is concluded that L-dopa enhances reflex bradycardia through central alpha-receptor stimulation .

Example answer:
{"entities": [{"text": "L-dopa", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: In addition , the role of dopamine receptors in mediating nicotine-induced locomotor stimulation was investigated by examining the effects of selective D1 and D2 dopamine receptor antagonists on activity induced by nicotine .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "nicotine-induced", "type": "Chemical"}, {"text": "nicotine", "type": "Chemical"}]}

Example input:
Sentence: The present study was designed to examine the effect of 5-HT1B receptor ligands microinjected into the subregions of the nucleus accumbens ( the shell and the core ) on the locomotor hyperactivity induced by cocaine in rats .

Example answer:
{"entities": [{"text": "locomotor hyperactivity", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: These results indicate that noradrenergic neurons have an important role in the manifestation of catalepsy induced by THC , whereas dopaminergic neurons are important in catalepsy induced by haloperidol .

Example answer:
{"entities": [{"text": "catalepsy", "type": "Disease"}, {"text": "THC", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Input:
Sentence: These results suggest that activation of CB1 receptors offers neuroprotection against dopaminergic lesion and the development of L-DOPA-induced dyskinesias .

## Item bc5cdr:test:3636
Example input:
Sentence: Rats were treated with the vehicle ( 2 mL/kg of distilled water and 5 % w/v cellulose , 10 days ) , gum Arabic ( 2 mL/kg of a 10 % w/v aqueous suspension of gum Arabic powder , orally for 10 days ) , or gum Arabic concomitantly with GM ( 80mg/kg/day intramuscularly , during the last six days of the treatment period ) .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}]}

Example input:
Sentence: The control rats received atropine sulfate , but also saline and olive oil instead of other antidotes and DFP , respectively .

Example answer:
{"entities": [{"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: Male Wistar rats were implanted bilaterally with cannulae into the accumbens shell or core , and then were locally injected with GR 55562 ( an antagonist of 5-HT1B receptors ) or CP 93129 ( an agonist of 5-HT1B receptors ) .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "Chemical"}, {"text": "Ato-treated", "type": "Chemical"}]}

Example input:
Sentence: Rats were treated with a single IV injection of puromycin aminonucleoside , ( PAN , 7.5 mg/kg ) and 24 hour urine samples were obtained prior to sacrifice on days 3,5,7,10,17,27,41 ( N = 5-10 per group ) .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: 2 and 10 mg/kg/i.p. , or an equal volume of saline for the control group ( n = 20 ) ; 15 minutes later , all the animals were injected with a single 50 mg/kg/i.p .

Example answer:
{"entities": []}

Example input:
Sentence: Male SD rats ( n = 30 ) were treated with Ato ( 50 mg/kg per day in drinking water ) or tap water for 15 days .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/", "type": "Chemical"}, {"text": "K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}]}

Example input:
Sentence: Thirty male Sprague-Dawley rats were divided randomly into four treatment groups : saline , dexamethasone ( dex ) , allopurinol plus saline , and allopurinol plus dex .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "dex", "type": "Chemical"}, {"text": "allopurinol", "type": "Chemical"}]}

Example input:
Sentence: Ten rats received saline as a control group .

Example answer:
{"entities": []}

Input:
Sentence: A total of 60 male Wistar albino rats were randomly divided into four groups ( 15/group ) : The control group injected with single doses of normal saline ( i.c.v ) followed 24 h later by BCNU solvent ( i.v ) .

## Item bc5cdr:test:3713
Example input:
Sentence: INTERPRETATION : Repeated exposure of human beings to HCFCs 123 and 124 can result in serious liver injury in a large proportion of the exposed population .

Example answer:
{"entities": [{"text": "liver injury", "type": "Disease"}]}

Example input:
Sentence: METHOD : The sample for the study consisted of 50 patients to whom subcutaneous heparin was administered .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: A low incidence of cardiovascular malformations was observed after exposure to each of the four calcium channel blockers , but this incidence was statistically significant only for verapamil and nifedipine .

Example answer:
{"entities": [{"text": "cardiovascular malformations", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: Acetylsalicylic acid , dipyridamole , and hydrocortisone all appear to have cardioprotective effects when tested in this model .

Example answer:
{"entities": [{"text": "Acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}]}

Example input:
Sentence: During treatment , adverse cardiac effects were observed in 14 patients ( 18 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Administration of this regimen to breast cancer patients who have been treated by chemotherapy and those with impaired heart function requires careful attention .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "impaired heart function", "type": "Disease"}]}

Example input:
Sentence: RELEVANCE TO CLINICAL PRACTICE : When administering subcutaneous heparin injections , it is important to extend the duration of the injection .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: The patient was admitted to the hospital , anticoagulated with unfractionated heparin , and given intravenous diltiazem for rate control and intravenous amiodarone for rate and rhythm control .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}]}

Example input:
Sentence: Since the introduction of angiotensin converting enzyme ( ACE ) inhibitors into the adjunctive treatment of patients with congestive heart failure , cases of severe hypotension , especially on the first day of treatment , have occasionally been reported .

Example answer:
{"entities": [{"text": "angiotensin converting enzyme ( ACE ) inhibitors", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: PATIENTS AND METHODS : Patients with more than 50 % decrease in platelet count or thrombocytopenia ( < 150 x 10 ( 9 ) /L ) after exposure to heparin , who had a positive two-step antigen assay [ optical density ( OD ) > 0.4 and > 50 inhibition with high concentration of heparin ] were included in the study .

Example answer:
{"entities": [{"text": "thrombocytopenia", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Input:
Sentence: Special attention must be paid to cardiac patients who are often exposed to heparin multiple times during their course of treatment .

## Item bc5cdr:test:3290
Example input:
Sentence: Biopsies performed in five patients revealed new pathological changes : One membranoproliferative glomerulopathy and interstitial nephritis .

Example answer:
{"entities": [{"text": "membranoproliferative glomerulopathy", "type": "Disease"}, {"text": "interstitial nephritis", "type": "Disease"}]}

Example input:
Sentence: This case study reveals an unusual finding of rapidly proliferative crescentic glomerulonephritis in a patient treated with rifampin who had no other identifiable causes for developing this disease .

Example answer:
{"entities": [{"text": "glomerulonephritis", "type": "Disease"}, {"text": "rifampin", "type": "Chemical"}]}

Example input:
Sentence: A case is presented of a reversible intra-Hisian block occurring under amiodarone treatment for atrial tachycardia in a patient without clear intraventricular conduction abnormalities .

Example answer:
{"entities": [{"text": "intra-Hisian block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atrial tachycardia", "type": "Disease"}, {"text": "intraventricular conduction abnormalities", "type": "Disease"}]}

Example input:
Sentence: Amiodarone-induced sinoatrial block .

Example answer:
{"entities": [{"text": "Amiodarone-induced", "type": "Chemical"}, {"text": "sinoatrial block", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVE : To report a case of a severe interaction between simvastatin , amiodarone , and atazanavir resulting in rhabdomyolysis and acute renal failure .

Example answer:
{"entities": [{"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}, {"text": "rhabdomyolysis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: Severe rhabdomyolysis and acute renal failure secondary to concomitant use of simvastatin , amiodarone , and atazanavir .

Example answer:
{"entities": [{"text": "rhabdomyolysis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: Review of this and previously reported cases indicates the need for early diagnosis of amiodarone pneumonitis , immediate withdrawal of amiodarone , and prompt but continued steroid therapy to ensure full recovery .

Example answer:
{"entities": [{"text": "amiodarone", "type": "Chemical"}, {"text": "pneumonitis", "type": "Disease"}, {"text": "steroid", "type": "Chemical"}]}

Example input:
Sentence: Amiodarone should be used with caution during long-term oral therapy in patients with or without clear intraventricular conduction defects .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "Chemical"}]}

Example input:
Sentence: We observed sinoatrial block due to chronic amiodarone administration in a 5-year-old boy with primary cardiomyopathy , Wolff-Parkinson-White syndrome and supraventricular tachycardia .

Example answer:
{"entities": [{"text": "sinoatrial block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "primary cardiomyopathy", "type": "Disease"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "supraventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: Pneumonitis with pleural and pericardial effusion and neuropathy during amiodarone therapy .

Example answer:
{"entities": [{"text": "neuropathy", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}]}

Input:
Sentence: The present case highlights the possibility that differential diagnosis between an amiodarone-related pulmonary lesion and a neoplasm can be very difficult radiologically , and suggests that membranous glomerulonephritis might be another possible complication of amiodarone treatment .

## Item bc5cdr:test:3432
Example input:
Sentence: After EE treatment , changes in immunostaining for 7H6 and ZO-1 were similar to those seen in periportal hepatocytes after BDL , but distributed more diffusely throughout the lobule .

Example answer:
{"entities": [{"text": "EE", "type": "Chemical"}]}

Example input:
Sentence: We tested the sulfated polysaccharide fucoidan , which has been reported to reduce inflammatory brain damage , in a rat model of intracerebral hemorrhage induced by injection of bacterial collagenase into the caudate nucleus .

Example answer:
{"entities": [{"text": "fucoidan", "type": "Chemical"}, {"text": "brain damage", "type": "Disease"}, {"text": "intracerebral hemorrhage", "type": "Disease"}]}

Example input:
Sentence: In contrast , SSR103800 failed to affect hyperactivity induced by amphetamine or naturally observed in dopamine transporter ( DAT ( -/- ) ) knockout mice ( 10-30 mg/kg p.o . ) .

Example answer:
{"entities": [{"text": "SSR103800", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "Disease"}, {"text": "METH", "type": "Chemical"}, {"text": "MPTP", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "METH-induced", "type": "Chemical"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Partial lesions were made with kainic acid in the interpeduncular nucleus of the ventral midbrain of the rat .

Example answer:
{"entities": [{"text": "kainic acid", "type": "Chemical"}]}

Example input:
Sentence: On the contrary , the cataleptogenic effect of haloperidol was significantly reduced in rats treated with desipramine and 6-OHDA but not in rats treated with 6-OHDA or in rats with lesions of the locus coeruleus .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "desipramine", "type": "Chemical"}, {"text": "6-OHDA", "type": "Chemical"}]}

Example input:
Sentence: In order to elucidate the role of the catecholaminergic system in the cataleptogenic effect of delta 9-tetrahydrocannabinol ( THC ) , the effect of pretreatment with 6-hydroxydopamine ( 6-OHDA ) or with desipramine and 6-OHDA and lesions of the locus coeruleus were investigated in rats .

Example answer:
{"entities": [{"text": "delta 9-tetrahydrocannabinol", "type": "Chemical"}, {"text": "THC", "type": "Chemical"}, {"text": "6-hydroxydopamine", "type": "Chemical"}, {"text": "6-OHDA", "type": "Chemical"}, {"text": "desipramine", "type": "Chemical"}]}

Example input:
Sentence: The cataleptogenic effect of THC was significantly reduced in rats treated with 6-OHDA and in rats with lesions of the locus coeruleus but not in rats treated with desipramine and 6-OHDA , as compared with control rats .

Example answer:
{"entities": [{"text": "THC", "type": "Chemical"}, {"text": "6-OHDA", "type": "Chemical"}, {"text": "desipramine", "type": "Chemical"}]}

Input:
Sentence: A lesion induced by 6-OHDA produced more severe motor deterioration in CB1 KO mice accompanied by more loss of DA neurons and increased PENK gene expression in the CPu .

## Item bc5cdr:test:3537
Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Disease"}]}

Example input:
Sentence: Histological and immunohistochemical investigations ( HE-LFB , CD-68 , Neurofilament ) revealed degeneration of myelin and axons as well as pseudocystic transformation in areas exposed to vincristine , accompanied by secondary changes with numerous prominent macrophages .

Example answer:
{"entities": [{"text": "pseudocystic transformation", "type": "Disease"}, {"text": "vincristine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Reversible inferior colliculus lesions could be considered as the characteristic for metronidazole-induced encephalopathy , next to the dentate nucleus involvement .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "Disease"}, {"text": "metronidazole-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: The pooled statistical analysis for ventricular septal ( VSD ) and midline ( MD ) defects was performed for rat fetuses exposed to piroxicam , selective and non-selective COX-2 inhibitor based on present and historic data .

Example answer:
{"entities": [{"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: Inappropriate use of carbamazepine and vigabatrin in typical absence seizures .

Example answer:
{"entities": [{"text": "carbamazepine", "type": "Chemical"}, {"text": "vigabatrin", "type": "Chemical"}, {"text": "absence seizures", "type": "Disease"}]}

Example input:
Sentence: Carbamazepine and vigabatrin are contraindicated in typical absence seizures .

Example answer:
{"entities": [{"text": "Carbamazepine", "type": "Chemical"}, {"text": "vigabatrin", "type": "Chemical"}, {"text": "absence seizures", "type": "Disease"}]}

Example input:
Sentence: Sub-chronic low dose gamma-vinyl GABA ( vigabatrin ) inhibits cocaine-induced increases in nucleus accumbens dopamine .

Example answer:
{"entities": [{"text": "gamma-vinyl GABA", "type": "Chemical"}, {"text": "vigabatrin", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: The authors present three patients with de novo absence epilepsy after administration of carbamazepine and vigabatrin .

Example answer:
{"entities": [{"text": "absence epilepsy", "type": "Disease"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "vigabatrin", "type": "Chemical"}]}

Example input:
Sentence: Vigabatrin was also used in the treatment of two children .

Example answer:
{"entities": [{"text": "Vigabatrin", "type": "Chemical"}]}

Example input:
Sentence: Absences were aggravated in both cases where vigabatrin was added on to concurrent treatment .

Example answer:
{"entities": [{"text": "vigabatrin", "type": "Chemical"}]}

Input:
Sentence: Binasal visual field defects are not specific to vigabatrin .

## Item bc5cdr:test:3533
Example input:
Sentence: Twenty-four patients with recurrent Grade I to IV astrocytomas , whose resection and irradiation therapy had failed , received two to eight courses of intra-arterial BCNU therapy .

Example answer:
{"entities": [{"text": "astrocytomas", "type": "Disease"}, {"text": "BCNU", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Six of 61 women ( 10 % ) developed clinically reversible grade 3 CHF following infusional cyclophosphamide with a median percent decline in ejection fraction of 31 % .

Example answer:
{"entities": [{"text": "CHF", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Head-up tilt caused systolic orthostatic hypotension which was marked in six of 20 PD patients on selegiline , one of whom lost consciousness with unrecordable blood pressures .

Example answer:
{"entities": [{"text": "systolic orthostatic hypotension", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "selegiline", "type": "Chemical"}]}

Example input:
Sentence: Propylthiouracil therapy was withdrawn , and she was treated with a 1-month course of prednisone , which alleviated her symptoms .

Example answer:
{"entities": [{"text": "Propylthiouracil", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}]}

Example input:
Sentence: Repeated cerebral perfusion SPECT scans revealed decreased basal ganglia perfusion while the movement disorder was present , and a return to normal perfusion when the rabbit syndrome resolved .

Example answer:
{"entities": [{"text": "decreased basal ganglia perfusion", "type": "Disease"}, {"text": "movement disorder", "type": "Disease"}, {"text": "rabbit syndrome", "type": "Disease"}]}

Example input:
Sentence: Lipopolysaccharide pretreatment did not affect the basal body temperature or methamphetamine-elicited hyperthermia three days later .

Example answer:
{"entities": [{"text": "Lipopolysaccharide", "type": "Chemical"}, {"text": "methamphetamine-elicited", "type": "Chemical"}, {"text": "hyperthermia", "type": "Disease"}]}

Example input:
Sentence: Following major intracranial surgery in a 35-year-old man , sodium pentothal was intravenously infused to minimize cerebral ischaemia .

Example answer:
{"entities": [{"text": "sodium pentothal", "type": "Chemical"}, {"text": "cerebral ischaemia", "type": "Disease"}]}

Example input:
Sentence: He was hospitalized for a myocardial infarction with pulmonary edema , treated with high-dose diuretics .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "pulmonary edema", "type": "Disease"}]}

Example input:
Sentence: At presentation , advanced encephalopathy and cerebral edema were present in 51 ( 76 % ) and 29 ( 41.4 % ) patients , respectively .

Example answer:
{"entities": [{"text": "encephalopathy", "type": "Disease"}, {"text": "cerebral edema", "type": "Disease"}]}

Example input:
Sentence: An allergic reaction consisting of angioneurotic edema secondary to continuous infusion 5-fluorouracil occurred in a patient with recurrent carcinoma of the oral cavity , cirrhosis , and cisplatin-induced impaired renal function .

Example answer:
{"entities": [{"text": "allergic reaction", "type": "Disease"}, {"text": "angioneurotic edema", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "carcinoma of the oral cavity", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "impaired renal function", "type": "Disease"}]}

Input:
Sentence: At re-warming , patient had resolution of her cerebral edema and intracranial hypertension .
