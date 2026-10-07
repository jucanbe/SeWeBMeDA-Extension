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

## Item bc5cdr:test:1224
Input:
Sentence: By 7 days the vessel was almost restored to normal .

## Item bc5cdr:test:1231
Input:
Sentence: He later recovered normal visual acuity .

## Item bc5cdr:test:74
Input:
Sentence: We conclude that previously reported hypoglycemia , hyperbilirubinemia , polycythemia , neonatal apnea , and bradycardia are not invariable and can not be statistically correlated with chronic propranolol therapy .

## Item bc5cdr:test:1126
Input:
Sentence: The present results suggest a selective involvement of central noradrenergic neurones in the locomotor stimulant effect of amphetamine in the rat .

## Item bc5cdr:test:1014
Input:
Sentence: This change with propranolol sensitivity was calculated as the apparent Ka , this was unchanged by atropine ( 11.7 +/- 2.1 and 10.1 +/- 2.5 ml/ng ) .

## Item bc5cdr:test:1189
Input:
Sentence: We investigated how these two drugs act on the cardiovascular systems of 20 dogs whose hearts had been denervated by a procedure we had devised .

## Item bc5cdr:test:935
Input:
Sentence: Under barbiturate anesthesia , virtually all of the myocardial contractile indices were depressed significantly in barium-exposed rats relative to the corresponding control-fed rats .

## Item bc5cdr:test:743
Input:
Sentence: As the first dihydropyridine available for use in the United States , nifedipine controls angina and hypertension with minimal depression of cardiac function .

## Item bc5cdr:test:1140
Input:
Sentence: Animals surviving for 20 min were immediately stressed by a swim test in 25 degrees C water , and death-producing tonic seizures were scored for 2 min .

## Item bc5cdr:test:1018
Input:
Sentence: This paper reports the results of a study of 50 menopausal women receiving hormonal replacement therapy .

## Item bc5cdr:test:890
Input:
Sentence: Improvement of abnormal EEG was noticed in 76 % of diffuse paroxysms and in 67 % of focal paroxysms .

## Item bc5cdr:test:1171
Input:
Sentence: Massive bleeding appeared during surgery which lasted for six hours .

## Item bc5cdr:test:1333
Input:
Sentence: The two drugs may act synergistically on both the AV node and the peripheral circulation .

## Item bc5cdr:test:947
Input:
Sentence: PPA , 75 mg alone , increased blood pressure ( 31 +/- 14 mm Hg systolic , 20 +/- 5 mm Hg diastolic ) , and propranolol pretreatment antagonized this increase ( 12 +/- 10 mm Hg systolic , 10 +/- 7 mm Hg diastolic ) .

## Item bc5cdr:test:1165
Input:
Sentence: In vivo injection of bepridil at a dose of 5 mg/kg ( i.v . )

## Item bc5cdr:test:1182
Input:
Sentence: In all but 1 patient , antirifampicin antibodies were detected .

## Item bc5cdr:test:1343
Input:
Sentence: She recovered without complications .

## Item bc5cdr:test:968
Input:
Sentence: Using mice derived from a classical F2 and backcross genetic design , a relationship between nicotine-induced seizures and alpha-bungarotoxin nicotinic receptor concentration was found .

## Item bc5cdr:test:988
Input:
Sentence: Other known reasons for seizures were ruled out and the convulsions stopped a few hours after cessation of morphine and did not reoccur in the subsequent 8 months .

## Item bc5cdr:test:1353
Input:
Sentence: Animals became somnolent and none died .

## Item bc5cdr:test:977
Input:
Sentence: BNPP ( 1 to 8 mM ) reduced APAP deacetylation and covalent binding in F344 renal cortical homogenates in a concentration-dependent manner .

## Item bc5cdr:test:970
Input:
Sentence: The binding sites from seizure sensitive and resistant mice were equally affected by treatment with dithiothreitol , trypsin or heat .

## Item bc5cdr:test:969
Input:
Sentence: Mice sensitive to the convulsant effects of nicotine had greater alpha-bungarotoxin binding in the hippocampus than seizure insensitive mice .

## Item bc5cdr:test:1051
Input:
Sentence: Vasopressin as a possible contributor to hypertension .

## Item bc5cdr:test:965
Input:
Sentence: Similar to the remnant kidney model in PAN nephrosis the development of glomerular sclerosis may be related to `` mesangial overloading . ''

## Item bc5cdr:test:1058
Input:
Sentence: However , the role of vasopressin remains to be determined in human essential hypertension .

