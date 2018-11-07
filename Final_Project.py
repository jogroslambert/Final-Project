#!/usr/bin/env python
# coding: utf-8

# # Group File Number: 4702

# # MetaSpades Terminal Command

# spades.py --meta -o Final_Project/SPAdes_out -1 /data/metagenomes/160523Alm_D16-4702_1_sequence.fastq.gz -2 /data/metagenomes/160523Alm_D16-4702_2_sequence.fastq.gz -t 2 -m 16 

# When we tried to run MetaSpades, we kept getting a memory error which prevented us from completing the metaspades portions. 

# # One Codex Terminal Command
# onecodex login
# 
# onecodex upload 160523Alm_D16-4702_1_sequence.fastq.gz
# 
# onecodex upload 160523Alm_D16-4702_2_sequence.fastq.gz
# 

# ## Quantify the abundance of different microbes in your metagenome:
# 
# We used One Codex to quantify the abundance of microbes in our metagenome. In total, about 8% of the reads were classified in the OneCodex database. Overall, we found over 150 different species with at least .01% estimated abundance in the classified reads. These classified reads span cellular organisms, Archaea, and mostly, bacteria. Among these bacteria, there are bacteria candidate phyla, proteobacteria, actinobacteria, armatimonadetes, chloroflexi, and acidobacteria. 
# 
# 9.96 % of the classified reads corresponded to the genome of Actinomyces odontolyticus, a gram-positive bacilli that belongs to the Actinomyces genus. This bacterium has been associated with particular clinical syndroms. Actinomyces bacteria can cause actinomycosis, a long-term infection, in humans. Although infection caused by Actinomyces odontolyticus is very rare. 
# 
# The second most present microorganism in our sample is Armatimonadetes bacterium, its genome makes up 6.56% of the classified reads. It is a gram-negative bacteria. After being a candidate phylum described solely based on 16S RNA clones, a bacterial strain belonging to the phylum was identified in 2011.
# 
# Actinobacteria bacterium makes up 6.27% of the classified reads. These are gram-positive bacteria that decompose organic matter in soil, some species of the phylum even grow symbiotically with the plants roots, fixing nitrogen for the plan in exchange for access to the plants’ saccharides.
# 
# Finally, Candidatus Rokubacteria bacterium is the last organism who has a medium abundance of 5.39% of the classified reads, as it is a candidate phylum, little is known about this organism.
# 
# One Codex has found over 20 other species with low to very low abundance in our sample. For example, E.coli makes up 1.79% of the classified reads.
# 
# ![](analysis_taxonomy.png)

# In[ ]:




