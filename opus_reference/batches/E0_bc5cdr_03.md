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

## Item bc5cdr:test:1431
Input:
Sentence: Protective effect of clentiazem against epinephrine-induced cardiac injury in rats .

## Item bc5cdr:test:1560
Input:
Sentence: Lamivudine is effective in suppressing hepatitis B virus DNA in Chinese hepatitis B surface antigen carriers : a placebo-controlled trial .

## Item bc5cdr:test:1561
Input:
Sentence: Lamivudine is a novel 2',3'-dideoxy cytosine analogue that has potent inhibitory effects on hepatitis B virus replication in vitro and in vivo .

## Item bc5cdr:test:1786
Input:
Sentence: The skin tests revealed positive delayed reactions of 24 hours and 48 hours by IDR and patch tests to only some PRC with common chains in their structures .

## Item bc5cdr:test:1795
Input:
Sentence: In 25 out of 32 episodes ( 78 % ) , plasma ammonium levels and mental status returned to normal within 2 days after adequate management .

## Item bc5cdr:test:657
Input:
Sentence: The effects of oral administration of caffeine ( 10 mg/kg ) on behavioral ratings , somatic symptoms , blood pressure and plasma levels of 3-methoxy-4-hydroxyphenethyleneglycol ( MHPG ) and cortisol were determined in 17 healthy subjects and 21 patients meeting DSM-III criteria for agoraphobia with panic attacks or panic disorder .