## Item bc5cdr:test:1286
Input:
Sentence: These changes were maximal in the hour immediately after medications and slowly returned toward base-line levels thereafter .

## Item bc5cdr:test:1212
Input:
Sentence: The pathology specimen contained clinically occult invasive carcinoma of the renal pelvis .

## Item bc5cdr:test:1199
Input:
Sentence: The Dimer-X group had a higher incidence of nausea and dizziness .

## Item bc5cdr:test:1111
Input:
Sentence: A significant increase in the myocardial t1/2 of the I-131 HA was observed only at a higher cumulative dose , 10 mg/kg .

## Item bc5cdr:test:1219
Input:
Sentence: Medial changes in arterial spasm induced by L-norepinephrine .

## Item bc5cdr:test:983
Input:
Sentence: It is concluded that PAP formation , in vivo , accounts , at least in part , for APAP-induced renal tubular necrosis .

## Item bc5cdr:test:1251
Input:
Sentence: Skeletal movements occurred in 50 % of patients ; 30 % experienced respiratory upset , one sufficiently severe to necessitate abandoning the technique .

## Item bc5cdr:test:1124
Input:
Sentence: However , the increased rearings and the amphetamine-induced stereotypies were not blocked by pretreatment with DSP4 .

## Item bc5cdr:test:1038
Input:
Sentence: Aza patients had significantly more staphylococcal infections than all other transplant groups ( P less than 0.005 ) , and systemic fungal infections occurred only in the liver transplant group .

## Item bc5cdr:test:1287
Input:
Sentence: These results suggest that the renal protective effects of misoprostol is dose-dependent .

## Item bc5cdr:test:1446
Input:
Sentence: A new model to test potential protectors .

## Item bc5cdr:test:1456
Input:
Sentence: plus 2 weeks of observation ) .

## Item bc5cdr:test:1010
Input:
Sentence: The effects on isoproterenol tachycardia were determined before and after atropine ( 0.04 mg/kg IV ) .

## Item bc5cdr:test:809
Input:
Sentence: Eighty patients who were to receive CYA 50 mg/kg/d for four days as preparation for marrow grafting underwent a total of 84 transplants for aplastic anemia , Wiskott-Aldrich syndrome , or severe combined immunodeficiency syndrome .

## Item bc5cdr:test:1310
Input:
Sentence: We conclude that cardiac pacing during resuscitative efforts in pediatric patients suffering from acute myocardial dysfunction may not have long-term value in and of itself ; however , if temporary hemodynamic stability is achieved by this procedure , it may provide additional time needed to institute other therapeutic modalities .

## Item bc5cdr:test:932
Input:
Sentence: Barium-supplemented Long-Evans hooded rats were characterized by a persistent hypertension that was evident after 1 month of barium ( 100 micrograms/ml mineral fortified water ) treatment .

## Item bc5cdr:test:1035
Input:
Sentence: Renal patients on cyclosporine had the fewest bacteremias .

## Item bc5cdr:test:1336
Input:
Sentence: and 15.0 ( 10.2-23.7 ) mg/kg , p.o. , respectively , while that of flunarizine was 34.0 ( 26.0-44.8 ) mg/kg , p.o .

## Item bc5cdr:test:1350
Input:
Sentence: RESULTS : In group 1 , animals received cocaine followed by vehicle .

## Item bc5cdr:test:1484
Input:
Sentence: A series of six cases .

## Item bc5cdr:test:926
Input:
Sentence: Low doses of pilocarpine caused a pronounced enhancement of the catalepsy that was induced by the dopaminergic blocker , haloperidol .

## Item bc5cdr:test:1032
Input:
Sentence: The randomized Aza patients had more overall infections ( P less than 0.05 ) and more nonviral infections ( P less than 0.02 ) than the randomized cyclosporine patients .

## Item bc5cdr:test:1373
Input:
Sentence: Assessment of cardiomyocyte DNA synthesis during hypertrophy in adult mice .

## Item bc5cdr:test:941
Input:
Sentence: Overall , the altered cardiac contractility and excitability characteristics , the myocardial metabolic disturbances , and the hypersensitivity of the cardiovascular system to sodium pentobarbital suggest the existence of a heretofore undescribed cardiomyopathic disorder induced by chronic barium exposure .

## Item bc5cdr:test:1054
Input:
Sentence: Administration of DDAVP which has antidiuretic action but minimal vasopressor effect failed to increase blood pressure to the levels observed after administration of AVP .

## Item bc5cdr:test:1214
Input:
Sentence: Twenty carcinomas of the urinary bladder and one carcinoma of the prostate have been reported in association with its use .

