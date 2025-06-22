## How to run YogiCam

These instructions are for myself in case I forget how to run YogiCam.

```bash
# to run yogicam on local host:
ssh harshita@yogicam.local
cd dog_cam_app/
python yogi_cam_server.py
# yogicam will be available at http://yogicam.local:5000

# to set up ngrok, start a new terminal tab:
ssh harshita@yogicam.local
brew install ngrok # if not yet installed
ngrok config add-authtoken $YOUR_TOKEN # if not yet authorized
ngrok http 5000

# to exit ssh:
exit
```