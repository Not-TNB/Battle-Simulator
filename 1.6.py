import random
from random import randint, choice
from colorama import Fore, Back, Style, init

init()

class Weapon:
  def __init__(self,name: str,quality: int,type: str):
    self.name = name
    self.quality = quality
    self.type = type

# please forgive me for these sinful lines of code
fist = Weapon('their fists',0,'melee')
stick = Weapon('a stick',0,'melee')
knife = Weapon('a knife',1,'melee')
sword = Weapon('a sword',2,'melee')
axe = Weapon('an axe',3,'hybrid')
hammer = Weapon('a hammer',4,'melee')
chainsaw = Weapon('a chainsaw',5,'melee')
deagle = Weapon('a DEAGLE',6,'ranged')
m4 = Weapon('an M4 with a bayonet',7,'hybrid')
m134 = Weapon('an M134',8,'ranged')
nukecodes = Weapon(f'{Fore.RED}{Style.BRIGHT}NUCLEAR LAUNCH CODES{Style.RESET_ALL}',9,'hybrid')
paper = Weapon('a sheet of paper',0,'')
clothes = Weapon('some spare clothes',1,'')
wood = Weapon('some wood',2,'')
leather = Weapon('a leather padding',3,'')
stone = Weapon('some stone armor',4,'')
metal = Weapon('a metal plate',5,'')
shield = Weapon('a good shield',6,'')
metal = Weapon('a set of metal armor',7,'')
diamond = Weapon('diamond armor',8,'')
netherite = Weapon(f'{Fore.YELLOW}{Style.BRIGHT}NETHERITE{Style.RESET_ALL}',9,'')

weapons = [stick, knife, sword, axe, hammer, chainsaw, deagle, m4, m134, nukecodes]
armor = [paper, clothes, wood, leather, stone, metal, shield, metal, diamond, netherite]
misc = ['nothing','food','some water','communism','sand','dirt','a medkit','air???','a twig that snapped when they touched it','a stand arrow','food','food','food','food','food','food']
interaction = [' talked with ',' flipped off ',' casually said the n word in front of ',' played with ',' sang with ',' spied on ',' greeted ',' debated with ',' screamed at ',' wrote a message to ',' thought about brutally murdering ',' wanted to fight ',' puked right in front of ',' played a little game with ',' posed with ',' interrogated ',' threw a pie at ']
exinteraction = [[' told ',' to go die'],[' thought that fighting ',' was futile'],[' showed hentai to ',', who was disgusted'],[' joined ',' in acting weird'],[' caught ',' in 4k'],[' wanted to play ddakji with ',', who quickly refused'],[' played good cop while ',' played bad cop'],[' was confused on how to play squid game, ',' was confused too']]
deathmsg = [Fore.RED + i + Fore.RESET for i in [' and said a prayer before ending them',' and also slit their throat',' somehow breaking their neck',' thus finishing them off',' and put a bullet through their skull',' and said "omae wa mou shinderu"',' then teabagged them',' and made a hole through their stomach',' with a stab but didn\'t stop stabbing until they had 69 stab wounds',' and beheaded them']]
selfdeathmsg = [Fore.RED + i + Fore.RESET for i in [' killed themselves',' buried themselves in the ground',' frontflipped unsuccessfully',' tried to swim in lava',' walked off a building',' shot themself',' died',' got isekai\'d']]
selfinteraction = [' went AFK for a bit',' slept',' wandered around',' did nothing',' read a book',' did the fortnite dance',' looked at themselves in the mirror',' waited',' spaced out',' failed to kill themself']
# make area themes and sections
nature = ['forest','deep forest','grass plains','river','beach','flower field']
city = ['streets','office','mall','church','park','school','store']
future = ['night city','abandoned lab','wastelands','dried ocean','futuretopia city','neon highway']
arealist = choice([nature,city,future])

def roll(p, q):
  '''p/q chance of returning True, and False otherwise'''
  return randint(1, q) <= p

