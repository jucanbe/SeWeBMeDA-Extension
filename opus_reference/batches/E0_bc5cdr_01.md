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

## Item bc5cdr:test:121
Input:
Sentence: A patient with renal disease developed Coombs-positive hemolytic anemia while receiving cephalothin therapy .

## Item bc5cdr:test:192
Input:
Sentence: The chronic feeding of small amounts ( 0.3-3 % of diet weight ) of certain amino derivatives of caproate resulted in hyperglycemia , an elevated glucose tolerance curve and , occasionally , glucosuria .

## Item bc5cdr:test:773
Input:
Sentence: All three patients required therapy discontinuation .

## Item bc5cdr:test:774
Input:
Sentence: Cardiac enzymes remained normal despite transient electrocardiographic ( EKG ) changes .

## Item bc5cdr:test:625
Input:
Sentence: Thus , `` stress '' levels of adrenaline ( 230 pg/ml ) for 6 h cause a delayed and protracted pressor effect .

## Item bc5cdr:test:58
Input:
Sentence: Recurrent subarachnoid hemorrhage associated with aminocaproic acid therapy and acute renal artery thrombosis .

## Item bc5cdr:test:328
Input:
Sentence: Two weeks before his death he was readmitted because of aplastic crisis with septicemia and marked abnormalities in liver function and died of hemorrhagic bronchopneumonia .

## Item bc5cdr:test:547
Input:
Sentence: The effectiveness of haloperidol pretreatment in preventing the toxic effects of high doses of amphetamine and cocaine was studied in rats .

## Item bc5cdr:test:481
Input:
Sentence: Menstrual abnormalities ( 79 % ) , weight gain ( 60 % ) , muscle cramps/myalgias ( 40 % ) , and transaminase elevations ( 40 % ) were the most common adverse reactions .

## Item bc5cdr:test:551
Input:
Sentence: Haloperidol decreased the incidence of cocaine-induced seizures at the two highest doses , but the lowering of the mortality rate did not reach statistical significance at any dose .

## Item bc5cdr:test:691
Input:
Sentence: The initial response to the primary attack by the cyclophosphamide metabolites seems to be fragmentation of the luminal membrane .

## Item bc5cdr:test:642
Input:
Sentence: Procaterol , a new beta-2 adrenoceptor stimulant , was studied in a double-blind , placebo-controlled , cross-over trial in patients with bronchial asthma .

## Item bc5cdr:test:725
Input:
Sentence: In six of eight patients ( 75 % ) who we treated for recurrent or resistant glioma , sudden severe neurologic deterioration occurred .

## Item bc5cdr:test:656
Input:
Sentence: Increased anxiogenic effects of caffeine in panic disorders .

## Item bc5cdr:test:558
Input:
Sentence: This is the first published report documenting the preferential in vivo binding of estrogen to nuclei of cells in estrogen induced hamster renal carcinomas .

## Item bc5cdr:test:650
Input:
Sentence: The studies were performed using an experimental model of isoproterenol-induced heart hypertrophy in rats .

## Item bc5cdr:test:555
Input:
Sentence: Estrogen binding sites were demonstrated by autoradiography in one transplantable and five primary diethylstilbesterol induced renal carcinomas in three hamsters .

## Item bc5cdr:test:815
Input:
Sentence: There was no difference in the rate of engraftment of evaluable patients in the two groups ( P greater than 0.5 ) .

## Item bc5cdr:test:741
Input:
Sentence: Clinical applications of calcium channel blockers parallel their tissue selectivity .

## Item bc5cdr:test:855
Input:
Sentence: ( ABSTRACT TRUNCATED AT 250 WORDS )

## Item bc5cdr:test:29
Input:
Sentence: 4 cases of endometrial carcinoma referred from elsewhere demonstrated the problems of inappropriate and unsupervised unopposed oestrogen therapy and the difficulty in distinguishing severe hyperplasia from malignancy .

