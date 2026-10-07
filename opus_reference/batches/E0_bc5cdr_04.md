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

## Item bc5cdr:test:2142
Input:
Sentence: Twenty-one reports of antimicrobial-induced mania were found in the literature .

## Item bc5cdr:test:2129
Input:
Sentence: The relevance of these features for patients using PDN remains to be elucidated .

## Item bc5cdr:test:2338
Input:
Sentence: Patients underwent regular measurement of prostate-specific antigen ( PSA ) , urea and electrolytes , serum bFGF and VEGF .

## Item bc5cdr:test:2159
Input:
Sentence: However , in vivo and in vitro studies have demonstrated that myometrial cells are also targets of the relaxant effects of nitric oxide ( NO ) .

## Item bc5cdr:test:2072
Input:
Sentence: Patients were eligible for DSE if they had used cocaine within 24 hours preceding the onset of chest pain and had a normal ECG and tropinin I level .

## Item bc5cdr:test:1430
Input:
Sentence: As TNF and PAF are thought to be involved in the development of septic shock and adult respiratory distress syndrome , we hypothesize that high-dose Ara-C may be associated with cytokine release .

## Item bc5cdr:test:1388
Input:
Sentence: ANP did not cause significant changes in MAP in both strains as compared to vehicle , but it abolished AVP-induced MAP increase in WKY and SHR .

## Item bc5cdr:test:2177
Input:
Sentence: Temocapril ( 8 mg/kg/day ) was administered to the rats which were killed at weeks 4 , 14 or 20 .

## Item bc5cdr:test:1335
Input:
Sentence: S-312 , S-312-d , but not S-312-l , L-type calcium channel antagonists , showed anticonvulsant effects on the audiogenic tonic convulsions in DBA/2 mice ; and their ED50 values were 18.4 ( 12.8-27.1 ) mg/kg , p.o .

## Item bc5cdr:test:2203
Input:
Sentence: Inbred DBA/2 and C57BL/6 female mice were injected with CY , and the effect of the drug on the bladder was assessed during 100 days by light microscopy using different staining procedures , and after 30 days by conventional electron microscopy .

## Item bc5cdr:test:1589
Input:
Sentence: Among users of third-generation progestagens , the risk of VTE was higher in users of desogestrel with 20 g ethinyloestradiol than in users of gestodene or desogestrel with 30 g ethinyloestradiol .

## Item bc5cdr:test:2083
Input:
Sentence: We sought to determine if prenatal cocaine exposure increases the incidence of subependymal cysts in preterm infants .

## Item bc5cdr:test:1764
Input:
Sentence: Glibenclamide-sensitive hypotension produced by helodermin assessed in the rat .

## Item bc5cdr:test:2382
Input:
Sentence: The hypoventilation maneuver led to an increase in the arterial Paco2 , followed by an increase in VE .

## Item bc5cdr:test:2015
Input:
Sentence: METHODS : Twenty-three dogs were randomized to receive either 1 ) three intravenous ( IV ) boluses of cocaine 7.5 mg/kg with ethanol ( 1 g/kg ) as an IV infusion ( C+E , n = 8 ) , 2 ) three cocaine boluses only ( C , n = 6 ) , 3 ) ethanol infusion only ( E , n = 5 ) , or 4 ) placebo boluses and infusion ( n = 4 ) .

## Item bc5cdr:test:2391
Input:
Sentence: Serum levels of tumor necrosis factor-alpha and interferon-gamma were also determined by ELISA .

## Item bc5cdr:test:1597
Input:
Sentence: Scopolamine ( 10 mg/kg ) and pentobarbital ( 5 mg/kg ) prevented development of pilocarpine-induced behavioral seizure but MK-801 ( 0.5 mg/kg ) did not .

## Item bc5cdr:test:2090
Input:
Sentence: CONCLUSIONS : We found an increased incidence of subependymal cyst formation in preterm infants who were exposed to cocaine prenatally .

