def list_benefits():
    return ["gym pass", "vale_alimentação",
    "plano_de_saúde", "seguro_de_vida",
    "seguro_de_patrimônio"]
    
    
def build_sentence(benefit):
    #print(benefit)
    return benefit

#def build_sentence(benefit):
#    pass
    
def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()