## Item bc5cdr:test:1455
Input:
Sentence: As this schedule exerted more toxicity than needed to investigate protective agents , the protection of ICRF-187 was determined using a dose schedule with lower general toxicity ( 6 weekly doses of 4 mg/kg doxorubicin given i.v .

## Item bc5cdr:test:1253
Input:
Sentence: Levodopa-induced dyskinesias are improved by fluoxetine .

## Item bc5cdr:test:1240
Input:
Sentence: Indomethacin-induced hyperkalemia in three patients with gouty arthritis .

## Item bc5cdr:test:1708
Input:
Sentence: MATERIALS AND METHODS : Carbetocin was given as an intramuscular injection immediately after the birth of the infant in 45 healthy women with normal singleton pregnancies who delivered vaginally at term .

## Item bc5cdr:test:1469
Input:
Sentence: VT appeared in fewer dogs and at a later time , and there were more sinoatrial beats and less ectopies .

## Item bc5cdr:test:1584
Input:
Sentence: FINDINGS : 85 women met the inclusion criteria for VTE , two of whom were users of progestagen-only OCs .

## Item bc5cdr:test:1834
Input:
Sentence: Cells were treated for 0-24 h with each compound ( 0-200 microM ) .

## Item bc5cdr:test:1470
Input:
Sentence: Epinephrine shortened QT less after bupivacaine than in control animals .

## Item bc5cdr:test:1667
Input:
Sentence: For this purpose , experimental conditions were created in which NSAIDs had previously been observed to produce effects on phasic and tonic pain by either central or peripheral mechanisms .

## Item bc5cdr:test:1491
Input:
Sentence: This report describes a case of encephalopathy developed in the course of amitriptyline therapy , during a remission of unipolar depression .

## Item bc5cdr:test:1857
Input:
Sentence: Reduced nicotinamide adenine dinucleotide phosphate-diaphorase ( NADPH-d ) histochemistry was also employed to visualize NOS as an index of enzyme expression in mice brain regions related to motor control .

## Item bc5cdr:test:1497
Input:
Sentence: Ten weeks of diethylstilbestrol ( DES ) treatment caused female F344 rat pituitaries to grow to an average of 109.2 +/- 6.3 mg ( mean +/- SE ) versus 11.3 +/- 1.4 mg for untreated rats , and to become highly hemorrhagic .

## Item bc5cdr:test:1736
Input:
Sentence: Clinical assessment as well as blinded ratings of Unified Parkinson 's Disease Rating Scale ( UPDRS ) scores were carried out pre- and postoperatively .

## Item bc5cdr:test:1682
Input:
Sentence: Among 3,129 dobutamine stress echocardiographic studies , a hypertensive response , defined as systolic blood pressure ( BP ) > or = 220 mm Hg and/or diastolic BP > or = 110 mm Hg , occurred in 30 patients ( 1 % ) .

## Item bc5cdr:test:1742
Input:
Sentence: Gamma Knife pallidotomy is as effective as radiofrequency pallidotomy in controlling certain of the symptoms of Parkinson 's disease .

## Item bc5cdr:test:1738
Input:
Sentence: 85 percent of patients with dyskinesias were relieved of symptoms , regardless of whether the pallidotomies were performed with the Gamma Knife or radiofrequency methods .

## Item bc5cdr:test:1492
Input:
Sentence: This patient could have been diagnosed as having either neuroleptic malignant syndrome ( NMS ) or serotonin syndrome ( SS ) .

## Item bc5cdr:test:1368
Input:
Sentence: The SOD-induced increase in glomerular filtration rate was associated with a marked improvement in RBF , an increase in urinary cGMP excretion , and a decrease in renal renin and endothelin-1 content .

## Item bc5cdr:test:1887
Input:
Sentence: The association was stronger with longer duration of use when compared to shorter duration of use and was more pronounced in recent users than in remote users .

## Item bc5cdr:test:1692
Input:
Sentence: We conclude that CNA and INA demonstrated similar profiles with regard to safety , morbidity , and mortality .

## Item bc5cdr:test:771
Input:
Sentence: Cardiac symptoms , including hypotension , developed in three patients with advanced colorectal carcinoma while being treated with cisplatin ( CDDP ) and 5-fluorouracil ( 5-FU ) .

## Item bc5cdr:test:1928
Input:
Sentence: We report 4 cases , one of them in a previously healthy person .

## Item bc5cdr:test:1917
Input:
Sentence: Patients in group A had significant mortality at 2-year follow-up ( 28 % ) , in contrast to zero mortality in the other three groups .

## Item bc5cdr:test:1934
Input:
Sentence: We communicate a case in a previously healthy person , a fact not found in the recent literature .

## Item bc5cdr:test:1341
Input:
Sentence: We describe a 47-year-old woman with an acute myocardial infarction after administration of sumatriptan 6 mg subcutaneously for cluster headache .

## Item bc5cdr:test:1715
Input:
Sentence: The majority of additional administration of oxytocics ( 4/5 ) and blood transfusion ( 3/5 ) occurred in the dose groups of 200 microg .

## Item bc5cdr:test:1972
Input:
Sentence: There were no statistically significant differences in EPSs between groups .

## Item bc5cdr:test:1781
Input:
Sentence: The mechanisms of proarrhythmic effects of Dubutamine are discussed .

## Item bc5cdr:test:1980
Input:
Sentence: Useful Field of View ( UFOV -- a test of visual attention ) was also undertaken .

## Item bc5cdr:test:1978
Input:
Sentence: A driving simulator ( Transport Research Laboratory ) was used to measure reaction time ( RT ) , speed maintenance and steering accuracy .

## Item bc5cdr:test:1775
Input:
Sentence: Both systolic and diastolic blood pressures of these 13 patients were decreased significantly after 4 weeks of nifedipine therapy , and blood pressure was maintained within the normal range thereafter for 25 months .

## Item bc5cdr:test:1993
Input:
Sentence: A randomised , double-blind , placebo-controlled , crossover study design was employed .

## Item bc5cdr:test:1106
Input:
Sentence: It is concluded that anticholinesterases are only partially effective in restoring neuromuscular function in succinylcholine apnoea despite muscle twitch activity typical of phase II block .

## Item bc5cdr:test:1532
Input:
Sentence: The improvement in GFR was not associated with enhanced glomerular hypertrophy or increased segmental glomerulosclerosis , tubulointerstitial injury , or renal cortical malondialdehyde content .

## Item bc5cdr:test:2007
Input:
Sentence: Withdrawals occurred in 27.1 % of the high- and 30.7 % of the low-dose groups .

## Item bc5cdr:test:1157
Input:
Sentence: A case of nontraumatic dissecting aneurysm of the basilar artery in association with hypertension , smoke , and oral contraceptives is reported in a young female patient with a locked-in syndrome .

## Item bc5cdr:test:1592
Input:
Sentence: The increased odds ratio associated with products containing 20 micrograms ethinyloestradiol and desogestrel compared with the 30 micrograms product is biologically implausible , and is likely to be the result of preferential prescribing and , thus , confounding .

## Item bc5cdr:test:1596
Input:
Sentence: Intraperitoneal injection of pilocarpine ( 400 mg/kg ) induced tonic and clonic seizure .

## Item bc5cdr:test:1441
Input:
Sentence: In conclusion , clentiazem attenuated epinephrine-induced cardiac injury , possibly through its effect on the adrenergic pathway .

## Item bc5cdr:test:1739
Input:
Sentence: About 2/3 of the patients in both Gamma Knife and radiofrequency groups showed improvements in bradykinesia and rigidity , although when considered as a group neither the Gamma Knife nor the radiofrequency group showed statistically significant improvements in UPDRS scores .

## Item bc5cdr:test:1758
Input:
Sentence: A clear reduction of BS synthesis was found in bile-diverted rats treated with EE , yet biliary BS composition was only minimally affected .

## Item bc5cdr:test:1623
Input:
Sentence: Induction of the ventricular tachyarrhythmia was prevented by oral d , l-sotalol in 35 ( 43 % ) patients ; the ventricular tachyarrhythmia remained inducible in 40 ( 49 % ) patients ; and two ( 2.5 % ) patients did not tolerate even 40 mg of d , l-sotalol once daily .

## Item bc5cdr:test:1939
Input:
Sentence: Although there have been case reports of epidural morphine with these symptoms and signs , this has not been previously documented with IV or patient-controlled analgesia morphine .

## Item bc5cdr:test:1683
Input:
Sentence: Patients with this response more often had a history of hypertension and had higher resting systolic and diastolic BP before dobutamine infusion .

## Item bc5cdr:test:1695
Input:
Sentence: He gave a five-year history of polyuria and polydipsia , during which time urinalysis had been negative for glucose .

## Item bc5cdr:test:1943
Input:
Sentence: Heart rate ( HR ) , mean arterial pressure ( MBP ) , positive rate of increase of left ventricular pressure ( +LVdP/dt ) , echocardiographically assessed left ventricular ejection fraction ( LVEF ) , and fractional shortening ( FS ) , as well as chronotropic response to isoproterenol and exercise-induced sympathetic stimulation were evaluated under baseline and posttreatment conditions .

## Item bc5cdr:test:1751
Input:
Sentence: This is the first reported patient with neuroleptic malignant syndrome probably caused by methylphenidate .

## Item bc5cdr:test:1905
Input:
Sentence: RESULTS : The patient had episodic deterioration of vision in both eyes , with clinical features resembling ischemic optic neuropathies .

## Item bc5cdr:test:2059
Input:
Sentence: METHODS AND RESULTS : Transmembrane action potentials from epicardium , midmyocardium , and endocardium were recorded simultaneously , together with a transmural ECG , in arterially perfused canine and rabbit left ventricular preparations .

## Item bc5cdr:test:1973
Input:
Sentence: However , olanzapine-treated patients had a statistically significant greater mean ( +/- SD ) weight gain than placebo-treated patients ( 2.1 +/- 2.8 vs 0.45 +/- 2.3 kg , respectively ) and also experienced more treatment-emergent somnolence ( 21 patients [ 38.2 % ] vs 5 [ 8.3 % ] , respectively ) .

## Item bc5cdr:test:2012
Input:
Sentence: In combination , these substances are substantially more toxic than either drug alone .

## Item bc5cdr:test:1507
Input:
Sentence: Chemical cystitis was induced by cyclophosphamide ( CYP ) which is metabolized to acrolein , an irritant eliminated in the urine .

## Item bc5cdr:test:2074
Input:
Sentence: All patients were admitted to the hospital for serial testing after the DSE testing in the intensive diagnostic and treatment unit .

## Item bc5cdr:test:1995
Input:
Sentence: Methoxamine evoked non-significant increases in MUP and diastolic blood pressure but caused a significant rise in systolic blood pressure and significant fall in heart rate at maximum dosage .

## Item bc5cdr:test:1593
Input:
Sentence: MK-801 augments pilocarpine-induced electrographic seizure but protects against brain damage in rats .

## Item bc5cdr:test:2003
Input:
Sentence: Patients with New York Heart Association classes II to IV CHF and left ventricular ejection fractions of no greater than 0.30 ( n = 3164 ) were randomized and followed up for a median of 46 months .

## Item bc5cdr:test:1836
Input:
Sentence: Results were confirmed by determination of internucleosomal DNA fragmentation using gel electrophoresis for HL60 cell samples and terminal deoxynucleotidyl transferase assay in HBMP cells .

## Item bc5cdr:test:2091
Input:
Sentence: This result is consistent with results of similar studies in term infants .

## Item bc5cdr:test:1864
Input:
Sentence: DESIGN : A randomised crossover study of recovery time of systolic and diastolic left ventricular function after exercise and dobutamine induced ischaemia .

## Item bc5cdr:test:2026
Input:
Sentence: We emphasize the anti-dopaminergic effect of veralipride .

## Item bc5cdr:test:1811
Input:
Sentence: Nociceptin , also known as orphanin FQ , is an endogenous ligand for the orphan opioid receptor-like receptor 1 ( ORL1 ) and involves in various functions in the central nervous system ( CNS ) .

## Item bc5cdr:test:1526
Input:
Sentence: Therefore , we examined whether recombinant human ( rh ) IGF-I is a safer alternative for the treatment of growth failure in rats with chronic PAN nephropathy .

## Item bc5cdr:test:1865
Input:
Sentence: SUBJECTS : 10 patients with stable angina , angiographically proven coronary artery disease , and normal left ventricular function .

## Item bc5cdr:test:1892
Input:
Sentence: Heparin , first used to prevent the clotting of blood in vitro , has been clinically used to treat thrombosis for more than 50 years .

## Item bc5cdr:test:2110
Input:
Sentence: Auditory thresholds were tested by evoked auditory brain stem responses at 1 month after birth .

## Item bc5cdr:test:1882
Input:
Sentence: Patients with no identifiable cause of pulmonary hypertension were classed as PPH .

## Item bc5cdr:test:1835
Input:
Sentence: Apoptosis was assessed by fluorescence microscopy in Hoechst 33342- and propidium iodide stained cell samples .

## Item bc5cdr:test:2134
Input:
Sentence: The overall response rate was 38 % , the median time to response was 10 weeks , the median duration of response was 26 weeks , and the median survival was 37 weeks .

## Item bc5cdr:test:1750
Input:
Sentence: A relative gamma-aminobutyric acid-ergic deficiency might occur because diazepam , a gamma-aminobutyric acid-mimetic agent , was strikingly effective .

## Item bc5cdr:test:2144
Input:
Sentence: The WHO reported 82 cases .

## Item bc5cdr:test:2049
Input:
Sentence: Decreased left ventricular systolic function was demonstrated in 5 ( 14 % ) patients , but in none of the controls ( p = 0.055 ) .

## Item bc5cdr:test:1536
Input:
Sentence: We conclude that : 1 ) administration of rhIGF-I improves growth and GFR in rats with chronic PAN nephropathy and 2 ) unlike rhGH , long-term use of rhIGF-I does not worsen renal functional and structural injury in this disease model .