## Item bc5cdr:test:450
Input:
Sentence: When circumflex artery blood flow was maintained constant , the increases in CxAD induced by cromakalim ( 10 micrograms/kg ) , pinacidil ( 30 micrograms/kg ) and nitroglycerin ( 10 micrograms/kg ) were reduced by 68 +/- 7 , 54 +/- 9 and 1 +/- 1 % , respectively .

## Item bc5cdr:test:762
Input:
Sentence: Theophylline concentrations at this endpoint in serum ( total ) and CSF were similar but serum ( free ) and brain concentrations were slightly different in pregnant rats .

## Item bc5cdr:test:451
Input:
Sentence: Thus , whereas nitroglycerin preferentially and flow-independently dilates large coronary arteries , cromakalim and pinacidil dilate both large and small coronary arteries and this effect is not dependent upon the simultaneous beta adrenoceptors-mediated rise in myocardial metabolic demand .

## Item bc5cdr:test:674
Input:
Sentence: A case of oral penicillin anaphylaxis is described , and the terminology , occurrence , clinical manifestations , pathogenesis , prevention , and treatment of anaphylaxis are reviewed .

## Item bc5cdr:test:756
Input:
Sentence: Their glomeruli showed changes of progressive FSGS .

## Item bc5cdr:test:869
Input:
Sentence: Reversal to normal heart rate was found on day 7 .

## Item bc5cdr:test:439
Input:
Sentence: Neurologic toxicities have been described with IT-methotrexate , IT-cytosine arabinoside and IT-TSPA .

## Item bc5cdr:test:589
Input:
Sentence: In anesthetized dogs , a high dose of ACC-9653 ( 31 mg/kg ) was infused over 15 , 20 , and 30 min and the responses were compared to an equimolar dose of phenytoin sodium ( 21 mg/kg ) .

## Item bc5cdr:test:614
Input:
Sentence: In a patient receiving phenytoin who presents a viral-like illness , early recognition and discontinuation of the drug are mandatory .

## Item bc5cdr:test:681
Input:
Sentence: In a series of five experiments , the modulating role of naloxone on a scopolamine-induced retention deficit in a passive avoidance paradigm was investigated in mice .

## Item bc5cdr:test:207
Input:
Sentence: Progesterone potentiation of bupivacaine arrhythmogenicity in pentobarbital-anesthetized rats and beating rat heart cell cultures .

## Item bc5cdr:test:895
Input:
Sentence: Data on 9,037 patients were collected by 1,455 participating physicians .

## Item bc5cdr:test:699
Input:
Sentence: were studied in 32 children ( mean age 6.9 yr ) pretreated with either physiological saline or alfentanil 50 micrograms kg-1 .

## Item bc5cdr:test:171
Input:
Sentence: The incidence of neurotoxicity may be reduced by employing lower doses of methotrexate in the presence of central nervous system leukemia , in older children and adults , and in the presence of epidural leakage .

## Item bc5cdr:test:791
Input:
Sentence: However , it has not previously been described in association with the use of Imipramine .

## Item bc5cdr:test:60
Input:
Sentence: Epsilon aminocaproic acid ( EACA ) has been used to prevent rebleeding in patients with subarachnoid hemorrhage ( SAH ) .

## Item bc5cdr:test:640
Input:
Sentence: Procaterol and terbutaline in bronchial asthma .

## Item bc5cdr:test:602
Input:
Sentence: During the 14-day run-in and during washout periods , inhaled beta-agonists were withheld and ipratropium bromide was substituted for rescue purposes .

## Item bc5cdr:test:378
Input:
Sentence: In order to evaluate the efficacy , time-course of action and predictors of response to topical capsaicin , 39 patients with chronic post-herpetic neuralgia ( PHN ) , median duration 24 months , were treated with 0.025 % capsaicin cream for 8 weeks .

## Item bc5cdr:test:707
Input:
Sentence: A morphometric study of isoproterenol induced myocardial fibrosis .

