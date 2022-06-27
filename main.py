import random
weapons = [[0,'a stick'],[1,'a knife'],[2,'a sword'],[3,'an axe'],[4,'a hammer'],[5,'a chainsaw'],[6,'a deagle'],[7,'an M16'],[8,'a literal M134 Minigun'],[9,'nuclear launch codes, who the hell hid those in the field']]
armor = [[0,'a sheet of paper'],[1,'some clothes'],[2,'some wood'],[3,'some leather padding'],[4,'a stone block'],[5,'a metal plate'],[6,'a decent shield'],[7,'some metal armor'],[8,'diamond armor'],[9,'actual netherite']]
misc = ['nothing','disappointment','some water','communism','sand','dirt','a medkit','air???','a twig that snapped when they touched it','a stand arrow']
interaction = [' talked with ',' flipped off ',' casually said the n word in front of ',' played with ',' sang with ',' spied on ',' greeted ',' debated with ',' looked at the border with ',' threw rocks at the sea with ',' thought about brutally murdering ',' wanted to fight ',' puked right in front of ',' played a little game with ',' posed with ',' interrogated ',' threw a pie at ']
exinteraction = [[' told ',' to go die'],[' thought that fighting ',' was futile'],[' showed hentai to ',', who was disgusted'],[' joined ',' in acting weird'],[' caught ',' in 4k'],[' wanted to play ddakji with ',', who quickly refused'],[' tried ','\'(s) homemade cooking'],[' played good cop while ',' played bad cop'],[' was confused on how to play squid game, ',' was confused too']]
deathmsg = [' and said a prayer before ending them',', also they slit their throat',' somehow breaking their neck',' and buried them',' thus finishing them off',' and put a bullet through their skull',' and spat on their dead body',', they said "omae wa mou shinderu"',' then teabagged them',', destroying their mind in the process',' with a stab but didn\'t stop stabbing until they had 48 stab wounds',' and beheaded them']

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
    if random.randint(1,100) <= 10:
      event = random.randint(1,3)
      if event == 1:
        self.eventPlague()
      elif event == 2:
        self.eventGoblin()
      else:
        self.eventNuclear()
      self.events += 'everyone else not mentioned also survived\n'
    else:
      for f1 in self.fighters:
        action = random.randint(1, 4)
        if action <= 2:
          f2 = random.choice(self.fighters)
          if f2 == f1:                                           # if the choice is themself,
            self.events += f'{f1.Name} tried to attack themself,'
            if random.randint(1, 5) == 1:                        # and they roll 1 on a d5
              self.events += ' committing suicide in the process\n'   # they die
              self.fighters.remove(f1)
            else:
              self.events += ' but yeah no\n'
          else:
            if random.randint(1, 2) == 1:
              if random.randint(1, 2) == 1:
                self.events += f'{f1.Name}{random.choice(interaction)}{f2.Name}\n'
              else:
                action = random.choice(exinteraction)
                self.events += f'{f1.Name}{action[0]}{f2.Name}{action[1]}\n'
            else:
              skill = random.randint(1, 5)                       # skill chosen
              if skill <= 2:                                     # if it's 1 or 2
                res = f1.combo(f2)
                self.events += res[0]
                if res[1] == True:
                  self.fighters.remove(f2)
              elif skill == 5:                                   # else if it's 5
                res = f1.heavy(f2)                               # remove buff
                self.events += '\t' + res[0] + '\n'
                if res[1] == True:
                  self.fighters.remove(f2)
                  break
              else:
                res = f1.attack(f2)
                self.events += res[0] + '\n'
                if res[1] == True: self.fighters.remove(f2)
        elif action == 3:
          thing = random.randint(1, 3)                           # category decider
          if thing == 1:
            item = random.choice(weapons)
            self.events += f'{f1.Name} found {item[1]} (quality {str(item[0])}), '
            if len(f1.Items) == 9:
              self.events += 'but their inventory is full'
              if item[0] <= 4:
                self.events += ' so they ignored it\n'
              elif random.randint(1,4) > 1:
                for i in range(5):
                  thing = weapons[i]
                  if thing in f1.Items:
                    f1.Items.remove(thing)
                    events += f' so they discarded their {thing[1]} for a better weapon\n'
                    f1.Atk -= 12 * (thing[0] + 1)
                    f1.Atk += 12 * (item[0] + 1)
                    f1.Items.append(item)
                    break
                thing = random.choice(f1.Items)
                self.events += f' so they removed their {thing[1]} and took the weapon\n'
                f1.Items.remove(thing)
                if thing in weapons:
                  f1.Atk -= 12 * (thing[0] + 1)
                elif thing in armor:
                  f1.Def -= 2 * (thing[0] + 1)
                f1.Atk += 12 * (item[0] + 1)
                f1.Items.append(item)
            elif item in f1.Items:
              self.events += 'but they can\'t hold more than one of those\n'
            else:
              self.events += 'their ATK has increased\n'
              f1.Atk += 12 * (item[0] + 1)
              f1.Items.append(item)
          elif thing == 2:
            item = random.choice(armor)
            self.events += f'{f1.Name} found {item[1]} (quality {str(item[0])}), '
            if len(f1.Items) == 9:
              self.events += 'but their inventory is full'
              if item[0] <= 4:
                self.events += ' so they ignored it\n'
              elif random.randint(1,4) > 1:
                for i in range(5):
                  thing = armor[i]
                  if thing in f1.Items:
                    f1.Items.remove(thing)
                    self.events += f' so they discarded their {thing[1]} for some better armor (pieces)\n'
                    f1.Def -= 2 * (thing[0] + 1)
                    f1.Def += 2 * (item[0] + 1)
                    f1.Items.append(item)
                    break
                thing = random.choice(f1.Items)
                self.events += f' so they removed their {thing[1]} and took the armor (piece)\n'
                f1.Items.remove(thing)
                if thing in weapons:
                  f1.Atk -= 12 * (thing[0] + 1)
                elif thing in armor:
                  f1.Def -= 2 * (thing[0] + 1)
                f1.Atk += 12 * (item[0] + 1)
                f1.Items.append(item)
            else:
              self.events += 'their DEF has increased\n'
              f1.Def += 2 * (item[0] + 1)
              f1.Items.append(item)
          else:
            item = random.choice(misc)
            self.events += f'{f1.Name} found {item}'
            if f1.Items == 9 and item == 'communism':
              self.events += ', but their inventory is full\n'
            elif item == misc[3]:
              self.events += ', they obtained the blessings of the Soviet Union\n'
              f1.Atk += 100
              f1.Cr += 5
              f1.Cd += 30
              f1.Items.append(item)
            elif item == misc[6]:
              self.events += ', they healed themselves\n'
              f1.Hp += random.randint(1000,2000)
            elif item == misc[9]:
              if random.randint(1, 5) != 5:
                self.events += ', but died trying to use it\n'           # oof
                self.fighters.remove(f1)
              else:
                self.events += ', and obtained a stand\n'
                f1.Hp += 3000
                f1.Atk += 150
                if f1.Def < 75:
                  f1.Def += 5
                f1.Cr += 10
                f1.Cd += 100
            else:
              self.events += '\n'
      if self.events == f'---TURN {self.turns}---\n':
        self.events += 'Nothing happened this turn\n'
    self.events += f'\nCurrent Stats:\n'
    for f in self.all_fighters:
      if f not in self.fighters: self.events += f'\t{f.Name}: 0 HP, {f.kills} kills (DEAD)\n'
      else: self.events += f'\t{f.Name}: {f.Hp} HP, {f.kills} kills\n'
    self.events += f'\nFighters left: {len(self.fighters)}\n'
    print(self.events + f'---END OF TURN {self.turns}---\n\n')
  
  def eventNuclear(self):
    self.events += f'WORLD EVENT\nWARNING: NUCLEAR LAUNCH INBOUND\n'
    for f1 in self.fighters:
      if [9,'nuclear launch codes, who the hell hid those in the field'] in f1.Items and random.randint(1,3) == 1:
        self.events += f'{str(f1.Name)}: Who the fuck used MY nuclear launch codes?!\n'
    # the carnage begins
    for f1 in self.fighters:
      fate = random.randint(1,8)
      if fate <= 2 and len(self.fighters) != 1:
        self.events += f'{str(f1.Name)} died on the initial blast.\n'
        self.fighters.remove(f1)
      elif fate <= 5 and len(self.fighters) != 1:
        f2 = random.choice(self.fighters)
        if f2 == f1:
          self.events += f'{f1.Name} died to flying debris hitting their head.\n'
          self.fighters.remove(f1)
        else:
          self.events += f'{f1.Name} smacked {f2.Name} real hard they died '
          self.fighters.remove(f2)
          f1.kills += 1
          if random.randint(1,3) < 3 and len(self.fighters) != 1:
            self.events += 'but they failed to escape the radiation, get karma\'ed\n'
            self.fighters.remove(f1)
          else:
            self.events += 'and they managed to escape unscathed\n'
      elif fate <= 6 and len(self.fighters) != 1:
        self.events += f'{f1.Name} managed to escape the blast but could not survive the radiation\n'
        self.fighters.remove(f1)
      else:
        self.events += f'{f1.Name} survived\n'

  def eventPlague(self):
    self.events += f'WORLD EVENT\nWARNING: SECTOR PLAGUE DETECTED\n'
    sector = []
    for i in self.fighters:
      if random.randint(1,4) == 1:
        f1 = random.choice(self.fighters)
        if f1 not in sector:
          sector.append(f1)
    self.events += 'FIGHTERS CAUGHT:\n'
    for i in sector:
      self.events += f'- {i.Name}\n'
    for f1 in sector:
      fate = random.randint(1,3)
      if fate == 1 and len(self.fighters) != 1:
        self.events += f'{f1.Name} died to the plague\n'
        self.fighters.remove(f1)
        sector.remove(f1)
      elif fate == 2 and len(self.fighters) != 1:
        f2 = random.choice(sector)
        if f2 != f1:
          self.events += f'{f1.Name} pushed {f2.Name} into the plague cloud '
          self.fighters.remove(f2)
          sector.remove(f2)
          f1.kills += 1
          if random.randint(1,2) == 1 and len(self.fighters) != 1:
            self.events += 'but unintentionally pushed themselves in too\n'
            self.fighters.remove(f1)
            sector.remove(f1)
          else:
            self.events += 'and lived\n'
        else:
          self.events += f'{f1.Name} tripped on a rock whilst trying to escape ENTITY_PLAGUE_CLOUD\n'
          self.fighters.remove(f1)
          sector.remove(f1)
      else:
        self.events += f'{f1.Name} survived\n'
    
  def eventGoblin(self):
    self.events += 'WORLD EVENT\nWARNING: GOBLINS INCOMING\n'
    death = [' got a knife thrown towards their head\n',' got ganged on by a shit ton of goblins\n',' fought until their last breath\n',' nearly escaped only to get blown up\n',' fucking died\n']
    live = [' killed a few goblins on their way out\n',' survived\n',' ran away safely\n',' participated in ending the invasion\n',' managed to 360-no scope a goblin, damn\n']
    for f1 in self.fighters:
      fate = random.randint(1,4)
      if fate <= 2 and len(self.fighters) != 1:
        self.events += f1.Name + random.choice(death)
        self.fighters.remove(f1)
      elif fate == 3 and len(self.fighters) != 1:
        damage = round(random.randint(600,1500) * (100 - f1.Def) / 100)
        f1.Hp -= damage
        if f1.Hp <= 0:
          self.events += f'{f1.Name} took {str(damage)} damage and{random.choice(death)}'
          self.fighters.remove(f1)
        else:
          self.events += f'{f1.Name} took {str(damage)} damage but{random.choice(live)}'
      else:
        self.events += f1.Name + random.choice(live)

