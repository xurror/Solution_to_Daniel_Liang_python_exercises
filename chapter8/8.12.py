# Liang 8.12

def findGenes(genome):
    genes = ''
    itr = 0
    triplet = ['TAG', 'TAA', 'TGA']
    genome = genome.replace('ATG', ' ATG').split()

    for gene in genome:
        if gene.startswith('ATG') and 'TAG' in gene or 'TAA' in gene or 'TGA' in gene:
            while gene.rfind(triplet[itr]) < 0: # Locate the triplet in gene
                itr += 1
            if len(gene[3:gene.rfind(triplet[itr])]) % 3 == 0: # Extract the gene from sub-genome
                genes += gene[3:gene.rfind(triplet[itr])] + ' '
            itr = 0

    if len(genes) > 2:
        return genes
    else:
        return 'No gene found'
                
def main():
    genome = input('Enter a genome string: ')

    if findGenes(genome).startswith('No'):
        print (findGenes(genome))
    else:
        for gene in findGenes(genome).split():
            print (gene)

if __name__ == '__main__':
    main()
