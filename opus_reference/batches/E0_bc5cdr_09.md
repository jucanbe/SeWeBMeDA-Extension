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

## Item bc5cdr:test:4556
Input:
Sentence: One week after the last DOX treatment ( acute stage ) , MHC-CB7 mice exhibited improved cardiac function and lower levels of cardiomyocyte apoptosis when compared with the NON-TXG mice .

## Item bc5cdr:test:4555
Input:
Sentence: METHODS AND RESULTS : Two-week-old MHC-CB7 mice ( which express dominant-interfering p53 in cardiomyocytes ) and their non-transgenic ( NON-TXG ) littermates received weekly DOX injections for 5 weeks ( 25 mg/kg cumulative dose ) .

## Item bc5cdr:test:4243
Input:
Sentence: CASE : We describe a second case of fluconazole associated agranulocytosis with thrombocytopenia and recovery upon discontinuation of therapy .

## Item bc5cdr:test:4559
Input:
Sentence: Mice with cardiomyocyte-restricted deletion of STAT3 exhibited worse cardiac function , higher levels of cardiomyocyte apoptosis , and a greater induction of Ku70 and Ku80 in response to DOX treatment during the acute stage when compared with control animals .

## Item bc5cdr:test:4519
Input:
Sentence: METHODS : S-53482 was administered dermally to rats at 30 , 100 , and 300 mg/kg during organogenesis , and S-23121 was administered at 200 , 400 , and 800 mg/kg ( the maximum applicable dose level ) .

## Item bc5cdr:test:4340
Input:
Sentence: On the contrary , though not clinically apparent , pethidine potentially causes inhibitory impacts on the CNS and impairs normal cerebellar and oculomotor function in the short term .

## Item bc5cdr:test:4018
Input:
Sentence: The impact of immune-mediated heparin-induced thrombocytopenia type II ( HIT type II ) as a cause of thrombocytopenia after liver transplantation is not yet understood , with few literature citations reporting contradictory results .

## Item bc5cdr:test:4710
Input:
Sentence: METHODS : This randomized , double-blinded study was conducted in 100 patients randomly allocated into five groups of 20 patients each .

## Item bc5cdr:test:4553
Input:
Sentence: Children are particularly sensitive to DOX-induced heart failure .

## Item bc5cdr:test:4277
Input:
Sentence: We report syncope and bradycardia in an 11-year-old girl following administration of intranasal dexmedetomidine for sedation for a voiding cystourethrogram .

## Item bc5cdr:test:4275
Input:
Sentence: We present a case of yellow phosphorus poisoning in which a patient presented with florid clinical features of cholestasis highlighting the fact that cholestasis can rarely be a presenting feature of yellow phosphorus hepatotoxicity .

## Item bc5cdr:test:4551
Input:
Sentence: P53 inhibition exacerbates late-stage anthracycline cardiotoxicity .

## Item bc5cdr:test:4724
Input:
Sentence: Western blot analysis revealed that AQP2 expression in medullary tissues was lowered after 3 and 5 days in WT mice ; however , AQP2 was unchanged in PKCa KO .

## Item bc5cdr:test:4725
Input:
Sentence: Similar results were observed with UT-A1 expression .

## Item bc5cdr:test:4383
Input:
Sentence: Valproate-induced hyperammonemic encephalopathy in a renal transplanted patient .

## Item bc5cdr:test:4489
Input:
Sentence: Postthrombectomy continuous CDT with alteplase was commenced while argatroban was withheld , and complete patency of the SVC and central veins was achieved after three days of therapy .

## Item bc5cdr:test:4312
Input:
Sentence: Independent predictors of postoperative seizures included age , female sex , redo cardiac surgery , calcification of ascending aorta , congestive heart failure , deep hypothermic circulatory arrest , duration of aortic cross-clamp and tranexamic acid .

## Item bc5cdr:test:4654
Input:
Sentence: The patient also received simvastatin .

## Item bc5cdr:test:4767
Input:
Sentence: Serum cardiac marker enzyme , histopathological variables and expression of protein levels were analyzed .

## Item bc5cdr:test:4576
Input:
Sentence: The results showed that aconitine stimulated apoptosis time-dependently .

## Item bc5cdr:test:4366
Input:
Sentence: On the basis of the findings reported herein , a dose of 60 mg/m ( 2 ) of CCNU combined with 250 mg/m ( 2 ) of CTX ( divided over 5 days ) q 4 wk is tolerable in tumor-bearing dogs .

