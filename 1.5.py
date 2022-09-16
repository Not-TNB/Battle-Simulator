import random
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
armor = Weapon('a set of metal armor',7,'')
diamond = Weapon('diamond armor',8,'')
netherite = Weapon(f'{Fore.YELLOW}{Style.BRIGHT}NETHERITE{Style.RESET_ALL}',9,'')

weapons = [stick, knife, sword, axe, hammer, chainsaw, deagle, m4, m134, nukecodes]
armor = [paper, clothes, wood, leather, stone, metal, shield, armor, diamond, netherite]
misc = ['nothing','food','some water','communism','sand','dirt','a medkit','air???','a twig that snapped when they touched it','a stand arrow','food','food','food','food','food','food']
interaction = [' talked with ',' flipped off ',' casually said the n word in front of ',' played with ',' sang with ',' spied on ',' greeted ',' debated with ',' screamed at ',' wrote a message to ',' thought about brutally murdering ',' wanted to fight ',' puked right in front of ',' played a little game with ',' posed with ',' interrogated ',' threw a pie at ']
exinteraction = [[' told ',' to go die'],[' thought that fighting ',' was futile'],[' showed hentai to ',', who was disgusted'],[' joined ',' in acting weird'],[' caught ',' in 4k'],[' wanted to play ddakji with ',', who quickly refused'],[' played good cop while ',' played bad cop'],[' was confused on how to play squid game, ',' was confused too']]
deathmsg = [Fore.RED + i + Fore.RESET for i in [' and said a prayer before ending them',' and also slit their throat',' somehow breaking their neck',' thus finishing them off',' and put a bullet through their skull',' and said "omae wa mou shinderu"',' then teabagged them',' and made a hole through their stomach',' with a stab but didn\'t stop stabbing until they had 69 stab wounds',' and beheaded them']]
selfdeathmsg = [Fore.RED + i + Fore.RESET for i in [' killed themselves',' buried themselves in the ground',' frontflipped unsuccessfully',' tried to swim in lava',' walked off a building',' shot themself',' died',' got isekai\'d']]
selfinteraction = [' went AFK for a bit',' slept',' wandered around',' did nothing',' read a book',' did the fortnite dance',' looked at themselves in the mirror',' waited',' spaced out',' failed to kill themself']
arealist = ['Forest','Plains','School','City']

