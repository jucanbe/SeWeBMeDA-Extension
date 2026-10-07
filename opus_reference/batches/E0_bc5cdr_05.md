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

## Item bc5cdr:test:2698
Input:
Sentence: The QT prolongation appeared to respond to administration of i.v .

## Item bc5cdr:test:2701
Input:
Sentence: PURPOSE : GAP43 has been thought to be linked with mossy fiber sprouting ( MFS ) in various experimental models of epilepsy .

## Item bc5cdr:test:2162
Input:
Sentence: In an open , cross-over , controlled design , patients were randomized to receive either DCF per os or GTN patches the first days of menses , when menstrual cramps became unendurable .

## Item bc5cdr:test:2477
Input:
Sentence: Induction of rosaceiform dermatitis during treatment of facial inflammatory dermatoses with tacrolimus ointment .

## Item bc5cdr:test:2595
Input:
Sentence: Nondyskinetic patients , but not the dyskinetic ones , showed less oropharyngeal swallowing efficiency ( OPSE ) for liquid food than controls ( Dunnett , P = 0.02 ) .

## Item bc5cdr:test:2498
Input:
Sentence: Prominent white-matter hypertrophy may result from altered myelination and adaptive glial changes , including gliosis secondary to neuronal damage .

## Item bc5cdr:test:2699
Input:
Sentence: calcium gluconate .

## Item bc5cdr:test:2870
Input:
Sentence: Carotid arteries , vena cava , and sympathetic ganglia from LNNA rats had higher basal levels of superoxide compared with those from control rats .

## Item bc5cdr:test:2878
Input:
Sentence: RESULTS : Polymorphisms TaqID , Ser311Cys and rs6277 were not polymorphic in the population recruited in the present study .

## Item bc5cdr:test:2500
Input:
Sentence: Disruption of hepatic lipid homeostasis in mice after amiodarone treatment is associated with peroxisome proliferator-activated receptor-alpha target gene activation .

## Item bc5cdr:test:1849
Input:
Sentence: RATIONALE : NG-nitro-L-arginine ( L-NOARG ) , an inhibitor of nitric-oxide synthase ( NOS ) , induces catalepsy in mice .

## Item bc5cdr:test:2748
Input:
Sentence: Drug-induced liver injury : an analysis of 461 incidences submitted to the Spanish registry over a 10-year period .

## Item bc5cdr:test:2652
Input:
Sentence: Evans Blue ( mug g-1 of brain tissue ) was greater in the 90/HTN group ( 24.4 +/- 6.0 ) versus the control group ( 12.3 +/- 4.1 ) , which was in turn greater than the 15/HTN group ( 7.3 +/- 3.2 ) .

## Item bc5cdr:test:2897
Input:
Sentence: This learning decrement persisted up to the last follow-up 4 weeks post-training .

## Item bc5cdr:test:2549
Input:
Sentence: RESULTS : Ribavirin-induced anemia occurred in 18 ( 20.5 % ) patients during treatment .

## Item bc5cdr:test:2904
Input:
Sentence: Neither myeloperoxidase- nor proteinase-3-antineutrophil cytoplasmic antibody was positive .

## Item bc5cdr:test:2351
Input:
Sentence: Immediately after the administration of levobupivacaine 0.5 % with epinephrine 2.5 microgram/mL , the patients developed grand mal seizures , despite negative aspiration for blood and no clinical signs of intravenous epinephrine administration .

## Item bc5cdr:test:2571
Input:
Sentence: ST elevation with chest discomfort disappeared since he began taking long-acting diltiazem .

## Item bc5cdr:test:2840
Input:
Sentence: The greater LV hypertrophy in TGR rats was associated with more pronounced downregulation of beta-AR and upregulation of LV beta-AR kinase-1 mRNA levels compared with those in SD rats .

## Item bc5cdr:test:2915
Input:
Sentence: The overall patient survival was 88.3 % , and 82.4 % after 1 and 2 years , respectively .

## Item bc5cdr:test:2914
Input:
Sentence: RESULTS : At a median follow-up of 14.1 months , the overall recurrence rate in the 51 patients was 3.9 % ( 2/51 ) .