## Item bc5cdr:test:1899
Input:
Sentence: Although reasonable incidences of many of these side effects can be `` softly '' deduced from current reports dealing with unfractionated heparin , at present the incidences of these side effects with newer low molecular weight heparins appear to be much less common .

## Item bc5cdr:test:2061
Input:
Sentence: Azimilide , however , significantly prolonged APD and QT interval at concentrations from 0.1 to 10 micromol/L but shortened them at 30 micromol/L .

## Item bc5cdr:test:1986
Input:
Sentence: CONCLUSIONS : Pupillary dilation may lead to a decrease in vision and daylight driving performance in young people .

## Item bc5cdr:test:2178
Input:
Sentence: At each time point , systolic blood pressure ( BP ) , urinary protein excretion and renal histopathological findings were evaluated , and morphometric image analysis was done .

## Item bc5cdr:test:2085
Input:
Sentence: Infants were categorized into 1 of 2 groups : those exposed to cocaine and those not exposed to cocaine .

## Item bc5cdr:test:2183
Input:
Sentence: There was a significant correlation between urinary protein excretion and GSI ( r = 0.808 , p < 0.0001 ) .

## Item bc5cdr:test:1372
Input:
Sentence: These results suggest that 1 ) both SOD and DMTU have protective effects on GM-mediated nephropathy , 2 ) the mechanisms for the protective effects differ for SOD and DMTU , and 3 ) superoxide anions play a critical role in GM-induced renal vasoconstriction .