## Item bc5cdr:test:2008
Input:
Sentence: Subgroups presumed to be at higher risk for ACE inhibitor intolerance ( blood pressure , < 120 mm Hg ; creatinine , > or =132.6 micromol/L [ > or =1.5 mg/dL ] ; age , > or =70 years ; and patients with diabetes ) generally tolerated the high-dose strategy .

## Item bc5cdr:test:1381
Input:
Sentence: The purpose of the present study was to compare influence of central arginine vasopressin ( AVP ) and of atrial natriuretic peptide ( ANP ) on control of arterial blood pressure ( MAP ) and heart rate ( HR ) in normotensive ( WKY ) and spontaneously hypertensive ( SHR ) rats .

## Item bc5cdr:test:1770
Input:
Sentence: These findings suggest that helodermin-produced hypotension is partly attributable to the activation of glibenclamide-sensitive K+ channels ( K ( ATP ) channels ) , which presumably exist on arterial smooth muscle cells .

## Item bc5cdr:test:2103
Input:
Sentence: Neuropathy may thus be a common complication of thalidomide in older patients .

## Item bc5cdr:test:2406
Input:
Sentence: The cognitive functions remained unchanged .

## Item bc5cdr:test:2404
Input:
Sentence: ( p < 0.0005 ) .

## Item bc5cdr:test:1390
Input:
Sentence: In SHR but not in WKY administration of ANP , AVP and ANP + AVP decreased CCB during Phe-induced MAP elevation .

## Item bc5cdr:test:2416
Input:
Sentence: Eyes subsequently enucleated because of treatment failure ( n = 4 ) were examined histologically .

## Item bc5cdr:test:1799
Input:
Sentence: The effects of quinine and 4-aminopyridine on conditioned place preference and changes in motor activity induced by morphine in rats .

## Item bc5cdr:test:2437
Input:
Sentence: All had reported incidents of being very embarrassed whilst eating hot spicy foods .

## Item bc5cdr:test:2446
Input:
Sentence: Plasma concentrations did not differ significantly between the two formulations .

## Item bc5cdr:test:2029
Input:
Sentence: Bradycardia occurred in a 45-year-old male patient who was Viracept in combination with other anti-HIV drugs .

## Item bc5cdr:test:2322
Input:
Sentence: Indomethacin-induced morphologic changes in the rat urinary bladder epithelium .

## Item bc5cdr:test:2321
Input:
Sentence: The finding of an augmented risk of pacemaker insertion in elderly women receiving amiodarone requires further investigation .

## Item bc5cdr:test:2326
Input:
Sentence: METHODS : Three groups were established : a control group ( n = 10 ) , a high-dose group ( n = 10 ) , treated with one intraperitoneal injection of indomethacin 20 mg/kg , and a therapeutic dose group ( n = 10 ) in which oral indomethacin was administered 3.25 mg/kg body weight daily for 3 weeks .

## Item bc5cdr:test:2031
Input:
Sentence: Frequency of appearance of myeloperoxidase-antineutrophil cytoplasmic antibody ( MPO-ANCA ) in Graves ' disease patients treated with propylthiouracil and the relationship between MPO-ANCA and clinical manifestations .

## Item bc5cdr:test:2497
Input:
Sentence: MA may selectively damage the medial temporal lobe and , consistent with metabolic studies , the cingulate-limbic cortex , inducing neuroadaptation , neuropil reduction , or cell death .

## Item bc5cdr:test:2080
Input:
Sentence: CONCLUSION : No exaggerated adrenergic response was detected when dobutamine was administered to patients with cocaine-related chest pain .

## Item bc5cdr:test:2063
Input:
Sentence: Although both dl-sotalol and azimilide rarely induced EADs in canine left ventricles , they produced frequent EADs in rabbits , in which more pronounced QT prolongation was seen .

## Item bc5cdr:test:1876
Input:
Sentence: Dobutamine induced ischaemia could therefore be used to study the pathophysiology of this phenomenon further in patients with coronary artery disease .