## Item bc5cdr:test:2354
Input:
Sentence: Both patients were treated preoperatively with beta-adrenergic antagonist medications , which may have masked the cardiovascular signs of the unintentional intravascular administration of levobupivacaine with epinephrine .

## Item bc5cdr:test:2305
Input:
Sentence: The selective blockade of A2 adenosine receptor by DMPX ( 3,7-dimethyl-1-propargylxanthine ) significantly enhanced cocaine-induced locomotor activity of animals .

## Item bc5cdr:test:2953
Input:
Sentence: The number of hilar neurons immunoreactive for Prox-1 , a granule-cell-specific marker , was estimated using the optical fractionator method .

## Item bc5cdr:test:2700
Input:
Sentence: Growth-associated protein 43 expression in hippocampal molecular layer of chronic epileptic rats treated with cycloheximide .

## Item bc5cdr:test:2863
Input:
Sentence: Mean arterial pressure of conscious rats was 119 +/- 2 mm Hg in control and 194 +/- 5 mm Hg in LNNA rats ( P < 0.05 ) .

## Item bc5cdr:test:2730
Input:
Sentence: SEARCH STRATEGY : We searched the following databases up to November 2004 : the Cochrane Menstrual Disorders and Subfertility Group Trials Register , Cochrane Central Register of Controlled Trials ( CENTRAL ) , MEDLINE , EMBASE , Biological Abstracts .

## Item bc5cdr:test:2756
Input:
Sentence: Indeed , the incidence of liver transplantation and death in this group was 11.7 % if patients had jaundice at presentation , whereas the corresponding figure was 3.8 % in nonjaundiced patients ( P < .04 ) .

## Item bc5cdr:test:1779
Input:
Sentence: The authors describe the case of a 56-year-old woman with chronic , severe heart failure secondary to dilated cardiomyopathy and absence of significant ventricular arrhythmias who developed QT prolongation and torsade de pointes ventricular tachycardia during one cycle of intermittent low dose ( 2.5 mcg/kg per min ) dobutamine .

## Item bc5cdr:test:2965
Input:
Sentence: Eight of 13 participants were rated as responders on the basis of their improvement scores on the Clinical Global Impressions scale .

## Item bc5cdr:test:2612
Input:
Sentence: CONCLUSIONS : These data show that inhibition of NF-kappaB activation attenuates tubulointerstitial nephritis induced by gentamicin .

## Item bc5cdr:test:2774
Input:
Sentence: Erdosteine caused a marked reduction in the extent of tubular damage .

## Item bc5cdr:test:2811
Input:
Sentence: METHODS : Six groups of 6 BALB/c mice were treated with saline , DOX alone or DOX ( 4 mg/kg i.v . )

## Item bc5cdr:test:2213
Input:
Sentence: High-dose 5-fluorouracil / folinic acid in combination with three-weekly mitomycin C in the treatment of advanced gastric cancer .

## Item bc5cdr:test:2478
Input:
Sentence: BACKGROUND : Tacrolimus ointment is increasingly used for anti-inflammatory treatment of sensitive areas such as the face , and recent observations indicate that the treatment is effective in steroid-aggravated rosacea and perioral dermatitis .

## Item bc5cdr:test:2789
Input:
Sentence: After a period of 2.5 years on CPA treatment , four patients out of twenty-four were found to be affected by coronary heart disease .

## Item bc5cdr:test:2983
Input:
Sentence: DESIGN : Retrospective study .

## Item bc5cdr:test:2297
Input:
Sentence: It is concluded that this protection by carvedilol against both the structural and functional cardiac tissue damage may afford significant clinical advantage in minimizing the dose-limiting mitochondrial dysfunction and cardiomyopathy that accompanies long-term doxorubicin therapy in cancer patients .

## Item bc5cdr:test:2796
Input:
Sentence: Both the precordial pain and the electrocardiographic changes disappeared spontaneously after the discontinuation of 5-FU .

## Item bc5cdr:test:2312
Input:
Sentence: OBJECTIVES : The aim of this study was to determine whether the use of amiodarone in patients with atrial fibrillation ( AF ) increases the risk of bradyarrhythmia requiring a permanent pacemaker .

