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

## Item bc5cdr:test:2897
Example input:
Sentence: While she was weak , 2-Hz repetitive stimulation revealed a decrement without significant facilitation at rapid rates or after exercise , suggesting postsynaptic neuromuscular blockade .

Example answer:
{"entities": [{"text": "postsynaptic neuromuscular blockade", "type": "Disease"}]}

Example input:
Sentence: They showed significantly more rapid improvement of motor function in the first week following hemorrhage and better memory retention in the passive avoidance test .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "Disease"}]}

Example input:
Sentence: Both patients recovered quickly after stopping glyburide therapy and have remained well for a follow-up period of 1 year .

Example answer:
{"entities": [{"text": "glyburide", "type": "Chemical"}]}

Example input:
Sentence: This 4-week cycle was repeated until there was evidence of excessive toxicity or disease progression .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Recurrence was studied in 82 evaluable patients after 1 year of follow-up and in 72 patients followed for 2-3 years ( mean 32 months ) .

Example answer:
{"entities": []}

Example input:
Sentence: Motor behavior , passive avoidance , and skilled forelimb function were tested repeatedly for six weeks .

Example answer:
{"entities": []}

Example input:
Sentence: Symptoms persisted for three months despite TAC dose reduction , administration of IVIG and four doses of methylprednisolone pulse therapy .

Example answer:
{"entities": [{"text": "TAC", "type": "Chemical"}, {"text": "methylprednisolone", "type": "Chemical"}]}

