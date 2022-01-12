# Energy reporting system
<h3> RestAPI for internal use for energy consumption tracking, monitoring and reporting </h3>

The RestAPI main purpose is to replace the daunting task of writing and transfering things between Excel tables. The person that is doing the data entry would fill out the data and it would automatically transfer it to the "Daily .... consumption" table.
It will also be feasible to generate the reports for accounting automatically using the data that is already present which will elimanate one more task.<br><p>
Also since we have all the data in one place we will be able to generate graphs for daily, monthly and yearly consumption and keep track of past records in one place. Currently every year is on separate file.
It will also allow us to access the database and make corrections when needed from a remote location.<br><p>
The other benefit will be that a lot of manual work will also be reduced because it will be possible to connect this API with already existing ones so it will be able to download the data that is now manually transfered 
between files.
<br><p> The other task is for our service providers to be able to request payments for their services.
<br><p>The system can be expanded also to other service providers to request payments and upload invoices for the projects or services they provide us.

All dependencies are listed in the requirements.txt file. 
### Install packages with pip: -r requirements.txt

```
$ pip install -r requirements.txt
```

<p></p>

### List of all endpoints:<p>

* Register for all users except service providers:
  * POST www.example.com/register.json
  
* Login for all users except service providers
  * POST www.example.com/login.json

* Register for service providers 
  * POST www.example.com/register/service_provider.json

* Login for service providers
  * POST www.example.com/login/service_provider.json

### Note: All users when they register are set to default role of unknown. 
    Until promoted they will be able only to perform get requests.

* GET /water
  * Example: www.example.com/energy/water.json

Response body:
```
    {
        "sorting": 10,
        "glazing": 30,
        "total_m3": 680,
        "pk": 14,
        "administration": 5,
        "created_on": "2021-12-30T17:48:50.588684",
        "high_pressure_casting": 30,
        "casting": 90
    }

```

* POST /water - requires login and role == data_entry or data_analyst
  * Example:  www.example.com/energy/water.json

Response body:
```
{
    "total_m3": 680,
    "sorting": 10,
    "glazing": 30,
    "created_on": "2022-01-12T23:03:27.620780",
    "pk": 31,
    "high_pressure_casting": 30,
    "casting": 90,
    "administration": 5
}

```

* PUT /water - requires login and role == data_entry or data_analyst
  * Example:  www.example.com/energy/water/[int].json

Response body:
```
{
    "total_m3": 190,
    "sorting": 10,
    "glazing": 30,
    "created_on": "2021-12-23T16:55:45.914940",
    "pk": 9,
    "high_pressure_casting": 30,
    "casting": 30,
    "administration": 5
}
```
* DELETE /water - requires login and role == data_entry or data_analyst
  * Example:  www.example.com/energy/water/[int].json

Response body:
```

```
#################
GAS
#################
* GET /gas
  * Example: www.example.com/energy/gas.json

Response body:
```
{
    "kilns": 100,
    "sorting": 10,
    "pk": 15,
    "shuttle_kilns": 50,
    "high_pressure_casting": 30,
    "total_Nm3": 230,
    "casting": 90,
    "administration": 5,
    "created_on": "2022-01-12T23:09:39.761270",
    "glazing": 30
}

```

* POST /gas
  * Example: www.example.com/energy/gas.json

Response body:

```
{
    "kilns": 100,
    "sorting": 10,
    "pk": 15,
    "shuttle_kilns": 50,
    "high_pressure_casting": 30,
    "total_Nm3": 230,
    "casting": 90,
    "administration": 5,
    "created_on": "2022-01-12T23:09:39.761270",
    "glazing": 30
}

```

* PUT /gas - requires login and role == data_entry or data_analyst
  * Example:  www.example.com/energy/gas/[int].json
  
Response body:
```
{
    "kilns": 100,
    "sorting": 10,
    "pk": 15,
    "shuttle_kilns": 50,
    "high_pressure_casting": 30,
    "total_Nm3": 230,
    "casting": 90,
    "administration": 5,
    "created_on": "2022-01-12T23:09:39.761270",
    "glazing": 30
}
```
* DELETE /gas - requires login and role == data_entry or data_analyst
  * Example:  www.example.com/energy/gas/[int].json

Response body:
```

```

#################
ELECTRICITY
#################

* GET /electricity
  * Example: www.example.com/energy/electricity.json

Response body:
```
{
    "kilns": 100,
    "sorting": 10,
    "pk": 15,
    "shuttle_kilns": 50,
    "high_pressure_casting": 30,
    "total_electricity": 230,
    "casting": 90,
    "administration": 5,
    "created_on": "2022-01-12T23:09:39.761270",
    "glazing": 30
}

```

* POST /electricity
  * Example: www.example.com/energy/electricity.json

Response body:

```
{
    "kilns": 100,
    "sorting": 10,
    "pk": 15,
    "shuttle_kilns": 50,
    "high_pressure_casting": 30,
    "total_kwh": 230,
    "casting": 90,
    "administration": 5,
    "created_on": "2022-01-12T23:09:39.761270",
    "glazing": 30
}

```

* PUT /electricity - requires login and role == data_entry or data_analyst
  * Example:  www.example.com/energy/electricity/[int].json
  
Response body:
```
{
    "kilns": 100,
    "sorting": 10,
    "pk": 15,
    "shuttle_kilns": 50,
    "high_pressure_casting": 30,
    "total_kwh": 230,
    "casting": 90,
    "administration": 5,
    "created_on": "2022-01-12T23:09:39.761270",
    "glazing": 30
}
```
* DELETE /electricity - requires login and role == data_entry or data_analyst
  * Example:  www.example.com/energy/electricity/[int].json

Response body:
```

```
#################
COMPRESSORS
#################
* GET /compressors
  * Example: www.example.com/energy/compressors.json

Response body:
```
{
    "compressor_four": 30,
    "pk": 7,
    "compressor_five": 20,
    "compressor_one": 20,
    "compressor_two": 30,
    "created_on": "2022-01-12T23:14:17.139118",
    "compressor_three": 100,
    "total_kwh": 200
}
```

* POST /compressors
  * Example: www.example.com/energy/compressors.json

Response body:

```
{
    "compressor_four": 30,
    "pk": 7,
    "compressor_five": 20,
    "compressor_one": 20,
    "compressor_two": 30,
    "created_on": "2022-01-12T23:14:17.139118",
    "compressor_three": 100,
    "total_kwh": 200
}

```

* PUT /compressors
  * Example: www.example.com/energy/compressors[id].json

Response body:

```
{
    "compressor_four": 30,
    "pk": 7,
    "compressor_five": 20,
    "compressor_one": 20,
    "compressor_two": 30,
    "created_on": "2022-01-12T23:14:17.139118",
    "compressor_three": 100,
    "total_kwh": 200
}

```


* DELETE /compressors
  * Example: www.example.com/energy/compressors[id].json

Response body:
```

```
#################
PAYMENT REQUESTS
#################

* GET payment requests - Requires role == bulgar_gaz or energo_pro
  * Example:  www.example.com/payments.json
  
Response body:

```
    {
        "user_id": 3,
        "pk": 38,
        "updated_by": null,
        "type": "electricity",
        "amount": 999,
        "metric": "kwh",
        "updated_on": null,
        "created_on": "2022-01-11T20:42:03.780521",
        "total_invoice_amount": 9999,
        "state": "State.pending"
    }
```

* POST payment requests - Requires role == bulgar_gaz or energo_pro
  * Example:  www.example.com/payments.json
  
Response body:

```
    {
        "user_id": 3,
        "pk": 38,
        "updated_by": null,
        "type": "electricity",
        "amount": 999,
        "metric": "kwh",
        "updated_on": null,
        "created_on": "2022-01-11T20:42:03.780521",
        "total_invoice_amount": 9999,
        "state": "State.pending"
    }
```

* PUT payment requests - Requires role == bulgar_gaz or energo_pro
  * Example:  www.example.com/payments[int].json
  
Response body:

```
    {
        "user_id": 3,
        "pk": 38,
        "updated_by": null,
        "type": "electricity",
        "amount": 999,
        "metric": "kwh",
        "updated_on": null,
        "created_on": "2022-01-11T20:42:03.780521",
        "total_invoice_amount": 9999,
        "state": "State.pending"
    }
```

* DELETE payment requests - Requires role == bulgar_gaz or energo_pro
  * Example:  payments[int].json
    
```

```
* PUT approve payment requests - Requires role == accountant
  * Example: www.example.com/accountants/payments/[id]/approved

Response body:

```
{
    "created_on": "2022-01-11T20:42:03.780521",
    "user_id": 3,
    "updated_by": null,
    "metric": "kwh",
    "pk": 38,
    "type": "electricity",
    "total_invoice_amount": 9999,
    "amount": 999,
    "updated_on": null,
    "state": "State.approved"
}
```

* PUT reject payment requests - Requires role == accountant
  * Example: www.example.com/accountants/payments/[int]/approved

Response body:

```
{
    "created_on": "2022-01-11T20:42:03.780521",
    "user_id": 3,
    "updated_by": null,
    "metric": "kwh",
    "pk": 38,
    "type": "electricity",
    "total_invoice_amount": 9999,
    "amount": 999,
    "updated_on": null,
    "state": "State.approved"
}
```

* PUT change role - Requires role == CEO
  * Example: www.example.com/role_change/[id]
Response body:

```
{
    "message": "Role changed!"
}
```

* PUT change role of a service provider (bulgar_gaz or energo_pro) - Requires role == CEO
  * Example: www.example.com/role_change_service_provider/[id]
  
Response body:

```
{
    "message": "Role changed!"
}
```

    

    
    
    
    
