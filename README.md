# Encryption-using-Homomorphic-Encryption

This Encryption module is mostly used in drone to cloud data communication 

Autonomous drones are increasingly being used for surveillance, logistics, and military purposes, making secure drone-to-cloud communication imperative. Drones relay sensitive 
data, including GPS coordinates, camera feed, and telemetry, to the cloud for real-time processing. Whereas conventional encryption protects data in transit, the data would need to be
decrypted for processing, exposing the system to eavesdropping and unauthorized control. This is where we propose a privacy-preserving communication system based on CKKS Homomorphic Encryption,
allowing computations (addition, multiplication, polynomial evaluation) to be performed directly on encrypted real-number data. This allows drones to offload encrypted sensor data securely to the 
cloud, where AI models can do the processing without decrypting the data, thus protecting it from data leakage or intercept. The encrypted control commands are then generated in the cloud, after which 
they are transmitted back to the drone, which decrypts them using private keys, thus ensuring that only trustworthy and authenticated instructions are carried along with the drone. We implemented and 
tested the CKKS platform, assessing performance, security, and computation overhead. The results affirm CKKS real-time encrypted computation capability with near-zero latency, qualifying it as a resilient 
and scalable solution. This system avoids the pitfalls of classical encryption by ensuring end-to-end data confidentiality, enabling efficient drone operation by means of secure cloud AI processing.

