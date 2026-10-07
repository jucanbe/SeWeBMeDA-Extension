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

## Item bc5cdr:test:83
Input:
Sentence: Treatment has been continued in 3 individuals for 6-13 months with persistence of the pressor effect , although there appears to have been some decrease in the degree of response with time .

## Item bc5cdr:test:46
Input:
Sentence: Gram-negative bacilli were the most common causative organisms and 69 % of these infections were cured .

## Item bc5cdr:test:140
Input:
Sentence: Ninety-three rats were randomly divided into three groups .

## Item bc5cdr:test:102
Input:
Sentence: At therapeutic doses both substances raised the mean tremor amplitude to about three times the control level .

## Item bc5cdr:test:175
Input:
Sentence: The pressor response to the intracisternal ( i.c . )

## Item bc5cdr:test:103
Input:
Sentence: At the same time , the mean period within each class of amplitudes shortened by 10 -- 20 ms , whereas the mean periods calculated from all oscillations together did not change significantly .

## Item bc5cdr:test:152
Input:
Sentence: The second mother had a male infant by caesarean section .

## Item bc5cdr:test:296
Input:
Sentence: to 5 mg b.d .

## Item bc5cdr:test:310
Input:
Sentence: A high index of suspicion may lead to a quick diagnostic procedure and successful decompressive surgery .

## Item bc5cdr:test:325
Input:
Sentence: ( ABSTRACT TRUNCATED AT 250 WORDS )

## Item bc5cdr:test:380
Input:
Sentence: A follow-up investigation was performed 10-12 months after study onset on the patients who had improved .

## Item bc5cdr:test:262
Input:
Sentence: Baseline blood pressures were higher in fluctuating patients ; a higher baseline blood pressure correlated with greater hypotensive effects .

## Item bc5cdr:test:117
Input:
Sentence: It is thus confirmed that the histological characteristics of myopathic rat muscle induced experimentally are extraordinarily similar to those of human myopathy as confirmed during biopsies performed at the Orthopaedic Traumatological Centre , Florence .

## Item bc5cdr:test:2
Input:
Sentence: Noradrenergic influences on the activity of analgesics in rats .

## Item bc5cdr:test:91
Input:
Sentence: A mean overall dose of etomidate 17.4 microgram/kg/min .

## Item bc5cdr:test:176
Input:
Sentence: injection of carbachol ( 1 mug ) in anesthetized rats was analyzed .

## Item bc5cdr:test:97
Input:
Sentence: A method permitting measurement of finger tremor as a displacement-time curve is described , using a test system with simple amplitude calibration .

## Item bc5cdr:test:274
Input:
Sentence: Despite extensive clinical experience the role of digoxin is still not well defined .

## Item bc5cdr:test:183
Input:
Sentence: carbachol ( 1 mug ) was almost completely blocked by i.c .

## Item bc5cdr:test:190
Input:
Sentence: carbachol ortral and peripheral adrenergic mechanisms , and that the sympathetic trunk is the main pathway .

## Item bc5cdr:test:289
Input:
Sentence: 303 Chinese patients with mild to moderate hypertension entered the study .

## Item bc5cdr:test:155
Input:
Sentence: In view of the risks to both mother and fetus in women with prosthetic cardiac valves it is recommended that therapeutic abortion be advised as the first alternative .

## Item bc5cdr:test:201
Input:
Sentence: However , livers from female , and especially pregnant female rats , were strikingly resistant to the effects of tetracycline on depression of output of triglyceride under these experimental conditions .

## Item bc5cdr:test:288
Input:
Sentence: A 6-week open study of the introduction of isradipine treatment was conducted in general practice in Hong Kong .

## Item bc5cdr:test:36
Input:
Sentence: The exact mechanism by which diphenylhydantoin exerts its toxic effects is not known .

## Item bc5cdr:test:297
Input:
Sentence: at 4 weeks in patients with diastolic blood pressure greater than 90 mmHg and their further response was greater than those remaining on 2.5 mg b.d .

## Item bc5cdr:test:113
Input:
Sentence: We are still a long way from discovering an unequivocal pathogenetic interpretation of progressive muscular dystrophy in man .

## Item bc5cdr:test:396
Input:
Sentence: Two cases had a fatal outcome and one resulted in severe sequelae .