## Item bc5cdr:test:2905
Input:
Sentence: These manifestations met the American College of Rheumatology 1990 criteria for the classification of polyarteritis nodosa .

## Item bc5cdr:test:2988
Input:
Sentence: Three of the 4 patients were taking less than 6.5 mg/kg per day and all patients had normal renal and liver function test results .

## Item bc5cdr:test:2995
Input:
Sentence: This had been apparently uncomplicated and she had maintained a remarkably high level of physical activity .

## Item bc5cdr:test:2868
Input:
Sentence: The superoxide scavenger tempol ( 30 , 100 , and 300 micromol kg ( -1 ) , IV ) did not change arterial pressure in control rats but caused a dose-dependent decrease in LNNA rats ( -18 +/- 8 , -26 +/- 15 , and -54 +/- 11 mm Hg ) .

## Item bc5cdr:test:2943
Input:
Sentence: The effects of CAA on cysteine protease activities and thiols could be reproduced in cell lysate .

## Item bc5cdr:test:2944
Input:
Sentence: Acidification , which slowed the reaction of CAA with thiol donors , could also attenuate effects of CAA on necrosis markers , thiol depletion and cysteine protease inhibition in living cells .

## Item bc5cdr:test:2533
Input:
Sentence: Postoperatively , she was given a patient-controlled analgesia device delivering boluses of diamorphine 0.5 mg and droperidol 0.025 mg. Whilst using the device she gradually became anxious , the feeling worsening after each bolus .

## Item bc5cdr:test:2846
Input:
Sentence: In the inpatient setting , the frequency of QT interval prolongation with methadone treatment , its dose dependence , and the importance of cofactors such as drug-drug interactions remain unknown .

## Item bc5cdr:test:2682
Input:
Sentence: Case-control study of regular analgesic and nonsteroidal anti-inflammatory use and end-stage renal disease .

## Item bc5cdr:test:2463
Input:
Sentence: We present magnetic resonance imaging findings of a 5-year-old girl who had a rapidly installing hemolytic anemia crisis induced by trimethoprim-sulfomethoxazole , resulting in cerebral anoxia leading to permanent damage .

## Item bc5cdr:test:2648
Input:
Sentence: Part A , for eight rats in each group brain injury was evaluated by staining tissue using 2,3,5-triphenyltetrazolium chloride and edema was evaluated by microgravimetry .

## Item bc5cdr:test:2912
Input:
Sentence: METHODS : A retrospective chart analysis and a review of the organ transplant database identified 51 patients ( 43 men and 8 women ) transplanted for benign HBV-related cirrhotic diseases between June 2002 and December 2004 who had survived more than 3 months .

## Item bc5cdr:test:2849
Input:
Sentence: In addition to methadone dose , 15 demographic , biological , and pharmacological variables were considered as potential risk factors for QT prolongation .

## Item bc5cdr:test:3039
Input:
Sentence: There was no further deterioration in the patient 's condition during transport to hospital .

## Item bc5cdr:test:3054
Input:
Sentence: Mean changes in MSDBP and mean sitting systolic BP ( MSSBP ) were analyzed at the 8-week core study end point .

## Item bc5cdr:test:2847
Input:
Sentence: METHODS : We performed a systematic , retrospective study comparing active or former intravenous drug users receiving methadone and those not receiving methadone among all patients hospitalized over a 5-year period in a tertiary care hospital .

## Item bc5cdr:test:2854
Input:
Sentence: CONCLUSIONS : QT interval prolongation in methadone maintenance patients hospitalized in a tertiary care center is a frequent finding .

## Item bc5cdr:test:3057
Input:
Sentence: Control was defined as MSDBP < 90 mm Hg compared with baseline .

## Item bc5cdr:test:3061
Input:
Sentence: Each combination was associated with significantly greater reductions in MSSBP and MSDBP compared with the monotherapies and placebo ( all , P < 0.001 ) .

## Item bc5cdr:test:2706
Input:
Sentence: RESULTS : Densitometry showed no significant difference regarding GAP43-ir in the IML between Pilo , CHX+Pilo , and control groups .