## Item bc5cdr:test:4386
Input:
Sentence: Valproate-induced hyperammonemic encephalopathy is an uncommon but serious effect of valproate treatment .

## Item bc5cdr:test:4657
Input:
Sentence: The creatine kinase peaked at 62,246 IU/L and the patient was treated with intravenous normal saline .

## Item bc5cdr:test:4678
Input:
Sentence: Renal lesions were analyzed in hematoxylin and eosin , periodic acid-Schiff , and Masson 's trichrome stains .

## Item bc5cdr:test:4789
Input:
Sentence: Her symptoms improved through physical therapy but persisted to some degree .

## Item bc5cdr:test:4457
Input:
Sentence: Providers should similarly consider the likelihood of hypotension or bradycardia before starting either sedative .

## Item bc5cdr:test:4372
Input:
Sentence: She was re-induced with nelarabine 1500 mg/m ( 2 ) on days 1 , 3 , and 5 with 1 dose of IT cytarabine 100 mg on day 2 as central nervous system ( CNS ) prophylaxis .

## Item bc5cdr:test:4687
Input:
Sentence: Additionally , WT mice were treated with a B2 receptor antagonist after cisplatin administration .

## Item bc5cdr:test:4627
Input:
Sentence: GFC produced an increased latency to first seizure , at doses 25mg/kg ( 20.12 + 2.20 min ) , 50mg/kg ( 20.95 + 2.21 min ) or 75 mg/kg ( 23.43 + 1.99 min ) when compared with seized mice .

## Item bc5cdr:test:4694
Input:
Sentence: METHODS : A retrospective case series involving 11 birdshot retinochoroidopathy patients ( 11 eyes ) .

## Item bc5cdr:test:4387
Input:
Sentence: Here , we describe the case of a 15-year-old girl who was on a long-term therapy with valproate due to epilepsy and revealed impaired consciousness with hyperammonemia 12 days after renal transplantation .

## Item bc5cdr:test:4250
Input:
Sentence: AIMS : To investigate whether alterations of myocardial strain and high-sensitive cardiac troponin T ( cTnT ) could predict future cardiac dysfunction in patients after epirubicin exposure .

## Item bc5cdr:test:4836
Input:
Sentence: In order to conduct reliable testing in this regard , it is essential that a positive control for induction be available .

## Item bc5cdr:test:4441
Input:
Sentence: However , the Rg1 and Rb1 ginsenosides failed to prevent OIH in either test .

## Item bc5cdr:test:4573
Input:
Sentence: To investigate effects of aconitine on myocardial injury , we performed cytotoxicity assay in neonatal rat ventricular myocytes ( NRVMs ) , as well as measured lactate dehydrogenase level in the culture medium of NRVMs and activities of serum cardiac enzymes in rats .

## Item bc5cdr:test:4669
Input:
Sentence: Peripheral neuropathy was common ( 63 % ) , but severe grade 3-4 peripheral neuropathy was not observed .

## Item bc5cdr:test:4676
Input:
Sentence: Four animal groups ( n = 6 ) were tested during 9 weeks : control , CsA , SRL , and conversion ( CsA for 3 weeks followed by SRL for 6 weeks ) .

## Item bc5cdr:test:4613
Input:
Sentence: Testosterone ameliorates streptozotocin-induced memory impairment in male rats .

## Item bc5cdr:test:3992
Input:
Sentence: This depressive-like profile induced by METH was accompanied by a marked depletion of frontostriatal dopaminergic and serotonergic neurotransmission , indicated by a reduction in the levels of dopamine , DOPAC and HVA , tyrosine hydroxylase and serotonin , observed at both 3 and 49 days post-administration .

## Item bc5cdr:test:4797
Input:
Sentence: Maleate induced cell damage and reactive oxygen species ( ROS ) production in LLC-PK1 cells in culture .

## Item bc5cdr:test:4683
Input:
Sentence: Kinin B2 receptor deletion and blockage ameliorates cisplatin-induced acute renal injury .

## Item bc5cdr:test:4610
Input:
Sentence: Ethambutol is known to cause optic neuropathy and , more rarely , axonal polyneuropathy .