## Item bc5cdr:test:225
Input:
Sentence: Daily dosages of 5-10 mg corrected the hyperprolactinemia and restored menstruation in four of the six patients .

## Item bc5cdr:test:349
Input:
Sentence: Nissl-staining and antibodies against the neuron-specific calcium-binding protein , parvalbumin , served to detect neuronal damage in SNR .

## Item bc5cdr:test:374
Input:
Sentence: In addition , no significant histological change was observed in the heart of animals that received DOX in the form of HPMA copolymer conjugates and were killed at the end of the study .

## Item bc5cdr:test:347
Input:
Sentence: The neuropathology of SNR was investigated using immunohistochemical techniques with the major emphasis on the time-course of changes in neurons and astrocytes .

## Item bc5cdr:test:428
Input:
Sentence: Also , systemic vascular resistance ( SVR ) decreased during the eight-minute observation period ( P less than 0.01 ) .

## Item bc5cdr:test:406
Input:
Sentence: The patient 's change in mental status was first reported nine days after the initiation of therapy .

## Item bc5cdr:test:356
Input:
Sentence: By 6 h , vasogenic edema covered the lesioned SNR .

## Item bc5cdr:test:332
Input:
Sentence: We studied the effects of chronic selective neuronal lesion of rostral ventrolateral medulla on mean arterial pressure , heart rate , and neurogenic tone in conscious , unrestrained spontaneously hypertensive rats .

## Item bc5cdr:test:465
Input:
Sentence: However , there was a significant difference in parameters reflecting bone turnover rates between groups .

## Item bc5cdr:test:472
Input:
Sentence: Evaluation revealed a hemoglobin of three grams , 3+ Coombs ' test with polyspecific anti-human globulin and monospecific IgG reagents , and a warm reacting autoantibody .

## Item bc5cdr:test:480
Input:
Sentence: Virtually all patients experienced one or more adverse reactions .

## Item bc5cdr:test:55
Input:
Sentence: After a single oral dose of 4 mg/kg indomethacin ( IDM ) to sodium and volume depleted rats plasma renin activity ( PRA ) and systolic blood pressure fell significantly within four hours .

## Item bc5cdr:test:219
Input:
Sentence: Due to an accidental malfunctioning of the infusion pump , the patient was inadvertently administered a toxic dosage of the drug which caused renal insufficiency .

## Item bc5cdr:test:266
Input:
Sentence: The hypotensive effect appears to be related to the higher baseline blood pressure we observed in fluctuating patients relative to stable patients .

## Item bc5cdr:test:148
Input:
Sentence: Fetal risks due to warfarin therapy during pregnancy .

## Item bc5cdr:test:202
Input:
Sentence: These differences between the sexes could not be related to altered disposition of tetracycline or altered uptake of oleic acid .

## Item bc5cdr:test:8
Input:
Sentence: Pentazocine dose-dependently decreased the brain level of NA .

## Item bc5cdr:test:197
Input:
Sentence: In the intact male and female rat , no direct relationship was observed between dose of tetracycline and hepatic accumulation of triglyceride .

## Item bc5cdr:test:226
Input:
Sentence: One woman , however , developed worsened psychiatric symptoms while taking bromocriptine , and it was discontinued .

## Item bc5cdr:test:251
Input:
Sentence: Although generally regarded as `` safe , '' possible serious cardiac effects of bromocriptine should be acknowledged .

## Item bc5cdr:test:474
Input:
Sentence: Emergency physicians treating children must be aware of this syndrome in order to diagnose and treat it correctly .

## Item bc5cdr:test:96
Input:
Sentence: A method for the measurement of tremor , and a comparison of the effects of tocolytic beta-mimetics .

## Item bc5cdr:test:385
Input:
Sentence: Treatment response was not correlated with the incidence , time-course or severity of capsaicin-induced burning .

## Item bc5cdr:test:411
Input:
Sentence: The pathophysiology underlying this acute hepatic injury is unknown .

## Item bc5cdr:test:405
Input:
Sentence: We present a case in which an 89-year-old woman in a long-term care facility became confused after the initiation of misoprostol therapy .

## Item bc5cdr:test:434
Input:
Sentence: The last such episode was of acute renal failure at which stage the patient was seen by the authors of this report .

