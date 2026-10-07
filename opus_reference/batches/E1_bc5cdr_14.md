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

## Item bc5cdr:test:2849
Example input:
Sentence: Progressive improvement occurred in 7 cases after commencement of prednisolone and methotrexate , and in one case spontaneously .

Example answer:
{"entities": [{"text": "prednisolone", "type": "Chemical"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: Multivariate analysis showed a 2.8-fold increased risk of thrombosis in females .

Example answer:
{"entities": [{"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: These patients had Q-T prolongation and recurrent syncope due to polymorphous ventricular tachycardia .

Example answer:
{"entities": [{"text": "Q-T prolongation", "type": "Disease"}, {"text": "syncope", "type": "Disease"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: Recurrence rates were 31.4 % with rizatriptan and 15.3 % with ergotamine/caffeine .

Example answer:
{"entities": [{"text": "rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}]}

Example input:
Sentence: This calls for attention when ketoconazole is administered to patients with risk factors for acquired long QT syndrome .

Example answer:
{"entities": [{"text": "ketoconazole", "type": "Chemical"}, {"text": "long QT syndrome", "type": "Disease"}]}

Example input:
Sentence: We postulate that by virtue of its direct blocking action on IKr , ketoconazole alone may prolong QT interval and induce TdP .

Example answer:
{"entities": [{"text": "ketoconazole", "type": "Chemical"}, {"text": "TdP", "type": "Disease"}]}

Example input:
Sentence: Choreoathetoid movements associated with rapid adjustment to methadone .

Example answer:
{"entities": [{"text": "Choreoathetoid movements", "type": "Disease"}, {"text": "methadone", "type": "Chemical"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: These data indicate that the free ED50 in plasma for terfenadine ( 1.9 nM ) , terodiline ( 76 nM ) , cisapride ( 11 nM ) and E4031 ( 1.9 nM ) closely correlate with the free concentration in man causing QT effects .

Example answer:
{"entities": [{"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}, {"text": "E4031", "type": "Chemical"}]}

Example input:
Sentence: Four compounds known to increase QT interval and cause TDP were investigated : terfenadine , terodiline , cisapride and E4031 .

Example answer:
{"entities": [{"text": "TDP", "type": "Disease"}, {"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}, {"text": "E4031", "type": "Chemical"}]}

Input:
Sentence: In addition to methadone dose , 15 demographic , biological , and pharmacological variables were considered as potential risk factors for QT prolongation .

## Item bc5cdr:test:3061
Example input:
Sentence: Dex increased SBP ( 110 +/- 2-126 +/- 3 mmHg ; P < 0.001 ) and decreased thymus ( P < 0.001 ) and bodyweights ( P '' < 0.01 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}, {"text": "increased SBP", "type": "Disease"}, {"text": "decreased thymus ( P < 0.001 ) and bodyweights", "type": "Disease"}]}

Example input:
Sentence: In a placebo-controlled , single-blinded , crossover study , we assessed the effect of `` real '' repetitive transcranial magnetic stimulation ( rTMS ) versus `` sham '' rTMS ( placebo ) on peak dose dyskinesias in patients with Parkinson 's disease ( PD ) .

Example answer:
{"entities": [{"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : DBP , but not SBP , reduction was associated with neurological worsening after the intravenous administration of high-dose nimodipine after acute stroke .

Example answer:
{"entities": [{"text": "nimodipine", "type": "Chemical"}, {"text": "acute stroke", "type": "Disease"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: Patients with a DBP reduction of > or =20 % in the high-dose group had a significantly increased adjusted OR for the compound outcome variable death or dependency ( Barthel Index < 60 ) ( n/N=25/26 , OR 10 .

Example answer:
{"entities": [{"text": "DBP reduction", "type": "Disease"}, {"text": "death", "type": "Disease"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}, {"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: In multivariate analysis , a significant correlation between DBP reduction and worsening of the neurological score was found for the high-dose group ( beta=0.49 , P=0 .

Example answer:
{"entities": [{"text": "DBP reduction", "type": "Disease"}]}

Example input:
Sentence: On the Positive and Negative Syndrome Scale positive subscale , all treatments were superior to placebo with LOCF and MMRM ; asenapine at 5 mg BID was superior to placebo on the negative subscale with MMRM and on the general psychopathology subscale with LOCF and MMRM .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}]}

Example input:
Sentence: Nimodipine treatment resulted in a statistically significant reduction in systolic BP ( SBP ) and diastolic BP ( DBP ) from baseline compared with placebo during the first few days .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "Chemical"}, {"text": "reduction in systolic BP", "type": "Disease"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Input:
Sentence: Each combination was associated with significantly greater reductions in MSSBP and MSDBP compared with the monotherapies and placebo ( all , P < 0.001 ) .

## Item bc5cdr:test:2955
Example input:
Sentence: A significant decrease in neuronal density of the hippocampal hilar formation was identified in vehicle- and PDTC-treated rats following status epilepticus .

Example answer:
{"entities": [{"text": "PDTC-treated", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}]}

Example input:
Sentence: EEG recordings were made in SJL , A/J and C57BL/6J mice revealing a close correspondence between electrical activity and behavior .

Example answer:
{"entities": []}

Example input:
Sentence: These data support the hypothesis that SE-induced mossy fiber sprouting and synaptic reorganization are relevant characteristics of seizure development in these murine strains , resembling rat models of human temporal lobe epilepsy .

Example answer:
{"entities": [{"text": "SE-induced", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}]}

Example input:
Sentence: Dopamine turnover ratios ( DOPAC : DA and HVA : DA ) were found to be lower in those animals exposed to the exploratory box when compared to their home cage counterparts .

Example answer:
{"entities": [{"text": "Dopamine", "type": "Chemical"}, {"text": "DOPAC", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}, {"text": "HVA", "type": "Chemical"}]}

Example input:
Sentence: CSS mapping suggests seizure susceptibility loci on mouse Chromosomes 10 and 18 .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Three hundred fifty-five adult male CSS mice , 58 B6 , and 39 A/J were tested for susceptibility to pilocarpine-induced seizures .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Mature male and female mice from six inbred stains were tested for susceptibility to behavioral seizures induced by a single injection of cocaine .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: These data might indicate that the generation of reactive oxygen species and activation of NF-kappaB plays a more central role in seizure-associated neuronal damage in the temporal cortex as compared to the hippocampal hilus .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "seizure-associated", "type": "Disease"}, {"text": "neuronal damage", "type": "Disease"}]}

Example input:
Sentence: In Mg ( 2+ ) -free bathing medium containing bicuculline , conditions designed to increase excitability in the slices , electrical stimulation of the hilus resulted in a single population spike in granule cells from control mice and pilocarpine-treated mice that did not experience SE .

Example answer:
{"entities": [{"text": "Mg", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "pilocarpine-treated", "type": "Chemical"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Population responses in granule cells of the dentate gyrus were examined in transverse slices of the ventral hippocampus from pilocarpine-treated and untreated mice .

Example answer:
{"entities": [{"text": "pilocarpine-treated", "type": "Chemical"}]}

Input:
Sentence: Interestingly , the size of the population appears to be correlated with the frequency of behavioral seizures , because animals with more ectopic granule cells in the hilus have more frequent behavioral seizures .

## Item bc5cdr:test:2316
Example input:
Sentence: The adjusted odds ratio was 2.5 ( 95 percent confidence interval , 1.5 to 4.1 ) among women who used second-generation oral contraceptives and 1.3 ( 95 percent confidence interval , 0.7 to 2.5 ) among those who used third-generation oral contraceptives .

Example answer:
{"entities": [{"text": "oral contraceptives", "type": "Chemical"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Disease"}]}

Example input:
Sentence: A low incidence of cardiovascular malformations was observed after exposure to each of the four calcium channel blockers , but this incidence was statistically significant only for verapamil and nifedipine .

Example answer:
{"entities": [{"text": "cardiovascular malformations", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: Among women who used oral contraceptives , the odds ratio was 2.1 ( 95 percent confidence interval , 1.5 to 3.0 ) for those without a prothrombotic mutation and 1.9 ( 95 percent confidence interval , 0.6 to 5.5 ) for those with a mutation CONCLUSIONS : The risk of myocardial infarction was increased among women who used second-generation oral contraceptives .

Example answer:
{"entities": [{"text": "oral contraceptives", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: We observed sinoatrial block due to chronic amiodarone administration in a 5-year-old boy with primary cardiomyopathy , Wolff-Parkinson-White syndrome and supraventricular tachycardia .

Example answer:
{"entities": [{"text": "sinoatrial block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "primary cardiomyopathy", "type": "Disease"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "supraventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: Reduction in the dosage of amiodarone resulted in the disappearance of the sinoatrial block and the persistence of asymptomatic sinus bradycardia .

Example answer:
{"entities": [{"text": "amiodarone", "type": "Chemical"}, {"text": "sinoatrial block", "type": "Disease"}, {"text": "sinus bradycardia", "type": "Disease"}]}

Example input:
Sentence: The patient was admitted to the hospital , anticoagulated with unfractionated heparin , and given intravenous diltiazem for rate control and intravenous amiodarone for rate and rhythm control .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}]}

Example input:
Sentence: Amiodarone should be used with caution during long-term oral therapy in patients with or without clear intraventricular conduction defects .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "Chemical"}]}

Example input:
Sentence: A patient with sinuatrial disease and implanted pacemaker was treated with amiodarone ( maximum dose 1000 mg , maintenance dose 800 mg daily ) for 10 months , for control of supraventricular tachyarrhythmias .

Example answer:
{"entities": [{"text": "sinuatrial disease", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "supraventricular tachyarrhythmias", "type": "Disease"}]}

Input:
Sentence: Multivariable logistic regression was used to estimate the odds ratio ( OR ) of pacemaker insertion associated with amiodarone use , controlling for baseline risk factors and exposure to sotalol , Class I antiarrhythmic agents , beta-blockers , calcium channel blockers , and digoxin .

## Item bc5cdr:test:2716
Example input:
Sentence: Eight healthy volunteers inhaled nicotine in darkness during a functional magnetic resonance imaging ( fMRI ) experiment ; eye movements were registered using video-oculography .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}]}

Example input:
Sentence: Concentrations of coniine and nicotine sulfate were 0.015 % , 0.03 % , 0.075 % , 0.15 % , 0.75 % , 1.5 % , 3 % , and 6 % and 1 % , 5 % , and 10 % , respectively .

Example answer:
{"entities": [{"text": "coniine", "type": "Chemical"}, {"text": "nicotine", "type": "Chemical"}]}

Example input:
Sentence: Animals were administered nicotine , carbachol , or neostigmine via timed tail vein infusion , and the latencies to onset of tremor and clonus were recorded and converted to threshold dose .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}, {"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: There was a statistically significant ( P < or = 0.01 ) decrease in movement in coniine and nicotine sulfate treated chicks as determined by ultrasound .

Example answer:
{"entities": [{"text": "coniine", "type": "Chemical"}, {"text": "nicotine", "type": "Chemical"}]}

Example input:
Sentence: Compared with sham-operated controls , lesions significantly ( p < 0.25 ) blunted the early ( < 60 min ) free-field locomotor hypoactivity caused by nicotine ( 0.5 mg kg ( -1 ) , i.m .

Example answer:
{"entities": [{"text": "locomotor hypoactivity", "type": "Disease"}, {"text": "nicotine", "type": "Chemical"}]}

Example input:
Sentence: Nicotine ( 1.0 mg/kg ) caused a significant increase in locomotor activity in rats that were habituated to the test environment , but had only a weak and delayed stimulant action in rats that were unfamiliar with the test environment .

Example answer:
{"entities": [{"text": "Nicotine", "type": "Chemical"}, {"text": "increase in locomotor activity", "type": "Disease"}]}

Example input:
Sentence: beta4 -/- mice were less sensitive to the effects of nicotine both at low doses , measured as decreased exploration in an open field , and at high doses , measured as sensitivity to nicotine-induced seizures .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: alpha3 +/- mice were partially resistant to nicotine-induced seizures when compared to wild-type littermates .

Example answer:
{"entities": [{"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Swiss albino mice prepared with intrajugular catheters were tested in photocell cages after administration of 93 mg/kg ( LD50 ) of cocaine and GNC92H2 infusions ranging from 30 to 190 mg/kg .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "GNC92H2", "type": "Chemical"}]}

Input:
Sentence: METHODS : Adult male Swiss Webster mice ( 25-32 g ) were given nicotine ( 0.05-0.25 mg/kg s.c. ) or saline 10 min before caffeine ( 70 mg/kg i.p . )

## Item bc5cdr:test:2701
Example input:
Sentence: At hippocampal Schaeffer collateral-CA1 synapses , long-term potentiation was preserved in BMC-transplanted rats compared to epileptic controls .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}]}

Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: By using this strategy to study the involvement of MRP2 in brain access of antiepileptic drugs ( AEDs ) , we recently reported that phenytoin is a substrate for MRP2 in the BBB .

Example answer:
{"entities": [{"text": "phenytoin", "type": "Chemical"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Similar to rats , systemic pilocarpine injection causes status epilepticus ( SE ) and the eventual development of spontaneous seizures and mossy fiber sprouting in C57BL/6 and CD1 mice , but the physiological correlates of these events have not been identified in mice .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Striatal microglia expressing eGFP constitutively show morphological changes after METH that are characteristic of activation .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}]}

Example input:
Sentence: BMCs obtained from green fluorescent protein ( GFP ) transgenic mice or rats were transplanted intravenously after induction of status epilepticus ( SE ) .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Prevention of seizures and reorganization of hippocampal functions by transplantation of bone marrow cells in the acute phase of experimental epilepsy .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "epilepsy", "type": "Disease"}]}

Example input:
Sentence: In this study , we investigated whether increased generation of FR during status epilepticus would be sufficient to provoke abnormalities in mtDNA and in the expression and activity of cytochrome c oxidase ( CCO ) , complex IV of the respiratory chain , in the chronic phase of the pilocarpine model of temporal lobe epilepsy .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}, {"text": "temporal lobe epilepsy", "type": "Disease"}]}

Example input:
Sentence: These data support the hypothesis that SE-induced mossy fiber sprouting and synaptic reorganization are relevant characteristics of seizure development in these murine strains , resembling rat models of human temporal lobe epilepsy .

Example answer:
{"entities": [{"text": "SE-induced", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}]}

Input:
Sentence: PURPOSE : GAP43 has been thought to be linked with mossy fiber sprouting ( MFS ) in various experimental models of epilepsy .

## Item bc5cdr:test:2854
Example input:
Sentence: His bundle recordings showed an atrial tachycardia with intermittent exit block and greatly prolonged BH and HV intervals ( 40 and 100 msec , respectively ) .

Example answer:
{"entities": [{"text": "atrial tachycardia", "type": "Disease"}]}

Example input:
Sentence: We postulate that by virtue of its direct blocking action on IKr , ketoconazole alone may prolong QT interval and induce TdP .

Example answer:
{"entities": [{"text": "ketoconazole", "type": "Chemical"}, {"text": "TdP", "type": "Disease"}]}

Example input:
Sentence: Choreoathetoid movements associated with rapid adjustment to methadone .

Example answer:
{"entities": [{"text": "Choreoathetoid movements", "type": "Disease"}, {"text": "methadone", "type": "Chemical"}]}

Example input:
Sentence: Symptoms persisted for three months despite TAC dose reduction , administration of IVIG and four doses of methylprednisolone pulse therapy .

Example answer:
{"entities": [{"text": "TAC", "type": "Chemical"}, {"text": "methylprednisolone", "type": "Chemical"}]}

Example input:
Sentence: This is a case report of euphoria and choreoathetoid movements both transiently induced by rapid adjustment to the selective mu-opioid receptor agonist methadone in an inpatient previously abusing heroine and cocaine .

Example answer:
{"entities": [{"text": "choreoathetoid movements", "type": "Disease"}, {"text": "methadone", "type": "Chemical"}, {"text": "heroine", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: These seven cases demonstrate that procainamide can produce an acquired prolonged Q-T syndrome with polymorphous ventricular tachycardia .

Example answer:
{"entities": [{"text": "procainamide", "type": "Chemical"}, {"text": "prolonged Q-T syndrome", "type": "Disease"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: Her QT interval returned to normal upon withdrawal of ketoconazole .

Example answer:
{"entities": [{"text": "ketoconazole", "type": "Chemical"}]}

Example input:
Sentence: These patients had Q-T prolongation and recurrent syncope due to polymorphous ventricular tachycardia .

Example answer:
{"entities": [{"text": "Q-T prolongation", "type": "Disease"}, {"text": "syncope", "type": "Disease"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: Four compounds known to increase QT interval and cause TDP were investigated : terfenadine , terodiline , cisapride and E4031 .

Example answer:
{"entities": [{"text": "TDP", "type": "Disease"}, {"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}, {"text": "E4031", "type": "Chemical"}]}

Example input:
Sentence: We report a woman with coronary artery disease who developed a markedly prolonged QT interval and torsades de pointes ( TdP ) after taking ketoconazole for treatment of fungal infection .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "prolonged QT interval", "type": "Disease"}, {"text": "torsades de pointes", "type": "Disease"}, {"text": "TdP", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "fungal infection", "type": "Disease"}]}

Input:
Sentence: CONCLUSIONS : QT interval prolongation in methadone maintenance patients hospitalized in a tertiary care center is a frequent finding .

## Item bc5cdr:test:2868
Example input:
Sentence: Changes evoked by a single intraperitoneal injection of rilmenidine ( 600 microg/kg ) or alpha-methyldopa ( 100 mg/kg ) , selective I1- and alpha2-receptor agonists , respectively , in blood pressure , hemodynamic variability , and locomotor activity were assessed in radiotelemetered sham-operated and ovariectomized ( Ovx ) Sprague-Dawley female rats with or without 12-wk estrogen replacement .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "estrogen", "type": "Chemical"}]}

Example input:
Sentence: Following discontinuation of SNP , blood pressure in the control animals rebounded to 94 torr , as compared with 78 torr in the saralasin-treated rats .

Example answer:
{"entities": [{"text": "SNP", "type": "Chemical"}, {"text": "saralasin-treated", "type": "Chemical"}]}

Example input:
Sentence: Pretreatment of TCR , at a dose of 0.5 mL/100 g bodyweight per day , orally for 30 days , prevented the increase in lipid peroxidation and activity of marker enzymes observed in isoproterenol-induced rats ( 85 mg kg ( -1 ) s. c. for 2 days at an interval of 24 h ) .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: The lung weights were lower and PaO2 was improved in rats given this enzyme-blocking agent .

Example answer:
{"entities": []}

Example input:
Sentence: Treatment with Ato improved endothelial function , reduced superoxide production and reduced SBP in Dex-treated SD rats .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}, {"text": "superoxide", "type": "Chemical"}, {"text": "Dex-treated", "type": "Chemical"}]}

Example input:
Sentence: In unanesthetized , spontaneously hypertensive rats the decrease in blood pressure and heart rate produced by intravenous clonidine , 5 to 20 micrograms/kg , was inhibited or reversed by nalozone , 0.2 to 2 mg/kg .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}, {"text": "clonidine", "type": "Chemical"}, {"text": "nalozone", "type": "Chemical"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/", "type": "Chemical"}, {"text": "K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}]}

Example input:
Sentence: In the present study , we investigated whether 50 mg/kg per day , p.o. , Ato could prevent endothelial NO synthase ( eNOS ) downregulation and the increase in O2- in Sprague-Dawley ( SD ) rats , thereby reducing blood pressure .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}, {"text": "O2-", "type": "Chemical"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Input:
Sentence: The superoxide scavenger tempol ( 30 , 100 , and 300 micromol kg ( -1 ) , IV ) did not change arterial pressure in control rats but caused a dose-dependent decrease in LNNA rats ( -18 +/- 8 , -26 +/- 15 , and -54 +/- 11 mm Hg ) .

## Item bc5cdr:test:2943
Example input:
Sentence: High levels of matrix Gla protein are found at sites of artery calcification in rats treated with vitamin D plus Warfarin , and chemical analysis showed that the protein that accumulated was indeed not gamma-carboxylated .

Example answer:
{"entities": [{"text": "artery calcification", "type": "Disease"}, {"text": "vitamin D", "type": "Chemical"}, {"text": "Warfarin", "type": "Chemical"}, {"text": "gamma-carboxylated", "type": "Chemical"}]}

Example input:
Sentence: We found that maltolyl p-coumarate significantly decreased apoptotic cell death and reduced reactive oxygen species , cytochrome c release , and caspase 3 activation .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}]}

Example input:
Sentence: Immunohistochemistry displayed significantly increased expressions of MMP-2 , MMP-9 , ADAM-10 and ADAM-17 ( all p < 0.01 ) in intima and media for CaCl ( 2 ) -treated segments .

Example answer:
{"entities": [{"text": "CaCl ( 2 )", "type": "Chemical"}]}

Example input:
Sentence: The lung weights were lower and PaO2 was improved in rats given this enzyme-blocking agent .

Example answer:
{"entities": []}

Example input:
Sentence: MMP-2 , MMP-9 , ADAM-10 and ADAM-17 mRNA levels were increased in CaCl ( 2 ) -treated segments ( all p < 0.01 ) , with trends of elevation in CaCl ( 2 ) -untreated segments , as compared with NaCl-treated segments .

Example answer:
{"entities": [{"text": "CaCl ( 2 )", "type": "Chemical"}, {"text": "NaCl-treated", "type": "Chemical"}]}

Example input:
Sentence: Independent but not additive effects of Na and Ca are shown by decreases in the values of [ verapamil ] o needed to reduce BF by 30 % ( IC30 ) with the following order of inhibitory potency : LNa > LCa > HCa > N , resulting LNa+HCa similar to LNa .

Example answer:
{"entities": [{"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: PURPOSE : This study was designed to establish a rat model of thoracic aortic aneurysm ( TAA ) by calcium chloride ( CaCl ( 2 ) ) -induced arterial injury and to explore the potential role of a disintegrin and metalloproteinase ( ADAM ) , matrix metalloproteinases ( MMPs ) and their endogenous inhibitors ( TIMPs ) in TAA formation .

Example answer:
{"entities": [{"text": "thoracic aortic aneurysm", "type": "Disease"}, {"text": "TAA", "type": "Disease"}, {"text": "calcium chloride", "type": "Chemical"}, {"text": "CaCl ( 2 )", "type": "Chemical"}, {"text": "arterial injury", "type": "Disease"}]}

Example input:
Sentence: When instilled directly into the bladder , CAA exerts urotoxic effects , it is , however , susceptible to detoxification with mesna .

Example answer:
{"entities": [{"text": "CAA", "type": "Chemical"}, {"text": "mesna", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : This study establishes a TAA model by periarterial CaCl ( 2 ) exposure in rats , and demonstrates a significant elevation of expression of MMP-2 , MMP-9 , ADAM10 and ADAM17 in the pathogenesis of vascular remodeling .

Example answer:
{"entities": [{"text": "TAA", "type": "Disease"}, {"text": "CaCl ( 2 )", "type": "Chemical"}]}

Example input:
Sentence: Based on clinical data , indicating that chloroacetaldehyde ( CAA ) is an important metabolite of oxazaphosphorine cytostatics , an experimental study was carried out in order to elucidate the role of CAA in the development of hemorrhagic cystitis .

Example answer:
{"entities": [{"text": "chloroacetaldehyde", "type": "Chemical"}, {"text": "CAA", "type": "Chemical"}]}

Input:
Sentence: The effects of CAA on cysteine protease activities and thiols could be reproduced in cell lysate .

## Item bc5cdr:test:2789
Example input:
Sentence: A 47-year-old patient suffering from coronary artery disease was admitted to the CCU in shock with III .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "shock", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Patients who are more than 10 years post-OLTX have CRF and ESRD at a high rate .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: A patient is reported who developed progressive cardiomyopathy two and one-half years after receiving 580 mg/m2 which apparently represents late , late cardiotoxicity .

Example answer:
{"entities": [{"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: CASE SUMMARIES : Two patients developed prolonged cholestatic hepatitis after receiving ticlopidine following percutaneous coronary angioplasty , with complete remission during the follow-up period .

Example answer:
{"entities": [{"text": "ticlopidine", "type": "Chemical"}]}

Example input:
Sentence: In 8 patients followed for 24 weeks , gallbladder contractility remained depressed throughout therapy .

Example answer:
{"entities": [{"text": "depressed", "type": "Disease"}]}

Example input:
Sentence: Five patients were diagnosed as having subclinical heart failure after the completion of chemotherapy .

Example answer:
{"entities": [{"text": "heart failure", "type": "Disease"}]}

Example input:
Sentence: Three patients developed congestive heart failure after the completion of chemotherapy .

Example answer:
{"entities": [{"text": "congestive heart failure", "type": "Disease"}]}

Example input:
Sentence: In the pre-treatment evaluation , signs of cardiovascular disease were found in 33 patients ( 43 % ) .

Example answer:
{"entities": [{"text": "cardiovascular disease", "type": "Disease"}]}

Example input:
Sentence: Treatment duration longer than 1 year was associated with an eightfold increased risk ( OR = 7.7 , 95 % CI 0.9 to 69 ) .

Example answer:
{"entities": []}

Example input:
Sentence: During treatment , adverse cardiac effects were observed in 14 patients ( 18 % ) .

Example answer:
{"entities": []}

Input:
Sentence: After a period of 2.5 years on CPA treatment , four patients out of twenty-four were found to be affected by coronary heart disease .

## Item bc5cdr:test:3094
Example input:
Sentence: METHODS : We conducted a retrospective review of 70 consecutive microvascular decompression operations and studied those patients who received topical papaverine for vasospasm .

Example answer:
{"entities": [{"text": "papaverine", "type": "Chemical"}, {"text": "vasospasm", "type": "Disease"}]}

Example input:
Sentence: These effects gave rise to an increase in the right atrial pressure and a decrease in the left one with a consequent stretching of the foramen ovale and the creation of massive right-to-left shunting .

Example answer:
{"entities": []}

Example input:
Sentence: At the end of the procedure , Group A ( n = 20 ) had 20 mg/0.5 mL of methylprednisolone and 10 mg/0.5 mL of gentamicin injected into the posterior sub-Tenon 's space and Group B ( n = 20 ) had the same combination injected into the anterior sub-Tenon 's space .

Example answer:
{"entities": [{"text": "methylprednisolone", "type": "Chemical"}, {"text": "gentamicin", "type": "Chemical"}]}

Example input:
Sentence: The patients were randomly allocated to one of three groups ; those in group A ( n = 10 ) were subjected to controlled hypotension alone , those in group B ( n = 10 ) to haemodilution alone and those in group C ( n = 10 ) to both controlled hypotension and haemodilution .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}]}

Example input:
Sentence: Within 8 hours after initiation of therapy the patient died with a clinical picture resembling massive pulmonary obstruction due to choriocarcinomic tissue plugs , probably originating from the uterus .

Example answer:
{"entities": [{"text": "pulmonary obstruction", "type": "Disease"}]}

Example input:
Sentence: The surgery and anaesthesia were uneventful , but 3 days after surgery , the patient reported an area of hypoaesthesia over L3-L4 dermatomes of the leg which had been operated on ( loss of pinprick sensation ) without reduction in muscular strength .

Example answer:
{"entities": [{"text": "loss of pinprick sensation", "type": "Disease"}]}

Example input:
Sentence: Groups 1 and 2 underwent micropuncture studies after 10 days .

Example answer:
{"entities": []}

Example input:
Sentence: Finally , percutaneous methods for the exclusion of left atrial appendage are under investigation in high-risk patients .

Example answer:
{"entities": []}

Example input:
Sentence: INTERVENTION AND OUTCOME : An 18-gauge Touhy needle was inserted until loss of resistance occurred at the L4-5 level .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : A double-blind double-armed prospective study comprised 40 patients who had uneventful sutureless phacoemulsification under sub-Tenon 's local infiltration of 3 mL of plain lignocaine .

Example answer:
{"entities": [{"text": "lignocaine", "type": "Chemical"}]}

Input:
Sentence: The sutures were passed individually through four tourniquets and exteriorized untied via the left atriotomy .

## Item bc5cdr:test:3095
Example input:
Sentence: After 35 days in the TG + HAART cohort , left ventricular mass increased 160 % by echocardiography .

Example answer:
{"entities": []}

Example input:
Sentence: Pathologically , granular cytoplasmic changes were found in cardiac myocytes , indicating enlarged , damaged mitochondria .

Example answer:
{"entities": []}

Example input:
Sentence: The pooled statistical analysis for ventricular septal ( VSD ) and midline ( MD ) defects was performed for rat fetuses exposed to piroxicam , selective and non-selective COX-2 inhibitor based on present and historic data .

Example answer:
{"entities": [{"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: A patient with sinuatrial disease and implanted pacemaker was treated with amiodarone ( maximum dose 1000 mg , maintenance dose 800 mg daily ) for 10 months , for control of supraventricular tachyarrhythmias .

Example answer:
{"entities": [{"text": "sinuatrial disease", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "supraventricular tachyarrhythmias", "type": "Disease"}]}

Example input:
Sentence: The expression of arginine vasopressin ( AVP ) gene in the paraventricular ( PVN ) and supraoptic nuclei ( SON ) was investigated in rats with lithium ( Li ) -induced polyuria , using in situ hybridization histochemistry and radioimmunoassay .

Example answer:
{"entities": [{"text": "arginine vasopressin", "type": "Chemical"}, {"text": "AVP", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "Li", "type": "Chemical"}, {"text": "polyuria", "type": "Disease"}]}

Example input:
Sentence: End-systolic left ventricular posterior wall dimension at the 5-micrograms/kg per min dobutamine infusion for the doxorubicin-treated group was 14.1 +/- 2.4 mm versus 19.3 +/- 2.6 mm for control subjects ( p less than 0.01 ) .

Example answer:
{"entities": [{"text": "dobutamine", "type": "Chemical"}, {"text": "doxorubicin-treated", "type": "Chemical"}]}

Example input:
Sentence: By using transthoracic echocardiography , anterior and posterior wall thickness , LV diameters and LV fractional shortening ( FS ) were measured in all rats before DOX or saline , and at weeks 6 and 9 after treatment in all surviving rats .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: The most important findings were that compared with values in control subjects , end-systolic left ventricular posterior wall dimension and percent of left ventricular posterior wall thickening in doxorubicin-treated patients were decreased at baseline study and these findings were more clearly delineated with dobutamine stimulation .

Example answer:
{"entities": [{"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}]}

Example input:
Sentence: Under anesthesia , the superior temporal gyrus of adult macaque monkeys was exposed , and the tonotopic organization of A1 was mapped using conventional microelectrode recording techniques .

Example answer:
{"entities": []}

Example input:
Sentence: At termination of the experiments , mice underwent echocardiography , quantitation of abundance of molecular markers of CM ( ventricular mRNA encoding atrial natriuretic factor [ ANF ] and sarcoplasmic calcium ATPase [ SERCA2 ] ) , and determination of plasma LA .

Example answer:
{"entities": [{"text": "CM", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "LA", "type": "Chemical"}]}

Input:
Sentence: Sonomicrometry crystals were implanted around the mitral annulus and left ventricle to measure geometry and regional function .

## Item bc5cdr:test:1644
Example input:
Sentence: Lesions reduced the extent of immunohistological staining for choline acetyltransferase in the interpeduncular nucleus ( p < 0.025 ) , but not for tyrosine hydroxylase in the surrounding catecholaminergic A10 region .

Example answer:
{"entities": []}

Example input:
Sentence: One h after treatment , serum prolactin levels decreased markedly .

Example answer:
{"entities": []}

Example input:
Sentence: After EE treatment , changes in immunostaining for 7H6 and ZO-1 were similar to those seen in periportal hepatocytes after BDL , but distributed more diffusely throughout the lobule .

Example answer:
{"entities": [{"text": "EE", "type": "Chemical"}]}

Example input:
Sentence: Sulpiride induced only SOCS-1 in the medial preoptic area , where GnRH neurons are regulated , but in the arcuate nucleus and choroid plexus , PRL-R , SOCS-3 , and CIS mRNA levels were also induced .

Example answer:
{"entities": [{"text": "Sulpiride", "type": "Chemical"}]}

Example input:
Sentence: Hypothalamic prolactin receptor messenger ribonucleic acid levels , prolactin signaling , and hyperprolactinemic inhibition of pulsatile luteinizing hormone secretion are dependent on estradiol .

Example answer:
{"entities": [{"text": "ribonucleic acid", "type": "Chemical"}, {"text": "hyperprolactinemic", "type": "Disease"}, {"text": "estradiol", "type": "Chemical"}]}

Example input:
Sentence: On the other hand , pretreatment with p-chlorophenylalamine ( 3 X 320 mg/kg i.p. , 24 hr ) , a serotonin depletor , caused no significant change in the hyperactivity .

Example answer:
{"entities": [{"text": "p-chlorophenylalamine", "type": "Chemical"}, {"text": "serotonin", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}]}

Example input:
Sentence: We first tested whether chronic hyperprolactinemia inhibited two neuroendocrine parameters necessary for female fertility : pulsatile LH secretion and the estrogen-induced LH surge .

Example answer:
{"entities": [{"text": "hyperprolactinemia", "type": "Disease"}, {"text": "estrogen-induced", "type": "Chemical"}]}

Example input:
Sentence: However , only secretory granules showed the positive reaction products for prolactin 6 h after bromocriptine treatment of the adenoma cells .

Example answer:
{"entities": [{"text": "bromocriptine", "type": "Chemical"}, {"text": "adenoma", "type": "Disease"}]}

Example input:
Sentence: In the present study , we investigated the changes occurring at the protein level in striatal samples obtained from the unilaterally 6-hydroxydopamine-lesion rat model of PD treated with saline , L-DOPA or bromocriptine using two-dimensional difference gel electrophoresis and mass spectrometry ( MS ) .

Example answer:
{"entities": [{"text": "6-hydroxydopamine-lesion", "type": "Chemical"}, {"text": "PD", "type": "Disease"}, {"text": "L-DOPA", "type": "Chemical"}, {"text": "bromocriptine", "type": "Chemical"}]}

Example input:
Sentence: Chronic hyperprolactinemia induced by the dopamine antagonist sulpiride caused a 40 % reduction LH pulse frequency in ovariectomized rats , but only in the presence of chronic low levels of estradiol .

Example answer:
{"entities": [{"text": "hyperprolactinemia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "sulpiride", "type": "Chemical"}, {"text": "estradiol", "type": "Chemical"}]}

Input:
Sentence: There was no change in the levels of DA , norepinephrine ( NE ) , serotonin ( 5-HT ) , or their metabolites in the arcuate nucleus ( AN ) , medial preoptic area ( MPA ) , caudate putamen ( CP ) , substantia nigra ( SN ) , and zona incerta ( ZI ) , except for a decrease in 5-hydroxyindoleacetic acid ( 5-HIAA ) in the AN after 6-months of hyperprolactinemia and an increase in DA concentrations in the AN after 9-months of hyperprolactinemia .

## Item bc5cdr:test:3100
Example input:
Sentence: Subsequent addition of phenylephrine infusion , sufficient to re-elevate mean arterial pressure to 106 +/- 4 mm Hg ( P less than 0.001 ) for 30 minutes , increased left ventricular filling pressure to 17 +/- 2 mm Hg ( P less than 0.05 ) and also significantly increased sigmaST ( P less than 0.05 ) .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}]}

Example input:
Sentence: At normal [ Na ] o , decrease ( 0.675 mM ) or increase ( 3.6 mM ) of [ Ca ] o did not modify BF ; a reduction of ten times ( 0.135 mM of normal [ Ca ] o was effective to reduce BF by 40 +/- 13 % .

Example answer:
{"entities": [{"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}]}

Example input:
Sentence: In the five rats that developed somatic rigidity , ICP and CVP increased significantly above baseline ( delta ICP 7.5 +/- 1.0 mmHg , delta CVP 5.9 +/- 1.3 mmHg ) .

Example answer:
{"entities": [{"text": "somatic rigidity", "type": "Disease"}]}

Example input:
Sentence: End-systolic left ventricular posterior wall dimension at baseline for the doxorubicin-treated group was 11 +/- 1.9 mm versus 13.1 +/- 1.5 mm for control subjects ( p less than 0.01 ) .

Example answer:
{"entities": [{"text": "doxorubicin-treated", "type": "Chemical"}]}

Example input:
Sentence: The SPV during hypotension was 15.7 +/- 6.7 mm Hg in the HEM group , compared with 9.1 +/- 2.0 mm Hg in the SNP group ( P less than 0.02 ) .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "HEM", "type": "Disease"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: It decreased by 16 +/- 3 % by lowering [ Na ] o to 78 mM ( LNa ) , 23 +/- 2 % by lowering simultaneously [ Na ] o to 78 mM and [ Ca ] o to 0.675 mM ( LNa+LCa ) and 31 +/- 5 % by lowering [ Na ] o to 78 mM plus increasing [ Ca ] o to 3.6 mM ( LNa+HCa ) .

Example answer:
{"entities": [{"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}]}

Example input:
Sentence: Analysis of data revealed a significant correlation between maximal cTnT and ED and ES LV diameters/BW ( r=0.81 and 0.65 ; p < 0.0001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Left ventricular filling pressure decreased from 19 +/- 2 to 11 +/- 2 mm Hg ( P less than 0.001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: By using transthoracic echocardiography , anterior and posterior wall thickness , LV diameters and LV fractional shortening ( FS ) were measured in all rats before DOX or saline , and at weeks 6 and 9 after treatment in all surviving rats .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: End-diastolic ( ED ) and end-systolic ( ES ) LV diameters/BW significantly increased , whereas LV FS was decreased after 9 weeks in the DOX group ( p < 0.001 ) .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Input:
Sentence: Concomitantly , the diastolic diameter of the LV base and LV sphericity decreased ( i.e. , improved ) from 37.4 +/- 9.3 to 35.9 +/- 10 mm ( p = 0.063 ) , and from 67.9 +/- 18.6 % to 65.3 +/- 18.9 % ( p = 0.016 ) , respectively .

## Item bc5cdr:test:2944
Example input:
Sentence: The aorta/serum-ratio and the radioactive build-up 24 and 48 hours after injection of 131I-HSA was reduced in animals treated with D-pen for 42 days , indicating an impeded transmural transport of tracer which may be caused by a steric exclusion effect of abundant hyaluronate .

Example answer:
{"entities": [{"text": "D-pen", "type": "Chemical"}, {"text": "hyaluronate", "type": "Chemical"}]}

Example input:
Sentence: The results indicated that concomitant treatment with gum Arabic and GM significantly increased creatinine and urea by about 183 and 239 % , respectively ( compared to 432 and 346 % , respectively , in rats treated with cellulose and GM ) , and decreased that of cortical GSH by 21 % ( compared to 27 % in the cellulose plus GM group ) The GM-induced proximal tubular necrosis appeared to be slightly less severe in rats given GM together with gum Arabic than in those given GM and cellulose .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}, {"text": "urea", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "GM-induced", "type": "Chemical"}, {"text": "tubular necrosis", "type": "Disease"}]}

Example input:
Sentence: Induction of intravascular coagulation and inhibition of fibrinolysis by injection of thrombin and tranexamic acid ( AMCA ) in the rat gives rise to pulmonary and renal insufficiency resembling that occurring after trauma or sepsis in man .

Example answer:
{"entities": [{"text": "intravascular coagulation", "type": "Disease"}, {"text": "tranexamic acid", "type": "Chemical"}, {"text": "AMCA", "type": "Chemical"}, {"text": "trauma", "type": "Disease"}, {"text": "sepsis", "type": "Disease"}]}

Example input:
Sentence: We found that maltolyl p-coumarate significantly decreased apoptotic cell death and reduced reactive oxygen species , cytochrome c release , and caspase 3 activation .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}]}

Example input:
Sentence: Mitochondrial radiocalcium uptakes were significantly decreased in animals pretreated with acetylsalicylic acid or dipyridamole or when hydrocortisone was added to the epinephrine infusion ( 2,682,2,803 , and 3,424 counts per minute per gram of dried fraction , respectively ) .

Example answer:
{"entities": [{"text": "radiocalcium", "type": "Chemical"}, {"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine", "type": "Chemical"}]}

Example input:
Sentence: The lung weights were lower and PaO2 was improved in rats given this enzyme-blocking agent .

Example answer:
{"entities": []}

Example input:
Sentence: Independent but not additive effects of Na and Ca are shown by decreases in the values of [ verapamil ] o needed to reduce BF by 30 % ( IC30 ) with the following order of inhibitory potency : LNa > LCa > HCa > N , resulting LNa+HCa similar to LNa .

Example answer:
{"entities": [{"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : This study establishes a TAA model by periarterial CaCl ( 2 ) exposure in rats , and demonstrates a significant elevation of expression of MMP-2 , MMP-9 , ADAM10 and ADAM17 in the pathogenesis of vascular remodeling .

Example answer:
{"entities": [{"text": "TAA", "type": "Disease"}, {"text": "CaCl ( 2 )", "type": "Chemical"}]}

Example input:
Sentence: PURPOSE : This study was designed to establish a rat model of thoracic aortic aneurysm ( TAA ) by calcium chloride ( CaCl ( 2 ) ) -induced arterial injury and to explore the potential role of a disintegrin and metalloproteinase ( ADAM ) , matrix metalloproteinases ( MMPs ) and their endogenous inhibitors ( TIMPs ) in TAA formation .

Example answer:
{"entities": [{"text": "thoracic aortic aneurysm", "type": "Disease"}, {"text": "TAA", "type": "Disease"}, {"text": "calcium chloride", "type": "Chemical"}, {"text": "CaCl ( 2 )", "type": "Chemical"}, {"text": "arterial injury", "type": "Disease"}]}

Example input:
Sentence: Based on clinical data , indicating that chloroacetaldehyde ( CAA ) is an important metabolite of oxazaphosphorine cytostatics , an experimental study was carried out in order to elucidate the role of CAA in the development of hemorrhagic cystitis .

Example answer:
{"entities": [{"text": "chloroacetaldehyde", "type": "Chemical"}, {"text": "CAA", "type": "Chemical"}]}

Input:
Sentence: Acidification , which slowed the reaction of CAA with thiol donors , could also attenuate effects of CAA on necrosis markers , thiol depletion and cysteine protease inhibition in living cells .

## Item bc5cdr:test:2831
Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: We report a woman with coronary artery disease who developed a markedly prolonged QT interval and torsades de pointes ( TdP ) after taking ketoconazole for treatment of fungal infection .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "prolonged QT interval", "type": "Disease"}, {"text": "torsades de pointes", "type": "Disease"}, {"text": "TdP", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "fungal infection", "type": "Disease"}]}

Example input:
Sentence: TDP is a side-effect that has led to withdrawal of several drugs from the market ( e.g .

Example answer:
{"entities": [{"text": "TDP", "type": "Disease"}]}

Example input:
Sentence: In addition , reflex bradycardia caused by injected norepinephrine was significantly enhanced by L-dopa , DL-Threo-dihydroxyphenylserine had no effect on blood pressure , heart rate or reflex responses to norepinephrine .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}, {"text": "DL-Threo-dihydroxyphenylserine", "type": "Chemical"}]}

Example input:
Sentence: After starting PGE1 or TMP , MAP and rate pressure product ( RPP ) decreased significantly compared with preinfusion values ( P < 0.01 ) , and the degree of hypotension due to PGE1 remained constant until 60 min after its discontinuation .

Example answer:
{"entities": [{"text": "PGE1", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: However , L-dopa restored the bradycardia caused by norepinephrine in addition to decreasing blood pressure and heart rate .

Example answer:
{"entities": [{"text": "L-dopa", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}]}

Example input:
Sentence: The potential of compounds to cause TDP was evaluated by monitoring their effects on MAPD in dog .

Example answer:
{"entities": [{"text": "TDP", "type": "Disease"}]}

Example input:
Sentence: We postulate that by virtue of its direct blocking action on IKr , ketoconazole alone may prolong QT interval and induce TdP .

Example answer:
{"entities": [{"text": "ketoconazole", "type": "Chemical"}, {"text": "TdP", "type": "Disease"}]}

Example input:
Sentence: Torsades de pointes ( TDP ) is a potentially fatal ventricular tachycardia associated with increases in QT interval and monophasic action potential duration ( MAPD ) .

Example answer:
{"entities": [{"text": "Torsades de pointes", "type": "Disease"}, {"text": "TDP", "type": "Disease"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: Four compounds known to increase QT interval and cause TDP were investigated : terfenadine , terodiline , cisapride and E4031 .

Example answer:
{"entities": [{"text": "TDP", "type": "Disease"}, {"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}, {"text": "E4031", "type": "Chemical"}]}

Input:
Sentence: The major triggering factors of Tdp were hypokalemia and sudden decrease in heart rate .

## Item bc5cdr:test:3121
Example input:
Sentence: CONCLUSIONS : Prilocaine may be preferable to lidocaine for short surgical procedures because it has a similar duration of action but a lower incidence of TNSs .

Example answer:
{"entities": [{"text": "Prilocaine", "type": "Chemical"}, {"text": "lidocaine", "type": "Chemical"}, {"text": "TNSs", "type": "Disease"}]}

Example input:
Sentence: Thirty-six patients were treated with BCNU every 6 to 8 weeks , either by transfemoral catheterization of the internal carotid or vertebral artery or through a fully implantable intracarotid drug delivery system , beginning with a dose of 200 mg/sq m body surface area .

Example answer:
{"entities": [{"text": "BCNU", "type": "Chemical"}]}

Example input:
Sentence: Since the cranial condition precluded use of more usual methods , lidocaine was given intra-arterially , with careful cardiovascular monitoring , to counteract the vasospasm .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "vasospasm", "type": "Disease"}]}

Example input:
Sentence: Cerebral blood flow and cerebral metabolic rate for oxygen were measured during isoflurane-induced hypotension in 10 patients subjected to craniotomy for clipping of a cerebral aneurysm .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "isoflurane-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "cerebral aneurysm", "type": "Disease"}]}

Example input:
Sentence: METHODS : A double-blind double-armed prospective study comprised 40 patients who had uneventful sutureless phacoemulsification under sub-Tenon 's local infiltration of 3 mL of plain lignocaine .

Example answer:
{"entities": [{"text": "lignocaine", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Following induction of anesthesia by fentanyl ( 0.15 mg kg ( -1 ) ) and propofol ( 2.0 mg kg ( -1 ) ) , 13 patients received phenylephrine ( 0.1 mg iv ) and 12 patients received ephedrine ( 10 mg iv ) to restore mean arterial pressure ( MAP ) .

Example answer:
{"entities": [{"text": "fentanyl", "type": "Chemical"}, {"text": "propofol", "type": "Chemical"}, {"text": "phenylephrine", "type": "Chemical"}, {"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: METHODS : We conducted a retrospective review of 70 consecutive microvascular decompression operations and studied those patients who received topical papaverine for vasospasm .

Example answer:
{"entities": [{"text": "papaverine", "type": "Chemical"}, {"text": "vasospasm", "type": "Disease"}]}

Example input:
Sentence: Following major intracranial surgery in a 35-year-old man , sodium pentothal was intravenously infused to minimize cerebral ischaemia .

Example answer:
{"entities": [{"text": "sodium pentothal", "type": "Chemical"}, {"text": "cerebral ischaemia", "type": "Disease"}]}

Example input:
Sentence: METHODS : Ninety patients classified as American Society of Anesthesiologists physical status I or II who were scheduled for short gynecologic procedures under spinal anesthesia were randomly allocated to receive 2.5 ml 2 % lidocaine in 7.5 % glucose , 2 % prilocaine in 7.5 % glucose , or 0.5 % bupivacaine in 7.5 % glucose .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "glucose", "type": "Chemical"}, {"text": "prilocaine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: Reduction in injection pain using buffered lidocaine as a local anesthetic before cardiac catheterization .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}]}

Input:
Sentence: METHODS : This prospective study included 28 patients undergoing carotid endarterectomy under local anesthesia .

## Item bc5cdr:test:2623
Example input:
Sentence: METHODS : We used computerized pharmacy records to identify all adult psychiatric inpatients treated with clozapine ( 1995-96 ) , reviewed their medical records to score incidence and severity of delirium , and tested associations with potential risk factors .

Example answer:
{"entities": [{"text": "psychiatric", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "delirium", "type": "Disease"}]}

Example input:
Sentence: Mean post-SCr increases were significantly less with iopamidol ( all patients : 0.07 versus 0.12 mg/dL , 6.2 versus 10.6 micromol/L , P=0.03 ; patients with diabetes : 0.07 versus 0.16 mg/dL , 6.2 versus 14.1 micromol/L , P=0.01 ) .

Example answer:
{"entities": [{"text": "iopamidol", "type": "Chemical"}, {"text": "diabetes", "type": "Disease"}]}

Example input:
Sentence: In patients with diabetes , SCr increases > or = 0.5 mg/dL were 5.1 % ( 4 of 78 patients ) with iopamidol and 13.0 % ( 12 of 92 patients ) with iodixanol ( P=0.11 ) , whereas SCr increases > or = 25 % were 10.3 % and 15.2 % , respectively ( P=0.37 ) .

Example answer:
{"entities": [{"text": "diabetes", "type": "Disease"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}]}

Example input:
Sentence: There was no significant difference between occupancy levels obtained with haloperidol or risperidone .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "risperidone", "type": "Chemical"}]}

Example input:
Sentence: To determine if routine risperidone treatment is associated with a unique degree of D2 receptor occupancy and pattern of clinical effects , we used [ 123I ] IBZM SPECT to determine D2 occupancy in subjects treated with routine clinical doses of risperidone ( n = 12 ) or haloperidol ( n = 7 ) .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Previous clinical studies have proposed that risperidone 's pharmacologic profile may produce improved efficacy for negative psychotic symptoms and decreased propensity for extrapyramidal side effects ; features shared by so-called 'atypical ' neuroleptics .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}, {"text": "psychotic symptoms", "type": "Disease"}]}

Example input:
Sentence: Risperidone is an antipsychotic drug with high affinity at dopamine D2 and serotonin 5-HT2 receptors .

Example answer:
{"entities": [{"text": "Risperidone", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "serotonin 5-HT2", "type": "Chemical"}]}

Example input:
Sentence: Considering that clozapine remains the gold standard in treatment of resistant psychosis , there is an urgent need to raise awareness among medical and paramedical staff involved in the care of these patients .

Example answer:
{"entities": [{"text": "clozapine", "type": "Chemical"}, {"text": "psychosis", "type": "Disease"}]}

Example input:
Sentence: Importantly , both classical ( haloperidol ) and atypical ( olanzapine , clozapine and aripiprazole ) antipsychotics were effective in all these models of hyperactivity .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "olanzapine", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "aripiprazole", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Input:
Sentence: There was a significant difference in insulin sensitivity index among groups ( F ( 33 ) = 10.66 ; P < .001 ) ( clozapine < olanzapine < risperidone ) , with subjects who received clozapine and olanzapine exhibiting significant insulin resistance compared with subjects who were treated with risperidone ( clozapine vs risperidone , t ( 33 ) = -4.29 ; P < .001 ; olanzapine vs risperidone , t ( 33 ) = -3.62 ; P = .001 [ P < .001 ] ) .

## Item bc5cdr:test:2982
Example input:
Sentence: This study describes neuropsychiatric side effects in patients after treatment with mefloquine .

Example answer:
{"entities": [{"text": "mefloquine", "type": "Chemical"}]}

Example input:
Sentence: Other possible adverse effects -- such as gastrointestinal disorders , orthostatic hypotension , levodopa-induced psychosis , sleep disturbances or parasomnias , or drug interactions -- also require carefully monitored individual treatment .

Example answer:
{"entities": [{"text": "gastrointestinal disorders", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "levodopa-induced", "type": "Chemical"}, {"text": "psychosis", "type": "Disease"}, {"text": "sleep disturbances", "type": "Disease"}, {"text": "parasomnias", "type": "Disease"}]}

Example input:
Sentence: We prospectively evaluated the adverse reactions of apraclonidine in 20 normal volunteers by instilling a single drop of 1 % apraclonidine in their right eyes .

Example answer:
{"entities": [{"text": "apraclonidine", "type": "Chemical"}]}

Example input:
Sentence: Various ocular symptoms and findings caused by carboplatin toxicity were seen .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVE : To examine the effect of raloxifene on major adverse events that occur with postmenopausal estrogen therapy or tamoxifen .

Example answer:
{"entities": [{"text": "raloxifene", "type": "Chemical"}, {"text": "estrogen", "type": "Chemical"}, {"text": "tamoxifen", "type": "Chemical"}]}

Example input:
Sentence: An analysis is presented of 220 cases of possible neurotoxic reactions to halogenated hydroxyquinolines reported from outside Japan .

Example answer:
{"entities": [{"text": "neurotoxic", "type": "Disease"}, {"text": "halogenated hydroxyquinolines", "type": "Chemical"}]}

Example input:
Sentence: Neurotoxicity of halogenated hydroxyquinolines : clinical analysis of cases reported outside Japan .

Example answer:
{"entities": [{"text": "Neurotoxicity", "type": "Disease"}, {"text": "halogenated hydroxyquinolines", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVE : To report a case of central retinal vein occlusion associated with clomiphene citrate ( CC ) .

Example answer:
{"entities": [{"text": "retinal vein occlusion", "type": "Disease"}, {"text": "clomiphene citrate", "type": "Chemical"}, {"text": "CC", "type": "Chemical"}]}

Example input:
Sentence: An objective causality assessment revealed that the adverse drug event was probably related to the use of ticlopidine .

Example answer:
{"entities": [{"text": "ticlopidine", "type": "Chemical"}]}

Example input:
Sentence: The ocular hypotensive effects were statistically significant for apraclonidine-treated eyes throughout the study and also statistically significant for contralateral eyes from three hours after topical administration of 1 % apraclonidine .

Example answer:
{"entities": [{"text": "ocular hypotensive", "type": "Disease"}, {"text": "apraclonidine-treated", "type": "Chemical"}, {"text": "apraclonidine", "type": "Chemical"}]}

Input:
Sentence: OBJECTIVE : To review the natural history and ocular and systemic adverse effects of patients taking hydroxychloroquine sulfate who attended an ophthalmic screening program .

## Item bc5cdr:test:2338
Example input:
Sentence: PATIENTS AND METHODS : Forty-two patients with biopsy-proven prostatic adenocarcinoma [ 26 with stage C ( T3N0M0 ) and 16 with stage D1 ( T3N1M0 ) ] were included in this study .

Example answer:
{"entities": [{"text": "prostatic adenocarcinoma", "type": "Disease"}]}

Example input:
Sentence: together for 30 consecutive days and challenged with ISO on the day 29th and 30th , showed a significant ( P < 0.05 ) decrease in heart weight , serum marker enzymes , lipid peroxidation , Ca+2 ATPase and a significant increase in the body weight , endogenous antioxidants , Na+/K+ ATPase and Mg+2 ATPase when compared with ISO treated group and green tea or vitamin E alone treated groups .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}, {"text": "green tea", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}]}

Example input:
Sentence: Compared with control patients , CRF and ESRD patients had higher preoperative serum creatinine levels , a greater percentage of patients with hepatorenal syndrome , higher percentage requirement for dialysis in the first 3 months postoperatively , and a higher 1-year serum creatinine .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "hepatorenal syndrome", "type": "Disease"}]}

Example input:
Sentence: All the patients were skin test negative to BPO ; 49 of 51 ( 96 % ) were also negative to MDM , and 44 of 46 ( 96 % ) to PG .

Example answer:
{"entities": [{"text": "BPO", "type": "Chemical"}, {"text": "MDM", "type": "Disease"}, {"text": "PG", "type": "Chemical"}]}

Example input:
Sentence: The development of severe CAB-induced anemia in prostate cancer patients did not correlate with T baseline values ( T < 3 ng/ml versus T > or = 3 ng/ml ) , with age ( < 76 yrs versus > or = 76 yrs ) , and clinical stage ( stage C versus stage D1 ) .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "prostate cancer", "type": "Disease"}]}

Example input:
Sentence: In the present study , cis-platin ( 80-120 mg/m2BSA ) and 5-FU ( 1000 mg/m2BSA daily as a continuous infusion during 5 days ) were given to 76 patients before radiotherapy and surgery .

Example answer:
{"entities": [{"text": "cis-platin", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}]}

Example input:
Sentence: Patients were admitted to the hospital for measurement of lithium level , creatinine clearance , urine volume , and maximum osmolality .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : Our data suggest that rHuEPO-beta correctable CAB-induced anemia occurs in 14.3 % of prostate cancer patients after 6 months of therapy .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "prostate cancer", "type": "Disease"}]}

Example input:
Sentence: Hb , PSA and Testosterone measurements were recorded .

Example answer:
{"entities": [{"text": "Testosterone", "type": "Chemical"}]}

Example input:
Sentence: Every patient was screened for testosterone and 451 were screened for prolactin on the basis of low sexual desire , gynecomastia or testosterone less than 4 ng./ml .

Example answer:
{"entities": [{"text": "testosterone", "type": "Chemical"}, {"text": "low sexual desire", "type": "Disease"}, {"text": "gynecomastia", "type": "Disease"}]}

Input:
Sentence: Patients underwent regular measurement of prostate-specific antigen ( PSA ) , urea and electrolytes , serum bFGF and VEGF .

## Item bc5cdr:test:2886
Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: A comparable overexpression of Pgp in the BBB was obtained after pilocarpine-induced seizures in wild-type Wistar rats .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: QTLs for susceptibility to pilocarpine-induced seizures , a model of temporal lobe epilepsy , have not been reported , and CSS have not previously been used to localize seizure susceptibility genes .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: Therefore , like VPA , the finding that VPU could drastically reduce pilocarpine-induced increases in glutamate and aspartate should account , at least partly , for its anticonvulsant activity observed in pilocarpine-induced seizure in experimental animals .

Example answer:
{"entities": [{"text": "VPA", "type": "Chemical"}, {"text": "VPU", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: We report QTLs identified using a B6 ( host ) x A/J ( donor ) CSS panel to localize genes involved in susceptibility to pilocarpine-induced seizures .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Investigation of mitochondrial involvement in the experimental model of epilepsy induced by pilocarpine .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: Three hundred fifty-five adult male CSS mice , 58 B6 , and 39 A/J were tested for susceptibility to pilocarpine-induced seizures .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Based on the finding that VPU and VPA could protect the animals against pilocarpine-induced seizure it is suggested that the reduction of inhibitory amino acid neurotransmitters was comparatively minor and offset by a pronounced reduction of glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: Similar to rats , systemic pilocarpine injection causes status epilepticus ( SE ) and the eventual development of spontaneous seizures and mossy fiber sprouting in C57BL/6 and CD1 mice , but the physiological correlates of these events have not been identified in mice .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Input:
Sentence: Thereafter , seizures were induced by pilocarpine injections in trained and non-trained control groups .

## Item bc5cdr:test:3179
Example input:
Sentence: Compared with control patients , CRF and ESRD patients had higher preoperative serum creatinine levels , a greater percentage of patients with hepatorenal syndrome , higher percentage requirement for dialysis in the first 3 months postoperatively , and a higher 1-year serum creatinine .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "hepatorenal syndrome", "type": "Disease"}]}

Example input:
Sentence: Two patients with similar clinical features are presented : both patients had chronic renal failure , on hemodialysis for many years but recently begun on a high-flux dialyzer ; both had been receiving a carbidopa/levodopa preparation ; and both had the onset of hallucinosis and recurrent seizures , which were refractory to anticonvulsants .

Example answer:
{"entities": [{"text": "chronic renal failure", "type": "Disease"}, {"text": "carbidopa/levodopa", "type": "Chemical"}, {"text": "hallucinosis", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Therefore , in adult patients affected by HUS , dialysis should not be discontinued prematurely ; moreover , bilateral nephrectomy , for treatment of severe hypertension and microangiopathic hemolytic anemia , should be performed with caution .

Example answer:
{"entities": [{"text": "HUS", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "microangiopathic hemolytic anemia", "type": "Disease"}]}

Example input:
Sentence: The development of ESRD decreases survival , particularly in those patients treated with dialysis only .

Example answer:
{"entities": [{"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Potassium was applied by reverse dialysis twice , separated by 75 min .

Example answer:
{"entities": [{"text": "Potassium", "type": "Chemical"}]}

Example input:
Sentence: She was treated with heparin , dipyridamole and hemodialysis ; and after more than three months , her urinary output rose above 500 ml ; and six months after the onset of anuria , dialysis treatment was stopped .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "anuria", "type": "Disease"}]}

Example input:
Sentence: The patient was discharged and continued outpatient dialysis for 1 month until his renal function recovered .

Example answer:
{"entities": []}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Disease"}]}

Example input:
Sentence: Thus , interference with the central venous infusion by the dialysis catheter was suspected .

Example answer:
{"entities": []}

Example input:
Sentence: The abruptness of the renal failure and its reversibility within days suggests that there was a functional component to the renal dysfunction .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "renal dysfunction", "type": "Disease"}]}

Input:
Sentence: Dialysis was immediately initiated .

## Item bc5cdr:test:3199
Example input:
Sentence: Autoantibodies against P450 2E1 or P58 , previously associated with halothane hepatitis , were detected in the serum of five affected workers .

Example answer:
{"entities": [{"text": "halothane hepatitis", "type": "Disease"}]}

Example input:
Sentence: The objective of this study was to report our experience concerning the effectiveness of the prophylactic administration of lamivudine in hepatitis B virus surface antigen ( HBs Ag ) positive patients with rheumatologic disease .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}, {"text": "hepatitis B virus surface antigen", "type": "Chemical"}, {"text": "HBs Ag", "type": "Chemical"}, {"text": "rheumatologic disease", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : This is the first study in the literature investigating a link between angiogenesis soluble markers and ribavirin induced anemia in patients with hepatitis C and we could not find any relation .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "anemia", "type": "Disease"}, {"text": "hepatitis C", "type": "Disease"}]}

Example input:
Sentence: In the prophylactic lamivudine group severe hepatitis were observed only in 1 patient ( 2.7 % ) of 37 patients ( p < 0.006 ) .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: However , the concomitant occurrence of HBeAg negativity ( PC/BCP ) , sP120T , and LAM resistance resulted in the restoration of replication to levels of wild-type HBV .

Example answer:
{"entities": [{"text": "HBeAg", "type": "Chemical"}, {"text": "LAM", "type": "Chemical"}]}

Example input:
Sentence: Cancer patients who are chronic carriers of HBV have a higher hepatic complication rate while receiving cytotoxic chemotherapy ( CT ) and this has mainly been attributed to HBV reactivation .

Example answer:
{"entities": [{"text": "Cancer", "type": "Disease"}, {"text": "hepatic complication", "type": "Disease"}]}

Example input:
Sentence: Biological features of hepatitis disappeared in all cases after cessation of the incriminated drug , while biliary , viral and immunological searches were negative .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Cholestatic hepatitis is a rare adverse effect of ticlopidine that may be immune mediated .

Example answer:
{"entities": [{"text": "ticlopidine", "type": "Chemical"}]}

Example input:
Sentence: In this study , cancer patients who have solid and hematological malignancies with chronic HBV infection received the antiviral agent lamivudine prior and during CT compared with historical control group who did not receive lamivudine .

Example answer:
{"entities": [{"text": "cancer", "type": "Disease"}, {"text": "hematological malignancies", "type": "Disease"}, {"text": "HBV infection", "type": "Disease"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: From these results , we conclude that ribavirin has an antiviral effect in advanced cases of AHF , and that anemia , the only secondary reaction observed , can be easily managed .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "AHF", "type": "Disease"}, {"text": "anemia", "type": "Disease"}]}

Input:
Sentence: Anti-HCV was negative in all of them .

## Item bc5cdr:test:2783
Example input:
Sentence: In males , the non-competitive NMDA antagonist dextromethorphan enhanced the antihyperalgesic effect of low to moderate doses of morphine in a dose-and time-dependent manner .

Example answer:
{"entities": [{"text": "NMDA", "type": "Chemical"}, {"text": "dextromethorphan", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: Acute reserpine and subchronic haloperidol treatments change synaptosomal brain glutamate uptake and elicit orofacial dyskinesia in rats .

Example answer:
{"entities": [{"text": "reserpine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "orofacial dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Other possible adverse effects -- such as gastrointestinal disorders , orthostatic hypotension , levodopa-induced psychosis , sleep disturbances or parasomnias , or drug interactions -- also require carefully monitored individual treatment .

Example answer:
{"entities": [{"text": "gastrointestinal disorders", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "levodopa-induced", "type": "Chemical"}, {"text": "psychosis", "type": "Disease"}, {"text": "sleep disturbances", "type": "Disease"}, {"text": "parasomnias", "type": "Disease"}]}

Example input:
Sentence: Compared with placebo subjects , alprazolam patients developed more adverse reactions ( 21 % v. 0 % ) of depression , enuresis , disinhibition and aggression ; and more side-effects , particularly sedation , irritability , impaired memory , weight loss and ataxia .

Example answer:
{"entities": [{"text": "alprazolam", "type": "Chemical"}, {"text": "depression", "type": "Disease"}, {"text": "enuresis", "type": "Disease"}, {"text": "aggression", "type": "Disease"}, {"text": "irritability", "type": "Disease"}, {"text": "impaired memory", "type": "Disease"}, {"text": "weight loss", "type": "Disease"}, {"text": "ataxia", "type": "Disease"}]}

Example input:
Sentence: However , use of BZDs/RDs was associated with dizziness , inability to sleep after awaking at night and tiredness in the mornings during the week prior to admission and with stronger depressive symptoms measured at the beginning of the hospital stay .

Example answer:
{"entities": [{"text": "BZDs/RDs", "type": "Chemical"}, {"text": "dizziness", "type": "Disease"}, {"text": "inability to sleep", "type": "Disease"}, {"text": "tiredness", "type": "Disease"}, {"text": "depressive symptoms", "type": "Disease"}]}

Example input:
Sentence: In contrast , monkeys with long-term MPTP exposure , slow symptom progression and/or long symptom duration prior to initiation of levodopa therapy were more resistant to developing LIDs ( e.g. , dyskinesia developed no sooner than 146 days of chronic levodopa administration ) .

Example answer:
{"entities": [{"text": "MPTP", "type": "Chemical"}, {"text": "levodopa", "type": "Chemical"}, {"text": "LIDs", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Whereas patient 1 showed lesions of up to 1 cm readily detectable on magnetic resonance imaging under prolonged co-trimoxazole treatment , therapy of patient 2 was switched early .

Example answer:
{"entities": [{"text": "co-trimoxazole", "type": "Chemical"}]}

Example input:
Sentence: In the present paper the authors describe 2 female patients who developed incontinence secondary to the selective serotonin reuptake inhibitors paroxetine and sertraline , as well as a third who developed this side effect on venlafaxine .

Example answer:
{"entities": [{"text": "incontinence", "type": "Disease"}, {"text": "serotonin", "type": "Chemical"}, {"text": "paroxetine", "type": "Chemical"}, {"text": "sertraline", "type": "Chemical"}, {"text": "venlafaxine", "type": "Chemical"}]}

Example input:
Sentence: The underlying mechanism of withdrawal-emergent RS in the present case may have been related to the pharmacological profile of risperidone , a serotonin-dopamine antagonist , suggesting the pathophysiologic influence of the serotonin system in the development of RS .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}, {"text": "serotonin-dopamine", "type": "Chemical"}, {"text": "serotonin", "type": "Chemical"}, {"text": "RS", "type": "Disease"}]}

Example input:
Sentence: Similarly , in patient diaries , although both treatments caused reduction in subjective dyskinesia scores during the days of intervention , the effect was sustained for 3 days after the intervention for the real rTMS only .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}]}

Input:
Sentence: Such a temporal relationship between the use of mirtazapine and the symptoms of RLS in our patient did not support a potentiating effect of domperione on mirtazapine-associated RLS .

## Item bc5cdr:test:2297
Example input:
Sentence: The most important findings were that compared with values in control subjects , end-systolic left ventricular posterior wall dimension and percent of left ventricular posterior wall thickening in doxorubicin-treated patients were decreased at baseline study and these findings were more clearly delineated with dobutamine stimulation .

Example answer:
{"entities": [{"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}]}

Example input:
Sentence: The effect of long-term timolol treatment on heart size after myocardial infarction was evaluated by X-ray in a double-blind study including 241 patients ( placebo 126 , timolol 115 ) .

Example answer:
{"entities": [{"text": "timolol", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: We suggest that our patient 's tubular dysfunction and myopathy may have resulted from mitochondrial dysfunction which is triggered by tacrolimus and augmented by lamivudine .

Example answer:
{"entities": [{"text": "tubular dysfunction", "type": "Disease"}, {"text": "myopathy", "type": "Disease"}, {"text": "mitochondrial dysfunction", "type": "Disease"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: We investigated the diagnostic value of cTnI and cTnT for the diagnosis of myocardial damage in a rat model of doxorubicin ( DOX ) -induced cardiomyopathy , and we examined the relationship between serial cTnI and cTnT with the development of cardiac disorders monitored by echocardiography and histological examinations in this model .

Example answer:
{"entities": [{"text": "myocardial damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiac disorders", "type": "Disease"}]}

Example input:
Sentence: Our results demonstrate that both cisplatin and paclitaxel cause early mitochondrial impairment with loss of membrane potential and induction of autophagic vacuoles in neurons .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "mitochondrial impairment", "type": "Disease"}]}

Example input:
Sentence: Administration of this regimen to breast cancer patients who have been treated by chemotherapy and those with impaired heart function requires careful attention .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "impaired heart function", "type": "Disease"}]}

Example input:
Sentence: Dobutamine stress echocardiography : a sensitive indicator of diminished myocardial function in asymptomatic doxorubicin-treated long-term survivors of childhood cancer .

Example answer:
{"entities": [{"text": "Dobutamine", "type": "Chemical"}, {"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: Mitochondrial injury may be involved in the progression of heart failure caused by adriamycin via the autophagy pathway .

Example answer:
{"entities": [{"text": "heart failure", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}]}

Example input:
Sentence: To develop a more sensitive echocardiographic screening test for cardiac damage due to doxorubicin , a cohort study was performed using dobutamine infusion to differentiate asymptomatic long-term survivors of childhood cancer treated with doxorubicin from healthy control subjects .

Example answer:
{"entities": [{"text": "cardiac damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: Doxorubicin is an effective anticancer chemotherapeutic agent known to cause acute and chronic cardiomyopathy .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}]}

Input:
Sentence: It is concluded that this protection by carvedilol against both the structural and functional cardiac tissue damage may afford significant clinical advantage in minimizing the dose-limiting mitochondrial dysfunction and cardiomyopathy that accompanies long-term doxorubicin therapy in cancer patients .

## Item bc5cdr:test:3033
Example input:
Sentence: It is recommended that further studies and investigations are undertaken in the effort to minimize such severe side effects .

Example answer:
{"entities": []}

Example input:
Sentence: The aim of the study was to assess the clinical significance of genetic variants in butyrylcholinesterase gene ( BCHE ) in patients with a suspected prolonged duration of action of succinylcholine after ECT .

Example answer:
{"entities": [{"text": "succinylcholine", "type": "Chemical"}]}

Example input:
Sentence: There is a need for a well-defined animal model in which these blood dyscrasias can be studied .

Example answer:
{"entities": [{"text": "blood dyscrasias", "type": "Disease"}]}

Example input:
Sentence: In recent years , evidence from animal models of Parkinson 's disease has provided important information to understand the effect of specific receptor and post-receptor molecular mechanisms underlying the development of dyskinetic movements .

Example answer:
{"entities": [{"text": "Parkinson 's disease", "type": "Disease"}, {"text": "dyskinetic movements", "type": "Disease"}]}

Example input:
Sentence: It has been shown to be extremely effective in the treatment of peptic ulcer disease , reflux esophagitis , and the Zollinger-Ellison syndrome .

Example answer:
{"entities": [{"text": "peptic ulcer disease", "type": "Disease"}, {"text": "reflux esophagitis", "type": "Disease"}, {"text": "Zollinger-Ellison syndrome", "type": "Disease"}]}

Example input:
Sentence: Following the initial period of therapy , emerging difficulties require a reassessment of therapeutic approaches , such as dosage adjustment or introduction of a dopamine agonist .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: Further research is needed to delineate the frequency of this troubling side effect and how best to treat it .

Example answer:
{"entities": []}

Example input:
Sentence: We describe a 15-yr-old girl who had orthotopic liver transplantation because of Wilson 's disease .

Example answer:
{"entities": [{"text": "Wilson 's disease", "type": "Disease"}]}

Example input:
Sentence: Further studies of specifically elderly patients are now required to establish safer and more appropriate guidelines for drug therapy .

Example answer:
{"entities": []}

Example input:
Sentence: Further studies are necessary to determine the exact extent of this problem and to improve the efficacy of diagnostic methods .

Example answer:
{"entities": []}

Input:
Sentence: Further studies are needed for a better clarification of Wilson 's disease therapy , and in particular to differentiate specific therapies for different Wilson 's disease phenotypes .

## Item bc5cdr:test:2819
Example input:
Sentence: Our studies indicate that nephrotoxicity of MTX + 5-FU + CY administered jointly is lower than in monotherapy .

Example answer:
{"entities": [{"text": "nephrotoxicity", "type": "Disease"}, {"text": "MTX", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "CY", "type": "Chemical"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: TCR prevented the isoproterenol-induced decrease in antioxidant enzymes in the heart and increased the rate of ADP-stimulated oxygen uptake and respiratory coupling ratio .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "ADP-stimulated", "type": "Chemical"}, {"text": "oxygen", "type": "Chemical"}]}

Example input:
Sentence: These findings indicate the synergistic protective effect of green tea and vitamin E during ISO induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}, {"text": "ISO", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: Although there was a discrepancy between the amount of cTnI and cTnT after DOX , probably due to heterogeneity in cross-reactivities of mAbs to various cTnI and cTnT forms , it is likely that cTnT in rats after DOX indicates cell damage determined by the magnitude of injury induced and that cTnT should be a useful marker for the prediction of experimentally induced cardiotoxicity and possibly for cardioprotective experiments .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: Neither a tumor-protective effect nor reduced toxicity to normal tissues was observed with the addition of amifostine to cisplatin in this trial .

Example answer:
{"entities": [{"text": "tumor-protective", "type": "Disease"}, {"text": "toxicity", "type": "Disease"}, {"text": "amifostine", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Among markers of ischemic injury after DOX in rats , cTnT showed the greatest ability to detect myocardial damage assessed by echocardiographic detection and histological changes .

Example answer:
{"entities": [{"text": "ischemic injury", "type": "Disease"}, {"text": "DOX", "type": "Chemical"}, {"text": "myocardial damage", "type": "Disease"}]}

Example input:
Sentence: Acetylsalicylic acid , dipyridamole , and hydrocortisone all appear to have cardioprotective effects when tested in this model .

Example answer:
{"entities": [{"text": "Acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}]}

Example input:
Sentence: Results indicate that GSPE preexposure prior to AAP , AMI and DOX , provided near complete protection in terms of serum chemistry changes ( ALT , BUN and CPK ) , and significantly reduced DNA fragmentation .

Example answer:
{"entities": [{"text": "GSPE", "type": "Chemical"}, {"text": "AAP", "type": "Chemical"}, {"text": "AMI", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}]}

Input:
Sentence: The mean protective effect by adding monoHER before DOX led to a significant 4.4-fold reduction ( P < 0.001 , 95 % CI 2.3-8.2 ) of abnormal cardiomyocytes .

## Item bc5cdr:test:1837
Example input:
Sentence: Moreover , L-NOArg and 7-NI but not L-NIL intensify antihyperalgesic activity of HOE 140 or des-Arg10HOE 140 in toxic neuropathy .

Example answer:
{"entities": [{"text": "HOE 140", "type": "Chemical"}, {"text": "des-Arg10HOE 140", "type": "Chemical"}, {"text": "toxic neuropathy", "type": "Disease"}]}

Example input:
Sentence: Our results demonstrate that both cisplatin and paclitaxel cause early mitochondrial impairment with loss of membrane potential and induction of autophagic vacuoles in neurons .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "mitochondrial impairment", "type": "Disease"}]}

Example input:
Sentence: The initiated hepatocytes in the liver were assayed as the gamma-glutamyltransferase ( gamma-GT ) positive foci formed following a 2-week selection regimen consisting of dietary 0.02 % 2-acetylaminofluorene coupled with a necrogenic dose of CCl4 .

Example answer:
{"entities": [{"text": "2-acetylaminofluorene", "type": "Chemical"}, {"text": "CCl4", "type": "Chemical"}]}

Example input:
Sentence: Cells were pretreated with maltolyl p-coumarate , before exposed to amyloid beta peptide ( 1-42 ) , glutamate or H2O2 .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "H2O2", "type": "Chemical"}]}

Example input:
Sentence: In order to elucidate the role of the catecholaminergic system in the cataleptogenic effect of delta 9-tetrahydrocannabinol ( THC ) , the effect of pretreatment with 6-hydroxydopamine ( 6-OHDA ) or with desipramine and 6-OHDA and lesions of the locus coeruleus were investigated in rats .

Example answer:
{"entities": [{"text": "delta 9-tetrahydrocannabinol", "type": "Chemical"}, {"text": "THC", "type": "Chemical"}, {"text": "6-hydroxydopamine", "type": "Chemical"}, {"text": "6-OHDA", "type": "Chemical"}, {"text": "desipramine", "type": "Chemical"}]}

Example input:
Sentence: FK 506 decreased eNOS activity and the levels of eNOS mRNA in the aorta ( 48 % and 55 % , respectively ) .

Example answer:
{"entities": [{"text": "FK 506", "type": "Chemical"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: We found that maltolyl p-coumarate significantly decreased apoptotic cell death and reduced reactive oxygen species , cytochrome c release , and caspase 3 activation .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}]}

Example input:
Sentence: Three months later the patient was exposed to a single dose of metoprolol , diltiazem , propafenone ( since he had received this drug in the past ) , and sparteine ( as a probe for the debrisoquine/sparteine type polymorphism of oxidative drug metabolism ) .

Example answer:
{"entities": [{"text": "metoprolol", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "propafenone", "type": "Chemical"}, {"text": "sparteine", "type": "Chemical"}, {"text": "debrisoquine/sparteine", "type": "Chemical"}]}

Example input:
Sentence: In vivo protection of dna damage associated apoptotic and necrotic cell deaths during acetaminophen-induced nephrotoxicity , amiodarone-induced lung toxicity and doxorubicin-induced cardiotoxicity by a novel IH636 grape seed proanthocyanidin extract .

Example answer:
{"entities": [{"text": "necrotic", "type": "Disease"}, {"text": "acetaminophen-induced", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "amiodarone-induced", "type": "Chemical"}, {"text": "lung toxicity", "type": "Disease"}, {"text": "doxorubicin-induced", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}, {"text": "IH636 grape seed proanthocyanidin extract", "type": "Chemical"}]}

Input:
Sentence: The catechol and hydroquinone metabolites , NCQ436 and NCQ344 , induced apoptosis in HL60 and HBMP cells in a time- and concentration dependent manner , while the phenols , NCR181 , FLA873 , and FLA797 , and the derivatives formed by oxidation of the pyrrolidine ring , FLA838 , NCM001 , and NCL118 , had no effect .

## Item bc5cdr:test:3049
Example input:
Sentence: All 20 patients responded to this regimen , 16/20 ( 80 % ) achieved a complete remission , and 20 % obtained a partial remission .

Example answer:
{"entities": []}

Example input:
Sentence: Nimodipine treatment resulted in a statistically significant reduction in systolic BP ( SBP ) and diastolic BP ( DBP ) from baseline compared with placebo during the first few days .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "Chemical"}, {"text": "reduction in systolic BP", "type": "Disease"}]}

Example input:
Sentence: Patients who developed hyperkalemia were older and more likely to have diabetes , had higher baseline serum potassium levels and lower baseline potassium supplement doses , and were more likely to be treated with beta-blockers than controls ( n = 134 ) .

Example answer:
{"entities": [{"text": "hyperkalemia", "type": "Disease"}, {"text": "diabetes", "type": "Disease"}, {"text": "potassium", "type": "Chemical"}]}

Example input:
Sentence: A policy of unrestricted prescription of appetite suppressants may lead to a high incidence of associated primary pulmonary hypertension .

Example answer:
{"entities": [{"text": "appetite suppressants", "type": "Chemical"}, {"text": "primary pulmonary hypertension", "type": "Disease"}]}

Example input:
Sentence: The possible interaction of tizanidine and other antihypertensive agents should be kept in mind when prescribing therapy to treat either hypertension or spasticity in such patients .

Example answer:
{"entities": [{"text": "tizanidine", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "spasticity", "type": "Disease"}]}

Example input:
Sentence: Since the introduction of angiotensin converting enzyme ( ACE ) inhibitors into the adjunctive treatment of patients with congestive heart failure , cases of severe hypotension , especially on the first day of treatment , have occasionally been reported .

Example answer:
{"entities": [{"text": "angiotensin converting enzyme ( ACE ) inhibitors", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Eighty-nine new referral hypertensive out-patients and 46 new referral non-hypertensive chronically physically ill out-patients completed a mood rating scale at regular intervals for one year .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}]}

Example input:
Sentence: Controlled hypotension in groups A and C was induced with PGE1 to maintain mean arterial blood pressure at 55 mmHg for 180 min .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "PGE1", "type": "Chemical"}]}

Example input:
Sentence: Each patient was subjected to an identical anesthetic protocol and similar drug-induced reductions in mean arterial blood pressure ( BP ) ( 50 to 55 mmHg ) .

Example answer:
{"entities": [{"text": "reductions in mean arterial blood pressure", "type": "Disease"}]}

Input:
Sentence: BACKGROUND : One third of patients treated for hypertension attain adequate blood pressure ( BP ) control , and multidrug regimens are often required .

## Item bc5cdr:test:2822
Example input:
Sentence: Treatment-related adverse events ( AEs ) occurred in 44 % and 52 % , 57 % , and 41 % of the asenapine at 5 and 10 mg BID , haloperidol , and placebo groups , respectively .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: The ACTIVE-W ( Atrial Fibrillation Clopidogrel Trial with Irbesartan for Prevention of Vascular Events ) study has demonstrated that warfarin is superior to platelet therapy ( clopidogrel plus aspirin ) in the prevention af embolic events .

Example answer:
{"entities": [{"text": "Atrial Fibrillation", "type": "Disease"}, {"text": "Clopidogrel", "type": "Chemical"}, {"text": "Irbesartan", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}, {"text": "clopidogrel", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "embolic events", "type": "Disease"}]}

Example input:
Sentence: Idraparinux , a Factor Xa inhibitor , is being evaluated in patients with atrial fibrillation .

Example answer:
{"entities": [{"text": "Idraparinux", "type": "Chemical"}, {"text": "atrial fibrillation", "type": "Disease"}]}

Example input:
Sentence: In the remaining three patients , procainamide was administered orally for treatment of chronic premature ventricular contractions or atrial flutter .

Example answer:
{"entities": [{"text": "procainamide", "type": "Chemical"}, {"text": "premature ventricular contractions", "type": "Disease"}, {"text": "atrial flutter", "type": "Disease"}]}

Example input:
Sentence: We prospectively evaluated the adverse reactions of apraclonidine in 20 normal volunteers by instilling a single drop of 1 % apraclonidine in their right eyes .

Example answer:
{"entities": [{"text": "apraclonidine", "type": "Chemical"}]}

Example input:
Sentence: Thirty days after amiodarone discontinuation , His bundle electrograms showed atrial flutter without intra-Hisian or infra-Hisian delay .

Example answer:
{"entities": [{"text": "amiodarone", "type": "Chemical"}, {"text": "atrial flutter", "type": "Disease"}]}

Example input:
Sentence: This drug caused biventricular dysfunction , due to its negative inotropic effect , and hypotension , due to its peripheral vasodilatory effect .

Example answer:
{"entities": [{"text": "biventricular dysfunction", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Serious adverse effects are uncommon and mainly have been related to the depression of cardiac contractility and conduction , especially when the drug is combined with beta-blocking agents .

Example answer:
{"entities": [{"text": "depression", "type": "Disease"}]}

Example input:
Sentence: The convulsant activity of bupivacaine was not significantly modified but calcium channel blockers decreased the time of latency to obtain bupivacaine-induced convulsions ; this effect was less pronounced with bepridil .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "bupivacaine-induced", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "bepridil", "type": "Chemical"}]}

Input:
Sentence: Clinical evaluation of adverse effects during bepridil administration for atrial fibrillation and flutter .

## Item bc5cdr:test:2739
Example input:
Sentence: We investigated this association , according to the type of progestagen included in third-generation ( i.e. , desogestrel or gestodene ) and second-generation ( i.e. , levonorgestrel ) oral contraceptives , the dose of estrogen , and the presence or absence of prothrombotic mutations METHODS : In a nationwide , population-based , case-control study , we identified and enrolled 248 women 18 through 49 years of age who had had a first myocardial infarction between 1990 and 1995 and 925 control women who had not had a myocardial infarction and who were matched for age , calendar year of the index event , and area of residence .

Example answer:
{"entities": [{"text": "progestagen", "type": "Chemical"}, {"text": "desogestrel", "type": "Chemical"}, {"text": "gestodene", "type": "Chemical"}, {"text": "levonorgestrel", "type": "Chemical"}, {"text": "oral contraceptives", "type": "Chemical"}, {"text": "estrogen", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Patients who are more than 10 years post-OLTX have CRF and ESRD at a high rate .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Raloxifene did not increase risk for cataracts ( RR 0.9 ; 95 % CI 0.8-1.1 ) , gallbladder disease ( RR 1.0 ; 95 % CI 0.7-1.3 ) , endometrial hyperplasia ( RR 1.3 ; 95 % CI 0.4-5.1 ) , or endometrial cancer ( RR 0.9 ; 95 % CI 0.3-2.7 ) .

Example answer:
{"entities": [{"text": "Raloxifene", "type": "Chemical"}, {"text": "cataracts", "type": "Disease"}, {"text": "gallbladder disease", "type": "Disease"}, {"text": "endometrial hyperplasia", "type": "Disease"}, {"text": "endometrial cancer", "type": "Disease"}]}

Example input:
Sentence: Octreotide , an effective treatment for acromegaly , induces gall bladder stones in 13-60 % of patients .

Example answer:
{"entities": [{"text": "Octreotide", "type": "Chemical"}, {"text": "acromegaly", "type": "Disease"}, {"text": "gall bladder stones", "type": "Disease"}]}

Example input:
Sentence: Our results suggest that the suppression of gallbladder contractility is the cause of the successive formation of bile sludge , gallstones , and cholecystitis during octreotide therapy in Chinese acromegalic patients .

Example answer:
{"entities": [{"text": "gallstones", "type": "Disease"}, {"text": "cholecystitis", "type": "Disease"}, {"text": "octreotide", "type": "Chemical"}, {"text": "acromegalic", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : Our results suggest that high-dose testosterone therapy may adversely affect atherosclerosis in postmenopausal women and indicate that androgen replacement in these women may not be harmless .

Example answer:
{"entities": [{"text": "testosterone", "type": "Chemical"}, {"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: High-dose testosterone is associated with atherosclerosis in postmenopausal women .

Example answer:
{"entities": [{"text": "testosterone", "type": "Chemical"}, {"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: Prospective study of the long-term effects of somatostatin analog ( octreotide ) on gallbladder function and gallstone formation in Chinese acromegalic patients .

Example answer:
{"entities": [{"text": "octreotide", "type": "Chemical"}, {"text": "gallstone", "type": "Disease"}, {"text": "acromegalic", "type": "Disease"}]}

Example input:
Sentence: METHODS : In a population-based study in 513 naturally postmenopausal women aged 54-67 years , we studied the association between self-reported intramuscularly administered high-dose estrogen-testosterone therapy ( estradiol- and testosterone esters ) and aortic atherosclerosis .

Example answer:
{"entities": [{"text": "estrogen-testosterone", "type": "Chemical"}, {"text": "estradiol- and testosterone esters", "type": "Chemical"}, {"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: It is therefore very important to follow the changes of gallbladder function during long-term octreotide therapy of acromegalic patients .

Example answer:
{"entities": [{"text": "octreotide", "type": "Chemical"}, {"text": "acromegalic", "type": "Disease"}]}

Input:
Sentence: Long-term oestrogen-only HT also significantly increased the risk of stroke and gallbladder disease .

## Item bc5cdr:test:2666
Example input:
Sentence: The reports illustrate the need for clinicians to consider acetaminophen in patients with hypotension of unknown origin .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: These studies suggest that both phenacetin and acetaminophen may contribute to the burden of ESRD , with the risk of the latter being somewhat less than that of the former .

Example answer:
{"entities": [{"text": "phenacetin", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Post hoc analyses indicated that efficacy was similar with asenapine and haloperidol ; greater contrasts were seen in AEs , especially extrapyramidal symptoms .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}, {"text": "extrapyramidal symptoms", "type": "Disease"}]}

Example input:
Sentence: A lower relative risk would be expected for acetaminophen if the risk of both drugs in combination with other analgesics was higher than the risk of either agent alone .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}]}

Example input:
Sentence: By contrast , we were unable to substantiate an increased risk from paracetamol consumption for renal papillary necrosis or any of these cancers although there was a suggestion of an association with cancer of the ureter .

Example answer:
{"entities": [{"text": "paracetamol", "type": "Chemical"}, {"text": "renal papillary necrosis", "type": "Disease"}, {"text": "cancers", "type": "Disease"}, {"text": "cancer of the ureter", "type": "Disease"}]}

Example input:
Sentence: The antinociception produced by ( +/- ) -PG-9 was prevented by the unselective muscarinic antagonist atropine , the M1-selective antagonists pirenzepine and dicyclomine and the acetylcholine depletor hemicholinium-3 , but not by the opioid antagonist naloxone , the gamma-aminobutyric acidB antagonist 3-aminopropyl-diethoxy-methyl-phosphinic acid , the H3 agonist R- ( alpha ) -methylhistamine , the D2 antagonist quinpirole , the 5-hydroxytryptamine4 antagonist 2-methoxy-4-amino-5-chlorobenzoic acid 2- ( diethylamino ) ethyl ester hydrochloride , the 5-hydroxytryptamin1A antagonist 1- ( 2-methoxyphenyl ) -4- [ 4- ( 2-phthalimido ) butyl ] piperazine hydrobromide and the polyamines depletor reserpine .

Example answer:
{"entities": [{"text": ")", "type": "Chemical"}, {"text": "gamma-aminobutyric", "type": "Chemical"}, {"text": "3-aminopropyl-diethoxy-methyl-phosphinic", "type": "Chemical"}, {"text": "R- ( alpha )", "type": "Chemical"}, {"text": "2-methoxy-4-amino-5-chlorobenzoic acid 2- ( diethylamino ) ethyl", "type": "Chemical"}, {"text": "1- ( 2-methoxyphenyl ) -4- [ 4- ( 2-phthalimido ) butyl ]", "type": "Chemical"}]}

Example input:
Sentence: Thus , acetaminophen has been used both as a single agent and in combination with other analgesics , whereas phenacetin was available only in combinations .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "phenacetin", "type": "Chemical"}]}

Example input:
Sentence: The risk of developing renal papillary necrosis or cancer of the renal pelvis , ureter or bladder associated with consumption of either phenacetin or paracetamol was calculated from data acquired by questionnaire from 381 cases and 808 controls .

Example answer:
{"entities": [{"text": "renal papillary necrosis", "type": "Disease"}, {"text": "phenacetin", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: A patient who allegedly consumed 100 tablets of an over-the-counter analgesic containing sodium acetylsalicylate , caffeine , and acetaminophen displayed no significant CNS stimulation despite the presence of 175 micrograms of caffeine per mL of serum .

Example answer:
{"entities": [{"text": "sodium acetylsalicylate", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}]}

Example input:
Sentence: Animal and clinical studies have suggested that N-methyl-D-aspartate ( NMDA ) antagonists , such as ketamine , may be effective in improving opioid analgesia in difficult pain syndromes , such as neuropathic pain .

Example answer:
{"entities": [{"text": "N-methyl-D-aspartate", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "ketamine", "type": "Chemical"}, {"text": "pain", "type": "Disease"}, {"text": "neuropathic pain", "type": "Disease"}]}

Input:
Sentence: BACKGROUND : Acetaminophen ( paracetamol -- P ) and Nimesulide ( N ) are widely used analgesic-antipyretic/anti-inflammatory drugs .

## Item bc5cdr:test:2950
Example input:
Sentence: The effect of PDTC on status epilepticus-associated cell loss in the hippocampus and piriform cortex was evaluated in the rat fractionated pilocarpine model .

Example answer:
{"entities": [{"text": "PDTC", "type": "Chemical"}, {"text": "status", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: These data might indicate that the generation of reactive oxygen species and activation of NF-kappaB plays a more central role in seizure-associated neuronal damage in the temporal cortex as compared to the hippocampal hilus .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "seizure-associated", "type": "Disease"}, {"text": "neuronal damage", "type": "Disease"}]}

Example input:
Sentence: In Mg ( 2+ ) -free bathing medium containing bicuculline , conditions designed to increase excitability in the slices , electrical stimulation of the hilus resulted in a single population spike in granule cells from control mice and pilocarpine-treated mice that did not experience SE .

Example answer:
{"entities": [{"text": "Mg", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "pilocarpine-treated", "type": "Chemical"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: The in vitro data suggest that the site responsible for the decrease in seizure activity 24 h after gamma-HCH may be the GABA-A receptor-linked chloride channel .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}, {"text": "GABA-A", "type": "Chemical"}]}

Example input:
Sentence: Prevention of seizures and reorganization of hippocampal functions by transplantation of bone marrow cells in the acute phase of experimental epilepsy .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "epilepsy", "type": "Disease"}]}

Example input:
Sentence: In vehicle-treated rats , status epilepticus caused pronounced neuronal damage in the piriform cortex comprising both pyramidal cells and interneurons .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "neuronal damage", "type": "Disease"}]}

Example input:
Sentence: These data support the hypothesis that SE-induced mossy fiber sprouting and synaptic reorganization are relevant characteristics of seizure development in these murine strains , resembling rat models of human temporal lobe epilepsy .

Example answer:
{"entities": [{"text": "SE-induced", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}]}

Example input:
Sentence: Similar to rats , systemic pilocarpine injection causes status epilepticus ( SE ) and the eventual development of spontaneous seizures and mossy fiber sprouting in C57BL/6 and CD1 mice , but the physiological correlates of these events have not been identified in mice .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: In this study , we investigated whether increased generation of FR during status epilepticus would be sufficient to provoke abnormalities in mtDNA and in the expression and activity of cytochrome c oxidase ( CCO ) , complex IV of the respiratory chain , in the chronic phase of the pilocarpine model of temporal lobe epilepsy .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}, {"text": "temporal lobe epilepsy", "type": "Disease"}]}

Example input:
Sentence: A significant decrease in neuronal density of the hippocampal hilar formation was identified in vehicle- and PDTC-treated rats following status epilepticus .

Example answer:
{"entities": [{"text": "PDTC-treated", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}]}

Input:
Sentence: It has been suggested that the ectopic hilar granule cells could contribute to the spontaneous seizures that ultimately develop after status epilepticus .

## Item bc5cdr:test:2948
Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: In Mg ( 2+ ) -free bathing medium containing bicuculline , conditions designed to increase excitability in the slices , electrical stimulation of the hilus resulted in a single population spike in granule cells from control mice and pilocarpine-treated mice that did not experience SE .

Example answer:
{"entities": [{"text": "Mg", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "pilocarpine-treated", "type": "Chemical"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Three hundred fifty-five adult male CSS mice , 58 B6 , and 39 A/J were tested for susceptibility to pilocarpine-induced seizures .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: A comparable overexpression of Pgp in the BBB was obtained after pilocarpine-induced seizures in wild-type Wistar rats .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: The effect of PDTC on status epilepticus-associated cell loss in the hippocampus and piriform cortex was evaluated in the rat fractionated pilocarpine model .

Example answer:
{"entities": [{"text": "PDTC", "type": "Chemical"}, {"text": "status", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: In vehicle-treated rats , status epilepticus caused pronounced neuronal damage in the piriform cortex comprising both pyramidal cells and interneurons .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "neuronal damage", "type": "Disease"}]}

Example input:
Sentence: Population responses in granule cells of the dentate gyrus were examined in transverse slices of the ventral hippocampus from pilocarpine-treated and untreated mice .

Example answer:
{"entities": [{"text": "pilocarpine-treated", "type": "Chemical"}]}

Example input:
Sentence: Similar to rats , systemic pilocarpine injection causes status epilepticus ( SE ) and the eventual development of spontaneous seizures and mossy fiber sprouting in C57BL/6 and CD1 mice , but the physiological correlates of these events have not been identified in mice .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: A significant decrease in neuronal density of the hippocampal hilar formation was identified in vehicle- and PDTC-treated rats following status epilepticus .

Example answer:
{"entities": [{"text": "PDTC-treated", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}]}

Input:
Sentence: Stereological methods reveal the robust size and stability of ectopic hilar granule cells after pilocarpine-induced status epilepticus in the adult rat .

## Item bc5cdr:test:3250
Example input:
Sentence: Fentanyl did reduce minor intraoperative movement but had no sevoflurane-sparing effect and increased respiratory depression , hypotension and bradycardia .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "Chemical"}, {"text": "sevoflurane-sparing", "type": "Chemical"}, {"text": "respiratory depression", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Recent evidence suggests that transient neurologic symptoms ( TNSs ) frequently follow lidocaine spinal anesthesia but are infrequent with bupivacaine .

Example answer:
{"entities": [{"text": "transient neurologic symptoms", "type": "Disease"}, {"text": "TNSs", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : The utilization of phenylephrine to correct hypotension induced by anesthesia has a negative impact on S ( c ) O ( 2 ) while ephedrine maintains frontal lobe oxygenation potentially related to an increase in CO .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: To evaluate the effect of prostaglandin E1 ( PGE1 ) or trimethaphan ( TMP ) induced hypotension on epidural blood flow ( EBF ) during spinal surgery , EBF was measured using the heat clearance method in 30 patients who underwent postero-lateral interbody fusion under isoflurane anaesthesia .

Example answer:
{"entities": [{"text": "prostaglandin E1", "type": "Chemical"}, {"text": "PGE1", "type": "Chemical"}, {"text": "trimethaphan", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "isoflurane", "type": "Chemical"}]}

Example input:
Sentence: These results suggest that PGE1 may be preferable to TMP for hypotensive anaesthesia in spinal surgery because TMP decreased EBF .

Example answer:
{"entities": [{"text": "PGE1", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}, {"text": "hypotensive", "type": "Disease"}]}

Example input:
Sentence: METHODS : Ninety patients classified as American Society of Anesthesiologists physical status I or II who were scheduled for short gynecologic procedures under spinal anesthesia were randomly allocated to receive 2.5 ml 2 % lidocaine in 7.5 % glucose , 2 % prilocaine in 7.5 % glucose , or 0.5 % bupivacaine in 7.5 % glucose .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "glucose", "type": "Chemical"}, {"text": "prilocaine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: Transient neurologic symptoms after spinal anesthesia : a lower incidence with prilocaine and bupivacaine than with lidocaine .

Example answer:
{"entities": [{"text": "Transient neurologic symptoms", "type": "Disease"}, {"text": "prilocaine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: A transient neurological deficit following intrathecal injection of 1 % hyperbaric bupivacaine for unilateral spinal anaesthesia .

Example answer:
{"entities": [{"text": "neurological deficit", "type": "Disease"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: However , we suggest that a low solution concentration should be preferred for unilateral spinal anaesthesia with a hyperbaric anaesthetic solution ( if pencil-point needle and slow injection rate are employed ) , in order to minimize the risk of a localized high peak anaesthetic concentration , which might lead to a transient neurological deficit .

Example answer:
{"entities": [{"text": "neurological deficit", "type": "Disease"}]}

Example input:
Sentence: We describe a case of transient neurological deficit that occurred after unilateral spinal anaesthesia with 8 mg of 1 % hyperbaric bupivacaine slowly injected through a 25-gauge pencil-point spinal needle .

Example answer:
{"entities": [{"text": "neurological deficit", "type": "Disease"}, {"text": "bupivacaine", "type": "Chemical"}]}

Input:
Sentence: Efforts must therefore continue to be made to obviate this setback OBJECTIVE : To evaluate the cardiovascular and respiratory changes during unilateral and conventional spinal anaesthesia .

## Item bc5cdr:test:3252
Example input:
Sentence: The spinal cords of the animals that received bupivacaine , low pH normal saline ( pH 3.0 ) , or normal saline did not show abnormal findings .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: Ten rats had arterial , central venous ( CVP ) , and subdural cannulae inserted under halothane anesthesia .

Example answer:
{"entities": [{"text": "halothane", "type": "Chemical"}]}

Example input:
Sentence: Transient neurologic symptoms after spinal anesthesia : a lower incidence with prilocaine and bupivacaine than with lidocaine .

Example answer:
{"entities": [{"text": "Transient neurologic symptoms", "type": "Disease"}, {"text": "prilocaine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: METHODS : A double-blind double-armed prospective study comprised 40 patients who had uneventful sutureless phacoemulsification under sub-Tenon 's local infiltration of 3 mL of plain lignocaine .

Example answer:
{"entities": [{"text": "lignocaine", "type": "Chemical"}]}

Example input:
Sentence: A transient neurological deficit following intrathecal injection of 1 % hyperbaric bupivacaine for unilateral spinal anaesthesia .

Example answer:
{"entities": [{"text": "neurological deficit", "type": "Disease"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: These results suggest that PGE1 may be preferable to TMP for hypotensive anaesthesia in spinal surgery because TMP decreased EBF .

Example answer:
{"entities": [{"text": "PGE1", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}, {"text": "hypotensive", "type": "Disease"}]}

Example input:
Sentence: However , we suggest that a low solution concentration should be preferred for unilateral spinal anaesthesia with a hyperbaric anaesthetic solution ( if pencil-point needle and slow injection rate are employed ) , in order to minimize the risk of a localized high peak anaesthetic concentration , which might lead to a transient neurological deficit .

Example answer:
{"entities": [{"text": "neurological deficit", "type": "Disease"}]}

Example input:
Sentence: We describe a case of transient neurological deficit that occurred after unilateral spinal anaesthesia with 8 mg of 1 % hyperbaric bupivacaine slowly injected through a 25-gauge pencil-point spinal needle .

Example answer:
{"entities": [{"text": "neurological deficit", "type": "Disease"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: The patients were randomly allocated to one of three groups ; those in group A ( n = 10 ) were subjected to controlled hypotension alone , those in group B ( n = 10 ) to haemodilution alone and those in group C ( n = 10 ) to both controlled hypotension and haemodilution .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}]}

Example input:
Sentence: METHODS : Ninety patients classified as American Society of Anesthesiologists physical status I or II who were scheduled for short gynecologic procedures under spinal anesthesia were randomly allocated to receive 2.5 ml 2 % lidocaine in 7.5 % glucose , 2 % prilocaine in 7.5 % glucose , or 0.5 % bupivacaine in 7.5 % glucose .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "glucose", "type": "Chemical"}, {"text": "prilocaine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Input:
Sentence: Patients were randomly allocated into one of two groups : lateral and conventional spinal anaesthesia groups .

## Item bc5cdr:test:2857
Example input:
Sentence: Hypertension was observed in animals that had a reduction in glomeruli as well as in a group that did not have a reduction in glomerular number , suggesting that a reduction in glomerular number is not the sole cause for the development of hypertension .

Example answer:
{"entities": [{"text": "Hypertension", "type": "Disease"}, {"text": "reduction in glomerular number", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: Atorvastatin ( Ato ) possesses pleiotropic properties that have been reported to improve endothelial function through increased availability of NO and reduced O2- production in various forms of hypertension .

Example answer:
{"entities": [{"text": "Atorvastatin", "type": "Chemical"}, {"text": "Ato", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}, {"text": "O2-", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: To clarify the mechanisms of FK 506-induced hypertension , we studied the chronic effects of FK 506 on the synthesis of endothelin-1 ( ET-1 ) , the expression of mRNA of ET-1 and endothelin-converting enzyme-1 ( ECE-1 ) , the endothelial nitric oxide synthase ( eNOS ) activity , and the expression of mRNA of eNOS and C-type natriuretic peptide ( CNP ) in rat blood vessels .

Example answer:
{"entities": [{"text": "FK", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "FK 506", "type": "Chemical"}, {"text": "nitric oxide", "type": "Chemical"}]}

Example input:
Sentence: Glucocorticoid-induced hypertension ( GC-HT ) in the rat is associated with nitric oxide-redox imbalance .

Example answer:
{"entities": [{"text": "hypertension", "type": "Disease"}, {"text": "nitric", "type": "Chemical"}]}

Example input:
Sentence: To assess the molecular basis of disturbances in transmembraneous transport of Na+ , we studied the response of cardiac ( Na , K ) -ATPase to NO-deficient hypertension induced in rats by NO-synthase inhibition with 40 mg/kg/day N ( G ) -nitro-L-arginine methyl ester ( L-NAME ) for 4 four weeks .

Example answer:
{"entities": [{"text": "Na+", "type": "Chemical"}, {"text": "Na", "type": "Chemical"}, {"text": "K", "type": "Chemical"}, {"text": "NO-deficient", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "NO-synthase", "type": "Chemical"}, {"text": "N ( G ) -nitro-L-arginine methyl ester", "type": "Chemical"}, {"text": "L-NAME", "type": "Chemical"}]}

Example input:
Sentence: Inhibition of NO-synthase induced a reversible hypertension accompanied by depressed Na+-extrusion from cardiac cells as a consequence of deteriorated Na+-binding properties of the ( Na , K ) -ATPase .

Example answer:
{"entities": [{"text": "NO-synthase", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "depressed", "type": "Disease"}, {"text": "Na+-extrusion", "type": "Chemical"}, {"text": "Na+-binding", "type": "Chemical"}, {"text": "Na", "type": "Chemical"}, {"text": "K", "type": "Chemical"}]}

Example input:
Sentence: Changes of sodium and ATP affinities of the cardiac ( Na , K ) -ATPase during and after nitric oxide deficient hypertension .

Example answer:
{"entities": [{"text": "sodium", "type": "Chemical"}, {"text": "ATP", "type": "Chemical"}, {"text": "Na", "type": "Chemical"}, {"text": "K", "type": "Chemical"}, {"text": "nitric oxide", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: Inhibition of NO synthesis induces sustained hypertension .

Example answer:
{"entities": [{"text": "NO", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: A deficient L-arginine-nitric oxide system is implicated in cortisol-induced hypertension .

Example answer:
{"entities": [{"text": "L-arginine-nitric oxide", "type": "Chemical"}, {"text": "cortisol-induced", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: Dexamethasone ( Dex ) -induced hypertension is characterized by endothelial dysfunction associated with nitric oxide ( NO ) deficiency and increased superoxide ( O2- ) production .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "Chemical"}, {"text": "Dex", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "nitric oxide", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}, {"text": "superoxide", "type": "Chemical"}, {"text": "O2-", "type": "Chemical"}]}

Input:
Sentence: Mechanisms of hypertension induced by nitric oxide ( NO ) deficiency : focus on venous function .

## Item bc5cdr:test:3259
Example input:
Sentence: Respiratory insufficiency was further worsened by Proteus mirabilis infection and severe bronchoconstriction .

Example answer:
{"entities": [{"text": "Respiratory insufficiency", "type": "Disease"}, {"text": "Proteus mirabilis infection", "type": "Disease"}]}

Example input:
Sentence: The patients were randomly allocated to one of three groups ; those in group A ( n = 10 ) were subjected to controlled hypotension alone , those in group B ( n = 10 ) to haemodilution alone and those in group C ( n = 10 ) to both controlled hypotension and haemodilution .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}]}

Example input:
Sentence: Two groups of supine subjects were studied under placebo-controlled conditions , one during the night , when sleeping ( n = 7 ) and the other at daytime , when awake ( n = 6 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Mean peak forced expiratory volume in 1 second ( FEV1 ) increases over baseline and the proportion of patients attaining at least a 15 % increase in the FEV1 ( responders ) were 31 % and 90 % , respectively , for ipratropium and 17 % and 50 % , respectively , for theophylline .

Example answer:
{"entities": [{"text": "ipratropium", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}]}

Example input:
Sentence: The lung weights were lower and PaO2 was improved in rats given this enzyme-blocking agent .

Example answer:
{"entities": []}

Example input:
Sentence: A respiratory arrest with severe desaturation and bradycardia occurred .

Example answer:
{"entities": [{"text": "respiratory arrest", "type": "Disease"}, {"text": "desaturation", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: When respiratory failure was produced by hypoventilation ( pH 7.05 to 7.25 ; PC02 70 to 100 mm Hg : P02 20 to 40 mm Hg ) , infusion of aminophylline resulted in an even greater decrease in ventricular fibrillation threshold to 60 percent of the control level .

Example answer:
{"entities": [{"text": "respiratory failure", "type": "Disease"}, {"text": "hypoventilation", "type": "Disease"}, {"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}]}

Example input:
Sentence: The systemic , central venous , pulmonary capillary wedge pressures , and heart rates , were similar in the two groups .

Example answer:
{"entities": []}

Example input:
Sentence: The animals were mechanically ventilated to achieve normocarbia ( PCO2 = 42 +/- 1 mmHg , mean +/- SE ) .

Example answer:
{"entities": []}

Example input:
Sentence: Mild hypoxia ( SO2 < 90 % ) was the most common event ( 11 patients ) ; 3 patients ( 2 % ) presented transient hypoxia due to upper airway obstruction by probe introduction and 8 ( 5.8 % ) due to hypoxia caused by MZ use .

Example answer:
{"entities": [{"text": "hypoxia", "type": "Disease"}, {"text": "airway obstruction", "type": "Disease"}, {"text": "MZ", "type": "Chemical"}]}

Input:
Sentence: The mean respiratory rate and oxygen saturations in the two groups were similar .

## Item bc5cdr:test:3034
Example input:
Sentence: Controlled hypotension in groups A and C was induced with PGE1 to maintain mean arterial blood pressure at 55 mmHg for 180 min .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "PGE1", "type": "Chemical"}]}

Example input:
Sentence: Mean arterial pressure was decreased to 50 mm Hg for 30 minutes either by hemorrhage ( HEM , n = 7 ) or by continuous infusion of sodium nitroprusside ( SNP , n = 7 ) .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "Disease"}, {"text": "HEM", "type": "Disease"}, {"text": "sodium nitroprusside", "type": "Chemical"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: Epinephrine has a proven role in cardiac arrest in prehospital care ; however , use by paramedics in patients with suspected allergic reaction and severe hypertension should be viewed with caution .

Example answer:
{"entities": [{"text": "Epinephrine", "type": "Chemical"}, {"text": "cardiac arrest", "type": "Disease"}, {"text": "allergic reaction", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: The role of the renin -- angiotensin system in the maintenance of blood pressure during halothane anesthesia and sodium nitroprusside ( SNP ) -induced hypotension was evaluated .

Example answer:
{"entities": [{"text": "angiotensin", "type": "Chemical"}, {"text": "halothane", "type": "Chemical"}, {"text": "sodium nitroprusside", "type": "Chemical"}, {"text": "SNP", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Isoproterenol pretreatment for 15 days caused cardiac hypertrophy without affecting baseline blood pressure and heart rate .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "Chemical"}, {"text": "cardiac hypertrophy", "type": "Disease"}]}

Example input:
Sentence: Under such conditions , angiotensin II receptor blockade by losartan probably induced a critical fall in glomerular filtration pressure .

Example answer:
{"entities": [{"text": "angiotensin II", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: After starting PGE1 or TMP , MAP and rate pressure product ( RPP ) decreased significantly compared with preinfusion values ( P < 0.01 ) , and the degree of hypotension due to PGE1 remained constant until 60 min after its discontinuation .

Example answer:
{"entities": [{"text": "PGE1", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: In each group , SNP infusion resulted in an initial decrease in blood pressure from 86 torr and 83 torr , respectively , to 48 torr .

Example answer:
{"entities": [{"text": "SNP", "type": "Chemical"}]}

Input:
Sentence: A dramatic drop in blood pressure following prehospital GTN administration .

## Item bc5cdr:test:2957
Example input:
Sentence: Similar to rats , systemic pilocarpine injection causes status epilepticus ( SE ) and the eventual development of spontaneous seizures and mossy fiber sprouting in C57BL/6 and CD1 mice , but the physiological correlates of these events have not been identified in mice .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: A significant decrease in neuronal density of the hippocampal hilar formation was identified in vehicle- and PDTC-treated rats following status epilepticus .

Example answer:
{"entities": [{"text": "PDTC-treated", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}]}

Example input:
Sentence: We report QTLs identified using a B6 ( host ) x A/J ( donor ) CSS panel to localize genes involved in susceptibility to pilocarpine-induced seizures .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: In this study , we investigated whether increased generation of FR during status epilepticus would be sufficient to provoke abnormalities in mtDNA and in the expression and activity of cytochrome c oxidase ( CCO ) , complex IV of the respiratory chain , in the chronic phase of the pilocarpine model of temporal lobe epilepsy .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}, {"text": "temporal lobe epilepsy", "type": "Disease"}]}

Example input:
Sentence: The effect of PDTC on status epilepticus-associated cell loss in the hippocampus and piriform cortex was evaluated in the rat fractionated pilocarpine model .

Example answer:
{"entities": [{"text": "PDTC", "type": "Chemical"}, {"text": "status", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: Investigation of mitochondrial involvement in the experimental model of epilepsy induced by pilocarpine .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: In Mg ( 2+ ) -free bathing medium containing bicuculline , conditions designed to increase excitability in the slices , electrical stimulation of the hilus resulted in a single population spike in granule cells from control mice and pilocarpine-treated mice that did not experience SE .

Example answer:
{"entities": [{"text": "Mg", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "pilocarpine-treated", "type": "Chemical"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: QTLs for susceptibility to pilocarpine-induced seizures , a model of temporal lobe epilepsy , have not been reported , and CSS have not previously been used to localize seizure susceptibility genes .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: Population responses in granule cells of the dentate gyrus were examined in transverse slices of the ventral hippocampus from pilocarpine-treated and untreated mice .

Example answer:
{"entities": [{"text": "pilocarpine-treated", "type": "Chemical"}]}

Input:
Sentence: The results provide new insight into the potential role of ectopic hilar granule cells in the pilocarpine model of temporal lobe epilepsy .
