import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    
    sample_id = []
    dna_sequence = []
    species = []
    has_start = []
    has_stop = []
    has_atat = []
    has_ggg = []

    for i in range(len(samples["sample_id"])):

        seq : str = samples["dna_sequence"][i]

        if(seq[0 : 3] == "ATG"):
            has_start.append(1)
        else:
            has_start.append(0)
        
        if(seq[-3 : ] in {"TAA", "TAG", "TGA"}):
            has_stop.append(1)
        else:
            has_stop.append(0)
        
        try:
            seq.index("ATAT")
            has_atat.append(1)
        except:
            has_atat.append(0)
        
        try:
            seq.index("GGG")
            has_ggg.append(1)
        except:
            has_ggg.append(0)

        sample_id.append(samples["sample_id"][i])
        dna_sequence.append(samples["dna_sequence"][i])
        species.append(samples["species"][i])
    
    data = {
        "sample_id" : sample_id,
        "dna_sequence" : dna_sequence,
        "species" : species,
        "has_start" : has_start,
        "has_stop" : has_stop,
        "has_atat" : has_atat,
        "has_ggg" : has_ggg
    }

    print(data)

    return pd.DataFrame(data)


{'sample_id': [1, 'ATGCTAGCTAGCTAA', 'Human', 2, 'GGGTCAATCATC', 'Human', 3, 'ATATATCGTAGCTA', 'Human', 4, 'ATGGGGTCATCATAA', 'Mouse', 5, 'TCAGTCAGTCAG', 'Mouse', 6, 'ATATCGCGCTAG', 'Zebrafish', 7, 'CGTATGCGTCGTA', 'Zebrafish'], 'dna_sequence': [], 'species': [], 'has_start': [1, 0, 0, 1, 0, 0, 0], 'has_stop': [1, 0, 0, 1, 0, 1, 0], 'has_atat': [0, 0, 1, 0, 0, 1, 0], 'has_ggg': [0, 1, 0, 1, 0, 0, 0]}