## Item bc5cdr:test:1069
Input:
Sentence: Alternating sinus rhythm and intermittent sinoatrial block induced by propranolol .

## Item bc5cdr:test:943
Input:
Sentence: Propranolol antagonism of phenylpropanolamine-induced hypertension .

## Item bc5cdr:test:1427
Input:
Sentence: Thorough bacteriological screening failed to provide evidence of infection .

## Item bc5cdr:test:1104
Input:
Sentence: Repeated doses of edrophonium to 70 mg and neostigmine to 2.5 mg did not antagonize or augment the block .

## Item bc5cdr:test:1549
Input:
Sentence: Two subsequent CO2-rebreathing tests were performed in healthy young volunteers .

## Item bc5cdr:test:1274
Input:
Sentence: Paclitaxel 3-hour infusion given alone and combined with carboplatin : preliminary results of dose-escalation trials .

## Item bc5cdr:test:1415
Input:
Sentence: No patient was disabled and no lymphoproliferative disorder was observed .

## Item bc5cdr:test:798
Input:
Sentence: Of 158 asthmatic patients who were placed on inhaled beclomethasone , 15 ( 9.5 % ) developed either hoarseness ( 8 ) , oral thrush ( 6 ) , or both ( 1 ) .

## Item bc5cdr:test:1554
Input:
Sentence: The CO2-response curves for the two tests were compared within the same subject .

## Item bc5cdr:test:804
Input:
Sentence: Concomitant use of oral prednisone and topical beclomethasone may increase the risk of developing hoarseness or candidiasis .

## Item bc5cdr:test:1297
Input:
Sentence: Three young infants , all of birth weight < 1,500 g , experienced myoclonus following the intravenous administration of lorazepam .

## Item bc5cdr:test:1460
Input:
Sentence: The results indicate that this new model is very sensitive and enables monitoring of the development of cardiotoxicity with time .

## Item bc5cdr:test:1163
Input:
Sentence: In vitro perfusion of bepridil in the life-support medium for isolated sino-atrial tissue from rabbit heart , caused a reduction in action potential ( AP ) spike frequency ( recorded by KCl microelectrodes ) starting at doses of 5 X 10 ( -6 ) M. This effect was dose-dependent up to concentrations of 5 X 10 ( -5 ) M , whereupon blockade of sinus activity set in .

## Item bc5cdr:test:1264
Input:
Sentence: The one case of toxic epidermal necrolysis occurred in a patient who took cephalexin .

## Item bc5cdr:test:1317
Input:
Sentence: There was a statistically longer time to first episode of nausea ( P = .0015 ) and vomiting ( P = .0001 ) , and fewer patients were administered additional antiemetic medication in the 10-micrograms/kg dosing groups than in the 5-micrograms/kg dosing group .

## Item bc5cdr:test:1369
Input:
Sentence: SOD did not attenuate the tubular damage .

## Item bc5cdr:test:1113
Input:
Sentence: Our findings suggest that the changes leading to an alteration of myocardial dynamic imaging with I-131 HA are not the initiating factor in doxorubicin cardiotoxicity .

## Item bc5cdr:test:1613
Input:
Sentence: Grade 3/4 nonhematologic toxicities were uncommon .

## Item bc5cdr:test:1169
Input:
Sentence: Hepatitis and renal tubular acidosis after anesthesia with methoxyflurane .

## Item bc5cdr:test:1342
Input:
Sentence: The patient had no history of underlying ischaemic heart disease or Prinzmetal 's angina .

## Item bc5cdr:test:994
Input:
Sentence: Intravenous inoculation of 4.2 x 10 ( 10 ) to 7.8 x 10 ( 10 ) pyocin type 6 Pseudomonas organisms in monkeys given vincristine sulfate 4 days previously resulted in fatal infection in 11 of 14 monkeys , whereas none of four receiving Pseudomonas alone died .

## Item bc5cdr:test:1503
Input:
Sentence: Only 5 of the 160 F2 pituitaries exhibited the hemorrhagic phenotype ; 36 of the 160 F2 pituitaries were in the F344 range of mass , but 31 of these were not hemorrhagic , indicating that the hemorrhagic phenotype is not merely a consequence of extensive growth .

## Item bc5cdr:test:1506
Input:
Sentence: Immunocytochemical techniques were used to examine alterations in the expression of neuronal nitric oxide synthase ( NOS ) in bladder pathways following acute and chronic irritation of the urinary tract of the rat .

