import json
from BasicPythonPractice.Person import Person
from BasicPythonPractice.Product import Product
class RulesEngine():
    def loadrules(self):
        with open('C:/Users/Anitha/Desktop/visio/rules.json') as json_file:
            rules = json.load(json_file)
            print(rules)
            mydict = rules['rules']
            # for mykey in mydict.keys():
            #     if mykey == "rule2":
            #         print(mykey + " ")
            #         print(mydict[mykey]['creditScore']['value'])
            #         print(mydict[mykey]['interestRate']['interestPercent'])

        return mydict


    def runRules(self,person, product, rules):
        self.output_interest_rate = 0
        self.is_disqualified = False
        print('###' + str(type(rules)))
        for rule in rules.keys():
            print('###rule: ' + rule)
            if rules[rule]['person']['productOfferred']:
                self.is_disqualified = True
            if rules[rule]['enable'] == 'Y':
                if (rules[rule]['person']['state'] == person.state or  rules[rule]['person']['state'] == 'ALL' ) and rules[rule]['person']['productOfferred'] == 'Y':
                    if rules[rule]['person']['creditCheck'] == 'Y':
                        if rules[rule]['person']['creditScore']['limit'] == 'high' and person.credit_score >= rules[rule]['person']['creditScore']['value']:
                            if rules[rule]['product']['name'] == product.name or rules[rule]['product']['name'] == 'ALL':
                                if rules[rule]['product']['interestRate']['change'] == 'decrease':
                                    if self.output_interest_rate > 0:
                                        print('###1###' + str(self.output_interest_rate))
                                        self.output_interest_rate = self.output_interest_rate - rules[rule]['product']['interestRate']['interestPercent']
                                        print('###2###' + str(self.output_interest_rate))
                                    else:
                                        self.output_interest_rate = rules[rule]['product']['interestRate']['initialRate'] - rules[rule]['product']['interestRate']['interestPercent']
                                        print('###3###' + str(self.output_interest_rate))
                                elif rules[rule]['product']['interestRate']['change'] == 'increase':
                                    if self.output_interest_rate > 0:
                                        self.output_interest_rate = self.output_interest_rate + rules[rule]['product']['interestRate']['interestPercent']
                                        print('###4###' + str(self.output_interest_rate))
                                    else:
                                        self.output_interest_rate = rules[rule]['product']['interestRate']['initialRate'] + rules[rule]['product']['interestRate']['interestPercent']
                                        print('###5###' + str(self.output_interest_rate))

                        elif  rules[rule]['person']['creditScore']['limit'] == 'low' and person.credit_score < rules[rule]['person']['creditScore']['value']:
                            if rules[rule]['product']['name'] == product.name or rules[rule]['product']['name'] == 'ALL':
                                if rules[rule]['product']['interestRate']['change'] == 'decrease':
                                    if self.output_interest_rate > 0:
                                        self.output_interest_rate = self.output_interest_rate - rules[rule]['product']['interestRate']['interestPercent']
                                        print('###6###' + str(self.output_interest_rate))
                                    else:
                                        self.output_interest_rate = rules[rule]['product']['interestRate']['initialRate'] - rules[rule]['product']['interestRate']['interestPercent']
                                        print('###7###' + str(self.output_interest_rate))
                                elif rules[rule]['product']['interestRate']['change'] == 'increase':
                                    if self.output_interest_rate > 0:
                                        self.output_interest_rate = self.output_interest_rate + rules[rule]['product']['interestRate']['interestPercent']
                                        print('###8###' + str(self.output_interest_rate))
                                    else:
                                        self.output_interest_rate = rules[rule]['product']['interestRate']['initialRate'] + rules[rule]['product']['interestRate']['interestPercent']
                                        print('###9##' + str(self.output_interest_rate))

                    else:
                        if rules[rule]['product']['name'] == product.name or rules[rule]['product']['name'] == 'ALL':
                            if rules[rule]['product']['interestRate']['change'] == 'decrease':
                                if self.output_interest_rate > 0:
                                    self.output_interest_rate = self.output_interest_rate - \
                                                                rules[rule]['product']['interestRate'][
                                                                    'interestPercent']
                                    print('###10##' + str(self.output_interest_rate))
                                else:
                                    self.output_interest_rate = rules[rule]['product']['interestRate']['initialRate'] - \
                                                                rules[rule]['product']['interestRate'][
                                                                    'interestPercent']
                                    print('###11##' + str(self.output_interest_rate))
                            elif rules[rule]['product']['interestRate']['change'] == 'increase':
                                if self.output_interest_rate > 0:
                                    self.output_interest_rate = self.output_interest_rate + \
                                                                rules[rule]['product']['interestRate'][
                                                                    'interestPercent']
                                    print('###12##' + str(self.output_interest_rate))
                                else:
                                    self.output_interest_rate = rules[rule]['product']['interestRate']['initialRate'] + \
                                                                rules[rule]['product']['interestRate'][
                                                                    'interestPercent']
                                    print('###13##' + str(self.output_interest_rate))

        print('product.interest_rate ' + str(self.output_interest_rate))
        print('product.disqualified ' + str(self.is_disqualified  ))

test_person = Person(720, 'Florida')
test_product = Product('7-1 ARM', 5.0)
test_rulesEngine = RulesEngine()
test_rulesEngine.runRules(test_person,test_product, test_rulesEngine.loadrules())