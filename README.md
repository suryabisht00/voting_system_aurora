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









Database structure:-

# User Management Schema

## User Management (user_management.User)

| Field Name           | Type                                   |
|----------------------|----------------------------------------|
| user_id              | AutoField (PK)                        |
| aadhaar_number       | CharField (unique)                    |
| voter_id             | CharField (unique)                    |
| mobile_number        | CharField (unique)                    |
| is_verified          | BooleanField                           |
| username             | CharField (unique)                    |
| password             | CharField                              |
| first_name           | CharField                              |
| last_name            | CharField                              |
| email                | EmailField                             |
| date_joined          | DateTimeField                          |
| last_login           | DateTimeField                          |

---

## Aadhaar (aadhaar.Aadhaar)

| Field Name           | Type                                   |
|----------------------|----------------------------------------|
| aadhaar_id           | AutoField (PK)                        |
| user                 | OneToOneField (FK)                    |
| aadhaar_number       | CharField (unique)                    |
| name                 | CharField                              |
| father_name          | CharField                              |
| dob                  | DateField                              |
| address              | TextField                              |
| gender               | CharField                              |
| mobile_number        | CharField                              |
| photo                | ImageField                             |
| created_at           | DateTimeField                          |

---

## Voter ID (voter_id.VoterID)

| Field Name           | Type                                   |
|----------------------|----------------------------------------|
| voter_id             | AutoField (PK)                        |
| user                 | OneToOneField (FK)                    |
| voter_id             | CharField (unique)                    |
| name                 | CharField                              |
| father_name          | CharField                              |
| dob                  | DateField                              |
| address              | TextField                              |
| gender               | CharField                              |
| photo                | ImageField                             |
| created_at           | DateTimeField                          |

---

## Verification (verification.ExtractedData)

| Field Name                      | Type                                   |
|---------------------------------|----------------------------------------|
| extracted_id                    | AutoField (PK)                        |
| user                            | ForeignKey (FK)                       |
| extracted_name                  | CharField                              |
| extracted_father_name           | CharField                              |
| extracted_dob                   | DateField                              |
| extracted_address               | TextField                              |
| extracted_gender                | CharField                              |
| extracted_aadhaar_number        | CharField                              |
| extracted_voter_id              | CharField                              |
| extracted_photo                 | ImageField                             |
| created_at                      | DateTimeField                          |

---

## Verification (verification.Verification)

| Field Name                      | Type                                   |
|---------------------------------|----------------------------------------|
| verification_id                 | AutoField (PK)                        |
| user                            | ForeignKey (FK)                       |
| aadhaar_status                  | BooleanField                           |
| voter_id_status                 | BooleanField                           |
| photo_status                    | BooleanField                           |
| verification_timestamp           | DateTimeField                          |

---

## Candidate (voting.Candidate)

| Field Name                      | Type                                   |
|---------------------------------|----------------------------------------|
| candidate_id                    | AutoField (PK)                        |
| name                            | CharField                              |
| party                           | CharField                              |
| constituency                    | CharField                              |

---

## Vote (voting.Vote)

| Field Name                      | Type                                   |
|---------------------------------|----------------------------------------|
| vote_id                         | AutoField (PK)                        |
| user                            | ForeignKey (FK)                       |
| candidate                       | ForeignKey (FK)                       |
| blockchain_hash                 | CharField (unique)                    |
| timestamp                       | DateTimeField                          |
