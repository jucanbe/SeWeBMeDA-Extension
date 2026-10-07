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

## Item bc5cdr:test:1692
Example input:
Sentence: All concentrations of nicotine sulfate caused some lethality but a no effect level for coniine lethality was 0.75 % .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "coniine", "type": "Chemical"}]}

Example input:
Sentence: Using as the reference group women who were not using oral contraception , had no recent pregnancy or menopausal symptoms , the case-control analysis gave an adjusted odds ratio ( OR ( adj ) ) of 7.44 ( 95 % CI 3.67-15.08 ) for CPA/EE use compared with an OR ( adj ) of 2.58 ( 95 % CI 1.60-4.18 ) for use of conventional COCs .

Example answer:
{"entities": [{"text": "CPA/EE", "type": "Chemical"}]}

Example input:
Sentence: Finally , 15 patients were excluded from the study ( noncompliance 14 , death 1 ) ; thus , 60 patients ( 31 in group I and 29 in group II ) were eligible for analysis .

Example answer:
{"entities": [{"text": "death", "type": "Disease"}]}

Example input:
Sentence: No other risk factors for CNS toxicity were identified .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Because of the rapid systemic clearance of BCNU ( 1,3-bis- ( 2-chloroethyl ) -1-nitrosourea ) , intra-arterial administration should provide a substantial advantage over intravenous administration for the treatment of malignant gliomas .

Example answer:
{"entities": [{"text": "BCNU", "type": "Chemical"}, {"text": "1,3-bis- ( 2-chloroethyl ) -1-nitrosourea", "type": "Chemical"}, {"text": "malignant gliomas", "type": "Disease"}]}

Example input:
Sentence: RESULTS : The age-adjusted incidence rate ratio for CPA/EE versus conventional COCs was 2.20 [ 95 % confidence interval ( CI ) 1.35-3.58 ] .

Example answer:
{"entities": [{"text": "CPA/EE", "type": "Chemical"}]}

Example input:
Sentence: These findings suggest that NRA0160 may have unique antipsychotic activities without the liability of motor side effects typical of classical antipsychotics .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}]}

Example input:
Sentence: NRA0160 and clozapine antagonized MAP-induced stereotyped behavior in mice , although their effects did not exceed 50 % inhibition , even at the highest dose given .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "MAP-induced", "type": "Chemical"}]}

Example input:
Sentence: Subjects were 1210 inpatients with New York Heart Association ( NYHA ) functional class II and III .

Example answer:
{"entities": []}

Example input:
Sentence: 16 , 95 % CI 1.02 to 101.74 ) and death alone ( n/N=9/26 , OR 4.336 , 95 % CI 1.131 16.619 ) compared with all placebo patients ( n/N=62/92 and 14/92 , respectively ) .

Example answer:
{"entities": [{"text": "death", "type": "Disease"}]}

Input:
Sentence: We conclude that CNA and INA demonstrated similar profiles with regard to safety , morbidity , and mortality .

## Item bc5cdr:test:1683
Example input:
Sentence: BACKGROUND : Electrocardiography has a very low sensitivity in detecting dobutamine-induced myocardial ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}]}

Example input:
Sentence: d-1 given for 4 weeks , elevated blood pressure from 102+/-13 to 152+/-15 mm Hg and increased the synthesis of ET-1 and the levels of ET-1 mRNA in the mesenteric artery ( 240 % and 230 % , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: These results suggest that hypertension after chronic intrarenal noradrenaline infusion is produced by relatively higher levels of circulating noradrenaline and by triggering of an additional intrarenal pressor mechanism .

Example answer:
{"entities": [{"text": "hypertension", "type": "Disease"}, {"text": "noradrenaline", "type": "Chemical"}]}

Example input:
Sentence: Nimodipine treatment resulted in a statistically significant reduction in systolic BP ( SBP ) and diastolic BP ( DBP ) from baseline compared with placebo during the first few days .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "Chemical"}, {"text": "reduction in systolic BP", "type": "Disease"}]}

Example input:
Sentence: The most important findings were that compared with values in control subjects , end-systolic left ventricular posterior wall dimension and percent of left ventricular posterior wall thickening in doxorubicin-treated patients were decreased at baseline study and these findings were more clearly delineated with dobutamine stimulation .

Example answer:
{"entities": [{"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}]}

Example input:
Sentence: In addition , reflex bradycardia caused by injected norepinephrine was significantly enhanced by L-dopa , DL-Threo-dihydroxyphenylserine had no effect on blood pressure , heart rate or reflex responses to norepinephrine .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}, {"text": "DL-Threo-dihydroxyphenylserine", "type": "Chemical"}]}

Example input:
Sentence: Dobutamine infusion at 10 micrograms/kg per min was discontinued after six studies secondary to a 50 % incidence rate of adverse symptoms .

Example answer:
{"entities": [{"text": "Dobutamine", "type": "Chemical"}]}

Example input:
Sentence: Dobutamine stress echocardiography : a sensitive indicator of diminished myocardial function in asymptomatic doxorubicin-treated long-term survivors of childhood cancer .