## Item bc5cdr:test:533
Input:
Sentence: Three major results are reported .

## Item bc5cdr:test:483
Input:
Sentence: No patient has died or suffered any apparent long-term sequelae that were directly attributable to the drug .

## Item bc5cdr:test:461
Input:
Sentence: In addition to experiencing hypercalcemic episodes with peak calcium values of 2.7 to 3.8 mmol/L ( 10.7 to 15.0 mg/dL ) , patients in the hypercalcemic group exhibited a significant increase in the mean calcium concentration obtained during 6 months before the switch , compared with the mean value obtained during the 7 months of observation after the switch ( 2.4 +/- 0.03 to 2.5 +/- 0.03 mmol/L [ 9.7 +/- 0.2 to 10.2 +/- 0.1 mg/dL ] , P = 0.006 ) .

## Item bc5cdr:test:583
Input:
Sentence: The ED50 doses were 16 mg/kg for i.v .

## Item bc5cdr:test:495
Input:
Sentence: It was concluded that formulations at or below 0.5 per cent CHP may prove acceptable for wound care , but the vehicle system needs pharmaceutical improvement to render it more tolerable and easier to use .

## Item bc5cdr:test:156
Input:
Sentence: Effect of D-Glucarates on basic antibiotic-induced renal damage in rats .

## Item bc5cdr:test:593
Input:
Sentence: routes of administration .

## Item bc5cdr:test:238
Input:
Sentence: injection to rats , abecarnil and diazepam decreased in a time-dependent and dose-related ( 0.25-20 mg/kg i.p . )

## Item bc5cdr:test:241
Input:
Sentence: To better correlate the biochemical and the pharmacological effects , we studied the action of abecarnil on [ 35S ] TBPS binding , exploratory motility and on isoniazid-induced biochemical and pharmacological effects in mice .

## Item bc5cdr:test:303
Input:
Sentence: A case of acute hepatitis induced by zidovudine in a 38-year-old patient with AIDS is presented .

## Item bc5cdr:test:208
Input:
Sentence: The effects of progesterone treatment on bupivacaine arrhythmogenicity in beating rat heart myocyte cultures and on anesthetized rats were determined .

## Item bc5cdr:test:210
Input:
Sentence: Each concentration of progesterone ( 6.25 , 12.5 , 25 , and 50 micrograms/ml ) caused a significant and concentration-dependent reduction in the AD50 for bupivacaine .

## Item bc5cdr:test:400
Input:
Sentence: The relationship between the occurrence of encephalitis and the decrease in microfilaremia is evident .

## Item bc5cdr:test:519
Input:
Sentence: Thus prior dosing with H1- and H2-antagonists provides only partial protection .

## Item bc5cdr:test:408
Input:
Sentence: Because no other factors related to this patient changed significantly , the delirium experienced by this patient possibly resulted from misoprostol therapy .

## Item bc5cdr:test:525
Input:
Sentence: The concentration of GABA was only slightly but significantly decreased in the colliculi without modifications in the other areas .

## Item bc5cdr:test:438
Input:
Sentence: Both cases developed axonal neuropathy with motor predominance in the lower extremities 1 and 6 months after IT chemotherapy was administered .

## Item bc5cdr:test:458
Input:
Sentence: Etiology of hypercalcemia in hemodialysis patients on calcium carbonate therapy .

## Item bc5cdr:test:362
Input:
Sentence: Both cell elements may suffer in common from metabolic disturbance and neurotransmitter dysfunction as occur during massive status epilepticus .

## Item bc5cdr:test:409
Input:
Sentence: Hepatocellular oxidant stress following intestinal ischemia-reperfusion injury .

## Item bc5cdr:test:85
Input:
Sentence: The studies suggest that propranolol is a useful drug in selected patients with severe idiopathic orthostatic hypotension .

## Item bc5cdr:test:567
Input:
Sentence: The mean H concentration during hypotension in the inspiratory gas was 0.7 +/- 0.1 vol % , the mean E concentration 1.6 +/- 0.2 vol % , and the mean I concentration 1.0 +/- 0.1 vol % .

## Item bc5cdr:test:476
Input:
Sentence: The long-term safety of danazol in women with hereditary angioedema .