## Item bc5cdr:test:2857
Input:
Sentence: Mechanisms of hypertension induced by nitric oxide ( NO ) deficiency : focus on venous function .

## Item bc5cdr:test:2955
Input:
Sentence: Interestingly , the size of the population appears to be correlated with the frequency of behavioral seizures , because animals with more ectopic granule cells in the hilus have more frequent behavioral seizures .

## Item bc5cdr:test:3094
Input:
Sentence: The sutures were passed individually through four tourniquets and exteriorized untied via the left atriotomy .

## Item bc5cdr:test:2355
Input:
Sentence: CONCLUSIONS : Although levobupivacaine may have a safer cardiac toxicity profile than racemic bupivacaine , if adequate amounts of levobupivacaine reach the circulation , it will result in convulsions .

## Item bc5cdr:test:3095
Input:
Sentence: Sonomicrometry crystals were implanted around the mitral annulus and left ventricle to measure geometry and regional function .

## Item bc5cdr:test:3100
Input:
Sentence: Concomitantly , the diastolic diameter of the LV base and LV sphericity decreased ( i.e. , improved ) from 37.4 +/- 9.3 to 35.9 +/- 10 mm ( p = 0.063 ) , and from 67.9 +/- 18.6 % to 65.3 +/- 18.9 % ( p = 0.016 ) , respectively .

## Item bc5cdr:test:2886
Input:
Sentence: Thereafter , seizures were induced by pilocarpine injections in trained and non-trained control groups .

## Item bc5cdr:test:3121
Input:
Sentence: METHODS : This prospective study included 28 patients undergoing carotid endarterectomy under local anesthesia .

## Item bc5cdr:test:2581
Input:
Sentence: did not induce catalepsy , and did not antagonize apomorphine ( 1.5 and 3 mg/kg ) stereotypy and apomorphine ( 0.05 mg/kg ) -induced catalepsy .

## Item bc5cdr:test:3138
Input:
Sentence: RESULTS : There were no group differences in psychopathology or `` eyes task '' performance , but the RC group , who otherwise had similar illicit substance use histories to the OC group , exhibited impaired fear recognition accuracy compared to the OC and CN groups .

## Item bc5cdr:test:3140
Input:
Sentence: The OC group was slower than CN when correctly identifying disgust .

## Item bc5cdr:test:2604
Input:
Sentence: METHODS : 38 female Wistar rats were injected with gentamicin , 40 mg/kg , twice a day for 9 days , 38 with gentamicin + PDTC , and 28 with 0.15 M NaCl solution .

## Item bc5cdr:test:2802
Input:
Sentence: The experience of this case , together with a review of the literature , suggests that FBAL is related to 5-FU-induced cardiotoxicity .

## Item bc5cdr:test:2574
Input:
Sentence: RATIONALE : 5-Hydroxytryptamine , via stimulation of 5-HT 2C receptors , exerts a tonic inhibitory influence on dopaminergic neurotransmission , whereas activation of 5-HT 2A receptors enhances stimulated DAergic neurotransmission .

## Item bc5cdr:test:2822
Input:
Sentence: Clinical evaluation of adverse effects during bepridil administration for atrial fibrillation and flutter .

## Item bc5cdr:test:1644
Input:
Sentence: There was no change in the levels of DA , norepinephrine ( NE ) , serotonin ( 5-HT ) , or their metabolites in the arcuate nucleus ( AN ) , medial preoptic area ( MPA ) , caudate putamen ( CP ) , substantia nigra ( SN ) , and zona incerta ( ZI ) , except for a decrease in 5-hydroxyindoleacetic acid ( 5-HIAA ) in the AN after 6-months of hyperprolactinemia and an increase in DA concentrations in the AN after 9-months of hyperprolactinemia .

## Item bc5cdr:test:3179
Input:
Sentence: Dialysis was immediately initiated .

## Item bc5cdr:test:2621
Input:
Sentence: RESULTS : The mean +/- SD duration of treatment with the identified atypical antipsychotic agent was 68.3 +/- 28.9 months ( clozapine ) , 29.5 +/- 17.5 months ( olanzapine ) , and 40.9 +/- 33.7 ( risperidone ) .