class BattleField:
  def __init__(self, fighters: list):
    self.fighters = fighters
    self.all_fighters = tuple(self.fighters)
    self.turns = 0
    self.events = ''

  def progress(self):
    self.turns += 1
    random.shuffle(self.fighters)
    self.events = f'---TURN {self.turns}---\n'
    if random.randint(1, 10) == 1:
      self.events += Fore.RED + 'WORLD EVENT\nWARNING: '
      random.choice([self.eventPlague, self.eventGoblin, self.eventNuclear, self.eventLightning, self.eventMath])()
      self.events += 'everyone else not mentioned also survived\n'
    else:
      for f1 in self.fighters:
        if random.randint(1,100) >= 75:
          newarea = random.choice(arealist)
          while newarea == f1.area:
            newarea = random.choice(arealist)
          f1.area = newarea
          self.events += f'{f1.Name} moved to the {newarea}\n'
        f1.hunger -= random.randint(2,7)
        if f1.hunger <= 0:
          f1.Hp -= 1000
          if f1.Hp <= 0:
            self.events += f'{f1.Name} {Fore.RED}died of starvation{Fore.RESET}\n'
            self.fighters.remove(f1)
        else:
          action = random.randint(1, 4)
          if action <= 2:
            f2 = random.choice(self.fighters)
            if f2 == f1:                                           # if the choice is themself,
              self.events += f'{f1.Name}'
              if random.randint(1, 6) == 1:                        # and they roll 1 on a d6,
                self.events += random.choice(selfdeathmsg) + '\n'       # they die
                self.fighters.remove(f1)
              else:
                self.events += random.choice(selfinteraction) + '\n'
            else:
              if random.randint(1, 2) == 1:
                if random.randint(1, 2) == 1:
                  self.events += f'{f1.Name}{random.choice(interaction)}{f2.Name}\n'
                else:
                  action = random.choice(exinteraction)
                  self.events += f'{f1.Name}{action[0]}{f2.Name}{action[1]}\n'
              else:
                fighterweapon = []
                chosenweapon = None
                tempatk = 0
                for i in f1.Items:
                  if i in weapons:
                    fighterweapon.append(i)
                if fighterweapon == []:
                  chosenweapon = fist
                else:
                  chosenweapon = random.choice(fighterweapon)
                if chosenweapon.type == 'ranged' and f2.area == f1.area:
                  tempatk = 30
                  self.events += f'{Back.RED}{f1.Name} got a damage penalty for trying to use a ranged weapon on {f2.Name}{Back.RESET}\n'
                elif chosenweapon.type == 'melee' and f2.area != f1.area:
                  tempatk = 1000
                  self.events += f'{Back.RED}{f1.Name} couldn\'t reach {f2.Name} with their melee weapon{Back.RESET}\n'
                savedatk = f1.Atk
                f1.Atk -= (f1.Atk * (tempatk / 100))
                f1.Atk = round(f1.Atk)
                skill = random.randint(1,6)
                if skill == 1:
                  res = f1.combo(f2)
                  self.events += res[0]
                  if res[1] == True: self.fighters.remove(f2)
                elif skill == 2:                         
                  res = f1.heavy(f2)
                  self.events += res[0] + '\n'
                  if res[1] == True: self.fighters.remove(f2)
                else:
                  res = f1.attack(f2)
                  self.events += res[0] + '\n'
                  if res[1] == True: self.fighters.remove(f2)
                f1.Atk = savedatk
          elif action == 3:
            thing = random.randint(1, 3)                           # category decider
            if thing == 1:
              item = random.choice(weapons)
              self.events += f'{f1.Name} found {Fore.BLUE}{item.name}{Fore.RESET} (quality {item.quality}, {item.type}), '
              if len(f1.Items) == 9:
                self.events += 'but their inventory is full so they ignored it\n'
              elif item in f1.Items:
                self.events += 'but they can\'t hold more than one of those\n'
              else:
                self.events += 'their ATK has increased\n'
                f1.Atk += 12 * (item.quality + 1)
                f1.Items.append(item)
            elif thing == 2:
              item = random.choice(armor)
              self.events += f'{f1.Name} found {Fore.BLUE}{item.name}{Fore.RESET} (quality {item.quality}), '
              if len(f1.Items) == 9:
                self.events += 'but their inventory is full so they ignored it\n'
              else:
                self.events += 'their DEF has increased\n'
                f1.Def += 2 * (item.quality + 1)
                f1.Items.append(item)
            else:
              item = random.choice(misc)
              self.events += f'{f1.Name} found {item}'
              if item == 'communism':
                self.events += f', {Fore.RED}their offensive stats increased{Fore.RESET}\n'
                f1.Atk += 100
                f1.Cr += 5
                f1.Cd += 30
              elif item == 'a medkit':
                addedHp = random.randint(1000, 2000)
                self.events += f', {Fore.GREEN}they gained {addedHp}HP{Fore.RESET}\n'
                f1.Hp += addedHp
              elif item == 'a stand arrow':
                if random.randint(1, 5) != 5:
                  self.events += f', {Fore.RED}but died trying to use it{Fore.RESET}\n' # oof
                  self.fighters.remove(f1)
                else:
                  self.events += f' and obtained a {Fore.YELLOW}{Back.MAGENTA}stand{Style.RESET_ALL}\n'
                  f1.Hp += 3000
                  f1.Atk += 150
                  if f1.Def < 75:
                    f1.Def += 5
                  f1.Cr += 10
                  f1.Cd += 100
              elif item == 'food':
                foodType = random.randint(1, 5)
                if foodType == 1:
                  self.events += f' and ate it {Fore.RED}just to die from food poisoning{Fore.RESET}\n'
                  self.fighters.remove(f1)
                elif foodType == 2:
                  self.events += f', {Fore.GREEN}it was the best meal they had thus recovering 30 hunger and 1000 HP{Fore.RESET}\n'
                  f1.hunger += 30
                  f1.Hp += 1000
                else:
                  saturation = random.randint(10,20)
                  self.events += f' and ate it thus recovering {Fore.GREEN}{str(saturation)} hunger and 250 HP{Fore.RESET}\n'
                  f1.hunger += saturation
                  f1.Hp += 250
              else:
                self.events += '\n'
      if self.events == f'---TURN {self.turns}---\n':
        self.events += 'Nothing happened this turn\n'
    self.events += f'\nCurrent Stats:\n'
    for f in self.all_fighters:
      if f not in self.fighters: self.events += Style.DIM + Fore.RED + f'\t{f.Name}: 0 HP, {f.kills} kills [' + ', '.join([f'{Fore.RED}{i.name}{Fore.RED}' for i in f.Items]) + Style.DIM + Fore.RED + '] (DEAD)' + Style.RESET_ALL
      else: self.events += f'\t{f.Name}: {f.Hp} HP, {f.kills} kills, in {f.area} [' + ', '.join([i.name for i in f.Items]) + ']'
      self.events += '\n'
    self.events += Style.DIM + Fore.CYAN + f'\nFighters left: {len(self.fighters)}\n' + Style.RESET_ALL
    print(self.events + f'---END OF TURN {self.turns}---\n\n')
  
  def eventNuclear(self):
    self.events += f'NUCLEAR LAUNCH INBOUND\n' + Fore.RESET
    for f1 in self.fighters:
      if nukecodes in f1.Items and random.randint(1, 3) == 1:
        self.events += f'{str(f1.Name)}: Who the fuck used MY nuclear launch codes?!\n'
    # the carnage begins
    for f1 in self.fighters:
      fate = random.randint(1, 80) + (f1.iq / 10)
      if fate <= 20 and len(self.fighters) != 1:
        self.events += f'{str(f1.Name)} {Fore.RED}died on the initial blast.{Fore.RESET}\n'
        self.fighters.remove(f1)
      elif fate <= 52 and len(self.fighters) != 1:
        f2 = random.choice(self.fighters)
        if f2 == f1:
          self.events += f'{f1.Name} {Fore.RED}died to flying debris hitting their head.{Fore.RESET}\n'
          self.fighters.remove(f1)
        else:
          self.events += f'{f1.Name} smacked {f2.Name} so hard that they {Fore.RED}died{Fore.RESET} '
          self.fighters.remove(f2)
          f1.kills += 1
          if random.randint(1,3) < 3 and len(self.fighters) != 1:
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
    self.events += f'SECTOR PLAGUE DETECTED\n' + Fore.RESET
    sector = []
    area = random.choice(arealist)
    for i in self.fighters:
      if i.area == area:
        sector.append(i)
    caught = ', '.join([i.Name for i in sector]) if sector != [] else 'None'
    self.events += f'AFFECTED SECTOR: {area}\nFIGHTERS CAUGHT: ' + caught + '\n'
    for f1 in sector:
      fate = random.randint(1,90) + (f1.iq / 10)
      if fate <= 30 and len(self.fighters) != 1:
        self.events += f'{f1.Name} {Fore.RED}died to the plague{Fore.RESET}\n'
        self.fighters.remove(f1)
        sector.remove(f1)
      elif fate <= 65 and len(self.fighters) != 1:
        f2 = random.choice(sector)
        if f2 != f1:
          self.events += f'{f1.Name} pushed {f2.Name} {Fore.RED}into the plague cloud{Fore.RESET} '
          self.fighters.remove(f2)
          sector.remove(f2)
          f1.kills += 1
          if random.randint(1,2) == 1 and len(self.fighters) != 1:
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
    self.events += 'GOBLINS INCOMING\n' + Fore.RESET
    death = [Fore.RED + i + Fore.RESET for i in [' got a knife thrown towards their head\n',' got ganged on by a shit ton of goblins\n',' fought until their last breath\n',' nearly escaped only to get blown up\n',' fucking died\n']]
    live = [' killed a few goblins on their way out\n',' survived\n',' ran away safely\n',' participated in ending the invasion\n',' managed to 360-no scope a goblin, damn\n']
    for f1 in self.fighters:
      fate = random.randint(1,80) + (f1.Atk / 100)
      if fate <= 30 and len(self.fighters) != 1:
        self.events += f1.Name + random.choice(death)
        self.fighters.remove(f1)
      elif fate <= 70 and len(self.fighters) != 1:
        damage = round(random.randint(600,1500) * (100 - f1.Def) / 100)
        f1.Hp -= damage
        if f1.Hp <= 0:
          self.events += f'{f1.Name} took {str(damage)} damage and{random.choice(death)}'
          self.fighters.remove(f1)
        else:
          self.events += f'{f1.Name} took {str(damage)} damage but{random.choice(live)}'
      else:
        self.events += f1.Name + random.choice(live)
  
  def eventLightning(self):
    self.events += 'INSANE THUNDERSTORM INCOMING\n' + Fore.RESET
    for f1 in self.fighters:
      fate = random.randint(1,3)
      if fate == 1 and len(self.fighters) != 1:
        self.events += f1.Name + f'{Fore.RED} was struck by lightning{Fore.RESET}\n'
        self.fighters.remove(f1)
      else:
        self.events += f1.Name + ' survived\n'

  def eventMath(self):
    dialogue = ['Not_TNB what the fuck are you doing here','what','hey uh Not_TNB why are you giving everyone a math test','are we making this an intelligence fight now']
    self.events += f'{Fore.CYAN}Not_TNB (aka JIMMY){Fore.RED} has started a {Fore.CYAN}MATH TEST?{Fore.RESET}\n"{random.choice(dialogue)}" - kawali\n'
    for f1 in self.fighters:
      f1.area = 'School'
      fate = random.randint(1,100)
      difficulty = random.randint(1,10)
      passing = 3*(20-difficulty)+(f1.iq/10)
      self.events += f'{f1.Name} got a difficulty {difficulty} test '
      if fate < (passing / 2):
        if len(self.fighters) != 1:
          self.events += Fore.RED + 'but failed horribly and was executed by JIMMY\n' + Fore.RESET
          self.fighters.remove(f1)
        else:
          self.events += 'failed horribly and was supposed to be executed by JIMMY but was the last one standing\n'
      elif fate < passing:
        self.events += Style.BRIGHT + Fore.RED + 'but failed and was fucked over by JIMMY\n' + Style.RESET_ALL
        f1.Atk -= 300
        f1.Def -= 20
        if f1.Hp > 1500: f1.Hp = 1500
      elif fate >= 95:
        self.events += Style.BRIGHT + Fore.YELLOW + 'and was blessed by Jimmy for getting an excellent score\n' + Style.RESET_ALL
        f1.Atk += 300
        f1.Def += 20
        f1.Hp += 1500
        f1.iq += 1
      else:
        self.events += 'and passed\n'