## Item bc5cdr:test:115
Input:
Sentence: Myopathy due to lack of vitamin E and myopathy induced by certain viruses have much in common anatomically and pathologically with the human form .

## Item bc5cdr:test:393
Input:
Sentence: These cases call attention to possible paranoid exacerbations with serotonin reuptake blockers in select patients and raise neurobiological considerations regarding paranoia .

## Item bc5cdr:test:327
Input:
Sentence: The case of an 11-year-old boy is reported who was known to have Fanconi 's anemia for 3 years and was treated with androgens , corticosteroids and transfusions .

## Item bc5cdr:test:505
Input:
Sentence: infusion of clonazepam ; none had any neurological symptoms .

## Item bc5cdr:test:394
Input:
Sentence: Five cases of encephalitis during treatment of loiasis with diethylcarbamazine .

## Item bc5cdr:test:119
Input:
Sentence: The authors conclude by affirming the undoubted efficacy of the anabolizing steroids in experimental myopathic disease , but they have reservations as to the transfer of the results into the human field , where high dosage can not be carried out continuously because of the effects of the drug on virility ; because the tissue injury too often occurs at an irreversible stage vis-a-vis the `` regeneration '' of the muscle tissue ; and finally because the dystrophic injurious agent is certainly not the lack of vitamin E but something as yet unknown .

## Item bc5cdr:test:301
Input:
Sentence: Two patients with leprosy who developed hemolysis and acute renal failure following rifampin are reported .

## Item bc5cdr:test:419
Input:
Sentence: The lack of a significant increase in products of lipid peroxidation suggests that the oxidant stress is of insufficient magnitude to result in irreversible injury to hepatocyte cell membranes .

## Item bc5cdr:test:613
Input:
Sentence: The hematologic , biochemical and pathologic features indicate a mixed hepatocellular damage due to drug hypersensitivity .

## Item bc5cdr:test:616
Input:
Sentence: We studied mortality after pertussis immunization in the mouse .

## Item bc5cdr:test:544
Input:
Sentence: This is inconsistent with the well-established finding that nifedipine induces tachycardia in normally innervated hearts .

## Item bc5cdr:test:452
Input:
Sentence: Finally , two mechanisms at least , direct vasodilation and flow dependency , are involved in the cromakalim- and pinacidil-induced increase in CxAD .

## Item bc5cdr:test:244
Input:
Sentence: Moreover , 0.05 mg/kg of this beta-carboline reduced markedly the increase of [ 35S ] TBPS binding and the convulsions induced by isoniazid ( 200 mg/kg s.c. ) .

## Item bc5cdr:test:634
Input:
Sentence: Adverse ocular reactions possibly associated with isotretinoin .

## Item bc5cdr:test:205
Input:
Sentence: Vincristine was accidentally given intrathecally to a child with leukaemia , producing sensory and motor dysfunction followed by encephalopathy and death .

## Item bc5cdr:test:568
Input:
Sentence: In addition , the patients received fentanyl and d-tubocurarine .

## Item bc5cdr:test:478
Input:
Sentence: We therefore investigated the long-term safety of danazol by performing a retrospective chart review of 60 female patients with hereditary angioedema treated with danazol for a continuous period of 6 months or longer .

## Item bc5cdr:test:662
Input:
Sentence: Caffeine increased plasma cortisol levels equally in the patient and healthy groups .

## Item bc5cdr:test:231
Input:
Sentence: These effects were completely antagonized by pretreatment with a glutamate/N-methyl-D-aspartate antagonist , aminophosphonovaleric acid .

## Item bc5cdr:test:34
Input:
Sentence: Skin rash is a well-known complication of diphenylhydantoin treatment as is benign and malignant lymphadenopathy .

## Item bc5cdr:test:740
Input:
Sentence: The favorable efficacy and tolerability profiles of these agents make them attractive therapeutic modalities .

## Item bc5cdr:test:498
Input:
Sentence: We report here a retrospective study of 123 children ( median age , 6.5 years ) receiving high-dose busulfan in combined chemotherapy before bone marrow transplantation for malignant solid tumors , brain tumors excluded .

## Item bc5cdr:test:298
Input:
Sentence: Intravascular hemolysis and acute renal failure following intermittent rifampin therapy .
