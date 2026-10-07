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

## Item bc5cdr:test:408
Example input:
Sentence: She subsequently died some 5 weeks after the commencement of her drug therapy.Post-mortem examination showed evidence of massive hepatocellular necrosis , acute hypersensitivity myocarditis , focal acute tubulo-interstitial nephritis and extensive bone marrow necrosis , with no evidence of malignancy .

Example answer:
{"entities": [{"text": "massive hepatocellular necrosis", "type": "Disease"}, {"text": "myocarditis", "type": "Disease"}, {"text": "nephritis", "type": "Disease"}, {"text": "bone marrow necrosis", "type": "Disease"}, {"text": "malignancy", "type": "Disease"}]}

Example input:
Sentence: Desipramine-induced delirium at `` subtherapeutic '' concentrations : a case report .

Example answer:
{"entities": [{"text": "Desipramine-induced", "type": "Chemical"}, {"text": "delirium", "type": "Disease"}]}

Example input:
Sentence: Three months later the patient was exposed to a single dose of metoprolol , diltiazem , propafenone ( since he had received this drug in the past ) , and sparteine ( as a probe for the debrisoquine/sparteine type polymorphism of oxidative drug metabolism ) .

Example answer:
{"entities": [{"text": "metoprolol", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "propafenone", "type": "Chemical"}, {"text": "sparteine", "type": "Chemical"}, {"text": "debrisoquine/sparteine", "type": "Chemical"}]}

Example input:
Sentence: Within 8 hours after initiation of therapy the patient died with a clinical picture resembling massive pulmonary obstruction due to choriocarcinomic tissue plugs , probably originating from the uterus .

Example answer:
{"entities": [{"text": "pulmonary obstruction", "type": "Disease"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: Delirium was inconsistently recognized clinically in milder cases and was associated with increased length-of-stay and higher costs , and inferior clinical outcome .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}]}

Example input:
Sentence: Simvastatinezetimibe and escitalopram ( which she was taking for depression ) were discontinued , and other potential causes of hepatotoxicity were excluded .

Example answer:
{"entities": [{"text": "Simvastatinezetimibe", "type": "Chemical"}, {"text": "escitalopram", "type": "Chemical"}, {"text": "depression", "type": "Disease"}, {"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Delirium was found in 10 % of clozapine-treated inpatients , particularly in older patients exposed to other central anticholinergics .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}, {"text": "clozapine-treated", "type": "Chemical"}]}

Example input:
Sentence: Delirium , which may be induced by tricyclic drug therapy in the elderly , can be caused by tricyclics with low anticholinergic potency .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}]}

Example input:
Sentence: An elderly patient treated with low dose Desipramine developed a delirium while her plasma level was in the `` subtherapeutic '' range .

Example answer:
{"entities": [{"text": "Desipramine", "type": "Chemical"}, {"text": "delirium", "type": "Disease"}]}

Input:
Sentence: Because no other factors related to this patient changed significantly , the delirium experienced by this patient possibly resulted from misoprostol therapy .

## Item bc5cdr:test:231
Example input:
Sentence: Based on the finding that VPU and VPA could protect the animals against pilocarpine-induced seizure it is suggested that the reduction of inhibitory amino acid neurotransmitters was comparatively minor and offset by a pronounced reduction of glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: The present study aimed to investigate the anticonvulsant activity as well as the effects on the level of hippocampal amino acid neurotransmitters ( glutamate , aspartate , glycine and GABA ) of N- ( 2-propylpentanoyl ) urea ( VPU ) in comparison to its parent compound , valproic acid ( VPA ) .

Example answer:
{"entities": [{"text": "amino acid", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}, {"text": "N- ( 2-propylpentanoyl ) urea", "type": "Chemical"}, {"text": "VPU", "type": "Chemical"}, {"text": "valproic acid", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: This pilot study leads to the conclusion that glutamate supplementation at the chosen regimen fails to protect against peripheral neurotoxicity of PAC .

Example answer:
{"entities": [{"text": "glutamate", "type": "Chemical"}, {"text": "peripheral neurotoxicity", "type": "Disease"}, {"text": "PAC", "type": "Chemical"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: Therefore , like VPA , the finding that VPU could drastically reduce pilocarpine-induced increases in glutamate and aspartate should account , at least partly , for its anticonvulsant activity observed in pilocarpine-induced seizure in experimental animals .

Example answer:
{"entities": [{"text": "VPA", "type": "Chemical"}, {"text": "VPU", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Animal and clinical studies have suggested that N-methyl-D-aspartate ( NMDA ) antagonists , such as ketamine , may be effective in improving opioid analgesia in difficult pain syndromes , such as neuropathic pain .

Example answer:
{"entities": [{"text": "N-methyl-D-aspartate", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "ketamine", "type": "Chemical"}, {"text": "pain", "type": "Disease"}, {"text": "neuropathic pain", "type": "Disease"}]}

Example input:
Sentence: LY274614 , 3SR,4aRS,6SR,8aRS-6- [ phosphonomethyl ] decahydr oisoquinoline-3- carboxylic acid , has been described as a potent antagonist of the N-methyl-D-aspartate ( NMDA ) subtype of glutamate receptor .

Example answer:
{"entities": [{"text": "LY274614", "type": "Chemical"}, {"text": "3SR,4aRS,6SR,8aRS-6- [ phosphonomethyl ] decahydr oisoquinoline-3- carboxylic acid", "type": "Chemical"}, {"text": "N-methyl-D-aspartate", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: Pretreatment with either VPU ( 50 and 100 mg/kg ) or VPA ( 300 and 600 mg/kg ) completely abolished pilocarpine-evoked increases in extracellular glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-evoked", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: In acute pain models , N-methyl-D-aspartate ( NMDA ) antagonists enhance the antinociceptive effects of morphine to a greater extent in males than females .

Example answer:
{"entities": [{"text": "acute pain", "type": "Disease"}, {"text": "N-methyl-D-aspartate", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}]}

Input:
Sentence: These effects were completely antagonized by pretreatment with a glutamate/N-methyl-D-aspartate antagonist , aminophosphonovaleric acid .

## Item bc5cdr:test:362
Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "Disease"}, {"text": "METH", "type": "Chemical"}, {"text": "MPTP", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "METH-induced", "type": "Chemical"}]}

Example input:
Sentence: By using this strategy to study the involvement of MRP2 in brain access of antiepileptic drugs ( AEDs ) , we recently reported that phenytoin is a substrate for MRP2 in the BBB .

Example answer:
{"entities": [{"text": "phenytoin", "type": "Chemical"}]}

Example input:
Sentence: The effect of PDTC on status epilepticus-associated cell loss in the hippocampus and piriform cortex was evaluated in the rat fractionated pilocarpine model .

Example answer:
{"entities": [{"text": "PDTC", "type": "Chemical"}, {"text": "status", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: Similar to rats , systemic pilocarpine injection causes status epilepticus ( SE ) and the eventual development of spontaneous seizures and mossy fiber sprouting in C57BL/6 and CD1 mice , but the physiological correlates of these events have not been identified in mice .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: A significant decrease in neuronal density of the hippocampal hilar formation was identified in vehicle- and PDTC-treated rats following status epilepticus .

Example answer:
{"entities": [{"text": "PDTC-treated", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}]}

Example input:
Sentence: These data might indicate that the generation of reactive oxygen species and activation of NF-kappaB plays a more central role in seizure-associated neuronal damage in the temporal cortex as compared to the hippocampal hilus .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "seizure-associated", "type": "Disease"}, {"text": "neuronal damage", "type": "Disease"}]}

Example input:
Sentence: In vehicle-treated rats , status epilepticus caused pronounced neuronal damage in the piriform cortex comprising both pyramidal cells and interneurons .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "neuronal damage", "type": "Disease"}]}

Example input:
Sentence: In this study , we investigated whether increased generation of FR during status epilepticus would be sufficient to provoke abnormalities in mtDNA and in the expression and activity of cytochrome c oxidase ( CCO ) , complex IV of the respiratory chain , in the chronic phase of the pilocarpine model of temporal lobe epilepsy .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}, {"text": "temporal lobe epilepsy", "type": "Disease"}]}

Example input:
Sentence: Mitochondrial abnormalities have been associated with several aspects of epileptogenesis , such as energy generation , control of cell death , neurotransmitter synthesis , and free radical ( FR ) production .

Example answer:
{"entities": [{"text": "Mitochondrial abnormalities", "type": "Disease"}, {"text": "death", "type": "Disease"}]}

Input:
Sentence: Both cell elements may suffer in common from metabolic disturbance and neurotransmitter dysfunction as occur during massive status epilepticus .

## Item bc5cdr:test:328
Example input:
Sentence: A patient who received antithymocyte globulin therapy for aplastic anemia due to D-penicillamine therapy is described .

Example answer:
{"entities": [{"text": "antithymocyte globulin", "type": "Chemical"}, {"text": "aplastic anemia", "type": "Disease"}, {"text": "D-penicillamine", "type": "Chemical"}]}

Example input:
Sentence: We describe a 15-yr-old girl who had orthotopic liver transplantation because of Wilson 's disease .

Example answer:
{"entities": [{"text": "Wilson 's disease", "type": "Disease"}]}

Example input:
Sentence: Despite therapy with ursodeoxycholic acid , prednisone , and then tacrolimus , her cholestatic disease was unrelenting , with cirrhosis shown by biopsy 6 months after presentation .

Example answer:
{"entities": [{"text": "ursodeoxycholic acid", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "cholestatic disease", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}]}

Example input:
Sentence: We report on two fatal cases of accidental intrathecal vincristine instillation in a 5-year old girl with recurrent acute lymphoblastic leucemia and a 57-year old man with lymphoblastic lymphoma .

Example answer:
{"entities": [{"text": "vincristine", "type": "Chemical"}, {"text": "acute lymphoblastic leucemia", "type": "Disease"}, {"text": "lymphoblastic lymphoma", "type": "Disease"}]}

Example input:
Sentence: We report the case of a patient who developed acute hepatitis with extensive hepatocellular necrosis , 7 months after the onset of administration of clotiazepam , a thienodiazepine derivative .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}, {"text": "extensive hepatocellular necrosis", "type": "Disease"}, {"text": "clotiazepam", "type": "Chemical"}, {"text": "thienodiazepine", "type": "Chemical"}]}

Example input:
Sentence: A patient with cryptogenic cirrhosis and disseminated sporotrichosis developed acute renal failure immediately following the administration of amphotericin B on four separate occasions .