class Fighter:
  def __init__(self, name: str):
    self.Name = name
    self.Hp = random.randint(3000, 6000)
    self.Atk = random.randint(300, 900)
    self.Def = random.randint(10, 50)
    self.Cd = random.randint(120, 200)
    self.Cr = random.randint(30, 70)
    self.Block = round(self.Def / 4)
    self.hunger = random.randint(40,100)
    self.kills = 0
    self.dead = False
    self.Items = []
    self.area = 'Spawn'
    self.iq = random.randint(85,140)

  def __str__(self):
    return Style.DIM + Fore.CYAN + f'Fighter {self.Name}:\n\tHP: {self.Hp}\n\tAtk: {self.Atk}\n\tDef: {self.Def}\n\tCrit: {self.Cr}/{self.Cd}\n\t' + Style.RESET_ALL 
  
  def attack(self, other):
    crit = ''
    death = False
    if random.randint(1, 100) <= other.Block:      # Account for chance of Block
      return [f'{self.Name}\'s attack was blocked by {other.Name}!', death]
    dmg = random.randint(self.Atk-30, self.Atk+30) # Base DMG is from Atk-30 to Atk+30
    if random.randint(1, 100) <= self.Cr:          # Account for chance of Crit
      dmg = dmg * self.Cd / 100 
      crit = f' {Fore.RED}CRITICAL{Fore.RESET}'
    dmg = dmg * (100 - other.Def) / 100            # Account for opponent's Def
    dmg = round(dmg)                               # Round DMG
    if dmg < 0:
      dmg = 0
    other.Hp -= dmg                                # Subtract DMG from opponent's Hp
    if dmg == 0:
      dmg = f'{Fore.RED}no{Fore.RESET}'
    if other.Hp <= 0:
      self.kills += 1
      death = True
      chew = ''
      steal = ''
      cannibalism = random.randint(1,100)
      if (cannibalism <= 30 and self.hunger > 10) or (cannibalism <= 70 and self.hunger <= 10):
        hunger = random.randint(7,15)
        chew = f', they also ate {other.Name}\'s corpse and {Fore.GREEN}gained {hunger} hunger{Fore.RESET} but lost 1000 HP'
        self.hunger += hunger
        self.Hp -= 1000
        if self.Hp <= 1:
          self.Hp = 1
      if (netherite in other.Items or (nukecodes in other.Items and nukecodes not in self.Items)) and len(self.Items) != 9:
        item = None
        for i in other.Items:
          if i == netherite or i == nukecodes:
            item = i
            break
        steal = f' (they took the corpse\'s {item.name})'
        other.Items.remove(item)
        self.Items.append(item)
        if item == netherite:
          self.Def += 2 * (netherite.quality + 1)
        else:
          self.Atk += 12 * (nukecodes.quality + 1)
      return [f'{self.Name} dealt {dmg}{crit} damage to {other.Name}{deathmsg[random.randint(0,len(deathmsg) - 1)]}{chew}{steal}', death]
    return [f'{self.Name} dealt {dmg}{crit} damage to {other.Name}', death]

  def heavy(self,other):
    bonus = random.randint(600, 1200)               # buff the attacker atk
    self.Atk += bonus
    events = Fore.MAGENTA + f'HEAVY ATTACK ({self.Name} ON {other.Name}): \n' + Fore.RESET
    inres = self.attack(other)
    self.Atk -= bonus                              # remove buff
    return [events + '\t' + inres[0], inres[1]]

  def combo(self,other):
    hits = random.randint(3, 10)                                                   # number of hits
    events = Fore.MAGENTA + f'COMBO ({self.Name} ON {other.Name}):\n' + Fore.RESET # combo initiation
    for i in range(hits):
      inres = self.attack(other)
      events += '\t' + inres[0] + '\n'
      if inres[1] == True: break
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