## Item bc5cdr:test:737
Input:
Sentence: An autoimmune pathogenesis of the bile duct destruction is suggested .

## Item bc5cdr:test:735
Input:
Sentence: Prominent fibrosis and hepatocellular regeneration were also present ; however , the lobular architecture was preserved .

## Item bc5cdr:test:651
Input:
Sentence: A correlation of the blood pressure was neither found in the development nor in the attempt to suppress the development of heart hypertrophy with the two beta-receptor blockers .

## Item bc5cdr:test:224
Input:
Sentence: Six stable psychiatric outpatients with hyperprolactinemia and amenorrhea/oligomenorrhea associated with their neuroleptic medications were treated with bromocriptine .

## Item bc5cdr:test:520
Input:
Sentence: Convulsant effect of lindane and regional brain concentration of GABA and dopamine .

## Item bc5cdr:test:730
Input:
Sentence: This complication appears to represent a significant new toxicity of high-dose etoposide therapy for malignant glioma .

## Item bc5cdr:test:746
Input:
Sentence: The coronary vasodilating properties of nisoldipine have led to the investigation of this agent for use in angina .

## Item bc5cdr:test:863
Input:
Sentence: The increase in pressure rate product after dipyridamole was significantly less than that during the treadmill exercise .

## Item bc5cdr:test:761
Input:
Sentence: Sprague-Dawley rats that were 20 days pregnant and nonpregnant rats of the same age and strain received infusions of aminophylline until onset of maximal seizures which occurred after 28 and 30 minutes respectively .

## Item bc5cdr:test:541
Input:
Sentence: Nifedipine induced bradycardia in a patient with autonomic neuropathy .

## Item bc5cdr:test:749
Input:
Sentence: The enhancement of aminonucleoside nephrosis by the co-administration of protamine .

## Item bc5cdr:test:807
Input:
Sentence: At these high doses of CYA , serious cardiotoxicity may occur , but definitive risk factors for the development of such cardiotoxicity have not been described .

## Item bc5cdr:test:679
Input:
Sentence: Possible pathophysiological mechanisms which may have been operative in this case include : a direct central nervous system ( CNS ) toxic effect of valproic acid ; a paradoxical epileptogenic effect secondary to the drug ; and an indirect CNS toxic effect mediated through valproic acid-induced hyperammonemia .

## Item bc5cdr:test:1000
Input:
Sentence: Comparing the relative sensitivity to central depression and excitation revealed that rats were least likely to have convulsions at doses that did not first cause loss of consciousness , while cats most clearly showed marked central excitatory actions .

## Item bc5cdr:test:906
Input:
Sentence: Four groups of rats ( n = 7 ) were studied : jj and jJ rats treated either with aspirin 300 mg/kg every other day or sham-treated .

## Item bc5cdr:test:777
Input:
Sentence: Fatal aplastic anemia in a patient treated with carbamazepine .

## Item bc5cdr:test:933
Input:
Sentence: Analysis of in vivo myocardial excitability , contractility , and metabolic characteristics at 16 months revealed other significant barium-induced disturbances within the cardiovascular system .

## Item bc5cdr:test:1012
Input:
Sentence: The difference in the effects of the two was significant .

## Item bc5cdr:test:587
Input:
Sentence: The total doses of ACC-9653 or phenytoin sodium necessary to convert the arrhythmia to a normal sinus rhythm were 24 +/- 6 and 14 +/- 3 mg/kg , respectively .

## Item bc5cdr:test:1022
Input:
Sentence: The mean treatment period was 18 months .

## Item bc5cdr:test:942
Input:
Sentence: These experimental findings represent the first indication that life-long barium ingestion may have significant adverse effects on the mammalian cardiovascular system .

## Item bc5cdr:test:1027
Input:
Sentence: These results suggest that hormonal replacement therapy can be safely prescribed if the following criteria are satisfied : 1 ) preliminary evaluation of patients from a clinical , metabolic , cytologic , and mammographic perspective ; 2 ) cyclic treatment schedule , with a progestative phase of 10 days ; and 3 ) periodic complete follow-up , with accurate thermographic evaluation of the breast target tissues .

