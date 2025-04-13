# azure-function-rg-creator
```
azure-function-rg-creator/
├── host.json
├── requirements.txt
└── CreateResourceGroup/
    ├── function.json
    └── _init_.py
```

Payload for POST API
```
curl --location 'http://localhost:7071/api/createrg' \
--header 'x-functions-key: '' \
--header 'Content-Type: application/json' \
--data '{
    "resourceGroupName": "deepak-eastus-rg",
    "resourceGroupRegion": "eastus"
}'
```

Reponse Result
```
{
"status": "Success",
 "resourceGroup": {"name": "deepak-eastus-rg", "location": "eastus"}
}
```
