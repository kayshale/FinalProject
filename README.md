# Patient Co-Pay and Insurance Coverage Application
Kayshale Ortiz | 
IS437 | 
Final Project Proposal
# Narrative
At the Norton Healthcare Clinic, there is a team of 10 Providers that serve patients traveling from in and out of state. Norton accepts a wide variety of Insurance Providers, from local Medicaid beneficiaries to Blue Cross Blue Shield. The purpose of this application is to simplify the process of recording payments from patients (Co-Pays) and to record payment received from Insurance Providers to the Norton Healthcare Clinic. As an administrator of this clinic, it is important to accurately and efficiently record payments received to the clinic to avoid confusing the patient by sending a past due notification for a payment they already made. Similarly, it is important to properly submit claims to Insurance Providers with accurate information about the patient visit to ensure the practice is compensated properly.
Originally, these records were being kept in paper files and in a silo system where there were double records, missing receipts, and outdated Patient and Provider information. As a result, claims were being submitted with Providers that no longer worked at Norton and being denied by Insurance Providers along with many other issues. 

# Use Case
With my simple application, administrators will be able to:
* Receptionists
	* Create/view/update Patient profiles
	* Record payments made towards an invoice
		* This record will then need to be confirmed and applied to the invoice by the Billing Admin
* HR Admin
	* Create/view/update Provider files
* Billing Admin
	* Create/view/update claims
	* Create/view/update invoices sent to patients
	* View/Update Payments recorded by Receptionist

![Use Case Diagram](link-to-image)

# Assumptions
* A patient/provider/claim/invoice needs to be created by its respective administrator before anything can be done
* Each Admin has unique login credential
* When the receptionist records payments, it is not automatically applied to the account/invoice
 	* The Billing Admin needs to verify the payment and then credit the invoice
* When the Billing Admin submits a claim, an external source (Insurance Provider) determines the status of the claim 
* Patient ID’s are their Insurance Member ID’s 
* PCP (Primary Care Physician)ID’s are also license numbers, all Providers at this clinic are licensed in the state the clinic is located
* Provider Specialty is not required to submit claims
* Terminated Providers are removed from the database to avoid accidentally populating claims incorrectly
* When Invoices are paid in full, the Billing Admin changes status from “Open” to “Close”
* There may be several InsuranceID’s for the same Provider but never for the same Provider and Policy Type 
	* Ex. 
		* 00000001 | Blue Cross Blue Shield | Basic 
		* 00000011 | Blue Cross Blue Shield | Family Plan
* Each Insurance has a designated Service Rep for issues regarding claims and patient coverage
* Patients may only have one (1) PCP at a time 
* For each Co-Payment Recorded, there is an AdminID indicating who initiated the action
* For each claim submitted, there is an AdminID indicating who initiated the action
* For each invoice created, there is an AdminID indicating who initiated the action
* Providers may see several patients 
* Patients may have several invoices
* Invoices must only have one patient, Descriptions help the patient understand which visit the co-pay is for (in case of several lines)
* Unpaid Invoices will be added to the most recent invoice sent to the patient
	* Invoices will also show credits (previous payments)
* All admins need a username and password in the database to verify themselves
