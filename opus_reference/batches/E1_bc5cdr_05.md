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

## Item bc5cdr:test:926
Example input:
Sentence: RESULTS : Bilateral infusions of neurotensin into the globus pallidus reversed haloperidol-induced parkinsonian catalepsy in rats .

Example answer:
{"entities": [{"text": "neurotensin", "type": "Chemical"}, {"text": "haloperidol-induced", "type": "Chemical"}, {"text": "parkinsonian catalepsy", "type": "Disease"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: NRA0160 and clozapine significantly induced catalepsy in rats , although their effects did not exceed 50 % induction even at the highest dose given .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}]}

Example input:
Sentence: THP exhibited an antipsychotic-like profile by potentiating haloperidol-induced catalepsy , reducing amphetamine-induced hyperactivity and reducing apomorphine-induced climbing in mice .

Example answer:
{"entities": []}

Example input:
Sentence: These results indicate that noradrenergic neurons have an important role in the manifestation of catalepsy induced by THC , whereas dopaminergic neurons are important in catalepsy induced by haloperidol .

Example answer:
{"entities": [{"text": "catalepsy", "type": "Disease"}, {"text": "THC", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: No changes in haloperidol-induced catalepsy or MK-801-induced locomotion were seen following PD .

Example answer:
{"entities": [{"text": "haloperidol-induced", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "MK-801-induced", "type": "Chemical"}]}

Example input:
Sentence: On the contrary , the cataleptogenic effect of haloperidol was significantly reduced in rats treated with desipramine and 6-OHDA but not in rats treated with 6-OHDA or in rats with lesions of the locus coeruleus .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "desipramine", "type": "Chemical"}, {"text": "6-OHDA", "type": "Chemical"}]}

