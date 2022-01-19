# Inno Doctor 
A web application for creating and maintaining Patient Records and Prescriptions for each of the registered patients.
The intended users of this app will be Doctors/ Health care providers.

## Project Setup

Clone the project

```bash
    git clone https://github.com/sha-since1999/inno-doctor.git
```

Create a virtual environment. ( if using linux then use)

```bash
    python3 -m venv venv
```
Activate virtual environment
```bash
    source venv/bin/activate
```
Install dependencies

```bash
    pip install -r requirements.txt
```
Change directory to project root

```bash
	cd inno-Doctor/
```
Setup Database

```bash
    python manage.py makemigrations
    python manage.py migrate
```
Run the Server [Development Mode]
```bash
    export IS_PRODUCTION=False
    python manage.py runserver
```
Run the Server [Production Mode]
```bash
	export IS_PRODUCTION=True
	export EMAIL_HOST=<smtp server address>  
	export EMAIL_HOST_USER=<mail username>
	export EMAIL_HOST_PASSWORD=<mail password>
	python manage.py runserver
```

## Project Description

### Doctors' end :
- Easy **Login** and **Registration** for users (i.e. Doctors) with **email authentication**, **Forget Password**.
![Screenshot from 2022-01-16 21-33-47](https://user-images.githubusercontent.com/60402729/149667743-bcf5d795-ce65-4591-a00d-67d67b28cd74.png)
- Every account need to be **activated** first using a **unique link** that is sent to the registered email.
![Screenshot from 2022-01-16 21-55-16](https://user-images.githubusercontent.com/60402729/149668585-0ae509c5-6fff-41f8-ba47-9a8ecd496331.png)

- **Profile section** where the user (i.e. Doctor) can update his email, password or name.
![Screenshot from 2022-01-16 21-44-24](https://user-images.githubusercontent.com/60402729/149668178-34ee0e9f-cedd-42b1-a309-b2f343805dc4.png)

-  Once logged in, the doctor can **check the patient** details by searching his **aadhar no** in the database.
![Screenshot from 2022-01-16 21-44-30](https://user-images.githubusercontent.com/60402729/149668165-b0cd5175-185f-4d8a-bd91-a3797e418488.png)
- In case, there is **no record found**, then the doctor can **add the patient** records to the database.
![Screenshot from 2022-01-16 21-59-05](https://user-images.githubusercontent.com/60402729/149668718-f6533590-e962-43c7-a35f-8fe503e9d634.png)

![Screenshot from 2022-01-16 21-44-37](https://user-images.githubusercontent.com/60402729/149668159-c87f92ea-aa00-4720-a2dc-46c84bdc598a.png)
- The patient records page contains the data about his/her medical history, it includes **Medication Statements, Problem Lists, Vital Signs, Social History,** and **Past History of Illnesses**.
![Screenshot from 2022-01-16 21-45-01](https://user-images.githubusercontent.com/60402729/149668152-0c0f804c-cbef-4410-9367-cbd54aa46711.png)
![Screenshot from 2022-01-16 21-45-06](https://user-images.githubusercontent.com/60402729/149668138-e4a85943-c060-4f6a-87c7-3a6a5c56de42.png)

- For a **single** patient, there can be **multiple** Medication Statements, similarly within a **single** medication statement, there can be **multiple** medication items.
![Screenshot from 2022-01-16 22-02-28](https://user-images.githubusercontent.com/60402729/149668844-b0f407bf-0a7e-433a-9749-607755b70c20.png)
- A patient can also have **multiple** problems in Problem List.
![Screenshot from 2022-01-16 22-06-52](https://user-images.githubusercontent.com/60402729/149669011-76294920-1eb5-4237-8d81-271e580eae8b.png)
- Social history and Vital Sign have a **single** entry for a **single** patient.
![Screenshot from 2022-01-16 22-11-22](https://user-images.githubusercontent.com/60402729/149669152-e2246d7d-d33e-4b83-87bd-a3d08ff81af7.png)
![Screenshot from 2022-01-16 22-11-12](https://user-images.githubusercontent.com/60402729/149669157-8876d381-9c49-44e8-bf3d-64101b5aa2fe.png)
- The doctor can perform **create, read** and **update** operations over all these above mentioned patient records.
- **i18n** and **l10n** 
![Screenshot from 2022-01-16 21-32-40](https://user-images.githubusercontent.com/60402729/149667745-55052063-f58c-4db1-b3fe-a49b5ffec807.png)

### Patients' end:
- A patient can visit the app and can view his eprescription without logging in.
![Screenshot from 2022-01-16 21-33-47](https://user-images.githubusercontent.com/60402729/149667743-bcf5d795-ce65-4591-a00d-67d67b28cd74.png)
- However, to keep it a bit secure, there is an additional layer where patient enters his aadhar id and date of birth.
![Screenshot from 2022-01-16 21-34-05](https://user-images.githubusercontent.com/60402729/149667742-2e2973ee-0bb9-468b-8e08-8ffca9f7f1c8.png)
- The E-Prescription is fetched using the **most recent entry** in the medication statement for the patient.
![Screenshot from 2022-01-16 21-34-09](https://user-images.githubusercontent.com/60402729/149667740-44be29df-704e-40e7-9fe4-817960067fe3.png)


## Database Schema
![Hackfest Final](https://user-images.githubusercontent.com/60402729/149654736-bd75931d-7c06-42a5-a426-d8a01a78e53c.png)