## Item bc5cdr:test:2380
Input:
Sentence: RESULTS : The hyperventilation maneuver caused a decrease in spontaneous ventilation in pilocarpine-treated and control rats .

## Item bc5cdr:test:2532
Input:
Sentence: A multiparous woman in good psychological health underwent urgent caesarean section in labour .

## Item bc5cdr:test:2254
Input:
Sentence: METHODS : Outcomes were examined in patients admitted for possible MI after cocaine use .

## Item bc5cdr:test:2385
Input:
Sentence: CONCLUSIONS : The data indicate that pilocarpine-treated animals have an altered ability to react to ( or compensate for ) blood gas changes with changes in ventilation and suggest that it is centrally determined .

## Item bc5cdr:test:1960
Input:
Sentence: Definite , although limited , antineoplastic activity is observed in patients with well-defined platinum- and paclitaxel-refractory ovarian cancer .

## Item bc5cdr:test:1727
Input:
Sentence: contrast material to enable diagnosis of ureteric stones or obstruction in patients with HIV infection who receive indinavir therapy .

## Item bc5cdr:test:2401
Input:
Sentence: Preoperative and postoperative assessments of these patients at 1 , 3 , 6 and 12 months follow-up , in `` on '' and `` off '' drug conditions , was carried out using Unified Parkinson 's Disease Rating Scale , Hoehn and Yahr staging , England activities of daily living score and video recordings .

## Item bc5cdr:test:2245
Input:
Sentence: CONCLUSIONS : Children treated with indinavir have a high cumulative incidence of persistent sterile leukocyturia .

## Item bc5cdr:test:2402
Input:
Sentence: RESULTS : After one year of electrical stimulation of the STN , the patients ' scores for activities of daily living and motor examination scores ( Unified Parkinson 's Disease Rating Scale parts II and III ) off medication improved by 62 % and 61 % respectively ( p < 0.0005 ) .

## Item bc5cdr:test:2555
Input:
Sentence: Patients who experience a fall in hemoglobin concentrations of 2 g/dL or more at week 2 after the start of treatment should be monitored with particular care .

## Item bc5cdr:test:2455
Input:
Sentence: We found 19 trials , involving 2441 patients treated by VNR and 2050 control patients .

## Item bc5cdr:test:2565
Input:
Sentence: The progressive nature of mitochondrial injury suggests that mitochondria , not other subcellular organelles , are the major site of intracellular injury .

## Item bc5cdr:test:2461
Input:
Sentence: However , the risk associated with VNR seems to be similar to that of other chemotherapeutic agents in the same indications .

## Item bc5cdr:test:2105
Input:
Sentence: Overexpression of copper/zinc-superoxide dismutase protects from kanamycin-induced hearing loss .

## Item bc5cdr:test:2496
Input:
Sentence: MRI-based maps suggest that chronic methamphetamine abuse causes a selective pattern of cerebral deterioration that contributes to impaired memory performance .

## Item bc5cdr:test:2325
Input:
Sentence: In addition to tiaprofenic acid , indomethacin has been reported to be associated with this condition .

## Item bc5cdr:test:2491
Input:
Sentence: Using magnetic resonance imaging ( MRI ) and new computational brain-mapping techniques , we determined the pattern of structural brain alterations associated with chronic MA abuse in human subjects and related these deficits to cognitive impairment .

## Item bc5cdr:test:2605
Input:
Sentence: The animals were killed 5 and 30 days after these injections and the kidneys were removed for histological and immunohistochemical studies .

## Item bc5cdr:test:1609
Input:
Sentence: 5-Fluorouracil plus folinic acid and paclitaxel ( Taxol ; Bristol-Myers Squibb Company , Princeton , NJ ) are effective salvage therapies for metastatic breast cancer patients .

## Item bc5cdr:test:2618
Input:
Sentence: Patients Fifty subjects signed informed consent and 41 underwent the frequently sampled intravenous glucose tolerance test .