class Fighter:
  def __init__(self, name: str):
    self.Name = name
    self.Hp = random.randint(3000, 6000)
    self.Atk = random.randint(200, 800)
    self.Def = random.randint(10, 50)
    self.Cd = random.randint(120, 200)
    self.Cr = random.randint(30, 70)
    self.Block = round(self.Def / 4)
    self.kills = 0
    self.dead = False
    self.Items = []

  def __str__(self):
    return f'Fighter {self.Name}:\n\tHP: {self.Hp}\n\tAtk: {self.Atk}\n\tDef: {self.Def}\n\tCrit: {self.Cr}/{self.Cd}\n\t'    
  
  def attack(self, other):
    crit = ''
    death = False
    if random.randint(1, 100) <= other.Block:      # Account for chance of Block
      return [f'{self.Name}\'s attack was blocked by {other.Name}!', death]
    dmg = random.randint(self.Atk-30, self.Atk+30) # Base DMG is from Atk-30 to Atk+30
    if random.randint(1, 100) <= self.Cr:          # Account for chance of Crit
      dmg = dmg * self.Cd / 100 
      crit = ' (CRIT)'
    dmg = dmg * (100 - other.Def) / 100            # Account for opponent's Def
    dmg = round(dmg)                               # Round DMG
    other.Hp -= dmg                                # Subtract DMG from opponent's Hp
    if other.Hp <= 0:
      self.kills += 1
      death = True
      return [f'{self.Name} dealt {dmg} damage to {other.Name}{deathmsg[random.randint(0,len(deathmsg) - 1)]}{crit}', death]
    return [f'{self.Name} dealt {dmg} damage to {other.Name}{crit}', death]

  def heavy(self,other):
    bonus = random.randint(600,1200)                 # buff the attacker atk
    self.Atk += bonus
    events = f'HEAVY ATTACK ({self.Name} ON {other.Name}):\n'
    inres = self.attack(other)
    self.Atk -= bonus                                  # remove buff
    return [events + inres[0],inres[1]]

  def combo(self,other):
    hits = random.randint(3, 10)                     # number of hits
    events = f'COMBO ({self.Name} ON {other.Name}):\n'   # combo initiation
    for i in range(hits):
      inres = self.attack(other)
      events += '\t' + inres[0] + '\n'
      if inres[1] == True:
        break
    return [events,inres[1]]

def main():
  fighters = input('Input a comma seperated list of names\n>>> ').split(', ')
  battle = BattleField([Fighter(x) for x in fighters])

  print('\n---CHARACTER STATS---')
  for f in battle.fighters: print(f)
  print()

  while len(battle.fighters) != 1:
    battle.progress()
    input()
  else:
    print(f'{battle.fighters[0].Name} WINS!!!\n{battle.fighters[0]}\nHeld Items: {battle.fighters[0].Items}')
    input('Click Enter To Quit > ')
  
if __name__ == '__main__':
  main()