## Item bc5cdr:test:4493
Input:
Sentence: Effects of dehydroepiandrosterone in amphetamine-induced schizophrenia models in mice .

## Item bc5cdr:test:4511
Input:
Sentence: IKr and IKs blockers concentration-dependently prolonged corrected FPD ( FPDc ) , whereas Ca ( 2+ ) channel blockers concentration-dependently shortened FPDc .

## Item bc5cdr:test:4672
Input:
Sentence: The VTD regimen may be safe and effective as a consolidation therapy in the treatment of MM in Japanese population .

## Item bc5cdr:test:4814
Input:
Sentence: METHODS : We used logistic regression to determine the associations of these pollutants with self-reported , doctor-diagnosed Parkinson 's disease .

## Item bc5cdr:test:4361
Input:
Sentence: Neutropenia was the principal toxic effect , and the overall frequency of grade 4 neutropenia after the first treatment of CCNU/CTX was 30 % ( 95 % confidence interval , 19-43 % ) .

## Item bc5cdr:test:4824
Input:
Sentence: A rat model of IUGR was established by PCE , male fetuses and adult offspring at the age of postnatal week 24 were euthanized .

## Item bc5cdr:test:4227
Input:
Sentence: METHODS : Rats were anaesthetised with ketamine and were given 0.5 mg/kg/min propofol in intralipid ( Group P ) , propofol in medialipid ( Group L ) , or saline ( Group C ) over 20 min .

## Item bc5cdr:test:4758
Input:
Sentence: A total of 350 patients ( 215 [ 61.4 % ] < 5 years of age and 135 [ 38.6 % ] > 5 years of age ) were followed-up after treatment with injectable artesunate for severe malaria in hospitals and health centers of the Democratic Republic of the Congo .

## Item bc5cdr:test:4329
Input:
Sentence: In the preceding months , the patient had a number of admissions with transient unilateral hemiparesis with facial droop , and had been started on valproate for presumed hemiplegic migraine .

## Item bc5cdr:test:4736
Input:
Sentence: We conclude that amlodipine can cause dysguesia .

## Item bc5cdr:test:4205
Input:
Sentence: Concerns about long-term methotrexate ( MTX ) neurotoxicity in the 1990s led to modifications in intrathecal ( IT ) therapy , leucovorin rescue , and frequency of systemic MTX administration in children with acute lymphoblastic leukemia .

## Item bc5cdr:test:4408
Input:
Sentence: Intradermal glutamate and capsaicin injections : intra- and interindividual variability of provoked hyperalgesia and allodynia .

## Item bc5cdr:test:4740
Input:
Sentence: This particular case is of interest as rhabdomyolysis only occurred after an increase in the dose of clarithromycin .

## Item bc5cdr:test:4855
Input:
Sentence: Inorganic As exposure during key developmental periods is associated with a variety of adverse health effects including those that are evident in adulthood .

## Item bc5cdr:test:4583
Input:
Sentence: In the present study , the effect of chronic pre-treatment with metformin on cardiac dysfunction and toll-like receptor 4 ( TLR4 ) activities following myocardial infarction and their relation with AMPK were assessed .

## Item bc5cdr:test:4811
Input:
Sentence: Newly identified links to kidney cancer and associations with aggressive prostate cancer require further evaluation .

## Item bc5cdr:test:4853
Input:
Sentence: Mechanisms Underlying Latent Disease Risk Associated with Early-Life Arsenic Exposure : Current Research Trends and Scientific Gaps .

## Item bc5cdr:test:4784
Input:
Sentence: MATERIAL AND METHOD : A 40-year-old woman presented with decreased sensation and paresthesia over her right lateral forearm ; the paresthesia had occurred after a steroid injection in the right lateral epicondyle 3 months before .

## Item bc5cdr:test:4443
Input:
Sentence: Our data suggested that the ginsenoside Re , but not Rg1 or Rb1 , may contribute toward reversal of OIH .

## Item bc5cdr:test:4497
Input:
Sentence: Amphetamine ( 3 mg/kg ip ) induced hyper locomotion , apomorphine ( 1.5 mg/kg subcutaneously [ sc ] ) induced climbing , and haloperidol ( 1.5 mg/kg sc ) induced catalepsy tests were used as animal models of schizophrenia .

## Item bc5cdr:test:4716
Input:
Sentence: The onset time of succinylcholine was significantly longer with increasing the amount of precurarizing dose of rocuronium ( P < 0.001 ) .

