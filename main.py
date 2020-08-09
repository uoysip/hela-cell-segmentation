from model import *
from data import *

#os.environ["CUDA_VISIBLE_DEVICES"] = "0"

data_gen_args = dict(rotation_range=0.2,
                    width_shift_range=0.05,
                    height_shift_range=0.05,
                    shear_range=0.05,
                    zoom_range=0.05,
                    horizontal_flip=True,
                    fill_mode='nearest')

data_gen = trainGenerator(2,'data/train','images','labels',data_gen_args,save_to_dir = None)

model = unet()
model_checkpoint = ModelCheckpoint('trained_model.hdf5', monitor='loss',verbose=1, save_best_only=True)

model.fit_generator(data_gen,steps_per_epoch=300,epochs=1,callbacks=[model_checkpoint])

test_gen = testGenerator("data/results")
results = model.predict_generator(test_gen,84,verbose=1)
saveResult("data/results",results)