## Item bc5cdr:test:2207
Input:
Sentence: Mast cells appeared in the connective and muscular layers of the bladder at a much higher number in DBA/2 mice than in C57BL/6 mice or untreated controls .

## Item bc5cdr:test:2001
Input:
Sentence: The present study examines the safety and tolerability of high- compared with low-dose lisinopril in CHF .

## Item bc5cdr:test:2021
Input:
Sentence: CONCLUSIONS : Cocaine and ethanol in combination were more toxic than either substance alone .

## Item bc5cdr:test:1802
Input:
Sentence: Quinine is known to block voltage- , calcium- and ATP-sensitive K ( + ) -channels while 4-aminopyridine is known to block voltage-sensitive K ( + ) -channels .

## Item bc5cdr:test:2221
Input:
Sentence: Patients ' characteristics were : male/female ratio 20/13 ; median age 57 ( 27-75 ) years ; median WHO status 1 ( 0-2 ) .

## Item bc5cdr:test:2088
Input:
Sentence: The incidence of subependymal cysts in the 117 remaining infants was 14 % ( 16 of 117 ) .

## Item bc5cdr:test:1861
Input:
Sentence: CONCLUSIONS : The results give further support to the hypothesis that NO plays a role in motor behavior control and suggest that it may take part in the synaptic changes produced by antipsychotic treatment .

