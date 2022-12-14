import cv2
import numpy as np
import time
import pyzbar.pyzbar as pyzbar
from ibmcloudant.cloudant_v1 import CloudantV1
from ibmcloudant import CouchDbSessionAuthenticator
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator

authenticator = BasicAuthenticator('apikey-v2-l2fbdnxi81dzhqd35dh2stpxiddi2a7r9xzn7o4yslc','bd447d6dce6b242650b50a0598fb7bec')
service=CloudantV1(authenticator=authenticator)
service.set_service_url('https://apikey-v2-l2fbdnxi81dzhqd35dh2stpxiddi2a7r9xzn7o4yslc:bd447d6dce6b242650b50a0598fb7bec@0000ea1a-955f-48ed-aeb9-e6679f14408a-bluemix.cloudantnosqldb.appdomain.cloud')

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame=cap.read()
    decodedObjects=pyzbar.decode(frame)
    for obj in decodedObjects:
        #print("Data",obj.data)
        a=obj.data.decode('UTF-8')
        cv2.putText(frame,"Ticket",(50,50),font,2,
                    (255,0,0),3)
        #print(a)
        try:
            response=service.get_document(
                db ='booking',
                doc_id = a
              ).get_result()
            print(response)
            time.sleep(5)
        except Exception as e:
            print("Not a Valid Ticket")
            time.sleep(5)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
client.disconnect()
