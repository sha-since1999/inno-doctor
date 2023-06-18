# Inno Doctor
A web application aims to streamline and enhance the management of patient records for doctors. The project leverages the Django framework and incorporates containerization using Docker for efficient deployment. Hosted on AWS ECS (Elastic Container Service), the application offers seamless integration with GitHub CI (Continuous Integration) pipeline for automated builds and deployments.

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

- Easy **Login** and **Registration** for users (i.e. Doctors) with **email
  authentication**, **Forget Password**.
  ![Screenshot from 2022-01-23 22-08-58](https://user-images.githubusercontent.com/59283795/150688537-e0b4832d-82e2-4de2-abfd-f7c04d851a1a.png)
- Every account need to be **activated** first using a **unique link** that is
  sent to the registered email.

- **Profile section** where the user (i.e. Doctor) can update his email,
  password or name.
  ![Screenshot from 2022-01-23 22-47-46](https://user-images.githubusercontent.com/59283795/150690003-86c8f2f9-fbbe-401f-8b76-c1a8c8e930d2.png)

- Once logged in, the doctor can **check the patient** details by searching
  his **aadhar no** in the database.
  ![Screenshot from 2022-01-23 22-17-32](https://user-images.githubusercontent.com/59283795/150689719-542abf76-c1c0-45b1-8d53-66f76293c614.png)

- In case, there is **no record found**, then the doctor can **add the patient**
  records to the database.
  ![Screenshot from 2022-01-23 22-19-27](https://user-images.githubusercontent.com/59283795/150689736-5dff1f85-3c71-4356-b963-2a6c60f4a5f5.png)

- The patient records page contains the data about his/her medical history, it
  includes **Medication Statements, Problem Lists, Vital Signs, Social
  History,** and **Past History of Illnesses**.
  ![Screenshot from 2022-01-23 22-18-28](https://user-images.githubusercontent.com/59283795/150689069-61790ecb-6930-462f-b4c4-9d2059cd1f87.png)

- For a **single** patient, there can be **multiple** Medication Statements,
  similarly within a **single** medication statement, there can be **multiple**
  medication items.
  ![Screenshot from 2022-01-23 22-37-59](https://user-images.githubusercontent.com/59283795/150689814-06833af7-83d6-4f20-a94c-c3b6bd3eea1a.png)
- A patient can also have **multiple** problems in Problem List.

![Screenshot from 2022-01-23 22-45-38](https://user-images.githubusercontent.com/59283795/150690046-7fe868ac-536a-43bb-b550-941c8c4ed649.png)

- Social history and Vital Sign have a **single** entry for a **single**
  patient.
  ![Screenshot from 2022-01-23 22-38-18](https://user-images.githubusercontent.com/59283795/150689821-69f72973-19a2-49c3-aea8-a39040303caa.png)
  ![Screenshot from 2022-01-23 22-38-28](https://user-images.githubusercontent.com/59283795/150689823-fd23e6c8-43cd-4d8c-bc4b-b95a6b5606a5.png)
- The doctor can perform **create, read** and **update** operations over all
  these above mentioned patient records.
- **i18n** and **l10n**
  ![Screenshot from 2022-01-23 22-47-00](https://user-images.githubusercontent.com/59283795/150689974-be3ff7a3-77e6-4951-b847-aa6bf5f80ce9.png)

### Patients' end:

- A patient can visit the app and can view his eprescription without logging in.
  ![Screenshot from 2022-01-23 22-08-58](https://user-images.githubusercontent.com/59283795/150688537-e0b4832d-82e2-4de2-abfd-f7c04d851a1a.png)
- However, to keep it a bit secure, there is an additional layer where patient
  enters his aadhar id and date of birth.

![Screenshot from 2022-01-23 22-50-58](https://user-images.githubusercontent.com/59283795/150690140-5ca90de9-e072-40fd-af8f-ac893d02e37d.png)

- The E-Prescription is fetched using the **most recent entry** in the
  medication statement for the patient.
  ![Screenshot from 2022-01-23 22-51-07](https://user-images.githubusercontent.com/59283795/150690141-a0520538-e9f2-4c90-8d70-ebbe2c8c30d4.png)

## Database Schema

![Hackfest Final](https://user-images.githubusercontent.com/60402729/149654736-bd75931d-7c06-42a5-a426-d8a01a78e53c.png)