## Item bc5cdr:test:4704
Input:
Sentence: Adverse events included increased intraocular pressure ( 54.5 % ) and cataract formation ( 100 % ) .

## Item bc5cdr:test:4600
Input:
Sentence: A metoprolol-terbinafine combination induced bradycardia .

## Item bc5cdr:test:4739
Input:
Sentence: Clarithromycin is the most documented cytochrome P450 3A4 ( CYP3A4 ) inhibitor to cause an adverse interaction with simvastatin .

## Item bc5cdr:test:4608
Input:
Sentence: By inhibiting the cytochrome P450 2D6 , terbinafine had decreased metoprolol 's clearance , leading in metoprolol accumulation which has resulted in clinically significant sinus bradycardia .

## Item bc5cdr:test:4625
Input:
Sentence: However , there is no research on GFC effects in the central nervous system of rodents .

## Item bc5cdr:test:4692
Input:
Sentence: Safety and efficacy of fluocinolone acetonide intravitreal implant ( 0.59 mg ) in birdshot retinochoroidopathy .

## Item bc5cdr:test:4850
Input:
Sentence: An earlier suggestion of increased lung cancer risk at high levels of metolachlor use in this cohort was not confirmed in this update .

## Item bc5cdr:test:4480
Input:
Sentence: Use of argatroban and catheter-directed thrombolysis with alteplase in an oncology patient with heparin-induced thrombocytopenia with thrombosis .

## Item bc5cdr:test:4693
Input:
Sentence: PURPOSE : To report the treatment outcomes of the fluocinolone acetonide intravitreal implant ( 0.59 mg ) in patients with birdshot retinochoroidopathy whose disease is refractory or intolerant to conventional immunomodulatory therapy .

## Item bc5cdr:test:4719
Input:
Sentence: Lithium , an effective antipsychotic , induces nephrogenic diabetes insipidus ( NDI ) in 40 % of patients .

## Item bc5cdr:test:4769
Input:
Sentence: Western blot analysis showed that isoproterenol-induced phosphorylation of STAT3 was maintained or further enhanced by betaine treatment in myocardium .

## Item bc5cdr:test:4841
Input:
Sentence: UNASSIGNED : Metolachlor , a widely used herbicide , is classified as a Group C carcinogen by the U.S. Environmental Protection Agency based on increased liver neoplasms in female rats .

## Item bc5cdr:test:4747
Input:
Sentence: Here , we report a case of prolonged neuromuscular block after administration of suxamethonium leading to the discovery of a novel BCHE variant ( c.695T > A , p.Val204Asp ) .

## Item bc5cdr:test:4857
Input:
Sentence: OBJECTIVES : This work summarizes research on the molecular mechanisms that underlie the increased risk of cancer development in adulthood that is associated with early-life iAs exposure .

## Item bc5cdr:test:4776
Input:
Sentence: A case of a patient with hepatocellular carcinoma that developed neutropenia after treatment with quetiapine is described here .

## Item bc5cdr:test:4549
Input:
Sentence: We found that metformin suppressed the progression of kindling , ameliorated the cognitive impairment and decreased brain oxidative stress .

## Item bc5cdr:test:4858
Input:
Sentence: DISCUSSION : Epigenetic reprogramming that imparts functional changes in gene expression , the development of cancer stem cells , and immunomodulation are plausible underlying mechanisms by which early-life iAs exposure elicits latent carcinogenic effects .

## Item bc5cdr:test:4766
Input:
Sentence: Acute myocardial ischemic injury was induced in rats by subcutaneous injection of isoproterenol ( 85 mg/kg ) , for two consecutive days .

## Item bc5cdr:test:4628
Input:
Sentence: In addition , GABA content of mice hippocampus treated with GFC75 plus P400 showed an increase of 46.90 % when compared with seized mice .

## Item bc5cdr:test:4232
Input:
Sentence: The cumulative bupivacaine dose given at those time points was higher in Group P. Plasma bupivacaine levels were significantly lower in Group P than in Group C. Bupivacaine levels in the brain and heart were significantly lower in Group P and Group L than in Group C. CONCLUSION : We conclude that pre-treatment with propofol in intralipid , compared with propofol in medialipid or saline , delayed the onset of bupivacaine-induced cardiotoxic effects as well as reduced plasma bupivacaine levels .

