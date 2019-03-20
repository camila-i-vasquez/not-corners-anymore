import h5py
import pandas as pd
import numpy as np

from h5py import File

file_name = 'nyu_depth_data_labeled.mat'
def dataProcessing(filename):
   f = h5py.File(filename, 'r')
   my_dict = {}
   my_dict['accelData'] = ['roll', 'yaw',  'pitch', 'tilt']
   my_dict['depths']=['height', 'width', 'N']
   my_dict['images'] =['height', 'width', 'RGB', 'N']
   my_dict['labels']=['height', 'width', 'N']
   my_dict['names']=['names']
   my_dict['rawDepths']=['height','width', 'N']
   accelData=f['accelData'][()]
   depths = f['depths'][()]
   images = f['images'][()]
   labels = f['labels'][()]
   rawDepths = f['rawDepths'][()]
   names=[]
   for name in f.get("names"):
    names.append("".join(list(map(lambda x: chr(x), list(f[name[0]])))))
   np.save('accelData', accelData)
   np.save('depths', depths)
   np.save('images', images)
   np.save('labels', labels)
   np.save('names', names)
   np.save('rawDepths', rawDepths)

dataProcessing(file_name)
def loadingData():
   accelData = np.load('accelData.npy')
   depths = np.load('depths.npy')
   images = np.load('images.npy')
   labels =np.load('labels.npy')
   names = np.load('names.npy')
   rawDepths = np.load('rawDepths.npy')
   return accelData,depths,images,labels,names, rawDepths
   #accelData,depths,images,labels,names, rawDepths =loadingData() makes all these arrays available to you in that file
   #it takes hella time but... 
#cleaning up name df
name =np.load('names.npy')
names_df = pd.DataFrame(data=name, columns=['name'])
names_df.isnull().sum()
for name in names_df['name']:
    print(name)