## Item bc5cdr:test:2098
Input:
Sentence: Thalidomide was discontinued in 55 patients for lack of therapeutic response .

## Item bc5cdr:test:2284
Input:
Sentence: These results were explained by an asymmetric cerebral blood flow depending upon the paw preference in rats .

## Item bc5cdr:test:2099
Input:
Sentence: Of 67 patients initially enrolled , 24 remained on thalidomide for 3 months , 8 remained at 6 months , and 3 remained at 9 months .

## Item bc5cdr:test:2046
Input:
Sentence: Prevalence of heart disease in asymptomatic chronic cocaine users .

## Item bc5cdr:test:1474
Input:
Sentence: Bupivacaine antagonizes epinephrine dysrhythmogenicity in conscious dogs susceptible to VT and in anesthetized dogs with spontaneous postinfarct dysrhythmias .

## Item bc5cdr:test:2027
Input:
Sentence: Viracept and irregular heartbeat warning .

## Item bc5cdr:test:1044
Input:
Sentence: Intraperitoneal administration of cholecystokinin octapeptide sulphate ester ( CCK-8-SE ) and nonsulphated cholecystokinin octapeptide ( CCK-8-NS ) enhanced the latency of seizures induced by picrotoxin in mice .

## Item bc5cdr:test:2112
Input:
Sentence: In the transgenic group , kanamycin increased the threshold by only 15 dB over the respective controls .