## Item bc5cdr:test:2164
Input:
Sentence: Patients received up to 3 doses/day of 50 mg DCF or 2.5 mg/24 h transdermal GTN for the first 3 days of the cycle , according to their needs .

## Item bc5cdr:test:2527
Input:
Sentence: In isoproterenol administered rats , the level of lipid peroxides increased significantly in the serum and heart .

## Item bc5cdr:test:2114
Input:
Sentence: The protection by overexpression of superoxide dismutase supports the hypothesis that oxidant stress plays a significant role in aminoglycoside-induced ototoxicity .

## Item bc5cdr:test:2055
Input:
Sentence: Oral pre-treatment with PK ( 80 mg kg ( -1 ) day ( -1 ) for 15 days ) significantly prevented the isoproterenol-induced myocardial infarction and maintained the rats at near normal status .

## Item bc5cdr:test:2660
Input:
Sentence: RESULTS : Two hundred twenty-eight patients ( 42 % men ) with a mean age of 81.1 ( range 76-94 ) were included in the analysis .

## Item bc5cdr:test:2536
Input:
Sentence: We feel that , although the dramatic extrapyramidal side effects of dopaminergic antiemetics are well known , more subtle manifestations may easily be overlooked .

## Item bc5cdr:test:2185
Input:
Sentence: It appears that temocapril was effective in retarding renal progression and protected renal function in PAN neprotic rats .

## Item bc5cdr:test:2553
Input:
Sentence: Such factors as sex ( female ) , age ( > or =60 years old ) , and the ribavirin dose by body weight ( 12 mg/kg or more ) were significant by univariate analysis .

## Item bc5cdr:test:2411
Input:
Sentence: Ocular motility changes after subtenon carboplatin chemotherapy for retinoblastoma .

## Item bc5cdr:test:2342
Input:
Sentence: Adverse effects included constipation , morning drowsiness , dizziness and rash , and resulted in withdrawal from the study by three men .

## Item bc5cdr:test:1902
Input:
Sentence: PURPOSE : To report a case of bilateral optic neuropathy in a patient receiving tacrolimus ( FK 506 , Prograf ; Fujisawa USA , Inc , Deerfield , Illinois ) for immunosuppression after orthotropic liver transplantation .

## Item bc5cdr:test:2489
Input:
Sentence: We visualize , for the first time , the profile of structural deficits in the human brain associated with chronic methamphetamine ( MA ) abuse .

## Item bc5cdr:test:2289
Input:
Sentence: The objective of this investigation was to test the hypothesis that carvedilol , a nonselective beta-adrenergic receptor antagonist with potent antioxidant properties , protects against the cardiac and hepatic mitochondrial bioenergetic dysfunction associated with subchronic doxorubicin toxicity .

## Item bc5cdr:test:1916
Input:
Sentence: Patients with hypercalcemia resulting from medical diseases and bipolar patients with lithium-associated hypercalcemia had significantly higher frequencies of conduction defects .

## Item bc5cdr:test:2054
Input:
Sentence: The cardioprotective effect of the ethanol extract of Picrorrhiza kurroa rhizomes and roots ( PK ) on isoproterenol-induced myocardial infarction in rats with respect to lipid metabolism in serum and heart tissue has been investigated .

## Item bc5cdr:test:2687
Input:
Sentence: Controls were patients admitted to the same hospitals from where the cases arose , also matched by age and sex .

## Item bc5cdr:test:1517
Input:
Sentence: Effects of CD-832 on isoproterenol ( ISO ) -induced myocardial ischemia were studied in dogs with partial coronary stenosis of the left circumflex coronary artery and findings were compared with those for nifedipine or diltiazem .

## Item bc5cdr:test:2324
Input:
Sentence: Nonsteroidal anti-inflammatory drug-induced cystitis is a poorly recognized and under-reported condition .

## Item bc5cdr:test:2479
Input:
Sentence: We report on rosaceiform dermatitis as a complication of treatment with tacrolimus ointment .