class BattleField:
  def __init__(self, fighters: list):
    self.fighters = fighters
    self.all_fighters = tuple(self.fighters)
    self.turns = 0
    self.events = ''
    self.hell = False

  # MAIN GAME LOGIC, ALL THE SHIT STARTS HERE
  def progress(self):
    self.turns += 1

    random.shuffle(self.fighters)
    self.events = f'########## TURN {self.turns} ##########\n'
    if roll(1, 10):
      self.events += Fore.RED + 'WORLD EVENT\nWARNING: '
      choice([self.eventPlague, self.eventGoblin, self.eventNuclear, self.eventLightning, self.eventMath, self.eventAntiChurch])()
      self.events += 'everyone else not mentioned also survived\n'
    else:
      for f1 in self.fighters:
        self.checkChangeArea(f1)
        if self.checkHunger(f1) == True: continue

        action = randint(1, 4)
        if action <= 2:
          f2 = choice(self.fighters)
          if f2 == f1: self.hitSelf(f1)
          else: choice([self.interact, self.atkSequence])(f1, f2)
        elif action == 3: choice([self.pickupWeapon, self.pickupArmor, self.pickupMisc])(f1)

    self.printEvents()

  # FUNCTIONS USED IN PROGRESS()
  def checkChangeArea(self, f):
    if self.hell == True:
      f.Hp = max(1,f.Hp-250)
    if roll(1, 4):
      newarea = choice(arealist)
      while newarea == f.area:
        newarea = choice(arealist)
      f.area = newarea
      self.events += f'{f.Name} moved to the {newarea}\n'

  def checkHunger(self, f):
    if f.hunger > 0: 
      f.hunger = max(0, f.hunger-randint(2, 7))
      return False
    f.Hp -= 1000
    if f.Hp <= 0:
      self.events += f'{f.Name} {Fore.RED}died of starvation{Fore.RESET}\n'
      self.fighters.remove(f)
      return True
    
  def hitSelf(self, f):
    self.events += f'{f.Name}'
    if roll(1, 6):
      self.events += choice(selfdeathmsg) + '\n'
      self.fighters.remove(f)
    else: self.events += choice(selfinteraction) + '\n'

  def interact(self, f1, f2):
    if roll(1, 2):
      self.events += f'{f1.Name}{choice(interaction)}{f2.Name}\n'
    else:
      action = choice(exinteraction)
      self.events += f'{f1.Name}{action[0]}{f2.Name}{action[1]}\n'

  def chooseWeapon(self, f1, f2):
    fighterWeapon = [i for i in f1.Items if i in weapons]
    chosenWeapon = None
    tempAtk = 0
    if fighterWeapon == []: chosenWeapon = fist
    else: chosenWeapon = choice(fighterWeapon)
    if chosenWeapon.type == 'ranged' and f2.area == f1.area:
      tempAtk = 30
      self.events += f'{Back.RED}{f1.Name} got a damage penalty for trying to use a ranged weapon on {f2.Name}{Back.RESET}\n'
    elif chosenWeapon.type == 'melee' and f2.area != f1.area:
      tempAtk = 1
      self.events += f'{Back.RED}{f1.Name} couldn\'t reach {f2.Name} with their melee weapon{Back.RESET}\n'    
    return tempAtk
  
  def atkSequence(self, f1, f2):
    tempAtk = self.chooseWeapon(f1, f2) 
    if tempAtk == 1: return
    savedAtk = f1.Atk
    f1.Atk -= round(f1.Atk * (tempAtk / 100))
    f1.Atk = savedAtk
    match randint(1,6):
      case 1:
        res = f1.combo(f2)
        self.events += res[0]
      case 2:                         
        res = f1.heavy(f2)
        self.events += res[0] + '\n'
      case _:
        res = f1.attack(f2)
        self.events += res[0] + '\n'
    if res[1] == True: self.fighters.remove(f2)
  
  def pickupWeapon(self, f):
    item = choice(weapons)
    self.events += f'{f.Name} found {Fore.BLUE}{item.name}{Fore.RESET} (quality {item.quality}, {item.type}), '
    if len(f.Items) == 9:
      self.events += 'but their inventory is full, so they ignored it\n'
    elif item in f.Items:
      self.events += 'but they can\'t hold more than one of those\n'
    else:
      self.events += 'their ATK has increased\n'
      f.Atk += 12 * (item.quality + 1)
      f.Items.append(item)
  
  def pickupArmor(self, f):
    item = choice(armor)
    self.events += f'{f.Name} found {Fore.BLUE}{item.name}{Fore.RESET} (quality {item.quality}), '
    if len(f.Items) == 9:
      self.events += 'but their inventory is full, so they ignored it\n'
    else:
      self.events += 'their DEF has increased\n'
      f.Def += 2 * (item.quality + 1)
      f.Items.append(item)
  
  def eatFood(self, f):
    match randint(1, 5):
      case 1:
        self.events += f' and ate it {Fore.RED}just to die from food poisoning{Fore.RESET}\n'
        f.hunger = -1
        self.fighters.remove(f)
      case 2:
        self.events += f', {Fore.GREEN}it was the best meal they had thus recovering 30 hunger and 1000 HP{Fore.RESET}\n'
        f.hunger += 30
        f.Hp += 1000
      case _:
        saturation = randint(10,20)
        self.events += f' and ate it thus recovering {Fore.GREEN}{str(saturation)} hunger and 250 HP{Fore.RESET}\n'
        f.hunger += saturation
        f.Hp += 250

  def pickupMisc(self, f):
    item = choice(misc)
    self.events += f'{f.Name} found {item}'
    match item:
      case 'communism':
        self.events += f', {Fore.RED}their offensive stats increased{Fore.RESET}\n'
        f.Atk += 100
        f.Cr += 5
        f.Cd += 30
      case 'a medkit':
        addedHp = randint(1000, 2000)
        self.events += f', {Fore.GREEN}they gained {addedHp}HP{Fore.RESET}\n'
        f.Hp += addedHp
      case 'a stand arrow':
        if roll(1, 5):
          self.events += f', {Fore.RED}but died trying to use it{Fore.RESET}\n' # oof
          self.fighters.remove(f)
        else:
          self.events += f' and obtained a {Fore.YELLOW}{Back.MAGENTA}stand{Style.RESET_ALL}\n'
          f.Hp += 3000
          f.Atk += 150
          if f.Def < 75: f.Def += 5
          f.Cr += 10
          f.Cd += 100
      case 'food': self.eatFood(f)
      case _: self.events += '\n'
    
  def printEvents(self):
    if self.events.count('\n') == 1:
      self.events += 'Nothing happened this turn\n'
    self.events += f'\n----- CURRENT PLAYER STATISTICS: -----\n'
    for f in self.all_fighters:
      if f not in self.fighters:
        f.Hp = 0
        printInventory = ', '.join([f'{Fore.RED}{i.name}{Fore.RED}' for i in f.Items])   
        self.events += Style.DIM + Fore.RED
      else: printInventory = ', '.join([i.name for i in f.Items])      
      template = f'{f.Name}: {f.Hp} HP, {f.hunger} Hunger, {f.kills} kills, in {f.area} [{printInventory}]'
      self.events += template + Style.RESET_ALL + '\n'
    self.events += Style.DIM + Fore.CYAN + f'\nFighters left: {len(self.fighters)}\n' + Style.RESET_ALL
    print(self.events + f'########## END OF TURN {self.turns} ##########\n\n')
  
  def eventNuclear(self):
    if self.hell == False: self.events += 'NUCLEAR LAUNCH INBOUND\n' + Fore.RESET
    else: self.events += 'PURGE BLAST INBOUND\n' + Fore.RESET
    for f1 in self.fighters:
      if nukecodes in f1.Items and randint(1, 3) == 1:
        self.events += f'{str(f1.Name)}: Who the fuck used MY nuclear launch codes?!\n'
    # the carnage begins
    for f1 in self.fighters:
      fate = randint(1, 80) + (f1.iq / 10)
      if fate <= 20 and len(self.fighters) != 1:
        self.events += f'{str(f1.Name)} {Fore.RED}died on the initial blast.{Fore.RESET}\n'
        self.fighters.remove(f1)
      elif fate <= 52 and len(self.fighters) != 1:
        f2 = choice(self.fighters)
        if f2 == f1:
          self.events += f'{f1.Name} {Fore.RED}died to flying debris hitting their head.{Fore.RESET}\n'
          self.fighters.remove(f1)
        else:
          self.events += f'{f1.Name} smacked {f2.Name} so hard that they {Fore.RED}died{Fore.RESET} '
          self.fighters.remove(f2)
          f1.kills += 1
          if roll(2, 3) and len(self.fighters) != 1:
            self.events += f'but {Fore.RED}they failed to escape the radiation, get karma\'ed{Fore.RESET}\n'
            self.fighters.remove(f1)
          else:
            self.events += 'and they managed to escape unscathed\n'
      elif fate <= 64 and len(self.fighters) != 1:
        self.events += f'{f1.Name} managed to escape the blast {Fore.RED}but could not survive the radiation{Fore.RESET}\n'
        self.fighters.remove(f1)
      else:
        self.events += f'{f1.Name} survived\n'

  def eventPlague(self):
    if self.hell == False: self.events += 'SECTOR PLAGUE DETECTED\n' + Fore.RESET
    else: self.events += 'EXTERMINATION AURA DETECTED\n' + Fore.RESET
    sector = []
    area = choice(arealist)
    for i in self.fighters:
      if i.area == area:
        sector.append(i)
    caught = ', '.join([i.Name for i in sector]) if sector != [] else 'None'
    self.events += f'AFFECTED SECTOR: {area}\nFIGHTERS CAUGHT: ' + caught + '\n'
    for f1 in sector:
      fate = randint(1,90) + (f1.iq / 10)
      if fate <= 30 and len(self.fighters) != 1:
        self.events += f'{f1.Name} {Fore.RED}died to the plague{Fore.RESET}\n'
        self.fighters.remove(f1)
        sector.remove(f1)
      elif fate <= 65 and len(self.fighters) != 1:
        f2 = choice(sector)
        if f2 != f1:
          self.events += f'{f1.Name} pushed {f2.Name} {Fore.RED}into the plague cloud{Fore.RESET} '
          self.fighters.remove(f2)
          sector.remove(f2)
          f1.kills += 1
          if roll(1, 2) and len(self.fighters) != 1:
            self.events += f'but {Fore.RED}unintentionally pushed themselves in too{Fore.RESET}\n'
            self.fighters.remove(f1)
            sector.remove(f1)
          else:
            self.events += 'and lived\n'
        else:
          self.events += f'{f1.Name} {Fore.RED}tripped on a rock whilst trying to escape ENTITY_PLAGUE_CLOUD{Fore.RESET}\n'
          self.fighters.remove(f1)
          sector.remove(f1)
      else:
        self.events += f'{f1.Name} survived\n'
    
  def eventGoblin(self):
    if self.hell == False: self.events += 'GOBLINS INCOMING\n' + Fore.RESET
    else: self.events += 'SINNERS INCOMING\n' + Fore.RESET
    death = [Fore.RED + i + Fore.RESET for i in [' got a knife thrown towards their head\n',' got ganged on and died\n',' fought until their last breath\n',' nearly escaped only to get blown up\n',' fucking died\n']]
    live = [' killed a few on their way out\n',' survived\n',' ran away safely\n',' participated in ending the invasion\n',' managed to pull off a 360 no-scope, damn\n']
    for f1 in self.fighters:
      fate = randint(1,80) + (f1.Atk / 100)
      if fate <= 30 and len(self.fighters) != 1:
        self.events += f1.Name + choice(death)
        self.fighters.remove(f1)
      elif fate <= 70 and len(self.fighters) != 1:
        damage = max(1, round(randint(600,1500) * (100 - f1.Def) / 100))
        if self.hell == True: damage = round(damage * 1.5)
        f1.Hp -= damage
        if f1.Hp <= 0:
          self.events += f'{f1.Name} took {str(damage)} damage and{choice(death)}'
          self.fighters.remove(f1)
        else:
          self.events += f'{f1.Name} took {str(damage)} damage but{choice(live)}'
      else:
        self.events += f1.Name + choice(live)
  
  def eventLightning(self):
    self.events += 'INSANE THUNDERSTORM INCOMING\n' + Fore.RESET
    for f1 in self.fighters:
      fate = randint(1,3)
      if fate == 1 and len(self.fighters) != 1:
        self.events += f1.Name + f'{Fore.RED} was struck by lightning{Fore.RESET}\n'
        self.fighters.remove(f1)
      else:
        self.events += f1.Name + ' survived\n'

  def eventMath(self):
    if self.hell == False:
      dialogue = ['Not_TNB what the fuck are you doing here','what','hey uh Not_TNB why are you giving everyone a math test','are we making this an intelligence fight now']
      self.events += f'{Fore.CYAN}Not_TNB (aka JIMMY){Fore.RED} has started a {Fore.CYAN}MATH TEST?{Fore.RESET}\n"{choice(dialogue)}" - kawali\n'
    else:
      dialogue = ['kawali you don\'t have to do this','may the gods allow your survival','hope you remember your integrals','now you\'ve done it','oops','why is this not math']
      self.events += f'{Fore.YELLOW}kawali{Fore.RED} has started a {Fore.YELLOW}QUANTUM PHYSICS TEST{Fore.RESET}\n"{choice(dialogue)}" - Not_TNB\n'
    for f1 in self.fighters:
      if self.hell == False: f1.area = 'school'
      else: f1.area = 'school but worse'
      fate = randint(1,100)
      difficulty = randint(1,10)
      if self.hell == True: difficulty += 5
      passing = 3*(20-difficulty)+(f1.iq/10)
      self.events += f'{f1.Name} got a difficulty {difficulty} test '
      if fate < (passing / 2):
        if len(self.fighters) != 1:
          if self.hell == False: self.events += Fore.RED + 'but failed horribly and was executed by JIMMY\n' + Fore.RESET
          else: self.events += Fore.RED + 'and was reduced to a singularity' + Fore.RESET
          self.fighters.remove(f1)
        else:
          if self.hell == False: self.events += 'failed horribly and was supposed to be executed by JIMMY but was the last one standing\n'
          else: self.events += 'and almost broke down, but was spared by kawali as the victor'
      elif fate < passing:
        if self.hell == False:
          self.events += Style.BRIGHT + Fore.RED + 'but failed and was fucked over by JIMMY\n' + Style.RESET_ALL
          f1.Atk -= 300
          f1.Def -= 20
          if f1.Hp > 1500: f1.Hp = 1500
        else:
          self.events += Style.BRIGHT + Fore.RED + 'but failed and was obliterated by kawali\n' + Style.RESET_ALL
          f1.Atk = max(1,f1.Atk-500)
          f1.Def = max(1,f1.Def-100)
          f1.Hp = 500
      elif fate >= 95:
        if self.hell == False: self.events += Style.BRIGHT + Fore.YELLOW + 'and was blessed by JIMMY for getting an excellent score\n' + Style.RESET_ALL
        else: self.events += Fore.YELLOW + 'and overcame the overly ridiculous trial\n' + Style.RESET_ALL
        f1.Atk += 300
        f1.Def += 20
        f1.Hp += 1500
        f1.iq += 1
      else:
        if self.hell == False: self.events += 'and passed\n'
        else: self.events += 'and was spared from mindfuck\n'

  def eventAntiChurch(self):
    global arealist
    self.hell = True
    self.events += 'THE ANTICHURCH HAS AWOKEN\n' + Fore.RESET
    arealist = ['Flaming Forest','Broken City','Abandoned Metropolis','Burning Fields','Irredeemable Land','Death Valley','Antichurch']
    for f in self.fighters:
      f.area = choice(arealist)
      self.events += f'{f.Name} was forced to the {f.area}'
      if f.area == 'Antichurch':
        self.events += f'{Fore.RED} and was sacrificed{Fore.RESET}\n'
        self.fighters.remove(f)
      else: self.events += '\n'