Example input:
Sentence: Initial testing in a time-dependent forgetting task employing a 24-h delay between training and testing showed that metrifonate improved object recognition ( at 10 and 30 mg/kg , p.o .

Example answer:
{"entities": [{"text": "metrifonate", "type": "Chemical"}]}

Example input:
Sentence: After 2 weeks of treatment , patients tested 5-8 h after the last dose of medication did not show any decrement of performance .

Example answer:
{"entities": []}

Example input:
Sentence: Significant declines in simple and sustained attention , working memory , and verbal memory were observed at 1 hour postdose compared to baseline for both age groups with a trend toward return to baseline by 5 hours postdose .

Example answer:
{"entities": []}

Input:
Sentence: This learning decrement persisted up to the last follow-up 4 weeks post-training .

## Item bc5cdr:test:2904
Example input:
Sentence: At termination of the experiments , mice underwent echocardiography , quantitation of abundance of molecular markers of CM ( ventricular mRNA encoding atrial natriuretic factor [ ANF ] and sarcoplasmic calcium ATPase [ SERCA2 ] ) , and determination of plasma LA .

Example answer:
{"entities": [{"text": "CM", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "LA", "type": "Chemical"}]}

Example input:
Sentence: Reactive oxygen species have been implicated in the pathogenesis of acute puromycin aminonucleoside ( PAN ) -induced nephropathy , with antioxidants significantly reducing the proteinuria .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: Neutropenia grade greater than or equal to 3 was seen in 15 patients , infections with recovery in 3 , and grand mal seizures in 1 patient .

Example answer:
{"entities": [{"text": "Neutropenia", "type": "Disease"}, {"text": "infections", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: World Health Organization Grade 3-4 neutropenia and thrombocytopenia occurred in 39.9 % and 11.4 % of patients , respectively .

Example answer:
{"entities": [{"text": "neutropenia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Immunofluorescence staining with the MRP2 antibody was found to label a high number of microvessels throughout the brain in normal Wistar rats , whereas such labeling was absent in TR ( - ) rats .

Example answer:
{"entities": []}

Example input:
Sentence: Severe hematologic toxicity ( neutrophil count < 1000/mm3 and/or hemoglobin < 8 g/dl ) occurred in 4 patients assigned to group I and 7 assigned to group II .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: A literature review revealed no prior reports of pericarditis in anti-MPO pANCA-positive vasculitis associated with propylthio- uracil therapy .

Example answer:
{"entities": [{"text": "pericarditis", "type": "Disease"}, {"text": "vasculitis", "type": "Disease"}, {"text": "propylthio- uracil", "type": "Chemical"}]}

Example input:
Sentence: The serum of six affected workers and five controls was tested for autoantibodies that react with human liver cytochrome-P450 2E1 ( P450 2E1 ) and P58 protein disulphide isomerase isoform ( P58 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Propylthiouracil-induced perinuclear-staining antineutrophil cytoplasmic autoantibody-positive vasculitis in conjunction with pericarditis .

Example answer:
{"entities": [{"text": "Propylthiouracil-induced", "type": "Chemical"}, {"text": "vasculitis", "type": "Disease"}, {"text": "pericarditis", "type": "Disease"}]}

Example input:
Sentence: Serologic evaluation revealed the presence of perinuclear-staining antineutrophil cytoplasmic autoantibodies ( pANCA ) against myeloperoxidase ( MPO ) .

Example answer:
{"entities": []}

Input:
Sentence: Neither myeloperoxidase- nor proteinase-3-antineutrophil cytoplasmic antibody was positive .

## Item bc5cdr:test:2571
Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: A case of triamterene nephrolithiasis is reported in a man after 4 years of hydrochlorothiazide-triamterene therapy for hypertension .

Example answer:
{"entities": [{"text": "triamterene", "type": "Chemical"}, {"text": "nephrolithiasis", "type": "Disease"}, {"text": "hydrochlorothiazide-triamterene", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: He was hospitalized for a myocardial infarction with pulmonary edema , treated with high-dose diuretics .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "pulmonary edema", "type": "Disease"}]}

Example input:
Sentence: Increased frequency of venous thromboembolism with the combination of docetaxel and thalidomide in patients with metastatic androgen-independent prostate cancer .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "docetaxel", "type": "Chemical"}, {"text": "thalidomide", "type": "Chemical"}, {"text": "prostate cancer", "type": "Disease"}]}

Example input:
Sentence: A 54-year-old hypothyroid male taking thyroxine and simvastatin presented with bilateral leg compartment syndrome and myonecrosis .

Example answer:
{"entities": [{"text": "hypothyroid", "type": "Disease"}, {"text": "thyroxine", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "compartment syndrome", "type": "Disease"}, {"text": "myonecrosis", "type": "Disease"}]}

Example input:
Sentence: The patient was admitted to the hospital , anticoagulated with unfractionated heparin , and given intravenous diltiazem for rate control and intravenous amiodarone for rate and rhythm control .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}]}

Example input:
Sentence: Three months later the patient was exposed to a single dose of metoprolol , diltiazem , propafenone ( since he had received this drug in the past ) , and sparteine ( as a probe for the debrisoquine/sparteine type polymorphism of oxidative drug metabolism ) .

Example answer:
{"entities": [{"text": "metoprolol", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "propafenone", "type": "Chemical"}, {"text": "sparteine", "type": "Chemical"}, {"text": "debrisoquine/sparteine", "type": "Chemical"}]}

Example input:
Sentence: We report a woman with coronary artery disease who developed a markedly prolonged QT interval and torsades de pointes ( TdP ) after taking ketoconazole for treatment of fungal infection .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "prolonged QT interval", "type": "Disease"}, {"text": "torsades de pointes", "type": "Disease"}, {"text": "TdP", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "fungal infection", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : The addition of thalidomide to docetaxel in the treatment of prostate cancer significantly increases the frequency of VTE .

Example answer:
{"entities": [{"text": "thalidomide", "type": "Chemical"}, {"text": "docetaxel", "type": "Chemical"}, {"text": "prostate cancer", "type": "Disease"}, {"text": "VTE", "type": "Disease"}]}

Example input:
Sentence: Pneumonitis , bilateral pleural effusions , echocardiographic evidence of cardiac tamponade , and positive autoantibodies developed in a 43-year-old man , who was receiving long-term sulfasalazine therapy for chronic ulcerative colitis .

Example answer:
{"entities": [{"text": "Pneumonitis", "type": "Disease"}, {"text": "pleural effusions", "type": "Disease"}, {"text": "cardiac tamponade", "type": "Disease"}, {"text": "sulfasalazine", "type": "Chemical"}, {"text": "ulcerative colitis", "type": "Disease"}]}

Input:
Sentence: ST elevation with chest discomfort disappeared since he began taking long-acting diltiazem .

## Item bc5cdr:test:2574
Example input:
Sentence: The selective 5-HT6 receptor antagonist Ro4368554 restores memory performance in cholinergic and serotonergic models of memory deficiency in the rat .

Example answer:
{"entities": [{"text": "Ro4368554", "type": "Chemical"}, {"text": "memory deficiency", "type": "Disease"}]}

Example input:
Sentence: Effects of 5-HT1B receptor ligands microinjected into the accumbal shell or core on the cocaine-induced locomotor hyperactivity in rats .

Example answer:
{"entities": [{"text": "cocaine-induced", "type": "Chemical"}, {"text": "locomotor hyperactivity", "type": "Disease"}]}

Example input:
Sentence: They suggest that , in normal conscious rats , the central tachycardia of bromocriptine appears to predominate and to mask the bradycardia of this agonist at peripheral dopamine D2 receptors .

Example answer:
{"entities": [{"text": "tachycardia", "type": "Disease"}, {"text": "bromocriptine", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: These results indicate that noradrenergic neurons have an important role in the manifestation of catalepsy induced by THC , whereas dopaminergic neurons are important in catalepsy induced by haloperidol .

Example answer:
{"entities": [{"text": "catalepsy", "type": "Disease"}, {"text": "THC", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Animal studies suggest that incontinence secondary to serotonergic antidepressants could be mediated by the 5HT4 receptors found on the bladder .

Example answer:
{"entities": [{"text": "incontinence", "type": "Disease"}, {"text": "serotonergic antidepressants", "type": "Chemical"}]}

Example input:
Sentence: The present study sought to characterize the cognitive-enhancing effects of the 5-HT ( 6 ) antagonist Ro4368554 ( 3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole ) in a rat object recognition task employing a cholinergic ( scopolamine pretreatment ) and a serotonergic- ( tryptophan ( TRP ) depletion ) deficient model , and compared its pattern of action with that of the acetylcholinesterase inhibitor metrifonate .

Example answer:
{"entities": [{"text": "5-HT", "type": "Chemical"}, {"text": "Ro4368554", "type": "Chemical"}, {"text": "3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole", "type": "Chemical"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "tryptophan", "type": "Chemical"}, {"text": "TRP", "type": "Chemical"}, {"text": "metrifonate", "type": "Chemical"}]}

Example input:
Sentence: does not antagonize the reserpine hypothermia in mice and does not potentiate the 5-hydroxytryptophan head twitches in rats .

Example answer:
{"entities": [{"text": "reserpine", "type": "Chemical"}, {"text": "hypothermia", "type": "Disease"}, {"text": "5-hydroxytryptophan", "type": "Chemical"}]}

Example input:
Sentence: The present study was designed to examine the effect of 5-HT1B receptor ligands microinjected into the subregions of the nucleus accumbens ( the shell and the core ) on the locomotor hyperactivity induced by cocaine in rats .

Example answer:
{"entities": [{"text": "locomotor hyperactivity", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Antagonists at serotonin type 6 ( 5-HT ( 6 ) ) receptors show activity in models of learning and memory .

Example answer:
{"entities": [{"text": "serotonin", "type": "Chemical"}, {"text": "5-HT", "type": "Chemical"}]}

Example input:
Sentence: Dopamine D2 receptors were elevated in the striatum , whereas serotonin 2C , but not serotonin 1A , receptors were elevated in the orbital frontal cortex .

Example answer:
{"entities": [{"text": "Dopamine", "type": "Chemical"}, {"text": "serotonin", "type": "Chemical"}]}

Input:
Sentence: RATIONALE : 5-Hydroxytryptamine , via stimulation of 5-HT 2C receptors , exerts a tonic inhibitory influence on dopaminergic neurotransmission , whereas activation of 5-HT 2A receptors enhances stimulated DAergic neurotransmission .

## Item bc5cdr:test:2914
Example input:
Sentence: Of the patients developing one or more recurrences during the first year , only 50 % presented with further recurrence once the instillations were stopped .

Example answer:
{"entities": []}

Example input:
Sentence: All 20 patients responded to this regimen , 16/20 ( 80 % ) achieved a complete remission , and 20 % obtained a partial remission .

Example answer:
{"entities": []}

Example input:
Sentence: Eleven patients ( six male ) with median age 47 years ( range 27-73 ) , median disease duration 50 months ( range 9-178 ) and median follow-up period of patients 13.8 months ( range 5-27 ) were enrolled in this study .

Example answer:
{"entities": []}

Example input:
Sentence: The median duration of survival in the 12 patients was 54 weeks ( range 21 to more than 156 weeks ) , with an 18-month survival rate of 42 % .

Example answer:
{"entities": []}

Example input:
Sentence: Of 24 evaluable patients , two achieved a complete remission and one achieved a partial remission for an overall response rate of 12.5 % ( 95 % confidence interval : 2.6-32.4 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: After a median follow-up of 22 months , the median progression free survival rate was 7 months , and the median survival time was 16 months .

Example answer:
{"entities": []}

Example input:
Sentence: The median follow-up period was 14 months .

Example answer:
{"entities": []}

Example input:
Sentence: In patients that were free of recurrence during the first year , 80 % remained tumor-free during the 2- to 3-year follow-up period .

Example answer:
{"entities": [{"text": "tumor-free", "type": "Disease"}]}

Example input:
Sentence: Of the 82 evaluable patients , 50 did not show any recurrence after 1 year ( 61 % ) , while 32 presented with one or more recurrences ( 39 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Recurrence was studied in 82 evaluable patients after 1 year of follow-up and in 72 patients followed for 2-3 years ( mean 32 months ) .

Example answer:
{"entities": []}

Input:
Sentence: RESULTS : At a median follow-up of 14.1 months , the overall recurrence rate in the 51 patients was 3.9 % ( 2/51 ) .

## Item bc5cdr:test:2915
Example input:
Sentence: Patients developing ESRD had a 6-year survival after onset of ESRD of 27 % for the patients receiving hemodialysis versus 71.4 % for the patients developing ESRD who subsequently received kidney transplants .

Example answer:
{"entities": [{"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Median progression-free survival was 5 months .

Example answer:
{"entities": []}

Example input:
Sentence: A complete responder had relapse-free survival up to 17 months .

Example answer:
{"entities": []}

Example input:
Sentence: Of 24 evaluable patients , two achieved a complete remission and one achieved a partial remission for an overall response rate of 12.5 % ( 95 % confidence interval : 2.6-32.4 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Median survival was 16 months .

Example answer:
{"entities": []}

Example input:
Sentence: After a median follow-up of 22 months , the median progression free survival rate was 7 months , and the median survival time was 16 months .

Example answer:
{"entities": []}

Example input:
Sentence: It was `` serious '' for almost 2/3 of the patients ( 62.5 % ) and its outcome favourable in most of the cases ( 82 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: The median time to progression was 16 weeks and the 1-year survival rate was 33 % .

Example answer:
{"entities": []}

Example input:
Sentence: Overall survival from the time of OLTX was not significantly different among groups , but by year 13 , the survival of the patients who had ESRD was only 28.2 % compared with 54.6 % in the control group .

Example answer:
{"entities": [{"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: The median duration of survival in the 12 patients was 54 weeks ( range 21 to more than 156 weeks ) , with an 18-month survival rate of 42 % .

Example answer:
{"entities": []}

Input:
Sentence: The overall patient survival was 88.3 % , and 82.4 % after 1 and 2 years , respectively .

## Item bc5cdr:test:2652
Example input:
Sentence: Although the AE RBCs from an individual not taking dapsone had increased incubated Heinz body formation , the GSH content and GSH stability were normal .

Example answer:
{"entities": [{"text": "dapsone", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}]}

Example input:
Sentence: together for 30 consecutive days and challenged with ISO on the day 29th and 30th , showed a significant ( P < 0.05 ) decrease in heart weight , serum marker enzymes , lipid peroxidation , Ca+2 ATPase and a significant increase in the body weight , endogenous antioxidants , Na+/K+ ATPase and Mg+2 ATPase when compared with ISO treated group and green tea or vitamin E alone treated groups .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}, {"text": "green tea", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: Seizures induced by hexafluorodiethyl ether ( HFDE ) were also found to be a more sensitive measure of protection by CBZ than seizures induced by maximal electroshock ( MES ) .

Example answer:
{"entities": [{"text": "Seizures", "type": "Disease"}, {"text": "hexafluorodiethyl ether", "type": "Chemical"}, {"text": "HFDE", "type": "Chemical"}, {"text": "CBZ", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Using functional magnetic resonance imaging ( fMRI ) in normal volunteers , we studied the gabapentin-induced modulation of brain activity in response to nociceptive mechanical stimulation of normal skin and capsaicin-induced secondary hyperalgesia .

Example answer:
{"entities": [{"text": "gabapentin-induced", "type": "Chemical"}, {"text": "capsaicin-induced", "type": "Chemical"}, {"text": "secondary hyperalgesia", "type": "Disease"}]}

Example input:
Sentence: The present study was designed to evaluate two endogenous and one synthetic neuroactive steroid that positively modulate the gamma-aminobutyric acid ( GABA ( A ) ) receptor against the increase in sensitivity to the convulsant effects of cocaine engendered by repeated cocaine administration ( seizure kindling ) .

Example answer:
{"entities": [{"text": "steroid", "type": "Chemical"}, {"text": "gamma-aminobutyric acid", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Gamma-hexachlorocyclohexane ( gamma-HCH ) , the active ingredient of the insecticide lindane , has been shown to decrease seizure threshold to pentylenetrazol ( PTZ ) 3 h after exposure to gamma-HCH and conversely increase threshold to PTZ-induced seizures 24 h after exposure to gamma-HCH ( Vohland et al .

Example answer:
{"entities": [{"text": "Gamma-hexachlorocyclohexane", "type": "Chemical"}, {"text": "gamma-HCH", "type": "Chemical"}, {"text": "lindane", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "PTZ", "type": "Chemical"}, {"text": "PTZ-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: The first ultrastructural changes in structural elements of the blood-brain-barrier ( BBB ) in the cerebellar cortex were detectable after 3 months of the experiment .

Example answer:
{"entities": []}

Example input:
Sentence: In both ecstasy and cannabis groups brain activation was decreased in the right medial frontal gyrus , left parahippocampal gyrus , left dorsal cingulate gyrus , and left caudate .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}, {"text": "cannabis", "type": "Chemical"}]}

Example input:
Sentence: In the course of developing this model , a common vehicle , propylene glycol , by itself in high doses , was found to exhibit protective properties against induced seizures and inhibited weight gain .

Example answer:
{"entities": [{"text": "propylene glycol", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}]}

Input:
Sentence: Evans Blue ( mug g-1 of brain tissue ) was greater in the 90/HTN group ( 24.4 +/- 6.0 ) versus the control group ( 12.3 +/- 4.1 ) , which was in turn greater than the 15/HTN group ( 7.3 +/- 3.2 ) .

## Item bc5cdr:test:2840
Example input:
Sentence: Furthermore , our data suggest that TR ( - ) rats are an interesting tool to study consequences of overexpression of Pgp in the BBB on access of drugs in the brain , without the need of inducing seizures or other Pgp-enhancing events for this purpose .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: HS diet for 4 wk caused a progressive increase in BP , protein and albumin excretion , and glomerular sclerosis in male DS rats , which were attenuated by castration .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : The data on TR ( - ) rats indicate that Pgp plays an important role in the compensation of MRP2 deficiency in the BBB .

Example answer:
{"entities": []}

Example input:
Sentence: In the five rats that developed somatic rigidity , ICP and CVP increased significantly above baseline ( delta ICP 7.5 +/- 1.0 mmHg , delta CVP 5.9 +/- 1.3 mmHg ) .

Example answer:
{"entities": [{"text": "somatic rigidity", "type": "Disease"}]}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "a reduced locomotor activity", "type": "Disease"}]}

Example input:
Sentence: Untreated group 3 rats exhibited a progressive reduction in GFR ( 0.35 +/- 0.08 ml/min at 4 months , 0.27 +/- 0.07 ml/min at 6 months ) .

Example answer:
{"entities": []}

Example input:
Sentence: TR ( - ) rats exhibited a significant up-regulation of Pgp in brain capillary endothelial cells compared with wild-type controls .

Example answer:
{"entities": []}

Example input:
Sentence: These results suggest that dehydration and/or the activation of visceral afferent inputs may contribute to the elevation of plasma AVP and the upregulation of AVP gene expression in the PVN and the SON of the Li-induced diabetes insipidus rat .

Example answer:
{"entities": [{"text": "dehydration", "type": "Disease"}, {"text": "AVP", "type": "Chemical"}, {"text": "Li-induced", "type": "Chemical"}, {"text": "diabetes insipidus", "type": "Disease"}]}

Example input:
Sentence: Plasma concentration of AVP and transcripts of AVP gene in the PVN and SON were significantly increased in the Li-treated rats compared with controls .

Example answer:
{"entities": [{"text": "AVP", "type": "Chemical"}, {"text": "Li-treated", "type": "Chemical"}]}

Input:
Sentence: The greater LV hypertrophy in TGR rats was associated with more pronounced downregulation of beta-AR and upregulation of LV beta-AR kinase-1 mRNA levels compared with those in SD rats .

## Item bc5cdr:test:2602
Example input:
Sentence: Although most cases of antibiotic induced acute interstitial nephritis are benign and self-limited , some patients are at risk for permanent renal injury .

Example answer:
{"entities": [{"text": "interstitial nephritis", "type": "Disease"}, {"text": "renal injury", "type": "Disease"}]}

Example input:
Sentence: Irreversible damage to the medullary interstitium in experimental analgesic nephropathy in F344 rats .

Example answer:
{"entities": [{"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: Five of 33 ( 15 % ) of the tobramycin-treated patients and 16 of 29 ( 55.2 % ) of the gentamicin-treated patients had renal failure .

Example answer:
{"entities": [{"text": "tobramycin-treated", "type": "Chemical"}, {"text": "gentamicin-treated", "type": "Chemical"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: Doxorubicin-induced nephropathy leads to epithelial sodium channel ( ENaC ) -dependent volume retention and renal fibrosis .

Example answer:
{"entities": [{"text": "Doxorubicin-induced", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "sodium", "type": "Chemical"}, {"text": "volume retention", "type": "Disease"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: Baseline renal ACE positively correlated with the relative rise in proteinuria after adriamycin ( r = 0.62 , P < 0.01 ) , renal interstitial alpha-smooth muscle actin ( r = 0.49 , P < 0.05 ) , interstitial macrophage influx ( r = 0.56 , P < 0.05 ) , interstitial collagen III ( r = 0.53 , P < 0.05 ) , glomerular alpha-smooth muscle actin ( r = 0.74 , P < 0.01 ) and glomerular desmin ( r = 0.48 , P < 0.05 ) .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: Two patients developed acute tubular necrosis , characterized clinically by acute oliguric renal failure , while they were receiving a combination of cephalothin sodium and gentamicin sulfate therapy .

Example answer:
{"entities": [{"text": "acute tubular necrosis", "type": "Disease"}, {"text": "cephalothin sodium", "type": "Chemical"}, {"text": "gentamicin sulfate", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : As anticipated , adriamycin elicited nephrotic range proteinuria , renal interstitial damage and mild focal glomerulosclerosis .

Example answer:
{"entities": [{"text": "adriamycin", "type": "Chemical"}, {"text": "nephrotic", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "renal interstitial damage", "type": "Disease"}, {"text": "focal glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: In this study , 62 patients with confirmed initial normal renal function and treated with 2 to 5 mg/kg/day of gentamicin sulfate or tobramycin sulfate for a minimum of seven days were followed up prospectively for the development of aminoglycoside-related renal failure , defined as at least a one-third reduction in renal function .

Example answer:
{"entities": [{"text": "gentamicin sulfate", "type": "Chemical"}, {"text": "tobramycin sulfate", "type": "Chemical"}, {"text": "aminoglycoside-related", "type": "Chemical"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: Thus , gentamicin was associated with renal failure more than three times as often as was tobramycin .

Example answer:
{"entities": [{"text": "gentamicin", "type": "Chemical"}, {"text": "renal failure", "type": "Disease"}, {"text": "tobramycin", "type": "Chemical"}]}

Input:
Sentence: BACKGROUND : Animals treated with gentamicin can show residual areas of interstitial fibrosis in the renal cortex .

## Item bc5cdr:test:2847
Example input:
Sentence: Clinical tolerability of both agents has been good , with fewer than 3 % of patients withdrawn from treatment because of clinical adverse experiences .

Example answer:
{"entities": []}

Example input:
Sentence: Moderate or severe adverse events were more common in subjects on clonidine ( 79.4 % versus 49.2 % ; p =.0006 ) but not associated with higher rates of early study withdrawal .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: This is a case report of euphoria and choreoathetoid movements both transiently induced by rapid adjustment to the selective mu-opioid receptor agonist methadone in an inpatient previously abusing heroine and cocaine .

Example answer:
{"entities": [{"text": "choreoathetoid movements", "type": "Disease"}, {"text": "methadone", "type": "Chemical"}, {"text": "heroine", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Disease"}]}

Example input:
Sentence: Two groups of patients receiving tacrolimus were compared over a period of 1 year , one group comprising hypertensive patients who were receiving nifedipine , and the other comprising nonhypertensive patients not receiving nifedipine .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "hypertensive", "type": "Disease"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: The drug was withdrawn on presentation to hospital in 11 patients , with rapid clinical improvement in 9 .

Example answer:
{"entities": []}

Example input:
Sentence: Eighty-nine new referral hypertensive out-patients and 46 new referral non-hypertensive chronically physically ill out-patients completed a mood rating scale at regular intervals for one year .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}]}

Example input:
Sentence: Since adverse reactions are frequent , less than 50 percent of patients are able to continue a particular drug for more than one year .

Example answer:
{"entities": []}

Example input:
Sentence: She reported her use of methamphetamine for five years and had not experienced any major carious episodes before she started using the drug .

Example answer:
{"entities": [{"text": "methamphetamine", "type": "Chemical"}, {"text": "carious episodes", "type": "Disease"}]}

Example input:
Sentence: METHODS : Retrospective review of medical records of 236 patients with hyperthyroidism admitted in our department ( in- or out-patients ) from 1986 to 1992 .

Example answer:
{"entities": [{"text": "hyperthyroidism", "type": "Disease"}]}

Input:
Sentence: METHODS : We performed a systematic , retrospective study comparing active or former intravenous drug users receiving methadone and those not receiving methadone among all patients hospitalized over a 5-year period in a tertiary care hospital .

## Item bc5cdr:test:2953
Example input:
Sentence: The cell populations were examined regarding total cell recovery correlated with gland weight , intracellular prolactin ( PRL ) content and subsequent release in primary culture , immunocytochemical PRL staining , density and/or size alterations via separation on Ficoll-Hypaque and by unit gravity sedimentation , and cell cycle analysis , after acriflavine DNA staining , by laser flow cytometry .

Example answer:
{"entities": [{"text": "acriflavine", "type": "Chemical"}]}

Example input:
Sentence: Population responses in granule cells of the dentate gyrus were examined in transverse slices of the ventral hippocampus from pilocarpine-treated and untreated mice .

Example answer:
{"entities": [{"text": "pilocarpine-treated", "type": "Chemical"}]}

Example input:
Sentence: In Mg ( 2+ ) -free bathing medium containing bicuculline , conditions designed to increase excitability in the slices , electrical stimulation of the hilus resulted in a single population spike in granule cells from control mice and pilocarpine-treated mice that did not experience SE .

Example answer:
{"entities": [{"text": "Mg", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "pilocarpine-treated", "type": "Chemical"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Sulpiride induced only SOCS-1 in the medial preoptic area , where GnRH neurons are regulated , but in the arcuate nucleus and choroid plexus , PRL-R , SOCS-3 , and CIS mRNA levels were also induced .

Example answer:
{"entities": [{"text": "Sulpiride", "type": "Chemical"}]}

Example input:
Sentence: However , only secretory granules showed the positive reaction products for prolactin 6 h after bromocriptine treatment of the adenoma cells .

Example answer:
{"entities": [{"text": "bromocriptine", "type": "Chemical"}, {"text": "adenoma", "type": "Disease"}]}

Example input:
Sentence: Focal glutamate photostimulation of the granule cell layer at sites distant from the recording pipette resulted in population responses of 1-30 s duration in slices from SE survivors but not other groups .

Example answer:
{"entities": [{"text": "glutamate", "type": "Chemical"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Electron microscopy disclosed many secretory granules , slightly distorted rough endoplasmic reticulum , and partially dilated Golgi cisternae in the prolactinoma cells .

Example answer:
{"entities": [{"text": "prolactinoma", "type": "Disease"}]}

Example input:
Sentence: The prolactinoma cells at this time were well granulated , with vesiculated rough endoplasmic reticulum and markedly dilated Golgi cisternae .

Example answer:
{"entities": [{"text": "prolactinoma", "type": "Disease"}]}

Example input:
Sentence: 9 ( 2006 ) , 917 ] recently identified the microglial-specific fractalkine receptor ( CX3CR1 ) as an important mediator of MPTP-induced neurodegeneration of DA neurons .

Example answer:
{"entities": [{"text": "MPTP-induced", "type": "Chemical"}, {"text": "neurodegeneration", "type": "Disease"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: Electron microscopical immunohistochemistry revealed positive reaction products noted on the secretory granules , Golgi cisternae , and endoplasmic reticulum of the untreated rat prolactinoma cells .

Example answer:
{"entities": [{"text": "prolactinoma", "type": "Disease"}]}

Input:
Sentence: The number of hilar neurons immunoreactive for Prox-1 , a granule-cell-specific marker , was estimated using the optical fractionator method .

## Item bc5cdr:test:2581
Example input:
Sentence: No changes in haloperidol-induced catalepsy or MK-801-induced locomotion were seen following PD .

Example answer:
{"entities": [{"text": "haloperidol-induced", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "MK-801-induced", "type": "Chemical"}]}

Example input:
Sentence: THP exhibited an antipsychotic-like profile by potentiating haloperidol-induced catalepsy , reducing amphetamine-induced hyperactivity and reducing apomorphine-induced climbing in mice .

Example answer:
{"entities": []}

Example input:
Sentence: ) , while apomorphine ( 1.5 mg/kg s.c. ) and amphetamine ( 2 mg/kg s.c. ) were used for studying climbing behavior and locomotor activities , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: Noradrenergic involvement in catalepsy induced by delta 9-tetrahydrocannabinol .

Example answer:
{"entities": [{"text": "catalepsy", "type": "Disease"}, {"text": "delta 9-tetrahydrocannabinol", "type": "Chemical"}]}

Example input:
Sentence: The present study was designed to study the effect of histamine H ( 3 ) -receptor ligands on neuroleptic-induced catalepsy , apomorphine-induced climbing behavior and amphetamine-induced locomotor activities in mice .

Example answer:
{"entities": [{"text": "histamine", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "apomorphine-induced", "type": "Chemical"}, {"text": "amphetamine-induced", "type": "Chemical"}]}

Example input:
Sentence: The development of apomorphine-induced ( 1.0 mg/kg s.c. once daily ) aggressive behavior of adult male and female Wistar rats obtained from the same breeder was studied in two consecutive sets .

Example answer:
{"entities": [{"text": "apomorphine-induced", "type": "Chemical"}, {"text": "aggressive behavior", "type": "Disease"}]}

Example input:
Sentence: However , unlike these latter , SSR103800 did not produce catalepsy ( retention on the bar test ) up to 30 mg/kg p.o .

Example answer:
{"entities": [{"text": "SSR103800", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}]}

Example input:
Sentence: The stereotypies induced by d-amphetamine or apomorphine are not potentiated by TRI .

Example answer:
{"entities": [{"text": "d-amphetamine", "type": "Chemical"}, {"text": "apomorphine", "type": "Chemical"}, {"text": "TRI", "type": "Chemical"}]}

Example input:
Sentence: NRA0160 and clozapine significantly induced catalepsy in rats , although their effects did not exceed 50 % induction even at the highest dose given .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}]}

Example input:
Sentence: Catalepsy was induced by haloperidol ( 2 mg/kg p.o .

Example answer:
{"entities": [{"text": "Catalepsy", "type": "Disease"}, {"text": "haloperidol", "type": "Chemical"}]}

Input:
Sentence: did not induce catalepsy , and did not antagonize apomorphine ( 1.5 and 3 mg/kg ) stereotypy and apomorphine ( 0.05 mg/kg ) -induced catalepsy .

## Item bc5cdr:test:2604
Example input:
Sentence: In this experimental study we used 30 Sprague-Dawley rats , 27 of which had gentamicin instilled into the middle ear .

Example answer:
{"entities": [{"text": "gentamicin", "type": "Chemical"}]}

Example input:
Sentence: Male rats were subcutaneously injected with morphine ( 10 mg/kg ) twice a day at 12 hour intervals for 10 days , and Rg1 ( 30 mg/kg ) was intraperitoneally injected 2 hours after the second injection of morphine once a day for 10 days .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "Rg1", "type": "Chemical"}]}

Example input:
Sentence: Male SD rats ( n = 30 ) were treated with Ato ( 50 mg/kg per day in drinking water ) or tap water for 15 days .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}]}

Example input:
Sentence: METHODS : For a period of 2 weeks , CsA 15 mg/kg/day ( given orally ) , FK506 3.0 mg/kg/day ( given orally ) or SRL 0.4 mg/kg/day ( given intraperitoneally ) was administered once a day as these doses have earlier been found to achieve a significant immunosuppressive effect in Sprague-Dawley rats .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: Rats received subcutaneous injections of 17beta-estradiol ( 2 microg/rat ) or oil once daily for four consecutive days .

Example answer:
{"entities": [{"text": "17beta-estradiol", "type": "Chemical"}]}

Example input:
Sentence: Male Wistar rats were implanted bilaterally with cannulae into the accumbens shell or core , and then were locally injected with GR 55562 ( an antagonist of 5-HT1B receptors ) or CP 93129 ( an agonist of 5-HT1B receptors ) .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Example input:
Sentence: Male Sprague-Dawley rats were treated with D-penicillamine ( D-pen ) 500 mg/kg/day for 10 or 42 days .

Example answer:
{"entities": [{"text": "D-penicillamine", "type": "Chemical"}, {"text": "D-pen", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Thirty-five Wistar rats were given 1.5 mg/kg DOX , i.v. , weekly for up to 8 weeks for a total cumulative dose of 12 mg/kg BW .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: Streptomycin sulfate ( 300 mg/kg s.c. ) was injected for various periods into preweanling rats and for 3 weeks into weanling rats .

Example answer:
{"entities": [{"text": "Streptomycin", "type": "Chemical"}]}

Example input:
Sentence: Rats were treated with a single IV injection of puromycin aminonucleoside , ( PAN , 7.5 mg/kg ) and 24 hour urine samples were obtained prior to sacrifice on days 3,5,7,10,17,27,41 ( N = 5-10 per group ) .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Input:
Sentence: METHODS : 38 female Wistar rats were injected with gentamicin , 40 mg/kg , twice a day for 9 days , 38 with gentamicin + PDTC , and 28 with 0.15 M NaCl solution .

## Item bc5cdr:test:2965
Example input:
Sentence: The overall response rate ( World Health Organization [ WHO ] criteria ) was 15 % ( CR , 2 % ; PR 13 % ; 95 % CI , 6 % to 29 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Efficacy was evaluated using the Clinical Global Impression-Sexual Function ( CGI-SF ; the primary outcome measure ) , the International Index of Erectile Function ( IIEF ) , Arizona Sexual Experience Scale ( ASEX ) , and Erectile Dysfunction Inventory of Treatment Satisfaction ( EDITS ) ( secondary outcome measures ) .

Example answer:
{"entities": [{"text": "Erectile Dysfunction", "type": "Disease"}]}

Example input:
Sentence: The overall response rate was 26 % ( 95 % confidence interval , 15-41 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : The sensitivity improved dramatically from 16 % to 79 % , positive predictive value increased from 60 % to 68 % and negative predictive value from 54 % to 78 % , and specificity decreased from 90 % to 67 % .

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

Example input:
Sentence: Most patients showed improvement in individual parameters and global score of quality of life .

Example answer:
{"entities": []}

Example input:
Sentence: An objective response was observed in 73.5 % of the patients ( 95 % confidence interval [ CI ] , 55.6-87.1 % ) , including 4 complete responses ( 11.7 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Of 24 evaluable patients , two achieved a complete remission and one achieved a partial remission for an overall response rate of 12.5 % ( 95 % confidence interval : 2.6-32.4 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Of 18 patients evaluable for response , seven ( 39 % ) achieved a complete response and six ( 33 % ) achieved a partial response .

Example answer:
{"entities": []}

Input:
Sentence: Eight of 13 participants were rated as responders on the basis of their improvement scores on the Clinical Global Impressions scale .

## Item bc5cdr:test:2811
Example input:
Sentence: Rats were treated with the vehicle ( 2 mL/kg of distilled water and 5 % w/v cellulose , 10 days ) , gum Arabic ( 2 mL/kg of a 10 % w/v aqueous suspension of gum Arabic powder , orally for 10 days ) , or gum Arabic concomitantly with GM ( 80mg/kg/day intramuscularly , during the last six days of the treatment period ) .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}]}

Example input:
Sentence: Conversely , brain normetanephrine concentration was increased from saline control by amantadine in the BALB/C mice .

Example answer:
{"entities": [{"text": "normetanephrine", "type": "Chemical"}, {"text": "amantadine", "type": "Chemical"}]}

Example input:
Sentence: Readministration of amantadine , after a drug-free overnight period , increased motility from respective saline control in all strains with exception of the BALB/C mice where suppression of motility occurred .

Example answer:
{"entities": [{"text": "amantadine", "type": "Chemical"}, {"text": "suppression of motility", "type": "Disease"}]}

Example input:
Sentence: Ten rats received saline as a control group .

Example answer:
{"entities": []}

Example input:
Sentence: Subsequent amantadine treatments produced enhancement of motility from corresponding control in all mouse strains with the BALB/C mice being the least sensitive .

Example answer:
{"entities": [{"text": "amantadine", "type": "Chemical"}]}

Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "Chemical"}]}

Example input:
Sentence: Swiss albino mice prepared with intrajugular catheters were tested in photocell cages after administration of 93 mg/kg ( LD50 ) of cocaine and GNC92H2 infusions ranging from 30 to 190 mg/kg .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "GNC92H2", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Thirty-five Wistar rats were given 1.5 mg/kg DOX , i.v. , weekly for up to 8 weeks for a total cumulative dose of 12 mg/kg BW .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: Thirty male Sprague-Dawley rats were divided randomly into four treatment groups : saline , dexamethasone ( dex ) , allopurinol plus saline , and allopurinol plus dex .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "dex", "type": "Chemical"}, {"text": "allopurinol", "type": "Chemical"}]}

Example input:
Sentence: 2 and 10 mg/kg/i.p. , or an equal volume of saline for the control group ( n = 20 ) ; 15 minutes later , all the animals were injected with a single 50 mg/kg/i.p .

Example answer:
{"entities": []}

Input:
Sentence: METHODS : Six groups of 6 BALB/c mice were treated with saline , DOX alone or DOX ( 4 mg/kg i.v . )

## Item bc5cdr:test:2496
Example input:
Sentence: Memory retrieval of experiences acquired prior to cocaine administration was impaired and negatively correlated with NFkappaB activity in the frontal cortex .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Methamphetamine-induced neurotoxicity and microglial activation are not mediated by fractalkine receptor signaling .

Example answer:
{"entities": [{"text": "Methamphetamine-induced", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: These data lend further support to the proposal that cognitive processes mediated by the prefrontal cortex may be impaired by recreational ecstasy use .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: Cocaine causes memory and learning impairments in rats : involvement of nuclear factor kappa B and oxidative stress , and prevention by topiramate .

Example answer:
{"entities": [{"text": "Cocaine", "type": "Chemical"}, {"text": "topiramate", "type": "Chemical"}]}

Example input:
Sentence: The prolonged depletion of dopamine in the striatum in mice , given multiple injections of methamphetamine , was also antagonized dose-dependently and completely by LY274614 .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "LY274614", "type": "Chemical"}]}

Example input:
Sentence: Learning and memory deficits in ecstasy users and their neural correlates during a face-learning task .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: Methamphetamine ( METH ) damages dopamine ( DA ) nerve endings by a process that has been linked to microglial activation but the signaling pathways that mediate this response have not yet been delineated .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "Chemical"}, {"text": "METH", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Methamphetamine is a very addictive , powerful stimulant that increases wakefulness and physical activity and can produce other effects such as cardiac dysrhythmias , hypertension , hallucinations , and violent behavior .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "Chemical"}, {"text": "cardiac dysrhythmias", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "hallucinations", "type": "Disease"}, {"text": "violent behavior", "type": "Disease"}]}

Example input:
Sentence: In recent years working memory deficits have been reported in users of MDMA ( 3,4-methylenedioxymethamphetamine , ecstasy ) .

Example answer:
{"entities": [{"text": "memory deficits", "type": "Disease"}, {"text": "MDMA", "type": "Chemical"}, {"text": "3,4-methylenedioxymethamphetamine", "type": "Chemical"}, {"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: In addition , working memory processing in ecstasy users has been shown to be associated with neural alterations in hippocampal and/or cortical regions as measured by functional magnetic resonance imaging ( fMRI ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Input:
Sentence: MRI-based maps suggest that chronic methamphetamine abuse causes a selective pattern of cerebral deterioration that contributes to impaired memory performance .

## Item bc5cdr:test:2629
Example input:
Sentence: The absolute risk for bladder cancer in the cohort reached 10 % 16 years after diagnosis of Wegener 's granulomatosis , and a history of bladder cancer was ( non-significantly ) twice as common as expected at the time of diagnosis of Wegener 's granulomatosis .

Example answer:
{"entities": [{"text": "bladder cancer", "type": "Disease"}, {"text": "Wegener 's granulomatosis", "type": "Disease"}]}

Example input:
Sentence: From June 2004 to October 2006 , 11 HBs Ag positive patients with rheumatologic diseases , who were on both immunosuppressive and prophylactic lamivudine therapies , were retrospectively assessed .

Example answer:
{"entities": [{"text": "HBs Ag", "type": "Chemical"}, {"text": "rheumatologic diseases", "type": "Disease"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: Cells were pretreated with maltolyl p-coumarate , before exposed to amyloid beta peptide ( 1-42 ) , glutamate or H2O2 .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "H2O2", "type": "Chemical"}]}

Example input:
Sentence: Baseline renal ACE did not correlate with focal glomerulosclerosis ( r = 0.22 , NS ) .

Example answer:
{"entities": [{"text": "focal glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: Two subsets of patients were identified from this latter group : the first included four patients ( 5 % of the total population ) who developed major toxicity resulting in Fanconi 's syndrome ( TDFS ) ; and the second group included five patients with elevated beta 2 microglobulinuria and low phosphate reabsorption .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "Fanconi 's syndrome", "type": "Disease"}, {"text": "TDFS", "type": "Disease"}, {"text": "phosphate", "type": "Chemical"}]}

Example input:
Sentence: Among the 5 patients with white matter abnormalities , 4 patients ( 80.0 % ) showed higher than normal ADC values on initial MR images , and all showed complete resolution on follow-up images .

Example answer:
{"entities": [{"text": "white matter abnormalities", "type": "Disease"}]}

Example input:
Sentence: Taking these in vitro and in vivo results together , our study suggests that maltolyl p-coumarate is a potentially effective candidate against Alzheimer 's disease that is characterized by wide spread neuronal death and progressive decline of cognitive function .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "Alzheimer 's disease", "type": "Disease"}, {"text": "neuronal death", "type": "Disease"}, {"text": "decline of cognitive function", "type": "Disease"}]}

Example input:
Sentence: A 34-year-old lady developed a constellation of dermatitis , fever , lymphadenopathy and hepatitis , beginning on the 17th day of a course of oral sulphasalazine for sero-negative rheumatoid arthritis .

Example answer:
{"entities": [{"text": "dermatitis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "lymphadenopathy", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Example input:
Sentence: Srl should be used with ACEi/ARB therapy and patients monitored for proteinuria and increased renal dysfunction .

Example answer:
{"entities": [{"text": "Srl", "type": "Chemical"}, {"text": "ACEi/ARB", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "renal dysfunction", "type": "Disease"}]}

Example input:
Sentence: The semi-quantitative scoring was significantly worst in the group treated with CsA plus SRL ( P < 0.001 compared with controls ) and the analysis of the total grade of fibrosis also showed the highest proportion in the same group and was significantly different from controls ( P < 0.02 ) .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "fibrosis", "type": "Disease"}]}

Input:
Sentence: BACKGROUND : Patients with primary systemic amyloidosis ( AL ) have a poor prognosis .

## Item bc5cdr:test:2870
Example input:
Sentence: Noxious chemical stimulation of rat facial mucosa increases intracranial blood flow through a trigemino-parasympathetic reflex -- an experimental model for vascular dysfunctions in cluster headache .

Example answer:
{"entities": [{"text": "vascular dysfunctions", "type": "Disease"}, {"text": "cluster headache", "type": "Disease"}]}

Example input:
Sentence: The aim of this study is to examine the role of gastric acid back-diffusion , mast cell histamine release , lipid peroxide ( LPO ) generation and mucosal microvascular permeability in modulating gastric hemorrhage and ulcer in rats with atherosclerosis induced by coadministration of vitamin D2 and cholesterol .

Example answer:
{"entities": [{"text": "histamine", "type": "Chemical"}, {"text": "gastric hemorrhage", "type": "Disease"}, {"text": "ulcer", "type": "Disease"}, {"text": "atherosclerosis", "type": "Disease"}, {"text": "vitamin D2", "type": "Chemical"}, {"text": "cholesterol", "type": "Chemical"}]}

Example input:
Sentence: Treatment with Ato improved endothelial function , reduced superoxide production and reduced SBP in Dex-treated SD rats .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}, {"text": "superoxide", "type": "Chemical"}, {"text": "Dex-treated", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : This study establishes a TAA model by periarterial CaCl ( 2 ) exposure in rats , and demonstrates a significant elevation of expression of MMP-2 , MMP-9 , ADAM10 and ADAM17 in the pathogenesis of vascular remodeling .

Example answer:
{"entities": [{"text": "TAA", "type": "Disease"}, {"text": "CaCl ( 2 )", "type": "Chemical"}]}

Example input:
Sentence: The [ verapamil ] o that arrested atrial beating ( AC ) was also potentiated with the order LNa = LNa+LCa = LNa+HCa = LCa > HCa = N. The results indicate that rat atrial spontaneous beating is more dependent on [ Na ] o than on [ Ca ] o in a range of +/- 50 % of their normal concentration .

Example answer:
{"entities": [{"text": "verapamil", "type": "Chemical"}, {"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Thoracic aorta of male Sprague-Dawley rats was exposed to 0.5M CaCl ( 2 ) or normal saline ( NaCl ) .

Example answer:
{"entities": [{"text": "CaCl ( 2 )", "type": "Chemical"}, {"text": "NaCl", "type": "Chemical"}]}

Example input:
Sentence: Ten rats had arterial , central venous ( CVP ) , and subdural cannulae inserted under halothane anesthesia .

Example answer:
{"entities": [{"text": "halothane", "type": "Chemical"}]}

Example input:
Sentence: High levels of matrix Gla protein are found at sites of artery calcification in rats treated with vitamin D plus Warfarin , and chemical analysis showed that the protein that accumulated was indeed not gamma-carboxylated .

Example answer:
{"entities": [{"text": "artery calcification", "type": "Disease"}, {"text": "vitamin D", "type": "Chemical"}, {"text": "Warfarin", "type": "Chemical"}, {"text": "gamma-carboxylated", "type": "Chemical"}]}

Example input:
Sentence: TR ( - ) rats exhibited a significant up-regulation of Pgp in brain capillary endothelial cells compared with wild-type controls .

Example answer:
{"entities": []}

Example input:
Sentence: Six weeks after clipping of one renal artery , hypertensive rats ( 178 +/- 4 mm Hg ) were randomly assigned to three groups : untreated hypertensive controls ( n = 8 ) , enalapril-treated ( n = 8 ) , or nitrendipine-treated ( n = 10 ) .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}, {"text": "enalapril-treated", "type": "Chemical"}, {"text": "nitrendipine-treated", "type": "Chemical"}]}

Input:
Sentence: Carotid arteries , vena cava , and sympathetic ganglia from LNNA rats had higher basal levels of superoxide compared with those from control rats .

## Item bc5cdr:test:2603
Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: Histologic changes were found in rat kidneys after administration of MTX , CY and NG , while no such change was observed after 5-FU and joint administration of MTX + 5-FU + CY compared to controls .

Example answer:
{"entities": [{"text": "MTX", "type": "Chemical"}, {"text": "CY", "type": "Chemical"}, {"text": "NG", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}]}

Example input:
Sentence: In the present work we assessed the effect of treatment of rats with gum Arabic on acute renal failure induced by gentamicin ( GM ) nephrotoxicity .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}]}

Example input:
Sentence: NFkappaB activity was decreased in the frontal cortex of cocaine treated rats , as well as GSH concentration and glutathione peroxidase activity in the hippocampus , whereas nNOS activity in the hippocampus was increased .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}]}

Example input:
Sentence: The nephrotoxic action of anticancer drugs such as nitrogranulogen ( NG ) , methotrexate ( MTX ) , 5-fluorouracil ( 5-FU ) and cyclophosphamide ( CY ) administered alone or in combination [ MTX + 5-FU + CY ( CMF ) ] was evaluated in experiments on Wistar rats .

Example answer:
{"entities": [{"text": "nephrotoxic", "type": "Disease"}, {"text": "nitrogranulogen", "type": "Chemical"}, {"text": "NG", "type": "Chemical"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "MTX", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CY", "type": "Chemical"}]}

Example input:
Sentence: Using puromycin aminonucleoside nephrosis ( PAN ) rats , we studied early ultrastructural and permeability changes in relation to the expression of the podocyte-associated molecules nephrin , a-actinin , dendrin , and plekhh2 , the last two of which were only recently discovered in podocytes .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : This rat study demonstrated a synergistic nephrotoxic effect of CsA plus SRL , whereas FK506 plus SRL was better tolerated .

Example answer:
{"entities": [{"text": "nephrotoxic", "type": "Disease"}, {"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}]}

Example input:
Sentence: In conclusion , the NF-kappaB inhibitor and antioxidant PDTC protected the piriform cortex , whereas it did not affect hilar neuronal loss .

Example answer:
{"entities": [{"text": "PDTC", "type": "Chemical"}, {"text": "neuronal loss", "type": "Disease"}]}

Example input:
Sentence: The aim of this study was to examine further the renal function , including morphological analysis of the kidneys of male Sprague-Dawley rats treated with either cyclosporine A ( CsA ) , tacrolimus ( FK506 ) or SRL as monotherapies or in different combinations .

Example answer:
{"entities": [{"text": "cyclosporine A", "type": "Chemical"}, {"text": "CsA", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: Pyrrolidine dithiocarbamate ( PDTC ) has a dual mechanism of action as an antioxidant and an inhibitor of the transcription factor kappa-beta .

Example answer:
{"entities": [{"text": "Pyrrolidine dithiocarbamate", "type": "Chemical"}, {"text": "PDTC", "type": "Chemical"}]}

Input:
Sentence: This study investigated the expression of nuclear factor-kappaB ( NF-kappaB ) , mitogen-activated protein ( MAP ) kinases and macrophages in the renal cortex and structural and functional renal changes of rats treated with gentamicin or gentamicin + pyrrolidine dithiocarbamate ( PDTC ) , an NF-kappaB inhibitor .

## Item bc5cdr:test:2983
Example input:
Sentence: A review of all reported cases in the literature is given .

Example answer:
{"entities": []}

Example input:
Sentence: Aim of the study was to determine sensitivity , reproducibility , reference values and the agreement with a questionnaire .

Example answer:
{"entities": []}

Example input:
Sentence: Published cases from the literature are reviewed and pertinent features discussed .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : We conducted a prospective , randomized , double-blind study in the emergency department of a central-city teaching hospital .

Example answer:
{"entities": []}

Example input:
Sentence: METHOD : Open , case series design .

Example answer:
{"entities": []}

Example input:
Sentence: Experimental design consisted of four groups : control ( vehicle alone ) , GSPE alone , drug alone and GSPE+drug .

Example answer:
{"entities": [{"text": "GSPE", "type": "Chemical"}, {"text": "GSPE+drug", "type": "Chemical"}]}

Example input:
Sentence: A prospective study .

Example answer:
{"entities": []}

Example input:
Sentence: DESIGN : Case study .

Example answer:
{"entities": []}

Example input:
Sentence: DESIGN : This study was designed as within-subject , quasi-experimental research .

Example answer:
{"entities": []}

Example input:
Sentence: DESIGN : Retrospective analysis of a randomized phase II trial .

Example answer:
{"entities": []}

Input:
Sentence: DESIGN : Retrospective study .

## Item bc5cdr:test:2621
Example input:
Sentence: Considering that clozapine remains the gold standard in treatment of resistant psychosis , there is an urgent need to raise awareness among medical and paramedical staff involved in the care of these patients .

Example answer:
{"entities": [{"text": "clozapine", "type": "Chemical"}, {"text": "psychosis", "type": "Disease"}]}

Example input:
Sentence: The side effect profiles of the atypical antipsychotics are more advantageous than those of the conventional neuroleptics .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : After 12 weeks of treatment , the mean ( sd ) scores for CGI-SF were significantly lower , i.e .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : For the 60 patients who completed phase A , standard-dose haloperidol was efficacious and superior to both low-dose haloperidol and placebo for scores on the Brief Psychiatric Rating Scale psychosis factor and on psychomotor agitation .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "psychosis", "type": "Disease"}, {"text": "psychomotor agitation", "type": "Disease"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: In a double-blind 6-week trial , 458 patients with acute schizophrenia were randomly assigned to fixed-dose treatment with asenapine at 5 mg twice daily ( BID ) , asenapine at 10 mg BID , placebo , or haloperidol at 4 mg BID ( to verify assay sensitivity ) .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "Disease"}, {"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Previous clinical studies have proposed that risperidone 's pharmacologic profile may produce improved efficacy for negative psychotic symptoms and decreased propensity for extrapyramidal side effects ; features shared by so-called 'atypical ' neuroleptics .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}, {"text": "psychotic symptoms", "type": "Disease"}]}

Example input:
Sentence: Importantly , both classical ( haloperidol ) and atypical ( olanzapine , clozapine and aripiprazole ) antipsychotics were effective in all these models of hyperactivity .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "olanzapine", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "aripiprazole", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}]}

Example input:
Sentence: Associated factors were co-treatment with other centrally antimuscarinic agents , poor clinical outcome , older age , and longer hospitalization ( by 17.5 days , increasing cost ) ; sex , diagnosis or medical co-morbidity , and daily clozapine dose , which fell with age , were unrelated .

Example answer:
{"entities": [{"text": "clozapine", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Subjects ( n = 139 ) were 72 women and 67 men , aged 40.8 +/- 12.1 years , hospitalized for 24.9 +/- 23.3 days , and given clozapine , gradually increased to an average daily dose of 282 +/- 203 mg ( 3.45 +/- 2.45 mg/kg ) for 18.9 +/- 16.4 days .

Example answer:
{"entities": [{"text": "clozapine", "type": "Chemical"}]}

Input:
Sentence: RESULTS : The mean +/- SD duration of treatment with the identified atypical antipsychotic agent was 68.3 +/- 28.9 months ( clozapine ) , 29.5 +/- 17.5 months ( olanzapine ) , and 40.9 +/- 33.7 ( risperidone ) .

## Item bc5cdr:test:2497
Example input:
Sentence: 9 ( 2006 ) , 917 ] recently identified the microglial-specific fractalkine receptor ( CX3CR1 ) as an important mediator of MPTP-induced neurodegeneration of DA neurons .

Example answer:
{"entities": [{"text": "MPTP-induced", "type": "Chemical"}, {"text": "neurodegeneration", "type": "Disease"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: Results show that cumulative HAART caused mitochondrial CM with elevated LA in AIDS transgenic mice .

Example answer:
{"entities": [{"text": "CM", "type": "Disease"}, {"text": "LA", "type": "Chemical"}, {"text": "AIDS", "type": "Disease"}]}

Example input:
Sentence: These data indicate that a critical percentage of NTE inhibition in brain and spinal cord sampled shortly after Mipafox exposure can predict neuropathic damage in rats several weeks later .

Example answer:
{"entities": [{"text": "Mipafox", "type": "Chemical"}, {"text": "neuropathic damage", "type": "Disease"}]}

Example input:
Sentence: Ecstasy-specific hypoactivity was evident in the right dorsal anterior cingulated cortex ( ACC ) and left posterior cingulated cortex .

Example answer:
{"entities": [{"text": "Ecstasy-specific", "type": "Chemical"}]}

Example input:
Sentence: Because such a compensatory mechanism most likely occurs to reduce injury to the brain from cytotoxic compounds , the present data substantiate the concept that MRP2 performs a protective role in the BBB .

Example answer:
{"entities": [{"text": "injury to the brain", "type": "Disease"}]}

Example input:
Sentence: In both ecstasy and cannabis groups brain activation was decreased in the right medial frontal gyrus , left parahippocampal gyrus , left dorsal cingulate gyrus , and left caudate .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}, {"text": "cannabis", "type": "Chemical"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: Under anesthesia , the superior temporal gyrus of adult macaque monkeys was exposed , and the tonotopic organization of A1 was mapped using conventional microelectrode recording techniques .

Example answer:
{"entities": []}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "Disease"}, {"text": "METH", "type": "Chemical"}, {"text": "MPTP", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "METH-induced", "type": "Chemical"}]}

Example input:
Sentence: Mitochondrial abnormalities have been associated with several aspects of epileptogenesis , such as energy generation , control of cell death , neurotransmitter synthesis , and free radical ( FR ) production .

Example answer:
{"entities": [{"text": "Mitochondrial abnormalities", "type": "Disease"}, {"text": "death", "type": "Disease"}]}

Input:
Sentence: MA may selectively damage the medial temporal lobe and , consistent with metabolic studies , the cingulate-limbic cortex , inducing neuroadaptation , neuropil reduction , or cell death .

## Item bc5cdr:test:2988
Example input:
Sentence: A slow bolus of subhypnotic doses of ketamine ( 0.25 mg/kg or 0.50 mg/kg ) was given to 10 cancer patients whose pain was unrelieved by morphine in a randomized , double-blind , crossover , double-dose study .

Example answer:
{"entities": [{"text": "ketamine", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: were correlated with serum concentrations and renal and hepatic function in 36 patients , 30 patients had no M.S .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSIONS : The results indicated a favorable therapeutic profile for haloperidol in doses of 2-3 mg/day , although a subgroup developed moderate to severe extrapyramidal signs .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "extrapyramidal signs", "type": "Disease"}]}

Example input:
Sentence: CASE REPORT : We describe 2 patients who were regular consumers of alcohol and who developed liver failure within 3-5 days after hospitalization and stopping alcohol consumption while being treated with 4 g paracetamol/day .

Example answer:
{"entities": [{"text": "alcohol", "type": "Chemical"}, {"text": "liver failure", "type": "Disease"}, {"text": "paracetamol/day", "type": "Chemical"}]}

Example input:
Sentence: With mild toxicity , a reduction to 30 or 40 mg/kg per dose should result in a reversal of the abnormal results to normal within four weeks .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: In this study , 62 patients with confirmed initial normal renal function and treated with 2 to 5 mg/kg/day of gentamicin sulfate or tobramycin sulfate for a minimum of seven days were followed up prospectively for the development of aminoglycoside-related renal failure , defined as at least a one-third reduction in renal function .

Example answer:
{"entities": [{"text": "gentamicin sulfate", "type": "Chemical"}, {"text": "tobramycin sulfate", "type": "Chemical"}, {"text": "aminoglycoside-related", "type": "Chemical"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: Finally , we examined the low dose of 150 mg/kg ( 50 mg/kg per day ) using a similar washout period .

Example answer:
{"entities": []}

Example input:
Sentence: injections of organ specific three drugs ( AAP : 500 mg/Kg for 24 h ; AMI : 50 mg/Kg/day for four days ; DOX : 20 mg/Kg for 48 h ) .

Example answer:
{"entities": [{"text": "AAP", "type": "Chemical"}, {"text": "AMI", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: We propose that the paracetamol dose should not exceed 2 g/day in such patients and that their liver function should be monitored closely while being treated with paracetamol .

Example answer:
{"entities": [{"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: These 6 patients had both renal and liver dysfunction ( P less than 0.05 ) , as well as cimetidine trough-concentrations of more than 1.25 microgram/ml ( P less than 0.05 ) .

Example answer:
{"entities": [{"text": "cimetidine", "type": "Chemical"}]}

Input:
Sentence: Three of the 4 patients were taking less than 6.5 mg/kg per day and all patients had normal renal and liver function test results .

## Item bc5cdr:test:2995
Example input:
Sentence: The excess event rate was 1.8 per 1,000 woman-years ( 95 % CI -0.5-4.1 ) , and the number needed to treat to cause 1 event was 170 ( 95 % CI 100-582 ) over 3.3 years .

Example answer:
{"entities": []}

Example input:
Sentence: Based on this principle a 27-year old woman , classified as being in the high-risk group ( Goldstein and Berkowitz score : 11 ) , was treated with multiple cytotoxic drugs .

Example answer:
{"entities": []}

Example input:
Sentence: There were no severe events and there was no need to interrupt the examinations .

Example answer:
{"entities": []}

Example input:
Sentence: It is postulated that her death was caused by hypersensitivity to suxamethonium , associated with her 5-day immobilization .

Example answer:
{"entities": [{"text": "death", "type": "Disease"}, {"text": "hypersensitivity", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: She was unable to urinate .

Example answer:
{"entities": []}

Example input:
Sentence: Motor behavior , passive avoidance , and skilled forelimb function were tested repeatedly for six weeks .

Example answer:
{"entities": []}

Example input:
Sentence: She had a gradual return of motor function and ability of feeling Foley catheter .

Example answer:
{"entities": []}

Example input:
Sentence: While she was weak , 2-Hz repetitive stimulation revealed a decrement without significant facilitation at rapid rates or after exercise , suggesting postsynaptic neuromuscular blockade .

Example answer:
{"entities": [{"text": "postsynaptic neuromuscular blockade", "type": "Disease"}]}

Example input:
Sentence: Possible contributing factors may have been concomitant antidepressant use and unaccustomed physical activity .

Example answer:
{"entities": [{"text": "antidepressant", "type": "Chemical"}]}

Example input:
Sentence: After her strength returned , repetitive stimulation was normal , but single fiber EMG revealed increased jitter and blocking .

Example answer:
{"entities": []}

Input:
Sentence: This had been apparently uncomplicated and she had maintained a remarkably high level of physical activity .

## Item bc5cdr:test:2628
Example input:
Sentence: Myopathy , associated in some cases with myoglobinuria , and in 2 cases with transient renal failure , has been rarely reported with lovastatin , especially in patients concomitantly treated with cyclosporin , gemfibrozil or niacin .

Example answer:
{"entities": [{"text": "Myopathy", "type": "Disease"}, {"text": "myoglobinuria", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}, {"text": "lovastatin", "type": "Chemical"}, {"text": "cyclosporin", "type": "Chemical"}, {"text": "gemfibrozil", "type": "Chemical"}, {"text": "niacin", "type": "Chemical"}]}

Example input:
Sentence: We report a case of ranitidine-induced acute interstitial nephritis in a recipient of a cadaveric renal allograft presenting with acute allograft dysfunction within 48 hours of exposure to the drug .

Example answer:
{"entities": [{"text": "ranitidine-induced", "type": "Chemical"}, {"text": "interstitial nephritis", "type": "Disease"}]}

Example input:
Sentence: Although tacrolimus was suspected to be the cause of late post-transplant renal acidosis and was replaced by sirolimus , acidosis , and electrolyte imbalance got worse .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "acidosis", "type": "Disease"}, {"text": "sirolimus", "type": "Chemical"}]}

Example input:
Sentence: Three yr after transplantation she developed renal Fanconi syndrome with severe metabolic acidosis , hypophosphatemia , glycosuria , and aminoaciduria .

Example answer:
{"entities": [{"text": "renal Fanconi syndrome", "type": "Disease"}, {"text": "metabolic acidosis", "type": "Disease"}, {"text": "hypophosphatemia", "type": "Disease"}, {"text": "glycosuria", "type": "Disease"}, {"text": "aminoaciduria", "type": "Disease"}]}

Example input:
Sentence: Massive urinary protein excretion has been observed after conversion from calcineurin inhibitors to mammalian target of rapamycin ( mToR ) inhibitors , especially sirolimus , in renal transplant recipients with chronic allograft nephropathy .

Example answer:
{"entities": [{"text": "rapamycin", "type": "Chemical"}, {"text": "sirolimus", "type": "Chemical"}, {"text": "chronic allograft nephropathy", "type": "Disease"}]}

Example input:
Sentence: Two patients developed acute tubular necrosis , characterized clinically by acute oliguric renal failure , while they were receiving a combination of cephalothin sodium and gentamicin sulfate therapy .

Example answer:
{"entities": [{"text": "acute tubular necrosis", "type": "Disease"}, {"text": "cephalothin sodium", "type": "Chemical"}, {"text": "gentamicin sulfate", "type": "Chemical"}]}

Example input:
Sentence: Massive proteinuria and acute renal failure after oral bisphosphonate ( alendronate ) administration in a patient with focal segmental glomerulosclerosis .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "bisphosphonate", "type": "Chemical"}, {"text": "alendronate", "type": "Chemical"}, {"text": "focal segmental glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: A patient with cryptogenic cirrhosis and disseminated sporotrichosis developed acute renal failure immediately following the administration of amphotericin B on four separate occasions .

Example answer:
{"entities": [{"text": "cirrhosis", "type": "Disease"}, {"text": "sporotrichosis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}]}

Example input:
Sentence: Severe rhabdomyolysis and acute renal failure secondary to concomitant use of simvastatin , amiodarone , and atazanavir .

Example answer:
{"entities": [{"text": "rhabdomyolysis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Input:
Sentence: Acute renal insufficiency after high-dose melphalan in patients with primary systemic amyloidosis during stem cell transplantation .

## Item bc5cdr:test:2774
Example input:
Sentence: Despite inducing extensive erythrocyte lysis , TAM does not shift the osmotic fragility curves of erythrocytes .

Example answer:
{"entities": [{"text": "TAM", "type": "Chemical"}]}

Example input:
Sentence: The development of ESRD decreases survival , particularly in those patients treated with dialysis only .

Example answer:
{"entities": [{"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Captopril may , by the same mechanism , reduce the increase in glomerular filtration that is known to occur after an injection of thrombin , thereby diminishing the aggregation of fibrin monomers in the glomeruli , with the result that less fibrin will be deposited and thus less kidney damage will be produced .

Example answer:
{"entities": [{"text": "Captopril", "type": "Chemical"}, {"text": "kidney damage", "type": "Disease"}]}

Example input:
Sentence: The risk of renal papillary necrosis was increased nearly 20-fold by consumption of phenacetin , which also increased the risk for cancer of the renal pelvis and bladder but not for ureteric cancer .

Example answer:
{"entities": [{"text": "renal papillary necrosis", "type": "Disease"}, {"text": "phenacetin", "type": "Chemical"}, {"text": "ureteric cancer", "type": "Disease"}]}

Example input:
Sentence: Patients who developed renal insufficiency had lower baseline body weight and higher baseline serum creatinine , required higher doses of loop diuretics , and were more likely to be treated with thiazide diuretics than controls .

Example answer:
{"entities": [{"text": "renal insufficiency", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "thiazide", "type": "Chemical"}]}

Example input:
Sentence: Histologic changes were found in rat kidneys after administration of MTX , CY and NG , while no such change was observed after 5-FU and joint administration of MTX + 5-FU + CY compared to controls .

Example answer:
{"entities": [{"text": "MTX", "type": "Chemical"}, {"text": "CY", "type": "Chemical"}, {"text": "NG", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}]}

Example input:
Sentence: These effects suggest that the protection from hemolysis by tocopherols is related to a decreased TAM incorporation in condensed membranes and the structural damage of the erythrocyte membrane is consequently avoided .

Example answer:
{"entities": [{"text": "hemolysis", "type": "Disease"}, {"text": "tocopherols", "type": "Chemical"}, {"text": "TAM", "type": "Chemical"}]}

Example input:
Sentence: Histopathological examination of kidney , heart and lung sections revealed moderate to massive tissue damage with a variety of morphological aberrations by all the three drugs in the absence of GSPE preexposure than in its presence .

Example answer:
{"entities": [{"text": "tissue damage", "type": "Disease"}, {"text": "GSPE", "type": "Chemical"}]}

Example input:
Sentence: We propose that amphotericin , in the setting of reduced effective arterial volume , may activate tubuloglomerular feedback , thereby contributing to acute renal failure .

Example answer:
{"entities": [{"text": "amphotericin", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: Picloxydine irrigations appeared to have a lower incidence of erosive cystitis but further studies would have to be performed before it could be recommended for use in urological procedures .

Example answer:
{"entities": [{"text": "Picloxydine", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Input:
Sentence: Erdosteine caused a marked reduction in the extent of tubular damage .

## Item bc5cdr:test:2700
Example input:
Sentence: BMCs obtained from green fluorescent protein ( GFP ) transgenic mice or rats were transplanted intravenously after induction of status epilepticus ( SE ) .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Prevention of seizures and reorganization of hippocampal functions by transplantation of bone marrow cells in the acute phase of experimental epilepsy .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "epilepsy", "type": "Disease"}]}

Example input:
Sentence: The effect of PDTC on status epilepticus-associated cell loss in the hippocampus and piriform cortex was evaluated in the rat fractionated pilocarpine model .

Example answer:
{"entities": [{"text": "PDTC", "type": "Chemical"}, {"text": "status", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: When hippocampal ACh was measured during testing for handling-induced convulsions , extracellular ACh was significantly elevated ( 192 % ) in WSP mice , but was nonsignificantly elevated ( 59 % ) in WSR mice .

Example answer:
{"entities": [{"text": "ACh", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}]}

Example input:
Sentence: In this study , we investigated whether increased generation of FR during status epilepticus would be sufficient to provoke abnormalities in mtDNA and in the expression and activity of cytochrome c oxidase ( CCO ) , complex IV of the respiratory chain , in the chronic phase of the pilocarpine model of temporal lobe epilepsy .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}, {"text": "temporal lobe epilepsy", "type": "Disease"}]}

Example input:
Sentence: A comparable overexpression of Pgp in the BBB was obtained after pilocarpine-induced seizures in wild-type Wistar rats .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: A significant decrease in neuronal density of the hippocampal hilar formation was identified in vehicle- and PDTC-treated rats following status epilepticus .

Example answer:
{"entities": [{"text": "PDTC-treated", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}]}

Example input:
Sentence: At hippocampal Schaeffer collateral-CA1 synapses , long-term potentiation was preserved in BMC-transplanted rats compared to epileptic controls .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}]}

Input:
Sentence: Growth-associated protein 43 expression in hippocampal molecular layer of chronic epileptic rats treated with cycloheximide .

## Item bc5cdr:test:2796
Example input:
Sentence: Orthostatic hypotension was ameliorated 4 days after withdrawal of selegiline and totally abolished 7 days after discontinuation of the drug .

Example answer:
{"entities": [{"text": "Orthostatic hypotension", "type": "Disease"}, {"text": "selegiline", "type": "Chemical"}]}

Example input:
Sentence: This complication reappeared on day 25 during the second dose of 5-fluorouracil and folinic acid , which were then the only drugs given .

Example answer:
{"entities": [{"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: When deferoxamine therapy was discontinued and serial studies were performed , audiograms in seven cases reverted to normal or near normal within two to three weeks , and nine of 13 patients with symptoms became asymptomatic .

Example answer:
{"entities": [{"text": "deferoxamine", "type": "Chemical"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: After the administration of NG , 5-FU and CY neither a statistically significant increase in creatinine concentration nor an increase in creatinine clearance was observed compared to the group receiving no cytostatics .

Example answer:
{"entities": [{"text": "NG", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "CY", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: After starting PGE1 or TMP , MAP and rate pressure product ( RPP ) decreased significantly compared with preinfusion values ( P < 0.01 ) , and the degree of hypotension due to PGE1 remained constant until 60 min after its discontinuation .

Example answer:
{"entities": [{"text": "PGE1", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: He developed acute neurologic symptoms of mental confusion , disorientation and irritability , and then lapsed into a deep coma , lasting for approximately 40 hours during the first dose ( day 2 ) of 5-fluorouracil and folinic acid infusion .

Example answer:
{"entities": [{"text": "confusion", "type": "Disease"}, {"text": "disorientation", "type": "Disease"}, {"text": "irritability", "type": "Disease"}, {"text": "coma", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: Thirty days after amiodarone discontinuation , His bundle electrograms showed atrial flutter without intra-Hisian or infra-Hisian delay .

Example answer:
{"entities": [{"text": "amiodarone", "type": "Chemical"}, {"text": "atrial flutter", "type": "Disease"}]}

Example input:
Sentence: It is concluded that patients on 5-FU treatment should be under close supervision and that the treatment should be discontinued if chest pain or tachyarrhythmia is observed .

Example answer:
{"entities": [{"text": "5-FU", "type": "Chemical"}, {"text": "chest pain", "type": "Disease"}, {"text": "tachyarrhythmia", "type": "Disease"}]}

Input:
Sentence: Both the precordial pain and the electrocardiographic changes disappeared spontaneously after the discontinuation of 5-FU .

## Item bc5cdr:test:2905
Example input:
Sentence: CONCLUSIONS : This study demonstrates that chronic FK506 nephropathy consists primarily of arteriolopathy manifesting as insudative hyalinosis of the arteriolar wall , and suggests that mild-type chronic FK506 nephropathy is a condition which may lead to deterioration of renal allograft function .

Example answer:
{"entities": [{"text": "FK506", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: A 49-year-old woman was transferred to our department because of quadriparesis , lancinating pain , sensory loss , and paresthesia of the distal limbs .

Example answer:
{"entities": [{"text": "quadriparesis", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "sensory loss", "type": "Disease"}, {"text": "paresthesia", "type": "Disease"}]}

Example input:
Sentence: We describe 3 episodes of microangiopathic hemolytic anemia ( MAHA ) in 2 solid organ recipients under FK506 ( tacrolimus ) therapy .

Example answer:
{"entities": [{"text": "microangiopathic hemolytic anemia", "type": "Disease"}, {"text": "MAHA", "type": "Disease"}, {"text": "FK506", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}]}

Example input:
Sentence: From June 2004 to October 2006 , 11 HBs Ag positive patients with rheumatologic diseases , who were on both immunosuppressive and prophylactic lamivudine therapies , were retrospectively assessed .

Example answer:
{"entities": [{"text": "HBs Ag", "type": "Chemical"}, {"text": "rheumatologic diseases", "type": "Disease"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: A 34-year-old lady developed a constellation of dermatitis , fever , lymphadenopathy and hepatitis , beginning on the 17th day of a course of oral sulphasalazine for sero-negative rheumatoid arthritis .

Example answer:
{"entities": [{"text": "dermatitis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "lymphadenopathy", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Example input:
Sentence: Chronic FK506 nephropathy consisted of rough and foamy tubular vacuolization ( 5 biopsies ) , arteriolopathy ( angiodegeneration of the arteriolar wall ; 20 biopsies ) , focal segmental glomerulosclerosis ( 4 biopsies ) and the striped form of interstitial fibrosis ( 11 biopsies ) .

Example answer:
{"entities": [{"text": "FK506", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "focal segmental glomerulosclerosis", "type": "Disease"}, {"text": "interstitial fibrosis", "type": "Disease"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: These 13 included cases of malignant hypertension , thrombotic microangiopathy , lupus nephritis , Henoch-Schonlein nephritis , crescentic glomerulonephritis , and cocaine-related acute renal failure .

Example answer:
{"entities": [{"text": "malignant hypertension", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "lupus nephritis", "type": "Disease"}, {"text": "Henoch-Schonlein nephritis", "type": "Disease"}, {"text": "glomerulonephritis", "type": "Disease"}, {"text": "cocaine-related", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: RESULTS : The main pathologic diagnoses ( some overlap ) were acute rejection ( AR ; n = 4 ) , chronic rejection ( CR ; n=5 ) , AR+CR ( n =4 ) , recurrent IgA nephropathy ( n =5 ) , normal findings ( n =2 ) , minimal-type chronic FK506 nephropathy ( n = 9 ) , and mild-type FK506 nephropathy ( n = 11 ) .

Example answer:
{"entities": [{"text": "IgA nephropathy", "type": "Disease"}, {"text": "FK506", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: Intracranial aneurysms or arteriovenous malformations were present in 17 of 32 patients studied angiographically or at autopsy ; cerebral vasculitis was present in two patients .

Example answer:
{"entities": [{"text": "Intracranial aneurysms", "type": "Disease"}, {"text": "arteriovenous malformations", "type": "Disease"}, {"text": "cerebral vasculitis", "type": "Disease"}]}

Input:
Sentence: These manifestations met the American College of Rheumatology 1990 criteria for the classification of polyarteritis nodosa .

## Item bc5cdr:test:3039
Example input:
Sentence: He was awake , revealed no changes of mental status and at rest there were no further motor symptoms .

Example answer:
{"entities": []}

Example input:
Sentence: The drug was withdrawn on presentation to hospital in 11 patients , with rapid clinical improvement in 9 .

Example answer:
{"entities": []}

Example input:
Sentence: Fewer than 6 % of patients in either group were considered by the investigator to have a worsening of their overall disease condition during the study .

Example answer:
{"entities": []}

Example input:
Sentence: Most patients showed improvement in individual parameters and global score of quality of life .

Example answer:
{"entities": []}

Example input:
Sentence: Severe distress was noted in the recovery phase in two patients .

Example answer:
{"entities": []}

Example input:
Sentence: The patient 's symptoms improved slightly over the next few hours .

Example answer:
{"entities": []}

Example input:
Sentence: One patient had complete response , seven had stable disease , none had partial response and five had progressive disease .

Example answer:
{"entities": []}

Example input:
Sentence: All patients recovered without sequelae .

Example answer:
{"entities": []}

Example input:
Sentence: The majority of patients ( > 60 % ) experienced no change in their disease status from baseline .

Example answer:
{"entities": []}

Example input:
Sentence: Three patients had no change and disease progressed in two .

Example answer:
{"entities": []}

Input:
Sentence: There was no further deterioration in the patient 's condition during transport to hospital .

## Item bc5cdr:test:2648
Example input:
Sentence: An experimental model was developed in the rat to measure changes in lacrimation and intracranial blood flow following noxious chemical stimulation of facial mucosa .

Example answer:
{"entities": []}

Example input:
Sentence: These data indicate that a critical percentage of NTE inhibition in brain and spinal cord sampled shortly after Mipafox exposure can predict neuropathic damage in rats several weeks later .

Example answer:
{"entities": [{"text": "Mipafox", "type": "Chemical"}, {"text": "neuropathic damage", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : This study establishes a TAA model by periarterial CaCl ( 2 ) exposure in rats , and demonstrates a significant elevation of expression of MMP-2 , MMP-9 , ADAM10 and ADAM17 in the pathogenesis of vascular remodeling .

Example answer:
{"entities": [{"text": "TAA", "type": "Disease"}, {"text": "CaCl ( 2 )", "type": "Chemical"}]}

Example input:
Sentence: In the present study , we investigated the changes occurring at the protein level in striatal samples obtained from the unilaterally 6-hydroxydopamine-lesion rat model of PD treated with saline , L-DOPA or bromocriptine using two-dimensional difference gel electrophoresis and mass spectrometry ( MS ) .

Example answer:
{"entities": [{"text": "6-hydroxydopamine-lesion", "type": "Chemical"}, {"text": "PD", "type": "Disease"}, {"text": "L-DOPA", "type": "Chemical"}, {"text": "bromocriptine", "type": "Chemical"}]}

Example input:
Sentence: All rats in the sodium-depleted group had histopathological evidence of patchy tubular cytoplasmic degeneration in tubules that was not observed in any normal-salt or salt-loaded rat .

Example answer:
{"entities": [{"text": "sodium-depleted", "type": "Chemical"}]}

Example input:
Sentence: Ten rats had arterial , central venous ( CVP ) , and subdural cannulae inserted under halothane anesthesia .

Example answer:
{"entities": [{"text": "halothane", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Thoracic aorta of male Sprague-Dawley rats was exposed to 0.5M CaCl ( 2 ) or normal saline ( NaCl ) .

Example answer:
{"entities": [{"text": "CaCl ( 2 )", "type": "Chemical"}, {"text": "NaCl", "type": "Chemical"}]}

Example input:
Sentence: Permeability of the blood-brain barrier was quantitated by clearance of fluorescent-labeled dextran before and during phenylephrine-induced acute hypertension in rats treated with vehicle and Hoe-140 ( 0.1 microM ) .

Example answer:
{"entities": [{"text": "dextran", "type": "Chemical"}, {"text": "phenylephrine-induced", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "Hoe-140", "type": "Chemical"}]}

Example input:
Sentence: By using transthoracic echocardiography , anterior and posterior wall thickness , LV diameters and LV fractional shortening ( FS ) were measured in all rats before DOX or saline , and at weeks 6 and 9 after treatment in all surviving rats .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Immunofluorescence staining with the MRP2 antibody was found to label a high number of microvessels throughout the brain in normal Wistar rats , whereas such labeling was absent in TR ( - ) rats .

Example answer:
{"entities": []}

Input:
Sentence: Part A , for eight rats in each group brain injury was evaluated by staining tissue using 2,3,5-triphenyltetrazolium chloride and edema was evaluated by microgravimetry .

## Item bc5cdr:test:2945
Example input:
Sentence: Because Warfarin treatment had no effect on the elevation in serum calcium produced by vitamin D , the synergy between Warfarin and vitamin D is probably best explained by the hypothesis that Warfarin inhibits the activity of matrix Gla protein as a calcification inhibitor .

Example answer:
{"entities": [{"text": "Warfarin", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "vitamin D", "type": "Chemical"}, {"text": "calcification", "type": "Disease"}]}

Example input:
Sentence: Although the exact mechanism of hepatotoxicity of these agents is not known , the results suggest that trifluoroacetyl-altered liver proteins are involved .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}, {"text": "trifluoroacetyl-altered", "type": "Chemical"}]}

Example input:
Sentence: High levels of matrix Gla protein are found at sites of artery calcification in rats treated with vitamin D plus Warfarin , and chemical analysis showed that the protein that accumulated was indeed not gamma-carboxylated .

Example answer:
{"entities": [{"text": "artery calcification", "type": "Disease"}, {"text": "vitamin D", "type": "Chemical"}, {"text": "Warfarin", "type": "Chemical"}, {"text": "gamma-carboxylated", "type": "Chemical"}]}

Example input:
Sentence: The aorta/serum-ratio and the radioactive build-up 24 and 48 hours after injection of 131I-HSA was reduced in animals treated with D-pen for 42 days , indicating an impeded transmural transport of tracer which may be caused by a steric exclusion effect of abundant hyaluronate .

Example answer:
{"entities": [{"text": "D-pen", "type": "Chemical"}, {"text": "hyaluronate", "type": "Chemical"}]}

Example input:
Sentence: PURPOSE : This study was designed to establish a rat model of thoracic aortic aneurysm ( TAA ) by calcium chloride ( CaCl ( 2 ) ) -induced arterial injury and to explore the potential role of a disintegrin and metalloproteinase ( ADAM ) , matrix metalloproteinases ( MMPs ) and their endogenous inhibitors ( TIMPs ) in TAA formation .

Example answer:
{"entities": [{"text": "thoracic aortic aneurysm", "type": "Disease"}, {"text": "TAA", "type": "Disease"}, {"text": "calcium chloride", "type": "Chemical"}, {"text": "CaCl ( 2 )", "type": "Chemical"}, {"text": "arterial injury", "type": "Disease"}]}

Example input:
Sentence: The events are consistent with a severe reaction to calcium chelation by sodium citrate anticoagulant resulting in symptomatic systemic hypocalcemia .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "sodium citrate", "type": "Chemical"}, {"text": "hypocalcemia", "type": "Disease"}]}

Example input:
Sentence: We conclude that careful screening for medications and underlying conditions predisposing to hypocalcemia is recommended to help prevent severe reactions due to citrate toxicity .

Example answer:
{"entities": [{"text": "hypocalcemia", "type": "Disease"}, {"text": "citrate", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : This study establishes a TAA model by periarterial CaCl ( 2 ) exposure in rats , and demonstrates a significant elevation of expression of MMP-2 , MMP-9 , ADAM10 and ADAM17 in the pathogenesis of vascular remodeling .

Example answer:
{"entities": [{"text": "TAA", "type": "Disease"}, {"text": "CaCl ( 2 )", "type": "Chemical"}]}

Example input:
Sentence: When instilled directly into the bladder , CAA exerts urotoxic effects , it is , however , susceptible to detoxification with mesna .

Example answer:
{"entities": [{"text": "CAA", "type": "Chemical"}, {"text": "mesna", "type": "Chemical"}]}

Example input:
Sentence: Based on clinical data , indicating that chloroacetaldehyde ( CAA ) is an important metabolite of oxazaphosphorine cytostatics , an experimental study was carried out in order to elucidate the role of CAA in the development of hemorrhagic cystitis .

Example answer:
{"entities": [{"text": "chloroacetaldehyde", "type": "Chemical"}, {"text": "CAA", "type": "Chemical"}]}

Input:
Sentence: Thus , CAA directly reacts with cellular protein and non-protein thiols , mediating its toxicity on hRPTEC .

## Item bc5cdr:test:3054
Example input:
Sentence: CONCLUSIONS : DBP , but not SBP , reduction was associated with neurological worsening after the intravenous administration of high-dose nimodipine after acute stroke .

Example answer:
{"entities": [{"text": "nimodipine", "type": "Chemical"}, {"text": "acute stroke", "type": "Disease"}]}

Example input:
Sentence: End-diastolic ( ED ) and end-systolic ( ES ) LV diameters/BW significantly increased , whereas LV FS was decreased after 9 weeks in the DOX group ( p < 0.001 ) .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: The correlation between average BP change during the first 2 days and the outcome at day 21 was analyzed .

Example answer:
{"entities": []}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}, {"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: Systolic blood pressures ( SBP ) and bodyweights were recorded each alternate day .

Example answer:
{"entities": []}

Example input:
Sentence: The delta down , which is the measure of decrease of SBP after a mechanical breath , was 20.3 +/- 8.4 and 10.1 +/- 3.8 mm Hg in the HEM and SNP groups , respectively , during hypotension ( P less than 0.02 ) .

Example answer:
{"entities": [{"text": "HEM", "type": "Disease"}, {"text": "SNP", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Systolic blood pressure ( SBP ) was measured on alternate days using the tail-cuff method .

Example answer:
{"entities": []}

Example input:
Sentence: After 4-week administration of L-NAME , the systolic blood pressure ( SBP ) increased by 36 % .

Example answer:
{"entities": [{"text": "L-NAME", "type": "Chemical"}]}

Example input:
Sentence: Nimodipine treatment resulted in a statistically significant reduction in systolic BP ( SBP ) and diastolic BP ( DBP ) from baseline compared with placebo during the first few days .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "Chemical"}, {"text": "reduction in systolic BP", "type": "Disease"}]}

Input:
Sentence: Mean changes in MSDBP and mean sitting systolic BP ( MSSBP ) were analyzed at the 8-week core study end point .

## Item bc5cdr:test:2692
Example input:
Sentence: Compared with control patients , CRF and ESRD patients had higher preoperative serum creatinine levels , a greater percentage of patients with hepatorenal syndrome , higher percentage requirement for dialysis in the first 3 months postoperatively , and a higher 1-year serum creatinine .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "hepatorenal syndrome", "type": "Disease"}]}

Example input:
Sentence: Overall , in high-risk patients , warfarin is superior to aspirin in preventing strokes , with a relative risk reduction of 36 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "strokes", "type": "Disease"}]}

Example input:
Sentence: Pooled data from trials comparing antithrombotic treatment with placebo have shown that warfarin reduces the risk of stroke by 62 % , and that aspirin alone reduces the risk by 22 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "stroke", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: Patients developing ESRD had a 6-year survival after onset of ESRD of 27 % for the patients receiving hemodialysis versus 71.4 % for the patients developing ESRD who subsequently received kidney transplants .

Example answer:
{"entities": [{"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: The development of ESRD decreases survival , particularly in those patients treated with dialysis only .

Example answer:
{"entities": [{"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Patients who develop ESRD have a higher preoperative and 1-year serum creatinine and are more likely to have hepatorenal syndrome .

Example answer:
{"entities": [{"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "hepatorenal syndrome", "type": "Disease"}]}

Example input:
Sentence: These studies suggest that both phenacetin and acetaminophen may contribute to the burden of ESRD , with the risk of the latter being somewhat less than that of the former .

Example answer:
{"entities": [{"text": "phenacetin", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Six epidemiologic studies in the United States and Europe indicate that habitual use of phenacetin is associated with the development of chronic renal failure and end-stage renal disease ( ESRD ) , with a relative risk in the range of 4 to 19 .

Example answer:
{"entities": [{"text": "phenacetin", "type": "Chemical"}, {"text": "chronic renal failure", "type": "Disease"}, {"text": "end-stage renal disease", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: The possibility that habitual use of acetaminophen alone increases the risk of ESRD has not been clearly demonstrated , but can not be dismissed .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: However , three case control studies , one each in North Carolina , northern Maryland , and West Berlin , Germany , showed that habitual use of acetaminophen is also associated with chronic renal failure and ESRD , with a relative risk in the range of 2 to 4 .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "chronic renal failure", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Input:
Sentence: The risk of ESRD associated with aspirin was related to the cumulated dose and duration of use , and it was particularly high among the subset of patients with vascular nephropathy as underlying disease [ 2.35 ( 1.17-4.72 ) ] .

## Item bc5cdr:test:2841
Example input:
Sentence: Changes evoked by a single intraperitoneal injection of rilmenidine ( 600 microg/kg ) or alpha-methyldopa ( 100 mg/kg ) , selective I1- and alpha2-receptor agonists , respectively , in blood pressure , hemodynamic variability , and locomotor activity were assessed in radiotelemetered sham-operated and ovariectomized ( Ovx ) Sprague-Dawley female rats with or without 12-wk estrogen replacement .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "estrogen", "type": "Chemical"}]}

Example input:
Sentence: Male Wistar rats were implanted bilaterally with cannulae into the accumbens shell or core , and then were locally injected with GR 55562 ( an antagonist of 5-HT1B receptors ) or CP 93129 ( an agonist of 5-HT1B receptors ) .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Example input:
Sentence: Effects of long-term pretreatment with isoproterenol on bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: TCR prevented the isoproterenol-induced decrease in antioxidant enzymes in the heart and increased the rate of ADP-stimulated oxygen uptake and respiratory coupling ratio .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "ADP-stimulated", "type": "Chemical"}, {"text": "oxygen", "type": "Chemical"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: The electrophysiological recording in vitro showed that Rg1 restored the LTP in slices from the rats treated with morphine , but not changed LTP in the slices from normal saline- or morphine/Rg1-treated rats ; this restoration could be inhibited by N-methyl-D-aspartate ( NMDA ) receptor antagonist MK801 .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}, {"text": "morphine/Rg1-treated", "type": "Chemical"}, {"text": "N-methyl-D-aspartate", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "MK801", "type": "Chemical"}]}

Example input:
Sentence: Chronic hyperprolactinemia induced by the dopamine antagonist sulpiride caused a 40 % reduction LH pulse frequency in ovariectomized rats , but only in the presence of chronic low levels of estradiol .

Example answer:
{"entities": [{"text": "hyperprolactinemia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "sulpiride", "type": "Chemical"}, {"text": "estradiol", "type": "Chemical"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "a reduced locomotor activity", "type": "Disease"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Input:
Sentence: The decrease in the heart rate ( HR ) induced by the beta-AR antagonist metoprolol in conscious rats was significantly attenuated in TGR compared with SD rats ( -9.9 +/- 1.7 % vs. -18.1 +/- 1.5 % ) , whereas the effect of parasympathetic blockade by atropine on HR was similar in both strains .

## Item bc5cdr:test:2706
Example input:
Sentence: Given alone to any accumbal subregion , GR 55562 ( 0.1-10 microg/side ) or CP 93129 ( 0.1-10 microg/side ) did not change basal locomotor activity .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}, {"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : The sensitivity improved dramatically from 16 % to 79 % , positive predictive value increased from 60 % to 68 % and negative predictive value from 54 % to 78 % , and specificity decreased from 90 % to 67 % .

Example answer:
{"entities": []}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: The FK506 plus SRL combination showed only a marginally higher degree of fibrosis as compared with controls ( P=0.05 ) .

Example answer:
{"entities": [{"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: Visual analogue scores ( mean +/- SD ) during induction were lower in Groups L ( 3.3 +/- 2.5 ) and T ( 4.1 +/- 2.7 ) than in Group C ( 5.6 +/- 2.3 ) ; P = 0.0031 .

Example answer:
{"entities": []}

Example input:
Sentence: In the bolus group , 26.0 % ( 13/50 ) had akathisia compared with 32.7 % ( 16/49 ) in the infusion group ( Delta=-6.7 % ; 95 % confidence interval [ CI ] -24.6 % to 11.2 % ) .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: Among the 2000 spots compared for statistical difference , 67 spots were significantly changed in abundance and identified using matrix-assisted laser desorption/ionization time-of-flight MS , atmospheric pressure matrix-assisted laser desorption/ionization and HPLC coupled tandem MS ( LC/MS/MS ) .

Example answer:
{"entities": []}

Example input:
Sentence: Mean post-SCr increases were significantly less with iopamidol ( all patients : 0.07 versus 0.12 mg/dL , 6.2 versus 10.6 micromol/L , P=0.03 ; patients with diabetes : 0.07 versus 0.16 mg/dL , 6.2 versus 14.1 micromol/L , P=0.01 ) .

Example answer:
{"entities": [{"text": "iopamidol", "type": "Chemical"}, {"text": "diabetes", "type": "Disease"}]}

Example input:
Sentence: The semi-quantitative scoring was significantly worst in the group treated with CsA plus SRL ( P < 0.001 compared with controls ) and the analysis of the total grade of fibrosis also showed the highest proportion in the same group and was significantly different from controls ( P < 0.02 ) .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "fibrosis", "type": "Disease"}]}

Input:
Sentence: RESULTS : Densitometry showed no significant difference regarding GAP43-ir in the IML between Pilo , CHX+Pilo , and control groups .

## Item bc5cdr:test:3057
Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: In contrast to controls , methoctramine increased -- instead of decreased -- the tonic responses at high frequencies .

Example answer:
{"entities": [{"text": "methoctramine", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : The mean hemoglobin ( Hb ) levels were significantly declined in all patients from baseline of 14.2 g/dl to 14.0 g/dl , 13.5 g/dl , 13.2 g/dl and 12.7 g/dl at 1 , 2 , 3 and 6 months post-CAB , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: Patients with a DBP reduction of > or =20 % in the high-dose group had a significantly increased adjusted OR for the compound outcome variable death or dependency ( Barthel Index < 60 ) ( n/N=25/26 , OR 10 .

Example answer:
{"entities": [{"text": "DBP reduction", "type": "Disease"}, {"text": "death", "type": "Disease"}]}

Example input:
Sentence: The maximal NGF contents obtained by PG-9 were 17.6-fold of the control value .

Example answer:
{"entities": []}

Example input:
Sentence: Controlled hypotension in groups A and C was induced with PGE1 to maintain mean arterial blood pressure at 55 mmHg for 180 min .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "PGE1", "type": "Chemical"}]}

Example input:
Sentence: The delta down , which is the measure of decrease of SBP after a mechanical breath , was 20.3 +/- 8.4 and 10.1 +/- 3.8 mm Hg in the HEM and SNP groups , respectively , during hypotension ( P less than 0.02 ) .

Example answer:
{"entities": [{"text": "HEM", "type": "Disease"}, {"text": "SNP", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: ) , a positive control , showed only 30 % inhibition .

Example answer:
{"entities": []}

Example input:
Sentence: Sham-operated rats served as normotensive controls ( 128 +/- 3 mm Hg , n = 8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Controlled hypotension to an average MAP of 50-55 mm Hg was induced by increasing the dose of isoflurane , and maintained at an inspired concentration of 2.2 +/- 0.2 % .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "Hg", "type": "Chemical"}, {"text": "isoflurane", "type": "Chemical"}]}

Input:
Sentence: Control was defined as MSDBP < 90 mm Hg compared with baseline .

## Item bc5cdr:test:2912
Example input:
Sentence: Liver function tests , hepatitis B virus ( HBV ) serologic markers , and HBV DNA levels of the patients during follow-up were obtained from hospital file records .

Example answer:
{"entities": [{"text": "hepatitis B", "type": "Disease"}]}

Example input:
Sentence: Twenty-three hours after heart transplantation , life-threatening acute right heart failure was diagnosed in a patient requiring continuous venovenous hemodiafiltration ( CVVHDF ) .

Example answer:
{"entities": [{"text": "right heart failure", "type": "Disease"}]}

Example input:
Sentence: Hepatitis B virus ( HBV ) is one of the major causes of chronic liver disease worldwide .

Example answer:
{"entities": [{"text": "Hepatitis B", "type": "Disease"}, {"text": "liver disease", "type": "Disease"}]}

Example input:
Sentence: HBV lamivudine-resistant strains were detected in 3 of 15 mono-infected chronic hepatitis B patients and 10 of 20 HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "lamivudine-resistant", "type": "Chemical"}, {"text": "hepatitis B", "type": "Disease"}]}

Example input:
Sentence: In this study , cancer patients who have solid and hematological malignancies with chronic HBV infection received the antiviral agent lamivudine prior and during CT compared with historical control group who did not receive lamivudine .

Example answer:
{"entities": [{"text": "cancer", "type": "Disease"}, {"text": "hematological malignancies", "type": "Disease"}, {"text": "HBV infection", "type": "Disease"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: The patient cohort ( 14 men , 11 women ) was treated with SRL as conversion therapy , due to chronic allograft nephropathy ( CAN ) ( n = 15 ) neoplasia ( n = 8 ) ; Kaposi 's sarcoma , Four skin cancers , One intestinal tumors , One renal cell carsinom ) or BK virus nephropathy ( n = 2 ) .

Example answer:
{"entities": [{"text": "SRL", "type": "Chemical"}, {"text": "chronic allograft nephropathy", "type": "Disease"}, {"text": "CAN", "type": "Disease"}, {"text": "neoplasia", "type": "Disease"}, {"text": "Kaposi 's sarcoma", "type": "Disease"}, {"text": "skin cancers", "type": "Disease"}, {"text": "intestinal tumors", "type": "Disease"}, {"text": "renal cell carsinom", "type": "Disease"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: Despite therapy with ursodeoxycholic acid , prednisone , and then tacrolimus , her cholestatic disease was unrelenting , with cirrhosis shown by biopsy 6 months after presentation .

Example answer:
{"entities": [{"text": "ursodeoxycholic acid", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "cholestatic disease", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}]}

Example input:
Sentence: The latter group was further sub-divided into 13 occult HBV ( HBsAg-negative ) and 7 overt HBV ( HBsAg- positive ) patients .

Example answer:
{"entities": [{"text": "HBsAg-negative", "type": "Chemical"}, {"text": "HBsAg-", "type": "Chemical"}]}

Example input:
Sentence: Cancer patients who are chronic carriers of HBV have a higher hepatic complication rate while receiving cytotoxic chemotherapy ( CT ) and this has mainly been attributed to HBV reactivation .

Example answer:
{"entities": [{"text": "Cancer", "type": "Disease"}, {"text": "hepatic complication", "type": "Disease"}]}

Example input:
Sentence: From June 2004 to October 2006 , 11 HBs Ag positive patients with rheumatologic diseases , who were on both immunosuppressive and prophylactic lamivudine therapies , were retrospectively assessed .

Example answer:
{"entities": [{"text": "HBs Ag", "type": "Chemical"}, {"text": "rheumatologic diseases", "type": "Disease"}, {"text": "lamivudine", "type": "Chemical"}]}

Input:
Sentence: METHODS : A retrospective chart analysis and a review of the organ transplant database identified 51 patients ( 43 men and 8 women ) transplanted for benign HBV-related cirrhotic diseases between June 2002 and December 2004 who had survived more than 3 months .

## Item bc5cdr:test:2612
Example input:
Sentence: CONCLUSION : This rat study demonstrated a synergistic nephrotoxic effect of CsA plus SRL , whereas FK506 plus SRL was better tolerated .

Example answer:
{"entities": [{"text": "nephrotoxic", "type": "Disease"}, {"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}]}

Example input:
Sentence: The results suggest a possible involvement of the renin-angiotensin system in the development of puromycin aminonucleoside-induced nephrosis .

Example answer:
{"entities": [{"text": "puromycin", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: Serum- and glucocorticoid-inducible kinase 1 in doxorubicin-induced nephrotic syndrome .

Example answer:
{"entities": [{"text": "doxorubicin-induced", "type": "Chemical"}, {"text": "nephrotic syndrome", "type": "Disease"}]}

Example input:
Sentence: Two patients developed acute tubular necrosis , characterized clinically by acute oliguric renal failure , while they were receiving a combination of cephalothin sodium and gentamicin sulfate therapy .

Example answer:
{"entities": [{"text": "acute tubular necrosis", "type": "Disease"}, {"text": "cephalothin sodium", "type": "Chemical"}, {"text": "gentamicin sulfate", "type": "Chemical"}]}

Example input:
Sentence: Thus , gentamicin was associated with renal failure more than three times as often as was tobramycin .

Example answer:
{"entities": [{"text": "gentamicin", "type": "Chemical"}, {"text": "renal failure", "type": "Disease"}, {"text": "tobramycin", "type": "Chemical"}]}

Example input:
Sentence: Puromycin aminonucleoside nephrosis was induced by single intraperitoneal injection of puromycin aminonucleoside ( PAN , 20 mg/100g BW ) .

Example answer:
{"entities": [{"text": "Puromycin aminonucleoside", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : As anticipated , adriamycin elicited nephrotic range proteinuria , renal interstitial damage and mild focal glomerulosclerosis .

Example answer:
{"entities": [{"text": "adriamycin", "type": "Chemical"}, {"text": "nephrotic", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "renal interstitial damage", "type": "Disease"}, {"text": "focal glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: Doxorubicin-induced nephropathy leads to epithelial sodium channel ( ENaC ) -dependent volume retention and renal fibrosis .

Example answer:
{"entities": [{"text": "Doxorubicin-induced", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "sodium", "type": "Chemical"}, {"text": "volume retention", "type": "Disease"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: In this study , 62 patients with confirmed initial normal renal function and treated with 2 to 5 mg/kg/day of gentamicin sulfate or tobramycin sulfate for a minimum of seven days were followed up prospectively for the development of aminoglycoside-related renal failure , defined as at least a one-third reduction in renal function .

Example answer:
{"entities": [{"text": "gentamicin sulfate", "type": "Chemical"}, {"text": "tobramycin sulfate", "type": "Chemical"}, {"text": "aminoglycoside-related", "type": "Chemical"}, {"text": "renal failure", "type": "Disease"}]}

Input:
Sentence: CONCLUSIONS : These data show that inhibition of NF-kappaB activation attenuates tubulointerstitial nephritis induced by gentamicin .

## Item bc5cdr:test:2846
Example input:
Sentence: In contrast to controls , methoctramine increased -- instead of decreased -- the tonic responses at high frequencies .

Example answer:
{"entities": [{"text": "methoctramine", "type": "Chemical"}]}

Example input:
Sentence: This article describes two critically ill patients in whom transient episodes of hypotension reproducibly developed after administration of acetaminophen .

Example answer:
{"entities": [{"text": "critically ill", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}, {"text": "acetaminophen", "type": "Chemical"}]}

Example input:
Sentence: More patients were ( completely , very or somewhat ) satisfied 2 h after treatment with rizatriptan ( 69.8 % ) than at 2 h after treatment with ergotamine/caffeine ( 38.6 % , p < or = 0.001 ) .

Example answer:
{"entities": [{"text": "rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}]}

Example input:
Sentence: These data indicate that the free ED50 in plasma for terfenadine ( 1.9 nM ) , terodiline ( 76 nM ) , cisapride ( 11 nM ) and E4031 ( 1.9 nM ) closely correlate with the free concentration in man causing QT effects .

Example answer:
{"entities": [{"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}, {"text": "E4031", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Methamphetamine is a very addictive , powerful stimulant that increases wakefulness and physical activity and can produce other effects such as cardiac dysrhythmias , hypertension , hallucinations , and violent behavior .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "Chemical"}, {"text": "cardiac dysrhythmias", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "hallucinations", "type": "Disease"}, {"text": "violent behavior", "type": "Disease"}]}

Example input:
Sentence: Impotence was more common among male patients than controls and was found to be associated with co-morbidity and the taking of methotrexate .

Example answer:
{"entities": [{"text": "Impotence", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: However , marked tachycardia associated with the use of ephedrine in combination with propofol occurred in the majority of patients , occasionally reaching high levels in individual patients .

Example answer:
{"entities": [{"text": "tachycardia", "type": "Disease"}, {"text": "ephedrine", "type": "Chemical"}, {"text": "propofol", "type": "Chemical"}]}

Example input:
Sentence: Choreoathetoid movements associated with rapid adjustment to methadone .

Example answer:
{"entities": [{"text": "Choreoathetoid movements", "type": "Disease"}, {"text": "methadone", "type": "Chemical"}]}

Example input:
Sentence: This is a case report of euphoria and choreoathetoid movements both transiently induced by rapid adjustment to the selective mu-opioid receptor agonist methadone in an inpatient previously abusing heroine and cocaine .

Example answer:
{"entities": [{"text": "choreoathetoid movements", "type": "Disease"}, {"text": "methadone", "type": "Chemical"}, {"text": "heroine", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Four compounds known to increase QT interval and cause TDP were investigated : terfenadine , terodiline , cisapride and E4031 .

Example answer:
{"entities": [{"text": "TDP", "type": "Disease"}, {"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}, {"text": "E4031", "type": "Chemical"}]}

Input:
Sentence: In the inpatient setting , the frequency of QT interval prolongation with methadone treatment , its dose dependence , and the importance of cofactors such as drug-drug interactions remain unknown .
