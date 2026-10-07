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

## Item bc5cdr:test:3266
Input:
Sentence: Clinically significant anemia ( hemoglobin < 7 g/dL ) was observed in 5.4 % of patients ( CD4 , 165 cells/microL ) and hepatitis ( clinical jaundice with alanine aminotransferase > 5 times upper limits of normal ) in 3.5 % of patients ( CD4 , 260 cells/microL ) .

## Item bc5cdr:test:1837
Input:
Sentence: The catechol and hydroquinone metabolites , NCQ436 and NCQ344 , induced apoptosis in HL60 and HBMP cells in a time- and concentration dependent manner , while the phenols , NCR181 , FLA873 , and FLA797 , and the derivatives formed by oxidation of the pyrrolidine ring , FLA838 , NCM001 , and NCL118 , had no effect .

## Item bc5cdr:test:3644
Input:
Sentence: The most severe adverse reactions to carbamazepine have been observed in the haemopoietic system , the liver and the cardiovascular system .

## Item bc5cdr:test:3000
Input:
Sentence: Risks and benefits of COX-2 inhibitors vs non-selective NSAIDs : does their cardiovascular risk exceed their gastrointestinal benefit ?

## Item bc5cdr:test:3451
Input:
Sentence: Systemic anticoagulation is unsafe and regional citrate anticoagulation in the absence of a functional liver carries the risk of citrate toxicity .

## Item bc5cdr:test:3533
Input:
Sentence: At re-warming , patient had resolution of her cerebral edema and intracranial hypertension .

## Item bc5cdr:test:3590
Input:
Sentence: Immunoblotting and immunohistochemistry revealed decreased expression of Na ( + ) /K ( + ) -ATPase , NHE3 , NBC1 , and AQP1 in the kidney of gentamicin-treated rats .

## Item bc5cdr:test:3537
Input:
Sentence: Binasal visual field defects are not specific to vigabatrin .

## Item bc5cdr:test:3185
Input:
Sentence: Rifampicin-associated segmental necrotizing glomerulonephritis in staphylococcal endocarditis .

## Item bc5cdr:test:3439
Input:
Sentence: The intracerebroventricular ( ICV ) administration of ouabain ( a Na ( + ) /K ( + ) -ATPase inhibitor ) in rats has been suggested to mimic some symptoms of human bipolar mania .

## Item bc5cdr:test:3554
Input:
Sentence: After adjusting for potential confounders , we found that the risk of HIV seroconversion among participants who were daily smokers of crack cocaine increased over time ( period 1 : hazard ratio [ HR ] 1.03 , 95 % confidence interval [ CI ] 0.57-1.85 ; period 2 : HR 1.68 , 95 % CI 1.01-2.80 ; and period 3 : HR 2.74 , 95 % CI 1.06-7.11 ) .

## Item bc5cdr:test:3604
Input:
Sentence: The participants had physical examination , medical record extraction , and venipuncture , CD4+T-cell counts determination , measurement of depression symptoms ( using the self-report Center for Epidemiological Studies-Depression Scale ) , and alcohol use assessment at enrollment , and semiannually until March 2000 .

## Item bc5cdr:test:3360
Input:
Sentence: Comparison of laryngeal mask with endotracheal tube for anesthesia in endoscopic sinus surgery .

## Item bc5cdr:test:3608
Input:
Sentence: The association between alcohol consumption and depression was significant ( p < 0.001 ) .

## Item bc5cdr:test:3712
Input:
Sentence: Current `` diagnostic '' tests , which primarily include functional and antigenic assays , have more of a confirmatory than diagnostic role in the management of HIT .

## Item bc5cdr:test:3465
Input:
Sentence: DISCUSSION : Flecainide and pharmacologically similar agents that interact with sodium channels may cause delirium in susceptible patients .

## Item bc5cdr:test:3722
Input:
Sentence: Patients with ADSD were identified .

## Item bc5cdr:test:3268
Input:
Sentence: Among the patients with 1 year of follow-up , NVP therapy was significantly associated with developing rash and d4T therapy with developing peripheral neuropathy ( p < 0.05 ) .