## Item bc5cdr:test:2484
Input:
Sentence: In 1 patient with atopic dermatitis , telangiectatic and papular rosacea insidiously appeared after 5 months of treatment .

## Item bc5cdr:test:2705
Input:
Sentence: Animals were killed between 30 and 60 days later , and brain sections were processed for GAP43 immunohistochemistry .

## Item bc5cdr:test:2435
Input:
Sentence: All patients had gustatory hyperhidrosis , which interfered with their social activities , after transthroacic endoscopic sympathectomy , and which was associated with compensatory focal hyperhidrosis .

## Item bc5cdr:test:2336
Input:
Sentence: We undertook an open-label study using thalidomide 100 mg once daily for up to 6 months in 20 men with androgen-independent prostate cancer .

## Item bc5cdr:test:2718
Input:
Sentence: injections .

## Item bc5cdr:test:2720
Input:
Sentence: Locomotor activity was recorded for individual groups by using the same treatment protocol with the EPM test .

## Item bc5cdr:test:2349
Input:
Sentence: We describe 2 cases of grand mal seizures following accidental intravascular injection of levobupivacaine .

## Item bc5cdr:test:2501
Input:
Sentence: Amiodarone , an efficacious and widely used antiarrhythmic agent , has been reported to cause hepatotoxicity in some patients .

## Item bc5cdr:test:2737
Input:
Sentence: MAIN RESULTS : All the statistically significant results were derived from the two biggest trials .

## Item bc5cdr:test:2531
Input:
Sentence: A case of postoperative anxiety due to low dose droperidol used with patient-controlled analgesia .

## Item bc5cdr:test:1769
Input:
Sentence: Oxyhemoglobin did not affect helodermin-induced hypotension , whereas it shortened the duration of acetylcholine ( ACh ) -produced hypotension .

## Item bc5cdr:test:2430
Input:
Sentence: A low dose and prompt discontinuation of the drug is recommended particularly in individuals with diabetes mellitus , glaucoma or who are heavy smokers .

## Item bc5cdr:test:2631
Input:
Sentence: High-dose intravenous melphalan followed by peripheral blood stem cell transplant ( PBSCT ) appears to be the most promising therapy , but treatment mortality can be high .

## Item bc5cdr:test:2629
Input:
Sentence: BACKGROUND : Patients with primary systemic amyloidosis ( AL ) have a poor prognosis .

## Item bc5cdr:test:2546
Input:
Sentence: This study was conducted to identify the factors contributing to ribavirin-induced anemia .

## Item bc5cdr:test:2147
Input:
Sentence: Cases reported by the FDA showed clarithromycin and ciprofloxacin to be the most frequently associated with the development of mania .

## Item bc5cdr:test:2358
Input:
Sentence: The authors present a case of early ( within 4 days ) development of torsade de pointes ( TdP ) associated with oral amiodarone therapy .

## Item bc5cdr:test:2688
Input:
Sentence: Odds ratios were calculated using a conditional logistic model , including potential confounding factors , both for the whole study population and for the various underlying diseases .

## Item bc5cdr:test:1988
Input:
Sentence: A case of isotretinoin embryopathy with bilateral anotia and Taussig-Bing malformation .

## Item bc5cdr:test:2685
Input:
Sentence: METHODS : The cases were all patients entering the local dialysis program because of ESRD in the study area between June 1 , 1995 and November 30 , 1997 .

## Item bc5cdr:test:2723
Input:
Sentence: Administration of each drug and their combinations did not produce any effect on locomotor activity .

## Item bc5cdr:test:2417
Input:
Sentence: RESULTS : Limitation of ocular motility was detected in all 12 eyes of 10 patients treated for intraocular retinoblastoma with 1 to 6 injections of subtenon carboplatin as part of multimodality therapy .

## Item bc5cdr:test:2602
Input:
Sentence: BACKGROUND : Animals treated with gentamicin can show residual areas of interstitial fibrosis in the renal cortex .