## Item bc5cdr:test:934
Input:
Sentence: The most distinctive aspect of the barium effect was a demonstrated hypersensitivity of the cardiovascular system to sodium pentobarbital .

## Item bc5cdr:test:805
Input:
Sentence: Cyclophosphamide cardiotoxicity : an analysis of dosing as a risk factor .

## Item bc5cdr:test:847
Input:
Sentence: Myocardial levels of VIP were assayed before and after the development of heart failure in two canine models .

## Item bc5cdr:test:825
Input:
Sentence: These models may also be useful in developing insights into the pathophysiology of aminoglycoside-induced nephrotoxicity .

## Item bc5cdr:test:835
Input:
Sentence: Pilocarpine , given intraperitoneally to rats , reproduces the neuropathological sequelae of temporal lobe epilepsy and provides a relevant animal model for studying mechanisms of buildup of convulsive activity and pathways operative in the generalization and propagation of seizures within the forebrain .

## Item bc5cdr:test:760
Input:
Sentence: The purpose of this investigation was to determine whether the neurotoxicity of theophylline is altered in advanced pregnancy .

## Item bc5cdr:test:865
Input:
Sentence: We conclude that the dipyridamole ECG test is as useful as the exercise ECG test for the assessment of coronary artery disease .

## Item bc5cdr:test:235
Input:
Sentence: Added in vitro to rat cortical membrane preparation , abecarnil increased [ 3H ] GABA binding , enhanced muscimol-stimulated 36Cl- uptake and reduced the binding of t- [ 35S ] butylbicyclophosphorothionate ( [ 35S ] TBPS ) .

## Item bc5cdr:test:633
Input:
Sentence: The lack of any consistent protective effect noted with the alkylxanthines tested in the present study indicates that adenosine plays little , if any , pathophysiological role in gentamicin-induced ARF .

## Item bc5cdr:test:765
Input:
Sentence: It is concluded that advanced pregnancy has a negligible effect on the neurotoxic response to theophylline in rats .

## Item bc5cdr:test:618
Input:
Sentence: After pretreatment with 3 mg of cyproheptadine , 2 mg mianserin , or 2 mg chlorpheniramine , only 5 of 105 animals ( 5 % ) died after receiving BSA on day +7 ( p less than 0.001 ) .

## Item bc5cdr:test:997
Input:
Sentence: Toxic actions of flurazepam ( FZP ) were studied in cats , mice and rats .

## Item bc5cdr:test:63
Input:
Sentence: Since intravascular fibrin thrombi are often observed in patients with fibrinolytic disorders , EACA should not be implicated in the pathogenesis of fibrin thrombi in patients with disseminated intravascular coagulation or other `` consumption coagulopathies . ''

## Item bc5cdr:test:911
Input:
Sentence: Aspirin treatment reduced PGE2 synthesis in all regions , but outer medullary PGE2 remained higher in jj ( 18 +/- 3 ) than jJ rats ( 9 +/- 2 ) ( p less than 0.05 ) .

## Item bc5cdr:test:1017
Input:
Sentence: Hormones and risk of breast cancer .

## Item bc5cdr:test:912
Input:
Sentence: PGF2 alpha was also significantly higher in the outer medulla of jj rats with and without aspirin administration ( p less than 0.05 ) .

## Item bc5cdr:test:534
Input:
Sentence: First , pretreatment with MK-801 produced an effective and dose-dependent anticonvulsant action with the lithium-pilocarpine model but not with rats treated with pilocarpine alone , suggesting that different biochemical mechanisms control seizures in these two models .

## Item bc5cdr:test:922
Input:
Sentence: We can not advocate the administration of lidocaine prophylactically in the early hours of suspected myocardial infarction .