Example answer:
{"entities": [{"text": "cirrhosis", "type": "Disease"}, {"text": "sporotrichosis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}]}

Example input:
Sentence: Respiratory insufficiency was further worsened by Proteus mirabilis infection and severe bronchoconstriction .

Example answer:
{"entities": [{"text": "Respiratory insufficiency", "type": "Disease"}, {"text": "Proteus mirabilis infection", "type": "Disease"}]}

Example input:
Sentence: We report the case of a patient in whom troleandomycin-induced hepatitis was followed by prolonged anicteric cholestasis .

Example answer:
{"entities": [{"text": "troleandomycin-induced", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}, {"text": "cholestasis", "type": "Disease"}]}

Example input:
Sentence: Within 8 hours after initiation of therapy the patient died with a clinical picture resembling massive pulmonary obstruction due to choriocarcinomic tissue plugs , probably originating from the uterus .

Example answer:
{"entities": [{"text": "pulmonary obstruction", "type": "Disease"}]}

Example input:
Sentence: She subsequently died some 5 weeks after the commencement of her drug therapy.Post-mortem examination showed evidence of massive hepatocellular necrosis , acute hypersensitivity myocarditis , focal acute tubulo-interstitial nephritis and extensive bone marrow necrosis , with no evidence of malignancy .

Example answer:
{"entities": [{"text": "massive hepatocellular necrosis", "type": "Disease"}, {"text": "myocarditis", "type": "Disease"}, {"text": "nephritis", "type": "Disease"}, {"text": "bone marrow necrosis", "type": "Disease"}, {"text": "malignancy", "type": "Disease"}]}

Input:
Sentence: Two weeks before his death he was readmitted because of aplastic crisis with septicemia and marked abnormalities in liver function and died of hemorrhagic bronchopneumonia .

## Item bc5cdr:test:224
Example input:
Sentence: It has been shown that bromocriptine-induced tachycardia , which persisted after adrenalectomy , is ( i ) mediated by central dopamine D2 receptor activation and ( ii ) reduced by 5-day isoproterenol pretreatment , supporting therefore the hypothesis that this effect is dependent on sympathetic outflow to the heart .

Example answer:
{"entities": [{"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: Immunohistochemical , electron microscopic and morphometric studies of estrogen-induced rat prolactinomas after bromocriptine treatment .

Example answer:
{"entities": [{"text": "estrogen-induced", "type": "Chemical"}, {"text": "prolactinomas", "type": "Disease"}, {"text": "bromocriptine", "type": "Chemical"}]}

Example input:
Sentence: Hyperprolactinemia can reduce fertility and libido .

Example answer:
{"entities": [{"text": "Hyperprolactinemia", "type": "Disease"}]}

Example input:
Sentence: Chronic hyperprolactinemia induced by the dopamine antagonist sulpiride caused a 40 % reduction LH pulse frequency in ovariectomized rats , but only in the presence of chronic low levels of estradiol .

Example answer:
{"entities": [{"text": "hyperprolactinemia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "sulpiride", "type": "Chemical"}, {"text": "estradiol", "type": "Chemical"}]}

Example input:
Sentence: Endocrine therapy consisted of testosterone heptylate or human chorionic gonadotropin for hypogonadism and bromocriptine for hyperprolactinemia .

Example answer:
{"entities": [{"text": "testosterone heptylate", "type": "Chemical"}, {"text": "hypogonadism", "type": "Disease"}, {"text": "bromocriptine", "type": "Chemical"}, {"text": "hyperprolactinemia", "type": "Disease"}]}

Example input:
Sentence: We first tested whether chronic hyperprolactinemia inhibited two neuroendocrine parameters necessary for female fertility : pulsatile LH secretion and the estrogen-induced LH surge .

Example answer:
{"entities": [{"text": "hyperprolactinemia", "type": "Disease"}, {"text": "estrogen-induced", "type": "Chemical"}]}

Example input:
Sentence: To clarify the effects of bromocriptine on prolactinoma cells in vivo , immunohistochemical , ultrastructural and morphometrical analyses were applied to estrogen-induced rat prolactinoma cells 1 h and 6 h after injection of bromocriptine ( 3 mg/kg of body weight ) .

Example answer:
{"entities": [{"text": "bromocriptine", "type": "Chemical"}, {"text": "prolactinoma", "type": "Disease"}, {"text": "estrogen-induced", "type": "Chemical"}]}

Example input:
Sentence: However , only secretory granules showed the positive reaction products for prolactin 6 h after bromocriptine treatment of the adenoma cells .

Example answer:
{"entities": [{"text": "bromocriptine", "type": "Chemical"}, {"text": "adenoma", "type": "Disease"}]}

Example input:
Sentence: These findings suggest that lowered serum prolactin levels in the early phase of bromocriptine treatment may result from an impaired secretion of prolactin due to decreasing numbers of cytoplasmic microtubules .

Example answer:
{"entities": [{"text": "bromocriptine", "type": "Chemical"}]}

Example input:
Sentence: Bromocriptine was definitely effective in cases with prolactin greater than 35 ng./ml .

Example answer:
{"entities": [{"text": "Bromocriptine", "type": "Chemical"}]}

Input:
Sentence: Six stable psychiatric outpatients with hyperprolactinemia and amenorrhea/oligomenorrhea associated with their neuroleptic medications were treated with bromocriptine .

## Item bc5cdr:test:461
Example input:
Sentence: Mean serum creatinine level before conversion was 2.21 mg/dL and thereafter , 4.93 mg/dL ( P = .02 ) .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: Serum creatinine values did not change significantly : 1.98 +/- 0.8 mg/dL before SRL therapy and 2.53 +/- 1.9 mg/dL at last follow-up ( P = .14 ) .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: The number of previous manic episodes did not affect the probability of switching , whereas a high score on the hyperthymia component of the Semistructured Affective Temperament Interview was associated with a greater risk of switching ( p = .008 ) .

Example answer:
{"entities": [{"text": "manic", "type": "Disease"}]}

Example input:
Sentence: Calcium concentrations 1 day postpartum were higher in cows treated with vitamin D3 about 32 days prepartum ( 8.8 mg/100 ml ) than in control cows ( 5.5 mg/100 ml ) .

Example answer:
{"entities": [{"text": "Calcium", "type": "Chemical"}, {"text": "vitamin D3", "type": "Chemical"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}, {"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: The events are consistent with a severe reaction to calcium chelation by sodium citrate anticoagulant resulting in symptomatic systemic hypocalcemia .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "sodium citrate", "type": "Chemical"}, {"text": "hypocalcemia", "type": "Disease"}]}

Example input:
Sentence: A patient is reported who developed progressive cardiomyopathy two and one-half years after receiving 580 mg/m2 which apparently represents late , late cardiotoxicity .

Example answer:
{"entities": [{"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: Before the switch , 11.5 % of patients had high-grade proteinuria ( > 1.0 g/day ) ; this increased to 22.9 % postswitch ( p = 0.006 ) .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: Myocardial calcium concentrations also were decreased ( 11.2 , 8.3 , and 8.9 mg. per 100 Gm .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}]}

Example input:
Sentence: Myocardial concentrations of calcium also increased significantly ( 12.0 vs. 5.0 mg.per 100 Gm .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}]}

Input:
Sentence: In addition to experiencing hypercalcemic episodes with peak calcium values of 2.7 to 3.8 mmol/L ( 10.7 to 15.0 mg/dL ) , patients in the hypercalcemic group exhibited a significant increase in the mean calcium concentration obtained during 6 months before the switch , compared with the mean value obtained during the 7 months of observation after the switch ( 2.4 +/- 0.03 to 2.5 +/- 0.03 mmol/L [ 9.7 +/- 0.2 to 10.2 +/- 0.1 mg/dL ] , P = 0.006 ) .

## Item bc5cdr:test:458
Example input:
Sentence: Compared with control patients , CRF and ESRD patients had higher preoperative serum creatinine levels , a greater percentage of patients with hepatorenal syndrome , higher percentage requirement for dialysis in the first 3 months postoperatively , and a higher 1-year serum creatinine .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "hepatorenal syndrome", "type": "Disease"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Disease"}]}

Example input:
Sentence: Patients who developed renal insufficiency had lower baseline body weight and higher baseline serum creatinine , required higher doses of loop diuretics , and were more likely to be treated with thiazide diuretics than controls .

Example answer:
{"entities": [{"text": "renal insufficiency", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "thiazide", "type": "Chemical"}]}

Example input:
Sentence: Upon additional retrospective analysis , it was noted that bumetanide is a loop diuretic that may cause significant hypocalcemia .

Example answer:
{"entities": [{"text": "bumetanide", "type": "Chemical"}, {"text": "loop diuretic", "type": "Chemical"}, {"text": "hypocalcemia", "type": "Disease"}]}

Example input:
Sentence: High doses of the vitamin K antagonist Warfarin are also known to cause calcification of the artery media , but at treatment times of 2 weeks or longer yet not at 1 week .

Example answer:
{"entities": [{"text": "vitamin K", "type": "Chemical"}, {"text": "Warfarin", "type": "Chemical"}, {"text": "calcification of the artery", "type": "Disease"}]}

Example input:
Sentence: High doses of vitamin D are known to cause calcification of the artery media in as little as 3 to 4 days .

Example answer:
{"entities": [{"text": "vitamin D", "type": "Chemical"}, {"text": "calcification of the artery", "type": "Disease"}]}

Example input:
Sentence: Large parenteral doses of vitamin D3 ( 15 to 17.5 x 10 ( 6 ) IU vitamin D3 ) were associated with prolonged hypercalcemia , hyperphosphatemia , and large increases of vitamin D3 and its metabolites in the blood plasma of nonlactating nonpregnant and pregnant Jersey cows .

Example answer:
{"entities": [{"text": "vitamin D3", "type": "Chemical"}, {"text": "hypercalcemia", "type": "Disease"}, {"text": "hyperphosphatemia", "type": "Disease"}]}

Example input:
Sentence: There was a close parallel between the effect of vitamin D dose on artery calcification and the effect of vitamin D dose on the elevation of serum calcium , which suggests that vitamin D may induce artery calcification through its effect on serum calcium .

Example answer:
{"entities": [{"text": "vitamin D", "type": "Chemical"}, {"text": "artery calcification", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}]}

Example input:
Sentence: Two patients with similar clinical features are presented : both patients had chronic renal failure , on hemodialysis for many years but recently begun on a high-flux dialyzer ; both had been receiving a carbidopa/levodopa preparation ; and both had the onset of hallucinosis and recurrent seizures , which were refractory to anticonvulsants .

Example answer:
{"entities": [{"text": "chronic renal failure", "type": "Disease"}, {"text": "carbidopa/levodopa", "type": "Chemical"}, {"text": "hallucinosis", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: The events are consistent with a severe reaction to calcium chelation by sodium citrate anticoagulant resulting in symptomatic systemic hypocalcemia .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "sodium citrate", "type": "Chemical"}, {"text": "hypocalcemia", "type": "Disease"}]}

Input:
Sentence: Etiology of hypercalcemia in hemodialysis patients on calcium carbonate therapy .

## Item bc5cdr:test:567
Example input:
Sentence: Mean arterial pressure was decreased to 50 mm Hg for 30 minutes either by hemorrhage ( HEM , n = 7 ) or by continuous infusion of sodium nitroprusside ( SNP , n = 7 ) .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "Disease"}, {"text": "HEM", "type": "Disease"}, {"text": "sodium nitroprusside", "type": "Chemical"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: Anaesthesia was maintained with an inspired isoflurane concentration of 0.75 % ( plus 67 % nitrous oxide in oxygen ) , during which CBF and CMRO2 were 34.3 +/- 2.1 ml/100 g min-1 and 2.32 +/- 0.16 ml/100 g min-1 at PaCO2 4.1 +/- 0.1 kPa ( mean +/- SEM ) .

Example answer:
{"entities": [{"text": "isoflurane", "type": "Chemical"}, {"text": "nitrous oxide", "type": "Chemical"}, {"text": "oxygen", "type": "Chemical"}]}

Example input:
Sentence: Controlled hypotension in groups A and C was induced with PGE1 to maintain mean arterial blood pressure at 55 mmHg for 180 min .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "PGE1", "type": "Chemical"}]}

Example input:
Sentence: When respiratory failure was produced by hypoventilation ( pH 7.05 to 7.25 ; PC02 70 to 100 mm Hg : P02 20 to 40 mm Hg ) , infusion of aminophylline resulted in an even greater decrease in ventricular fibrillation threshold to 60 percent of the control level .

Example answer:
{"entities": [{"text": "respiratory failure", "type": "Disease"}, {"text": "hypoventilation", "type": "Disease"}, {"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}]}

Example input:
Sentence: Mean arterial pressure ( as a percentage of control +/- SEM ) during randomized infusions of 0.03 , 0.1 , 0.3 , or 1.0 microgram/kg/min was 99 +/- 1 , 95 +/- 1 ( p less than 0.05 ) , 93 +/- 1 ( p less than 0.01 ) , or 79 +/- 6 % ( p less than 0.001 ) , respectively , but no tachycardia and no augmentation of the norepinephrine release rate ( up to 0.3 microgram/kg/min ) were observed , which is in contrast to comparable hypotension induced by hydralazine or nitroglycerin .

Example answer:
{"entities": [{"text": "tachycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "hydralazine", "type": "Chemical"}, {"text": "nitroglycerin", "type": "Chemical"}]}

Example input:
Sentence: It is concluded that increases in the SPV and the delta down are characteristic of a hypotensive state due to a predominant decrease in preload .

Example answer:
{"entities": [{"text": "hypotensive", "type": "Disease"}]}

Example input:
Sentence: Transient hypotension ( SAP < 90mmHg ) occurred in 1 patient ( 0.7 % ) .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: The delta down , which is the measure of decrease of SBP after a mechanical breath , was 20.3 +/- 8.4 and 10.1 +/- 3.8 mm Hg in the HEM and SNP groups , respectively , during hypotension ( P less than 0.02 ) .

Example answer:
{"entities": [{"text": "HEM", "type": "Disease"}, {"text": "SNP", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Controlled hypotension to an average MAP of 50-55 mm Hg was induced by increasing the dose of isoflurane , and maintained at an inspired concentration of 2.2 +/- 0.2 % .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "Hg", "type": "Chemical"}, {"text": "isoflurane", "type": "Chemical"}]}

Example input:
Sentence: The SPV during hypotension was 15.7 +/- 6.7 mm Hg in the HEM group , compared with 9.1 +/- 2.0 mm Hg in the SNP group ( P less than 0.02 ) .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "HEM", "type": "Disease"}, {"text": "SNP", "type": "Chemical"}]}

Input:
Sentence: The mean H concentration during hypotension in the inspiratory gas was 0.7 +/- 0.1 vol % , the mean E concentration 1.6 +/- 0.2 vol % , and the mean I concentration 1.0 +/- 0.1 vol % .

## Item bc5cdr:test:452
Example input:
Sentence: CONCLUSION : Higher OD is associated with significant risk of subsequent thrombosis in patients with isolated-HIT ; percent inhibition , however , was not predictive .

Example answer:
{"entities": [{"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: We conclude that noxious stimulation of facial mucosa increases intracranial blood flow and lacrimation via a trigemino-parasympathetic reflex .

Example answer:
{"entities": []}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: In individuals with preexisting , high-grade coronary arterial narrowing , acute myocardial infarction may result from an increase in myocardial oxygen demand associated with cocaine-induced increase in rate-pressure product .

Example answer:
{"entities": [{"text": "acute myocardial infarction", "type": "Disease"}, {"text": "oxygen", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}]}

Example input:
Sentence: Noxious chemical stimulation of rat facial mucosa increases intracranial blood flow through a trigemino-parasympathetic reflex -- an experimental model for vascular dysfunctions in cluster headache .

Example answer:
{"entities": [{"text": "vascular dysfunctions", "type": "Disease"}, {"text": "cluster headache", "type": "Disease"}]}

Example input:
Sentence: In microdialysis experiments , the lines did not differ in basal release of ACh , and 50 mM KCl increased ACh output in both lines of mice .

Example answer:
{"entities": [{"text": "ACh", "type": "Chemical"}, {"text": "KCl", "type": "Chemical"}]}

Example input:
Sentence: While contractions to carbachol and ATP were the same in inflamed and in control strips when related to a reference potassium response , isoprenaline-induced relaxations were smaller in inflamed strips .

Example answer:
{"entities": [{"text": "carbachol", "type": "Chemical"}, {"text": "ATP", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}, {"text": "isoprenaline-induced", "type": "Chemical"}]}

Example input:
Sentence: This drug caused biventricular dysfunction , due to its negative inotropic effect , and hypotension , due to its peripheral vasodilatory effect .

Example answer:
{"entities": [{"text": "biventricular dysfunction", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : The rate of contrast-induced nephropathy , defined by multiple end points , is not statistically different after the intraarterial administration of iopamidol or iodixanol to high-risk patients , with or without diabetes mellitus .

Example answer:
{"entities": [{"text": "nephropathy", "type": "Disease"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}, {"text": "diabetes mellitus", "type": "Disease"}]}

Example input:
Sentence: Nitroprusside-induced hypotension evokes ACTH secretion which is primarily mediated by enhanced secretion of immunoreactive corticotropin-releasing factor ( irCRF ) into the hypophysial-portal circulation .

Example answer:
{"entities": [{"text": "Nitroprusside-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Input:
Sentence: Finally , two mechanisms at least , direct vasodilation and flow dependency , are involved in the cromakalim- and pinacidil-induced increase in CxAD .

## Item bc5cdr:test:327
Example input:
Sentence: A 54-year-old hypothyroid male taking thyroxine and simvastatin presented with bilateral leg compartment syndrome and myonecrosis .

Example answer:
{"entities": [{"text": "hypothyroid", "type": "Disease"}, {"text": "thyroxine", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "compartment syndrome", "type": "Disease"}, {"text": "myonecrosis", "type": "Disease"}]}

Example input:
Sentence: Combined androgen blockade-induced anemia in prostate cancer patients without bone involvement .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "prostate cancer", "type": "Disease"}]}

Example input:
Sentence: Fanconi syndrome , as well as myopathy , is well recognized in patients with mitochondrial disorders and caused by depletion of mtDNA .

Example answer:
{"entities": [{"text": "Fanconi syndrome", "type": "Disease"}, {"text": "myopathy", "type": "Disease"}, {"text": "mitochondrial disorders", "type": "Disease"}]}

Example input:
Sentence: A patient who received antithymocyte globulin therapy for aplastic anemia due to D-penicillamine therapy is described .

Example answer:
{"entities": [{"text": "antithymocyte globulin", "type": "Chemical"}, {"text": "aplastic anemia", "type": "Disease"}, {"text": "D-penicillamine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : Our data suggest that rHuEPO-beta correctable CAB-induced anemia occurs in 14.3 % of prostate cancer patients after 6 months of therapy .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "prostate cancer", "type": "Disease"}]}

Example input:
Sentence: Two subsets of patients were identified from this latter group : the first included four patients ( 5 % of the total population ) who developed major toxicity resulting in Fanconi 's syndrome ( TDFS ) ; and the second group included five patients with elevated beta 2 microglobulinuria and low phosphate reabsorption .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "Fanconi 's syndrome", "type": "Disease"}, {"text": "TDFS", "type": "Disease"}, {"text": "phosphate", "type": "Chemical"}]}

Example input:
Sentence: The development of severe CAB-induced anemia in prostate cancer patients did not correlate with T baseline values ( T < 3 ng/ml versus T > or = 3 ng/ml ) , with age ( < 76 yrs versus > or = 76 yrs ) , and clinical stage ( stage C versus stage D1 ) .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "prostate cancer", "type": "Disease"}]}

Example input:
Sentence: We report on two fatal cases of accidental intrathecal vincristine instillation in a 5-year old girl with recurrent acute lymphoblastic leucemia and a 57-year old man with lymphoblastic lymphoma .

Example answer:
{"entities": [{"text": "vincristine", "type": "Chemical"}, {"text": "acute lymphoblastic leucemia", "type": "Disease"}, {"text": "lymphoblastic lymphoma", "type": "Disease"}]}

Example input:
Sentence: Three yr after transplantation she developed renal Fanconi syndrome with severe metabolic acidosis , hypophosphatemia , glycosuria , and aminoaciduria .

Example answer:
{"entities": [{"text": "renal Fanconi syndrome", "type": "Disease"}, {"text": "metabolic acidosis", "type": "Disease"}, {"text": "hypophosphatemia", "type": "Disease"}, {"text": "glycosuria", "type": "Disease"}, {"text": "aminoaciduria", "type": "Disease"}]}

Example input:
Sentence: CASE SUMMARY : A 13-year-old boy was treated with ampicillin and gentamicin because of suspected septicemia .

Example answer:
{"entities": [{"text": "ampicillin", "type": "Chemical"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "septicemia", "type": "Disease"}]}

Input:
Sentence: The case of an 11-year-old boy is reported who was known to have Fanconi 's anemia for 3 years and was treated with androgens , corticosteroids and transfusions .

## Item bc5cdr:test:393
Example input:
Sentence: Conventional agents are associated with unwanted central nervous system effects , including extrapyramidal symptoms ( EPS ) , tardive dyskinesia , sedation , and possible impairment of some cognitive measures , as well as cardiac effects , orthostatic hypotension , hepatic changes , anticholinergic side effects , sexual dysfunction , and weight gain .

Example answer:
{"entities": [{"text": "extrapyramidal symptoms", "type": "Disease"}, {"text": "EPS", "type": "Disease"}, {"text": "tardive dyskinesia", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}]}

Example input:
Sentence: Based on these observations , it is concluded that 5-HT2 blockade obtained with risperidone at D2 occupancy rates of 60 % and above does not appear to protect against the risk for extrapyramidal side effects .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}]}

Example input:
Sentence: In other words , the present results suggest that the accumbal shell 5-HT1B receptors play a permissive role in the behavioural response to the psychostimulant .

Example answer:
{"entities": []}

Example input:
Sentence: The underlying mechanism of withdrawal-emergent RS in the present case may have been related to the pharmacological profile of risperidone , a serotonin-dopamine antagonist , suggesting the pathophysiologic influence of the serotonin system in the development of RS .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}, {"text": "serotonin-dopamine", "type": "Chemical"}, {"text": "serotonin", "type": "Chemical"}, {"text": "RS", "type": "Disease"}]}

Example input:
Sentence: The typical fluoxetine-induced symptoms of restlessness , constant pacing , purposeless movements of the feet and legs , and marked anxiety were indistinguishable from those of neuroleptic-induced akathisia .

Example answer:
{"entities": [{"text": "fluoxetine-induced", "type": "Chemical"}, {"text": "anxiety", "type": "Disease"}, {"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: Acute psychosis due to treatment with phenytoin in a nonepileptic patient .

Example answer:
{"entities": [{"text": "Acute psychosis", "type": "Disease"}, {"text": "phenytoin", "type": "Chemical"}]}

Example input:
Sentence: This case suggests that the psychotic symptoms that occur following phenytoin treatment in some epileptic patients may be the direct result of medication , unrelated to seizures .

Example answer:
{"entities": [{"text": "psychotic symptoms", "type": "Disease"}, {"text": "phenytoin", "type": "Chemical"}, {"text": "epileptic", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: In the present paper the authors describe 2 female patients who developed incontinence secondary to the selective serotonin reuptake inhibitors paroxetine and sertraline , as well as a third who developed this side effect on venlafaxine .

Example answer:
{"entities": [{"text": "incontinence", "type": "Disease"}, {"text": "serotonin", "type": "Chemical"}, {"text": "paroxetine", "type": "Chemical"}, {"text": "sertraline", "type": "Chemical"}, {"text": "venlafaxine", "type": "Chemical"}]}

Example input:
Sentence: The case of a nonepileptic patient who developed psychosis following phenytoin treatment for trigeminal neuralgia is described .

Example answer:
{"entities": [{"text": "psychosis", "type": "Disease"}, {"text": "phenytoin", "type": "Chemical"}, {"text": "trigeminal neuralgia", "type": "Disease"}]}

Input:
Sentence: These cases call attention to possible paranoid exacerbations with serotonin reuptake blockers in select patients and raise neurobiological considerations regarding paranoia .

## Item bc5cdr:test:476
Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Disease"}]}

Example input:
Sentence: We describe a 70-year-old Hispanic woman who developed fulminant hepatic failure necessitating liver transplantation 10 weeks after conversion from simvastatin 40 mg/day to simvastatin 10 mg-ezetimibe 40 mg/day .

Example answer:
{"entities": [{"text": "fulminant hepatic failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "simvastatin 10 mg-ezetimibe 40", "type": "Chemical"}]}

Example input:
Sentence: We report a woman with coronary artery disease who developed a markedly prolonged QT interval and torsades de pointes ( TdP ) after taking ketoconazole for treatment of fungal infection .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "prolonged QT interval", "type": "Disease"}, {"text": "torsades de pointes", "type": "Disease"}, {"text": "TdP", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "fungal infection", "type": "Disease"}]}

Example input:
Sentence: A history of angioedema secondary to lisinopril therapy was elicited .

Example answer:
{"entities": [{"text": "angioedema", "type": "Disease"}, {"text": "lisinopril", "type": "Chemical"}]}

Example input:
Sentence: The estimated incidence of angioedema during angiotensin-converting enzyme ( ACE ) inhibitor treatment is between 1 and 7 per thousand patients .

Example answer:
{"entities": [{"text": "angioedema", "type": "Disease"}, {"text": "angiotensin-converting enzyme ( ACE ) inhibitor", "type": "Chemical"}]}

Example input:
Sentence: A patient with cryptogenic cirrhosis and disseminated sporotrichosis developed acute renal failure immediately following the administration of amphotericin B on four separate occasions .

Example answer:
{"entities": [{"text": "cirrhosis", "type": "Disease"}, {"text": "sporotrichosis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}]}

Example input:
Sentence: METHODS : In a population-based study in 513 naturally postmenopausal women aged 54-67 years , we studied the association between self-reported intramuscularly administered high-dose estrogen-testosterone therapy ( estradiol- and testosterone esters ) and aortic atherosclerosis .

Example answer:
{"entities": [{"text": "estrogen-testosterone", "type": "Chemical"}, {"text": "estradiol- and testosterone esters", "type": "Chemical"}, {"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: The angioedema resolved after therapy with intravenous steroids and diphenhydramine hydrochloride .

Example answer:
{"entities": [{"text": "angioedema", "type": "Disease"}, {"text": "steroids", "type": "Chemical"}, {"text": "diphenhydramine", "type": "Chemical"}]}

Example input:
Sentence: We report a case of bile duct hamartoma which developed in a patient who had been on long-term danazol treatment .

Example answer:
{"entities": [{"text": "danazol", "type": "Chemical"}]}

Example input:
Sentence: Bile duct hamartoma occurring in association with long-term treatment with danazol .

Example answer:
{"entities": [{"text": "danazol", "type": "Chemical"}]}

Input:
Sentence: The long-term safety of danazol in women with hereditary angioedema .

## Item bc5cdr:test:478
Example input:
Sentence: The estimated incidence of angioedema during angiotensin-converting enzyme ( ACE ) inhibitor treatment is between 1 and 7 per thousand patients .

Example answer:
{"entities": [{"text": "angioedema", "type": "Disease"}, {"text": "angiotensin-converting enzyme ( ACE ) inhibitor", "type": "Chemical"}]}

Example input:
Sentence: A patient with cryptogenic cirrhosis and disseminated sporotrichosis developed acute renal failure immediately following the administration of amphotericin B on four separate occasions .

Example answer:
{"entities": [{"text": "cirrhosis", "type": "Disease"}, {"text": "sporotrichosis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}]}

Example input:
Sentence: We conducted a 12-month controlled trial of mazindol , a putative growth hormone secretion inhibitor , in 83 boys with Duchenne dystrophy .

Example answer:
{"entities": [{"text": "mazindol", "type": "Chemical"}, {"text": "Duchenne dystrophy", "type": "Disease"}]}

Example input:
Sentence: Propylthiouracil therapy was withdrawn , and she was treated with a 1-month course of prednisone , which alleviated her symptoms .

Example answer:
{"entities": [{"text": "Propylthiouracil", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}]}

Example input:
Sentence: A history of angioedema secondary to lisinopril therapy was elicited .

Example answer:
{"entities": [{"text": "angioedema", "type": "Disease"}, {"text": "lisinopril", "type": "Chemical"}]}

Example input:
Sentence: The angioedema resolved after therapy with intravenous steroids and diphenhydramine hydrochloride .

Example answer:
{"entities": [{"text": "angioedema", "type": "Disease"}, {"text": "steroids", "type": "Chemical"}, {"text": "diphenhydramine", "type": "Chemical"}]}

Example input:
Sentence: Two of 14 patients with Cushing 's syndrome treated on a long-term basis with ketoconazole developed sustained hypertension .

Example answer:
{"entities": [{"text": "Cushing 's syndrome", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: METHODS : In a population-based study in 513 naturally postmenopausal women aged 54-67 years , we studied the association between self-reported intramuscularly administered high-dose estrogen-testosterone therapy ( estradiol- and testosterone esters ) and aortic atherosclerosis .

Example answer:
{"entities": [{"text": "estrogen-testosterone", "type": "Chemical"}, {"text": "estradiol- and testosterone esters", "type": "Chemical"}, {"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: Bile duct hamartoma occurring in association with long-term treatment with danazol .

Example answer:
{"entities": [{"text": "danazol", "type": "Chemical"}]}

Example input:
Sentence: We report a case of bile duct hamartoma which developed in a patient who had been on long-term danazol treatment .

Example answer:
{"entities": [{"text": "danazol", "type": "Chemical"}]}

Input:
Sentence: We therefore investigated the long-term safety of danazol by performing a retrospective chart review of 60 female patients with hereditary angioedema treated with danazol for a continuous period of 6 months or longer .

## Item bc5cdr:test:115
Example input:
Sentence: There was no correlation between vitamin B12 or folate levels and development of myelosuppression .

Example answer:
{"entities": [{"text": "vitamin B12", "type": "Chemical"}, {"text": "folate", "type": "Chemical"}, {"text": "myelosuppression", "type": "Disease"}]}

Example input:
Sentence: Peripheral neuropathy due to nutritional deficiency of thiamine and riboflavin was common ( 10.1 % ) and presented mainly as sensory and sensori-motor neuropathy .

Example answer:
{"entities": [{"text": "Peripheral neuropathy", "type": "Disease"}, {"text": "nutritional deficiency", "type": "Disease"}, {"text": "thiamine", "type": "Chemical"}, {"text": "riboflavin", "type": "Chemical"}, {"text": "sensori-motor neuropathy", "type": "Disease"}]}

Example input:
Sentence: In a 37-year-old woman with documented pentazocine-induced fibrous myopathy of triceps and deltoid muscles bilaterally and a three-week history of right wrist drop , electrodiagnostic examination showed a severe but partial lesion of the right radial nerve distal to the branches to the triceps , in addition to the fibrous myopathy .

Example answer:
{"entities": [{"text": "pentazocine-induced", "type": "Chemical"}, {"text": "fibrous myopathy", "type": "Disease"}]}

Example input:
Sentence: In the remaining cases , a combination of myelopathy , visual disturbance , and peripheral neuropathy was the most common manifestation .

Example answer:
{"entities": [{"text": "myelopathy", "type": "Disease"}, {"text": "visual disturbance", "type": "Disease"}, {"text": "peripheral neuropathy", "type": "Disease"}]}

Example input:
Sentence: What is less well known is a phenomenon whereby statins may induce a myopathy , which persists or may progress after stopping the drug .

Example answer:
{"entities": [{"text": "statins", "type": "Chemical"}, {"text": "myopathy", "type": "Disease"}]}

Example input:
Sentence: These defects explain the abnormal erythrocyte shape and decreased mechanical stability promoted by TAM , resulting in hemolytic anemia .

Example answer:
{"entities": [{"text": "TAM", "type": "Chemical"}, {"text": "hemolytic anemia", "type": "Disease"}]}

Example input:
Sentence: Vitamin B12 and folinic acid supplementation of ZDV therapy does not seem useful in preventing or reducing ZDV-induced myelotoxicity in the overall treated population , although a beneficial effect in certain subgroups of patients can not be excluded .

Example answer:
{"entities": [{"text": "Vitamin B12", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}, {"text": "ZDV", "type": "Chemical"}, {"text": "ZDV-induced", "type": "Chemical"}, {"text": "myelotoxicity", "type": "Disease"}]}

Example input:
Sentence: We suggest that our patient 's tubular dysfunction and myopathy may have resulted from mitochondrial dysfunction which is triggered by tacrolimus and augmented by lamivudine .

Example answer:
{"entities": [{"text": "tubular dysfunction", "type": "Disease"}, {"text": "myopathy", "type": "Disease"}, {"text": "mitochondrial dysfunction", "type": "Disease"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: Fanconi syndrome , as well as myopathy , is well recognized in patients with mitochondrial disorders and caused by depletion of mtDNA .

Example answer:
{"entities": [{"text": "Fanconi syndrome", "type": "Disease"}, {"text": "myopathy", "type": "Disease"}, {"text": "mitochondrial disorders", "type": "Disease"}]}

Example input:
Sentence: The mechanism of this myopathy is uncertain but may involve the induction by statins of an endoplasmic reticulum stress response with associated up-regulation of MHC-I expression and antigen presentation by muscle fibres .

Example answer:
{"entities": [{"text": "myopathy", "type": "Disease"}, {"text": "statins", "type": "Chemical"}]}

Input:
Sentence: Myopathy due to lack of vitamin E and myopathy induced by certain viruses have much in common anatomically and pathologically with the human form .

## Item bc5cdr:test:737
Example input:
Sentence: Drug-associated acute-onset vanishing bile duct and Stevens-Johnson syndromes in a child .

Example answer:
{"entities": [{"text": "vanishing bile duct", "type": "Disease"}, {"text": "Stevens-Johnson syndromes", "type": "Disease"}]}

Example input:
Sentence: In control rats , immunostaining for 7H6 and ZO-1 colocalized to outline bile canaliculi in a continuous fashion .

Example answer:
{"entities": []}

Example input:
Sentence: Although hepatocyte TJs are impaired in cholestasis , attempts to localize the precise site of hepatocyte TJ damage by freeze-fracture electron microscopy have produced limited information .

Example answer:
{"entities": [{"text": "cholestasis", "type": "Disease"}]}

Example input:
Sentence: In contrast , 7H6 and ZO-1 immunostaining was more discontinuous , outlining the bile canaliculi after BDL .

Example answer:
{"entities": []}

Example input:
Sentence: Our results suggest that the suppression of gallbladder contractility is the cause of the successive formation of bile sludge , gallstones , and cholecystitis during octreotide therapy in Chinese acromegalic patients .

Example answer:
{"entities": [{"text": "gallstones", "type": "Disease"}, {"text": "cholecystitis", "type": "Disease"}, {"text": "octreotide", "type": "Chemical"}, {"text": "acromegalic", "type": "Disease"}]}

Example input:
Sentence: Hepatocyte tight junctions ( TJs ) , the only intercellular barrier between the sinusoidal and the canalicular spaces , play a key role in bile formation .

Example answer:
{"entities": []}

Example input:
Sentence: A previously healthy child who developed acute , severe , rapidly progressive vanishing bile duct syndrome shortly after Stevens-Johnson syndrome is described ; this was temporally associated with ibuprofen use .

Example answer:
{"entities": [{"text": "vanishing bile duct syndrome", "type": "Disease"}, {"text": "Stevens-Johnson syndrome", "type": "Disease"}, {"text": "ibuprofen", "type": "Chemical"}]}

Example input:
Sentence: We used rat models of intrahepatic cholestasis by ethinyl estradiol ( EE ) treatment and extrahepatic cholestasis by bile duct ligation ( BDL ) to precisely determine the site of TJ damage .

Example answer:
{"entities": [{"text": "intrahepatic cholestasis", "type": "Disease"}, {"text": "ethinyl estradiol", "type": "Chemical"}, {"text": "EE", "type": "Chemical"}, {"text": "extrahepatic cholestasis", "type": "Disease"}]}

Example input:
Sentence: This case documents acute drug-related vanishing bile duct syndrome in the pediatric age group and suggests shared immune mechanisms in the pathogenesis of both Stevens-Johnson syndrome and vanishing bile duct syndrome .

Example answer:
{"entities": [{"text": "vanishing bile duct syndrome", "type": "Disease"}, {"text": "Stevens-Johnson syndrome", "type": "Disease"}]}

Example input:
Sentence: Acute vanishing bile duct syndrome is a rare but established cause of progressive cholestasis in adults , is most often drug or toxin related , and is of unknown pathogenesis .

Example answer:
{"entities": [{"text": "vanishing bile duct", "type": "Disease"}, {"text": "cholestasis", "type": "Disease"}]}

Input:
Sentence: An autoimmune pathogenesis of the bile duct destruction is suggested .

## Item bc5cdr:test:740
Example input:
Sentence: In the double blind study with haloperidol , both substances were found to be highly effective in the treatment of psychotic syndromes belonging predominantly to the schizophrenia group .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "psychotic syndromes belonging predominantly to the schizophrenia group", "type": "Disease"}]}

Example input:
Sentence: As a result , there is a growing interest in the development of pharmacological agents with potential antipsychotic properties that enhance the activity of the glutamatergic system via a modulation of the NMDA receptor .

Example answer:
{"entities": [{"text": "NMDA", "type": "Chemical"}]}

Example input:
Sentence: They offer protection against seizures in a range of models and seem to inhibit certain stages of drug dependence in preclinical assessments .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "drug dependence", "type": "Disease"}]}

Example input:
Sentence: Given its excellent tolerance profile and low toxicity , further evaluation of VNB in combination therapy is warranted .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "VNB", "type": "Chemical"}]}

Example input:
Sentence: The last decade has seen the emergence of tacrolimus as a potent immunosuppressive agent with mechanisms of action virtually identical to those of cyclosporine .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "cyclosporine", "type": "Chemical"}]}

Example input:
Sentence: Importantly , both classical ( haloperidol ) and atypical ( olanzapine , clozapine and aripiprazole ) antipsychotics were effective in all these models of hyperactivity .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "olanzapine", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "aripiprazole", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}]}

Example input:
Sentence: Capecitabine has a well-established safety profile and can be given safely to patients with advanced age , hepatic and renal dysfunctions .

Example answer:
{"entities": [{"text": "Capecitabine", "type": "Chemical"}]}

Example input:
Sentence: Recent reports indicate that single agent therapy with vinorelbine ( VNB ) or gemcitabine ( GEM ) may obtain a response rate of 20-30 % in elderly patients , with acceptable toxicity and improvement in symptoms and quality of life .

Example answer:
{"entities": [{"text": "vinorelbine", "type": "Chemical"}, {"text": "VNB", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "GEM", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Both active treatments were well tolerated .

Example answer:
{"entities": []}

Example input:
Sentence: Clinical tolerability of both agents has been good , with fewer than 3 % of patients withdrawn from treatment because of clinical adverse experiences .

Example answer:
{"entities": []}

Input:
Sentence: The favorable efficacy and tolerability profiles of these agents make them attractive therapeutic modalities .

## Item bc5cdr:test:171
Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: In conclusion mitochondrial toxicity is an early common event both in paclitaxel and cisplatin induced neurotoxicity .

Example answer:
{"entities": [{"text": "mitochondrial toxicity", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Central nervous system ( CNS ) complications during treatment of childhood acute lymphoblastic leukemia ( ALL ) remain a challenging clinical problem .

Example answer:
{"entities": [{"text": "Central nervous system ( CNS ) complications", "type": "Disease"}, {"text": "acute lymphoblastic leukemia", "type": "Disease"}, {"text": "ALL", "type": "Disease"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "Disease"}, {"text": "METH", "type": "Chemical"}, {"text": "MPTP", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "METH-induced", "type": "Chemical"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Remission induction of meningeal leukemia with high-dose intravenous methotrexate .

Example answer:
{"entities": [{"text": "meningeal leukemia", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: High-dose intravenous methotrexate is an effective treatment for the induction of remission after meningeal relapse in acute lymphoblastic leukemia .

Example answer:
{"entities": [{"text": "methotrexate", "type": "Chemical"}, {"text": "acute lymphoblastic leukemia", "type": "Disease"}]}

Example input:
Sentence: CNS complications included posterior reversible leukoencephalopathy syndrome ( n = 10 ) , stroke ( n = 5 ) , temporal lobe epilepsy ( n = 2 ) , high-dose methotrexate toxicity ( n = 2 ) , syndrome of inappropriate antidiuretic hormone secretion ( n = 1 ) , and other unclassified events ( n = 7 ) .

Example answer:
{"entities": [{"text": "leukoencephalopathy", "type": "Disease"}, {"text": "stroke", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "inappropriate antidiuretic hormone secretion", "type": "Disease"}]}

Example input:
Sentence: Twenty children with acute lymphoblastic leukemia who developed meningeal disease were treated with a high-dose intravenous methotrexate regimen that was designed to achieve and maintain CSF methotrexate concentrations of 10 ( -5 ) mol/L without the need for concomitant intrathecal dosing .

Example answer:
{"entities": [{"text": "acute lymphoblastic leukemia", "type": "Disease"}, {"text": "meningeal disease", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}]}

Input:
Sentence: The incidence of neurotoxicity may be reduced by employing lower doses of methotrexate in the presence of central nervous system leukemia , in older children and adults , and in the presence of epidural leakage .

## Item bc5cdr:test:301
Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Disease"}]}

Example input:
Sentence: Two patients developed acute tubular necrosis , characterized clinically by acute oliguric renal failure , while they were receiving a combination of cephalothin sodium and gentamicin sulfate therapy .

Example answer:
{"entities": [{"text": "acute tubular necrosis", "type": "Disease"}, {"text": "cephalothin sodium", "type": "Chemical"}, {"text": "gentamicin sulfate", "type": "Chemical"}]}

Example input:
Sentence: Massive proteinuria and acute renal failure after oral bisphosphonate ( alendronate ) administration in a patient with focal segmental glomerulosclerosis .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "bisphosphonate", "type": "Chemical"}, {"text": "alendronate", "type": "Chemical"}, {"text": "focal segmental glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: Reactive oxygen species have been implicated in the pathogenesis of acute puromycin aminonucleoside ( PAN ) -induced nephropathy , with antioxidants significantly reducing the proteinuria .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: Severe rhabdomyolysis and acute renal failure secondary to concomitant use of simvastatin , amiodarone , and atazanavir .

Example answer:
{"entities": [{"text": "rhabdomyolysis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: Two patients with similar clinical features are presented : both patients had chronic renal failure , on hemodialysis for many years but recently begun on a high-flux dialyzer ; both had been receiving a carbidopa/levodopa preparation ; and both had the onset of hallucinosis and recurrent seizures , which were refractory to anticonvulsants .

Example answer:
{"entities": [{"text": "chronic renal failure", "type": "Disease"}, {"text": "carbidopa/levodopa", "type": "Chemical"}, {"text": "hallucinosis", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: This case study reveals an unusual finding of rapidly proliferative crescentic glomerulonephritis in a patient treated with rifampin who had no other identifiable causes for developing this disease .

Example answer:
{"entities": [{"text": "glomerulonephritis", "type": "Disease"}, {"text": "rifampin", "type": "Chemical"}]}

Example input:
Sentence: A patient with cryptogenic cirrhosis and disseminated sporotrichosis developed acute renal failure immediately following the administration of amphotericin B on four separate occasions .

Example answer:
{"entities": [{"text": "cirrhosis", "type": "Disease"}, {"text": "sporotrichosis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}]}

Example input:
Sentence: A Cambodian woman with hemoglobin E trait ( AE ) and leprosy developed a Heinz body hemolytic anemia while taking a dose of dapsone ( 50 mg/day ) not usually associated with clinical hemolysis .

Example answer:
{"entities": [{"text": "leprosy", "type": "Disease"}, {"text": "hemolytic anemia", "type": "Disease"}, {"text": "dapsone", "type": "Chemical"}, {"text": "hemolysis", "type": "Disease"}]}

Example input:
Sentence: This patient underwent a 10-month regimen of rifampin and isoniazid for pulmonary tuberculosis and was discovered to have developed signs of severe renal failure five weeks after completion of therapy .

Example answer:
{"entities": [{"text": "rifampin", "type": "Chemical"}, {"text": "isoniazid", "type": "Chemical"}, {"text": "pulmonary tuberculosis", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Input:
Sentence: Two patients with leprosy who developed hemolysis and acute renal failure following rifampin are reported .

## Item bc5cdr:test:244
Example input:
Sentence: A 17-day-old infant on isoniazid therapy 13 mg/kg daily from birth because of maternal tuberculosis was admitted after 4 days of clonic fits .

Example answer:
{"entities": [{"text": "isoniazid", "type": "Chemical"}, {"text": "tuberculosis", "type": "Disease"}, {"text": "clonic fits", "type": "Disease"}]}

Example input:
Sentence: Apamin ( 10 ng ) had a tendency to decrease the convulsive threshold ( 21.6 +/- 2.2 to 19.9 +/- 2.5 mg. l ( -1 ) ) but this was not statistically significant .

Example answer:
{"entities": [{"text": "Apamin", "type": "Chemical"}, {"text": "convulsive", "type": "Disease"}]}

Example input:
Sentence: Two mouse lines selected for differential sensitivities to beta-carboline-induced seizures are also differentially sensitive to various pharmacological effects of other GABA ( A ) receptor ligands .

Example answer:
{"entities": [{"text": "beta-carboline-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: Neonatal pyridoxine responsive convulsions due to isoniazid therapy .

Example answer:
{"entities": [{"text": "pyridoxine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "isoniazid", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Sensitivity to several convulsion endpoints induced by nicotine , carbachol , and neostigmine were significantly greater in WSR versus WSP mice .

Example answer:
{"entities": [{"text": "convulsion", "type": "Disease"}, {"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}]}

Example input:
Sentence: Oral administration of CBZ as an aqueous suspension every 8 h at a dose of 250 mg/kg was continuously protective against HFDE-induced seizures and was minimally toxic as measured by weight gain over 8 weeks of treatment .

Example answer:
{"entities": [{"text": "CBZ", "type": "Chemical"}, {"text": "HFDE-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}]}

Example input:
Sentence: In vitro , gamma-HCH , pentylenetetrazol and picrotoxin were shown to inhibit 3H-TBOB binding in mouse whole brain , with IC50 values of 4.6 , 404 and 9.4 microM , respectively .

Example answer:
{"entities": [{"text": "gamma-HCH", "type": "Chemical"}, {"text": "pentylenetetrazol", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "3H-TBOB", "type": "Chemical"}]}

Example input:
Sentence: The rats received AChE reactivator pralidoxime-2-chloride ( 2PAM ) ( 30.0 mg/kg BW ) , anticonvulsant diazepam ( 2.0 mg/kg BW ) , A ( 1 ) -adenosine receptor agonist N ( 6 ) -cyclopentyl adenosine ( CPA ) ( 2.0 mg/kg BW ) , NMDA-receptor antagonist dizocilpine maleate ( +-MK801 hydrogen maleate ) ( 2.0 mg/kg BW ) or their combinations with cholinolytic drug atropine sulfate ( 50.0 mg/kg BW ) immediately or 30 min after the single SC injection of DFP .

Example answer:
{"entities": [{"text": "pralidoxime-2-chloride", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "N ( 6 ) -cyclopentyl adenosine", "type": "Chemical"}, {"text": "CPA", "type": "Chemical"}, {"text": "NMDA-receptor", "type": "Chemical"}, {"text": "dizocilpine maleate", "type": "Chemical"}, {"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: In the absence of caffeine , acetaminophen ( up to 300 mg/kg ) did not modify the seizures induced by maximal electroshock and did not alter the convulsant dose of pentylenetetrezol in mice ( tests performed by the Anticonvulsant Screening Project of NINCDS ) .

Example answer:
{"entities": [{"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "pentylenetetrezol", "type": "Chemical"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Input:
Sentence: Moreover , 0.05 mg/kg of this beta-carboline reduced markedly the increase of [ 35S ] TBPS binding and the convulsions induced by isoniazid ( 200 mg/kg s.c. ) .

## Item bc5cdr:test:63
Example input:
Sentence: Intracranial aneurysms or arteriovenous malformations were present in 17 of 32 patients studied angiographically or at autopsy ; cerebral vasculitis was present in two patients .

Example answer:
{"entities": [{"text": "Intracranial aneurysms", "type": "Disease"}, {"text": "arteriovenous malformations", "type": "Disease"}, {"text": "cerebral vasculitis", "type": "Disease"}]}

Example input:
Sentence: This case report shows that ciprofloxacin may precipitate life-threatening thrombocytopenia and haemolytic anaemia , even in the early phases of treatment and without apparent previous exposures .

Example answer:
{"entities": [{"text": "ciprofloxacin", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "haemolytic anaemia", "type": "Disease"}]}

Example input:
Sentence: Rare serious complications may occur in some patients , including haemorrhagic pancreatitis , bone marrow suppression , VPA-induced hepatotoxicity and VPA-induced encephalopathy .

Example answer:
{"entities": [{"text": "pancreatitis", "type": "Disease"}, {"text": "bone marrow suppression", "type": "Disease"}, {"text": "VPA-induced", "type": "Chemical"}, {"text": "hepatotoxicity", "type": "Disease"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: A search of the literature on the thromboembolic complications of CC does not include this severe ophthalmic complication , although mild visual disturbance after CC intake is not uncommon .

Example answer:
{"entities": [{"text": "thromboembolic", "type": "Disease"}, {"text": "CC", "type": "Chemical"}, {"text": "visual disturbance", "type": "Disease"}]}

Example input:
Sentence: The epidemiological studies that assessed the risk of venous thromboembolism ( VTE ) associated with newer oral contraceptives ( OC ) did not distinguish between patterns of OC use , namely first-time users , repeaters and switchers .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "VTE", "type": "Disease"}, {"text": "oral contraceptives", "type": "Chemical"}, {"text": "OC", "type": "Chemical"}]}

Example input:
Sentence: The amount of fibrin in the kidneys was also considerably lower than in animals which received thrombin and AMCA alone .

Example answer:
{"entities": [{"text": "AMCA", "type": "Chemical"}]}

Example input:
Sentence: Two subsets of patients were identified from this latter group : the first included four patients ( 5 % of the total population ) who developed major toxicity resulting in Fanconi 's syndrome ( TDFS ) ; and the second group included five patients with elevated beta 2 microglobulinuria and low phosphate reabsorption .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "Fanconi 's syndrome", "type": "Disease"}, {"text": "TDFS", "type": "Disease"}, {"text": "phosphate", "type": "Chemical"}]}

Example input:
Sentence: Histologic examination of the renal tissue showed evidence of intravascular coagulation , primarily affecting the small arteries , arterioles , and glomeruli .

Example answer:
{"entities": [{"text": "intravascular coagulation", "type": "Disease"}]}

Example input:
Sentence: Five patients with carcinoma developed thrombotic microangiopathy ( characterized by renal insufficiency , microangiopathic hemolytic anemia , and usually thrombocytopenia ) after treatment with cisplatin , bleomycin , and a vinca alkaloid .

Example answer:
{"entities": [{"text": "carcinoma", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "microangiopathic hemolytic anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "bleomycin", "type": "Chemical"}, {"text": "vinca alkaloid", "type": "Chemical"}]}

Example input:
Sentence: Induction of intravascular coagulation and inhibition of fibrinolysis by injection of thrombin and tranexamic acid ( AMCA ) in the rat gives rise to pulmonary and renal insufficiency resembling that occurring after trauma or sepsis in man .

Example answer:
{"entities": [{"text": "intravascular coagulation", "type": "Disease"}, {"text": "tranexamic acid", "type": "Chemical"}, {"text": "AMCA", "type": "Chemical"}, {"text": "trauma", "type": "Disease"}, {"text": "sepsis", "type": "Disease"}]}

Input:
Sentence: Since intravascular fibrin thrombi are often observed in patients with fibrinolytic disorders , EACA should not be implicated in the pathogenesis of fibrin thrombi in patients with disseminated intravascular coagulation or other `` consumption coagulopathies . ''

## Item bc5cdr:test:192
Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: Seven patients developed glucose tolerance curves characteristic of diabetes but these were mild , did not require treatment and returned to normal on ceasing didanosine .

Example answer:
{"entities": [{"text": "glucose tolerance curves", "type": "Disease"}, {"text": "diabetes", "type": "Disease"}, {"text": "didanosine", "type": "Chemical"}]}

Example input:
Sentence: This pilot study leads to the conclusion that glutamate supplementation at the chosen regimen fails to protect against peripheral neurotoxicity of PAC .

Example answer:
{"entities": [{"text": "glutamate", "type": "Chemical"}, {"text": "peripheral neurotoxicity", "type": "Disease"}, {"text": "PAC", "type": "Chemical"}]}

Example input:
Sentence: Proteinuria increased significantly from a median of 0.13 g/day ( range 0-5.7 ) preswitch to 0.23 g/day ( 0-9.88 ) at 24 months postswitch ( p = 0.0024 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 99mTc-glucarate was easy to prepare , stable for 96 h and was used to study its biodistribution in rats with isoproterenol-induced acute myocardial infarction .

Example answer:
{"entities": [{"text": "99mTc-glucarate", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: Mitochondrial radiocalcium uptakes were significantly decreased in animals pretreated with acetylsalicylic acid or dipyridamole or when hydrocortisone was added to the epinephrine infusion ( 2,682,2,803 , and 3,424 counts per minute per gram of dried fraction , respectively ) .

Example answer:
{"entities": [{"text": "radiocalcium", "type": "Chemical"}, {"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine", "type": "Chemical"}]}

Example input:
Sentence: The results indicated that concomitant treatment with gum Arabic and GM significantly increased creatinine and urea by about 183 and 239 % , respectively ( compared to 432 and 346 % , respectively , in rats treated with cellulose and GM ) , and decreased that of cortical GSH by 21 % ( compared to 27 % in the cellulose plus GM group ) The GM-induced proximal tubular necrosis appeared to be slightly less severe in rats given GM together with gum Arabic than in those given GM and cellulose .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}, {"text": "urea", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "GM-induced", "type": "Chemical"}, {"text": "tubular necrosis", "type": "Disease"}]}

Example input:
Sentence: HS diet for 4 wk caused a progressive increase in BP , protein and albumin excretion , and glomerular sclerosis in male DS rats , which were attenuated by castration .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Input:
Sentence: The chronic feeding of small amounts ( 0.3-3 % of diet weight ) of certain amino derivatives of caproate resulted in hyperglycemia , an elevated glucose tolerance curve and , occasionally , glucosuria .

## Item bc5cdr:test:394
Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Example input:
Sentence: Pneumonitis , bilateral pleural effusions , echocardiographic evidence of cardiac tamponade , and positive autoantibodies developed in a 43-year-old man , who was receiving long-term sulfasalazine therapy for chronic ulcerative colitis .

Example answer:
{"entities": [{"text": "Pneumonitis", "type": "Disease"}, {"text": "pleural effusions", "type": "Disease"}, {"text": "cardiac tamponade", "type": "Disease"}, {"text": "sulfasalazine", "type": "Chemical"}, {"text": "ulcerative colitis", "type": "Disease"}]}

Example input:
Sentence: Associated factors were co-treatment with other centrally antimuscarinic agents , poor clinical outcome , older age , and longer hospitalization ( by 17.5 days , increasing cost ) ; sex , diagnosis or medical co-morbidity , and daily clozapine dose , which fell with age , were unrelated .

Example answer:
{"entities": [{"text": "clozapine", "type": "Chemical"}]}

Example input:
Sentence: We report a patient in whom hypersensitivity to carbamazepine presented with generalized erythroderma , a severe leukemoid reaction , eosinophilia , hyponatremia , and renal failure .

Example answer:
{"entities": [{"text": "hypersensitivity", "type": "Disease"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "erythroderma", "type": "Disease"}, {"text": "leukemoid reaction", "type": "Disease"}, {"text": "eosinophilia", "type": "Disease"}, {"text": "hyponatremia", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: A case of veno-occlusive disease of the liver with fatal outcome after dacarbazine ( DTIC ) therapy for melanoma is reported .

Example answer:
{"entities": [{"text": "veno-occlusive disease of the liver", "type": "Disease"}, {"text": "dacarbazine", "type": "Chemical"}, {"text": "DTIC", "type": "Chemical"}, {"text": "melanoma", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Reversible inferior colliculus lesions could be considered as the characteristic for metronidazole-induced encephalopathy , next to the dentate nucleus involvement .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "Disease"}, {"text": "metronidazole-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: This was most frequently found in children , many of whom had received clioquinol as treatment for acrodermatitis enteropathica .

Example answer:
{"entities": [{"text": "clioquinol", "type": "Chemical"}, {"text": "acrodermatitis enteropathica", "type": "Disease"}]}

Example input:
Sentence: Three infants , born of two mothers with inflammatory bowel disease who received treatment with sulphasalazine throughout pregnancy , were found to have major congenital anomalies .

Example answer:
{"entities": [{"text": "inflammatory bowel disease", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "congenital anomalies", "type": "Disease"}]}

Example input:
Sentence: MATERIALS AND METHODS : From November 2005 to September 2007 , 8 patients ( 5 men and 3 women ) were diagnosed as having metronidazole-induced encephalopathy ( age range ; 43-78 years ) .

Example answer:
{"entities": [{"text": "metronidazole-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: A 34-year-old lady developed a constellation of dermatitis , fever , lymphadenopathy and hepatitis , beginning on the 17th day of a course of oral sulphasalazine for sero-negative rheumatoid arthritis .

Example answer:
{"entities": [{"text": "dermatitis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "lymphadenopathy", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Input:
Sentence: Five cases of encephalitis during treatment of loiasis with diethylcarbamazine .

## Item bc5cdr:test:207
Example input:
Sentence: Changes evoked by a single intraperitoneal injection of rilmenidine ( 600 microg/kg ) or alpha-methyldopa ( 100 mg/kg ) , selective I1- and alpha2-receptor agonists , respectively , in blood pressure , hemodynamic variability , and locomotor activity were assessed in radiotelemetered sham-operated and ovariectomized ( Ovx ) Sprague-Dawley female rats with or without 12-wk estrogen replacement .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "estrogen", "type": "Chemical"}]}

Example input:
Sentence: In control rats , intravenous bromocriptine ( 150 microg/kg ) induced significant hypotension and tachycardia .

Example answer:
{"entities": [{"text": "bromocriptine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: The convulsant activity of bupivacaine was not significantly modified but calcium channel blockers decreased the time of latency to obtain bupivacaine-induced convulsions ; this effect was less pronounced with bepridil .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "bupivacaine-induced", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "bepridil", "type": "Chemical"}]}

Example input:
Sentence: In Group 1 the rats were trained under the influence of pentobarbital to run to the same shelf as in the normal state .

Example answer:
{"entities": [{"text": "pentobarbital", "type": "Chemical"}]}

Example input:
Sentence: By implantation of electrodes and electrophysiological recording in vivo , the results showed that Rg1 restored the long-term potentiation ( LTP ) impaired by morphine in both freely moving and anaesthetised rats .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: In isolated perfused heart preparations from isoproterenol-pretreated rats , the isoproterenol-induced maximal increase in left ventricular systolic pressure was significantly reduced , compared with saline-pretreated rats ( the EC50 of the isoproterenol-induced increase in left ventricular systolic pressure was enhanced approximately 22-fold ) .

Example answer:
{"entities": [{"text": "isoproterenol-pretreated", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Chronic hyperprolactinemia induced by the dopamine antagonist sulpiride caused a 40 % reduction LH pulse frequency in ovariectomized rats , but only in the presence of chronic low levels of estradiol .

Example answer:
{"entities": [{"text": "hyperprolactinemia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "sulpiride", "type": "Chemical"}, {"text": "estradiol", "type": "Chemical"}]}

Example input:
Sentence: Effects of long-term pretreatment with isoproterenol on bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Input:
Sentence: Progesterone potentiation of bupivacaine arrhythmogenicity in pentobarbital-anesthetized rats and beating rat heart cell cultures .

## Item bc5cdr:test:651
Example input:
Sentence: The magnitude and time course of the increase in heart rate and the decrease in systolic blood pressure after nitroglycerin were similar in the normal and diabetic subjects without autonomic neuropathy , whereas a lesser increase in heart rate and a greater decrease in systolic blood pressure occurred in the diabetic subjects with autonomic neuropathy .

Example answer:
{"entities": [{"text": "nitroglycerin", "type": "Chemical"}, {"text": "diabetic", "type": "Disease"}, {"text": "autonomic neuropathy", "type": "Disease"}]}

Example input:
Sentence: In each group , SNP infusion resulted in an initial decrease in blood pressure from 86 torr and 83 torr , respectively , to 48 torr .

Example answer:
{"entities": [{"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: Nimodipine treatment resulted in a statistically significant reduction in systolic BP ( SBP ) and diastolic BP ( DBP ) from baseline compared with placebo during the first few days .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "Chemical"}, {"text": "reduction in systolic BP", "type": "Disease"}]}

Example input:
Sentence: Hypertension was observed in animals that had a reduction in glomeruli as well as in a group that did not have a reduction in glomerular number , suggesting that a reduction in glomerular number is not the sole cause for the development of hypertension .

Example answer:
{"entities": [{"text": "Hypertension", "type": "Disease"}, {"text": "reduction in glomerular number", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: Following discontinuation of SNP , blood pressure in the control animals rebounded to 94 torr , as compared with 78 torr in the saralasin-treated rats .

Example answer:
{"entities": [{"text": "SNP", "type": "Chemical"}, {"text": "saralasin-treated", "type": "Chemical"}]}

Example input:
Sentence: The rise in blood pressure became less marked when higher concentrations of sevoflurane or enflurane were administered and the blood pressure at convulsions decreased significantly in 1.6 % sevoflurane , and in 0.8 % and 1.6 % enflurane .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "Chemical"}, {"text": "enflurane", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}]}

Example input:
Sentence: This drug caused biventricular dysfunction , due to its negative inotropic effect , and hypotension , due to its peripheral vasodilatory effect .

Example answer:
{"entities": [{"text": "biventricular dysfunction", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: The patient had no apparent associated conditions which might have predisposed him to the development of bradyarrhythmias ; and , thus , this probably represented a true idiosyncrasy to lidocaine .

Example answer:
{"entities": [{"text": "bradyarrhythmias", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: Isoproterenol pretreatment for 15 days caused cardiac hypertrophy without affecting baseline blood pressure and heart rate .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "Chemical"}, {"text": "cardiac hypertrophy", "type": "Disease"}]}

Example input:
Sentence: Serious adverse effects are uncommon and mainly have been related to the depression of cardiac contractility and conduction , especially when the drug is combined with beta-blocking agents .

Example answer:
{"entities": [{"text": "depression", "type": "Disease"}]}

Input:
Sentence: A correlation of the blood pressure was neither found in the development nor in the attempt to suppress the development of heart hypertrophy with the two beta-receptor blockers .

## Item bc5cdr:test:558
Example input:
Sentence: Electron microscopical immunohistochemistry revealed positive reaction products noted on the secretory granules , Golgi cisternae , and endoplasmic reticulum of the untreated rat prolactinoma cells .

Example answer:
{"entities": [{"text": "prolactinoma", "type": "Disease"}]}

Example input:
Sentence: We compared the effects of 17beta-estradiol in adult male and ovariectomized female rats subjected to lithium-pilocarpine-induced SE .

Example answer:
{"entities": [{"text": "17beta-estradiol", "type": "Chemical"}, {"text": "lithium-pilocarpine-induced", "type": "Chemical"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: 17beta-Estradiol did not alter the onset of first clonus in ovariectomized rats but accelerated it in males .

Example answer:
{"entities": [{"text": "17beta-Estradiol", "type": "Chemical"}]}

Example input:
Sentence: The relative amounts of alphaENaC , betaENaC and gammaENaC mRNAs were determined in kidneys from these rats by real-time quantitative TaqMan PCR , and the amounts of proteins by Western blot .

Example answer:
{"entities": []}

Example input:
Sentence: Pituitary tumors were induced in F344 female rats by chronic treatment with diethylstilbestrol ( DES , 8-10 mg ) implanted subcutaneously in silastic capsules .

Example answer:
{"entities": [{"text": "Pituitary tumors", "type": "Disease"}, {"text": "diethylstilbestrol", "type": "Chemical"}, {"text": "DES", "type": "Chemical"}]}

Example input:
Sentence: Interestingly , estradiol also induced PRL-R , SOCS-3 , and CIS mRNA levels independently .

Example answer:
{"entities": [{"text": "estradiol", "type": "Chemical"}]}

Example input:
Sentence: 17beta-Estradiol reduced the argyrophilic neurons in the CA1 and CA3-C sectors of ovariectomized rats .

Example answer:
{"entities": [{"text": "17beta-Estradiol", "type": "Chemical"}]}

Example input:
Sentence: Estrogens protect ovariectomized rats from hippocampal injury induced by kainic acid-induced status epilepticus ( SE ) .

Example answer:
{"entities": [{"text": "hippocampal injury", "type": "Disease"}, {"text": "kainic", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Tamoxifen ( TAM ) , the antiestrogenic drug most widely prescribed in the chemotherapy of breast cancer , induces changes in normal discoid shape of erythrocytes and hemolytic anemia .

Example answer:
{"entities": [{"text": "Tamoxifen", "type": "Chemical"}, {"text": "TAM", "type": "Chemical"}, {"text": "breast cancer", "type": "Disease"}, {"text": "hemolytic anemia", "type": "Disease"}]}

Example input:
Sentence: Characterization of estrogen-induced adenohypophyseal tumors in the Fischer 344 rat .

Example answer:
{"entities": [{"text": "estrogen-induced", "type": "Chemical"}, {"text": "adenohypophyseal tumors", "type": "Disease"}]}

Input:
Sentence: This is the first published report documenting the preferential in vivo binding of estrogen to nuclei of cells in estrogen induced hamster renal carcinomas .

## Item bc5cdr:test:616
Example input:
Sentence: These results suggest that antithrombosis of TET and FAN in mice may be mainly related to the antiplatelet aggregation activities .

Example answer:
{"entities": []}

Example input:
Sentence: BMCs obtained from green fluorescent protein ( GFP ) transgenic mice or rats were transplanted intravenously after induction of status epilepticus ( SE ) .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "Chemical"}]}

Example input:
Sentence: When hippocampal ACh was measured during testing for handling-induced convulsions , extracellular ACh was significantly elevated ( 192 % ) in WSP mice , but was nonsignificantly elevated ( 59 % ) in WSR mice .

Example answer:
{"entities": [{"text": "ACh", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}]}

Example input:
Sentence: In this study , the severity of response to other seizure-inducing agents was tested in mice 1 and 24 h after intraperitoneal administration of 80 mg/kg gamma-HCH .

Example answer:
{"entities": [{"text": "seizure-inducing", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}]}

Example input:
Sentence: However , the increase in release of ACh produced by the first application of KCl was 2-fold higher in WSP versus WSR mice .

Example answer:
{"entities": [{"text": "ACh", "type": "Chemical"}, {"text": "KCl", "type": "Chemical"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Intracerebroventricular injection of U-II also caused an increase in : food intake at doses of 100 and 1,000 ng/mouse , water intake at doses of 100-10,000 ng/mouse , and horizontal locomotion activity at a dose of 10,000 ng/mouse .

Example answer:
{"entities": [{"text": "U-II", "type": "Chemical"}]}

Example input:
Sentence: To determine mitochondrial events from HAART in vivo , 8-week-old hemizygous transgenic AIDS mice ( NL4-3Delta gag/pol ; TG ) and wild-type FVB/n littermates were treated with the HAART combination of zidovudine , lamivudine , and indinavir or vehicle control for 10 days or 35 days .

Example answer:
{"entities": [{"text": "AIDS", "type": "Disease"}, {"text": "zidovudine", "type": "Chemical"}, {"text": "lamivudine", "type": "Chemical"}, {"text": "indinavir", "type": "Chemical"}]}

Example input:
Sentence: At termination of the experiments , mice underwent echocardiography , quantitation of abundance of molecular markers of CM ( ventricular mRNA encoding atrial natriuretic factor [ ANF ] and sarcoplasmic calcium ATPase [ SERCA2 ] ) , and determination of plasma LA .

Example answer:
{"entities": [{"text": "CM", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "LA", "type": "Chemical"}]}

Input:
Sentence: We studied mortality after pertussis immunization in the mouse .

## Item bc5cdr:test:450
Example input:
Sentence: Nitroprusside infusion was associated with a significant ( p less than 0.05 ) increase in heart rate and cardiac output ; rebound hypertension was observed in three patients after discontinuation of nitroprusside .

Example answer:
{"entities": [{"text": "increase in heart rate and cardiac output", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "nitroprusside", "type": "Chemical"}]}

Example input:
Sentence: Nitroprusside caused significant decreases in arterial blood pressure and systemic vascular resistance and increases in heart rate , but did not change cardiac output or QS/QT .

Example answer:
{"entities": [{"text": "Nitroprusside", "type": "Chemical"}, {"text": "decreases in arterial blood pressure", "type": "Disease"}]}

Example input:
Sentence: Mean arterial pressure was decreased to 50 mm Hg for 30 minutes either by hemorrhage ( HEM , n = 7 ) or by continuous infusion of sodium nitroprusside ( SNP , n = 7 ) .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "Disease"}, {"text": "HEM", "type": "Disease"}, {"text": "sodium nitroprusside", "type": "Chemical"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: Nitroglycerin has been shown to reduce ST-segment elevation during acute myocardial infarction , an effect potentiated in the dog by agents that reverse nitroglycerin-induced hypotension .

Example answer:
{"entities": [{"text": "Nitroglycerin", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}, {"text": "nitroglycerin-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: During nitroprusside infusion low levels of CPAP do not markedly alter cardiovascular dynamics , but high levels of CPAP ( 10 cm H2O ) , while decreasing QS/QT , produce marked decreases in arterial blood pressure and cardiac output .

Example answer:
{"entities": [{"text": "nitroprusside", "type": "Chemical"}, {"text": "H2O", "type": "Chemical"}]}

Example input:
Sentence: Mean arterial pressure ( as a percentage of control +/- SEM ) during randomized infusions of 0.03 , 0.1 , 0.3 , or 1.0 microgram/kg/min was 99 +/- 1 , 95 +/- 1 ( p less than 0.05 ) , 93 +/- 1 ( p less than 0.01 ) , or 79 +/- 6 % ( p less than 0.001 ) , respectively , but no tachycardia and no augmentation of the norepinephrine release rate ( up to 0.3 microgram/kg/min ) were observed , which is in contrast to comparable hypotension induced by hydralazine or nitroglycerin .

Example answer:
{"entities": [{"text": "tachycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "hydralazine", "type": "Chemical"}, {"text": "nitroglycerin", "type": "Chemical"}]}

Example input:
Sentence: Ten cm H2O CPAP before nitroprusside infusion produced a further decrease in arterial blood pressure and significantly increased heart rate and decreased cardiac output and QS/QT .

Example answer:
{"entities": [{"text": "H2O", "type": "Chemical"}, {"text": "nitroprusside", "type": "Chemical"}, {"text": "decrease in arterial blood pressure", "type": "Disease"}, {"text": "decreased cardiac output", "type": "Disease"}]}

Example input:
Sentence: These data indicate that nitroprusside infusion rates that decrease mean arterial blood pressure by 40-50 per cent do not change cardiac output or QS/QT .

Example answer:
{"entities": [{"text": "nitroprusside", "type": "Chemical"}]}

Example input:
Sentence: Before nitroprusside infusion , 5 cm H2O CPAP significantly , P less than .05 , decreased arterial blood pressure , but did not significantly alter heart rate , cardiac output , systemic vascular resistance , or QS/QT .

Example answer:
{"entities": [{"text": "nitroprusside", "type": "Chemical"}, {"text": "H2O", "type": "Chemical"}]}

Example input:
Sentence: Ten patients with acute transmural myocardial infarctions received intravenous nitroglycerin , sufficient to reduce mean arterial pressure from 107 +/- 6 to 85 +/- 6 mm Hg ( P less than 0.001 ) , for 60 minutes .

Example answer:
{"entities": [{"text": "myocardial infarctions", "type": "Disease"}, {"text": "nitroglycerin", "type": "Chemical"}]}

Input:
Sentence: When circumflex artery blood flow was maintained constant , the increases in CxAD induced by cromakalim ( 10 micrograms/kg ) , pinacidil ( 30 micrograms/kg ) and nitroglycerin ( 10 micrograms/kg ) were reduced by 68 +/- 7 , 54 +/- 9 and 1 +/- 1 % , respectively .

## Item bc5cdr:test:451
Example input:
Sentence: Concurrent treatment of both dietary groups with Warfarin produced massive focal calcification of the artery media in the ad libitum-fed rats but no detectable artery calcification in the restricted-diet , growth-inhibited group .

Example answer:
{"entities": [{"text": "Warfarin", "type": "Chemical"}, {"text": "calcification of the artery", "type": "Disease"}, {"text": "artery calcification", "type": "Disease"}]}

Example input:
Sentence: Reversal by phenylephrine of the beneficial effects of intravenous nitroglycerin in patients with acute myocardial infarction .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "nitroglycerin", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: A low incidence of cardiovascular malformations was observed after exposure to each of the four calcium channel blockers , but this incidence was statistically significant only for verapamil and nifedipine .

Example answer:
{"entities": [{"text": "cardiovascular malformations", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: Our results suggest that addition of phenylephrine to nitroglycerin is not beneficial in the treatment of patients with acute myocardial infarction .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "nitroglycerin", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: In individuals with preexisting , high-grade coronary arterial narrowing , acute myocardial infarction may result from an increase in myocardial oxygen demand associated with cocaine-induced increase in rate-pressure product .

Example answer:
{"entities": [{"text": "acute myocardial infarction", "type": "Disease"}, {"text": "oxygen", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}]}

Example input:
Sentence: The effect of nitroglycerin on heart rate and systolic blood pressure was compared in 5 normal subjects , 12 diabetic subjects without autonomic neuropathy , and 5 diabetic subjects with autonomic neuropathy .

Example answer:
{"entities": [{"text": "nitroglycerin", "type": "Chemical"}, {"text": "diabetic", "type": "Disease"}, {"text": "autonomic neuropathy", "type": "Disease"}]}

Example input:
Sentence: Dipyridamole significantly increased coronary blood flow before and after 7.5 or 15 mm/kg i.v .

Example answer:
{"entities": [{"text": "Dipyridamole", "type": "Chemical"}]}

Example input:
Sentence: The magnitude and time course of the increase in heart rate and the decrease in systolic blood pressure after nitroglycerin were similar in the normal and diabetic subjects without autonomic neuropathy , whereas a lesser increase in heart rate and a greater decrease in systolic blood pressure occurred in the diabetic subjects with autonomic neuropathy .

Example answer:
{"entities": [{"text": "nitroglycerin", "type": "Chemical"}, {"text": "diabetic", "type": "Disease"}, {"text": "autonomic neuropathy", "type": "Disease"}]}

Example input:
Sentence: Nitroglycerin has been shown to reduce ST-segment elevation during acute myocardial infarction , an effect potentiated in the dog by agents that reverse nitroglycerin-induced hypotension .

Example answer:
{"entities": [{"text": "Nitroglycerin", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}, {"text": "nitroglycerin-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Ten patients with acute transmural myocardial infarctions received intravenous nitroglycerin , sufficient to reduce mean arterial pressure from 107 +/- 6 to 85 +/- 6 mm Hg ( P less than 0.001 ) , for 60 minutes .

Example answer:
{"entities": [{"text": "myocardial infarctions", "type": "Disease"}, {"text": "nitroglycerin", "type": "Chemical"}]}

Input:
Sentence: Thus , whereas nitroglycerin preferentially and flow-independently dilates large coronary arteries , cromakalim and pinacidil dilate both large and small coronary arteries and this effect is not dependent upon the simultaneous beta adrenoceptors-mediated rise in myocardial metabolic demand .

## Item bc5cdr:test:773
Example input:
Sentence: Eight patients were dead in the last follow-up ; two of them died of treatment-related toxicity .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Seven patients had previously received radiotherapy and seven had received hormone therapy .

Example answer:
{"entities": []}

Example input:
Sentence: All patients had some response to the combined therapy and five of the seven went into complete remission after one or two courses of AraG/VP/CPM .

Example answer:
{"entities": [{"text": "AraG/VP/CPM", "type": "Chemical"}]}

Example input:
Sentence: Reports of persistent paralysis after the discontinuance of these drugs have most often involved aminosteroid-based NMBAs such as vecuronium bromide , especially when used in conjunction with corticosteroids .

Example answer:
{"entities": [{"text": "paralysis", "type": "Disease"}, {"text": "vecuronium bromide", "type": "Chemical"}]}

Example input:
Sentence: After discontinuing isoniazid therapy a similar pattern of behavior was noted that was controlled by pyridoxine .

Example answer:
{"entities": [{"text": "isoniazid", "type": "Chemical"}, {"text": "pyridoxine", "type": "Chemical"}]}

Example input:
Sentence: Discontinuance of effective chemotherapy in this patient during partial remission resulted in fatal disease progression .

Example answer:
{"entities": []}

Example input:
Sentence: The patient recovered within 1 week following discontinuation of antianginal therapy .

Example answer:
{"entities": []}

Example input:
Sentence: After discontinuing the oral alendronate , the patient underwent six cycles of hemodialysis and four cycles of LDL apheresis .

Example answer:
{"entities": [{"text": "alendronate", "type": "Chemical"}]}

Example input:
Sentence: Most patients ( 57 % ) stopped treatment because of disease progression .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Sixty-seven of 926 patients ( 7.2 % ) required discontinuation of spironolactone due to hyperkalemia ( n = 33 ) or renal failure ( n = 34 ) .

Example answer:
{"entities": [{"text": "spironolactone", "type": "Chemical"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Input:
Sentence: All three patients required therapy discontinuation .

## Item bc5cdr:test:625
Example input:
Sentence: Mean arterial pressure was decreased to 50 mm Hg for 30 minutes either by hemorrhage ( HEM , n = 7 ) or by continuous infusion of sodium nitroprusside ( SNP , n = 7 ) .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "Disease"}, {"text": "HEM", "type": "Disease"}, {"text": "sodium nitroprusside", "type": "Chemical"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: Application of a delayed feedback signal , in the form of a 2-h systemic corticosterone infusion in urethane-anesthetized rats with pharmacological blockade of glucocorticoid synthesis , is without effect on the resting secretion of arginine vasopressin and oxytocin at any corticosterone feedback dose tested .

Example answer:
{"entities": [{"text": "corticosterone", "type": "Chemical"}, {"text": "urethane-anesthetized", "type": "Chemical"}, {"text": "arginine vasopressin", "type": "Chemical"}, {"text": "oxytocin", "type": "Chemical"}]}

Example input:
Sentence: After starting PGE1 or TMP , MAP and rate pressure product ( RPP ) decreased significantly compared with preinfusion values ( P < 0.01 ) , and the degree of hypotension due to PGE1 remained constant until 60 min after its discontinuation .

Example answer:
{"entities": [{"text": "PGE1", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: On the other hand , pretreatment with p-chlorophenylalamine ( 3 X 320 mg/kg i.p. , 24 hr ) , a serotonin depletor , caused no significant change in the hyperactivity .

Example answer:
{"entities": [{"text": "p-chlorophenylalamine", "type": "Chemical"}, {"text": "serotonin", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}]}

Example input:
Sentence: In isolated perfused heart preparations from isoproterenol-pretreated rats , the isoproterenol-induced maximal increase in left ventricular systolic pressure was significantly reduced , compared with saline-pretreated rats ( the EC50 of the isoproterenol-induced increase in left ventricular systolic pressure was enhanced approximately 22-fold ) .

Example answer:
{"entities": [{"text": "isoproterenol-pretreated", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: d-1 given for 4 weeks , elevated blood pressure from 102+/-13 to 152+/-15 mm Hg and increased the synthesis of ET-1 and the levels of ET-1 mRNA in the mesenteric artery ( 240 % and 230 % , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: Isoproterenol pretreatment for 15 days caused cardiac hypertrophy without affecting baseline blood pressure and heart rate .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "Chemical"}, {"text": "cardiac hypertrophy", "type": "Disease"}]}

Example input:
Sentence: Controlled hypotension in groups A and C was induced with PGE1 to maintain mean arterial blood pressure at 55 mmHg for 180 min .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "PGE1", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Subsequent addition of phenylephrine infusion , sufficient to re-elevate mean arterial pressure to 106 +/- 4 mm Hg ( P less than 0.001 ) for 30 minutes , increased left ventricular filling pressure to 17 +/- 2 mm Hg ( P less than 0.05 ) and also significantly increased sigmaST ( P less than 0.05 ) .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}]}

Input:
Sentence: Thus , `` stress '' levels of adrenaline ( 230 pg/ml ) for 6 h cause a delayed and protracted pressor effect .

## Item bc5cdr:test:774
Example input:
Sentence: After recovery of blood pressure to control values , the extrusion of Na+ from cardiac cells was normalized , as revealed by restoration of the ( Na , K ) -ATPase activity .

Example answer:
{"entities": [{"text": "Na+", "type": "Chemical"}, {"text": "Na", "type": "Chemical"}, {"text": "K", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : If ECG alone is used for specificity , the combination with dP/dtejc improved the sensitivity of the test and could be a cost-savings alternative to cardiac imaging or perfusion studies to detect myocardial ischemia , especially in patients unable to exercise .

Example answer:
{"entities": [{"text": "myocardial ischemia", "type": "Disease"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: Routine EKG monitoring during infusional cyclophosphamide did not predict CHF development .

Example answer:
{"entities": [{"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CHF", "type": "Disease"}]}

Example input:
Sentence: Age-related changes in ultrasound production corresponded with changes in cardiovascular variables , including baseline cardiac rate and clonidine-induced bradycardia .

Example answer:
{"entities": [{"text": "clonidine-induced", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : To assess the added diagnostic value of a new cardiac performance index ( dP/dtejc ) measurement , based on brachial artery flow changes , as compared to standard 12-lead ECG , for detecting dobutamine-induced myocardial ischemia , using Tc99m-Sestamibi single-photon emission computed tomography as the gold standard of comparison to assess the presence or absence of ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "Tc99m-Sestamibi", "type": "Chemical"}, {"text": "ischemia", "type": "Disease"}]}

Example input:
Sentence: TCR prevented the isoproterenol-induced decrease in antioxidant enzymes in the heart and increased the rate of ADP-stimulated oxygen uptake and respiratory coupling ratio .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "ADP-stimulated", "type": "Chemical"}, {"text": "oxygen", "type": "Chemical"}]}

Example input:
Sentence: together for 30 consecutive days and challenged with ISO on the day 29th and 30th , showed a significant ( P < 0.05 ) decrease in heart weight , serum marker enzymes , lipid peroxidation , Ca+2 ATPase and a significant increase in the body weight , endogenous antioxidants , Na+/K+ ATPase and Mg+2 ATPase when compared with ISO treated group and green tea or vitamin E alone treated groups .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}, {"text": "green tea", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}]}

Example input:
Sentence: These changes in the serum transaminases were associated with corresponding depletions in the cardiac GOT and GPT .

Example answer:
{"entities": []}

Example input:
Sentence: Cardiac marker enzymes and antioxidative parameters in serum and heart tissues were measured .

Example answer:
{"entities": []}

Input:
Sentence: Cardiac enzymes remained normal despite transient electrocardiographic ( EKG ) changes .

## Item bc5cdr:test:568
Example input:
Sentence: Omitting fentanyl reduces nausea and vomiting , without increasing pain , after sevoflurane for day surgery .

Example answer:
{"entities": [{"text": "fentanyl", "type": "Chemical"}, {"text": "nausea", "type": "Disease"}, {"text": "vomiting", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "sevoflurane", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Omission of fentanyl did not reduce the overall incidence of postoperative nausea and vomiting , but did reduce the incidence of vomiting and/or moderate to severe nausea prior to discharge from 20 % and 17 % with fentanyl and fentanyl-dexamethasone , respectively , to 5 % ( P = 0.013 ) .

Example answer:
{"entities": [{"text": "fentanyl", "type": "Chemical"}, {"text": "postoperative nausea and vomiting", "type": "Disease"}, {"text": "vomiting", "type": "Disease"}, {"text": "nausea", "type": "Disease"}, {"text": "fentanyl-dexamethasone", "type": "Chemical"}]}

Example input:
Sentence: Bladder retention of urine as a result of continuous intravenous infusion of fentanyl : 2 case reports .

Example answer:
{"entities": [{"text": "retention of urine", "type": "Disease"}, {"text": "fentanyl", "type": "Chemical"}]}

Example input:
Sentence: Two patients with similar clinical features are presented : both patients had chronic renal failure , on hemodialysis for many years but recently begun on a high-flux dialyzer ; both had been receiving a carbidopa/levodopa preparation ; and both had the onset of hallucinosis and recurrent seizures , which were refractory to anticonvulsants .

Example answer:
{"entities": [{"text": "chronic renal failure", "type": "Disease"}, {"text": "carbidopa/levodopa", "type": "Chemical"}, {"text": "hallucinosis", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Disease"}]}

Example input:
Sentence: This complication reappeared on day 25 during the second dose of 5-fluorouracil and folinic acid , which were then the only drugs given .

Example answer:
{"entities": [{"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: Fentanyl did reduce minor intraoperative movement but had no sevoflurane-sparing effect and increased respiratory depression , hypotension and bradycardia .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "Chemical"}, {"text": "sevoflurane-sparing", "type": "Chemical"}, {"text": "respiratory depression", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Here , 2 cases of urinary bladder retention leading to renal pelvocalyceal dilatation mimicking hydronephrosis as a result of continuous infusion of fentanyl are reported .

Example answer:
{"entities": [{"text": "urinary bladder retention", "type": "Disease"}, {"text": "hydronephrosis", "type": "Disease"}, {"text": "fentanyl", "type": "Chemical"}]}

Example input:
Sentence: Patients were randomly allocated to either receive or not receive 1 1 fentanyl , while a third group received dexamethasone in addition to fentanyl .

Example answer:
{"entities": [{"text": "fentanyl", "type": "Chemical"}, {"text": "dexamethasone", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Following induction of anesthesia by fentanyl ( 0.15 mg kg ( -1 ) ) and propofol ( 2.0 mg kg ( -1 ) ) , 13 patients received phenylephrine ( 0.1 mg iv ) and 12 patients received ephedrine ( 10 mg iv ) to restore mean arterial pressure ( MAP ) .

Example answer:
{"entities": [{"text": "fentanyl", "type": "Chemical"}, {"text": "propofol", "type": "Chemical"}, {"text": "phenylephrine", "type": "Chemical"}, {"text": "ephedrine", "type": "Chemical"}]}

Input:
Sentence: In addition , the patients received fentanyl and d-tubocurarine .

## Item bc5cdr:test:699
Example input:
Sentence: During an 18-month period of study 41 hemodialyzed patients receiving desferrioxamine ( 10-40 mg/kg BW/3 times weekly ) for the first time were monitored for detection of audiovisual toxicity .

Example answer:
{"entities": [{"text": "desferrioxamine", "type": "Chemical"}, {"text": "audiovisual toxicity", "type": "Disease"}]}

Example input:
Sentence: On the other hand , pretreatment with p-chlorophenylalamine ( 3 X 320 mg/kg i.p. , 24 hr ) , a serotonin depletor , caused no significant change in the hyperactivity .

Example answer:
{"entities": [{"text": "p-chlorophenylalamine", "type": "Chemical"}, {"text": "serotonin", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}]}

Example input:
Sentence: A 17-day-old infant on isoniazid therapy 13 mg/kg daily from birth because of maternal tuberculosis was admitted after 4 days of clonic fits .

Example answer:
{"entities": [{"text": "isoniazid", "type": "Chemical"}, {"text": "tuberculosis", "type": "Disease"}, {"text": "clonic fits", "type": "Disease"}]}

Example input:
Sentence: Patients in Group C received 2 ml normal saline , Group L , 2 ml , lidocaine 2 % ( 40 mg ) and Group T , 2 ml thiopentone 2.5 % ( 50 mg ) .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "thiopentone", "type": "Chemical"}]}

Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "Chemical"}, {"text": "Ato-treated", "type": "Chemical"}]}

Example input:
Sentence: 2 and 10 mg/kg/i.p. , or an equal volume of saline for the control group ( n = 20 ) ; 15 minutes later , all the animals were injected with a single 50 mg/kg/i.p .

Example answer:
{"entities": []}

Example input:
Sentence: CASE SUMMARY : A 13-year-old boy was treated with ampicillin and gentamicin because of suspected septicemia .

Example answer:
{"entities": [{"text": "ampicillin", "type": "Chemical"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "septicemia", "type": "Disease"}]}

Example input:
Sentence: METHOD : In a 16-week multicenter , double-blind trial , 122 children with ADHD were randomly assigned to clonidine ( n = 31 ) , methylphenidate ( n = 29 ) , clonidine and methylphenidate ( n = 32 ) , or placebo ( n = 30 ) .

Example answer:
{"entities": [{"text": "ADHD", "type": "Disease"}, {"text": "clonidine", "type": "Chemical"}, {"text": "methylphenidate", "type": "Chemical"}]}

Example input:
Sentence: The authors present a 10-year-old boy chronically treated with lisinopril , an angiotensin converting enzyme inhibitor , to control hypertension who developed hypotension following the addition of tizanidine , an alpha-2 agonist , for the treatment of spasticity .

Example answer:
{"entities": [{"text": "lisinopril", "type": "Chemical"}, {"text": "angiotensin", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}, {"text": "tizanidine", "type": "Chemical"}, {"text": "spasticity", "type": "Disease"}]}

Example input:
Sentence: Following instrumentation , halothane was discontinued and alfentanil ( 125 mu/kg ) administered iv during emergence from halothane anesthesia .

Example answer:
{"entities": [{"text": "halothane", "type": "Chemical"}, {"text": "alfentanil", "type": "Chemical"}]}

Input:
Sentence: were studied in 32 children ( mean age 6.9 yr ) pretreated with either physiological saline or alfentanil 50 micrograms kg-1 .

## Item bc5cdr:test:691
Example input:
Sentence: Chloroacetaldehyde and its contribution to urotoxicity during treatment with cyclophosphamide or ifosfamide .

Example answer:
{"entities": [{"text": "Chloroacetaldehyde", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "ifosfamide", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Six of 61 women ( 10 % ) developed clinically reversible grade 3 CHF following infusional cyclophosphamide with a median percent decline in ejection fraction of 31 % .

Example answer:
{"entities": [{"text": "CHF", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}]}

Example input:
Sentence: Cyclophosphamide therapy increases the risk of carcinoma of the bladder .

Example answer:
{"entities": [{"text": "Cyclophosphamide", "type": "Chemical"}]}

Example input:
Sentence: Moreover , systemic lipopolysaccharide pretreatment ( 1 mg/kg ) attenuated local methamphetamine infusion-produced dopamine and 3,4-dihydroxyphenylacetic acid depletions in the striatum , indicating that the protective effect of lipopolysaccharide is less likely due to interrupted peripheral distribution or metabolism of methamphetamine .

Example answer:
{"entities": [{"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "3,4-dihydroxyphenylacetic acid", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : The results indicate a dose-response relationship between cyclophosphamide and the risk of bladder cancer , high cumulative risks in the entire cohort , and also the possibility of risk factors operating even before Wegener 's granulomatosis .

Example answer:
{"entities": [{"text": "cyclophosphamide", "type": "Chemical"}, {"text": "bladder cancer", "type": "Disease"}, {"text": "Wegener 's granulomatosis", "type": "Disease"}]}

Example input:
Sentence: Additionally , since membrane leakage is a final stage of cytotoxicity , the disruption of the structural characteristics of biomembranes by TAM may contribute to the multiple mechanisms of its anticancer action .

Example answer:
{"entities": [{"text": "TAM", "type": "Chemical"}]}

Example input:
Sentence: Our results demonstrate that both cisplatin and paclitaxel cause early mitochondrial impairment with loss of membrane potential and induction of autophagic vacuoles in neurons .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "mitochondrial impairment", "type": "Disease"}]}

Example input:
Sentence: INTRODUCTION : Cyclophosphamide is an alkylating agent given frequently as a component of many conditioning regimens .

Example answer:
{"entities": [{"text": "Cyclophosphamide", "type": "Chemical"}]}

Example input:
Sentence: In cyclophosphamide-induced cystitis in the rat , detrusor function is impaired and the expression and effects of muscarinic receptors altered .

Example answer:
{"entities": [{"text": "cyclophosphamide-induced", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Example input:
Sentence: In vitro characterization of parasympathetic and sympathetic responses in cyclophosphamide-induced cystitis in the rat .

Example answer:
{"entities": [{"text": "cyclophosphamide-induced", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Input:
Sentence: The initial response to the primary attack by the cyclophosphamide metabolites seems to be fragmentation of the luminal membrane .

## Item bc5cdr:test:725
Example input:
Sentence: They became more severe in the later months of the experiment , and were most severe after 12 months , located mainly in the molecular layer of the cerebellar cortex .

Example answer:
{"entities": []}

Example input:
Sentence: Among the 5 patients with white matter abnormalities , 4 patients ( 80.0 % ) showed higher than normal ADC values on initial MR images , and all showed complete resolution on follow-up images .

Example answer:
{"entities": [{"text": "white matter abnormalities", "type": "Disease"}]}

Example input:
Sentence: Because of the rapid systemic clearance of BCNU ( 1,3-bis- ( 2-chloroethyl ) -1-nitrosourea ) , intra-arterial administration should provide a substantial advantage over intravenous administration for the treatment of malignant gliomas .

Example answer:
{"entities": [{"text": "BCNU", "type": "Chemical"}, {"text": "1,3-bis- ( 2-chloroethyl ) -1-nitrosourea", "type": "Chemical"}, {"text": "malignant gliomas", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Glioblastoma is a malignant tumor that occurs in the cerebrum during adulthood .

Example answer:
{"entities": [{"text": "Glioblastoma", "type": "Disease"}, {"text": "malignant tumor", "type": "Disease"}]}

Example input:
Sentence: One patient was prematurely discontinued from the study for severe headache and abdominal pain .

Example answer:
{"entities": [{"text": "headache", "type": "Disease"}, {"text": "abdominal pain", "type": "Disease"}]}

Example input:
Sentence: In SE survivors , similar stimulation resulted in a population spike followed , at a variable latency , by negative DC shifts and repetitive afterdischarges of 3-60 s duration , which were blocked by ionotropic glutamate receptor antagonists .

Example answer:
{"entities": [{"text": "SE", "type": "Disease"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: He developed acute neurologic symptoms of mental confusion , disorientation and irritability , and then lapsed into a deep coma , lasting for approximately 40 hours during the first dose ( day 2 ) of 5-fluorouracil and folinic acid infusion .

Example answer:
{"entities": [{"text": "confusion", "type": "Disease"}, {"text": "disorientation", "type": "Disease"}, {"text": "irritability", "type": "Disease"}, {"text": "coma", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: CASE : A 58-year-old man received an intracarotid injection of carboplatin for recurrent glioblastomas in his left temporal lobe .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}, {"text": "glioblastomas", "type": "Disease"}]}

Example input:
Sentence: Twelve patients with Grade III or IV astrocytomas were treated after partial resection of the tumor without prior radiation therapy .

Example answer:
{"entities": [{"text": "astrocytomas", "type": "Disease"}, {"text": "tumor", "type": "Disease"}]}

Example input:
Sentence: Twenty-four patients with recurrent Grade I to IV astrocytomas , whose resection and irradiation therapy had failed , received two to eight courses of intra-arterial BCNU therapy .

Example answer:
{"entities": [{"text": "astrocytomas", "type": "Disease"}, {"text": "BCNU", "type": "Chemical"}]}

Input:
Sentence: In six of eight patients ( 75 % ) who we treated for recurrent or resistant glioma , sudden severe neurologic deterioration occurred .

## Item bc5cdr:test:481
Example input:
Sentence: Of the 14 patients , 5 ( 35.7 % ) had white matter abnormalities , 1 ( 7.1 % ) had putaminal hemorrhage , and 8 ( 57.1 % ) had normal findings on initial MR images .

Example answer:
{"entities": [{"text": "white matter abnormalities", "type": "Disease"}, {"text": "putaminal hemorrhage", "type": "Disease"}]}

Example input:
Sentence: Minor side effects included nausea ( thirteen patients ) , emesis ( eight of the thirteen patients with nausea ) , clumsiness ( evident as ataxic movements in ten patients ) , and dysphoric reaction ( one patient ) .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "emesis", "type": "Disease"}, {"text": "clumsiness", "type": "Disease"}, {"text": "ataxic movements", "type": "Disease"}, {"text": "dysphoric reaction", "type": "Disease"}]}

Example input:
Sentence: Myasthenia gravis presenting as weakness after magnesium administration .

Example answer:
{"entities": [{"text": "Myasthenia gravis", "type": "Disease"}, {"text": "magnesium", "type": "Chemical"}]}

Example input:
Sentence: One to 2 % of patients have elevations of serum transaminases to greater than 3 times the upper limit of normal .

Example answer:
{"entities": []}

Example input:
Sentence: Conventional agents are associated with unwanted central nervous system effects , including extrapyramidal symptoms ( EPS ) , tardive dyskinesia , sedation , and possible impairment of some cognitive measures , as well as cardiac effects , orthostatic hypotension , hepatic changes , anticholinergic side effects , sexual dysfunction , and weight gain .

Example answer:
{"entities": [{"text": "extrapyramidal symptoms", "type": "Disease"}, {"text": "EPS", "type": "Disease"}, {"text": "tardive dyskinesia", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}]}

Example input:
Sentence: There were 13 cases of adverse reactions ( 0.34 % ) , ten of which were mild reactions such as nausea , exanthema , urtication , itchiness , and urgency to defecate , and did not require treatment .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "exanthema", "type": "Disease"}, {"text": "urtication", "type": "Disease"}, {"text": "itchiness", "type": "Disease"}]}

Example input:
Sentence: The most common toxicities encountered were transient serum transaminase and bilirubin elevations , neutropenia , and mucositis .

Example answer:
{"entities": [{"text": "toxicities", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}, {"text": "neutropenia", "type": "Disease"}, {"text": "mucositis", "type": "Disease"}]}

Example input:
Sentence: Other possible adverse effects -- such as gastrointestinal disorders , orthostatic hypotension , levodopa-induced psychosis , sleep disturbances or parasomnias , or drug interactions -- also require carefully monitored individual treatment .

Example answer:
{"entities": [{"text": "gastrointestinal disorders", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "levodopa-induced", "type": "Chemical"}, {"text": "psychosis", "type": "Disease"}, {"text": "sleep disturbances", "type": "Disease"}, {"text": "parasomnias", "type": "Disease"}]}

Example input:
Sentence: Grade 3-4 adverse effects included myelosuppression , fatigue , somnolence/depressed mood , neuropathy and dyspnea .

Example answer:
{"entities": [{"text": "myelosuppression", "type": "Disease"}, {"text": "fatigue", "type": "Disease"}, {"text": "somnolence/depressed mood", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}, {"text": "dyspnea", "type": "Disease"}]}

Example input:
Sentence: The most common adverse events were nausea ( 17.2 % and 16.1 % ; 95 % CI , -3.7 to 6.0 ) , hiccups ( 10.7 % and 6.6 % ; 95 % CI , 0.5 to 7.8 ) , and headache ( 8.7 % and 9.9 % ; 95 % Cl , -5.0 to 2.6 ) .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "hiccups", "type": "Disease"}, {"text": "headache", "type": "Disease"}]}

Input:
Sentence: Menstrual abnormalities ( 79 % ) , weight gain ( 60 % ) , muscle cramps/myalgias ( 40 % ) , and transaminase elevations ( 40 % ) were the most common adverse reactions .

## Item bc5cdr:test:735
Example input:
Sentence: At autopsy the liver was enlarged and firm with signs of venous congestion .

Example answer:
{"entities": [{"text": "venous congestion", "type": "Disease"}]}

Example input:
Sentence: Histological evaluation of hearts from all rats given DOX revealed significant slight degrees of perivascular and interstitial fibrosis .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: The morphological analysis of the kidneys included a semi-quantitative scoring system analysing the degree of striped fibrosis , subcapsular fibrosis and the number of basophilic tubules , plus an additional stereological analysis of the total grade of fibrosis in the cortex stained with Sirius Red .

Example answer:
{"entities": [{"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: There was no evidence of repair to the damaged medullary interstitial matrix , or proliferation of remaining undamaged type 1 medullary interstitial cells after the recovery period following analgesic treatment .

Example answer:
{"entities": []}

Example input:
Sentence: Although hepatocyte TJs are impaired in cholestasis , attempts to localize the precise site of hepatocyte TJ damage by freeze-fracture electron microscopy have produced limited information .

Example answer:
{"entities": [{"text": "cholestasis", "type": "Disease"}]}

Example input:
Sentence: Hepatocyte tight junctions ( TJs ) , the only intercellular barrier between the sinusoidal and the canalicular spaces , play a key role in bile formation .

Example answer:
{"entities": []}

Example input:
Sentence: Minimal cholestasis was seen in two cases and portal fibrosis of a reversible degree in eight .

Example answer:
{"entities": [{"text": "cholestasis", "type": "Disease"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: FINDINGS : The liver biopsy sample showed hepatocellular necrosis which was prominent in perivenular zone three and extended focally from portal tracts to portal tracts and centrilobular areas ( bridging necrosis ) .

Example answer:
{"entities": [{"text": "necrosis", "type": "Disease"}]}

Example input:
Sentence: Different lobular distributions of altered hepatocyte tight junctions in rat models of intrahepatic and extrahepatic cholestasis .

Example answer:
{"entities": []}

Example input:
Sentence: This study is the first to demonstrate that impairment of hepatocyte TJs occurs heterogenously in the liver lobule after BDL and suggests that BDL and EE treatments produce different lobular distributions of increased paracellular permeability .

Example answer:
{"entities": [{"text": "EE", "type": "Chemical"}]}

Input:
Sentence: Prominent fibrosis and hepatocellular regeneration were also present ; however , the lobular architecture was preserved .

## Item bc5cdr:test:601
Example input:
Sentence: Treatment-related adverse events ( AEs ) occurred in 44 % and 52 % , 57 % , and 41 % of the asenapine at 5 and 10 mg BID , haloperidol , and placebo groups , respectively .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: The patient was taking 80 mg simvastatin at bedtime ( initiated 27 days earlier ) ; amiodarone at a dose of 400 mg daily for 7 days , then 200 mg daily ( initiated 19 days earlier ) ; and 400 mg atazanavir daily ( initiated at least 2 years previously ) .

Example answer:
{"entities": [{"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: METHOD : In a 6-week random-assignment , double-blind , placebo-controlled trial ( phase A ) , haloperidol , 2-3 mg/day ( standard dose ) , and haloperidol , 0.50-0.75 mg/day ( low dose ) , were compared in 71 outpatients with Alzheimer 's disease .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "Alzheimer 's disease", "type": "Disease"}]}

Example input:
Sentence: METHODS : Seventeen subjects who were genotyped as CYP2D6 extensive metabolizers were enrolled in this randomized , open-label , crossover study to receive a single oral dose of desipramine ( 50 mg ) on two separate occasions , once alone and once after multiple doses of cinacalcet ( 90 mg for 7 days ) .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}]}

Example input:
Sentence: To determine sensitivity we assessed tremor in 44 patients with obstructive lung disease after administration of cumulative doses of salbutamol .

Example answer:
{"entities": [{"text": "tremor", "type": "Disease"}, {"text": "obstructive lung disease", "type": "Disease"}, {"text": "salbutamol", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : The results indicated a favorable therapeutic profile for haloperidol in doses of 2-3 mg/day , although a subgroup developed moderate to severe extrapyramidal signs .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "extrapyramidal signs", "type": "Disease"}]}

Example input:
Sentence: Mean peak forced expiratory volume in 1 second ( FEV1 ) increases over baseline and the proportion of patients attaining at least a 15 % increase in the FEV1 ( responders ) were 31 % and 90 % , respectively , for ipratropium and 17 % and 50 % , respectively , for theophylline .

Example answer:
{"entities": [{"text": "ipratropium", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}]}

Example input:
Sentence: The bronchodilator effects of a single dose of ipratropium bromide aerosol ( 36 micrograms ) and short-acting theophylline tablets ( dose titrated to produce serum levels of 10-20 micrograms/mL ) were compared in a double-blind , placebo-controlled crossover study in 21 patients with stable , chronic obstructive pulmonary disease .

Example answer:
{"entities": [{"text": "ipratropium bromide", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}, {"text": "chronic obstructive pulmonary disease", "type": "Disease"}]}

Example input:
Sentence: In a double-blind 6-week trial , 458 patients with acute schizophrenia were randomly assigned to fixed-dose treatment with asenapine at 5 mg twice daily ( BID ) , asenapine at 10 mg BID , placebo , or haloperidol at 4 mg BID ( to verify assay sensitivity ) .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "Disease"}, {"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Input:
Sentence: Twelve asthmatic patients ( FEV1 , 81 +/- 4 % predicted ) , requiring only occasional inhaled beta-agonists as their sole therapy , were given a 14-day treatment with high dose inhaled salbutamol ( HDS ) , 4,000 micrograms daily , low dose inhaled salbutamol ( LDS ) , 800 micrograms daily , or placebo ( PI ) by metered-dose inhaler in a double-blind , randomized crossover design .

## Item bc5cdr:test:498
Example input:
Sentence: Long-term follow-up of ifosfamide renal toxicity in children treated for malignant mesenchymal tumors : an International Society of Pediatric Oncology report .

Example answer:
{"entities": [{"text": "ifosfamide", "type": "Chemical"}, {"text": "renal toxicity", "type": "Disease"}, {"text": "malignant mesenchymal tumors", "type": "Disease"}]}

Example input:
Sentence: This low percentage ( 5 % ) of TDFS must be evaluated with respect to the efficacy of ifosfamide in the treatment of mesenchymal tumors in children .

Example answer:
{"entities": [{"text": "ifosfamide", "type": "Chemical"}, {"text": "mesenchymal tumors", "type": "Disease"}]}

Example input:
Sentence: We report on two fatal cases of accidental intrathecal vincristine instillation in a 5-year old girl with recurrent acute lymphoblastic leucemia and a 57-year old man with lymphoblastic lymphoma .

Example answer:
{"entities": [{"text": "vincristine", "type": "Chemical"}, {"text": "acute lymphoblastic leucemia", "type": "Disease"}, {"text": "lymphoblastic lymphoma", "type": "Disease"}]}

Example input:
Sentence: METHODS : Forty-nine patients with advanced NSCLC were included , 38 of whom were age > /= 70 years and 11 were age < 70 years but who had some contraindication to receiving cisplatin .

Example answer:
{"entities": [{"text": "NSCLC", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: Based on this principle a 27-year old woman , classified as being in the high-risk group ( Goldstein and Berkowitz score : 11 ) , was treated with multiple cytotoxic drugs .

Example answer:
{"entities": []}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Example input:
Sentence: Twenty children with acute lymphoblastic leukemia who developed meningeal disease were treated with a high-dose intravenous methotrexate regimen that was designed to achieve and maintain CSF methotrexate concentrations of 10 ( -5 ) mol/L without the need for concomitant intrathecal dosing .

Example answer:
{"entities": [{"text": "acute lymphoblastic leukemia", "type": "Disease"}, {"text": "meningeal disease", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: Severe toxicity was correlated with the higher cumulative dose of 60 g/m2 of ifosfamide , a younger age ( less than 2 1/2 years old ) , and a predominance of vesicoprostatic tumor involvement .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "tumor", "type": "Disease"}]}

Example input:
Sentence: The renal function of 74 children with malignant mesenchymal tumors in complete remission and who have received the same ifosfamide chemotherapy protocol ( International Society of Pediatric Oncology Malignant Mesenchymal Tumor Study 84 [ SIOP MMT 84 ] ) were studied 1 year after the completion of treatment .

Example answer:
{"entities": [{"text": "malignant mesenchymal tumors", "type": "Disease"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "Malignant Mesenchymal Tumor", "type": "Disease"}]}

Example input:
Sentence: In view of the known tendency of busulfan to induce cellular atypia and carcinoma in other sites , periodic urinary cytology is suggested in patients on long-term therapy .

Example answer:
{"entities": [{"text": "busulfan", "type": "Chemical"}, {"text": "carcinoma", "type": "Disease"}]}

Input:
Sentence: We report here a retrospective study of 123 children ( median age , 6.5 years ) receiving high-dose busulfan in combined chemotherapy before bone marrow transplantation for malignant solid tumors , brain tumors excluded .

## Item bc5cdr:test:741
Example input:
Sentence: Pregnant rats were administered one of these calcium channel blockers during the period of cardiac morphogenesis and the offspring examined on day 20 of gestation for cardiovascular malformations .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "cardiovascular malformations", "type": "Disease"}]}

Example input:
Sentence: Apamin , a selective blocker of calcium-dependent potassium channels , was administered intracerebroventricularly in rats anesthetized with 0.8 % sevoflurane to investigate the mechanism of the anticonvulsive effects .

Example answer:
{"entities": [{"text": "Apamin", "type": "Chemical"}, {"text": "calcium-dependent", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}, {"text": "sevoflurane", "type": "Chemical"}]}

Example input:
Sentence: The effect of a 6-week treatment with the calcium channel blocker nitrendipine or the angiotensin converting enzyme inhibitor enalapril on blood pressure , albuminuria , renal hemodynamics , and morphology of the nonclipped kidney was studied in rats with two-kidney , one clip renovascular hypertension .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "nitrendipine", "type": "Chemical"}, {"text": "angiotensin", "type": "Chemical"}, {"text": "enalapril", "type": "Chemical"}, {"text": "albuminuria", "type": "Disease"}, {"text": "renovascular hypertension", "type": "Disease"}]}

Example input:
Sentence: Preclinical toxicologic investigation suggested that a new calcium channel blocker , Ro 40-5967 , induced cardiovascular alterations in rat fetuses exposed to this agent during organogenesis .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "Ro 40-5967", "type": "Chemical"}, {"text": "cardiovascular alterations", "type": "Disease"}]}

Example input:
Sentence: The reduction of cyclosporine- or tacrolimus trough levels and the administration of calcium channel blockers led to relief of pain .

Example answer:
{"entities": [{"text": "cyclosporine-", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: The present study was designed to investigate the hypothesis that calcium channel blockers in general induce cardiovascular malformations indicating a pharmacologic class effect .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "cardiovascular malformations", "type": "Disease"}]}

Example input:
Sentence: The purpose of this study was to investigate the influence of calcium channel blockers on bupivacaine-induced acute toxicity .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "bupivacaine-induced", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: A low incidence of cardiovascular malformations was observed after exposure to each of the four calcium channel blockers , but this incidence was statistically significant only for verapamil and nifedipine .

Example answer:
{"entities": [{"text": "cardiovascular malformations", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: For each of the three tested calcium channel blockers ( diltiazem , verapamil and bepridil ) 6 groups of mice were treated by two different doses , i.e .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "bepridil", "type": "Chemical"}]}

Example input:
Sentence: We studied three calcium channel blockers of different structure , nifedipine , diltiazem , and verapamil , along with the new agent .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "nifedipine", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Input:
Sentence: Clinical applications of calcium channel blockers parallel their tissue selectivity .
