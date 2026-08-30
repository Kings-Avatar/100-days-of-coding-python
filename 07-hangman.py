print("Welcome to Hangman\nThis is your word")
import random

words = ['harry','interchange', 'agrochemical', 'edition', 'ambassador', 'anatomy', 'adaptable', 'synopsis', 'calling',
    'airliner', 'missing', 'airsick', 'alleviator', 'anemone', 'airlift', 'alternatives', 'anaesthesia',
    'adjudicate', 'alienate', 'agriculture', 'aftershave', 'adoringly', 'analogous', 'documents', 'ambition',
    'agribusiness', 'anchorite', 'alternate', 'alchemist', 'representing', 'amnesty', 'ampoule', 'airflow',
    'adipocere', 'amylase', 'validate', 'alloyage', 'airless', 'advertent', 'profiling', 'systemexit',
    'alkalinity', 'amicably', 'ambushment', 'airworthy', 'amputate', 'admirable', 'amniotic', 'amplification',
    'academy', 'anatomical', 'airmail', 'directory', 'adsorption', 'amanuensis', 'accurate', 'amblyopia',
    'ambergris', 'acceptable', 'alimony', 'getsizeof', 'aficionado', 'acronym', 'anachronism', 'agitation',
    'allegorize', 'adjacent', 'affricate', 'redirect', 'ambient', 'hexversion', 'ancientry', 'ageless',
    'available', 'container', 'almsgiver', 'pertaining', 'derived', 'raising', 'adolescent', 'pathname',
    'acquisition', 'information', 'amaranth', 'providing', 'anagram', 'advocate', 'anarchistic', 'affinity',
    'agility', 'airbase', 'executable', 'analogy', 'affiliate', 'admittee', 'affrayer', 'almshouse',
    'aluminate', 'ambulate', 'adjoinant', 'adherent', 'executables', 'exports', 'amateurish', 'anathema',
    'adenosine', 'subclasses', 'allegory', 'alternative', 'adrenal', 'allegretto', 'portable', 'algaecide',
    'anatomize', 'aircrew', 'amputee', 'advertise', 'decoding', 'alpinist', 'alderman', 'adulation',
    'allegro', 'aggressor', 'accident', 'accommodate', 'results', 'anarchism', 'actually', 'altruistic',
    'something', 'allegation', 'anchorage', 'agronomy', 'displayhook', 'alphabet', 'altruism', 'according',
    'affable', 'treated', 'property', 'ambiguous', 'amnesiac', 'ammunition', 'address', 'airship',
    'counter', 'messages', 'purpose', 'affordance', 'aerator', 'affluent', 'alveolus', 'aerobatics',
    'ambivalent', 'accustom', 'analysand', 'airbrush', 'encoding', 'contains', 'setrecursionlimit', 'aeronaut',
    'function', 'alpinism', 'allotropic', 'allotropy', 'subclassing', 'alcohol', 'anaemic', 'aircraft',
    'analyze', 'allomorph', 'activity', 'alehouse', 'adaptation', 'devnull', 'anaesthetic', 'complex',
    'addiction', 'alkaloid', 'hashable', 'acrobat', 'anatomist', 'adequate', 'acclaim', 'amperage',
    'integer', 'airtight', 'altogether', 'affective', 'amenable', 'alluvium', 'andante', 'adjunct',
    'aldehyde', 'ambulance', 'encoded', 'amygdala', 'datatypes', 'acquire', 'exception', 'mathematical',
    'streaming', 'excepthook', 'allowable', 'posixpath', 'adhesion', 'entries', 'actualize', 'javascript',
    'ammonite', 'airstrip', 'agglomerate', 'aliment', 'defaultdict', 'actions', 'adjustment', 'albinism',
    'amazingly', 'gettrace', 'version', 'affability', 'absence', 'aeration', 'aghastness', 'adversary',
    'alterable', 'ammonia', 'alkaline', 'userstring', 'advisement', 'standard', 'adulatory', 'specialized',
    'admiration', 'adorable', 'exposes', 'alliteration', 'amiable', 'altitude', 'depending', 'analyzable',
    'airspeed', 'adjournment', 'account', 'provides', 'alignment', 'amazonian', 'aminoacid', 'alveolar',
    'creating', 'advisable', 'addictive', 'allocation', 'aliquot', 'modules', 'options', 'alienable',
    'adipose', 'environment', 'alternator', 'counting', 'amusingly', 'adducent', 'remembers', 'accumulate',
    'analgesic', 'allusion', 'allergy', 'amazing', 'amplifier', 'current', 'actuary', 'arguments',
    'airborne', 'ambulation', 'adjective', 'interact', 'acquaint', 'browser', 'affliction', 'component',
    'aliveness', 'tracing', 'anaphora', 'afforest', 'amongst', 'advocacy', 'admixture', 'ambidexter',
    'agrimony', 'implements', 'indicating', 'agreeably', 'administer', 'ammazeable', 'ambulatory', 'amiably',
    'alphabetize', 'setdlopenflags', 'amassable', 'accomplish', 'anasarca', 'affront', 'windows',
    'different', 'ancestor', 'multiple', 'adulthood', 'copyright', 'amicability', 'allotment', 'ordereddict',
    'alertness', 'airpost', 'anesthetize', 'adulterant', 'amphibian', 'between', 'getrecursionlimit', 'afterword',
    'mappings', 'getvalue', 'afterglow', 'aliphatic', 'pythondocs', 'accordance', 'agrarian', 'amputation',
    'decimal', 'anaconda', 'altimeter', 'anarchist', 'anaerobic', 'arbitrary', 'agonize', 'replace',
    'amiability', 'outside', 'acknowledge', 'airwave', 'altruist', 'package', 'amphibious', 'strongly',
    'although', 'acceptance', 'agonizing', 'handler', 'programs', 'specific', 'aluminum', 'aggrieve',
    'acoustic', 'analyzer', 'ability', 'amicable', 'setprofile', 'getrefcount', 'interactive', 'anaemia',
    'adsorbent', 'airiness', 'anesthetist', 'affected', 'agnostic', 'adverbial', 'allophone', 'affirmer',
    'ailment', 'analgesia', 'isinstance', 'anaesthetist', 'ambrosial', 'amnesia', 'lightweight', 'alternation',
    'ambiguity', 'accusation', 'acidified', 'overridden', 'addition', 'academic', 'amalgam', 'affixation',
    'airworthiness', 'amazement', 'enclosed', 'interpreter', 'agitator', 'alchemy', 'amebocyte', 'amphitheater',
    'airshow', 'maxunicode', 'userlist', 'adaptive', 'alumnae', 'anesthetic', 'allative', 'settrace',
    'amenity', 'affection', 'aggregate', 'agreement', 'aneroid', 'activation', 'pathsep', 'advisory',
    'combine', 'anaerobe', 'original', 'airglow', 'analyst', 'almighty', 'agoraphobia', 'command',
    'anabolic', 'adoptive', 'variable', 'admissible', 'platform', 'session', 'androgyny', 'getprofile',
    'aerodrome', 'appends', 'stringio', 'adjudge', 'achievement', 'anaesthetize', 'albumin', 'wrapper',
    'ancestral', 'alliterate', 'alfalfa', 'amenability', 'adroitness', 'possible', 'amidship', 'allantois',
    'identifier', 'adventure', 'amelioration', 'aileron', 'accompany', 'actress', 'adornment', 'amphetamine',
    'compact', 'control', 'alright', 'alkalize', 'familiar', 'agelong', 'assigning', 'albinotic',
    'admission', 'printed', 'allergic', 'amortize', 'install', 'typeerror', 'afternoon', 'activist',
    'agitate', 'expecting', 'advance', 'androgen', 'afterpiece', 'airlock', 'objects', 'albatross',
    'ancestry', 'maxsize', 'affluence', 'admonish', 'adoration', 'airline', 'aggression', 'ancillary',
    'hierarchies', 'adenoma', 'allspice', 'defpath', 'alienist', 'aneurysm', 'aerosol', 'alexandrite',
    'alertly', 'amusing', 'against', 'airport', 'anarchy', 'abolish', 'specializing', 'allegoric',
    'amortization', 'adverse', 'andiron', 'externally', 'amative']
hangman_word= random.choice(words)
space = "_" * (len(hangman_word))
print(space)

lives = 6
user_guess = space

def game_over():
    return lose() or win()

def lose():
    return lives==0

def win():
    if user_guess == hangman_word:
        print("You won!")
    return user_guess == hangman_word
user_guessed = ""
while not game_over():
    user_input =input("Your desired letter (in small letters)")
    user_guessed += user_input
    new_space =""
    for i in range (len(hangman_word)):
        if hangman_word[i] == user_input:
            new_space+=hangman_word[i]
        else:
            new_space+=user_guess[i]
    if user_guess == new_space:
        lives-=1
    user_guess = new_space
    print(new_space)
    print(f"Remaining lives = {lives}")
    print(f"your guesses = {user_guessed}")

if lose():
    print("Game Over. Better luck next time!")