## Item bc5cdr:test:2603
Input:
Sentence: This study investigated the expression of nuclear factor-kappaB ( NF-kappaB ) , mitogen-activated protein ( MAP ) kinases and macrophages in the renal cortex and structural and functional renal changes of rats treated with gentamicin or gentamicin + pyrrolidine dithiocarbamate ( PDTC ) , an NF-kappaB inhibitor .

## Item bc5cdr:test:3617
Input:
Sentence: METHODS : SE was induced by pilocarpine injection .

## Item bc5cdr:test:3746
Input:
Sentence: Transfusion reaction workup was negative .

## Item bc5cdr:test:3849
Input:
Sentence: This was evident only when a sensory component was involved in the induction of plasticity , indicating that cerebellar sensory processing function is involved in the resurgence of M1 plasticity .

## Item bc5cdr:test:3509
Input:
Sentence: Cocaine is a risk factor for both ischemic and haemorrhagic stroke .

## Item bc5cdr:test:3853
Input:
Sentence: These results suggest that alterations in cerebellar sensory processing function , occurring secondary to abnormal basal ganglia signals reaching it , may be an important element contributing to the maladaptive sensorimotor plasticity of M1 and the emergence of abnormal involuntary movements .

## Item bc5cdr:test:3494
Input:
Sentence: It is unclear whether a coronary CTA strategy would be efficacious in cocaine-associated chest pain , as coronary vasospasm may account for some of the ischemia .

## Item bc5cdr:test:3856
Input:
Sentence: METHODS : Sixty female Sprague-Dawley ( SD ) rats were randomly divided into three groups .

## Item bc5cdr:test:3205
Input:
Sentence: The differential effects of bupivacaine and lidocaine on prostaglandin E2 release , cyclooxygenase gene expression and pain in a clinical pain model .

## Item bc5cdr:test:3676
Input:
Sentence: Patients often consume the drug with suicidal intent or with a background of substance dependence .

## Item bc5cdr:test:3884
Input:
Sentence: On an intention-to-treat basis , 55 % of the patients achieved at least partial response , including 19 % CR and 35 % achieved at least very good partial response .

## Item bc5cdr:test:3290
Input:
Sentence: The present case highlights the possibility that differential diagnosis between an amiodarone-related pulmonary lesion and a neoplasm can be very difficult radiologically , and suggests that membranous glomerulonephritis might be another possible complication of amiodarone treatment .

## Item bc5cdr:test:3713
Input:
Sentence: Special attention must be paid to cardiac patients who are often exposed to heparin multiple times during their course of treatment .

## Item bc5cdr:test:3783
Input:
Sentence: Moreover , numerous patchy , well-limited fibrotic areas , compatible with post-necrotic tissue repair , were found after 6-month temsirolimus therapy .

## Item bc5cdr:test:3916
Input:
Sentence: Median duration of response was 34.4 months , and it was higher in patients who received RD until progression ( not reached versus 19 months , p < 0.001 ) .

## Item bc5cdr:test:3774
Input:
Sentence: CONCLUSIONS : EndoMT is a novel pathway leading to early development of diabetic nephropathy .

## Item bc5cdr:test:3007
Input:
Sentence: Among users of aspirin , they were : 14,671 to rofecoxib , 22,875 to celecoxib , 9,832 to NS-NSAIDs and 38,048 to acetaminophen .

## Item bc5cdr:test:3409
Input:
Sentence: For PCI , argatroban has not been investigated in hepatically impaired patients ; dose adjustment is unnecessary for adult age , sex , race/ethnicity or obesity , and lesser doses may be adequate with concurrent glycoprotein IIb/IIIa inhibition .

## Item bc5cdr:test:3804
Input:
Sentence: On day 8 , the patient developed acute renal failure ( serum creatinine 1.9 mg/dL , increased from 1.2 mg/dL the previous day and 0.8 mg/dL on admission ) .

## Item bc5cdr:test:3920
Input:
Sentence: Dose reductions were needed in 31 % of patients and permanent discontinuation in 38.9 % .