## Item bc5cdr:test:1207
Input:
Sentence: The abolition of muscle fasciculations ( by 0.075mg/kg dose of Fazadinium ) did not influence the occurrence of scoline pain .

## Item bc5cdr:test:1396
Input:
Sentence: An adverse drug interaction with piroxicam , which she took occasionally , may have exacerbated the coagulopathy .

## Item bc5cdr:test:1691
Input:
Sentence: The incidence of intubation was similar .

## Item bc5cdr:test:928
Input:
Sentence: Intracranial injection of an acetylcholine-synthesis inhibitor , hemicholinium , prevented the catalepsy that is usually induced by haloperidol .

## Item bc5cdr:test:1411
Input:
Sentence: Cytomegalovirus infections were treated successfully with ganciclovir in 11 patients .

## Item bc5cdr:test:1419
Input:
Sentence: The correlation between high serum tricyclic antidepressant concentrations and central nervous system side effects has been well established .

## Item bc5cdr:test:1046
Input:
Sentence: The analogues CCK-8-SE and CCK-8-NS ( dose range 0.2-6.4 mumol/kg ) and caerulein dose range 0.1-0.8 mumol/kg ) showed bell-shaped dose-effect curves , with the greatest maximum inhibition for CCK-8-NS .

## Item bc5cdr:test:1563
Input:
Sentence: Forty-two Chinese HBsAg carriers were randomized to receive placebo ( 6 patients ) or lamivudine orally in dosages of 25 mg , 100 mg , or 300 mg daily ( 12 patients for each dosage ) .

## Item bc5cdr:test:1036
Input:
Sentence: Analysis of site of infection showed a preponderance of abdominal infections in liver patients , intrathoracic infections in heart patients , and urinary tract infections in renal patients .

## Item bc5cdr:test:1713
Input:
Sentence: Maximum blood loss was greatest at the upper and lower dose levels , and lowest in the 70-125 microg dose range .

## Item bc5cdr:test:1714
Input:
Sentence: Four out of six cases with blood loss > or = 1000 ml occurred in the 200 microg group .

## Item bc5cdr:test:1122
Input:
Sentence: Male rats received the noradrenaline neurotoxin DSP4 ( 50 mg/kg ) 7 days prior to injection of D-amphetamine ( 10 or 40 mumol/kg i.p . ) .

## Item bc5cdr:test:1725
Input:
Sentence: The calculi are not opaque , and secondary signs of obstruction may be absent or minimal and should be sought carefully .

## Item bc5cdr:test:1365
Input:
Sentence: Administration of GM at 40 mg/kg sc for 13 days to rats induced a significant reduction in renal blood flow ( RBF ) and inulin clearance ( CIn ) as well as marked tubular damage .

## Item bc5cdr:test:1355
Input:
Sentence: Animals became somnolent after diazepam and then active after flumazenil administration .

## Item bc5cdr:test:1616
Input:
Sentence: Plasma paclitaxel concentrations were measured at the completion of paclitaxel infusion and at 24 hours in 19 patients .

## Item bc5cdr:test:1625
Input:
Sentence: Neither ECG [ sinus-cycle length ( SCL ) , QT or QTc interval , or U wave ] nor clinical parameters identified patients at risk for torsades de pointes .

## Item bc5cdr:test:1628
Input:
Sentence: During follow-up , seven ( 20 % ) patients had a nonfatal ventricular tachycardia recurrence , and two ( 6 % ) patients died suddenly .

## Item bc5cdr:test:1380
Input:
Sentence: Central cardiovascular effects of AVP and ANP in normotensive and spontaneously hypertensive rats .

## Item bc5cdr:test:1689
Input:
Sentence: Symptomatic hypokalemia did not occur .

## Item bc5cdr:test:1690
Input:
Sentence: CNA patients had higher heart rates during treatment , which may reflect severity of illness .

## Item bc5cdr:test:1291
Input:
Sentence: Angiotensin-converting enzyme ( ACE ) inhibitors , used to treat hypertension and congestive heart failure , were introduced in Europe in the middle of the eighties , and the use of these drugs has increased progressively .

## Item bc5cdr:test:1400
Input:
Sentence: Patients were managed with cyclosporine and azathioprine .

## Item bc5cdr:test:1705
Input:
Sentence: CONCLUSIONS : In humans , the intracoronary infusion of cocaine sufficient in amount to achieve a high drug concentration in coronary sinus blood causes a deterioration of LV systolic and diastolic performance .

## Item bc5cdr:test:1541
Input:
Sentence: Co-administration of nefiracetam and apomorphine during training or 10h thereafter produced no significant anti-amnesic effect .
