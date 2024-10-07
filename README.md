1. User Management App
Functionality:
Handles user registration, login, and authentication.
Manages SMS-based OTP verification using services like Twilio.
Stores user details such as Aadhaar and Voter ID associations.
2. Aadhaar App
Functionality:
Stores Aadhaar card details (name, father’s name, DOB, address, Aadhaar number, gender, photo).
Links Aadhaar details to the user model.
Provides APIs or forms to upload Aadhaar data for verification.
3. Voter ID App
Functionality:
Stores Voter ID details (name, father’s name, DOB, address, voter ID number, gender, photo).
Links Voter ID details to the user model.
Provides APIs or forms to upload voter ID data for verification.
4. Verification App
Functionality:
Compares uploaded Aadhaar and Voter ID data to stored database records.
Uses AI/ML models for extracting and verifying Aadhaar and Voter ID data (OCR for text, face recognition for photo verification).
Logs verification results (success/failure).
5. Voting App
Functionality:
Manages the voting process (casting votes, viewing candidates).
Integrates with blockchain to record votes in a tamper-proof manner.
Stores vote data, including blockchain transaction hashes for integrity.