class Fighter:
  def __init__(self, name: str):
    self.Name = name
    self.Hp = randint(3000, 6000)
    self.Atk = randint(300, 900)
    self.Def = randint(10, 50)
    self.Cd = randint(120, 200)
    self.Cr = randint(30, 70)
    self.Block = round(self.Def / 4)
    self.hunger = randint(40, 100)
    self.kills = 0
    self.dead = False
    self.Items = []
    self.area = 'Spawn'
    self.iq = randint(85, 140)

  def __str__(self):
    return Style.DIM + Fore.CYAN + f'Fighter {self.Name}:\n\tHP: {self.Hp}\n\tAtk: {self.Atk}\n\tDef: {self.Def}\n\tCrit: {self.Cr}/{self.Cd}\n\tHunger: {self.hunger}\n\t' + Style.RESET_ALL 
  
  def checkCannibal(self, other):
    cannibalism = randint(1,100)
    if (cannibalism <= 30 and self.hunger > 10) or (cannibalism <= 70 and self.hunger <= 10):
      hunger = randint(7,15)
      self.hunger += hunger
      self.Hp -= 1000
      if self.Hp <= 1:
        self.Hp = 1
      return f', they also ate {other.Name}\'s corpse and {Fore.GREEN}gained {hunger} hunger{Fore.RESET} but lost 1000 HP'
    return ''

  def grabSpecialItem(self, other):
    if (netherite in other.Items or (nukecodes in other.Items and nukecodes not in self.Items)) and len(self.Items) != 9:
      item = Weapon('', 0, '')
      for i in other.Items:
        if i == netherite or i == nukecodes:
          item = i
          break
      other.Items.remove(item)
      self.Items.append(item)
      if item == netherite: self.Def += 2 * (netherite.quality + 1)
      elif item == nukecodes: self.Atk += 12 * (nukecodes.quality + 1)
      return f' (they took the corpse\'s {item.name})'
    return ''

  def attack(self, other):
    crit = ''
    death = False
    if roll(other.Block, 100):                     # Account for Block chance
      return [f'{self.Name}\'s attack was blocked by {other.Name}!', death]
    dmg = randint(self.Atk-30, self.Atk+30)        # Atk-30 <= Base DMG <= Atk+30
    if roll(self.Cr, 100):                         # Account for chance of Crit
      dmg = dmg * self.Cd / 100 
      crit = f' {Fore.RED}CRITICAL{Fore.RESET}'
    dmg = dmg * (100 - other.Def) / 100            # Account for opponent's Def
    dmg = max(0, round(dmg))                       # Round DMG and set a minimum to 0
    other.Hp -= dmg                                # Subtract DMG from opponent's Hp
    if dmg == 0: dmg = f'{Fore.RED}no{Fore.RESET}'
    if other.Hp <= 0:
      self.kills += 1
      death = True
      chew = steal = ''
      self.checkCannibal(other)
      steal = self.grabSpecialItem(other)
      return [f'{self.Name} dealt {dmg}{crit} damage to {other.Name}{deathmsg[randint(0,len(deathmsg) - 1)]}{chew}{steal}', death]
    return [f'{self.Name} dealt {dmg}{crit} damage to {other.Name}', death]

  def heavy(self,other):
    original = self.Atk
    bonus = randint(600, 1000) # buff the attacker atk
    multiplier = 1 + random.random()
    self.Atk = round(self.Atk*multiplier) + bonus
    events = Fore.MAGENTA + f'HEAVY ATTACK ({self.Name} ON {other.Name}): \n' + Fore.RESET
    inres = self.attack(other)
    self.Atk = original # remove buffs
    return [events + '\t' + inres[0], inres[1]]

  def combo(self,other):
    hits = randint(3, 10) # number of hits
    events = Fore.MAGENTA + f'COMBO ({self.Name} ON {other.Name}):\n' + Fore.RESET # combo initiation
    inres = ''
    savedAtk = self.Atk
    for i in range(hits):
      self.Atk = round(savedAtk * ((11-i)/10))
      inres = self.attack(other)
      events += '\t' + inres[0] + '\n'
      if inres[1] == True: break
    self.Atk = savedAtk
    return [events, inres[1]]

def main():
  fighters = input('Input a comma seperated list of names\n> ').split(', ')
  battle = BattleField([Fighter(x) for x in fighters])

  print(Fore.CYAN + '\n---FIGHTER STATS---' + Fore.RESET)
  for f in battle.fighters: print(f)
  print()

  while len(battle.fighters) != 1:
    battle.progress()
    input()
  else:
    print(Fore.YELLOW + f'{battle.fighters[0].Name} WINS!!!\n{Fore.RESET}{battle.fighters[0]}\nHeld Items: ' + ', '.join([i.name for i in battle.fighters[0].Items]))
    input('Click Enter To Quit > ')
  
if __name__ == '__main__':
  main()
# theres nothing else down here
# i just wanted to add lines
# so it can become 500 lines
# because funni   - kawali