## Item bc5cdr:test:3724
Input:
Sentence: For patients with bilateral abductor paralysis , age , sex , paralytic Botox dose , prior Botox dose , and course following paralysis were noted .

## Item bc5cdr:test:3750
Input:
Sentence: Other causes of anemia should be considered in patients with worse-than-expected anemia after chemotherapy .

## Item bc5cdr:test:3836
Input:
Sentence: Patients with the diagnosis of methamphetamine based on DSM-IV were interviewed using the Mini International Neuropsychiatric Interview ( M.I.N.I . )

## Item bc5cdr:test:3432
Input:
Sentence: A lesion induced by 6-OHDA produced more severe motor deterioration in CB1 KO mice accompanied by more loss of DA neurons and increased PENK gene expression in the CPu .

## Item bc5cdr:test:3718
Input:
Sentence: Reported adverse effects include a period of breathiness , throat pain , and difficulty with swallowing liquids .

## Item bc5cdr:test:3614
Input:
Sentence: BACKGROUND : Neuroinflammation occurs after seizures and is implicated in epileptogenesis .

## Item bc5cdr:test:3725
Input:
Sentence: RESULTS : From a database of 452 patients receiving Botox , 352 patients had been diagnosed with ADSD .

## Item bc5cdr:test:3616
Input:
Sentence: In this work CCR2 and CCL2 expression were examined following status epilepticus ( SE ) induced by pilocarpine injection .

## Item bc5cdr:test:3845
Input:
Sentence: Cerebellar sensory processing alterations impact motor cortical plasticity in Parkinson 's disease : clues from dyskinetic patients .

## Item bc5cdr:test:3759
Input:
Sentence: Verapamil responsiveness was determined by peak percent change in basal prolactin levels ( PRL ) .

## Item bc5cdr:test:3636
Input:
Sentence: A total of 60 male Wistar albino rats were randomly divided into four groups ( 15/group ) : The control group injected with single doses of normal saline ( i.c.v ) followed 24 h later by BCNU solvent ( i.v ) .

## Item bc5cdr:test:3721
Input:
Sentence: METHODS : Patients that received Botox injections for spasmodic dysphonia between January 2000 and October 2009 were evaluated .

## Item bc5cdr:test:3753
Input:
Sentence: AIM : Verapamil stimulation test was previously investigated as a tool for differential diagnosis of hyperprolactinemia , but with conflicting results .

## Item bc5cdr:test:3602
Input:
Sentence: We evaluated the association of alcohol consumption and depression , and their effects on HIV disease progression among women with HIV .

## Item bc5cdr:test:3762
Input:
Sentence: CONCLUSION : Verapamil responsiveness is not a reliable finding for the differential diagnosis of hyperprolactinemia .

## Item bc5cdr:test:3681
Input:
Sentence: Two acetaminophen-induced ALF patients reattempted suicide post-LT ( one died 8 years post-LT ) .

## Item bc5cdr:test:3997
Input:
Sentence: This is especially relevant in multidrug therapy where more than one drug can cause a similar ocular adverse effect .

## Item bc5cdr:test:3466
Input:
Sentence: A MEDLINE search ( 1966-January 2009 ) revealed one in vivo pharmacokinetic study on the interaction between flecainide , a CYP2D6 substrate , and paroxetine , a CYP2D6 inhibitor , as well as 3 case reports of flecainide-induced delirium .

## Item bc5cdr:test:3683
Input:
Sentence: Multidisciplinary approaches with long-term psychiatric follow-up may contribute to low post-transplant suicide rates seen and low rates of graft loss because of non-compliance .

## Item bc5cdr:test:3898
Input:
Sentence: AChE activity was significantly decreased in the hippocampus of mice with BPA compared to control mice , whereas no difference was found in the prefrontal cortex , hypothalamus and cerebellum .

## Item bc5cdr:test:3437
Input:
Sentence: These results suggest that activation of CB1 receptors offers neuroprotection against dopaminergic lesion and the development of L-DOPA-induced dyskinesias .

