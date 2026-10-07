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

## Item bc5cdr:test:4074
Example input:
Sentence: Total cumulative doses were 36 or 60 g/m2 of ifosfamide ( six or 10 cycles of ifosfamide , vincristine , and dactinomycin [ IVA ] ) .

Example answer:
{"entities": [{"text": "ifosfamide", "type": "Chemical"}, {"text": "ifosfamide , vincristine , and dactinomycin", "type": "Chemical"}, {"text": "IVA", "type": "Chemical"}]}

Example input:
Sentence: In the current study the efficacy and toxicity of the combination of GEM and VNB in elderly patients with advanced NSCLC or those with some contraindication to receiving cisplatin were assessed .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "GEM", "type": "Chemical"}, {"text": "VNB", "type": "Chemical"}, {"text": "NSCLC", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: injections of organ specific three drugs ( AAP : 500 mg/Kg for 24 h ; AMI : 50 mg/Kg/day for four days ; DOX : 20 mg/Kg for 48 h ) .

Example answer:
{"entities": [{"text": "AAP", "type": "Chemical"}, {"text": "AMI", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: For the cytoprotection study , animals were orally gavaged 100 mg/Kg GSPE for 7-10 days followed by i.p .

Example answer:
{"entities": [{"text": "GSPE", "type": "Chemical"}]}

Example input:
Sentence: Treatment , given every 21 days for a maximum of three cycles , consisted of paclitaxel by 3-hour infusion followed the next day by a fixed dose of cisplatin ( 75 mg/m2 ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: Recent reports indicate that single agent therapy with vinorelbine ( VNB ) or gemcitabine ( GEM ) may obtain a response rate of 20-30 % in elderly patients , with acceptable toxicity and improvement in symptoms and quality of life .

Example answer:
{"entities": [{"text": "vinorelbine", "type": "Chemical"}, {"text": "VNB", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "GEM", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: After 154 courses of therapy , the median dose intensity was 131 mg/m ( 2 ) for paclitaxel ( 97.3 % ) , 117 mg/m ( 2 ) for cisplatin ( 97.3 % ) , and 1378 mg/m ( 2 ) for gemcitabine ( 86.2 % ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : The combination of GEM and VNB is moderately active and well tolerated except in patients age > /= 75 years .

Example answer:
{"entities": [{"text": "GEM", "type": "Chemical"}, {"text": "VNB", "type": "Chemical"}]}

Example input:
Sentence: A median of 2 cycles of therapy was administered to the 37 eligible patients .

Example answer:
{"entities": []}

Example input:
Sentence: Treatment was comprised of VNB , 25 mg/m ( 2 ) , plus GEM , 1000 mg/m ( 2 ) , both on Days 1 , 8 , and 15 every 28 days .

Example answer:
{"entities": [{"text": "VNB", "type": "Chemical"}, {"text": "GEM", "type": "Chemical"}]}

Input:
Sentence: One hundred and twenty-two cycles of GEM-P were administered in total ( median 3 cycles ; range 1-6 ) .

## Item bc5cdr:test:4078
Example input:
Sentence: Seventeen of these had a response or were stable for a median of 20 weeks ( range 6 to more than 66 weeks ) .

Example answer:
{"entities": []}

Example input:
Sentence: Mean follow-up on SRL therapy was 20 +/- 12 ( 6 to 43 ) months .

Example answer:
{"entities": [{"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: Treatment was comprised of VNB , 25 mg/m ( 2 ) , plus GEM , 1000 mg/m ( 2 ) , both on Days 1 , 8 , and 15 every 28 days .

Example answer:
{"entities": [{"text": "VNB", "type": "Chemical"}, {"text": "GEM", "type": "Chemical"}]}

Example input:
Sentence: Eleven patients ( six male ) with median age 47 years ( range 27-73 ) , median disease duration 50 months ( range 9-178 ) and median follow-up period of patients 13.8 months ( range 5-27 ) were enrolled in this study .

Example answer:
{"entities": []}

Example input:
Sentence: The follow-up period was 12 months .

Example answer:
{"entities": []}

Example input:
Sentence: The median time to progression was 16 weeks and the 1-year survival rate was 33 % .

Example answer:
{"entities": []}

Example input:
Sentence: Median progression-free survival was 5 months .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSIONS : The combination of GEM and VNB is moderately active and well tolerated except in patients age > /= 75 years .

Example answer:
{"entities": [{"text": "GEM", "type": "Chemical"}, {"text": "VNB", "type": "Chemical"}]}

Example input:
Sentence: After a median follow-up of 22 months , the median progression free survival rate was 7 months , and the median survival time was 16 months .

Example answer:
{"entities": []}

Example input:
Sentence: The median follow-up period was 14 months .

Example answer:
{"entities": []}

Input:
Sentence: Median follow-up from the start of GEM-P was 4.5 years .

## Item bc5cdr:test:3965
Example input:
Sentence: This retrospective study examines the incidence and treatment of ESRD and chronic renal failure ( CRF ) in OLTX patients .

Example answer:
{"entities": [{"text": "ESRD", "type": "Disease"}, {"text": "chronic renal failure", "type": "Disease"}, {"text": "CRF", "type": "Disease"}]}

Example input:
Sentence: PTCR also occurs in certain native kidney diseases , though the association is not as strong as that for TG .

Example answer:
{"entities": [{"text": "kidney diseases", "type": "Disease"}, {"text": "TG", "type": "Disease"}]}

Example input:
Sentence: We suggest that our patient 's tubular dysfunction and myopathy may have resulted from mitochondrial dysfunction which is triggered by tacrolimus and augmented by lamivudine .

Example answer:
{"entities": [{"text": "tubular dysfunction", "type": "Disease"}, {"text": "myopathy", "type": "Disease"}, {"text": "mitochondrial dysfunction", "type": "Disease"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: In all clones with combined immune escape and LAM resistance mutations , the nucleotide analogues adefovir and tenofovir remained effective in suppressing viral replication in vitro .

Example answer:
{"entities": [{"text": "LAM", "type": "Chemical"}, {"text": "nucleotide", "type": "Chemical"}, {"text": "adefovir", "type": "Chemical"}, {"text": "tenofovir", "type": "Chemical"}]}

Example input:
Sentence: The clinical utility of FK 506 is complicated by substantial hypertension and nephrotoxicity .

Example answer:
{"entities": [{"text": "FK 506", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "nephrotoxicity", "type": "Disease"}]}

Example input:
Sentence: RESULTS : As anticipated , adriamycin elicited nephrotic range proteinuria , renal interstitial damage and mild focal glomerulosclerosis .

Example answer:
{"entities": [{"text": "adriamycin", "type": "Chemical"}, {"text": "nephrotic", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "renal interstitial damage", "type": "Disease"}, {"text": "focal glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : This study demonstrates that chronic FK506 nephropathy consists primarily of arteriolopathy manifesting as insudative hyalinosis of the arteriolar wall , and suggests that mild-type chronic FK506 nephropathy is a condition which may lead to deterioration of renal allograft function .

Example answer:
{"entities": [{"text": "FK506", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : At 13 years after OLTX , the incidence of severe renal dysfunction was 18.1 % ( CRF 8.6 % and ESRD 9.5 % ) .

Example answer:
{"entities": [{"text": "renal dysfunction", "type": "Disease"}, {"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Input:
Sentence: The potential for tenofovir to cause a range of kidney syndromes has been established from mechanistic and randomised clinical trials .

## Item bc5cdr:test:3768
Example input:
Sentence: Using puromycin aminonucleoside nephrosis ( PAN ) rats , we studied early ultrastructural and permeability changes in relation to the expression of the podocyte-associated molecules nephrin , a-actinin , dendrin , and plekhh2 , the last two of which were only recently discovered in podocytes .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: Endothelial-dependent relaxation and eNOS mRNA expression were greater in the Dex + Ato group than in the Dex only group ( P < 0.05 and P < 0.0001 , respectively ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}, {"text": "Ato", "type": "Chemical"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "Chemical"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Azidothymidine ( AZT ) -induced anemia in mice can be reversed by the administration of IGF-IL-3 ( fusion protein of insulin-like growth factor II ( IGF II ) and interleukin 3 ) .

Example answer:
{"entities": [{"text": "Azidothymidine", "type": "Chemical"}, {"text": "AZT", "type": "Chemical"}, {"text": "anemia", "type": "Disease"}]}

Example input:
Sentence: Bovine liver erythroid cells were cultured on monolayers of human bone marrow endothelial cells previously treated with EPO and IGF-IL-3 .

Example answer:
{"entities": []}

Example input:
Sentence: There was a significant reduction of thymidine incorporation into both erythroid and endothelial cells in cultures pre-treated with IGF-IL-3 and EPO .

Example answer:
{"entities": [{"text": "thymidine", "type": "Chemical"}]}

Example input:
Sentence: Endothelial cell culture supernatants separated by ultrafiltration and ultracentrifugation from cells treated with EPO and IL-3 significantly reduced thymidine incorporation into erythroid cells as compared to identical fractions obtained from the media of cells cultured with EPO alone .

Example answer:
{"entities": [{"text": "thymidine", "type": "Chemical"}]}

Example input:
Sentence: At termination of the experiments , mice underwent echocardiography , quantitation of abundance of molecular markers of CM ( ventricular mRNA encoding atrial natriuretic factor [ ANF ] and sarcoplasmic calcium ATPase [ SERCA2 ] ) , and determination of plasma LA .

Example answer:
{"entities": [{"text": "CM", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "LA", "type": "Chemical"}]}

Input:
Sentence: RESEARCH DESIGN AND METHODS : EndoMT was induced in a mouse pancreatic microvascular endothelial cell line ( MMEC ) in the presence of advanced glycation end products ( AGEs ) and in the endothelial lineage-traceble mouse line Tie2-Cre ; Loxp-EGFP by administration of AGEs , with nonglycated mouse albumin serving as a control .

## Item bc5cdr:test:3995
Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: The correlation between neuropathic damage and inhibition of neurotoxic esterase or neuropathy target enzyme ( NTE ) was examined in rats acutely exposed to Mipafox ( N , N'-diisopropylphosphorodiamidofluoridate ) , a neurotoxic organophosphate .

Example answer:
{"entities": [{"text": "neuropathic damage", "type": "Disease"}, {"text": "neurotoxic", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}, {"text": "Mipafox", "type": "Chemical"}, {"text": "N , N'-diisopropylphosphorodiamidofluoridate", "type": "Chemical"}, {"text": "organophosphate", "type": "Chemical"}]}

Example input:
Sentence: Reversible inferior colliculus lesion in metronidazole-induced encephalopathy : magnetic resonance findings on diffusion-weighted and fluid attenuated inversion recovery imaging .

Example answer:
{"entities": [{"text": "inferior colliculus lesion", "type": "Disease"}, {"text": "metronidazole-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Peripheral neuropathy has been noted as a complication of therapy with perhexiline maleate , a drug widely used in France ( and in clinical trials in the United States ) for the prophylactic treatment of angina pectoris .

Example answer:
{"entities": [{"text": "Peripheral neuropathy", "type": "Disease"}, {"text": "perhexiline maleate", "type": "Chemical"}, {"text": "angina pectoris", "type": "Disease"}]}

Example input:
Sentence: Compression neuropathy of the radial nerve due to pentazocine-induced fibrous myopathy .

Example answer:
{"entities": [{"text": "pentazocine-induced", "type": "Chemical"}, {"text": "fibrous myopathy", "type": "Disease"}]}

Example input:
Sentence: These data indicate that a critical percentage of NTE inhibition in brain and spinal cord sampled shortly after Mipafox exposure can predict neuropathic damage in rats several weeks later .

Example answer:
{"entities": [{"text": "Mipafox", "type": "Chemical"}, {"text": "neuropathic damage", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Reversible inferior colliculus lesions could be considered as the characteristic for metronidazole-induced encephalopathy , next to the dentate nucleus involvement .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "Disease"}, {"text": "metronidazole-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVE : This is to present reversible inferior colliculus lesions in metronidazole-induced encephalopathy , to focus on the diffusion-weighted imaging ( DWI ) and fluid attenuated inversion recovery ( FLAIR ) imaging .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "Disease"}, {"text": "metronidazole-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: The full syndrome of subacute myelo-optic neuropathy was more frequent in women , but they tended to have taken greater quantities of the drug .

Example answer:
{"entities": []}

Example input:
Sentence: Isoniazid was the most frequent agent in drug-induced neuropathy .

Example answer:
{"entities": [{"text": "Isoniazid", "type": "Chemical"}, {"text": "neuropathy", "type": "Disease"}]}

Input:
Sentence: Linezolid-induced optic neuropathy .

## Item bc5cdr:test:3765
Example input:
Sentence: Patients who developed renal insufficiency had lower baseline body weight and higher baseline serum creatinine , required higher doses of loop diuretics , and were more likely to be treated with thiazide diuretics than controls .

Example answer:
{"entities": [{"text": "renal insufficiency", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "thiazide", "type": "Chemical"}]}

Example input:
Sentence: Patients who developed hyperkalemia were older and more likely to have diabetes , had higher baseline serum potassium levels and lower baseline potassium supplement doses , and were more likely to be treated with beta-blockers than controls ( n = 134 ) .

Example answer:
{"entities": [{"text": "hyperkalemia", "type": "Disease"}, {"text": "diabetes", "type": "Disease"}, {"text": "potassium", "type": "Chemical"}]}

Example input:
Sentence: Furthermore , glomerulosclerosis index was significantly increased in the nitrendipine-treated group compared with the hypertensive controls ( 0.38 +/- 0.1 versus 0.13 +/- 0.04 ) .

Example answer:
{"entities": [{"text": "glomerulosclerosis", "type": "Disease"}, {"text": "nitrendipine-treated", "type": "Chemical"}, {"text": "hypertensive", "type": "Disease"}]}

Example input:
Sentence: We propose that amphotericin , in the setting of reduced effective arterial volume , may activate tubuloglomerular feedback , thereby contributing to acute renal failure .

Example answer:
{"entities": [{"text": "amphotericin", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: ACE inhibitor and angiotensin-releasing blocker ( ARB ) therapy reduced proteinuria development .

Example answer:
{"entities": [{"text": "ACE inhibitor", "type": "Chemical"}, {"text": "angiotensin-releasing blocker", "type": "Chemical"}, {"text": "ARB", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: The results suggest a possible involvement of the renin-angiotensin system in the development of puromycin aminonucleoside-induced nephrosis .

Example answer:
{"entities": [{"text": "puromycin", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: In this patient , renal artery stenosis combined with heart failure and diuretic therapy certainly resulted in a strong activation of the renin-angiotensin system ( RAS ) .

Example answer:
{"entities": [{"text": "renal artery stenosis", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}]}

Example input:
Sentence: The effect of a 6-week treatment with the calcium channel blocker nitrendipine or the angiotensin converting enzyme inhibitor enalapril on blood pressure , albuminuria , renal hemodynamics , and morphology of the nonclipped kidney was studied in rats with two-kidney , one clip renovascular hypertension .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "nitrendipine", "type": "Chemical"}, {"text": "angiotensin", "type": "Chemical"}, {"text": "enalapril", "type": "Chemical"}, {"text": "albuminuria", "type": "Disease"}, {"text": "renovascular hypertension", "type": "Disease"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : The rate of contrast-induced nephropathy , defined by multiple end points , is not statistically different after the intraarterial administration of iopamidol or iodixanol to high-risk patients , with or without diabetes mellitus .

Example answer:
{"entities": [{"text": "nephropathy", "type": "Disease"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}, {"text": "diabetes mellitus", "type": "Disease"}]}

Input:
Sentence: OBJECTIVE : A multicenter , controlled trial showed that early blockade of the renin-angiotensin system in patients with type 1 diabetes and normoalbuminuria did not retard the progression of nephropathy , suggesting that other mechanism ( s ) are involved in the pathogenesis of early diabetic nephropathy ( diabetic nephropathy ) .

## Item bc5cdr:test:4000
Example input:
Sentence: RESULT ( S ) : A 36-year-old Chinese woman developed central retinal vein occlusion after eight courses of CC .

Example answer:
{"entities": [{"text": "retinal vein occlusion", "type": "Disease"}, {"text": "CC", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVE : This is to present reversible inferior colliculus lesions in metronidazole-induced encephalopathy , to focus on the diffusion-weighted imaging ( DWI ) and fluid attenuated inversion recovery ( FLAIR ) imaging .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "Disease"}, {"text": "metronidazole-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: At presentation , advanced encephalopathy and cerebral edema were present in 51 ( 76 % ) and 29 ( 41.4 % ) patients , respectively .

Example answer:
{"entities": [{"text": "encephalopathy", "type": "Disease"}, {"text": "cerebral edema", "type": "Disease"}]}

Example input:
Sentence: Ophthalmologic examinations showed ptosis on the right upper lid and restricted right eye movement without any other neurological signs .

Example answer:
{"entities": [{"text": "ptosis on the right upper lid", "type": "Disease"}, {"text": "restricted right eye movement", "type": "Disease"}]}

Example input:
Sentence: A delayed complication in nine patients has been unilateral loss of vision secondary to a retinal vasculitis .

Example answer:
{"entities": [{"text": "loss of vision", "type": "Disease"}, {"text": "retinal vasculitis", "type": "Disease"}]}

Example input:
Sentence: In the remaining cases , a combination of myelopathy , visual disturbance , and peripheral neuropathy was the most common manifestation .

Example answer:
{"entities": [{"text": "myelopathy", "type": "Disease"}, {"text": "visual disturbance", "type": "Disease"}, {"text": "peripheral neuropathy", "type": "Disease"}]}

Example input:
Sentence: Fundus fluorescein angiography confirmed macular capillary closure and telangiectasis .

Example answer:
{"entities": [{"text": "fluorescein", "type": "Chemical"}, {"text": "telangiectasis", "type": "Disease"}]}

Example input:
Sentence: Visual toxicity was of retinal origin and was characterized by a tritan-type dyschromatopsy , sometimes associated with a loss of visual acuity and pigmentary retinal deposits .

Example answer:
{"entities": [{"text": "Visual toxicity", "type": "Disease"}, {"text": "dyschromatopsy", "type": "Disease"}, {"text": "a loss of visual acuity", "type": "Disease"}, {"text": "pigmentary retinal deposits", "type": "Disease"}]}

Example input:
Sentence: Although the intraocular pressure elevation caused by secondary acute angle-closure glaucoma decreased and ocular pain diminished , inexorable papilledema and exudative retinal detachment continued for 3 weeks .

Example answer:
{"entities": [{"text": "glaucoma", "type": "Disease"}, {"text": "ocular pain", "type": "Disease"}, {"text": "papilledema", "type": "Disease"}, {"text": "retinal detachment", "type": "Disease"}]}

Example input:
Sentence: Finally , 6 weeks later , diffuse chorioretinal atrophy with optic atrophy occurred and the vision in his left eye was lost .

Example answer:
{"entities": [{"text": "chorioretinal atrophy", "type": "Disease"}, {"text": "optic atrophy", "type": "Disease"}]}

Input:
Sentence: Color vision was defective and fundus examination revealed optic disc edema in both eyes .

## Item bc5cdr:test:4142
Example input:
Sentence: The primary outcome was a postdose SCr increase > or = 0.5 mg/dL ( 44.2 micromol/L ) over baseline .

Example answer:
{"entities": []}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: Following polytherapy according to the CMF regimen , a statistically significant decrease ( p = 0.0343 ) in creatinine clearance was found , but creatinine concentration did not increase significantly compared to controls .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: Patients with a DBP reduction of > or =20 % in the high-dose group had a significantly increased adjusted OR for the compound outcome variable death or dependency ( Barthel Index < 60 ) ( n/N=25/26 , OR 10 .

Example answer:
{"entities": [{"text": "DBP reduction", "type": "Disease"}, {"text": "death", "type": "Disease"}]}

Example input:
Sentence: Two weeks after the initiation of therapy , her hematocrit had decreased from 44.1 % to 20.4 % , and she had a positive direct Coombs antiglobulin test and an elevated indirect bilirubin .

Example answer:
{"entities": [{"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : This rat study demonstrated a synergistic nephrotoxic effect of CsA plus SRL , whereas FK506 plus SRL was better tolerated .

Example answer:
{"entities": [{"text": "nephrotoxic", "type": "Disease"}, {"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Using in vivo microdialysis , we compared acute exposure ( 450 mg/kg ) to an identical sub-chronic exposure ( 150 mg/kg per day for 3 days ) , followed by 1- or 3-day washout .

Example answer:
{"entities": []}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}, {"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: Severe toxicity was correlated with the higher cumulative dose of 60 g/m2 of ifosfamide , a younger age ( less than 2 1/2 years old ) , and a predominance of vesicoprostatic tumor involvement .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "tumor", "type": "Disease"}]}

Example input:
Sentence: Dex increased SBP ( 110 +/- 2-126 +/- 3 mmHg ; P < 0.001 ) and decreased thymus ( P < 0.001 ) and bodyweights ( P '' < 0.01 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}, {"text": "increased SBP", "type": "Disease"}, {"text": "decreased thymus ( P < 0.001 ) and bodyweights", "type": "Disease"}]}

Input:
Sentence: The chronological study showed an effect of a cumulative dose on body weight ( R = -0.99 , p = 0.011 ) , necrosis ( R = 1.00 , p = 0.004 ) , TAP ( R = 0.95 , p = 0.049 ) , and DNA SBs ( R = -0.95 , p = 0.049 ) .

## Item bc5cdr:test:4162
Example input:
Sentence: All rats were terminated either 24 h or 3 weeks after the DFP injection .

Example answer:
{"entities": [{"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: Rats were treated with the vehicle ( 2 mL/kg of distilled water and 5 % w/v cellulose , 10 days ) , gum Arabic ( 2 mL/kg of a 10 % w/v aqueous suspension of gum Arabic powder , orally for 10 days ) , or gum Arabic concomitantly with GM ( 80mg/kg/day intramuscularly , during the last six days of the treatment period ) .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}]}

Example input:
Sentence: After gastric surgery , rat stomachs were irrigated for 3 h with either simulated gastric juice or normal saline .

Example answer:
{"entities": []}

Example input:
Sentence: Control rats received halothane anesthesia ( 1 MAC ) for one hour , followed by SNP infusion , 40 microgram/kg/min , for 30 min , followed by a 30-min recovery period .

Example answer:
{"entities": [{"text": "halothane", "type": "Chemical"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: Male SD rats ( n = 30 ) were treated with Ato ( 50 mg/kg per day in drinking water ) or tap water for 15 days .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}]}

Example input:
Sentence: All of the rats in the saline-treated epileptic control group developed SRS , whereas none of the BMC-treated epileptic animals had seizures in the short term ( 15 days after transplantation ) , regardless of the BMC source .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}, {"text": "SRS", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Over a range of 1-150 days of DES treatment , pairs of control and DES-treated rats were sacrificed , and their pituitaries dissociated enzymatically into single-cell preparations .

Example answer:
{"entities": [{"text": "DES", "type": "Chemical"}, {"text": "DES-treated", "type": "Chemical"}]}

Example input:
Sentence: Rats treated for 11 days with morphine and withdrawn for 36-40 h showed differences in the development of tolerance : about half of the animals showed a rigidity after the test dose of morphine that was not significantly less than in the controls and were akinetic ( A group ) .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "rigidity", "type": "Disease"}, {"text": "akinetic", "type": "Disease"}]}

Example input:
Sentence: In contrast , in normal-salt rats creatinine clearance was decreased but to a lesser extent at week 2 and 3 , and in salt-loaded rats creatinine clearance did not change for 2 weeks and was decreased by 43 % at week 3 .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "Chemical"}, {"text": "Ato-treated", "type": "Chemical"}]}

Input:
Sentence: The saline- and apigenin-treated rats that did not step through into the dark compartment during the cut-off time ( 540 s ) were retested weekly for up to eight weeks .

## Item bc5cdr:test:3934
Example input:
Sentence: Although preclinical and clinical findings suggest pulsatile stimulation of striatal postsynaptic receptors as a key mechanism underlying levodopa-induced dyskinesias , their pathogenesis is still unclear .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: Recent preclinical and clinical data from promising lines of research focus on the differential role of presynaptic versus postsynaptic mechanisms , dopamine receptor subtypes , ionotropic and metabotropic glutamate receptors , and non-dopaminergic neurotransmitter systems in the pathophysiology of levodopa-induced dyskinesias .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: Seven patients suffering from Parkinson 's disease ( PD ) with severely disabling dyskinesia received low-dose propranolol as an adjunct to the currently used medical treatment .

Example answer:
{"entities": [{"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "propranolol", "type": "Chemical"}]}

Example input:
Sentence: L-DOPA-induced dyskinesia ( LID ) is among the motor complications that arise in Parkinson 's disease ( PD ) patients after a prolonged treatment with L-DOPA .

Example answer:
{"entities": [{"text": "L-DOPA-induced", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "LID", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "L-DOPA", "type": "Chemical"}]}

Example input:
Sentence: Monkeys with acute ( short-term ) MPTP exposure , rapid symptom onset and short symptom duration prior to initiation of levodopa therapy developed dyskinesia between 11 and 24 days of daily levodopa administration .

Example answer:
{"entities": [{"text": "MPTP", "type": "Chemical"}, {"text": "levodopa", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Improvement of levodopa-induced dyskinesia by propranolol in Parkinson 's disease .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "propranolol", "type": "Chemical"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: Repetitive transcranial magnetic stimulation for levodopa-induced dyskinesias in Parkinson 's disease .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: Levodopa-induced dyskinesias ( LIDs ) present a major problem for the long-term management of Parkinson 's disease ( PD ) patients .

Example answer:
{"entities": [{"text": "Levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "LIDs", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: Development of levodopa-induced dyskinesias in parkinsonian monkeys may depend upon rate of symptom onset and/or duration of symptoms .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "parkinsonian", "type": "Disease"}]}

Example input:
Sentence: Levodopa-induced dyskinesias in patients with Parkinson 's disease : filling the bench-to-bedside gap .

Example answer:
{"entities": [{"text": "Levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Input:
Sentence: Risk factors and predictors of levodopa-induced dyskinesia among multiethnic Malaysians with Parkinson 's disease .

## Item bc5cdr:test:3950
Example input:
Sentence: We retrospectively examined the records of 25 renal transplant patients , who developed or displayed increased proteinuria after SRL conversion .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: Three yr after transplantation she developed renal Fanconi syndrome with severe metabolic acidosis , hypophosphatemia , glycosuria , and aminoaciduria .

Example answer:
{"entities": [{"text": "renal Fanconi syndrome", "type": "Disease"}, {"text": "metabolic acidosis", "type": "Disease"}, {"text": "hypophosphatemia", "type": "Disease"}, {"text": "glycosuria", "type": "Disease"}, {"text": "aminoaciduria", "type": "Disease"}]}

Example input:
Sentence: Thus , proteinuria may develop in cardiac transplant patients after switch to Srl , which may have an adverse effect on renal function in these patients .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "Srl", "type": "Chemical"}]}

Example input:
Sentence: Although tacrolimus was suspected to be the cause of late post-transplant renal acidosis and was replaced by sirolimus , acidosis , and electrolyte imbalance got worse .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "acidosis", "type": "Disease"}, {"text": "sirolimus", "type": "Chemical"}]}

Example input:
Sentence: Massive urinary protein excretion has been observed after conversion from calcineurin inhibitors to mammalian target of rapamycin ( mToR ) inhibitors , especially sirolimus , in renal transplant recipients with chronic allograft nephropathy .

Example answer:
{"entities": [{"text": "rapamycin", "type": "Chemical"}, {"text": "sirolimus", "type": "Chemical"}, {"text": "chronic allograft nephropathy", "type": "Disease"}]}

Example input:
Sentence: Whether proteinuria was due to sirolimus or only a consequence of calcineurin inhibitors withdrawal remained unsolved until high range proteinuria has been observed during sirolimus therapy in islet transplantation and in patients who received sirolimus de novo .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "sirolimus", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Sirolimus induces or aggravates pre-existing proteinuria in an unpredictable subset of renal allograft recipients .

Example answer:
{"entities": [{"text": "Sirolimus", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: Clinically significant proteinuria following the administration of sirolimus to renal transplant recipients .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "sirolimus", "type": "Chemical"}]}

Example input:
Sentence: Development of proteinuria after switch to sirolimus-based immunosuppression in long-term cardiac transplant patients .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "sirolimus-based", "type": "Chemical"}]}

Example input:
Sentence: Proteinuria after conversion to sirolimus in renal transplant recipients .

Example answer:
{"entities": [{"text": "Proteinuria", "type": "Disease"}, {"text": "sirolimus", "type": "Chemical"}]}

Input:
Sentence: An unexpected diagnosis in a renal-transplant patient with proteinuria treated with everolimus : AL amyloidosis .

## Item bc5cdr:test:4160
Example input:
Sentence: This study indicates that with stable halothane anesthesia , the partial recovery of blood pressure during SNP infusion and the post-SNP rebound of blood pressure can be completely blocked by saralasin .

Example answer:
{"entities": [{"text": "halothane", "type": "Chemical"}, {"text": "SNP", "type": "Chemical"}, {"text": "saralasin", "type": "Chemical"}]}

Example input:
Sentence: 2 and 10 mg/kg/i.p. , or an equal volume of saline for the control group ( n = 20 ) ; 15 minutes later , all the animals were injected with a single 50 mg/kg/i.p .

Example answer:
{"entities": []}

Example input:
Sentence: The amounts of alphaENaC , betaENaC and gammaENaC proteins were not increased during PAN-induced sodium retention .

Example answer:
{"entities": [{"text": "PAN-induced", "type": "Chemical"}, {"text": "sodium", "type": "Chemical"}]}

Example input:
Sentence: Thirty male Sprague-Dawley rats were divided randomly into four treatment groups : saline , dexamethasone ( dex ) , allopurinol plus saline , and allopurinol plus dex .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "dex", "type": "Chemical"}, {"text": "allopurinol", "type": "Chemical"}]}

Example input:
Sentence: Enalapril treatment blunted but did not prevent reduction in GFR in group 4 ( 0.86 +/- 0.15 ml/min at 4 months , 0.69 +/- 0.13 ml/min at 6 months , both P less than 0.05 vs. group 3 ) .

Example answer:
{"entities": [{"text": "Enalapril", "type": "Chemical"}]}

Example input:
Sentence: Groups 1 and 3 remained untreated while groups 2 and 4 received enalapril .

Example answer:
{"entities": [{"text": "enalapril", "type": "Chemical"}]}

Example input:
Sentence: Patients in Group C received 2 ml normal saline , Group L , 2 ml , lidocaine 2 % ( 40 mg ) and Group T , 2 ml thiopentone 2.5 % ( 50 mg ) .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "thiopentone", "type": "Chemical"}]}

Example input:
Sentence: Conservative treatment , including bladder irrigation with physiological saline and instillation of prostaglandin F2 alpha , failed to totally control hemorrhage .

Example answer:
{"entities": [{"text": "prostaglandin F2 alpha", "type": "Chemical"}, {"text": "hemorrhage", "type": "Disease"}]}

Example input:
Sentence: together for 30 consecutive days and challenged with ISO on the day 29th and 30th , showed a significant ( P < 0.05 ) decrease in heart weight , serum marker enzymes , lipid peroxidation , Ca+2 ATPase and a significant increase in the body weight , endogenous antioxidants , Na+/K+ ATPase and Mg+2 ATPase when compared with ISO treated group and green tea or vitamin E alone treated groups .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}, {"text": "green tea", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}]}

Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "Chemical"}, {"text": "Ato-treated", "type": "Chemical"}]}

Input:
Sentence: There were no differences between saline- and apigenin-treated groups in the 24 h retention trial .

## Item bc5cdr:test:4173
Example input:
Sentence: In all of 7 patients examined acutely , gallbladder contractility was inhibited after a single 100-micrograms injection .

Example answer:
{"entities": []}

Example input:
Sentence: We also used microdialysis to measure basal and potassium-stimulated acetylcholine ( ACh ) release in the CA1 region of the hippocampus .

Example answer:
{"entities": [{"text": "potassium-stimulated", "type": "Chemical"}, {"text": "acetylcholine", "type": "Chemical"}, {"text": "ACh", "type": "Chemical"}]}

Example input:
Sentence: GR 55562 ( 0.1-10 microg/side ) , administered intra-accumbens shell prior to cocaine , dose-dependently attenuated the psychostimulant-induced locomotor hyperactivity .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}, {"text": "locomotor hyperactivity", "type": "Disease"}]}

Example input:
Sentence: In microdialysis experiments , the lines did not differ in basal release of ACh , and 50 mM KCl increased ACh output in both lines of mice .

Example answer:
{"entities": [{"text": "ACh", "type": "Chemical"}, {"text": "KCl", "type": "Chemical"}]}

Example input:
Sentence: Acetaminophen ( up to 150 micrograms/mL ) did not retard the incorporation of radioactive adenosine into ATP in slices of rat cerebral cortex .

Example answer:
{"entities": [{"text": "Acetaminophen", "type": "Chemical"}, {"text": "adenosine", "type": "Chemical"}, {"text": "ATP", "type": "Chemical"}]}

Example input:
Sentence: injection of methyl beta-carboline-3-carboxylate ( beta-CCM ) , an inverse agonist of the GABA ( A ) receptor benzodiazepine site .

Example answer:
{"entities": [{"text": "methyl beta-carboline-3-carboxylate", "type": "Chemical"}, {"text": "beta-CCM", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}, {"text": "benzodiazepine", "type": "Chemical"}]}

Example input:
Sentence: A single MPEP ( 5 mg/kg ip ) injection reduced the basal extracellular dopamine level in the striatum , as well as dopamine release stimulated either by methamphetamine ( 10 mg/kg sc ) or by intrastriatally administered veratridine ( 100 microM ) .

Example answer:
{"entities": [{"text": "MPEP", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "veratridine", "type": "Chemical"}]}

Example input:
Sentence: When injected into the accumbens shell ( but not the core ) before cocaine , CP 93129 ( 0.1-10 microg/side ) enhanced the locomotor response to cocaine ; the maximum effect being observed after 10 microg/side of the agonist .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Example input:
Sentence: An initial dose of 0.1 microgram.kg-1.min-1 of PGE1 ( 15 patients ) , or 10 micrograms.kg-1.min-1 of TMP ( 15 patients ) was administered intravenously after the dural opening and the dose was adjusted to maintain the mean arterial blood pressure ( MAP ) at about 60 mmHg .

Example answer:
{"entities": [{"text": "PGE1", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}]}

Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "Chemical"}]}

Input:
Sentence: Furthermore , microinjection of CCK-8 ( 0.1 and 1ug , i.c.v . )

## Item bc5cdr:test:3793
Example input:
Sentence: The ACTIVE-W ( Atrial Fibrillation Clopidogrel Trial with Irbesartan for Prevention of Vascular Events ) study has demonstrated that warfarin is superior to platelet therapy ( clopidogrel plus aspirin ) in the prevention af embolic events .

Example answer:
{"entities": [{"text": "Atrial Fibrillation", "type": "Disease"}, {"text": "Clopidogrel", "type": "Chemical"}, {"text": "Irbesartan", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}, {"text": "clopidogrel", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "embolic events", "type": "Disease"}]}

Example input:
Sentence: We investigated this association , according to the type of progestagen included in third-generation ( i.e. , desogestrel or gestodene ) and second-generation ( i.e. , levonorgestrel ) oral contraceptives , the dose of estrogen , and the presence or absence of prothrombotic mutations METHODS : In a nationwide , population-based , case-control study , we identified and enrolled 248 women 18 through 49 years of age who had had a first myocardial infarction between 1990 and 1995 and 925 control women who had not had a myocardial infarction and who were matched for age , calendar year of the index event , and area of residence .

Example answer:
{"entities": [{"text": "progestagen", "type": "Chemical"}, {"text": "desogestrel", "type": "Chemical"}, {"text": "gestodene", "type": "Chemical"}, {"text": "levonorgestrel", "type": "Chemical"}, {"text": "oral contraceptives", "type": "Chemical"}, {"text": "estrogen", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : Our results suggest that high-dose testosterone therapy may adversely affect atherosclerosis in postmenopausal women and indicate that androgen replacement in these women may not be harmless .

Example answer:
{"entities": [{"text": "testosterone", "type": "Chemical"}, {"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: After discontinuing the oral alendronate , the patient underwent six cycles of hemodialysis and four cycles of LDL apheresis .

Example answer:
{"entities": [{"text": "alendronate", "type": "Chemical"}]}

Example input:
Sentence: Massive proteinuria and acute renal failure after oral bisphosphonate ( alendronate ) administration in a patient with focal segmental glomerulosclerosis .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "bisphosphonate", "type": "Chemical"}, {"text": "alendronate", "type": "Chemical"}, {"text": "focal segmental glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : To study the long-term effects of androgen treatment on atherosclerosis in postmenopausal women .

Example answer:
{"entities": [{"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: The amount of daily urinary protein decreased from 15.6 to 2.8 g. Within 14 days of the oral bisphosphonate ( alendronate sodium ) administration , the amount of daily urinary protein increased rapidly up to 12.8 g with acute renal failure .

Example answer:
{"entities": [{"text": "bisphosphonate", "type": "Chemical"}, {"text": "alendronate sodium", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: METHODS : The Multiple Outcomes of Raloxifene Evaluation , a multicenter , randomized , double-blind trial , enrolled 7,705 postmenopausal women with osteoporosis .

Example answer:
{"entities": [{"text": "Raloxifene", "type": "Chemical"}, {"text": "osteoporosis", "type": "Disease"}]}

Example input:
Sentence: METHODS : In a population-based study in 513 naturally postmenopausal women aged 54-67 years , we studied the association between self-reported intramuscularly administered high-dose estrogen-testosterone therapy ( estradiol- and testosterone esters ) and aortic atherosclerosis .

Example answer:
{"entities": [{"text": "estrogen-testosterone", "type": "Chemical"}, {"text": "estradiol- and testosterone esters", "type": "Chemical"}, {"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: METHODS : Thirty-nine postmenopausal women with osteopenia or osteoporosis were included in this prospective , controlled clinical study .

Example answer:
{"entities": [{"text": "osteopenia", "type": "Disease"}, {"text": "osteoporosis", "type": "Disease"}]}

Input:
Sentence: Alendronate , a biphosphonate , is effective for both the treatment and prevention of osteoporosis in postmenopausal women .

## Item bc5cdr:test:4115
Example input:
Sentence: Outcome improvement with more intensive chemotherapy has significantly increased the incidence and severity of adverse events .

Example answer:
{"entities": []}

Example input:
Sentence: Calcineurin-inhibitor induced pain syndrome ( CIPS ) : a severe disabling complication after organ transplantation .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "CIPS", "type": "Disease"}]}

Example input:
Sentence: Cancer patients who are chronic carriers of HBV have a higher hepatic complication rate while receiving cytotoxic chemotherapy ( CT ) and this has mainly been attributed to HBV reactivation .

Example answer:
{"entities": [{"text": "Cancer", "type": "Disease"}, {"text": "hepatic complication", "type": "Disease"}]}

Example input:
Sentence: Five patients were diagnosed as having subclinical heart failure after the completion of chemotherapy .

Example answer:
{"entities": [{"text": "heart failure", "type": "Disease"}]}

Example input:
Sentence: Multivariate stepwise logistic regression analysis using preoperative and postoperative variables identified that an increase of serum creatinine compared with average at 1 year , 3 months , and 4 weeks postoperatively were independent risk factors for the development of CRF or ESRD with odds ratios of 2.6 , 2.2 , and 1.6 , respectively .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Treatment duration longer than 1 year was associated with an eightfold increased risk ( OR = 7.7 , 95 % CI 0.9 to 69 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Three patients developed congestive heart failure after the completion of chemotherapy .

Example answer:
{"entities": [{"text": "congestive heart failure", "type": "Disease"}]}

Example input:
Sentence: After two to seven cycles of chemotherapy , nine patients showed a decrease in tumor size and surrounding edema on contrast-enhanced computerized tomography scans .

Example answer:
{"entities": [{"text": "tumor", "type": "Disease"}, {"text": "edema", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Six of 30 patients ( 20 % ) without prior chemotherapy achieved a partial response ( PR ) ( 95 % confidence interval [ CI ] , 8 % to 39 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: One of 16 patients ( 6 % ) with prior chemotherapy had a complete response ( CR ) of 31 weeks ' duration ( 95 % CI , 0 % to 30 % ) .

Example answer:
{"entities": []}

Input:
Sentence: CIN more frequently developed in patients who had undergone CT within 45 days after the last chemotherapy ( P = 0.005 ) ; it was also an independent risk factor ( P = 0.017 ) .

## Item bc5cdr:test:4283
Example input:
Sentence: The most striking effect was sedation which increased with the dose , 2 mg producing deep sleep although the subjects could still be aroused .

Example answer:
{"entities": []}

Example input:
Sentence: Based on these observations , it is concluded that 5-HT2 blockade obtained with risperidone at D2 occupancy rates of 60 % and above does not appear to protect against the risk for extrapyramidal side effects .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}]}

Example input:
Sentence: Optimal control of the absences was achieved with sodium valproate , lamotrigine , or ethosuximide alone or in combination .

Example answer:
{"entities": [{"text": "sodium valproate", "type": "Chemical"}, {"text": "lamotrigine", "type": "Chemical"}, {"text": "ethosuximide", "type": "Chemical"}]}

Example input:
Sentence: Sedation has been commonly used in the neonate to decrease the stress and pain from the noxious stimuli and invasive procedures in the neonatal intensive care unit , as well as to facilitate synchrony between ventilator and spontaneous breaths .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}]}

Example input:
Sentence: Conventional agents are associated with unwanted central nervous system effects , including extrapyramidal symptoms ( EPS ) , tardive dyskinesia , sedation , and possible impairment of some cognitive measures , as well as cardiac effects , orthostatic hypotension , hepatic changes , anticholinergic side effects , sexual dysfunction , and weight gain .

Example answer:
{"entities": [{"text": "extrapyramidal symptoms", "type": "Disease"}, {"text": "EPS", "type": "Disease"}, {"text": "tardive dyskinesia", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}]}

Example input:
Sentence: The sudden onset of respiratory distress , rash , and a history of a new medicine led the two paramedics on the scene to administer subcutaneous epinephrine .

Example answer:
{"entities": [{"text": "respiratory distress", "type": "Disease"}, {"text": "rash", "type": "Disease"}, {"text": "epinephrine", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : TEE is a semi-invasive tool broadly used and its utilization associated to sedatives drugs might to affect the procedure safety .

Example answer:
{"entities": []}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: Increasing doses of catecholamines , sedatives , and muscle relaxants administered through a central venous catheter were ineffective .

Example answer:
{"entities": [{"text": "catecholamines", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : TEE with sedation presents a low rate of events .

Example answer:
{"entities": []}

Input:
Sentence: Unanticipated and previously unreported outcomes may be witnessed as we expand the use of certain sedatives to alternative routes of administration .

## Item bc5cdr:test:4279
Example input:
Sentence: It is concluded that when this electroencephalographic and behavioural picture is seen in drug intoxication , in the absence of significant hypoxaemia , a favourable outcome may be anticipated .

Example answer:
{"entities": [{"text": "hypoxaemia", "type": "Disease"}]}

Example input:
Sentence: It is postulated that her death was caused by hypersensitivity to suxamethonium , associated with her 5-day immobilization .

Example answer:
{"entities": [{"text": "death", "type": "Disease"}, {"text": "hypersensitivity", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: Urgent fasciotomies were performed and the patient made an uneventful recovery with the withdrawal of simvastatin .

Example answer:
{"entities": [{"text": "simvastatin", "type": "Chemical"}]}

Example input:
Sentence: Discontinuance of effective chemotherapy in this patient during partial remission resulted in fatal disease progression .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSIONS : The venlafaxine overdose in our patient resulted in a single episode of generalized seizure but elicited no further sequelae .

Example answer:
{"entities": [{"text": "venlafaxine", "type": "Chemical"}, {"text": "overdose", "type": "Disease"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: This was followed by ventricular fibrillation in one patient and sudden death in another .

Example answer:
{"entities": [{"text": "ventricular fibrillation", "type": "Disease"}, {"text": "sudden death", "type": "Disease"}]}

Example input:
Sentence: Neither the patient nor the anaesthetist was aware of the diagnosis before this potentially lethal complication occurred .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSION : TEE with sedation presents a low rate of events .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Minutes after oral administration , the patient developed nausea , sweating and hypotension , and finally collapsed .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Four patients who were rendered comatose or stuporous by drug intoxication , but who were not hypoxic , are described .

Example answer:
{"entities": [{"text": "comatose", "type": "Disease"}, {"text": "stuporous", "type": "Disease"}]}

Input:
Sentence: Upon leaving the sedation area , the patient collapsed , with no apparent inciting event .

## Item bc5cdr:test:4088
Example input:
Sentence: Fifteen polydrug ecstasy users and 15 polydrug non-ecstasy user controls completed a general drug use questionnaire , the Brixton Spatial Anticipation task ( set shifting ) , Backward Digit Span procedure ( memory updating ) , Inhibition of Return ( inhibition ) , an emotional intelligence scale , the Tromso Social Intelligence Scale and the Dysexecutive Questionnaire ( DEX ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: During the six-month follow up , depression was quantified through the Beck and Zung-Conde scales every two months .

Example answer:
{"entities": [{"text": "depression", "type": "Disease"}]}

Example input:
Sentence: Health , physical abilities and cognitive function were compared between BZD/RD users and non-users , and adjustments were made for confounding variables .

Example answer:
{"entities": []}

Example input:
Sentence: This was accounted for by a significant number of depressions occurring in methyl dopa treated patients with psychiatric histories .

Example answer:
{"entities": [{"text": "depressions", "type": "Disease"}, {"text": "methyl dopa", "type": "Chemical"}, {"text": "psychiatric", "type": "Disease"}]}

Example input:
Sentence: Compared with placebo subjects , alprazolam patients developed more adverse reactions ( 21 % v. 0 % ) of depression , enuresis , disinhibition and aggression ; and more side-effects , particularly sedation , irritability , impaired memory , weight loss and ataxia .

Example answer:
{"entities": [{"text": "alprazolam", "type": "Chemical"}, {"text": "depression", "type": "Disease"}, {"text": "enuresis", "type": "Disease"}, {"text": "aggression", "type": "Disease"}, {"text": "irritability", "type": "Disease"}, {"text": "impaired memory", "type": "Disease"}, {"text": "weight loss", "type": "Disease"}, {"text": "ataxia", "type": "Disease"}]}

Example input:
Sentence: Ecstasy users performed significantly worse in learning and memory compared to controls and cannabis users .

Example answer:
{"entities": [{"text": "Ecstasy", "type": "Chemical"}, {"text": "cannabis", "type": "Chemical"}]}

Example input:
Sentence: Depressed mood was more common among patients and was associated with certain sexual difficulties , but not with impotence .

Example answer:
{"entities": [{"text": "Depressed mood", "type": "Disease"}, {"text": "impotence", "type": "Disease"}]}

Example input:
Sentence: In a double blind cross-over study with control group , the patients under timolol treatment presented higher depression values measured through the Beck and the Zung-Conde scales ( p < 0.001 vs control ) .

Example answer:
{"entities": [{"text": "timolol", "type": "Chemical"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: The results showed a high prevalence of depression in both groups of patients , with no preponderance in the hypertensive group .

Example answer:
{"entities": [{"text": "depression", "type": "Disease"}, {"text": "hypertensive", "type": "Disease"}]}

Example input:
Sentence: Hypertensive patients with psychiatric histories had a higher prevalence of depression than the comparison patients .

Example answer:
{"entities": [{"text": "Hypertensive", "type": "Disease"}, {"text": "psychiatric", "type": "Disease"}, {"text": "depression", "type": "Disease"}]}

Input:
Sentence: RESULTS : Both user groups exhibited significantly greater levels of anxiety and depression than nonusers .

## Item bc5cdr:test:3459
Example input:
Sentence: All patients received CAB [ leuprolide acetate ( LHRH-A ) 3.75 mg , intramuscularly , every 28 days plus 250 mg flutamide , tid , per Os ] and were evaluated for anemia by physical examination and laboratory tests at baseline and 4 subsequent intervals ( 1 , 2 , 3 and 6 months post-CAB ) .

Example answer:
{"entities": [{"text": "leuprolide acetate", "type": "Chemical"}, {"text": "LHRH-A", "type": "Chemical"}, {"text": "flutamide", "type": "Chemical"}, {"text": "anemia", "type": "Disease"}]}

Example input:
Sentence: Subjects were receiving desferrioxamine ( DFO ) chelation treatment with a mean daily dose of 50-60 mg/kg , 5-6 days a week during the first six years of the study , which was then reduced to 40-50 mg/kg for the following eight years .

Example answer:
{"entities": [{"text": "desferrioxamine", "type": "Chemical"}, {"text": "DFO", "type": "Chemical"}]}

Example input:
Sentence: The men were randomly assigned to bupropion SR ( 150 mg twice daily , 117 ) or placebo ( twice daily , 117 ) for 12 weeks .

Example answer:
{"entities": [{"text": "bupropion", "type": "Chemical"}]}

Example input:
Sentence: Seventy-five human immunodeficiency virus ( HIV ) -infected patients with CD4+ cell counts < 500/mm3 were randomized to receive either ZDV ( 500 mg daily ) alone ( group I , n = 38 ) or in combination with folinic acid ( 15 mg daily ) and intramascular vitamin B12 ( 1000 micrograms monthly ) ( group II , n = 37 ) .

Example answer:
{"entities": [{"text": "human immunodeficiency virus ( HIV ) -infected", "type": "Disease"}, {"text": "ZDV", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}, {"text": "vitamin B12", "type": "Chemical"}]}

Example input:
Sentence: One week prior to admission a therapy with standard doses of metoprolol ( 100 mg t.i.d .

Example answer:
{"entities": [{"text": "metoprolol", "type": "Chemical"}]}

Example input:
Sentence: We report a case of a 31 year old female who required admission to the Intensive Care Unit for ventilation and full supportive therapy , following ingestion of 13.5g bupropion .

Example answer:
{"entities": [{"text": "bupropion", "type": "Chemical"}]}

Example input:
Sentence: This complication reappeared on day 25 during the second dose of 5-fluorouracil and folinic acid , which were then the only drugs given .

Example answer:
{"entities": [{"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: Three months later the patient was exposed to a single dose of metoprolol , diltiazem , propafenone ( since he had received this drug in the past ) , and sparteine ( as a probe for the debrisoquine/sparteine type polymorphism of oxidative drug metabolism ) .

Example answer:
{"entities": [{"text": "metoprolol", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "propafenone", "type": "Chemical"}, {"text": "sparteine", "type": "Chemical"}, {"text": "debrisoquine/sparteine", "type": "Chemical"}]}

Example input:
Sentence: The patient was taking 80 mg simvastatin at bedtime ( initiated 27 days earlier ) ; amiodarone at a dose of 400 mg daily for 7 days , then 200 mg daily ( initiated 19 days earlier ) ; and 400 mg atazanavir daily ( initiated at least 2 years previously ) .

Example answer:
{"entities": [{"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Input:
Sentence: On admission the patient was taking carvedilol 12 mg twice daily , warfarin 2 mg/day , folic acid 1 mg/day , levothyroxine 100 microg/day , pantoprazole 40 mg/day , paroxetine 40 mg/day , and flecainide 100 mg twice daily .

## Item bc5cdr:test:4206
Example input:
Sentence: Similarly , in patient diaries , although both treatments caused reduction in subjective dyskinesia scores during the days of intervention , the effect was sustained for 3 days after the intervention for the real rTMS only .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Organic mental disorder was observed in a 29-year-old female in the prognostic period after the onset of carmofur-induced leukoencephalopathy .

Example answer:
{"entities": [{"text": "Organic mental disorder", "type": "Disease"}, {"text": "carmofur-induced", "type": "Chemical"}, {"text": "leukoencephalopathy", "type": "Disease"}]}

Example input:
Sentence: Twenty children with acute lymphoblastic leukemia who developed meningeal disease were treated with a high-dose intravenous methotrexate regimen that was designed to achieve and maintain CSF methotrexate concentrations of 10 ( -5 ) mol/L without the need for concomitant intrathecal dosing .

Example answer:
{"entities": [{"text": "acute lymphoblastic leukemia", "type": "Disease"}, {"text": "meningeal disease", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: At presentation , advanced encephalopathy and cerebral edema were present in 51 ( 76 % ) and 29 ( 41.4 % ) patients , respectively .

Example answer:
{"entities": [{"text": "encephalopathy", "type": "Disease"}, {"text": "cerebral edema", "type": "Disease"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: During a 9-year period , we retrospectively collected 27 neurological events ( 11 % ) in as many patients , from 253 children enrolled in the ALL front-line protocol .

Example answer:
{"entities": [{"text": "ALL", "type": "Disease"}]}

Example input:
Sentence: CNS complications included posterior reversible leukoencephalopathy syndrome ( n = 10 ) , stroke ( n = 5 ) , temporal lobe epilepsy ( n = 2 ) , high-dose methotrexate toxicity ( n = 2 ) , syndrome of inappropriate antidiuretic hormone secretion ( n = 1 ) , and other unclassified events ( n = 7 ) .

Example answer:
{"entities": [{"text": "leukoencephalopathy", "type": "Disease"}, {"text": "stroke", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "inappropriate antidiuretic hormone secretion", "type": "Disease"}]}

Example input:
Sentence: Central nervous system complications during treatment of acute lymphoblastic leukemia in a single pediatric institution .

Example answer:
{"entities": [{"text": "Central nervous system complications", "type": "Disease"}, {"text": "acute lymphoblastic leukemia", "type": "Disease"}]}

Example input:
Sentence: Exclusion criteria included CNS leukemic infiltration at diagnosis , therapy-related peripheral neuropathy , late-onset encephalopathy , or long-term neurocognitive defects .

Example answer:
{"entities": [{"text": "leukemic infiltration", "type": "Disease"}, {"text": "peripheral neuropathy", "type": "Disease"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "neurocognitive defects", "type": "Disease"}]}

Example input:
Sentence: Central nervous system ( CNS ) complications during treatment of childhood acute lymphoblastic leukemia ( ALL ) remain a challenging clinical problem .

Example answer:
{"entities": [{"text": "Central nervous system ( CNS ) complications", "type": "Disease"}, {"text": "acute lymphoblastic leukemia", "type": "Disease"}, {"text": "ALL", "type": "Disease"}]}

Input:
Sentence: In this study , neurocognitive outcomes and neuroradiologic evidence of leukoencephalopathy were compared in children treated with intense central nervous system ( CNS ) -directed therapy ( P9605 ) versus those receiving fewer CNS-directed treatment days during intensive consolidation ( P9201 ) .

## Item bc5cdr:test:4322
Example input:
Sentence: Two groups of supine subjects were studied under placebo-controlled conditions , one during the night , when sleeping ( n = 7 ) and the other at daytime , when awake ( n = 6 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Initial testing in a time-dependent forgetting task employing a 24-h delay between training and testing showed that metrifonate improved object recognition ( at 10 and 30 mg/kg , p.o .

Example answer:
{"entities": [{"text": "metrifonate", "type": "Chemical"}]}

Example input:
Sentence: They showed significantly more rapid improvement of motor function in the first week following hemorrhage and better memory retention in the passive avoidance test .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "Disease"}]}

Example input:
Sentence: Neuropsychological testing showed impaired word fluency , psychomotor speed and working memory .

Example answer:
{"entities": [{"text": "impaired word fluency , psychomotor speed and working memory", "type": "Disease"}]}

Example input:
Sentence: These results suggest that the facilitation of memory retrieval by pre-test morphine might be the direct action of morphine rather than a state dependent effect .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: A conjunction analysis of the encode and recall phases of the task revealed ecstasy-specific hyperactivity in bilateral frontal regions , left temporal , right parietal , bilateral temporal , and bilateral occipital brain regions .

Example answer:
{"entities": [{"text": "ecstasy-specific", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}]}

Example input:
Sentence: Amnesia produced by scopolamine and cycloheximide were reversed by morphine given 30 min before the test trial ( pre-test ) , and pre-test morphine also facilitated the memory retrieval in the animals administered naloxone during the training trial .

Example answer:
{"entities": [{"text": "Amnesia", "type": "Disease"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "cycloheximide", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}, {"text": "naloxone", "type": "Chemical"}]}

Example input:
Sentence: Similarly , pre-test scopolamine partially reversed the scopolamine-induced amnesia , but not significantly ; and pre-test cycloheximide failed to reverse the cycloheximide-induced amnesia .

Example answer:
{"entities": [{"text": "scopolamine", "type": "Chemical"}, {"text": "scopolamine-induced", "type": "Chemical"}, {"text": "amnesia", "type": "Disease"}, {"text": "cycloheximide", "type": "Chemical"}, {"text": "cycloheximide-induced", "type": "Chemical"}]}

Example input:
Sentence: For comparison of sleep architecture variables , 12 healthy comparison participants underwent a single night of experimental polysomnography that followed 1 night of accommodation polysomnography .

Example answer:
{"entities": []}

Example input:
Sentence: Correlation with rating recall after one week was best when first-time ratings were requested as late as one day after injection ( R ( 2 ) =0.79 ) indicating that both rating retrievals utilized similar memory traces .

Example answer:
{"entities": []}

Input:
Sentence: Memory recall of word pairs was evaluated before and after a period of sleep , with and without interference prior to testing .

## Item bc5cdr:test:4323
Example input:
Sentence: Memory retrieval of experiences acquired prior to cocaine administration was impaired and negatively correlated with NFkappaB activity in the frontal cortex .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: The current study aimed to assess the impact of MDMA use on three separate central executive processes ( set shifting , inhibition and memory updating ) and also on `` prefrontal '' mediated social and emotional judgement processes .

Example answer:
{"entities": [{"text": "MDMA", "type": "Chemical"}]}

Example input:
Sentence: After adjustment for these variables as confounders , use of BZDs/RDs was not associated with cognitive function as measured by the MMSE .

Example answer:
{"entities": [{"text": "BZDs/RDs", "type": "Chemical"}]}

Example input:
Sentence: A conjunction analysis of the encode and recall phases of the task revealed ecstasy-specific hyperactivity in bilateral frontal regions , left temporal , right parietal , bilateral temporal , and bilateral occipital brain regions .

Example answer:
{"entities": [{"text": "ecstasy-specific", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}]}

Example input:
Sentence: Cognitive ability was assessed by the Mini-Mental State Examination ( MMSE ) .

Example answer:
{"entities": []}

Example input:
Sentence: In contrast , learning of new tasks was enhanced and correlated with the increase of nNOS activity and the decrease of glutathione peroxidase .

Example answer:
{"entities": [{"text": "glutathione", "type": "Chemical"}]}

Example input:
Sentence: Elevated plus maze and passive avoidance apparatus served as the exteroceptive behavioral models for testing memory .

Example answer:
{"entities": []}

Example input:
Sentence: Spatial learning capacity was assessed in the Morris water maze .

Example answer:
{"entities": []}

Example input:
Sentence: Passive avoidance paradigm and elevated plus maze test were used to assess cognitive function .

Example answer:
{"entities": []}

Example input:
Sentence: Neuropsychological testing showed impaired word fluency , psychomotor speed and working memory .

Example answer:
{"entities": [{"text": "impaired word fluency , psychomotor speed and working memory", "type": "Disease"}]}

Input:
Sentence: In addition , we assessed neurocognitive performances across tasks of learning , memory and executive functioning .

## Item bc5cdr:test:4096
Example input:
Sentence: In the patient described , the presence of asterixis during infusion of ifosfamide , normal laboratory findings and imaging studies and the resolution of symptoms following the discontinuation of the drug suggest that negative myoclonus is associated with the use of IFX .

Example answer:
{"entities": [{"text": "asterixis", "type": "Disease"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "myoclonus", "type": "Disease"}, {"text": "IFX", "type": "Chemical"}]}

Example input:
Sentence: Long-term follow-up of ifosfamide renal toxicity in children treated for malignant mesenchymal tumors : an International Society of Pediatric Oncology report .

Example answer:
{"entities": [{"text": "ifosfamide", "type": "Chemical"}, {"text": "renal toxicity", "type": "Disease"}, {"text": "malignant mesenchymal tumors", "type": "Disease"}]}

Example input:
Sentence: During an 18-month period of study 41 hemodialyzed patients receiving desferrioxamine ( 10-40 mg/kg BW/3 times weekly ) for the first time were monitored for detection of audiovisual toxicity .

Example answer:
{"entities": [{"text": "desferrioxamine", "type": "Chemical"}, {"text": "audiovisual toxicity", "type": "Disease"}]}

Example input:
Sentence: Total cumulative doses were 36 or 60 g/m2 of ifosfamide ( six or 10 cycles of ifosfamide , vincristine , and dactinomycin [ IVA ] ) .

Example answer:
{"entities": [{"text": "ifosfamide", "type": "Chemical"}, {"text": "ifosfamide , vincristine , and dactinomycin", "type": "Chemical"}, {"text": "IVA", "type": "Chemical"}]}

Example input:
Sentence: This low percentage ( 5 % ) of TDFS must be evaluated with respect to the efficacy of ifosfamide in the treatment of mesenchymal tumors in children .

Example answer:
{"entities": [{"text": "ifosfamide", "type": "Chemical"}, {"text": "mesenchymal tumors", "type": "Disease"}]}

Example input:
Sentence: CNS toxic effects of the antineoplastic agent ifosfamide ( IFX ) are frequent and include a variety of neurological symptoms that can limit drug use .

Example answer:
{"entities": [{"text": "ifosfamide", "type": "Chemical"}, {"text": "IFX", "type": "Chemical"}]}

Example input:
Sentence: At presentation , advanced encephalopathy and cerebral edema were present in 51 ( 76 % ) and 29 ( 41.4 % ) patients , respectively .

Example answer:
{"entities": [{"text": "encephalopathy", "type": "Disease"}, {"text": "cerebral edema", "type": "Disease"}]}

Example input:
Sentence: We report a case of a 51-year-old man who developed severe , disabling negative myoclonus of the upper and lower extremities after the infusion of ifosfamide for plasmacytoma .

Example answer:
{"entities": [{"text": "myoclonus", "type": "Disease"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "plasmacytoma", "type": "Disease"}]}

Example input:
Sentence: Ifosfamide encephalopathy presenting with asterixis .

Example answer:
{"entities": [{"text": "Ifosfamide", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "asterixis", "type": "Disease"}]}

Example input:
Sentence: Severe toxicity was correlated with the higher cumulative dose of 60 g/m2 of ifosfamide , a younger age ( less than 2 1/2 years old ) , and a predominance of vesicoprostatic tumor involvement .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "tumor", "type": "Disease"}]}

Input:
Sentence: Encephalopathy has been reported in 10-40 % of patients receiving high-dose IV ifosfamide .

## Item bc5cdr:test:4099
Example input:
Sentence: Upon rechallenge with either cephalosporin , the hematologic syndrome was reproduced in most dogs tested ; cefonicid ( but not cefazedone ) -treated dogs showed a substantially reduced induction period ( 15 +/- 5 days ) compared to that of the first exposure to the drug ( 61 +/- 24 days ) .

Example answer:
{"entities": [{"text": "cephalosporin", "type": "Chemical"}, {"text": "hematologic syndrome", "type": "Disease"}, {"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}]}

Example input:
Sentence: In the patient described , the presence of asterixis during infusion of ifosfamide , normal laboratory findings and imaging studies and the resolution of symptoms following the discontinuation of the drug suggest that negative myoclonus is associated with the use of IFX .

Example answer:
{"entities": [{"text": "asterixis", "type": "Disease"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "myoclonus", "type": "Disease"}, {"text": "IFX", "type": "Chemical"}]}

Example input:
Sentence: Five hours after exposure , he developed disulfiram-like syndrome with flushing , tachycardia , and arterial hypotension after consuming three glasses of wine .

Example answer:
{"entities": [{"text": "disulfiram-like", "type": "Chemical"}, {"text": "flushing", "type": "Disease"}, {"text": "tachycardia", "type": "Disease"}, {"text": "arterial hypotension", "type": "Disease"}]}

Example input:
Sentence: This complication reappeared on day 25 during the second dose of 5-fluorouracil and folinic acid , which were then the only drugs given .

Example answer:
{"entities": [{"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: The patient 's ophthalmological symptoms improved rapidly 3 weeks after discontinuation of pegylated IFN alpha-2b and ribavirin .

Example answer:
{"entities": [{"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: Severe toxicity was correlated with the higher cumulative dose of 60 g/m2 of ifosfamide , a younger age ( less than 2 1/2 years old ) , and a predominance of vesicoprostatic tumor involvement .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "tumor", "type": "Disease"}]}

Example input:
Sentence: We report a case of a 51-year-old man who developed severe , disabling negative myoclonus of the upper and lower extremities after the infusion of ifosfamide for plasmacytoma .

Example answer:
{"entities": [{"text": "myoclonus", "type": "Disease"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "plasmacytoma", "type": "Disease"}]}

Example input:
Sentence: The administration of ifosfamide was discontinued and within 12 h the asterixis resolved completely .

Example answer:
{"entities": [{"text": "ifosfamide", "type": "Chemical"}, {"text": "asterixis", "type": "Disease"}]}

Example input:
Sentence: Ifosfamide encephalopathy presenting with asterixis .

Example answer:
{"entities": [{"text": "Ifosfamide", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "asterixis", "type": "Disease"}]}

Example input:
Sentence: He developed acute neurologic symptoms of mental confusion , disorientation and irritability , and then lapsed into a deep coma , lasting for approximately 40 hours during the first dose ( day 2 ) of 5-fluorouracil and folinic acid infusion .

Example answer:
{"entities": [{"text": "confusion", "type": "Disease"}, {"text": "disorientation", "type": "Disease"}, {"text": "irritability", "type": "Disease"}, {"text": "coma", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Input:
Sentence: RESULTS : All five patients experienced symptoms of encephalopathy soon after ( within 12 h-2 days ) receiving ifosfamide .

## Item bc5cdr:test:4240
Example input:
Sentence: Hepatitis may develop weeks after discontinuation of the drug and may run a prolonged course , but complete remission was observed in all reported cases .

Example answer:
{"entities": [{"text": "Hepatitis", "type": "Disease"}]}

Example input:
Sentence: Despite therapy with ursodeoxycholic acid , prednisone , and then tacrolimus , her cholestatic disease was unrelenting , with cirrhosis shown by biopsy 6 months after presentation .

Example answer:
{"entities": [{"text": "ursodeoxycholic acid", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "cholestatic disease", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}]}

Example input:
Sentence: Finally , pruritus disappeared within 19 months , and liver tests returned to normal 27 months after the onset of hepatitis .

Example answer:
{"entities": [{"text": "pruritus", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: Liver biopsies should be undertaken at regular intervals if azathioprine therapy is continued so that structural liver damage may be detected at an early and reversible stage .

Example answer:
{"entities": [{"text": "azathioprine", "type": "Chemical"}, {"text": "liver damage", "type": "Disease"}]}

Example input:
Sentence: The patient 's ophthalmological symptoms improved rapidly 3 weeks after discontinuation of pegylated IFN alpha-2b and ribavirin .

Example answer:
{"entities": [{"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: Shortly after treatment their tests normalized and during follow-up period none of the patients had abnormal liver function tests .

Example answer:
{"entities": [{"text": "abnormal liver function", "type": "Disease"}]}

Example input:
Sentence: We describe a 70-year-old Hispanic woman who developed fulminant hepatic failure necessitating liver transplantation 10 weeks after conversion from simvastatin 40 mg/day to simvastatin 10 mg-ezetimibe 40 mg/day .

Example answer:
{"entities": [{"text": "fulminant hepatic failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "simvastatin 10 mg-ezetimibe 40", "type": "Chemical"}]}

Example input:
Sentence: The patient 's lipid panel had been maintained with simvastatin for 18 months before the conversion without evidence of hepatotoxicity .

Example answer:
{"entities": [{"text": "simvastatin", "type": "Chemical"}, {"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: Hepatitis was usually reversible when treatment was stopped , with the results of liver function tests returning to normal after an average of 3.1 months .

Example answer:
{"entities": [{"text": "Hepatitis", "type": "Disease"}]}

Input:
Sentence: The liver biochemistries eventually normalized within 3 weeks of stopping the fluvastatin .

## Item bc5cdr:test:4104
Example input:
Sentence: The patient 's ophthalmological symptoms improved rapidly 3 weeks after discontinuation of pegylated IFN alpha-2b and ribavirin .

Example answer:
{"entities": [{"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: Long-term follow-up of ifosfamide renal toxicity in children treated for malignant mesenchymal tumors : an International Society of Pediatric Oncology report .

Example answer:
{"entities": [{"text": "ifosfamide", "type": "Chemical"}, {"text": "renal toxicity", "type": "Disease"}, {"text": "malignant mesenchymal tumors", "type": "Disease"}]}

Example input:
Sentence: The typical signs of VPA-induced encephalopathy are impaired consciousness , sometimes marked EEG background slowing , increased seizure frequency , with or without hyperammonemia .

Example answer:
{"entities": [{"text": "VPA-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "impaired consciousness", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "hyperammonemia", "type": "Disease"}]}

Example input:
Sentence: An electroencephalogram showed continuous , generalized irregular slowing with admixed periodic triphasic waves indicating symptomatic encephalopathy .

Example answer:
{"entities": [{"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: OUTCOME : Following discontinuation of LEV , EEG and neuropsychological findings improved and seizure frequency decreased .

Example answer:
{"entities": [{"text": "LEV", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Severe toxicity was correlated with the higher cumulative dose of 60 g/m2 of ifosfamide , a younger age ( less than 2 1/2 years old ) , and a predominance of vesicoprostatic tumor involvement .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "tumor", "type": "Disease"}]}

Example input:
Sentence: In the patient described , the presence of asterixis during infusion of ifosfamide , normal laboratory findings and imaging studies and the resolution of symptoms following the discontinuation of the drug suggest that negative myoclonus is associated with the use of IFX .

Example answer:
{"entities": [{"text": "asterixis", "type": "Disease"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "myoclonus", "type": "Disease"}, {"text": "IFX", "type": "Chemical"}]}

Example input:
Sentence: We report a case of a 51-year-old man who developed severe , disabling negative myoclonus of the upper and lower extremities after the infusion of ifosfamide for plasmacytoma .

Example answer:
{"entities": [{"text": "myoclonus", "type": "Disease"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "plasmacytoma", "type": "Disease"}]}

Example input:
Sentence: CNS toxic effects of the antineoplastic agent ifosfamide ( IFX ) are frequent and include a variety of neurological symptoms that can limit drug use .

Example answer:
{"entities": [{"text": "ifosfamide", "type": "Chemical"}, {"text": "IFX", "type": "Chemical"}]}

Example input:
Sentence: Ifosfamide encephalopathy presenting with asterixis .

Example answer:
{"entities": [{"text": "Ifosfamide", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "asterixis", "type": "Disease"}]}

Input:
Sentence: CONCLUSIONS : Severity of ifosfamide related encephalopathy correlates with EEG changes .

## Item bc5cdr:test:3777
Example input:
Sentence: BACKGROUND : Although the prevalence of nonsmall cell lung carcinoma ( NSCLC ) is high among elderly patients , few data are available regarding the efficacy and toxicity of chemotherapy in this group of patients .

Example answer:
{"entities": [{"text": "nonsmall cell lung carcinoma", "type": "Disease"}, {"text": "NSCLC", "type": "Disease"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: It has shown promising results alone or in combination with other chemotherapeutic agents in colorectal , breast , pancreaticobiliary , gastric , renal cell and head and neck cancers .

Example answer:
{"entities": []}

Example input:
Sentence: This study is the first to demonstrate that impairment of hepatocyte TJs occurs heterogenously in the liver lobule after BDL and suggests that BDL and EE treatments produce different lobular distributions of increased paracellular permeability .

Example answer:
{"entities": [{"text": "EE", "type": "Chemical"}]}

Example input:
Sentence: Thirty milliliters of blood was obtained for isolation of peripheral blood mononuclear cells after each treatment period .

Example answer:
{"entities": []}

Example input:
Sentence: Patients treated with alkylating agents have an increased risk of development of acute nonlymphocytic leukemia , and both alkylating agents and azathioprine are associated with the development of non-Hodgkin 's lymphoma .

Example answer:
{"entities": [{"text": "alkylating agents", "type": "Chemical"}, {"text": "acute nonlymphocytic leukemia", "type": "Disease"}, {"text": "azathioprine", "type": "Chemical"}, {"text": "non-Hodgkin 's lymphoma", "type": "Disease"}]}

Example input:
Sentence: Paclitaxel , cisplatin , and gemcitabine combination chemotherapy within a multidisciplinary therapeutic approach in metastatic nonsmall cell lung carcinoma .

Example answer:
{"entities": [{"text": "Paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "nonsmall cell lung carcinoma", "type": "Disease"}]}

Example input:
Sentence: The patient cohort ( 14 men , 11 women ) was treated with SRL as conversion therapy , due to chronic allograft nephropathy ( CAN ) ( n = 15 ) neoplasia ( n = 8 ) ; Kaposi 's sarcoma , Four skin cancers , One intestinal tumors , One renal cell carsinom ) or BK virus nephropathy ( n = 2 ) .

Example answer:
{"entities": [{"text": "SRL", "type": "Chemical"}, {"text": "chronic allograft nephropathy", "type": "Disease"}, {"text": "CAN", "type": "Disease"}, {"text": "neoplasia", "type": "Disease"}, {"text": "Kaposi 's sarcoma", "type": "Disease"}, {"text": "skin cancers", "type": "Disease"}, {"text": "intestinal tumors", "type": "Disease"}, {"text": "renal cell carsinom", "type": "Disease"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: Activity was noted in mesothelioma , leiomyosarcoma , and basal cell carcinoma .

Example answer:
{"entities": [{"text": "mesothelioma", "type": "Disease"}, {"text": "leiomyosarcoma", "type": "Disease"}, {"text": "basal cell carcinoma", "type": "Disease"}]}

Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: Thalidomide has limited single-agent activity in relapsed or refractory indolent non-Hodgkin lymphomas : a phase II trial of the Cancer and Leukemia Group B. Thalidomide is an immunomodulatory agent with demonstrated activity in multiple myeloma , mantle cell lymphoma and lymphoplasmacytic lymphoma .

Example answer:
{"entities": [{"text": "Thalidomide", "type": "Chemical"}, {"text": "non-Hodgkin lymphomas", "type": "Disease"}, {"text": "Cancer", "type": "Disease"}, {"text": "Leukemia", "type": "Disease"}, {"text": "multiple myeloma", "type": "Disease"}, {"text": "mantle cell lymphoma", "type": "Disease"}, {"text": "lymphoplasmacytic lymphoma", "type": "Disease"}]}

Input:
Sentence: Mantle cell lymphoma ( MCL ) is a rare and aggressive type of B-cell non-Hodgkin 's lymphoma .

## Item bc5cdr:test:3959
Example input:
Sentence: Rg1 , as a ginsenoside extracted from Panax ginseng , could ameliorate spatial learning impairment .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "ginsenoside", "type": "Chemical"}, {"text": "learning impairment", "type": "Disease"}]}

Example input:
Sentence: ) , administered 20 min before the training session , prevented amnesia induced by both the non selective antimuscarinic drug scopolamine and the M1-selective antagonist S- ( - ) -ET-126 .

Example answer:
{"entities": [{"text": "S- ( - )", "type": "Chemical"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Example input:
Sentence: In SE survivors , similar stimulation resulted in a population spike followed , at a variable latency , by negative DC shifts and repetitive afterdischarges of 3-60 s duration , which were blocked by ionotropic glutamate receptor antagonists .

Example answer:
{"entities": [{"text": "SE", "type": "Disease"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: We tested the sulfated polysaccharide fucoidan , which has been reported to reduce inflammatory brain damage , in a rat model of intracerebral hemorrhage induced by injection of bacterial collagenase into the caudate nucleus .

Example answer:
{"entities": [{"text": "fucoidan", "type": "Chemical"}, {"text": "brain damage", "type": "Disease"}, {"text": "intracerebral hemorrhage", "type": "Disease"}]}

Example input:
Sentence: The antiepileptic drugs , phenobarbitone and carbamazepine are well known to cause cognitive impairment on chronic use .

Example answer:
{"entities": [{"text": "phenobarbitone", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "cognitive impairment", "type": "Disease"}]}

Example input:
Sentence: METHODS : For a period of 2 weeks , CsA 15 mg/kg/day ( given orally ) , FK506 3.0 mg/kg/day ( given orally ) or SRL 0.4 mg/kg/day ( given intraperitoneally ) was administered once a day as these doses have earlier been found to achieve a significant immunosuppressive effect in Sprague-Dawley rats .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: The patient 's ophthalmological symptoms improved rapidly 3 weeks after discontinuation of pegylated IFN alpha-2b and ribavirin .

Example answer:
{"entities": [{"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: Concomitant curcumin administration prevented the cognitive impairment and decreased the increased oxidative stress induced by these antiepileptic drugs .

Example answer:
{"entities": [{"text": "curcumin", "type": "Chemical"}, {"text": "cognitive impairment", "type": "Disease"}]}

Example input:
Sentence: Oral administration of CBZ as an aqueous suspension every 8 h at a dose of 250 mg/kg was continuously protective against HFDE-induced seizures and was minimally toxic as measured by weight gain over 8 weeks of treatment .

Example answer:
{"entities": [{"text": "CBZ", "type": "Chemical"}, {"text": "HFDE-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}]}

Input:
Sentence: One month of oral galactose treatment initiated immediately after the STZ-icv administration , successfully prevented development of the STZ-icv-induced cognitive deficits .

## Item bc5cdr:test:4257
Example input:
Sentence: The cardiotoxicity of conventional anthracycline therapy highlights a need to search for methods that are highly sensitive and capable of predicting cardiac dysfunction .

Example answer:
{"entities": [{"text": "cardiotoxicity", "type": "Disease"}, {"text": "anthracycline", "type": "Chemical"}, {"text": "cardiac dysfunction", "type": "Disease"}]}

Example input:
Sentence: All 20 patients responded to this regimen , 16/20 ( 80 % ) achieved a complete remission , and 20 % obtained a partial remission .

Example answer:
{"entities": []}

Example input:
Sentence: Eight patients were dead in the last follow-up ; two of them died of treatment-related toxicity .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Of the 59 cases , 26 ( 44 % ) had a fatal outcome , compared to 136 ( 25 % ) among the non-warfarin patients ( p < 0.01 ) .

Example answer:
{"entities": []}

Example input:
Sentence: The most common signs of cardiotoxicity were chest pain , ST-T wave changes and atrial fibrillation .

Example answer:
{"entities": [{"text": "cardiotoxicity", "type": "Disease"}, {"text": "chest pain", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}]}

Example input:
Sentence: Five patients were diagnosed as having subclinical heart failure after the completion of chemotherapy .

Example answer:
{"entities": [{"text": "heart failure", "type": "Disease"}]}

Example input:
Sentence: Three patients developed congestive heart failure after the completion of chemotherapy .

Example answer:
{"entities": [{"text": "congestive heart failure", "type": "Disease"}]}

Example input:
Sentence: The incidence of cardiotoxicity was not higher in patients with signs of cardiovascular disease than in those without in the pre-treatment evaluation .

Example answer:
{"entities": [{"text": "cardiotoxicity", "type": "Disease"}, {"text": "cardiovascular disease", "type": "Disease"}]}

Example input:
Sentence: A patient is reported who developed progressive cardiomyopathy two and one-half years after receiving 580 mg/m2 which apparently represents late , late cardiotoxicity .

Example answer:
{"entities": [{"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: During treatment , adverse cardiac effects were observed in 14 patients ( 18 % ) .

Example answer:
{"entities": []}

Input:
Sentence: RESULTS : Fourteen patients ( 18.67 % ) developed cardiotoxicity after treatment .

## Item bc5cdr:test:4350
Example input:
Sentence: injections of organ specific three drugs ( AAP : 500 mg/Kg for 24 h ; AMI : 50 mg/Kg/day for four days ; DOX : 20 mg/Kg for 48 h ) .

Example answer:
{"entities": [{"text": "AAP", "type": "Chemical"}, {"text": "AMI", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: Nephrotoxicity was assessed by measuring the concentrations of creatinine and urea in the plasma and reduced glutathione ( GSH ) in the kidney cortex , and by light microscopic examination of kidney sections .

Example answer:
{"entities": [{"text": "Nephrotoxicity", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "urea", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}]}

Example input:
Sentence: The nephrotoxic action of anticancer drugs such as nitrogranulogen ( NG ) , methotrexate ( MTX ) , 5-fluorouracil ( 5-FU ) and cyclophosphamide ( CY ) administered alone or in combination [ MTX + 5-FU + CY ( CMF ) ] was evaluated in experiments on Wistar rats .

Example answer:
{"entities": [{"text": "nephrotoxic", "type": "Disease"}, {"text": "nitrogranulogen", "type": "Chemical"}, {"text": "NG", "type": "Chemical"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "MTX", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CY", "type": "Chemical"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: However , at the end of 3 weeks , amphotericin B levels in the kidneys and liver were significantly higher in salt-depleted and normal-salt rats than those in salt-loaded rats , with plasma/kidney ratios of 21 , 14 , and 8 in salt-depleted , normal-salt , and salt-loaded rats , respectively .

Example answer:
{"entities": [{"text": "amphotericin B", "type": "Chemical"}]}

Example input:
Sentence: Urinary excretion of Pirarubicin in the first 24 hours was less than or equal to 10 % .

Example answer:
{"entities": [{"text": "Pirarubicin", "type": "Chemical"}]}

Example input:
Sentence: Massive urinary protein excretion has been observed after conversion from calcineurin inhibitors to mammalian target of rapamycin ( mToR ) inhibitors , especially sirolimus , in renal transplant recipients with chronic allograft nephropathy .

Example answer:
{"entities": [{"text": "rapamycin", "type": "Chemical"}, {"text": "sirolimus", "type": "Chemical"}, {"text": "chronic allograft nephropathy", "type": "Disease"}]}

Example input:
Sentence: The rat biodistribution studies showed a rapid blood clearance via the kidneys .

Example answer:
{"entities": []}

Example input:
Sentence: Sodium chloride solution ( 0.9 % ) or noradrenaline in doses of 4 , 12 and 36 micrograms h-1 kg-1 was infused for five consecutive days , either intrarenally ( by a new technique ) or intravenously into rats with one kidney removed .

Example answer:
{"entities": [{"text": "Sodium chloride", "type": "Chemical"}, {"text": "noradrenaline", "type": "Chemical"}]}

Example input:
Sentence: The area under the plasma concentration time curve at 90 min was 4-12 times greater than for oral drug , suggesting the existence of an absorption-limiting process in the intestine , and providing an alternate form of administration for quaternary drugs .

Example answer:
{"entities": []}

Input:
Sentence: This drug is rapidly absorbed from the gastrointestinal tract , and most of it is excreted from the kidney .

## Item bc5cdr:test:3741
Example input:
Sentence: Although evidences of mitochondrial abnormalities were found in previously published studies , our results do not suggest that the FRs , generated during the acute phase , determined important abnormalities in mtDNA , in expression of CCO-I , and in CCO activity .

Example answer:
{"entities": [{"text": "mitochondrial abnormalities", "type": "Disease"}]}

Example input:
Sentence: We also assessed cell viability , mitochondrial membrane potential changes and counted autophagic vacuoles in cultured cardiomyocytes .

Example answer:
{"entities": []}

Example input:
Sentence: Our results demonstrate that both cisplatin and paclitaxel cause early mitochondrial impairment with loss of membrane potential and induction of autophagic vacuoles in neurons .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "mitochondrial impairment", "type": "Disease"}]}

Example input:
Sentence: Assay for mitochondrial respiratory function and histopathological examination of heart tissues were performed .

Example answer:
{"entities": []}

Example input:
Sentence: Mitochondrial radiocalcium uptakes were significantly decreased in animals pretreated with acetylsalicylic acid or dipyridamole or when hydrocortisone was added to the epinephrine infusion ( 2,682,2,803 , and 3,424 counts per minute per gram of dried fraction , respectively ) .

Example answer:
{"entities": [{"text": "radiocalcium", "type": "Chemical"}, {"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVES : To assess the added diagnostic value of a new cardiac performance index ( dP/dtejc ) measurement , based on brachial artery flow changes , as compared to standard 12-lead ECG , for detecting dobutamine-induced myocardial ischemia , using Tc99m-Sestamibi single-photon emission computed tomography as the gold standard of comparison to assess the presence or absence of ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "Tc99m-Sestamibi", "type": "Chemical"}, {"text": "ischemia", "type": "Disease"}]}

Example input:
Sentence: We suggest that our patient 's tubular dysfunction and myopathy may have resulted from mitochondrial dysfunction which is triggered by tacrolimus and augmented by lamivudine .

Example answer:
{"entities": [{"text": "tubular dysfunction", "type": "Disease"}, {"text": "myopathy", "type": "Disease"}, {"text": "mitochondrial dysfunction", "type": "Disease"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: The pooled statistical analysis for ventricular septal ( VSD ) and midline ( MD ) defects was performed for rat fetuses exposed to piroxicam , selective and non-selective COX-2 inhibitor based on present and historic data .

Example answer:
{"entities": [{"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : 3MA significantly improved cardiac function and reduced mitochondrial injury .

Example answer:
{"entities": [{"text": "3MA", "type": "Chemical"}]}

Example input:
Sentence: Mitochondrial injury may be involved in the progression of heart failure caused by adriamycin via the autophagy pathway .

Example answer:
{"entities": [{"text": "heart failure", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}]}

Input:
Sentence: MitoQ , a mitochondrial-targeted antioxidant , was shown to completely prevent these mitochondrial abnormalities as well as cardiac dysfunction characterized here by a diastolic dysfunction studied with a conductance catheter to obtain pressure-volume data .

## Item bc5cdr:test:4169
Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: NRA0160 and clozapine significantly reversed the disruption of prepulse inhibition ( PPI ) in rats produced by apomorphine .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "apomorphine", "type": "Chemical"}]}

Example input:
Sentence: NFkappaB activity was decreased in the frontal cortex of cocaine treated rats , as well as GSH concentration and glutathione peroxidase activity in the hippocampus , whereas nNOS activity in the hippocampus was increased .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}]}

Example input:
Sentence: The results showed that rats treated with Morphine/Rg1 decreased escape latency and increased the time spent in platform quadrant and entering frequency .

Example answer:
{"entities": [{"text": "Morphine/Rg1", "type": "Chemical"}]}

Example input:
Sentence: NRA0160 and clozapine significantly shortened the phencyclidine ( PCP ) -induced prolonged swimming latency in rats in a water maze task .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "phencyclidine", "type": "Chemical"}, {"text": "PCP", "type": "Chemical"}]}

Example input:
Sentence: Population responses in granule cells of the dentate gyrus were examined in transverse slices of the ventral hippocampus from pilocarpine-treated and untreated mice .

Example answer:
{"entities": [{"text": "pilocarpine-treated", "type": "Chemical"}]}

Example input:
Sentence: We conclude that Rg1 may significantly improve the spatial learning capacity impaired by chonic morphine administration and restore the morphine-inhibited LTP .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}, {"text": "morphine-inhibited", "type": "Chemical"}]}

Example input:
Sentence: At hippocampal Schaeffer collateral-CA1 synapses , long-term potentiation was preserved in BMC-transplanted rats compared to epileptic controls .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}]}

Example input:
Sentence: The electrophysiological recording in vitro showed that Rg1 restored the LTP in slices from the rats treated with morphine , but not changed LTP in the slices from normal saline- or morphine/Rg1-treated rats ; this restoration could be inhibited by N-methyl-D-aspartate ( NMDA ) receptor antagonist MK801 .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}, {"text": "morphine/Rg1-treated", "type": "Chemical"}, {"text": "N-methyl-D-aspartate", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "MK801", "type": "Chemical"}]}

Example input:
Sentence: By implantation of electrodes and electrophysiological recording in vivo , the results showed that Rg1 restored the long-term potentiation ( LTP ) impaired by morphine in both freely moving and anaesthetised rats .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}]}

Input:
Sentence: Here , we investigated the effects of CCK-8 on long-term potentiation ( LTP ) in the lateral perforant path ( LPP ) -granule cell synapse of rat dentate gyrus ( DG ) in acute saline or morphine-treated rats .

## Item bc5cdr:test:4171
Example input:
Sentence: Male rats were subcutaneously injected with morphine ( 10 mg/kg ) twice a day at 12 hour intervals for 10 days , and Rg1 ( 30 mg/kg ) was intraperitoneally injected 2 hours after the second injection of morphine once a day for 10 days .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "Rg1", "type": "Chemical"}]}

Example input:
Sentence: Ginsenoside Rg1 restores the impairment of learning induced by chronic morphine administration in rats .

Example answer:
{"entities": [{"text": "Ginsenoside Rg1", "type": "Chemical"}, {"text": "impairment of learning", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: The results showed that rats treated with Morphine/Rg1 decreased escape latency and increased the time spent in platform quadrant and entering frequency .

Example answer:
{"entities": [{"text": "Morphine/Rg1", "type": "Chemical"}]}

Example input:
Sentence: The morphine-induced hyperactivity was potentiated by scopolamine and attenuated by physostigmine .

Example answer:
{"entities": [{"text": "morphine-induced", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "physostigmine", "type": "Chemical"}]}

Example input:
Sentence: Antinociceptive effect of morphine was reduced in chronically treated rats ( 39+/-10 vs. 18+/-5 au ) while the combination-induced antinociception was remained similar as an acute treatment ( 298+/-7 vs. 280+/-17 au ) .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: The subcutaneous administration of 10 mg/kg of morphine-HC1 produced a marked increase in locomotor activity in mice .

Example answer:
{"entities": [{"text": "morphine-HC1", "type": "Chemical"}, {"text": "increase in locomotor activity", "type": "Disease"}]}

Example input:
Sentence: Pretreatment of mice with alpha-methyltyrosine ( 20 mg/kg i.p. , one hour ) , an inhibitor of tyrosine hydroxylase , significantly decreased the activity-increasing effects of morphine .

Example answer:
{"entities": [{"text": "alpha-methyltyrosine", "type": "Chemical"}, {"text": "tyrosine", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: By implantation of electrodes and electrophysiological recording in vivo , the results showed that Rg1 restored the long-term potentiation ( LTP ) impaired by morphine in both freely moving and anaesthetised rats .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: We conclude that Rg1 may significantly improve the spatial learning capacity impaired by chonic morphine administration and restore the morphine-inhibited LTP .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}, {"text": "morphine-inhibited", "type": "Chemical"}]}

Example input:
Sentence: The electrophysiological recording in vitro showed that Rg1 restored the LTP in slices from the rats treated with morphine , but not changed LTP in the slices from normal saline- or morphine/Rg1-treated rats ; this restoration could be inhibited by N-methyl-D-aspartate ( NMDA ) receptor antagonist MK801 .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}, {"text": "morphine/Rg1-treated", "type": "Chemical"}, {"text": "N-methyl-D-aspartate", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "MK801", "type": "Chemical"}]}

Input:
Sentence: Acute morphine ( 30mg/kg , s.c. ) treatment significantly attenuated hippocampal LTP and CCK-8 ( 1ug , i.c.v . )

## Item bc5cdr:test:4381
Example input:
Sentence: IMPORTANCE OF THE FIELD : Fluoropyrimidines , in particular 5-fluorouracil ( 5-FU ) , have been the mainstay of treatment for several solid tumors , including colorectal , breast and head and neck cancers , for > 40 years .

Example answer:
{"entities": [{"text": "Fluoropyrimidines", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "tumors", "type": "Disease"}]}

Example input:
Sentence: Her incontinence resolved with the change of medication .

Example answer:
{"entities": [{"text": "incontinence", "type": "Disease"}]}

Example input:
Sentence: We report a case of a 31 year old female who required admission to the Intensive Care Unit for ventilation and full supportive therapy , following ingestion of 13.5g bupropion .

Example answer:
{"entities": [{"text": "bupropion", "type": "Chemical"}]}

Example input:
Sentence: Despite therapy with ursodeoxycholic acid , prednisone , and then tacrolimus , her cholestatic disease was unrelenting , with cirrhosis shown by biopsy 6 months after presentation .

Example answer:
{"entities": [{"text": "ursodeoxycholic acid", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "cholestatic disease", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}]}

Example input:
Sentence: Paclitaxel/cisplatin is an effective first-line regimen for locoregionally advanced head and neck cancer and continued study is warranted .

Example answer:
{"entities": [{"text": "Paclitaxel/cisplatin", "type": "Chemical"}, {"text": "head and neck cancer", "type": "Disease"}]}

Example input:
Sentence: The patient was treated with methylprednisolone and gradually improved .

Example answer:
{"entities": [{"text": "methylprednisolone", "type": "Chemical"}]}

Example input:
Sentence: Lamivudine was well tolerated and was continued in all patients .

Example answer:
{"entities": [{"text": "Lamivudine", "type": "Chemical"}]}

Example input:
Sentence: Administration of this regimen to breast cancer patients who have been treated by chemotherapy and those with impaired heart function requires careful attention .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "impaired heart function", "type": "Disease"}]}

Example input:
Sentence: Based on this principle a 27-year old woman , classified as being in the high-risk group ( Goldstein and Berkowitz score : 11 ) , was treated with multiple cytotoxic drugs .

Example answer:
{"entities": []}

Example input:
Sentence: Propylthiouracil therapy was withdrawn , and she was treated with a 1-month course of prednisone , which alleviated her symptoms .

Example answer:
{"entities": [{"text": "Propylthiouracil", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}]}

Input:
Sentence: She is currently being treated with best supportive care .

## Item bc5cdr:test:4082
Example input:
Sentence: A conjunction analysis of the encode and recall phases of the task revealed ecstasy-specific hyperactivity in bilateral frontal regions , left temporal , right parietal , bilateral temporal , and bilateral occipital brain regions .

Example answer:
{"entities": [{"text": "ecstasy-specific", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}]}

Example input:
Sentence: Ecstasy users performed significantly worse in learning and memory compared to controls and cannabis users .

Example answer:
{"entities": [{"text": "Ecstasy", "type": "Chemical"}, {"text": "cannabis", "type": "Chemical"}]}

Example input:
Sentence: It has been consistently shown that ecstasy users display impairments in learning and memory performance .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: Learning and memory deficits in ecstasy users and their neural correlates during a face-learning task .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: MDMA polydrug users show process-specific central executive impairments coupled with impaired social and emotional judgement processes .

Example answer:
{"entities": [{"text": "MDMA", "type": "Chemical"}, {"text": "impaired social and emotional judgement processes", "type": "Disease"}]}

Example input:
Sentence: Ecstasy-specific hypoactivity was evident in the right dorsal anterior cingulated cortex ( ACC ) and left posterior cingulated cortex .

Example answer:
{"entities": [{"text": "Ecstasy-specific", "type": "Chemical"}]}

Example input:
Sentence: In both ecstasy and cannabis groups brain activation was decreased in the right medial frontal gyrus , left parahippocampal gyrus , left dorsal cingulate gyrus , and left caudate .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}, {"text": "cannabis", "type": "Chemical"}]}

Example input:
Sentence: Fifteen polydrug ecstasy users and 15 polydrug non-ecstasy user controls completed a general drug use questionnaire , the Brixton Spatial Anticipation task ( set shifting ) , Backward Digit Span procedure ( memory updating ) , Inhibition of Return ( inhibition ) , an emotional intelligence scale , the Tromso Social Intelligence Scale and the Dysexecutive Questionnaire ( DEX ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: These data lend further support to the proposal that cognitive processes mediated by the prefrontal cortex may be impaired by recreational ecstasy use .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: In addition , working memory processing in ecstasy users has been shown to be associated with neural alterations in hippocampal and/or cortical regions as measured by functional magnetic resonance imaging ( fMRI ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Input:
Sentence: Basal functioning of the hypothalamic-pituitary-adrenal ( HPA ) axis and psychological distress in recreational ecstasy polydrug users .

## Item bc5cdr:test:4118
Example input:
Sentence: METHODS : Seventeen subjects who were genotyped as CYP2D6 extensive metabolizers were enrolled in this randomized , open-label , crossover study to receive a single oral dose of desipramine ( 50 mg ) on two separate occasions , once alone and once after multiple doses of cinacalcet ( 90 mg for 7 days ) .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}]}

Example input:
Sentence: A 40-year-old man with leukemia and no history of cardiac disease developed recurrent , brief episodes of apparent sinus arrest while receiving continuous-infusion cimetidine 50 mg/hour .

Example answer:
{"entities": [{"text": "leukemia", "type": "Disease"}, {"text": "cardiac disease", "type": "Disease"}, {"text": "sinus arrest", "type": "Disease"}, {"text": "cimetidine", "type": "Chemical"}]}

Example input:
Sentence: Relative to desipramine alone , mean AUC and C ( max ) of desipramine increased 3.6- and 1.8-fold when coadministered with cinacalcet .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}]}

Example input:
Sentence: Five patients were diagnosed as having subclinical heart failure after the completion of chemotherapy .

Example answer:
{"entities": [{"text": "heart failure", "type": "Disease"}]}

Example input:
Sentence: Although responding patients were scheduled to receive consolidation radiotherapy and 24 patients received preplanned second-line chemotherapy after disease progression , the response and toxicity rates reported refer only to the chemotherapy regimen given .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Outcome improvement with more intensive chemotherapy has significantly increased the incidence and severity of adverse events .

Example answer:
{"entities": []}

Example input:
Sentence: After two to seven cycles of chemotherapy , nine patients showed a decrease in tumor size and surrounding edema on contrast-enhanced computerized tomography scans .

Example answer:
{"entities": [{"text": "tumor", "type": "Disease"}, {"text": "edema", "type": "Disease"}]}

Example input:
Sentence: One of 16 patients ( 6 % ) with prior chemotherapy had a complete response ( CR ) of 31 weeks ' duration ( 95 % CI , 0 % to 30 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Six of 30 patients ( 20 % ) without prior chemotherapy achieved a partial response ( PR ) ( 95 % confidence interval [ CI ] , 8 % to 39 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Three patients developed congestive heart failure after the completion of chemotherapy .

Example answer:
{"entities": [{"text": "congestive heart failure", "type": "Disease"}]}

Input:
Sentence: CIN developed 4.5-times more frequently in patients with cancer who had undergone recent chemotherapy .

## Item bc5cdr:test:4154
Example input:
Sentence: When hippocampal ACh was measured during testing for handling-induced convulsions , extracellular ACh was significantly elevated ( 192 % ) in WSP mice , but was nonsignificantly elevated ( 59 % ) in WSR mice .

Example answer:
{"entities": [{"text": "ACh", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}]}

Example input:
Sentence: The present study was designed to evaluate two endogenous and one synthetic neuroactive steroid that positively modulate the gamma-aminobutyric acid ( GABA ( A ) ) receptor against the increase in sensitivity to the convulsant effects of cocaine engendered by repeated cocaine administration ( seizure kindling ) .

Example answer:
{"entities": [{"text": "steroid", "type": "Chemical"}, {"text": "gamma-aminobutyric acid", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: FINDINGS : FS containing tAMCA caused paroxysmal brain activity which was associated with distinct convulsive behaviours .

Example answer:
{"entities": [{"text": "tAMCA", "type": "Chemical"}, {"text": "convulsive", "type": "Disease"}]}

Example input:
Sentence: However , tAMCA has been shown to cause epileptic seizures .

Example answer:
{"entities": [{"text": "tAMCA", "type": "Chemical"}, {"text": "epileptic seizures", "type": "Disease"}]}

Example input:
Sentence: BE-Induced seizures occurred more frequently and had significantly longer latencies than those induced by equimolar amounts of cocaine .

Example answer:
{"entities": [{"text": "BE-Induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Seizure activity due to PTZ and picrotoxin ( PTX ) was significantly decreased ; however , seizure activity due to 3-mercaptopropionic acid ( MPA ) , bicuculline ( BCC ) , methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate ( DMCM ) , or strychnine ( STR ) was not different from control .

Example answer:
{"entities": [{"text": "Seizure", "type": "Disease"}, {"text": "PTZ", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "PTX", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "3-mercaptopropionic acid", "type": "Chemical"}, {"text": "MPA", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "BCC", "type": "Chemical"}, {"text": "methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate", "type": "Chemical"}, {"text": "DMCM", "type": "Chemical"}, {"text": "strychnine", "type": "Chemical"}, {"text": "STR", "type": "Chemical"}]}

Example input:
Sentence: The degree of these seizures increased with increasing concentration of tAMCA .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "tAMCA", "type": "Chemical"}]}

Example input:
Sentence: These data might indicate that the generation of reactive oxygen species and activation of NF-kappaB plays a more central role in seizure-associated neuronal damage in the temporal cortex as compared to the hippocampal hilus .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "seizure-associated", "type": "Disease"}, {"text": "neuronal damage", "type": "Disease"}]}

Example input:
Sentence: QTLs for susceptibility to pilocarpine-induced seizures , a model of temporal lobe epilepsy , have not been reported , and CSS have not previously been used to localize seizure susceptibility genes .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Using linear regression we found that no correlation exists between seizure duration , elevation of phenytoin serum levels and cerebellar volume .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}, {"text": "phenytoin", "type": "Chemical"}]}

Input:
Sentence: Multivariate analysis showed that trough TAC level was the only independent risk factor associated with the seizures .

## Item bc5cdr:test:4192
Example input:
Sentence: Renal papillary necrosis ( RPN ) and a decreased urinary concentrating ability developed during continuous long-term treatment with aspirin and paracetamol in female Fischer 344 rats .

Example answer:
{"entities": [{"text": "Renal papillary necrosis", "type": "Disease"}, {"text": "RPN", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: Although most cases of antibiotic induced acute interstitial nephritis are benign and self-limited , some patients are at risk for permanent renal injury .

Example answer:
{"entities": [{"text": "interstitial nephritis", "type": "Disease"}, {"text": "renal injury", "type": "Disease"}]}

Example input:
Sentence: These 13 included cases of malignant hypertension , thrombotic microangiopathy , lupus nephritis , Henoch-Schonlein nephritis , crescentic glomerulonephritis , and cocaine-related acute renal failure .

Example answer:
{"entities": [{"text": "malignant hypertension", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "lupus nephritis", "type": "Disease"}, {"text": "Henoch-Schonlein nephritis", "type": "Disease"}, {"text": "glomerulonephritis", "type": "Disease"}, {"text": "cocaine-related", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: In 414 patients , contrast volume , presence of diabetes mellitus , use of N-acetylcysteine , mean baseline SCr , and estimated glomerular filtration rate were comparable in the 2 groups .

Example answer:
{"entities": [{"text": "diabetes mellitus", "type": "Disease"}, {"text": "N-acetylcysteine", "type": "Chemical"}]}

Example input:
Sentence: Diagnosis of this potentially fatal complication may be delayed or missed if renal tissue or the peripheral blood smear is not examined , because renal failure may be ascribed to cisplatin nephrotoxicity and the anemia and thrombocytopenia to drug-induced bone marrow suppression .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "bone marrow suppression", "type": "Disease"}]}

Example input:
Sentence: The risk of renal papillary necrosis was increased nearly 20-fold by consumption of phenacetin , which also increased the risk for cancer of the renal pelvis and bladder but not for ureteric cancer .

Example answer:
{"entities": [{"text": "renal papillary necrosis", "type": "Disease"}, {"text": "phenacetin", "type": "Chemical"}, {"text": "ureteric cancer", "type": "Disease"}]}

Example input:
Sentence: Doxorubicin-induced nephropathy leads to epithelial sodium channel ( ENaC ) -dependent volume retention and renal fibrosis .

Example answer:
{"entities": [{"text": "Doxorubicin-induced", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "sodium", "type": "Chemical"}, {"text": "volume retention", "type": "Disease"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: Reactive oxygen species have been implicated in the pathogenesis of acute puromycin aminonucleoside ( PAN ) -induced nephropathy , with antioxidants significantly reducing the proteinuria .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: Cardiac Angiography in Renally Impaired Patients ( CARE ) study : a randomized double-blind trial of contrast-induced nephropathy in patients with chronic kidney disease .

Example answer:
{"entities": [{"text": "nephropathy", "type": "Disease"}, {"text": "chronic kidney disease", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : The rate of contrast-induced nephropathy , defined by multiple end points , is not statistically different after the intraarterial administration of iopamidol or iodixanol to high-risk patients , with or without diabetes mellitus .

Example answer:
{"entities": [{"text": "nephropathy", "type": "Disease"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}, {"text": "diabetes mellitus", "type": "Disease"}]}

Input:
Sentence: INTRODUCTION AND OBJECTIVE : Contrast-induced nephropathy ( CIN ) significantly increases the morbidity and mortality of patients .

## Item bc5cdr:test:4307
Example input:
Sentence: RESULTS : Sixty percent in Group A developed postoperative emetic symptoms , headache , or both ; 1 patient in Group B developed symptoms .

Example answer:
{"entities": [{"text": "postoperative emetic symptoms", "type": "Disease"}, {"text": "headache", "type": "Disease"}]}

Example input:
Sentence: Estradiol reduces seizure-induced hippocampal injury in ovariectomized female but not in male rats .

Example answer:
{"entities": [{"text": "Estradiol", "type": "Chemical"}, {"text": "seizure-induced", "type": "Disease"}, {"text": "hippocampal injury", "type": "Disease"}]}

Example input:
Sentence: Seizure activity due to PTZ and picrotoxin ( PTX ) was significantly decreased ; however , seizure activity due to 3-mercaptopropionic acid ( MPA ) , bicuculline ( BCC ) , methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate ( DMCM ) , or strychnine ( STR ) was not different from control .

Example answer:
{"entities": [{"text": "Seizure", "type": "Disease"}, {"text": "PTZ", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "PTX", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "3-mercaptopropionic acid", "type": "Chemical"}, {"text": "MPA", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "BCC", "type": "Chemical"}, {"text": "methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate", "type": "Chemical"}, {"text": "DMCM", "type": "Chemical"}, {"text": "strychnine", "type": "Chemical"}, {"text": "STR", "type": "Chemical"}]}

Example input:
Sentence: Over the long-term chronic phase ( 120 days after transplantation ) , only 25 % of BMC-treated epileptic animals had seizures , but with a lower frequency and duration compared to the epileptic control group .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Prevention of seizures and reorganization of hippocampal functions by transplantation of bone marrow cells in the acute phase of experimental epilepsy .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "epilepsy", "type": "Disease"}]}

Example input:
Sentence: Groups were compared for preoperative laboratory variables , diagnosis , postoperative variables , survival , type of ESRD therapy , and survival from onset of ESRD .

Example answer:
{"entities": [{"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: OUTCOME : Following discontinuation of LEV , EEG and neuropsychological findings improved and seizure frequency decreased .

Example answer:
{"entities": [{"text": "LEV", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Using linear regression we found that no correlation exists between seizure duration , elevation of phenytoin serum levels and cerebellar volume .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}, {"text": "phenytoin", "type": "Chemical"}]}

Example input:
Sentence: Twenty-three h postoperatively he developed a brief self-limited seizure .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Multivariate stepwise logistic regression analysis using preoperative and postoperative variables identified that an increase of serum creatinine compared with average at 1 year , 3 months , and 4 weeks postoperatively were independent risk factors for the development of CRF or ESRD with odds ratios of 2.6 , 2.2 , and 1.6 , respectively .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Input:
Sentence: Multivariate regression analysis was performed to identify independent predictors of postoperative seizures .

## Item bc5cdr:test:4310
Example input:
Sentence: Using linear regression we found that no correlation exists between seizure duration , elevation of phenytoin serum levels and cerebellar volume .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}, {"text": "phenytoin", "type": "Chemical"}]}

Example input:
Sentence: OUTCOME : Following discontinuation of LEV , EEG and neuropsychological findings improved and seizure frequency decreased .

Example answer:
{"entities": [{"text": "LEV", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: All of the rats in the saline-treated epileptic control group developed SRS , whereas none of the BMC-treated epileptic animals had seizures in the short term ( 15 days after transplantation ) , regardless of the BMC source .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}, {"text": "SRS", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: In this study , the severity of response to other seizure-inducing agents was tested in mice 1 and 24 h after intraperitoneal administration of 80 mg/kg gamma-HCH .

Example answer:
{"entities": [{"text": "seizure-inducing", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}]}

Example input:
Sentence: Over the long-term chronic phase ( 120 days after transplantation ) , only 25 % of BMC-treated epileptic animals had seizures , but with a lower frequency and duration compared to the epileptic control group .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Most had hyperacute presentation ; the median icterus encephalopathy interval was 4.5 ( 0-30 ) days .

Example answer:
{"entities": [{"text": "icterus", "type": "Disease"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: One hour after the administration of gamma-HCH , the activity of seizure-inducing agents was increased , regardless of their mechanism , while 24 h after gamma-HCH a differential response was observed .

Example answer:
{"entities": [{"text": "gamma-HCH", "type": "Chemical"}, {"text": "seizure-inducing", "type": "Disease"}]}

Example input:
Sentence: The in vitro data suggest that the site responsible for the decrease in seizure activity 24 h after gamma-HCH may be the GABA-A receptor-linked chloride channel .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}, {"text": "GABA-A", "type": "Chemical"}]}

Example input:
Sentence: Twenty-three h postoperatively he developed a brief self-limited seizure .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}]}

Input:
Sentence: The median ( IQR [ range ] ) time after surgery when the seizure occurred was 7 ( 6-12 [ 1-216 ] ) h and 8 ( 6-11 [ 4-18 ] ) h , respectively .