Example answer:
{"entities": [{"text": "Dobutamine", "type": "Chemical"}, {"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: To develop a more sensitive echocardiographic screening test for cardiac damage due to doxorubicin , a cohort study was performed using dobutamine infusion to differentiate asymptomatic long-term survivors of childhood cancer treated with doxorubicin from healthy control subjects .

Example answer:
{"entities": [{"text": "cardiac damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: The increase in dP/dtejc during infusion of dobutamine in this group was severely impaired as compared to the non-ischemic group .

Example answer:
{"entities": [{"text": "dobutamine", "type": "Chemical"}]}

Input:
Sentence: Patients with this response more often had a history of hypertension and had higher resting systolic and diastolic BP before dobutamine infusion .

## Item bc5cdr:test:1682
Example input:
Sentence: d-1 given for 4 weeks , elevated blood pressure from 102+/-13 to 152+/-15 mm Hg and increased the synthesis of ET-1 and the levels of ET-1 mRNA in the mesenteric artery ( 240 % and 230 % , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: To develop a more sensitive echocardiographic screening test for cardiac damage due to doxorubicin , a cohort study was performed using dobutamine infusion to differentiate asymptomatic long-term survivors of childhood cancer treated with doxorubicin from healthy control subjects .

Example answer:
{"entities": [{"text": "cardiac damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: Dobutamine infusion at 10 micrograms/kg per min was discontinued after six studies secondary to a 50 % incidence rate of adverse symptoms .

Example answer:
{"entities": [{"text": "Dobutamine", "type": "Chemical"}]}

Example input:
Sentence: End-systolic left ventricular posterior wall dimension at the 5-micrograms/kg per min dobutamine infusion for the doxorubicin-treated group was 14.1 +/- 2.4 mm versus 19.3 +/- 2.6 mm for control subjects ( p less than 0.01 ) .

Example answer:
{"entities": [{"text": "dobutamine", "type": "Chemical"}, {"text": "doxorubicin-treated", "type": "Chemical"}]}

Example input:
Sentence: The most important findings were that compared with values in control subjects , end-systolic left ventricular posterior wall dimension and percent of left ventricular posterior wall thickening in doxorubicin-treated patients were decreased at baseline study and these findings were more clearly delineated with dobutamine stimulation .

Example answer:
{"entities": [{"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}]}

Example input:
Sentence: METHODS : The study group comprised 40 patients undergoing Sestamibi-SPECT/dobutamine stress test .

Example answer:
{"entities": [{"text": "Sestamibi-SPECT/dobutamine", "type": "Chemical"}]}

Example input:
Sentence: Transient hypotension ( SAP < 90mmHg ) occurred in 1 patient ( 0.7 % ) .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: On hospital admission , blood pressure of the intubated , bradyarrhythmic patient was 100/65 mmHg .

Example answer:
{"entities": []}

Example input:
Sentence: Systolic blood pressure was elevated by an average of 7 mm Hg .

Example answer:
{"entities": []}

Example input:
Sentence: Dobutamine stress echocardiography : a sensitive indicator of diminished myocardial function in asymptomatic doxorubicin-treated long-term survivors of childhood cancer .

Example answer:
{"entities": [{"text": "Dobutamine", "type": "Chemical"}, {"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Input:
Sentence: Among 3,129 dobutamine stress echocardiographic studies , a hypertensive response , defined as systolic blood pressure ( BP ) > or = 220 mm Hg and/or diastolic BP > or = 110 mm Hg , occurred in 30 patients ( 1 % ) .

## Item bc5cdr:test:1491
Example input:
Sentence: Its occurrence in a patient being treated with imipramine is described , representing the first reported case of this syndrome in conjunction with antidepressants .

Example answer:
{"entities": [{"text": "imipramine", "type": "Chemical"}, {"text": "antidepressants", "type": "Chemical"}]}

Example input:
Sentence: Reversible inferior colliculus lesion in metronidazole-induced encephalopathy : magnetic resonance findings on diffusion-weighted and fluid attenuated inversion recovery imaging .

Example answer:
{"entities": [{"text": "inferior colliculus lesion", "type": "Disease"}, {"text": "metronidazole-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: In six of the probable cases the neurological disturbance consisted of an acute reversible encephalopathy usually related to the ingestion of a high dose of clioquinol over a short period .

Example answer:
{"entities": [{"text": "neurological disturbance", "type": "Disease"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "clioquinol", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Reversible inferior colliculus lesions could be considered as the characteristic for metronidazole-induced encephalopathy , next to the dentate nucleus involvement .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "Disease"}, {"text": "metronidazole-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: This was a case of acute palsy of the recurrent laryngeal nerve and superimposed severe acute sensorimotor axonal polyneuropathy caused by high-dose disulfiram intoxication .

Example answer:
{"entities": [{"text": "palsy", "type": "Disease"}, {"text": "polyneuropathy", "type": "Disease"}, {"text": "disulfiram", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVE : This is to present reversible inferior colliculus lesions in metronidazole-induced encephalopathy , to focus on the diffusion-weighted imaging ( DWI ) and fluid attenuated inversion recovery ( FLAIR ) imaging .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "Disease"}, {"text": "metronidazole-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: We observed sinoatrial block due to chronic amiodarone administration in a 5-year-old boy with primary cardiomyopathy , Wolff-Parkinson-White syndrome and supraventricular tachycardia .

Example answer:
{"entities": [{"text": "sinoatrial block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "primary cardiomyopathy", "type": "Disease"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "supraventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: We report a favorable response to treatment with citalopram by a 15-year-old boy with major depression who exhibited palpebral twitching during his first 2 weeks of treatment .

Example answer:
{"entities": [{"text": "citalopram", "type": "Chemical"}, {"text": "major depression", "type": "Disease"}, {"text": "palpebral twitching", "type": "Disease"}]}

Example input:
Sentence: Dothiepin and amitriptyline were equally effective in alleviating the symptoms of depressive illness , and both were significantly superior to placebo .

Example answer:
{"entities": [{"text": "Dothiepin", "type": "Chemical"}, {"text": "amitriptyline", "type": "Chemical"}, {"text": "depressive illness", "type": "Disease"}]}

Example input:
Sentence: In a 6-week double-blind parallel treatment study , dothiepin and amitriptyline were compared to placebo in the treatment of 33 depressed outpatients .

Example answer:
{"entities": [{"text": "dothiepin", "type": "Chemical"}, {"text": "amitriptyline", "type": "Chemical"}, {"text": "depressed", "type": "Disease"}]}

Input:
Sentence: This report describes a case of encephalopathy developed in the course of amitriptyline therapy , during a remission of unipolar depression .

## Item bc5cdr:test:1887
Example input:
Sentence: Associated factors were co-treatment with other centrally antimuscarinic agents , poor clinical outcome , older age , and longer hospitalization ( by 17.5 days , increasing cost ) ; sex , diagnosis or medical co-morbidity , and daily clozapine dose , which fell with age , were unrelated .

Example answer:
{"entities": [{"text": "clozapine", "type": "Chemical"}]}

Example input:
Sentence: Using functional imaging and a face-learning task , we investigated neural correlates of encoding and recalling face-name associations in 20 recreational drug users whose predominant drug use was ecstasy and 20 controls .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: No association was found with other pretreatment characteristics .

Example answer:
{"entities": []}

Example input:
Sentence: administration were apparent earlier and sometimes lasted longer than those following oral administration .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSIONS : Long-term use and concomitant use of more than one BZD/RD were common in elderly patients hospitalised because of acute illnesses .

Example answer:
{"entities": []}

Example input:
Sentence: Long-term use was associated with daytime and night-time symptoms indicative of poorer health and potentially caused by the adverse effects of these drugs .

Example answer:
{"entities": []}

Example input:
Sentence: The association remained after additional adjustment for diabetes , cholesterol level , systolic blood pressure , or alcohol use .

Example answer:
{"entities": [{"text": "diabetes", "type": "Disease"}, {"text": "cholesterol", "type": "Chemical"}, {"text": "alcohol", "type": "Chemical"}]}

Example input:
Sentence: Treatment duration longer than 1 year was associated with an eightfold increased risk ( OR = 7.7 , 95 % CI 0.9 to 69 ) .

Example answer:
{"entities": []}

Example input:
Sentence: No association was found for hormone use less than 1 year .

Example answer:
{"entities": []}

Example input:
Sentence: Correlation with rating recall after one week was best when first-time ratings were requested as late as one day after injection ( R ( 2 ) =0.79 ) indicating that both rating retrievals utilized similar memory traces .

Example answer:
{"entities": []}

Input:
Sentence: The association was stronger with longer duration of use when compared to shorter duration of use and was more pronounced in recent users than in remote users .

## Item bc5cdr:test:1623
Example input:
Sentence: glycopyrrolate and atropine in the prevention of bradycardia and arrhythmias following repeated doses of suxamethonium in children .

Example answer:
{"entities": [{"text": "glycopyrrolate", "type": "Chemical"}, {"text": "atropine", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "arrhythmias", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: A patient with sinuatrial disease and implanted pacemaker was treated with amiodarone ( maximum dose 1000 mg , maintenance dose 800 mg daily ) for 10 months , for control of supraventricular tachyarrhythmias .

Example answer:
{"entities": [{"text": "sinuatrial disease", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "supraventricular tachyarrhythmias", "type": "Disease"}]}

Example input:
Sentence: It has been shown that bromocriptine-induced tachycardia , which persisted after adrenalectomy , is ( i ) mediated by central dopamine D2 receptor activation and ( ii ) reduced by 5-day isoproterenol pretreatment , supporting therefore the hypothesis that this effect is dependent on sympathetic outflow to the heart .

Example answer:
{"entities": [{"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: In four patients , polymorphous ventricular tachycardia appeared after intravenous administration of 200 to 400 mg of procainamide for the treatment of sustained ventricular tachycardia .

Example answer:
{"entities": [{"text": "ventricular tachycardia", "type": "Disease"}, {"text": "procainamide", "type": "Chemical"}]}

Example input:
Sentence: immediately before the induction of anaesthesia , to prevent arrhythmia and bradycardia following repeated doses of suxamethonium in children , was studied .

Example answer:
{"entities": [{"text": "arrhythmia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: Flestolol produced a dose-dependent attenuation of isoproterenol-induced tachycardia .

Example answer:
{"entities": [{"text": "Flestolol", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: UM-272 ( N , N-dimethylpropranolol ) , a quaternary antiarrhythmic agent , was administered sublingually to dogs with ouabain-induced ventricular tachycardias .

Example answer:
{"entities": [{"text": "UM-272", "type": "Chemical"}, {"text": "N , N-dimethylpropranolol", "type": "Chemical"}, {"text": "ouabain-induced", "type": "Chemical"}, {"text": "ventricular tachycardias", "type": "Disease"}]}

Example input:
Sentence: Flestolol effectively reduced heart rate in patients with supraventricular tachyarrhythmia .

Example answer:
{"entities": [{"text": "Flestolol", "type": "Chemical"}, {"text": "supraventricular tachyarrhythmia", "type": "Disease"}]}

Input:
Sentence: Induction of the ventricular tachyarrhythmia was prevented by oral d , l-sotalol in 35 ( 43 % ) patients ; the ventricular tachyarrhythmia remained inducible in 40 ( 49 % ) patients ; and two ( 2.5 % ) patients did not tolerate even 40 mg of d , l-sotalol once daily .

## Item bc5cdr:test:1469
Example input:
Sentence: A nonregenerative anemia was the most compromising of the cytopenias and occurred in approximately 50 % of dogs receiving 400-500 mg/kg cefonicid or 540-840 mg/kg cefazedone .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "cytopenias", "type": "Disease"}, {"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}]}

Example input:
Sentence: All these effects of DES were more pronounced among previously ovariectomized animals .

Example answer:
{"entities": [{"text": "DES", "type": "Chemical"}]}

Example input:
Sentence: When respiratory failure was produced by hypoventilation ( pH 7.05 to 7.25 ; PC02 70 to 100 mm Hg : P02 20 to 40 mm Hg ) , infusion of aminophylline resulted in an even greater decrease in ventricular fibrillation threshold to 60 percent of the control level .

Example answer:
{"entities": [{"text": "respiratory failure", "type": "Disease"}, {"text": "hypoventilation", "type": "Disease"}, {"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}]}

Example input:
Sentence: This observation , along with the rapid rate of decline in red cell mass parameters of affected dogs , suggests that a hemolytic component complicated the red cell production problem and that multiple toxicologic mechanisms contributed to the cytopenia .

Example answer:
{"entities": [{"text": "hemolytic", "type": "Disease"}, {"text": "cytopenia", "type": "Disease"}]}

Example input:
Sentence: His bundle recordings showed an atrial tachycardia with intermittent exit block and greatly prolonged BH and HV intervals ( 40 and 100 msec , respectively ) .

Example answer:
{"entities": [{"text": "atrial tachycardia", "type": "Disease"}]}

Example input:
Sentence: By using transthoracic echocardiography , anterior and posterior wall thickness , LV diameters and LV fractional shortening ( FS ) were measured in all rats before DOX or saline , and at weeks 6 and 9 after treatment in all surviving rats .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: Dopamine turnover ratios ( DOPAC : DA and HVA : DA ) were found to be lower in those animals exposed to the exploratory box when compared to their home cage counterparts .

Example answer:
{"entities": [{"text": "Dopamine", "type": "Chemical"}, {"text": "DOPAC", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}, {"text": "HVA", "type": "Chemical"}]}

Example input:
Sentence: There was also a higher incidence of tachyarrhythmias ( P less than 0.05 ) and ventricular ectopic beats ( P less than 0.05 ) in the morphine infusion group .

Example answer:
{"entities": [{"text": "tachyarrhythmias", "type": "Disease"}, {"text": "ventricular ectopic beats", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: Over the period 1993-1996 , 551 cases of VTE were identified in Germany and the UK along with 2066 controls .

Example answer:
{"entities": [{"text": "VTE", "type": "Disease"}]}

Example input:
Sentence: Sublingual UM-272 converted ventricular tachycardia to sinus rhythm in all 5 dogs .

Example answer:
{"entities": [{"text": "UM-272", "type": "Chemical"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Input:
Sentence: VT appeared in fewer dogs and at a later time , and there were more sinoatrial beats and less ectopies .

## Item bc5cdr:test:1541
Example input:
Sentence: Climbing behavior induced by apomorphine was reduced in animals treated with THP .

Example answer:
{"entities": []}

Example input:
Sentence: Maltolyl p-coumarate was found to attenuate cognitive deficits in both rat models using passive avoidance test and to reduce apoptotic cell death observed in the hippocampus of the amyloid beta peptide ( 1-42 ) -infused rats .

Example answer:
{"entities": [{"text": "Maltolyl p-coumarate", "type": "Chemical"}, {"text": "cognitive deficits", "type": "Disease"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}]}

Example input:
Sentence: The administration of phenobarbitone and carbamazepine for 21days caused a significant impairment of learning and memory as well as an increased oxidative stress .

Example answer:
{"entities": [{"text": "phenobarbitone", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "impairment of learning and memory", "type": "Disease"}]}

Example input:
Sentence: In the present study , we investigated whether maltolyl p-coumarate could improve cognitive decline in scopolamine-injected rats and in amyloid beta peptide ( 1-42 ) -infused rats .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "cognitive decline", "type": "Disease"}, {"text": "scopolamine-injected", "type": "Chemical"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}]}

Example input:
Sentence: Apomorphine , a nonselective dopamine agonist , was selected due to its biphasic behavioral effects , its ability to induce hypothermia , and to produce distinct changes to dopamine turnover in the rodent brain .

Example answer:
{"entities": [{"text": "Apomorphine", "type": "Chemical"}, {"text": "dopamine agonist", "type": "Chemical"}, {"text": "hypothermia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: NRA0160 and clozapine significantly reversed the disruption of prepulse inhibition ( PPI ) in rats produced by apomorphine .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "apomorphine", "type": "Chemical"}]}

Example input:
Sentence: In male animals , repeated apomorphine treatment induced a gradual development of aggressive behavior as evidenced by the increased intensity of aggressiveness and shortened latency before the first attack toward the opponent .

Example answer:
{"entities": [{"text": "apomorphine", "type": "Chemical"}, {"text": "aggressive behavior", "type": "Disease"}, {"text": "aggressiveness", "type": "Disease"}]}

Example input:
Sentence: Initial testing in a time-dependent forgetting task employing a 24-h delay between training and testing showed that metrifonate improved object recognition ( at 10 and 30 mg/kg , p.o .

Example answer:
{"entities": [{"text": "metrifonate", "type": "Chemical"}]}

Example input:
Sentence: Amnesia produced by scopolamine and cycloheximide were reversed by morphine given 30 min before the test trial ( pre-test ) , and pre-test morphine also facilitated the memory retrieval in the animals administered naloxone during the training trial .

Example answer:
{"entities": [{"text": "Amnesia", "type": "Disease"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "cycloheximide", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}, {"text": "naloxone", "type": "Chemical"}]}

Example input:
Sentence: ) , administered 20 min before the training session , prevented amnesia induced by both the non selective antimuscarinic drug scopolamine and the M1-selective antagonist S- ( - ) -ET-126 .

Example answer:
{"entities": [{"text": "S- ( - )", "type": "Chemical"}]}

Input:
Sentence: Co-administration of nefiracetam and apomorphine during training or 10h thereafter produced no significant anti-amnesic effect .

## Item bc5cdr:test:1775
Example input:
Sentence: Controlled hypotension in groups A and C was induced with PGE1 to maintain mean arterial blood pressure at 55 mmHg for 180 min .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "PGE1", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: After starting PGE1 or TMP , MAP and rate pressure product ( RPP ) decreased significantly compared with preinfusion values ( P < 0.01 ) , and the degree of hypotension due to PGE1 remained constant until 60 min after its discontinuation .

Example answer:
{"entities": [{"text": "PGE1", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: d-1 given for 4 weeks , elevated blood pressure from 102+/-13 to 152+/-15 mm Hg and increased the synthesis of ET-1 and the levels of ET-1 mRNA in the mesenteric artery ( 240 % and 230 % , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: The magnitude and time course of the increase in heart rate and the decrease in systolic blood pressure after nitroglycerin were similar in the normal and diabetic subjects without autonomic neuropathy , whereas a lesser increase in heart rate and a greater decrease in systolic blood pressure occurred in the diabetic subjects with autonomic neuropathy .

Example answer:
{"entities": [{"text": "nitroglycerin", "type": "Chemical"}, {"text": "diabetic", "type": "Disease"}, {"text": "autonomic neuropathy", "type": "Disease"}]}

Example input:
Sentence: After 4-week administration of L-NAME , the systolic blood pressure ( SBP ) increased by 36 % .

Example answer:
{"entities": [{"text": "L-NAME", "type": "Chemical"}]}

Example input:
Sentence: In each group , SNP infusion resulted in an initial decrease in blood pressure from 86 torr and 83 torr , respectively , to 48 torr .

Example answer:
{"entities": [{"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: Two groups of patients receiving tacrolimus were compared over a period of 1 year , one group comprising hypertensive patients who were receiving nifedipine , and the other comprising nonhypertensive patients not receiving nifedipine .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "hypertensive", "type": "Disease"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: Nifedipine significantly improved kidney function as indicated by a significant lowering of serum creatinine levels at 6 and 12 months .

Example answer:
{"entities": [{"text": "Nifedipine", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: Nimodipine treatment resulted in a statistically significant reduction in systolic BP ( SBP ) and diastolic BP ( DBP ) from baseline compared with placebo during the first few days .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "Chemical"}, {"text": "reduction in systolic BP", "type": "Disease"}]}

Input:
Sentence: Both systolic and diastolic blood pressures of these 13 patients were decreased significantly after 4 weeks of nifedipine therapy , and blood pressure was maintained within the normal range thereafter for 25 months .

## Item bc5cdr:test:1563
Example input:
Sentence: In the prophylactic lamivudine group severe hepatitis were observed only in 1 patient ( 2.7 % ) of 37 patients ( p < 0.006 ) .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: Our study suggests that prophylactic lamivudine significantly decreases the incidence of HBV reactivation and overall morbidity in cancer patients during and after immunosuppressive therapy .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: Seventy-five human immunodeficiency virus ( HIV ) -infected patients with CD4+ cell counts < 500/mm3 were randomized to receive either ZDV ( 500 mg daily ) alone ( group I , n = 38 ) or in combination with folinic acid ( 15 mg daily ) and intramascular vitamin B12 ( 1000 micrograms monthly ) ( group II , n = 37 ) .

Example answer:
{"entities": [{"text": "human immunodeficiency virus ( HIV ) -infected", "type": "Disease"}, {"text": "ZDV", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}, {"text": "vitamin B12", "type": "Chemical"}]}

Example input:
Sentence: Prophylactic administration of lamivudine in patients who required immunosuppressive therapy seems to be safe , well tolerated and effective in preventing HBV reactivation .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: Thirty-five lamivudine-na ve HBV infected patients with or without HIV co-infection were studied : 15 chronic HBV mono-infected patients and 20 HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "lamivudine-na", "type": "Chemical"}, {"text": "HBV infected", "type": "Disease"}, {"text": "HIV co-infection", "type": "Disease"}, {"text": "HBV mono-infected", "type": "Disease"}]}

Example input:
Sentence: HBV lamivudine-resistant strains were detected in 3 of 15 mono-infected chronic hepatitis B patients and 10 of 20 HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "lamivudine-resistant", "type": "Chemical"}, {"text": "hepatitis B", "type": "Disease"}]}

Example input:
Sentence: The objective of this study was to report our experience concerning the effectiveness of the prophylactic administration of lamivudine in hepatitis B virus surface antigen ( HBs Ag ) positive patients with rheumatologic disease .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}, {"text": "hepatitis B virus surface antigen", "type": "Chemical"}, {"text": "HBs Ag", "type": "Chemical"}, {"text": "rheumatologic disease", "type": "Disease"}]}

Example input:
Sentence: In this study , cancer patients who have solid and hematological malignancies with chronic HBV infection received the antiviral agent lamivudine prior and during CT compared with historical control group who did not receive lamivudine .

Example answer:
{"entities": [{"text": "cancer", "type": "Disease"}, {"text": "hematological malignancies", "type": "Disease"}, {"text": "HBV infection", "type": "Disease"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: From June 2004 to October 2006 , 11 HBs Ag positive patients with rheumatologic diseases , who were on both immunosuppressive and prophylactic lamivudine therapies , were retrospectively assessed .

Example answer:
{"entities": [{"text": "HBs Ag", "type": "Chemical"}, {"text": "rheumatologic diseases", "type": "Disease"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: Lamivudine for the prevention of hepatitis B virus reactivation in hepatitis-B surface antigen ( HBSAG ) seropositive cancer patients undergoing cytotoxic chemotherapy .

Example answer:
{"entities": [{"text": "Lamivudine", "type": "Chemical"}, {"text": "hepatitis B", "type": "Disease"}, {"text": "hepatitis-B surface antigen", "type": "Chemical"}, {"text": "HBSAG", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Input:
Sentence: Forty-two Chinese HBsAg carriers were randomized to receive placebo ( 6 patients ) or lamivudine orally in dosages of 25 mg , 100 mg , or 300 mg daily ( 12 patients for each dosage ) .

## Item bc5cdr:test:1934
Example input:
Sentence: Studies dealing with myocardial infarction are more informative when dealt with age .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: It has not been reported previously in children .

Example answer:
{"entities": []}

Example input:
Sentence: This case illustrates the need for close vigilance in adverse drug reactions , particularly in the elderly .

Example answer:
{"entities": [{"text": "adverse drug reactions", "type": "Disease"}]}

Example input:
Sentence: The mean age of patients in the 16 probable cases was 57.9 , with hepatotoxicity being more common in women .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: It may even present in patients who have tolerated this medicine well in the past .

Example answer:
{"entities": []}

Example input:
Sentence: The majority of patients ( > 60 % ) experienced no change in their disease status from baseline .

Example answer:
{"entities": []}

Example input:
Sentence: Prolonged apnea in our case ensued because the information about suicidal attempt by OP compound was concealed from the treating team .

Example answer:
{"entities": [{"text": "apnea", "type": "Disease"}, {"text": "OP compound", "type": "Chemical"}]}

Example input:
Sentence: None of these well validated cases occurred within the first 10 days after treatment .

Example answer:
{"entities": []}

Example input:
Sentence: Some case reports are published in the literature but no systematic study from a sample of patients has been published .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSION : This case started with a media report in a popular newspaper , initiated by published , peer-reviewed research on herbals , and involved human failure in a case history , medical examination and clinical treatment .

Example answer:
{"entities": []}

Input:
Sentence: We communicate a case in a previously healthy person , a fact not found in the recent literature .

## Item bc5cdr:test:1758
Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/", "type": "Chemical"}, {"text": "K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: HS diet for 4 wk caused a progressive increase in BP , protein and albumin excretion , and glomerular sclerosis in male DS rats , which were attenuated by castration .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: In salt-depleted rats , amphotericin B decreased creatinine clearance linearly with time , with an 85 % reduction by week 3 .

Example answer:
{"entities": [{"text": "amphotericin B", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: In conclusion , reductions in creatinine clearance and renal amphotericin B accumulation after chronic amphotericin B administration were enhanced by salt depletion and attenuated by sodium loading in rats .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "amphotericin B", "type": "Chemical"}, {"text": "sodium", "type": "Chemical"}]}

Example input:
Sentence: In control rats , immunostaining for 7H6 and ZO-1 colocalized to outline bile canaliculi in a continuous fashion .

Example answer:
{"entities": []}

Example input:
Sentence: This study is the first to demonstrate that impairment of hepatocyte TJs occurs heterogenously in the liver lobule after BDL and suggests that BDL and EE treatments produce different lobular distributions of increased paracellular permeability .

Example answer:
{"entities": [{"text": "EE", "type": "Chemical"}]}

Example input:
Sentence: After EE treatment , changes in immunostaining for 7H6 and ZO-1 were similar to those seen in periportal hepatocytes after BDL , but distributed more diffusely throughout the lobule .

Example answer:
{"entities": [{"text": "EE", "type": "Chemical"}]}

Example input:
Sentence: We used rat models of intrahepatic cholestasis by ethinyl estradiol ( EE ) treatment and extrahepatic cholestasis by bile duct ligation ( BDL ) to precisely determine the site of TJ damage .

Example answer:
{"entities": [{"text": "intrahepatic cholestasis", "type": "Disease"}, {"text": "ethinyl estradiol", "type": "Chemical"}, {"text": "EE", "type": "Chemical"}, {"text": "extrahepatic cholestasis", "type": "Disease"}]}

Input:
Sentence: A clear reduction of BS synthesis was found in bile-diverted rats treated with EE , yet biliary BS composition was only minimally affected .

## Item bc5cdr:test:1532
Example input:
Sentence: Furthermore , glomerulosclerosis index was significantly increased in the nitrendipine-treated group compared with the hypertensive controls ( 0.38 +/- 0.1 versus 0.13 +/- 0.04 ) .

Example answer:
{"entities": [{"text": "glomerulosclerosis", "type": "Disease"}, {"text": "nitrendipine-treated", "type": "Chemical"}, {"text": "hypertensive", "type": "Disease"}]}

Example input:
Sentence: HS diet for 4 wk caused a progressive increase in BP , protein and albumin excretion , and glomerular sclerosis in male DS rats , which were attenuated by castration .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: A further deterioration was seen when CsA was combined with either FK506 or SRL , whereas the GFR remained unchanged in the group treated with FK506 plus SRL when compared with treatment with any of the single substances .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: When comparing all lithium treated versus non-lithium-treated groups , lithium caused a reduction in glomerular filtration rate ( GFR ) without significant changes in effective renal plasma flow ( as determined by a marker secreted into the proximal tubules ) or lithium clearance .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: HP failed to accentuante progression of renal failure and in fact tended to increase GFR and decrease plasma creatinine levels in lithium pretreated rats .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : CsA , FK506 and SRL all significantly decreased the GFR .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: NX caused an additive deterioration in GFR which , however , was ameliorated by HP .

Example answer:
{"entities": []}

Example input:
Sentence: Untreated group 3 rats exhibited a progressive reduction in GFR ( 0.35 +/- 0.08 ml/min at 4 months , 0.27 +/- 0.07 ml/min at 6 months ) .

Example answer:
{"entities": []}

Example input:
Sentence: In this model of chronic renal failure the decline in GFR is not accompanied by a corresponding fall in effective renal plasma flow , which may be the functional expression of the formation of nonfiltrating atubular glomeruli .

Example answer:
{"entities": [{"text": "chronic renal failure", "type": "Disease"}]}

Example input:
Sentence: Reduction in GFR was associated with the development of glomerular sclerosis in both treated and untreated rats .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Input:
Sentence: The improvement in GFR was not associated with enhanced glomerular hypertrophy or increased segmental glomerulosclerosis , tubulointerstitial injury , or renal cortical malondialdehyde content .

## Item bc5cdr:test:1917
Example input:
Sentence: RESULTS : The patients in the study group were significantly younger than the patients in the control group ( P < 0.002 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Three patients had no change and disease progressed in two .

Example answer:
{"entities": []}

Example input:
Sentence: Median progression-free survival was 5 months .

Example answer:
{"entities": []}

Example input:
Sentence: In multivariate analysis , three factors independently predicted mortality : serum bilirubin ( > or=10.8 mg/dL ) , prothrombin time ( PT ) prolongation ( > or=26 seconds ) , and grade III/IV encephalopathy at presentation .

Example answer:
{"entities": [{"text": "bilirubin", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: After a median follow-up of 22 months , the median progression free survival rate was 7 months , and the median survival time was 16 months .

Example answer:
{"entities": []}

Example input:
Sentence: Overall survival from the time of OLTX was not significantly different among groups , but by year 13 , the survival of the patients who had ESRD was only 28.2 % compared with 54.6 % in the control group .

Example answer:
{"entities": [{"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Eight patients were dead in the last follow-up ; two of them died of treatment-related toxicity .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Groups 1 and 3 remained untreated while groups 2 and 4 received enalapril .

Example answer:
{"entities": [{"text": "enalapril", "type": "Chemical"}]}

Example input:
Sentence: The median duration of survival in the 12 patients was 54 weeks ( range 21 to more than 156 weeks ) , with an 18-month survival rate of 42 % .

Example answer:
{"entities": []}

Example input:
Sentence: Finally , 15 patients were excluded from the study ( noncompliance 14 , death 1 ) ; thus , 60 patients ( 31 in group I and 29 in group II ) were eligible for analysis .

Example answer:
{"entities": [{"text": "death", "type": "Disease"}]}

Input:
Sentence: Patients in group A had significant mortality at 2-year follow-up ( 28 % ) , in contrast to zero mortality in the other three groups .

## Item bc5cdr:test:1667
Example input:
Sentence: The aim of this study was to assess the effects of gabapentin , a drug effective in neuropathic pain patients , on brain processing of nociceptive information in normal and central sensitization states .

Example answer:
{"entities": [{"text": "gabapentin", "type": "Chemical"}, {"text": "neuropathic pain", "type": "Disease"}]}

Example input:
Sentence: The reduction of cyclosporine- or tacrolimus trough levels and the administration of calcium channel blockers led to relief of pain .

Example answer:
{"entities": [{"text": "cyclosporine-", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: These findings indicate that gabapentin has a measurable antinociceptive effect and a stronger antihyperalgesic effect most evident in the brain areas undergoing deactivation , thus supporting the concept that gabapentin is more effective in modulating nociceptive transmission when central sensitization is present .

Example answer:
{"entities": [{"text": "gabapentin", "type": "Chemical"}]}

Example input:
Sentence: Bradykinin receptors antagonists and nitric oxide synthase inhibitors in vincristine and streptozotocin induced hyperalgesia in chemotherapy and diabetic neuropathy rat model .

Example answer:
{"entities": [{"text": "Bradykinin", "type": "Chemical"}, {"text": "nitric oxide", "type": "Chemical"}, {"text": "vincristine", "type": "Chemical"}, {"text": "streptozotocin", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "diabetic neuropathy", "type": "Disease"}]}

Example input:
Sentence: To this end , persistent hyperalgesia was induced by administration of capsaicin in the tail of gonadally intact F344 rats , following which the tail was immersed in a mildly noxious thermal stimulus , and tail-withdrawal latencies measured .

Example answer:
{"entities": [{"text": "hyperalgesia", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: For both experiments the drug intake led to significant increases in PRL secretion , acting preferentially on tonic secretion as pulse amplitude and frequency did not differ significantly from corresponding control values .

Example answer:
{"entities": []}

Example input:
Sentence: The antinociception produced by ( +/- ) -PG-9 was prevented by the unselective muscarinic antagonist atropine , the M1-selective antagonists pirenzepine and dicyclomine and the acetylcholine depletor hemicholinium-3 , but not by the opioid antagonist naloxone , the gamma-aminobutyric acidB antagonist 3-aminopropyl-diethoxy-methyl-phosphinic acid , the H3 agonist R- ( alpha ) -methylhistamine , the D2 antagonist quinpirole , the 5-hydroxytryptamine4 antagonist 2-methoxy-4-amino-5-chlorobenzoic acid 2- ( diethylamino ) ethyl ester hydrochloride , the 5-hydroxytryptamin1A antagonist 1- ( 2-methoxyphenyl ) -4- [ 4- ( 2-phthalimido ) butyl ] piperazine hydrobromide and the polyamines depletor reserpine .

Example answer:
{"entities": [{"text": ")", "type": "Chemical"}, {"text": "gamma-aminobutyric", "type": "Chemical"}, {"text": "3-aminopropyl-diethoxy-methyl-phosphinic", "type": "Chemical"}, {"text": "R- ( alpha )", "type": "Chemical"}, {"text": "2-methoxy-4-amino-5-chlorobenzoic acid 2- ( diethylamino ) ethyl", "type": "Chemical"}, {"text": "1- ( 2-methoxyphenyl ) -4- [ 4- ( 2-phthalimido ) butyl ]", "type": "Chemical"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: In inflamed preparations , the muscarinic receptor antagonism on the phasic component of the electrical field stimulation-evoked contraction was decreased and the pirenzepine and 4-DAMP antagonism on the tonic component was much less efficient than in controls .

Example answer:
{"entities": [{"text": "pirenzepine", "type": "Chemical"}, {"text": "4-DAMP", "type": "Chemical"}]}

Example input:
Sentence: Based on these data , it can be postulated that ( +/- ) -PG-9 exerted an antinociceptive effect mediated by a central potentiation of cholinergic transmission .

Example answer:
{"entities": [{"text": ")", "type": "Chemical"}]}

Input:
Sentence: For this purpose , experimental conditions were created in which NSAIDs had previously been observed to produce effects on phasic and tonic pain by either central or peripheral mechanisms .

## Item bc5cdr:test:1928
Example input:
Sentence: The second case occurred in a 55-year-old farmer following cutaneous contact with Dormex .

Example answer:
{"entities": [{"text": "Dormex", "type": "Chemical"}]}

Example input:
Sentence: We report the case of a 30-year-old Caucasian man who came to the emergency department in atrial fibrillation with rapid ventricular response .

Example answer:
{"entities": [{"text": "atrial fibrillation", "type": "Disease"}]}

Example input:
Sentence: A 45-year-old man , an admitted frequent cocaine user , presented to the Emergency Department ( ED ) on two separate occasions with a history of priapism after cocaine use .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "priapism", "type": "Disease"}]}

Example input:
Sentence: One patient had complete response , seven had stable disease , none had partial response and five had progressive disease .

Example answer:
{"entities": []}

Example input:
Sentence: The first case involved a 59-year-old man who used Dormex , which contains hydrogen cyanamide , without protection after consuming a large amount of alcohol during a meal .

Example answer:
{"entities": [{"text": "Dormex", "type": "Chemical"}, {"text": "hydrogen cyanamide", "type": "Chemical"}, {"text": "alcohol", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : This case started with a media report in a popular newspaper , initiated by published , peer-reviewed research on herbals , and involved human failure in a case history , medical examination and clinical treatment .

Example answer:
{"entities": []}

Example input:
Sentence: A 49-year-old woman was transferred to our department because of quadriparesis , lancinating pain , sensory loss , and paresthesia of the distal limbs .

Example answer:
{"entities": [{"text": "quadriparesis", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "sensory loss", "type": "Disease"}, {"text": "paresthesia", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : A 72-year-old white man with underlying human immunodeficiency virus , atrial fibrillation , coronary artery disease , and hyperlipidemia presented with generalized pain , fatigue , and dark orange urine for 3 days .

Example answer:
{"entities": [{"text": "human immunodeficiency virus", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "coronary artery disease", "type": "Disease"}, {"text": "hyperlipidemia", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "fatigue", "type": "Disease"}]}

Example input:
Sentence: CASE SUMMARY : A 25-year-old male patient , with a height of 175 cm and weight of 72 kg presented to Marmara University Hospital Emergency Department , Istanbul , Turkey , with 5 days ' history of jaundice , malaise , nausea , and vomiting .

Example answer:
{"entities": [{"text": "jaundice", "type": "Disease"}, {"text": "nausea", "type": "Disease"}, {"text": "vomiting", "type": "Disease"}]}

Example input:
Sentence: The mean age of patients in the 16 probable cases was 57.9 , with hepatotoxicity being more common in women .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}]}

Input:
Sentence: We report 4 cases , one of them in a previously healthy person .

## Item bc5cdr:test:1380
Example input:
Sentence: The expression of arginine vasopressin ( AVP ) gene in the paraventricular ( PVN ) and supraoptic nuclei ( SON ) was investigated in rats with lithium ( Li ) -induced polyuria , using in situ hybridization histochemistry and radioimmunoassay .

Example answer:
{"entities": [{"text": "arginine vasopressin", "type": "Chemical"}, {"text": "AVP", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "Li", "type": "Chemical"}, {"text": "polyuria", "type": "Disease"}]}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "a reduced locomotor activity", "type": "Disease"}]}

Example input:
Sentence: In the five rats that developed somatic rigidity , ICP and CVP increased significantly above baseline ( delta ICP 7.5 +/- 1.0 mmHg , delta CVP 5.9 +/- 1.3 mmHg ) .

Example answer:
{"entities": [{"text": "somatic rigidity", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : This study establishes a TAA model by periarterial CaCl ( 2 ) exposure in rats , and demonstrates a significant elevation of expression of MMP-2 , MMP-9 , ADAM10 and ADAM17 in the pathogenesis of vascular remodeling .

Example answer:
{"entities": [{"text": "TAA", "type": "Disease"}, {"text": "CaCl ( 2 )", "type": "Chemical"}]}

Example input:
Sentence: The effect of a 6-week treatment with the calcium channel blocker nitrendipine or the angiotensin converting enzyme inhibitor enalapril on blood pressure , albuminuria , renal hemodynamics , and morphology of the nonclipped kidney was studied in rats with two-kidney , one clip renovascular hypertension .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "nitrendipine", "type": "Chemical"}, {"text": "angiotensin", "type": "Chemical"}, {"text": "enalapril", "type": "Chemical"}, {"text": "albuminuria", "type": "Disease"}, {"text": "renovascular hypertension", "type": "Disease"}]}

Example input:
Sentence: Six weeks after clipping of one renal artery , hypertensive rats ( 178 +/- 4 mm Hg ) were randomly assigned to three groups : untreated hypertensive controls ( n = 8 ) , enalapril-treated ( n = 8 ) , or nitrendipine-treated ( n = 10 ) .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}, {"text": "enalapril-treated", "type": "Chemical"}, {"text": "nitrendipine-treated", "type": "Chemical"}]}

Example input:
Sentence: The effects of varying the extracellular concentrations of Na and Ca ( [ Na ] o and [ Ca ] o ) on both , the spontaneous beating and the negative chronotropic action of verapamil , were studied in the isolated rat atria .

Example answer:
{"entities": [{"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: These results suggest that dehydration and/or the activation of visceral afferent inputs may contribute to the elevation of plasma AVP and the upregulation of AVP gene expression in the PVN and the SON of the Li-induced diabetes insipidus rat .

Example answer:
{"entities": [{"text": "dehydration", "type": "Disease"}, {"text": "AVP", "type": "Chemical"}, {"text": "Li-induced", "type": "Chemical"}, {"text": "diabetes insipidus", "type": "Disease"}]}

Example input:
Sentence: In unanesthetized , spontaneously hypertensive rats the decrease in blood pressure and heart rate produced by intravenous clonidine , 5 to 20 micrograms/kg , was inhibited or reversed by nalozone , 0.2 to 2 mg/kg .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}, {"text": "clonidine", "type": "Chemical"}, {"text": "nalozone", "type": "Chemical"}]}

Example input:
Sentence: These findings indicate that in spontaneously hypertensive rats the effects of central alpha-adrenoceptor stimulation involve activation of opiate receptors .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}]}

Input:
Sentence: Central cardiovascular effects of AVP and ANP in normotensive and spontaneously hypertensive rats .

## Item bc5cdr:test:1560
Example input:
Sentence: Lamivudine was added because of de nova hepatitis B infection during her follow-up .

Example answer:
{"entities": [{"text": "Lamivudine", "type": "Chemical"}, {"text": "hepatitis B infection", "type": "Disease"}]}

Example input:
Sentence: In this study , cancer patients who have solid and hematological malignancies with chronic HBV infection received the antiviral agent lamivudine prior and during CT compared with historical control group who did not receive lamivudine .

Example answer:
{"entities": [{"text": "cancer", "type": "Disease"}, {"text": "hematological malignancies", "type": "Disease"}, {"text": "HBV infection", "type": "Disease"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: HBV lamivudine-resistant strains were detected in 3 of 15 mono-infected chronic hepatitis B patients and 10 of 20 HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "lamivudine-resistant", "type": "Chemical"}, {"text": "hepatitis B", "type": "Disease"}]}

Example input:
Sentence: Mutations associated with lamivudine-resistance in therapy-na ve hepatitis B virus ( HBV ) infected patients with and without HIV co-infection : implications for antiretroviral therapy in HBV and HIV co-infected South African patients .

Example answer:
{"entities": [{"text": "lamivudine-resistance", "type": "Chemical"}, {"text": "hepatitis B virus ( HBV ) infected", "type": "Disease"}, {"text": "HIV co-infection", "type": "Disease"}]}

Example input:
Sentence: Prophylactic administration of lamivudine in patients who required immunosuppressive therapy seems to be safe , well tolerated and effective in preventing HBV reactivation .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: The objectives were to assess the efficacy of lamivudine in reducing the incidence of HBV reactivation , and diminishing morbidity and mortality during CT. Two groups were compared in this study .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: This was an exploratory study to investigate lamivudine-resistant hepatitis B virus ( HBV ) strains in selected lamivudine-na ve HBV carriers with and without human immunodeficiency virus ( HIV ) co-infection in South African patients .

Example answer:
{"entities": [{"text": "lamivudine-resistant", "type": "Chemical"}, {"text": "hepatitis B", "type": "Disease"}, {"text": "lamivudine-na", "type": "Chemical"}, {"text": "human immunodeficiency virus ( HIV ) co-infection", "type": "Disease"}]}

Example input:
Sentence: Our study suggests that prophylactic lamivudine significantly decreases the incidence of HBV reactivation and overall morbidity in cancer patients during and after immunosuppressive therapy .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: The objective of this study was to report our experience concerning the effectiveness of the prophylactic administration of lamivudine in hepatitis B virus surface antigen ( HBs Ag ) positive patients with rheumatologic disease .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}, {"text": "hepatitis B virus surface antigen", "type": "Chemical"}, {"text": "HBs Ag", "type": "Chemical"}, {"text": "rheumatologic disease", "type": "Disease"}]}

Example input:
Sentence: Lamivudine for the prevention of hepatitis B virus reactivation in hepatitis-B surface antigen ( HBSAG ) seropositive cancer patients undergoing cytotoxic chemotherapy .

Example answer:
{"entities": [{"text": "Lamivudine", "type": "Chemical"}, {"text": "hepatitis B", "type": "Disease"}, {"text": "hepatitis-B surface antigen", "type": "Chemical"}, {"text": "HBSAG", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Input:
Sentence: Lamivudine is effective in suppressing hepatitis B virus DNA in Chinese hepatitis B surface antigen carriers : a placebo-controlled trial .

## Item bc5cdr:test:1781
Example input:
Sentence: As a consequence of blocking I ( f ) , clonidine reduced the slope of the diastolic depolarization and the frequency of pacemaker potentials in sinoatrial node cells from wild-type and alpha2ABC-knockout mice .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: glycopyrrolate and atropine in the prevention of bradycardia and arrhythmias following repeated doses of suxamethonium in children .

Example answer:
{"entities": [{"text": "glycopyrrolate", "type": "Chemical"}, {"text": "atropine", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "arrhythmias", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: UM-272 ( N , N-dimethylpropranolol ) , a quaternary antiarrhythmic agent , was administered sublingually to dogs with ouabain-induced ventricular tachycardias .

Example answer:
{"entities": [{"text": "UM-272", "type": "Chemical"}, {"text": "N , N-dimethylpropranolol", "type": "Chemical"}, {"text": "ouabain-induced", "type": "Chemical"}, {"text": "ventricular tachycardias", "type": "Disease"}]}

Example input:
Sentence: In the remaining three patients , procainamide was administered orally for treatment of chronic premature ventricular contractions or atrial flutter .

Example answer:
{"entities": [{"text": "procainamide", "type": "Chemical"}, {"text": "premature ventricular contractions", "type": "Disease"}, {"text": "atrial flutter", "type": "Disease"}]}

Example input:
Sentence: Effects of long-term pretreatment with isoproterenol on bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: Previous anecdotal reports have linked creatine to the development of arrhythmia .

Example answer:
{"entities": [{"text": "creatine", "type": "Chemical"}, {"text": "arrhythmia", "type": "Disease"}]}

Example input:
Sentence: Procainamide-induced polymorphous ventricular tachycardia .

Example answer:
{"entities": [{"text": "Procainamide-induced", "type": "Chemical"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: In four patients , polymorphous ventricular tachycardia appeared after intravenous administration of 200 to 400 mg of procainamide for the treatment of sustained ventricular tachycardia .

Example answer:
{"entities": [{"text": "ventricular tachycardia", "type": "Disease"}, {"text": "procainamide", "type": "Chemical"}]}

Example input:
Sentence: The effects of varying the extracellular concentrations of Na and Ca ( [ Na ] o and [ Ca ] o ) on both , the spontaneous beating and the negative chronotropic action of verapamil , were studied in the isolated rat atria .

Example answer:
{"entities": [{"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Input:
Sentence: The mechanisms of proarrhythmic effects of Dubutamine are discussed .

## Item bc5cdr:test:1980
Example input:
Sentence: Initial testing in a time-dependent forgetting task employing a 24-h delay between training and testing showed that metrifonate improved object recognition ( at 10 and 30 mg/kg , p.o .

Example answer:
{"entities": [{"text": "metrifonate", "type": "Chemical"}]}

Example input:
Sentence: They showed significantly more rapid improvement of motor function in the first week following hemorrhage and better memory retention in the passive avoidance test .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "Disease"}]}

Example input:
Sentence: HBV viral load was performed with Amplicor HBV Monitor test v2.0 ( Roche Diagnostics , Penzberg , Germany ) .

Example answer:
{"entities": []}

Example input:
Sentence: Mean peak forced expiratory volume in 1 second ( FEV1 ) increases over baseline and the proportion of patients attaining at least a 15 % increase in the FEV1 ( responders ) were 31 % and 90 % , respectively , for ipratropium and 17 % and 50 % , respectively , for theophylline .

Example answer:
{"entities": [{"text": "ipratropium", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}]}

Example input:
Sentence: Elevated plus maze and passive avoidance apparatus served as the exteroceptive behavioral models for testing memory .

Example answer:
{"entities": []}

Example input:
Sentence: During monitoring , visual hallucinations did not correlate with EEG readings , nor did video recording capture any of the described events .

Example answer:
{"entities": [{"text": "visual hallucinations", "type": "Disease"}]}

Example input:
Sentence: The average FEV1 increases during the 6-hour observation period were 18 % for ipratropium and 8 % for theophylline .

Example answer:
{"entities": [{"text": "ipratropium", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}]}

Example input:
Sentence: The visual analog scale ( VAS ) was used to measure pain intensity and a stop-watch was used to time the pain period .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}]}

Example input:
Sentence: Passive avoidance paradigm and elevated plus maze test were used to assess cognitive function .

Example answer:
{"entities": []}

Example input:
Sentence: Eight healthy volunteers inhaled nicotine in darkness during a functional magnetic resonance imaging ( fMRI ) experiment ; eye movements were registered using video-oculography .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}]}

Input:
Sentence: Useful Field of View ( UFOV -- a test of visual attention ) was also undertaken .

## Item bc5cdr:test:1978
Example input:
Sentence: By implantation of electrodes and electrophysiological recording in vivo , the results showed that Rg1 restored the long-term potentiation ( LTP ) impaired by morphine in both freely moving and anaesthetised rats .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: Direct comparison between sham and real rTMS effects showed no significant difference in clinician-assessed dyskinesia severity .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Similarly , in patient diaries , although both treatments caused reduction in subjective dyskinesia scores during the days of intervention , the effect was sustained for 3 days after the intervention for the real rTMS only .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Locomotor activity was assessed in male Sprague-Dawley rats tested in photocell cages .

Example answer:
{"entities": []}

Example input:
Sentence: However , comparison with the baseline showed small but significant reduction in dyskinesia severity following real rTMS but not placebo .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Ten patients with PD and prominent dyskinesias had rTMS ( 1,800 pulses ; 1 Hz rate ) delivered over the motor cortex for 4 consecutive days twice , once real stimuli and once sham stimulation were used ; evaluations were done at the baseline and 1 day after the end of each of the treatment series .

Example answer:
{"entities": [{"text": "PD", "type": "Disease"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: In conclusion , although Ro4368554 did not improve a time-related retention deficit , it reversed a cholinergic and a serotonergic memory deficit , suggesting that both mechanisms may be involved in the facilitation of object memory by Ro4368554 and , possibly , other 5-HT ( 6 ) receptor antagonists .

Example answer:
{"entities": [{"text": "memory", "type": "Disease"}]}

Example input:
Sentence: RAMH per se showed significant reduction in locomotor time , distance traveled and average speed but THP ( 15 mg/kg i.p . )

Example answer:
{"entities": []}

Example input:
Sentence: They showed significantly more rapid improvement of motor function in the first week following hemorrhage and better memory retention in the passive avoidance test .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "Disease"}]}

Example input:
Sentence: Analysis of neurotransmitter concentration in some brain regions on the test day showed that dopamine concentration of the vehicle/scopolamine group was significantly lower than that of the vehicle/vehicle group , but this phenomenon was reversed when s-limonene or s-perillyl alcohol were administered before the injection of scopolamine .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "s-limonene", "type": "Chemical"}, {"text": "s-perillyl alcohol", "type": "Chemical"}, {"text": "scopolamine", "type": "Chemical"}]}

Input:
Sentence: A driving simulator ( Transport Research Laboratory ) was used to measure reaction time ( RT ) , speed maintenance and steering accuracy .

## Item bc5cdr:test:1993
Example input:
Sentence: Our study was designed to determine the effects of combined nitroglycerin and phenylephrine therapy .

Example answer:
{"entities": [{"text": "nitroglycerin", "type": "Chemical"}, {"text": "phenylephrine", "type": "Chemical"}]}

Example input:
Sentence: Data from a Transnational case-control study were used to assess the risk of VTE for the latter patterns of use , while accounting for duration of use .

Example answer:
{"entities": [{"text": "VTE", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : The combination of cisplatin and amifostine in this study resulted in an overall response rate of 16 % .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "amifostine", "type": "Chemical"}]}

Example input:
Sentence: Two groups of supine subjects were studied under placebo-controlled conditions , one during the night , when sleeping ( n = 7 ) and the other at daytime , when awake ( n = 6 ) .

Example answer:
{"entities": []}

Example input:
Sentence: In a placebo-controlled , single-blinded , crossover study , we assessed the effect of `` real '' repetitive transcranial magnetic stimulation ( rTMS ) versus `` sham '' rTMS ( placebo ) on peak dose dyskinesias in patients with Parkinson 's disease ( PD ) .

Example answer:
{"entities": [{"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: METHODS : We conducted a prospective , randomized , double-blind study in the emergency department of a central-city teaching hospital .

Example answer:
{"entities": []}

Example input:
Sentence: DESIGN : Retrospective analysis of a randomized phase II trial .

Example answer:
{"entities": []}

Example input:
Sentence: Crossover studies were performed 2 weeks apart .

Example answer:
{"entities": []}

Example input:
Sentence: For the subsequent 6-week double-blind crossover phase ( phase B ) , patients taking standard- or low-dose haloperidol were switched to placebo , and patients taking placebo were randomly assigned to standard- or low-dose haloperidol .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: In a randomized , double-blind , placebo-controlled , crossover study , we studied 12 volunteers in three experiments .

Example answer:
{"entities": []}

Input:
Sentence: A randomised , double-blind , placebo-controlled , crossover study design was employed .

## Item bc5cdr:test:2007
Example input:
Sentence: Subjects with SNHL were submitted to DFO reduction or temporary withdrawal .

Example answer:
{"entities": [{"text": "SNHL", "type": "Disease"}, {"text": "DFO", "type": "Chemical"}]}

Example input:
Sentence: Finally , we examined the low dose of 150 mg/kg ( 50 mg/kg per day ) using a similar washout period .

Example answer:
{"entities": []}

Example input:
Sentence: In the bolus group , 26.0 % ( 13/50 ) had akathisia compared with 32.7 % ( 16/49 ) in the infusion group ( Delta=-6.7 % ; 95 % confidence interval [ CI ] -24.6 % to 11.2 % ) .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Sixty-seven of 926 patients ( 7.2 % ) required discontinuation of spironolactone due to hyperkalemia ( n = 33 ) or renal failure ( n = 34 ) .

Example answer:
{"entities": [{"text": "spironolactone", "type": "Chemical"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: Patients with a DBP reduction of > or =20 % in the high-dose group had a significantly increased adjusted OR for the compound outcome variable death or dependency ( Barthel Index < 60 ) ( n/N=25/26 , OR 10 .

Example answer:
{"entities": [{"text": "DBP reduction", "type": "Disease"}, {"text": "death", "type": "Disease"}]}

Example input:
Sentence: Clinical tolerability of both agents has been good , with fewer than 3 % of patients withdrawn from treatment because of clinical adverse experiences .

Example answer:
{"entities": []}

Example input:
Sentence: The drug was withdrawn on presentation to hospital in 11 patients , with rapid clinical improvement in 9 .

Example answer:
{"entities": []}

Example input:
Sentence: Response rates according to three sets of criteria were greater with the standard dose ( 55 % -60 % ) than the low dose ( 25 % -35 % ) and placebo ( 25 % -30 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Moderate or severe adverse events were more common in subjects on clonidine ( 79.4 % versus 49.2 % ; p =.0006 ) but not associated with higher rates of early study withdrawal .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Two hundred sixty-five patients were included in this analysis ( n=92 , 93 , and 80 for placebo , low dose , and high dose , respectively ) .

Example answer:
{"entities": []}

Input:
Sentence: Withdrawals occurred in 27.1 % of the high- and 30.7 % of the low-dose groups .

## Item bc5cdr:test:1455
Example input:
Sentence: The protective effect of LY274614 was dose-dependent , being maximum at 10-40 mgkg ( i.p . ) .

Example answer:
{"entities": [{"text": "LY274614", "type": "Chemical"}]}

Example input:
Sentence: Severe toxicity was correlated with the higher cumulative dose of 60 g/m2 of ifosfamide , a younger age ( less than 2 1/2 years old ) , and a predominance of vesicoprostatic tumor involvement .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "tumor", "type": "Disease"}]}

Example input:
Sentence: The recommended starting dose for Phase II trials is 60 mg/m2 IV bolus every 3 weeks .

Example answer:
{"entities": []}

Example input:
Sentence: The protective action of subcutaneously ( SC ) administered antidotes or their combinations in DFP ( 2.0 mg/kg BW ) intoxication was studied in 9-10-weeks-old Han-Wistar male rats .

Example answer:
{"entities": [{"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Thirty-five Wistar rats were given 1.5 mg/kg DOX , i.v. , weekly for up to 8 weeks for a total cumulative dose of 12 mg/kg BW .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: METHODS : For a period of 2 weeks , CsA 15 mg/kg/day ( given orally ) , FK506 3.0 mg/kg/day ( given orally ) or SRL 0.4 mg/kg/day ( given intraperitoneally ) was administered once a day as these doses have earlier been found to achieve a significant immunosuppressive effect in Sprague-Dawley rats .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: PEG 400 impressively decreased both acute high-dose and chronic low-dose-ADR-associated lethality .

Example answer:
{"entities": [{"text": "PEG 400", "type": "Chemical"}]}

Example input:
Sentence: With mild toxicity , a reduction to 30 or 40 mg/kg per dose should result in a reversal of the abnormal results to normal within four weeks .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Total cumulative doses were 36 or 60 g/m2 of ifosfamide ( six or 10 cycles of ifosfamide , vincristine , and dactinomycin [ IVA ] ) .

Example answer:
{"entities": [{"text": "ifosfamide", "type": "Chemical"}, {"text": "ifosfamide , vincristine , and dactinomycin", "type": "Chemical"}, {"text": "IVA", "type": "Chemical"}]}

Example input:
Sentence: Subjects were receiving desferrioxamine ( DFO ) chelation treatment with a mean daily dose of 50-60 mg/kg , 5-6 days a week during the first six years of the study , which was then reduced to 40-50 mg/kg for the following eight years .

Example answer:
{"entities": [{"text": "desferrioxamine", "type": "Chemical"}, {"text": "DFO", "type": "Chemical"}]}

Input:
Sentence: As this schedule exerted more toxicity than needed to investigate protective agents , the protection of ICRF-187 was determined using a dose schedule with lower general toxicity ( 6 weekly doses of 4 mg/kg doxorubicin given i.v .

## Item bc5cdr:test:1739
Example input:
Sentence: Basal CGRP concentration was significantly higher and platelet 5-HT content tended to be lower in subjects who experienced a migraine attack .

Example answer:
{"entities": [{"text": "CGRP", "type": "Chemical"}, {"text": "5-HT", "type": "Chemical"}, {"text": "migraine", "type": "Disease"}]}

Example input:
Sentence: The results suggest the existence of residual beneficial clinical aftereffects of consecutive daily applications of low-frequency rTMS on dyskinesias in PD .

Example answer:
{"entities": [{"text": "dyskinesias", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: Ten patients with PD and prominent dyskinesias had rTMS ( 1,800 pulses ; 1 Hz rate ) delivered over the motor cortex for 4 consecutive days twice , once real stimuli and once sham stimulation were used ; evaluations were done at the baseline and 1 day after the end of each of the treatment series .

Example answer:
{"entities": [{"text": "PD", "type": "Disease"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: The semi-quantitative scoring was significantly worst in the group treated with CsA plus SRL ( P < 0.001 compared with controls ) and the analysis of the total grade of fibrosis also showed the highest proportion in the same group and was significantly different from controls ( P < 0.02 ) .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: Ballistic and choreic dyskinesia were markedly ameliorated , whereas dystonia was not .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}, {"text": "dystonia", "type": "Disease"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: In a placebo-controlled , single-blinded , crossover study , we assessed the effect of `` real '' repetitive transcranial magnetic stimulation ( rTMS ) versus `` sham '' rTMS ( placebo ) on peak dose dyskinesias in patients with Parkinson 's disease ( PD ) .

Example answer:
{"entities": [{"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: However , comparison with the baseline showed small but significant reduction in dyskinesia severity following real rTMS but not placebo .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Similarly , in patient diaries , although both treatments caused reduction in subjective dyskinesia scores during the days of intervention , the effect was sustained for 3 days after the intervention for the real rTMS only .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: In the five rats that developed somatic rigidity , ICP and CVP increased significantly above baseline ( delta ICP 7.5 +/- 1.0 mmHg , delta CVP 5.9 +/- 1.3 mmHg ) .

Example answer:
{"entities": [{"text": "somatic rigidity", "type": "Disease"}]}

Input:
Sentence: About 2/3 of the patients in both Gamma Knife and radiofrequency groups showed improvements in bradykinesia and rigidity , although when considered as a group neither the Gamma Knife nor the radiofrequency group showed statistically significant improvements in UPDRS scores .

## Item bc5cdr:test:1497
Example input:
Sentence: Chronic hyperprolactinemia induced by the dopamine antagonist sulpiride caused a 40 % reduction LH pulse frequency in ovariectomized rats , but only in the presence of chronic low levels of estradiol .

Example answer:
{"entities": [{"text": "hyperprolactinemia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "sulpiride", "type": "Chemical"}, {"text": "estradiol", "type": "Chemical"}]}

Example input:
Sentence: Six- to 9-month old rats receiving prenatal dexamethasone on days 17 and 18 of gestation had a 17 % reduction in glomeruli ( 23 380+/-587 ) compared with control rats ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}]}

Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "Chemical"}, {"text": "Ato-treated", "type": "Chemical"}]}

Example input:
Sentence: Offspring of rats administered dexamethasone on days 15 and 16 gestation had a 20 % reduction in glomerular number compared with control at 6 to 9 months of age ( 22 527+/-509 versus 28 050+/-561 , P < 0.05 ) , which was comparable to the percent reduction in glomeruli measured at 3 weeks of age .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "reduction in glomerular number", "type": "Disease"}]}

Example input:
Sentence: Male rats that received prenatal dexamethasone on days 15 and 16 , 17 and 18 , and 13 and 14 of gestation had elevated blood pressures at 6 months of age ; the latter group did not have a reduction in glomerular number .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "elevated blood pressures", "type": "Disease"}, {"text": "reduction in glomerular number", "type": "Disease"}]}

Example input:
Sentence: HS diet for 4 wk caused a progressive increase in BP , protein and albumin excretion , and glomerular sclerosis in male DS rats , which were attenuated by castration .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: Total cell yields from DES-treated pituitaries increased from 1.3 times control yields at 8 days of treatment to 58.9 times control values by day 150 .

Example answer:
{"entities": [{"text": "DES-treated", "type": "Chemical"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: Over a range of 1-150 days of DES treatment , pairs of control and DES-treated rats were sacrificed , and their pituitaries dissociated enzymatically into single-cell preparations .

Example answer:
{"entities": [{"text": "DES", "type": "Chemical"}, {"text": "DES-treated", "type": "Chemical"}]}

Example input:
Sentence: Pituitary tumors were induced in F344 female rats by chronic treatment with diethylstilbestrol ( DES , 8-10 mg ) implanted subcutaneously in silastic capsules .

Example answer:
{"entities": [{"text": "Pituitary tumors", "type": "Disease"}, {"text": "diethylstilbestrol", "type": "Chemical"}, {"text": "DES", "type": "Chemical"}]}

Input:
Sentence: Ten weeks of diethylstilbestrol ( DES ) treatment caused female F344 rat pituitaries to grow to an average of 109.2 +/- 6.3 mg ( mean +/- SE ) versus 11.3 +/- 1.4 mg for untreated rats , and to become highly hemorrhagic .

## Item bc5cdr:test:2012
Example input:
Sentence: It was found that he was a poor metabolizer of all four drugs , indicating that their metabolism is under the same genetic control .

Example answer:
{"entities": []}

Example input:
Sentence: Effect of some anticancer drugs and combined chemotherapy on renal toxicity .

Example answer:
{"entities": [{"text": "renal toxicity", "type": "Disease"}]}

Example input:
Sentence: INTRODUCTION : Many substances that form methemoglobin ( MHb ) effectively counter cyanide ( CN ) toxicity .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: However , combinations of different therapeutic regimens require consideration of potential adverse reactions .

Example answer:
{"entities": []}

Example input:
Sentence: Moreover , the coadministration of these frequently used drugs is expected to be especially harmful in this subgroup of patients .

Example answer:
{"entities": []}

Example input:
Sentence: In conclusion , CPA , diazepam and 2PAM in combination with atropine prevented the occurrence of serious signs of poisoning and thus reduced the toxicity of DFP in rat .

Example answer:
{"entities": [{"text": "CPA", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "atropine", "type": "Chemical"}, {"text": "poisoning", "type": "Disease"}, {"text": "toxicity", "type": "Disease"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: Both compounds caused deformations and lethality in a dose-dependent manner .

Example answer:
{"entities": [{"text": "deformations", "type": "Disease"}]}

Example input:
Sentence: Haematological toxicity was greater for the combination than AraG alone , although median time to neutrophil and platelet recovery was consistent with other salvage therapies .

Example answer:
{"entities": [{"text": "Haematological toxicity", "type": "Disease"}, {"text": "AraG", "type": "Chemical"}]}

Example input:
Sentence: A lower relative risk would be expected for acetaminophen if the risk of both drugs in combination with other analgesics was higher than the risk of either agent alone .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}]}

Example input:
Sentence: of a combination of 3 drugs : 6 mg. papaverine , 100 micrograms .

Example answer:
{"entities": [{"text": "papaverine", "type": "Chemical"}]}

Input:
Sentence: In combination , these substances are substantially more toxic than either drug alone .

## Item bc5cdr:test:1725
Example input:
Sentence: In the remaining 12 patients , localised computed tomography of the gall bladder showed that eight had stones with maximum attenuation scores of < 100 Hounsfield units ( values of < 100 HU predict cholesterol rich , dissolvable stones ) .

Example answer:
{"entities": [{"text": "cholesterol", "type": "Chemical"}]}

Example input:
Sentence: Patients were admitted to the hospital for measurement of lithium level , creatinine clearance , urine volume , and maximum osmolality .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: The associated urinary concentrating defect is reversible only during the early stages of structural damage to the inner medulla .

Example answer:
{"entities": []}

Example input:
Sentence: There were no severe events and there was no need to interrupt the examinations .

Example answer:
{"entities": []}

Example input:
Sentence: Both obstructive ( P less than 0.05 ) and central apnoea ( P less than 0.05 ) occurred more frequently in patients who had a morphine infusion .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: Although the intraocular pressure elevation caused by secondary acute angle-closure glaucoma decreased and ocular pain diminished , inexorable papilledema and exudative retinal detachment continued for 3 weeks .

Example answer:
{"entities": [{"text": "glaucoma", "type": "Disease"}, {"text": "ocular pain", "type": "Disease"}, {"text": "papilledema", "type": "Disease"}, {"text": "retinal detachment", "type": "Disease"}]}

Example input:
Sentence: Here we show that perceived pain intensity in secondary hyperalgesia is decreased when attention is distracted away from the painful pinprick stimulus with a visual task .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "hyperalgesia", "type": "Disease"}]}

Example input:
Sentence: By using transthoracic echocardiography , anterior and posterior wall thickness , LV diameters and LV fractional shortening ( FS ) were measured in all rats before DOX or saline , and at weeks 6 and 9 after treatment in all surviving rats .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: Extracorporeal lithotripsy successfully removed a renal calculus in one patient and surgery removed a staghorn calculus in another , permitting continued treatment .

Example answer:
{"entities": [{"text": "renal calculus", "type": "Disease"}, {"text": "calculus", "type": "Disease"}]}

Example input:
Sentence: In other individuals with no underlying atherosclerotic obstruction , coronary occlusion may be due to spasm , thrombus , or both .

Example answer:
{"entities": [{"text": "atherosclerotic obstruction", "type": "Disease"}, {"text": "coronary occlusion", "type": "Disease"}, {"text": "spasm", "type": "Disease"}, {"text": "thrombus", "type": "Disease"}]}

Input:
Sentence: The calculi are not opaque , and secondary signs of obstruction may be absent or minimal and should be sought carefully .

## Item bc5cdr:test:1751
Example input:
Sentence: This is a case report of euphoria and choreoathetoid movements both transiently induced by rapid adjustment to the selective mu-opioid receptor agonist methadone in an inpatient previously abusing heroine and cocaine .

Example answer:
{"entities": [{"text": "choreoathetoid movements", "type": "Disease"}, {"text": "methadone", "type": "Chemical"}, {"text": "heroine", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: The remaining patient in the series developed fulminant hepatitis when the drug was accidentally recommenced 1 year after a prior episode of methyldopa-induced hepatitis .

Example answer:
{"entities": [{"text": "fulminant hepatitis", "type": "Disease"}, {"text": "methyldopa-induced", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: We report an undiagnosed case of myotonia congenita in a 24-year-old previously healthy primigravida , who developed life threatening masseter spasm following a standard dose of intravenous suxamethonium for induction of anaesthesia .

Example answer:
{"entities": [{"text": "myotonia congenita", "type": "Disease"}, {"text": "masseter spasm", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: We report the increased amount of motor disability in four patients with idiopathic Parkinson 's disease after exposure to the antidepressant fluoxetine .

Example answer:
{"entities": [{"text": "motor disability", "type": "Disease"}, {"text": "idiopathic Parkinson 's disease", "type": "Disease"}, {"text": "antidepressant", "type": "Chemical"}, {"text": "fluoxetine", "type": "Chemical"}]}

Example input:
Sentence: Cerebral vasculitis following oral methylphenidate intake in an adult : a case report .

Example answer:
{"entities": [{"text": "Cerebral vasculitis", "type": "Disease"}, {"text": "methylphenidate", "type": "Chemical"}]}

Example input:
Sentence: The case of a nonepileptic patient who developed psychosis following phenytoin treatment for trigeminal neuralgia is described .

Example answer:
{"entities": [{"text": "psychosis", "type": "Disease"}, {"text": "phenytoin", "type": "Chemical"}, {"text": "trigeminal neuralgia", "type": "Disease"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: We conclude that methylphenidate mediated vasculitis should be considered in patients with neurological symptoms and a history of methylphenidate therapy .

Example answer:
{"entities": [{"text": "methylphenidate", "type": "Chemical"}, {"text": "vasculitis", "type": "Disease"}]}

Example input:
Sentence: Cerebral vasculitis associated with amphetamine abuse is well documented , and in rare cases ischaemic stroke has been reported after methylphenidate intake in children .

Example answer:
{"entities": [{"text": "Cerebral vasculitis", "type": "Disease"}, {"text": "amphetamine abuse", "type": "Disease"}, {"text": "ischaemic stroke", "type": "Disease"}, {"text": "methylphenidate", "type": "Chemical"}]}

Example input:
Sentence: We report the case of a 63-year-old female who was treated with methylphenidate due to hyperactivity and suffered from multiple ischaemic strokes .

Example answer:
{"entities": [{"text": "methylphenidate", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "ischaemic strokes", "type": "Disease"}]}

Input:
Sentence: This is the first reported patient with neuroleptic malignant syndrome probably caused by methylphenidate .

## Item bc5cdr:test:1861
Example input:
Sentence: Their ototoxicity is a serious health problem and , as their ototoxic mechanism involves the production of NO , we need to assess the use of NO inhibitors for the prevention of aminoglycoside-induced sensorineural hearing loss .

Example answer:
{"entities": [{"text": "ototoxicity", "type": "Disease"}, {"text": "ototoxic", "type": "Disease"}, {"text": "NO", "type": "Chemical"}, {"text": "aminoglycoside-induced", "type": "Chemical"}, {"text": "sensorineural hearing loss", "type": "Disease"}]}

Example input:
Sentence: NRA0160 and clozapine antagonized locomotor hyperactivity induced by methamphetamine ( MAP ) in mice .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "MAP", "type": "Chemical"}]}

Example input:
Sentence: THP exhibited an antipsychotic-like profile by potentiating haloperidol-induced catalepsy , reducing amphetamine-induced hyperactivity and reducing apomorphine-induced climbing in mice .

Example answer:
{"entities": []}

Example input:
Sentence: This study aimed at investigating the potential antipsychotic-like properties of SSR103800 , with a particular focus on models of hyperactivity , involving either drug challenge ( ie , amphetamine and MK-801 ) or transgenic mice ( ie , NMDA Nr1 ( neo-/- ) and DAT ( -/- ) ) .

Example answer:
{"entities": [{"text": "SSR103800", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "MK-801", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}]}

Example input:
Sentence: The data strengthen the evidence that the neurotoxic effect of amphetamine and related compounds toward nigrostriatal dopamine neurons involves NMDA receptors and that LY274614 is an NMDA receptor antagonist with long-lasting in vivo effects in rats .

Example answer:
{"entities": [{"text": "neurotoxic", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "LY274614", "type": "Chemical"}]}

Example input:
Sentence: Previous clinical studies have proposed that risperidone 's pharmacologic profile may produce improved efficacy for negative psychotic symptoms and decreased propensity for extrapyramidal side effects ; features shared by so-called 'atypical ' neuroleptics .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}, {"text": "psychotic symptoms", "type": "Disease"}]}

Example input:
Sentence: However , the observation that antagonists of the glutamate N-methyl-D-aspartate ( NMDA ) receptor produce schizophrenic-like symptoms in humans has led to the idea of a dysfunctioning of the glutamatergic system via its NMDA receptor .

Example answer:
{"entities": [{"text": "glutamate", "type": "Chemical"}, {"text": "N-methyl-D-aspartate", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "schizophrenic-like", "type": "Disease"}]}

Example input:
Sentence: NRA0160 and clozapine significantly reversed the disruption of prepulse inhibition ( PPI ) in rats produced by apomorphine .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "apomorphine", "type": "Chemical"}]}

Example input:
Sentence: These findings suggest that NRA0160 may have unique antipsychotic activities without the liability of motor side effects typical of classical antipsychotics .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}]}

Example input:
Sentence: As a result , there is a growing interest in the development of pharmacological agents with potential antipsychotic properties that enhance the activity of the glutamatergic system via a modulation of the NMDA receptor .

Example answer:
{"entities": [{"text": "NMDA", "type": "Chemical"}]}

Input:
Sentence: CONCLUSIONS : The results give further support to the hypothesis that NO plays a role in motor behavior control and suggest that it may take part in the synaptic changes produced by antipsychotic treatment .

## Item bc5cdr:test:1335
Example input:
Sentence: RESULTS : Sensitivity to several convulsion endpoints induced by nicotine , carbachol , and neostigmine were significantly greater in WSR versus WSP mice .

Example answer:
{"entities": [{"text": "convulsion", "type": "Disease"}, {"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}]}

Example input:
Sentence: VPU was more potent than VPA , exhibiting the median effective dose ( ED ( 50 ) ) of 49 mg/kg in protecting rats against pilocarpine-induced seizure whereas the corresponding value for VPA was 322 mg/kg .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: For each of the three tested calcium channel blockers ( diltiazem , verapamil and bepridil ) 6 groups of mice were treated by two different doses , i.e .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "bepridil", "type": "Chemical"}]}

Example input:
Sentence: The extent of inhibition of brain cholinesterase activity evoked by DCE at the dose of 400 mg/kg was 22 % in young and 19 % in aged mice .

Example answer:
{"entities": [{"text": "DCE", "type": "Chemical"}]}

Example input:
Sentence: Thus , FS containing 47.5 mg/ml tAMCA evoked generalized seizures in all tested rats ( n=6 ) while the lowest concentration of tAMCA ( 0.5 mg/ml ) only evoked brief episodes of jerk-correlated convulsive potentials in 1 of 6 rats .

Example answer:
{"entities": [{"text": "tAMCA", "type": "Chemical"}, {"text": "generalized seizures", "type": "Disease"}, {"text": "convulsive", "type": "Disease"}]}

Example input:
Sentence: Apamin , a selective blocker of calcium-dependent potassium channels , was administered intracerebroventricularly in rats anesthetized with 0.8 % sevoflurane to investigate the mechanism of the anticonvulsive effects .

Example answer:
{"entities": [{"text": "Apamin", "type": "Chemical"}, {"text": "calcium-dependent", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}, {"text": "sevoflurane", "type": "Chemical"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: In behavioral studies , pre-treatment of mice with BD1018 , BD1063 , or LR132 significantly attenuated cocaine-induced convulsions and lethality .

Example answer:
{"entities": [{"text": "BD1018", "type": "Chemical"}, {"text": "BD1063", "type": "Chemical"}, {"text": "LR132", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}]}

Example input:
Sentence: Apamin ( 10 ng ) had a tendency to decrease the convulsive threshold ( 21.6 +/- 2.2 to 19.9 +/- 2.5 mg. l ( -1 ) ) but this was not statistically significant .

Example answer:
{"entities": [{"text": "Apamin", "type": "Chemical"}, {"text": "convulsive", "type": "Disease"}]}

Example input:
Sentence: The rats received AChE reactivator pralidoxime-2-chloride ( 2PAM ) ( 30.0 mg/kg BW ) , anticonvulsant diazepam ( 2.0 mg/kg BW ) , A ( 1 ) -adenosine receptor agonist N ( 6 ) -cyclopentyl adenosine ( CPA ) ( 2.0 mg/kg BW ) , NMDA-receptor antagonist dizocilpine maleate ( +-MK801 hydrogen maleate ) ( 2.0 mg/kg BW ) or their combinations with cholinolytic drug atropine sulfate ( 50.0 mg/kg BW ) immediately or 30 min after the single SC injection of DFP .

Example answer:
{"entities": [{"text": "pralidoxime-2-chloride", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "N ( 6 ) -cyclopentyl adenosine", "type": "Chemical"}, {"text": "CPA", "type": "Chemical"}, {"text": "NMDA-receptor", "type": "Chemical"}, {"text": "dizocilpine maleate", "type": "Chemical"}, {"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Input:
Sentence: S-312 , S-312-d , but not S-312-l , L-type calcium channel antagonists , showed anticonvulsant effects on the audiogenic tonic convulsions in DBA/2 mice ; and their ED50 values were 18.4 ( 12.8-27.1 ) mg/kg , p.o .

## Item bc5cdr:test:1695
Example input:
Sentence: In 7 of the 28 patients there was a striking temporal association between the initiation of sirolimus and the development of nephrotic-range proteinuria .

Example answer:
{"entities": [{"text": "sirolimus", "type": "Chemical"}, {"text": "nephrotic-range", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: Proteinuria increased significantly from a median of 0.13 g/day ( range 0-5.7 ) preswitch to 0.23 g/day ( 0-9.88 ) at 24 months postswitch ( p = 0.0024 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Development of proteinuria after switch to sirolimus-based immunosuppression in long-term cardiac transplant patients .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "sirolimus-based", "type": "Chemical"}]}

Example input:
Sentence: Before the switch , 11.5 % of patients had high-grade proteinuria ( > 1.0 g/day ) ; this increased to 22.9 % postswitch ( p = 0.006 ) .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: Before conversion 8 ( 32 % ) patients had no proteinuria , whereas afterwards all patients had proteinuria .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: Patients without proteinuria had increased renal function ( median 42.5 vs. 64.1 , p = 0.25 ) , whereas patients who developed high-grade proteinuria showed decreased renal function at the end of follow-up ( median 39.6 vs. 29.2 , p = 0.125 ) .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: Whether proteinuria was due to sirolimus or only a consequence of calcineurin inhibitors withdrawal remained unsolved until high range proteinuria has been observed during sirolimus therapy in islet transplantation and in patients who received sirolimus de novo .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "sirolimus", "type": "Chemical"}]}

Example input:
Sentence: Two subsets of patients were identified from this latter group : the first included four patients ( 5 % of the total population ) who developed major toxicity resulting in Fanconi 's syndrome ( TDFS ) ; and the second group included five patients with elevated beta 2 microglobulinuria and low phosphate reabsorption .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "Fanconi 's syndrome", "type": "Disease"}, {"text": "TDFS", "type": "Disease"}, {"text": "phosphate", "type": "Chemical"}]}

Example input:
Sentence: She was treated with heparin , dipyridamole and hemodialysis ; and after more than three months , her urinary output rose above 500 ml ; and six months after the onset of anuria , dialysis treatment was stopped .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "anuria", "type": "Disease"}]}

Example input:
Sentence: Three yr after transplantation she developed renal Fanconi syndrome with severe metabolic acidosis , hypophosphatemia , glycosuria , and aminoaciduria .

Example answer:
{"entities": [{"text": "renal Fanconi syndrome", "type": "Disease"}, {"text": "metabolic acidosis", "type": "Disease"}, {"text": "hypophosphatemia", "type": "Disease"}, {"text": "glycosuria", "type": "Disease"}, {"text": "aminoaciduria", "type": "Disease"}]}

Input:
Sentence: He gave a five-year history of polyuria and polydipsia , during which time urinalysis had been negative for glucose .

## Item bc5cdr:test:1474
Example input:
Sentence: None of the animals that received bupivacaine , normal saline , or normal saline titrated to a pH 3.0 developed hind-limb paralysis .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}, {"text": "paralysis", "type": "Disease"}]}

Example input:
Sentence: Patients given prilocaine were more likely to develop hearing loss ( 10 out of 22 ) than those given bupivacaine ( 4 out of 22 ) ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "prilocaine", "type": "Chemical"}, {"text": "hearing loss", "type": "Disease"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: The purpose of this study was to investigate the influence of calcium channel blockers on bupivacaine-induced acute toxicity .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "bupivacaine-induced", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Mediation of enhanced reflex vagal bradycardia by L-dopa via central dopamine formation in dogs .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "L-dopa", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: The effects of aminophylline on the ventricular fibrillation threshold during normal acid-base conditions and during respiratory failure were studied in anesthetized open chest dogs .

Example answer:
{"entities": [{"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}, {"text": "respiratory failure", "type": "Disease"}]}

Example input:
Sentence: UM-272 ( N , N-dimethylpropranolol ) , a quaternary antiarrhythmic agent , was administered sublingually to dogs with ouabain-induced ventricular tachycardias .

Example answer:
{"entities": [{"text": "UM-272", "type": "Chemical"}, {"text": "N , N-dimethylpropranolol", "type": "Chemical"}, {"text": "ouabain-induced", "type": "Chemical"}, {"text": "ventricular tachycardias", "type": "Disease"}]}

Example input:
Sentence: The convulsant activity of bupivacaine was not significantly modified but calcium channel blockers decreased the time of latency to obtain bupivacaine-induced convulsions ; this effect was less pronounced with bepridil .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "bupivacaine-induced", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "bepridil", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Input:
Sentence: Bupivacaine antagonizes epinephrine dysrhythmogenicity in conscious dogs susceptible to VT and in anesthetized dogs with spontaneous postinfarct dysrhythmias .

## Item bc5cdr:test:1939
Example input:
Sentence: CONCLUSION : Complications associated with epidural steroid injections are rare .

Example answer:
{"entities": [{"text": "steroid", "type": "Chemical"}]}

Example input:
Sentence: This is a case report of euphoria and choreoathetoid movements both transiently induced by rapid adjustment to the selective mu-opioid receptor agonist methadone in an inpatient previously abusing heroine and cocaine .

Example answer:
{"entities": [{"text": "choreoathetoid movements", "type": "Disease"}, {"text": "methadone", "type": "Chemical"}, {"text": "heroine", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Both obstructive ( P less than 0.05 ) and central apnoea ( P less than 0.05 ) occurred more frequently in patients who had a morphine infusion .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Example input:
Sentence: There was also a higher incidence of tachyarrhythmias ( P less than 0.05 ) and ventricular ectopic beats ( P less than 0.05 ) in the morphine infusion group .

Example answer:
{"entities": [{"text": "tachyarrhythmias", "type": "Disease"}, {"text": "ventricular ectopic beats", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: After verifying the epidural space , bupivacaine and triamcinolone diacetate were injected .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}, {"text": "triamcinolone diacetate", "type": "Chemical"}]}

Example input:
Sentence: Simultaneous administration of morphine with metamizol resulted in a markedly antinociceptive potentiation and an increasing of the duration of action after a single ( 298+/-7 vs. 139+/-36 units area ( ua ) ; P < 0.001 ) and repeated administration ( 280+/-17 vs. 131+/-22 ua ; P < 0.001 ) .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "metamizol", "type": "Chemical"}]}

Example input:
Sentence: The following case is a report of cauda equina syndrome possibly caused by epidural injection of triamcinolone and bupivacaine .

Example answer:
{"entities": [{"text": "cauda equina syndrome", "type": "Disease"}, {"text": "triamcinolone", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: Cauda equina syndrome is a rare complication of epidural anesthesia .

Example answer:
{"entities": [{"text": "Cauda equina syndrome", "type": "Disease"}]}

Example input:
Sentence: infusion of morphine ( mean 73.6 mg ) and five patients receiving a continuous extradural infusion of 0.25 % bupivacaine ( mean 192 mg ) in the 24-h period following upper abdominal surgery .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Input:
Sentence: Although there have been case reports of epidural morphine with these symptoms and signs , this has not been previously documented with IV or patient-controlled analgesia morphine .

## Item bc5cdr:test:2059
Example input:
Sentence: By using transthoracic echocardiography , anterior and posterior wall thickness , LV diameters and LV fractional shortening ( FS ) were measured in all rats before DOX or saline , and at weeks 6 and 9 after treatment in all surviving rats .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : If ECG alone is used for specificity , the combination with dP/dtejc improved the sensitivity of the test and could be a cost-savings alternative to cardiac imaging or perfusion studies to detect myocardial ischemia , especially in patients unable to exercise .

Example answer:
{"entities": [{"text": "myocardial ischemia", "type": "Disease"}]}

Example input:
Sentence: A reproducible model for producing diffuse myocardial injury ( epinephrine infusion ) has been developed to study the cardioprotective effects of agents or maneuvers which might alter the evolution of acute myocardial infarction .

Example answer:
{"entities": [{"text": "myocardial injury", "type": "Disease"}, {"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Sublingual UM-272 converted ventricular tachycardia to sinus rhythm in all 5 dogs .

Example answer:
{"entities": [{"text": "UM-272", "type": "Chemical"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: Epicardial coronary collateral vessels were demonstrated in all four patients ; a coronary `` steal '' phenomenon may be the mechanism of the dipyridamole-induced ischemia observed .

Example answer:
{"entities": [{"text": "dipyridamole-induced", "type": "Chemical"}, {"text": "ischemia", "type": "Disease"}]}

Example input:
Sentence: Mediation of enhanced reflex vagal bradycardia by L-dopa via central dopamine formation in dogs .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "L-dopa", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: The ventricular fibrillation threshold was measured by passing a gated train of 12 constant current pulses through the ventricular myocardium during the vulnerable period of the cardiac cycle .

Example answer:
{"entities": [{"text": "ventricular fibrillation", "type": "Disease"}]}

Example input:
Sentence: Simultaneous measurements of ECG and brachial artery dP/dtejc were performed at each dobutamine level .

Example answer:
{"entities": [{"text": "dobutamine", "type": "Chemical"}]}

Example input:
Sentence: At termination of the experiments , mice underwent echocardiography , quantitation of abundance of molecular markers of CM ( ventricular mRNA encoding atrial natriuretic factor [ ANF ] and sarcoplasmic calcium ATPase [ SERCA2 ] ) , and determination of plasma LA .

Example answer:
{"entities": [{"text": "CM", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "LA", "type": "Chemical"}]}

Input:
Sentence: METHODS AND RESULTS : Transmembrane action potentials from epicardium , midmyocardium , and endocardium were recorded simultaneously , together with a transmural ECG , in arterially perfused canine and rabbit left ventricular preparations .

## Item bc5cdr:test:1943
Example input:
Sentence: Left ventricular filling pressure decreased from 19 +/- 2 to 11 +/- 2 mm Hg ( P less than 0.001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: After 35 days in the TG + HAART cohort , left ventricular mass increased 160 % by echocardiography .

Example answer:
{"entities": []}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: These rats also showed declines in left ventricular systolic pressure , maximum and minimum rate of developed left ventricular pressure , and elevation of left ventricular end-diastolic pressure and ST-segment .

Example answer:
{"entities": []}

Example input:
Sentence: After starting PGE1 or TMP , MAP and rate pressure product ( RPP ) decreased significantly compared with preinfusion values ( P < 0.01 ) , and the degree of hypotension due to PGE1 remained constant until 60 min after its discontinuation .

Example answer:
{"entities": [{"text": "PGE1", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Isoproterenol pretreatment for 15 days caused cardiac hypertrophy without affecting baseline blood pressure and heart rate .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "Chemical"}, {"text": "cardiac hypertrophy", "type": "Disease"}]}

Example input:
Sentence: By using transthoracic echocardiography , anterior and posterior wall thickness , LV diameters and LV fractional shortening ( FS ) were measured in all rats before DOX or saline , and at weeks 6 and 9 after treatment in all surviving rats .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: In isolated perfused heart preparations from isoproterenol-pretreated rats , the isoproterenol-induced maximal increase in left ventricular systolic pressure was significantly reduced , compared with saline-pretreated rats ( the EC50 of the isoproterenol-induced increase in left ventricular systolic pressure was enhanced approximately 22-fold ) .

Example answer:
{"entities": [{"text": "isoproterenol-pretreated", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: End-diastolic ( ED ) and end-systolic ( ES ) LV diameters/BW significantly increased , whereas LV FS was decreased after 9 weeks in the DOX group ( p < 0.001 ) .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: Subsequent addition of phenylephrine infusion , sufficient to re-elevate mean arterial pressure to 106 +/- 4 mm Hg ( P less than 0.001 ) for 30 minutes , increased left ventricular filling pressure to 17 +/- 2 mm Hg ( P less than 0.05 ) and also significantly increased sigmaST ( P less than 0.05 ) .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}]}

Input:
Sentence: Heart rate ( HR ) , mean arterial pressure ( MBP ) , positive rate of increase of left ventricular pressure ( +LVdP/dt ) , echocardiographically assessed left ventricular ejection fraction ( LVEF ) , and fractional shortening ( FS ) , as well as chronotropic response to isoproterenol and exercise-induced sympathetic stimulation were evaluated under baseline and posttreatment conditions .

## Item bc5cdr:test:1589
Example input:
Sentence: Previous studies have demonstrated an increased risk of venous thromboembolism ( VTE ) associated with CPA/EE compared with conventional combined oral contraceptives ( COCs ) .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "VTE", "type": "Disease"}, {"text": "CPA/EE", "type": "Chemical"}, {"text": "oral contraceptives", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : The addition of thalidomide to docetaxel in the treatment of prostate cancer significantly increases the frequency of VTE .

Example answer:
{"entities": [{"text": "thalidomide", "type": "Chemical"}, {"text": "docetaxel", "type": "Chemical"}, {"text": "prostate cancer", "type": "Disease"}, {"text": "VTE", "type": "Disease"}]}

Example input:
Sentence: MEASUREMENTS AND MAIN RESULTS : None of 23 patients who received docetaxel alone developed VTE , whereas 9 of 47 patients ( 19 % ) who received docetaxel plus thalidomide developed VTE ( p=0.025 ) .

Example answer:
{"entities": [{"text": "docetaxel", "type": "Chemical"}, {"text": "VTE", "type": "Disease"}, {"text": "thalidomide", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : We have demonstrated an increased risk of VTE associated with the use of CPA/EE in women with acne , hirsutism or PCOS although residual confounding by indication can not be excluded .

Example answer:
{"entities": [{"text": "VTE", "type": "Disease"}, {"text": "CPA/EE", "type": "Chemical"}, {"text": "acne", "type": "Disease"}, {"text": "hirsutism", "type": "Disease"}, {"text": "PCOS", "type": "Disease"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: The results with respect to the use of third-generation oral contraceptives were inconclusive but suggested that the risk was lower than the risk associated with second-generation oral contraceptives .

Example answer:
{"entities": [{"text": "oral contraceptives", "type": "Chemical"}]}

Example input:
Sentence: Among women who used oral contraceptives , the odds ratio was 2.1 ( 95 percent confidence interval , 1.5 to 3.0 ) for those without a prothrombotic mutation and 1.9 ( 95 percent confidence interval , 0.6 to 5.5 ) for those with a mutation CONCLUSIONS : The risk of myocardial infarction was increased among women who used second-generation oral contraceptives .

Example answer:
{"entities": [{"text": "oral contraceptives", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: The adjusted rate ratio of VTE for repeat users of third generation OC was 0.6 ( 95 % CI:0.3-1.2 ) relative to repeat users of second generation pills , whereas it was 1.3 ( 95 % CI:0.7-2.4 ) for switchers from second to third generation pills relative to switchers from third to second generation pills .

Example answer:
{"entities": [{"text": "VTE", "type": "Disease"}, {"text": "OC", "type": "Chemical"}]}

Example input:
Sentence: We conclude that second and third generation agents are associated with equivalent risks of VTE when the same agent is used repeatedly after interruption periods or when users are switched between the two generations of pills .

Example answer:
{"entities": [{"text": "VTE", "type": "Disease"}]}

Example input:
Sentence: We investigated this association , according to the type of progestagen included in third-generation ( i.e. , desogestrel or gestodene ) and second-generation ( i.e. , levonorgestrel ) oral contraceptives , the dose of estrogen , and the presence or absence of prothrombotic mutations METHODS : In a nationwide , population-based , case-control study , we identified and enrolled 248 women 18 through 49 years of age who had had a first myocardial infarction between 1990 and 1995 and 925 control women who had not had a myocardial infarction and who were matched for age , calendar year of the index event , and area of residence .

Example answer:
{"entities": [{"text": "progestagen", "type": "Chemical"}, {"text": "desogestrel", "type": "Chemical"}, {"text": "gestodene", "type": "Chemical"}, {"text": "levonorgestrel", "type": "Chemical"}, {"text": "oral contraceptives", "type": "Chemical"}, {"text": "estrogen", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Input:
Sentence: Among users of third-generation progestagens , the risk of VTE was higher in users of desogestrel with 20 g ethinyloestradiol than in users of gestodene or desogestrel with 30 g ethinyloestradiol .

## Item bc5cdr:test:2003
Example input:
Sentence: His bundle recordings showed an atrial tachycardia with intermittent exit block and greatly prolonged BH and HV intervals ( 40 and 100 msec , respectively ) .

Example answer:
{"entities": [{"text": "atrial tachycardia", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Compared to controls , aortic regurgitation ( OR : 3.1 ; 95 % IC : 1.1-8.8 ) and mitral regurgitation ( OR : 10.7 ; 95 % IC : 2.1-53 ) were more frequent in PD patients ( tricuspid : NS ) .

Example answer:
{"entities": [{"text": "aortic regurgitation", "type": "Disease"}, {"text": "mitral regurgitation", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: A patient is reported who developed progressive cardiomyopathy two and one-half years after receiving 580 mg/m2 which apparently represents late , late cardiotoxicity .

Example answer:
{"entities": [{"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: A second echocardiography was performed ( median interval : 13 months ) after pergolide withdrawal ( n=10 patients ) .

Example answer:
{"entities": [{"text": "pergolide", "type": "Chemical"}]}

Example input:
Sentence: The duration of the examination and the mean ejection fraction ( EF ) were 16.4+/-6.1 minutes and 60+/-9 % , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: Echocardiographic data from the experimental group of 21 patients ( mean age 16 +/- 5 years ) treated from 1.6 to 14.3 years ( median 5.3 ) before this study with 27 to 532 mg/m2 of doxorubicin ( mean 196 ) were compared with echocardiographic data from 12 normal age-matched control subjects .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "Chemical"}]}

Example input:
Sentence: Analysis was performed on 61 women with chemotherapy-responsive metastatic breast cancer receiving 96-h infusional cyclophosphamide as part of a triple sequential high-dose regimen to assess association between presence of peritransplant congestive heart failure ( CHF ) and the following pretreatment characteristics : presence of electrocardiogram ( EKG ) abnormalities , age , hypertension , prior cardiac history , smoking , diabetes mellitus , prior use of anthracyclines , and left-sided chest irradiation .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "CHF", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "diabetes mellitus", "type": "Disease"}, {"text": "anthracyclines", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Six of 61 women ( 10 % ) developed clinically reversible grade 3 CHF following infusional cyclophosphamide with a median percent decline in ejection fraction of 31 % .

Example answer:
{"entities": [{"text": "CHF", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}]}

Example input:
Sentence: After 35 days in the TG + HAART cohort , left ventricular mass increased 160 % by echocardiography .

Example answer:
{"entities": []}

Example input:
Sentence: Subjects were 1210 inpatients with New York Heart Association ( NYHA ) functional class II and III .

Example answer:
{"entities": []}

Input:
Sentence: Patients with New York Heart Association classes II to IV CHF and left ventricular ejection fractions of no greater than 0.30 ( n = 3164 ) were randomized and followed up for a median of 46 months .

## Item bc5cdr:test:1593
Example input:
Sentence: Pyrrolidine dithiocarbamate protects the piriform cortex in the pilocarpine status epilepticus model .

Example answer:
{"entities": [{"text": "Pyrrolidine dithiocarbamate", "type": "Chemical"}, {"text": "pilocarpine", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}]}

Example input:
Sentence: This prolonged depletion of dopamine in the striatum was antagonized by dizocilpine ( MK-801 , a non-competitive antagonist of NMDA receptors ) or by LY274614 ( a competitive antagonist of NMDA receptors ) .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "dizocilpine", "type": "Chemical"}, {"text": "MK-801", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "LY274614", "type": "Chemical"}]}

Example input:
Sentence: Three hundred fifty-five adult male CSS mice , 58 B6 , and 39 A/J were tested for susceptibility to pilocarpine-induced seizures .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: The electrophysiological recording in vitro showed that Rg1 restored the LTP in slices from the rats treated with morphine , but not changed LTP in the slices from normal saline- or morphine/Rg1-treated rats ; this restoration could be inhibited by N-methyl-D-aspartate ( NMDA ) receptor antagonist MK801 .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}, {"text": "morphine/Rg1-treated", "type": "Chemical"}, {"text": "N-methyl-D-aspartate", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "MK801", "type": "Chemical"}]}

Example input:
Sentence: Therefore , like VPA , the finding that VPU could drastically reduce pilocarpine-induced increases in glutamate and aspartate should account , at least partly , for its anticonvulsant activity observed in pilocarpine-induced seizure in experimental animals .

Example answer:
{"entities": [{"text": "VPA", "type": "Chemical"}, {"text": "VPU", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: A comparable overexpression of Pgp in the BBB was obtained after pilocarpine-induced seizures in wild-type Wistar rats .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: Based on the finding that VPU and VPA could protect the animals against pilocarpine-induced seizure it is suggested that the reduction of inhibitory amino acid neurotransmitters was comparatively minor and offset by a pronounced reduction of glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: In addition , PD female rats showed increased ( 3 ) H-MK-801 binding in the striatum and hippocampus , but not in the cortex .

Example answer:
{"entities": [{"text": "H-MK-801", "type": "Chemical"}]}

Example input:
Sentence: VPU was more potent than VPA , exhibiting the median effective dose ( ED ( 50 ) ) of 49 mg/kg in protecting rats against pilocarpine-induced seizure whereas the corresponding value for VPA was 322 mg/kg .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Input:
Sentence: MK-801 augments pilocarpine-induced electrographic seizure but protects against brain damage in rats .

## Item bc5cdr:test:2074
Example input:
Sentence: Patients with stage D2-3 disease , abnormal hemoglobin level or renal and liver function tests that were higher than the upper limits were excluded from the study .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : Retrospective review of medical records of 236 patients with hyperthyroidism admitted in our department ( in- or out-patients ) from 1986 to 1992 .

Example answer:
{"entities": [{"text": "hyperthyroidism", "type": "Disease"}]}

Example input:
Sentence: All patients recovered without sequelae .

Example answer:
{"entities": []}

Example input:
Sentence: Of 24 evaluable patients , two achieved a complete remission and one achieved a partial remission for an overall response rate of 12.5 % ( 95 % confidence interval : 2.6-32.4 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Initial brain magnetic resonance imaging ( MRI ) were obtained after the hospitalization , including DWI ( 8/8 ) , apparent diffusion coefficient ( ADC ) map ( 4/8 ) , FLAIR ( 7/8 ) , and T2-weighted image ( 8/8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Fewer than 6 % of patients in either group were considered by the investigator to have a worsening of their overall disease condition during the study .

Example answer:
{"entities": []}

Example input:
Sentence: She was admitted to the medical intensive care unit , venlafaxine was discontinued , and no further sequelae were seen .

Example answer:
{"entities": [{"text": "venlafaxine", "type": "Chemical"}]}

Example input:
Sentence: Patients were admitted to the hospital for measurement of lithium level , creatinine clearance , urine volume , and maximum osmolality .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: METHODS : a total of 13 patients were referred to the Danish Cholinesterase Research Unit after ECT during 38 months .

Example answer:
{"entities": []}

Example input:
Sentence: Before treatment all patients had a cardiac evaluation and during treatment serial ECG recordings were performed .

Example answer:
{"entities": []}

Input:
Sentence: All patients were admitted to the hospital for serial testing after the DSE testing in the intensive diagnostic and treatment unit .