test=names_df['name'].unique()
names_df['name']=names_df['name']\
    .str.replace('bagf', 'bag')\
    .str.replace('bear can','beer can')\
    .str.replace('bbasket', 'basket')\
    .str.replace('billo', 'bills')\
    .str.replace('biro','bird')\
    .str.replace('blines','blind')\
    .str.replace('board_','board')\
    .str.replace('body sparay', 'body spray')\
    .str.replace('boo', 'book')\
    .str.replace('troly', 'trolley')\
    .str.replace('bottled water', 'bottle of water')\
    .str.replace('bourd', 'board')\
    .str.replace('box of raisens', 'box of raisins')\
    .str.replace('broad', 'bread')\
    .str.replace('bup', 'bun')\
    .str.replace('cahir','chair')\
    .str.replace('calender', 'calendar')\
    .str.replace('bulb point', 'bulb')\
    .str.replace('cabinet  desk', 'cabinet desk')\
    .str.replace('carboard', 'cardboard')\
    .str.replace('card board', 'cardboard')\
    .str.replace('card borad', 'cardboard')\
    .str.replace('carten', 'carton')\
    .str.replace('caserol', 'casserole')\
    .str.replace('celling', 'ceiling')\
    .str.replace('char', 'chair')\
    .str.replace('chapathi', 'chapati')\
    .str.replace('charir', 'chair')\
    .str.replace('cigratte', 'cigarette')\
    .str.replace('cloor', 'door')\
    .str.replace('cloths rack', 'cloth rack')\
    .str.replace('coke bottle', 'coke bottles')\
    .str.replace('conatiner', 'container')\
    .str.replace('container_', 'container')\
    .str.replace('copboard', 'cupboard')\
    .str.replace('corton', 'carton')\
    .str.replace('counter  table','counter table')\
    .str.replace('crater', 'crate')\
    .str.replace('cup board', 'cupboard')\
    .str.replace('borad', 'board')\
    .str.replace('daing', 'dining')\
    .str.replace('taple', 'table')\
    .str.replace('tapel', 'table')\
    .str.replace('dolly', 'doll')\
    .str.replace('draw', 'drawer')\
    .str.replace('dtrawer', 'drawer')\
    .str.replace('dusbin', 'dustbin')\
    .str.replace('dust pin', 'dustbin')\
    .str.replace('eclectical', 'electrical')\
    .str.replace('envelop', 'envelope')\
    .str.replace('fire aid', 'first aid')\
    .str.replace('alaram', 'alarm')\
    .str.replace('flor', 'flour')\
    .str.replace('fole', 'food')\
    .str.replace('fruits stand', 'fruit stand')\
    .str.replace('fry pan', 'frying pan')\
    .str.replace('haanger', 'hanger')\
    .str.replace('handi craft', 'handicraft')\
    .str.replace('hel slipper', 'heel slipper')\
    .str.replace('hpoto', 'photo')\
    .str.replace('inkjetâprinter', 'inkjet printer')\
    .str.replace('invator', 'inverter')\
    .str.replace('jalousie', 'blouse')\
    .str.replace('jersy', 'jersey')\
    .str.replace('lable', 'ladle')\
    .str.replace('ladel','ladle')\
    .str.replace('lamo','lamp')\
    .str.replace('lectern','lecturn')\
    .str.replace('library book shelf', 'library bookshelf')\
    .str.replace('library books shelf', 'library bookshelf')\
    .str.replace('lihgt','light')\
    .str.replace('loock', 'lock')\
    .str.replace('lush', 'plush')\
    .str.replace('machione', 'machine')\
    .str.replace('magic eight ball', '8-ball')\
    .str.replace('metalic', 'metallic')\
    .str.replace('music  records', 'music records')\
    .str.replace('nachine', 'machine')\
    .str.replace('news paper','newspaper')\
    .str.replace('note book', 'notebook')\
    .str.replace('oilgan', 'oil can')\
    .str.replace('oil cane','oil can')\
    .str.replace('packte', 'packet')\
    .str.replace('pakcet', 'packet')\
    .str.replace('palnt', 'plant')\
    .str.replace('palstic', 'plastic')\
    .str.replace('paoers', 'papers')\
    .str.replace('role', 'roll')\
    .str.replace('papr', 'paper')\
    .str.replace('pilllow', 'pillow')\
    .str.replace('pink pong','ping pong')\
    .str.replace('plastic  spoon', 'plastic spoon')\
    .str.replace('plastic cane','plastic can')\
    .str.replace('pluk', 'plug')\
    .str.replace('polytene', 'polythene')\
    .str.replace('ppaer', 'paper')\
    .str.replace('punc hmachine', 'punch machine')\
    .str.replace('cort', 'coat')\
    .str.replace('reck', 'rack')\
    .str.replace('refrigerator', 'refridgerator')\
    .str.replace('refrigerator,cubbord,oven', 'large kitchen appliances')\
    .str.replace('remore', 'remote')\
    .str.replace('rollar', 'roller')\
    .str.replace('rool', 'room')\
    .str.replace('rugf', 'rug')\
    .str.replace('contaioner', 'container')\
    .str.replace('saptula', 'spatula')\
    .str.replace('scruber', 'scrubber')\
    .str.replace('self', 'shelf')\
    .str.replace('shalf', 'shelf')\
    .str.replace('senery', 'scenery')\
    .str.replace('sheldf','shelf')\
    .str.replace('shop', 'shoe')\
    .str.replace('small wessels', 'small vessels')\
    .str.replace('soapoil', 'soap oil')\
    .str.replace('boxe', 'box')\
    .str.replace('spike rack', 'spice rack')\
    .str.replace('stasinary','stationary')\
    .str.replace('stationery', 'stationary')\
    .str.replace('stickets', 'sticker')\
    .str.replace('suit case', 'suitcase')\
    .str.replace('suitecase', 'suitcase')\
    .str.replace('sweat shirts', 'sweatshirts')\
    .str.replace('swichboard', 'switchboard')\
    .str.replace('switch board','switchboard')\
    .str.replace('switch bopard','switchboard')\
    .str.replace('swtch', 'switch')\
    .str.replace('t shirt', 't-shirt')\
    .str.replace('t shit', 't-shirt')\
    .str.replace('t-shrit','t-shirt')\
    .str.replace('taddy bear', 'teddy bear')\
    .str.replace('tages', 'tags')\
    .str.replace('refrigerator,cubbord,oven', 'television')\
    .str.replace('terace', 'terrace')\
    .str.replace('thooth brush', 'toothbrush')\
    .str.replace('role', 'roll')\
    .str.replace('tobasco', 'tabasco')\
    .str.replace('tooth brush', 'toothbrush')\
    .str.replace('tooth paste' , 'toothpaste')\
    .str.replace('tovel', 'towel')\
    .str.replace('towell', 'towel')\
    .str.replace('trolly', 'trolley')\
    .str.replace('tsble', 'table')\
    .str.replace('elight', 'light')\
    .str.replace('tshirt', 't-shirt')\
    .str.replace('lightr', 'light')\
    .str.replace('tubwe', 'tube')\
    .str.replace('tyre', 'tire')\
    .str.replace('umberella', 'umbrella')\
    .str.replace('umbrelloa', 'umbrella')\
    .str.replace('vasoline', 'vaseline')\
    .str.replace('vessal', 'vessel')\
    .str.replace('wadrope', 'wardrobe')\
    .str.replace('wakll', 'wall')\
    .str.replace('  hanger', ' hanger')\
    .str.replace('ahnegr', 'hanger')\
    .str.replace('ahnger', 'hanger')\
    .str.replace('aper', 'paper')\
    .str.replace('apper', 'paper')\
    .str.replace('hnager', 'hanger')\
    .str.replace('hunger', 'hanger')\
    .str.replace('paiting', 'painting')\
    .str.replace('ppaer', 'paper')\
    .str.replace('ward robe', 'wardrobe')\
    .str.replace('ward rope', 'wardrobe')\
    .str.replace('wast', 'waste')\
    .str.replace('water cane', 'water can')\
    .str.replace('bottle of water', 'water bottle')\
    .str.replace('puryfier', 'purifier')\
    .str.replace('way', 'wall')\
    .str.replace('well', 'wall')\
    .str.replace('whieboard', 'whiteboard')\
    .str.replace('white board', 'whiteboard')\
    .str.replace('shelv', 'shelf')\
    .str.replace('winsow', 'window')\
    .str.replace('wodden', 'wooden')\
    .str.replace('xhair', 'chair')\
    .str.replace('yable', 'table')
   np.save('names', names_df)