## Item bc5cdr:test:3883
Input:
Sentence: The median number of bort-dex cycles was 6 , up to a maximum of 12 cycles .

## Item bc5cdr:test:3793
Input:
Sentence: Alendronate , a biphosphonate , is effective for both the treatment and prevention of osteoporosis in postmenopausal women .

## Item bc5cdr:test:3918
Input:
Sentence: Adverse events were reported in 68.9 % of patients ( myelosuppression in 49.4 % ) and 12.7 % of patients needed hospitalization .

## Item bc5cdr:test:3789
Input:
Sentence: This case is a good example of electrolyte imbalance causing acute life-threatening cardiac events .

## Item bc5cdr:test:4031
Input:
Sentence: She otherwise reported that she is quite active , rides horses , and does show jumping without any limitations in her physical activity .

## Item bc5cdr:test:3732
Input:
Sentence: The likely mechanism of paralysis is diffusion of Botox around the muscular process of the arytenoid to the posterior cricoarytenoid muscles .

## Item bc5cdr:test:3730
Input:
Sentence: The incidence of abductor paralysis after Botox injection for ADSD was 0.34 % .

## Item bc5cdr:test:3741
Input:
Sentence: MitoQ , a mitochondrial-targeted antioxidant , was shown to completely prevent these mitochondrial abnormalities as well as cardiac dysfunction characterized here by a diastolic dysfunction studied with a conductance catheter to obtain pressure-volume data .

## Item bc5cdr:test:3945
Input:
Sentence: Eighty-one percent of patients with dyskinesia had clinical fluctuations .

## Item bc5cdr:test:3311
Input:
Sentence: Prolonged treatment with losartan showed further reduction of glomerulosclerosis associated with reduced progression of tubular atrophy and interstitial fibrosis , thus preventing heavy proteinuria and chronic renal failure .

## Item bc5cdr:test:3981
Input:
Sentence: Early postoperative delirium incidence risk factors were then assessed through three different multiple regression models .

## Item bc5cdr:test:3777
Input:
Sentence: Mantle cell lymphoma ( MCL ) is a rare and aggressive type of B-cell non-Hodgkin 's lymphoma .

## Item bc5cdr:test:3991
Input:
Sentence: However , METH significantly increased the immobility time in the tail suspension test at 3 and 49 days post-administration .

## Item bc5cdr:test:3972
Input:
Sentence: The pattern of kidney syndromes in this population series mirrors that reported in randomised clinical trials .

## Item bc5cdr:test:4078
Input:
Sentence: Median follow-up from the start of GEM-P was 4.5 years .

## Item bc5cdr:test:3635
Input:
Sentence: The present study aimed to explore the effect of MT induction on carmustine ( BCNU ) -induced hippocampal cognitive dysfunction in rats .

## Item bc5cdr:test:3904
Input:
Sentence: The subcutaneous injection of isoproterenol ( 30 mg/kg ) into rats twice at an interval of 24 h , for two consecutive days , led to a significant increase in serum lactate dehydrogenase , creatine phosphokinase , alanine transaminase , aspartate transaminase , and angiotensin-converting enzyme activities , total cholesterol , triglycerides , free serum fatty acid , cardiac tissue malondialdehyde ( MDA ) , and nitric oxide levels and a significant decrease in levels of glutathione and superoxide dismutase in cardiac tissue as compared to the normal control group ( P < 0.05 ) .

## Item bc5cdr:test:3752
Input:
Sentence: Verapamil stimulation test in hyperprolactinemia : loss of prolactin response in anatomic or functional stalk effect .

## Item bc5cdr:test:3876
Input:
Sentence: Reports about cases of hepatotoxicity due to clopidogrel are increasing in the last few years , after the increased use of this drug .

## Item bc5cdr:test:4004
Input:
Sentence: Our report emphasizes the need for monitoring of visual function in patients on long-term linezolid treatment .

## Item bc5cdr:test:4139
Input:
Sentence: Animals used at M0 ( n = 8 ) were also used at moment -24 h of acute study .

