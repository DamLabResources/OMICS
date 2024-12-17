SANDBOX := ~/share/omics_sandbox
WORK := $(SANDBOX)/goea/$(USER)

hello:
	echo Welcome to Gene Ontology Enrichment Analysis (GOEA)

# -- GOEA ------------------------------------------------------------
goea:
	find_enrichment.py study.txt population.txt association.txt --pval=0.05 --method=fdr_bh --pval_field=fdr_bh --outfile=results_id2gos.xlsx

# -- ONTOLOGIES ------------------------------------------------------
obo: go-basic.obo

obos: go-basic.obo goslim_generic.obo

goslim: goslim_generic.obo

goslim_generic.obo:
	wget http://current.geneontology.org/ontology/subsets/goslim_generic.obo

go-basic.obo:
	wget http://current.geneontology.org/ontology/go-basic.obo

# -- SANDBOX ---------------------------------------------------------
mk_sandbox: $(WORK)
	cp -f *.pdf $(WORK)
	cp -f *.md $(WORK)
	cp -f *.txt $(WORK)
	cp -f *.tsv $(WORK)
	cp -f makefile $(WORK)
	cp -f sandbox.sh ../..
	find $(WORK) -type f

chmod:
	chmod 777 $(SANDBOX)

$(WORK):
	mkdir -p $(WORK)

# -- CLEAN -----------------------------------------------------------
clean:
	rm -f *.obo