## Item bc5cdr:test:1025
Input:
Sentence: Themography confirmed the existence of an excessive breast stimulation in 1 women who complained of moderate mastodynia and in 5 of the 7 women who complained of severe mastodynia .

## Item bc5cdr:test:672
Input:
Sentence: Oxitropium proves to be a valuable alternative to theophylline in nocturnal asthma , since it is equally potent , safer and does not require the titration of dosage .

## Item bc5cdr:test:1024
Input:
Sentence: Mastodynia was reported by 21 patients , and physical examination revealed a light increase in breast firmness in 12 women and a moderate increase in breast nodularity in 2 women .

## Item bc5cdr:test:654
Input:
Sentence: Neither propranolol nor B 24/76 could stop the changes in the characteristic myosin isoenzyme pattern of the hypertrophied rat heart .

## Item bc5cdr:test:893
Input:
Sentence: Postmarketing study of timolol-hydrochlorothiazide antihypertensive therapy .

## Item bc5cdr:test:564
Input:
Sentence: The feasibility of using labetalol , an alpha- and beta-adrenergic blocking agent , as a hypotensive agent in combination with inhalation anaesthetics ( halothane , enflurane or isoflurane ) was studied in 23 adult patients undergoing middle-ear surgery .

## Item bc5cdr:test:1168
Input:
Sentence: This effect , which results in a flattening of the phase 0 and phase 4 slope , together with a longer AP duration , may be due to an increase in the time constants of slow inward ionic currents ( already demonstrated elsewhere ) , but also to an increased time constant for deactivation of the outward potassium current ( Ip ) .

## Item bc5cdr:test:954
Input:
Sentence: This is probably because PPA has less beta 2 activity than does norepinephrine .

## Item bc5cdr:test:1201
Input:
Sentence: These differences occur especially in the age groups under 30 years .

## Item bc5cdr:test:586
Input:
Sentence: ACC-9653 and phenytoin sodium have similar antiarrhythmic activity against ouabain-induced ventricular tachycardia in anesthetized dogs .

## Item bc5cdr:test:808
Input:
Sentence: Since chemotherapeutic agent toxicity generally correlates with dose per body surface area , we retrospectively calculated the dose of CYA in patients transplanted at our institution to determine whether the incidence of CYA cardiotoxicity correlated with the dose per body surface area .

## Item bc5cdr:test:984
Input:
Sentence: Morphine-induced seizures in newborn infants .

## Item bc5cdr:test:827
Input:
Sentence: Monosodium glutamate ( MSG ) administration to neonatal rodents produces convulsions and results in numerous biochemical and behavioral deficits .

## Item bc5cdr:test:985
Input:
Sentence: Two neonates suffered from generalized seizures during the course of intravenous morphine sulfate for post-operative analgesia .

## Item bc5cdr:test:601
Input:
Sentence: Twelve asthmatic patients ( FEV1 , 81 +/- 4 % predicted ) , requiring only occasional inhaled beta-agonists as their sole therapy , were given a 14-day treatment with high dose inhaled salbutamol ( HDS ) , 4,000 micrograms daily , low dose inhaled salbutamol ( LDS ) , 800 micrograms daily , or placebo ( PI ) by metered-dose inhaler in a double-blind , randomized crossover design .

## Item bc5cdr:test:713
Input:
Sentence: The rapid reversion after insulin treatment excludes the possibility that streptozotocin in itself causes the ISO resistance and points towards a direct insulin effect on myocardial catecholamine sensitivity in diabetic rats .

## Item bc5cdr:test:1223
Input:
Sentence: At 1 day their number was reduced to about 1/10 of the original number .

## Item bc5cdr:test:857
Input:
Sentence: Electrocardiographic changes after dipyridamole infusion ( 0.568 mg/kg/4 min ) were studied in 41 patients with coronary artery disease and compared with those after submaximal treadmill exercise by use of the body surface mapping technique .

## Item bc5cdr:test:1226
Input:
Sentence: These findings suggest that smooth muscle cells are susceptible to damage in the course of their specific function .