## Item bc5cdr:test:2982
Input:
Sentence: OBJECTIVE : To review the natural history and ocular and systemic adverse effects of patients taking hydroxychloroquine sulfate who attended an ophthalmic screening program .

## Item bc5cdr:test:2819
Input:
Sentence: The mean protective effect by adding monoHER before DOX led to a significant 4.4-fold reduction ( P < 0.001 , 95 % CI 2.3-8.2 ) of abnormal cardiomyocytes .

## Item bc5cdr:test:2628
Input:
Sentence: Acute renal insufficiency after high-dose melphalan in patients with primary systemic amyloidosis during stem cell transplantation .

## Item bc5cdr:test:2831
Input:
Sentence: The major triggering factors of Tdp were hypokalemia and sudden decrease in heart rate .

## Item bc5cdr:test:2841
Input:
Sentence: The decrease in the heart rate ( HR ) induced by the beta-AR antagonist metoprolol in conscious rats was significantly attenuated in TGR compared with SD rats ( -9.9 +/- 1.7 % vs. -18.1 +/- 1.5 % ) , whereas the effect of parasympathetic blockade by atropine on HR was similar in both strains .

## Item bc5cdr:test:3033
Input:
Sentence: Further studies are needed for a better clarification of Wilson 's disease therapy , and in particular to differentiate specific therapies for different Wilson 's disease phenotypes .

## Item bc5cdr:test:3049
Input:
Sentence: BACKGROUND : One third of patients treated for hypertension attain adequate blood pressure ( BP ) control , and multidrug regimens are often required .

## Item bc5cdr:test:3073
Input:
Sentence: RESULTS : Pb exposure produced lasting impairments in learning , attention , inhibitory control , and arousal regulation , paralleling the areas of dysfunction seen in Pb-exposed children .

## Item bc5cdr:test:2950
Input:
Sentence: It has been suggested that the ectopic hilar granule cells could contribute to the spontaneous seizures that ultimately develop after status epilepticus .

## Item bc5cdr:test:2739
Input:
Sentence: Long-term oestrogen-only HT also significantly increased the risk of stroke and gallbladder disease .

## Item bc5cdr:test:2948
Input:
Sentence: Stereological methods reveal the robust size and stability of ectopic hilar granule cells after pilocarpine-induced status epilepticus in the adult rat .

## Item bc5cdr:test:2945
Input:
Sentence: Thus , CAA directly reacts with cellular protein and non-protein thiols , mediating its toxicity on hRPTEC .

## Item bc5cdr:test:3086
Input:
Sentence: No panic attack was observed after the caffeine-free solution intake .

## Item bc5cdr:test:3092
Input:
Sentence: The study aim was to identify these benefits in a canine model of acute heart failure .

## Item bc5cdr:test:3252
Input:
Sentence: Patients were randomly allocated into one of two groups : lateral and conventional spinal anaesthesia groups .

## Item bc5cdr:test:3119
Input:
Sentence: Such complications are most important in situations where there is a pre-existing contralateral paralysis .

## Item bc5cdr:test:3259
Input:
Sentence: The mean respiratory rate and oxygen saturations in the two groups were similar .

## Item bc5cdr:test:2716
Input:
Sentence: METHODS : Adult male Swiss Webster mice ( 25-32 g ) were given nicotine ( 0.05-0.25 mg/kg s.c. ) or saline 10 min before caffeine ( 70 mg/kg i.p . )

## Item bc5cdr:test:2902
Input:
Sentence: Minocycline-induced vasculitis fulfilling the criteria of polyarteritis nodosa .

## Item bc5cdr:test:2795
Input:
Sentence: After admission , the patient received a continuous intravenous infusion of 5-FU ( 1000 mg/day ) , during which precordial pain with right bundle branch block occurred concomitantly with a high serum FBAL concentration of 1955 ng/ml .

## Item bc5cdr:test:3108
Input:
Sentence: The laboratory data revealed normal plasma electrolyte and ammonia levels but leukocytosis .

## Item bc5cdr:test:2666
Input:
Sentence: BACKGROUND : Acetaminophen ( paracetamol -- P ) and Nimesulide ( N ) are widely used analgesic-antipyretic/anti-inflammatory drugs .
