"""Entity schemas of the benchmark datasets.

Type names are the gold labels used in Datasets/<dataset>/*.csv. Definitions
follow the prompts of the original beam-tree generator so that generation,
annotation and classification describe the types identically.
"""
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATASETS_DIR = PROJECT_ROOT / "Datasets"
SYNTHETIC_FULL_DIR = PROJECT_ROOT / "SyntheticDataset"
SYNTHETIC_DIR = PROJECT_ROOT / "synthetic"
RESULTS_DIR = PROJECT_ROOT / "results"


@dataclass(frozen=True)
class DatasetSchema:
    name: str
    folder: str
    s_full_file: str
    types: Dict[str, str]
    # generator domain name (DOMAIN_WEIGHTS key / S-full "domain" column) -> gold type
    domain_to_type: Dict[str, str]
    # generator domain name -> class local name in the generator KG
    domain_to_kg_class: Dict[str, str]
    generator: Dict = field(default_factory=dict)

    @property
    def type_names(self) -> List[str]:
        return list(self.types)

    def normalize_domain(self, domain: str) -> Optional[str]:
        """Map any spelling of a generator domain to its gold type."""
        key = domain.strip().lower().replace(" ", "")
        for d, t in self.domain_to_type.items():
            if d.lower() == key or t.lower() == key:
                return t
        return None


BC5CDR = DatasetSchema(
    name="BC5CDR",
    folder="bc5cdr",
    s_full_file="BC5CDR.csv",
    types={
        "Chemical": "Drug, compound, molecule, medication (e.g., cisplatin, aspirin).",
        "Disease": "Pathological or medical condition (e.g., diabetes, lymphoma).",
    },
    domain_to_type={"Disease": "Disease", "Chemical": "Chemical"},
    domain_to_kg_class={"Disease": "Disease", "Chemical": "Chemical"},
    generator=dict(power_a=100.0, power_b=-3.0, power_depth=30, kg_namespace="http://example.org/bc5cdr#",
                   entity_base="http://example.org/bc5cdr/"),
)

BIORED = DatasetSchema(
    name="BioRED",
    folder="biored",
    s_full_file="biored.csv",
    types={
        "CellLine": "A specific cell line used in biomedical research (e.g., HeLa, A549).",
        "ChemicalEntity": "A chemical compound, drug, or small molecule (e.g., doxorubicin, ethanol).",
        "DiseaseOrPhenotypicFeature": "A disease or observable trait (e.g., Parkinson's disease, fever).",
        "GeneOrGeneProduct": "A gene or its expressed product (e.g., TP53, insulin).",
        "OrganismTaxon": "A species or strain (e.g., Homo sapiens, E. coli).",
        "SequenceVariant": "A specific variation in a DNA/RNA/protein sequence (e.g., BRCA1 c.68_69delAG).",
    },
    domain_to_type={
        "cellline": "CellLine",
        "chemicalentity": "ChemicalEntity",
        "diseaseorphenotypicfeature": "DiseaseOrPhenotypicFeature",
        "geneorgeneproduct": "GeneOrGeneProduct",
        "organismtaxon": "OrganismTaxon",
        "sequencevariant": "SequenceVariant",
    },
    domain_to_kg_class={d: d for d in [
        "cellline", "chemicalentity", "diseaseorphenotypicfeature",
        "geneorgeneproduct", "organismtaxon", "sequencevariant"]},
    generator=dict(power_a=114.0, power_b=-3.0, power_depth=30, kg_namespace="http://example.org/biored#",
                   entity_base="http://example.org/biored/"),
)

_MM_TYPES = {
    "AnatomicalStructure": "Specific parts of the body or anatomical regions (e.g., left ventricle, femoral artery).",
    "Bacterium": "Bacterial organisms mentioned in the text (e.g., Escherichia coli, Staphylococcus aureus).",
    "BiologicFunction": "Biological or physiological processes and functions (e.g., immune response, hemostasis).",
    "BiomedicalOccupationOrDiscipline": "Biomedical roles or disciplines (e.g., cardiologist, oncology, radiology).",
    "BodySubstance": "Substances originating from the body (e.g., blood, plasma, cerebrospinal fluid).",
    "BodySystem": "Functional body systems (e.g., cardiovascular system, respiratory system).",
    "Chemical": "Chemical substances and compounds (e.g., ethanol, sodium chloride).",
    "ClinicalAttribute": "Clinical characteristics or attributes (e.g., severity, stage II, BMI).",
    "Eukaryote": "Eukaryotic organisms such as parasites or fungi (e.g., Plasmodium falciparum, Candida albicans).",
    "Finding": "Clinical findings or observations (e.g., fever, rash, wheezing, elevated creatinine).",
    "Food": "Food items or nutrients (e.g., milk, gluten, high-fat diet).",
    "HealthCareActivity": "Healthcare-related activities not primarily procedures (e.g., nursing care, follow-up visit).",
    "InjuryOrPoisoning": "Injuries, poisonings, and related conditions (e.g., blunt trauma, acetaminophen overdose).",
    "IntellectualProduct": "Guidelines, questionnaires, reports, and other intellectual artifacts (e.g., clinical guideline, survey form).",
    "MedicalDevice": "Medical instruments or devices (e.g., pacemaker, ventilator, stent).",
    "Organization": "Institutions or organizations (e.g., hospital, research institute, WHO).",
    "PopulationGroup": "Groups of people or patient populations (e.g., elderly patients, pediatric population).",
    "ProfessionalOrOccupationalGroup": "Professional groups or categories (e.g., nurses, surgeons, laboratory technicians).",
    "ResearchActivity": "Research-related activities or study types (e.g., randomized controlled trial, cohort study).",
    "SpatialConcept": "Spatial or locational concepts relevant to medicine (e.g., upper quadrant, distal segment).",
    "Virus": "Viral agents (e.g., influenza virus, SARS-CoV-2).",
}
# The generator uses "HealthcareActivity"; the gold label is "HealthCareActivity".
_MM_DOMAINS = {("HealthcareActivity" if t == "HealthCareActivity" else t): t for t in _MM_TYPES}

MEDMENTIONS = DatasetSchema(
    name="MedMentions",
    folder="MedMentions",
    s_full_file="MedMentions.csv",
    types=_MM_TYPES,
    domain_to_type=_MM_DOMAINS,
    domain_to_kg_class={d: d.lower() for d in _MM_DOMAINS},
    generator=dict(power_a=121.0, power_b=-3.0, power_depth=30, kg_namespace="http://example.org/medmentions#",
                   entity_base="http://example.org/medmentions/"),
)

SCHEMAS: Dict[str, DatasetSchema] = {s.name: s for s in (BC5CDR, BIORED, MEDMENTIONS)}


def get_schema(name: str) -> DatasetSchema:
    for key, schema in SCHEMAS.items():
        if key.lower() == name.lower() or schema.folder.lower() == name.lower():
            return schema
    raise KeyError(f"Unknown dataset '{name}'. Known: {list(SCHEMAS)}")
