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

## Item bc5cdr:test:3554
Example input:
Sentence: When injected into the accumbens shell ( but not the core ) before cocaine , CP 93129 ( 0.1-10 microg/side ) enhanced the locomotor response to cocaine ; the maximum effect being observed after 10 microg/side of the agonist .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: The half-life ( t1/2 ) of cocaine is relatively short , but some of the consequences of its use , such as seizures and strokes , can occur hours after exposure .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "strokes", "type": "Disease"}]}

Example input:
Sentence: In individuals with preexisting , high-grade coronary arterial narrowing , acute myocardial infarction may result from an increase in myocardial oxygen demand associated with cocaine-induced increase in rate-pressure product .

Example answer:
{"entities": [{"text": "acute myocardial infarction", "type": "Disease"}, {"text": "oxygen", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVES : Given its preclinical success for treating substance abuse and the increased risk of visual field defects ( VFD ) associated with cumulative lifetime exposure , we explored the effects of sub-chronic low dose GVG on cocaine-induced increases in nucleus accumbens ( NAcc ) dopamine ( DA ) .

Example answer:
{"entities": [{"text": "substance abuse", "type": "Disease"}, {"text": "visual field defects", "type": "Disease"}, {"text": "VFD", "type": "Disease"}, {"text": "GVG", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Progressive abstinence from cocaine was associated with worsening of all measured polysomnographic sleep outcomes .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Using as the reference group women who were not using oral contraception , had no recent pregnancy or menopausal symptoms , the case-control analysis gave an adjusted odds ratio ( OR ( adj ) ) of 7.44 ( 95 % CI 3.67-15.08 ) for CPA/EE use compared with an OR ( adj ) of 2.58 ( 95 % CI 1.60-4.18 ) for use of conventional COCs .

Example answer:
{"entities": [{"text": "CPA/EE", "type": "Chemical"}]}

Example input:
Sentence: The adjusted odds ratio was 2.5 ( 95 percent confidence interval , 1.5 to 4.1 ) among women who used second-generation oral contraceptives and 1.3 ( 95 percent confidence interval , 0.7 to 2.5 ) among those who used third-generation oral contraceptives .

Example answer:
{"entities": [{"text": "oral contraceptives", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Sub-chronic GVG exposure inhibited the effect of cocaine for 3 days , which exceeded in magnitude and duration the identical acute dose .

Example answer:
{"entities": [{"text": "GVG", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Among women who used oral contraceptives , the odds ratio was 2.1 ( 95 percent confidence interval , 1.5 to 3.0 ) for those without a prothrombotic mutation and 1.9 ( 95 percent confidence interval , 0.6 to 5.5 ) for those with a mutation CONCLUSIONS : The risk of myocardial infarction was increased among women who used second-generation oral contraceptives .

Example answer:
{"entities": [{"text": "oral contraceptives", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Input:
Sentence: After adjusting for potential confounders , we found that the risk of HIV seroconversion among participants who were daily smokers of crack cocaine increased over time ( period 1 : hazard ratio [ HR ] 1.03 , 95 % confidence interval [ CI ] 0.57-1.85 ; period 2 : HR 1.68 , 95 % CI 1.01-2.80 ; and period 3 : HR 2.74 , 95 % CI 1.06-7.11 ) .

## Item bc5cdr:test:3608
Example input:
Sentence: Hypertensive patients with psychiatric histories had a higher prevalence of depression than the comparison patients .

Example answer:
{"entities": [{"text": "Hypertensive", "type": "Disease"}, {"text": "psychiatric", "type": "Disease"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: Thyroid disorders , illicit drug or stimulant use , and acute alcohol intoxication are among these causes .

Example answer:
{"entities": [{"text": "Thyroid disorders", "type": "Disease"}, {"text": "acute alcohol intoxication", "type": "Disease"}]}

Example input:
Sentence: The association remained after additional adjustment for diabetes , cholesterol level , systolic blood pressure , or alcohol use .

Example answer:
{"entities": [{"text": "diabetes", "type": "Disease"}, {"text": "cholesterol", "type": "Chemical"}, {"text": "alcohol", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : The septo-hippocampal cholinergic pathway has been implicated in epileptogenesis , and genetic factors influence the response to cholinergic agents , but limited data are available on cholinergic involvement in alcohol withdrawal severity .

Example answer:
{"entities": [{"text": "alcohol", "type": "Chemical"}]}

Example input:
Sentence: In less than 1 hour after the ingestion of alcohol , he developed malaise with flushing of the face , tachycardia , and dyspnea .

Example answer:
{"entities": [{"text": "alcohol", "type": "Chemical"}, {"text": "flushing of the face", "type": "Disease"}, {"text": "tachycardia", "type": "Disease"}, {"text": "dyspnea", "type": "Disease"}]}

Example input:
Sentence: The results showed a high prevalence of depression in both groups of patients , with no preponderance in the hypertensive group .

Example answer:
{"entities": [{"text": "depression", "type": "Disease"}, {"text": "hypertensive", "type": "Disease"}]}

Example input:
Sentence: During the six-month follow up , depression was quantified through the Beck and Zung-Conde scales every two months .

Example answer:
{"entities": [{"text": "depression", "type": "Disease"}]}

Example input:
Sentence: This was accounted for by a significant number of depressions occurring in methyl dopa treated patients with psychiatric histories .

Example answer:
{"entities": [{"text": "depressions", "type": "Disease"}, {"text": "methyl dopa", "type": "Chemical"}, {"text": "psychiatric", "type": "Disease"}]}

Example input:
Sentence: Current estimates suggest that between 0.4 % and 8.3 % of children and adolescents are affected by major depression .

Example answer:
{"entities": [{"text": "major depression", "type": "Disease"}]}

Example input:
Sentence: Depressed mood was more common among patients and was associated with certain sexual difficulties , but not with impotence .

Example answer:
{"entities": [{"text": "Depressed mood", "type": "Disease"}, {"text": "impotence", "type": "Disease"}]}

Input:
Sentence: The association between alcohol consumption and depression was significant ( p < 0.001 ) .

## Item bc5cdr:test:3722
Example input:
Sentence: RESULTS : The main pathologic diagnoses ( some overlap ) were acute rejection ( AR ; n = 4 ) , chronic rejection ( CR ; n=5 ) , AR+CR ( n =4 ) , recurrent IgA nephropathy ( n =5 ) , normal findings ( n =2 ) , minimal-type chronic FK506 nephropathy ( n = 9 ) , and mild-type FK506 nephropathy ( n = 11 ) .

Example answer:
{"entities": [{"text": "IgA nephropathy", "type": "Disease"}, {"text": "FK506", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: The pooled statistical analysis for ventricular septal ( VSD ) and midline ( MD ) defects was performed for rat fetuses exposed to piroxicam , selective and non-selective COX-2 inhibitor based on present and historic data .

Example answer:
{"entities": [{"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: Carbamazepine ( CBZ ) , a commonly used AED , has been implicated in some clinical studies .

Example answer:
{"entities": [{"text": "Carbamazepine", "type": "Chemical"}, {"text": "CBZ", "type": "Chemical"}]}

Example input:
Sentence: From January 1986 to January 2009 , 1223 consecutive ALF patients were evaluated : ATT alone was the cause in 70 ( 5.7 % ) patients .

Example answer:
{"entities": [{"text": "ALF", "type": "Disease"}]}

Example input:
Sentence: METHOD : In a 16-week multicenter , double-blind trial , 122 children with ADHD were randomly assigned to clonidine ( n = 31 ) , methylphenidate ( n = 29 ) , clonidine and methylphenidate ( n = 32 ) , or placebo ( n = 30 ) .

Example answer:
{"entities": [{"text": "ADHD", "type": "Disease"}, {"text": "clonidine", "type": "Chemical"}, {"text": "methylphenidate", "type": "Chemical"}]}

Example input:
Sentence: The occurrence of this ADR was more frequent in patients aged between 61 and 80 years .

Example answer:
{"entities": []}

Example input:
Sentence: Patients with stage D2-3 disease , abnormal hemoglobin level or renal and liver function tests that were higher than the upper limits were excluded from the study .

Example answer:
{"entities": []}

Example input:
Sentence: Among the 5 patients with white matter abnormalities , 4 patients ( 80.0 % ) showed higher than normal ADC values on initial MR images , and all showed complete resolution on follow-up images .

Example answer:
{"entities": [{"text": "white matter abnormalities", "type": "Disease"}]}

Example input:
Sentence: The remaining 1 patient ( 20.0 % ) showed lower than normal ADC value and showed incomplete resolution with cortical laminar necrosis .

Example answer:
{"entities": [{"text": "cortical laminar necrosis", "type": "Disease"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Disease"}]}

Input:
Sentence: Patients with ADSD were identified .

## Item bc5cdr:test:3268
Example input:
Sentence: Peripheral neuropathy due to nutritional deficiency of thiamine and riboflavin was common ( 10.1 % ) and presented mainly as sensory and sensori-motor neuropathy .

Example answer:
{"entities": [{"text": "Peripheral neuropathy", "type": "Disease"}, {"text": "nutritional deficiency", "type": "Disease"}, {"text": "thiamine", "type": "Chemical"}, {"text": "riboflavin", "type": "Chemical"}, {"text": "sensori-motor neuropathy", "type": "Disease"}]}

Example input:
Sentence: In the remaining cases , a combination of myelopathy , visual disturbance , and peripheral neuropathy was the most common manifestation .

Example answer:
{"entities": [{"text": "myelopathy", "type": "Disease"}, {"text": "visual disturbance", "type": "Disease"}, {"text": "peripheral neuropathy", "type": "Disease"}]}

Example input:
Sentence: Monkeys with acute ( short-term ) MPTP exposure , rapid symptom onset and short symptom duration prior to initiation of levodopa therapy developed dyskinesia between 11 and 24 days of daily levodopa administration .

Example answer:
{"entities": [{"text": "MPTP", "type": "Chemical"}, {"text": "levodopa", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: In contrast , monkeys with long-term MPTP exposure , slow symptom progression and/or long symptom duration prior to initiation of levodopa therapy were more resistant to developing LIDs ( e.g. , dyskinesia developed no sooner than 146 days of chronic levodopa administration ) .

Example answer:
{"entities": [{"text": "MPTP", "type": "Chemical"}, {"text": "levodopa", "type": "Chemical"}, {"text": "LIDs", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: These data indicate that a critical percentage of NTE inhibition in brain and spinal cord sampled shortly after Mipafox exposure can predict neuropathic damage in rats several weeks later .

Example answer:
{"entities": [{"text": "Mipafox", "type": "Chemical"}, {"text": "neuropathic damage", "type": "Disease"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: This pilot trial aimed to evaluate the role of glutamate supplementation for preventing PAC-induced peripheral neuropathy in a randomized , placebo-controlled , double-blinded clinical and electro-diagnostic study .

Example answer:
{"entities": [{"text": "glutamate", "type": "Chemical"}, {"text": "PAC-induced", "type": "Chemical"}, {"text": "peripheral neuropathy", "type": "Disease"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Peripheral neuropathy has been noted as a complication of therapy with perhexiline maleate , a drug widely used in France ( and in clinical trials in the United States ) for the prophylactic treatment of angina pectoris .

Example answer:
{"entities": [{"text": "Peripheral neuropathy", "type": "Disease"}, {"text": "perhexiline maleate", "type": "Chemical"}, {"text": "angina pectoris", "type": "Disease"}]}

Example input:
Sentence: Peripheral neuropathy occurred in 12 patients and pancreatitis in six .

Example answer:
{"entities": [{"text": "Peripheral neuropathy", "type": "Disease"}, {"text": "pancreatitis", "type": "Disease"}]}

Input:
Sentence: Among the patients with 1 year of follow-up , NVP therapy was significantly associated with developing rash and d4T therapy with developing peripheral neuropathy ( p < 0.05 ) .

## Item bc5cdr:test:3460
Example input:
Sentence: We describe a patient who developed dilated cardiomyopathy and clinical congestive heart failure after 2 months of therapy with amphotericin B ( AmB ) for disseminated coccidioidomycosis .

Example answer:
{"entities": [{"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}, {"text": "AmB", "type": "Chemical"}, {"text": "coccidioidomycosis", "type": "Disease"}]}

Example input:
Sentence: Thirty days after amiodarone discontinuation , His bundle electrograms showed atrial flutter without intra-Hisian or infra-Hisian delay .

Example answer:
{"entities": [{"text": "amiodarone", "type": "Chemical"}, {"text": "atrial flutter", "type": "Disease"}]}

Example input:
Sentence: Five of 8 patients ( 63 % ) improved during fusidic acid treatment : 3 at two weeks and 2 after four weeks .

Example answer:
{"entities": [{"text": "fusidic acid", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Since the introduction of angiotensin converting enzyme ( ACE ) inhibitors into the adjunctive treatment of patients with congestive heart failure , cases of severe hypotension , especially on the first day of treatment , have occasionally been reported .

Example answer:
{"entities": [{"text": "angiotensin converting enzyme ( ACE ) inhibitors", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: When deferoxamine therapy was discontinued and serial studies were performed , audiograms in seven cases reverted to normal or near normal within two to three weeks , and nine of 13 patients with symptoms became asymptomatic .

Example answer:
{"entities": [{"text": "deferoxamine", "type": "Chemical"}]}

Example input:
Sentence: This complication reappeared on day 25 during the second dose of 5-fluorouracil and folinic acid , which were then the only drugs given .

Example answer:
{"entities": [{"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: Idraparinux , a Factor Xa inhibitor , is being evaluated in patients with atrial fibrillation .

Example answer:
{"entities": [{"text": "Idraparinux", "type": "Chemical"}, {"text": "atrial fibrillation", "type": "Disease"}]}

Example input:
Sentence: In the remaining three patients , procainamide was administered orally for treatment of chronic premature ventricular contractions or atrial flutter .

Example answer:
{"entities": [{"text": "procainamide", "type": "Chemical"}, {"text": "premature ventricular contractions", "type": "Disease"}, {"text": "atrial flutter", "type": "Disease"}]}

Example input:
Sentence: Angiotensin-converting enzyme inhibitors and angiotensin II receptor-blocking drugs hold promise in atrial fibrillation through cardiac remodelling .

Example answer:
{"entities": [{"text": "Angiotensin-converting", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "cardiac remodelling", "type": "Disease"}]}

Input:
Sentence: Flecainide had been started 2 weeks prior for atrial fibrillation .

## Item bc5cdr:test:3614
Example input:
Sentence: Inflammatory cells are postulated to mediate some of the brain damage following ischemic stroke .

Example answer:
{"entities": [{"text": "brain damage", "type": "Disease"}, {"text": "ischemic stroke", "type": "Disease"}]}

Example input:
Sentence: A significant decrease in neuronal density of the hippocampal hilar formation was identified in vehicle- and PDTC-treated rats following status epilepticus .

Example answer:
{"entities": [{"text": "PDTC-treated", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}]}

Example input:
Sentence: In this study , we investigated whether increased generation of FR during status epilepticus would be sufficient to provoke abnormalities in mtDNA and in the expression and activity of cytochrome c oxidase ( CCO ) , complex IV of the respiratory chain , in the chronic phase of the pilocarpine model of temporal lobe epilepsy .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}, {"text": "temporal lobe epilepsy", "type": "Disease"}]}

Example input:
Sentence: These findings suggest that overgrowth of the exencephalic neural tissue causes the altered distribution patterns of vessels , subsequent peripheral circulatory failure and/or hemorrhaging in various parts of the exencephalic head , leading to the multiple modes of tissue reduction during transformation from exencephaly to anencephaly .

Example answer:
{"entities": [{"text": "exencephalic", "type": "Disease"}, {"text": "circulatory failure", "type": "Disease"}, {"text": "hemorrhaging", "type": "Disease"}, {"text": "exencephaly", "type": "Disease"}, {"text": "anencephaly", "type": "Disease"}]}

Example input:
Sentence: Our findings indicate that beta2-adrenoceptor overstimulation during an early critical period results in microglial activation associated with innate neuroinflammatory pathways and behavioral abnormalities , similar to those described in autism .

Example answer:
{"entities": [{"text": "behavioral abnormalities", "type": "Disease"}, {"text": "autism", "type": "Disease"}]}

Example input:
Sentence: Prevention of seizures and reorganization of hippocampal functions by transplantation of bone marrow cells in the acute phase of experimental epilepsy .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "epilepsy", "type": "Disease"}]}

Example input:
Sentence: Similar to rats , systemic pilocarpine injection causes status epilepticus ( SE ) and the eventual development of spontaneous seizures and mossy fiber sprouting in C57BL/6 and CD1 mice , but the physiological correlates of these events have not been identified in mice .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Mitochondrial abnormalities have been associated with several aspects of epileptogenesis , such as energy generation , control of cell death , neurotransmitter synthesis , and free radical ( FR ) production .

Example answer:
{"entities": [{"text": "Mitochondrial abnormalities", "type": "Disease"}, {"text": "death", "type": "Disease"}]}

Example input:
Sentence: These data support the hypothesis that SE-induced mossy fiber sprouting and synaptic reorganization are relevant characteristics of seizure development in these murine strains , resembling rat models of human temporal lobe epilepsy .

Example answer:
{"entities": [{"text": "SE-induced", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}]}

Example input:
Sentence: These data might indicate that the generation of reactive oxygen species and activation of NF-kappaB plays a more central role in seizure-associated neuronal damage in the temporal cortex as compared to the hippocampal hilus .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "seizure-associated", "type": "Disease"}, {"text": "neuronal damage", "type": "Disease"}]}

Input:
Sentence: BACKGROUND : Neuroinflammation occurs after seizures and is implicated in epileptogenesis .

## Item bc5cdr:test:3856
Example input:
Sentence: Rats treated with L-DOPA were allocated to two groups based on the presence or absence of LID .

Example answer:
{"entities": [{"text": "L-DOPA", "type": "Chemical"}, {"text": "LID", "type": "Disease"}]}

Example input:
Sentence: Sham-operated rats served as normotensive controls ( 128 +/- 3 mm Hg , n = 8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: In Group 2 the rats were trained to approach different shelves in different drug states .

Example answer:
{"entities": []}

Example input:
Sentence: In female rats , only a weak tendency toward aggressiveness was found .

Example answer:
{"entities": [{"text": "aggressiveness", "type": "Disease"}]}

Example input:
Sentence: The aim of this study was to examine further the renal function , including morphological analysis of the kidneys of male Sprague-Dawley rats treated with either cyclosporine A ( CsA ) , tacrolimus ( FK506 ) or SRL as monotherapies or in different combinations .

Example answer:
{"entities": [{"text": "cyclosporine A", "type": "Chemical"}, {"text": "CsA", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: In conclusion , the present study demonstrates gender differences in the development of the apomorphine-induced aggressive behavior and indicates that the female rats do not fill the validation criteria for use in this method .

Example answer:
{"entities": [{"text": "apomorphine-induced", "type": "Chemical"}, {"text": "aggressive behavior", "type": "Disease"}]}

Example input:
Sentence: Locomotor activity was assessed in male Sprague-Dawley rats tested in photocell cages .

Example answer:
{"entities": []}

Example input:
Sentence: Ten rats received saline as a control group .

Example answer:
{"entities": []}

Example input:
Sentence: Male Sprague-Dawley rats were treated with D-penicillamine ( D-pen ) 500 mg/kg/day for 10 or 42 days .

Example answer:
{"entities": [{"text": "D-penicillamine", "type": "Chemical"}, {"text": "D-pen", "type": "Chemical"}]}

Example input:
Sentence: Thirty male Sprague-Dawley rats were divided randomly into four treatment groups : saline , dexamethasone ( dex ) , allopurinol plus saline , and allopurinol plus dex .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "dex", "type": "Chemical"}, {"text": "allopurinol", "type": "Chemical"}]}

Input:
Sentence: METHODS : Sixty female Sprague-Dawley ( SD ) rats were randomly divided into three groups .

## Item bc5cdr:test:3849
Example input:
Sentence: 9 ( 2006 ) , 917 ] recently identified the microglial-specific fractalkine receptor ( CX3CR1 ) as an important mediator of MPTP-induced neurodegeneration of DA neurons .

Example answer:
{"entities": [{"text": "MPTP-induced", "type": "Chemical"}, {"text": "neurodegeneration", "type": "Disease"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: Because such a compensatory mechanism most likely occurs to reduce injury to the brain from cytotoxic compounds , the present data substantiate the concept that MRP2 performs a protective role in the BBB .

Example answer:
{"entities": [{"text": "injury to the brain", "type": "Disease"}]}

Example input:
Sentence: Under anesthesia , the superior temporal gyrus of adult macaque monkeys was exposed , and the tonotopic organization of A1 was mapped using conventional microelectrode recording techniques .

Example answer:
{"entities": []}

Example input:
Sentence: This study tested the hypothesis that activation of nociceptive muscle afferent fibers would be linked to an increased excitability of the human jaw-stretch reflex and whether this process would be sensitive to length and velocity of the stretch .

Example answer:
{"entities": [{"text": "nociceptive muscle", "type": "Disease"}]}

Example input:
Sentence: She noticed hoarseness and distally accentuated motor and sensory dysfunction after she had recovered from this state .

Example answer:
{"entities": [{"text": "hoarseness", "type": "Disease"}]}

Example input:
Sentence: The results indicate that the deprived area of A1 undergoes extensive reorganization and becomes responsive to intact cochlear frequencies .

Example answer:
{"entities": []}

Example input:
Sentence: These data support the hypothesis that SE-induced mossy fiber sprouting and synaptic reorganization are relevant characteristics of seizure development in these murine strains , resembling rat models of human temporal lobe epilepsy .

Example answer:
{"entities": [{"text": "SE-induced", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}]}

Example input:
Sentence: Abnormal movements and deafness occurred only in rats treated during the preweaning period ; within this period the greatest sensitivities for these abnormalities occurred from 2 to 11-17 and 5 to 11 days of age , respectively , indicating that the cochlea is more sensitive to streptomycin than the site ( vestibular or central ) responsible for the dyskinesias .

Example answer:
{"entities": [{"text": "Abnormal movements", "type": "Disease"}, {"text": "deafness", "type": "Disease"}, {"text": "streptomycin", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: The first ultrastructural changes in structural elements of the blood-brain-barrier ( BBB ) in the cerebellar cortex were detectable after 3 months of the experiment .

Example answer:
{"entities": []}

Example input:
Sentence: Alterations in the structural elements of the BBB coexisted with marked lesions of neurons of the cerebellum ( Purkinje cells are earliest ) .

Example answer:
{"entities": []}

Input:
Sentence: This was evident only when a sensory component was involved in the induction of plasticity , indicating that cerebellar sensory processing function is involved in the resurgence of M1 plasticity .

## Item bc5cdr:test:3871
Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: NRA0160 and clozapine significantly reversed the disruption of prepulse inhibition ( PPI ) in rats produced by apomorphine .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "apomorphine", "type": "Chemical"}]}

Example input:
Sentence: Adriamycin ( 50 mg/50 ml ) was administered intravesically within 24 h after transurethral resection of TA-T1 ( O-A ) bladder tumors .

Example answer:
{"entities": [{"text": "Adriamycin", "type": "Chemical"}, {"text": "bladder tumors", "type": "Disease"}]}

Example input:
Sentence: PURPOSE : The influence of an irreversible inhibitor of constitutive NO synthase ( L-NOArg ; 1.0 mg/kg ip ) , a relatively selective inhibitor of inducible NO synthase ( L-NIL ; 1.0 mg/kg ip ) and a relatively specific inhibitor of neuronal NO synthase ( 7-NI ; 0.1 mg/kg ip ) , on antihyperalgesic action of selective antagonists of B2 and B1 receptors : D-Arg- [ Hyp3 , Thi5 , D-Tic7 , Oic8 ] bradykinin ( HOE 140 ; 70 nmol/kg ip ) or des Arg10 HOE 140 ( 70 nmol/kg ip ) respectively , in model of diabetic ( streptozotocin-induced ) and toxic ( vincristine-induced ) neuropathy was investigated .

Example answer:
{"entities": [{"text": "NO", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}, {"text": "HOE 140", "type": "Chemical"}, {"text": "des Arg10 HOE 140", "type": "Chemical"}]}

Example input:
Sentence: Bradykinin receptors antagonists and nitric oxide synthase inhibitors in vincristine and streptozotocin induced hyperalgesia in chemotherapy and diabetic neuropathy rat model .

Example answer:
{"entities": [{"text": "Bradykinin", "type": "Chemical"}, {"text": "nitric oxide", "type": "Chemical"}, {"text": "vincristine", "type": "Chemical"}, {"text": "streptozotocin", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "diabetic neuropathy", "type": "Disease"}]}

Example input:
Sentence: Responses of urinary strip preparations from control and cyclophosphamide-pretreated rats to electrical field stimulation and to agonists were assessed in the absence and presence of muscarinic , adrenergic and purinergic receptor antagonists .

Example answer:
{"entities": [{"text": "cyclophosphamide-pretreated", "type": "Chemical"}]}

Example input:
Sentence: In cyclophosphamide-induced cystitis in the rat , detrusor function is impaired and the expression and effects of muscarinic receptors altered .

Example answer:
{"entities": [{"text": "cyclophosphamide-induced", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Example input:
Sentence: Animal studies suggest that incontinence secondary to serotonergic antidepressants could be mediated by the 5HT4 receptors found on the bladder .

Example answer:
{"entities": [{"text": "incontinence", "type": "Disease"}, {"text": "serotonergic antidepressants", "type": "Chemical"}]}

Example input:
Sentence: FANFT-induced cell proliferation in the bladder was significantly suppressed by aspirin co-administration after 4 weeks but not after 12 weeks .

Example answer:
{"entities": [{"text": "FANFT-induced", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}]}

Input:
Sentence: Perfusion of bladder with P2X3 and NK1 receptors antagonists ameliorated the bladder function .

## Item bc5cdr:test:3712
Example input:
Sentence: BACKGROUND : Direct thrombin inhibitors ( DTIs ) provide an alternative method of anticoagulation for patients with a history of heparin-induced thrombocytopenia ( HIT ) or HIT with thrombosis ( HITT ) undergoing cardiopulmonary bypass ( CPB ) .

Example answer:
{"entities": [{"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "HIT", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}, {"text": "HITT", "type": "Disease"}]}

Example input:
Sentence: Determining testosterone only in cases of low sexual desire or abnormal physical examination would have missed 40 % of the cases with low testosterone , including 37 % of those subsequently improved by androgen therapy .

Example answer:
{"entities": [{"text": "testosterone", "type": "Chemical"}, {"text": "low sexual desire", "type": "Disease"}]}

Example input:
Sentence: Serologic testing and immunologic studies were done , and a pericardial biopsy was performed .

Example answer:
{"entities": []}

Example input:
Sentence: OBJECTIVES : To assess the added diagnostic value of a new cardiac performance index ( dP/dtejc ) measurement , based on brachial artery flow changes , as compared to standard 12-lead ECG , for detecting dobutamine-induced myocardial ischemia , using Tc99m-Sestamibi single-photon emission computed tomography as the gold standard of comparison to assess the presence or absence of ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "Tc99m-Sestamibi", "type": "Chemical"}, {"text": "ischemia", "type": "Disease"}]}

Example input:
Sentence: Clinical examinations and skin , oral and parenteral challenges with different corticosteroids and ELISA tests were performed .

Example answer:
{"entities": [{"text": "corticosteroids", "type": "Chemical"}]}

Example input:
Sentence: Assay for mitochondrial respiratory function and histopathological examination of heart tissues were performed .

Example answer:
{"entities": []}

Example input:
Sentence: Diagnosis of these patients can be achieved only if specific AX-related reagents are employed .

Example answer:
{"entities": [{"text": "AX-related", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVES : To correlate optical density and percent inhibition of a two-step heparin-induced thrombocytopenia ( HIT ) antigen assay with thrombosis ; the assay utilizes reaction inhibition characteristics of a high heparin concentration .

Example answer:
{"entities": [{"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "HIT", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Forty of 94 HIT patients had thrombosis at diagnosis ; 54/94 had isolated-HIT without thrombosis .

Example answer:
{"entities": [{"text": "HIT", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: At diagnosis there was no significant difference in OD between HIT patients with thrombosis and those with isolated-HIT .

Example answer:
{"entities": [{"text": "HIT", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}]}

Input:
Sentence: Current `` diagnostic '' tests , which primarily include functional and antigenic assays , have more of a confirmatory than diagnostic role in the management of HIT .

## Item bc5cdr:test:3746
Example input:
Sentence: OBJECTIVES : To assess the added diagnostic value of a new cardiac performance index ( dP/dtejc ) measurement , based on brachial artery flow changes , as compared to standard 12-lead ECG , for detecting dobutamine-induced myocardial ischemia , using Tc99m-Sestamibi single-photon emission computed tomography as the gold standard of comparison to assess the presence or absence of ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "Tc99m-Sestamibi", "type": "Chemical"}, {"text": "ischemia", "type": "Disease"}]}

Example input:
Sentence: The blood amounts and hematoma volumes were significantly correlated , and the hematoma induced by 0.014-unit collagenase was adequate to detect ICH deterioration .

Example answer:
{"entities": [{"text": "hematoma", "type": "Disease"}, {"text": "ICH", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : An association has been found between transplant glomerulopathy ( TG ) and reduplication of peritubular capillary basement membranes ( PTCR ) .

Example answer:
{"entities": [{"text": "transplant glomerulopathy", "type": "Disease"}, {"text": "TG", "type": "Disease"}]}

Example input:
Sentence: All patients were on a regular transfusion-chelation program maintaining a mean hemoglobin level of 9.5 gr/dl .

Example answer:
{"entities": []}

Example input:
Sentence: All the patients were skin test negative to BPO ; 49 of 51 ( 96 % ) were also negative to MDM , and 44 of 46 ( 96 % ) to PG .

Example answer:
{"entities": [{"text": "BPO", "type": "Chemical"}, {"text": "MDM", "type": "Disease"}, {"text": "PG", "type": "Chemical"}]}

Example input:
Sentence: Diagnosis of this potentially fatal complication may be delayed or missed if renal tissue or the peripheral blood smear is not examined , because renal failure may be ascribed to cisplatin nephrotoxicity and the anemia and thrombocytopenia to drug-induced bone marrow suppression .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "bone marrow suppression", "type": "Disease"}]}

Example input:
Sentence: Haemodilution in groups B and C was produced by withdrawing approximately 1000 mL of blood and replacing it with the same amount of dextran solution , and final haematocrit values were 21 or 22 % .

Example answer:
{"entities": [{"text": "Haemodilution", "type": "Disease"}, {"text": "dextran", "type": "Chemical"}]}

Example input:
Sentence: When both skin test and RAST for BPO were negative , single-blind , placebo-controlled challenge tests were done to ensure tolerance of PG or sensitivity to AX .

Example answer:
{"entities": [{"text": "BPO", "type": "Chemical"}, {"text": "PG", "type": "Chemical"}, {"text": "AX", "type": "Chemical"}]}

Example input:
Sentence: The patient required massive transfusion support ( 55 units of red blood cells , 42 units of fresh-frozen plasma , 40 units of cryoprecipitate , 40 units of platelets , and three doses of recombinant Factor VIIa ) for severe intraoperative and postoperative bleeding .

Example answer:
{"entities": []}

Example input:
Sentence: Because DTIs do not have reversal agents , surgical teams and transfusion services should remain aware of the possibility of massive transfusion events during anticoagulation with these agents .

Example answer:
{"entities": []}

Input:
Sentence: Transfusion reaction workup was negative .

## Item bc5cdr:test:3750
Example input:
Sentence: The development of severe anemia at 6 months post-CAB was predictable by the reduction of Hb baseline value of more than 2.5 g/dl after 3 months of CAB ( p = 0.01 ) .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}]}

Example input:
Sentence: Three patients developed congestive heart failure after the completion of chemotherapy .

Example answer:
{"entities": [{"text": "congestive heart failure", "type": "Disease"}]}

Example input:
Sentence: Patients treated with alkylating agents have an increased risk of development of acute nonlymphocytic leukemia , and both alkylating agents and azathioprine are associated with the development of non-Hodgkin 's lymphoma .

Example answer:
{"entities": [{"text": "alkylating agents", "type": "Chemical"}, {"text": "acute nonlymphocytic leukemia", "type": "Disease"}, {"text": "azathioprine", "type": "Chemical"}, {"text": "non-Hodgkin 's lymphoma", "type": "Disease"}]}

Example input:
Sentence: Five patients with carcinoma developed thrombotic microangiopathy ( characterized by renal insufficiency , microangiopathic hemolytic anemia , and usually thrombocytopenia ) after treatment with cisplatin , bleomycin , and a vinca alkaloid .

Example answer:
{"entities": [{"text": "carcinoma", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "microangiopathic hemolytic anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "bleomycin", "type": "Chemical"}, {"text": "vinca alkaloid", "type": "Chemical"}]}

Example input:
Sentence: At six months post-CAB , patients with severe anemia had a Hb mean value of 10.2 +/- 0.1 g/dl ( X +/- SE ) , whereas the other patients had mild anemia with Hb mean value of 13.2 +/- 0.17 ( X +/- SE ) .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}]}

Example input:
Sentence: Combined androgen blockade-induced anemia in prostate cancer patients without bone involvement .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "prostate cancer", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : Our data suggest that rHuEPO-beta correctable CAB-induced anemia occurs in 14.3 % of prostate cancer patients after 6 months of therapy .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "prostate cancer", "type": "Disease"}]}

Example input:
Sentence: Diagnosis of this potentially fatal complication may be delayed or missed if renal tissue or the peripheral blood smear is not examined , because renal failure may be ascribed to cisplatin nephrotoxicity and the anemia and thrombocytopenia to drug-induced bone marrow suppression .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "bone marrow suppression", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : To determine the onset and extent of combined androgen blockade ( CAB ) -induced anemia in prostate cancer patients without bone involvement .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "prostate cancer", "type": "Disease"}]}

Example input:
Sentence: The development of severe CAB-induced anemia in prostate cancer patients did not correlate with T baseline values ( T < 3 ng/ml versus T > or = 3 ng/ml ) , with age ( < 76 yrs versus > or = 76 yrs ) , and clinical stage ( stage C versus stage D1 ) .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "prostate cancer", "type": "Disease"}]}

Input:
Sentence: Other causes of anemia should be considered in patients with worse-than-expected anemia after chemotherapy .

## Item bc5cdr:test:3759
Example input:
Sentence: The present study was undertaken to examine the role of sleep disturbance , induced by clomipramine administration , on the secretory rate of prolactin ( PRL ) in addition to the direct drug effect .

Example answer:
{"entities": [{"text": "sleep disturbance", "type": "Disease"}, {"text": "clomipramine", "type": "Chemical"}]}

Example input:
Sentence: Hypothalamic prolactin receptor messenger ribonucleic acid levels , prolactin signaling , and hyperprolactinemic inhibition of pulsatile luteinizing hormone secretion are dependent on estradiol .

Example answer:
{"entities": [{"text": "ribonucleic acid", "type": "Chemical"}, {"text": "hyperprolactinemic", "type": "Disease"}, {"text": "estradiol", "type": "Chemical"}]}

Example input:
Sentence: Estradiol is known to influence expression of the long form of prolactin receptors ( PRL-R ) and components of prolactin 's signaling pathway .

Example answer:
{"entities": [{"text": "Estradiol", "type": "Chemical"}]}

Example input:
Sentence: Independent but not additive effects of Na and Ca are shown by decreases in the values of [ verapamil ] o needed to reduce BF by 30 % ( IC30 ) with the following order of inhibitory potency : LNa > LCa > HCa > N , resulting LNa+HCa similar to LNa .

Example answer:
{"entities": [{"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: To test the hypothesis that estrogen increases PRL-R expression and sensitivity to prolactin , we next demonstrated that estradiol greatly augments prolactin-induced STAT5 activation .

Example answer:
{"entities": [{"text": "estrogen", "type": "Chemical"}, {"text": "estradiol", "type": "Chemical"}]}

Example input:
Sentence: Lastly , we measured PRL-R and suppressor of cytokine signaling ( SOCS-1 and -3 and CIS , which reflect the level of prolactin signaling ) mRNAs in response to sulpiride and estradiol .

Example answer:
{"entities": [{"text": "sulpiride", "type": "Chemical"}, {"text": "estradiol", "type": "Chemical"}]}

Example input:
Sentence: As the relative increase in PRL secretion expressed as a percentage of the mean did not significantly differ between the night and day time studies ( 46 +/- 19 % vs 34 +/- 10 % ) , it can be concluded that the observed sleep disturbance did not interfere with the drug action per se .

Example answer:
{"entities": [{"text": "sleep disturbance", "type": "Disease"}]}

Example input:
Sentence: For both experiments the drug intake led to significant increases in PRL secretion , acting preferentially on tonic secretion as pulse amplitude and frequency did not differ significantly from corresponding control values .

Example answer:
{"entities": []}

Example input:
Sentence: Possible mechanisms that involve a verapamil-related increase in platelet and/or vascular alpha 2-adrenoreceptor affinity for catecholamines are discussed .

Example answer:
{"entities": [{"text": "verapamil-related", "type": "Chemical"}, {"text": "catecholamines", "type": "Chemical"}]}

Example input:
Sentence: Dose-dependent bradycardia induced by verapamil was potentiated by LNa , LCa , and HCa .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}]}

Input:
Sentence: Verapamil responsiveness was determined by peak percent change in basal prolactin levels ( PRL ) .

## Item bc5cdr:test:3884
Example input:
Sentence: Six partial responses were observed for an overall response rate of 16 % .

Example answer:
{"entities": []}

Example input:
Sentence: The overall response rate ( World Health Organization [ WHO ] criteria ) was 15 % ( CR , 2 % ; PR 13 % ; 95 % CI , 6 % to 29 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: An objective response was observed in 73.5 % of the patients ( 95 % confidence interval [ CI ] , 55.6-87.1 % ) , including 4 complete responses ( 11.7 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: One of 16 patients ( 6 % ) with prior chemotherapy had a complete response ( CR ) of 31 weeks ' duration ( 95 % CI , 0 % to 30 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: All 20 patients responded to this regimen , 16/20 ( 80 % ) achieved a complete remission , and 20 % obtained a partial remission .

Example answer:
{"entities": []}

Example input:
Sentence: Of 18 patients evaluable for response , seven ( 39 % ) achieved a complete response and six ( 33 % ) achieved a partial response .

Example answer:
{"entities": []}

Example input:
Sentence: Of 24 evaluable patients , two achieved a complete remission and one achieved a partial remission for an overall response rate of 12.5 % ( 95 % confidence interval : 2.6-32.4 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Six of 30 patients ( 20 % ) without prior chemotherapy achieved a partial response ( PR ) ( 95 % confidence interval [ CI ] , 8 % to 39 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Two patients attained a complete response ( 4 % ) and 11 patients ( 22 % ) achieved a partial response .

Example answer:
{"entities": []}

Example input:
Sentence: According to intention-to-treat , the overall response rate was 71.4 % ( 95 % CI , 53 .

Example answer:
{"entities": []}

Input:
Sentence: On an intention-to-treat basis , 55 % of the patients achieved at least partial response , including 19 % CR and 35 % achieved at least very good partial response .

## Item bc5cdr:test:3617
Example input:
Sentence: Animals were administered nicotine , carbachol , or neostigmine via timed tail vein infusion , and the latencies to onset of tremor and clonus were recorded and converted to threshold dose .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}, {"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: Infarcts in substantia nigra pars reticulata were evoked by prolonged pilocarpine-induced status epilepticus .

Example answer:
{"entities": [{"text": "Infarcts in substantia nigra pars reticulata", "type": "Disease"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}]}

Example input:
Sentence: The animal model used to produce infarction implies artery ligation but chemical induction can be easily obtained with isoproterenol .

Example answer:
{"entities": [{"text": "infarction", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: Investigation of mitochondrial involvement in the experimental model of epilepsy induced by pilocarpine .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: In Mg ( 2+ ) -free bathing medium containing bicuculline , conditions designed to increase excitability in the slices , electrical stimulation of the hilus resulted in a single population spike in granule cells from control mice and pilocarpine-treated mice that did not experience SE .

Example answer:
{"entities": [{"text": "Mg", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "pilocarpine-treated", "type": "Chemical"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: We compared the effects of 17beta-estradiol in adult male and ovariectomized female rats subjected to lithium-pilocarpine-induced SE .

Example answer:
{"entities": [{"text": "17beta-estradiol", "type": "Chemical"}, {"text": "lithium-pilocarpine-induced", "type": "Chemical"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: SE was induced 20 h following the second injection and terminated 3 h later .

Example answer:
{"entities": [{"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Similar to rats , systemic pilocarpine injection causes status epilepticus ( SE ) and the eventual development of spontaneous seizures and mossy fiber sprouting in C57BL/6 and CD1 mice , but the physiological correlates of these events have not been identified in mice .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Input:
Sentence: METHODS : SE was induced by pilocarpine injection .

## Item bc5cdr:test:3466
Example input:
Sentence: CONCLUSIONS : Delirium was found in 10 % of clozapine-treated inpatients , particularly in older patients exposed to other central anticholinergics .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}, {"text": "clozapine-treated", "type": "Chemical"}]}

Example input:
Sentence: He developed acute neurologic symptoms of mental confusion , disorientation and irritability , and then lapsed into a deep coma , lasting for approximately 40 hours during the first dose ( day 2 ) of 5-fluorouracil and folinic acid infusion .

Example answer:
{"entities": [{"text": "confusion", "type": "Disease"}, {"text": "disorientation", "type": "Disease"}, {"text": "irritability", "type": "Disease"}, {"text": "coma", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: Reported medications included bumetanide , pravastatin , and paroxetine .

Example answer:
{"entities": [{"text": "bumetanide", "type": "Chemical"}, {"text": "pravastatin", "type": "Chemical"}, {"text": "paroxetine", "type": "Chemical"}]}

Example input:
Sentence: In the present paper the authors describe 2 female patients who developed incontinence secondary to the selective serotonin reuptake inhibitors paroxetine and sertraline , as well as a third who developed this side effect on venlafaxine .

Example answer:
{"entities": [{"text": "incontinence", "type": "Disease"}, {"text": "serotonin", "type": "Chemical"}, {"text": "paroxetine", "type": "Chemical"}, {"text": "sertraline", "type": "Chemical"}, {"text": "venlafaxine", "type": "Chemical"}]}

Example input:
Sentence: Desipramine-induced delirium at `` subtherapeutic '' concentrations : a case report .

Example answer:
{"entities": [{"text": "Desipramine-induced", "type": "Chemical"}, {"text": "delirium", "type": "Disease"}]}

Example input:
Sentence: We report the increased amount of motor disability in four patients with idiopathic Parkinson 's disease after exposure to the antidepressant fluoxetine .

Example answer:
{"entities": [{"text": "motor disability", "type": "Disease"}, {"text": "idiopathic Parkinson 's disease", "type": "Disease"}, {"text": "antidepressant", "type": "Chemical"}, {"text": "fluoxetine", "type": "Chemical"}]}

Example input:
Sentence: Three months later the patient was exposed to a single dose of metoprolol , diltiazem , propafenone ( since he had received this drug in the past ) , and sparteine ( as a probe for the debrisoquine/sparteine type polymorphism of oxidative drug metabolism ) .

Example answer:
{"entities": [{"text": "metoprolol", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "propafenone", "type": "Chemical"}, {"text": "sparteine", "type": "Chemical"}, {"text": "debrisoquine/sparteine", "type": "Chemical"}]}

Example input:
Sentence: The purpose of this study was to evaluate the effect of cinacalcet on CYP2D6 activity , using desipramine as a probe substrate , in healthy subjects .

Example answer:
{"entities": [{"text": "cinacalcet", "type": "Chemical"}, {"text": "desipramine", "type": "Chemical"}]}

Example input:
Sentence: An elderly patient treated with low dose Desipramine developed a delirium while her plasma level was in the `` subtherapeutic '' range .

Example answer:
{"entities": [{"text": "Desipramine", "type": "Chemical"}, {"text": "delirium", "type": "Disease"}]}

Example input:
Sentence: METHODS : Seventeen subjects who were genotyped as CYP2D6 extensive metabolizers were enrolled in this randomized , open-label , crossover study to receive a single oral dose of desipramine ( 50 mg ) on two separate occasions , once alone and once after multiple doses of cinacalcet ( 90 mg for 7 days ) .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}]}

Input:
Sentence: A MEDLINE search ( 1966-January 2009 ) revealed one in vivo pharmacokinetic study on the interaction between flecainide , a CYP2D6 substrate , and paroxetine , a CYP2D6 inhibitor , as well as 3 case reports of flecainide-induced delirium .

## Item bc5cdr:test:3681
Example input:
Sentence: We have described a unique patient who had reversible and dose-related myasthenia gravis after penicillamine and chloroquine therapy for rheumatoid arthritis .

Example answer:
{"entities": [{"text": "myasthenia gravis", "type": "Disease"}, {"text": "penicillamine", "type": "Chemical"}, {"text": "chloroquine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Example input:
Sentence: CASE SUMMARY : A 40-year-old woman with major depression took an overdose of venlafaxine in an apparent suicide attempt .

Example answer:
{"entities": [{"text": "major depression", "type": "Disease"}, {"text": "overdose", "type": "Disease"}, {"text": "venlafaxine", "type": "Chemical"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: This article describes two critically ill patients in whom transient episodes of hypotension reproducibly developed after administration of acetaminophen .

Example answer:
{"entities": [{"text": "critically ill", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}, {"text": "acetaminophen", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : ATT-ALF constituted 5.7 % of ALF at our center and had a high mortality rate .

Example answer:
{"entities": [{"text": "ALF", "type": "Disease"}]}

Example input:
Sentence: ATT-ALF patients were younger ( 32.87 [ +/-15.8 ] years ) , and 49 ( 70 % ) of them were women .

Example answer:
{"entities": []}

Example input:
Sentence: However , three case control studies , one each in North Carolina , northern Maryland , and West Berlin , Germany , showed that habitual use of acetaminophen is also associated with chronic renal failure and ESRD , with a relative risk in the range of 2 to 4 .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "chronic renal failure", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: The mortality rate among patients with ATT-ALF was high ( 67.1 % , n = 47 ) , and only 23 ( 32.9 % ) patients recovered with medical treatment .

Example answer:
{"entities": []}

Example input:
Sentence: Antituberculosis therapy ( ATT ) -associated acute liver failure ( ATT-ALF ) is the commonest drug-induced ALF in South Asia .

Example answer:
{"entities": [{"text": "Antituberculosis", "type": "Chemical"}, {"text": "acute liver failure", "type": "Disease"}, {"text": "ALF", "type": "Disease"}]}

Example input:
Sentence: From January 1986 to January 2009 , 1223 consecutive ALF patients were evaluated : ATT alone was the cause in 70 ( 5.7 % ) patients .

Example answer:
{"entities": [{"text": "ALF", "type": "Disease"}]}

Input:
Sentence: Two acetaminophen-induced ALF patients reattempted suicide post-LT ( one died 8 years post-LT ) .

## Item bc5cdr:test:3439
Example input:
Sentence: Therefore , like VPA , the finding that VPU could drastically reduce pilocarpine-induced increases in glutamate and aspartate should account , at least partly , for its anticonvulsant activity observed in pilocarpine-induced seizure in experimental animals .

Example answer:
{"entities": [{"text": "VPA", "type": "Chemical"}, {"text": "VPU", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Cocaine-induced anxiety was also attenuated in Dbh +/- mice following administration of disulfiram , a dopamine beta-hydroxylase ( DBH ) inhibitor .

Example answer:
{"entities": [{"text": "Cocaine-induced", "type": "Chemical"}, {"text": "anxiety", "type": "Disease"}, {"text": "disulfiram", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: The effects of varying the extracellular concentrations of Na and Ca ( [ Na ] o and [ Ca ] o ) on both , the spontaneous beating and the negative chronotropic action of verapamil , were studied in the isolated rat atria .

Example answer:
{"entities": [{"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: Long-term intragastric application of the antiepileptic drug sodium valproate ( Vupral `` Polfa '' ) at the effective dose of 200 mg/kg b. w. once daily to rats for 1 , 3 , 6 , 9 and 12 months revealed neurological disorders indicating cerebellum damage ( `` valproate encephalopathy '' ) .

Example answer:
{"entities": [{"text": "sodium valproate", "type": "Chemical"}, {"text": "neurological disorders", "type": "Disease"}, {"text": "cerebellum damage", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: A comparable overexpression of Pgp in the BBB was obtained after pilocarpine-induced seizures in wild-type Wistar rats .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : In this preliminary report , divalproex sodium was a superior alternative to lithium in bipolar patients experiencing cognitive deficits , loss of creativity , and functional impairments .

Example answer:
{"entities": [{"text": "divalproex sodium", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "bipolar", "type": "Disease"}, {"text": "cognitive deficits", "type": "Disease"}, {"text": "loss of creativity", "type": "Disease"}, {"text": "functional impairments", "type": "Disease"}]}

Example input:
Sentence: The rats received AChE reactivator pralidoxime-2-chloride ( 2PAM ) ( 30.0 mg/kg BW ) , anticonvulsant diazepam ( 2.0 mg/kg BW ) , A ( 1 ) -adenosine receptor agonist N ( 6 ) -cyclopentyl adenosine ( CPA ) ( 2.0 mg/kg BW ) , NMDA-receptor antagonist dizocilpine maleate ( +-MK801 hydrogen maleate ) ( 2.0 mg/kg BW ) or their combinations with cholinolytic drug atropine sulfate ( 50.0 mg/kg BW ) immediately or 30 min after the single SC injection of DFP .

Example answer:
{"entities": [{"text": "pralidoxime-2-chloride", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "N ( 6 ) -cyclopentyl adenosine", "type": "Chemical"}, {"text": "CPA", "type": "Chemical"}, {"text": "NMDA-receptor", "type": "Chemical"}, {"text": "dizocilpine maleate", "type": "Chemical"}, {"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: Apamin , a selective blocker of calcium-dependent potassium channels , was administered intracerebroventricularly in rats anesthetized with 0.8 % sevoflurane to investigate the mechanism of the anticonvulsive effects .

Example answer:
{"entities": [{"text": "Apamin", "type": "Chemical"}, {"text": "calcium-dependent", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}, {"text": "sevoflurane", "type": "Chemical"}]}

Input:
Sentence: The intracerebroventricular ( ICV ) administration of ouabain ( a Na ( + ) /K ( + ) -ATPase inhibitor ) in rats has been suggested to mimic some symptoms of human bipolar mania .

## Item bc5cdr:test:3711
Example input:
Sentence: PATIENTS AND METHODS : Patients with more than 50 % decrease in platelet count or thrombocytopenia ( < 150 x 10 ( 9 ) /L ) after exposure to heparin , who had a positive two-step antigen assay [ optical density ( OD ) > 0.4 and > 50 inhibition with high concentration of heparin ] were included in the study .

Example answer:
{"entities": [{"text": "thrombocytopenia", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: A study on the effect of the duration of subcutaneous heparin injection on bruising and pain .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}, {"text": "bruising", "type": "Disease"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Forty of 94 HIT patients had thrombosis at diagnosis ; 54/94 had isolated-HIT without thrombosis .

Example answer:
{"entities": [{"text": "HIT", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: Pooled data from trials comparing antithrombotic treatment with placebo have shown that warfarin reduces the risk of stroke by 62 % , and that aspirin alone reduces the risk by 22 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "stroke", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Although different methods to prevent bruising and pain following the subcutaneous injection of heparin have been widely studied and described , the effect of injection duration on the occurrence of bruising and pain is little documented .

Example answer:
{"entities": [{"text": "bruising", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : It was determined that injection duration had an effect on bruising and pain following the subcutaneous administration of heparin .

Example answer:
{"entities": [{"text": "bruising", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: Ximelagatran , an oral direct thrombin inhibitor , was found to be as efficient as vitamin K antagonist drugs in the prevention of embolic events , but has been recently withdrawn because of abnormal liver function tests .

Example answer:
{"entities": [{"text": "Ximelagatran", "type": "Chemical"}, {"text": "vitamin K", "type": "Chemical"}, {"text": "embolic events", "type": "Disease"}, {"text": "abnormal liver function", "type": "Disease"}]}

Example input:
Sentence: AIM : This study was carried out to determine the effect of injection duration on bruising and pain following the administration of the subcutaneous injection of heparin .

Example answer:
{"entities": [{"text": "bruising", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVES : To correlate optical density and percent inhibition of a two-step heparin-induced thrombocytopenia ( HIT ) antigen assay with thrombosis ; the assay utilizes reaction inhibition characteristics of a high heparin concentration .

Example answer:
{"entities": [{"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "HIT", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Direct thrombin inhibitors ( DTIs ) provide an alternative method of anticoagulation for patients with a history of heparin-induced thrombocytopenia ( HIT ) or HIT with thrombosis ( HITT ) undergoing cardiopulmonary bypass ( CPB ) .

Example answer:
{"entities": [{"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "HIT", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}, {"text": "HITT", "type": "Disease"}]}

Input:
Sentence: The treatment of HIT mandates an immediate cessation of all heparin exposure and the institution of an antithrombotic therapy , most commonly using a direct thrombin inhibitor .

## Item bc5cdr:test:3509
Example input:
Sentence: Clinical and experimental data published to date suggest several possible mechanisms by which cocaine may result in acute myocardial infarction .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: We describe eight patients in whom cocaine use was related to stroke and review 39 cases from the literature .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "stroke", "type": "Disease"}]}

Example input:
Sentence: Intracranial aneurysms and cocaine abuse : analysis of prognostic indicators .

Example answer:
{"entities": [{"text": "Intracranial aneurysms", "type": "Disease"}, {"text": "cocaine abuse", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : Cocaine use predisposed aneurysmal rupture at a significantly earlier age and in much smaller aneurysms .

Example answer:
{"entities": [{"text": "Cocaine", "type": "Chemical"}, {"text": "aneurysmal rupture", "type": "Disease"}, {"text": "aneurysms", "type": "Disease"}]}

Example input:
Sentence: Eleven of the cocaine abusers and none of the controls had ECG evidence of significant myocardial injury defined as myocardial infarction , ischemia , and bundle branch block .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "myocardial injury", "type": "Disease"}, {"text": "myocardial infarction", "type": "Disease"}, {"text": "ischemia", "type": "Disease"}, {"text": "bundle branch block", "type": "Disease"}]}

Example input:
Sentence: In individuals with preexisting , high-grade coronary arterial narrowing , acute myocardial infarction may result from an increase in myocardial oxygen demand associated with cocaine-induced increase in rate-pressure product .

Example answer:
{"entities": [{"text": "acute myocardial infarction", "type": "Disease"}, {"text": "oxygen", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVE : The outcome of subarachnoid hemorrhage associated with cocaine abuse is reportedly poor .

Example answer:
{"entities": [{"text": "subarachnoid hemorrhage", "type": "Disease"}, {"text": "cocaine abuse", "type": "Disease"}]}

Example input:
Sentence: Stroke followed cocaine use by inhalation , intranasal , intravenous , and intramuscular routes .

Example answer:
{"entities": [{"text": "Stroke", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Stroke associated with cocaine use .

Example answer:
{"entities": [{"text": "Stroke", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: These data indicate that ( 1 ) the apparent incidence of stroke related to cocaine use is increasing ; ( 2 ) cocaine-associated stroke occurs primarily in young adults ; ( 3 ) stroke may follow any route of cocaine administration ; ( 4 ) stroke after cocaine use is frequently associated with intracranial aneurysms and arteriovenous malformations ; and ( 5 ) in cocaine-associated stroke , the frequency of intracranial hemorrhage exceeds that of cerebral infarction .

Example answer:
{"entities": [{"text": "stroke", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}, {"text": "cocaine-associated", "type": "Chemical"}, {"text": "intracranial aneurysms", "type": "Disease"}, {"text": "arteriovenous malformations", "type": "Disease"}, {"text": "intracranial hemorrhage", "type": "Disease"}, {"text": "cerebral infarction", "type": "Disease"}]}

Input:
Sentence: Cocaine is a risk factor for both ischemic and haemorrhagic stroke .

## Item bc5cdr:test:3774
Example input:
Sentence: Using puromycin aminonucleoside nephrosis ( PAN ) rats , we studied early ultrastructural and permeability changes in relation to the expression of the podocyte-associated molecules nephrin , a-actinin , dendrin , and plekhh2 , the last two of which were only recently discovered in podocytes .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: Reactive oxygen species have been implicated in the pathogenesis of acute puromycin aminonucleoside ( PAN ) -induced nephropathy , with antioxidants significantly reducing the proteinuria .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: We suggest that our patient 's tubular dysfunction and myopathy may have resulted from mitochondrial dysfunction which is triggered by tacrolimus and augmented by lamivudine .

Example answer:
{"entities": [{"text": "tubular dysfunction", "type": "Disease"}, {"text": "myopathy", "type": "Disease"}, {"text": "mitochondrial dysfunction", "type": "Disease"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: These results suggest that dehydration and/or the activation of visceral afferent inputs may contribute to the elevation of plasma AVP and the upregulation of AVP gene expression in the PVN and the SON of the Li-induced diabetes insipidus rat .

Example answer:
{"entities": [{"text": "dehydration", "type": "Disease"}, {"text": "AVP", "type": "Chemical"}, {"text": "Li-induced", "type": "Chemical"}, {"text": "diabetes insipidus", "type": "Disease"}]}

Example input:
Sentence: Reduction of heparan sulphate-associated anionic sites in the glomerular basement membrane of rats with streptozotocin-induced diabetic nephropathy .

Example answer:
{"entities": [{"text": "heparan", "type": "Chemical"}, {"text": "streptozotocin-induced", "type": "Chemical"}, {"text": "diabetic nephropathy", "type": "Disease"}]}

Example input:
Sentence: We conclude that in streptozotocin-diabetic rats with an increased urinary albumin excretion , a reduced heparan sulphate charge barrier/density is found at the lamina rara externa of the glomerular basement membrane .

Example answer:
{"entities": [{"text": "streptozotocin-diabetic", "type": "Chemical"}, {"text": "heparan sulphate", "type": "Chemical"}]}

Example input:
Sentence: Heparan sulphate-associated anionic sites in the glomerular basement membrane were studied in rats 8 months after induction of diabetes by streptozotocin and in age- adn sex-matched control rats , employing the cationic dye cuprolinic blue .

Example answer:
{"entities": [{"text": "Heparan", "type": "Chemical"}, {"text": "diabetes", "type": "Disease"}, {"text": "streptozotocin", "type": "Chemical"}, {"text": "cuprolinic blue", "type": "Chemical"}]}

Example input:
Sentence: Podocyte injury and focal segmental glomerulosclerosis have been related to mToR inhibition in some patients , but the pathways underlying these lesions remain hypothetic .

Example answer:
{"entities": [{"text": "glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : The rate of contrast-induced nephropathy , defined by multiple end points , is not statistically different after the intraarterial administration of iopamidol or iodixanol to high-risk patients , with or without diabetes mellitus .

Example answer:
{"entities": [{"text": "nephropathy", "type": "Disease"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}, {"text": "diabetes mellitus", "type": "Disease"}]}

Input:
Sentence: CONCLUSIONS : EndoMT is a novel pathway leading to early development of diabetic nephropathy .

## Item bc5cdr:test:3920
Example input:
Sentence: RESULTS : Two hundred sixty-five patients were included in this analysis ( n=92 , 93 , and 80 for placebo , low dose , and high dose , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: There were no serious clinical side effects , but dose reduction was required in two patients because of nausea .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}]}

Example input:
Sentence: The drug was withdrawn on presentation to hospital in 11 patients , with rapid clinical improvement in 9 .

Example answer:
{"entities": []}

Example input:
Sentence: With mild toxicity , a reduction to 30 or 40 mg/kg per dose should result in a reversal of the abnormal results to normal within four weeks .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Discontinuance of effective chemotherapy in this patient during partial remission resulted in fatal disease progression .

Example answer:
{"entities": []}

Example input:
Sentence: After discontinuing the oral alendronate , the patient underwent six cycles of hemodialysis and four cycles of LDL apheresis .

Example answer:
{"entities": [{"text": "alendronate", "type": "Chemical"}]}

Example input:
Sentence: Patients with a DBP reduction of > or =20 % in the high-dose group had a significantly increased adjusted OR for the compound outcome variable death or dependency ( Barthel Index < 60 ) ( n/N=25/26 , OR 10 .

Example answer:
{"entities": [{"text": "DBP reduction", "type": "Disease"}, {"text": "death", "type": "Disease"}]}

Example input:
Sentence: With either discontinuation or decreased dosage of the drug the symptoms disappeared and did not recur .

Example answer:
{"entities": []}

Example input:
Sentence: Most patients ( 57 % ) stopped treatment because of disease progression .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Sixty-seven of 926 patients ( 7.2 % ) required discontinuation of spironolactone due to hyperkalemia ( n = 33 ) or renal failure ( n = 34 ) .

Example answer:
{"entities": [{"text": "spironolactone", "type": "Chemical"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Input:
Sentence: Dose reductions were needed in 31 % of patients and permanent discontinuation in 38.9 % .

## Item bc5cdr:test:3714
Example input:
Sentence: Since the introduction of angiotensin converting enzyme ( ACE ) inhibitors into the adjunctive treatment of patients with congestive heart failure , cases of severe hypotension , especially on the first day of treatment , have occasionally been reported .

Example answer:
{"entities": [{"text": "angiotensin converting enzyme ( ACE ) inhibitors", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: AIM : This study was carried out to determine the effect of injection duration on bruising and pain following the administration of the subcutaneous injection of heparin .

Example answer:
{"entities": [{"text": "bruising", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: Recently , synthetic fibrinolysis inhibitors such as tranexamic acid ( tAMCA ) have been considered as substitutes for aprotinin .

Example answer:
{"entities": [{"text": "tranexamic acid", "type": "Chemical"}, {"text": "tAMCA", "type": "Chemical"}]}

Example input:
Sentence: The ACTIVE-W ( Atrial Fibrillation Clopidogrel Trial with Irbesartan for Prevention of Vascular Events ) study has demonstrated that warfarin is superior to platelet therapy ( clopidogrel plus aspirin ) in the prevention af embolic events .

Example answer:
{"entities": [{"text": "Atrial Fibrillation", "type": "Disease"}, {"text": "Clopidogrel", "type": "Chemical"}, {"text": "Irbesartan", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}, {"text": "clopidogrel", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "embolic events", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : To correlate optical density and percent inhibition of a two-step heparin-induced thrombocytopenia ( HIT ) antigen assay with thrombosis ; the assay utilizes reaction inhibition characteristics of a high heparin concentration .

Example answer:
{"entities": [{"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "HIT", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: Overall , in high-risk patients , warfarin is superior to aspirin in preventing strokes , with a relative risk reduction of 36 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "strokes", "type": "Disease"}]}

Example input:
Sentence: PATIENTS AND METHODS : Patients with more than 50 % decrease in platelet count or thrombocytopenia ( < 150 x 10 ( 9 ) /L ) after exposure to heparin , who had a positive two-step antigen assay [ optical density ( OD ) > 0.4 and > 50 inhibition with high concentration of heparin ] were included in the study .

Example answer:
{"entities": [{"text": "thrombocytopenia", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: Pooled data from trials comparing antithrombotic treatment with placebo have shown that warfarin reduces the risk of stroke by 62 % , and that aspirin alone reduces the risk by 22 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "stroke", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: Ximelagatran , an oral direct thrombin inhibitor , was found to be as efficient as vitamin K antagonist drugs in the prevention of embolic events , but has been recently withdrawn because of abnormal liver function tests .

Example answer:
{"entities": [{"text": "Ximelagatran", "type": "Chemical"}, {"text": "vitamin K", "type": "Chemical"}, {"text": "embolic events", "type": "Disease"}, {"text": "abnormal liver function", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Direct thrombin inhibitors ( DTIs ) provide an alternative method of anticoagulation for patients with a history of heparin-induced thrombocytopenia ( HIT ) or HIT with thrombosis ( HITT ) undergoing cardiopulmonary bypass ( CPB ) .

Example answer:
{"entities": [{"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "HIT", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}, {"text": "HITT", "type": "Disease"}]}

Input:
Sentence: Direct thrombin inhibitors are appropriate , evidence-based alternatives to heparin in patients with a history of HIT , who need to undergo percutaneous coronary intervention .

## Item bc5cdr:test:3409
Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Simvastatinezetimibe and escitalopram ( which she was taking for depression ) were discontinued , and other potential causes of hepatotoxicity were excluded .

Example answer:
{"entities": [{"text": "Simvastatinezetimibe", "type": "Chemical"}, {"text": "escitalopram", "type": "Chemical"}, {"text": "depression", "type": "Disease"}, {"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: Srl should be used with ACEi/ARB therapy and patients monitored for proteinuria and increased renal dysfunction .

Example answer:
{"entities": [{"text": "Srl", "type": "Chemical"}, {"text": "ACEi/ARB", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "renal dysfunction", "type": "Disease"}]}

Example input:
Sentence: Experiments with systemic administration of the Pgp substrate phenobarbital and the selective Pgp inhibitor tariquidar in TR ( - ) rats substantiated that Pgp is functional and compensates for the lack of MRP2 in the BBB .

Example answer:
{"entities": [{"text": "phenobarbital", "type": "Chemical"}, {"text": "tariquidar", "type": "Chemical"}]}

Example input:
Sentence: STUDY DESIGN AND METHODS : Plasma samples from before and after CPB were analyzed postoperatively for argatroban concentration using a modified ecarin clotting time ( ECT ) assay .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Correlation of plasma argatroban concentration versus the patient 's coagulation variables and clinical course suggest that prolonged elevated levels of plasma argatroban may have contributed to the patient 's extended coagulopathy .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "coagulopathy", "type": "Disease"}]}

Example input:
Sentence: Prolonged elevation of plasma argatroban in a cardiac transplant patient with a suspected history of heparin-induced thrombocytopenia with thrombosis .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Unexpectedly high concentrations of argatroban were measured in these samples ( range , 0-32 microg/mL ) , and a prolonged plasma argatroban half life ( t ( 1/2 ) ) of 514 minutes was observed ( published elimination t ( 1/2 ) is 39-51 minutes [ < or = 181 minutes with hepatic impairment ] ) .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "hepatic impairment", "type": "Disease"}]}

Example input:
Sentence: In the following report , a 65-year-old critically ill patient with a suspected history of HITT was administered argatroban for anticoagulation on bypass during heart transplantation .

Example answer:
{"entities": [{"text": "critically ill", "type": "Disease"}, {"text": "HITT", "type": "Disease"}, {"text": "argatroban", "type": "Chemical"}]}

Example input:
Sentence: This is the first report to measure plasma argatroban concentration in the context of CPB and extended coagulopathy .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "coagulopathy", "type": "Disease"}]}

Input:
Sentence: For PCI , argatroban has not been investigated in hepatically impaired patients ; dose adjustment is unnecessary for adult age , sex , race/ethnicity or obesity , and lesser doses may be adequate with concurrent glycoprotein IIb/IIIa inhibition .

## Item bc5cdr:test:3602
Example input:
Sentence: Patient response was assessed using changes in CD4+ lymphocyte subset count , HIV p24 antigen , weight , and quality of life .

Example answer:
{"entities": []}

Example input:
Sentence: regular consumption of alcohol , liver failure is possible when therapeutic doses are ingested .

Example answer:
{"entities": [{"text": "alcohol", "type": "Chemical"}, {"text": "liver failure", "type": "Disease"}]}

Example input:
Sentence: In addition , working memory processing in ecstasy users has been shown to be associated with neural alterations in hippocampal and/or cortical regions as measured by functional magnetic resonance imaging ( fMRI ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : The septo-hippocampal cholinergic pathway has been implicated in epileptogenesis , and genetic factors influence the response to cholinergic agents , but limited data are available on cholinergic involvement in alcohol withdrawal severity .

Example answer:
{"entities": [{"text": "alcohol", "type": "Chemical"}]}

Example input:
Sentence: Only minor changes in CD4+ lymphocyte subset count were observed in AIDS patients , although a more significant rise occurred in those with earlier stages of disease .

Example answer:
{"entities": [{"text": "AIDS", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : A 72-year-old white man with underlying human immunodeficiency virus , atrial fibrillation , coronary artery disease , and hyperlipidemia presented with generalized pain , fatigue , and dark orange urine for 3 days .

Example answer:
{"entities": [{"text": "human immunodeficiency virus", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "coronary artery disease", "type": "Disease"}, {"text": "hyperlipidemia", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "fatigue", "type": "Disease"}]}

Example input:
Sentence: Seventy-five human immunodeficiency virus ( HIV ) -infected patients with CD4+ cell counts < 500/mm3 were randomized to receive either ZDV ( 500 mg daily ) alone ( group I , n = 38 ) or in combination with folinic acid ( 15 mg daily ) and intramascular vitamin B12 ( 1000 micrograms monthly ) ( group II , n = 37 ) .

Example answer:
{"entities": [{"text": "human immunodeficiency virus ( HIV ) -infected", "type": "Disease"}, {"text": "ZDV", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}, {"text": "vitamin B12", "type": "Chemical"}]}

Example input:
Sentence: In the present study , we have investigated the molecular mechanisms by which female hormones influence cholesterol metabolism in macrophages in response to the HIV protease inhibitor ritonavir .

Example answer:
{"entities": [{"text": "cholesterol", "type": "Chemical"}, {"text": "ritonavir", "type": "Chemical"}]}

Example input:
Sentence: The association remained after additional adjustment for diabetes , cholesterol level , systolic blood pressure , or alcohol use .

Example answer:
{"entities": [{"text": "diabetes", "type": "Disease"}, {"text": "cholesterol", "type": "Chemical"}, {"text": "alcohol", "type": "Chemical"}]}

Example input:
Sentence: Depressed mood was more common among patients and was associated with certain sexual difficulties , but not with impotence .

Example answer:
{"entities": [{"text": "Depressed mood", "type": "Disease"}, {"text": "impotence", "type": "Disease"}]}

Input:
Sentence: We evaluated the association of alcohol consumption and depression , and their effects on HIV disease progression among women with HIV .

## Item bc5cdr:test:3836
Example input:
Sentence: In addition , working memory processing in ecstasy users has been shown to be associated with neural alterations in hippocampal and/or cortical regions as measured by functional magnetic resonance imaging ( fMRI ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: METHOD : The response of 44 patients meeting DSM-IV criteria for bipolar disorder to naturalistic treatment was assessed for at least 6 weeks using the Montgomery-Asberg Depression Rating Scale and the Bech-Rafaelson Mania Rating Scale .

Example answer:
{"entities": [{"text": "bipolar disorder", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Methamphetamine is a very addictive , powerful stimulant that increases wakefulness and physical activity and can produce other effects such as cardiac dysrhythmias , hypertension , hallucinations , and violent behavior .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "Chemical"}, {"text": "cardiac dysrhythmias", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "hallucinations", "type": "Disease"}, {"text": "violent behavior", "type": "Disease"}]}

Example input:
Sentence: Methamphetamine ( 10 mg/kg sc ) , administered five times , reduced the levels of dopamine and its metabolites in striatal tissue when measured 72 h after the last injection .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: Neuroprotection rendered by MPEP may be associated with the reduction of the methamphetamine-induced dopamine efflux in the striatum due to the blockade of extrastriatal mGluR5 , and with a decrease in hyperthermia .

Example answer:
{"entities": [{"text": "MPEP", "type": "Chemical"}, {"text": "methamphetamine-induced", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "hyperthermia", "type": "Disease"}]}

Example input:
Sentence: A single MPEP ( 5 mg/kg ip ) injection reduced the basal extracellular dopamine level in the striatum , as well as dopamine release stimulated either by methamphetamine ( 10 mg/kg sc ) or by intrastriatally administered veratridine ( 100 microM ) .

Example answer:
{"entities": [{"text": "MPEP", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "veratridine", "type": "Chemical"}]}

Example input:
Sentence: The prolonged depletion of dopamine in the striatum in mice , given multiple injections of methamphetamine , was also antagonized dose-dependently and completely by LY274614 .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "LY274614", "type": "Chemical"}]}

Example input:
Sentence: This study aimed at investigating the potential antipsychotic-like properties of SSR103800 , with a particular focus on models of hyperactivity , involving either drug challenge ( ie , amphetamine and MK-801 ) or transgenic mice ( ie , NMDA Nr1 ( neo-/- ) and DAT ( -/- ) ) .

Example answer:
{"entities": [{"text": "SSR103800", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "MK-801", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}]}

Example input:
Sentence: Oral rehabilitation of patients using methamphetamine can be challenging .

Example answer:
{"entities": [{"text": "methamphetamine", "type": "Chemical"}]}

Example input:
Sentence: In recent years working memory deficits have been reported in users of MDMA ( 3,4-methylenedioxymethamphetamine , ecstasy ) .

Example answer:
{"entities": [{"text": "memory deficits", "type": "Disease"}, {"text": "MDMA", "type": "Chemical"}, {"text": "3,4-methylenedioxymethamphetamine", "type": "Chemical"}, {"text": "ecstasy", "type": "Chemical"}]}

Input:
Sentence: Patients with the diagnosis of methamphetamine based on DSM-IV were interviewed using the Mini International Neuropsychiatric Interview ( M.I.N.I . )

## Item bc5cdr:test:3616
Example input:
Sentence: Based on the finding that VPU and VPA could protect the animals against pilocarpine-induced seizure it is suggested that the reduction of inhibitory amino acid neurotransmitters was comparatively minor and offset by a pronounced reduction of glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: Investigation of mitochondrial involvement in the experimental model of epilepsy induced by pilocarpine .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: In vehicle-treated rats , status epilepticus caused pronounced neuronal damage in the piriform cortex comprising both pyramidal cells and interneurons .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "neuronal damage", "type": "Disease"}]}

Example input:
Sentence: We report QTLs identified using a B6 ( host ) x A/J ( donor ) CSS panel to localize genes involved in susceptibility to pilocarpine-induced seizures .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: QTLs for susceptibility to pilocarpine-induced seizures , a model of temporal lobe epilepsy , have not been reported , and CSS have not previously been used to localize seizure susceptibility genes .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: Pyrrolidine dithiocarbamate protects the piriform cortex in the pilocarpine status epilepticus model .

Example answer:
{"entities": [{"text": "Pyrrolidine dithiocarbamate", "type": "Chemical"}, {"text": "pilocarpine", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}]}

Example input:
Sentence: Infarcts in substantia nigra pars reticulata were evoked by prolonged pilocarpine-induced status epilepticus .

Example answer:
{"entities": [{"text": "Infarcts in substantia nigra pars reticulata", "type": "Disease"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}]}

Example input:
Sentence: In this study , we investigated whether increased generation of FR during status epilepticus would be sufficient to provoke abnormalities in mtDNA and in the expression and activity of cytochrome c oxidase ( CCO ) , complex IV of the respiratory chain , in the chronic phase of the pilocarpine model of temporal lobe epilepsy .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}, {"text": "temporal lobe epilepsy", "type": "Disease"}]}

Example input:
Sentence: Similar to rats , systemic pilocarpine injection causes status epilepticus ( SE ) and the eventual development of spontaneous seizures and mossy fiber sprouting in C57BL/6 and CD1 mice , but the physiological correlates of these events have not been identified in mice .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Input:
Sentence: In this work CCR2 and CCL2 expression were examined following status epilepticus ( SE ) induced by pilocarpine injection .

## Item bc5cdr:test:3853
Example input:
Sentence: Abnormal movements and deafness occurred only in rats treated during the preweaning period ; within this period the greatest sensitivities for these abnormalities occurred from 2 to 11-17 and 5 to 11 days of age , respectively , indicating that the cochlea is more sensitive to streptomycin than the site ( vestibular or central ) responsible for the dyskinesias .

Example answer:
{"entities": [{"text": "Abnormal movements", "type": "Disease"}, {"text": "deafness", "type": "Disease"}, {"text": "streptomycin", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: Striatal microglia expressing eGFP constitutively show morphological changes after METH that are characteristic of activation .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}]}

Example input:
Sentence: Repeated cerebral perfusion SPECT scans revealed decreased basal ganglia perfusion while the movement disorder was present , and a return to normal perfusion when the rabbit syndrome resolved .

Example answer:
{"entities": [{"text": "decreased basal ganglia perfusion", "type": "Disease"}, {"text": "movement disorder", "type": "Disease"}, {"text": "rabbit syndrome", "type": "Disease"}]}

Example input:
Sentence: Abnormal processing of somatosensory inputs in the central nervous system ( central sensitization ) is the mechanism accounting for the enhanced pain sensitivity in the skin surrounding tissue injury ( secondary hyperalgesia ) .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "tissue injury", "type": "Disease"}, {"text": "secondary hyperalgesia", "type": "Disease"}]}

Example input:
Sentence: Our findings indicate that beta2-adrenoceptor overstimulation during an early critical period results in microglial activation associated with innate neuroinflammatory pathways and behavioral abnormalities , similar to those described in autism .

Example answer:
{"entities": [{"text": "behavioral abnormalities", "type": "Disease"}, {"text": "autism", "type": "Disease"}]}

Example input:
Sentence: These data support the hypothesis that SE-induced mossy fiber sprouting and synaptic reorganization are relevant characteristics of seizure development in these murine strains , resembling rat models of human temporal lobe epilepsy .

Example answer:
{"entities": [{"text": "SE-induced", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}]}

Example input:
Sentence: In 24 patients with this complication , the marked slowing of motor nerve conduction velocity and the electromyographic changes imply mainly a demyelinating disorder .

Example answer:
{"entities": [{"text": "demyelinating disorder", "type": "Disease"}]}

Example input:
Sentence: Alterations in the structural elements of the BBB coexisted with marked lesions of neurons of the cerebellum ( Purkinje cells are earliest ) .

Example answer:
{"entities": []}

Example input:
Sentence: Abnormal brain responses to somatosensory stimuli have been found in patients with hyperalgesia as well as in normal subjects during experimental central sensitization .

Example answer:
{"entities": [{"text": "hyperalgesia", "type": "Disease"}]}

Example input:
Sentence: The rapid alternations of rigidity and the signs of dopaminergic activation observed in the animals of the AS/KS group might be due to rapid shifts in the predominance of various DA-innervated structures .

Example answer:
{"entities": [{"text": "rigidity", "type": "Disease"}]}

Input:
Sentence: These results suggest that alterations in cerebellar sensory processing function , occurring secondary to abnormal basal ganglia signals reaching it , may be an important element contributing to the maladaptive sensorimotor plasticity of M1 and the emergence of abnormal involuntary movements .

## Item bc5cdr:test:3387
Example input:
Sentence: Post hoc analyses indicated that efficacy was similar with asenapine and haloperidol ; greater contrasts were seen in AEs , especially extrapyramidal symptoms .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}, {"text": "extrapyramidal symptoms", "type": "Disease"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND/AIMS : Recently ribavirin has been found to inhibit angiogenesis and a number of angiogenesis inhibitors such as sunitinib and sorafenib have been found to cause acute hemolysis .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "sunitinib", "type": "Chemical"}, {"text": "sorafenib", "type": "Chemical"}, {"text": "hemolysis", "type": "Disease"}]}

Example input:
Sentence: METHODS : This was a multicenter , randomized , open-label study in adult smokers with heart disease , hypertension not controlled by medication , and/or diabetes mellitus .

Example answer:
{"entities": [{"text": "heart disease", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "diabetes mellitus", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND AND PURPOSE : The Intravenous Nimodipine West European Stroke Trial ( INWEST ) found a correlation between nimodipine-induced reduction in blood pressure ( BP ) and an unfavorable outcome in acute stroke .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "Chemical"}, {"text": "Stroke", "type": "Disease"}, {"text": "nimodipine-induced", "type": "Chemical"}, {"text": "reduction in blood pressure", "type": "Disease"}, {"text": "acute stroke", "type": "Disease"}]}

Example input:
Sentence: Clinical studies of pipe smokers and people using transdermal nicotine support the idea that toxins other than nicotine are the most important causes of acute cardiovascular events .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}]}

Example input:
Sentence: Acetylsalicylic acid , dipyridamole , and hydrocortisone all appear to have cardioprotective effects when tested in this model .

Example answer:
{"entities": [{"text": "Acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}]}

Example input:
Sentence: The ACTIVE-W ( Atrial Fibrillation Clopidogrel Trial with Irbesartan for Prevention of Vascular Events ) study has demonstrated that warfarin is superior to platelet therapy ( clopidogrel plus aspirin ) in the prevention af embolic events .

Example answer:
{"entities": [{"text": "Atrial Fibrillation", "type": "Disease"}, {"text": "Clopidogrel", "type": "Chemical"}, {"text": "Irbesartan", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}, {"text": "clopidogrel", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "embolic events", "type": "Disease"}]}

Example input:
Sentence: Overall , in high-risk patients , warfarin is superior to aspirin in preventing strokes , with a relative risk reduction of 36 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "strokes", "type": "Disease"}]}

Example input:
Sentence: Pooled data from trials comparing antithrombotic treatment with placebo have shown that warfarin reduces the risk of stroke by 62 % , and that aspirin alone reduces the risk by 22 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "stroke", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}]}

Input:
Sentence: STUDY SELECTION : English-language randomized , controlled trials ( RCTs ) ; case-control studies ; meta-analyses ; and systematic reviews of aspirin versus control for the primary prevention of cardiovascular disease ( CVD ) were selected to answer the following questions : Does aspirin decrease coronary heart events , strokes , death from coronary heart events or stroke , or all-cause mortality in adults without known CVD ?

## Item bc5cdr:test:3997
Example input:
Sentence: MDMA polydrug users show process-specific central executive impairments coupled with impaired social and emotional judgement processes .

Example answer:
{"entities": [{"text": "MDMA", "type": "Chemical"}, {"text": "impaired social and emotional judgement processes", "type": "Disease"}]}

Example input:
Sentence: A few minutes after administration of the drugs , they presented urticaria ( patients 1 and 2 ) and conjunctivitis ( patient 1 ) .

Example answer:
{"entities": [{"text": "urticaria", "type": "Disease"}, {"text": "conjunctivitis", "type": "Disease"}]}

Example input:
Sentence: Various ocular symptoms and findings caused by carboplatin toxicity were seen .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: The overall incidence of side effects and the frequency and severity of blurred vision , dry mouth , and drowsiness were significantly less with dothiepin than with amitriptyline .

Example answer:
{"entities": [{"text": "blurred vision", "type": "Disease"}, {"text": "dry mouth", "type": "Disease"}, {"text": "dothiepin", "type": "Chemical"}, {"text": "amitriptyline", "type": "Chemical"}]}

Example input:
Sentence: Fewer subjects reported adverse events following treatment with desipramine alone than when receiving desipramine with cinacalcet ( 33 versus 86 % ) , the most frequent of which ( nausea and headache ) have been reported for patients treated with either desipramine or cinacalcet .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}, {"text": "nausea", "type": "Disease"}, {"text": "headache", "type": "Disease"}]}

Example input:
Sentence: We prospectively evaluated the adverse reactions of apraclonidine in 20 normal volunteers by instilling a single drop of 1 % apraclonidine in their right eyes .

Example answer:
{"entities": [{"text": "apraclonidine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Currently accepted intravitreal antibiotic regimens may cause retinal toxicity and macular ischaemia .

Example answer:
{"entities": [{"text": "retinal toxicity", "type": "Disease"}, {"text": "ischaemia", "type": "Disease"}]}

Example input:
Sentence: Generally , carboplatin is said to have milder side effects than cisplatin , whose ocular and orbital toxicity are well known .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: The ocular hypotensive effects were statistically significant for apraclonidine-treated eyes throughout the study and also statistically significant for contralateral eyes from three hours after topical administration of 1 % apraclonidine .

Example answer:
{"entities": [{"text": "ocular hypotensive", "type": "Disease"}, {"text": "apraclonidine-treated", "type": "Chemical"}, {"text": "apraclonidine", "type": "Chemical"}]}

Example input:
Sentence: The ocular myasthenia associated with combination therapy of pegylated IFN alpha-2b and ribavirin for CHC is very rarely reported ; therefore , we present this case with a review of the various eye complications of IFN therapy .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "CHC", "type": "Disease"}, {"text": "IFN", "type": "Chemical"}]}

Input:
Sentence: This is especially relevant in multidrug therapy where more than one drug can cause a similar ocular adverse effect .

## Item bc5cdr:test:3752
Example input:
Sentence: These findings suggest that lowered serum prolactin levels in the early phase of bromocriptine treatment may result from an impaired secretion of prolactin due to decreasing numbers of cytoplasmic microtubules .

Example answer:
{"entities": [{"text": "bromocriptine", "type": "Chemical"}]}

Example input:
Sentence: Hypothalamic prolactin receptor messenger ribonucleic acid levels , prolactin signaling , and hyperprolactinemic inhibition of pulsatile luteinizing hormone secretion are dependent on estradiol .

Example answer:
{"entities": [{"text": "ribonucleic acid", "type": "Chemical"}, {"text": "hyperprolactinemic", "type": "Disease"}, {"text": "estradiol", "type": "Chemical"}]}

Example input:
Sentence: Iatrogenically induced intractable atrioventricular reentrant tachycardia after verapamil and catheter ablation in a patient with Wolff-Parkinson-White syndrome and idiopathic dilated cardiomyopathy .

Example answer:
{"entities": [{"text": "atrioventricular reentrant tachycardia", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "idiopathic dilated cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: These seven cases demonstrate that procainamide can produce an acquired prolonged Q-T syndrome with polymorphous ventricular tachycardia .

Example answer:
{"entities": [{"text": "procainamide", "type": "Chemical"}, {"text": "prolonged Q-T syndrome", "type": "Disease"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: The effects of varying the extracellular concentrations of Na and Ca ( [ Na ] o and [ Ca ] o ) on both , the spontaneous beating and the negative chronotropic action of verapamil , were studied in the isolated rat atria .

Example answer:
{"entities": [{"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: Dose-dependent bradycardia induced by verapamil was potentiated by LNa , LCa , and HCa .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: Possible mechanisms that involve a verapamil-related increase in platelet and/or vascular alpha 2-adrenoreceptor affinity for catecholamines are discussed .

Example answer:
{"entities": [{"text": "verapamil-related", "type": "Chemical"}, {"text": "catecholamines", "type": "Chemical"}]}

Example input:
Sentence: Hyperprolactinemia can reduce fertility and libido .

Example answer:
{"entities": [{"text": "Hyperprolactinemia", "type": "Disease"}]}

Example input:
Sentence: We first tested whether chronic hyperprolactinemia inhibited two neuroendocrine parameters necessary for female fertility : pulsatile LH secretion and the estrogen-induced LH surge .

Example answer:
{"entities": [{"text": "hyperprolactinemia", "type": "Disease"}, {"text": "estrogen-induced", "type": "Chemical"}]}

Example input:
Sentence: Chronic hyperprolactinemia induced by the dopamine antagonist sulpiride caused a 40 % reduction LH pulse frequency in ovariectomized rats , but only in the presence of chronic low levels of estradiol .

Example answer:
{"entities": [{"text": "hyperprolactinemia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "sulpiride", "type": "Chemical"}, {"text": "estradiol", "type": "Chemical"}]}

Input:
Sentence: Verapamil stimulation test in hyperprolactinemia : loss of prolactin response in anatomic or functional stalk effect .

## Item bc5cdr:test:3494
Example input:
Sentence: The finding of cocaine-induced vasoconstriction in segments of ( noninnervated ) human umbilical artery suggests that the presence or absence of intact innervation is not sufficient to explain the discrepant data involving the possibility of alpha-mediated effects .

Example answer:
{"entities": [{"text": "cocaine-induced", "type": "Chemical"}]}

Example input:
Sentence: With regard to spasm , the clinical findings are largely circumstantial , and the locus of cocaine-induced vasoconstriction remains speculative .

Example answer:
{"entities": [{"text": "spasm", "type": "Disease"}, {"text": "cocaine-induced", "type": "Chemical"}]}

Example input:
Sentence: Electrocardiographic evidence of myocardial injury in psychiatrically hospitalized cocaine abusers .

Example answer:
{"entities": [{"text": "myocardial injury", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: These data indicate that ( 1 ) the apparent incidence of stroke related to cocaine use is increasing ; ( 2 ) cocaine-associated stroke occurs primarily in young adults ; ( 3 ) stroke may follow any route of cocaine administration ; ( 4 ) stroke after cocaine use is frequently associated with intracranial aneurysms and arteriovenous malformations ; and ( 5 ) in cocaine-associated stroke , the frequency of intracranial hemorrhage exceeds that of cerebral infarction .

Example answer:
{"entities": [{"text": "stroke", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}, {"text": "cocaine-associated", "type": "Chemical"}, {"text": "intracranial aneurysms", "type": "Disease"}, {"text": "arteriovenous malformations", "type": "Disease"}, {"text": "intracranial hemorrhage", "type": "Disease"}, {"text": "cerebral infarction", "type": "Disease"}]}

Example input:
Sentence: Clinical and experimental data published to date suggest several possible mechanisms by which cocaine may result in acute myocardial infarction .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Cocaine related chest pain : are we seeing the tip of an iceberg ?

Example answer:
{"entities": [{"text": "Cocaine", "type": "Chemical"}, {"text": "chest pain", "type": "Disease"}]}

Example input:
Sentence: Eleven of the cocaine abusers and none of the controls had ECG evidence of significant myocardial injury defined as myocardial infarction , ischemia , and bundle branch block .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "myocardial injury", "type": "Disease"}, {"text": "myocardial infarction", "type": "Disease"}, {"text": "ischemia", "type": "Disease"}, {"text": "bundle branch block", "type": "Disease"}]}

Example input:
Sentence: The mechanism of chest pain related to cocaine use is discussed and treatment dilemmas are discussed .

Example answer:
{"entities": [{"text": "chest pain", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: In individuals with preexisting , high-grade coronary arterial narrowing , acute myocardial infarction may result from an increase in myocardial oxygen demand associated with cocaine-induced increase in rate-pressure product .

Example answer:
{"entities": [{"text": "acute myocardial infarction", "type": "Disease"}, {"text": "oxygen", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}]}

Example input:
Sentence: In particular , the tendency of cocaine to produce chest pain ought to be in the mind of the emergency nurse when faced with a young victim of chest pain who is otherwise at low risk .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "chest pain", "type": "Disease"}]}

Input:
Sentence: It is unclear whether a coronary CTA strategy would be efficacious in cocaine-associated chest pain , as coronary vasospasm may account for some of the ischemia .

## Item bc5cdr:test:3918
Example input:
Sentence: Treatment-related adverse events ( AEs ) occurred in 44 % and 52 % , 57 % , and 41 % of the asenapine at 5 and 10 mg BID , haloperidol , and placebo groups , respectively .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Moderate or severe adverse events were more common in subjects on clonidine ( 79.4 % versus 49.2 % ; p =.0006 ) but not associated with higher rates of early study withdrawal .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: There were 13 cases of adverse reactions ( 0.34 % ) , ten of which were mild reactions such as nausea , exanthema , urtication , itchiness , and urgency to defecate , and did not require treatment .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "exanthema", "type": "Disease"}, {"text": "urtication", "type": "Disease"}, {"text": "itchiness", "type": "Disease"}]}

Example input:
Sentence: Gastrointestinal bleed , seizures , infection , and acute renal failure were documented in seven ( 10 % ) , five ( 7.1 % ) , 26 ( 37.1 % ) , and seven ( 10 % ) patients , respectively .

Example answer:
{"entities": [{"text": "Gastrointestinal bleed", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "infection", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: During treatment , adverse cardiac effects were observed in 14 patients ( 18 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: This age group had an increased risk of myelosuppression .

Example answer:
{"entities": [{"text": "myelosuppression", "type": "Disease"}]}

Example input:
Sentence: The most common adverse events were nausea ( 17.2 % and 16.1 % ; 95 % CI , -3.7 to 6.0 ) , hiccups ( 10.7 % and 6.6 % ; 95 % CI , 0.5 to 7.8 ) , and headache ( 8.7 % and 9.9 % ; 95 % Cl , -5.0 to 2.6 ) .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "hiccups", "type": "Disease"}, {"text": "headache", "type": "Disease"}]}

Example input:
Sentence: Grade 3-4 adverse effects included myelosuppression , fatigue , somnolence/depressed mood , neuropathy and dyspnea .

Example answer:
{"entities": [{"text": "myelosuppression", "type": "Disease"}, {"text": "fatigue", "type": "Disease"}, {"text": "somnolence/depressed mood", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}, {"text": "dyspnea", "type": "Disease"}]}

Example input:
Sentence: Serious adverse events were reported in 11 and 13 patients in the respective groups .

Example answer:
{"entities": []}

Example input:
Sentence: Myelosuppression was more in patients with hepatic dysfunction .

Example answer:
{"entities": [{"text": "Myelosuppression", "type": "Disease"}, {"text": "hepatic dysfunction", "type": "Disease"}]}

Input:
Sentence: Adverse events were reported in 68.9 % of patients ( myelosuppression in 49.4 % ) and 12.7 % of patients needed hospitalization .

## Item bc5cdr:test:3732
Example input:
Sentence: Short-latency reflex responses were evoked in the masseter and temporalis muscles by a stretch device with different velocities and displacements before , during , and after the pain .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}]}

Example input:
Sentence: Although paralysis after magnesium administration has been described in patients with known myasthenia gravis , it has not previously been reported to be the initial or only manifestation of the disease .

Example answer:
{"entities": [{"text": "paralysis", "type": "Disease"}, {"text": "magnesium", "type": "Chemical"}, {"text": "myasthenia gravis", "type": "Disease"}]}

Example input:
Sentence: Anaesthetists ' nightmare : masseter spasm after induction in an undiagnosed case of myotonia congenita .

Example answer:
{"entities": [{"text": "masseter spasm", "type": "Disease"}, {"text": "myotonia congenita", "type": "Disease"}]}

Example input:
Sentence: The results suggest that rigidity , which is assumed to be due to an action of morphine in the striatum , can be antagonized by another process leading to dopaminergic activation in the striatum .

Example answer:
{"entities": [{"text": "rigidity", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: Laryngeal electromyography ( thyroarytenoid muscle ) showed ample denervation potentials .

Example answer:
{"entities": []}

Example input:
Sentence: Of the 20 animals that received subarachnoid injection of 2-chloroprocaine-CE seven ( 35 % ) developed hind-limb paralysis .

Example answer:
{"entities": [{"text": "2-chloroprocaine-CE", "type": "Chemical"}, {"text": "paralysis", "type": "Disease"}]}

Example input:
Sentence: Atracurium besylate , a short-acting benzylisoquinolinium NMBA that is eliminated independently of renal or hepatic function , has also been associated with persistent paralysis , but only when used with corticosteroids .

Example answer:
{"entities": [{"text": "Atracurium besylate", "type": "Chemical"}, {"text": "benzylisoquinolinium", "type": "Chemical"}, {"text": "paralysis", "type": "Disease"}]}

Example input:
Sentence: Persistent paralysis after prolonged use of atracurium in the absence of corticosteroids .

Example answer:
{"entities": [{"text": "paralysis", "type": "Disease"}, {"text": "atracurium", "type": "Chemical"}]}

Example input:
Sentence: Reports of persistent paralysis after the discontinuance of these drugs have most often involved aminosteroid-based NMBAs such as vecuronium bromide , especially when used in conjunction with corticosteroids .

Example answer:
{"entities": [{"text": "paralysis", "type": "Disease"}, {"text": "vecuronium bromide", "type": "Chemical"}]}

Example input:
Sentence: None of the animals that received bupivacaine , normal saline , or normal saline titrated to a pH 3.0 developed hind-limb paralysis .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}, {"text": "paralysis", "type": "Disease"}]}

Input:
Sentence: The likely mechanism of paralysis is diffusion of Botox around the muscular process of the arytenoid to the posterior cricoarytenoid muscles .

## Item bc5cdr:test:3721
Example input:
Sentence: Ten patients with PD and prominent dyskinesias had rTMS ( 1,800 pulses ; 1 Hz rate ) delivered over the motor cortex for 4 consecutive days twice , once real stimuli and once sham stimulation were used ; evaluations were done at the baseline and 1 day after the end of each of the treatment series .

Example answer:
{"entities": [{"text": "PD", "type": "Disease"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: We studied 20 patients receiving long-term carbonic anhydrase inhibitor treatment for periodic paralysis and myotonia .

Example answer:
{"entities": [{"text": "paralysis", "type": "Disease"}, {"text": "myotonia", "type": "Disease"}]}

Example input:
Sentence: Similarly , in patient diaries , although both treatments caused reduction in subjective dyskinesia scores during the days of intervention , the effect was sustained for 3 days after the intervention for the real rTMS only .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: When deferoxamine therapy was discontinued and serial studies were performed , audiograms in seven cases reverted to normal or near normal within two to three weeks , and nine of 13 patients with symptoms became asymptomatic .

Example answer:
{"entities": [{"text": "deferoxamine", "type": "Chemical"}]}

Example input:
Sentence: Haloperidol administration ( one dose of 12 mg/kg once a week s.c. ) for 4 weeks caused an increase in vacuous chewing , tongue protrusion and duration of facial twitching observed in four weekly evaluations .

Example answer:
{"entities": [{"text": "Haloperidol", "type": "Chemical"}]}

Example input:
Sentence: During an 18-month period of study 41 hemodialyzed patients receiving desferrioxamine ( 10-40 mg/kg BW/3 times weekly ) for the first time were monitored for detection of audiovisual toxicity .

Example answer:
{"entities": [{"text": "desferrioxamine", "type": "Chemical"}, {"text": "audiovisual toxicity", "type": "Disease"}]}

Example input:
Sentence: Amiodarone should be used with caution during long-term oral therapy in patients with or without clear intraventricular conduction defects .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "Chemical"}]}

Example input:
Sentence: These results suggest that spasm provocation tests , which use an intracoronary injection of a relatively low dose of methylergonovine , have a high sensitivity in variant angina and the vasoreactivity of the right coronary artery may be greater than that of the other coronary arteries .

Example answer:
{"entities": [{"text": "spasm", "type": "Disease"}, {"text": "methylergonovine", "type": "Chemical"}, {"text": "variant angina", "type": "Disease"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: We report an undiagnosed case of myotonia congenita in a 24-year-old previously healthy primigravida , who developed life threatening masseter spasm following a standard dose of intravenous suxamethonium for induction of anaesthesia .

Example answer:
{"entities": [{"text": "myotonia congenita", "type": "Disease"}, {"text": "masseter spasm", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Input:
Sentence: METHODS : Patients that received Botox injections for spasmodic dysphonia between January 2000 and October 2009 were evaluated .

## Item bc5cdr:test:3804
Example input:
Sentence: Compared with control patients , CRF and ESRD patients had higher preoperative serum creatinine levels , a greater percentage of patients with hepatorenal syndrome , higher percentage requirement for dialysis in the first 3 months postoperatively , and a higher 1-year serum creatinine .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "hepatorenal syndrome", "type": "Disease"}]}

Example input:
Sentence: Nine days later the patient 's creatine kinase had dropped to 1695 U/L and creatinine was 3.3 mg/dL .

Example answer:
{"entities": [{"text": "creatine", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: A patient with cryptogenic cirrhosis and disseminated sporotrichosis developed acute renal failure immediately following the administration of amphotericin B on four separate occasions .

Example answer:
{"entities": [{"text": "cirrhosis", "type": "Disease"}, {"text": "sporotrichosis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}]}

Example input:
Sentence: Mean serum creatinine level before conversion was 2.21 mg/dL and thereafter , 4.93 mg/dL ( P = .02 ) .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: Serum creatinine values did not change significantly : 1.98 +/- 0.8 mg/dL before SRL therapy and 2.53 +/- 1.9 mg/dL at last follow-up ( P = .14 ) .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: Two patients developed acute tubular necrosis , characterized clinically by acute oliguric renal failure , while they were receiving a combination of cephalothin sodium and gentamicin sulfate therapy .

Example answer:
{"entities": [{"text": "acute tubular necrosis", "type": "Disease"}, {"text": "cephalothin sodium", "type": "Chemical"}, {"text": "gentamicin sulfate", "type": "Chemical"}]}

Example input:
Sentence: Serum creatinine ( SCr ) levels and estimated glomerular filtration rate were assessed at baseline and 2 to 5 days after receiving medications .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: We report a case of ranitidine-induced acute interstitial nephritis in a recipient of a cadaveric renal allograft presenting with acute allograft dysfunction within 48 hours of exposure to the drug .

Example answer:
{"entities": [{"text": "ranitidine-induced", "type": "Chemical"}, {"text": "interstitial nephritis", "type": "Disease"}]}

Example input:
Sentence: The amount of daily urinary protein decreased from 15.6 to 2.8 g. Within 14 days of the oral bisphosphonate ( alendronate sodium ) administration , the amount of daily urinary protein increased rapidly up to 12.8 g with acute renal failure .

Example answer:
{"entities": [{"text": "bisphosphonate", "type": "Chemical"}, {"text": "alendronate sodium", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: Patients who developed renal insufficiency had lower baseline body weight and higher baseline serum creatinine , required higher doses of loop diuretics , and were more likely to be treated with thiazide diuretics than controls .

Example answer:
{"entities": [{"text": "renal insufficiency", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "thiazide", "type": "Chemical"}]}

Input:
Sentence: On day 8 , the patient developed acute renal failure ( serum creatinine 1.9 mg/dL , increased from 1.2 mg/dL the previous day and 0.8 mg/dL on admission ) .

## Item bc5cdr:test:3823
Example input:
Sentence: Kindled seizures were induced by daily administration of 60 mg/kg cocaine for 5 days .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: The frequency of sound-induced seizures after 12.5 or 25 mg/kg caffeine was reduced from 50 to 5 % by acetaminophen .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}]}

Example input:
Sentence: In the absence of caffeine , acetaminophen ( up to 300 mg/kg ) did not modify the seizures induced by maximal electroshock and did not alter the convulsant dose of pentylenetetrezol in mice ( tests performed by the Anticonvulsant Screening Project of NINCDS ) .

Example answer:
{"entities": [{"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "pentylenetetrezol", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Sensitivity to several convulsion endpoints induced by nicotine , carbachol , and neostigmine were significantly greater in WSR versus WSP mice .

Example answer:
{"entities": [{"text": "convulsion", "type": "Disease"}, {"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}]}

Example input:
Sentence: Apamin ( 10 ng ) had a tendency to decrease the convulsive threshold ( 21.6 +/- 2.2 to 19.9 +/- 2.5 mg. l ( -1 ) ) but this was not statistically significant .

Example answer:
{"entities": [{"text": "Apamin", "type": "Chemical"}, {"text": "convulsive", "type": "Disease"}]}

Example input:
Sentence: The convulsive threshold ( mean +/- SD ) was 41.4 +/- 6.5 mg. l ( -1 ) with lidocaine infusion ( 6 mg.kg ( -1 ) .min ( -1 ) ) , increasing significantly to 66.6 +/- 10.9 mg. l ( -1 ) when the end-tidal concentration of sevoflurane was 0.8 % .

Example answer:
{"entities": [{"text": "convulsive", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}, {"text": "sevoflurane", "type": "Chemical"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Evidence is accumulating that lindane can be toxic to the central nervous system and may be associated with aplastic anaemia .

Example answer:
{"entities": [{"text": "lindane", "type": "Chemical"}, {"text": "toxic to the central nervous system", "type": "Disease"}, {"text": "aplastic anaemia", "type": "Disease"}]}

Example input:
Sentence: Differential effects of gamma-hexachlorocyclohexane ( lindane ) on pharmacologically-induced seizures .

Example answer:
{"entities": [{"text": "gamma-hexachlorocyclohexane", "type": "Chemical"}, {"text": "lindane", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Gamma-hexachlorocyclohexane ( gamma-HCH ) , the active ingredient of the insecticide lindane , has been shown to decrease seizure threshold to pentylenetrazol ( PTZ ) 3 h after exposure to gamma-HCH and conversely increase threshold to PTZ-induced seizures 24 h after exposure to gamma-HCH ( Vohland et al .

Example answer:
{"entities": [{"text": "Gamma-hexachlorocyclohexane", "type": "Chemical"}, {"text": "gamma-HCH", "type": "Chemical"}, {"text": "lindane", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "PTZ", "type": "Chemical"}, {"text": "PTZ-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Input:
Sentence: decreased convulsion incidence and severity and prolonged latency time to convulsion following injection with a convulsive dose of lindane ( 8 mg/kg , i.p . ) .

## Item bc5cdr:test:3718
Example input:
Sentence: Minor side effects included nausea ( thirteen patients ) , emesis ( eight of the thirteen patients with nausea ) , clumsiness ( evident as ataxic movements in ten patients ) , and dysphoric reaction ( one patient ) .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "emesis", "type": "Disease"}, {"text": "clumsiness", "type": "Disease"}, {"text": "ataxic movements", "type": "Disease"}, {"text": "dysphoric reaction", "type": "Disease"}]}

Example input:
Sentence: Less frequent toxic effects included thrombocytopenia , anemia , nausea , mild alopecia , phlebitis , and mucositis .

Example answer:
{"entities": [{"text": "thrombocytopenia", "type": "Disease"}, {"text": "anemia", "type": "Disease"}, {"text": "nausea", "type": "Disease"}, {"text": "alopecia", "type": "Disease"}, {"text": "phlebitis", "type": "Disease"}, {"text": "mucositis", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Minutes after oral administration , the patient developed nausea , sweating and hypotension , and finally collapsed .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Various reported side effects of fentanyl administration include chest wall rigidity , hypotension , respiratory depression , and bradycardia .

Example answer:
{"entities": [{"text": "fentanyl", "type": "Chemical"}, {"text": "chest wall rigidity", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}, {"text": "respiratory depression", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: The most common adverse events ( incidence > or = 5 % in one group ) after rizatriptan and ergotamine/caffeine , respectively , were dizziness ( 6.7 and 5.3 % ) , nausea ( 4.2 and 8.5 % ) and somnolence ( 5.5 and 2.3 % ) .

Example answer:
{"entities": [{"text": "rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}, {"text": "dizziness", "type": "Disease"}, {"text": "nausea", "type": "Disease"}, {"text": "somnolence", "type": "Disease"}]}

Example input:
Sentence: Conventional agents are associated with unwanted central nervous system effects , including extrapyramidal symptoms ( EPS ) , tardive dyskinesia , sedation , and possible impairment of some cognitive measures , as well as cardiac effects , orthostatic hypotension , hepatic changes , anticholinergic side effects , sexual dysfunction , and weight gain .

Example answer:
{"entities": [{"text": "extrapyramidal symptoms", "type": "Disease"}, {"text": "EPS", "type": "Disease"}, {"text": "tardive dyskinesia", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}]}

Example input:
Sentence: In less than 1 hour after the ingestion of alcohol , he developed malaise with flushing of the face , tachycardia , and dyspnea .

Example answer:
{"entities": [{"text": "alcohol", "type": "Chemical"}, {"text": "flushing of the face", "type": "Disease"}, {"text": "tachycardia", "type": "Disease"}, {"text": "dyspnea", "type": "Disease"}]}

Example input:
Sentence: The most common adverse events were nausea ( 17.2 % and 16.1 % ; 95 % CI , -3.7 to 6.0 ) , hiccups ( 10.7 % and 6.6 % ; 95 % CI , 0.5 to 7.8 ) , and headache ( 8.7 % and 9.9 % ; 95 % Cl , -5.0 to 2.6 ) .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "hiccups", "type": "Disease"}, {"text": "headache", "type": "Disease"}]}

Example input:
Sentence: Other possible adverse effects -- such as gastrointestinal disorders , orthostatic hypotension , levodopa-induced psychosis , sleep disturbances or parasomnias , or drug interactions -- also require carefully monitored individual treatment .

Example answer:
{"entities": [{"text": "gastrointestinal disorders", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "levodopa-induced", "type": "Chemical"}, {"text": "psychosis", "type": "Disease"}, {"text": "sleep disturbances", "type": "Disease"}, {"text": "parasomnias", "type": "Disease"}]}

Example input:
Sentence: Grade 3-4 adverse effects included myelosuppression , fatigue , somnolence/depressed mood , neuropathy and dyspnea .

Example answer:
{"entities": [{"text": "myelosuppression", "type": "Disease"}, {"text": "fatigue", "type": "Disease"}, {"text": "somnolence/depressed mood", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}, {"text": "dyspnea", "type": "Disease"}]}

Input:
Sentence: Reported adverse effects include a period of breathiness , throat pain , and difficulty with swallowing liquids .

## Item bc5cdr:test:3301
Example input:
Sentence: In conclusion , reductions in creatinine clearance and renal amphotericin B accumulation after chronic amphotericin B administration were enhanced by salt depletion and attenuated by sodium loading in rats .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "amphotericin B", "type": "Chemical"}, {"text": "sodium", "type": "Chemical"}]}

Example input:
Sentence: Therefore , we studied the predictive effect of renal ACE activity for the severity of renal damage induced by a single injection of adriamycin in rats .

Example answer:
{"entities": [{"text": "renal damage", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}]}

Example input:
Sentence: Effects of an inhibitor of angiotensin converting enzyme ( Captopril ) on pulmonary and renal insufficiency due to intravascular coagulation in the rat .

Example answer:
{"entities": [{"text": "angiotensin", "type": "Chemical"}, {"text": "Captopril", "type": "Chemical"}, {"text": "intravascular coagulation", "type": "Disease"}]}

Example input:
Sentence: Rats were given a single dose of adriamycin and one month later divided into four groups matched for albuminuria , blood pressure , and plasma albumin concentration .

Example answer:
{"entities": [{"text": "adriamycin", "type": "Chemical"}, {"text": "albuminuria", "type": "Disease"}]}

Example input:
Sentence: Six weeks after clipping of one renal artery , hypertensive rats ( 178 +/- 4 mm Hg ) were randomly assigned to three groups : untreated hypertensive controls ( n = 8 ) , enalapril-treated ( n = 8 ) , or nitrendipine-treated ( n = 10 ) .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}, {"text": "enalapril-treated", "type": "Chemical"}, {"text": "nitrendipine-treated", "type": "Chemical"}]}

Example input:
Sentence: Groups 3 and 4 were studied at four and at six months to assess the effect of enalapril on progression of renal injury in adriamycin nephrosis .

Example answer:
{"entities": [{"text": "enalapril", "type": "Chemical"}, {"text": "renal injury", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: This case report highlights the fact that the angiotensin II receptor antagonist losartan can cause serious unexpected complications in patients with renovascular disease and should be used with extreme caution in this setting .

Example answer:
{"entities": [{"text": "angiotensin II", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "renovascular disease", "type": "Disease"}]}

Example input:
Sentence: The effect of a 6-week treatment with the calcium channel blocker nitrendipine or the angiotensin converting enzyme inhibitor enalapril on blood pressure , albuminuria , renal hemodynamics , and morphology of the nonclipped kidney was studied in rats with two-kidney , one clip renovascular hypertension .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "nitrendipine", "type": "Chemical"}, {"text": "angiotensin", "type": "Chemical"}, {"text": "enalapril", "type": "Chemical"}, {"text": "albuminuria", "type": "Disease"}, {"text": "renovascular hypertension", "type": "Disease"}]}

Example input:
Sentence: Under such conditions , angiotensin II receptor blockade by losartan probably induced a critical fall in glomerular filtration pressure .

Example answer:
{"entities": [{"text": "angiotensin II", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Input:
Sentence: BACKGROUND : The aim of the study was to investigate the antihypertensive effects of angiotensin II type-1 receptor blocker , losartan , and its potential in slowing down renal disease progression in spontaneously hypertensive rats ( SHR ) with adriamycin ( ADR ) nephropathy .

## Item bc5cdr:test:3789
Example input:
Sentence: She subsequently died some 5 weeks after the commencement of her drug therapy.Post-mortem examination showed evidence of massive hepatocellular necrosis , acute hypersensitivity myocarditis , focal acute tubulo-interstitial nephritis and extensive bone marrow necrosis , with no evidence of malignancy .

Example answer:
{"entities": [{"text": "massive hepatocellular necrosis", "type": "Disease"}, {"text": "myocarditis", "type": "Disease"}, {"text": "nephritis", "type": "Disease"}, {"text": "bone marrow necrosis", "type": "Disease"}, {"text": "malignancy", "type": "Disease"}]}

Example input:
Sentence: After detailing the course of events , we discuss the role of paradoxical coronary spasm and hypotension-mediated myocardial ischemia occurring downstream to significant coronary arterial stenosis in the pathophysiology of acute coronary insufficiency .

Example answer:
{"entities": [{"text": "spasm", "type": "Disease"}, {"text": "hypotension-mediated", "type": "Disease"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "coronary arterial stenosis", "type": "Disease"}, {"text": "acute coronary insufficiency", "type": "Disease"}]}

Example input:
Sentence: Iatrogenically induced intractable atrioventricular reentrant tachycardia after verapamil and catheter ablation in a patient with Wolff-Parkinson-White syndrome and idiopathic dilated cardiomyopathy .

Example answer:
{"entities": [{"text": "atrioventricular reentrant tachycardia", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "idiopathic dilated cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: Further signs were hyperhidrosis , hypersalivation , bronchorrhoea , and severe miosis ; the electrocardiographic finding was atrio-ventricular dissociation .

Example answer:
{"entities": [{"text": "hyperhidrosis", "type": "Disease"}, {"text": "hypersalivation", "type": "Disease"}, {"text": "bronchorrhoea", "type": "Disease"}, {"text": "miosis", "type": "Disease"}, {"text": "atrio-ventricular dissociation", "type": "Disease"}]}

Example input:
Sentence: Severe reversible left ventricular systolic and diastolic dysfunction due to accidental iatrogenic epinephrine overdose .

Example answer:
{"entities": [{"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "epinephrine", "type": "Chemical"}, {"text": "overdose", "type": "Disease"}]}

Example input:
Sentence: In this report we describe the case of a 37-year-old white woman with Ebstein 's anomaly , who developed a rare syndrome called platypnea-orthodeoxia , characterized by massive right-to-left interatrial shunting with transient profound hypoxia and cyanosis .

Example answer:
{"entities": [{"text": "Ebstein 's anomaly", "type": "Disease"}, {"text": "platypnea-orthodeoxia", "type": "Disease"}, {"text": "hypoxia", "type": "Disease"}, {"text": "cyanosis", "type": "Disease"}]}

Example input:
Sentence: We describe a 25-year-old woman with pre-existing mitral valve prolapse who developed intractable ventricular fibrillation after consuming a `` natural energy '' guarana health drink containing a high concentration of caffeine .

Example answer:
{"entities": [{"text": "mitral valve prolapse", "type": "Disease"}, {"text": "ventricular fibrillation", "type": "Disease"}, {"text": "caffeine", "type": "Chemical"}]}

Example input:
Sentence: He was hospitalized for a myocardial infarction with pulmonary edema , treated with high-dose diuretics .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "pulmonary edema", "type": "Disease"}]}

Example input:
Sentence: The present report describes a case of cardiac arrest and subsequent death as a result of hyperkalaemia following the use of suxamethonium in a 23-year-old Malawian woman .

Example answer:
{"entities": [{"text": "cardiac arrest", "type": "Disease"}, {"text": "death", "type": "Disease"}, {"text": "hyperkalaemia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Input:
Sentence: This case is a good example of electrolyte imbalance causing acute life-threatening cardiac events .