## Item bc5cdr:test:4142
Input:
Sentence: The chronological study showed an effect of a cumulative dose on body weight ( R = -0.99 , p = 0.011 ) , necrosis ( R = 1.00 , p = 0.004 ) , TAP ( R = 0.95 , p = 0.049 ) , and DNA SBs ( R = -0.95 , p = 0.049 ) .

## Item bc5cdr:test:4020
Input:
Sentence: METHOD : We retrospectively evaluated the medical records of 205 consecutive adult patients who underwent full-size liver transplantation between January 2006 and December 2010 due to end-stage or malignant liver disease .

## Item bc5cdr:test:3823
Input:
Sentence: decreased convulsion incidence and severity and prolonged latency time to convulsion following injection with a convulsive dose of lindane ( 8 mg/kg , i.p . ) .

## Item bc5cdr:test:3901
Input:
Sentence: Biochemical effects of Solidago virgaurea extract on experimental cardiotoxicity .

## Item bc5cdr:test:3937
Input:
Sentence: METHODS : This is a cross-sectional study involving 95 patients with PD on uninterrupted levodopa therapy for at least 6 months .

## Item bc5cdr:test:3680
Input:
Sentence: During follow-up ( median 5 years ) , there were no significant differences in rejection ( acute and chronic ) , graft failure or survival between the groups ( acetaminophen-induced ALF 1 year 87 % , 5 years 75 % ; non-acetaminophen-induced ALF 88 % , 78 % ; CLD 93 % , 82 % : P > 0.6 log rank ) .

## Item bc5cdr:test:3831
Input:
Sentence: The aim of this work is to call attention to the risk of tacrolimus use in patients with SSc .

## Item bc5cdr:test:4032
Input:
Sentence: There was no evidence of any recent stress or status migrainosus .

## Item bc5cdr:test:3943
Input:
Sentence: Dyskinesia was present in 44 % ( n = 42 ) with median levodopa therapy of 3 years .

## Item bc5cdr:test:3682
Input:
Sentence: CONCLUSIONS : Despite a high prevalence of psychiatric disturbance , outcomes for patients transplanted emergently for acetaminophen-induced ALF were comparable to those transplanted for non-acetaminophen-induced ALF and electively for CLD .

## Item bc5cdr:test:3834
Input:
Sentence: The association between psychiatric co-morbidity and methamphetamine-induced psychosis was also studied .

## Item bc5cdr:test:3665
Input:
Sentence: BACKGROUND : Renal dysfunction induced by iodinated contrast medium ( CM ) administration can minimize the benefit of the interventional procedure in patients undergoing renal angioplasty ( PTRA ) .

## Item bc5cdr:test:4041
Input:
Sentence: Strikingly , despite prolonged abstinence ( mean , 4.98 ; range , 4-9 years ) , past ecstasy users showed few signs of recovery .

## Item bc5cdr:test:4195
Input:
Sentence: Patients were divided into three groups and each group had 20 patients .

## Item bc5cdr:test:4074
Input:
Sentence: One hundred and twenty-two cycles of GEM-P were administered in total ( median 3 cycles ; range 1-6 ) .

## Item bc5cdr:test:3338
Input:
Sentence: Both isomers of propranolol were capable of preventing adrenaline-induced cardiac arrhythmias in cats anaesthetized with halothane , but the mean dose of ( - ) -propranolol was 0.09+/-0.02 mg/kg whereas that of ( + ) -propranolol was 4.2+/-1.2 mg/kg .

## Item bc5cdr:test:3711
Input:
Sentence: The treatment of HIT mandates an immediate cessation of all heparin exposure and the institution of an antithrombotic therapy , most commonly using a direct thrombin inhibitor .

## Item bc5cdr:test:3965
Input:
Sentence: The potential for tenofovir to cause a range of kidney syndromes has been established from mechanistic and randomised clinical trials .

## Item bc5cdr:test:3995
Input:
Sentence: Linezolid-induced optic neuropathy .

## Item bc5cdr:test:3714
Input:
Sentence: Direct thrombin inhibitors are appropriate , evidence-based alternatives to heparin in patients with a history of HIT , who need to undergo percutaneous coronary intervention .
