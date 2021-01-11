import re
import math
from datetime import datetime
#filecheck = re.compile(r'\w+\s*\.txt')

#whatsapp = input('Enter whatsapp file name.txt:\n')
	

count = 0
#This is used to count message per sendet
messsender = {}


message_sent ={}


messinfo = []


active_user =  0

wordcount_user = {}

himess ={}

stopworda =['my', 'My', 'can', 'Can','is','this','This','and', 'And', 'a', 'A', 'or', 'an', '-', ',', ':', '.', 'you', 'are', 'as', 'at','be', 'by','do', '=', 'her', 'his', 'it', '*', 'I', 'of', 'The', 'the', 'we', 'We', 'to', 'To','on', 'in', 'In','ma', 'Ma', 'ok', 'Ok', 'OK', 'was', 'not', 'Not', 'Sir', 'sir', 'Mrs', 'mrs', 'did', 'You', 'Your', 'your', 'for', 'For', 'My', 'I\'m', 'all', 'All', 'have', 'Have', 'let', 'Let', 'yes', 'Yes', 'no', 'No', 'will', 'Will', 'with', 'With', 'me', ]

def stopwords(w):
	for x in stopworda:
		if x == w:
			return
	return w
	
def highestmess(message):
	c = [b for a, b in message.items ()]
	c.sort(reverse=True)
	d = c[0]
	i = {}
	for g, h in message.items():
		if h == d:
			i.setdefault(g,h)
	return i
			
	
#÷÷÷÷÷÷÷÷÷÷÷÷÷÷This is for daychat data	
date_regex = re.compile (r'\d{4}-\d{2}-\d{2},')#\s(\d+):\d{2}\s(a.m|p.m).
daysw = {}		
	
	
####-------------------------------------------------------------------------------------------#########
#This is the pattern for matching.
message = re.compile(r'(?P<mdate>\d{4}-\d{2}-\d{2}),\s(?P<mtime>\d+:\d{2}\s(?:a.m.|p.m.))\s-(?P<msender>(?:(?:\s\w*)*)[^:]*):\s(?P<mess>.*)')
messagecon =re.compile(r'(\d{4}-\d{2}-\d{2}),\s(\d+:\d{2}\s(a.m.|p.m.))\s-')

#"/home/owonuro/scripts3/basic4.txt"
with open('/sdcard/qpython/scripts3/basic4.txt') as whatsapp:
    whatsapp2 = whatsapp.readlines()
    for line in whatsapp2:
      
        message1 = message.search(line)
          
        if message1:
            count +=1
            sender = message1.group('msender')
            date = message1.group('mdate')
            time = message1.group('mtime')
            realmessage =message1.group('mess')
            
            #This is used to arrange the messages into dic and list.
            message_sent.setdefault(sender,[])
            ab = message_sent[sender]
            ab.append({})
            
            messsender.setdefault(sender, 0)
            x = messsender[sender]
            
            """The x in the code below is used to create 
            individual dictionary for messages, dates and time"""
            abc = ab[x]
            abc.setdefault('date',date)
            abc.setdefault('time',time)
            abc.setdefault('message',realmessage)
            
            #This is used to count the messages from each person.
            
            messsender[sender] = messsender[sender]+1
        #This condition help to get other info that are not direct message.  
        else:
            messagecon1 = messagecon.search(line)
            if messagecon1:
                #messinfo.append(line)
                
                """file1 = open('/sdcard/qpython/scripts3/whatsre.txt', 'a+')
                file1.write(f'*{line} \n')
                file1.close()"""
            
            #This is used to group messages that does not start with date but is an additional message. 
            else:
                abc['message'] = abc['message'] +' '+line

################################################################################################
        regexdate = date_regex.search(line)
        if regexdate:
            test = regexdate.group (0)
            count += 1
            time_t = datetime.strptime(test,"%Y-%m-%d,")#2020-04-16, 9:10 a.m.
            time_2 =datetime.ctime (time_t)
            days =time_2.split ()[0]
            daysw.setdefault(days, 0)
            daysw[days] = daysw [days] + 1
            #print (daysw)
#######################################More of day chart code above
###----------------------------------------------------------------------------------------------------------------------------####
               
  
for o, p in message_sent.items():
	wordcount_user.setdefault(o, {})
	for zc, zd in wordcount_user.items():
		zd.setdefault('media', 0)
		zd.setdefault('words', 0)
		zd.setdefault('messages', 0)
		zd.setdefault('most_used_words', [])
	#mostu store most used word for more analysis
	mostu = {}
	
	for q in p:
		
		za = q['message']
		if za != 'This message was deleted':
			if za == '<Media omitted>':
				zd['media'] = zd['media'] + 1
			else:
				zb = za.split()
				ze = len(zb)
				zd['words'] = zd['words'] + ze
				for wo5 in zb:
					wo = stopwords(wo5)
					if wo == wo5:
						mostu.setdefault(wo, 0)
						mostu[wo] = mostu[wo] +1
	woa = wordcount_user
	wob = woa[o]
	woc = wob['most_used_words']
	
	
	
	mostu2 =[]
	mostu3 = []
	for zj in mostu.values():
		mostu2.append(zj)
	mostu2.sort(reverse=True)
	if len(mostu2) > 2:
		mostu3 = mostu2[0:3]
	for wo2 in mostu3:
		for zl, zm in mostu.items():
			if wo2 == zm:
				woc.append(zl)
###--------------------------------------------------------------------------------------------###	

				

 
#####------------------------------------------------------------------------------------##
#This is used to add the message count into the wordcount_user dic.
for ca, cb in messsender.items():
	for cc, cd in wordcount_user.items():
		if ca == cc:
			cd['messages'] =cd['messages']+cb

###---------------------------------------------------------------------------------------------###






###----------------------------------------------------------------------------------------############


####----------------------------------------------------------------------------###
#This is to calculate final results
for zf, zg in wordcount_user.items():
	
	mostu4 = list(set(zg['most_used_words']))
	if len(mostu4) <= 2:
		mostu5 = 0
	else:
		mostu5 =', '.join(mostu4)
	
		
	active_user +=1
	zh = zg['messages'] - zg['media']
	if zh != 0:
		zi = zg['words'] //zh
	elif zh == 0:
		zi = zh
	print(f"{active_user}. {zf} \n\tMessages sent: {zg['messages']} \n\tTotal Words: {zg['words']} \n\tMedias sent: {zg['media']} \n\tWords per message: {zi} \n\tCommon words: {mostu5}\n")



###-----------------------------------------------------------------------##    
xa = highestmess(messsender)
    
print(f'Total messages sent: {count}.') 
print(f'Active members: {active_user}.')
print(f'Average messages: {count//active_user}.')
for ra, ma in xa.items():
	ru=ra.strip()
	print(f'{ru} has the highest messages: {ma}')


#############DAY CHART ANALYSIS########################### 

days_week = ['Mon', 'Tue', 'Wed','Thu','Fri','Sat','Sun']
print ('\nACTIVE DAYS CHART')
for day in days_week:
    for days, no in daysw.items ():
        if day == days:
            a ='■'
            print (f'{day} •>{a*math.ceil(no/33)}')
               
###--------------------------------------------------------------------------##        
"""for se, me in message_sent.items():
	print(f'~{se}: \n{me}')"""