Example input:
Sentence: 1 h prior to haloperidol resulted in a dose-dependent increase in the catalepsy times ( P < 0.05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: in the rat haloperidol-induced catalepsy model for Parkinson 's disease .

Example answer:
{"entities": [{"text": "haloperidol-induced", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: Catalepsy was induced by haloperidol ( 2 mg/kg p.o .

Example answer:
{"entities": [{"text": "Catalepsy", "type": "Disease"}, {"text": "haloperidol", "type": "Chemical"}]}

Input:
Sentence: Low doses of pilocarpine caused a pronounced enhancement of the catalepsy that was induced by the dopaminergic blocker , haloperidol .

## Item bc5cdr:test:1231
Example input:
Sentence: RESULT ( S ) : A 36-year-old Chinese woman developed central retinal vein occlusion after eight courses of CC .

Example answer:
{"entities": [{"text": "retinal vein occlusion", "type": "Disease"}, {"text": "CC", "type": "Chemical"}]}

Example input:
Sentence: One patient had focal seizures and transient hemiparesis but recovered completely .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "transient hemiparesis", "type": "Disease"}]}

Example input:
Sentence: Decompression and neurolysis were performed with good subsequent recovery of function .

Example answer:
{"entities": []}

Example input:
Sentence: The frequency of visual loss decreased after the concentration of the ethanol diluent was lowered .

Example answer:
{"entities": [{"text": "visual loss", "type": "Disease"}, {"text": "ethanol", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Although intravitreal aminoglycosides have substantially improved visual prognosis in endophthalmitis , macular infarction may impair full visual recovery .

Example answer:
{"entities": [{"text": "aminoglycosides", "type": "Chemical"}, {"text": "endophthalmitis", "type": "Disease"}, {"text": "infarction", "type": "Disease"}]}

Example input:
Sentence: All four recovered completely without neurological sequelae following the withdrawal of the offending agents .

Example answer:
{"entities": [{"text": "neurological sequelae", "type": "Disease"}]}

Example input:
Sentence: The patient 's ophthalmological symptoms improved rapidly 3 weeks after discontinuation of pegylated IFN alpha-2b and ribavirin .

Example answer:
{"entities": [{"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: Desferrioxamine withdrawal resulted in a complete recovery of visual function in 1 patient and partial recovery in 3 , and a complete reversal of hearing loss in 3 patients and partial recovery in 3 .

Example answer:
{"entities": [{"text": "Desferrioxamine", "type": "Chemical"}, {"text": "hearing loss", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Endophthalmitis resolved with improvement in visual acuity to 6/24 at three months .

Example answer:
{"entities": [{"text": "Endophthalmitis", "type": "Disease"}]}

Example input:
Sentence: Finally , 6 weeks later , diffuse chorioretinal atrophy with optic atrophy occurred and the vision in his left eye was lost .

Example answer:
{"entities": [{"text": "chorioretinal atrophy", "type": "Disease"}, {"text": "optic atrophy", "type": "Disease"}]}

Input:
Sentence: He later recovered normal visual acuity .

## Item bc5cdr:test:1000
Example input:
Sentence: In the five rats that developed somatic rigidity , ICP and CVP increased significantly above baseline ( delta ICP 7.5 +/- 1.0 mmHg , delta CVP 5.9 +/- 1.3 mmHg ) .

Example answer:
{"entities": [{"text": "somatic rigidity", "type": "Disease"}]}

Example input:
Sentence: They suggest that , in normal conscious rats , the central tachycardia of bromocriptine appears to predominate and to mask the bradycardia of this agonist at peripheral dopamine D2 receptors .

Example answer:
{"entities": [{"text": "tachycardia", "type": "Disease"}, {"text": "bromocriptine", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: The relationship between hippocampal acetylcholine release and cholinergic convulsant sensitivity in withdrawal seizure-prone and withdrawal seizure-resistant selected mouse lines .

Example answer:
{"entities": [{"text": "acetylcholine", "type": "Chemical"}, {"text": "seizure-prone", "type": "Disease"}, {"text": "seizure-resistant", "type": "Disease"}]}

Example input:
Sentence: Treated rats were then evaluated for incidence , latency , and seizure pattern or for locomotor activity in animals without seizures .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Abnormal movements and deafness occurred only in rats treated during the preweaning period ; within this period the greatest sensitivities for these abnormalities occurred from 2 to 11-17 and 5 to 11 days of age , respectively , indicating that the cochlea is more sensitive to streptomycin than the site ( vestibular or central ) responsible for the dyskinesias .

Example answer:
{"entities": [{"text": "Abnormal movements", "type": "Disease"}, {"text": "deafness", "type": "Disease"}, {"text": "streptomycin", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: BE-Injected rats that did not have seizures had significantly more locomotor activity than cocaine-injected animals without seizures .

Example answer:
{"entities": [{"text": "BE-Injected", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "cocaine-injected", "type": "Chemical"}]}

Example input:
Sentence: Specifically , WSP mice may have lower sensitivity to cholinergic convulsants compared with WSR because of postsynaptic receptor desensitization brought on by higher activity of cholinergic neurons .

Example answer:
{"entities": [{"text": "convulsants", "type": "Disease"}]}

Example input:
Sentence: METHODS : Cholinergic convulsant sensitivity was examined in alcohol-na ve Withdrawal Seizure-Prone ( WSP ) and-Resistant ( WSR ) mice .

Example answer:
{"entities": [{"text": "alcohol-na", "type": "Chemical"}, {"text": "Seizure-Prone", "type": "Disease"}]}

Example input:
Sentence: When hippocampal ACh was measured during testing for handling-induced convulsions , extracellular ACh was significantly elevated ( 192 % ) in WSP mice , but was nonsignificantly elevated ( 59 % ) in WSR mice .

Example answer:
{"entities": [{"text": "ACh", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Sensitivity to several convulsion endpoints induced by nicotine , carbachol , and neostigmine were significantly greater in WSR versus WSP mice .

Example answer:
{"entities": [{"text": "convulsion", "type": "Disease"}, {"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}]}

Input:
Sentence: Comparing the relative sensitivity to central depression and excitation revealed that rats were least likely to have convulsions at doses that did not first cause loss of consciousness , while cats most clearly showed marked central excitatory actions .

## Item bc5cdr:test:1126
Example input:
Sentence: Nicotine ( 1.0 mg/kg ) caused a significant increase in locomotor activity in rats that were habituated to the test environment , but had only a weak and delayed stimulant action in rats that were unfamiliar with the test environment .

Example answer:
{"entities": [{"text": "Nicotine", "type": "Chemical"}, {"text": "increase in locomotor activity", "type": "Disease"}]}

Example input:
Sentence: Here its ability to antagonize the prolonged depletion of dopamine in the striatum by amphetamine in iprindole-treated rats is reported .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "iprindole-treated", "type": "Chemical"}]}

Example input:
Sentence: Regional localization of the antagonism of amphetamine-induced hyperactivity by intracerebral calcitonin injections .

Example answer:
{"entities": [{"text": "amphetamine-induced", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "calcitonin", "type": "Chemical"}]}

Example input:
Sentence: These results indicate that noradrenergic neurons have an important role in the manifestation of catalepsy induced by THC , whereas dopaminergic neurons are important in catalepsy induced by haloperidol .

Example answer:
{"entities": [{"text": "catalepsy", "type": "Disease"}, {"text": "THC", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: NRA0160 and clozapine antagonized locomotor hyperactivity induced by methamphetamine ( MAP ) in mice .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "MAP", "type": "Chemical"}]}

Example input:
Sentence: Protection against amphetamine-induced neurotoxicity toward striatal dopamine neurons in rodents by LY274614 , an excitatory amino acid antagonist .

Example answer:
{"entities": [{"text": "amphetamine-induced", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "LY274614", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}]}

Example input:
Sentence: The present study was designed to examine the effect of 5-HT1B receptor ligands microinjected into the subregions of the nucleus accumbens ( the shell and the core ) on the locomotor hyperactivity induced by cocaine in rats .

Example answer:
{"entities": [{"text": "locomotor hyperactivity", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: TRI given repeatedly to rats increases the locomotor hyperactivity induced by d-amphetamine , quinpirole and ( + ) -7-hydroxy-dipropyloaminotetralin ( dopamine D2 and D3 effects ) .

Example answer:
{"entities": [{"text": "TRI", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "d-amphetamine", "type": "Chemical"}, {"text": "quinpirole", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: The areas where calcitonin is most effective in decreasing locomotor activity are located in the hypothalamus and nucleus accumbens , suggesting that these areas are the major sites of action of calcitonin in inhibiting amphetamine-induced locomotor activity .

Example answer:
{"entities": [{"text": "calcitonin", "type": "Chemical"}, {"text": "amphetamine-induced", "type": "Chemical"}]}

Example input:
Sentence: The data strengthen the evidence that the neurotoxic effect of amphetamine and related compounds toward nigrostriatal dopamine neurons involves NMDA receptors and that LY274614 is an NMDA receptor antagonist with long-lasting in vivo effects in rats .

Example answer:
{"entities": [{"text": "neurotoxic", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "LY274614", "type": "Chemical"}]}

Input:
Sentence: The present results suggest a selective involvement of central noradrenergic neurones in the locomotor stimulant effect of amphetamine in the rat .

## Item bc5cdr:test:934
Example input:
Sentence: In control rats , intravenous bromocriptine ( 150 microg/kg ) induced significant hypotension and tachycardia .

Example answer:
{"entities": [{"text": "bromocriptine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: The effects of varying the extracellular concentrations of Na and Ca ( [ Na ] o and [ Ca ] o ) on both , the spontaneous beating and the negative chronotropic action of verapamil , were studied in the isolated rat atria .

Example answer:
{"entities": [{"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: Bromocriptine-induced hypotension was unaffected by isoproterenol pretreatment , while tachycardia was reversed to significant bradycardia , an effect that was partly reduced by i.v .

Example answer:
{"entities": [{"text": "Bromocriptine-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Furthermore , the effects are mediated through dopamine rather than norepinephrine and do not require the carotid sinus baroreceptors .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "norepinephrine", "type": "Chemical"}]}

Example input:
Sentence: A detailed clinical history , together with skin tests , RAST ( radioallergosorbent test ) , and controlled challenge tests , was used to establish whether patients allergic to beta-lactam antibiotics had selective immediate allergic responses to amoxicillin ( AX ) or were cross-reacting with other penicillin derivatives .

Example answer:
{"entities": [{"text": "allergic", "type": "Disease"}, {"text": "beta-lactam", "type": "Chemical"}, {"text": "amoxicillin", "type": "Chemical"}, {"text": "AX", "type": "Chemical"}, {"text": "penicillin", "type": "Chemical"}]}

Example input:
Sentence: Dissociated learning of rats in the normal state and the state of amnesia produced by pentobarbital ( 15 mg/kg , ip ) was carried out .

Example answer:
{"entities": [{"text": "amnesia", "type": "Disease"}, {"text": "pentobarbital", "type": "Chemical"}]}

Example input:
Sentence: In Group 1 the rats were trained under the influence of pentobarbital to run to the same shelf as in the normal state .

Example answer:
{"entities": [{"text": "pentobarbital", "type": "Chemical"}]}

Example input:
Sentence: Learning of rats under amnesia caused by pentobarbital .

Example answer:
{"entities": [{"text": "amnesia", "type": "Disease"}, {"text": "pentobarbital", "type": "Chemical"}]}

Example input:
Sentence: These findings show that the brain-dissociated state induced by pentobarbital is formed with the participation of the mechanisms of information perception .

Example answer:
{"entities": [{"text": "pentobarbital", "type": "Chemical"}]}

Input:
Sentence: The most distinctive aspect of the barium effect was a demonstrated hypersensitivity of the cardiovascular system to sodium pentobarbital .

## Item bc5cdr:test:965
Example input:
Sentence: Native kidney specimens included a wide range of glomerulopathies as well as cases of thrombotic microangiopathy , malignant hypertension , acute interstitial nephritis , and acute tubular necrosis .

Example answer:
{"entities": [{"text": "glomerulopathies", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "malignant hypertension", "type": "Disease"}, {"text": "interstitial nephritis", "type": "Disease"}, {"text": "acute tubular necrosis", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : PAN glomeruli already showed significant pathology by day 4 , despite relatively mild proteinuria .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: HS diet for 4 wk caused a progressive increase in BP , protein and albumin excretion , and glomerular sclerosis in male DS rats , which were attenuated by castration .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: In this model of chronic renal failure the decline in GFR is not accompanied by a corresponding fall in effective renal plasma flow , which may be the functional expression of the formation of nonfiltrating atubular glomeruli .

Example answer:
{"entities": [{"text": "chronic renal failure", "type": "Disease"}]}

Example input:
Sentence: By day 45-126 , at a time when glomerular scarring was present , GLEPP1 was absent from glomerulosclerotic areas although the total glomerular content of GLEPP1 was not different from normal .

Example answer:
{"entities": []}

Example input:
Sentence: Reduction in GFR was associated with the development of glomerular sclerosis in both treated and untreated rats .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : An association has been found between transplant glomerulopathy ( TG ) and reduplication of peritubular capillary basement membranes ( PTCR ) .

Example answer:
{"entities": [{"text": "transplant glomerulopathy", "type": "Disease"}, {"text": "TG", "type": "Disease"}]}

Example input:
Sentence: The present study was performed to elucidate the role of SGK1 in the volume retention and fibrosis during nephrotic syndrome .

Example answer:
{"entities": [{"text": "volume retention", "type": "Disease"}, {"text": "fibrosis", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : This study demonstrates that chronic FK506 nephropathy consists primarily of arteriolopathy manifesting as insudative hyalinosis of the arteriolar wall , and suggests that mild-type chronic FK506 nephropathy is a condition which may lead to deterioration of renal allograft function .

Example answer:
{"entities": [{"text": "FK506", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: In conclusion , gene-targeted mice lacking SGK1 showed blunted volume retention , yet were not protected against renal fibrosis during experimental nephrotic syndrome .

Example answer:
{"entities": [{"text": "volume retention", "type": "Disease"}, {"text": "fibrosis", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}]}

Input:
Sentence: Similar to the remnant kidney model in PAN nephrosis the development of glomerular sclerosis may be related to `` mesangial overloading . ''

## Item bc5cdr:test:1140
Example input:
Sentence: When respiratory failure was produced by hypoventilation ( pH 7.05 to 7.25 ; PC02 70 to 100 mm Hg : P02 20 to 40 mm Hg ) , infusion of aminophylline resulted in an even greater decrease in ventricular fibrillation threshold to 60 percent of the control level .

Example answer:
{"entities": [{"text": "respiratory failure", "type": "Disease"}, {"text": "hypoventilation", "type": "Disease"}, {"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}]}

Example input:
Sentence: Based on the finding that VPU and VPA could protect the animals against pilocarpine-induced seizure it is suggested that the reduction of inhibitory amino acid neurotransmitters was comparatively minor and offset by a pronounced reduction of glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: Over the long-term chronic phase ( 120 days after transplantation ) , only 25 % of BMC-treated epileptic animals had seizures , but with a lower frequency and duration compared to the epileptic control group .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Oral administration of CBZ as an aqueous suspension every 8 h at a dose of 250 mg/kg was continuously protective against HFDE-induced seizures and was minimally toxic as measured by weight gain over 8 weeks of treatment .

Example answer:
{"entities": [{"text": "CBZ", "type": "Chemical"}, {"text": "HFDE-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}]}

Example input:
Sentence: In six conscious , trained dogs , maintained on a normal sodium intake of 2 to 4 mEq/kg/day , sympathetic activity was assessed as the release rate of norepinephrine and epinephrine during 15-minute i.v .

Example answer:
{"entities": [{"text": "sodium", "type": "Chemical"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "epinephrine", "type": "Chemical"}]}

Example input:
Sentence: After a 30-min baseline measure of locomotor activity ( day 0 ) , animals were maintained on a cyclic diet of 12-h deprivation followed by 12-h access to 10 % sucrose solution and chow pellets ( 12 h access starting 4 h after onset of the dark period ) for 21 days .

Example answer:
{"entities": [{"text": "sucrose", "type": "Chemical"}]}

Example input:
Sentence: All of the rats in the saline-treated epileptic control group developed SRS , whereas none of the BMC-treated epileptic animals had seizures in the short term ( 15 days after transplantation ) , regardless of the BMC source .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}, {"text": "SRS", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: The animals were mechanically ventilated to achieve normocarbia ( PCO2 = 42 +/- 1 mmHg , mean +/- SE ) .

Example answer:
{"entities": []}

Example input:
Sentence: 2 and 10 mg/kg/i.p. , or an equal volume of saline for the control group ( n = 20 ) ; 15 minutes later , all the animals were injected with a single 50 mg/kg/i.p .

Example answer:
{"entities": []}

Example input:
Sentence: In this study , the severity of response to other seizure-inducing agents was tested in mice 1 and 24 h after intraperitoneal administration of 80 mg/kg gamma-HCH .

Example answer:
{"entities": [{"text": "seizure-inducing", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}]}

Input:
Sentence: Animals surviving for 20 min were immediately stressed by a swim test in 25 degrees C water , and death-producing tonic seizures were scored for 2 min .

## Item bc5cdr:test:1017
Example input:
Sentence: We investigated this association , according to the type of progestagen included in third-generation ( i.e. , desogestrel or gestodene ) and second-generation ( i.e. , levonorgestrel ) oral contraceptives , the dose of estrogen , and the presence or absence of prothrombotic mutations METHODS : In a nationwide , population-based , case-control study , we identified and enrolled 248 women 18 through 49 years of age who had had a first myocardial infarction between 1990 and 1995 and 925 control women who had not had a myocardial infarction and who were matched for age , calendar year of the index event , and area of residence .

Example answer:
{"entities": [{"text": "progestagen", "type": "Chemical"}, {"text": "desogestrel", "type": "Chemical"}, {"text": "gestodene", "type": "Chemical"}, {"text": "levonorgestrel", "type": "Chemical"}, {"text": "oral contraceptives", "type": "Chemical"}, {"text": "estrogen", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: METHODS : In a population-based study in 513 naturally postmenopausal women aged 54-67 years , we studied the association between self-reported intramuscularly administered high-dose estrogen-testosterone therapy ( estradiol- and testosterone esters ) and aortic atherosclerosis .

Example answer:
{"entities": [{"text": "estrogen-testosterone", "type": "Chemical"}, {"text": "estradiol- and testosterone esters", "type": "Chemical"}, {"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: Estrogens protect ovariectomized rats from hippocampal injury induced by kainic acid-induced status epilepticus ( SE ) .

Example answer:
{"entities": [{"text": "hippocampal injury", "type": "Disease"}, {"text": "kainic", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Pituitary tumors were induced in F344 female rats by chronic treatment with diethylstilbestrol ( DES , 8-10 mg ) implanted subcutaneously in silastic capsules .

Example answer:
{"entities": [{"text": "Pituitary tumors", "type": "Disease"}, {"text": "diethylstilbestrol", "type": "Chemical"}, {"text": "DES", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : An association between the use of oral contraceptives and the risk of myocardial infarction has been found in some , but not all , studies .

Example answer:
{"entities": [{"text": "oral contraceptives", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: No association was found for hormone use less than 1 year .

Example answer:
{"entities": []}

Example input:
Sentence: The risk of myocardial infarction was similar among women who used oral contraceptives whether or not they had a prothrombotic mutation .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptives", "type": "Chemical"}]}

Example input:
Sentence: Tamoxifen ( TAM ) , the antiestrogenic drug most widely prescribed in the chemotherapy of breast cancer , induces changes in normal discoid shape of erythrocytes and hemolytic anemia .

Example answer:
{"entities": [{"text": "Tamoxifen", "type": "Chemical"}, {"text": "TAM", "type": "Chemical"}, {"text": "breast cancer", "type": "Disease"}, {"text": "hemolytic anemia", "type": "Disease"}]}

Example input:
Sentence: Characterization of estrogen-induced adenohypophyseal tumors in the Fischer 344 rat .

Example answer:
{"entities": [{"text": "estrogen-induced", "type": "Chemical"}, {"text": "adenohypophyseal tumors", "type": "Disease"}]}

Example input:
Sentence: Oral contraceptives and the risk of myocardial infarction .

Example answer:
{"entities": [{"text": "Oral contraceptives", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Input:
Sentence: Hormones and risk of breast cancer .

## Item bc5cdr:test:771
Example input:
Sentence: Early trials of cisplatin and amifostine also suggested that the incidence and severity of cisplatin-induced nephrotoxicity , ototoxicity , and neuropathy were reduced .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "amifostine", "type": "Chemical"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "ototoxicity", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}]}

Example input:
Sentence: One of the twins developed complete heart block and dilated cardiomyopathy related to lopinavir/ritonavir therapy , a boosted protease-inhibitor agent , while the other twin developed mild bradycardia .

Example answer:
{"entities": [{"text": "heart block", "type": "Disease"}, {"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "lopinavir/ritonavir", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: A 61-year-old man was treated with combination chemotherapy incorporating cisplatinum , etoposide , high-dose 5-fluorouracil ( 2,250 mg/m2/24 hours ) and folinic acid for an inoperable gastric adenocarcinoma .

Example answer:
{"entities": [{"text": "cisplatinum", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}, {"text": "gastric adenocarcinoma", "type": "Disease"}]}

Example input:
Sentence: Cardiac toxicity observed in association with high-dose cyclophosphamide-based chemotherapy for metastatic breast cancer .

Example answer:
{"entities": [{"text": "Cardiac toxicity", "type": "Disease"}, {"text": "cyclophosphamide-based", "type": "Chemical"}, {"text": "breast cancer", "type": "Disease"}]}

Example input:
Sentence: Three patients developed congestive heart failure after the completion of chemotherapy .

Example answer:
{"entities": [{"text": "congestive heart failure", "type": "Disease"}]}

Example input:
Sentence: Five patients with carcinoma developed thrombotic microangiopathy ( characterized by renal insufficiency , microangiopathic hemolytic anemia , and usually thrombocytopenia ) after treatment with cisplatin , bleomycin , and a vinca alkaloid .

Example answer:
{"entities": [{"text": "carcinoma", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "microangiopathic hemolytic anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "bleomycin", "type": "Chemical"}, {"text": "vinca alkaloid", "type": "Chemical"}]}

Example input:
Sentence: Since the introduction of angiotensin converting enzyme ( ACE ) inhibitors into the adjunctive treatment of patients with congestive heart failure , cases of severe hypotension , especially on the first day of treatment , have occasionally been reported .

Example answer:
{"entities": [{"text": "angiotensin converting enzyme ( ACE ) inhibitors", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: An allergic reaction consisting of angioneurotic edema secondary to continuous infusion 5-fluorouracil occurred in a patient with recurrent carcinoma of the oral cavity , cirrhosis , and cisplatin-induced impaired renal function .

Example answer:
{"entities": [{"text": "allergic reaction", "type": "Disease"}, {"text": "angioneurotic edema", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "carcinoma of the oral cavity", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "impaired renal function", "type": "Disease"}]}

Example input:
Sentence: Analysis was performed on 61 women with chemotherapy-responsive metastatic breast cancer receiving 96-h infusional cyclophosphamide as part of a triple sequential high-dose regimen to assess association between presence of peritransplant congestive heart failure ( CHF ) and the following pretreatment characteristics : presence of electrocardiogram ( EKG ) abnormalities , age , hypertension , prior cardiac history , smoking , diabetes mellitus , prior use of anthracyclines , and left-sided chest irradiation .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "CHF", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "diabetes mellitus", "type": "Disease"}, {"text": "anthracyclines", "type": "Chemical"}]}

Example input:
Sentence: Adverse cardiac effects during induction chemotherapy treatment with cis-platin and 5-fluorouracil .

Example answer:
{"entities": [{"text": "cis-platin", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}]}

Input:
Sentence: Cardiac symptoms , including hypotension , developed in three patients with advanced colorectal carcinoma while being treated with cisplatin ( CDDP ) and 5-fluorouracil ( 5-FU ) .

## Item bc5cdr:test:827
Example input:
Sentence: Thus , FS containing 47.5 mg/ml tAMCA evoked generalized seizures in all tested rats ( n=6 ) while the lowest concentration of tAMCA ( 0.5 mg/ml ) only evoked brief episodes of jerk-correlated convulsive potentials in 1 of 6 rats .

Example answer:
{"entities": [{"text": "tAMCA", "type": "Chemical"}, {"text": "generalized seizures", "type": "Disease"}, {"text": "convulsive", "type": "Disease"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: In behavioral studies , pre-treatment of mice with BD1018 , BD1063 , or LR132 significantly attenuated cocaine-induced convulsions and lethality .

Example answer:
{"entities": [{"text": "BD1018", "type": "Chemical"}, {"text": "BD1063", "type": "Chemical"}, {"text": "LR132", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}]}

Example input:
Sentence: The biochemical results of brain biogenic amines of BALB/C mouse strain suggest a probable decrease of catecholamine turnover rate and/or metabolism by monoamine oxidase and a resulting increase in O-methylation of norepinephrine which may account for a behavioral depression caused by amantadine in the BALB/C mice .

Example answer:
{"entities": [{"text": "amines", "type": "Chemical"}, {"text": "catecholamine", "type": "Chemical"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "behavioral depression", "type": "Disease"}, {"text": "amantadine", "type": "Chemical"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Mature male and female mice from six inbred stains were tested for susceptibility to behavioral seizures induced by a single injection of cocaine .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Clomipramine exposure in immature rats produced significant behavioral and biochemical changes that include enhanced anxiety ( elevated plus maze and marble burying ) , behavioral inflexibility ( perseveration in the spontaneous alternation task and impaired reversal learning ) , working memory impairment ( e.g. , win-shift paradigm ) , hoarding , and corticostriatal dysfunction .

Example answer:
{"entities": [{"text": "Clomipramine", "type": "Chemical"}, {"text": "anxiety", "type": "Disease"}, {"text": "behavioral inflexibility", "type": "Disease"}, {"text": "memory impairment", "type": "Disease"}, {"text": "hoarding", "type": "Disease"}, {"text": "corticostriatal dysfunction", "type": "Disease"}]}

Example input:
Sentence: Neuroinflammation and behavioral abnormalities after neonatal terbutaline treatment in rats : implications for autism .

Example answer:
{"entities": [{"text": "Neuroinflammation", "type": "Disease"}, {"text": "behavioral abnormalities", "type": "Disease"}, {"text": "terbutaline", "type": "Chemical"}, {"text": "autism", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Sensitivity to several convulsion endpoints induced by nicotine , carbachol , and neostigmine were significantly greater in WSR versus WSP mice .

Example answer:
{"entities": [{"text": "convulsion", "type": "Disease"}, {"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}]}

Input:
Sentence: Monosodium glutamate ( MSG ) administration to neonatal rodents produces convulsions and results in numerous biochemical and behavioral deficits .

## Item bc5cdr:test:1014
Example input:
Sentence: It is suggested that the effects of Captopril on the lungs may be attributable to a vasodilatory effect due to a reduction in the circulating level of Angiotension II and an increase in prostacyclin ( secondary to an increase in bradykinin ) .

Example answer:
{"entities": [{"text": "Captopril", "type": "Chemical"}, {"text": "Angiotension II", "type": "Chemical"}, {"text": "prostacyclin", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}, {"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: However , there was no significant difference in the lidocaine concentrations measured when the systolic blood pressure became 70 mmHg .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: The effectiveness of administration of glycopyrrolate 5 and 10 micrograms kg-1 and atropine 10 and 20 micrograms kg-1 i.v .

Example answer:
{"entities": [{"text": "glycopyrrolate", "type": "Chemical"}, {"text": "atropine", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : The sensitivity improved dramatically from 16 % to 79 % , positive predictive value increased from 60 % to 68 % and negative predictive value from 54 % to 78 % , and specificity decreased from 90 % to 67 % .

Example answer:
{"entities": []}

Example input:
Sentence: After administration of phenylephrine , MAP increased ( 51 +/- 12 to 81 +/- 13 mmHg ; P < 0.001 ; mean +/- SD ) .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}]}

Example input:
Sentence: While contractions to carbachol and ATP were the same in inflamed and in control strips when related to a reference potassium response , isoprenaline-induced relaxations were smaller in inflamed strips .

Example answer:
{"entities": [{"text": "carbachol", "type": "Chemical"}, {"text": "ATP", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}, {"text": "isoprenaline-induced", "type": "Chemical"}]}

Example input:
Sentence: It is recommended that either glycopyrrolate 10 micrograms kg-1 or atropine 20 micrograms kg-1 i.v .

Example answer:
{"entities": [{"text": "glycopyrrolate", "type": "Chemical"}, {"text": "atropine", "type": "Chemical"}]}

Example input:
Sentence: Generally , atropine reduced contractions , but in contrast to controls , it also reduced responses to low electrical field stimulation intensity ( 1-5 Hz ) in inflamed preparations .

Example answer:
{"entities": [{"text": "atropine", "type": "Chemical"}]}

Input:
Sentence: This change with propranolol sensitivity was calculated as the apparent Ka , this was unchanged by atropine ( 11.7 +/- 2.1 and 10.1 +/- 2.5 ml/ng ) .

## Item bc5cdr:test:1165
Example input:
Sentence: At the end of the procedure , Group A ( n = 20 ) had 20 mg/0.5 mL of methylprednisolone and 10 mg/0.5 mL of gentamicin injected into the posterior sub-Tenon 's space and Group B ( n = 20 ) had the same combination injected into the anterior sub-Tenon 's space .

Example answer:
{"entities": [{"text": "methylprednisolone", "type": "Chemical"}, {"text": "gentamicin", "type": "Chemical"}]}

Example input:
Sentence: Injection of Captopril ( 1 mg/kg ) , an inhibitor of angiotensin converting enzyme ( ACE ) , reduced both pulmonary and renal insufficiency in this rat model .

Example answer:
{"entities": [{"text": "Captopril", "type": "Chemical"}, {"text": "angiotensin", "type": "Chemical"}]}

Example input:
Sentence: For each of the three tested calcium channel blockers ( diltiazem , verapamil and bepridil ) 6 groups of mice were treated by two different doses , i.e .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "bepridil", "type": "Chemical"}]}

Example input:
Sentence: METHODS : In this study , WR242511 was administered intravenously ( IV ) in 2 female and 4 male rhesus monkeys in doses of 3.5 and/or 7.0 mg/kg ; a single male also received WR242511 orally ( PO ) at 7.0 mg/kg .

Example answer:
{"entities": [{"text": "WR242511", "type": "Chemical"}]}

Example input:
Sentence: Streptomycin sulfate ( 300 mg/kg s.c. ) was injected for various periods into preweanling rats and for 3 weeks into weanling rats .

Example answer:
{"entities": [{"text": "Streptomycin", "type": "Chemical"}]}

Example input:
Sentence: The 65 dogs in the study received injections in the subarachnoid space as follows : 6 to 8 ml of bupivacaine ( N = 15 ) , 2-chloroprocaine-CE ( N = 20 ) , low pH normal saline ( pH 3.0 ) ( N = 20 ) , or normal saline ( N = 10 ) .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}, {"text": "2-chloroprocaine-CE", "type": "Chemical"}]}

Example input:
Sentence: In the in vivo study , the administration ( 50 mg/kg , i.p . )

Example answer:
{"entities": []}

Example input:
Sentence: injections of organ specific three drugs ( AAP : 500 mg/Kg for 24 h ; AMI : 50 mg/Kg/day for four days ; DOX : 20 mg/Kg for 48 h ) .

Example answer:
{"entities": [{"text": "AAP", "type": "Chemical"}, {"text": "AMI", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: 2 and 10 mg/kg/i.p. , or an equal volume of saline for the control group ( n = 20 ) ; 15 minutes later , all the animals were injected with a single 50 mg/kg/i.p .

Example answer:
{"entities": []}

Example input:
Sentence: Two separate equimolar doses ( 0.2 and 0.4 mumol ) of either cocaine or BE were injected ventricularly in unanesthetized juvenile rats .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "BE", "type": "Chemical"}]}

Input:
Sentence: In vivo injection of bepridil at a dose of 5 mg/kg ( i.v . )

## Item bc5cdr:test:1171
Example input:
Sentence: Blood was collected from the antecubital vein four times : 60 min before and after the nitroglycerin application , and 60 and 120 min after the beginning of the migraine attack ( mean 344 and 404 min ; 12 subjects ) .

Example answer:
{"entities": [{"text": "nitroglycerin", "type": "Chemical"}, {"text": "migraine", "type": "Disease"}]}

Example input:
Sentence: Five hours after exposure , he developed disulfiram-like syndrome with flushing , tachycardia , and arterial hypotension after consuming three glasses of wine .

Example answer:
{"entities": [{"text": "disulfiram-like", "type": "Chemical"}, {"text": "flushing", "type": "Disease"}, {"text": "tachycardia", "type": "Disease"}, {"text": "arterial hypotension", "type": "Disease"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: Twenty-three hours after heart transplantation , life-threatening acute right heart failure was diagnosed in a patient requiring continuous venovenous hemodiafiltration ( CVVHDF ) .

Example answer:
{"entities": [{"text": "right heart failure", "type": "Disease"}]}

Example input:
Sentence: Gastrointestinal bleed , seizures , infection , and acute renal failure were documented in seven ( 10 % ) , five ( 7.1 % ) , 26 ( 37.1 % ) , and seven ( 10 % ) patients , respectively .

Example answer:
{"entities": [{"text": "Gastrointestinal bleed", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "infection", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: She subsequently died some 5 weeks after the commencement of her drug therapy.Post-mortem examination showed evidence of massive hepatocellular necrosis , acute hypersensitivity myocarditis , focal acute tubulo-interstitial nephritis and extensive bone marrow necrosis , with no evidence of malignancy .

Example answer:
{"entities": [{"text": "massive hepatocellular necrosis", "type": "Disease"}, {"text": "myocarditis", "type": "Disease"}, {"text": "nephritis", "type": "Disease"}, {"text": "bone marrow necrosis", "type": "Disease"}, {"text": "malignancy", "type": "Disease"}]}

Example input:
Sentence: Flow and metabolism were measured 5-13 days after the subarachnoid haemorrhage by a modification of the classical Kety-Schmidt technique using xenon-133 i.v .

Example answer:
{"entities": [{"text": "subarachnoid haemorrhage", "type": "Disease"}, {"text": "xenon-133", "type": "Chemical"}]}

Example input:
Sentence: Despite pharmacological and supportive interventions , laboratory parameters worsened and the patient died 17 hours after admission .

Example answer:
{"entities": []}

Example input:
Sentence: Within 8 hours after initiation of therapy the patient died with a clinical picture resembling massive pulmonary obstruction due to choriocarcinomic tissue plugs , probably originating from the uterus .

Example answer:
{"entities": [{"text": "pulmonary obstruction", "type": "Disease"}]}

Example input:
Sentence: The patient required massive transfusion support ( 55 units of red blood cells , 42 units of fresh-frozen plasma , 40 units of cryoprecipitate , 40 units of platelets , and three doses of recombinant Factor VIIa ) for severe intraoperative and postoperative bleeding .

Example answer:
{"entities": []}

Input:
Sentence: Massive bleeding appeared during surgery which lasted for six hours .

## Item bc5cdr:test:804
Example input:
Sentence: Dexamethasone ( Dex ) -induced hypertension is characterized by endothelial dysfunction associated with nitric oxide ( NO ) deficiency and increased superoxide ( O2- ) production .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "Chemical"}, {"text": "Dex", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "nitric oxide", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}, {"text": "superoxide", "type": "Chemical"}, {"text": "O2-", "type": "Chemical"}]}

Example input:
Sentence: 17beta-Estradiol did not alter the onset of first clonus in ovariectomized rats but accelerated it in males .

Example answer:
{"entities": [{"text": "17beta-Estradiol", "type": "Chemical"}]}

Example input:
Sentence: Adult rats given dexamethasone on days 15 and 16 of gestation had more glomeruli with glomerulosclerosis than control rats .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "Chemical"}, {"text": "Ato-treated", "type": "Chemical"}]}

Example input:
Sentence: This study shows that prenatal dexamethasone in rats results in a reduction in glomerular number , glomerulosclerosis , and hypertension when administered at specific points during gestation .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "reduction in glomerular number", "type": "Disease"}, {"text": "glomerulosclerosis", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Topical papaverine for the treatment of vasospasm was associated with the onset of a transient disturbance in neurophysiological function of the ascending auditory brainstem pathway .

Example answer:
{"entities": [{"text": "papaverine", "type": "Chemical"}, {"text": "vasospasm", "type": "Disease"}]}

Example input:
Sentence: Dexamethasone is frequently administered to the developing fetus to accelerate pulmonary development .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSIONS : The administration of methylprednisolone and gentamicin in the posterior sub-Tenon 's space was related to a high incidence of side effects including nausea , vomiting , and headache .

Example answer:
{"entities": [{"text": "methylprednisolone", "type": "Chemical"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "nausea , vomiting", "type": "Disease"}, {"text": "headache", "type": "Disease"}]}

Example input:
Sentence: Two patients treated with parenteral paramethasone ( Triniol ) and dexamethasone ( Sedionbel ) are described .

Example answer:
{"entities": [{"text": "paramethasone", "type": "Chemical"}, {"text": "dexamethasone", "type": "Chemical"}]}

Example input:
Sentence: Corticosteroids different from paramethasone also produced hypersensitivity reactions in these patients ; however , a few of them were tolerated .

Example answer:
{"entities": [{"text": "paramethasone", "type": "Chemical"}, {"text": "hypersensitivity", "type": "Disease"}]}

Input:
Sentence: Concomitant use of oral prednisone and topical beclomethasone may increase the risk of developing hoarseness or candidiasis .

## Item bc5cdr:test:1286
Example input:
Sentence: After intravenous administration of labetalol , metoprolol and midazolam the patient 's condition improved , and 15 min later he woke up .

Example answer:
{"entities": [{"text": "labetalol", "type": "Chemical"}, {"text": "metoprolol", "type": "Chemical"}, {"text": "midazolam", "type": "Chemical"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: Similarly , in patient diaries , although both treatments caused reduction in subjective dyskinesia scores during the days of intervention , the effect was sustained for 3 days after the intervention for the real rTMS only .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: In contrast with other beta blockers , flestolol-induced effects reverse rapidly ( within 30 minutes ) following discontinuation because of its short half-life .

Example answer:
{"entities": [{"text": "flestolol-induced", "type": "Chemical"}]}

Example input:
Sentence: During the early stages of analgesic treatment , the changes in urinary concentrating ability were reversible , but after prolonged analgesic treatment , maximum urinary concentrating ability failed to recover .

Example answer:
{"entities": []}

Example input:
Sentence: Renal structure and concentrating ability were examined after a recovery period of up to 18 weeks , when no analgesics were given , to investigate whether the analgesic-induced changes were reversible .

Example answer:
{"entities": []}

Example input:
Sentence: Since it takes three to 12 months to achieve maximal effects , those patients who are unable to continue the drug receive little benefit from it .

Example answer:
{"entities": []}

Example input:
Sentence: This change resulted within 2-4 weeks in the 50-200 % increase in the plasma levels of these neuroleptics and the appearance of extrapyramidal symptoms .

Example answer:
{"entities": [{"text": "extrapyramidal symptoms", "type": "Disease"}]}

Example input:
Sentence: After 2 weeks of treatment , patients tested 5-8 h after the last dose of medication did not show any decrement of performance .

Example answer:
{"entities": []}

Example input:
Sentence: Significant declines in simple and sustained attention , working memory , and verbal memory were observed at 1 hour postdose compared to baseline for both age groups with a trend toward return to baseline by 5 hours postdose .

Example answer:
{"entities": []}

Input:
Sentence: These changes were maximal in the hour immediately after medications and slowly returned toward base-line levels thereafter .

## Item bc5cdr:test:943
Example input:
Sentence: Here its ability to antagonize the prolonged depletion of dopamine in the striatum by amphetamine in iprindole-treated rats is reported .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "iprindole-treated", "type": "Chemical"}]}

Example input:
Sentence: On the other hand , pretreatment with p-chlorophenylalamine ( 3 X 320 mg/kg i.p. , 24 hr ) , a serotonin depletor , caused no significant change in the hyperactivity .

Example answer:
{"entities": [{"text": "p-chlorophenylalamine", "type": "Chemical"}, {"text": "serotonin", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}]}

Example input:
Sentence: We describe the effect of phenylephrine and ephedrine on frontal lobe oxygenation ( S ( c ) O ( 2 ) ) following anesthesia-induced hypotension .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "ephedrine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Phenylephrine but not ephedrine reduces frontal lobe oxygenation following anesthesia-induced hypotension .

Example answer:
{"entities": [{"text": "Phenylephrine", "type": "Chemical"}, {"text": "ephedrine", "type": "Chemical"}, {"text": "reduces frontal lobe oxygenation", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : The utilization of phenylephrine to correct hypotension induced by anesthesia has a negative impact on S ( c ) O ( 2 ) while ephedrine maintains frontal lobe oxygenation potentially related to an increase in CO .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: Seven patients suffering from Parkinson 's disease ( PD ) with severely disabling dyskinesia received low-dose propranolol as an adjunct to the currently used medical treatment .

Example answer:
{"entities": [{"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "propranolol", "type": "Chemical"}]}

Example input:
Sentence: Improvement of levodopa-induced dyskinesia by propranolol in Parkinson 's disease .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "propranolol", "type": "Chemical"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: Cerebral infarction with a single oral dose of phenylpropanolamine .

Example answer:
{"entities": [{"text": "Cerebral infarction", "type": "Disease"}, {"text": "phenylpropanolamine", "type": "Chemical"}]}

Example input:
Sentence: Phenylpropanolamine ( PPA ) , a synthetic sympathomimetic that is structurally similar to amphetamine , is available over the counter in anorectics , nasal congestants , and cold preparations .

Example answer:
{"entities": [{"text": "Phenylpropanolamine", "type": "Chemical"}, {"text": "PPA", "type": "Chemical"}, {"text": "amphetamine", "type": "Chemical"}]}

Example input:
Sentence: In experiments using specific adrenergic antagonists , we found that pretreatment with the beta-adrenergic receptor antagonist propranolol blocked cocaine-induced anxiety-like behavior in Dbh +/- and wild-type C57BL6/J mice , while the alpha ( 1 ) antagonist prazosin and the alpha ( 2 ) antagonist yohimbine had no effect .

Example answer:
{"entities": [{"text": "propranolol", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "anxiety-like", "type": "Disease"}, {"text": "prazosin", "type": "Chemical"}, {"text": "yohimbine", "type": "Chemical"}]}

Input:
Sentence: Propranolol antagonism of phenylpropanolamine-induced hypertension .

## Item bc5cdr:test:1333
Example input:
Sentence: Apamin , a selective blocker of calcium-dependent potassium channels , was administered intracerebroventricularly in rats anesthetized with 0.8 % sevoflurane to investigate the mechanism of the anticonvulsive effects .

Example answer:
{"entities": [{"text": "Apamin", "type": "Chemical"}, {"text": "calcium-dependent", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}, {"text": "sevoflurane", "type": "Chemical"}]}

Example input:
Sentence: In streptozotocin-induced hyperalgesia , inducible NO synthase participates in pronociceptive activity of bradykinin , whereas in vincristine-induced hyperalgesia bradykinin seemed to activate neuronal NO synthase pathway .

Example answer:
{"entities": [{"text": "streptozotocin-induced", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "NO", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}, {"text": "vincristine-induced", "type": "Chemical"}]}

Example input:
Sentence: Ten rats had arterial , central venous ( CVP ) , and subdural cannulae inserted under halothane anesthesia .

Example answer:
{"entities": [{"text": "halothane", "type": "Chemical"}]}

Example input:
Sentence: The blood flow responses seem to be mediated by the release of acetylcholine and VIP within the meninges .

Example answer:
{"entities": [{"text": "acetylcholine", "type": "Chemical"}]}

Example input:
Sentence: In this patient , renal artery stenosis combined with heart failure and diuretic therapy certainly resulted in a strong activation of the renin-angiotensin system ( RAS ) .

Example answer:
{"entities": [{"text": "renal artery stenosis", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}]}

Example input:
Sentence: They suggest that , in normal conscious rats , the central tachycardia of bromocriptine appears to predominate and to mask the bradycardia of this agonist at peripheral dopamine D2 receptors .

Example answer:
{"entities": [{"text": "tachycardia", "type": "Disease"}, {"text": "bromocriptine", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: The evoked increases in dural blood flow were also abolished by topical pre-administration of atropine ( 1 mm ) and [ Lys1 , Pro2,5 , Arg3,4 , Tyr6 ] -VIP ( 0.1 mm ) , a vasoactive intestinal polypeptide ( VIP ) antagonist , onto the exposed dura mater .

Example answer:
{"entities": [{"text": "increases in dural blood flow", "type": "Disease"}, {"text": "atropine", "type": "Chemical"}]}

Example input:
Sentence: The [ verapamil ] o that arrested atrial beating ( AC ) was also potentiated with the order LNa = LNa+LCa = LNa+HCa = LCa > HCa = N. The results indicate that rat atrial spontaneous beating is more dependent on [ Na ] o than on [ Ca ] o in a range of +/- 50 % of their normal concentration .

Example answer:
{"entities": [{"text": "verapamil", "type": "Chemical"}, {"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}]}

Example input:
Sentence: This drug caused biventricular dysfunction , due to its negative inotropic effect , and hypotension , due to its peripheral vasodilatory effect .

Example answer:
{"entities": [{"text": "biventricular dysfunction", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Phenylephrine infusion increased arterial pressure , arteriolar diameter and clearance of fluorescent dextran by a similar magnitude in both groups .

Example answer:
{"entities": [{"text": "Phenylephrine", "type": "Chemical"}, {"text": "dextran", "type": "Chemical"}]}

Input:
Sentence: The two drugs may act synergistically on both the AV node and the peripheral circulation .

## Item bc5cdr:test:1343
Example input:
Sentence: Her incontinence resolved with the change of medication .

Example answer:
{"entities": [{"text": "incontinence", "type": "Disease"}]}

Example input:
Sentence: Urgent fasciotomies were performed and the patient made an uneventful recovery with the withdrawal of simvastatin .

Example answer:
{"entities": [{"text": "simvastatin", "type": "Chemical"}]}

Example input:
Sentence: She had a gradual return of motor function and ability of feeling Foley catheter .

Example answer:
{"entities": []}

Example input:
Sentence: Her aminotransferase levels returned to normal by postoperative day 23 , and her 2-year follow-up showed no adverse events .

Example answer:
{"entities": []}

Example input:
Sentence: Decompression and neurolysis were performed with good subsequent recovery of function .

Example answer:
{"entities": []}

Example input:
Sentence: Propylthiouracil therapy was withdrawn , and she was treated with a 1-month course of prednisone , which alleviated her symptoms .

Example answer:
{"entities": [{"text": "Propylthiouracil", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}]}

Example input:
Sentence: Her symptoms totally regressed after drug withdrawal and reappeared when acitretin was reintroduced .

Example answer:
{"entities": [{"text": "acitretin", "type": "Chemical"}]}

Example input:
Sentence: The magnesium was stopped and she recovered over a few days .

Example answer:
{"entities": [{"text": "magnesium", "type": "Chemical"}]}

Example input:
Sentence: All four recovered completely without neurological sequelae following the withdrawal of the offending agents .

Example answer:
{"entities": [{"text": "neurological sequelae", "type": "Disease"}]}

Example input:
Sentence: All patients recovered without sequelae .

Example answer:
{"entities": []}

Input:
Sentence: She recovered without complications .

## Item bc5cdr:test:969
Example input:
Sentence: The relationship between hippocampal acetylcholine release and cholinergic convulsant sensitivity in withdrawal seizure-prone and withdrawal seizure-resistant selected mouse lines .

Example answer:
{"entities": [{"text": "acetylcholine", "type": "Chemical"}, {"text": "seizure-prone", "type": "Disease"}, {"text": "seizure-resistant", "type": "Disease"}]}

Example input:
Sentence: Binding of nicotine to nicotinic acetylcholine receptors ( nAChRs ) elicits a series of dose-dependent behaviors that go from altered exploration , sedation , and tremors , to seizures and death .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "acetylcholine", "type": "Chemical"}, {"text": "tremors", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "death", "type": "Disease"}]}

Example input:
Sentence: Specifically , WSP mice may have lower sensitivity to cholinergic convulsants compared with WSR because of postsynaptic receptor desensitization brought on by higher activity of cholinergic neurons .

Example answer:
{"entities": [{"text": "convulsants", "type": "Disease"}]}

Example input:
Sentence: METHODS : Cholinergic convulsant sensitivity was examined in alcohol-na ve Withdrawal Seizure-Prone ( WSP ) and-Resistant ( WSR ) mice .

Example answer:
{"entities": [{"text": "alcohol-na", "type": "Chemical"}, {"text": "Seizure-Prone", "type": "Disease"}]}

Example input:
Sentence: Together , these results suggest that the beta4 and the alpha3 subunits are mediators of nicotine-induced seizures and hypolocomotion .

Example answer:
{"entities": [{"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "hypolocomotion", "type": "Disease"}]}

Example input:
Sentence: We examined the role of the beta4 subunits in nicotine-induced seizures and hypolocomotion in beta4 homozygous null ( beta4 -/- ) and alpha3 heterozygous ( +/- ) mice .

Example answer:
{"entities": [{"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "hypolocomotion", "type": "Disease"}]}

Example input:
Sentence: The alpha3 and beta4 nicotinic acetylcholine receptor subunits are necessary for nicotine-induced seizures and hypolocomotion in mice .

Example answer:
{"entities": [{"text": "acetylcholine", "type": "Chemical"}, {"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "hypolocomotion", "type": "Disease"}]}

Example input:
Sentence: beta4 -/- mice were less sensitive to the effects of nicotine both at low doses , measured as decreased exploration in an open field , and at high doses , measured as sensitivity to nicotine-induced seizures .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Sensitivity to several convulsion endpoints induced by nicotine , carbachol , and neostigmine were significantly greater in WSR versus WSP mice .

Example answer:
{"entities": [{"text": "convulsion", "type": "Disease"}, {"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}]}

Example input:
Sentence: alpha3 +/- mice were partially resistant to nicotine-induced seizures when compared to wild-type littermates .

Example answer:
{"entities": [{"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Input:
Sentence: Mice sensitive to the convulsant effects of nicotine had greater alpha-bungarotoxin binding in the hippocampus than seizure insensitive mice .

## Item bc5cdr:test:968
Example input:
Sentence: Specifically , WSP mice may have lower sensitivity to cholinergic convulsants compared with WSR because of postsynaptic receptor desensitization brought on by higher activity of cholinergic neurons .

Example answer:
{"entities": [{"text": "convulsants", "type": "Disease"}]}

Example input:
Sentence: In behavioral studies , pre-treatment of mice with BD1018 , BD1063 , or LR132 significantly attenuated cocaine-induced convulsions and lethality .

Example answer:
{"entities": [{"text": "BD1018", "type": "Chemical"}, {"text": "BD1063", "type": "Chemical"}, {"text": "LR132", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}]}

Example input:
Sentence: METHODS : Cholinergic convulsant sensitivity was examined in alcohol-na ve Withdrawal Seizure-Prone ( WSP ) and-Resistant ( WSR ) mice .

Example answer:
{"entities": [{"text": "alcohol-na", "type": "Chemical"}, {"text": "Seizure-Prone", "type": "Disease"}]}

Example input:
Sentence: Mature male and female mice from six inbred stains were tested for susceptibility to behavioral seizures induced by a single injection of cocaine .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Sensitivity to several convulsion endpoints induced by nicotine , carbachol , and neostigmine were significantly greater in WSR versus WSP mice .

Example answer:
{"entities": [{"text": "convulsion", "type": "Disease"}, {"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}]}

Example input:
Sentence: Together , these results suggest that the beta4 and the alpha3 subunits are mediators of nicotine-induced seizures and hypolocomotion .

Example answer:
{"entities": [{"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "hypolocomotion", "type": "Disease"}]}

Example input:
Sentence: beta4 -/- mice were less sensitive to the effects of nicotine both at low doses , measured as decreased exploration in an open field , and at high doses , measured as sensitivity to nicotine-induced seizures .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: alpha3 +/- mice were partially resistant to nicotine-induced seizures when compared to wild-type littermates .

Example answer:
{"entities": [{"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: We examined the role of the beta4 subunits in nicotine-induced seizures and hypolocomotion in beta4 homozygous null ( beta4 -/- ) and alpha3 heterozygous ( +/- ) mice .

Example answer:
{"entities": [{"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "hypolocomotion", "type": "Disease"}]}

Example input:
Sentence: The alpha3 and beta4 nicotinic acetylcholine receptor subunits are necessary for nicotine-induced seizures and hypolocomotion in mice .

Example answer:
{"entities": [{"text": "acetylcholine", "type": "Chemical"}, {"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "hypolocomotion", "type": "Disease"}]}

Input:
Sentence: Using mice derived from a classical F2 and backcross genetic design , a relationship between nicotine-induced seizures and alpha-bungarotoxin nicotinic receptor concentration was found .

## Item bc5cdr:test:1111
Example input:
Sentence: SCr increases > or = 0.5 mg/dL occurred in 4.4 % ( 9 of 204 patients ) after iopamidol and 6.7 % ( 14 of 210 patients ) after iodixanol ( P=0.39 ) , whereas rates of SCr increases > or = 25 % were 9.8 % and 12.4 % , respectively ( P=0.44 ) .

Example answer:
{"entities": [{"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}]}

Example input:
Sentence: Total cumulative doses were 36 or 60 g/m2 of ifosfamide ( six or 10 cycles of ifosfamide , vincristine , and dactinomycin [ IVA ] ) .

Example answer:
{"entities": [{"text": "ifosfamide", "type": "Chemical"}, {"text": "ifosfamide , vincristine , and dactinomycin", "type": "Chemical"}, {"text": "IVA", "type": "Chemical"}]}

Example input:
Sentence: Cardiomyopathy is frequent when the total dose exceeds 600 mg/m2 and occurs within one to six months after cessation of therapy .

Example answer:
{"entities": [{"text": "Cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: Mitochondrial radiocalcium uptakes were significantly decreased in animals pretreated with acetylsalicylic acid or dipyridamole or when hydrocortisone was added to the epinephrine infusion ( 2,682,2,803 , and 3,424 counts per minute per gram of dried fraction , respectively ) .

Example answer:
{"entities": [{"text": "radiocalcium", "type": "Chemical"}, {"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine", "type": "Chemical"}]}

Example input:
Sentence: A patient is reported who developed progressive cardiomyopathy two and one-half years after receiving 580 mg/m2 which apparently represents late , late cardiotoxicity .

Example answer:
{"entities": [{"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: Intracerebroventricular injection of U-II also caused an increase in : food intake at doses of 100 and 1,000 ng/mouse , water intake at doses of 100-10,000 ng/mouse , and horizontal locomotion activity at a dose of 10,000 ng/mouse .

Example answer:
{"entities": [{"text": "U-II", "type": "Chemical"}]}

Example input:
Sentence: The aorta/serum-ratio and the radioactive build-up 24 and 48 hours after injection of 131I-HSA was reduced in animals treated with D-pen for 42 days , indicating an impeded transmural transport of tracer which may be caused by a steric exclusion effect of abundant hyaluronate .

Example answer:
{"entities": [{"text": "D-pen", "type": "Chemical"}, {"text": "hyaluronate", "type": "Chemical"}]}

Example input:
Sentence: Myocardial calcium concentrations also were decreased ( 11.2 , 8.3 , and 8.9 mg. per 100 Gm .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: Myocardial concentrations of calcium also increased significantly ( 12.0 vs. 5.0 mg.per 100 Gm .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}]}

Input:
Sentence: A significant increase in the myocardial t1/2 of the I-131 HA was observed only at a higher cumulative dose , 10 mg/kg .

## Item bc5cdr:test:988
Example input:
Sentence: This case suggests that the psychotic symptoms that occur following phenytoin treatment in some epileptic patients may be the direct result of medication , unrelated to seizures .

Example answer:
{"entities": [{"text": "psychotic symptoms", "type": "Disease"}, {"text": "phenytoin", "type": "Chemical"}, {"text": "epileptic", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Amnesia produced by scopolamine and cycloheximide were reversed by morphine given 30 min before the test trial ( pre-test ) , and pre-test morphine also facilitated the memory retrieval in the animals administered naloxone during the training trial .

Example answer:
{"entities": [{"text": "Amnesia", "type": "Disease"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "cycloheximide", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}, {"text": "naloxone", "type": "Chemical"}]}

Example input:
Sentence: The study suggests that the activity-increasing effects of morphine are mediated by the release of catecholamines from adrenergic neurons in the brain .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "catecholamines", "type": "Chemical"}]}

Example input:
Sentence: The results suggest that rigidity , which is assumed to be due to an action of morphine in the striatum , can be antagonized by another process leading to dopaminergic activation in the striatum .

Example answer:
{"entities": [{"text": "rigidity", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: Whereas cocaine-induced seizures were best characterized as brief , generalized , and tonic and resulted in death , those induced by BE were prolonged , often multiple and mixed in type , and rarely resulted in death .

Example answer:
{"entities": [{"text": "cocaine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "death", "type": "Disease"}, {"text": "BE", "type": "Chemical"}]}

Example input:
Sentence: OUTCOME : Following discontinuation of LEV , EEG and neuropsychological findings improved and seizure frequency decreased .

Example answer:
{"entities": [{"text": "LEV", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: One hour after the administration of gamma-HCH , the activity of seizure-inducing agents was increased , regardless of their mechanism , while 24 h after gamma-HCH a differential response was observed .

Example answer:
{"entities": [{"text": "gamma-HCH", "type": "Chemical"}, {"text": "seizure-inducing", "type": "Disease"}]}

Example input:
Sentence: The in vitro data suggest that the site responsible for the decrease in seizure activity 24 h after gamma-HCH may be the GABA-A receptor-linked chloride channel .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}, {"text": "GABA-A", "type": "Chemical"}]}

Example input:
Sentence: Rats treated for 11 days with morphine and withdrawn for 36-40 h showed differences in the development of tolerance : about half of the animals showed a rigidity after the test dose of morphine that was not significantly less than in the controls and were akinetic ( A group ) .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "rigidity", "type": "Disease"}, {"text": "akinetic", "type": "Disease"}]}

Example input:
Sentence: Despite the underlying diseases , the prognosis for drug-induced de novo absence seizure is good because it subsides rapidly after discontinuing the use of the offending drugs .

Example answer:
{"entities": [{"text": "absence seizure", "type": "Disease"}]}

Input:
Sentence: Other known reasons for seizures were ruled out and the convulsions stopped a few hours after cessation of morphine and did not reoccur in the subsequent 8 months .

## Item bc5cdr:test:1058
Example input:
Sentence: L-arginine transport in humans with cortisol-induced hypertension .

Example answer:
{"entities": [{"text": "L-arginine", "type": "Chemical"}, {"text": "cortisol-induced", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: Upregulation of the expression of vasopressin gene in the paraventricular and supraoptic nuclei of the lithium-induced diabetes insipidus rat .

Example answer:
{"entities": [{"text": "vasopressin", "type": "Chemical"}, {"text": "lithium-induced", "type": "Chemical"}, {"text": "diabetes insipidus", "type": "Disease"}]}

Example input:
Sentence: The role of the renin -- angiotensin system in the maintenance of blood pressure during halothane anesthesia and sodium nitroprusside ( SNP ) -induced hypotension was evaluated .

Example answer:
{"entities": [{"text": "angiotensin", "type": "Chemical"}, {"text": "halothane", "type": "Chemical"}, {"text": "sodium nitroprusside", "type": "Chemical"}, {"text": "SNP", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: A deficient L-arginine-nitric oxide system is implicated in cortisol-induced hypertension .

Example answer:
{"entities": [{"text": "L-arginine-nitric oxide", "type": "Chemical"}, {"text": "cortisol-induced", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: This , together with our previous findings that allopurinol failed to prevent adrenocorticotrophic hormone induced hypertension , suggests that XO activity is not a major determinant of GC-HT in the rat .

Example answer:
{"entities": [{"text": "allopurinol", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: Atorvastatin ( Ato ) possesses pleiotropic properties that have been reported to improve endothelial function through increased availability of NO and reduced O2- production in various forms of hypertension .

Example answer:
{"entities": [{"text": "Atorvastatin", "type": "Chemical"}, {"text": "Ato", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}, {"text": "O2-", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: The goal of this study was to determine the role of synthesis/release of bradykinin to activate B2 receptors in disruption of the blood-brain barrier during acute hypertension .

Example answer:
{"entities": [{"text": "bradykinin", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: Portal plasma concentrations of neither arginine vasopressin nor oxytocin are significantly altered in this paradigm .

Example answer:
{"entities": [{"text": "arginine vasopressin", "type": "Chemical"}, {"text": "oxytocin", "type": "Chemical"}]}

Example input:
Sentence: The hypotensive episodes were severe enough to require vasopressor administration .

Example answer:
{"entities": [{"text": "hypotensive", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Vasopressor agents are used to correct anesthesia-induced hypotension .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}]}

Input:
Sentence: However , the role of vasopressin remains to be determined in human essential hypertension .

## Item bc5cdr:test:1353
Example input:
Sentence: Hypertension was observed in animals that had a reduction in glomeruli as well as in a group that did not have a reduction in glomerular number , suggesting that a reduction in glomerular number is not the sole cause for the development of hypertension .

Example answer:
{"entities": [{"text": "Hypertension", "type": "Disease"}, {"text": "reduction in glomerular number", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: Such attenuation was not found in animals which had been injected with GR 55562 into the accumbens core .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}]}

Example input:
Sentence: In two patients , the arrhythmia degenerated into irreversible ventricular fibrillation and both patients died .

Example answer:
{"entities": [{"text": "arrhythmia", "type": "Disease"}, {"text": "ventricular fibrillation", "type": "Disease"}]}

Example input:
Sentence: Following recovery , the monkeys were selectively deafened for high frequencies using kanamycin and furosemide .

Example answer:
{"entities": [{"text": "kanamycin", "type": "Chemical"}, {"text": "furosemide", "type": "Chemical"}]}

Example input:
Sentence: All these effects of DES were more pronounced among previously ovariectomized animals .

Example answer:
{"entities": [{"text": "DES", "type": "Chemical"}]}

Example input:
Sentence: A nonregenerative anemia was the most compromising of the cytopenias and occurred in approximately 50 % of dogs receiving 400-500 mg/kg cefonicid or 540-840 mg/kg cefazedone .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "cytopenias", "type": "Disease"}, {"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}]}

Example input:
Sentence: All animals were similarly symptomatic at the start of levodopa treatment and had similar therapeutic responses to the drug .

Example answer:
{"entities": [{"text": "levodopa", "type": "Chemical"}]}

Example input:
Sentence: The animals were mechanically ventilated to achieve normocarbia ( PCO2 = 42 +/- 1 mmHg , mean +/- SE ) .

Example answer:
{"entities": []}

Example input:
Sentence: Histopathology analyses in the 2 animals that died revealed liver and kidney toxicity , with greater severity in the orally-treated animal .

Example answer:
{"entities": []}

Example input:
Sentence: There was widespread metastatic calcification in the cows that died .

Example answer:
{"entities": []}

Input:
Sentence: Animals became somnolent and none died .

## Item bc5cdr:test:1182
Example input:
Sentence: CASE SUMMARY : A 13-year-old boy was treated with ampicillin and gentamicin because of suspected septicemia .

Example answer:
{"entities": [{"text": "ampicillin", "type": "Chemical"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "septicemia", "type": "Disease"}]}

Example input:
Sentence: This patient underwent a 10-month regimen of rifampin and isoniazid for pulmonary tuberculosis and was discovered to have developed signs of severe renal failure five weeks after completion of therapy .

Example answer:
{"entities": [{"text": "rifampin", "type": "Chemical"}, {"text": "isoniazid", "type": "Chemical"}, {"text": "pulmonary tuberculosis", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: Anaphylaxis was seen in 37 patients ( 69 % ) , the other 17 ( 31 % ) having urticaria and/or angioedema .

Example answer:
{"entities": [{"text": "Anaphylaxis", "type": "Disease"}, {"text": "urticaria", "type": "Disease"}, {"text": "angioedema", "type": "Disease"}]}

Example input:
Sentence: A literature review revealed no prior reports of pericarditis in anti-MPO pANCA-positive vasculitis associated with propylthio- uracil therapy .

Example answer:
{"entities": [{"text": "pericarditis", "type": "Disease"}, {"text": "vasculitis", "type": "Disease"}, {"text": "propylthio- uracil", "type": "Chemical"}]}

Example input:
Sentence: A total of 177 patients were diagnosed as allergic to beta-lactam antibiotics .

Example answer:
{"entities": [{"text": "allergic", "type": "Disease"}, {"text": "beta-lactam", "type": "Chemical"}]}

Example input:
Sentence: An allergic reaction consisting of angioneurotic edema secondary to continuous infusion 5-fluorouracil occurred in a patient with recurrent carcinoma of the oral cavity , cirrhosis , and cisplatin-induced impaired renal function .

Example answer:
{"entities": [{"text": "allergic reaction", "type": "Disease"}, {"text": "angioneurotic edema", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "carcinoma of the oral cavity", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "impaired renal function", "type": "Disease"}]}

Example input:
Sentence: This case study reveals an unusual finding of rapidly proliferative crescentic glomerulonephritis in a patient treated with rifampin who had no other identifiable causes for developing this disease .

Example answer:
{"entities": [{"text": "glomerulonephritis", "type": "Disease"}, {"text": "rifampin", "type": "Chemical"}]}

Example input:
Sentence: A detailed clinical history , together with skin tests , RAST ( radioallergosorbent test ) , and controlled challenge tests , was used to establish whether patients allergic to beta-lactam antibiotics had selective immediate allergic responses to amoxicillin ( AX ) or were cross-reacting with other penicillin derivatives .

Example answer:
{"entities": [{"text": "allergic", "type": "Disease"}, {"text": "beta-lactam", "type": "Chemical"}, {"text": "amoxicillin", "type": "Chemical"}, {"text": "AX", "type": "Chemical"}, {"text": "penicillin", "type": "Chemical"}]}

Example input:
Sentence: Pneumonitis , bilateral pleural effusions , echocardiographic evidence of cardiac tamponade , and positive autoantibodies developed in a 43-year-old man , who was receiving long-term sulfasalazine therapy for chronic ulcerative colitis .

Example answer:
{"entities": [{"text": "Pneumonitis", "type": "Disease"}, {"text": "pleural effusions", "type": "Disease"}, {"text": "cardiac tamponade", "type": "Disease"}, {"text": "sulfasalazine", "type": "Chemical"}, {"text": "ulcerative colitis", "type": "Disease"}]}

Example input:
Sentence: From June 2004 to October 2006 , 11 HBs Ag positive patients with rheumatologic diseases , who were on both immunosuppressive and prophylactic lamivudine therapies , were retrospectively assessed .

Example answer:
{"entities": [{"text": "HBs Ag", "type": "Chemical"}, {"text": "rheumatologic diseases", "type": "Disease"}, {"text": "lamivudine", "type": "Chemical"}]}

Input:
Sentence: In all but 1 patient , antirifampicin antibodies were detected .

## Item bc5cdr:test:713
Example input:
Sentence: The effects of exercise on the severity of isoproterenol-induced myocardial infarction were studied in female albino rats of 20,40,60 and 80 weeks of age .

Example answer:
{"entities": [{"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Nitroglycerin has been shown to reduce ST-segment elevation during acute myocardial infarction , an effect potentiated in the dog by agents that reverse nitroglycerin-induced hypotension .

Example answer:
{"entities": [{"text": "Nitroglycerin", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}, {"text": "nitroglycerin-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Seven patients developed glucose tolerance curves characteristic of diabetes but these were mild , did not require treatment and returned to normal on ceasing didanosine .

Example answer:
{"entities": [{"text": "glucose tolerance curves", "type": "Disease"}, {"text": "diabetes", "type": "Disease"}, {"text": "didanosine", "type": "Chemical"}]}

Example input:
Sentence: The magnitude and time course of the increase in heart rate and the decrease in systolic blood pressure after nitroglycerin were similar in the normal and diabetic subjects without autonomic neuropathy , whereas a lesser increase in heart rate and a greater decrease in systolic blood pressure occurred in the diabetic subjects with autonomic neuropathy .

Example answer:
{"entities": [{"text": "nitroglycerin", "type": "Chemical"}, {"text": "diabetic", "type": "Disease"}, {"text": "autonomic neuropathy", "type": "Disease"}]}

Example input:
Sentence: In patients with diabetes , SCr increases > or = 0.5 mg/dL were 5.1 % ( 4 of 78 patients ) with iopamidol and 13.0 % ( 12 of 92 patients ) with iodixanol ( P=0.11 ) , whereas SCr increases > or = 25 % were 10.3 % and 15.2 % , respectively ( P=0.37 ) .

Example answer:
{"entities": [{"text": "diabetes", "type": "Disease"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}]}

Example input:
Sentence: Preliminary studies suggest that statins could interfere with the risk of recurrence after electrical cardioversion .

Example answer:
{"entities": [{"text": "statins", "type": "Chemical"}]}

Example input:
Sentence: We conclude that in streptozotocin-diabetic rats with an increased urinary albumin excretion , a reduced heparan sulphate charge barrier/density is found at the lamina rara externa of the glomerular basement membrane .

Example answer:
{"entities": [{"text": "streptozotocin-diabetic", "type": "Chemical"}, {"text": "heparan sulphate", "type": "Chemical"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/", "type": "Chemical"}, {"text": "K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}]}

Input:
Sentence: The rapid reversion after insulin treatment excludes the possibility that streptozotocin in itself causes the ISO resistance and points towards a direct insulin effect on myocardial catecholamine sensitivity in diabetic rats .

## Item bc5cdr:test:1212
Example input:
Sentence: Histopathological examination of kidney , heart and lung sections revealed moderate to massive tissue damage with a variety of morphological aberrations by all the three drugs in the absence of GSPE preexposure than in its presence .

Example answer:
{"entities": [{"text": "tissue damage", "type": "Disease"}, {"text": "GSPE", "type": "Chemical"}]}

Example input:
Sentence: Thirteen biopsies were performed from stable functioning renal allografts with informed consent ( nonepisode biopsy ) and the other 13 were from dysfunctional renal allografts with a clinical indication for biopsy ( episode biopsy ) .

Example answer:
{"entities": []}

Example input:
Sentence: The risk of renal papillary necrosis was increased nearly 20-fold by consumption of phenacetin , which also increased the risk for cancer of the renal pelvis and bladder but not for ureteric cancer .

Example answer:
{"entities": [{"text": "renal papillary necrosis", "type": "Disease"}, {"text": "phenacetin", "type": "Chemical"}, {"text": "ureteric cancer", "type": "Disease"}]}

Example input:
Sentence: RESULTS : We found PTCR in 14 of 15 cases of TG , in 7 transplant biopsy specimens without TG , and in 13 of 143 native kidney biopsy specimens .

Example answer:
{"entities": [{"text": "TG", "type": "Disease"}]}

Example input:
Sentence: FINDINGS : The liver biopsy sample showed hepatocellular necrosis which was prominent in perivenular zone three and extended focally from portal tracts to portal tracts and centrilobular areas ( bridging necrosis ) .

Example answer:
{"entities": [{"text": "necrosis", "type": "Disease"}]}

Example input:
Sentence: The biopsy specimen showed pathognomonic features , including eosinophilic infiltration of the interstitial compartment .

Example answer:
{"entities": []}

Example input:
Sentence: The morphological analysis of the kidneys included a semi-quantitative scoring system analysing the degree of striped fibrosis , subcapsular fibrosis and the number of basophilic tubules , plus an additional stereological analysis of the total grade of fibrosis in the cortex stained with Sirius Red .

Example answer:
{"entities": [{"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: Native kidney specimens included a wide range of glomerulopathies as well as cases of thrombotic microangiopathy , malignant hypertension , acute interstitial nephritis , and acute tubular necrosis .

Example answer:
{"entities": [{"text": "glomerulopathies", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "malignant hypertension", "type": "Disease"}, {"text": "interstitial nephritis", "type": "Disease"}, {"text": "acute tubular necrosis", "type": "Disease"}]}

Example input:
Sentence: Biopsies performed in five patients revealed new pathological changes : One membranoproliferative glomerulopathy and interstitial nephritis .

Example answer:
{"entities": [{"text": "membranoproliferative glomerulopathy", "type": "Disease"}, {"text": "interstitial nephritis", "type": "Disease"}]}

Example input:
Sentence: Renal biopsy revealed severe glomerulonephritis with crescents , electron dense fibrillar deposits and moderate lymphocytic interstitial infiltrate .

Example answer:
{"entities": [{"text": "glomerulonephritis", "type": "Disease"}]}

Input:
Sentence: The pathology specimen contained clinically occult invasive carcinoma of the renal pelvis .

## Item bc5cdr:test:997
Example input:
Sentence: The correlation between neuropathic damage and inhibition of neurotoxic esterase or neuropathy target enzyme ( NTE ) was examined in rats acutely exposed to Mipafox ( N , N'-diisopropylphosphorodiamidofluoridate ) , a neurotoxic organophosphate .

Example answer:
{"entities": [{"text": "neuropathic damage", "type": "Disease"}, {"text": "neurotoxic", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}, {"text": "Mipafox", "type": "Chemical"}, {"text": "N , N'-diisopropylphosphorodiamidofluoridate", "type": "Chemical"}, {"text": "organophosphate", "type": "Chemical"}]}

Example input:
Sentence: The rats received AChE reactivator pralidoxime-2-chloride ( 2PAM ) ( 30.0 mg/kg BW ) , anticonvulsant diazepam ( 2.0 mg/kg BW ) , A ( 1 ) -adenosine receptor agonist N ( 6 ) -cyclopentyl adenosine ( CPA ) ( 2.0 mg/kg BW ) , NMDA-receptor antagonist dizocilpine maleate ( +-MK801 hydrogen maleate ) ( 2.0 mg/kg BW ) or their combinations with cholinolytic drug atropine sulfate ( 50.0 mg/kg BW ) immediately or 30 min after the single SC injection of DFP .

Example answer:
{"entities": [{"text": "pralidoxime-2-chloride", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "N ( 6 ) -cyclopentyl adenosine", "type": "Chemical"}, {"text": "CPA", "type": "Chemical"}, {"text": "NMDA-receptor", "type": "Chemical"}, {"text": "dizocilpine maleate", "type": "Chemical"}, {"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: THP exhibited an antipsychotic-like profile by potentiating haloperidol-induced catalepsy , reducing amphetamine-induced hyperactivity and reducing apomorphine-induced climbing in mice .

Example answer:
{"entities": []}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : Both selective and non-selective COX-2 inhibitors were toxic for rats fetuses when administered in the highest dose .

Example answer:
{"entities": []}

Example input:
Sentence: The rats treated with DFP-atropine showed severe typical OP-induced toxicity signs .

Example answer:
{"entities": [{"text": "DFP-atropine", "type": "Chemical"}, {"text": "OP-induced", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: A rat model was developed to examine the effects of chronic CBZ treatment on folate concentrations in the rat .

Example answer:
{"entities": [{"text": "CBZ", "type": "Chemical"}, {"text": "folate", "type": "Chemical"}]}

Example input:
Sentence: Chronic carbamazepine treatment in the rat : efficacy , toxicity , and effect on plasma and tissue folate concentrations .

Example answer:
{"entities": [{"text": "carbamazepine", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "folate", "type": "Chemical"}]}

Example input:
Sentence: In conclusion , CPA , diazepam and 2PAM in combination with atropine prevented the occurrence of serious signs of poisoning and thus reduced the toxicity of DFP in rat .

Example answer:
{"entities": [{"text": "CPA", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "atropine", "type": "Chemical"}, {"text": "poisoning", "type": "Disease"}, {"text": "toxicity", "type": "Disease"}, {"text": "DFP", "type": "Chemical"}]}

Input:
Sentence: Toxic actions of flurazepam ( FZP ) were studied in cats , mice and rats .

## Item bc5cdr:test:970
Example input:
Sentence: The relationship between hippocampal acetylcholine release and cholinergic convulsant sensitivity in withdrawal seizure-prone and withdrawal seizure-resistant selected mouse lines .

Example answer:
{"entities": [{"text": "acetylcholine", "type": "Chemical"}, {"text": "seizure-prone", "type": "Disease"}, {"text": "seizure-resistant", "type": "Disease"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: alpha3 +/- mice were partially resistant to nicotine-induced seizures when compared to wild-type littermates .

Example answer:
{"entities": [{"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: In vitro , gamma-HCH , pentylenetetrazol and picrotoxin were shown to inhibit 3H-TBOB binding in mouse whole brain , with IC50 values of 4.6 , 404 and 9.4 microM , respectively .

Example answer:
{"entities": [{"text": "gamma-HCH", "type": "Chemical"}, {"text": "pentylenetetrazol", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "3H-TBOB", "type": "Chemical"}]}

Example input:
Sentence: The pharmacological challenge data suggest that tolerance may occur to seizure activity induced by PTZ and PTX 24 h after gamma-HCH , since the response to only these two seizure-inducing agents is decreased .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}, {"text": "PTZ", "type": "Chemical"}, {"text": "PTX", "type": "Chemical"}, {"text": "gamma-HCH", "type": "Chemical"}, {"text": "seizure-inducing", "type": "Disease"}]}

Example input:
Sentence: B6 mice were resistant to seizures and slower to reach stages compared to A/J mice .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Sensitivity to several convulsion endpoints induced by nicotine , carbachol , and neostigmine were significantly greater in WSR versus WSP mice .

Example answer:
{"entities": [{"text": "convulsion", "type": "Disease"}, {"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Cholinergic convulsant sensitivity was examined in alcohol-na ve Withdrawal Seizure-Prone ( WSP ) and-Resistant ( WSR ) mice .

Example answer:
{"entities": [{"text": "alcohol-na", "type": "Chemical"}, {"text": "Seizure-Prone", "type": "Disease"}]}

Example input:
Sentence: Specifically , WSP mice may have lower sensitivity to cholinergic convulsants compared with WSR because of postsynaptic receptor desensitization brought on by higher activity of cholinergic neurons .

Example answer:
{"entities": [{"text": "convulsants", "type": "Disease"}]}

Example input:
Sentence: In this study , the severity of response to other seizure-inducing agents was tested in mice 1 and 24 h after intraperitoneal administration of 80 mg/kg gamma-HCH .

Example answer:
{"entities": [{"text": "seizure-inducing", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}]}

Input:
Sentence: The binding sites from seizure sensitive and resistant mice were equally affected by treatment with dithiothreitol , trypsin or heat .

## Item bc5cdr:test:835
Example input:
Sentence: Three hundred fifty-five adult male CSS mice , 58 B6 , and 39 A/J were tested for susceptibility to pilocarpine-induced seizures .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: The effect of PDTC on status epilepticus-associated cell loss in the hippocampus and piriform cortex was evaluated in the rat fractionated pilocarpine model .

Example answer:
{"entities": [{"text": "PDTC", "type": "Chemical"}, {"text": "status", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: QTLs for susceptibility to pilocarpine-induced seizures , a model of temporal lobe epilepsy , have not been reported , and CSS have not previously been used to localize seizure susceptibility genes .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Based on the finding that VPU and VPA could protect the animals against pilocarpine-induced seizure it is suggested that the reduction of inhibitory amino acid neurotransmitters was comparatively minor and offset by a pronounced reduction of glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: Therefore , like VPA , the finding that VPU could drastically reduce pilocarpine-induced increases in glutamate and aspartate should account , at least partly , for its anticonvulsant activity observed in pilocarpine-induced seizure in experimental animals .

Example answer:
{"entities": [{"text": "VPA", "type": "Chemical"}, {"text": "VPU", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: Investigation of mitochondrial involvement in the experimental model of epilepsy induced by pilocarpine .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: A comparable overexpression of Pgp in the BBB was obtained after pilocarpine-induced seizures in wild-type Wistar rats .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Similar to rats , systemic pilocarpine injection causes status epilepticus ( SE ) and the eventual development of spontaneous seizures and mossy fiber sprouting in C57BL/6 and CD1 mice , but the physiological correlates of these events have not been identified in mice .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Input:
Sentence: Pilocarpine , given intraperitoneally to rats , reproduces the neuropathological sequelae of temporal lobe epilepsy and provides a relevant animal model for studying mechanisms of buildup of convulsive activity and pathways operative in the generalization and propagation of seizures within the forebrain .

## Item bc5cdr:test:1104
Example input:
Sentence: Depletion of dopamine in the striatum was also antagonized when LY274614 was given after the injection of amphetamine ; LY274614 protected when given up to 4 hr after but not when given 8 or 24 hr after amphetamine .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "LY274614", "type": "Chemical"}, {"text": "amphetamine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : The utilization of phenylephrine to correct hypotension induced by anesthesia has a negative impact on S ( c ) O ( 2 ) while ephedrine maintains frontal lobe oxygenation potentially related to an increase in CO .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: As a consequence of blocking I ( f ) , clonidine reduced the slope of the diastolic depolarization and the frequency of pacemaker potentials in sinoatrial node cells from wild-type and alpha2ABC-knockout mice .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: The administration of ephedrine led to a similar increase in MAP ( 53 +/- 9 to 79 +/- 8 mmHg ; P < 0.001 ) , restored CO ( 3.2 +/- 1.2 to 5.0 +/- 1.3 l min ( -1 ) ) , and preserved S ( c ) O ( 2 ) .

Example answer:
{"entities": [{"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: It is longer acting than physostigmine and is used in anaesthesia to reverse the non-depolarizing neuromuscular block .

Example answer:
{"entities": [{"text": "physostigmine", "type": "Chemical"}]}

Example input:
Sentence: In SE survivors , similar stimulation resulted in a population spike followed , at a variable latency , by negative DC shifts and repetitive afterdischarges of 3-60 s duration , which were blocked by ionotropic glutamate receptor antagonists .

Example answer:
{"entities": [{"text": "SE", "type": "Disease"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: While she was weak , 2-Hz repetitive stimulation revealed a decrement without significant facilitation at rapid rates or after exercise , suggesting postsynaptic neuromuscular blockade .

Example answer:
{"entities": [{"text": "postsynaptic neuromuscular blockade", "type": "Disease"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Animals were administered nicotine , carbachol , or neostigmine via timed tail vein infusion , and the latencies to onset of tremor and clonus were recorded and converted to threshold dose .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}, {"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: In contrast , both methscopolamine and neostigmine , which do not penetrate the blood-brain barrier , had no effect on the hyperactivity produced by morphine .

Example answer:
{"entities": [{"text": "methscopolamine", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}]}

Input:
Sentence: Repeated doses of edrophonium to 70 mg and neostigmine to 2.5 mg did not antagonize or augment the block .

## Item bc5cdr:test:1069
Example input:
Sentence: In the seventh patient , a permanent ventricular pacemaker was inserted and , despite continuation of procainamide therapy , polymorphous ventricular tachycardia did not reoccur .

Example answer:
{"entities": [{"text": "procainamide", "type": "Chemical"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: Seven cases of procainamide-induced polymorphous ventricular tachycardia are presented .

Example answer:
{"entities": [{"text": "procainamide-induced", "type": "Chemical"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: UM-272 ( N , N-dimethylpropranolol ) , a quaternary antiarrhythmic agent , was administered sublingually to dogs with ouabain-induced ventricular tachycardias .

Example answer:
{"entities": [{"text": "UM-272", "type": "Chemical"}, {"text": "N , N-dimethylpropranolol", "type": "Chemical"}, {"text": "ouabain-induced", "type": "Chemical"}, {"text": "ventricular tachycardias", "type": "Disease"}]}

Example input:
Sentence: A patient with sinuatrial disease and implanted pacemaker was treated with amiodarone ( maximum dose 1000 mg , maintenance dose 800 mg daily ) for 10 months , for control of supraventricular tachyarrhythmias .

Example answer:
{"entities": [{"text": "sinuatrial disease", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "supraventricular tachyarrhythmias", "type": "Disease"}]}

Example input:
Sentence: Iatrogenically induced intractable atrioventricular reentrant tachycardia after verapamil and catheter ablation in a patient with Wolff-Parkinson-White syndrome and idiopathic dilated cardiomyopathy .

Example answer:
{"entities": [{"text": "atrioventricular reentrant tachycardia", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "idiopathic dilated cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: Procainamide-induced polymorphous ventricular tachycardia .

Example answer:
{"entities": [{"text": "Procainamide-induced", "type": "Chemical"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Reduction in the dosage of amiodarone resulted in the disappearance of the sinoatrial block and the persistence of asymptomatic sinus bradycardia .

Example answer:
{"entities": [{"text": "amiodarone", "type": "Chemical"}, {"text": "sinoatrial block", "type": "Disease"}, {"text": "sinus bradycardia", "type": "Disease"}]}

Example input:
Sentence: Amiodarone-induced sinoatrial block .

Example answer:
{"entities": [{"text": "Amiodarone-induced", "type": "Chemical"}, {"text": "sinoatrial block", "type": "Disease"}]}

Example input:
Sentence: We observed sinoatrial block due to chronic amiodarone administration in a 5-year-old boy with primary cardiomyopathy , Wolff-Parkinson-White syndrome and supraventricular tachycardia .

Example answer:
{"entities": [{"text": "sinoatrial block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "primary cardiomyopathy", "type": "Disease"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "supraventricular tachycardia", "type": "Disease"}]}

Input:
Sentence: Alternating sinus rhythm and intermittent sinoatrial block induced by propranolol .

## Item bc5cdr:test:798
Example input:
Sentence: To determine sensitivity we assessed tremor in 44 patients with obstructive lung disease after administration of cumulative doses of salbutamol .

Example answer:
{"entities": [{"text": "tremor", "type": "Disease"}, {"text": "obstructive lung disease", "type": "Disease"}, {"text": "salbutamol", "type": "Chemical"}]}

Example input:
Sentence: Corticosteroids different from paramethasone also produced hypersensitivity reactions in these patients ; however , a few of them were tolerated .

Example answer:
{"entities": [{"text": "paramethasone", "type": "Chemical"}, {"text": "hypersensitivity", "type": "Disease"}]}

Example input:
Sentence: These results show that ipratropium is a more potent bronchodilator than oral theophylline in patients with chronic airflow obstruction .

Example answer:
{"entities": [{"text": "ipratropium", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}, {"text": "chronic airflow obstruction", "type": "Disease"}]}

Example input:
Sentence: Suxamethonium causes prolonged apnea in patients in whom pseudocholinesterase enzyme gets deactivated by organophosphorus ( OP ) poisons .

Example answer:
{"entities": [{"text": "Suxamethonium", "type": "Chemical"}, {"text": "apnea", "type": "Disease"}, {"text": "organophosphorus ( OP ) poisons", "type": "Chemical"}]}

Example input:
Sentence: We present a case of paramedic misjudgment in the execution of a protocol for the treatment of allergic reaction in a case of pulmonary edema with wheezing .

Example answer:
{"entities": [{"text": "allergic reaction", "type": "Disease"}, {"text": "pulmonary edema", "type": "Disease"}, {"text": "wheezing", "type": "Disease"}]}

Example input:
Sentence: Mild hypoxia ( SO2 < 90 % ) was the most common event ( 11 patients ) ; 3 patients ( 2 % ) presented transient hypoxia due to upper airway obstruction by probe introduction and 8 ( 5.8 % ) due to hypoxia caused by MZ use .

Example answer:
{"entities": [{"text": "hypoxia", "type": "Disease"}, {"text": "airway obstruction", "type": "Disease"}, {"text": "MZ", "type": "Chemical"}]}

Example input:
Sentence: In the bolus group , 26.0 % ( 13/50 ) had akathisia compared with 32.7 % ( 16/49 ) in the infusion group ( Delta=-6.7 % ; 95 % confidence interval [ CI ] -24.6 % to 11.2 % ) .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Nine of 30 patients receiving lidocaine experienced TNSs , 1 of 30 patients receiving prilocaine ( P = 0.03 ) had them , and none of 30 patients receiving bupivacaine had TNSs .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "TNSs", "type": "Disease"}, {"text": "prilocaine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: Anaphylaxis was seen in 37 patients ( 69 % ) , the other 17 ( 31 % ) having urticaria and/or angioedema .

Example answer:
{"entities": [{"text": "Anaphylaxis", "type": "Disease"}, {"text": "urticaria", "type": "Disease"}, {"text": "angioedema", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : eleven of 13 patients with a prolonged duration of action of succinylcholine had mutations in BCHE , indicating that this is the possible reason for a prolonged period of apnea .

Example answer:
{"entities": [{"text": "succinylcholine", "type": "Chemical"}, {"text": "apnea", "type": "Disease"}]}

Input:
Sentence: Of 158 asthmatic patients who were placed on inhaled beclomethasone , 15 ( 9.5 % ) developed either hoarseness ( 8 ) , oral thrush ( 6 ) , or both ( 1 ) .

## Item bc5cdr:test:932
Example input:
Sentence: HS diet for 4 wk caused a progressive increase in BP , protein and albumin excretion , and glomerular sclerosis in male DS rats , which were attenuated by castration .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: In conclusion , reductions in creatinine clearance and renal amphotericin B accumulation after chronic amphotericin B administration were enhanced by salt depletion and attenuated by sodium loading in rats .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "amphotericin B", "type": "Chemical"}, {"text": "sodium", "type": "Chemical"}]}

Example input:
Sentence: However , at the end of 3 weeks , amphotericin B levels in the kidneys and liver were significantly higher in salt-depleted and normal-salt rats than those in salt-loaded rats , with plasma/kidney ratios of 21 , 14 , and 8 in salt-depleted , normal-salt , and salt-loaded rats , respectively .

Example answer:
{"entities": [{"text": "amphotericin B", "type": "Chemical"}]}

Example input:
Sentence: The male Wistar rats consuming a diet that contained LiCl ( 60 mmol/kg ) for 4 weeks developed marked polyuria .

Example answer:
{"entities": [{"text": "LiCl", "type": "Chemical"}, {"text": "polyuria", "type": "Disease"}]}

Example input:
Sentence: NX+HP caused a further rise in blood pressure in Li-pretreated rats .

Example answer:
{"entities": [{"text": "Li-pretreated", "type": "Chemical"}]}

Example input:
Sentence: Six weeks after clipping of one renal artery , hypertensive rats ( 178 +/- 4 mm Hg ) were randomly assigned to three groups : untreated hypertensive controls ( n = 8 ) , enalapril-treated ( n = 8 ) , or nitrendipine-treated ( n = 10 ) .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}, {"text": "enalapril-treated", "type": "Chemical"}, {"text": "nitrendipine-treated", "type": "Chemical"}]}

Example input:
Sentence: Treatment for 2 weeks with Warfarin caused massive focal calcification of the artery media in 20-day-old rats and less extensive focal calcification in 42-day-old rats .

Example answer:
{"entities": [{"text": "Warfarin", "type": "Chemical"}, {"text": "calcification of the artery", "type": "Disease"}, {"text": "calcification", "type": "Disease"}]}

Example input:
Sentence: Diabetic rats progressively developed albuminuria reaching 40.3 ( 32.2-62.0 ) mg/24 h after 8 months in contrast to the control animals ( 0.8 ( 0.2-0.9 ) mg/24 h , p < 0.002 ) .

Example answer:
{"entities": [{"text": "Diabetic", "type": "Disease"}, {"text": "albuminuria", "type": "Disease"}]}

Example input:
Sentence: To this end , persistent hyperalgesia was induced by administration of capsaicin in the tail of gonadally intact F344 rats , following which the tail was immersed in a mildly noxious thermal stimulus , and tail-withdrawal latencies measured .

Example answer:
{"entities": [{"text": "hyperalgesia", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Input:
Sentence: Barium-supplemented Long-Evans hooded rats were characterized by a persistent hypertension that was evident after 1 month of barium ( 100 micrograms/ml mineral fortified water ) treatment .

## Item bc5cdr:test:1124
Example input:
Sentence: In experiments using specific adrenergic antagonists , we found that pretreatment with the beta-adrenergic receptor antagonist propranolol blocked cocaine-induced anxiety-like behavior in Dbh +/- and wild-type C57BL6/J mice , while the alpha ( 1 ) antagonist prazosin and the alpha ( 2 ) antagonist yohimbine had no effect .

Example answer:
{"entities": [{"text": "propranolol", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "anxiety-like", "type": "Disease"}, {"text": "prazosin", "type": "Chemical"}, {"text": "yohimbine", "type": "Chemical"}]}

Example input:
Sentence: Such systemic lipopolysaccharide treatment mitigated methamphetamine-induced striatal dopamine and 3,4-dihydroxyphenylacetic acid depletions in a dose-dependent manner .

Example answer:
{"entities": [{"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "methamphetamine-induced", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "3,4-dihydroxyphenylacetic acid", "type": "Chemical"}]}

Example input:
Sentence: Depletion of dopamine in the striatum was also antagonized when LY274614 was given after the injection of amphetamine ; LY274614 protected when given up to 4 hr after but not when given 8 or 24 hr after amphetamine .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "LY274614", "type": "Chemical"}, {"text": "amphetamine", "type": "Chemical"}]}

Example input:
Sentence: The present study sought to characterize the cognitive-enhancing effects of the 5-HT ( 6 ) antagonist Ro4368554 ( 3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole ) in a rat object recognition task employing a cholinergic ( scopolamine pretreatment ) and a serotonergic- ( tryptophan ( TRP ) depletion ) deficient model , and compared its pattern of action with that of the acetylcholinesterase inhibitor metrifonate .

Example answer:
{"entities": [{"text": "5-HT", "type": "Chemical"}, {"text": "Ro4368554", "type": "Chemical"}, {"text": "3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole", "type": "Chemical"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "tryptophan", "type": "Chemical"}, {"text": "TRP", "type": "Chemical"}, {"text": "metrifonate", "type": "Chemical"}]}

Example input:
Sentence: This study aimed at investigating the potential antipsychotic-like properties of SSR103800 , with a particular focus on models of hyperactivity , involving either drug challenge ( ie , amphetamine and MK-801 ) or transgenic mice ( ie , NMDA Nr1 ( neo-/- ) and DAT ( -/- ) ) .

Example answer:
{"entities": [{"text": "SSR103800", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "MK-801", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}]}

Example input:
Sentence: On the other hand , pretreatment with p-chlorophenylalamine ( 3 X 320 mg/kg i.p. , 24 hr ) , a serotonin depletor , caused no significant change in the hyperactivity .

Example answer:
{"entities": [{"text": "p-chlorophenylalamine", "type": "Chemical"}, {"text": "serotonin", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}]}

Example input:
Sentence: In contrast , SSR103800 failed to affect hyperactivity induced by amphetamine or naturally observed in dopamine transporter ( DAT ( -/- ) ) knockout mice ( 10-30 mg/kg p.o . ) .

Example answer:
{"entities": [{"text": "SSR103800", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: We report that prenatally protein deprived ( PD ) female rats showed an increased stereotypic response to apomorphine and an increased locomotor response to amphetamine in adulthood .

Example answer:
{"entities": [{"text": "apomorphine", "type": "Chemical"}, {"text": "amphetamine", "type": "Chemical"}]}

Example input:
Sentence: THP exhibited an antipsychotic-like profile by potentiating haloperidol-induced catalepsy , reducing amphetamine-induced hyperactivity and reducing apomorphine-induced climbing in mice .

Example answer:
{"entities": []}

Example input:
Sentence: The stereotypies induced by d-amphetamine or apomorphine are not potentiated by TRI .

Example answer:
{"entities": [{"text": "d-amphetamine", "type": "Chemical"}, {"text": "apomorphine", "type": "Chemical"}, {"text": "TRI", "type": "Chemical"}]}

Input:
Sentence: However , the increased rearings and the amphetamine-induced stereotypies were not blocked by pretreatment with DSP4 .

## Item bc5cdr:test:1010
Example input:
Sentence: Generally , atropine reduced contractions , but in contrast to controls , it also reduced responses to low electrical field stimulation intensity ( 1-5 Hz ) in inflamed preparations .

Example answer:
{"entities": [{"text": "atropine", "type": "Chemical"}]}

Example input:
Sentence: TCR prevented the isoproterenol-induced decrease in antioxidant enzymes in the heart and increased the rate of ADP-stimulated oxygen uptake and respiratory coupling ratio .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "ADP-stimulated", "type": "Chemical"}, {"text": "oxygen", "type": "Chemical"}]}

Example input:
Sentence: In isolated perfused heart preparations from isoproterenol-pretreated rats , the isoproterenol-induced maximal increase in left ventricular systolic pressure was significantly reduced , compared with saline-pretreated rats ( the EC50 of the isoproterenol-induced increase in left ventricular systolic pressure was enhanced approximately 22-fold ) .

Example answer:
{"entities": [{"text": "isoproterenol-pretreated", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: Neither cardiac vagal nor sympathetic tone was altered by isoproterenol pretreatment .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: Isoproterenol pretreatment for 15 days caused cardiac hypertrophy without affecting baseline blood pressure and heart rate .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "Chemical"}, {"text": "cardiac hypertrophy", "type": "Disease"}]}

Example input:
Sentence: Bromocriptine-induced hypotension was unaffected by isoproterenol pretreatment , while tachycardia was reversed to significant bradycardia , an effect that was partly reduced by i.v .

Example answer:
{"entities": [{"text": "Bromocriptine-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Flestolol produced a dose-dependent attenuation of isoproterenol-induced tachycardia .

Example answer:
{"entities": [{"text": "Flestolol", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: Effects of long-term pretreatment with isoproterenol on bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Input:
Sentence: The effects on isoproterenol tachycardia were determined before and after atropine ( 0.04 mg/kg IV ) .

## Item bc5cdr:test:1251
Example input:
Sentence: She had a gradual return of motor function and ability of feeling Foley catheter .

Example answer:
{"entities": []}

Example input:
Sentence: No changes in haloperidol-induced catalepsy or MK-801-induced locomotion were seen following PD .

Example answer:
{"entities": [{"text": "haloperidol-induced", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "MK-801-induced", "type": "Chemical"}]}

Example input:
Sentence: Postural tremor was measured with the arm horizontally outstretched rest tremor with the arm supported by an armrest and finally tremor was measured after holding a 2-kg weight until exhaustion .

Example answer:
{"entities": [{"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: Guillain-Barr syndrome was the commonest identifiable cause ( 15.6 % ) , accounting for half of the cases with motor neuropathy .

Example answer:
{"entities": [{"text": "Guillain-Barr syndrome", "type": "Disease"}, {"text": "motor neuropathy", "type": "Disease"}]}

Example input:
Sentence: Transient hypotension ( SAP < 90mmHg ) occurred in 1 patient ( 0.7 % ) .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: A 49-year-old woman was transferred to our department because of quadriparesis , lancinating pain , sensory loss , and paresthesia of the distal limbs .

Example answer:
{"entities": [{"text": "quadriparesis", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "sensory loss", "type": "Disease"}, {"text": "paresthesia", "type": "Disease"}]}

Example input:
Sentence: When respiratory failure was produced by hypoventilation ( pH 7.05 to 7.25 ; PC02 70 to 100 mm Hg : P02 20 to 40 mm Hg ) , infusion of aminophylline resulted in an even greater decrease in ventricular fibrillation threshold to 60 percent of the control level .

Example answer:
{"entities": [{"text": "respiratory failure", "type": "Disease"}, {"text": "hypoventilation", "type": "Disease"}, {"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}]}

Example input:
Sentence: Respiratory insufficiency was further worsened by Proteus mirabilis infection and severe bronchoconstriction .

Example answer:
{"entities": [{"text": "Respiratory insufficiency", "type": "Disease"}, {"text": "Proteus mirabilis infection", "type": "Disease"}]}

Example input:
Sentence: Most patients ( 57 % ) stopped treatment because of disease progression .

Example answer:
{"entities": []}

Example input:
Sentence: Mild hypoxia ( SO2 < 90 % ) was the most common event ( 11 patients ) ; 3 patients ( 2 % ) presented transient hypoxia due to upper airway obstruction by probe introduction and 8 ( 5.8 % ) due to hypoxia caused by MZ use .

Example answer:
{"entities": [{"text": "hypoxia", "type": "Disease"}, {"text": "airway obstruction", "type": "Disease"}, {"text": "MZ", "type": "Chemical"}]}

Input:
Sentence: Skeletal movements occurred in 50 % of patients ; 30 % experienced respiratory upset , one sufficiently severe to necessitate abandoning the technique .

## Item bc5cdr:test:994
Example input:
Sentence: The animals were mechanically ventilated to achieve normocarbia ( PCO2 = 42 +/- 1 mmHg , mean +/- SE ) .

Example answer:
{"entities": []}

Example input:
Sentence: Toxicity in rhesus monkeys following administration of the 8-aminoquinoline 8- [ ( 4-amino-l-methylbutyl ) amino ] - 5- ( l-hexyloxy ) -6-methoxy-4-methylquinoline ( WR242511 ) .

Example answer:
{"entities": [{"text": "Toxicity", "type": "Disease"}, {"text": "8-aminoquinoline", "type": "Chemical"}, {"text": "8- [ ( 4-amino-l-methylbutyl ) amino ] - 5- ( l-hexyloxy ) -6-methoxy-4-methylquinoline", "type": "Chemical"}, {"text": "WR242511", "type": "Chemical"}]}

Example input:
Sentence: Streptomycin sulfate ( 300 mg/kg s.c. ) was injected for various periods into preweanling rats and for 3 weeks into weanling rats .

Example answer:
{"entities": [{"text": "Streptomycin", "type": "Chemical"}]}

Example input:
Sentence: Fatal myeloencephalopathy due to accidental intrathecal vincristin administration : a report of two cases .

Example answer:
{"entities": [{"text": "myeloencephalopathy", "type": "Disease"}, {"text": "vincristin", "type": "Chemical"}]}

Example input:
Sentence: Rats were treated with a single IV injection of puromycin aminonucleoside , ( PAN , 7.5 mg/kg ) and 24 hour urine samples were obtained prior to sacrifice on days 3,5,7,10,17,27,41 ( N = 5-10 per group ) .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: Swiss albino mice prepared with intrajugular catheters were tested in photocell cages after administration of 93 mg/kg ( LD50 ) of cocaine and GNC92H2 infusions ranging from 30 to 190 mg/kg .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "GNC92H2", "type": "Chemical"}]}

Example input:
Sentence: Histological and immunohistochemical investigations ( HE-LFB , CD-68 , Neurofilament ) revealed degeneration of myelin and axons as well as pseudocystic transformation in areas exposed to vincristine , accompanied by secondary changes with numerous prominent macrophages .

Example answer:
{"entities": [{"text": "pseudocystic transformation", "type": "Disease"}, {"text": "vincristine", "type": "Chemical"}]}

Example input:
Sentence: METHODS : In this study , WR242511 was administered intravenously ( IV ) in 2 female and 4 male rhesus monkeys in doses of 3.5 and/or 7.0 mg/kg ; a single male also received WR242511 orally ( PO ) at 7.0 mg/kg .

Example answer:
{"entities": [{"text": "WR242511", "type": "Chemical"}]}

Example input:
Sentence: The girl died seven days , the man four weeks after intrathecal injection of vincristine .

Example answer:
{"entities": [{"text": "vincristine", "type": "Chemical"}]}

Example input:
Sentence: We report on two fatal cases of accidental intrathecal vincristine instillation in a 5-year old girl with recurrent acute lymphoblastic leucemia and a 57-year old man with lymphoblastic lymphoma .

Example answer:
{"entities": [{"text": "vincristine", "type": "Chemical"}, {"text": "acute lymphoblastic leucemia", "type": "Disease"}, {"text": "lymphoblastic lymphoma", "type": "Disease"}]}

Input:
Sentence: Intravenous inoculation of 4.2 x 10 ( 10 ) to 7.8 x 10 ( 10 ) pyocin type 6 Pseudomonas organisms in monkeys given vincristine sulfate 4 days previously resulted in fatal infection in 11 of 14 monkeys , whereas none of four receiving Pseudomonas alone died .

## Item bc5cdr:test:809
Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Cyproterone acetate combined with ethinyl estradiol ( CPA/EE ) is licensed in the UK for the treatment of women with acne and hirsutism and is also a treatment option for polycystic ovary syndrome ( PCOS ) .

Example answer:
{"entities": [{"text": "Cyproterone acetate", "type": "Chemical"}, {"text": "ethinyl estradiol", "type": "Chemical"}, {"text": "CPA/EE", "type": "Chemical"}, {"text": "acne", "type": "Disease"}, {"text": "hirsutism", "type": "Disease"}, {"text": "polycystic ovary syndrome", "type": "Disease"}, {"text": "PCOS", "type": "Disease"}]}

Example input:
Sentence: METHODS : For a period of 2 weeks , CsA 15 mg/kg/day ( given orally ) , FK506 3.0 mg/kg/day ( given orally ) or SRL 0.4 mg/kg/day ( given intraperitoneally ) was administered once a day as these doses have earlier been found to achieve a significant immunosuppressive effect in Sprague-Dawley rats .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Seventeen subjects who were genotyped as CYP2D6 extensive metabolizers were enrolled in this randomized , open-label , crossover study to receive a single oral dose of desipramine ( 50 mg ) on two separate occasions , once alone and once after multiple doses of cinacalcet ( 90 mg for 7 days ) .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}]}

Example input:
Sentence: We report a case of a living donor renal transplant recipient who developed cyclosporine-induced TMA that responded to the withdrawal of cyclosporine in conjunction with plasmapheresis and fresh frozen plasma replacement therapy .

Example answer:
{"entities": [{"text": "cyclosporine-induced", "type": "Chemical"}, {"text": "TMA", "type": "Disease"}, {"text": "cyclosporine", "type": "Chemical"}]}

Example input:
Sentence: In the present study , cis-platin ( 80-120 mg/m2BSA ) and 5-FU ( 1000 mg/m2BSA daily as a continuous infusion during 5 days ) were given to 76 patients before radiotherapy and surgery .

Example answer:
{"entities": [{"text": "cis-platin", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}]}

Example input:
Sentence: Severe and clinically evident anemia was easily corrected by subcutaneous injections ( 3 times/week for 1 month ) of recombinant erythropoietin ( rHuEPO-beta ) .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}]}

Example input:
Sentence: The patient cohort ( 14 men , 11 women ) was treated with SRL as conversion therapy , due to chronic allograft nephropathy ( CAN ) ( n = 15 ) neoplasia ( n = 8 ) ; Kaposi 's sarcoma , Four skin cancers , One intestinal tumors , One renal cell carsinom ) or BK virus nephropathy ( n = 2 ) .

Example answer:
{"entities": [{"text": "SRL", "type": "Chemical"}, {"text": "chronic allograft nephropathy", "type": "Disease"}, {"text": "CAN", "type": "Disease"}, {"text": "neoplasia", "type": "Disease"}, {"text": "Kaposi 's sarcoma", "type": "Disease"}, {"text": "skin cancers", "type": "Disease"}, {"text": "intestinal tumors", "type": "Disease"}, {"text": "renal cell carsinom", "type": "Disease"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: A patient who received antithymocyte globulin therapy for aplastic anemia due to D-penicillamine therapy is described .

Example answer:
{"entities": [{"text": "antithymocyte globulin", "type": "Chemical"}, {"text": "aplastic anemia", "type": "Disease"}, {"text": "D-penicillamine", "type": "Chemical"}]}

Example input:
Sentence: We describe a 70-year-old Hispanic woman who developed fulminant hepatic failure necessitating liver transplantation 10 weeks after conversion from simvastatin 40 mg/day to simvastatin 10 mg-ezetimibe 40 mg/day .

Example answer:
{"entities": [{"text": "fulminant hepatic failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "simvastatin 10 mg-ezetimibe 40", "type": "Chemical"}]}

Input:
Sentence: Eighty patients who were to receive CYA 50 mg/kg/d for four days as preparation for marrow grafting underwent a total of 84 transplants for aplastic anemia , Wiskott-Aldrich syndrome , or severe combined immunodeficiency syndrome .

## Item bc5cdr:test:928
Example input:
Sentence: Effects of pallidal neurotensin on haloperidol-induced parkinsonian catalepsy : behavioral and electrophysiological studies .

Example answer:
{"entities": [{"text": "neurotensin", "type": "Chemical"}, {"text": "haloperidol-induced", "type": "Chemical"}, {"text": "parkinsonian catalepsy", "type": "Disease"}]}

Example input:
Sentence: Haloperidol administration ( one dose of 12 mg/kg once a week s.c. ) for 4 weeks caused an increase in vacuous chewing , tongue protrusion and duration of facial twitching observed in four weekly evaluations .

Example answer:
{"entities": [{"text": "Haloperidol", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Bilateral infusions of neurotensin into the globus pallidus reversed haloperidol-induced parkinsonian catalepsy in rats .

Example answer:
{"entities": [{"text": "neurotensin", "type": "Chemical"}, {"text": "haloperidol-induced", "type": "Chemical"}, {"text": "parkinsonian catalepsy", "type": "Disease"}]}

Example input:
Sentence: THP exhibited an antipsychotic-like profile by potentiating haloperidol-induced catalepsy , reducing amphetamine-induced hyperactivity and reducing apomorphine-induced climbing in mice .

Example answer:
{"entities": []}

Example input:
Sentence: These results indicate that noradrenergic neurons have an important role in the manifestation of catalepsy induced by THC , whereas dopaminergic neurons are important in catalepsy induced by haloperidol .

Example answer:
{"entities": [{"text": "catalepsy", "type": "Disease"}, {"text": "THC", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: No changes in haloperidol-induced catalepsy or MK-801-induced locomotion were seen following PD .

Example answer:
{"entities": [{"text": "haloperidol-induced", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "MK-801-induced", "type": "Chemical"}]}

Example input:
Sentence: On the contrary , the cataleptogenic effect of haloperidol was significantly reduced in rats treated with desipramine and 6-OHDA but not in rats treated with 6-OHDA or in rats with lesions of the locus coeruleus .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "desipramine", "type": "Chemical"}, {"text": "6-OHDA", "type": "Chemical"}]}

Example input:
Sentence: 1 h prior to haloperidol resulted in a dose-dependent increase in the catalepsy times ( P < 0.05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: in the rat haloperidol-induced catalepsy model for Parkinson 's disease .

Example answer:
{"entities": [{"text": "haloperidol-induced", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: Catalepsy was induced by haloperidol ( 2 mg/kg p.o .

Example answer:
{"entities": [{"text": "Catalepsy", "type": "Disease"}, {"text": "haloperidol", "type": "Chemical"}]}

Input:
Sentence: Intracranial injection of an acetylcholine-synthesis inhibitor , hemicholinium , prevented the catalepsy that is usually induced by haloperidol .
