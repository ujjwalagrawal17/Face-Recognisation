import pygame.camera
import time
import pygame.image
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()
for i in range (20):
    img = cam.get_image()
    pygame.image.save(img, "ujjwal_" + str(i) +".jpg")
    time.sleep(1)
pygame.camera.quit()