## Item bc5cdr:test:4481
Input:
Sentence: PURPOSE : The case of an oncology patient who developed heparin-induced thrombocytopenia with thrombosis ( HITT ) and was treated with argatroban plus catheter-directed thrombolysis ( CDT ) with alteplase is presented .

## Item bc5cdr:test:4792
Input:
Sentence: Curcumin prevents maleate-induced nephrotoxicity : relation to hemodynamic alterations , oxidative stress , mitochondrial oxygen consumption and activity of respiratory complex I .

## Item bc5cdr:test:4801
Input:
Sentence: It is concluded that curcumin is able to attenuate in vivo maleate-induced nephropathy and in vitro cell damage .

## Item bc5cdr:test:4662
Input:
Sentence: Simvastatin plasma concentration increased 30 times in this patient and statin induced muscle toxicity is related to the concentration of the statin in blood .

## Item bc5cdr:test:4539
Input:
Sentence: Metformin protects against seizures , learning and memory impairments and oxidative damage induced by pentylenetetrazole-induced kindling in mice .

## Item bc5cdr:test:4846
Input:
Sentence: We saw no association between metolachlor use and incidence of all cancers combined ( n = 5,701 with a 5-year lag ) or most site-specific cancers .

## Item bc5cdr:test:4721
Input:
Sentence: Targeting an alternative signaling pathway , such as PKC-mediated signaling , may be an effective method of treating lithium-induced polyuria .

## Item bc5cdr:test:4468
Input:
Sentence: A 62-year-old man was found to have bradycardia , hypothermia and respiratory failure 3 weeks after initiation of amiodarone therapy for atrial fibrillation .

## Item bc5cdr:test:4798
Input:
Sentence: In addition , maleate treatment reduced oxygen consumption in ADP-stimulated mitochondria and diminished respiratory control index when using malate/glutamate as substrate .

## Item bc5cdr:test:4763
Input:
Sentence: Regulation of signal transducer and activator of transcription 3 and apoptotic pathways by betaine attenuates isoproterenol-induced acute myocardial injury in rats .

## Item bc5cdr:test:4631
Input:
Sentence: The results indicate that GFC can exert anticonvulsant activity and reduce the frequency of installation of pilocarpine-induced status epilepticus , as demonstrated by increase in latency to first seizure and decrease in mortality rate of animals .

## Item bc5cdr:test:4682
Input:
Sentence: Conversion to SRL prevented CsA-induced renal damage evolution ( absent/mild grade lesions ) , while NGAL ( serum versus urine ) seems to be a feasible biomarker of CsA replacement to SRL .

## Item bc5cdr:test:4832
Input:
Sentence: UNASSIGNED : Epidemiological studies of 1,3-butadiene have suggest that exposures to humans are associated with chronic myeloid leukemia ( CML ) .

## Item bc5cdr:test:4795
Input:
Sentence: Maleate-induced renal injury included increase in renal vascular resistance and in the urinary excretion of total protein , glucose , sodium , neutrophil gelatinase-associated lipocalin ( NGAL ) and N-acetyl b-D-glucosaminidase ( NAG ) , upregulation of kidney injury molecule ( KIM ) -1 , decrease in renal blood flow and claudin-2 expression besides of necrosis and apoptosis of tubular cells on 24 h. Oxidative stress was determined by measuring the oxidation of lipids and proteins and diminution in renal Nrf2 levels .

## Item bc5cdr:test:4482
Input:
Sentence: SUMMARY : A 63-year-old Caucasian man with renal amyloidosis undergoing peripheral blood stem cell collection for an autologous stem cell transplant developed extensive bilateral upper-extremity deep venous thrombosis ( DVT ) and pulmonary embolism secondary to heparin-induced thrombocytopenia .

## Item bc5cdr:test:4804
Input:
Sentence: OBJECTIVE : Diazinon , a common organophosphate insecticide with genotoxic properties , was previously associated with lung cancer in the Agricultural Health Study ( AHS ) cohort , but few other epidemiological studies have examined diazinon-associated cancer risk .

## Item bc5cdr:test:4681
Input:
Sentence: Prolonged CsA exposure aggravated renal damage , without clear changes on the traditional markers , but with changes in serums TGF- b and IL-7 , TBARs clearance , and kidney TGF-b and mTOR .
